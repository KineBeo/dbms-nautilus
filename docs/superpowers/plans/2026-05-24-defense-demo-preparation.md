# Defense Demo Session Preparation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prepare all materials for the thesis defense demo session: feature list document, code tutorial for live coding, updated README (policy-compliant), and practice scenarios matching the teacher's hint about pipeline explanation + hyperparameter changes.

**Architecture:** Four deliverables — (1) demo feature list, (2) live-coding tutorial with practice exercises, (3) policy-compliant README.md, (4) practice Q&A cheat sheet. All stored in `docs/defense/` except README.md which goes in repo root.

**Tech Stack:** Markdown, Bash scripts, Rust (cargo), Python, LaTeX (existing thesis)

**Critical Policy Constraints (from policy.md):**
- Teacher will point at ANY code on GitHub and ask to explain the execution flow → must understand every file
- Teacher may ask for live small modifications → must be able to change code and re-run
- If student cannot explain or modify → **automatic fail**
- README.md is mandatory: must include install, deploy, and demo instructions
- Repository must have `/src` (our case: `fuzzer/`, `grammartec/`, `forksrv/`), `/references`, `README.md`
- Teacher hint: will ask about pipeline flow, may ask to change hyperparameters, change evaluation metrics, re-run with different dataset

---

## Task 1: Create Demo Feature List

**Files:**
- Create: `docs/defense/demo-features.md`

This document lists every feature you will demonstrate during the defense, organized by what the teacher might ask to see.

- [ ] **Step 1: Write the demo feature list**

Create `docs/defense/demo-features.md` with this content:

```markdown
# Defense Demo — Feature List

## 1. Grammar Engine (grammartec/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Grammar loading via PyO3 | `./target/release/generator -g grammars/active/sqlite_v3.py -t 10` | Python DSL → Rust rules via PyO3 bridge |
| Weighted sampling | Run generator 100x, count high-weight vs low-weight patterns | `weight=3.0` rules appear ~3x more than `weight=1.0` |
| Tree generation | `./target/release/generator -g grammars/active/sqlite_v3.py -t 5 -s` | Generates corpus/ folder with SQL files |
| Rule types | Open `grammars/active/sqlite_v3.py` | Plain rules, regex rules, script rules, weighted rules |

## 2. Fuzzer Core (fuzzer/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Full fuzzing campaign | `DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` | 60s campaign: config → fuzz → triage |
| Config system | `cat workdirs/sqlite-3.31.1_demo/config.ron` | RON config: threads, timeout, bitmap size, grammar path |
| Execution logging | `head -20 workdirs/sqlite-3.31.1_demo/exec.log` | Per-execution: strategy, new_bits, exit_reason |
| Multi-threaded mode | `THREADS=2 DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 mt_demo` | Shared bitmap, thread-safe queue |
| Smoke test suite | `./scripts/smoke_test.sh` | 11 component tests in ~90s |

## 3. Harness (harness/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Single SQL execution | `./harness/afl/sqlite_harness_sqlite-3.31.1 input.sql` | Fork-server mode, ASan+UBSan oracle |
| Crash reproduction | `cd results/crashes/BC003_.../1ca1c0159b42ae50 && ./reproduce.sh` | Trigger SQL → ASan output |
| Multi-version builds | `ls harness/afl/` | 4 CVE-bearing versions built |
| Build a harness | `cd harness/src && make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1` | AFL instrumentation + sanitizers |

## 4. Triage Pipeline (triage/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Crash collection | `python3 scripts/collect_crashes.py --scan-only` | Scans all campaigns, dedup by stack hash |
| CVE signature matching | `python3 -c "from triage.cve_signatures import _CVES; print(_CVES)"` | 6 CVE patterns as regex lists |
| Bug class registry | `cat results/crashes/registry.md` | 10 bug classes, 85 unique crashes |

## 5. Evaluation Pipeline (scripts/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Single campaign | `DURATION=120 ./scripts/run_eval.sh sqlite-3.31.1 demo_run` | End-to-end: config → fuzz → triage |
| Statistics | `python3 scripts/compute_stats.py` | Mann-Whitney U test, effect size |
| Figure generation | `python3 scripts/generate_figures.py` | Matplotlib plots for thesis |

## 6. Grammar Design (grammars/)

| Feature | Demo Command | What It Shows |
|---------|-------------|---------------|
| Active grammar (v3.4) | `head -50 grammars/active/sqlite_v3.py` | CVE seed rules, weighted dispatch |
| Uniform grammar (v3.3) | `diff grammars/active/sqlite_v3.py grammars/active/sqlite_v3_uniform.py \| head -30` | Same structure, no CVE seeds |
| EBNF baseline | `head -50 grammars/baseline/sqlite-ebnf.py` | Spec-derived, no attack patterns |

## 7. Key Results (can show from results/)

| Result | Evidence |
|--------|----------|
| 4/4 CVEs rediscovered | `results/ch4_final/rq1_cve_hits.csv` |
| 10 bug classes found | `results/crashes/registry.md` |
| TTFC ~1-2 seconds | `results/ch4_final/rq1_ttfc_per_cve.csv` |
| 108x more root causes vs baseline | `results/ch4_final/rq3_summary.csv` |
```

