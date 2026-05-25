# Live Coding Tutorial — Defense Preparation

## Part A: Execution Flow Walkthrough

The teacher will ask: "Explain the pipeline execution flow."

### Pipeline Overview (memorize this)

```
User runs: ./scripts/run_eval.sh sqlite-3.31.1 run1
                    |
                    v
        +---- run_eval.sh ----+
        | 1. Validate harness |
        | 2. Write config.ron |
        | 3. Start fuzzer     |
        | 4. Run triage       |
        +---------+-----------+
                  |
                  v
        +---- fuzzer binary (Rust) ----+
        | main.rs:                     |
        |   pyo3::prepare_python()     |  <- Init Python for grammar
        |   load_config(config.ron)    |  <- Read RON config
        |   load_grammar(sqlite_v3.py) |  <- PyO3 bridge -> Rule objects
        |   spawn N threads            |  <- Each runs fuzzing_thread()
        +---------+-------------------+
                  |
                  v (per thread)
        +---- fuzzing_thread() -------------------------+
        | 1. Generate initial inputs (gen phase)        |
        | 2. Loop: pick from queue                      |
        |    a. minimize_tree (shrink) -- preprocessing |
        |    b. minimize_rec (recursion) -- preprocessing|
        |    c. mut_rules (deterministic)               |
        |    d. mut_random (random subtree regen) x N   |
        |    e. mut_random_recursion x N                |
        |    f. mut_splice (from ChunkStore) x N        |
        | 3. Each mutation -> unparse -> bytes           |
        | 4. Write to file -> fork child                 |
        | 5. Child: harness reads SQL, executes          |
        | 6. Parent: read bitmap, check new edges        |
        | 7. New coverage? -> add to queue               |
        | 8. Crash? -> save to outputs/signaled/         |
        +------------------------------------------------+
```

Note: The thesis describes **5 mutation operators** (mut_rules, mut_random, mut_random_recursion, mut_splice, bulk random havoc). Minimization (minimize_tree, minimize_rec) is a separate preprocessing step in the Init phase, not counted as a mutation operator.

### Key File -> Function Mapping

