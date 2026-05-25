# DBMS-Nautilus: Grammar-Based Fuzzer for CVE Discovery in SQLite

Grammar-based coverage-guided fuzzer (built on Nautilus 2.0) with a domain-specific SQL grammar engineered for automated vulnerability discovery in SQLite. Fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) using weighted grammar sampling to target vulnerability-triggering code paths.

## Prerequisites

| Tool | Version | Install |
|------|---------|---------|
| Rust | stable (1.75+) | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Python | 3.13+ with dev headers | `sudo apt install python3-dev` |
| AFL++ | latest | `sudo apt install afl++` or build from source |
| clang | 14+ | `sudo apt install clang` |
| make | any | `sudo apt install build-essential` |
| GDB | any | `sudo apt install gdb` (for triage pipeline) |

Verify:

```bash
rustc --version        # rustc 1.75+
python3 --version      # Python 3.13+
afl-clang-fast --version  # afl-cc
clang --version        # clang 14+
```

## Build

### Step 1: Build the fuzzer

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo build --release
```

Expected: `Compiling fuzzer v0.1.0` followed by `Finished release [optimized]`

### Step 2: Build harnesses for all target versions

```bash
cd harness/src
make build-all
```

This compiles three harness variants per SQLite version:
- `harness/afl/` — AFL-instrumented with ASan+UBSan (for fuzzing)
- `harness/test/` — ASan+UBSan without AFL (for crash triage)
- `harness/nosanit/` — no sanitizers (for production exploitability testing)

### Step 3: Verify build

```bash
./scripts/smoke_test.sh
```

Expected: `11/11 PASSED, 0 FAILED, 0 SKIPPED`

## Demo

### Generate SQL from Grammar

```bash
./target/release/generator -g grammars/active/sqlite_v3.py -t 10
```

Output: A random SQL statement (CREATE TABLE + INSERT + SELECT with window functions, CTEs, boundary values, etc.)

### Run a 2-minute Fuzzing Campaign

```bash
DURATION=120 ./scripts/run_eval.sh sqlite-3.31.1 demo_run
```

Output: Campaign starts, finds crashes within seconds, triage classifies them. Check results:

```bash
head -20 workdirs/sqlite-3.31.1_demo_run/exec.log          # execution log
find workdirs/sqlite-3.31.1_demo_run/outputs/signaled -type f | wc -l  # crash count
```

### Reproduce a Known Crash (CVE-2020-13434: integer overflow)

```bash
cd results/crashes/BC003_signed_integer_overflow_in_sqlite3_str_vappendf/1ca1c0159b42ae50
./reproduce.sh
```

Output: ASan reports `signed integer overflow` in `sqlite3_str_vappendf`.

### Change Hyperparameters

```bash
TIMEOUT_MS=1000 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 timeout_demo   # longer timeout
THREADS=2 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 threads_demo          # multi-threaded
MAX_TREE_SIZE=500 DURATION=60 ./scripts/run_eval.sh sqlite-3.31.1 tree_demo     # larger SQL
```

### Full Evaluation (from thesis Chapter 4)

```bash
# RQ1: CVE rediscovery (4 versions x 5 runs x 15 min = ~5 hours)
DURATION=900 ./scripts/run_campaigns_safe.sh

# RQ3: Grammar comparison (DBMS-Nautilus vs EBNF-Baseline)
DURATION=900 ./scripts/run_comparison.sh

