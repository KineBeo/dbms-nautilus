# Crash Triage Report

**Total crashes:** 328  
**Unique crash sites:** 328  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 12 | 12 | 3% |
| Signal | 316 | 316 | 96% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `47bff0a4d8337d66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000173`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE q AS MATERIALIZED (VALUES (CURRENT_TIMESTAMP) ORDER BY TRUE DESC, CURRENT_DATE IS NULL DESC) SELECT +ifnull(FALSE IS DISTINCT FR
```

---

## Crash 2: `88ecd762a16d3a5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000594`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c1); SELECT CURRENT_DATE IS NULL COLLATE NOCASE || RAISE(IGNORE) < NULL GLOB ~CURRENT_TIME AS j FROM (SELECT CURRENT_DATE LIKE FALSE NOT IN 
```

---

## Crash 3: `6405fb0e112fd5dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001080`

```sql
SELECT printf('%s', 2147483648, 'yT_--1C_ '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT q.* FROM q JOIN r a ON CASE WHEN (CURRENT_DATE) < jsonb_patch('{}', '[1,2,3]') FILTER (WH
```

---

## Crash 4: `c20e9ad5e9b01e57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001650`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, b, a, b, a, c3); SELECT NOT EXISTS (SELECT DISTINCT r.* FROM (json_each('{"a":{"b":1}}')) INNER JOIN p INDEXED BY c3 WHERE RAISE(IGNOR
```

---

## Crash 5: `a69eaa25a7f671d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001920`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 6: `cc8d1dbd80c7f5c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001926`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT s.*, *; SELECT printf('%.*s', 21474
```

---

## Crash 7: `ae1ab294e9d60bcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001933`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT s.*, *; SELECT printf('%.
```

---

## Crash 8: `61c11cd28762a2d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001954`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); S
```

---

## Crash 9: `b6d7d2f22bc92dcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005823`

```sql
SELECT printf('%llu', 0, '_-Ex'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT ~CASE WHEN random() FILTER (WHERE RAISE(IGNORE)) OVER (PARTITION BY NULL OR RAISE(IGNORE) <= CUR
```

---

## Crash 10: `f7265742b86c95ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012247`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT CURRENT_TIMESTAMP GLOB FALSE > NULL AS a FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 11: `0e92d070e7272c8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020013`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TA
```

---

## Crash 12: `7abc1c27e2e21ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029833`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 13: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001870`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 14: `6ebea3693ead00c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002123`

```sql
SELECT printf('%.*d', -9223372036854775808, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 15: `d76ec25c9198ef18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002133`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 16: `cd811e72ee84d7dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002276`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 17: `fd67e2f4b4d67a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002287`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 18: `1992af63599b9d69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002294`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 19: `7b700e1313e9684e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002300`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE s
```

---

## Crash 20: `c7d5c8e2c1a14068` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002312`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 21: `26aa84e7119a624e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002649`

```sql
SELECT substr('', 9223372036854775807); SELECT printf('%.*f', -1, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO s
```

---

## Crash 22: `49591b01c28715c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002692`

```sql
SELECT substr('', 9223372036854775807); SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VA
```

---

## Crash 23: `bfaed22d4dc86453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003551`

```sql
SELECT round(1e308, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 24: `a4283ceaab3b9c2b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003774`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 25: `d6f233a9dc7ce40a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003801`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 26: `1f0da2fe948a393c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003821`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 27: `14854afb77e93c19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003832`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTE
```

---

## Crash 28: `9029f4806227f3ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003838`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 29: `b9c40d63a9ceadca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003844`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 30: `390c8693b3c92cbe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003865`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 31: `ee2e9138f9f5cea5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003878`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 32: `f3aa2f33ffe858a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003973`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 33: `dbf62319c1469cc6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003979`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 34: `18a1c988b0a7a1e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003994`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 35: `d5927090ac1736ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004325`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)) SELECT NULL AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 36: `b1a6606c9a102933` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005113`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE >> TRUE ISNULL IS NOT NULL); EXPLAIN QUERY PLAN VALUES (NULL AND TRUE BET
```

---

## Crash 37: `570bb14134b9c2ef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005194`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 38: `a5bd8767d8e267b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005504`

```sql
SELECT printf('%.*g', 9223372036854775807, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 39: `d8da0e2cd007e63d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006322`

```sql
SELECT round(1.0, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c
```

---

## Crash 40: `121c1cad1d2406a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007148`

```sql
SELECT round(1e308, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 41: `2b64a1c9835da574` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007248`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t
```

---

## Crash 42: `738080de1e8ca4bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007270`

```sql
SELECT printf('%.*g', -2147483648, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 43: `9717ff660fa7315e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007373`

```sql
SELECT round(1e-308, -9223372036854775808); SELECT printf('%s', 0, 'R'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO se
```

---

## Crash 44: `cb73d11222b7b33a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007579`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 45: `2f3a977fd9e80f3c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007771`

```sql
SELECT printf('%.*f', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 46: `6611542478ad7076` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009409`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RA
```

---

## Crash 47: `449d08a3f03420fd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009637`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION SELECT * FROM t2 NOT INDEXED GROUP BY TRUE, CURRENT_TIME; VALUES (NULL); CREATE TABLE seed_t0 (c0 INTEGER
```

---

## Crash 48: `a9e8f16d3f7b622b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010000`

```sql
SELECT substr('-prO-__HL__', 2147483648, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 49: `f4948ded56128e30` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010008`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (NULL IS NOT NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 50: `f6a93e05a0496852` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010017`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (TRUE IN (CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 51: `33e8bab58cbd2532` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010037`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(NULL, '$[#-1]') WHERE FALSE GROUP BY FALSE HAVING CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY 
```

---

## Crash 52: `860a7d0adabb97ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010045`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP AND CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 53: `4de9ebdc00eb7d9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010051`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 54: `263481603c366264` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010065`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (TRUE MATCH CURRENT_DATE > CURRENT_TIME - TRUE)); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 55: `174274276fc9abc5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010074`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 56: `e28c1ae4901dbe37` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010084`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT TRUE, c1 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 57: `5966fc3b2cfe2932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010091`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 58: `b5d1c7ff1fbe8e2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010102`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 59: `c40e3238d532e06c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010113`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (-CURRENT_DATE << CURRENT_DATE < NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 60: `5536f867627ebaf2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010130`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIME) INTERSECT SELECT ALL TRUE FROM json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 61: `10868441c9b214b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010140`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP IS NULL > CURRENT_TIMESTAMP AND CURRENT_DATE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 62: `c3d3f5e21d5c66d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010146`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_DATE OR CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 63: `8d7987114e7a2002` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010227`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES ('M-8 N _D0RH E_-8' COLLATE RTRIM) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 64: `2df9b4d4e87586a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010259`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAM
```

---

## Crash 65: `8a0c6cdde0c64230` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010340`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_DATE COLLATE RTRIM) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 66: `f7849d4bcdf019ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010394`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (NULL / CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 67: `8c4116280cd0c384` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010409`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP GLOB count(*)) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 68: `5f20c57ab5849bc3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010426`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP GLOB NULL) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 69: `3d3e37f21baa5552` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010454`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (FALSE << CURRENT_DATE < NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 70: `c4c5203bdfd44286` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010461`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (-CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 71: `3e58077052de841d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010470`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (-CURRENT_DATE << NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 72: `81b1ae87919e2316` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010485`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (NULL << NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 73: `75fdb06476f4a974` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010523`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (FALSE << CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 74: `f298b1d0cd58495a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010670`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (rank() OVER (), CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTE
```

---

## Crash 75: `2e23a2a4a8518d7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010749`

```sql
SELECT substr('', 4294967296, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 76: `0a37323037a8c0cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011100`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (FALSE) UNION VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 77: `c31f8f7b8ea9c60a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011396`

```sql
SELECT substr(' K-_-', 4294967295, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 78: `5f2c7ee1f1653f35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011406`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 79: `a946184918bf0b33` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011416`

```sql
SELECT printf('%.*s', -1, 0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 80: `739ec96142d9b15f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011453`

```sql
SELECT printf('%.*g', 4294967296, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 81: `4d847015f6057bab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011471`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 82: `8621edc1e8d0deb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011480`

```sql
SELECT substr('R__u 0  _3_- - R-xL', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 83: `4e0377b06582136f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011488`

```sql
SELECT printf('%lld', -2147483649, '86_07VH_C_---5Ue'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),
```

---

## Crash 84: `22313901a4e8e978` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011506`

```sql
SELECT printf('%.*d', -2147483648, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 85: `4bd9a788d392dcd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011521`

```sql
SELECT printf('%lld', -9223372036854775808, '1x - o64I__r- '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALU
```

---

## Crash 86: `b7825d45ea5d6554` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011553`

```sql
SELECT printf('%.*s', 9223372036854775807, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 87: `9ef034d3c4b5f630` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015357`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 INDEXED BY c1 LIMIT FALSE; WITH RECURSIVE p AS (VALUES (CAST(TRUE AS TEXT))) SELECT CURRENT_TIMESTAMP IS
```

---

## Crash 88: `6ba3930eed180b19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015392`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 INDEXED BY c1 LIMIT FALSE; WITH RECURSIVE p (a) AS (VALUES (FALSE)) SELECT TRUE LIKE TRUE ESCAPE TRUE AS
```

---

## Crash 89: `7958aee3d55171a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015405`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 INDEXED BY c1 LIMIT FALSE; SELECT DISTINCT * FROM json_tree('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 90: `c036b4592f4431ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015416`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 INDEXED BY c1 LIMIT FALSE; SELECT CURRENT_TIMESTAMP GLOB count(*) FROM p WHERE EXISTS (VALUES (FALSE)); 
```

---

## Crash 91: `54ba404c38b83b0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015422`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 INDEXED BY c1 LIMIT FALSE; SELECT * FROM json_tree('[1,2,3]') WHERE FALSE ORDER BY TRUE DESC NULLS LAST 
```

---

## Crash 92: `0c5beb6bc6c54ac5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015488`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 93: `8e7c9fce8c4912a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015597`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE IN (CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 94: `0a1488e27116d01e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015603`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE IN (CURRENT_TIME, rank() OVER (), CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 95: `96d32489566d8239` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017394`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION VALUES (NULL IS NOT NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 96: `ef907ed01bdd57ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017423`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE t1 AS (VALUES (CURRENT_TIME)) SELECT NULL IN (VALUES (TRUE)) AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FROM p; CREATE TABLE seed_t1(
```

---

## Crash 97: `c2ae2fc3f8380d53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019705`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 98: `4dc02aaf4552ecaa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019716`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 99: `947cf5b98cd335a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019738`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 100: `4cc4c174af4b76f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020083`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 101: `401962c40bd35d72` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020091`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 102: `465875bb4c7f6343` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020784`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT CURRENT_TIME AND TRUE AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 103: `63ee40f27be53936` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021204`

```sql
SELECT printf('%.*g', 2147483648, 1e308); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = l
```

---

## Crash 104: `35c8d313b375e445` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022032`

```sql
SELECT printf('%.*e', 9223372036854775807, 1e-308); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER
```

---

## Crash 105: `6afcefd5697065d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB CHECK (CURRENT_DATE)); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c
```

---

## Crash 106: `6068a04a34b890cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022178`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE, c1 GENERATED ALWAYS AS (a) , a NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 107: `564413a84d8abc68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022219`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT CURRENT_TIMESTAMP GLOB FALSE > CURRENT_TIMESTAMP NOT NULL AND CURRENT_DATE AS a FROM p; CREATE TABLE
```

---

## Crash 108: `1a5009025c849f43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022233`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT *, * FROM json_tree('[1,2,3]') WHERE FALSE ORDER BY TRUE DESC NULLS LAST LIMIT FALSE) SELECT * FROM r; CREATE TAB
```

---

## Crash 109: `7c6e209f85026dbe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022305`

```sql
SELECT substr('', 9223372036854775807, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 110: `3539e40d48e69f48` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022727`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL AND CURRENT_DATE || NULL != FAL
```

---

## Crash 111: `6e30f24b9334311e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022735`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 112: `589fd9b6e49c67fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022756`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL AND TRUE BETWEEN CURRENT_TIMEST
```

---

## Crash 113: `070eed3957f5141f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022782`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT FALSE | CURRENT_TIME GLOB count(*) FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 114: `6dcee61b966e7ed7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022804`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{"a":{"b":
```

---

## Crash 115: `1d73e9aea0cc15a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022830`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT * F
```

---

## Crash 116: `95abfaffe9ed5627` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022951`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (count(DISTINCT FALSE) FILTER (WHERE 
```

---

## Crash 117: `c14df422cc5037dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023537`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 118: `025e602c589f11f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023701`

```sql
SELECT substr('a', -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3
```

---

## Crash 119: `f526e05f76e828d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023722`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT DEFAULT 0.0); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 120: `0a4ee788659c83cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023729`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT count(*) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UNBOUNDED
```

---

## Crash 121: `c858178ce7609429` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023776`

```sql
SELECT printf('%.*d', 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 122: `aa9ef9c55055065f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023940`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); VALUES (FALSE) INTERSECT VALUES (row_number() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 123: `6af58ab24f5185d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023967`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); VALUES (FALSE) INTERSECT VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 124: `abf2a18ed7f13854` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026473`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (~CURRENT_DATE)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 125: `0d5a53bc2cfef155` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026482`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (CASE TRUE WHEN NULL THEN CURRENT_TIME END)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 126: `baae1a19edaa8440` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026580`

```sql
SELECT substr('Fge0V_563B-5l Gl', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44)
```

---

## Crash 127: `6463fc3d5ea7214b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029295`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 128: `69ba5a253fcf3d77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030185`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAY
```

---

## Crash 129: `7955685ee737a8a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031222`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)) SELECT count(DISTINCT FALSE) FILTER (WHERE CURRENT_TIME) AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FRO
```

---

## Crash 130: `24a1b5c46c4f395d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031433`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)) SELECT count(*) FILTER (WHERE CURRENT_TIME) AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FROM p; CREATE T
```

---

## Crash 131: `091713c74a01c3dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033599`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 132: `c1a79067133dc5cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033644`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 133: `c6fe24ef4d3b311e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033948`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME COLLATE NOCASE << CURRENT_TIME IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 134: `b683747664eccbe2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033963`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS NOT NULL IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 135: `f015505e0da7b775` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033976`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (SELECT TRUE FROM json_tree('[1,2,3]') WHERE FALSE)); PRAGMA quick_check; CREATE TABLE see
```

---

## Crash 136: `ce2a3bb7ba079956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034021`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY, c2 INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 137: `0ab252edcbd874ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034029`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT 3106.83E+480666568217765433463465093746832165709387783223867236870280110660544357); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(
```

---

## Crash 138: `68f8d14466c2709b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034036`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_DATE || CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 139: `55ed9259ed036ce8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034045`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT 0.0); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 140: `d86a34452e1b017d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034057`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 141: `42a0540a6bf72cc9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034103`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'Bf2A6063cA', c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 142: `a680155f55d2db57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034172`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DE
```

---

## Crash 143: `b11bfabf3ddb5af3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034182`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE)); INSERT INTO p DE
```

---

## Crash 144: `6266fb990a8ebdab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034188`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE 
```

---

## Crash 145: `1d441d997cefc7c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034410`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE 
```

---

## Crash 146: `79c2f2497571a846` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034808`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE 
```

---

## Crash 147: `d1552bcc7b14a236` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035421`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (NULL AND CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 148: `f6355a2947353f0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035466`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); INSERT OR IGNORE INTO p VALUES (
```

---

## Crash 149: `12c3e74e1c7dfdb5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035495`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT X'1dddAf4b1D'); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 150: `f32febdd5ce2acbd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035509`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS TRUE LIKE CURRENT_TIMESTAMP NOT NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 151: `1f263641e98b6459` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035600`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT 17836.7418440805163073840785328892050875302e+015593556708170); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 152: `5561e5cd049b843f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035645`

```sql
SELECT substr('', -9223372036854775808, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 153: `bf7602e8ae78ff26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035663`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 154: `f37ef614986f63e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035706`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (a LIKE CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 155: `ff776b1110bca617` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035743`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME COLLATE RTRIM)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 156: `d37013ae6a8e5242` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035777`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_DATE OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 157: `c30e0bb5a725c0bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036257`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME)); INSERT OR IGNORE INTO p VALUES (NOT TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 158: `fd42f97856c9a224` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036267`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME)); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (CAST(count(*) FILTER (WHERE TRUE BETWEEN CURRENT_DATE A
```

---

## Crash 159: `49235eedc9b55202` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036278`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 160: `2f83b98ec1873fc4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036292`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME)); INSERT OR REPLACE INTO p VALUES (TRUE >> TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 161: `9c8e54778e17ea00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036301`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT -6); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 162: `65ee51420a91aa7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036327`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * LIMIT CURRENT_TIMESTAMP, count(*) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURREN
```

---

## Crash 163: `0abb6aa6d6be5f70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036350`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (CURRENT_TIMESTAMP - FALSE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 164: `6e651a494c21acea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036363`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (NOT FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 165: `954c47a389624d67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036415`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT -37281380172456158197977207163438902638217648676028466.1960706248785232751775686927244, _rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL, 
```

---

## Crash 166: `6a0f11675accc6b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036422`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 167: `ba36c7706438a457` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036465`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (CAST(count(*) FILTER (WHERE TRUE BETWEEN CURRENT_DATE AND 
```

---

## Crash 168: `12caf6457cdd9cd3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036474`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (VALUES (FALSE))); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 169: `c64655bf9c94e635` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036526`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME, dense_rank() FILTER (WHERE CURRENT_DATE) OVER (ORDER BY TRUE ASC NULLS LAST ROWS BETWEEN C
```

---

## Crash 170: `4a54f74fd5d45e25` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036532`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME % -FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 171: `28d3d5f157fa35be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036564`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT 'l-_ '); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 172: `ab7deb9bd272fd75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036582`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT NOT NULL AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 173: `a01c4ad72362e4e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036649`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b GENERATED ALWAYS AS (a + 0) UNIQUE, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 174: `28eaeb70208e9982` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036697`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME % CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 175: `84edb6a843b5e12d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036733`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (NOT FALSE > CURRENT_TIME IS CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 176: `1f3b5bfa5c0518a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036740`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT X'87BAB2AEAeCc', c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 177: `0ecaae471ca8b337` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036752`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (NOT FALSE > CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 178: `2927bac47316c64d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036782`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS FALSE IS NOT FALSE NOTNULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 179: `8806f61f7d9543cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036853`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT -0); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 180: `7e442a2e1ea5e857` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036906`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_DATE / FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 181: `8c7545b632559c4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036935`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (CURRENT_DATE > CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 182: `319db85a9e3a4068` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036942`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (NOT X'')); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 183: `42c972e696aa2155` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036977`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (NULL)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 184: `ac38ae38359879d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036989`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); SELECT count(TRUE) FILTER (WHERE CURRENT_TIME) OVER () AS l0d___sd_y__5__pv_ FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE TABLE seed_t1(c1
```

---

## Crash 185: `6d66ae799635b510` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037016`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT NULL > CURRENT_TIMESTAMP AND CURRENT_DATE AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 186: `e655895b0dd4d3d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037061`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT ' '); CREATE TABLE IF NOT EXISTS q(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 187: `40626b26ed4d3dbf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037138`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK ('M-8 N _D0RH E_-8' IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 188: `c5ec416783953c40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037151`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS NULL IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 189: `599f5820059a7874` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037166`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (~CURRENT_DATE - TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 190: `d76a9ebbc864656a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037291`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME 
```

---

## Crash 191: `c36cf31da6b74c5a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037340`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check
```

---

## Crash 192: `a758eeb15e6c48af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037347`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAUL
```

---

## Crash 193: `9db2ec8e2a4c8a4c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037413`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 194: `2d597cb104898242` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037423`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 195: `87d7b1136c78ed0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037520`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (group_concat(TRUE) FILTER (WHERE TRUE BETWEEN CURRENT_DATE AND NULL)
```

---

## Crash 196: `5b0fb114b720347e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037527`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 197: `5a7c259db2ae6536` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037561`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (group_concat(TRUE) FILTER (WHERE CURRENT_TIME)))); PRAGMA integrity_
```

---

## Crash 198: `1a354a021159d471` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037575`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (TRUE BETWEEN CURRENT_DATE AND NULL))); PRAGMA integrity_check; CREAT
```

---

## Crash 199: `2f9ce12d1a100f70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037581`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (group_concat(TRUE) FILTER (WHERE TRUE)))); PRAGMA integrity_check; C
```

---

## Crash 200: `4a696daaa71f5bef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038492`

```sql
SELECT printf('%.*s', 4294967296, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 201: `4fd8cb6cea71b11b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038499`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT X'87BAB2AEAeCc', c3 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 202: `882a04e7b7b796eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038515`

```sql
SELECT printf('%x', 4294967295, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE 
```

---

## Crash 203: `d5c8b1212308d0e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038522`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (a) AS (VALUES (FALSE)) SELECT NULL IN (VALUES (CURRENT_TIME << CURRENT_TIME)) AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FROM p; C
```

---

## Crash 204: `32b590506c3debed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038594`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 205: `b86e460dca2399f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040359`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT 3106.83E+480666568217765433463465093746832165709387783223867236870280110660544357); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 206: `f07c4055766d8f24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 207: `167ecc7c9ae0b00d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040398`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') INTERSECT SELECT ALL * FROM json_tree('{"a":{"b":1}}')) SELECT * FROM p;
```

---

## Crash 208: `3f187e3ab86ab579` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040417`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (NULL)) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 209: `2b32a6c34e0c3f5d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040425`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME % -FALSE)); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 210: `84b6b5ab65b199c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040447`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY, c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 211: `33fb008f3925d77b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040469`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT -90.99); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 212: `5f49f78ea830a9c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041301`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGER,
```

---

## Crash 213: `940af6f0de8b8446` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041439`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 214: `949a5b7391a330c5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041453`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 215: `af358ba8e445e9dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042221`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NU
```

---

## Crash 216: `4e4eeea1ce7f6044` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044856`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP + FALSE)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 217: `e6115c1cf152d932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044973`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 218: `cf3d6f889f938298` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045014`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (CURRENT_TIMESTAMP NOTNULL)); INSERT OR REPLACE INTO p VALUES (~CURRENT_DATE * CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 219: `c4299525e56e26c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045023`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT NOT X'' AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 220: `d4df71ab1c5f6c66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045079`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT NOT CURRENT_DATE AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 221: `5fbf034062f77736` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045092`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL DEFAULT X'5FA1E2BF'); INSERT OR REPLACE INTO p VALUES (~CURRENT_DATE * CURRENT_TIMESTAMP); PRAGMA integrity_check
```

---

## Crash 222: `ae5479f59dcfa72b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046595`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT X'7f506feD'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 223: `5a305c0aca57abfb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046615`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT ''); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 224: `b69ebbc2e3ca296c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE p AS (WITH q AS (VALUES (CURRENT_TIME)) SELECT * FROM q JOIN json_tr
```

---

## Crash 225: `fd82e7dde04ca2eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047185`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p AS (WITH q AS (VALUES (CURRENT_TIME)) SELECT * FROM q JOIN json_each(NULL, '$[#-1]')) SELECT CURRENT_TIMESTAMP GLOB FALSE AS a FR
```

---

## Crash 226: `a8170966fc133039` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047341`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (RAISE(IGNORE)), b DATE CHECK (CURRENT_TIMESTAMP), _rowid_ BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM json_
```

---

## Crash 227: `2430853bae03ced9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047654`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT NULL FROM json_each('{"a":{"b"
```

---

## Crash 228: `9e1aa191d9e563b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047667`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (cume_dist() FILTER (WHERE CURRENT_DATE), TRUE); INSERT
```

---

## Crash 229: `c5f69562872c7775` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047678`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT +CURRENT_DATE GLOB CURRENT_DATE & NULL AS a, NULL COLLATE BINARY << -CURRENT_DATE << CURR
```

---

## Crash 230: `85db0f7381c820ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047726`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT q.*, +CURRENT_DATE GLOB CURRENT_DATE & NULL AS a, NULL COLLATE BINARY << -CURRENT_DATE <<
```

---

## Crash 231: `7dbcabc333d304b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047738`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q JOIN json_tree('[1,2,3]'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALU
```

---

## Crash 232: `7a95848974a5bfcf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047794`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 233: `f8616ac45c27615c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047803`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.* FROM q NOT INDEXED LEFT OUTER JOIN jsonb_tree('{}'); INSERT INTO p DEFAULT VALUES; EX
```

---

## Crash 234: `b74fb01b0fe54751` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047822`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CASE CURRENT_TIMESTAMP WHEN TRUE THEN -CURRENT_DATE COLLATE BINARY ELSE count(*) END GLOB
```

---

## Crash 235: `625cdd62534a78dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047882`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES
```

---

## Crash 236: `2e94fcc0dfa00638` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047892`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT D
```

---

## Crash 237: `dbf755d7b97d620a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047898`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIME)), r AS (SELECT *) SELEC
```

---

## Crash 238: `165df22546bcec98` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047904`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[1,2,3]') WHERE FALSE ORDER BY CURRENT_TIM
```

---

## Crash 239: `d6b8da5e938a069d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047929`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 240: `85daee7ae35bf8c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047948`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES
```

---

## Crash 241: `bfbe0116c52172e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047958`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 242: `87543182f224d916` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047977`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES
```

---

## Crash 243: `66c886ff5307f160` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048001`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT count(TRUE) FILTER (
```

---

## Crash 244: `839f197efcf506a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048144`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE ORDER BY TRUE DESC NULLS LAST LIMIT FALSE; EXPLAIN QUER
```

---

## Crash 245: `863811fa10f39934` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048150`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE ORDER BY TRUE DESC
```

---

## Crash 246: `4f5dadd8d2755791` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048249`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN DEFAULT '-2', _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 247: `d682bb87aacb87ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049971`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT 3084650650682473601.6486175088010642e+35); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA
```

---

## Crash 248: `44fd0e2ad4497830` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050554`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP <> CURRENT_TIMESTAMP COLLATE NOCASE)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 249: `5dc34d60f9c9b5a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050581`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (CURRENT_DATE > CAST(CURRENT_TIMESTAMP AS FLOAT))); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 250: `5417302c70a0144d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050620`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 251: `5c90ed5e1a132b4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIME)), t2 AS (VALUES (TRUE)) SELECT *; VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAM
```