| When teacher points at... | Key function to explain | What it does |
|---------------------------|------------------------|--------------|
| `fuzzer/src/main.rs` | `main()` line 233 | CLI parsing, config load, thread spawn |
| `fuzzer/src/main.rs` | `fuzzing_thread()` line 87 | Per-thread mutation loop: gen -> minimize -> mutate -> execute |
| `fuzzer/src/main.rs` | `process_input()` line 46 | Execute one mutated input: unparse -> fork -> check coverage |
| `fuzzer/src/fuzzer.rs` | `run_on_with_dedup()` line 170 | Unparse tree -> write file -> fork child -> read bitmap -> detect new edges |
| `fuzzer/src/fuzzer.rs` | `new_bits()` line 453 | Compare bitmap against global: if new edge -> return true |
| `fuzzer/src/fuzzer.rs` | `exec()` line 365 | Low-level: write bytes to file, call fork server run() |
| `fuzzer/src/state.rs` | `FuzzingState` struct (line 20) | Bundles Context + Mutator + Fuzzer + Config + shared ChunkStore per thread |
| `fuzzer/src/config.rs` | `Config` struct (line 9) | RON-deserializable: threads, timeout, bitmap_size, grammar path, policy |
| `fuzzer/src/queue.rs` | `Queue` struct (line 56) | Three-state pipeline: Init -> Det -> Random |
| `fuzzer/src/shared_state.rs` | `GlobalSharedState` (line 7) | Thread-shared: global bitmap, execution counters |
| `grammartec/src/context.rs` | `generate_tree_from_nt()` line 393 | Weighted sampling: pick rule via linear scan, recurse children |
| `grammartec/src/context.rs` | `add_rule()` line 66 | Register a production rule in the grammar |
| `grammartec/src/context.rs` | `get_random_rule_for_nt()` line 264 | O(n) weighted linear scan: sum weights, draw threshold, walk rules |
| `grammartec/src/rule.rs` | `Rule` enum (line 84) | PlainRule, ScriptRule, RegExpRule -- each has `weight: f32` field |
| `grammartec/src/tree.rs` | `unparse()` line 167 | Walk AST recursively -> concatenate leaf bytes -> SQL string |
| `grammartec/src/mutator.rs` | `minimize_tree()` line 32 | Try replacing subtrees with shortest valid derivation, keep if same coverage |
| `grammartec/src/mutator.rs` | `mut_rules()` line 103 | Deterministic: try every alternative production at each node |
| `grammartec/src/mutator.rs` | `mut_splice()` line 136 | Replace node with same-type subtree from ChunkStore |
| `grammartec/src/mutator.rs` | `mut_random()` line 177 | Pick random node -> regenerate its subtree (havoc mutation) |
| `grammartec/src/mutator.rs` | `mut_random_recursion()` line 197 | Repeat recursive productions to increase nesting depth |
| `grammartec/src/chunkstore.rs` | `ChunkStore::add_tree()` line 51 | Extract subtrees (<=30 nodes) from interesting inputs, store by nonterminal |
| `forksrv/src/lib.rs` | `ForkServer::run()` line 192 | Write to control pipe -> fork child -> read status pipe -> collect bitmap |
| `forksrv/src/exitreason.rs` | `ExitReason` enum (line 7) | `Normal(i32)`, `Timeouted`, `Signaled(i32)`, `Stopped(i32)` |
| `harness/src/sqlite_harness.c` | `setup_db()` line 38 | Opens blank `:memory:` database (constructor, runs before main) |
| `harness/src/sqlite_harness.c` | `main()` line 68 | `__AFL_INIT()` -> read SQL file -> `sqlite3_exec()` -> exit |
| `fuzzer/src/python_grammar_loader.rs` | `PyContext` struct (line 10) | PyO3 bridge: Python `ctx.rule()` calls -> Rust `Context::add_rule()` |
| `fuzzer/src/grammar_bandit.rs` | `select_group()` line 166 | **NOT in thesis.** Experimental Thompson Sampling (future work). All experiments use uniform. |
| `triage/cve_signatures.py` | `_CVES` list (line 15) | 6 CVE structural signatures as regex pattern lists |
| `triage/cve_signatures.py` | `missing_patterns()` (line 85) | Check which patterns a candidate SQL is missing for a CVE |
| `triage/stack_dedup.py` | `hash_frames()` (line 56) | GDB `bt 5` -> filter to SQLite-internal frames -> SHA256 -> dedup key |
| `triage/classify.py` | `classify_crash()` | Parse ASan/UBSan stderr -> categorize crash type (null_deref, overflow, etc.) |

### Practice: Explain These (say it out loud)

1. **"What happens when run_eval.sh starts?"**
   -> Creates workdir, writes config.ron (binary path, grammar path, thread count, timeout, bitmap size), then starts the fuzzer binary with `-c config.ron`. After the fuzzer finishes (DURATION seconds), runs `capture_coverage.py` and `classify.py` for triage.

2. **"How does the grammar generate SQL?"**
   -> Python file defines rules via `ctx.rule("NT", "expansion")`. PyO3 loads them into Rust `Context`. `generate_tree_from_nt("START")` calls `get_random_rule_for_nt()` which picks a rule for "START" using weighted linear scan (sum weights, draw random threshold, walk rules). Children are expanded recursively until all leaves are terminals. `unparse()` concatenates leaf bytes into SQL string.

3. **"How does the fuzzer detect a crash?"**
   -> The harness is compiled with ASan+UBSan (`-fsanitize=address,undefined`). Memory errors cause ASan to exit with code 223 (`ASAN_OPTIONS=exitcode=223`). UBSan exits with code 1 (`halt_on_error=1`). SQLite debug assertions trigger SIGTRAP. The fork server reads the child's exit status via `from_wait_status()`. Non-zero + non-timeout = crash -> saved to `outputs/signaled/`.

4. **"What is coverage-guided feedback?"**
   -> Each execution updates a shared memory bitmap (AFL-style). Each edge (branch A->B) in the control flow graph maps to a bitmap index via `(caller_block ^ callee_block) % bitmap_size`. After execution, `new_bits()` (fuzzer.rs:453) compares the thread-local bitmap against the global bitmap byte-by-byte. If any new bit is set = new edge discovered -> the input is "interesting" -> verified for deterministic behavior (re-executed 5 times) -> added to queue for further mutation.

