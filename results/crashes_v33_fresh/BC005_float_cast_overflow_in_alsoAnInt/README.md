# BC005: float_cast_overflow_in_alsoAnInt

**Severity:** LOW
**Subtype:** float-cast-overflow
**Key function:** `alsoAnInt`
**CVE:** none
**Versions affected:** 3.31.1, 3.32.0, 3.32.2
**Total crash count:** 21
**Unique hashes:** 10

## Error message

```
../cve_builds/sqlite-3.31.1/sqlite3.c:85071:16: runtime error: 1.11111e+37 is outside the range of representable values of type 'long long'
```

## Top frames (sample)

```
../cve_builds/sqlite-3.31.1/sqlite3.c:85071:16: runtime error: 1.11111e+37 is outside the range of representable values of type 'long long'
alsoAnInt
applyNumericAffinity
applyAffinity
sqlite3VdbeExec
```

## Crash hashes

- `7e847453d5f9a926`
- `f11ffd6c7a32fcf3`
- `675dce2802256a43`
- `9d7c1388cbe903ca`
- `a156622b9f5c75e9`
- `1e8f9bffc125d471`
- `082d290a01ade500`
- `86384c71790e7443`
- `1ae6577c1410311e`
- `e65d5e13d3831648`