---

## Crash 252: `1c037eae4c5c911a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050729`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (NULL AND TRUE BETWEEN NULL AND NOT TRUE) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 253: `cd605a97feaa8074` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050736`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIME) INTERSECT SELECT ALL TRUE FROM json_tree('{"a":{"b":1}}') INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 254: `f10a3cc2b7cf0147` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053320`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 255: `dafce901b230eafd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053352`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 256: `14ff152e66fdc443` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053420`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL DEFAULT 0); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA int
```

---

## Crash 257: `4c4661d3ac56d0e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054748`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM jsonb_each('[]') LEFT OUTER JOIN json_tree('{}') ON TRUE UNION SELECT DISTINCT * FROM json_each('{}') NATURA
```

---

## Crash 258: `fc3a68bb6ff44b5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055262`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING 
```

---

## Crash 259: `c112fc5858bf10e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055268`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (FALSE < CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 260: `bd9ac01bae05baab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055290`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH q AS (VALUES (CURRENT_TIME)) SELECT * FROM q LEFT OUTER JOIN json_each(NULL, '$[#-1]'); CREATE TAB
```

---

## Crash 261: `0b8389add39152ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055298`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); SELECT * FROM json_each(NULL, '$[#-1]') WHERE FALSE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURR
```

---

## Crash 262: `f541f0ba75b0f07d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055312`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT * FROM json_tree('[1,2,3]') WHERE FALSE ORDER BY TRUE DESC NULLS LAST LIMIT
```

