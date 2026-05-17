# Crash Triage Report

**Total crashes:** 404  
**Unique crash sites:** 404  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 203 | 203 | 50% |
| Signal | 201 | 201 | 49% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `a9e6f52226fb1859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALUES (0, substr(NULL IS NOT NULL, TRUE COLLATE RTRIM NOTNULL > (VALUES (CURRENT_TIMESTAMP)) COLLATE NOCASE | CURRENT_DATE <= N
```

---

## Crash 2: `10e8a5fb0fd9d736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000473`

```sql
SELECT printf('%.*g', 4294967295, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (TRUE ISNULL OR CURRENT_DATE IS NOT DISTINCT FROM NULL); ANALYZE p; CREATE TABLE
```

---

## Crash 3: `12adda09481caab5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000611`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT r.*, CASE CURRENT_TIME WHEN CURRENT_DATE LIKE RAISE(IGNORE) THEN ~TRUE | CURRENT_DATE << CURRENT_TIME BETWEEN FALSE AND NULL END AS t_k_
```

---

## Crash 4: `2f89061bb644d4b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000887`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c2); INSERT OR REPLACE INTO p VALUES (hex(~RAISE(IGNORE) NOT LIKE NULL * TRUE COLLATE RTRIM | FALSE | CURRENT_DATE IS NULL | TRUE NOT NULL 
```

---

## Crash 5: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000935`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 6: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001810`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 7: `d59d026bf45f6778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001857`

```sql
SELECT printf('%.*f', 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 8: `6be244305b43a506` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001935`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); IN
```

---

## Crash 9: `23b87d9584d37f45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001941`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO r VALUES (CAS
```

---

