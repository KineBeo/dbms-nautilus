# BC003: signed_integer_overflow_in_sqlite3_str_vappendf (CVE-2020-13434)

**Severity:** MEDIUM
**Subtype:** signed-integer-overflow
**Key function:** `sqlite3_str_vappendf`
**CVE:** CVE-2020-13434
**Versions affected:** 3.30.1, 3.31.1, 3.32.0
**Total crash count:** 1729
**Unique hashes:** 6

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
sqlite3_str_vappendf
sqlite3_str_appendf
printfFunc
sqlite3VdbeExec
```

## Crash hashes

- `767f16fdfbae8ba1`
- `1ca1c0159b42ae50`
- `b43f365a68048314`
- `7264a343681aca95`
- `44c6c886cff47bba`
- `937a301147a0c985`