---

## Crash 263: `cf8ef51b2ffdb79e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057040`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (NULL) INTERSECT VALUES (count(*) FILTER (WHERE FALSE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 264: `322c4bbe98097cf1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057192`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT ALL * FROM json_tree('{}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 265: `5b2c7fb560aea931` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057345`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS 
```

---

## Crash 266: `2078a34e2a80b590` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057501`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT X'' GLOB FALSE AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 267: `ec9849588a161976` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057507`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT * FROM json_tree('[1,2,3]') WHERE FALSE ORDER BY TRUE COLLATE RTRIM ASC NULLS LAST LIMIT FALSE) SELECT * FROM r; 
```

---

## Crash 268: `1ad301f5b9ce539d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058662`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE AND TRUE BETWEEN TRUE AND NOT TRUE ORDER BY TRUE DESC N
```

---

## Crash 269: `eeede62fb4d3ac35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058689`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE >> TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t
```

---

## Crash 270: `862ebc9fcff6899c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM p LEFT JOIN (VALUES (TRUE)) AS zu____t_k___w7zdv__q00_w__85ou6_79_of_8___pw08_a8__o7053__3z8u__8_hvq8
```

---

## Crash 271: `6629285c9e6e591c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058709`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 272: `50d0963b744a34ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058901`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) STORED, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT +CURRENT_DATE GLOB CURRENT_DATE & NU
```