- [ ] **Step 2: Verify all demo commands work**

Run each command from the feature list to confirm they work on your machine. Test at minimum:

```bash
# Grammar loading
./target/release/generator -g grammars/active/sqlite_v3.py -t 10

# Harness single execution
echo "SELECT 1;" > /tmp/test.sql && ./harness/afl/sqlite_harness_sqlite-3.31.1 /tmp/test.sql

# Crash reproduction
cd results/crashes/BC003_signed_integer_overflow_in_sqlite3_str_vappendf/1ca1c0159b42ae50
./reproduce.sh 2>&1 | head -5

# Quick campaign (60s)
DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 verify_demo
```

Expected: all commands succeed, campaign produces exec.log with entries, crash reproduction shows ASan output.

- [ ] **Step 3: Commit**

```bash
git add docs/defense/demo-features.md
git commit -m "docs: add defense demo feature list"
```

---

## Task 2: Create Live Coding Tutorial

**Files:**
- Create: `docs/defense/live-coding-tutorial.md`

This is the most critical document. It prepares you for the teacher pointing at any code and asking "explain this" or "change this parameter."

- [ ] **Step 1: Write the live coding tutorial**

Create `docs/defense/live-coding-tutorial.md`:

```markdown
# Live Coding Tutorial — Defense Preparation

## Part A: Execution Flow Walkthrough

The teacher will ask: "Explain the pipeline execution flow."

### Pipeline Overview (memorize this)

```
User runs: ./scripts/run_eval.sh sqlite-3.31.1 run1
                    │
                    ▼
        ┌──── run_eval.sh ────┐
        │ 1. Validate harness │
        │ 2. Write config.ron │
        │ 3. Start fuzzer     │
        │ 4. Run triage       │
        └─────────┬───────────┘
                  │
                  ▼
        ┌──── fuzzer binary (Rust) ────┐
        │ main.rs:                     │
        │   pyo3::prepare_python()     │  ← Init Python for grammar
        │   load_config(config.ron)    │  ← Read RON config
        │   load_grammar(sqlite_v3.py)│  ← PyO3 bridge → Rule objects
        │   spawn N threads           │  ← Each runs fuzzing_thread()
        └─────────┬───────────────────┘
                  │
                  ▼ (per thread)
        ┌──── fuzzing_thread() ────────────────────┐
        │ 1. Generate initial inputs (gen phase)   │
        │ 2. Loop: pick from queue                 │
        │    a. minimize_tree (shrink)              │
        │    b. minimize_rec (recursion)            │
        │    c. mut_rules (deterministic)           │
        │    d. mut_random (havoc) × N              │
        │    e. mut_random_recursion × N            │
        │    f. mut_splice (from ChunkStore) × N    │
        │ 3. Each mutation → unparse → bytes        │
        │ 4. Write to file → fork child             │
        │ 5. Child: harness reads SQL, executes     │
        │ 6. Parent: read bitmap, check new edges   │
        │ 7. New coverage? → add to queue           │
        │ 8. Crash? → save to outputs/signaled/     │
        └──────────────────────────────────────────┘
