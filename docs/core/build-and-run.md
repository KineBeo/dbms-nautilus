# Build and Run

Cargo workspace, harness compilation, campaign lifecycle, and configuration reference.

> Last updated: 2026-05-14. Build commands and config field names refer to the repository at the time of writing.

---

## 1. Cargo Workspace

The repository uses a Cargo workspace defined at the root `Cargo.toml`:

```toml
[workspace]
members = ["forksrv", "grammartec", "fuzzer"]
default-members = ["fuzzer"]
```

Build order: `forksrv` → `grammartec` (depends on `forksrv`) → `fuzzer`
(depends on both).

Key dependency versions:

| Crate | Version | Role |
|-------|---------|------|
| `pyo3` | 0.21.2 | Python grammar bridge (requires `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` on Python 3.13) |
| `rand` / `rand_distr` | 0.8 / 0.4 | RNG, random sampling |
| `nix` | 0.17.0 | Fork/signal/pipe syscalls |
| `ron` | * | Config file deserialization |
| `loaded_dice` | 0.2 | Weighted sampling (grammartec dep; available but sampling now done via inline weighted scan) |
| `clap` | 2.33.1 | CLI argument parsing |

---

## 2. Build Prerequisites

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export PYTHONPATH=/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
cargo build --release
```

The `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` flag is required when building
against Python 3.13, which PyO3 0.21 does not natively support via ABI3.

---

## 3. Harness Compilation

The harness is a plain C file with AFL instrumentation. Pre-compiled binaries
are stored under `harness/afl/`:

```
harness/afl/sqlite_harness_sqlite-3.30.1
harness/afl/sqlite_harness_sqlite-3.31.1
harness/afl/sqlite_harness_sqlite-3.32.0
harness/afl/sqlite_harness_sqlite-3.32.2
```

Compilation uses `afl-clang-fast` (or `afl-clang`) with ASan+UBSan:

```bash
# harness/src/Makefile
afl-clang-fast -O1 -g \
    -fsanitize=address,undefined \
    -DSQLITE_HEADER=\"../cve_builds/sqlite-3.31.1/sqlite3.h\" \
    sqlite_harness.c ../cve_builds/sqlite-3.31.1/sqlite3.c \
    -o sqlite_harness_sqlite-3.31.1
```

AFL instrumentation injects edge-coverage hooks that write to the shared-memory
bitmap whose ID is passed via `__AFL_SHM_ID`. The `__AFL_INIT()` macro in
`sqlite_harness.c` connects the harness to the fork-server protocol on file
descriptors 198/199.

The `setup_db()` constructor (called before `main()`) pre-loads the schema:
tables `t1`, `t2`, `t3` (regular), `fts_t1` (FTS3), indices, and views.

---

## 4. AFL Fork-Server Handshake

`ForkServer::new()` in `forksrv/src/lib.rs` handles both AFL 2.x (simple
handshake, `hello == 0`) and AFL++ 4.x (extended protocol: XOR reply
`hello ^ 0xffffffff`, then capability u32 `FS_OPT_MAPSIZE`).

The startup timeout is 30 seconds (to accommodate ASan initialization latency);
subsequent per-run timeouts use `config.timeout_in_millis`.

---

## 5. Campaign Lifecycle

Entry point: `scripts/run_eval.sh <sqlite_version> [run_id]`

**Step 1 — Resolve paths.**
The script checks that the harness binary at
`$ROOT/harness/afl/sqlite_harness_${VERSION}` exists. If not, it prints the
`make` command needed to build it and exits.

**Step 2 — Write `config.ron`.**
A `config.ron` is written to `$WORKDIR/${VERSION}_${RUN_ID}/config.ron`.
Key values are templated from environment variables (`THREADS`, `TIMEOUT_MS`,
`MAX_TREE_SIZE`, etc.).

**Step 3 — Set environment variables.**
`run_eval.sh` exports:
- `ASAN_OPTIONS=exitcode=223,abort_on_error=1,detect_leaks=0`
- `UBSAN_OPTIONS=halt_on_error=1,exitcode=1`
- `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1`
- `LD_LIBRARY_PATH` (linuxbrew lib path for Python shared objects)

**Step 4 — Launch the fuzzer.**
```bash
timeout "$DURATION" ./target/release/fuzzer -c "$CONFIG"
```

**Step 5 — Workdir structure.**
`main.rs` creates four subdirectories under `$WORKDIR`:

| Path | Contents |
|------|----------|
| `outputs/signaled/` | ASan, UBSan, and signal crashes |
| `outputs/queue/` | All queue entries (raw SQL text, named by id and ExitReason) |
| `outputs/timeout/` | Timed-out inputs |
| `outputs/chunks/` | Chunkstore serialisation (used by Splice) |

**Step 6 — Post-run triage.**
After the fuzzer exits:
1. `scripts/capture_coverage.py` — writes `$WORKDIR/coverage.json`.
2. `triage/classify.py` — classifies and deduplicates crashes; writes
   `$WORKDIR/triage.json` and `$WORKDIR/triage_report.md`.
3. `scripts/archive_campaign.sh` — (only when `$GRAMMAR_VERSION` is set)
   copies results to `results/campaigns/`.

---

## 6. Configuration Reference

All fields are defined in `fuzzer/src/config.rs`. Fields marked with
`#[serde(default)]` are optional and backward-compatible with older configs.