# Generate statistics and figures
python3 scripts/ch4_pipeline.py
python3 scripts/generate_figures.py
```

## Repository Structure

```
├── fuzzer/          # Rust: fuzzer coordinator (main loop, state, config, queue)
├── grammartec/      # Rust: grammar engine (rules, trees, mutations, weighted sampling)
├── forksrv/         # Rust: AFL-compatible fork server
├── harness/         # C: SQLite harness with ASan/UBSan instrumentation
│   ├── src/         # Source code + Makefile
│   ├── afl/         # Compiled fuzzing harnesses (AFL-instrumented)
│   ├── test/        # Compiled triage harnesses (ASan+UBSan, no AFL)
│   └── nosanit/     # Compiled production harnesses (no sanitizers)
├── grammars/        # Python: grammar DSL files
│   ├── active/      # Current grammars (v3.4 with CVE seeds + v3.3 uniform)
│   └── baseline/    # EBNF baseline grammar (spec-derived)
├── triage/          # Python: crash classification pipeline
├── scripts/         # Bash+Python: evaluation orchestration
├── cve_builds/      # SQLite source code for each target version
├── results/         # Experimental data
│   ├── ch4_final/   # Thesis Chapter 4 CSVs (RQ1, RQ2, RQ3)
│   └── crashes/     # Crash evidence archive (trigger SQL, ASan output, reproduce scripts)
├── reference/       # Research papers, policy documents
├── docs/            # Documentation
│   ├── thesis/      # LaTeX thesis source + defense slides
│   ├── core/        # Technical documentation (architecture, grammar engine, triage)
│   └── defense/     # Defense demo preparation materials
└── README.md        # This file
```

## CVE Targets

| Version | CVEs | Bug Type |
|---------|------|----------|
| sqlite-3.30.1 | CVE-2019-19646 | Infinite loop (GENERATED ALWAYS AS + integrity_check) |
| sqlite-3.31.1 | CVE-2020-13434, CVE-2020-9327 | Integer overflow in printf, null pointer dereference |
| sqlite-3.32.0 | CVE-2020-13435 | NULL pointer dereference in equalString |
| sqlite-3.32.2 | CVE-2020-15358, CVE-2020-13871 | Heap buffer over-read, use-after-free |

See [docs/cve-list.md](docs/cve-list.md) for full PoC SQL and details.

## Key Results (thesis Chapter 4)

- **CVE rediscovery:** 4/4 target CVEs rediscovered without embedding PoC SQL
- **Bug classes:** 13 distinct bug classes found (9 unique to DBMS-Nautilus, 4 shared with baseline)
- **Root causes:** 108x more unique root causes per campaign (mean 205.6 vs 1.9)
- **TTFC:** ~1-2 seconds to first crash (no significant difference between grammars)
- **Throughput trade-off:** 52.1% lower throughput (90.8 vs 189.9 exec/s)
- **79 campaigns** total: 20 RQ1 + 20 RQ2 + 39 RQ3, each 15 minutes, N=5 runs
- **Grammar:** 520 structural primitive rules + 6 CVE seed rules = 526 total

## Architecture

```
Grammar (Python DSL) → PyO3 → Grammartec (weighted sampling, tree mutation)
                                    ↓
                              Fuzzer Core (multi-threaded coordination)
                                    ↓
                              Fork Server (AFL-compatible, shared memory bitmap)
                                    ↓
                              SQLite Harness (ASan + UBSan oracle)
                                    ↓
                              Triage Pipeline (dedup, classify, CVE signature match)
```

## Documentation

See [docs/README.md](docs/README.md) for the full documentation index.

| Document | Description |
|----------|-------------|
| [System Architecture](docs/core/architecture.md) | System design, component diagrams, data flow |
| [Grammar Engine](docs/core/grammar-engine.md) | Weight system, PyO3 bridge, rule selection |
| [Coverage & Mutation Loop](docs/core/coverage-loop.md) | Bitmap feedback, queue management, mutation strategies |
| [Triage Pipeline](docs/core/triage-pipeline.md) | Crash classification, dedup, CVE signatures |
| [Build & Run](docs/core/build-and-run.md) | Build prereqs, harness compilation, config reference |
| [CVE List](docs/cve-list.md) | CVE targets with PoC SQL and harness status |
| [CHANGELOG](CHANGELOG.md) | Project-level changelog |

## License

See [LICENSE.md](LICENSE.md).