```

### Key File → Function Mapping

| When teacher points at... | Key function to explain | What it does |
|---------------------------|------------------------|--------------|
| `fuzzer/src/main.rs` | `main()` line 233 | CLI parsing, config load, thread spawn |
| `fuzzer/src/main.rs` | `fuzzing_thread()` line 87 | Per-thread mutation loop: gen → minimize → mutate → execute |
| `fuzzer/src/fuzzer.rs` | `run_on_with_dedup()` line 170 | Unparse tree → write file → fork child → read bitmap → detect new edges |
| `fuzzer/src/fuzzer.rs` | `new_bits()` line 453 | Compare bitmap against global: if new edge → return true |
| `fuzzer/src/state.rs` | `FuzzingState` struct | Bundles Context + Mutator + Config + ChunkStore per thread |
| `grammartec/src/context.rs` | `generate_tree_from_nt()` line 393 | Weighted sampling: pick rule via linear scan, recurse children |
| `grammartec/src/context.rs` | `add_rule()` line 66 | Register a production rule in the grammar |
| `grammartec/src/rule.rs` | `Rule` enum | PlainRule (literal), ScriptRule (Python), RegExpRule (regex) |
| `grammartec/src/rule.rs` | `Rule` enum (line 84) | PlainRule, ScriptRule, RegExpRule — each has `weight: f32` field |
| `grammartec/src/tree.rs` | `unparse()` line 167 | Walk AST recursively → concatenate leaf bytes → SQL string |
| `grammartec/src/mutator.rs` | `mut_random()` line 177 | Pick random node → regenerate its subtree (havoc mutation) |
| `grammartec/src/mutator.rs` | `mut_splice()` line 136 | Pick random node → replace with same-type chunk from ChunkStore |
| `grammartec/src/chunkstore.rs` | `ChunkStore::add_tree()` | Extract subtrees from interesting inputs → store by nonterminal type |
| `forksrv/src/lib.rs` | `ForkServer::run()` line 192 | Write to control pipe → fork child → read status pipe → collect bitmap |
| `harness/src/sqlite_harness.c` | `main()` line 68 | `__AFL_INIT()` → read SQL file → `sqlite3_exec()` → exit |
| `fuzzer/src/python_grammar_loader.rs` | `load_python_grammar()` | PyO3: exec Python file, call `ctx.rule()` → Rust `Context::add_rule()` |
| `fuzzer/src/grammar_bandit.rs` | `select_group()` line 166, `observe_reward()` line 203 | Thompson Sampling: sample Beta(α,β) per group → normalize → apply multipliers |
| `triage/cve_signatures.py` | `_CVES` list (line 15) | 6 CVEs as regex pattern lists; `missing_patterns()` (line 85) checks coverage |
| `triage/stack_dedup.py` | `hash_frames()` (line 56) | Extract top 5 GDB frames → filter to SQLite-internal → SHA256 → dedup key |

### Practice: Explain These (say it out loud)

1. **"What happens when run_eval.sh starts?"**
   → Creates workdir, writes config.ron (binary path, grammar path, thread count, timeout, bitmap size), then starts the fuzzer binary with `-c config.ron`.

2. **"How does the grammar generate SQL?"**
   → Python file defines rules via `ctx.rule("NT", "expansion")`. PyO3 loads them into Rust `Context`. `generate_tree_from_nt("START")` picks a rule for "START" (weighted random via linear scan over rule weights), expands children recursively until all leaves are terminals. `unparse()` concatenates leaf bytes into SQL string.

3. **"How does the fuzzer detect a crash?"**
   → The harness is compiled with ASan+UBSan. Memory errors cause ASan to exit with code 223. UBSan exits with code 1. The fork server reads the child's exit status. Non-zero + non-timeout = crash → saved to `outputs/signaled/`.

4. **"What is coverage-guided feedback?"**
   → Each execution updates a shared memory bitmap (AFL-style). Each edge in the control flow graph maps to a bitmap index. After execution, the fuzzer compares the bitmap against the global bitmap. If any new bit is set (= new edge discovered), the input is "interesting" → added to queue for further mutation.

5. **"How do mutations work?"**
   → Six strategies: (a) minimize_tree: try removing subtrees, keep if coverage preserved. (b) mut_rules: try every alternative rule for each node (deterministic). (c) mut_random (havoc): pick random node, regenerate subtree. (d) mut_random_recursion: inflate/deflate recursive structures. (e) mut_splice: replace node with same-type subtree from ChunkStore. ChunkStore accumulates subtrees from all interesting inputs → enables cross-input recombination.

6. **"What is the difference between your grammar and EBNF baseline?"**
   → EBNF baseline (`grammars/baseline/sqlite-ebnf.py`) is derived from SQLite's grammar spec — generates syntactically valid SQL but without attack patterns. Our grammar (`grammars/active/sqlite_v3.py`) decomposes SQL into Schema-Setup + Stress-Query + Validation-Op, adds boundary values (INT32_MAX, 1e308), window functions, CTE recursion, FTS queries — structural patterns that exercise CVE-bearing code paths. Result: 108x more unique root causes.

---

## Part B: Live Coding Exercises

The teacher hint says they may ask to: change hyperparameters, change evaluation metrics, re-run experiments.

### Exercise B1: Change Timeout (hyperparameter)

**Scenario:** "Change the per-execution timeout from 500ms to 1000ms and run a campaign."

**Steps:**
1. Open `scripts/run_eval.sh`
2. Find line: `TIMEOUT_MS="${TIMEOUT_MS:-500}"`
3. Either change the default or override via environment:
   ```bash
   TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 timeout_demo
   ```
4. Show the config.ron: `cat workdirs/sqlite-3.31.1_timeout_demo/config.ron`
   → Confirm `timeout_in_millis: 1000`

**What to explain:** Higher timeout means the fuzzer waits longer per execution before killing the child. Trade-off: fewer executions/second but catches bugs that need longer execution time (deep recursion, complex joins).

### Exercise B2: Change Thread Count (hyperparameter)

**Scenario:** "Run with 2 threads instead of 1."

**Steps:**
1. Override via environment:
   ```bash
   THREADS=2 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 threads_demo
   ```
2. Show config: `cat workdirs/sqlite-3.31.1_threads_demo/config.ron`
   → `number_of_threads: 2`
3. Show it ran faster: compare exec.log line counts between 1-thread and 2-thread runs.

**What to explain:** Multiple threads share the same bitmap (GlobalSharedState). Each thread has its own FuzzingState (Context, Mutator). More threads = more executions/second but diminishing returns due to bitmap contention.

### Exercise B3: Change Max Tree Size (hyperparameter)

**Scenario:** "What happens if you increase the maximum tree depth?"

**Steps:**
1. Override:
   ```bash
   MAX_TREE_SIZE=500 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 tree_demo
   ```
2. Compare generated SQL sizes:
   ```bash
   # Default (300)
   ./target/release/generator -g grammars/active/sqlite_v3.py -t 300 | wc -c
   # Larger (500)
   ./target/release/generator -g grammars/active/sqlite_v3.py -t 500 | wc -c
   ```

**What to explain:** `max_tree_size` limits the AST node count. Larger trees = more complex SQL = slower execution but potentially deeper state exploration. Too large = timeout kills most executions → wasted budget.

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
5. Revert the change after demo.

**What to explain:** The weighted sampler (linear scan in `get_random_rule_for_nt()`) converts weights to probabilities. Weight 5.0 vs weight 1.0 means the window function rule is chosen ~5x more often when the grammar engine selects a rule for that nonterminal. This is the core mechanism: bias generation toward structures that exercise specific code paths.

### Exercise B5: Change Evaluation Metric (metric change)

**Scenario:** "Instead of counting unique root causes, count unique crash stack hashes."

**Steps:**
1. Open `triage/stack_dedup.py`
2. Current: `hash_frames()` uses top 5 GDB frames → filter to SQLite-internal → SHA256
3. To count unique hashes:
   ```python
   # In a Python REPL:
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
4. Compare: "We report 10 bug classes (grouped by crash site function name) and 85 unique stack hashes."

