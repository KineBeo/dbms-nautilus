# Defense Q&A Cheat Sheet

Based on teacher hint: "explain pipeline flow, change hyperparameters, change evaluation metrics, re-run with different dataset."

## Category 1: Pipeline Flow Questions

**Q: Walk me through what happens from start to finish when you run a fuzzing campaign.**
A: `run_eval.sh` validates the harness binary exists, writes `config.ron` with parameters (grammar path, timeout, threads, bitmap size), then starts the fuzzer binary. The fuzzer initializes Python (PyO3), loads the grammar (each `ctx.rule()` call creates a Rust Rule object via the PyContext bridge), spawns N threads. Each thread generates initial inputs by sampling the grammar, then enters a mutation loop: pick input from queue, minimize (Init phase), mutate with 5 operators (deterministic rules, random subtree regen, recursion expansion, splice, bulk havoc), unparse tree to SQL bytes, write to temp file, fork child via fork server, child runs `sqlite3_exec()` on the SQL, parent reads coverage bitmap. If new edge found, add to queue; if crash (ASan exit 223, UBSan exit 1, or signal), save to `outputs/signaled/`. After the duration expires, triage runs: `classify.py` groups crashes by function name + sanitizer type into bug classes, `cve_signatures.py` checks structural patterns against known CVE signatures.

**Q: How does the grammar engine select which rule to apply?**
A: Each nonterminal has multiple alternative rules. When generating, `Context::generate_tree_from_nt()` (line 393) is called, which calls `get_random_rule_for_nt()` (line 264). It sums all applicable rule weights, draws a uniform random number in [0, total_weight), then walks rules subtracting weights until the threshold is crossed -- O(n) linear scan. Default weight is 1.0. Our grammar assigns higher weights (2.0-3.0) to rules producing attack-relevant SQL constructs (window functions, CTEs, boundary values). Note: the `loaded_dice` crate (O(1) alias method) exists in the codebase but is only used for recursion depth selection in `recursion_info.rs`, not for production rule sampling.

**Q: How does the fork server work?**
A: The harness binary is compiled with AFL instrumentation (`afl-clang-fast`). `__AFL_INIT()` at line 74 in `sqlite_harness.c` tells the binary to wait for commands from the fuzzer over a control pipe (fd 198). The fuzzer writes "go", harness `fork()`s, child processes one input via `sqlite3_exec()`, child exits, parent reads exit status + coverage bitmap via shared memory (fd 200), parent waits for next "go". This avoids re-loading the binary for each input (~10-100x faster than `exec()` per input). The `ForkServer::run()` method is at `forksrv/src/lib.rs:192`.

**Q: How do you detect bugs?**
A: Three oracle mechanisms: (1) ASan detects memory errors (buffer overflow, use-after-free, heap-buffer-read-past) and exits with code 223 (`ASAN_OPTIONS=exitcode=223`). (2) UBSan detects undefined behavior (integer overflow, null pointer dereference, misaligned access) and exits with code 1 (`halt_on_error=1`). (3) SQLite debug assertions (`SQLITE_DEBUG`) trigger SIGTRAP (signal 5), caught by the fork server as `Stopped(5)`. The fuzzer classifies exit reasons in `ExitReason` enum (`forksrv/src/exitreason.rs:7`): `Normal(i32)`, `Timeouted`, `Signaled(i32)`, `Stopped(i32)`.

**Q: How do mutations preserve syntactic validity?**
A: All mutations operate on the parse tree (AST), not on raw bytes. `mut_random()` picks a random node, regenerates its subtree using the grammar -- result is always a valid expansion of that nonterminal. `mut_splice()` replaces a node with a same-nonterminal-type subtree from ChunkStore -- type-compatible by construction. `mut_rules()` tries every alternative production rule for a node -- each alternative is grammar-valid. Only after mutation does `unparse()` (tree.rs:167) convert the tree back to SQL bytes by walking leaf nodes left to right.

