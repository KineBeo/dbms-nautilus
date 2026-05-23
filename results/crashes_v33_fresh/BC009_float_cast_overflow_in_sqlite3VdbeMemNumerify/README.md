# BC009: float_cast_overflow_in_sqlite3VdbeMemNumerify

**Severity:** LOW
**Subtype:** float-cast-overflow
**Key function:** `sqlite3VdbeMemNumerify`
**CVE:** none
**Versions affected:** 3.32.2
**Total crash count:** 6
**Unique hashes:** 2

## Error message

```
../cve_builds/sqlite-3.32.2/sqlite3.c:76366:47: runtime error: 3.33233e+39 is outside the range of representable values of type 'long long'
```

## Top frames (sample)

```
../cve_builds/sqlite-3.32.2/sqlite3.c:76366:47: runtime error: 3.33233e+39 is outside the range of representable values of type 'long long'
sqlite3VdbeMemNumerify
sqlite3VdbeMemCast
sqlite3VdbeExec
sqlite3Step
```

## Crash hashes

- `378bf38a628a91c2`
- `c6968dbc81249da2`
