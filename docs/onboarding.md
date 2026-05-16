# Onboarding Guide — rl-nautilus-phase-2

## Project Overview

**Name:** rl-nautilus-phase-2  
**Description:** Grammar-based greybox fuzzer (Nautilus 2.0) with structural-primitives grammar for automated CVE discovery in SQLite  
**Languages:** Rust, Python, C, Bash  
**Frameworks:** PyO3 (Rust↔Python bridge), AFL fork-server protocol

---

## Architecture Layers

The project has 10 architectural layers. Here's how they connect:

```
┌─────────────────────────────────────────────────────────────────┐
│                    Grammar Definitions (Python DSL)              │
│  grammars/active/sqlite_v3.py → loaded at runtime via PyO3      │
└────────────────────────────┬────────────────────────────────────┘
                             │ loads
┌────────────────────────────▼────────────────────────────────────┐
│              Grammar Engine — grammartec (Rust)                  │
│  context.rs (weighted sampling) → tree.rs → mutator.rs          │
└────────────────────────────┬────────────────────────────────────┘
                             │ generates/mutates SQL
┌────────────────────────────▼────────────────────────────────────┐
│                    Fuzzer Core (Rust)                            │
│  main.rs (thread pool) → fuzzer.rs (exec) → shared_state.rs    │
└────────────────────────────┬────────────────────────────────────┘
                             │ executes via
┌────────────────────────────▼────────────────────────────────────┐
│              Fork Server → SQLite Harness (C)                   │
│  forksrv/lib.rs → harness/sqlite_harness.c → sqlite3_exec()    │
└────────────────────────────┬────────────────────────────────────┘
                             │ produces crashes
┌────────────────────────────▼────────────────────────────────────┐
│                    Triage Pipeline (Python)                      │
│  classify.py → stack_dedup.py → cve_signatures.py               │
└─────────────────────────────────────────────────────────────────┘
```

### Layer Details

| Layer | Purpose | Key Files |
|-------|---------|-----------|
| **Fuzzer Core** | Thread pool, mutation loop, crash detection | `fuzzer/src/main.rs`, `fuzzer.rs`, `shared_state.rs` |
| **Grammar Engine** | Weighted rule sampling, tree generation, grammar-aware mutations | `grammartec/src/context.rs`, `loaded_dice.rs`, `mutator.rs`, `tree.rs` |
| **Fork Server** | AFL-compatible process execution, shared memory coverage bitmap | `forksrv/src/lib.rs`, `exitreason.rs` |
| **SQLite Harness** | Executes SQL against instrumented SQLite, sanitizer oracle | `harness/src/sqlite_harness.c`, `harness/src/Makefile` |
| **Triage Pipeline** | Crash replay, dedup by stack hash, CVE signature matching | `triage/classify.py`, `cve_signatures.py`, `stack_dedup.py` |
| **Grammar Definitions** | SQLite attack patterns in Python DSL (ctx.rule API) | `grammars/active/sqlite_v3.py` |
| **CVE-to-Grammar** | Transforms CVE POC SQL → generalized grammar patterns | `cve2grammar/cve2grammar/generalizer/pattern_generalizer.py` |
| **Scripts** | Campaign runners, analysis, plotting | `scripts/run_eval.sh`, `consolidate_data.py`, `plot_comparison.py` |
| **Configuration** | Build (Cargo.toml, Makefile), runtime (config.ron) | `Cargo.toml`, `config.ron` |
| **Documentation** | Architecture, CVE list, experiment results | `docs/`, `README.md` |

---

## Key Concepts

### Grammar-Based Fuzzing
The fuzzer doesn't generate random bytes — it generates structurally valid SQL from a grammar. The grammar defines production rules (non-terminals → alternatives). Each rule can have a **weight** that biases sampling toward interesting patterns.

### Weighted Sampling (Loaded Dice)
`grammartec/src/loaded_dice.rs` implements O(1) weighted random sampling via the alias method. This is how the grammar engine picks which rule alternative to expand — heavier weights = more likely to be chosen.

### AFL Fork-Server Protocol
Instead of starting a new process per test case (expensive), the fork server forks a pre-initialized child. The child inherits the already-opened database and just executes the SQL. Coverage is tracked via shared memory bitmap.

### Sanitizer Oracle
The harness is compiled with ASan (memory errors) + UBSan (undefined behavior). Bugs that would be silent in production become detectable crashes:
- Exit 1 = UBSan caught something
- Exit 223 = ASan caught something  
- Exit 134 = Debug assert fired (SIGABRT)

### Triage Pipeline
Raw crashes are meaningless until triaged. `classify.py` replays each crash, captures the stack trace, hashes the top 5 frames, and groups duplicates. 10,000 raw crashes typically reduce to 5-10 unique root causes.

---

## Guided Tour (Recommended Reading Order)

