# Crash Triage Report

**Total crashes:** 51  
**Unique crash sites:** 51  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 51 | 51 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `430ed95bcea58f37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000451`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; SELECT p.*, CASE WHEN CURRENT_TIME = CURRENT_TIMESTAMP IS NULL THEN NULL END NOT IN (+CURRENT_TIMESTAMP, NULL) GL
```

---

## Crash 2: `be2df93ea1046cf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000668`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c2); INSERT INTO q (a) VALUES (CURRENT_TIME != TRUE ISNULL * CURRENT_TIMESTAMP) ON CONFLICT(_rowid_) DO UPDATE SET a = CAST(CURRENT_TI
```

---

## Crash 3: `1606e9a7e207c71c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000988`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT OR ABORT INTO p VALUES (NOT TRUE & CURRENT_TIMESTAMP, CASE WHEN CURRENT_DATE >> RAISE(IGNORE) TH
```

---

## Crash 4: `66976e954b3a001a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000994`

```sql
SELECT printf('%lld', -1, 'T-- - _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT char(CURRENT_DATE IN (NULL / TRUE)) FILTER (WHERE NULL GLOB NULL IS NOT NULL LIKE CURRENT_TIME % 
```

---

## Crash 5: `3aea3af167f9c6e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001164`

```sql
SELECT printf('%.*e', 2147483648, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); VALUES (TRUE < CASE WHEN TRUE THEN FALSE ELSE RAISE(IGNORE) NOT NULL END << CURRENT_TIME OR TRUE <
```

---

## Crash 6: `1873ab19c6dd30d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001209`

```sql
SELECT printf('%.*s', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO r VALUES (CASE CASE FALSE ISNULL WHEN FALSE >= CURRENT_DATE <> CURRENT_TIME LIK
```

---

## Crash 7: `94ceee0412bd1283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008128`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c2, _rowid_, c1, c1); WITH p (a, c1) AS NOT MATERIALIZED (SELECT (VALUES (FALSE, RAISE(IGNORE) COLLATE BINARY)), p.* UNION VALUES (CURRENT_T
```

---

## Crash 8: `abd31abc1ecf0c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008287`

```sql
SELECT printf('%llu', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO p VALUES (json_quote(EXISTS (SELECT * ORDER BY CURRENT_TIME DESC NULLS FI
```

---

## Crash 9: `3e9c208d349c5ab4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009294`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('[]') WHERE TRUE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 10: `fd92008944d16606` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016708`

```sql
SELECT printf('%.*g', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP NOT LIKE FALSE > FALSE IS NOT DISTINCT FROM
```

---

## Crash 11: `976bbeac47730871` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020694`

```sql
SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p SELECT * FROM q NOT INDEXED; PRAGMA integrity_check; SELECT hex(zeroblob(0));
```

---

## Crash 12: `c76d13eaed63519c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027668`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 13: `3b2b116dc6e9a4c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027679`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 14: `c67e6c569e322448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027788`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 15: `11b9e2eb55df729b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027819`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 16: `49d71e45b8e46383` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034801`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (FALSE) UNION VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 SELECT ALL *, * FROM json
```

---

## Crash 17: `8d8f184388724d57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037124`

```sql
SELECT substr('- lI-Us', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO q VALUES (+~NOT EXISTS (SELECT +CURRENT_TIME AS a, *, * FROM (SELECT 
```

---

## Crash 18: `dcdcaaef3523aced` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037327`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT unicode(FALSE <> TRUE COLLATE RTRIM -> TRUE REGEXP TRUE) FILTER (WHERE CASE NULL IS CURRENT_TIMESTAMP WHEN CURR
```

---

## Crash 19: `e827f5f1d20d7e7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037448`

```sql
SELECT printf('%.*s', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CASE FALSE COLLATE NOCASE WHEN CURRENT_TIME IS DISTINCT FROM TRUE IS NOT DISTINCT FROM FALSE GLOB C
```

---

## Crash 20: `47ec7ad8aadecd61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037480`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CASE FALSE COLLATE NOCASE WHEN CURRENT_TIME IS DISTINCT FROM TRUE IS NOT DISTINCT FROM FALSE GLOB CURRENT_TIME
```

---

## Crash 21: `79853bcb0dfd04f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039107`

```sql
SELECT printf('%f', -2147483648, ' lie'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); WITH RECURSIVE t1 (c1, c3, c1) AS NOT MATERIALIZED (SELECT * FROM q UNION SELECT CASE CURRENT_DATE
```

---

## Crash 22: `0f9698a5217ea42a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039939`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, b); INSERT INTO t3 DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); 
```

---

## Crash 23: `45de0a4e1c136da0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041326`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b); INSERT OR REPLACE INTO p VALUES (+NOT EXISTS (SE
```

---

## Crash 24: `8ec3de2fb572b372` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041832`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CAST(NULL AS FLOAT)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT TRUE - CURRENT_DATE == p.a & TRUE * TRUE IS NOT RAI
```

---

## Crash 25: `27c478b1f1e2594c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044467`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT TRUE FROM p WHERE CURRENT_TIME GROUP BY CURRENT_DATE ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE
```

---

## Crash 26: `e20bd7d08204272d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047311`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c3, c2, a); INSERT INTO q VALUES (printf('', CURRENT_TIMESTAMP COLLATE BINARY) FILTER (WHERE ~(NULL N
```

---

## Crash 27: `7b1ea20eae6329f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049215`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 28: `744cd2579011faa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050631`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t2 NOT INDEXED CROSS JOIN jsonb_each('{}') ON count(*) OVER (PARTITION BY RAISE(IGNORE) ORDER BY R
```

---

## Crash 29: `f03518ce632bb102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051846`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2); VALUES (CURRENT_TIMESTA
```

---

## Crash 30: `ec8dc893dfdb82ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053348`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES ((
```

---

## Crash 31: `a71c5fcf202a2ed8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053711`

```sql
SELECT printf('%x', 2147483647, '_jL5_w--2-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2); INSERT INTO q VALUES (CAST(TRUE NOTNULL <= FALSE ISNULL << CURRENT_TIMESTAMP IS NOT
```

---

## Crash 32: `e6a8695a62265219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054362`

```sql
SELECT round(1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); SELECT CASE WHEN CURRENT_DATE GLOB CURRENT_TIME THEN NULL ELSE CURRENT_DATE END >= CURRENT_TIME IS TRUE IS
```

---

## Crash 33: `ff1eaf0280da9852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062657`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT * FROM p WHERE NULL GROUP BY CURRENT_TIME ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 34: `9c090fdef5ef0ff9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066281`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); SELECT FALSE FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP HAVING TRUE NOT IN (SELECT FALSE FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP ORDER
```

---

## Crash 35: `9e38ac15b5f1144e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075373`

```sql
SELECT round(0.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c1); SELECT unicode(NOT EXISTS (WITH RECURSIVE p (c1, b) AS NOT MATERIALIZED (SELECT * EXCEPT SELECT CURRENT_
```

---

## Crash 36: `43e39b8fc33048fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 37: `c75f7f433da67b5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078955`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UN
```

---

## Crash 38: `326e844efc428f4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081555`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (FALSE) UNION VALUES (percent_rank() OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c3, c1, c1, c2, c3, c2); VALUES (
```

---

## Crash 39: `0b84b99694bea74d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081587`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (FALSE) UNION VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c3, c1, c1, c2, c3, c2); VALUES (CURRENT_DATE, RAIS
```

---

## Crash 40: `e64dd8f12d205868` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082142`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIMESTAMP COLLATE RTRIM); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, * FROM (SELECT json_array_lengt
```

---

## Crash 41: `d8277cd437a3286a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092819`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 42: `ddc86cc6fb9b6df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095697`

```sql
SELECT substr(' ee O-8_-pw_A_6x', -2147483648, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, * FROM jsonb_each('{}') , json_tree('{}') WHERE NULL COLLATE RTRIM GROUP
```

---

## Crash 43: `3ede29d3813cc14d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103524`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO q VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check
```

---

## Crash 44: `d6a0f261fd371d22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103727`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 45: `c1ee786d3067e91b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112829`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO s VALUES (CASE CU
```

---

## Crash 46: `fcad66f763cf5d3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113196`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (NULL) INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO t3 VALUES (CURRENT_TIME
```

---

## Crash 47: `4a9d2656c7e36f9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116284`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CURRENT_TIME IS NOT NULL)); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 48: `088b8a9c73b4245d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117036`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UN
```

---

## Crash 49: `66027e57e66d39f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118309`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM q NOT INDEXED LIMIT FALSE OFFSET NULL IS NOT NU
```

---

## Crash 50: `72e446d9d4b58b71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118359`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM q NOT INDEXED LIMIT FALSE OFFSET NULL IS NOT CU
```

---

## Crash 51: `35b5473361fdc7d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118724`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT CURRENT_DATE LIMIT CURRENT_TIME);
```

---