| Field | Type | Default | Purpose |
|---|---|---|---|
| `path_to_bin_target` | `String` | (required) | Absolute path to the instrumented harness binary |
| `arguments` | `Vec<String>` | (required) | CLI arguments passed to target; `"@@"` is replaced with the path to the temp input file |
| `path_to_grammar` | `String` | (required) | Path to Python (`.py`) grammar file |
| `path_to_workdir` | `String` | (required) | Existing directory for outputs, logs, and config; must exist before launch |
| `number_of_threads` | `u8` | (required) | Number of parallel fuzzing threads; each thread runs its own fork server |
| `timeout_in_millis` | `u64` | (required) | Per-execution timeout in milliseconds; reads exceeding this trigger `ExitReason::Timeouted` |
| `bitmap_size` | `usize` | (required) | AFL coverage bitmap size in bytes; must match `AFL_MAP_SIZE` and harness `MAP_SIZE`; campaigns use `2097152` (2 MiB) |
| `thread_size` | `usize` | (required) | Stack size per fuzzing thread in bytes; `4194304` = 4 MiB |
| `number_of_generate_inputs` | `u16` | (required) | How many `generate_random("START")` calls per idle round (when queue is empty) |
| `max_tree_size` | `usize` | (required) | Maximum grammar derivation tree node count; caps recursive tree growth |
| `number_of_deterministic_mutations` | `usize` | (required) | Number of full Det cycles (each cycle covers all tree nodes once); `1` is the standard setting |
| `policy` | `String` | `"uniform"` | Grammar weight policy (currently only `"uniform"` is used) |

---

## 7. Configuration Quick-Start

Standard campaign config (uniform policy, 1 thread):

```
Config(
    path_to_bin_target: "./harness/afl/sqlite_harness_sqlite-3.31.1",
    arguments: ["@@"],
    path_to_grammar: "./grammars/active/sqlite_v3.py",
    path_to_workdir: "/tmp/sqlite-3.31.1_run1",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 2097152,
    thread_size: 4194304,
    number_of_generate_inputs: 1000,
    max_tree_size: 300,
    number_of_deterministic_mutations: 1,
)
```

---

## 8. Comparison Runner

`scripts/run_campaigns_safe.sh` runs v3.4 vs EBNF comparison campaigns:

```bash
./scripts/run_campaigns_safe.sh
```

Runs 5 repeats × 4 SQLite versions × 2 grammars (v3.4 + EBNF baseline).
Results land in `results/campaigns/` for analysis with `scripts/consolidate_data.py` and `scripts/plot_comparison.py`.
