# Crash Triage Report

**Total crashes:** 382  
**Unique crash sites:** 382  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 158 | 158 | 41% |
| Signal | 224 | 224 | 58% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `af60227d3143a9e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000102`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES (NULL >= RAISE(IGNORE) ISNULL IS NULL IS NOT NULL < (NULL LIKE FALSE << CURRENT_TIMESTAMP) IS NULL == +CURRENT_TIMESTAMP 
```

---

## Crash 2: `fa89834cd5d8a32a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000301`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, c3, c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT p.* FROM q WHERE ~CURRENT_DATE == TRUE COLLATE RTRIM IS CURRE
```

---

## Crash 3: `45bb4903d5e2616c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000546`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT FALSE COLLATE RTRIM AND RAISE(IGNORE) AS x3_, (CURRE
```

---

## Crash 4: `5a1d3ac152b955b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000610`

```sql
SELECT printf('%.*f', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT_DATE AND CURRENT_TIMESTAMP IN (SELECT *, *) AS a FROM t1 NATURAL JOIN s WHERE 
```

---

## Crash 5: `b397a242a61a7cd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000654`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 6: `ffb9938b9a23f3c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001160`

```sql
SELECT printf('%.*g', 2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c1); INSERT OR FAIL INTO q VALUES (+upper(FALSE) OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_TIMES
```

---

## Crash 7: `8aa56855e47d8ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001428`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c2, c1, a, _rowid_, c2); INSERT INTO q VALUES (CURRENT_TIME IS NULL - TRUE ISNULL + CURRENT_DATE <= NULL COLLATE RTRIM GLOB CURRENT_TIME IS 
```

---

## Crash 8: `6f08179f1f87e1d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001862`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 9: `6d1e4f865e0ce034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001879`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER
```

---

## Crash 10: `84bbaf041245a5b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002104`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE r (c3) AS (SELECT *) SELECT FALSE, * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 11: `364af1449cda6776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002117`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT *) SELECT FALSE, * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 12: `7704ccd79b810112` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME < TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = 
```

---

## Crash 13: `aa435f5cec131b3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 14: `253bb5361672a2ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004513`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 15: `f526ba1fe528ffa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004519`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 16: `e2b901e34aede640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004525`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 17: `bb15be6f303fa44a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004533`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 18: `9e65bd523df2e05d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004764`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1, c2); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a W
```

---

## Crash 19: `820b54060e9ebb91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005069`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 20: `cd02439b55f02014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005079`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 21: `a6cbb1ecee81f805` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005354`

```sql
SELECT substr('', 9223372036854775807, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELE
```

---

## Crash 22: `ee5412bd48d5948e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006387`

```sql
SELECT substr('_58w e-6 c_  u 4 ', -2147483649, -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((S
```

---

## Crash 23: `fff5e98ea93df419` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006617`

```sql
SELECT round(1e308, -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 24: `ba1cfd8796d85407` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006810`

```sql
SELECT substr('', 4294967296, -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 25: `829a24ccebcc845d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007050`

```sql
SELECT substr('', -9223372036854775808, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 26: `df329b8d323ad6ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007872`

```sql
SELECT printf('%llu', 2147483648, '_f-d L   '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 VALUES (CURRENT_DATE NOT LIKE CASE WHEN RAISE(IGNORE) THEN +0 | RAISE(IGNORE) E
```

---

## Crash 27: `94ab5b0eab8c4b66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007914`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(c3 BLOB, c3 GENERATED ALWAYS AS (c1) NOT NULL, c3 TEXT UNIQUE); INSERT INTO p VALUES (sum(CASE WHEN --CAST(CURRENT_TIME AS REAL) 
```

---

## Crash 28: `ffcd098be041bdc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008738`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME AS mk74; CREATE TABLE seed_a(c
```

---

## Crash 29: `2d1a479e22f95202` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008790`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); 
```

---

## Crash 30: `48adbb4c926886f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008803`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMES
```

---

## Crash 31: `6ab38727b17f7502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008868`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT '_W J Xn1-' NOTNULL ISNULL; CREATE TABLE se
```

---

## Crash 32: `02c290537e733168` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008978`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":1}') GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_a(c
```

---

## Crash 33: `11d19353afc04ca9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008984`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":1}') GROUP BY FALSE HAVING NULL; CREATE TABLE seed_a(c
```

---

## Crash 34: `91fe9b8c396ab293` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008990`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":1}') GROUP BY FALSE HAVING CURRENT_TIME; CREATE TABLE 
```

---

## Crash 35: `3245f00369482d5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009022`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('{"a":{"b":1}}') WHERE FALSE GROUP BY TRUE; CREA
```

---

## Crash 36: `56e290cb4eff1cea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009028`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE GROUP BY TRU
```

---

## Crash 37: `3a8df707865ef932` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009113`

```sql
SELECT printf('%.*s', -2147483648, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 38: `99c658567e4cc036` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009131`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP | TRUE), b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED; CREATE 
```

---

## Crash 39: `56888611a4eae1c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009182`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP | TRUE), b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CURRENT_TIME FROM json_tree('
```

---

## Crash 40: `068b4a086c43d6db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009683`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 41: `284a9c0a31f8f68d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011130`

```sql
SELECT printf('%.*g', -2147483648, 1.0); SELECT printf('%.*g', -2147483648, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (NOT EXISTS (VALUES (FALSE) INTERSECT 
```

---

## Crash 42: `976540be9da40ba9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012509`

```sql
SELECT printf('%.*d', 2147483648, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 43: `9c2f806d79359ace` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012518`

```sql
SELECT printf('%.*e', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 44: `c3d4a679920b4b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012524`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); WITH p AS (SELECT *) INSERT INTO p VALUES (CAST(TRUE AS REAL)); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 45: `060de180797bba30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012531`

```sql
SELECT printf('%.*f', -9223372036854775808, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 46: `12955b34fa6e3465` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012539`

```sql
SELECT substr('', 9223372036854775807, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 47: `416c912feab79922` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012545`

```sql
SELECT substr('', -9223372036854775808, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coal
```

---

## Crash 48: `9d04c79c87b91189` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012564`

```sql
SELECT round(-1e308, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 49: `1fd401893977e95e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012577`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); WITH s (rowid) AS (VALUES (RAISE(IGNORE))), t2 AS (VALUES (NULL)) INSERT INTO p VALUES (~FALSE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 50: `15ef2aeac16b4544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012583`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN se
```

---

## Crash 51: `8d9b5f6e4c33e889` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012589`

```sql
SELECT round(-1.0, 0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) F
```

---

## Crash 52: `5ac7274e5a016692` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012604`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL OR CURRENT_TIME) AS sub1;
```

---

## Crash 53: `2f5aea2108d86b30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012611`

```sql
SELECT printf('%.*e', 4294967296, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 54: `4d5ff2b4fc9e6cd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012626`

```sql
SELECT round(1.0, -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) F
```

---

## Crash 55: `84f50a6611b42642` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012637`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 56: `ec762fb602640dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012654`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 57: `7179ca6912fb14b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012665`

```sql
SELECT round(0.01, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 58: `9fd2161598b128c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012671`

```sql
SELECT printf('%.*s', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 59: `265565175b6edbec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012685`

```sql
SELECT printf('%.*s', 2147483648, 1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 60: `8379c274cde17b30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012694`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 61: `45b3c4e561f4306f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014464`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (TRUE)); INSERT INTO p VALUES (CURRENT_DATE); SELECT DISTINCT max(TRUE) OVER () FROM json_tree('{}') UNION VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 62: `b04ce8f798916631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014492`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (TRUE)); INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT * FROM json_each('{"a":{"b":1}}') LIMIT FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 63: `95b5840ee79f8f79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014824`

```sql
SELECT substr('', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 64: `6d8f8ad9d5cd113f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014978`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY RAISE(IGNORE) ASC NULLS FIRST LIMIT TRUE, count() OVER (PARTITION BY NULL ORDER BY TRUE ASC NULLS LAST ROWS BET
```

---

## Crash 65: `55391ccefb268724` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015144`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 66: `ea92ef6d74dd6701` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015383`

```sql
SELECT substr('Z3Ch_R- 542- ', 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 67: `81dd49d625ba5656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015391`

```sql
SELECT round(1e-308, -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))
```

---

## Crash 68: `f3eb8282e664563c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015397`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); WITH t2 AS (VALUES (NULL)) INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM json_each('{"a":1}') LIMIT CURRENT_TIME)); PRAGMA integrity_check; CREA
```

---

## Crash 69: `30da62c9cdc33309` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015404`

```sql
SELECT printf('%lld', -9223372036854775808, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(
```

---

## Crash 70: `f228d7a82c41cd1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015437`

```sql
SELECT printf('%.*e', -2147483649, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 71: `834600e2520f104d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015472`

```sql
SELECT printf('%x', -9223372036854775808, '_1-  P_5P'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT co
```

---

## Crash 72: `a633674e50980e16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017069`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 73: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023401`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 74: `8dd9473014792796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025347`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 75: `e613360a4710f65d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025355`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT TRUE AS r_5xl FROM p WHERE NUL
```

---

## Crash 76: `ddbef4e0a15e7904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025369`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT X'ca9FEfEB'); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IS NOT NULL
```

---

## Crash 77: `ff41bf8b5d34c904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025389`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(le
```

---

## Crash 78: `c5dbb4cafc8f90fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025504`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 79: `76fc66e807bb2fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025511`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 80: `3fa0641daac99151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025540`

```sql
SELECT printf('%.*s', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 81: `d3827b0f70bd564b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025564`

```sql
SELECT substr('Vk n_y_ _Ls___-_ ', 2147483648, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELEC
```

---

## Crash 82: `2a456f706b84f3a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025595`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); WITH RECURSIVE t3 (c1) AS (VALUES (FALSE)) SELECT * FROM t3; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 83: `59ce5847c05f6208` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025606`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid DATE UNIQUE); SELECT q.* FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 84: `4e6b1c0a6f4b7b01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025615`

```sql
SELECT printf('%.*e', 0, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 85: `5b1e7914d430512c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026916`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 86: `d3613a0d3e0ee24b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027216`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p (rowid) VALUES (CURRENT_TIME NOT LIKE FALSE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 87: `830a2551058bca90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027238`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p (rowid) VALUES (~FALSE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 88: `f6fc85a844b7fbd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027278`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p (rowid) VALUES (TRUE NOT IN (NULL)); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 89: `76eea160a63d423b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027645`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); VALUES (CURRENT_TIME) UNION ALL VALUES (TRUE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 90: `912b3920f1045e2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027670`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT CURRENT_TIME % NULL AS r_5xl UNION VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL
```

---

## Crash 91: `b379ab7127a4dd65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027681`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); VALUES (CURRENT_TIME) EXCEPT VALUES (TRUE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 92: `82eb4e35fa378b8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027695`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT * FROM js
```

---

## Crash 93: `51bb5533b0745c27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027709`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP OR TRUE
```

---

## Crash 94: `660eb18291d018ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028229`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2, c1, c3); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed
```

---

## Crash 95: `4e5b107abb0b1cf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028306`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WH
```

---

## Crash 96: `82670cef4450cf7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029629`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY RAISE(IGNORE), 
```

---

## Crash 97: `d951a37079486e8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029635`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM json_tree('{"a":1}') LEFT JOIN q AS y33d__33s9x__u WHERE CURRENT_
```

---

## Crash 98: `27f5282eb26054a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029642`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 99: `3843684989a30fe7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029648`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 100: `09408f5c0e10c183` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029660`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM (json_each('{}') INNER JOIN jsonb_each('[1,2,3]')) WHERE CURRENT_
```

---

## Crash 101: `ca8d100b4c0a0639` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029681`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 102: `ca1676fefd985f13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029690`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 103: `8a6b21ca211fdf51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029697`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM json_each('{}') LEFT OUTER JOIN (p JOIN json_each('{"a":1}') JOIN
```

---

## Crash 104: `70a223500bcf3e9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029713`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CASE WHEN TRUE IS NULL THEN CURRENT_TIME ELSE TRUE END)); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}
```

---

## Crash 105: `5d0762b4375bad08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029731`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE == CURRENT_DATE), b DATE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 106: `b0e202052945d446` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE 38.777045818896390118909484384540812837300
```

---

## Crash 107: `093430640f4cc8bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029756`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM jsonb_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTA
```

---

## Crash 108: `7fdf6500afaf106a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033475`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, c3 TEXT 
```

---

## Crash 109: `cacf0d26dc515813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033497`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, c3 TEXT 
```

---

## Crash 110: `e0a555a86bf47c9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE
```

---

## Crash 111: `7ba0257ceff2eea3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033754`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, b FLOAT 
```

---

## Crash 112: `5706117170c4020e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033782`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, b FLOAT 
```

---

## Crash 113: `9dbe3901213a68de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034147`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE T
```

---

## Crash 114: `1d85357b61e03519` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034241`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE T
```

---

## Crash 115: `2a409937243d0e49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043008`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p (rowid) VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 116: `3fd87a60016d0019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044463`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT percent_rank() OVER (PARTITION BY FALSE ORDER BY NULL DESC NULLS LAST RANGE BETWEEN UNBOUNDED PRECEDING
```

---

## Crash 117: `7f758c2b0075194d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044496`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN RAISE(IGNORE) AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 O
```

---

## Crash 118: `cd1aaae4c4d9bdc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044504`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (38.777045818896390118909484384540812837300814456657610084919e+3282895474121252436455) UNION VALUES (TRUE); CREA
```

---

## Crash 119: `cca9c1baf5f0829f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044510`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIKE FALSE NOT LIKE CURRENT_TIME ESCAP
```

---

## Crash 120: `dc0a3e68cd45e3c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044569`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT DISTINCT +substr(CURRENT_TIMESTAMP COLLATE NOCASE, FALSE), NOT EXISTS (WITH RECURSIVE p AS 
```

---

## Crash 121: `2305e8dcc82977d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044587`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 122: `360719e2bffac6bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044673`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT TRUE FROM json_tree('{"a":1}') LEFT JOIN json_tree('[]') UNION VALUES (TRUE); CREATE TA
```

---

## Crash 123: `eb59b8d106222943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044684`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT EXIST
```

---

## Crash 124: `e4dda5cc65df004d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044690`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT json_valid(NULL) AS a8_x_0k720d_0f10ki____60s_lor19_c6__b5r_41__z7q8__x0 FROM p NATURAL JOIN q WH
```

---

## Crash 125: `74e4bab99b42d944` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044728`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); VALUES (FALSE) INTERSECT VALUES (CURRENT_TIME) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 126: `790752296d674bde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046686`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (RAISE(IGNORE) IS NULL | TRUE)); CREATE TABLE IF NOT EXISTS q(c1 DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 127: `e51769073462420a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046720`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); SELECT count(DISTINCT CURRENT_TIMESTAMP) UNION VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 128: `8ef529e88555c397` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046732`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); SELECT DISTINCT percent_rank() OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST ROWS BETWEEN CURRENT ROW AN
```

---

## Crash 129: `08cebc70c0e978a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046748`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); SELECT DISTINCT percent_rank() OVER (ORDER BY EXISTS (VALUES (CURRENT_TIME)) RANGE BETWEEN UNBOUNDED PRECED
```

---

## Crash 130: `6c6e78d2f810e6d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047833`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY FALSE ASC NULLS FIRST, CURRENT_TIMESTAMP ASC NULLS LAST, CURRENT_TIMESTAMP ASC NULLS LAST LIMIT RAISE(
```

---

## Crash 131: `e1c794364aa94218` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q AS (VALUES (CASE CURRENT_TIME WHEN CURRENT_TIMESTAMP THEN CURRENT_DATE ELSE NULL END, FALSE)) SELECT * FROM q; CREATE TABLE s
```

---

## Crash 132: `39974bffc2fbfb30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048182`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT TRUE FROM json_each('[1,2,3]') UNION VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 133: `6437178599585166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048224`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC); INSERT INTO q VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNI
```

---

## Crash 134: `e42c399e2d52c2ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049836`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS (PARTITION BY RAISE(IGNORE) ORDER BY RAI
```

---

## Crash 135: `b175ee836058d896` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051313`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; SELECT * FROM (SELECT * FROM p WHERE TRUE COLLATE BI
```

---

## Crash 136: `b7a9da3749cc45a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051735`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('[]') CROSS JOIN jsonb_tree('{}') USING (c1, a) WHERE NULL ORDER BY CURRENT_DATE DESC NULLS L
```

---

## Crash 137: `cb06f21b66324119` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('[]') CROSS JOIN jsonb_tree('{}') USING (c1, a) WHERE NULL ORDER BY CURRENT_DATE DESC NULLS L
```

---

## Crash 138: `4fe6553ef5387c40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051770`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME IN (6, TRUE)); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 139: `33da3519ed4946d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051912`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('[]') CROSS JOIN jsonb_tree('{}') ON FALSE WHERE NULL ORDER BY CURRENT_DATE DESC NULLS LAST L
```

---

## Crash 140: `b0b186cffe150b07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052062`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308
```

---

## Crash 141: `344accc32e8f756a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052807`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT CURRENT_TIME & CURRENT_DATE FROM json_each('[{"a":1},{"b":2}]') UNION VALUES (CURRENT_D
```

---

## Crash 142: `9a75e24e718c4791` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058071`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (CURRENT_TIMESTAMP
```

---

## Crash 143: `c812df23eb7bd212` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058077`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURR
```

---

## Crash 144: `f1e0a61a07c8fa36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058145`

```sql
SELECT printf('%.*d', 4294967296, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 145: `a42c6243c25a36d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058221`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT DEFAULT -949583.583738402E+73); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 146: `0647e1ce69060262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058233`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT DISTINCT count(*) OVER (PARTITION BY FALSE ORDER BY NULL DESC NULLS LAST RANGE BETWEEN UNBO
```

---

## Crash 147: `31ede8d901dee0a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058576`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); VALUES (TRUE) UNION SELECT * ORDER BY TRUE UNION ALL SELECT * FROM json_each('{"a":1}') WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIMESTAM
```

---

## Crash 148: `e7ea6334192bdc19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070650`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF N
```

---

## Crash 149: `e965782f9e342943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072862`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE T
```

---

## Crash 150: `be63786e6ba317e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073115`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE
```

---

## Crash 151: `58a89badb855cef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TA
```

---

## Crash 152: `5360128ecb2f6e01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP / NULL || FALSE IS NOT NULL OR 
```

---

## Crash 153: `c783b1ed69433aa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073140`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE
```

---

## Crash 154: `e932418c8f2ad02b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073184`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE
```

---

## Crash 155: `8b7df6862a3f5dd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073828`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); SELECT DISTINCT cume_dist() OVER () FROM json_tree('{}') UNION VALUES (TRUE); CREATE TABLE seed_a
```

---

## Crash 156: `70498037fedb4eca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073853`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') WHERE TRUE ORDER BY CURRENT_DATE ASC NULLS FIRST LIMIT F
```

---

## Crash 157: `2f70b65b9e3bd6a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073872`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); SELECT DISTINCT count() OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST ROWS BETWEEN CURRENT ROW
```

---

## Crash 158: `c772393002e3e7c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078489`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); WITH t2 AS (VALUES (NULL)) INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 159: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001703`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 160: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001832`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 161: `1452ce1192f7bb9f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001975`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 162: `beec9b01ee7c09a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001986`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 163: `9031f83fff66bd14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001992`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 164: `04d306dd32221906` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (NULL + CURRENT_DATE AND CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE - TRUE < CURRENT_TIME >> CURRENT_TIME IN (TRUE)); PRAGMA in
```

---

## Crash 165: `ae998b7ddc9d9b1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE - TRUE < CURRENT_TIME >> CURRENT_TIME IN (TRUE)); PRAGMA integrity
```

---

## Crash 166: `9b08d53a89dd57e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003399`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (NULL + CURRENT_DATE AND CURRENT_TIME - TRUE < CURRENT_TIME >> CURRENT_TIME IN (TRUE)); PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 167: `d245366697660454` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003409`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (NULL + CURRENT_DATE AND CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE - TRUE < CURRENT_TIME IN (TRUE)); PRAGMA integrity_check; C
```

---

## Crash 168: `ccaa5f2db5475749` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003424`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 169: `57fd4f4c09ee758e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003431`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP IN (TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 170: `16fcd55302864147` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003462`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE IN (TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 171: `dcb48b4eb535a550` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003492`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIMESTAMP - TRUE < CURRENT_DATE IN (TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 172: `162ec401364ff1bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 173: `26ce728c7652a468` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003527`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_DATE IN (TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 174: `ec26e98f6ce88bed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003537`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE - TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 175: `33b445e6df1bbd54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003785`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 176: `64ee3bffbf88002a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005388`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 177: `a2f1000a7a3e6a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005840`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_TIME; CREA
```

---

## Crash 178: `9cef590c947dc27f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005974`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 179: `6df4c41af6158abc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006435`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN CHECK (-TRUE LIKE TRUE ESCAPE CURRENT_TIME NOTNULL)); VALUES (NULL); CREATE
```

---

## Crash 180: `aeac308ef3ab71d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006487`

```sql
SELECT printf('%lld', -2147483649, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 181: `b8b35b84c360aad8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007019`

```sql
SELECT substr('', 4294967296, -9223372036854775808); CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TA
```

---

## Crash 182: `158b3b038c457ef6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007036`

```sql
SELECT substr('', 4294967296, -9223372036854775808); CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 183: `865bc2c30a1aa37c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007553`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT
```

---

## Crash 184: `f7ae37fd9e2c60aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007560`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALU
```

---

## Crash 185: `a33e22a99a1ceeba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007566`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRU
```

---

## Crash 186: `ca0844baea38b600` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009772`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN NULL ISNULL AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VAL
```

---

## Crash 187: `404c84672425acd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_DATE AND FALSE | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DE
```

---

## Crash 188: `c68add0707035ddc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009836`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIME != TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VAL
```

---

## Crash 189: `f0df057ef4079887` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010004`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 190: `9940740ca25d7c94` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010025`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP | TRUE | TRUE | TRUE | TRUE | TRUE | TRUE | TRUE | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT 
```

---

## Crash 191: `bb7978d6e7bd8186` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010506`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 
```

---

## Crash 192: `fbffc1b182cecceb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010512`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN +FALSE AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (
```

---

## Crash 193: `7f91493831dac3fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010519`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN +FALSE COLLATE BINARY < CURRENT_TIMESTAMP AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREAT
```

---

## Crash 194: `a4b5ebe7b659a68d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010527`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN +CURRENT_TIMESTAMP AND FALSE NOT BETWEEN FALSE AND NULL COLLATE BINARY < CURRENT_TIMESTAMP AND NULL | TRUE), c1 BOOLEAN DEF
```

---

## Crash 195: `f91513ecc064b5b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010565`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VA
```

---

## Crash 196: `deb3e7197d6bc27f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010574`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN +CURRENT_TIME NOT BETWEEN FALSE AND NULL COLLATE BINARY < CURRENT_TIMESTAMP AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowi
```

---

## Crash 197: `6f0a76f583267b2c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010635`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND NULL | TRUE), c1 BOOLEAN DEFAULT TRUE, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VA
```

---

## Crash 198: `660647fc848dbdb4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010652`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 199: `0ed9e8d9ab74e562` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010658`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE, c1 BOOLEAN DEFAULT TRUE, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREAT
```

---

## Crash 200: `ef17037054380f59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (+FALSE COLLATE BINARY < CURRENT_TIMESTAMP), rowid INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREAT
```

---

## Crash 201: `6640e3beb8ef0aa5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010727`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND NULL | TRUE), c1 BOOLEAN DEFAULT CURRENT_TIME, rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EX
```

---

## Crash 202: `c43f6f76d9040611` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010765`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY, c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 203: `c0cb558e2c3eb3c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010822`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIME <> CURRENT_TIMESTAMP ISNULL AND NULL | TRUE), c1 BOOLEAN DEFAULT -621, rowid VARCHAR(255) PRIMARY KEY); CREATE
```

---

## Crash 204: `3961a6f4a8528e9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012743`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_DATE AND FALSE)); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 205: `dc8a9e19f8b8300d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012749`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); SELECT * FROM (VALUES (CURRENT_DATE)) AS a WHERE FALSE; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 206: `2ece60725d6b7b43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012757`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT SELECT CURRENT_TIMESTAMP; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 207: `f489aa05e9c7549b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012769`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); SELECT ALL * FROM json_tree('[1,2,3]') ORDER BY TRUE ASC NULLS FIRST; CREATE TABLE se
```

---

## Crash 208: `b256844a95019466` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); VALUES (FALSE) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 209: `9def224a36c82fcb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012801`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INT
```

---

## Crash 210: `1a8656c67efe0fd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); SELECT NULL UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 211: `71bcc46c9d550e6a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012819`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 212: `a547dac302f04320` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012827`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME UNION ALL VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 213: `884f01678afef964` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012840`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT DISTINCT percent_rank() OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM 
```

---

## Crash 214: `54fb40c2f12f9ef7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012849`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIME NOT LIKE FALSE) EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 215: `cdd88fd0a49fca17` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012855`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME INTERSECT VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 216: `392f04434987abbb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012871`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') JOIN (p NOT INDEXED); CREATE TA
```

---

## Crash 217: `96e1e8c84e334319` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012898`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME); VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_TIME))); CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 218: `bea53e485545e2c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012907`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME UNION VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 219: `46fb978b6e32fdca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012914`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM json_each('[]') WHERE TRUE GROUP BY RAISE(IGNORE), CURRENT_TIMESTAMP; INSERT 
```

---

## Crash 220: `9857d92d27921a4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013087`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIME); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') JOIN (p NOT INDEXED); CR
```

---

## Crash 221: `f8369934d1085d9b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013097`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIME); SELECT DISTINCT * FROM json_tree('[1,2,3]'); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 222: `13f43a854d0cc0d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013133`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CASE WHEN FALSE THEN CURRENT_TIME END); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 223: `97245c0f8c6f77c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013140`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CASE WHEN FALSE THEN NOT FALSE + TRUE END); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 224: `792ea0aa213f3891` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013147`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CASE WHEN FALSE THEN NOT FALSE + CASE WHEN CURRENT_TIMESTAMP THEN EXISTS (VALUES (RAISE(IGNORE))) E
```

---

## Crash 225: `2f8edf55015418df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013213`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT DISTINCT percent_rank() OVER () FROM json_each('[{"a":1},{"b":2}]'); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 226: `8f0040fff01273c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013261`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (NULL); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 227: `f88c4449c1fdf98f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013269`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIMESTAMP / CURRENT_TIMESTAMP); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 228: `75aa659f6ca374b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013276`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIMESTAMP / CURRENT_TIME OR FALSE); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 229: `93e494569299e67f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015523`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); SELECT CURRENT_DATE COLLATE BINARY EXCEPT VALUES (CURRENT_TIME NOT LIKE FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 230: `9aef418ee79f4e21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015579`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); SELECT * FROM (VALUES (CURRENT_DATE)) AS a WHERE CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)) ORDER BY TRUE DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 231: `f7ad80932a15594a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015588`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); SELECT * FROM json_each('[{"a":1},{"b":2}]') JOIN p NOT INDEXED WHERE CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)) ORDER BY TRUE DESC NULLS LAST; CREATE TABLE see
```

---

## Crash 232: `af231f6941c20b72` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015720`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); SELECT * FROM (VALUES (CURRENT_DATE)) AS a WHERE CURRENT_TIME ORDER BY TRUE DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 233: `719417a65a48671f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016295`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (CURRENT_DATE, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 234: `28360283a1d933dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016329`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 235: `0fb827207acca5c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016375`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, rowid NUMERIC NOT NULL DEFAULT 74.82E790584241430474393, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (NULL); CREATE TABLE seed_t1(c1 
```

---

## Crash 236: `4a709951a6cee831` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016387`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 INTEGER CHECK (TRUE IS NULL)); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 237: `4789e5b49496f2d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016452`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (json_extract(lag(CURRENT_DATE, CURRENT_TIME) OVER (PARTITION BY CURRENT_T
```

---

## Crash 238: `b3b7a15b8adab699` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016489`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b TEXT UNIQUE, c2 
```

---

## Crash 239: `2c72cf2f08ba02ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016515`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (last_insert_rowid()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 240: `68bf7d671db1c9d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016527`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (json_extract(percent_rank() OVER (PARTITION BY CURRENT_TIMESTAMP), '$.b.b')); CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 241: `01b4f4eb7ccf4be9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016535`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (json_extract(lag(CURRENT_DATE, CURRENT_TIME) OVER (PARTITION BY NULL), '$.b.b')); CREATE TABLE seed_t1(c1 
```

---

## Crash 242: `0705cfb4e25866f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016557`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (changes()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 243: `66ef22d629d99f3c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016591`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (random()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 244: `9b24954a75140b71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016601`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (json_extract(percent_rank() OVER (PARTITION BY CURRENT_TIME), '$')); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 245: `1ea1b880d5b3d8e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016620`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (total_changes()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 246: `be5142c18bd85dc6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018444`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 247: `e77e0ffa956ea988` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018471`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH r (a) AS (SELECT *) SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREAT
```

---

## Crash 248: `fd25318fd0cec838` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018539`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIMESTAMP - TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 249: `aa13f8eeb3f6638e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018555`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p SELECT CURRENT_TIMESTAMP EXCEPT VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 250: `208c4d43c32ad6e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018561`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT 74.82E790584241430474393, a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 251: `030f79dbc3d128a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018597`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); WITH p AS (SELECT *) INSERT INTO p VALUES (CAST(NULL AS REAL) NOT IN (NULL)); PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 252: `086e3f79273aa4e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018626`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 253: `55ab62cee446758d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018646`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 254: `b2e5324cfff80181` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018679`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS
```

---

## Crash 255: `cf10cc1b7d20be49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018685`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE INDEX IF NOT EXISTS
```

---

## Crash 256: `8a839c219edcc5ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018864`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 257: `2337e7c41cf510c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018894`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 258: `26f811470670e41b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018900`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT TRUE, a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t
```

---

## Crash 259: `414edbba9fd37e0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019644`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT FALSE, * FROM p NOT INDEXED ORDER BY CURRENT_TIM
```

---

## Crash 260: `5818b8f9e65ef560` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019657`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED ORDER BY NULL DESC NULLS FI
```

---

## Crash 261: `8e3b17c47f1691b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019664`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME AS mk74 FROM p NOT INDEXED ORDER BY
```

---

## Crash 262: `a3b684e4bb081ce4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019682`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED ORDER BY NULL DESC NULLS FI
```

---

## Crash 263: `1284e5c6cbabd098` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019689`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_DATE AND FALSE | TRUE), c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT
```

---

## Crash 264: `210e79ebb9504513` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019727`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); REPLACE INTO p VALUES (NULL + CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * F
```

---

## Crash 265: `831169a093eadfad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019747`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT row_number() OVER () FROM json_tree('{}') UNION VALUES (TRUE); CREA
```

---

## Crash 266: `8816a44082eb85df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019825`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each(TRUE, '$.key') ORDER BY CURRENT
```

---

## Crash 267: `a3302b51e9769809` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019866`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p JOIN json_each('{"a":1}') JOIN q ORDER 
```

---

## Crash 268: `165b68510e9d923e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019896`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED ORDER BY TRUE << CURRENT_TI
```

---

## Crash 269: `cc22fe330ba70249` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023962`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT q.* FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NU
```

---

## Crash 270: `b7b51c022c72a71e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025173`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NU
```

---

## Crash 271: `a76ef837103487c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026277`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE - TRUE); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 272: `850fd563fa79d6bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026301`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); WITH t1 AS (VALUES (TRUE)), t2 AS (VALUES (NULL)) INSERT INTO p VALUES (~CASE WHEN NOT EXISTS (VALUES (RAISE(IGNORE))) THEN NULL END); VALUES (NULL); CREATE
```

---

## Crash 273: `1c4f62c4a1c07eb7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026687`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 274: `c169f573158fc17f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p SELECT CURRENT_TIME EXCEPT VALUES (CURRENT_TIME OR FALSE); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 275: `18c368f34b7e39fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026705`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE - TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 276: `c78b53cd92d37dcb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 277: `6f50435420e1ad4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP / FALSE) AS sub1; CREATE TABLE seed_t1(c1 I
```

---

## Crash 278: `89ebb9ed595f856f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033683`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PR
```

---

## Crash 279: `4eaa68f30692e659` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034016`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (NULL + CURRENT_DATE AND CURREN
```

---

## Crash 280: `33083b4d9436aeab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034178`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE T
```

---

## Crash 281: `5f8bf368adb11481` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034277`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrit
```

---

## Crash 282: `ff015c5b10acf4ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE IS NOT (CURRENT_DATE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 283: `055b76fe24ed3d69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035260`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); WITH t2 AS (VALUES (NULL)) INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM json_each('{"a":1}') LIMIT TRUE)); PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 284: `4d5eb111ddc8ea6e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035274`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_TIMESTAMP)); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 285: `ae99da921f9901e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035283`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); WITH p AS (SELECT *) INSERT INTO p VALUES (CAST(TRUE AS VARCHAR(255))); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 286: `cf8a07b3ac5a741a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035293`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE < CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 287: `141a319edfb824a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035302`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND FALSE NOT BETWEEN FALSE AND NULL AND NULL)); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_DATE); PRA
```

---

## Crash 288: `b9bfc3ac082ad956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035308`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_TIME LIKE CURRENT_TIMESTAMP * TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 289: `163cf48f88312ee0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035314`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME < CASE WHEN TRUE IS NULL THEN CURRENT_TIME ELSE TRUE END); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 290: `4123d35a56142ee8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035321`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE >> CURRENT_DA
```

---

## Crash 291: `6d9e0af0c7d1df43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035331`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); SELECT * FROM (SELECT * FROM p WHERE json_extract(json_extract(FALSE, '$'), '$')) AS sub1; CREATE TABLE seed_
```

---

## Crash 292: `13252504a9c61754` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035341`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT TRUE); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 293: `2e9c6d5328b4477f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035368`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIMESTAMP ASC LIMIT count(DISTINCT CURRENT_TIMESTAMP); REPLACE INTO p VALUES (CURRENT_TIME < CU
```

---

## Crash 294: `b4fcdd5d2b949939` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035378`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME < CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 295: `e5f8524da5a39432` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035482`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE - TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 296: `ea7e2d8e16f21103` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035505`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE - TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIMESTAMP); PRAGMA integrity_check; CRE
```

---

## Crash 297: `5d1ac5e3c725c3a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035520`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIMEST
```

---

## Crash 298: `73d6894c67af233c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035544`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); WITH p AS (SELECT *) INSERT INTO p VALUES (FALSE NOT IN (-FALSE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 299: `15aa13a88648688b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035661`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 300: `fc8f899f4cad4410` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035694`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIME - TRUE); PRAGMA integrity_check; CREATE TABLE see
```

---

## Crash 301: `2c9511021f5ccaee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035744`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP AND TRUE NOT NULL GLOB FALSE ISNULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 302: `8e9aefa2a8ebb8c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035765`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIMESTAMP - +FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 303: `49b59a80cd651cef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035795`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 JOIN json_tree(TRUE, '$') WHERE RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VA
```

---

## Crash 304: `e46f55100dabf256` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035910`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND CURRENT_TIMESTAMP - CURRENT_DATE AND CURRENT_TIMESTAMP - CURRENT_DATE AND CURRENT_TIMESTAMP - CURRENT_DATE AN
```

---

## Crash 305: `7a8c6a11cb6436ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035926`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE AND TRUE NOT NULL IS NULL IN (CURRENT_TIME >> FALSE) NOTNULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 306: `d7e4a50fc02ede44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036146`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL || FALSE IS NOT NULL OR CUR
```

---

## Crash 307: `e35a080f4e6d0462` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE < NULL); PRAGMA integrity_check; CREATE T
```

---

## Crash 308: `1c646f0d2cf5abe5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036261`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT X'D9aD'); REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE < NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 309: `caeabb188d465ba6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036313`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIMESTAMP + CURRENT_TIME LIKE CURRENT_
```

---

## Crash 310: `b46c1df1787dd842` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036356`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (-NOT EXISTS (VALUES (FALSE)) >= NULL ISNULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 311: `6fbf21f4f2bf75b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036371`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 312: `30bdb3c4456ec26a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036393`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); REPLACE INTO p VALUES (NULL + CURRENT_TIME LIKE CURRENT_DATE ESCAPE TRUE); PRAGMA integrity_check; CREAT
```

---

## Crash 313: `250af367117572df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045246`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT count() AS g_ FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 314: `24a25aa31e3ba6bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045256`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT CURRENT_TIMESTAMP << NULL FROM json_each('[{"a":1},{"b":2}]') UNION VALUES (CURRENT_DAT
```

---

## Crash 315: `50cf7095fe740463` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045264`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (FALSE)); INSERT INTO p VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); PRAGMA integrity_check; CR
```

---

## Crash 316: `22c1ae8f9b96d510` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045273`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT * FROM json_tree('{}') UNION SELECT * FROM json_tree('[]'); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 317: `7f558dc9434b03fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045289`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (FALSE)); INSERT INTO p (rowid) VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 318: `f3395f55952d2598` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045333`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN DEFAULT X'FebFb7'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 319: `f6ee2c7d1b140db3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045842`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 320: `60cfd3673edfbe70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045876`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT ''); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 321: `a811484f947db4b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045930`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY, a BOOLEAN UNIQUE, c2 INT NOT NULL DEFAULT 055084.7404920e3); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integr
```

---

## Crash 322: `2e7749ba030c8ec8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045956`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP / FALSE || FALS
```

---

## Crash 323: `79e3cce16ebef11d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045986`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE IS NULL)); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 324: `9490f0acf7afbfd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045993`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 325: `91a150f0e184c159` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046026`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE -NOT EXISTS (VALUES (FALSE
```

---

## Crash 326: `9a90190b95755e05` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046035`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE == CURRENT_DATE), b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 327: `ee278728a349f62c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046110`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 328: `878ae76e4e3f0e19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046131`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER CHECK (TRUE), b INTEGER CHECK (CURRENT_TIMESTAMP), c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; P
```

---

## Crash 329: `0f81cd52afcd6351` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046196`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (CURRENT_DATE)); WITH p AS (SELECT *) INSERT INTO p VALUES (CURRENT_DATE >> -CURRENT_TIME); PRAGM
```

---

## Crash 330: `71439116548abee8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046300`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS
```

---

## Crash 331: `cd695193f22a043f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047457`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); SELECT * FROM (SELECT * FROM p WHERE json_extract(FALSE, '$[0].key')) AS sub1; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 332: `7724e17807187607` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048383`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL CHECK (CURRENT_TIMESTAMP IS NOT TRUE COLLATE RTRIM), c2 TEXT CHECK (TRUE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME)
```

---

## Crash 333: `32b85e5704a2b8ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050606`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 JOIN json_tree(TRUE, '$') WHERE RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VA
```

---

## Crash 334: `783c11043ee9b8c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050669`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p (rowid) VALUES (~json_patch('{"a":{"b":1}}', '{}')); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 335: `a65330ef042f698e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051503`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') JOIN (p NOT
```

---

## Crash 336: `4c9667f911a4d77b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT CURRENT_TIME IN (SELECT * FROM p) FROM json_tree('{}') UNION VALUES 
```

---

## Crash 337: `f674ea40c83cb0be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051674`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT CURRENT_TIME IN (SELECT * FROM p) FROM json_tree('{}') UNION VALUES (TRUE); CREATE TABLE se
```

---

## Crash 338: `aa6fe303af77a641` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056946`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); REPLACE INTO p VALUES (TRUE IN (VALUES (CURRENT_TIME) EXCEPT VALUES (FALSE))); PRAGMA integrity_check; C
```

---

## Crash 339: `311a20cda83bda65` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056980`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED UNION ALL VALUES (CURRENT_TIME); PRAGMA integrity_che
```

---

## Crash 340: `47310083ae9d01e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056995`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); REPLACE INTO p VALUES (CURRENT_TIME LIKE NULL > CURRENT_TIME ESCAPE TRUE); PRAGMA integrity_check; CREAT
```

---

## Crash 341: `7a37af38b5f2e986` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057024`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 342: `f8d5d7be85c0b02c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE PRIMARY KEY); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP)) SELECT CURRENT_TIMESTAMP IS TRUE FROM p; CREATE TAB
```

---

## Crash 343: `6f10c10a7ddd82ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057185`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS ()); CREATE TAB
```

---

## Crash 344: `7f4435593bb097c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057204`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN DEFAULT '-ft'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 345: `73d0f0225bb8d610` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057220`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN DEFAULT ' l - 2Z1-c_'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 346: `fea42269c8aceffd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057307`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN DEFAULT '0 '); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 347: `c37d24701b543199` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069904`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT DISTINCT max(CURRENT_DATE COLLATE BINARY) OVER () FROM json_tree('{}') UNION VALUES (TRUE); CREA
```

---

## Crash 348: `09436d8a5256b89a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069918`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT -8897.19819397340236581892330197636210843750456604588274419e-590910498209257598602734816529637178966665619164); REPLACE INTO p VALUES (NULL)
```

---

## Crash 349: `ec279cb5c55d95bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069929`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT 5406998000629.8077288); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 350: `9b945a53d7461786` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069970`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT '0 TBOb_ _ _Y- t-_rT'); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 351: `98d2f8ecdbfec317` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070025`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT -47281058801206995750090187079533088730340102863679223439372174669471345060819707649098512516982304590259789.10); REPLACE INTO p VALUES (NULL);
```

---

## Crash 352: `8080e55db0360dd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT avg(CURRENT_TIMESTAMP) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 353: `28dcdeb98797170c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_DATE IN (SELECT DISTIN
```

---

## Crash 354: `ec53ffae60e1f074` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070132`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE IS NOT NULL COLLATE BINARY || TRUE || TRUE || TRUE || TRUE || TRUE || CUR
```

---

## Crash 355: `c3a9c0f01d5a572f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070138`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIMESTAMP - TRUE); PRAGMA in
```

---

## Crash 356: `2e612ff9aa5eed3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070144`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 357: `e62949d5f084be7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070167`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); WITH p AS (SELECT *) INSERT INTO p VALUES (CAST(TRUE AS INT)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 358: `64306c52b013b4a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070259`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURRENT_TIMESTAMP - TRUE); PRAGM
```

---

## Crash 359: `b977fe88a0e00871` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070302`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 360: `bd9b538fe91dd173` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070341`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || CURREN
```

---

## Crash 361: `c55be0c1281603cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072218`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); VALUES (CURRENT_DATE) UNION VALUES (X'0eF919DCE4b24F'); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NUL
```

---

## Crash 362: `36d5f4e07628fed4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072239`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE 
```

---

## Crash 363: `6f57324a53c166a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072300`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (FALSE - TRUE); PRAGMA integrit
```

---

## Crash 364: `b3399240031b6cb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072432`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_DAT
```

---

## Crash 365: `66685b160957cf9d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072439`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE json_array(F
```

---

## Crash 366: `f7adcd93d40668e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072445`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (
```

---

## Crash 367: `828fce68d55f7615` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072500`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH t1 AS (VALUES (T
```

---

## Crash 368: `c454b4bba682c3b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072523`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE CURRENT_DATE
```

---

## Crash 369: `38297c466aff5346` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072635`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (
```

---

## Crash 370: `facb2d6c55b42dd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE q AS (VALUES (CURRENT_TIMESTAMP)) SELECT count() ISNULL FROM p; CREATE 
```

---

## Crash 371: `f256905ef7ebbfa5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073324`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY CURRENT_DATE AND CURRENT_TIME LIKE C
```

---

## Crash 372: `37a357551ba0b8c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073335`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC ROWS BETWEEN CURRENT_DATE
```

---

## Crash 373: `51ede71df465f37e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073343`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, _rowid_ BOOLEAN CHECK (NULL IS NOT c2)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC ROWS B
```

---

## Crash 374: `51ca3c8dbeee4494` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073355`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (PARTITION BY CURRENT_DATE, NULL), FALSE); CRE
```

---

## Crash 375: `4c5c5b70e967d67d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073369`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC GROUPS BETWEEN UNBOUNDED 
```

---

## Crash 376: `dabbca5e1d6f3eeb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073400`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY TRUE IS NULL DESC ROWS BETWEEN UNBOU
```

---

## Crash 377: `b0aa650103640f81` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073410`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IN ('')); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 378: `6725a09d83329e44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC ROWS BETWEEN CURRENT ROW 
```

---

## Crash 379: `82e8d821f79e510d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073523`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (count() OVER (ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PR
```

---

## Crash 380: `ee5190c7084077ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073650`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (NULL, NULL, CURRENT_TIMESTAMP, FALSE, FALSE, TRUE, CURRENT_
```

---

## Crash 381: `ee0fbc5225ae26d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073692`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (NULL, NULL, CURRENT_TIMESTAMP, FALSE, FALSE, TRUE, CURRENT_
```

---

## Crash 382: `df164cfd12e82b32` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL, c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE q AS (VALUES (CURRENT_TIMESTAMP)) SELECT count() FROM p; CREATE TABLE s
```

---