---

## Crash 273: `2fa43f7c33b6f61f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058934`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT -6, _rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE ORDER BY TRUE DESC NULLS LAST L
```

---

## Crash 274: `2bb276e585061d5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058978`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT X'3257ecA412fb'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE ORDER BY TRUE DESC NULLS LAST LIMIT FALSE;
```

---

## Crash 275: `2f2b25d9a0d400ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('[1,2,3]') LEFT OUTER JOIN p
```

---

## Crash 276: `a6e7b113ad4c88a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059598`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p LEFT JOIN (VALUES (TRUE)) AS zu_
```

---

## Crash 277: `522abd6812da75db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059614`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[]') LEFT OUTER JOIN json_each('[]') USING (c3) WHERE FALSE; INSERT INTO p DEFAULT VA
```

---

## Crash 278: `03439d043a65dad1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059626`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (CURRENT_TIME) INTERSECT SELECT ALL TRUE FROM json_tree('{"a":{"b":1}}'); PRAGM
```

---

## Crash 279: `dbfbee43857f72ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059637`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('[1,2,3]') INNER JOIN json_tree('[{"a":1},{"b":2}]') USING (b, a); INSERT INTO
```

---

## Crash 280: `a01e610fce60e897` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059650`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT -439584582061602.4E3963); CREATE TABLE IF NOT EXISTS q(rowid INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES
```

---

## Crash 281: `57de6513ec29bd73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059663`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES (NULL)) SELECT dense_rank() OVER () AS a FR
```

---

## Crash 282: `d6a583e5285a6e19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059768`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '-Ix4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 283: `5d85a9df1074b0d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059790`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p LEFT JOIN json_each('[1,2,3]') NATURAL
```

---

## Crash 284: `bcc4019976f8e074` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063805`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q LEFT OUTER JOIN p NOT INDEXED; CREATE TABLE IF NOT
```

---

## Crash 285: `a01479f33f48fb2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063857`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NU
```

---

## Crash 286: `9b8c787daabef255` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063867`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, r.* ORDER BY CURRENT_DATE ASC NULLS LAST LIMIT CURRENT_TIME COLLATE NOCASE << CURRENT_TIME NOT LIKE TRUE
```

---

## Crash 287: `7f15e6d5e65a50c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063942`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIME NOT LIKE dense_rank() COLLATE NOCASE != ~(last_insert_rowid()) NOTNULL IS NULL = TRUE IS NOT +
```

---

## Crash 288: `9b0062a38188629e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063982`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); 
```

---

## Crash 289: `a1f338b54dcddd03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064424`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'35Aa8Eb0f2CD85'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGE
```

---

## Crash 290: `a23bde24b050feef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064831`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNI
```

---

## Crash 291: `0c6596dea1f68665` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065225`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(25
```

---

## Crash 292: `866b323484e68e96` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065424`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a IN
```

---

## Crash 293: `398dcd66bdfc7977` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066338`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a VA
```

---

## Crash 294: `896050a261ea89fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066364`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (total_changes() OVER (PARTITION BY RAISE(IGNORE) ORDER BY RAISE(IGNORE) DESC NULLS FIRST ROWS BETWEEN UNBOU
```

---

## Crash 295: `f73279c2c59fb9e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066370`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (last_insert_rowid() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_TIME DESC RANGE BETWEEN UNBOUNDED PRECEDING 
```

---

## Crash 296: `347e88c9167f6546` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066395`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BO
```

---

## Crash 297: `bd1809204be53bf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066415`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a FL
```

---

## Crash 298: `f49e509d6af5a96c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066483`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT FALSE NOT BETWEEN CURRENT_DATE LIKE FALSE AND CURRENT_TIME / RAISE(IGNORE) LIKE ~(FALSE) / +CURRENT_TIMESTAM
```

---

## Crash 299: `4d88cd9f0c4d93c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067291`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE, c1 GENERATED ALWAYS AS (a) , a NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t0 (c0 INTEG
```

---

## Crash 300: `268a2525b77d367f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067678`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE CHECK (TRUE MATCH CURRENT_DATE > CURRENT_TIME - CURRENT_TIME % -FALSE)); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS CURRENT_TIMESTAMP; CREATE TABLE seed_t1(
```

---

## Crash 301: `43537559b907aa58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067685`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS CURRENT_TIMESTAMP; CREATE 
```

---

## Crash 302: `3dddba2bb504c7b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067723`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (max(CURRENT_DATE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 303: `dca53ef45e3f343a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067730`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT 'e _---EAli   b2 '); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 304: `44ec41c807f6c1f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067754`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 GENERATED ALWAYS AS (a * a) NOT NULL, c2 DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 305: `961576041b7a4b89` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067943`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT 3106.83E+480666568217765433463465093746832165709387783223867236870280110660544357); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p
```

---

## Crash 306: `c2703a88c9e3e452` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068105`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTE
```

---

## Crash 307: `a509d34b6fa6b1a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068112`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IS TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 308: `f2c6e37d00d05d66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070989`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (a) AS (VALUES (FALSE)) SELECT NULL LIKE TRUE ESCAPE NULL AS s4f__b12r1__c5_2__s2_7s826v74pb896__8 FROM p; CREATE TABLE seed_t1(c
```

---

## Crash 309: `13750001cf027530` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071785`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (group_concat(TRUE) FILTER (WHERE CUR
```

---

## Crash 310: `a4ea7cca86d5a567` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071822`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME IS X''))); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 311: `0e65e014c3fafa0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071834`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (RAISE(IGNORE) NOT IN (FALSE) % CAST(TRUE AS TEXT), rank() OVER (), CURRENT_TIME)) VALUES (g
```

---

## Crash 312: `1f3d600fc22f4509` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071861`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ROLLBACK INTO p VALUES (EXISTS (VALUES (CURRENT_DATE))); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 313: `249c83a33dbd7ff8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071972`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 314: `8620f476f089059d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071985`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 315: `8232bf7f57e568e4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072013`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (RAISE(IGNORE)) INTERSECT SELECT * FROM json_each('{"a":{"b":1}}') , (json_each('{"a":1}') N
```

---

## Crash 316: `bba52903d9ab55a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072037`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR REPLACE INTO p VALUES (TRUE >> FALSE - CURRENT_TIME - CURRENT_TIME - CURRENT_TIME - CURRENT_TIME - CURRENT_TIME); PRAGMA integrity_check; CREATE
```

---

## Crash 317: `ab611b2594b7351a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072078`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE p AS (VALUES (NULL)) SELECT TRUE = CAST(CURRENT_TIMESTAMP AS FLOAT) AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 318: `368c73c41c273c82` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072188`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE NOT IN (WITH q AS (VALUES (CURRENT_TIME)) VALUES (group_concat(TRUE) FILTER (WHERE NULL))) NOT IN (WITH q AS (VALUES (
```

---

## Crash 319: `7b9159945d47b36c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072224`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CAST(TRUE AS TEXT) IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 320: `a26126b23b6bcecb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072244`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE IS NOT FALSE NOTNULL IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 321: `5906aa452d10507a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072252`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS +CURRENT_DATE = CURRENT_DATE COLLATE NOCASE COLLATE NOCASE COLLATE NOCASE IS CURRENT_TIMESTAMP < FALSE)); INSERT INTO p DEFAU
```

---

## Crash 322: `6520af81ef278b09` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN DEFAULT '   U RsB_AmW o-v'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 323: `b45248c52845ff72` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072281`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS NULL LIKE TRUE ESCAPE NULL IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 324: `13d1095c2256b47c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072291`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS TRUE IS NOT NULL & TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE
```

---

## Crash 325: `fd65b5f22e3cfd32` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072318`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 BOOLEAN DEFAULT NULL, c2 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE see
```

---

## Crash 326: `5b839ac8efb62cfa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072424`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE I
```

---

## Crash 327: `0cd6f7242ab682eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072440`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURR
```

---

## Crash 328: `b83cbec342d92c62` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072497`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (TRUE IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS FALSE IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME
```

---
