# Crash Triage Report

**Total crashes:** 335  
**Unique crash sites:** 335  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 154 | 154 | 45% |
| Signal | 181 | 181 | 54% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `ad7bade1af46b43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000319`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); SELECT RAISE(IGNORE) IS NULL > TRUE COLLATE NOCASE IS DISTINCT FROM CURRENT_TIME >= CURRENT_TIME ISNULL IN (NULL) < FALSE REGEXP FALSE IS N
```

---

## Crash 2: `33e998b356120375` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000540`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 3: `14919854c8e7b122` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000597`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO r VALUES (CURRENT_TIMESTAMP NOT BETWEEN ~TRUE AND c1 < first_value(~NULL GLOB CURRENT_
```

---

## Crash 4: `120c39456d407312` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000886`

```sql
SELECT printf('%.*d', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IS NULL COLLATE NOCASE, typeof(TRUE) BETWEEN CURRENT_DATE AND TRUE NOT NULL 
```

---

## Crash 5: `8d332fab3b161fd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001108`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(b BLOB, c3 GENERATED ALWAYS AS (a + 0) NOT NULL UNIQUE, _rowid_ NUMERIC); SELECT CASE WHEN CURRENT_DATE THEN CASE RAISE(IGNORE) IS
```

---

## Crash 6: `5c0204a33e0a36b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001164`

```sql
SELECT substr('_-', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, b); WITH t1 AS MATERIALIZED (SELECT FALSE) INSERT INTO p VALUES ((json_array_length(FALSE))); EXPLAIN QU
```

---

## Crash 7: `65e708fab32ae211` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001231`

```sql
SELECT printf('%.*d', -1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); SELECT TRUE AS a, p.* FROM t3 JOIN q g ON CAST((CURRENT_TIMESTAMP) AS INTEGER) ISNULL <> CURRENT_DATE IS NO
```

---

## Crash 8: `eb33c7e44885468f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001349`

```sql
SELECT substr('- ', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO s VALUES (340.994778E-595121575346681567683748808456517450542508726729404566441483334302678980416
```

---

## Crash 9: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001538`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 10: `f7f495f0ac83be11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002159`

```sql
SELECT substr('Bh F-  5', -2147483648, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELE
```

---

## Crash 11: `9bec6dd900be7afa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002702`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, EXISTS (SELECT * FROM t3 NOT INDEXED GROUP BY CURRENT_TIMESTAMP HAVING RAISE(IGNORE) LIMIT RAISE(IGNOR
```

---

## Crash 12: `088f945ad9bae306` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002711`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t3 NOT INDEXED GROUP BY CURRENT_TIMESTAMP HAVING RAISE(IGNORE) LIMIT RAISE(IGNORE), CURRENT_TIME; 
```

---

## Crash 13: `a34a50f023277d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002764`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE see
```

---

## Crash 14: `78da9e76d8761687` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002849`