## Category 2: Hyperparameter Questions

**Q: What are the main hyperparameters?**
A: In config.ron: `timeout_in_millis` (per-execution timeout, default 500ms), `number_of_threads` (parallelism, default 1), `max_tree_size` (AST node limit, default 300), `bitmap_size` (coverage map size, 2MB in production campaigns, 64KB in smoke tests), `number_of_generate_inputs` (initial corpus size, default 1000), `number_of_deterministic_mutations` (mut_rules passes, default 1). In grammar: `weight` parameter on each rule (default 1.0). All hyperparameters are overridable via environment variables in `run_eval.sh`.

**Q: Show me how to change the timeout and re-run.**
A: `TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` -- this overrides the default via environment variable. The script writes it into config.ron. Verify: `grep timeout workdirs/sqlite-3.31.1_demo/config.ron` shows `timeout_in_millis: 1000`.

**Q: What happens if you increase max_tree_size?**
A: Larger trees = more complex SQL = deeper state exploration. But: more complex SQL takes longer to execute, so more inputs hit the timeout and get killed, wasting execution budget. The default 300 nodes balances complexity vs throughput. Thesis experiments used `max_tree_size: 300` with `timeout_in_millis: 500`.

**Q: What happens if you change the number of threads?**
A: More threads = more executions/second (linear scaling up to CPU count). Threads share the global coverage bitmap (`GlobalSharedState`, shared_state.rs:7) but each has its own `FuzzingState` (context, mutator, fork server instance). Thesis used single-thread to eliminate concurrency variance and ensure reproducibility.

## Category 3: Evaluation Metric Questions

**Q: What metrics did you use to compare grammars?**
A: Six metrics across three research questions (thesis Section 4.2): (1) CVE rediscovery rate (RQ1) -- proportion of 4 target CVEs found, matched via structural signature library with 80% fidelity threshold on top-5 stack frames. (2) Unique bug classes (RQ2) -- distinct combinations of crashing function + sanitizer diagnostic type. (3) Unique root causes (RQ3) -- distinct stack hashes per campaign (top 5 GDB frames, filtered to SQLite-internal). (4) Edge coverage (RQ3) -- unique control-flow edges in the AFL bitmap. (5) Throughput (RQ3) -- executions per second. (6) Time-to-first-crash/TTFC (RQ3) -- wall-clock seconds to first non-zero exit.