1. **Project Overview** — Read `README.md` and `CLAUDE.md` for the big picture
2. **Grammar Engine** — Start with `grammartec/src/context.rs` (core), then `loaded_dice.rs` (sampling), `rule.rs` (definitions), `mutator.rs` (mutations)
3. **Fork Server & Execution** — `forksrv/src/lib.rs` + `harness/src/sqlite_harness.c`
4. **Fuzzer Core Loop** — `fuzzer/src/main.rs` → `fuzzer.rs` → `shared_state.rs`
5. **Attack Grammars** — `grammars/active/sqlite_v3.py` + `cve2grammar/` pipeline
6. **Triage Pipeline** — `triage/classify.py` → `cve_signatures.py` → `stack_dedup.py`
7. **Experiment Infrastructure** — `scripts/run_eval.sh`, `run_campaigns_safe.sh`, `consolidate_data.py`

---

## File Map

### Fuzzer Core (`fuzzer/src/`)
| File | Purpose | Complexity |
|------|---------|------------|
| `main.rs` | Entry point — thread pool, mutation loop, stats | Complex |
| `fuzzer.rs` | Core execution — run_on_input, crash classification, save | Complex |
| `shared_state.rs` | Thread-shared coverage bitmaps, crash counters | Moderate |
| `config.rs` | FuzzerConfig struct from config.ron | Simple |

### Grammar Engine (`grammartec/src/`)
| File | Purpose | Complexity |
|------|---------|------------|
| `context.rs` | Holds rules + weighted dice sampler, generates trees | Complex |
| `mutator.rs` | Splice, havoc, recursive minimize strategies | Complex |
| `tree.rs` | Tree representation, unparse to bytes | Complex |
| `loaded_dice.rs` | O(1) weighted sampling via alias method | Moderate |
| `rule.rs` | Rule::plain, Rule::weighted definitions | Moderate |
| `chunkstore.rs` | Memory-efficient node allocation | Moderate |
| `recursion_info.rs` | Prevents infinite tree expansion | Simple |
| `newtypes.rs` | NodeID, RuleID, NTermID wrappers | Simple |

### Fork Server (`forksrv/src/`)
| File | Purpose | Complexity |
|------|---------|------------|
| `lib.rs` | Fork server — AFL protocol, shared memory, IPC | Complex |
| `exitreason.rs` | ExitReason enum (Normal/Timeouted/Signaled/Stopped) | Simple |
| `newtypes.rs` | SubprocessError, BitmapID | Simple |

### Triage (`triage/`)
| File | Purpose | Complexity |
|------|---------|------------|
| `classify.py` | Unified triage — replay, dedup, classify | Complex |
| `cve_signatures.py` | Structural regex patterns per CVE | Moderate |
| `stack_dedup.py` | GDB-based stack extraction + hash dedup | Moderate |
| `fidelity_score.py` | Measures grammar→CVE pattern coverage | Moderate |
| `minimize.py` | Crash input minimization | Moderate |

---

## Complexity Hotspots

These files require careful understanding before modifying:

| File | Why It's Complex |
|------|-----------------|
| `fuzzer/src/main.rs` | Multi-threaded coordination, 740 lines, all subsystems meet here |
| `grammartec/src/context.rs` | Core grammar engine, PyO3 bridge, weighted sampling |
| `grammartec/src/mutator.rs` | Multiple mutation strategies, tree manipulation |
| `forksrv/src/lib.rs` | Low-level Unix IPC (pipes, fork, waitpid, shared memory) |
| `cve2grammar/.../pattern_generalizer.py` | Tree-sitter AST manipulation, grammar pattern generation |

---

## Quick Start Commands

```bash
# Build
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo build --release

# Build harness (from harness/src/)
cd harness/src && make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1

# Run a campaign (15 min)
DURATION=900 ./scripts/run_eval.sh sqlite-3.31.1 run1

# Triage crashes
python3 triage/classify.py workdirs/sqlite-3.31.1_uniform_run1 --harness harness/test/sqlite_harness_sqlite-3.31.1_test

# Smoke test
./scripts/smoke_test.sh
```

---

## Harness Directory Structure

```
harness/
├── src/          ← Source code + Makefile
├── afl/          ← AFL-instrumented (for fuzzing campaigns)
├── test/         ← ASan+UBSan (for triage/crash replay)
└── nosanit/      ← No sanitizers (production-like, for exploitability proof)
```

---

## CVE Targets

The fuzzer targets 4 SQLite versions with known CVEs:

| Version | CVE(s) | Bug Type |
|---------|--------|----------|
| 3.30.1 | CVE-2019-19646 | Infinite loop (PRAGMA) |
| 3.31.1 | CVE-2020-13434, CVE-2020-9327 | Printf overflow, null deref |
| 3.32.0 | CVE-2020-13435 | Null pointer in query planner |
| 3.32.2 | CVE-2020-13871, CVE-2020-15358 | Use-after-free, heap over-read |