5. **"How do mutations work?"**
   -> Five mutation operators (thesis Section 3.1): (a) mut_rules -- deterministic rule substitution: try every alternative production at each node. (b) mut_random -- random subtree regeneration: pick random node, replace with fresh grammar derivation. (c) mut_random_recursion -- random recursion expansion: repeat recursive productions to increase nesting depth. (d) mut_splice -- splice: replace node with same-type subtree from ChunkStore (cross-input recombination). (e) bulk random havoc -- apply multiple random subtree replacements in succession. Minimization (minimize_tree, minimize_rec) is a separate preprocessing step applied in the Init phase, not counted as a mutation operator.

6. **"What is the difference between your grammar and EBNF baseline?"**
   -> EBNF baseline (`grammars/baseline/sqlite-ebnf.py`) is derived from SQLite's public grammar spec -- generates syntactically valid SQL but without attack patterns, uniform weights. Our grammar (`grammars/active/sqlite_v3.py`) decomposes SQL into Schema-Setup + Stress-Query + Validation-Op, adds boundary values (INT32_MAX, 1e308), window functions, CTE recursion, FTS queries -- structural patterns that exercise CVE-bearing code paths. Result: 108x more unique root causes per campaign (mean 205.6 vs 1.9) at the cost of 52.1% lower throughput.

7. **"What is the queue pipeline?"**
   -> Three-state pipeline adapted from Nautilus: Init -> Det -> Random. During Init, the input is minimized (shrink tree while preserving coverage). During Det, deterministic rule substitution tries every alternative. During Random, random mutations (havoc, recursion, splice) are applied. Original Nautilus has a fourth `detafl` stage for AFL-style byte-level mutations; we omit it because byte-level mutations produce parser-rejected SQL.

---

## Part B: Live Coding Exercises

The teacher hint says they may ask to: change hyperparameters, change evaluation metrics, re-run experiments.

### Exercise B1: Change Timeout (hyperparameter)

**Scenario:** "Change the per-execution timeout from 500ms to 1000ms and run a campaign."

**Steps:**
1. Open `scripts/run_eval.sh`
2. Find line: `TIMEOUT_MS="${TIMEOUT_MS:-500}"`
3. Override via environment:
   ```bash
   TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 timeout_demo
   ```
4. Show the config.ron: `cat workdirs/sqlite-3.31.1_timeout_demo/config.ron`
   -> Confirm `timeout_in_millis: 1000`

**What to explain:** Higher timeout means the fuzzer waits longer per execution before killing the child. Trade-off: fewer executions/second but catches bugs that need longer execution time (deep recursion, complex joins).

### Exercise B2: Change Thread Count (hyperparameter)

**Scenario:** "Run with 2 threads instead of 1."

**Steps:**
1. Override via environment:
   ```bash
   THREADS=2 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 threads_demo
   ```
2. Show config: `cat workdirs/sqlite-3.31.1_threads_demo/config.ron`
   -> `number_of_threads: 2`
3. Show it ran faster: compare exec.log line counts between 1-thread and 2-thread runs.

**What to explain:** Multiple threads share the same bitmap (GlobalSharedState, line 7 in shared_state.rs). Each thread has its own FuzzingState (Context, Mutator, Fuzzer). More threads = more executions/second but diminishing returns due to bitmap contention.

### Exercise B3: Change Max Tree Size (hyperparameter)

**Scenario:** "What happens if you increase the maximum tree depth?"

**Steps:**
1. Override:
   ```bash
   MAX_TREE_SIZE=500 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 tree_demo
   ```
2. Compare generated SQL sizes:
   ```bash
   ./target/release/generator -g grammars/active/sqlite_v3.py -t 300 | wc -c
   ./target/release/generator -g grammars/active/sqlite_v3.py -t 500 | wc -c
   ```

**What to explain:** `max_tree_size` limits the AST node count. Larger trees = more complex SQL = slower execution but potentially deeper state exploration. Too large = timeout kills most executions -> wasted budget. Thesis experiments used max_tree_size=300 with 500ms timeout.

### Exercise B4: Change Grammar Weight (hyperparameter)

**Scenario:** "Increase the weight of window function rules."

**Steps:**
1. Open `grammars/active/sqlite_v3.py`
2. Find the window function section (search for "Window-Func")
3. Change a weight, e.g. from `weight=2.0` to `weight=5.0`
4. Run generator to verify bias:
   ```bash
   for i in $(seq 1 100); do
     ./target/release/generator -g grammars/active/sqlite_v3.py -t 10 2>/dev/null
   done | grep -c "OVER"
   ```
