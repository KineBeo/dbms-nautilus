# BC006: null_pointer_in_sqlite3ExprCodeTarget

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `sqlite3ExprCodeTarget`
**CVE:** none
**Versions affected:** 3.30.1, 3.31.1, 3.32.0
**Total crash count:** 2011
**Unique hashes:** 3

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16: runtime error: applying zero offset to null pointer
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16: runtime error: applying zero offset to null pointer
sqlite3ExprCodeTarget
sqlite3ExprCodeExprList
innerLoopLoadRow
selectInnerLoop
```

## Crash hashes

- `42302883be9cc977`
- `c3220eea4184cae8`
- `9411c5875a64a648`