**What to explain:** Bug class = grouping by the crashing function name (higher-level). Stack hash = grouping by top-3 stack frames (finer-grained). We chose bug classes for the thesis because different inputs can crash at the same line but via different paths — bug classes are more meaningful for comparing grammar effectiveness.

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
   # After campaign finishes:
   find workdirs/sqlite-3.32.0_cross_demo/outputs/signaled -type f | wc -l
   ```

**What to explain:** Same grammar, different SQLite binary. The grammar targets structural patterns, not version-specific bugs. Some bugs exist in multiple versions (BC001 appears in all 4), some are version-specific (BC010 only in 3.31.1). This is cross-pollination: patterns designed for one CVE also trigger adjacent bugs.

### Exercise B7: Add a New Grammar Rule (live coding)

**Scenario:** "Add a rule that generates DELETE statements."

**Steps:**
1. Open `grammars/active/sqlite_v3.py`
2. Add after the INSERT section:
   ```python
   # DELETE statement
   ctx.rule("Stress-Query", "DELETE FROM {Table-Name} WHERE {Col-Ref} = {Literal-Value}")
   ```
3. Test:
   ```bash
   for i in $(seq 1 50); do
     ./target/release/generator -g grammars/active/sqlite_v3.py -t 10 2>/dev/null
   done | grep -c "DELETE"
   ```
4. Revert after demo.

**What to explain:** Adding a new rule is one line. The grammar engine picks it up automatically because PyO3 re-loads the Python file each time. The new rule gets weight 1.0 (default) and competes with existing Stress-Query alternatives.

---

## Part C: Theory Questions (from thesis)

### C1: What is grammar-based fuzzing?
Fuzzing = automated testing by feeding random inputs. Grammar-based = inputs follow a grammar (context-free grammar) so they are syntactically valid. This avoids wasting time on inputs the parser rejects immediately. Nautilus combines grammar-based generation with coverage-guided feedback (AFL-style bitmap).

### C2: What is ASan/UBSan?
AddressSanitizer (ASan) = compiler instrumentation that detects memory errors (buffer overflow, use-after-free, double-free). UndefinedBehaviorSanitizer (UBSan) = detects undefined behavior (integer overflow, null pointer dereference, misaligned access). Both are compile-time flags (`-fsanitize=address,undefined`). When a bug is triggered, the sanitizer prints a diagnostic and exits with a configured code (223 for ASan, 1 for UBSan in our harness).

### C3: What is a CVE?
Common Vulnerabilities and Exposures — a standardized identifier for security bugs. We target 6 CVEs across 4 SQLite versions. Our grammar rediscovers 4/4 target CVEs without embedding the PoC SQL.

### C4: What is Thompson Sampling?
A Bayesian bandit algorithm. Each grammar rule group has a Beta(α,β) distribution. After each execution: if the input found new coverage, increment α (success); otherwise increment β (failure). To select weights: sample from each group's Beta distribution, normalize. The effect: groups that produce more coverage get higher weights over time.

### C5: What is the fork server?
AFL's optimization: instead of exec()+loading the binary each time, the binary is loaded once and calls `__AFL_INIT()`. After that, the fuzzer tells the binary to `fork()`. The child runs one input and exits. The parent waits, reads the bitmap, and forks again. This avoids the overhead of process creation and binary loading (~10-100x speedup vs naive exec).

### C6: How does weighted rule sampling work?
Rule selection uses a linear scan in `get_random_rule_for_nt()` (context.rs:264): sum all applicable rule weights, draw a uniform random threshold, walk rules subtracting weights until the threshold is crossed. This is O(n) per sample where n = number of alternatives for that nonterminal. The `loaded_dice` crate (Vose-Walker alias method, O(1) sampling) is only used for recursion depth selection in `recursion_info.rs`, not for rule sampling.

### C7: What is cross-pollination (thesis finding)?
Our key finding: grammar patterns designed to trigger one specific CVE also trigger unrelated bugs. For example, window function + CTE patterns (designed for CVE-2020-13871) also trigger null pointer dereferences in unrelated code paths. This means a well-designed grammar provides broader coverage than its explicit targets.
```

