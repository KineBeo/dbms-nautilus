# BC008: misaligned_access_in_sqlite3ExprCodeTarget

**Severity:** HIGH
**Subtype:** misaligned-access
**Key function:** `sqlite3ExprCodeTarget`
**CVE:** none
**Versions affected:** 3.31.1
**Total crash count:** 13
**Unique hashes:** 13

## Error message

```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: member access within misaligned address 0x1ffffc020b93 for type 'struct AggInfo_func', which requires 8 byte alignment
```

## Top frames (sample)

```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: member access within misaligned address 0x1ffffc020b93 for type 'struct AggInfo_func', which requires 8 byte alignment
sqlite3ExprCodeTarget
sqlite3ExprCodeExprList
innerLoopLoadRow
selectInnerLoop
```

## Crash hashes

- `e4f1cdbc084cdca4`
- `9b23087d7bf066d3`
- `d0939087b0129f7d`
- `1bee57694ce6b107`
- `ea61d0701ef318e4`
- `a1436802e003bf8d`
- `7335fd423e7df525`
- `cafac669ab79177e`
- `2eeb0652db5806e4`
- `a4631f0826afe6b3`
- `6213cfc8effe111e`
- `c9339a11e91b8dd5`
- `dddede1eba6fce0f`
