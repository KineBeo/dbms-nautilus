# BC010: null_pointer_in_sqlite3Select (CVE-2020-9327)

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `sqlite3Select`
**CVE:** CVE-2020-9327
**Versions affected:** 3.31.1
**Total crash count:** 1
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.31.1/sqlite3.c:133698:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
```

## Top frames (sample)

```
../cve_builds/sqlite-3.31.1/sqlite3.c:133698:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
sqlite3Select
sqlite3CodeSubselect
sqlite3ExprCodeTarget
sqlite3ExprCodeTemp
```

## Crash hashes

- `2b1da72f9048599c`