5. Revert the change after demo: `git checkout grammars/active/sqlite_v3.py`

**What to explain:** The weighted sampler (linear scan in `get_random_rule_for_nt()`, context.rs:264) sums all rule weights for a nonterminal, draws a uniform random number in [0, total_weight), then walks rules subtracting weights until threshold is crossed. Weight 5.0 vs 1.0 means ~5x more likely to be selected. This biases generation toward structures that exercise specific code paths.

### Exercise B5: Change Evaluation Metric (metric change)

**Scenario:** "Instead of counting unique root causes, count unique crash stack hashes."

**Steps:**
1. Open `triage/stack_dedup.py`
2. Current: `hash_frames()` (line 56) uses GDB `bt 5` -> filter to SQLite-internal frames -> SHA256
3. To count unique hashes across all campaigns:
   ```python
   import json, os
   crash_dir = "results/crashes"
   hashes = set()
   for bc in os.listdir(crash_dir):
       bc_path = os.path.join(crash_dir, bc)
       if os.path.isdir(bc_path):
           for h in os.listdir(bc_path):
               if os.path.isdir(os.path.join(bc_path, h)):
                   hashes.add(h)
   print(f"Unique crash hashes: {len(hashes)}")
   ```
4. Compare: "We report 13 bug classes (grouped by crashing function + sanitizer diagnostic type) and 48 unique stack hashes after cross-campaign deduplication. The EBNF-Baseline finds only 4 of the same 13 classes."

**What to explain:** Bug class = grouping by the crashing function + sanitizer type (higher-level, 13 classes). Stack hash = grouping by top-5 GDB frames after filtering (finer-grained, 48 hashes). We chose bug classes for the thesis because they represent distinct vulnerability types; stack hashes capture different triggering paths to the same bug.

### Exercise B6: Run with Different Target Version (different dataset)

**Scenario:** "Run the same grammar against a different SQLite version."

**Steps:**
1. Pick a version that has a harness: `ls harness/afl/`
2. Run:
   ```bash
   DURATION=60 ./scripts/run_eval.sh sqlite-3.32.0 cross_demo
   ```
3. Compare crash counts:
   ```bash
   find workdirs/sqlite-3.32.0_cross_demo/outputs/signaled -type f | wc -l
   ```

**What to explain:** Same grammar, different SQLite binary. The grammar targets structural patterns, not version-specific bugs. Some bugs exist in multiple versions (BC001 null_pointer_in_sqlite3Fts5GetTokenizer appears in all 4), some are version-specific (BC010 null_pointer_in_sqlite3Select only in 3.31.1). This is cross-pollination: patterns designed for one CVE also trigger adjacent bugs in other versions.

### Exercise B7: Add a New Grammar Rule (live coding)

**Scenario:** "Add a rule that generates DELETE statements."

**Steps:**
1. Open `grammars/active/sqlite_v3.py`
2. Add after the INSERT section:
   ```python
   ctx.rule("Stress-Query", "DELETE FROM {Table-Name} WHERE {Col-Ref} = {Literal-Value}")
   ```
3. Test:
   ```bash
   for i in $(seq 1 50); do
     ./target/release/generator -g grammars/active/sqlite_v3.py -t 10 2>/dev/null
   done | grep -c "DELETE"
   ```
4. Revert after demo: `git checkout grammars/active/sqlite_v3.py`

**What to explain:** Adding a new rule is one line in the Python grammar. PyO3 re-loads the Python file each time the fuzzer starts. The new rule gets weight 1.0 (default) and competes with existing Stress-Query alternatives via weighted random selection. No Rust recompilation needed.

---

## Part C: Theory Questions (from thesis)

### C1: What is grammar-based fuzzing?
Fuzzing = automated testing by feeding random/semi-random inputs to find crashes. Grammar-based = inputs follow a context-free grammar so they are syntactically valid. This avoids wasting execution budget on inputs the SQL parser rejects immediately. DBMS-Nautilus combines grammar-based generation with coverage-guided feedback (AFL-style bitmap) -- a greybox approach.

