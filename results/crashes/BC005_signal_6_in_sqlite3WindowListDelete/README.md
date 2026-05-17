# BC005: signal_6_in_sqlite3WindowListDelete

**Severity:** MEDIUM
**Subtype:** signal-6
**Key function:** `sqlite3WindowListDelete`
**CVE:** none
**Versions affected:** 3.30.1
**Total crash count:** 13
**Unique hashes:** 4

## Error message

```
(none)
```

## Top frames (sample)

```
sqlite3WindowListDelete
clearSelect
sqlite3SelectDelete
sqlite3ExprDeleteNN
sqlite3ExprDeleteNN
```

## Crash hashes

- `24cb8086d4e4ccd4`
- `8bc28dd6c969fd49`
- `4a897df9e000b652`
- `0ec99606fd930d6c`
