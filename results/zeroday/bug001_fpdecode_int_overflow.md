# Bug 001: Signed Integer Overflow in sqlite3FpDecode

**Date Found:** 2026-05-20 00:42 ICT
**SQLite Version:** 3.53.0 (latest stable, released 2025-05-09)
**Severity:** Medium (UBSan-detected, undefined behavior per C standard)
**CWE:** CWE-190 Integer Overflow

## Summary

Signed integer overflow in `sqlite3FpDecode()` at sqlite3.c:37790.
When `iRound` parameter is INT32_MIN (or wraps to it via INT32_MAX+1),
the subtraction `p->iDP - iRound` overflows `int` type.

## Minimal Trigger

```sql
SELECT fpdecode(1e308, 2147483648, 65536);
```

Also triggers with:
```sql
SELECT fpdecode(1e308, -2147483648, 1);
```

## UBSan Output

```
sqlite3.c:37790:21: runtime error: signed integer overflow:
  309 - -2147483648 cannot be represented in type 'int'
  #0 sqlite3FpDecode  sqlite3.c:37790:21
  #1 fpdecodeFunc     sqlite3.c:136844:3
  #2 sqlite3VdbeExec  sqlite3.c:105299:3
```

## Root Cause

File: sqlite3.c, line 37790:
```c
iRound = p->iDP - iRound;
```

When `iRound <= 0` (line 37789 check), this subtraction is performed.
If `iRound == INT32_MIN` (-2147483648), then `p->iDP - (-2147483648)`
overflows because the result exceeds INT32_MAX.

The `fpdecode()` SQL function (debug-only) passes the second argument
directly as `iRound` via `sqlite3_value_int()` which returns INT32_MIN
for out-of-range values.

## Impact Analysis

- `fpdecode()` is SQLITE_DEBUG only, so direct exploitation requires debug builds
- However, `sqlite3FpDecode()` is also called from `sqlite3VXPrintf()` (the
  production printf implementation). The printf path clips precision before
  calling FpDecode, so it appears safe — but the underlying function has UB.
- The integer overflow is UB per C11 §6.5/5. Compilers may optimize assuming
  no signed overflow, potentially causing unexpected behavior.

## Nosanit Behavior

No crash without sanitizers — the overflow wraps silently on typical platforms.

## Discovery Method

Grammar-based greybox fuzzing with Nautilus + grammar v4.0.
Found within first minute of Campaign 1 on SQLite 3.53.0.
The `fpdecode()` function and `Boundary-Int` boundary values were
both new additions in grammar v4.0, specifically targeting under-tested
code paths in recent SQLite versions.