### C2: What is ASan/UBSan?
AddressSanitizer (ASan) = compiler instrumentation (`-fsanitize=address`) that detects memory errors at runtime: buffer overflow, use-after-free, double-free, stack/heap overflow. UndefinedBehaviorSanitizer (UBSan) = compiler instrumentation (`-fsanitize=undefined`) that detects undefined behavior: signed integer overflow, null pointer dereference, misaligned access, float cast overflow. Both are compile-time flags. When a bug is triggered, the sanitizer prints a diagnostic to stderr and exits with a configured code (223 for ASan via `ASAN_OPTIONS=exitcode=223`, 1 for UBSan via `halt_on_error=1`).

### C3: What is a CVE?
Common Vulnerabilities and Exposures -- a standardized identifier for publicly known security vulnerabilities. We target 6 CVEs across 4 SQLite versions: CVE-2019-19646 (infinite loop), CVE-2020-13434 (integer overflow in printf), CVE-2020-9327 (null pointer dereference), CVE-2020-13435 (null pointer in equalString), CVE-2020-13871 (use-after-free), CVE-2020-15358 (heap buffer over-read). Our grammar rediscovers 4/4 target CVEs without embedding the PoC SQL -- the grammar encodes structural patterns, not literal test cases.

### C4: What is the Thompson Sampling code in your repo?
**IMPORTANT: Thompson Sampling is NOT part of the thesis.** The code exists in `fuzzer/src/grammar_bandit.rs` (492 lines) as an experimental feature activated by `policy: "bandit"` in config.ron. It groups grammar rules into 6 categories (S1-S6), maintains Beta(alpha, beta) distributions per group, and uses Thompson Sampling to adapt weights at runtime. However, **all thesis experiments use `policy: "uniform"` (fixed weights)**. The thesis conclusion mentions reinforcement learning as a future direction, not a current contribution. If the teacher asks: "This is experimental code I wrote for future work. The thesis experiments all use fixed weights set at grammar design time."

### C5: What is the fork server?
AFL's optimization to avoid the overhead of `exec()` + binary loading for each test case. The harness binary is loaded once. `__AFL_INIT()` (harness/src/sqlite_harness.c:74) tells the binary to wait for commands from the fuzzer over a control pipe (fd 198). The fuzzer writes "go" -> harness `fork()`s -> child processes one SQL input via `sqlite3_exec()` -> child exits -> parent reads exit status + coverage bitmap via shared memory (fd 200) -> parent waits for next "go". This saves ~10-100x vs naive `exec()` per input because the binary, libraries, and initial state are loaded only once.

### C6: How does weighted rule sampling work?
Rule selection uses a linear scan in `get_random_rule_for_nt()` (context.rs:264): sum all applicable rule weights for the nonterminal, draw a uniform random number in [0, total_weight), walk rules subtracting each rule's weight until the running sum exceeds the threshold. This is O(n) per sample where n = number of alternatives for that nonterminal. The `loaded_dice` crate (Vose-Walker alias method, O(1) sampling) exists in the codebase but is only used for recursion depth selection in `recursion_info.rs`, not for production rule sampling.

### C7: What is cross-pollination (thesis finding)?
The key finding from RQ2: grammar patterns designed to trigger one specific CVE also trigger unrelated bugs. For example, window function + CTE patterns (included because CVE-2020-13871 involves use-after-free in window processing) also trigger null pointer dereferences in unrelated code paths (BC006, BC007, BC008). This means a well-designed grammar provides broader coverage than its explicit targets -- the structural primitives create a combinatorial space where unexpected bug-triggering compositions emerge from the interaction of independently designed rules.

### C8: What are the three research questions?
- **RQ1 (CVE Rediscovery):** Can DBMS-Nautilus, with low-weight seed rules, reliably rediscover known CVEs? Result: 4/4 CVEs rediscovered, most within seconds.
- **RQ2 (New Bug Detection):** Does DBMS-Nautilus, without seed rules, discover previously unreported bug classes? Result: 13 distinct bug classes (9 unique to DBMS-Nautilus), 48 unique stack hashes.
- **RQ3 (Performance Trade-off):** How does DBMS-Nautilus compare to EBNF-Baseline? Result: 108x more unique root causes (205.6 vs 1.9 per campaign), at 52.1% lower throughput (90.8 vs 189.9 exec/s). TTFC shows no significant difference.