- [ ] **Step 2: Practice each exercise at least once**

Actually run each exercise B1-B7 on your machine. Time yourself. Each should take under 2 minutes.

- [ ] **Step 3: Commit**

```bash
git add docs/defense/live-coding-tutorial.md
git commit -m "docs: add live coding tutorial for defense preparation"
```

---

## Task 3: Update README.md (Policy-Compliant)

**Files:**
- Modify: `README.md` (root)

Policy requires: README must include detailed instructions for environment setup, running code, and demo. Current README has the basics but needs more detail per policy requirements.

- [ ] **Step 1: Read current README**

Read the existing `README.md` (96 lines). Identify gaps vs policy:
- Missing: detailed environment setup (Python version, AFL++ install, Rust version)
- Missing: step-by-step demo instructions
- Missing: expected outputs for each command
- Missing: Vietnamese description (check if required)
- Outdated: Phase 3 says "Not started" but DQN was removed; should say "Deferred"

- [ ] **Step 2: Rewrite README.md**

Update `README.md` to include:

**Section 1: Project Title + Description** (keep existing, fix Phase 3 status)

**Section 2: Prerequisites** (expand):
```markdown
## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Rust | stable (1.75+) | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Python | 3.13+ with dev headers | `sudo apt install python3-dev` |
| AFL++ | latest | `sudo apt install afl++` or build from source |
| clang | 14+ | `sudo apt install clang` |
| make | any | `sudo apt install build-essential` |

Verify:
\`\`\`bash
rustc --version    # rustc 1.75+
python3 --version  # Python 3.13+
afl-clang-fast --version  # afl-cc
clang --version    # clang 14+
\`\`\`
```

**Section 3: Build** (expand with expected output):
```markdown
## Build

### Step 1: Build the fuzzer
\`\`\`bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo build --release
\`\`\`
Expected: `Compiling fuzzer v0.1.0` → `Finished release [optimized]`

### Step 2: Build harnesses for all target versions
\`\`\`bash
cd harness/src
make build-all
\`\`\`
Expected: Binaries in `harness/afl/`, `harness/test/`, `harness/nosanit/`

### Step 3: Verify build
\`\`\`bash
./scripts/smoke_test.sh
\`\`\`
Expected: `11/11 PASSED, 0 FAILED`
```

**Section 4: Demo** (new, required by policy):
```markdown
## Demo

### Quick Demo: Generate SQL from Grammar
\`\`\`bash
./target/release/generator -g grammars/active/sqlite_v3.py -t 10
\`\`\`
Output: A random SQL statement (CREATE TABLE + INSERT + SELECT with window functions, CTEs, etc.)

### Quick Demo: Run a 2-minute Fuzzing Campaign
\`\`\`bash
DURATION=120 ./scripts/run_eval.sh sqlite-3.31.1 demo_run
\`\`\`
Output: Campaign starts, finds crashes within seconds, triage classifies them.

### Quick Demo: Reproduce a Known Crash
\`\`\`bash
cd results/crashes/BC003_signed_integer_overflow_in_sqlite3_str_vappendf/1ca1c0159b42ae50
./reproduce.sh
\`\`\`
Output: ASan reports `signed integer overflow` in `sqlite3_str_vappendf`.

### Full Evaluation (from thesis Chapter 4)
\`\`\`bash
# RQ1: CVE rediscovery (4 versions × 5 runs × 15 min each = ~5 hours)
DURATION=900 RUNS=5 ./scripts/run_campaigns_safe.sh

# RQ3: Grammar comparison (DBMS-Nautilus vs EBNF-Baseline)
DURATION=900 ./scripts/run_comparison.sh
\`\`\`
```