**Q: How did you measure statistical significance?**
A: Mann-Whitney U test (non-parametric, doesn't assume normal distribution) with N=5 runs per configuration (N=4 for one EBNF cell on version 3.32.0 due to missing workdir). Effect size via Cliff's d. We chose Mann-Whitney because: (a) small sample size (N=5), (b) crash counts are not normally distributed, (c) it's the standard in fuzzing literature per Klees et al. USENIX Security 2018 recommendations. Results: large effect sizes (d=1.00, p<0.05) for unique root causes on all four versions.

**Q: Could you use a different metric?**
A: Yes. Alternative metrics: (a) unique code branches (vs edges) -- coarser but simpler. (b) Vargha-Delaney A12 effect size -- standard alternative to Cliff's d. (c) Time-to-N-crashes -- more informative than TTFC for sustained bug finding. (d) Bug severity weighting -- weight HIGH bugs more than LOW. The choice depends on what aspect of fuzzer effectiveness you want to measure.

## Category 4: Code Understanding Questions

**Q: Show me where the bitmap comparison happens.**
A: `fuzzer/src/fuzzer.rs`, function `new_bits()` at line 453. It compares the thread-local bitmap against the global shared bitmap byte-by-byte. If any byte in the local has bits not present in the global, new edge discovered, return true.

**Q: How does PyO3 bridge work?**
A: `fuzzer/src/python_grammar_loader.rs`. The `PyContext` struct (line 10) is a `#[pyclass]` wrapping a Rust `Context`. It exposes `rule()` (line 28) as a `#[pymethods]` method. The loader: (1) creates a Python module with `PyContext`, (2) injects it into the runtime, (3) `exec()` the grammar .py file, (4) each `ctx.rule()` call triggers `PyContext::rule()` which calls Rust `Context::add_rule()`. Grammar defined in Python for rapid iteration, compiled into Rust data structures for performance.

**Q: What is ChunkStore?**
A: `grammartec/src/chunkstore.rs`. A pool of subtrees from "interesting" inputs (those that found new coverage). When an input is added to the queue, `add_tree()` (line 51) extracts subtrees with <=30 nodes and stores them keyed by nonterminal type, deduplicating by serialized output. During `mut_splice()`, a random subtree of matching nonterminal type is picked from ChunkStore and grafted into the current tree. This enables cross-input recombination -- combining structural patterns discovered in separate executions.

**Q: How does the triage pipeline classify crashes?**
A: Three stages: (1) `stack_dedup.py:hash_frames()` (line 56) -- run GDB with `bt 5` to get top 5 stack frames, filter out system library and sanitizer runtime frames, keep SQLite-internal frames, SHA256 hash as unique crash identifier. (2) `classify.py:classify_crash()` -- parse ASan/UBSan stderr to determine crash type (null_deref, integer_overflow, misaligned_access, signal, float_cast_overflow), group by crashing function name into bug class (BC001-BC013). (3) `cve_signatures.py` -- regex-match the trigger SQL against `_CVES` list (line 15) of known CVE structural patterns for CVE attribution.

**Q: What is the three-state queue pipeline?**
A: Adapted from Nautilus: Init -> Det -> Random. Init: minimize the tree (shrink while preserving coverage), extract subtrees to ChunkStore. Det: apply deterministic `mut_rules()` (try every alternative at each node) plus random mutations. Random: apply random mutations only (havoc, recursion expansion, splice). Original Nautilus has a fourth `detafl` stage for AFL-style byte-level mutations; DBMS-Nautilus omits this because byte-level mutations on SQL produce parser-rejected inputs.

## Category 5: Research Contribution Questions

**Q: What is your main contribution?**
A: A domain-specific grammar engineering methodology for vulnerability discovery. The grammar encodes structural patterns extracted from CVE root-cause analysis as weighted production rules. The key insight is that these patterns generalize: rules designed for one CVE also trigger unrelated bugs (cross-pollination). We demonstrate this on SQLite, rediscovering 4/4 target CVEs and finding 13 bug classes (9 unique to our grammar) with 108x more unique root causes than the EBNF baseline.

**Q: What is cross-pollination?**
A: Our key finding from RQ2: grammar patterns designed to trigger one specific CVE also trigger unrelated bugs. For example, window function + CTE patterns (included because CVE-2020-13871 involves use-after-free in window processing) also trigger null pointer dereferences in unrelated code paths (BC006 in sqlite3ExprCodeTarget, BC007 in sqlite3AtoF). This means a well-designed grammar provides broader coverage than its explicit targets.

**Q: What are the limitations?**
A: Three main limitations (thesis Section 4.6): (1) Grammar design requires manual domain expertise -- tracing from CVE root cause to SQL structural patterns cannot be fully automated. (2) Weight sensitivity -- incorrect weights can concentrate sampling on a shallow bug region (e.g., early grammar versions had 92% FTS crashes due to overweighted FTS rules). (3) Hard reachability ceiling -- the grammar defines the boundary of what the fuzzer can discover; if a vulnerability requires a SQL construct not encoded as a nonterminal, no amount of fuzzing will find it.

**Q: Why not use reinforcement learning?**
A: The codebase contains experimental Thompson Sampling code (`grammar_bandit.rs`, 492 lines) but it is NOT evaluated in the thesis. All experiments use fixed grammar weights. The thesis conclusion lists RL integration as future work. The rationale: the current grammar already achieves 108x more root causes with fixed weights; the research question was whether grammar design matters, not whether adaptive weighting helps. RL would be the next research question.
