# BC002: misaligned_access_in_sqlite3WindowUnlinkFromSelect (CVE-2020-13871)

**Severity:** HIGH
**Subtype:** misaligned-access
**Key function:** `sqlite3WindowUnlinkFromSelect`
**CVE:** CVE-2020-13871
**Versions affected:** 3.30.1
**Total crash count:** 432
**Unique hashes:** 1

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:147736:5: runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which requires 8 byte alignment
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:147736:5: runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which requires 8 byte alignment
sqlite3WindowUnlinkFromSelect
sqlite3WindowDelete
sqlite3WindowListDelete
clearSelect
```

## Crash hashes

- `48cb7c287ece21f3`
