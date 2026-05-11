# RL-Nautilus: Grammar-Based Fuzzer with RL for CVE Discovery

Grammar-based coverage-guided fuzzer (Nautilus 2.0) enhanced with Reinforcement Learning for automated CVE discovery in SQLite. Fuzzes 4 CVE-bearing SQLite versions (3.30.1, 3.31.1, 3.32.0, 3.32.2) to compare weighted grammar sampling vs uniform sampling, then integrates a DQN agent for adaptive mutation strategies.

## Quick Start

### Prerequisites

- Rust toolchain (cargo)
- Python 3.13+ with dev headers
- AFL++ (`afl-clang-fast` on PATH)
- clang

### Build

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
cargo build --release
```

### Build a harness (example: sqlite-3.31.1)

```bash
cd harness
make TARGET=sqlite_harness_patterns_sqlite-3.31.1 SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c
```

### Run a 15-minute campaign

```bash
DURATION=900 ./scripts/run_eval.sh sqlite-3.31.1 my_run
```

### Run the full ablation (4 variants x 2 seeds)

```bash
DURATION=900 RUNS=2 TARGET=sqlite-3.31.1 ./scripts/run_ablation.sh
```

## Phase Status

| Phase | Status | Key Result |
|-------|--------|------------|
| Phase 1 — Infrastructure | Complete | Fork server, harnesses, grammar engine, oracle verified |
| Phase 2 — Attack grammar + measurement | Complete | TTFC ~1-2s; uniform > bandit on crash diversity (p~0.01) |
| Phase 3 — RL integration | Not started | DQN agent, MutationPolicy trait, runtime weight tuning |

## CVE Targets

| Version | CVEs | Type |
|---------|------|------|
| sqlite-3.30.1 | CVE-2019-19646 | Infinite loop |
| sqlite-3.31.1 | CVE-2020-13434, CVE-2020-9327 | Integer overflow, uninitialized ptr |
| sqlite-3.32.0 | CVE-2020-13435 | NULL ptr deref |
| sqlite-3.32.2 | CVE-2020-15358, CVE-2020-13871 | Heap read-past, use-after-free |

See [docs/cve-list.md](docs/cve-list.md) for full PoC SQL and details.

## Key Results (Phase 2)

- **Time-to-first-crash:** ~1-2 seconds across all versions and policies
- **Crash diversity:** Uniform sampling significantly outperforms bandit (p~0.01, Mann-Whitney U)
- **54 campaigns** completed: 3 versions x 2 policies x N=5, plus cross-version and smoke tests
- **Grammar v3.2:** 475 structural primitive rules covering all 6 CVE building blocks

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

See [docs/architecture.md](docs/architecture.md) for full system design with diagrams.

## Documentation

See [docs/README.md](docs/README.md) for the full documentation index.

| Document | Description |
|----------|-------------|
| [Architecture](docs/architecture.md) | System design, component diagrams, data flow |
| [Workflow Deep Dive](docs/workflow-deep-dive.md) | Fuzzer internals, execution loop, config reference |
| [Onboarding](docs/onboarding.md) | Build, install, run your first campaign |
| [CVE List](docs/cve-list.md) | CVE targets with PoC SQL and harness status |
| [CHANGELOG](CHANGELOG.md) | Project-level changelog |

## License

See [LICENSE.md](LICENSE.md).