```sql
SELECT printf('%.*e', 1, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 15: `b27bba7cebcae56a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002921`

```sql
SELECT printf('%.*s', -2147483648, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 16: `a4f98a1356df14e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003091`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 17: `f50ea42f7d1de0ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003819`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED CROSS JOIN json_each('[]') CROSS JOIN 
```

---

## Crash 18: `335518efbaf0f5dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003848`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED CROSS JOIN json_each('[]') CROSS JOIN 
```

---

## Crash 19: `b3ed43556d505540` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004620`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 20: `904e559c42175df3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004916`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q INDEXED BY c3 UNION ALL SELECT * FROM json_each('[]') ORDER BY TRUE ASC NULLS LAST; INSERT INTO p DEFAULT
```

---

## Crash 21: `a883abe1060fb8fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004922`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q INDEXED BY c3 UNION ALL SELECT * FROM json_each('[]') ORDER BY NULL MATCH NOT NULL COLLATE RTRIM ASC NULL
```

---

## Crash 22: `f2f77eb191e7a203` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004933`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q INDEXED BY c3 UNION ALL SELECT * FROM json_each('[]') ORDER BY CASE TRUE WHEN NOT NULL THEN RAISE(IGNORE)
```

---

## Crash 23: `79bf5305b0cd0bdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005632`

```sql
SELECT substr('15js _Wa-8 mn', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT printf('%.*e', 42949
```

---

## Crash 24: `546cc20611dfaac0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008723`

```sql
SELECT printf('%.*s', 2147483647, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 25: `2439107f0a3c66de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008736`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), b NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 26: `c9fa1525b6d71d53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008743`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (TRUE), a INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 27: `e9030da6f06f67f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008756`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 28: `820b54060e9ebb91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008774`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 29: `db2336223daff8e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008797`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT NULL LIMIT FALSE IS NOT NULL OFFSET CURRENT_DATE NOT LIKE TRUE; CREATE TABLE seed_a(c 
```

---

## Crash 30: `2f0a33a7f6805bfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008811`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, c3 REAL DEFAULT -871117458087959899336525929688783640280369.122582918388780344419827042303096656193294893071850600754); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 31: `473d25ea7a3d81dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008822`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 32: `95ed10dd39643614` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008831`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 33: `fcb51cf089c7c60f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008840`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, b DATE CHECK (NULL), a DATE CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 34: `7be507e5917be545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008851`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE, c1 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 35: `c5c1bcd1c2989997` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008884`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER DEFAULT 0, c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 36: `e8202b043f2bbf90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008907`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 37: `4cf3679bca131413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008936`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 38: `ef772ce52a8ea4a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, c3 NUMERIC DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 39: `3487a35aff89a5d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008963`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a FLOAT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 40: `5e0a330237d65b98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008977`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, a INT); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 41: `34c361421aece1de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009027`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_
```

---

## Crash 42: `ecc106e835bd5631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010466`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT
```

---

## Crash 43: `0b2e57a5ea98c2fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011301`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION SELECT * FROM t1 WHERE EXISTS (VALUES (NULL) UNION ALL VALUES (NULL)) GROUP BY FALSE WINDOW w1 AS 
```

---

## Crash 44: `f7b6dabba6ae1684` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011379`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 45: `3d19028d1839f6af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011559`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 46: `5c63b63d1c92ea0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011646`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 47: `5d3f67083ae81ad3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013322`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT INTO p (rowid) VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 48: `2b6efdf49fc2e7a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013361`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (NULL) UNION ALL VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 49: `0daf34004ea7dd3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014071`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 50: `52b4a74270453150` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014204`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 51: `806f649e1bddf2ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019163`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED CROSS JOIN json_each('[]') CROSS JOIN (r LEFT JOIN json_tree(TRUE, '$') LEFT JOIN 
```

---

## Crash 52: `f9200208d9c6d941` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019177`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED CROSS JOIN json_each('[]') CROSS JOIN (r LEFT JOIN json_tree(TRUE, '$') LEFT JOIN 
```

---

## Crash 53: `8da8fb25591343dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019213`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (~FALSE > CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 54: `e05e7238e710be6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019220`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (~CURRENT_DATE || CURRENT_TIME IS CURRENT_TIMESTAMP >= FALSE > CURRENT_DATE); CREATE TABLE seed_a(c UNI
```

---

## Crash 55: `2b461bc4cade9022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023641`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT -871117458087959899336525929688783640280369.122582918388780344419827042303096656193294893071850600754, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 56: `4dd3c5cc8b0df5d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023690`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP))) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 57: `5301f306176dcad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023698`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES (-541764.27543 NOT BETWEEN TRUE AND CURRENT_DATE); PRAGMA integrity_check; CREAT
```

---

## Crash 58: `b18ac4bcfd8d981e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023709`

```sql
SELECT substr('c-_- __-k1u_', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 59: `cdf9efebe133114a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023740`

```sql
SELECT printf('%.*s', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 60: `b79ee48311c5f003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026203`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY, c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); IN
```

---

## Crash 61: `57ae56c057550dae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027054`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 62: `5ee072f0c8efbf44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028357`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) UNION ALL SELECT DISTINCT NULL FROM p ORDER BY NULL DESC NULLS FIRST; PRAGMA int
```

---

## Crash 63: `5ae8a3034e1605fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029409`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH RECURSIVE q AS (VALUES (FALSE)) SELECT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 64: `9a54aed129d67723` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029440`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (FALSE)) SELECT * FROM json_each
```

---

## Crash 65: `f40091e4350639b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029534`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'', a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 66: `3a6001c448d30e60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030292`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 67: `38f7bf803d699fb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033657`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT OR FAIL INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 68: `a10345560ffd5b42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033896`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT X'bdfD209fEf', a REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 69: `aad351d54f9bac42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033907`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT TRUE COLLATE NOCASE AS a FROM json_tree('[{"a":1},{"b":2}]') ORDER BY TRUE DESC NUL
```

---

## Crash 70: `996d3a577dcd46fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033913`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (TRUE = CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 71: `40a52f09adfccf68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033948`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_tree('{}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 72: `d3a65ee17b8fa225` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033963`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL DEFAULT -30.57636300328023944222283053146236589e-62060787373811106604543); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 73: `d7c8d2cba5d1f237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033970`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (length(CURRENT_TIMESTAMP)), c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 74: `766ca992621fb67a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034465`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 75: `07221a9954217d81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036379`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 A
```

---

## Crash 76: `26598cfe55d7762b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036914`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * UNION SELECT * ORDER BY CURRENT_DATE ASC NULLS FIRST INTERSECT SELECT * FROM json_tree('{}') WHERE CUR
```

---

## Crash 77: `d082af22a1901cbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039756`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); SELECT ALL * FROM p AS p_ CROSS JOIN json_tree('[{"a":1},{"b":2}]') NATURAL LEFT JOIN p NOT INDEXED; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 78: `9597d9cb2bd59853` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040406`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * UNION ALL SELECT * ORDER BY NULL ASC NULLS FIRST INTERSECT SELECT * FROM t1 WHERE TRUE GROUP BY FALSE 
```

---

## Crash 79: `2d624fa7d5a43c90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040607`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 A
```

---

## Crash 80: `afbf959f912b0c7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041088`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 81: `9d93500b440d8aa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041190`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 82: `8fa19a5a36c72768` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 83: `599522f2786b2dd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045397`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 84: `45b9b843030a5ae1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045607`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE * -CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); INSERT INTO
```

---

## Crash 85: `cb7bb257177a93bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045825`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE * CURRENT_DATE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEF
```

---

## Crash 86: `194d0ae254375408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046095`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE * FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VA
```

---

## Crash 87: `228d15a97a6deec9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049771`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CAST(CURRENT_DATE AS INT)); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 88: `c33e66911626361b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050082`

```sql
SELECT substr('Bh F-  5', -2147483648, 9223372036854775807); CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); VALUES (row_number() OVER ()); CREATE TABLE 
```

---

## Crash 89: `5087994b249337b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052237`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE OR CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP
```

---

## Crash 90: `a06db799bb78c998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052261`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 91: `fef8731d10ff4bc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052410`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT -4742063220257680706999044552198739838373939670037862085497910913201018123790272430865573592195.88e+83, a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); I
```

---

## Crash 92: `4e68b4bee06b48a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052422`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'', a VARCHAR(255) UNIQUE, c2 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 93: `16e4b94c04d09d3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052428`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'', a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(DISTINCT CURRENT_TIMESTAMP)) INTERSEC
```

---

## Crash 94: `331dc238ca5e756f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052465`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(b REAL, a REAL UNIQUE); SELECT TRUE FROM q NATURAL JOIN p WHERE NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 95: `0e6683279ce16812` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052500`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'', a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY 
```

---

## Crash 96: `0b7e0012cab4f647` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052507`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME IS CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 97: `438cc28515fb31c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052605`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT FALSE, a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMAR
```

---

## Crash 98: `c9def162aa0dd678` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053656`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE I
```

---

## Crash 99: `abecbc94bfffb5ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054452`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (-CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 100: `8a516959359c7534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054884`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE << CURRENT_TIME IS NOT NULL) UNION ALL SELECT DISTINCT NULL FROM p ORDER BY NULL 
```

---

## Crash 101: `13f5ac9c514d1151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054905`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) UNION SELECT DISTINCT NULL FROM p ORDER BY NULL DESC NULLS FIRST; PRAGMA integri
```

---

## Crash 102: `1190f39158dd0370` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054936`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); VALUES (row_number() OVER (PARTITION BY CURRENT_DATE ORDER BY NULL ASC ROWS BETWEEN NULL PRECEDING AND CU
```

---

## Crash 103: `992da657d52baa9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054967`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED GROUP BY FALSE ORDER BY random() OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIME
```

---

## Crash 104: `98369e2344ab46d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054980`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) UNION ALL SELECT DISTINCT NULL FROM p AS p_ CROSS JOIN json_tree('[1,2,3]') NATU
```

---

## Crash 105: `fbcf29b0643c61d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054987`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) UNION ALL SELECT NULL ORDER BY NULL DESC NULLS FIRST; PRAGMA integrity_check; CR
```

---

## Crash 106: `dd6ffa441e63b68b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055003`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 
```

---

## Crash 107: `c205a6af4a10f917` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055031`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) INTERSECT SELECT DISTINCT NULL FROM p ORDER BY NULL DESC NULLS FIRST; PRAGMA int
```

---

## Crash 108: `81bb42c6035433f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055054`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT -0); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE) UNION ALL SELECT DISTINCT NULL FROM p ORDER BY NULL DESC NULLS FIRST
```

---

## Crash 109: `4d9cadd84958a7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055207`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE random(); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 110: `dfd9d33af93b7d77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055414`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP * -CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE T
```

---

## Crash 111: `c5ced3b0222ae4e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055608`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL) A
```

---

## Crash 112: `6a3bb01129ecc97a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055665`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH r (c3) AS (SELECT *) VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 113: `183d92ee9659c337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056122`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY
```

---

## Crash 114: `e137aaf4781a5d1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057502`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP AND 0, CURRENT_DATE); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_chec
```

---

## Crash 115: `f8941861f8a96e26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT json_valid(TRUE NOT IN (VALUES (FALSE) INTERSECT SELECT * ORDER BY FALSE ASC NULLS FIRST)) FI
```

---

## Crash 116: `398aefa5dff532db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057539`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 117: `56d94d43fcf69f08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057548`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS () ORDER BY 
```

---

## Crash 118: `30d9a27de9c536fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057554`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP OR CURRENT_DATE <= CURRENT_TIME
```

---

## Crash 119: `b6bf5e5fb4582469` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057565`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIMESTAMP FROM p AS p_ CROSS JOIN json_tree('[1,2,3]') NATURAL LEFT JOIN json_each(NULL, '$') 
```

---

## Crash 120: `2b201a1b4a88a967` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057571`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 121: `068ff0f4b0f8f88e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057594`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIMESTAMP AS f73mhp11ey9_249i73_52p0f20___20924i28_4fr3_pc92_1wd88k5u_f6__s926_5__8_k8iu2 FROM
```

---

## Crash 122: `d406eb8c516d55bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057601`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EX
```

---

## Crash 123: `6bee8521e163bf81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057610`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 124: `f12b8b61a88876bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057707`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 125: `f714a731b62a1170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057795`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (NULL LIKE FALSE); PRAGMA integrity_check; CREATE 
```

---

## Crash 126: `d12d066c184d9e9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062083`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 127: `0a4b17881a7d4a1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062100`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); VALUES (upper(CURRENT_TIME)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 128: `c5e47531a7a304ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT -4742063220257680706999044552198739838373939670037862085497910913201018123790272430865573592195.
```

---

## Crash 129: `5ac49afdb48c7087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069439`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (NULL IS NOT CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 130: `b7dc6031fda2d89a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069463`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC ROWS BETWEEN TRUE PRECEDING AND CURRENT ROW), TRUE
```

---

## Crash 131: `19678b993a7ac342` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069485`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES ((SELECT NULL AS a LIMIT CURRENT_DATE)); PRAGMA quick_check; CREATE TABLE seed_a
```

---

## Crash 132: `c2674add00520090` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069492`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT CURRENT_TIMESTAMP FROM json_tree('[{"a":1},{"b":2}]') CROSS JOIN json_tree(NULL, '$[#-1]')
```

---

## Crash 133: `ea4b0e6bb444406f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069505`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED GROUP BY FALSE ORDER BY random() OVER (PARTITION BY NULL ORDER BY CURRENT_TIMESTAMP ASC NULL
```

---

## Crash 134: `965e6ebafab07c74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069526`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (NULL >> CURRENT_DATE)); VALUES (NULL || CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 135: `08c644b190e1f5a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069540`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT DISTINCT * FROM json_each('[]') CROSS JOIN p NATURAL LEFT JOIN json_each(NULL, '$'); CREAT
```

---

## Crash 136: `082ea52b5a92b24b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078612`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (NULL & CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 137: `27f3fb5ccd6f914d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078618`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 138: `58f6d5d48062a6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078638`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE NULL IS NOT CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 139: `398a2090b4842dea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078649`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CASE CURRENT_TIMESTAMP WHEN NULL THEN TRUE ELSE FALSE END); CREATE TABLE seed
```

---

## Crash 140: `50247ef286f0d182` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078674`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL NOT IN (WITH q AS (VALUES (FALSE)) SELECT CURRENT_DATE AS e_54rp_8tj_0d___2___ FROM json_each('[1,2,3]') WHER
```

---

## Crash 141: `b25cb2d5318b3a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078832`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME IN (VALUES (CURRENT_TIME)) FROM (SELECT * FROM p WHER
```

---

## Crash 142: `fd21041e96995660` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC ROWS BETWEEN TRUE PRECEDING AND CURRENT ROW), TRU
```

---

## Crash 143: `f8b6cdf0517f8f75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082085`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES (TRUE >= 471194370091696177992746.047404136955787377527334485605546205962069711)
```

---

## Crash 144: `7dd7f31ac7065213` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082117`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN SELECT * FROM json_each('[]') GROUP BY FALSE ORDER BY CURRENT_DATE COLLATE BINARY DESC NULLS LAST LI
```

---

## Crash 145: `2dbc0eb2e95db6b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_each(CURRENT_TIMESTAMP / CURRENT_TIMESTAMP, '$'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 146: `fe8337ae8709102f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082234`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION SELECT * FROM p INDEXED BY c3 WHERE TRUE GROUP BY FALSE WINDOW w1 AS () ORDER BY CURRENT_TIMESTAMP
```

---

## Crash 147: `111f310408136718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION SELECT * FROM t1 WHERE TRUE GROUP BY FALSE WINDOW w1 AS (PARTITION BY CURRENT_DATE ORDER BY NULL A
```

---

## Crash 148: `2f02fcb33b1d3214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082287`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT ' '); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 149: `01846d6253c31640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082329`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION SELECT * FROM ((SELECT DISTINCT typeof(CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIME NOTNULL 
```

---

## Crash 150: `c76cc6f39a3712cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082449`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES (CAST(X'' AS INT) IS CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 151: `58c9c9331d9e1fa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082504`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (EXISTS (VALUES (NULL) EXCEPT VALUES (NULL))); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 152: `768fe07d846e6b10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082639`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ROLLBACK INTO p VALUES (NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json
```

---

## Crash 153: `63bdbea50c72d760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083244`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE COLLATE BINARY) UNION SELECT ALL * FROM p AS m2_h ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT FAL
```

---

## Crash 154: `73985d87b5c0844f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083263`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (max(NULL) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 155: `6809e2f43abe5375` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000000490`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 156: `4acd05ccb425441d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001932`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 157: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001941`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 158: `d7112703441051dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001948`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 159: `6a26157d27070457` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002398`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 160: `275fb888a989f67a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003709`

```sql
SELECT printf('%.*g', 2147483648, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 161: `69668412e9a023e4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004374`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE, c3 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 162: `bcee0f1c5c8ddbc4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004552`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT -871117458087959899336525929688783640280369.122582918388780344419827042303096656193294893071850600754, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 163: `1b01fed2258dd97f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004588`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT TRUE, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 164: `e1af9530fd3fce8c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004600`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 165: `6f4e3b10f82fa5b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004643`

```sql
SELECT round(0.01, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 166: `4cc82de3094e4cd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004724`

```sql
SELECT substr('70 Kfx_ -6', 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 167: `f397e045295d9b39` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006536`

```sql
SELECT round(1e-308, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 168: `a1101cd2b2e2de53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008516`

```sql
SELECT round(-1e308, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 169: `92e79dffcf3451a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008524`

```sql
SELECT round(0.01, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(
```

---

## Crash 170: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008530`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 171: `776656bcf04abc95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008540`

```sql
SELECT printf('%f', -2147483648, 'E_6j_2_z-61 fr___'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 172: `e31d55046be0e458` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008547`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE NOT BETWEEN TRUE AND CURRENT_TIME NOT NULL); PRAGMA quick_check; C
```

---

## Crash 173: `1a8840ec3c8327d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008554`

```sql
SELECT substr('_c-b_-740- _A-_', 9223372036854775807, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 
```

---

## Crash 174: `b4c942a28a464a68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008561`

```sql
SELECT round(-1.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 175: `09d9087eb5349e3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008571`

```sql
SELECT printf('%.*f', 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 176: `5f034909e1a3f5ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008580`

```sql
SELECT substr('', 4294967295, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 177: `6bc89d97ac6be4a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008602`

```sql
SELECT printf('%x', 2147483647, 'vJdm-7-_4'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123)
```

---

## Crash 178: `c0c4cb3227461e8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008610`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 179: `bfaed22d4dc86453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008622`

```sql
SELECT round(1e308, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 180: `8abc2e0a8f90df05` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008633`

```sql
SELECT printf('%lli', -9223372036854775808, 'K-vp _uxj6_-HCD2_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 V
```

---

## Crash 181: `6a0f11675accc6b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008659`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 182: `bdab642d5bf27614` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008691`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 183: `739ec96142d9b15f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009170`

```sql
SELECT printf('%.*g', 4294967296, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 184: `4f2052a197e5a873` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009205`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (NULL < CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 185: `ed2de07c30f993b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009220`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p (rowid) VALUES ((WITH RECURSIVE p AS (VALUES (NULL)), q AS (VALUES (FALSE)) SELECT * FROM q)); PRAGMA quick_check; CREATE TABLE seed_
```

---

## Crash 186: `2ee79b1ec9acfb7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009236`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT X'eF', c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 187: `afdd62eef485b66e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009253`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 188: `61b9751f5e78116e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009265`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -700504.12E7); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 189: `9d5c8e6e3729db5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009283`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT '-47 o'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 190: `68f1eaf7671dcf25` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009315`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, a BLOB NOT NULL DEFAULT -0); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 191: `d62c3cf91c9c0b62` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009345`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 192: `06fd5cf1bb3b4205` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009532`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, a BLOB NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 193: `870dad5262dddc0f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009555`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 194: `6970fc40bb365e30` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009575`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 195: `0533173599780039` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009594`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p (rowid) VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 196: `32840a20d3bb20eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009622`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE, c2 BOOLEAN PRIMARY KEY, c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREAT
```

---

## Crash 197: `a71eb4903d5eead4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009635`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 198: `71ce21d3f218dc68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009646`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT 2316059638599549987942100410082303938937528147979238347704841032770268883221658368318299668050388582566247788146.62114226957181516244605675E3291068839746464
```

---

## Crash 199: `083e8fa20c97c509` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009657`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (TRUE), a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 200: `9d2ae919023eeae7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009683`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT TRUE, a INT); INSERT INTO p (rowid) VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 201: `1dee2cce8ef38807` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009748`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT '', a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 202: `b282dbe242e0e2fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009793`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'', a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 203: `b376a5a090097f13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009805`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT TRUE, b REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 204: `413efe1ebd3cbbf6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009813`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT TRUE, a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT TRUE, a INT); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 205: `5a21a0df2e717468` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019252`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (~NULL & CURRENT_TIMESTAMP || TRUE >= CURRENT_TIMESTAMP > NULL); CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 206: `5f3ed13df6739acd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019304`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (~FALSE || CURRENT_TIME IS CURRENT_TIMESTAMP >= +CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 207: `b72209fd8e7cc33a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019328`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (~FALSE || CURRENT_TIME IS CURRENT_TIMESTAMP >= NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 208: `8177b43281bbc1a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025774`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 209: `fd598d8800e80442` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME <> CASE WHEN CURRENT_TIMESTAMP OR CU
```

---

## Crash 210: `ac240881c38e28a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027317`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_DATE AS INT)); PRAGMA quick_check;
```

---

## Crash 211: `c3db32e8da737603` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027332`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p (rowid) VALUES ((VALUES (NULL))); PRAGMA quick_check; CREATE TABLE 
```

---

## Crash 212: `31eb7be7a7ab9613` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027356`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM p AS p_ CROSS JOIN p NOT INDEXED NATURAL LEFT JOIN json_each(CURRENT_TIMESTAMP / CURRENT_TIM
```

---

## Crash 213: `f9d6bf0456b9345d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027393`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 214: `58f65fe7c873a5ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027407`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (EXISTS (VALUES (NULL) UNION ALL VALUES (NULL))); 
```

---

## Crash 215: `eeb428d034483398` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027516`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (b) VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE
```

---

## Crash 216: `6ead67eb24d4870c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027582`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (VALUES (NULL)), q AS (VALUES (FALSE)) VALUES (NULL); INSERT INTO p (c3) VALUES (CURRENT_TIME); PRAGMA quick_
```

---

## Crash 217: `0c0e9966948d7e4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028460`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT '_69h9ws1Rc JV__ -L', a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 218: `4447366716d4923e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028466`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT -871117458087959899336525929688783640280369.122582918388780344419827042303096656193294893071850600754); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT IN
```

---

## Crash 219: `b36ab5a3f9abee4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028589`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_each('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 220: `14bfa7c6b1896bd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028750`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT FALSE AS a FROM json_tree('[{"a":1},{"b":2}]
```

---

## Crash 221: `91a71abccc853e92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028759`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME IN (CURRENT_TIMESTAMP, TRUE COL
```

---

## Crash 222: `3ba515a9aa24b688` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028765`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t1 JOIN p NOT INDEXED ON CURRENT_TIME UNION ALL SELECT * ORDER BY NULL ASC NULLS FIRST; INSERT INTO 
```

---

## Crash 223: `6e8cdf2903fe1e50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028781`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -700504.12E7); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 224: `e09575a9d0b38d32` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028805`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (-TRUE), c2 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 225: `977a9a44dc8e27d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028837`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN CHECK (last_insert_rowid())); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 226: `a7383aeb14e51f7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028844`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]') ORDER 
```

---

## Crash 227: `d7b2e58d3f9eb3c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028859`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 228: `04ca5aa2af7994c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028865`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_DATE AS INT) IS CURRENT_TIMESTAMP); PRAGMA integrity_check; CR
```

---

## Crash 229: `db8698f49d8a12a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028938`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE
```

---

## Crash 230: `c386d459755b181e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028944`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE
```

---

## Crash 231: `d5d26788ef46a23c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029770`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[]') GROUP BY FALSE ORDER BY FALSE DESC NULLS L
```

---

## Crash 232: `4d847015f6057bab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029784`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 233: `7c4de92e4915e0e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029790`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE NOT BETWEEN NULL AND NULL); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 234: `56f85d9ed456550b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029801`

```sql
SELECT printf('%.*s', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 235: `021187523cb90c1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029813`

```sql
SELECT substr('_-- 7', 4294967296, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44
```

---

## Crash 236: `fe06214e50a2cdd3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033081`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') GROUP BY NULL, CURRENT_DATE; INSERT INTO p (rowid) VALUES ((VALUES (NULL))); PRA
```

---

## Crash 237: `8cde4e190e52601d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033095`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') GROUP BY NULL, CURRENT_DATE; INSERT INTO p SELECT TRUE FROM json_tree('[]') GROU
```

---

## Crash 238: `cd3785022c3f523f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033304`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (FALSE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t
```

---

## Crash 239: `f83933dd560e1d25` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034081`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (length(CURRENT_TIMESTAMP + TRUE) NOT NULL)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 240: `0a96269349379178` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034097`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT X'bdfD209fEf'); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 241: `d0ce587da5de401f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT rank() FILTER (WHERE CURRENT_TIMESTAMP) OVER w7, *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integ
```

---

## Crash 242: `43afa9af3238942f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034143`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (nullif(TRUE, FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 243: `f731ef3a22e13c00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034160`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (FALSE)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TAB
```

---

## Crash 244: `0787857615ce45ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034229`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X'EA'); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 245: `5c042400c4397f8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038727`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); WITH RECURSIVE p (c1) AS (SELECT *) INSERT INTO q VALUES (CURRENT_TIME); PRAGMA quick_chec
```

---

## Crash 246: `98d1cdb77e79237b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038758`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE NOT BETWEEN TRUE AND NULL); PRAGMA quick_check; CREAT
```

---

## Crash 247: `ae54527b79970dc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038769`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY TRUE, NULL ORDER BY NULL ASC LIMIT NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 248: `d19f72451f9ec48c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046418`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT 2316059638599549987942100410082303938937528147979238347704841032770268883221658368318299668050388582566247788146.6211422695718151624460567
```

---

## Crash 249: `f20beb4b1a17ead4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X'EA'); INSERT INTO p SELECT TRUE FROM json_tree('[]') GROUP BY TRUE; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 250: `2e3f8ef5e2f1cb78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046443`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT -4742063220257680706999044552198739838373939670037862085497910913201018123790272430865573592195.88e+83); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 251: `bc36b10fa17799ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046502`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT -009141712312.5); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 252: `acd5d932df255022` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046536`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X'EA'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X'EA'); INSERT
```

---

## Crash 253: `834f01214a5b3cfb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047350`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS () ORDER BY C
```

---

## Crash 254: `430ff8f65e4926be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047382`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY NULL, CURRENT_DATE WINDOW w1 AS
```

---

## Crash 255: `2d6bb961c898bb60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047393`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP COLLATE BINAR
```

---

## Crash 256: `ed2cd2f69bd76ca0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047499`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE NOT IN (TRUE)) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 257: `484786236003380c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047507`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT FALSE LIKE CURRENT_TIMESTAMP ESCAPE TRUE FROM q GROUP BY NULL INTERSECT VALUES (CURRENT_DATE); CREATE TA
```

---

## Crash 258: `cde2260c30354e8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047565`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') GROUP BY NULL, CURRENT_DATE; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP
```

---

## Crash 259: `0f11104fb478b14a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049688`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY
```

---

## Crash 260: `bd377833cc66ee39` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052096`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP | CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 261: `b4b3dc0bf25a1f79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052126`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE TRUE BETWEEN TRUE AND CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 262: `1986cbf86ccd6995` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053262`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT '6'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 263: `e60fc0ac1dde1d53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053277`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL CHECK (CURRENT_TIMESTAMP IS NOT FALSE)); CREATE TABLE IF NOT EXISTS q(c2 INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 264: `97f2af12214cf116` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053291`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -700504.12E7); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (max(NULL)) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 265: `c381c774e3bfcdbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053323`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL), a DATE CHECK (NULL < CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 266: `70635ba585cb26d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053383`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT '  5-Q_A6 __ z__'); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 267: `8c936782085aab80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053416`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL CHECK (NULL IS NULL < CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 268: `aededc0d3da385ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053430`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL CHECK (NULL BETWEEN CURRENT_TIMESTAMP AND FALSE >= TRUE >= TRUE >= TRUE >= TRUE)); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 269: `bae075c12b6e592d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053466`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS LAST, max(NULL) FILTER (WH
```

---

## Crash 270: `e9f785e107febd5c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053506`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL CHECK (TRUE IS TRUE)); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 271: `5353fda83ab4aad9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054428`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE * -CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 272: `c7f48bda19ade11a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054538`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE json_remove('{}', '$.a[-0]'); CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 273: `8332c69751c4e148` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054562`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_each('[1,2,3]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 274: `b9be49330b0d92bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054575`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM json_tree('[1,2,3]') LEFT JOIN q ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 275: `b8da010adb443cdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054612`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 276: `c5df81baf062c441` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054751`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM json_each('[]') CROSS JOIN json_tree(NULL, '$[#-1]') NATURAL LEFT JOIN p NOT INDEXED; CREATE
```

---

## Crash 277: `51d00010628dca6c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054759`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT X'f9dB', a INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 278: `c8f32baf737d4f61` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054779`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE json_remove('{}', '$'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 279: `e77c16fa056c02c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057089`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (b) VALUES (CURRENT_TIMESTAMP - CURRENT_TIMESTAMP - NULL); 
```

---

## Crash 280: `05777092dfa4e7f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057110`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS LAST, count(DISTINCT NULL)
```

---

## Crash 281: `ee5a4b52b6d45972` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057142`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); SELECT DISTINCT * FROM json_each('[]') CROSS JOIN p NATURAL LEFT JOIN json_each(NULL, '$') ORDER BY TRUE DESC N
```

---

## Crash 282: `4933037e140acc2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057248`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR ABORT INTO q VALUES (CAST(CURRENT_DATE AS NUMERIC)); PRAGMA qui
```

---

## Crash 283: `b6fd35adc7aba1b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (c1) VALUES (CURRENT_DATE) ON CONFLICT(rowid) DO UPDATE SET
```

---

## Crash 284: `c4313a89c8241f8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (c1) VALUES (CURRENT_DATE) ON CONFLICT(c1) DO UPDATE SET c
```

---

## Crash 285: `f1a592a83fd66d1c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057332`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (c1) VALUES (CURRENT_DATE) ON CONFLICT(_rowid_) DO UPDATE S
```

---

## Crash 286: `71c7bf465f92063c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057343`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (c1) VALUES (CURRENT_DATE) ON CONFLICT(c1) DO UPDATE SET ro
```

---

## Crash 287: `6105283ad136ec23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057378`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 TEXT PRIMARY KEY, _rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p (c1) VALUES (CURRENT_DATE) ON CONFLICT(c1) 
```

---

## Crash 288: `71e808a4ad0dc1e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059815`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT CURRENT_TIME NOT IN (FAL
```

---

## Crash 289: `861164a2bb274531` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059825`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME) EXCEPT SELECT CURRENT_TIMEST
```

---

## Crash 290: `8a644b166ef38855` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059837`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{}') W
```

---

## Crash 291: `498ca0f19799e36e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059863`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); VALUES (cume_dist() OVER ()); CREATE TABLE seed_t1
```

---

## Crash 292: `928a793532b06aec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059869`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT TRUE << CURRENT_TIME IS NOT NULL AS j_ FROM
```

---

## Crash 293: `63aec4342006c066` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059881`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP FROM j
```

---

## Crash 294: `bc71965fc818b70e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059892`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 295: `9126325e0fa078f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068875`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT FALSE AS a FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 296: `8d338b09c7c60423` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068883`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIME IN (SELECT * FROM json_each('[1,2,3]') GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIME); VALUES (FALS
```

---

## Crash 297: `148fd25e1d23f580` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068889`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIMESTAMP FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_TIM
```

---

## Crash 298: `4c10c9918539be7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068898`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CURRENT_TIME IS CURRENT_TIMESTAMP >= count(DISTINCT CURRENT_TIMESTAMP)); CREATE TABLE seed_t1
```

---

## Crash 299: `b25a0a909a270e23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068906`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_TIMESTAMP FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE WINDOW w1 AS ()
```

---

## Crash 300: `373c619453affc1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068916`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CAST(CAST(CAST(CAST(CAST(CAST(NULL AS INT) AS INT) AS INT) AS INT) AS INT) AS INT) IS CURRENT
```

---

## Crash 301: `987d356021710901` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068927`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_DATE FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 302: `188caf90fb13130f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068935`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CURRENT_TIME IS max(NULL) OVER () >= NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 303: `1ff445880869bd84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068946`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (), TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 304: `b938df441d82a8bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068956`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CURRENT_TIMESTAMP + TRUE >= NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 305: `b86d755cd0cae98a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068962`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT NULL LIMIT FALSE IS NOT NULL OFFSET CURRENT_DATE NOT LIKE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 306: `2da03a2f76a51ef1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068968`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CURRENT_TIME IS TRUE IS TRUE >= NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 307: `b4fe6b03a6bea603` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069012`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIMESTAMP WIND
```

---

## Crash 308: `1cff3cbb61b16f97` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069025`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME NOT BETWEEN TRUE AND CURRENT_TIME NOT BETWEEN TRUE AND TRUE NOT BETWEEN TRUE AND NULL NOT
```

---

## Crash 309: `69d985d197fb3f6c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069033`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE || CURRENT_TIME IS CURRENT_DATE NOT IN (VALUES (-NULL)) >= NULL); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 310: `5411cee231a0ed06` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069051`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.*; VALUES (FALSE || CURRENT_TIME IS CURRENT_TIMESTAMP >= NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 311: `1b39c7e4e0b6a250` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069247`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT max(NULL) FILTER (WHERE TRUE) AS a FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c
```

---

## Crash 312: `b282a143bea10b63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069263`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 313: `6e9ae39a1a4e89f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069275`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p SELECT ALL * FROM p; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 314: `c5fff094600b9713` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069296`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE COLLATE BINARY) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 315: `c2996ecd75598c4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069420`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 316: `8bc28dd6c969fd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082355`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION SELECT * FROM json_tree(EXISTS (SELECT RAISE(IGNORE) UNION ALL SELECT NULL FROM p NOT INDEXED WHER
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  yy_reduce
  sqlite3Parser
```

---

## Crash 317: `835ffb4e82885897` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087376`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE COLLATE RTRIM NOT NULL) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b V
```

---

## Crash 318: `b0765de74ca2a197` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089246`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME NOT IN (FALSE) FROM (SELECT * FROM p WHERE NULL) AS s
```

---

## Crash 319: `54c2924dca393f53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089254`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE, c2 BOOLEAN PRIMARY KEY, c1 BOOLEAN CHECK (length(CURRENT_TIMESTAMP + 5120527694.80e+9531893))); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); 
```

---

## Crash 320: `358b36a3bb46f6ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089285`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE, c2 BOOLEAN PRIMARY KEY, c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB CHECK (json_object(' h Z3t  _ 4', NULL))); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 321: `32361f916efcc3ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089315`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE, _rowid_ BLOB CHECK (rowid >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE), c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid B
```

---

## Crash 322: `fb7d04efca35fdda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089343`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE, c1 DATE NOT NULL DEFAULT X'd8d0bb'); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TA
```

---

## Crash 323: `a521da38b441956b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089451`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (rowid >= TRUE >= TRUE >= TRUE >= TRUE), a INT); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE T
```

---

## Crash 324: `0b37eebfb3b9aec8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089468`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_DATE MATCH TRUE)); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 325: `23d3dc16ae6a0a9b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089507`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (rowid >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE), a INT); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick
```

---

## Crash 326: `45e31e3e895a381f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000089528`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL DEFAULT X'F2d8A5'); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 327: `1f3e863814cd5840` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090062`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT '', a INT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (CURRENT_TIME) INTERSECT VALUES (FALSE)) AS zt_ JOIN p ORDER BY
```

---

## Crash 328: `ac0c98fe0b70f600` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090072`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (NULL > CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 329: `d55bd9a87248bc1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090085`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (rowid >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE), a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 330: `db85e28236626e92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090091`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (p.c3)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t
```

---

## Crash 331: `447faaf17606c4dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090101`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE TRUE = CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 332: `77125a4bc03d7f7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090111`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM p UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 333: `2c0dc9c6a4eee2fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090227`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT ' e2 _Ewbu', a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 334: `2e62ea8d2170f651` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090264`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (length(X'a0dF12CBfa30CF')), a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 335: `699b3cee4bb657fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000090273`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT ' -y', a INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---