**Section 5: Repository Structure** (required by policy):
```markdown
## Repository Structure

\`\`\`
├── fuzzer/          # Rust: fuzzer coordinator (main loop, state, config, queue)
├── grammartec/      # Rust: grammar engine (rules, trees, mutations, weighted sampling)
├── forksrv/         # Rust: AFL-compatible fork server
├── harness/         # C: SQLite harness with ASan/UBSan instrumentation
│   ├── src/         # Source code + Makefile
│   ├── afl/         # Compiled fuzzing harnesses
│   ├── test/        # Compiled triage harnesses (ASan+UBSan, no AFL)
│   └── nosanit/     # Compiled production harnesses (no sanitizers)
├── grammars/        # Python: grammar DSL files
│   ├── active/      # Current grammars (v3.4 + uniform)
│   └── baseline/    # EBNF baseline grammar
├── triage/          # Python: crash classification pipeline
├── scripts/         # Bash+Python: evaluation orchestration
├── cve_builds/      # SQLite source code for each target version
├── results/         # Experimental data (CSV, crash evidence, figures)
├── reference/       # Research papers, policy documents
├── docs/            # Documentation
│   ├── thesis/      # LaTeX thesis source + slides
│   └── core/        # Technical documentation
└── README.md        # This file
\`\`\`
```

**Section 6: Key Results** (keep existing, add evidence pointers)

**Section 7: Documentation** (keep existing)

**Section 8: License** (keep existing)

- [ ] **Step 3: Verify README commands work**

Run each command listed in the README to verify they produce the expected output.

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "docs: update README with policy-compliant setup and demo instructions"
```

---

## Task 4: Create Defense Q&A Cheat Sheet

**Files:**
- Create: `docs/defense/qa-cheatsheet.md`

Based on the teacher's hint, prepare answers to likely questions organized by category.

- [ ] **Step 1: Write the Q&A cheat sheet**

Create `docs/defense/qa-cheatsheet.md`:

```markdown
# Defense Q&A Cheat Sheet

Based on teacher hint: "explain pipeline flow, change hyperparameters, change evaluation metrics, re-run with different dataset."

## Category 1: Pipeline Flow Questions

**Q: Walk me through what happens from start to finish when you run a fuzzing campaign.**
A: run_eval.sh validates the harness binary exists → writes config.ron with parameters (grammar path, timeout, threads, bitmap size) → starts the fuzzer binary. The fuzzer initializes Python (PyO3), loads the grammar (each `ctx.rule()` call creates a Rust Rule object), spawns N threads. Each thread generates initial inputs by sampling the grammar, then enters a mutation loop: pick input from queue → minimize → mutate (havoc, splice, deterministic rules) → unparse tree to SQL bytes → write to temp file → fork child → child runs harness (sqlite3_exec on the SQL) → parent reads coverage bitmap → if new edge found, add to queue; if crash, save to outputs/signaled/. After the duration expires, triage runs: stack_dedup groups crashes by stack hash, classify.py identifies bug classes, cve_signatures.py checks for CVE pattern matches.

**Q: How does the grammar engine select which rule to apply?**
A: Each nonterminal has multiple alternative rules. When generating, `Context::generate_tree_from_nt()` (line 393) is called, which calls `get_random_rule_for_nt()` (line 264). It sums all applicable rule weights, draws a uniform random number, then walks rules subtracting weights until the threshold is crossed — O(n) linear scan. Default weight is 1.0. Our grammar assigns higher weights (2.0-3.0) to rules producing attack-relevant SQL constructs (window functions, CTEs, boundary values).

**Q: How does the fork server work?**
A: The harness binary links with AFL instrumentation. `__AFL_INIT()` at the start of `main()` tells the binary to wait for commands from the fuzzer over a control pipe. The fuzzer writes "go" → harness `fork()`s → child processes the input → child exits → parent reads exit status + coverage bitmap via shared memory → parent waits for next "go". This avoids re-loading the binary for each input (~10-100x faster than exec()).

