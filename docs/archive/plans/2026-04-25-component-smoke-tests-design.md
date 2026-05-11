# Component Smoke Tests — Design Spec

**Date:** 2026-04-25
**Goal:** A single bash script (`scripts/smoke_test.sh`) that validates every component from Ch.4–15 of `docs/system-guide.md` actually works as documented. Quick to run (<2 min without the integration campaign), zero extra dependencies.

---

## Deliverable

One file: `scripts/smoke_test.sh`

- Runs 11 numbered tests, prints `PASS` / `FAIL` for each.
- Exits 0 if all pass, exits 1 if any fail.
- Uses only the existing release binaries (`generator`, `fuzzer`), the built harness, and standard CLI tools.
- Requires `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1` and correct `LD_LIBRARY_PATH` (script sets both).

---

## Tests

### T01: Grammar Loading

**What:** Load `grammars/sqlite_patterns.py` through the `generator` binary.
**How:** `generator -g grammars/sqlite_patterns.py -t 1`. If it exits 0 and produces non-empty output, the grammar loaded and `Context::initialize()` succeeded (calc_min_len didn't panic with "Broken Grammar").
**Pass:** Exit code 0 AND stdout is non-empty.

### T02: Tree Generation — Variety

**What:** Generate 50 trees and check they're not all identical (weighted sampling + random generation are working).
**How:** Run `generator -g grammars/sqlite_patterns.py -t 20` 50 times, collect outputs, count unique.
**Pass:** At least 40 of 50 outputs are unique (>80%).

### T03: Tree Generation — Validity

**What:** Generated SQL is syntactically reasonable (not garbage bytes).
**How:** From the 50 outputs above, check every output contains at least one SQL keyword (`SELECT`, `CREATE`, `INSERT`, `PRAGMA`, `WITH`, `VALUES`, `DROP`, `ALTER`, `EXPLAIN`, `ANALYZE`, `ATTACH`, `DELETE`, `UPDATE`).
**Pass:** 100% of outputs contain at least one SQL keyword.

### T04: Weighted Sampling Bias

**What:** High-weight rules are selected more often than low-weight rules.
**How:** Generate 200 trees at depth 5. Count occurrences of high-weight patterns (e.g., strings matching `printf\|WINDOW\|RECURSIVE\|INTERSECT\|EXCEPT\|integrity_check\|generated`) vs low-weight ones (e.g., `ATTACH\|DROP\|CREATE INDEX`). The grammar has Pattern-Boundary-Func at weight 3.0, Window-Func-Complex at 3.0, and Drop-Stmt at 0.2.
**Pass:** High-weight pattern count > low-weight pattern count. (If weights had no effect, they'd be roughly proportional to rule count, which favors neither.)

### T05: Mutation — Havoc (via Generator)

**What:** The generator with different `-t` (depth) values produces different-sized outputs, proving the tree generation budget system works.
**How:** Generate 10 trees at depth 5 and 10 at depth 50. Compare average output lengths.
**Pass:** Average length at depth 50 > 2× average length at depth 5.

### T06: Harness — Normal Exit

**What:** The harness exits 0 on valid SQL.
**How:** Write `SELECT 1;` to a temp file, run `harness/sqlite_harness_patterns_sqlite-3.31.1 <tmpfile>`.
**Pass:** Exit code = 0.

### T07: Harness — Error Tolerance

**What:** The harness exits 0 on invalid SQL (syntax errors are not crashes).
**How:** Write `THIS IS NOT SQL AT ALL !@#$` to a temp file, run the harness.
**Pass:** Exit code = 0 (harness handles errors gracefully, doesn't crash on bad SQL).

### T08: Harness — Signal Detection

**What:** Verify the harness can produce non-zero exit codes.
**How:** Write SQL that triggers a known issue. Try a few candidates:
  1. `SELECT printf('%.*c', 2147483647, 42);` (CVE-2020-13434 — integer overflow in printf)
  2. `SELECT zeroblob(2147483647);` (large allocation)
  3. A very deep recursive CTE that may stack-overflow

If none of these crash on 3.31.1, this test documents the finding as `SKIP` with explanation (the harness may not have ASan enabled, or the CVE needs different trigger conditions). This is itself a valuable diagnostic.
**Pass:** Either we get a non-zero exit code (proving crash detection works), or we get a documented `SKIP` explaining why.

### T09: Harness — Multi-Version

**What:** All 4 harness binaries are executable and respond to input.
**How:** For each of `sqlite-3.30.1`, `sqlite-3.31.1`, `sqlite-3.32.0`, `sqlite-3.32.2`: run `harness <tmpfile>` with `SELECT 1;`.
**Pass:** All 4 exit with code 0.

### T10: Fork Server + Coverage Bitmap

**What:** The fuzzer binary can start, connect to the fork server, and execute inputs.
**How:** Run the fuzzer for 10 seconds with 1 thread:
```
timeout 10 ./target/release/fuzzer \
  -c <temp_config.ron> \
  -g grammars/sqlite_patterns.py \
  -o /tmp/smoke_workdir \
  harness/sqlite_harness_patterns_sqlite-3.31.1 @@
```
Check that `exec.log` exists and has content (proving executions happened). Check that `outputs/queue/` has at least 1 file (proving new coverage was found and the bitmap works).
**Pass:** `exec.log` is non-empty AND `outputs/queue/` has ≥1 file.

### T11: Integration — 60-Second Campaign

**What:** Full end-to-end fuzzing campaign produces meaningful results.
**How:** Run the fuzzer for 60 seconds (extends T10's workdir or uses fresh one).
After the run, check:
  1. `exec.log` has >100 lines (executions are happening at reasonable speed)
  2. `outputs/queue/` has ≥5 files (coverage is being discovered)
  3. `outputs/chunks/` has ≥10 files (ChunkStore is being populated — splice will work)
  4. At least 2 different mutation strategies appear to have found bits (parse the fuzzer's stdout for "New paths found by" lines — capture last screen output before timeout)
**Pass:** All 4 checks pass.

---

## Config for T10/T11

The script creates a temporary `config.ron`:

```ron
Config(
    path_to_bin_target: "harness/sqlite_harness_patterns_sqlite-3.31.1",
    arguments: ["@@"],
    path_to_grammar: "grammars/sqlite_patterns.py",
    path_to_workdir: "/tmp/smoke_workdir",
    number_of_threads: 1,
    timeout_in_millis: 500,
    bitmap_size: 65536,
    thread_size: 4194304,
    number_of_generate_inputs: 100,
    max_tree_size: 1000,
    number_of_deterministic_mutations: 1,
)
```

---

## Output Format

```
=== RL-Nautilus Component Smoke Tests ===

[T01] Grammar Loading .................. PASS
[T02] Tree Generation — Variety ........ PASS
[T03] Tree Generation — Validity ....... PASS
[T04] Weighted Sampling Bias ........... PASS
[T05] Mutation Budget (depth effect) ... PASS
[T06] Harness — Normal Exit ............ PASS
[T07] Harness — Error Tolerance ........ PASS
[T08] Harness — Crash Detection ........ SKIP (no crash triggered on 3.31.1; see details above)
[T09] Harness — Multi-Version .......... PASS
[T10] Fork Server + Coverage (10s) ..... PASS
[T11] Integration Campaign (60s) ....... PASS

Result: 10/11 PASSED, 0 FAILED, 1 SKIPPED
```

---

## Non-Goals

- Does NOT fix the `NodeID: Step` compile error in grammartec tests.
- Does NOT test the RL/DQN integration (Phase 3 — not yet wired).
- Does NOT test the triage pipeline (`triage/`).
- Does NOT test the `cve2grammar/` subtree.
- Does NOT require recompilation of any binary.

---

## Runtime Estimate

- T01–T09: ~30 seconds total
- T10: 10 seconds
- T11: 60 seconds
- **Total: ~2 minutes**
