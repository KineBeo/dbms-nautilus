# A1 Stack-Dedup Manual Verification

**Date:** 2026-04-22
**Workdir tested:** /tmp/nautilus_eval/sqlite-3.31.1_attack_run_3m
**Total crashes:** 12
**Unique root causes:** 2
**Harness:** `harness/sqlite_harness_patterns_sqlite-3.31.1`

## Result

| Cluster | Count | Top frame |
|---|---|---|
| 1 | 6 | `sqlite3_str_vappendf:sqlite3.c:28804` |
| 2 | 6 | `alsoAnInt:sqlite3.c:85071` |

## Plausibility judgment

Two genuine root causes, evenly split. Cluster 1 is the well-known CVE-2020-13434 printf precision-overflow path (`sqlite3_str_vappendf` line 28804 is the `%.*g` precision computation). Cluster 2 points at `alsoAnInt` in the VDBE layer — a distinct code path, likely triggered by the corpus's `hex(hex(hex(...)))` + large-int combinations. The split is consistent with the sampled SQL: cluster 1's representative uses `printf('%.*g', -2147483647, 0.01)` (classic 13434), cluster 2's uses `printf('abc', -2147483648, sum(DISTINCT hex(hex(...))))` (a different arithmetic path through `alsoAnInt`).

## Investigation that produced this result

The first A1 run returned `unique_root_causes=1` with `top_frame=<no-frame>` — gdb could not extract backtraces for any of the 12 crashes. Root cause of the tool failure:

1. The harness expects the crash filename as `argv[1]`, not stdin. The initial `gdb ... --ex "run < $crash"` was piping to stdin instead of passing the path.
2. LeakSanitizer aborts under ptrace by default, and the harness links LSan via ASan.

Fix applied to `triage/stack_dedup.py`:
- Changed `run < {crash}` → `run {crash}` (argv-style).
- Added `ASAN_OPTIONS=detect_leaks=0:abort_on_error=1` and `UBSAN_OPTIONS=abort_on_error=1` to the gdb subprocess environment.

Unit tests (8/8) still pass after the fix.
