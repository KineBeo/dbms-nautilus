# Crash Triage Report

**Total crashes:** 396  
**Unique crash sites:** 396  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 250 | 250 | 63% |
| Signal | 146 | 146 | 36% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `0ea98a2755af3f20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000357`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); WITH RECURSIVE q (c1) AS (SELECT q.* FROM json_tree(CURRENT_TIMESTAMP, '$[#-1]') LEFT JOIN p NOT INDEXED LEFT JOIN json_tree('[1,2,3]') LI
```

---

## Crash 2: `df37f8195004af93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000665`

```sql
SELECT printf('%.*g', -9223372036854775808); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p JOIN p fn8_ ON NOT RAISE(IGNORE); CREATE TABLE
```

---

## Crash 3: `8c251fdeb7fbdc62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000731`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT TRUE NOT BETWEEN TRUE AND TRUE AS k FROM q NATURAL JOIN t3 WHERE c
```

---

## Crash 4: `d8c437703522041f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000960`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT OR REPLACE INTO p VALUES (jsonb_remove('{}', '$[0].c') OVER (ORDER BY CASE WHEN count() OVER () THEN NULL COLLATE NOCASE ELSE CASE CU
```

---

## Crash 5: `3cbcbeef838024c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000981`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 6: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001441`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 7: `fbcbf8d8acdf8da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001531`

```sql
SELECT substr('_-W_-  D--J_W---D-', 9223372036854775807, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT TRUE NOT NULL C
```

---

## Crash 8: `6cec83a2a1460be2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001813`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT p.*, CURRENT_TIMESTAMP || FALSE IS c2 << RAISE(IGNORE) + RAISE(IGNORE) IS DISTINCT FROM TRUE
```

---

## Crash 9: `f3d220ad7c85437c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002053`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 10: `62177f1092af109c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002130`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE see
```

---

## Crash 11: `036a312f8c7db30b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002325`

```sql
SELECT printf('%u', 0, ' b1_N '); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 12: `060789850dc33747` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002350`

```sql
SELECT printf('%u', 0, ' b1_N '); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_
```

---

## Crash 13: `941487a85a6d356f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002360`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p DE
```

---

## Crash 14: `11150c378e432811` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002374`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 15: `ff550518e6b63cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002675`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT UNIQUE); INSERT IN
```

---

## Crash 16: `e0ae7d3b54ff3da1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002681`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 17: `af3876c6b5cf8301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003092`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (EXISTS (VALUES (CURRENT_TIME)), CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 18: `25225b05a9aa1df2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003160`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL, CURRENT_DATE <= count(*) FILTER (WHERE CURRENT_TIME)); CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 19: `ab2919eb09b9b30d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003167`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE <= count(*) FILTER (WHERE CURRENT_TIME)); CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 20: `53544c0d475bf9ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003175`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL, CURRENT_DATE <= CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_
```

---

## Crash 21: `07437d781a5f9d59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003205`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL, CURRENT_DATE <= NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 22: `4b93bdac384e0350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003281`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE CURRENT_DATE END, FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 23: `67b4e4333997f893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004197`

```sql
SELECT round(-1e308, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 24: `c9f5d8ac43c9ffe2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004306`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 25: `f2ce3827b75fa735` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004813`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_
```

---

## Crash 26: `0c9832fe2c14ec1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005295`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION SELECT DISTINCT * FROM json_tree('[1,2,3]') WHERE TRUE; INSERT INTO p DEFAULT VALUES
```

---

## Crash 27: `a4f98a1356df14e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006296`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 28: `3d975afc511fe469` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007627`

```sql
SELECT printf('%f', 1, 'B  -1--Q85'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); SELECT CASE -TRUE IN (VALUES (FALSE)) WHEN RAISE(IGNORE) COLLATE NOCASE NOT BETWEEN CURRENT_TIMESTAM
```

---

## Crash 29: `d760316a4da0abae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007761`

```sql
SELECT round(-1e308, 2147483648); SELECT printf('%.*g', 4294967296, 0.01); SELECT hex(zeroblob(0)); SELECT substr('-8MgP-I_p_pa-_u', 9223372036854775807, -2147483648); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 30: `3429c24a92136e9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009952`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT +RAISE(IGNORE) GLOB CURRENT_TIMESTAMP FROM jsonb_each('{"a":{"b":1}}') EXCEPT SELECT DISTINCT * FROM js
```

---

## Crash 31: `3a823db46365ec8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009988`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT +RAISE(IGNORE) GLOB CURRENT_TIMESTAMP FROM jsonb_each('{"a":{"b":1}}') EXCEPT SELECT * FROM p WHERE CUR
```

---

## Crash 32: `1f310c676b961ed0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012852`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) 
```

---

## Crash 33: `4d69e11c9b8a731e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013018`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VI
```

---

## Crash 34: `6645ca9d73a77e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013175`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 35: `28cb59298cccc1bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013211`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH q AS (SELECT *) SELECT DISTINCT * FROM jsonb_each('[]') LEFT OUTER JOIN p AS zb LEFT OUTER JOIN jsonb_tree('{}')
```

---

## Crash 36: `a4118be2676a120c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013226`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_
```

---

## Crash 37: `cc349f062e7137c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013272`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL CURRENT_TIME IN (NULL), * FROM json_tree('[{"a":1},{"b":2}]'); SELECT * FROM p NATURAL JOIN p WHERE CAS
```

---

## Crash 38: `b982ec819eee7335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013281`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN FALSE NOT BETWEEN NULL AND CURRENT_TIMESTAMP THEN CURRENT_TIME END; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 39: `229606cc25304290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013422`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 40: `61519508613583f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013535`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 41: `eb281a8e68c9e89b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013547`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE FALSE NOT BETWEEN NULL AND CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UN
```

---

## Crash 42: `f4ad81af2ccd51b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013635`

```sql
SELECT printf('%.*d', 9223372036854775807, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 43: `291bd7f557249ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013726`

```sql
SELECT printf('%x', 4294967296, 'P-w_'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 44: `6357720244df7f6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014543`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) UNION ALL VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_
```

---

## Crash 45: `1ec28e2c5d0af595` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014551`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM jsonb_each('{"a":{"b":1}}') NATURAL LEFT JOIN (q INDEXED BY rowid) NATURAL LEFT JOIN p INDEXED BY b LI
```

---

## Crash 46: `ae1ffddf419e86c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014563`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) INTERSECT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_
```

---

## Crash 47: `8b7d9d1be7166173` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014574`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (FALSE LIKE TRUE) EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JO
```

---

## Crash 48: `1ad635e3a5bdac74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014591`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (FALSE < CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 49: `ac9f6c69a1165716` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014599`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (FALSE)) VALUES (CURRENT_DATE) EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 50: `f7f647d47d70e993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014641`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (-NULL) EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a 
```

---

## Crash 51: `d21a07dc7f4dbb99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014650`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (CAST(CAST(CAST(CAST(CAST(CAST(CAST(CURRENT_TIMESTAMP AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS F
```