**Q: How do you detect bugs?**
A: Three oracle mechanisms: (1) ASan detects memory errors (buffer overflow, use-after-free, heap-buffer-read-past) and exits with code 223. (2) UBSan detects undefined behavior (integer overflow, null pointer dereference, misaligned access) and exits with code 1. (3) SQLite debug assertions trigger SIGTRAP (signal 5), caught by the fork server. The fuzzer classifies exit reasons in `ExitReason` enum (forksrv/src/exitreason.rs:7): `Normal(i32)`, `Timeouted`, `Signaled(i32)`, `Stopped(i32)`.

**Q: How do mutations preserve syntactic validity?**
A: All mutations operate on the parse tree (AST), not on raw bytes. `mut_random()` picks a random node, regenerates its subtree using the grammar — result is always a valid expansion. `mut_splice()` replaces a node with a same-nonterminal-type subtree from ChunkStore — type-compatible by construction. `mut_rules()` tries every alternative rule for a node — each alternative is grammar-valid. Only after mutation does `unparse()` convert the tree back to bytes.

## Category 2: Hyperparameter Questions

**Q: What are the main hyperparameters?**
A: In config.ron: `timeout_in_millis` (per-execution timeout, default 500ms), `number_of_threads` (parallelism, default 1), `max_tree_size` (AST node limit, default 300), `bitmap_size` (coverage map size, default 2MB), `number_of_generate_inputs` (initial corpus size, default 1000), `number_of_deterministic_mutations` (mut_rules passes, default 1). In grammar: `weight` parameter on each rule (default 1.0).

**Q: Show me how to change the timeout and re-run.**
A: `TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` — this overrides the default via environment variable. The script writes it into config.ron. Verify: `grep timeout workdirs/sqlite-3.31.1_demo/config.ron`.

**Q: What happens if you increase max_tree_size?**
A: Larger trees = more complex SQL = deeper state exploration. But: more complex SQL takes longer to execute, so more inputs hit the timeout and get killed → wasted execution budget. The default 300 balances complexity vs throughput. Our experiments used 1000 for the full campaigns.

## Category 3: Evaluation Metric Questions

**Q: What metrics did you use to compare grammars?**
A: Five metrics: (1) CVE rediscovery rate — how many of the 4 target CVEs were found. (2) Unique bug classes — grouping crashes by the function where they occur. (3) Unique root causes — distinct stack traces (finer-grained than bug classes). (4) Edge coverage — number of unique edges in the coverage bitmap over time. (5) Throughput — executions per second. (6) Time-to-first-crash (TTFC) — seconds until first crash in each campaign.

