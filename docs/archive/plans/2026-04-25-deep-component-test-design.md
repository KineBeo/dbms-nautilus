# Deep Component Test — Design Spec

**Date:** 2026-04-25
**Goal:** Prove every major component of RL-Nautilus actually works with concrete evidence. Two deliverables: (1) add strategy labels to exec.log, (2) a diagnostic bash script that runs a 90s campaign and produces a detailed per-component health report.

---

## Deliverables

### D1: Enriched Exec Logging (keep permanently)

**File:** `fuzzer/src/fuzzer.rs`

Add `ExecutionReason` label to all `exec_logger.log()` calls inside `run_on()`. The `exec_reason` parameter is already passed through the call chain but never written to the log.

**Current format:**
```
1042	NEW_COV	SELECT count(*)...
1187	ASAN(223)	CREATE TABLE x...
```

**New format:**
```
1042	Havoc:NEW_COV	SELECT count(*)...
1187	Splice:ASAN(223)	CREATE TABLE x...
1350	Det:NEW_COV	SELECT DISTINCT...
2001	Gen:TIMEOUT	WITH RECURSIVE...
```

**Implementation:** Add a helper method or match arm that converts `ExecutionReason` to a string prefix (`Havoc`, `HavocRec`, `Min`, `MinRec`, `Splice`, `Det`, `Gen`), then prepend it to the event label in each `exec_logger.log()` call within `run_on()`.

There are 5 logging sites in `run_on()` (fuzzer.rs:188-297):
1. Line ~369: `ASAN(223)` → `{strategy}:ASAN(223)`
2. Line ~372: `UBSAN(1)` → `{strategy}:UBSAN(1)`
3. Line ~375: `SIGNAL({sig})` → `{strategy}:SIGNAL({sig})`
4. Line ~379: `TIMEOUT` → `{strategy}:TIMEOUT`
5. Line ~395: `NEW_COV` → `{strategy}:NEW_COV`

Also need a `fn reason_label(r: &ExecutionReason) -> &'static str` helper:
```rust
fn reason_label(r: &ExecutionReason) -> &'static str {
    match r {
        ExecutionReason::Havoc => "Havoc",
        ExecutionReason::HavocRec => "HavocRec",
        ExecutionReason::Min => "Min",
        ExecutionReason::MinRec => "MinRec",
        ExecutionReason::Splice => "Splice",
        ExecutionReason::Det => "Det",
        ExecutionReason::Gen => "Gen",
    }
}
```

**Rebuild required:** `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo build --release`

---

### D2: Deep Test Script

**File:** `scripts/deep_test.sh`

A single bash script that:
1. Runs a 90-second fuzzing campaign with enriched logging
2. Parses `exec.log` and output directories
3. Produces a detailed component health report

#### Phase 1: Campaign (90s)

Create a temp workdir, write a `config.ron`, run:
```
timeout 90 ./target/release/fuzzer -c <config> >/dev/null 2>&1
```

Config: 1 thread, sqlite_patterns.py grammar, sqlite_harness_patterns_sqlite-3.31.1, timeout 500ms, bitmap 65536, max_tree_size 1000.

#### Phase 2: Report

Parse `exec.log` and output directories. 7 report sections:

**S1–S5: Mutation Strategies (one per strategy)**

For each of Havoc, HavocRec, Splice, Det, Gen:
- grep `{Strategy}:NEW_COV` in exec.log
- Count occurrences
- Extract first example SQL snippet (the third tab-separated field)
- Print count + example
- Verdict: `VERIFIED` if count > 0, `NOT OBSERVED` if count = 0

**S6: Coverage Feedback**

- Count total `NEW_COV` lines in exec.log (any strategy)
- Count files in `outputs/queue/`
- Count files in `outputs/chunks/`
- Check that queue file count > 0 (proves bitmap → queue pipeline works)
- Check that chunks file count > 0 (proves ChunkStore is populated)
- Verdict: `VERIFIED` if both > 0

**S7: Crash Detection**

- Count files in `outputs/signaled/`
- grep for `ASAN\|UBSAN\|SIGNAL` in exec.log
- If any crashes found: print count + first example → `VERIFIED`
- If no crashes: `NOT OBSERVED (0 crashes in 90s — normal for short runs)`

This is NOT a failure — 90 seconds is often too short to trigger CVEs. The important thing is that the crash detection *pipeline* is wired up (which we know from T06-T09 in smoke_test.sh).

#### Report Format

```
===============================================================
 RL-Nautilus Deep Component Test — Diagnostic Report
 Campaign: 90s, 1 thread, sqlite-3.31.1
 Workdir: /tmp/deep_XXXXXX
===============================================================

--- S1: HAVOC MUTATION ---
New coverage events: 23
Example: SELECT count(*) FROM t1 WHERE x IN (SELECT y FROM t2)
Verdict: VERIFIED

--- S2: HAVOC RECURSION ---
New coverage events: 5
Example: WITH RECURSIVE c(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM c...
Verdict: VERIFIED

--- S3: SPLICE MUTATION ---
New coverage events: 18
Example: CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT INTO p VALUES(1)
Verdict: VERIFIED

--- S4: DETERMINISTIC MUTATION ---
New coverage events: 41
Example: SELECT DISTINCT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b
Verdict: VERIFIED

--- S5: GENERATE (FRESH) ---
New coverage events: 12
Example: PRAGMA integrity_check; ANALYZE;
Verdict: VERIFIED

--- S6: COVERAGE FEEDBACK ---
Total NEW_COV events: 99
Queue files: 87 (inputs that found new paths)
Chunk files: 456 (subtrees harvested for splice)
Queue growth proves bitmap → new_bits() → queue.add() pipeline works.
Verdict: VERIFIED

--- S7: CRASH DETECTION ---
Signaled files: 0
Crash log entries: 0
NOT OBSERVED (0 crashes in 90s — normal for short runs)
The crash detection pipeline (ASan→exit 223→save) is wired correctly
per smoke_test.sh T06-T09.

===============================================================
 SUMMARY
===============================================================
Havoc .............. VERIFIED (23 new paths)
Havoc Recursion .... VERIFIED (5 new paths)
Splice ............. VERIFIED (18 new paths)
Deterministic ...... VERIFIED (41 new paths)
Generate ........... VERIFIED (12 new paths)
Coverage Feedback .. VERIFIED (99 events, 87 queue, 456 chunks)
Crash Detection .... NOT OBSERVED (expected for 90s)

Total exec.log lines: 103
Runtime: 90s
===============================================================
```

#### Exit Code

- Exit 0 if all 5 mutation strategies are VERIFIED and coverage feedback is VERIFIED
- Exit 1 if any mutation strategy shows NOT OBSERVED (this means a real bug — that strategy is silently broken)
- Crash Detection NOT OBSERVED does NOT cause exit 1 (it's expected for short runs)

---

## Non-Goals

- Does NOT test RL/DQN integration (that's Phase 3)
- Does NOT test the triage pipeline
- Does NOT require harness recompilation
- Does NOT modify the grammar or harness

---

## Runtime

- Rebuild: ~30 seconds
- Campaign: 90 seconds
- Parsing: ~5 seconds
- **Total: ~2 minutes**