---

## Crash 52: `fa8e071d245d82e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014658`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) UNION VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WH
```

---

## Crash 53: `16f91114cd91367e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014713`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b, c1, a); VALUES (NULL) EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 54: `f0ba4fb7252a726d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014739`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT json_patch('{"a":1}', '{"a":{"b":1}}') EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 55: `cea514062453b9fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014806`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT changes() EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_
```

---

## Crash 56: `e24b1cdf7a7acfb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014938`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (CAST(CAST(CAST(CAST(CAST(CAST(CAST(CAST(CURRENT_TIMESTAMP AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT))
```

---

## Crash 57: `413e6057c1858b4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014962`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (CURRENT_DATE >= NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 58: `4ca750b37494afd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014969`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (NULL <> FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 59: `3d07f15d8eedf350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL DEFAULT -948999301.158532594399517E-9157784527566534955999); VALUES (NULL) EXCEPT VALUES (CURRENT_TIME); CREAT
```

---

## Crash 60: `5cf1f33a23335143` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015032`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT FALSE * NOT CURRENT_TIMESTAMP IS FALSE FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () EXCEPT VALUES 
```

---

## Crash 61: `03bb6b1855fd45c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015038`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT FALSE * NOT CURRENT_TIMESTAMP FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () EXCEPT VALUES (CURRENT_
```

---

## Crash 62: `65f0eebb5b716068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015107`

```sql
SELECT round(0.0, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 63: `483a2bc567d1eda9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016904`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES ((SELECT * ORDER BY cume_dist() FILTER (WHERE FALSE) OVER (ORDER BY TRUE DESC NULLS FIRST ROWS BETWEEN NULL PRECEDING AND CU
```

---

