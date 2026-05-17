# BC008: null_pointer_in_sqlite3Atoi64

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `sqlite3Atoi64`
**CVE:** none
**Versions affected:** 3.30.1
**Total crash count:** 15
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:31024:27: runtime error: applying zero offset to null pointer
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:31024:27: runtime error: applying zero offset to null pointer
sqlite3Atoi64
memIntValue
sqlite3VdbeIntValue
sqlite3_value_int64
```

## Crash hashes

- `6e423265255b1822`
