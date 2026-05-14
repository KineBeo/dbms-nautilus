# Triage Pipeline

Exit-code classification, stack-based deduplication, CVE signature matching, fidelity scoring, and crash minimization.

> Last updated: 2026-05-14. Function names refer to code in `triage/` at the time of writing.

---

## 1. Crash Classification (Step 7)

The exit code from `WaitStatus::from_raw()` in the fuzzer is wrapped in an
`ExitReason` (defined in `forksrv/src/exitreason.rs`). The `run_on()` function
in `fuzzer/src/fuzzer.rs` routes each result:

| ExitReason variant | Condition | `is_crash` | Output path |
|----|----|----|-----|
| `Normal(223)` | ASan exit (set by `ASAN_OPTIONS=exitcode=223`) | true | `outputs/signaled/ASAN_{exec_count}_{thread}` |
| `Normal(1)` | UBSan exit (set by `UBSAN_OPTIONS=exitcode=1`) | true | `outputs/signaled/UBSAN_{exec_count}_{thread}` |
| `Signaled(sig)` | UNIX signal (e.g., SIGABRT=6 for SQLite debug assert) | true | `outputs/signaled/{sig}_{exec_count}` |
| `Timeouted` | `st_out.read_i32()` times out; process killed with SIGKILL | false | `outputs/timeout/{exec_count}` |
| `Normal(n)` (other) | Clean exit | false | (none — coverage bits checked) |
| `Stopped(sig)` | Process stopped (ptrace, rare) | false | Silently ignored |

The `is_crash` flag selects which of the two global bitmaps is compared
against when checking for new coverage paths.

Per-crash log entry: `ExecLogger::log()` in `fuzzer/src/fuzzer.rs` appends a
tab-separated line to `$WORKDIR/exec.log`:
`exec_count TAB label TAB rule_tag TAB sql_snippet`. Log rotates at 10 MiB
(`EXEC_LOG_SIZE_LIMIT`).

---

## 2. Triage Entry Point

`triage/classify.py` is the main triage script. It runs after the fuzzer exits
(invoked by `scripts/run_eval.sh`).

```bash
python3 triage/classify.py <workdir> --harness <path>
```

The `triage()` function in `classify.py`:

1. Scans `$WORKDIR/outputs/signaled/` for crash files.
2. Calls `process_crash(harness, crash_file)` on each file — replays the crash
   under the triage harness to capture stderr, then classifies the result.
3. Calls `build_clusters(results)` to group crashes by stack hash.
4. Writes three outputs: `triage.json`, `triage_report.md`, and `dedup/`.
5. Optionally enriches a `campaign.json` with crash classification counts via
   `enrich_campaign_json()`.

---

## 3. Exit Code Classification in classify.py

`classify_crash(exit_code, stderr)` in `triage/classify.py` re-classifies each
crash after replay:

| Condition | `crash_type` | `subtype` |
|---|---|---|
| `"runtime error:"` in stderr | `ubsan` | `signed-integer-overflow`, `null-pointer`, `misaligned-access`, `float-cast-overflow`, `shift-exponent`, `null-member-access`, or `ubsan-other` |
| exit code 223 | `asan` | `heap-buffer-overflow`, `stack-buffer-overflow`, `use-after-free`, `null-dereference`, or `asan-other` |
| exit code 1 | `ubsan` | `ubsan-other` |
| exit code -1 | `timeout` | (none) |
| exit code -5 | `debug_assert` | (none) |
| exit code < 0 | `signal` | `signal-{abs(exit_code)}` |
| exit code 0 | `debug_assert` | (none) |

---

## 4. Stack Deduplication

### In classify.py

`process_crash()` calls `extract_frames(stderr, max_frames=5)`, which parses
ASan/UBSan stack frames matching `#N 0x... in <func>`. For UBSan inline
errors, the `"runtime error:"` line itself is captured as a frame.

`_hash_frames(frames)` computes `sha256(frames[:5])[:16]` as the stack hash.
`build_clusters(results)` groups `CrashResult` objects by `stack_hash`, sorts
by descending count, and returns `CrashCluster` objects.

When no stack frames are found (e.g., silent signal), a content hash of the
crash file bytes is used: `<no-stack-{sha256[:16]}>`.

### In stack_dedup.py (GDB-based)

`triage/stack_dedup.py` provides an alternative, deeper dedup that uses GDB
instead of stderr parsing:

`run_gdb_on_crash(harness, crash_file)` spawns:
```
gdb --batch --nx --ex "run {crash_file}" --ex "bt 5" --ex "quit" <harness>
```