## Crash 64: `cd198cdbbbcbd066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016911`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":{"b":1}}') WHERE CURRENT_DATE >= NULL GROUP BY TRUE HAVING TRUE % CURRENT_DATE WINDOW w1 AS (), w2 A
```

---

## Crash 65: `9efa1153524a5f27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, b VARCHAR(255) GENERATED ALWAYS AS (FALSE) STORED); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 66: `1cdb5a6554f5e9af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016941`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (+~CASE CURRENT_DATE OR CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN NOT CURRENT_TIMESTAMP COLLATE BINARY END COLLATE RTRIM IS C
```

---

## Crash 67: `911998001f79bf3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016949`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT -948999301.158532594399517E-9157784527566534955999); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 68: `0059bdefb6c7f85c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016958`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT DISTINCT q.* FROM r NOT INDEXED JOIN jsonb_tree('{"a":{"b":1}}') CROSS JOIN json_tree('{"a":{"b":1}}'); I
```

---

## Crash 69: `fe165774f5fbbc07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016964`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NOT EXISTS (SELECT * ORDER BY CURRENT_TIME DESC NULLS LAST LIMIT FALSE OFFSET RAISE(IGNORE))); INSERT INTO p DEFAULT VALUES
```

---

## Crash 70: `599cbece0b2f2045` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016972`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT * ORDER BY TRUE ASC NULLS FIRST, percent_rank() FILTER (WHERE TRUE) OVER () ASC NULLS LAST; INSERT I
```

---

## Crash 71: `91c88165c22a24ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016980`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(RAISE(IGNORE), '$'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 72: `fce4bcc19a519b6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016986`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE LIKE NULL NOT LIKE TRUE ESCAPE CURRENT_TIMESTAMP, FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check
```

---

## Crash 73: `a237d4e34cb43c1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016996`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p VALUES (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (CURRENT_TIME NOT I
```

---

## Crash 74: `47a7b38960586235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017002`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') WHERE CURRENT_TIMESTAMP GROUP BY dense_rank() FILTER (WHERE RAISE(IGNORE)) OVER (ORDER BY TRUE 
```

---

## Crash 75: `7bf183a3c8e6304e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017011`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); REPLACE INTO p VALUES (NULL NOT BETWEEN FALSE AND FALSE NOT NULL); PRAGMA integrity_check; CREATE TABLE
```

---

## Crash 76: `ecfb6494ae4f3807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017035`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p VALUES (CURRENT_TIME NOT IN (CURRENT_TIMESTAMP, CURRENT_DATE)); PRAGMA integrity_check; C
```

---

## Crash 77: `0c3bb5bbc0cc2427` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017054`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE, c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 78: `8d17ccbc2a75e5d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017075`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 79: `660beb0e9d1bdab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017129`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a + 0) ); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 80: `32a86734279e819f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017145`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW 
```

---

## Crash 81: `2302cfdca5598250` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017169`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p (rowid) VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 82: `ef20e94d945468dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017175`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p (rowid) VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 83: `28c5e47b366383a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017189`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 84: `b8a964bd0ea6ef33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017201`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION VALUES (CURRENT_DATE / NULL NOT IN (CURRENT_DATE) || CURRENT_TIMESTAMP & TRUE LIKE N
```

---

## Crash 85: `e3db893396e52aed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017214`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION SELECT DISTINCT * FROM json_tree('[1,2,3]') WHERE cume_dist() OVER (ORDER BY NULL AS
```

---

## Crash 86: `5b0618abdc75e762` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017223`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL) UNION ALL SELECT DISTINCT * FROM (json_tree('[1,2,3]')) NATURAL LEFT JOIN json_each('
```

---

## Crash 87: `197c054d76e24879` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017241`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 88: `ff3aebfc25ec09db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017255`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () UNION ALL VALUES 
```

---

## Crash 89: `f9c091f9561e3033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION VALUES (CURRENT_DATE / NULL NOT IN (NULL BETWEEN NULL >> CURRENT_TIMESTAMP NOT LIKE 
```

---

## Crash 90: `f1c2841e28ee6869` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM (VALUES (FALSE)) AS x8_p_t_8_j_3a5_6i_8u7_s_92ii_21o__l2y53n_68uhb536s__2b_3n_37_
```

---

## Crash 91: `3bcc8b3ea87b3ff1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017936`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 92: `9b476553c80cce9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017973`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, rowid BLOB GENERATED ALWAYS AS (CASE NULL WHEN NULL THEN NULL END) VIRTUAL); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT INTO p DEFAULT VA
```

---

## Crash 93: `3a840b083e4df8fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019336`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL DEFAULT -80845.1981334504871269533355502482E+73430416); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT FALSE * NOT CURR
```

---

## Crash 94: `7572bc574de999f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020644`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT SELECT * FROM (VALUES (NULL)) AS m_ GROUP BY NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 95: `283f0524d1b50306` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021986`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT * FROM (SELECT NULL FROM q WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 96: `1660827cc1e85699` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT * FROM (SELECT * FROM q WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 97: `85569ab573a3c060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022182`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (TRUE IS NOT CURRENT_TIME, FALSE / CURRENT_DATE, TRUE)); CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 98: `ade3210ffdc72128` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022189`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (FALSE IN (VALUES (TRUE) UNION VALUES (CURRENT_TIME)), RAISE(IGNORE))); CREATE TABLE seed_a
```

---

## Crash 99: `93eafe44235034c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022201`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM jsonb_each('{"a":{"b":1}}') NATURAL LEFT JOIN (q INDEXED BY rowid) NATURAL LEFT JOIN (p INDEXED BY b L
```

---

## Crash 100: `dca9c815c18d6afc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022223`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (FALSE BETWEEN CURRENT_TIME AND CASE TRUE WHEN RAISE(IGNORE) THEN CURRENT_TIME END, RAISE(I
```

---

## Crash 101: `5f4bf0125122a408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022235`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (SELECT DISTINCT * FROM p LEFT JOIN json_each('{}') ON CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 102: `246cd71ce311c9fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022257`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (NULL, count(*) FILTER (WHERE CURRENT_TIME))); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 103: `05a103ba673130f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022266`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_each('[1,2,3]') JOIN (VALUES (NULL)) AS m_); CREATE TABLE seed_a(c UNI
```

---

## Crash 104: `068cda95e902a114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022348`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (VALUES (a IS NOT NULL ISNULL COLLATE RTRIM)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 105: `82033d8373633e0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025967`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 106: `ca6bffacf598884e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026395`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM p L
```

---

## Crash 107: `be58849ef97e0f7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032520`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES ((SELECT * ORDER BY cume_dist() FILTER (WHERE FALSE) OVER (PARTITION BY CURRENT_TIME) DESC), CURRENT_TIME)) VALUES (CA
```

---

## Crash 108: `1de2fb8cfea2cf3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032527`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE q (b) AS (VALUES (FALSE)) VALUES (CASE WHEN FALSE THEN NULL ELSE CURRENT_DATE END, FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 109: `b79845c019154be7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032539`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (length(CAST(CURRENT_TIME / CURRENT_TIMESTAMP AS INTEGER))); CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 110: `ecb4970b90885178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032552`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE NULL NOT IN (NULL BETWEEN NULL >> CURRENT_TIMESTAMP NOT LIKE co
```

---

## Crash 111: `d7bf7fd2bcfdbbbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032559`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE / NULL NOT IN (CURRENT_DATE) || CURRENT_TIMESTAMP & TRUE, FALSE); CREATE TABLE se
```

---

## Crash 112: `66181120a6058d85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032565`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE EXISTS (VALUES (CURRENT_TIME)) END, FALSE); CREATE TABLE seed_a
```

---

## Crash 113: `653c029b2487baef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032574`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE q (c2) AS (SELECT * ORDER BY RAISE(IGNORE) DESC NULLS FIRST LIMIT RAISE(IGNORE)), p AS (SELECT *) VALUES (CASE WHEN FALSE THEN NULL
```

---

## Crash 114: `0fc5c47f28b6543b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032596`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * LIMIT percent_rank() FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY RAISE(IGNORE) ORDER BY NULL DESC NULLS LAST
```

---

## Crash 115: `ba86964a43f1af16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032602`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') LEFT OUTER JOIN json_each('{"a":{"b":1}}') USING (b, c1)) VALUES (CASE 
```

---

## Crash 116: `233d3e7853bc85ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032633`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT ALL * FROM json_each('[]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 117: `c7cf565ddf40a862` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032751`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE
```

---

## Crash 118: `e884c1665030c205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032794`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE CURRENT_DATE || CURRENT_TIMESTAMP & TRUE END, FALSE); CREATE TA
```

---

## Crash 119: `d855727dbd39465f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032800`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE NULL NOT IN (FALSE) || CURRENT_TIMESTAMP & TRUE END, FALSE); CR
```

---

## Crash 120: `41c9747900d9a84d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032808`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CASE WHEN FALSE THEN NULL ELSE NULL NOT IN (NULL BETWEEN NULL >> CURRENT_TIMESTAMP AND CURRENT
```

---

## Crash 121: `6f4d069d4d676253` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032933`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 122: `d174adebf36c2c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032959`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE LIKE CURRENT_DATE ESCAPE TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 123: `8b5de6732efcfe8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032975`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN CURRENT ROW AND UNBO
```

---

## Crash 124: `6fb0314e1e9d59c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033109`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (count() FILTER (WHERE FALSE) OVER () <= NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 125: `08a8a795dd85b06c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033181`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL, TRUE IS NOT CURRENT_TIME, FALSE / CURRENT_DATE, TRUE); CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 126: `794c7210acecbc2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033228`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL, count(*) FILTER (WHERE +CURRENT_TIME NOTNULL)); CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 127: `7331900aec3410d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT OR ABORT INTO p VALUES (total_changes()); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 128: `838a1bc158af0b6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033333`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM r NOT INDEXED LEFT OUTER JOIN (jsonb_tree('[{"a":1},{"b":2}]')) LEFT OUTER JOIN (VALUES (CURRENT_TIMES
```

---

## Crash 129: `2d45cdc2de345031` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033346`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CASE WHEN RAISE(IGNORE) THEN RAISE(IGNORE) END COLLATE RTRIM MATCH TRUE >= +CURRENT_TIMESTAMP IN (~RAISE(IGNORE)) == 
```

---

## Crash 130: `44b5b5633b3e1bcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033356`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE <= ~CASE CURRENT_DATE OR CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN NOT CURRENT_TIM
```

---

## Crash 131: `435dffe98825fc29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033401`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CAST(CAST(CAST(CAST(CAST(CAST(CAST(CAST(CURRENT_TIMESTAMP AS FLOAT) AS FLOAT) AS FLOAT) AS FLO
```

---

## Crash 132: `387026852d4a97a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033409`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE <= NOT CURRENT_TIMESTAMP COLLATE BINARY); CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 133: `a492204f414b75a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033446`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE <= CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 134: `3f3e497d2fe50eca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033772`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT TRUE > NULL NOT IN (CURRENT_TIME) AS a; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 135: `90118099caaf1754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033791`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (ntile(CURRENT_DATE) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 136: `deee22810b543086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033800`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (count() FILTER (WHERE FALSE) NOT LIKE count() FILTER (WHERE FALSE)); CREATE TABLE seed_a(c UNI
```

---

## Crash 137: `a549db1dae363316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033843`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 138: `276d0601c86d4df2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033974`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (FALSE, group_concat(CURRENT_TIMESTAMP, '') FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE see
```

---

## Crash 139: `3f2819c0eccfdad4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034024`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (row_number() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 140: `d246ad3f99c51b0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035252`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE != CURRENT_TIMESTAMP
```

---

## Crash 141: `907efebb7ecaea82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035388`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME, NULL); VALUES (CURR
```

---

## Crash 142: `7fb740456b33626e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037289`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT); INSERT INTO p DEFAULT VAL
```

---

## Crash 143: `54c44a3656ef91c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037689`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, a TEXT PRIMARY KEY, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXI
```

---

## Crash 144: `91e92a19859c581e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037695`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 145: `11bdf97b81912e3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037723`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME NOT IN (CURRENT_TIMESTAMP, CURRENT_DATE, TRUE)); ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE
```

---

## Crash 146: `2c9de82cc032aeeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037737`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TAB
```

---

## Crash 147: `720295a2b9542d4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037744`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE), a VARCHAR(
```

---

## Crash 148: `d52a691a2dc0b3ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037756`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'aCDe1a'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE)
```

---

## Crash 149: `cef756b63eda2a2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037762`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT X'7DeA60E1f7ae'); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a
```

---

## Crash 150: `56296d2b75bac103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037773`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE), rowid INT CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c
```

---

## Crash 151: `92e97a5b22772318` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037798`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT OR ABORT INTO p VALUES (CAST(CURRENT_TIMESTA
```

---

## Crash 152: `b43b618812d308d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037829`

```sql
CREATE TABLE IF NOT EXISTS p(a INT DEFAULT ''); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; C
```

---

## Crash 153: `cdbd187ccdcf1295` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037848`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT -60340015708127.8e-0679870997538089); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT
```

---

## Crash 154: `9d2e31164f73a533` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037893`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 155: `367dd88b7e20a069` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037899`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE I
```

---

## Crash 156: `c3d5e36e3cea7e6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039837`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p SE
```

---

## Crash 157: `e5c4d0d5c000f37a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040057`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE % CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 158: `1b86dacbd5dd8fcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040826`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 159: `e03fe7db8774ac03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040836`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (TRUE IS NOT CURRENT_TIME, FALSE / CURRENT_DATE, TRUE)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 160: `149c4e7fb5bb46fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040845`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_DATE / NULL NOT IN (CURRENT_DATE) || CURRENT_TIMESTAMP & TRUE LIKE NULL)) SELECT * FROM p; CREATE TABLE seed_
```

---

## Crash 161: `d7ec435489e83b5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040876`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('[1,2,3]') JOIN (VALUES (NULL)) AS m_) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 162: `29bf57d5faafd445` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040884`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT FALSE * CURRENT_TIMESTAMP FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS ()) SELEC
```

---

## Crash 163: `8cc68ba16406552c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041670`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CA
```

---

## Crash 164: `fd6c938647adfdf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041678`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(CAST(CAST(CAST(CURRENT_TIMESTAMP AS FLOAT) AS FLOAT) AS FLOAT) AS FLOAT), '$')) SELECT 
```

---

## Crash 165: `8e6b5c3715085888` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041688`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT FALSE IS FALSE FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS ()) SELECT * FROM p;
```

---

## Crash 166: `d1099797db4c540c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041902`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT NULL AS a FROM json_each('[]')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 167: `0f4b3427aa8df222` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041967`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (count(*) OVER (PARTITION BY FALSE ORDER BY TRUE NOT IN (NULL) ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW)); 
```

---

## Crash 168: `c862aa17f65d9f7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041992`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED USING (c2, c1) ORDER BY TRUE ASC; VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 169: `b0299a44dda656e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042021`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 170: `6fc995c3950d34f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049236`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER () FROM json_each('[1,2,3]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 171: `2462ea8ad83acc25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049433`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH RECURSIVE p AS (SELECT ALL * FROM json_each('[]') LIMIT TRUE) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_
```

---

## Crash 172: `db96ea6ce2638f8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051697`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE * NOT CURRENT_TIMESTAMP IS +FALSE FROM p AS y_f3 INNER JOIN p USING (a) GROUP BY FALSE ORDER BY CURRENT_TIMES
```

---

## Crash 173: `680416c8e40daa5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051911`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{}') ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 174: `ea71b320af3c7318` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052310`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE r AS (SELECT *) SELECT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLU
```

---

## Crash 175: `b67e682a4c9a4059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053747`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(CURRENT_TIMESTAMP AS BOOLEAN), '$')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 176: `ea8455c8a6a9448f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053762`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(CURRENT_TIMESTAMP AS FLOAT), '$[#-1]')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 177: `7bd2c847fe20fb8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053769`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (min(FALSE))) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 178: `3b12b47d2c36debe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053795`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT OR REPLACE INTO q VALUES (NOT EXISTS (VALUES (RAISE(IGNORE)))); EXPLAIN QUERY PLAN VALUES (FALSE)
```

---

## Crash 179: `dc87781c4910dd10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053819`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(TRUE % CURRENT_DATE AS FLOAT), '$')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 180: `5bd17f4d09b77485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053846`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(CURRENT_TIMESTAMP AS FLOAT), '$.a')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 181: `3d7671b9a1b3681f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053943`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(CAST(NULL AS FLOAT), '$')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 182: `24eeb52c486eb159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053963`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each(FALSE, '$')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 183: `6ebe69fdb2f82327` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054090`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (TRUE) UNION VALUES (count() FILTER (WHERE FALSE) OVER ())) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 184: `eeadac0f617221e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054223`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT count(*) AS a FROM (VALUES (CURRENT_TIMESTAMP)) AS a) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 185: `a80c5cc898bdecc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054230`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT count(*) AS a FROM (json_tree('[1,2,3]'))) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 186: `c94327c58631fbbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054458`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 187: `725718a77addf01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054602`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('[1,2,3]') JOIN json_tree('[{"a":1},{"b":2}]')) SELECT * FROM p; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 188: `56d427030cab2ea1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055377`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('{"a":1}')) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); S
```

---

## Crash 189: `9ac0bb8387b28c06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058424`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT *, *, *, *, *, *, *, *, *, *, *, * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS 
```

---

## Crash 190: `b609b876ff1ff5db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058445`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT *, *, *, *, *, *, *, *, count(*) OVER (), * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WIND
```

---

## Crash 191: `d7f3f215cbe04772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058457`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL, CURRENT_TIMESTAMP WINDOW w1 AS ()) SELECT * F
```

---

## Crash 192: `9bbc5d3378a2fc3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058475`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (PARTITION BY CURRENT_TIMESTAMP O
```

---

## Crash 193: `bd09f3c0697d4e44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058484`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_each('[1,2,3]') JOIN json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS ())
```

---

## Crash 194: `bab0f4a4c1d73c2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058561`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE '-_6' GROUP BY NULL WINDOW w1 AS ()) SELECT * FROM p; CREATE TABLE seed_a(c UN
```

---

## Crash 195: `7f49256b04a820c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062212`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT -64588); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 196: `6e9ffbb4dbe75420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062530`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT X'Acee'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 197: `d8f0fa3d24f90b52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062802`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME NOT IN (CURRENT_TIMESTAMP, CURRENT_DATE, TRUE)); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, c1 
```

---

## Crash 198: `5b40e2d668ac23c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063085`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO p SELECT * FROM p; ANALYZE
```

---

## Crash 199: `e4451bd6ac52fdb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063117`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT OR ABORT INTO p VALUES (length(
```

---

## Crash 200: `13e3d677d86aca4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063288`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'aCDe1a'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 A
```

---

## Crash 201: `0d15e3b79d3ff3c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063297`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'aCDe1a'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 A
```

---

## Crash 202: `63b8b9753dd79af9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063358`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT -23762014736071.062395441157E051751605251703269); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CRE
```

---

## Crash 203: `497bc691d513a7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063364`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) 
```

---

## Crash 204: `7c34db928ebfc0f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063388`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'aCDe1a'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(25
```

---

## Crash 205: `fbe37c04c5ae9aca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063441`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'aCDe1a'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, c1 A
```

---

## Crash 206: `e9b9ebf93302b508` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063590`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT ntile(CURRENT_DA
```

---

## Crash 207: `7cd27d9dcb6a7c99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063597`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 208: `def26981d037d665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063616`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT * FROM (VALUES (NULL)) AS j_ LEFT JOI
```

---

## Crash 209: `6d0ac4a5c05ee278` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063636`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT count(*) OVER (P
```

---

## Crash 210: `d4e645e7dde83680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066290`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, NULL); VALUES (CURR
```

---

## Crash 211: `e54f5e63ccf8f9b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067154`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME, NULL); VALUES (FALS
```

---

## Crash 212: `9a3bf53109afa43f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067171`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(_rowid_) DO UPDATE 
```

---

## Crash 213: `5176ab56b0b8b725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067180`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME, NULL); VALUES (CURR
```

---

## Crash 214: `372ebbda710487d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068264`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (); CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1
```

---

## Crash 215: `e0652d4e939bde6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068945`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE r AS (SELECT *) SELECT count() FILTER (WHERE FALSE) FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 216: `e92a0aa45eb5e9f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069096`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT INTO p SELECT CURRENT_TIME FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL 
```

---

## Crash 217: `43d05ad501bf1e9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069329`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (dense_rank() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 218: `b6258784667c31f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069336`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (row_number() OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN CURRENT ROW AND CURRENT
```

---

## Crash 219: `63c1ef735ebe5bae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069349`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (rank() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3
```

---

## Crash 220: `fb213f3e3a7e603e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069356`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (group_concat(CURRENT_TIMESTAMP, '') OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 221: `d812eb24f6dfedcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069384`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT FALSE OR NULL) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 222: `3e63579b088dc70e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069397`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (row_number() OVER (ORDER BY NULL DESC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AND UNBOUN
```

---

## Crash 223: `5e4ad72aad6852bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069412`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (NULL IS NOT TRUE, CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 224: `e7298051579e3ebc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069428`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH t2 (c3, rowid, b, a, c1) AS (SELECT DISTINCT NULL > CURRENT_DATE AS a, p.* FROM jsonb_tree('[1,2,3]') NATURAL LEFT JOIN json_tree(~TRUE - CUR
```

---

## Crash 225: `0916236b519cd3c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069562`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (ntile(CURRENT_DATE) OVER (ORDER BY NULL DESC, TRUE)); CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 226: `9998398f926fc228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069598`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (FALSE IN (VALUES (TRUE) UNION VALUES (CURRENT_TIME))); CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 227: `4e3d78d3e4446e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069643`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE r AS (SELECT *) SELECT CURRENT_TIMESTAMP NOT LIKE count() FILTER (WHERE FALSE) FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 228: `c3d2f971c91e5222` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069764`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (ntile(TRUE) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 229: `d30249aeacc562eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069816`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES ((SELECT * ORDER BY RAISE(IGNORE) ASC LIMIT CURRENT_TIME) IN (SELECT * ORDER BY FALSE ASC NULLS LAST LIMIT FALSE))) VA
```

---

## Crash 230: `0fe05a1c1c8f7df3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069874`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (FALSE >> TRUE NOT LIKE FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 231: `e05efc3eeddb5bf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069992`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (count(DISTINCT NULL) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 232: `54ee4cf9ced56f47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070014`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (group_concat(CURRENT_TIMESTAMP, '') FILTER (WHERE CURRENT_TIME IS NULL COLLATE NOCASE)); CREAT
```

---

## Crash 233: `82d17fb362fa82b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070020`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (count(DISTINCT TRUE) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 234: `5f49aa3a0a25b29e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070063`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIME) INTERSECT VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 235: `fe3489d52ed55933` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070762`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CAST(FALSE AS FLOAT) <= FALSE COLLATE RTRIM >> CURRENT_DATE COLLATE NOCASE); CREATE TABLE seed
```

---

## Crash 236: `ff82aaa4457c58e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070836`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CAST(FALSE AS VARCHAR(255)) <= CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 237: `94184a71a1b1253d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070874`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CAST(FALSE AS FLOAT) <= CAST(FALSE AS FLOAT) <= CAST(FALSE AS FLOAT) <= CAST(FALSE AS FLOAT) <
```

---

## Crash 238: `6ae6fe9628662b0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070897`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIMESTAMP <= CAST(FALSE AS FLOAT) <= CAST(FALSE AS FLOAT) <= CAST(FALSE AS FLOAT) <= C
```

---

## Crash 239: `199736f80d1e16eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070969`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CAST(FALSE AS FLOAT) <= TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 240: `3ecdcc6de3126fb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070991`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT CURRENT_TIME FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE LIMI
```

---

## Crash 241: `3490df318e37c1a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071003`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE CASE WHEN FALSE THEN NULL ELSE EXISTS (VALUES (CURRENT_TIME
```

---

## Crash 242: `aa71ca7e0b4d9889` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071011`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT X'EC2BA6'); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE; CREATE T
```

---

## Crash 243: `ed76189a5ad30ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071024`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE CASE CURRENT_DATE OR CURRENT_TIMESTAMP WHEN CURRENT_DATE TH
```

---

## Crash 244: `83de1be2e8820283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071050`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME NOT LIKE CURRENT_DATE; CREATE TABLE seed_a(c U
```

---

## Crash 245: `88dafbbb770a2911` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071064`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING
```

---

## Crash 246: `557e853ad211f071` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071188`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (WITH RECURSIVE p AS (WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE) SELECT DIST
```

---

## Crash 247: `6e2c97bf9eede7b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071222`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE LIMIT FALSE) SE
```

---

## Crash 248: `665bddd286bc394f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071257`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT CURRENT_DATE, b DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE FA
```

---

## Crash 249: `5a4ce50308775abc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071263`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE LIKE CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN C
```

---

## Crash 250: `682b9407e3462cc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071272`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE LIKE CURRENT_DATE ESCAPE CASE CURRENT_DATE OR CURRENT_TIMESTAMP WHEN CURRENT_DATE
```

---

## Crash 251: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001891`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 252: `f95b2fca86b0a807` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002014`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 253: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002023`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 254: `1f86b7e07c79cf74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002283`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTE
```

---

## Crash 255: `b92b80a6a1cf85ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002556`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL AND CURRENT_TIME), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS
```

---

## Crash 256: `f99c3b1657a572b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002562`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORED
```

---

## Crash 257: `48ab927cb9811aa1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002569`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORED); CREATE TABLE IF NOT E
```

---

## Crash 258: `553041aa395a7432` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002582`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORED); CREATE TABLE IF NOT EXISTS
```

---

## Crash 259: `18c037801ad3e61c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002589`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NUL
```

---

## Crash 260: `5c59a3e43e19567e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002603`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORE
```

---

## Crash 261: `0e2e99039b0a8526` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002648`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORED); CREATE TABLE IF N
```

---

## Crash 262: `75f62a129ba1d900` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002874`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL NOT NULL != CURRENT_TIMESTAM
```

---

## Crash 263: `e3be028fa60bab60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002882`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL != CURRENT_TIMESTAMP, NULL);
```

---

## Crash 264: `830bd36983edc23a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002888`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP, NULL); VALUES 
```

---

## Crash 265: `eccc9bf55d8206cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002903`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (FALSE, NULL); VALUES (CURRENT_DAT
```

---

## Crash 266: `27f7555c04d6fa2d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002909`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE != CURRENT_TIMESTAMP
```

---

## Crash 267: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003366`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 268: `b132628365fe196f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003772`

```sql
SELECT substr('', 4294967296, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 269: `c46897f5621dd97b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003921`

```sql
SELECT round(0.01, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 270: `95580e34b73af1f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003943`

```sql
SELECT printf('%f', 9223372036854775807, ' ft N_V-3n_4'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44
```

---

## Crash 271: `f5fc51c31fb7fdaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004150`

```sql
SELECT substr('r2Y_r6_JRj   ', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 272: `5f15dc3e08ae9165` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004159`

```sql
SELECT substr('r2Y_r6_JRj   ', -2147483648); SELECT printf('%.*e', 0, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INT
```

---

## Crash 273: `1f15cdd5acbfb1f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004571`

```sql
SELECT round(-0.0, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3
```

---

## Crash 274: `182e5adc38073f0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004864`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT GENERATED ALWAYS AS (FALSE) VIRTUAL, c3 REAL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); C
```

---

## Crash 275: `ad11202b46b88a7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005640`

```sql
SELECT printf('%.*g', 2147483648, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 276: `08e05c10506457cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005871`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (NULL); SELECT printf('%.*g', -2147483648); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SEL
```

---

## Crash 277: `37bddad4378780bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005893`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (NULL) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483648); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),
```

---

## Crash 278: `ad2d3d5c255a18ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005962`

```sql
SELECT printf('%.*s', 9223372036854775807, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(1
```

---

## Crash 279: `6f64fbad4d925bd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007131`

```sql
SELECT substr('', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 280: `72e4233b96ccb627` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007331`

```sql
SELECT round(1e308, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 281: `3335159436f3fc7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007339`

```sql
SELECT round(1e308, -2147483648); SELECT printf('%.*e', 0, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2
```

---

## Crash 282: `3a26042fc2fad035` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007474`

```sql
SELECT printf('%.*e', 2147483647, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 283: `19f8fc2e6923602e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008875`

```sql
SELECT printf('%.*d', -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed
```

---

## Crash 284: `8437b7737ff2792c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008881`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123
```

---

## Crash 285: `c84ae51f41221b79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008893`

```sql
SELECT round(1e-308, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 286: `e6115c1cf152d932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008919`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 287: `f80dee072dfba3ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008946`

```sql
SELECT printf('%d', -1, 'TV_ _-_p- b_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 288: `0e255ab75d989334` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008961`

```sql
SELECT substr('_ 1frq10m- g-O_', 9223372036854775807, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO
```

---

## Crash 289: `cd931ecf256f1f50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008967`

```sql
SELECT substr('a9Ju_4_9 --0-_u-', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE
```

---

## Crash 290: `e479f85b4875a55e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010165`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 291: `0c14b83a5cdc5e86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010182`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT OR REPLACE INTO q VALUES (~CURRENT_DATE OR CURRENT_TIMESTAMP IS CURRENT_TIME); EXPLAIN QUERY PLAN
```

---

## Crash 292: `21e1f68d65d77708` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010199`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT OR REPLACE INTO q VALUES (TRUE | CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TA
```

---

## Crash 293: `c52a622d44884156` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010205`

```sql
SELECT substr('', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 294: `2e2847f3f6228c2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010235`

```sql
SELECT substr('1qTp8_1-aj1U', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 295: `a6ff41afd74f397a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010250`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (-1474891422520.01E6); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 296: `cfdb870e061ae912` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010274`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 297: `9eff427090fe22ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010316`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); INSERT OR ABORT INTO p VALUES (-1474891422520.01E6); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 298: `d99850116d9cdd3e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015875`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, rowid BLOB GENERATED ALWAYS AS (-FALSE) VIRTUAL); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; C
```

---

## Crash 299: `b32aa72904949fee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015907`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT OR REPLACE INTO q VALUES (TRUE | ~CASE CURRENT_DATE OR CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN T
```

---

## Crash 300: `29c82eb967c39049` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017612`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT FALSE * NOT CURRENT_TIMESTAMP IS FALSE FROM p JOIN p e0 ON CURRENT_TIME MATCH NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 301: `3b5007b3745eef3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017648`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT OR REPLACE INTO q VALUES (TRUE << TRUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(
```

---

## Crash 302: `432592cc1c410f15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017664`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME IN (NULL) FROM p JOIN p e0 ON CURRENT_TIME MATCH NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 303: `008fa7691886bf59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017684`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) INTERSECT SELECT * ORDER BY FALSE ASC, NULL DESC NULLS LAST; SELECT * FROM p JOIN p e0 ON CURR
```

---

## Crash 304: `8cf5b2731811635d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017694`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, c1 DATE PRIMARY KEY); SELECT * FROM p JOIN p e0 ON CURRENT_TIME MATCH NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 305: `83a0160f77c3d830` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017745`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL, c3 FLOAT NOT NULL DEFAULT NULL); SELECT * FROM p JOIN p e0 ON CURRENT_TIME MATCH NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 306: `0385cc0005950f77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017761`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIMESTAMP LIKE FALSE NOT NULL COLLATE NOCASE AS h_65__93554_2___7_26_4n3p0md7zq_2hpwj_hej_5vt FROM p JOIN p e0 ON CURRENT_TIME MATC
```

---

## Crash 307: `400629d81674b95e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017819`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('[]') LIMIT CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 308: `2035562d046ef340` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019155`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 309: `8e657b802aea76a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019162`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 310: `9f50bce1e3474892` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019183`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, b VARCHAR(255) GENERATED ALWAYS AS (FALSE) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 311: `a15d3b4976934300` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019260`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -2316); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 312: `ed593c6062e5f876` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023760`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIME ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE TABLE 
```

---

## Crash 313: `d4710fa420974c50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023781`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each(TRUE, '$'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 314: `7a47a917d2818e8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023806`

```sql
SELECT round(-1.0, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3
```

---

## Crash 315: `ffec1a57c9f0b2af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028549`

```sql
SELECT printf('%.*d', 2147483647, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 316: `44eb010696e32f65` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028797`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE), rowid INT CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 317: `7cee07b4f46922e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029310`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (TRUE - FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSER
```

---

## Crash 318: `8dbd124b4d1623ef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029338`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT X'7DeA60E1f7ae'); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 319: `78098d5e542c234f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029358`

```sql
SELECT round(-1.0, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(
```

---

## Crash 320: `5019720772cfbce7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029417`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q JOIN q e ON CAST(TRUE AS DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 321: `c8ee9fe84a86a490` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030076`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT DISTINCT *, * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 322: `8e87555765ca3eee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031887`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER DEFAULT 76782192891242715200479936.3E5); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 323: `5294d9883cec0876` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034516`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIME), c3 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(25
```

---

## Crash 324: `c41c7a5a567a8562` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035136`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE != CURRENT_TIMESTAMP
```

---

## Crash 325: `52d1f322eb720d81` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035172`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (CURRENT_DATE OR CURRENT_TIMESTAMP IS CURRENT_TIME), _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p
```

---

## Crash 326: `40d2631155b0af85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035194`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, b TEXT CHECK (NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VA
```

---

## Crash 327: `ec5254c2e800b4a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035200`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE != CURRENT_TIMESTAMP, NULL);
```

---

## Crash 328: `53e40f7e07da9e3d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035223`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE != CURRENT_TIMESTAMP
```

---

## Crash 329: `365b93a91d8f1244` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035230`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME IS NULL, NULL); VALU
```

---

## Crash 330: `6b3969ff5d251edd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035523`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT FALSE, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL NOT NULL != CURRENT_T
```

---

## Crash 331: `316fa3be2275aad6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035540`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL NOT NULL != CURRENT_TIMESTAM
```

---

## Crash 332: `bf83ec79631a9e7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035557`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, b TEXT CHECK (NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE >= FALSE IN (CURRENT_TIME))); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); I
```

---

## Crash 333: `5e54f7daf4a5c0b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035570`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL NOT NULL != CURRENT_TIMESTAM
```

---

## Crash 334: `192d94df80cb6e4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035598`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE, rowid BLOB GENERATED ALWAYS AS (FALSE LIKE TRUE) VIRTUAL); INSERT OR 
```

---

## Crash 335: `b5631e90d1f1ab75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037434`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HA
```

---

## Crash 336: `45f185d815b2b967` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037483`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CASE TRUE WHEN TRUE IS CURRENT_TIME THEN NULL END), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 337: `aa8557ddfc7f9f4c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037555`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL DEFAULT FALSE, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 338: `016b1cf7c14872bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038089`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c
```

---

## Crash 339: `3439b5f66fe79ea3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038121`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, b TEXT CHECK (FALSE >= NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); INSERT INTO p DEFAUL
```

---

## Crash 340: `fe9f9cf300403899` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038168`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); INSERT INTO p (rowid) VALUES 
```

---

## Crash 341: `c675ad56d3bc7153` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038190`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, b TEXT CHECK (CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CURRENT_TIMESTAMP THEN NULL END THEN NULL END THEN NULL END THEN N
```

---

## Crash 342: `3ab2ee7cd6bd9011` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038198`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT X'7DeA60E1f7ae'); CREATE T
```

---

## Crash 343: `5618b3260fda3a88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038232`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT 0, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); INSERT INTO p D
```

---

## Crash 344: `9ceb143afb619edc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038269`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT -38101, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); INSERT INTO p DEFAU
```

---

## Crash 345: `790e90da48e4f4db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038551`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL), b TEXT CHECK (CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CURRENT_TIMES
```

---

## Crash 346: `35a0cba62909878f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038569`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT * FROM p 
```

---

## Crash 347: `cca9140e73d101fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038583`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT -64588, b DATE PRIMAR
```

---

## Crash 348: `96329ac974e69e27` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038605`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -0826933089679854844712852225540510065366366106334344702293404555108921431991026853490665760.6e948, c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VA
```

---

## Crash 349: `dd48846a4ed17b28` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'EfBaEa48'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 350: `52483cb91e91c9aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040413`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT CHECK (FALSE)); SELECT FALSE * NOT CURRENT_TIMESTAMP IS FALSE, * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TA
```

---

## Crash 351: `cf095a071fc1f8e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040644`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY NULL ASC NULLS LAST; CREATE TABLE see
```

---

## Crash 352: `73e21feec79b9bc0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043441`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT FALSE * NOT CURRENT_TIMESTAMP IS FALSE FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 353: `1b9d5898eee13e64` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043453`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (ntile(CURRENT_DATE) OVER ())) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 354: `cd4c9868cabd23f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043470`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (count(DISTINCT NULL) FILTER (WHERE FALSE))) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 355: `d76becb7aadd8213` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043481`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[1,2,3]')) SELECT count() FILTER (WHERE FALSE) OVER (), * FROM p; CREATE TABLE seed_t1(c1 I
```

---

## Crash 356: `72f764cf904dce5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043494`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 357: `51eb0531453c47a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043529`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT *, * FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 358: `c7a1cc36ad9abd44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043557`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[1,2,3]')) SELECT p.* FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 359: `3d70808cb7cecf0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043626`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECU
```

---

## Crash 360: `ed90bae5b2b748f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050769`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT CURRENT_TIMESTAMP IN (VALUES (NULL)) AS y89__ FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t
```

---

## Crash 361: `14377856d85b13a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050778`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT count() FILTER (WHERE FALSE) OVER (), * FROM json_tree('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 I
```

---

## Crash 362: `2658bf2887ad8b73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050787`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 363: `4a703e0e7d805d38` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050805`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUD
```

---

## Crash 364: `4182f7e5659268e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051594`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURR
```

---

## Crash 365: `8b350e46bf551c47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058641`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE, c1 BOOLEAN PRIMARY KEY); SELECT * FROM json_tree(CURRENT_TIME, '$') JOIN json_each('{}') NATURAL LEFT JOIN json_each
```

---

## Crash 366: `ddc37af4be19d414` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058651`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE, c1 BOOLEAN PRIMARY KEY); SELECT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 367: `91ff253b4e9c0180` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058731`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (c2) NOT NULL UNIQUE, c1 BOOLEAN PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 368: `e8cac1c7bc980055` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058818`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); WITH RECURSIVE p AS (SELECT DISTINCT cume_dist() OVER () FROM json_each('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 369: `29ac38843dd0d54d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059017`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT X'900fc5A8' AS o__l_2869_ FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 370: `35ac64960bff09ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059050`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); WITH RECURSIVE r AS (SELECT *) SELECT count(*) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIME COLLATE BINARY ASC NULLS LAST ROWS BETWEEN UNBO
```

---

## Crash 371: `58cee1ac7bc26734` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059267`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT count() FILTER (WHERE FALSE) OVER (), CURRENT_TIMESTAMP IN (VALUES (NULL)) AS y89__ FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE 
```

---

## Crash 372: `6fee666fac42e936` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059289`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT count() FILTER (WHERE FALSE) OVER (), first_value(CURRENT_TIME) OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 I
```

---

## Crash 373: `63b290bfafdf750f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059298`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT dense_rank() OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 374: `06ed00d9ab178bfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059317`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); WITH RECURSIVE p AS (SELECT DISTINCT CAST(TRUE AS BLOB) AS a FROM json_each('[1,2,3]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 375: `844e0d0b4743fcdc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059354`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT OR ABORT INTO p VALUES (random()); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 376: `e3299c9f200f1f26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059368`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT rank() OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 377: `c4d639cec8bf08e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059488`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT count() FILTER (WHERE FALSE) OVER (), count(*) OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 378: `dfb0877b683d1663` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059495`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT count() FILTER (WHERE FALSE) OVER (), count(*) OVER (PARTITION BY TRUE, TRUE) FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t
```

---

## Crash 379: `0813b25ca2a2aa6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059529`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT TRUE, first_value(CURRENT_TIME) OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 380: `d6e54ead12d5c3ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060390`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL DEFAULT X'abb4B45203AD'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(rowid INT UNI
```

---

## Crash 381: `b05197cb757a6db8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060557`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'EfBaEa48'); WITH q (c2) AS (SELECT * ORDER BY RAISE(IGNORE) DESC NULLS FIRST LIMIT RAISE(IGNORE)), p AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIMES
```

---

## Crash 382: `491aa440184f874f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060592`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, rowid BLOB GENERATED ALWAYS AS (FALSE LIKE TRUE) VIRTUAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 383: `6592a72596221acc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062385`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid, b); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 384: `b15bacb95d5dddb6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063744`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (TRUE || CURRENT_TIMESTAMP NOT NULL), b TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 385: `4a941697e2a397f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063771`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT -676629749962.853626459253872629507202616677, b TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 386: `97aa294cbfafe4fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063805`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CURRENT_TIMESTAMP THEN NULL END THEN NULL END THEN NULL END THEN
```

---

## Crash 387: `ec4707453a620a10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063969`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (CURRENT_DATE IS NOT CURRENT_TIME COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 388: `7d2eb7f65a236137` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064001`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (NULL <= CURRENT_TIMESTAMP IS NULL), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 389: `d8b99b5f4388a80e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064018`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (TRUE AND CURRENT_DATE), c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 390: `dcf8ed3866655853` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065999`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); VALUES (NULL) EXCEPT
```

---

## Crash 391: `b9365c48538bd4f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066033`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT -64588, b DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); SELECT DISTINCT * FROM p LEF
```

---

## Crash 392: `eebbbc31a7fe06f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066053`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); SELECT DISTINCT *, *
```

---

## Crash 393: `5fa9a9a36e74df59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); SELECT DISTINCT FALS
```

---

## Crash 394: `82c1c0e14a7497a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066152`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); SELECT DISTINCT * FR
```

---

## Crash 395: `54c3b29a9e3368af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066159`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE, NULL); SELECT DISTINCT * FR
```

---

## Crash 396: `a1009174a4bb267d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068516`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE; CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) 
```

---
