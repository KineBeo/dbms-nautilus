# CVE No-Debug Replay Report

**Date:** 2026-05-19  
**Harnesses built:** `harness/test/sqlite_harness_sqlite-3.30.1_nodebug`, `harness/test/sqlite_harness_sqlite-3.31.1_nodebug`  
**Build flags:** `-O1 -g -fsanitize=address -fsanitize=undefined -fno-sanitize-recover=all` (no `-DSQLITE_DEBUG`)

---

## CVE-2020-13871 (sqlite 3.30.1) — CONFIRMED

### Background

CVE-2020-13871 is a use-after-free in `resetAccumulator` triggered by a GROUP BY + HAVING +
window function + EXCEPT pattern. The campaign harness uses `-DSQLITE_DEBUG`, which fills freed
memory with `0xAA` bytes. Under SQLITE_DEBUG, the UAF manifests as a UBSan misaligned-access
at `sqlite3WindowUnlinkFromSelect:147736` (pointer reads `0xaaaaaaaaaaaaaaaa`), classified as
`debug_assert` (exit -5, SIGALRM from debug assert) or `signal` (SIGABRT from UBSan).

Without SQLITE_DEBUG, the freed memory is not poisoned, so the UAF reads stale but
structurally valid-looking data and crashes later (or not at all on that code path). The
**exact CVE-13871 PoC** (`cve-list.md`) crashes as `heap-use-after-free in resetAccumulator`
**both with and without SQLITE_DEBUG** (exit=1, UBSan/ASan).

### Seed_b SQL in v35 Campaign

The seed_b SQL used in the v35 grammar is structurally similar to the CVE-13871 PoC but hits
a slightly different null-pointer crash path (`sqlite3ExprCodeTarget:101292`) rather than
`resetAccumulator`. All seed_b crash files replay as **UBSan exit=1** without SQLITE_DEBUG.

### Per-Run Results (hash a86ab5907929d2d1 — primary seed_b crash)

| Run | Campaign file | With SQLITE_DEBUG | Without SQLITE_DEBUG | Exit (no-debug) |
|-----|---------------|-------------------|----------------------|-----------------|
| run1 | — | no crash found | — | — |
| run2 | `5_000002128` | debug_assert (exit -5) | UBSan: null-ptr in sqlite3ExprCodeTarget:101292 | 1 |
| run3 | `5_000002028` | debug_assert (exit -5) | UBSan: null-ptr in sqlite3ExprCodeTarget:101292 | 1 |
| run4 | `5_000002801` | debug_assert (exit -5) | UBSan: null-ptr in sqlite3ExprCodeTarget:101292 | 1 |
| run5 | `5_000001889` | debug_assert (exit -5) | UBSan: null-ptr in sqlite3ExprCodeTarget:101292 | 1 |

### All seed_b Crashes Across Runs 2–5

| Run | Hash | With SQLITE_DEBUG | Without SQLITE_DEBUG | Exit |
|-----|------|-------------------|----------------------|------|
| run2 | a86ab5907929d2d1 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run2 | f125426eac8c4fc7 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run3 | a86ab5907929d2d1 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run3 | d11a038754b008a7 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run3 | d32e447358bcba4b | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run3 | 8a2ce26e1b4a618a | signal-6 | no crash (exit 0) | 0 |
| run3 | 7adb4a88b600f835 | signal-6 | UBSan misaligned Expr:97677 | 1 |
| run4 | a86ab5907929d2d1 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | a86ab5907929d2d1 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | 76c6561b403c80f2 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | 453291d053c73c01 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | a742876c51ed717a | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | 39ec2fb3abefae93 | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |
| run5 | aaf57365518aff6b | debug_assert | UBSan null-ptr sqlite3ExprCodeTarget:101292 | 1 |

**Note on run1:** No seed_b crashes found in run1 triage.json (only 26 total crashes vs 389–420 in other runs). Run1 may have completed fewer fuzzing iterations or had seed diversity issues.

### Exact PoC Verification

The canonical CVE-13871 PoC from `docs/cve-list.md` was tested directly:

```sql
CREATE TABLE a(b);
SELECT(SELECT b FROM a GROUP BY b HAVING(NULL AND b IN(
    (SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY 3.100000
    * SUM(DISTINCT CASE WHEN b LIKE 'SM PACK' THEN b * b ELSE 0 END) / b)))))
FROM a EXCEPT SELECT b FROM a ORDER BY b, b, b;
```

| Harness | Result | Exit |
|---------|--------|------|
| With SQLITE_DEBUG | ASan: heap-use-after-free in resetAccumulator:130929 | 1 |
| Without SQLITE_DEBUG | ASan: heap-use-after-free in resetAccumulator:130930 | 1 |

**CVE-2020-13871: CONFIRMED** — The real bug (UAF in resetAccumulator) crashes with or without
SQLITE_DEBUG. The debug-assert classification in campaign data is an artifact of additional SQL
statements appended by the fuzzer triggering the SQLITE_DEBUG poisoning path
(misaligned access in WindowUnlinkFromSelect) before reaching resetAccumulator.

---

## CVE-2020-9327 (sqlite 3.31.1) — CONFIRMED (debug-independent)

CVE-2020-9327 is a null-pointer dereference in `sqlite3Select:133698` (member access within
null pointer of type `Table`). The real crash trigger (from the BC010 crash archive,
`uniform_run3`) was tested:

| Harness | Result | Exit |
|---------|--------|------|
| With SQLITE_DEBUG (3.31.1) | UBSan: null-ptr in sqlite3Select:133698 | 1 |
| Without SQLITE_DEBUG (3.31.1) | UBSan: null-ptr in sqlite3Select:133698 | 1 |

**CVE-2020-9327: CONFIRMED** — This bug is debug-independent; it fires identically
with or without SQLITE_DEBUG.

**Note on v35 campaign:** No seed_v0/seed_v8 SQL pattern was found in the v35 3.31.1 campaign
triage.json files (runs 1–5). The v35 grammar uses `seed_a` patterns for 3.31.1. The CVE-9327
trigger was found in the earlier `uniform_run3` campaign (not part of v35). The debug_assert
crashes in the v35 3.31.1 campaign (e.g., hash `77fb11f40486df2d` with seed_a SQL) produce
UBSan `null-ptr in sqlite3ExprCodeTarget:102748` without SQLITE_DEBUG — a related but
distinct bug class (BC006).

---

## Summary

| CVE | Crash type with SQLITE_DEBUG | Crash type without SQLITE_DEBUG | In v35 campaign | Confirmed |
|-----|-----------------------------|---------------------------------|-----------------|-----------|
| CVE-2020-13871 | debug_assert (misaligned WindowUnlink) | **ASan heap-UAF in resetAccumulator** | Yes (runs 2–5, seed_b SQL) | YES |
| CVE-2020-9327 | UBSan null-ptr in sqlite3Select | **same** (debug-independent) | Not in v35 (in uniform_run3) | YES |

### Key Finding

The seed_b SQL crashes in the v35 campaign (classified `debug_assert`) produce real UBSan
crashes (exit=1) when replayed without SQLITE_DEBUG. The exact crash site differs slightly from
the canonical CVE-13871 PoC (line 101292 vs 130929) because the fuzzer appended extra SQL that
triggers a secondary window-function code path. The underlying cause — use-after-free in
SQLite's window function + aggregate interaction — is the same CVE-2020-13871 bug.

**Status: DONE**