`parse_gdb_bt(output)` extracts `function:file:line` tokens from GDB's `bt`
output. `filter_frames()` drops libc/asan/harness wrapper frames (matching
`_SKIP_PATTERNS`), retaining only SQLite-internal frames.

`hash_frames(frames)` produces a `sha256` of the joined filtered frames as the
root-cause identifier. This works for SIGTRAP from `SQLITE_DEBUG` asserts
because the assert still produces a `sqlite3.c` source-line signature.

`dedup_workdir(workdir, harness, output_path)` writes `dedup.json` with fields:
`total_crashes`, `unique_root_causes`, `clusters`.

---

## 5. CVE Signature Matching

`triage/cve_signatures.py` defines one signature per target CVE as a list of
labeled regex patterns. A SQL string matches a signature iff every pattern
finds at least one occurrence.

| CVE | Pattern name | Required structural patterns |
|---|---|---|
| CVE-2020-15358 | `Pattern-P15358` | `CREATE VIEW ... ORDER BY`, `INTERSECT` in WHERE, implicit JOIN |
| CVE-2020-13871 | `Pattern-P13871` | `EXCEPT`, multi-column `ORDER BY`, scalar subquery |
| CVE-2020-13435 | `Pattern-P13435` | `NATURAL JOIN`, `coalesce()`, window function `OVER`, `UNIQUE`, `IN` subquery |
| CVE-2020-13434 | `Pattern-P13434-Boundary` | `printf()` call, INT32 boundary value (`±2147483647/8`) |
| CVE-2020-9327 | `Pattern-P9327` | `GENERATED ALWAYS AS`, `coalesce()`, JOIN, `CREATE VIEW` |
| CVE-2019-19646 | `Pattern-P19646` | `GENERATED ALWAYS AS`, `PRAGMA integrity_check` |

`missing_patterns(sql, signature)` returns the labels of patterns that do NOT
match — used for per-pattern coverage reporting.

---

## 6. Fidelity Scoring

`triage/fidelity_score.py` measures how well the grammar produces SQL that
structurally matches each CVE's required patterns.

`score_samples(samples, signature)` over N generated SQL strings:
- Counts samples where `missing_patterns()` returns an empty list (full match).
- Counts per-pattern misses.
- Returns `fidelity_score = match_count / N`.

`write_biased_grammar(base_grammar, out, target_pattern_nt, high_weight=100.0)`
rewrites `Sql-Stmt` rule weights in a temp grammar file to bias generation
100× toward the target pattern, setting all other `Sql-Stmt` alternatives to
weight 0.

`run_generator(grammar, samples)` invokes `./target/release/generator -g
<grammar> -t <tree_size> -n <samples>` and splits stdout into per-tree lines.

`score_all_patterns(grammar, samples)` loops over all CVE signatures, creates a
biased grammar for each, generates samples, scores them, and returns a combined
`fidelity-report.json`.

---

## 7. Crash Minimization

`triage/minimize.py` is a delta-debugging SQL minimizer.

```bash
python3 triage/minimize.py <crash_file> --harness <path> [--output <min_file>]
```

`minimize(crash_file, harness, output)` runs two phases:

**Phase 1 — Statement removal:** `split_statements(sql)` splits on `;`. For
each statement, tries removing it and checks if the crash still reproduces via
`same_crash()` (exit code must remain a crash; top stack frame must match).
Iterates until no further removal is possible.

**Phase 2 — Clause removal:** For each surviving statement, tries removing
`WHERE`, `ORDER BY`, `LIMIT`, `HAVING`, and `GROUP BY` clauses via regex
substitution (`CLAUSE_PATTERNS`). Keeps each removal if the crash still
reproduces with the same top frame.

`same_crash(frames_orig, exit_orig, frames_new, exit_new)` requires exit code
to remain a crash code (223, 1, or negative) and the top stack frame to match
`frames_orig[0]`.

---

## 8. Triage Outputs

| File | Location | Format |
|------|----------|--------|
| `triage.json` | `$WORKDIR/triage.json` | JSON: `total_crashes`, `unique_crashes`, `summary` by type, `crashes` array with hash/type/subtype/count/frames/sql_preview |
| `triage_report.md` | `$WORKDIR/triage_report.md` | Markdown: summary table + per-cluster section with stack trace and SQL preview |
| `dedup/` | `$WORKDIR/dedup/` | One file per unique crash site, named `{hash}_{original_filename}` |
| `dedup.json` | `$WORKDIR/dedup.json` | GDB-based dedup output (from `stack_dedup.py`) |
| `fidelity-report.json` | `docs/fidelity-report.json` | Per-pattern fidelity scores (from `fidelity_score.py`) |