## Crash 10: `f8c4da6667d55af5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001948`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO r VALUES (CA
```

---

## Crash 11: `a06fce3a6818b798` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001954`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO r VALUES (CASE WHEN CASE 
```

---

## Crash 12: `23c318f198cb1b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001975`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO r VALUES (CASE WHEN CASE 
```

---

## Crash 13: `f72da56935c1304f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001996`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO r VALUES (CASE WHEN CASE TRUE WHEN FA
```

---

## Crash 14: `f3d220ad7c85437c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002324`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 15: `31665463451a674e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002605`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (FALSE)); PRAGMA quick_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 16: `5e45be06ab3ec2e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002668`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 17: `1987de18fbfb55ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003059`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP IS NULL > TRUE NOT LIKE CASE TRUE W
```

---

## Crash 18: `30e9c32da69788c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003069`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CASE TRUE WHEN CURRENT_TIME THEN NULL END; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 19: `45a1d01046fed825` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 20: `7df47aab472f1efb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003090`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE NULL ISNULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 21: `89f3933876e5b99b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE COLLATE BINARY ISNULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 22: `db62bba890215900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003102`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME * CURRENT_TIMESTAMP IS NULL > TRUE COLLATE BINARY ISNULL; CR
```

---

## Crash 23: `0f8d5265035a703d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003108`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * CURRENT_TIMESTAMP IS NULL > TRUE COLLA
```

---

## Crash 24: `2a1482aa0d0c5d10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003137`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME * CURRENT_TIMESTAMP IS NULL > TRUE COLLATE BINARY; CREATE TA
```

---

## Crash 25: `5987df417e6c6dc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003146`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NULL COLLATE BINARY; CREATE TABLE seed_a(c UNIQUE); 
```

---

## Crash 26: `1249ea8db8100f5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003152`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP > TRUE COLLATE BINARY; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 27: `391f963b366d8eb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003158`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE TRUE COLLATE BINARY; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 28: `1d003e0a25e8616f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003490`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIMESTAMP IS NULL > TRUE COLLATE BINARY ISNULL NOT LIKE C
```

---

## Crash 29: `287ec124dde35ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003501`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIMESTAMP IS NULL; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 30: `2f38184e329d55e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004217`

```sql
SELECT substr('F5', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 31: `3f4606af527ee9c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004245`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 32: `9c36a8ddcb2cd188` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004279`

```sql
SELECT printf('%.*f', -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 33: `0a502acce83dc6e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004487`

```sql
SELECT printf('%.*d', 9223372036854775807, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 34: `78502aa5b7ee8f5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004791`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 35: `da9f790b7d50c979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004876`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE IS NOT NULL ORDER BY CURRENT_TIME > TRUE / NULL ASC NULLS LAST; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 36: `371e05f51a27c1bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004914`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP ORDER BY RAISE(IGNORE) ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 37: `47f4da945f5918d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005260`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE MATCH ~-CURRENT_TIMESTAMP | TRUE AND CURRENT_TIMESTAMP NOT NULL 
```

---

## Crash 38: `5c34cf7487598822` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005268`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE ~-CURRENT_TIMESTAMP | TRUE AND CURRENT_TIMESTAMP NOT NULL) AS sub1; CR
```

---

## Crash 39: `6bff81a1e3259179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005276`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE ~CURRENT_TIMESTAMP | TRUE AND CURRENT_TIMESTAMP - FALSE LIKE (CURRENT_
```

---

## Crash 40: `6592d3d318212aae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE MATCH FALSE - FALSE LIKE (CURRENT_DATE)) AS sub1; CREATE TABLE s
```

---

## Crash 41: `89130da2bfa28321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005302`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE MATCH ~FALSE NOT NULL - FALSE LIKE (CURRENT_DATE)) AS sub1; CREA
```

---

## Crash 42: `769e638428dffc46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005318`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP - FALSE LIKE CURRENT_TIMESTAMP) AS sub1; CREATE TAB
```

---

## Crash 43: `e8559f491008aec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005335`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NULL - FALSE LIKE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UN
```

---

## Crash 44: `b2e6dec7f6a95dce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005692`

```sql
SELECT printf('%llu', 4294967295, '- -h372_ 16mmj_G '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT co
```

---

## Crash 45: `e9f8c50be45d595d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006151`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 46: `cf523d884e8f1e34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007447`

```sql
SELECT round(-0.0, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 47: `22492190d3ef6b6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007457`

```sql
SELECT round(-0.0, 2147483647); CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 TEXT DEFAULT FALSE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 48: `df29445d508ba609` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007666`

```sql
SELECT printf('%.*g', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 49: `f6fafd0ebf7cdd09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007789`

```sql
SELECT substr('d3Y- T ', -2147483649, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 50: `fe31ca2331c80216` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008086`

```sql
SELECT printf('%.*f', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIME NOTNULL COLLATE NOCASE NOT BETWEEN CURRENT_DATE COLLATE NOCASE AND CURRENT_TIMESTAMP, C
```

---

## Crash 51: `3d950e22e467de40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011886`

```sql
SELECT printf('%.*g', 2147483648); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 52: `19f5d618bb610c7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011949`

```sql
SELECT printf('%.*g', 2147483648); CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT CURRENT_TIME, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (TRUE); CREATE TABLE seed_a
```

---

## Crash 53: `6bae08383f1998d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012610`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE
```

---

## Crash 54: `61e17331c7f85ef8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013034`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT); SELECT * FROM p NATURAL JOIN p WHERE NULL ISNULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 55: `2afd493d20ab2c50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013174`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 56: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017528`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 57: `4ec2c3ce42fad957` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019041`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, c3 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 58: `5976ca7835a9dbb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019103`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, c1 REAL NOT NULL DEFAULT -31.9239443748663939, c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABL
```

---

## Crash 59: `2215d582f7519b90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019122`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, c3 BLOB NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 60: `f7d27822212d97dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019168`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, c3 TEXT DEFAULT -0); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 61: `76f6124f9227b2cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019180`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 62: `e9a13b3497391d56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019243`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, a REAL PRIMARY KEY, c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 63: `8fa3350f7fd0af15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020895`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL DEFAULT FALSE, c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 64: `68a7f78850acd7c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020907`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('[1,2,3]') , jsonb_each('{}') JOIN json_each('[]
```

---

## Crash 65: `b00494f495ee2452` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020913`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t1 (c3, a) AS (VALUES (CURRENT_DATE)), t2 AS (SELECT *) SELECT *; 
```

---

## Crash 66: `ceb65064907a9c23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020933`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL, CURRENT_DATE WINDOW w1 AS () LI
```

---

## Crash 67: `d20c4dca7dd24d26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020970`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r NOT INDEXED WHERE TRUE GROUP BY NULL, CURRENT_DATE LIMIT NULL; IN
```

---

## Crash 68: `71d993ea56a2a1ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021002`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[]') WHERE NULL INTERSECT SELECT q.*, count(*) BETWEEN N
```

---

## Crash 69: `ea0d4644ef361f0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021038`

```sql
SELECT round(1e308, 4294967296); SELECT printf('%.*s', 0, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELEC
```

---

## Crash 70: `9f5acb9837d65b5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021069`

```sql
SELECT round(1e308, 4294967296); CREATE TABLE IF NOT EXISTS p(a INT DEFAULT '- -V_-8-'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 71: `6ac838bf151c8c8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022371`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 72: `5a28aa9824e57259` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022881`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); SELECT * FROM json_each('{"a":1}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_
```

---

## Crash 73: `c6b0ba1f6642b8c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023945`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY TRUE WINDOW w1 AS (); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 74: `41517937d331d679` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024206`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE - TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 75: `a5a646f06e4ad3fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024212`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_
```

---

## Crash 76: `481158070aa2f7df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024699`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE IN (SELECT *)); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE seed_a(c UN
```

---

## Crash 77: `5e3ef9436d013c6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024708`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 78: `54f699ea13ac027d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024716`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE ~NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 79: `bbcda36fe4dc3e3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024724`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT '', c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE see
```

---

## Crash 80: `5a169d54a28573d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024730`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT *, * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 81: `3b776dfe41d9e143` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024739`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = 
```

---

## Crash 82: `dcc111c95167dbd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024750`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE NULL), TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) 
```

---

## Crash 83: `cd6d307d0f6d8247` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024766`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (VALUES (RAISE(IGNORE) COLLATE RTRIM)) - FALSE) AS sub1; CR
```

---

## Crash 84: `001a21c7b9bf4be8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024785`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE LIKE CASE WHEN RAISE(IGNORE) THEN CURRENT_TIME <= CURRENT_TIME ELSE CURRENT_DATE END IS rank() OVER (ORDER B
```

---

## Crash 85: `ac719fb399656ad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024809`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT p.*, CURRENT_DATE AS e5_u_31n1 FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE seed
```

---

## Crash 86: `cab498ed8d63505d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024816`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP NOT IN (SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIME COLLATE BINA
```

---

## Crash 87: `5e53ea98afa2466c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024826`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE GENERATED ALWAYS AS (FALSE) STORED, b BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; 
```

---

## Crash 88: `9dba660cd90e7245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024839`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p NATURAL JOIN (jsonb_each('[1,2,3]') LEFT OUTER JOIN jsonb_each('[{"a":1},{"b":2}]') JOIN json_eac
```

---

## Crash 89: `81a458ec184ce658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024855`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE & +TRUE | cume_dist() | CAST(CURRENT_TIMESTAMP >> NULL IS NOT NULL ISNULL IS NOT NOT TRUE = +CURRENT_T
```

---

## Crash 90: `b3671e258852f29b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024901`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) GENERATED ALWAYS AS (-FALSE) VIRTUAL, c2 FLOAT DEFAULT TRUE, b TEXT NOT NULL DEFAULT 50); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREA
```

---

## Crash 91: `752e62c83d68c8cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024926`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT FALSE AS j_898_54_38u_l7_f____o_2j25i_3_ul1_465vr8hahx_____s2_um_rtm_ph__535905h86jx8
```

---

## Crash 92: `ce2120eb22d3aee8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024946`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT 0); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 93: `c99842fb4c612a2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024958`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE - FALSE - FALSE - FALSE - FALSE - FALSE - FALSE - FALSE 
```

---

## Crash 94: `048bb5a9cb44d621` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024964`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE - FALSE) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); 
```

---

## Crash 95: `d19a753bfecaf769` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025045`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NULL - CURRENT_TIMESTAMP IS NOT NULL < CURRENT_TIME IS NULL) AS sub1; 
```

---

## Crash 96: `2f764dfdb4c00100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025063`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM (SELECT * FROM p WHERE NULL - CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 97: `7dc4985743993e2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP >= TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 98: `6c22ab3612eda071` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025117`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE >> FALSE - CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 99: `3e751b3417f64cb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT * FROM json_tree(percent_rank() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY TRUE ASC 
```

---

## Crash 100: `01d57a31e66d89af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025186`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL p.* FROM p; SELECT * FROM (SELECT * FROM p WHERE NULL - CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 101: `7025be5054e132c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025253`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NULL - NULL - NULL - NULL - NULL - NULL - NULL - NULL - NULL - NULL - 
```

---

## Crash 102: `abdab3562b4b0870` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025285`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE >> FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 103: `12a9b20cf3c5cd96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025318`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NULL - CURRENT_TIMESTAMP IS NOT NULL < CURRENT_TIME) AS sub1; CREATE T
```

---

## Crash 104: `9fa6882e7adaf023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025327`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NULL - CURRENT_TIMESTAMP < CURRENT_TIME) AS sub1; CREATE TABLE seed_a(
```

---

## Crash 105: `142d57f18cfae6b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025348`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP < CURRENT_TIME) AS sub1; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 106: `6d513a5532364b7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025401`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | TRUE - TRUE NOT BETWEEN TRUE AND CURRENT_TIMESTAM
```

---

## Crash 107: `e62e08a4798b0f2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025427`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CASE WHEN CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)) THEN CURRENT_TI
```

---

## Crash 108: `6d07d2a8e3f84186` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025437`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT -788433, c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | TRUE - FALSE) 
```

---

## Crash 109: `9781de23757cbd63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025446`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE NOT TRUE AND CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 110: `ba98e92ce3087bd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025463`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE CURRENT_TIME GROUP BY percent_rank() FILTER (WHERE CURRENT_TIMESTAMP) OVER () WINDOW w1 AS () LIMIT 
```

---

## Crash 111: `a574d3f065a209bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025471`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a + -2) UNIQUE, c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 112: `288c263793153a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025478`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT NULL, c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | TRUE - FALSE) AS 
```

---

## Crash 113: `8dafcd3bc631533e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025484`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 114: `001397c737450c61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025493`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT q.* FROM p AS v_yi2_p___k_q71h2__b99r_h_76_9__51_ny2w9__7_74__5_tf0; SELECT * FROM (SELECT * FROM p WHERE -CURRENT_
```

---

## Crash 115: `ebf1cbeaa2dd7f6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025500`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | CURRENT_TIME <= CURRENT_TIME - FALSE) AS sub1; CR
```

---

## Crash 116: `7e3baa7da935e57a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025524`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | CURRENT_TIMESTAMP BETWEEN FALSE AND FALSE & CURRE
```

---

## Crash 117: `f708e01967696941` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025644`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT p.*, s.*, -RAISE(IGNORE) BETWEEN RAISE(IGNORE) AND TRUE NOT LIKE TRUE >> CURRENT_TIMESTAMP + CURRENT_DATE 
```

---

## Crash 118: `32a0bdf40663cbb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025667`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP | TRUE - FALSE - FALSE - FALSE - FALSE - FALSE - FA
```

---

## Crash 119: `6bdc00913d46064e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027496`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (b, b, c2, c3, a) VALUES (+CURRENT_TIME NOT LIKE TRUE NOT NULL > ~FALSE <> TRUE NOT 
```

---

## Crash 120: `cb38d23b04a0b3e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027593`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_DATE DESC NULLS FIRST, FALSE IS NULL ASC NULLS LAST; CREATE TABLE seed_a(c 
```

---

## Crash 121: `0b1f6f6daad64f1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027607`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT NULL == FALSE ORDER BY TRUE ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 122: `e0e7eaf0b1409086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027622`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{}') ORDER BY TRUE ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 123: `d865c90657e7b133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027665`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP ORDER BY +++++++++++++++++++++++CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 124: `d924838020d880c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029418`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT ALL sum(CURRENT_DATE) OVER () FROM p); CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 125: `98bbaead63972caf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030153`

```sql
SELECT printf('%x', 0, '-A_D 1 '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 126: `df34444e9dafa92f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030163`

```sql
SELECT printf('%.*s', 9223372036854775807, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 127: `d15f1d441f405457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030199`

```sql
SELECT round(-1.0, -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 128: `3022f792d3e84fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030219`

```sql
SELECT round(1.0, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 129: `f4ad81af2ccd51b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030244`

```sql
SELECT printf('%.*d', 9223372036854775807, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 130: `2f457eae5f008502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030754`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); REPLACE INTO q VALUES (CURRENT_TIME); WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]
```

---

## Crash 131: `7e0ddc5e4b40d274` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030766`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); REPLACE INTO q VALUES (CURRENT_TIME); SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY json_typ
```

---

## Crash 132: `677134b7e80d3f57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030807`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); REPLACE INTO q VALUES (CURRENT_TIME); SELECT ALL sum(CURRENT_DATE) OVER (ORDER BY TRUE ASC ROWS BETWEEN 
```

---

## Crash 133: `84f50a6611b42642` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030924`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 134: `55400e2eb80a07a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031992`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (RAISE(IGNORE)), c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 135: `4be219b8686ac263` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031998`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (FALSE IS NULL), c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c U
```

---

## Crash 136: `de0849a724f4ed15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032026`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT ' -A18F _hi --'); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 137: `9240966a333b2693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032145`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIME; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 138: `ed4ffb35b36ca750` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032155`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIME; PRAGMA integrity_check; CREATE TABLE seed_a
```

---

## Crash 139: `cbcc9d37554adfd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032332`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT -31.9239443748663939); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 140: `2558ce4288f55e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037949`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT CURRENT_DATE AS e5_u_31n1 FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 141: `eabc57ba383f9e63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038012`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, c2 GENERATED ALWAYS AS (a) UNIQUE, a DATE NOT NULL DEFAULT 92567750121086292366221488341588979158214236474852576796963525863325217877987185461793267008939949808196
```

---

## Crash 142: `9e5d5180dc652470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038181`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NULL > TRUE COLLATE BINARY; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 143: `5ecaef70de06ba4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038267`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_DATE AS e5_u_31n1 FROM p WHERE NOT EXISTS (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 144: `0b877abadcce11d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038437`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p WHERE NULL GROUP BY NULL WINDOW w1 A
```

---

## Crash 145: `b644034a1bc549f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038899`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT -788433); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = s
```

---

## Crash 146: `6a73ae3eea40bd51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039003`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{}', '$.a') NOTNULL - CURRENT_TIMESTAMP ISNULL; CREATE TABLE
```

---

## Crash 147: `71e5eda9b0ef4020` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039080`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT 3794537025114333983640729.3); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); 
```

---

## Crash 148: `794461caee8fcbd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 149: `33ff60ec79467936` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041067`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF 
```

---

## Crash 150: `05a1233a33a4c780` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041584`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (+++++++++CURRENT_TIME NOT IN (FALSE)); PRAGMA quick_check; CREATE TA
```

---

## Crash 151: `d794aae86af8d170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041634`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 152: `930897c456208ef3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041664`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (~~~~~~~CURRENT_DATE)); PRAGMA quick_check; CREATE TABL
```

---

## Crash 153: `d0e02a0917917e01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041671`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (NOT EXISTS (VALUES (CURRENT_TIME)) - FALSE)); PRAGMA q
```

---

## Crash 154: `b5adedf4327eb007` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041678`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (CURRENT_TIME, CURRENT_TIME)); PRAGMA quick_check; CREA
```

---

## Crash 155: `36fac65ecc0b0086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041762`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (FALSE NOT IN (FALSE NOT IN (FALSE NOT IN (FALSE NOT IN
```

---

## Crash 156: `a95f47d24707b71c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044088`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED CROSS JOIN (p NATURAL JOIN json_tree('[{"a":1},{"b":2}]')) WHERE TRUE GROUP BY
```

---

## Crash 157: `47220b973e3f0695` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED CROSS JOIN (p NATURAL JOIN json_tree('[{"a":1},{"b":2}]')) WHERE TRUE GROUP BY
```

---

## Crash 158: `ce3a647917bf5b11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED CROSS JOIN (p NATURAL JOIN json_tree('[{"a":1},{"b":2}]')) WHERE TRUE GROUP BY
```

---

## Crash 159: `e7529549b4089feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045572`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NATURAL JOIN json_tree('[{"a":1},{"b":2}]'); CREATE TAB
```

---

## Crash 160: `c9638ce7d508415b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045602`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME, CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 161: `1b8c2c1fe2ede4ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045618`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT ALL row_number() OVER (ORDER BY TRUE ASC ROWS BETWEEN CURRENT_DATE P
```

---

## Crash 162: `df0cc0d90190ce90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045641`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE NULL), TRUE); CREAT
```

---

## Crash 163: `9cc66947ee3bc6fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045662`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UN
```

---

## Crash 164: `17b73ecf6322a43f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051258`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL DEFAULT X'B7EAEB47', a FLOAT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE) AS su
```

---

## Crash 165: `7d8878145c2765f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051299`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); SELECT (SELECT DISTINCT * FROM p) AS a FROM (SELECT * FROM q WHERE CURRENT_TIME) AS sub1; CREATE TABLE seed_a
```

---

## Crash 166: `e0e05cbd4f916599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051489`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p (c3, c3, _rowid_) VALUES (NULL, FALSE, TRUE); SELECT DISTINCT * FROM json_each('{}') WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS 
```

---

## Crash 167: `ecaa6f63b52881e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051507`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p (c3, c3, _rowid_) VALUES (NULL, FALSE, TRUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('{}') LEFT OUTER JOIN p ON 838278812717702027810767054
```

---

## Crash 168: `2d1ac8054a7cd4e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052493`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (TRUE OR CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 169: `be2d96a08af4c53f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057708`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR FAIL INTO p VALUES ('-'); SELECT ALL row_number() OVER () FROM p; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 170: `bc69e54f9754ab89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057735`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR IGNORE INTO p VALUES (X'ddACd9Fc'); SELECT ALL row_number() OVER () FROM p; CREATE TABLE seed_a
```

---

## Crash 171: `46b9999a81dc95a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057752`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT ALL first_value(FALSE) OVER () FROM p; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 172: `0d068615e222b8d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057767`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE 
```

---

## Crash 173: `2fd782b127a687dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057777`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT ALL row_number() OVER (PARTITION BY CURRENT_TIMESTAMP IN (VALUES (TR
```

---

## Crash 174: `54ce3a4ad3539d2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057875`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT ALL row_number() OVER () FROM p; CREATE TABLE IF NOT EXISTS p(c1 FLO
```

---

## Crash 175: `ca923246fdbb239d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058064`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, *, *, *, *, *, * FROM json_tree('{"a":{"b":1}}'); CREATE
```

---

## Crash 176: `4e566cfd16072f6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058108`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (count(*) FILTER (WHERE CURRENT
```

---

## Crash 177: `b29dde39b84f26bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058116`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_TIME) UNION VALUES (TRUE))); SELEC
```

---

## Crash 178: `2bbb387e168ec111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058133`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('[{"a":1},{"b":2}]') GROUP BY FALSE, NULL; CREATE T
```

---

## Crash 179: `d2f76bb0900873a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058152`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{}') LEFT OUTER JOIN p ON CURRENT_TIME; C
```

---

## Crash 180: `cb576d8042b7fadd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059984`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED CROSS JOIN (p NATURAL JOIN json_tree('[{"a":1},{"b":2}]')) WHERE TRUE GROUP BY
```

---

## Crash 181: `02a54ae12901efa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059996`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED CROSS JOIN (p NATURAL JOIN json_tree('[{"a":1},{"b":2}]')) WHERE TRUE GROUP BY
```

---

## Crash 182: `c06a962410491272` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060153`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE AS t_k, CURRENT_TIME IS NULL, * FROM (VALUES (TRUE == RAISE(IGNORE), NULL IS NOT NULL)) AS a LEFT JOIN
```

---

## Crash 183: `3354a2cb41e83516` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063130`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (total_changes()); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 184: `d78c9b24179c9796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063633`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (json_quote(CURRENT_TIME NOT IN (-CURRENT_TIMESTAMP))); PRAGMA quick_
```

---

## Crash 185: `9fc6864ff175caf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063762`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (FALSE NOT IN (NOT CURRENT_DATE))); PRAGMA quick_check;
```

---

## Crash 186: `1bebffc4c82cf578` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063774`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 187: `aef8e69f033eb554` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063817`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT IN (FALSE NOT IN (FALSE NOT IN (NULL, FALSE, TRUE)))); PRA
```

---

## Crash 188: `3978cd547352f734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063854`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (json_quote(last_insert_rowid())); PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 189: `fe81fb892df63b39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065462`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 190: `30ac87a62da3c66b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT *, count(*) FILTER (WHERE CURRENT_TIME) FROM p NATURAL JOIN p WHERE json_remove('{}', '$.a'); CREATE TA
```

---

## Crash 191: `8b61dd4562623960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{}', '$.a[#-1]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 192: `40421ebb4690b72e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068666`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_remove('[1,2,3]', '$.a'); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 193: `6fdc90e0bc6008f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068739`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{}', '$[0].key'); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 194: `c21ecb159ad3a649` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068762`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{"a":{"b":1}}', '$.a'); CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 195: `3941eaa74b2da87d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068854`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT 3794537025114333983640729.3); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME GLOB CURRENT_DATE COLLAT
```

---

## Crash 196: `5e35cb4649eb2940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068922`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT 3794537025114333983640729.3); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); VALUES (TRUE) UNION SELECT ALL CURRENT_TIMESTAMP FROM json_each('[{"a":1},
```

---

## Crash 197: `954c5284e346819b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069290`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (random()); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 198: `62eb19177afb02b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069306`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); VALUES (CURRENT_DATE) UNION SELECT ALL percent_rank() OVER () FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 199: `8ebc1574f870ed7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069319`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP > TRUE OR CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 200: `0ef45d014b2ab44a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069346`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP > CAST(TRUE AS REAL); CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 201: `3d85d8ff02253dba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069668`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (X'961b') EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 202: `293726d88a9a5b25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069711`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT NULL = NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 203: `e81789ee14f6e9f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069833`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, c2 GENERATED ALWAYS AS (a) UNIQUE, a DATE NOT NULL DEFAULT 92567750121086292366221488341588979158214236474852576796963525863325217877987185461793267008939949808196
```

---

## Crash 204: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001804`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 205: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001832`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 206: `5e9b86cbf10fd5c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002024`

```sql
SELECT printf('%.*d', 9223372036854775807, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 207: `a93b20de0dabdf40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002034`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 208: `c016404df6e837a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002085`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE
```

---

## Crash 209: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002094`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 210: `8d6fa0b4aeec7fa3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002103`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1
```

---

## Crash 211: `49a7c25f6b4380bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002110`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1
```

---

## Crash 212: `3c400a0f61b8f224` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002191`

```sql
SELECT substr('4k5--E', -9223372036854775808, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(4
```

---

## Crash 213: `e43fa375054964de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002245`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 214: `be03aa17f8156a3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002352`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL);
```

---

## Crash 215: `7339173871b2932a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002639`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 216: `98e5177bfefdc28b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002660`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 217: `ee6b9b6dcd32f4ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002729`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 218: `98088bc159580758` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002893`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 219: `8051f3ffc35f1d11` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003330`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * CURRENT_TIMESTAMP IS NULL > TRUE COLLA
```

---

## Crash 220: `812a9acaf8a3995e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003344`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * TRUE COLLATE BINARY ISNULL; CREATE TAB
```

---

## Crash 221: `df5d3e9bfc64a839` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * FALSE > TRUE COLLATE BINARY ISNULL NOT
```

---

## Crash 222: `26f396c39b2d9303` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003382`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * FALSE > TRUE COLLATE BINARY ISNULL NOT
```

---

## Crash 223: `c8ee9296d211546f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003403`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE NOT LIKE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 224: `2f3409d19f93309a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003412`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 225: `5585c3fadd5ef92e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003439`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP COLLATE NOCASE * FALSE > TRUE COLLATE BINARY ISNULL NOT
```

---

## Crash 226: `ce6bd3576ad69bc2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003795`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NOT json_type(NOT +FALSE 
```

---

## Crash 227: `b383a32d9f5be05f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003802`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NOT json_type(NOT +FALSE 
```

---

## Crash 228: `b85951f562a639d2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003840`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE >> FALSE WINDOW w1 
```

---

## Crash 229: `478fbb5511d6e333` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003867`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY CURRENT_TIME WINDOW w1 AS
```

---

## Crash 230: `32b590506c3debed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003885`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 231: `658b4760e354cc12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT (total_changes() FILTER (WHERE NULL)) OFFSET RAISE(IGNORE); INSERT INTO p DEF
```

---

## Crash 232: `fda03c3836eafc41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004125`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 233: `55ff95fe2c6db947` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004458`

```sql
SELECT round(1.0, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 234: `9a8b1583a50ca513` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004883`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE IS NOT NULL ORDER BY CURRENT_TIME > TRUE / NULL ASC NULLS LAST; SELECT hex(zeroblob(-1)); CREATE TABLE s
```

---

## Crash 235: `ba791d28278e5b58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004965`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 236: `24540121910b7145` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005087`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 237: `2ca36d356b749d68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005525`

```sql
SELECT printf('%.*g', 4294967296, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 238: `db169988f4707373` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005588`

```sql
SELECT printf('%s', 4294967296, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE 
```

---

## Crash 239: `ef7e2a71f325924c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006026`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 240: `c2f7eae0ac8341fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007381`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 241: `3d0efedcdf6f83d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017781`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 242: `802a0960ef04f69c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018033`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 243: `7700371078a10511` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018091`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 244: `38bf57a044043560` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020652`

```sql
SELECT round(1e308, 4294967296); SELECT round(-1e308, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO
```

---

## Crash 245: `82f404f4520e1ae4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020870`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INT GENERATED ALWAYS AS (NULL) STORED, c3 INT NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 246: `77c030862d035c15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022022`

```sql
SELECT substr('', 4294967295, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 247: `5f034909e1a3f5ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022068`

```sql
SELECT substr('', 4294967295, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 248: `d94e6df69d4354b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022109`

```sql
SELECT printf('%.*g', 2147483648, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 249: `9b896bd17a27dbb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023965`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 250: `7e0933e1308a1533` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023992`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') CROSS JOIN json_tree('[{"a":1},{"b":2}]') NATURAL JOIN json_each('{"a":1}'); CREATE TABLE see
```

---

## Crash 251: `27af851a9702ca3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024006`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 252: `a3e56b5e97ae9d75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028468`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (-CASE WHEN CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)) THEN CURRENT_TIME ELSE TRUE END); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 253: `9b88ed18d542e56d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032674`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 IN
```

---

## Crash 254: `8bc5bdf4d0bec3ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033403`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') ORDER BY TRUE ASC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 255: `b5b9dd9de605ff73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033429`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 256: `38e4c3c9cb0767d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') NATURAL LEFT JOIN (jsonb_each('[]')) LIMIT total_changes() FILTER (W
```

---

## Crash 257: `9d9c74c177e548d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033491`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT total_changes() FILTER (WHERE NULL) OFFSET RAISE(IGNORE); INSERT OR ABORT INT
```

---

## Crash 258: `998c1f174e117674` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033501`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{"a":{"b":1}}') CROSS JOIN json_tree('[]') USING (rowid, a) LIMIT total_changes() FILTER
```

---

## Crash 259: `e75d8e13afed57e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033510`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q INDEXED BY a LIMIT total_changes() FILTER (WHERE NULL) OFFSET RAISE(IGNORE); INSERT INTO p DEFAULT
```

---

## Crash 260: `a301b7454d42349b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033530`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT -31.9239443748663939, c2 DATE UNIQUE, b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT total_changes() F
```

---

## Crash 261: `1bd2121c52b681c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033561`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(-CURRENT_TIME LIKE +CURRENT_TIME ESCAPE RAISE(IGNORE) NOTNULL IS NOT lag(TRUE IN (RAISE(IG
```

---

## Crash 262: `e00a9586f2ba1228` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033567`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (json_tree('{}') , json_each('[]')) NATURAL JOIN json_tree(CURRENT_TIMESTAMP > NULL > CURRENT_DATE N
```

---

## Crash 263: `b4cab2f0b7cd6582` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033575`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree(CASE WHEN RAISE(IGNORE) THEN CURRENT_TIME COLLATE BINARY ELSE FALSE END % EXISTS (SELECT *
```

---

## Crash 264: `3c4f79bbad044d34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033612`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT total_changes() FILTER (WHERE NULL) OFFSET RAISE(IGNORE); INSERT I
```

---

## Crash 265: `c17f37100179deb8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033647`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT total_changes() FILTER (WHERE NULL) OFFSET RAISE(IGNORE); INSERT INTO p DEFAU
```

---

## Crash 266: `39767a9600aac900` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033653`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('{}') LIMIT total_changes() FILTER (WHERE NULL) OFFSET RAISE(IGNORE); INSERT INTO p DEFAU
```

---

## Crash 267: `df8d395b23291067` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033851`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 268: `7af988b7d9083e0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033941`

```sql
SELECT substr(' _2y- _Y 3zp', -2147483648, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),
```

---

## Crash 269: `f403c95cdc5cc3b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034015`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY CURRENT_DATE LIKE CURRENT
```

---

## Crash 270: `e86911692d5f8b32` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034023`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NOT FALSE || +CURRENT_TIM
```

---

## Crash 271: `a2fe43ec26c1ecf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034038`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NULL HAVING CURRENT_DATE 
```

---

## Crash 272: `58d4830013734c62` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034088`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NOT EXISTS (VALUES (RAISE
```

---

## Crash 273: `c602c2b3ca3ddfc4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034112`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NULL, CURRENT_DATE WINDOW
```

---

## Crash 274: `96f1b13ea3a66f3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034223`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p NATURAL JOIN json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROU
```

---

## Crash 275: `35b54549b4f371c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034238`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY CURRENT_TIME WINDOW w1 AS (
```

---

## Crash 276: `18f8fe78316ab2a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034264`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE / (CURRENT_TIMESTAM
```

---

## Crash 277: `869cb0de03c8be21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034271`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH t1 (c3) AS (VALUES (CURRENT_DATE)), t2 AS (SELECT *) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE 
```

---

## Crash 278: `7685d7260cc6d9f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034322`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE >> FALSE WINDOW w1 
```

---

## Crash 279: `ac5009595801f6a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034333`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE >> CURRENT_DATE IN 
```

---

## Crash 280: `648e737f860e88ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER DEFAULT X'3fDBBf40'); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each(
```

---

## Crash 281: `f84ae16af4b9b538` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034378`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY FALSE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT 
```

---

## Crash 282: `d6b26721a277b275` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034385`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE >> FALSE WINDOW w1 
```

---

## Crash 283: `ad51cc237b305f03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034460`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE X'961b' GROUP BY FALSE >> FALSE WINDOW w1 AS ()
```

---

## Crash 284: `d3c1be6d00d6b3b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034476`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY FALSE >> FALSE WINDOW w1 
```

---

## Crash 285: `5c499d64e92cd064` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034515`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p NOT INDEXED CROSS JOIN json_tree('[]') WHERE CURRENT_DATE GROUP BY 
```

---

## Crash 286: `732544c2d3da5118` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034991`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('[{"a":1},{"b":2}]') LEFT OUTER JOIN json_tree('[{"a":1},{"b":2}]') NATURAL JOIN json_each('{"
```

---

## Crash 287: `b23d14dd7545e327` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035019`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME BETWEEN NULL AND CURRENT_TIMESTAMP NOT IN (CURRENT_DATE)); CREATE TAB
```

---

## Crash 288: `48f84cb14fbe01ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035211`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) INTERSECT SELECT ALL sum(CURRENT_DATE) OVER (ORDER BY TRUE ASC ROWS BETWEEN CURRENT_DATE PRECEDING A
```

---

## Crash 289: `06c4a93a84901a49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035341`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) INTERSECT SELECT ALL count() OVER () FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 290: `beddc8bfd196ff80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035369`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (TRUE IS rank() OVER ()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 291: `8c571f5f294a1cad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035983`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (RAISE(IGNORE)), c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 292: `931fc8f42fbebae4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035993`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL GENERATED ALWAYS AS (FALSE) VIRTUAL, c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TA
```

---

## Crash 293: `91ec151a5023faaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036011`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a * a) UNIQUE, rowid INT PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 294: `74afe51936c2cf17` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036024`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a + -2) UNIQUE, c1 INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 295: `191b74bb94cef5d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036046`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 296: `5f34e13f010501b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036052`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IN (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 297: `fe98498306754f6f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036061`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT -0); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 298: `ac4e17e02be26e01` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036067`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 299: `0b6770a357e86119` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036138`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY, a INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 300: `48c2d6ee20bee880` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036464`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * FALSE <> CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 301: `fd317bc7229ed9ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036502`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIME + CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP IS NULL >
```

---

## Crash 302: `76eaaeb916154f03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036511`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY CURRENT_TIME WINDOW w1
```

---

## Crash 303: `bf57a6183f304dfe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036517`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM q WHERE EXISTS (VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE NULL), TRUE)); CREATE TA
```

---

## Crash 304: `d3c8174853a463b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036540`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE, a INT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIMESTAMP IS NULL > TRUE; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 305: `6ddf1261bb17d352` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036560`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c3 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIMESTAMP IS NULL > TRUE; CREATE 
```

---

## Crash 306: `cec9e63d0ebbf105` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_quote(FALSE NOT IN (NULL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 307: `dab3557f15d66775` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE * CURRENT_TIMESTAMP IS NULL > CURRENT_TIME BETWEEN NULL AND CURRENT
```

---

## Crash 308: `57330004b0c8160f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036728`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME + CURRENT_TIME IS NULL > TRUE; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 309: `d47806d9db767721` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036786`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); SELECT * FROM p NATURAL JOIN p WHERE TRUE NOT LIKE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 310: `e3b32286b9bf18c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036807`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE TRUE NOT LIKE CURRENT_TIMESTAMP COLLATE NOCASE * CURRENT_TIMESTAMP IS NUL
```

---

## Crash 311: `874df7c123fae9ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036836`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP >> CURRENT_DATE NOT LIKE CURRENT_TIME; CREATE TABLE see
```

---

## Crash 312: `4783cf133e965cf8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037025`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE NOT LIKE CASE CURRENT_DATE WHEN CURRENT_TIMESTAMP BETWEEN FA
```

---

## Crash 313: `4741e581afaae2e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037060`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE NOT LIKE 503030091049891332265593772074287174060101993892711
```

---

## Crash 314: `b114d468bd316f2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037200`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT NOT NULL DEFAULT 0, a INT GENERATED ALWAYS AS (NULL) STORED, c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE TR
```

---

## Crash 315: `42a3de420fcda444` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM (SELECT * FROM p WHERE json_quote(FALSE)) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 316: `f8547a20d9f578d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037236`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (CURRENT_TIME)) - FALSE ISNULL NOT LIKE FALSE; CREATE 
```

---

## Crash 317: `d10b5ac4aaa0aede` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037425`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT rowid FROM q WHERE EXISTS (VALUES (NULL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 318: `d5d9c77c4719cf88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037457`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT X'aeA5'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 319: `7cd283560ef7519c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037464`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_quote(CURRENT_TIME BETWEEN NULL AND CURRENT_TIMESTAMP NOT IN (CURREN
```

---

## Crash 320: `32b8f2d287acdac6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037504`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) UNION ALL SELECT * FROM jsonb_tree('{"a":1}') GROUP BY random() OVER (ORDER BY CURRENT_TIMESTAMP DE
```

---

## Crash 321: `60d90c2a8a8389ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('[{"a":1},{"b":2}]') , json_tree('[{"a":1},{"b":2}]'
```

---

## Crash 322: `8b240ffc1532e8e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037604`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMES
```

---

## Crash 323: `0e9445043c3de28f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043234`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (FALSE NOT LIKE CURRENT_TIMESTAMP) EXCEPT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 324: `d8a5b6db4e325c2d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043258`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 325: `e4537445224bd125` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043272`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP % random()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 326: `98f6f5fd82f921d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043297`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (rank() OVER ()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 327: `3ddd0d0529f84948` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043430`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (NULL) EXCEPT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 328: `b68d58e242263a30` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044579`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP IS TRUE NOT NULL; CREATE TABLE seed_t
```

---

## Crash 329: `2107eb2c4ac2006c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045180`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 330: `c9a2553413ccffb9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045219`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIME 
```

---

## Crash 331: `271a8d5de0c2b6af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045225`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT X'3fDBBf40'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_
```

---

## Crash 332: `fbcc9a599119e421` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045232`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_DATE IN (SELECT CURRENT_DATE IN (VALUES (NULL)))); EXPLAIN QU
```

---

## Crash 333: `e4a88d3aa04d6bde` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045268`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE
```

---

## Crash 334: `97f33dc9fe28cf0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045275`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE LIKE
```

---

## Crash 335: `dbcb948bad08d166` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045282`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT * FROM json_each('[{"a":1},{
```

---

## Crash 336: `9f3db2f4c0e97824` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045334`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (''); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c
```

---

## Crash 337: `3f39ab3400e13acf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045398`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE
```

---

## Crash 338: `59b1238ebd53b7ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046071`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIME COLLATE BINARY) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 339: `d32c7c59848778be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046083`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE LIKE TRUE ESCAPE NULL) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 340: `71517fef2f91126e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046120`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY CURRENT_TIME WINDOW w1 AS () UNION VALUES (CURREN
```

---

## Crash 341: `ea1a948ab4024a91` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046129`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 342: `c5f730b92fee30ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046151`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (TRUE >> CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 343: `6f5a0aca3897d018` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046526`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION SELECT ALL sum(CURRENT_DATE) OVER (ORDER BY TRUE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW) F
```

---

## Crash 344: `66903257d5c7ceda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046563`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('{}') WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST LIMIT ~CURRENT_DATE; CREATE TABLE see
```

---

## Crash 345: `b2edc1b10a484416` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046608`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (6.086099429282847828977378870710232504920259716175116101380e-17 IS NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 346: `881c868b4d372d15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046869`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION SELECT DISTINCT CURRENT_DATE AS d944_02 FROM json_each(CURRENT_TIMESTAMP, '$[#-1]') WHERE NULL; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 347: `0957cb79f9f4184f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047081`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIME GROUP BY
```

---

## Crash 348: `89a8d3348f3909b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047098`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[{"a":1},{"b":2}]'
```

---

## Crash 349: `960ee615a676456c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047326`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 350: `3fa4eb4aab54496e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047338`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE TRUE ESCAPE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 351: `f05b8abddd8872be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048327`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('{}') WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST LIMIT FALSE OFFSET CURRENT_DATE; C
```

---

## Crash 352: `9df277beb663e87d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048333`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (X'5eA77B9aa8'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT
```

---

## Crash 353: `8eebbd9077274f3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050812`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY, c2 REAL UNIQUE, c3 BOOLEAN UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 354: `9887115659023dbf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050868`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY, c2 BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(a); WITH RECURSIVE q AS (VALUES (CURRENT_DATE)) SELECT CAST(TRUE AS INTEGER) FROM p; CREATE TABLE 
```

---

## Crash 355: `edb8c10f3d2f36a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050879`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY, c2 BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT DISTINCT *, *, *, *, *, *, *, * FROM json_each('{}') WHERE CURRENT_TIMESTAMP; CREATE TA
```

---

## Crash 356: `15276805eed921a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050975`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c2 BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 357: `85753a851c5d8136` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051032`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY, c2 BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY TRUE; CREATE TABLE s
```

---

## Crash 358: `789f92aa5faeab1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053194`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p NATURAL JOIN json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY CURRENT_TIME W
```

---

## Crash 359: `fbfcee33b81345c3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055021`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_T
```

---

## Crash 360: `2a1c9c59fa9a9766` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055718`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p WHERE NULL GROUP BY NULL WIN
```

---

## Crash 361: `d26130d5721121e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055724`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (dense_rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 362: `8945a0b1945f9864` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055997`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT ALL * FROM json_tree(CURRENT_DATE * CURRENT_TIMESTAMP * CURRENT_DATE, '$[#-1]') UNION SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE N
```

---

## Crash 363: `35ca1c138e5f57f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056042`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY TRUE WINDOW w1 AS () UNION SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE NULL; CRE
```

---

## Crash 364: `9b2b25e7b194ec21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056062`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT ALL * FROM json_tree(FALSE - NULL, '$[#-1]') UNION SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE NULL; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 365: `5a23f56ef1ccace6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056087`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT ALL * FROM json_each(FALSE || CURRENT_TIMESTAMP NOT NULL, '$') UNION SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE NULL; CREATE TABLE
```

---

## Crash 366: `29b47350a5e651c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056184`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[1,2,3]') UNION SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 367: `b033bf5f0f3a2fd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056270`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION ALL SELECT DISTINCT CURRENT_DATE AS d944_02 FROM json_each(CURRENT_TIMESTAMP, '$[#-1]') WHERE NULL; CREATE TABLE seed_t1(c1 
```

---

## Crash 368: `1cba25384f741042` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056282`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION SELECT FALSE ORDER BY FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 369: `520b373fe861e58b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056376`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1, c3, b); VALUES (TRUE) UNION SELECT DISTINCT CURRENT_DATE AS d944_02 FROM json_each(CURRENT_TIMESTAMP, '$[#-1]') WHERE NULL; CREATE TABLE seed_t
```

---

## Crash 370: `a9922f102cea0af5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056616`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (count(*)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 IN
```

---

## Crash 371: `065d3e709a7e5582` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056772`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_DATE * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE * CURRENT_TIM
```

---

## Crash 372: `4ae8129cbe0b47c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056779`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION SELECT ALL FALSE IS FALSE FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 373: `c70704441be5c711` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056787`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_DATE ASC, CURRENT_TIMESTAMP DESC; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 374: `fe9c6d9732ff7bda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056902`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 375: `635bcfcad5b05294` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056910`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE) UNION VALUES (TRUE); CREATE
```

---

## Crash 376: `dec2a49cce55e6d2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056925`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 377: `1a52550ada5f477b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056957`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIME) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 378: `e158d9ff4a717d35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057528`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (FALSE == CAST(TRUE AS DATE) IN (CURRENT_TIME, CURRENT_TIME)) UNION VALUES (TRUE >> CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 379: `af02e715ab95dcd3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057536`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (-CURRENT_TIMESTAMP | TRUE - FALSE >> CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 380: `78028f1352c4943b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057640`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE
```

---

## Crash 381: `b4c67e8006c59c84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058433`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ABORT INTO p VALUES (json_quote(FALSE)); SELECT * FROM p NATURAL JOIN p WHERE CURR
```

---

## Crash 382: `4bfa5cb18c85df5a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058458`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (TRUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME ORDER BY row
```

---

## Crash 383: `aadc4ef0c4a5da2b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058497`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) UNION VALUES (json_patch('[1,2,3]', '[{"a":1},{"b":2}]')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 384: `c4629afa2b531d13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058503`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT * FROM json_tree(percent_rank() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY TRUE ASC
```

---

## Crash 385: `f9832e865d9ef3ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058517`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT ' -A18F _hi --'); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); REPLACE INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_D
```

---

## Crash 386: `4bdd388f608412be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058541`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME NOT IN (-CURRENT_TIMESTAMP)); SELECT * FROM p
```

---

## Crash 387: `033d89316a2eb7de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058655`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (TRUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME ORDER BY CUR
```

---

## Crash 388: `422a1db87d1c8e71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058667`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (TRUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME ORDER BY CURRENT_DATE DESC NU
```

---

## Crash 389: `0765fbc051669acc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060390`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (NULL) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); E
```

---

## Crash 390: `36fa6d54f9802642` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061797`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (rank() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST ROWS BETWEE
```

---

## Crash 391: `d1aae097ec971fbe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061821`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (rank() OVER ()) INTERSECT VALUES (json_quote(CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 392: `2d5f839d7123d707` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061832`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE * CURRENT_TIMESTAMP * CURRENT_DATE * CURRENT_TIMESTAMP * CURRENT_DATE * CURRENT_TIMEST
```

---

## Crash 393: `06fb54e3c23f0d5a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068151`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP IS TRUE; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 394: `bbd046687e2cb0db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068223`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CAST(TRUE AS DATE) IN (CURRENT_TIME, CURRENT_TIME); SELECT substr('', 429
```

---

## Crash 395: `ed5dee3d13c16c44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068582`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IN (CURRENT_TIME, CURRENT_TIME); SELECT substr('', 429496729
```

---

## Crash 396: `9dc078dccc444d7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069990`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_quote(NULL) * CURRENT_DATE LIKE CURRENT_TIMESTAMP IS CURRENT_TIMESTA
```

---

## Crash 397: `1eba8bbc29fdb105` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070054`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE json_quote(NULL) * -CURRENT_TIMESTAMP | TRUE; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 398: `0bd615db681c7302` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070166`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE TRUE * -CURRENT_TIMESTAMP | TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 399: `7b8ba64bbeae0875` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMES
```

---

## Crash 400: `91e75972ddf20881` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070628`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE 
```

---

## Crash 401: `fab0cbce8d1c23ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070634`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMES
```

---

## Crash 402: `e35b08b1b4f454a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070645`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP >> CURRENT_DATE + CURRENT_DATE COLL
```

---

## Crash 403: `b26f952deb2774ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070655`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * FALSE || CURRENT_TIMESTAMP NOT NU
```

---

## Crash 404: `2003824f7589781b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMES
```

---
