# BC007: misaligned_access_in_resetAccumulator

**Severity:** HIGH
**Subtype:** misaligned-access
**Key function:** `resetAccumulator`
**CVE:** none
**Versions affected:** 3.30.1
**Total crash count:** 13
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:130930:42: runtime error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList'), which requires 8 byte alignment
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:130930:42: runtime error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList'), which requires 8 byte alignment
resetAccumulator
sqlite3Select
sqlite3CodeSubselect
sqlite3ExprCodeTarget
```

## Crash hashes

- `186cc5604faecbe4`
