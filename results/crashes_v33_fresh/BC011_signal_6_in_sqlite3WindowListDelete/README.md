# BC011: signal_6_in_sqlite3WindowListDelete

**Severity:** MEDIUM
**Subtype:** signal-6
**Key function:** `sqlite3WindowListDelete`
**CVE:** none
**Versions affected:** 3.30.1
**Total crash count:** 5
**Unique hashes:** 2

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
sqlite3ExprDelete
```

## Crash hashes

- `4a897df9e000b652`
- `24cb8086d4e4ccd4`
