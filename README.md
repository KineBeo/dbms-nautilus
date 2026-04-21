# RL-Nautilus: Grammar-Based Fuzzer with RL for CVE Discovery

**Last Updated:** 2026-03-10

A grammar-based coverage-guided fuzzer (Nautilus 2.0) enhanced with Reinforcement Learning for automated CVE discovery in SQLite. Fuzzes 8 CVE-bearing SQLite versions to compare weighted grammar sampling vs uniform sampling, then integrates a DQN agent for adaptive mutation strategies.

**Location:** `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus/`

---

## About Nautilus 2.0

Nautilus is a coverage-guided, grammar-based fuzzer. By specifying the grammar of semi-valid inputs, Nautilus performs complex mutations and uncovers more interesting test cases. For details on the research, see the [NDSS 2019 paper](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2018/12/17/NDSS19-Nautilus.pdf).

Version 2.0 improvements:
- AFL++ 4.x compatibility with XOR handshake
- Python-based grammar specification
- Non-context-free grammar support via Python scripts
- Binary protocol/format support
- Regex-based terminals for efficient search space reduction

---

## Project Architecture

| Component | Language | Lines | Purpose |
|-----------|----------|-------|---------|
| **fuzzer/** | Rust | 1,658 | Multi-threaded coordinator, state machine, mutation pipeline |
| **grammartec/** | Rust | 2,441 | Grammar engine, weighted sampling (loaded_dice), tree mutation |
| **forksrv/** | Rust | 570 | AFL-compatible fork server, shared memory bitmap, XOR handshake |
| **harness/sqlite_harness.c** | C | ~200 | AFL fork-server harness, pre-loaded schema, memory safety oracle (ASan/UBSan) |
| **harness/sqlite_harness_cve13434.c** | C | ~180 | CVE-2020-13434 targeted harness — pre-loads PoC schema with trigger |
| **grammars/sqlite.py** | Python | 842 | 3-layer grammar: EBNF base + CVE stress templates with weights |
| **scripts/run_eval.sh** | Bash | ~80 | Campaign launcher with environment variable control |
| **scripts/analyze.py** | Python | ~150 | Post-campaign analysis (TTFC, coverage, crash stats) |
| **triage/dedup.py** | Python | ~200 | Crash deduplication (exit code + content hash) |
| **triage/minimize.py** | Python | ~180 | SQL crash minimization |
| **triage/report.py** | Python | ~150 | Crash report generator |
| **cve_builds/** | C sources | — | 8 SQLite CVE-bearing versions (3.26.0 through 3.39.1) |

### Fuzzing Flow

```
Grammar (sqlite.py, 155 rules, 9 CVE templates)
    ↓
Weighted Sampling (loaded_dice O(1))
    ↓
Tree Mutation (Min, Det, Splice, Havoc)
    ↓
Unparse to SQL
    ↓
Fork Server (forksrv, AFL++ XOR handshake)
    ↓
Harness (sqlite_harness.c, :memory: DB, pre-loaded schema)
    ↓
Oracle (ASan/UBSan detection: exit 223/1/SIGNAL(5) = crash)
    ↓
Coverage Feedback (shared memory bitmap, 262KB)
    ↓
Queue / Crashes (outputs/{queue,signaled})
```

---

## Prerequisites

### Required Tools

- **Rust:** Stable toolchain (install via [rustup](https://rustup.rs/))
- **Python 3.x** with dev headers: `libpython3-dev` (Ubuntu) or equivalent
- **AFL++:** afl-clang-fast compiler (v4.x recommended)
- **Build tools:** clang, make, gcc

### System Check

```bash
# Verify Rust
rustc --version && cargo --version

# Verify Python dev headers
python3-config --includes

# Verify AFL++
afl-clang-fast --version

# Verify make
make --version
```

### Required Environment Variables

These must be set before building and running:

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
```

**Why these?**
- `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` — Allows PyO3 to use Python's stable ABI, avoiding version mismatches
- `LD_LIBRARY_PATH` — Path to Linuxbrew libraries (if installed; adjust for your system)

---

## Setup & Building

### 1. Build the Rust Fuzzer

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus

# Export required variables
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"

# Build release binary
cargo build --release

# Binary location: ./target/release/fuzzer
```

Expected output:
```
   Compiling grammartec v0.1.0
   Compiling forksrv v0.1.0
   ...
    Finished release [optimized] target(s) in 45s
```

### 2. Build AFL Harnesses

General harness for broad CVE discovery:

```bash
cd harness

# sqlite-3.31.1 (CVE-2020-13434, easy target)
make SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c \
     TARGET=sqlite_harness_sqlite-3.31.1

# sqlite-3.30.1 (CVE-2020-11655)
make SQLITE=../cve_builds/sqlite-3.30.1/sqlite3.c \
     TARGET=sqlite_harness_sqlite-3.30.1

# sqlite-3.32.2 (patched CVE-2020-13434; may target CVE-2020-15358)
make SQLITE=../cve_builds/sqlite-3.32.2/sqlite3.c \
     TARGET=sqlite_harness_sqlite-3.32.2
```

**For older versions** (sqlite-3.26.0, 3.27.2), add mremap fix:

```bash
make SQLITE=../cve_builds/sqlite-3.26.0/sqlite3.c \
     TARGET=sqlite_harness_sqlite-3.26.0 \
     EXTRA_CFLAGS="-DHAVE_MREMAP=0"

make SQLITE=../cve_builds/sqlite-3.27.2/sqlite3.c \
     TARGET=sqlite_harness_sqlite-3.27.2 \
     EXTRA_CFLAGS="-DHAVE_MREMAP=0"
```

**CVE-2020-13434 Targeted Harness** (pre-loads PoC schema + trigger for fast crash detection):

```bash
# Compiles both AFL and test variants
make cve13434-build \
     SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c \
     TARGET=sqlite_harness_cve13434_sqlite-3.31.1
```

Binary locations:
- General: `harness/sqlite_harness_sqlite-3.31.1`
- Targeted: `harness/sqlite_harness_cve13434_sqlite-3.31.1`

### 3. Verify Build

Quick smoke test (30s):

```bash
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"

mkdir -p /tmp/nautilus_smoke/outputs/{signaled,timeout,queue}

DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 smoke
```

Expected output:
```
[*] Execution Count: 1422
[*] Coverage: 137 NEW_COV
[*] Crashes: 0 SIG, 0 TIMEOUT
```

---

## Running a Campaign

### Basic Campaign (General Harness)

```bash
# 5-minute pilot
DURATION=300 ./scripts/run_eval.sh sqlite-3.31.1 pilot1

# 24-hour full campaign
DURATION=86400 ./scripts/run_eval.sh sqlite-3.31.1 full_run1
```

### CVE-2020-13434 Targeted Campaign

Uses pre-loaded PoC schema for faster crash detection:

```bash
# 5-minute targeted pilot
DURATION=300 HARNESS_SUFFIX=cve13434_ ./scripts/run_eval.sh sqlite-3.31.1 cve13434_pilot1

# 24-hour targeted campaign
DURATION=86400 HARNESS_SUFFIX=cve13434_ ./scripts/run_eval.sh sqlite-3.31.1 cve13434_24h
```

### Environment Variables for run_eval.sh

| Variable | Default | Description |
|----------|---------|-------------|
| `DURATION` | 86400 | Campaign duration in seconds (300 = 5min, 3600 = 1h, 86400 = 24h) |
| `HARNESS_SUFFIX` | (empty) | Prefix before version in harness name; use `cve13434_` for CVE-2020-13434 targeted harness |
| `WORKDIR_BASE` | `/tmp/nautilus_eval` | Base directory for output |
| `GRAMMAR` | `grammars/sqlite.py` | Grammar file path |
| `MAX_TREE_SIZE` | 300 | Nautilus max_tree_size (limit parse tree depth) |
| `TIMEOUT_MS` | 500 | Per-execution timeout in milliseconds |
| `THREADS` | 1 | Number of Nautilus fuzzer threads |

Example with custom settings:

```bash
DURATION=600 \
  THREADS=4 \
  TIMEOUT_MS=200 \
  MAX_TREE_SIZE=500 \
  WORKDIR_BASE=/mnt/fuzz_results \
  ./scripts/run_eval.sh sqlite-3.31.1 custom_run
```

### Output Structure

```
/tmp/nautilus_eval/sqlite-3.31.1_pilot1/
├── config.ron                 # Generated Nautilus config
├── grammar_weights.json       # Grammar rule weights snapshot
├── fuzzer_log.txt             # Fuzzer debug output
└── outputs/
    ├── signaled/              # Crash-triggering inputs (SIG exits)
    │   ├── id_000000
    │   ├── id_000001
    │   └── ...
    ├── timeout/               # Timeout inputs
    │   └── id_000000
    └── queue/                 # Coverage-increasing inputs (NEW_COV)
        ├── id_000000
        ├── id_000001
        └── ...
```

---

## Fuzzing Flow (In Detail)

### 1. Grammar Initialization

Nautilus reads `grammars/sqlite.py` (842 lines), which defines:
- **EBNF base rules** (155 total): SELECT, UPDATE, INSERT, CREATE, DELETE, DROP, ALTER, etc.
- **9 CVE stress templates** with elevated weights:
  - `PRINTF_BOUNDARY_STRESS` (weight 3.0) — CVE-2020-13434 printf precision overflow
  - `FTS_STRESS` (weight 3.5) — FTS3 full-text search bugs
  - `WINDOW_FUNC_STRESS` (weight 2.5) — Window function edge cases
  - `NESTED_SUBQUERY_STRESS` (weight 2.5) — Nested subquery optimizer bugs
  - `CTE_STRESS` (weight 2.5) — Common table expression bugs
  - Others: JSON, trigger, index, aggregate stress

Weights are sampled via `loaded_dice::Dice` (O(1) weighted random selection).

### 2. Input Generation

For each fuzzing iteration:

```
For each thread:
  1. Pick seed from queue or generate fresh
  2. Select mutation strategy (Det, Splice, Havoc, Min, ...)
  3. Mutate parse tree (merge, delete, duplicate subtrees)
  4. Unparse tree → SQL input (via ctx.script() for semantic rules)
  5. Write to temp file
  → Loop to fork server
```

### 3. Fork Server & Execution

`forksrv/src/lib.rs` implements AFL++ 4.x fork server protocol:

```
[Startup Handshake]
  1. Child: Execute __AFL_INIT() (fork server constructor)
  2. Parent: Read hello from status pipe (0x41464c00..0x41464cff = "AFL\x?")
  3. Parent: Send XOR reply (hello ^ 0xffffffff)
  4. Parent: Read capabilities u32
  → Ready to fuzzing loop

[Per-Execution Loop]
  1. Parent: Send run command
  2. Parent: Read child PID
  3. Child: reads input from argv[1] temp file
  4. Child: execve() → harness runs once, exits with status
  5. Parent: Read exit status + coverage bitmap from SHM
  6. Parent: Check: exit status = crash? (223, 1, SIGNAL(5))?
  → Report crash / queue item / ignore
```

**Key Fix (2026-03-06):**
- `argv[0]` prepend fix — ensures harness sees argc=2
- Removed `__AFL_LOOP(1000)` — fork-server mode only (not AFL persistent mode)

### 4. Oracle (Crash Detection)

Harness exits with:
- **Exit 223** — ASan detected memory error (configured via `ASAN_OPTIONS`)
- **Exit 1** — UBSan detected undefined behavior (configured via `UBSAN_OPTIONS`)
- **SIGNAL(5)** (SIGTRAP) — SQLite `SQLITE_DEBUG` assertion fired
- **SIGNAL(6)** (SIGABRT) — Abort from assert/malloc failure

All non-zero exits + signals → reported as crashes.

### 5. Coverage Feedback & Queue

Harness writes coverage bitmap (262KB shared memory) after each execution. Fuzzer:
- Compares bitmap to previous max
- If coverage increased (NEW_COV) → save input to `outputs/queue/`
- If execution resulted in crash → save to `outputs/signaled/`
- Use queue items as mutation seeds

### 6. Mutation Stages (per Nautilus)

After each queue item:
1. **Deterministic (Det)** — Byte flips, bitwise ops, arithmetic
2. **Havoc** — Random mutations (random tree mutations)
3. **Splice** — Combine two queue items
4. **Custom** — Python grammar rules (weighted sampling)

---

## Grammar Pipeline (cve2grammar → generated grammar)

As of 2026-04-21, phase-2 vendors `cve2grammar` as a git subtree at
`cve2grammar/`. The pipeline transforms Manuel Rigger's DBMS bugs corpus
into `grammars/sqlite_generated.py`, a Nautilus grammar of 42 crash-oracle
templates.

```
scrape (manuelrigger.at/dbms-bugs) → Bug DTOs
  → LLM-generalize (cve2grammar /generalize)
  → cache/generalizer/*.json (42 crash templates, content-addressed)
  → render (python3 -m cve2grammar.generalizer.render)
  → grammars/sqlite_generated.py
  → fuzzer (cargo run --release)
```

### Run the pipeline

```bash
make setup     # cargo build + ready cve2grammar (in-place, no pip install)
make grammar   # render grammars/sqlite_generated.py from 42 cache entries
make test      # cargo test + pytest cve2grammar/
```

### Grammar coexistence

Two grammars live in `grammars/`:

| Grammar | Origin | Rules | Status |
|---------|--------|-------|--------|
| `sqlite_patterns.py` | hand-crafted | ~99 non-terminals, base SQLite productions | production |
| `sqlite_generated.py` | cve2grammar | 42 `ctx.rule("Sql-Stmt", ...)` from crash bugs | incomplete — see below |

Both target the same `Sql-Stmt` top-level. Select at runtime via
`config.ron` → `path_to_grammar`.

### Known: generated grammar is not yet self-contained

`sqlite_generated.py` currently defines only `Sql-Stmt` and references 24
base non-terminals (`Table-Name`, `Col-Def`, `GenCol-Expr`, etc.) that
live in `sqlite_patterns.py`. Nautilus loads one grammar file per run, so
the generated file panics with `Broken Grammar` until composed with the
base grammar.

**Next step (separate task):** update `scripts/build_grammar.sh` to
prepend `sqlite_patterns.py` to the rendered output, producing a
self-contained ~900-line grammar file.

---

## Harness Architecture

### sqlite_harness.c (General)

Located at `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus/harness/sqlite_harness.c`

**Features:**
- **Mode:** AFL fork-server (NOT persistent/AFL_LOOP)
- **Database:** `:memory:` (in-RAM, no disk I/O latency)
- **Pre-loaded Schema:** Tables `t1`, `t2`, `t3`, `fts_t1` (FTS3), indices, views, triggers
- **Input:** SQL from temp file (argv[1])
- **Oracle:**
  - ASan crash → exit 223
  - UBSan crash → exit 1
  - SIGNAL(5) = `SQLITE_DEBUG` assert
  - Semantic errors (syntax, constraint violations) → ignored (exit 0)

**Environment Variables (configured in harness):**
```c
ASAN_OPTIONS=halt_on_error=0:abort_on_error=0:exit_code=223
UBSAN_OPTIONS=halt_on_error=0:abort_on_error=0:exit_code=1
```

### sqlite_harness_cve13434.c (CVE-2020-13434 Targeted)

Located at `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus/harness/sqlite_harness_cve13434.c`

**Difference:** Pre-loads exact CVE-2020-13434 PoC schema:
```sql
CREATE TABLE a(b);
CREATE TRIGGER c AFTER INSERT ON a BEGIN
  SELECT printf('%.*g', 2147483647, 0.01);
END;
INSERT INTO a VALUES(1);
```

This schema is inserted before fuzzer-generated SQL. Fuzzer can generate INSERT, UPDATE, or printf-based SQL to trigger the vulnerability.

**Why two harnesses?**
- **General** (sqlite_harness.c): Discovers multiple CVEs across all rule combinations
- **Targeted** (sqlite_harness_cve13434.c): Fast TTFC (time-to-first-crash) for known CVE patterns; high crash rate for prioritized testing

---

## Grammar Weight System

### How Weights Work

Each rule has a weight (float):

```python
# In grammars/sqlite.py
ctx.rule("START", "{SQL_STMT}", weight=1.0)           # Base rule
ctx.rule("START", "{PRINTF_BOUNDARY_STRESS}", weight=3.0)  # 3x more likely to sample
```

When unparsing, Nautilus uses `loaded_dice::Dice` (weighted random):
- Sample from rules with probabilities proportional to weights
- O(1) lookup via binary search on cumulative weights

### CVE Stress Template Weights

| Template | Weight | Target CVE |
|----------|--------|-----------|
| Printf-Boundary | 3.0 | CVE-2020-13434 (printf precision overflow) |
| FTS-Stress | 3.5 | FTS3 full-text search bugs |
| Window-Func | 2.5 | Window function optimizer bugs |
| Nested-Subquery | 2.5 | Subquery optimization crashes |
| CTE-Stress | 2.5 | Common table expression bugs |
| JSON-Stress | 2.0 | JSON function errors |
| Trigger-Stress | 2.0 | Trigger execution bugs |
| Index-Stress | 2.0 | Index corruption/bugs |
| Aggregate-Stress | 2.0 | Aggregate function bugs |

### Tuning Weights

If a target CVE is under-discovered, increase its template weight:

```python
# In grammars/sqlite.py, increase printf_boundary weight
ctx.rule("PRINTF_BOUNDARY_STRESS", "SELECT printf('%.*g', {LARGE_INT}, {FLOAT})", weight=1.0)
# From 3.0 to 5.0 if under-represented in crashes
```

Then rebuild and re-run campaign.

---

## Triage Pipeline

After a campaign completes, crash inputs need analysis:

### 1. Deduplicate Crashes

Group identical crashes by exit code + content hash:

```bash
python3 triage/dedup.py \
  /tmp/nautilus_eval/sqlite-3.31.1_pilot1 \
  --harness harness/sqlite_harness_sqlite-3.31.1 \
  --output /tmp/nautilus_eval/sqlite-3.31.1_pilot1/dedup
```

**Output:**
```
/tmp/nautilus_eval/sqlite-3.31.1_pilot1/dedup/
├── clusters/
│   ├── cluster_001_cve13434_printf/
│   │   ├── representative.sql
│   │   ├── count: 142
│   │   └── variants/
│   │       ├── crash_000
│   │       ├── crash_001
│   │       └── ...
│   └── cluster_002_cve11655_window/
└── summary.json
```

**Note on SIGNAL(5):** SIGTRAP from SQLite assertions has no stack trace. dedup.py uses SQL content hash; for semantic grouping, manual review of SQL patterns is needed.

### 2. Minimize Crashes

Extract minimal SQL that still triggers the crash:

```bash
python3 triage/minimize.py \
  /tmp/nautilus_eval/sqlite-3.31.1_pilot1/dedup/clusters/cluster_001_cve13434_printf/representative.sql \
  --harness harness/sqlite_harness_sqlite-3.31.1
```

**Output:**
```
Original:  SELECT printf('%.*g', 2147483647, 0.01); (125 bytes)
Minimized: SELECT printf('%.*g', 2147483647, 0.01); (125 bytes) — cannot reduce further
Crash: SIGNAL(5) — SQLite debug assert (stack offset 28528 in sqlite3_str_vappendf)
```

### 3. Generate Report

Summarize all crashes with metadata:

```bash
python3 triage/report.py \
  /tmp/nautilus_eval/sqlite-3.31.1_pilot1/dedup \
  --harness harness/sqlite_harness_sqlite-3.31.1 \
  --output /tmp/nautilus_eval/sqlite-3.31.1_pilot1/report.md
```

**Report format:**
```markdown
# Crash Report: sqlite-3.31.1_pilot1

## Summary
- Total crashes: 219
- Clusters: 15
- Dominant cluster: CVE-2020-13434 printf precision overflow (142 crashes, 65%)

## Clusters
### Cluster 1: CVE-2020-13434 (142 crashes)
- Representative: SELECT printf('%.*g', 2147483647, 0.01);
- Exit code: SIGNAL(5)
- First seen: 3.2 seconds
- SQL pattern: printf('%.*[gfe]', INT32_MAX or large int, float)

...
```

---

## CVE Targets & Build Status

### Pilot Evaluation Results (CVE-2020-13434, 5-minute campaign, 2026-03-09)

**Version:** sqlite-3.31.1 (general harness)
- **Executions:** 18,984 (~299 exec/sec with ASan+UBSan)
- **Crashes detected:** 219 (SIG exits, all CVE-2020-13434 variants)
- **Queue size:** 1,002 items (excellent coverage growth)
- **Timeouts:** 7 (normal)
- **Distinct printf patterns:** 15 variants (`%.*g`, `%.*f`, `%.*e`, `%-10s` with INT32_MAX args)

### All 8 CVE-Bearing Versions

| Version | Harness Built | CVE Target | Status | Notes |
|---------|--------------|------------|--------|-------|
| sqlite-3.26.0 | ❌ | CVE-2020-11655 variant | Pending | Use `-DHAVE_MREMAP=0` |
| sqlite-3.27.2 | ❌ | CVE-2020-11655 variant | Pending | Use `-DHAVE_MREMAP=0` |
| sqlite-3.30.1 | ✅ | CVE-2020-11655 (AggInfo window bug) | Ready | Hard target; no pilot yet |
| sqlite-3.31.1 | ✅ | CVE-2020-13434 (easy), CVE-2020-11655 (hard) | **Ready** | Pilot ✅ — 219 crashes in 5min |
| sqlite-3.32.2 | ✅ | Patched (both 13434 & 11655); try CVE-2020-15358 | Ready | May not crash for known CVEs |
| sqlite-3.32.3 | ❌ | CVE-2022-35737 or CVE-2020-15358 | Pending | Source available |
| sqlite-3.34.0 | ❌ | CVE-2022-35737 | Pending | Source available |
| sqlite-3.39.1 | ❌ | CVE-2022-35737 (INSERT INTO ... SELECT) | Pending | Source available |

**Recommended Pilot Sequence:**
1. ✅ sqlite-3.31.1 — CVE-2020-13434 (Easy, 5min: 219 crashes)
2. sqlite-3.39.1 — CVE-2022-35737 (Medium, 1h estimate)
3. sqlite-3.30.1 — CVE-2020-11655 (Hard, 24h estimate)

### CVE Descriptions

**CVE-2020-13434** (Precision Overflow in printf)
- Affects: SQLite 3.8.3 to 3.32.0 (fixed 3.32.1)
- Trigger: `SELECT printf('%.*g', 2147483647, 0.01)`
- Error: Signed integer overflow in `sqlite3_str_vappendf` (line 28528)
- UBSan exit code: 1
- Severity: Low (DoS only, no RCE)

**CVE-2020-11655** (AggInfo Window Bug)
- Affects: SQLite 3.8.0 to 3.31.1 (fixed 3.32.0)
- Trigger: Complex nested aggregate + window function queries
- Error: Out-of-bounds access to AggInfo array
- Signal: SIGTRAP (SQLITE_DEBUG assert)
- Severity: Medium (information disclosure possible)

**CVE-2022-35737** (INSERT INTO ... SELECT)
- Affects: SQLite 3.37.0 to 3.39.1
- Trigger: `INSERT INTO ... SELECT` with mismatched columns
- Error: Column index out of bounds
- Severity: Medium (constraint violation bypass)

---

## Configuration Reference

### config.ron (Generated by run_eval.sh)

```ron
Config(
    path_to_bin_target: "./harness/sqlite_harness_sqlite-3.31.1",
    arguments: ["@@"],
    path_to_grammar: "grammars/sqlite.py",
    path_to_workdir: "/tmp/nautilus_eval/sqlite-3.31.1_pilot1",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 262144,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 300,
    number_of_deterministic_mutations: 1,
    rl_enabled: false,
)
```

**Key fields:**

| Field | Default | Description |
|-------|---------|-------------|
| `path_to_bin_target` | `./harness/sqlite_harness_...` | Path to compiled AFL harness |
| `arguments` | `["@@"]` | `@@` = temp file path (AFL convention) |
| `path_to_grammar` | `grammars/sqlite.py` | Grammar specification file |
| `path_to_workdir` | `/tmp/nautilus_eval/...` | Output directory (created if missing) |
| `number_of_threads` | 1 | Concurrent fuzzer threads (1 = single-threaded) |
| `timeout_in_millis` | 500 | Per-execution timeout (ms) |
| `bitmap_size` | 262144 | Coverage bitmap size (256KB); must match harness |
| `thread_size` | 4194304 | Memory per thread (4MB) |
| `number_of_generate_inputs` | 100 | Initial seeds to generate |
| `max_tree_size` | 300 | Max parse tree depth (limit recursion) |
| `number_of_deterministic_mutations` | 1 | Deterministic mutation rounds per queue item |
| `rl_enabled` | false | RL agent enabled? (Phase 2 stub) |

---

## Known Issues & Troubleshooting

| Issue | Symptom | Fix |
|-------|---------|-----|
| Harness uses `__AFL_LOOP(1000)` | Deadlock, all timeouts | Remove `__AFL_LOOP`; use fork-server only mode (RESOLVED 2026-03-06) |
| argv[0] not set | `argc=1` in harness, all UBSAN(1) false positives | Prepend argv[0] in `forksrv/src/lib.rs` (RESOLVED 2026-03-06) |
| AFL++ 4.x XOR handshake timeout | Fork server restart loop, SHM exhaustion | Implement correct handshake in `forksrv/src/lib.rs` with startup timeout (RESOLVED) |
| sqlite-3.26.0, 3.27.2 mremap() | Compilation error on aarch64 | Add `-DHAVE_MREMAP=0` EXTRA_CFLAGS |
| SIGNAL(5) crashes no stack trace | Dedup by SQL pattern only | Manual review of SQL semantics or improve dedup heuristics |
| `PYO3_PYTHON` not set | Build fails with "python not found" | Set `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` instead |
| RL stub not implemented | `rl_enabled: true` has no effect | Phase 2 work; leave `rl_enabled: false` for now |

### Debugging a Failed Campaign

```bash
# Check fuzzer logs
tail -100 /tmp/nautilus_eval/sqlite-3.31.1_pilot1/fuzzer_log.txt

# Verify harness binary exists
ls -lh harness/sqlite_harness_sqlite-3.31.1

# Test harness manually
echo "SELECT 1;" > /tmp/test.sql
./harness/sqlite_harness_sqlite-3.31.1 /tmp/test.sql
echo "Exit code: $?"

# Check coverage bitmap size
python3 -c "from forksrv import *; print('Bitmap OK')"

# Verify grammar loads
cargo run --bin generator -- -g grammars/sqlite.py -t 10
```

---

## Performance Tuning

### Execution Speed (exec/sec)

Baseline: 756 exec/sec (AFL fork server alone)
With ASan+UBSan overhead: 299 exec/sec (CVE-2020-13434 pilot)

**To improve:**
- **Reduce `timeout_in_millis`:** 500ms → 200ms (if harness is fast)
- **Increase `MAX_TREE_SIZE`:** Larger trees = more mutation, higher exec cost
- **Increase threads:** `THREADS=4` for 4-core systems
- **Use general harness:** Targeted harness (pre-loaded schema) slower than general

### Coverage Growth

If queue growth plateaus:
- **Increase mutation rounds:** `number_of_deterministic_mutations: 3`
- **Increase tree size:** `max_tree_size: 500`
- **Adjust weights:** Boost underrepresented CVE templates

### Crash Discovery

If crashes are rare:
- **Switch to targeted harness:** `HARNESS_SUFFIX=cve13434_`
- **Increase campaign duration:** 5min → 1h
- **Check grammar weights:** Ensure target CVE template weight > 2.0

---

## Verification Checklist

Before running a full campaign:

- [ ] Rust build succeeds: `cargo build --release`
- [ ] Python 3 headers installed: `python3-config --includes`
- [ ] AFL++ afl-clang-fast available: `afl-clang-fast --version`
- [ ] Harness compiles: `make SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1`
- [ ] Harness runs: `./harness/sqlite_harness_sqlite-3.31.1 /tmp/test.sql` (exit 0 on `SELECT 1;`)
- [ ] Grammar loads: `cargo run --bin generator -- -g grammars/sqlite.py -t 10` (produces SQL)
- [ ] Smoke test passes: `DURATION=30 ./scripts/run_eval.sh sqlite-3.31.1 smoke` (Execution Count > 0)
- [ ] Output directory created: `ls -d /tmp/nautilus_eval/sqlite-3.31.1_smoke`

---

## Quick Start

**5-minute pilot on CVE-2020-13434:**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus

# 1. Set environment
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"

# 2. Build Rust fuzzer
cargo build --release

# 3. Build harness (if not already built)
cd harness
make SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1
cd ..

# 4. Run pilot campaign
DURATION=300 ./scripts/run_eval.sh sqlite-3.31.1 cve13434_pilot1

# 5. Analyze results
python3 scripts/analyze.py /tmp/nautilus_eval/sqlite-3.31.1_cve13434_pilot1

# 6. Deduplicate crashes
python3 triage/dedup.py \
  /tmp/nautilus_eval/sqlite-3.31.1_cve13434_pilot1 \
  --harness harness/sqlite_harness_sqlite-3.31.1 \
  --output /tmp/nautilus_eval/sqlite-3.31.1_cve13434_pilot1/dedup
```

Expected results:
```
Execution Count:    ~18,984
Coverage:           ~1,002 queue items
Crashes:            ~219 SIG crashes (all CVE-2020-13434)
TTFC:               ~3.2 seconds
```

---

## References

- **Nautilus NDSS 2019 Paper:** https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2018/12/17/NDSS19-Nautilus.pdf
- **AFL++ Documentation:** https://github.com/AFLplusplus/AFLplusplus
- **SQLite CVE Archive:** https://www.cvedetails.com/vulnerability-list/vendor_id-9047/product_id-13418/
- **PyO3 Guide:** https://pyo3.rs/

---

**Project Status:** Phase 1 (Infrastructure) in progress — 3 of 8 harnesses built, pilot eval complete for CVE-2020-13434, remaining harnesses pending.

**Last Tested:** 2026-03-10 — Pilot campaign verified (18,984 execs, 219 crashes, 1,002 queue items).
