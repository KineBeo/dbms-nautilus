# Crash Triage Report

**Total crashes:** 19  
**Unique crash sites:** 19  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 19 | 19 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `4a18bf30693e133d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037765`

```sql
SELECT fpdecode(1e308, 2147483648, -1);
```

---

## Crash 2: `4c34ca5f694c5013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046920`

```sql
SELECT fpdecode(-1e308, -2147483648, 2147483647);
```

---

## Crash 3: `ee633d9ffacb20d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054210`

```sql
SELECT fpdecode(-1.0, -2147483648, -9223372036854775808); PRAGMA integrity_check;
```

---

## Crash 4: `289231ee1d53553e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081375`

```sql
SELECT fpdecode(-1e308, 2147483648, 0); VACUUM INTO ':memory:';
```

---

## Crash 5: `8ea8b0d1328229c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106311`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); ALTER TABLE q RENAME TO r; SELECT fpdecode(1e308, 2147483648, -1);
```

---

## Crash 6: `8c6c914a22ed4093` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119996`

```sql
SELECT fpdecode(-1e308, -2147483648, 9223372036854775807);
```

---

## Crash 7: `0a9fb2cb6ab27596` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142805`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT DISTINCT random(), CURRENT_TIMESTAMP, FALSE, FALSE, TRUE, CURRENT_DATE, TRUE, CURRENT_TIMESTAMP FROM jsonb_each(
```

---

## Crash 8: `5b432c533ca18714` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158942`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT last_insert_rowid() FROM 
```

---

## Crash 9: `0ba4c35957b35021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163812`

```sql
SELECT concat(NULL, TRUE, (VALUES (CURRENT_TIMESTAMP)), NULL, rank() OVER (), TRUE, TRUE, FALSE); SELECT fpdecode(-1e308, -2147483648, 2147483647);
```

---

## Crash 10: `44548fd13bf2d01b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220356`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM t3 WHERE CURRENT_TIME LIKE FALSE ESCAPE NULL; SELECT fpdecode(1.0, -2147483648, -1);
```

---

## Crash 11: `55f4a652bcdfd4a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253934`

```sql
SELECT round(-1.0, 0); SELECT fpdecode(-1e308, -2147483648, 2147483647);
```

---

## Crash 12: `5e291bbdf551136f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254044`

```sql
PRAGMA integrity_check; SELECT fpdecode(-1e308, -2147483648, 2147483647);
```

---

## Crash 13: `2ff20dbf8b713fb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267586`

```sql
SELECT printf('%.*s', -1, 1e-308); SELECT fpdecode(-1e308, -2147483648, 2147483647);
```

---

## Crash 14: `2eb34cf52a4ecd47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000289888`

```sql
SELECT concat(2147483647, -9e999, '-'); SELECT fpdecode(1e308, 2147483648, -1);
```

---

## Crash 15: `a3f230f34f355a3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000315631`

```sql
SELECT printf('%.*g', 32767); SELECT fpdecode(1e308, 2147483648, -1);
```

---

## Crash 16: `d9552a95dc0326b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000315726`

```sql
REINDEX; SELECT fpdecode(1e308, 2147483648, -1);
```

---

## Crash 17: `fa46ffd3e26b3395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000336513`

```sql
PRAGMA quick_check; PRAGMA journal_mode=PERSIST; SELECT fpdecode(1e308, 2147483648, -1); PRAGMA journal_mode=TRUNCATE;
```

---

## Crash 18: `c2dc8491ec234024` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000336616`

```sql
PRAGMA quick_check; VACUUM INTO ':memory:'; SELECT fpdecode(1e308, 2147483648, -1); PRAGMA journal_mode=TRUNCATE;
```

---

## Crash 19: `ebb9d5c405513936` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000336622`

```sql
PRAGMA quick_check; PRAGMA page_size; SELECT fpdecode(1e308, 2147483648, -1); PRAGMA journal_mode=TRUNCATE;
```

---
