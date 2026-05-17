# BC009: float_cast_overflow_in_sqlite3VdbeMemNumerify

**Severity:** LOW
**Subtype:** float-cast-overflow
**Key function:** `sqlite3VdbeMemNumerify`
**CVE:** none
**Versions affected:** 3.30.1, 3.32.0
**Total crash count:** 21
**Unique hashes:** 8

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:75399:47: runtime error: 3.33033e+31 is outside the range of representable values of type 'long long'
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:75399:47: runtime error: 3.33033e+31 is outside the range of representable values of type 'long long'
sqlite3VdbeMemNumerify
sqlite3VdbeMemCast
sqlite3VdbeExec
sqlite3Step
```

## Crash hashes

- `bac59134ef3dfd56`
- `d382ef495388025b`
- `8d5415552150a714`
- `5626c5f2bf880af1`
- `1ea15d624c4a515c`
- `835be844243f75b9`
- `cebcabaf18329332`
- `036cbb14b82d522f`