**Q: How did you measure statistical significance?**
A: Mann-Whitney U test (non-parametric, doesn't assume normal distribution) with N=5 runs per configuration. Effect size via rank-biserial correlation. We chose Mann-Whitney because: (a) small sample size (N=5), (b) crash counts are not normally distributed, (c) it's the standard in fuzzing literature (e.g., Klees et al. USENIX'18 recommendations).

**Q: Could you use a different metric?**
A: Yes. Alternative metrics: (a) unique code branches (vs edges) — coarser but simpler. (b) Vargha-Delaney A₁₂ effect size — standard alternative to rank-biserial. (c) Time-to-N-crashes — more informative than TTFC for sustained bug finding. (d) Bug severity weighting — weight HIGH bugs more than LOW. The choice depends on what aspect of fuzzer effectiveness you want to measure.

## Category 4: Code Understanding Questions

**Q: Show me where the bitmap comparison happens.**
A: `fuzzer/src/fuzzer.rs`, function `new_bits()` at line 453. It compares the thread-local bitmap against the global shared bitmap byte-by-byte. If any byte in the local has bits not present in the global → new edge → return true.

**Q: How does PyO3 bridge work?**
A: `fuzzer/src/python_grammar_loader.rs`. The `load_python_grammar()` function: (1) creates a Python module with a `PyContext` class, (2) injects it into the Python runtime, (3) `exec()` the grammar .py file, (4) each `ctx.rule()` call in Python triggers `PyContext::rule()` which calls Rust `Context::add_rule()`. The grammar is defined in Python for rapid iteration but compiled into Rust data structures for performance.

**Q: What is ChunkStore?**
A: `grammartec/src/chunkstore.rs`. A pool of subtrees from "interesting" inputs (those that found new coverage). When an input is added to the queue, its subtrees are extracted and stored by nonterminal type. During `mut_splice()`, a random subtree of matching type is picked from ChunkStore and grafted into the current tree. This enables cross-input recombination — combining parts from different successful inputs.

**Q: How does the triage pipeline classify crashes?**
A: Three stages: (1) `stack_dedup.py:hash_frames()` (line 56) — run GDB with `bt 5` to get top 5 stack frames, filter to SQLite-internal frames, SHA256 hash → unique crash identifier. (2) `classify.py` — group by crashing function name → bug class (BC001-BC010). (3) `cve_signatures.py` — regex-match the trigger SQL against known CVE structural patterns (`_CVES` list, line 15) → CVE attribution.
```

- [ ] **Step 2: Commit**

```bash
git add docs/defense/qa-cheatsheet.md
git commit -m "docs: add defense Q&A cheat sheet with practice scenarios"
```

---

## Task 5: Create Quick-Reference Card

**Files:**
- Create: `docs/defense/quick-reference.md`

A one-page card you can glance at during the defense (on your second monitor or printed).

- [ ] **Step 1: Write the quick reference**

Create `docs/defense/quick-reference.md`:

```markdown
# Quick Reference Card — Defense Demo

## Commands You'll Need

| Action | Command |
|--------|---------|
| Generate SQL | `./target/release/generator -g grammars/active/sqlite_v3.py -t 10` |
| Run 60s campaign | `DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Run smoke tests | `./scripts/smoke_test.sh` |
| Reproduce crash | `cd results/crashes/BC003_.../1ca1c0159b42ae50 && ./reproduce.sh` |
| Build fuzzer | `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release` |
| Build harness | `cd harness/src && make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1` |
| Change timeout | `TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Change threads | `THREADS=2 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Change tree size | `MAX_TREE_SIZE=500 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 demo` |
| Count crash hashes | `find results/crashes -mindepth 2 -maxdepth 2 -type d \| wc -l` |

## Key Numbers

| Metric | Value |
|--------|-------|
| CVEs rediscovered | 4/4 (100%) |
| Bug classes found | 10 (7 unique to our grammar) |
| Unique root causes | 85 crash hashes |
| TTFC | ~1-2 seconds |
| Root cause advantage | 108x vs EBNF baseline |
| Throughput cost | 2.1x slower than baseline |
| Grammar rules | 526 (v3.4) / 520 (uniform v3.3) |
| Total Rust LoC | ~6,200 |
| Total campaigns | 54 |

## File Locations

| What | Where |
|------|-------|
| Fuzzer main | `fuzzer/src/main.rs:233` (main), `:87` (fuzzing_thread) |
| Execution loop | `fuzzer/src/fuzzer.rs:170` (run_on_with_dedup) |
| Grammar engine | `grammartec/src/context.rs:393` (generate_tree_from_nt) |
| Weighted sampling | `grammartec/src/context.rs:264` (get_random_rule_for_nt, O(n) linear scan) |
| Mutations | `grammartec/src/mutator.rs:177` (mut_random), `:136` (mut_splice) |
| Tree → SQL | `grammartec/src/tree.rs:167` (unparse) |
| Fork server | `forksrv/src/lib.rs:192` (run) |
| Harness | `harness/src/sqlite_harness.c:68` (main) |
| Grammar (active) | `grammars/active/sqlite_v3.py` |
| CVE signatures | `triage/cve_signatures.py:15` (_CVES), `:85` (missing_patterns) |
| Stack dedup | `triage/stack_dedup.py:56` (hash_frames) |
| Config template | `scripts/run_eval.sh:73-86` (config.ron generation) |
| Crash evidence | `results/crashes/BC*/` |
| Thesis data | `results/ch4_final/` |
```

- [ ] **Step 2: Commit**

```bash
git add docs/defense/quick-reference.md
git commit -m "docs: add defense quick reference card"
```

---

## Task 6: Verify Everything End-to-End

**Files:**
- No new files

Final verification that all demo scenarios work on your machine.

- [ ] **Step 1: Run the smoke test**

```bash
./scripts/smoke_test.sh
```

Expected: 11/11 PASSED

- [ ] **Step 2: Run a quick campaign**

```bash
DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 final_verify
```

Expected: exec.log has entries, crashes found, queue populated.

- [ ] **Step 3: Test hyperparameter changes**

```bash
TIMEOUT_MS=1000 DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 hp_verify
THREADS=2 DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 mt_verify
```

Expected: Both campaigns run and produce results.

- [ ] **Step 4: Test crash reproduction**

```bash
cd results/crashes/BC003_signed_integer_overflow_in_sqlite3_str_vappendf/1ca1c0159b42ae50
./reproduce.sh 2>&1 | head -10
```

Expected: ASan output showing signed integer overflow.

- [ ] **Step 5: Test grammar modification and revert**

```bash
# Add a test rule
echo 'ctx.rule("Stress-Query", "SELECT 42 AS defense_test")' >> grammars/active/sqlite_v3.py
# Verify it works
./target/release/generator -g grammars/active/sqlite_v3.py -t 5 2>/dev/null | head -5
# Revert
git checkout grammars/active/sqlite_v3.py
```

Expected: Generator works with modified grammar, revert succeeds.

- [ ] **Step 6: Final commit of all defense materials**

```bash
git add docs/defense/
git commit -m "docs: complete defense demo preparation materials"
```
