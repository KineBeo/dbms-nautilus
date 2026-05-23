# BC002: null_pointer_in_sqlite3Fts5GetTokenizer

**Severity:** HIGH
**Subtype:** null-pointer
**Key function:** `sqlite3Fts5GetTokenizer`
**CVE:** none
**Versions affected:** 3.30.1, 3.31.1, 3.32.0, 3.32.2
**Total crash count:** 832
**Unique hashes:** 4

## Error message

```
../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44: runtime error: applying non-zero offset 8 to null pointer
```

## Top frames (sample)

```
../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44: runtime error: applying non-zero offset 8 to null pointer
sqlite3Fts5GetTokenizer
fts5ConfigDefaultTokenizer
sqlite3Fts5ConfigParse
fts5InitVtab
```

## Crash hashes

- `b45ae061172ad4b5`
- `8e36b1ab15ffac2b`
- `18c7efd9c88d6c67`
- `a57b932b08c49ed6`
