# BC007: null_pointer_in_sqlite3AtoF

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `sqlite3AtoF`
**CVE:** none
**Versions affected:** 3.30.1
**Total crash count:** 29
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:30783:24: runtime error: applying zero offset to null pointer
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:30783:24: runtime error: applying zero offset to null pointer
sqlite3AtoF
memRealValue
sqlite3VdbeRealValue
sqlite3VdbeBooleanValue
```

## Crash hashes

- `12d200e049b15130`
