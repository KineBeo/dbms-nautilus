# BC006: null_pointer_in_isAuxiliaryVtabOperator

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `isAuxiliaryVtabOperator`
**CVE:** none
**Versions affected:** 3.31.1
**Total crash count:** 20
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
```

## Top frames (sample)

```
../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
isAuxiliaryVtabOperator
exprAnalyze
sqlite3WhereExprAnalyze
sqlite3WhereBegin
```

## Crash hashes

- `78bd3886e40881c5`
