# Crash Triage Report

**Total crashes:** 376  
**Unique crash sites:** 376  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 186 | 186 | 49% |
| Signal | 190 | 190 | 50% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `88570f42128c3bdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000036`

```sql
SELECT substr('_eN9', -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 2: `de3f2f81ad825d2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000163`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 3: `7a646b61e036efe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000289`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO s VALUES (CURRENT_TIMESTAMP IS CURRENT_TIME != NOT TRUE IS NOT DISTINCT FROM TRUE <= RAISE(IGNORE) NOTNULL, CAST(NULL C
```

---

## Crash 4: `0eb7e3fbce661c8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000575`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c2); INSERT INTO q VALUES (NOT EXISTS (SELECT *, FALSE UNION SELECT DISTINCT * FROM json_each(FALSE IS NOT NULL, '$.key') ORDER BY FALS
```

---

## Crash 5: `cf2b0be0fb74f45c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000764`

```sql
SELECT printf('%.*f', -2147483649, 1e308); CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL, c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, * FROM jsonb_each('{"a":{"b":1}}') INNER JOIN js
```

---

## Crash 6: `d43a0357c7113863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000830`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE, _rowid_ BOOLEAN DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.* FROM jsonb_each('[{"a":1},{"b
```

---

## Crash 7: `a86ab5907929d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002204`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 8: `9c279412fc7324ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002589`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 9: `2be0cc15ff0722e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 10: `bf2ab3f1af19ed2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002620`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 11: `7ded342b3c74cc1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO s
```

---

## Crash 12: `f8885453cd11d115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003198`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SEL
```

---

## Crash 13: `f295b887e4efdb21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004879`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (SELECT DISTINCT * FROM q NATURAL LEFT JOIN jsonb_tree('{}') USING (c1, b) LIMIT NULL) SELECT *; VA
```

---

## Crash 14: `00f6cfc0a6cc5c63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004885`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q NATURAL LEFT JOIN jsonb_tree('{}') USING (c1, b) LIMIT NULL; VALUES (FALSE); CREATE TABLE seed
```

---

## Crash 15: `0591e22c4c6375b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004993`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 16: `e1bc95712e0ad7d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005158`

```sql
SELECT printf('%f', -9223372036854775808, ' __-_-c-_6n-1--'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SEL
```

---

## Crash 17: `8b67ad677b46520d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005186`

```sql
SELECT printf('%llu', 2147483647, '-20 _--BG--5_ oGfH'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT c
```

---

## Crash 18: `ab6e0105040d6867` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005270`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIME; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 19: `45e946ff2331b4ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005430`

```sql
SELECT substr('341-__Z ', -2147483648, -9223372036854775808); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; C
```

---

## Crash 20: `c9ea668cc58df4cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005451`

```sql
SELECT substr('341-__Z ', -2147483648, -9223372036854775808); CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE, c3 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(a TEXT GENERATED ALW
```

---

## Crash 21: `008dce5d7acf4b7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005503`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_DATE COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 22: `f961330d3bc1389a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 23: `f588e31497415aa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005530`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 24: `6fe6f093ab4872f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005541`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 25: `bfaf6c0461627db2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005583`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 26: `cf90ed5e08ebf1dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005689`

```sql
SELECT round(1.0, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 27: `fbf9f8299d8770de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005817`

```sql
SELECT printf('%.*g', 1, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 28: `400b3ffed052f693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006020`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 29: `536be8633414465b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007152`

```sql
SELECT substr('', 2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); INSERT OR FAIL INTO t3 VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP COLLATE NOCASE N
```

---

## Crash 30: `939391a4817c9864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010952`

```sql
SELECT printf('%.*d', -2147483649); SELECT substr('6_pj -75 ', 4294967296, -9223372036854775808); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 31: `ef1f78acf09fa280` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011518`

```sql
SELECT round(-1e308, 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 32: `99af64e43e668be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012844`

```sql
SELECT printf('%.*g', 1, 0.0); CREATE TABLE IF NOT EXISTS p(a REAL, c3 GENERATED ALWAYS AS (a = 0) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 33: `f1ccc8abe343864b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012942`

```sql
SELECT printf('%.*g', 1, 0.0); SELECT printf('%.*e', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT
```

---

## Crash 34: `52997ac05d201c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013750`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE BETWEEN CURRENT_TIME AND FALSE, * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY CURRENT
```

---

## Crash 35: `3b7374c82736460b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013762`

```sql
SELECT round(-1.0, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 36: `2474f1d93b7f3a34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013770`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL < TRUE COLLATE NOCASE IS NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a
```

---

## Crash 37: `353982b153fdfc98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013776`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY, c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 38: `03bbd69c67228cd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013895`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 39: `d88c37bfbe805b20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016256`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT -4065853369677773952647658212806698739660053625860849571600634502789589769050792344017169700449395906603513931528399435188223042537647429627021
```

---

## Crash 40: `dadea772815c54de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016309`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT -608189, c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UN
```

---

## Crash 41: `027bea1fb7fd88dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016317`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r INDEXED BY c3 EXCEPT SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(
```

---

## Crash 42: `681ac17e9f7979b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016363`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c2 INTEGER UNIQUE, c1 DATE GENERATED ALWAYS AS (NULL <= FALSE) VIRTUAL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 43: `fe6897b2887af0f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016384`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NOT TRUE OR CURRENT_TIME COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE se
```

---

## Crash 44: `497ed36de4dcdaf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016414`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (FALSE NOT LIKE NULL >= TRUE IS NULL COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREA
```

---

## Crash 45: `d1a2757096d5a11d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016445`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X''); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 46: `a1c86cc2d1e738bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016463`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 47: `0dfef088b1fb8dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016478`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT 'S u_A5---4 4_T 6  '); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 48: `471e6122ca8a1453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016552`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= NULL IS NULL COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE
```

---

## Crash 49: `5b106c49e073e313` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016563`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL IS N
```

---

## Crash 50: `5c232fa2ec35772f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016605`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); C
```

---

## Crash 51: `421400c3ff38918e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016638`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); CREATE TABLE IF NOT EX
```

---

## Crash 52: `cb8ffef7a10b6424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016672`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT N
```

---

## Crash 53: `dc8e177740c79731` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p D
```

---

## Crash 54: `c3edfa80630be2a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016790`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL IS NULL COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 55: `2f53ef4815207c20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016804`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL IS NULL >= TRUE COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a
```

---

## Crash 56: `80da023cd48b1633` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016850`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (FALSE NOT IN (CURRENT_TIMESTAMP))); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c
```

---

## Crash 57: `558d51b082b9a7dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (FALSE NOT IN (TRUE, CURRENT_TIMESTAMP))); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE se
```

---

## Crash 58: `d767469bd08108f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016887`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (~TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 59: `38daf49214cfbc24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016894`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (~NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 60: `385e9fb524929a5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016940`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 61: `0c397e1dac848d50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016966`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= FALSE LIKE NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed
```

---

## Crash 62: `3d10a7ff493f4646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016990`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL & CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 63: `2a30a1dd739e6c3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017006`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (FALSE | NULL), c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 64: `ba7ed5c1f54712d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017019`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p SELECT CURRENT_DATE AS s__7 FROM json_each('{"a":{"b":1}}') GROU
```

---

## Crash 65: `01f0ea56e2dd92f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017053`

```sql
SELECT substr(' 6', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 66: `b896aa19da035215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017126`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 67: `5c3822c79cc3aaa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017132`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p 
```

---

## Crash 68: `bd84a7c513e5556f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021401`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP LIKE CURRENT_DATE AS k_d__0__2ri_n__4jm5779__9_ik062_
```

---

## Crash 69: `c0538fa6d831c1b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021420`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c2 INTEGER UNIQUE, c1 DATE GENERATED ALWAYS AS (NULL <= FALSE) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT * FROM p NATURAL JOIN p WHER
```

---

## Crash 70: `9196c34266ae28e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021433`

```sql
SELECT printf('%.*d', -1, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 71: `75a3f50c86b07c8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022932`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[1,2,3]') WHERE X'2E3AAFD7' GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 72: `229e4f893157d076` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022984`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE
```

---

## Crash 73: `3342ea32240e62be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023010`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, c2 INTEGER UNIQUE, c1 DATE GENERATED ALWAYS AS (NULL <= FALSE) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; AN
```

---

## Crash 74: `ba85807b78b69151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023022`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT p.*, *, * FROM jsonb_tree('[1,2,3]') WHERE count(CURRENT_DATE GLOB CURRENT_DATE) OVER (PARTITION BY CURRE
```

---

## Crash 75: `d8f883f8e03976cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023063`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT (dense_rank() OVER (PARTITION BY RAISE(IGNORE))) < TRUE AS c__17h_80__3z5__5vq_z2f2__d89_lo_9_fq__e__q6_j_557b8__h
```

---

## Crash 76: `f5b2da8cc30fbede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023085`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT NOT EXISTS (VALUES (CURRENT_DATE IS NOT CURRENT_TIMESTAMP ISNULL) EXCEPT SELECT *, * FROM json_each(CURRENT_TIME, 
```

---

## Crash 77: `1f3967b96e6c87f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023113`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXIS
```

---

## Crash 78: `85cf524c9945dc48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023119`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXIS
```

---

## Crash 79: `cc8eb8e8a99edf4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023125`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXIS
```

---

## Crash 80: `ad277279b9a6b162` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXIS
```

---

## Crash 81: `6df68ee856b85ea2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED A
```

---

## Crash 82: `565d7fb261c354ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023664`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, c2 INTEGER UNIQUE, b INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UN
```

---

## Crash 83: `cb87a7eb95d289d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024181`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (FALSE IN (VALUES (CURRENT_TIME))); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 84: `055fe1cedbccc237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027874`

```sql
SELECT printf('%.*s', -1); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q NATURAL LEFT JOIN jsonb_tree('{}') USING (c1, b) LIMIT NULL; VALUES
```

---

## Crash 85: `f57dc486a5a595a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028433`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT count(*) FILTER (WHERE CURRENT_DATE), CURRENT_TIME IN 
```

---

## Crash 86: `2f1700e058200b38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028444`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p WHERE TRUE;
```

---

## Crash 87: `74d6fee028a46489` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028456`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT count(*) FILTER (WHERE CURRENT_DATE); CREATE TABLE see
```

---

## Crash 88: `333c911064f80e01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028477`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME); CR
```

---

## Crash 89: `3791fc32562e7e3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032152`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CAST(FALSE AS TEXT) | CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 90: `8c69659a0350cfe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032164`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH q AS (SELECT *) VALUES (TRUE) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = s
```

---

## Crash 91: `e9c193703bf9ee23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032208`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); SELECT CURRENT_DATE + TRUE AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 92: `bbaa614c1e3d311f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032235`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_DATE > NULL / CURRENT_TIME) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 93: `e769472d4e47e522` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033467`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); EXPLAIN QUERY PLAN WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)), t1 AS (VALUES (FALSE)) VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 94: `13d1c66786904f95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033487`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH q AS (SELECT *) VALUES (-CURRENT_TIME) INTERSECT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 95: `1a65fb2b49510871` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035827`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 96: `6311984c63eb71b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038938`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE || TRUE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 97: `b289800d328eeffe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038949`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); CREATE TABLE IF NOT EX
```

---

## Crash 98: `1c76cc5a234f781b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038971`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (NULL) INTERSECT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN see
```

---

## Crash 99: `0cb779dae72545cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039580`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT rank() OVER () FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 100: `daaaac79232e8871` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VAL
```

---

## Crash 101: `b4936c898e484b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039970`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (RAISE(IGNORE) MATCH TRUE), c2 TEXT); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE se
```

---

## Crash 102: `7e155f6a9eff2c1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039981`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_DATE < TRUE AND CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TA
```

---

## Crash 103: `82bd87e803a92e86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040004`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 104: `9563e4b4e943ef54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040012`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_DATE) INTERSECT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 105: `1525192326b9e818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040165`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT cume_dist() OVER (PARTITION BY RAISE(IGNORE) ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN CURRENT 
```

---

## Crash 106: `9c26a30b4728ed33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040184`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); INSERT INTO p SELECT DISTINCT coun
```

---

## Crash 107: `4ae11a36a7ca8914` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040192`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM p NATURAL JOIN json_each('{"a":1}') NATURAL JOIN json_each('[]'); CREATE TABLE IF NOT EX
```

---

## Crash 108: `b36cfe59c4b9a2c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040221`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); INSERT INTO p SELECT CURRENT_DATE 
```

---

## Crash 109: `3ba18658c5e5d5a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3, _rowid_); INSERT INTO p DEFAULT V
```

---

## Crash 110: `05e7a43dc44aea4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040329`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 111: `5d141209494c0100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040469`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME IN (CURRENT_TIMESTAMP)); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWA
```

---

## Crash 112: `ea7ba6d04a851a8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040476`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_DATE AS s__7 FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE; CREATE TABLE seed_t0 (c
```

---

## Crash 113: `cbafa3f415ab1bce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040493`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP GROUP BY RAISE(IGNORE) LIMIT FALSE, CURRENT_DAT
```

---

## Crash 114: `b41a4c2a33b63ef4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040504`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE + CURRENT_TIME IN (CURRENT_TIMESTAMP) COLLATE NOCASE); CREATE TABLE seed_t0 (c0 INTEG
```

---

## Crash 115: `64e37e76b566f22d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040564`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_DATE < TRUE), c2 TEXT); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN UNIQUE); VALUES (FALSE); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED 
```

---

## Crash 116: `ec969117f4386155` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040574`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY count(*); VALUES (FALSE); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT
```

---

## Crash 117: `eef667c2535a1299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040719`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 118: `9d7fcb5644894082` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041656`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN DEFAULT X'eB'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 119: `a86ba6dba7908086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041722`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 120: `d44d2e339da32eab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048069`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('{}') WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 121: `5db151face1fcc62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048076`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('{}') LEFT JOIN json_tree('[1,2,3]') ON NULL WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 122: `640b227a43095423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049177`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255)); INSERT INTO q VALUES (EXISTS (VALUES (FALSE))) ON CONFLICT DO NOTHING; VALUES (FALSE); CREATE TAB
```

---

## Crash 123: `ff364a8d13b68408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049532`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT DISTINCT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) FROM json_tree('[]') NATURAL LEFT JOIN json_each('{}') WHERE CURRENT_
```

---

## Crash 124: `55958d3ac1b69feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049552`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH q AS (SELECT *) SELECT CURRENT_DATE AS s__7 FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE INTERSECT VALUES (TRUE); CREATE T
```

---

## Crash 125: `0390ddaeaa061a77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049582`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP AS w_1y1s_5tu_phhwd94__g4__0a1cr_kiy8b0d9_z_f98__6n25__75__5u31ek0 FROM json_tree('[]') NATURAL LEFT J
```

---

## Crash 126: `bc29948bbba528d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049676`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TA
```

---

## Crash 127: `4d28ccdf451af49f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049694`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT DISTINCT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE INTERSECT VALU
```

---

## Crash 128: `29bcaba910a6b267` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052427`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (FALSE) STORED, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 129: `ff719ab230e246dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052481`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (FALSE) STORED, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 
```

---

## Crash 130: `35c7847a3ad98784` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052646`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (json_quote(TRUE)) STORED, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 131: `d233ca5869d9ecc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053594`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN se
```

---

## Crash 132: `ac820dc545ad217f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054453`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY FALSE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIE
```

---

## Crash 133: `a50f1fb9a46cc81b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054461`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count() OVER (PARTITION BY TRUE ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW)
```

---

## Crash 134: `ed55eef5dc78e335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054474`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_TIME DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)); CR
```

---

## Crash 135: `1fc0997f2c054391` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054495`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 136: `edf0efb10121a71f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054507`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]') ORDER BY FALSE COLLATE NOCASE DESC NULLS LAST LIMIT FALSE; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 137: `1e432d2957805943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054530`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT rank() OVER () ORDER BY rank() OVER () ASC NULLS LAST LIMIT CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 138: `0139b796716c4a34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054674`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE (WITH t3 AS (SELECT *) VALUES (CURRENT_TIMESTAMP))) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 139: `dcaa5a898339646a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054696`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY TRUE ROWS BETWEEN NULL IS NULL >= TRUE IS NULL COLLATE RTRIM PRECEDING AND CURREN
```

---

## Crash 140: `59313848454a96da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054735`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY TRUE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS)); CREATE
```

---

## Crash 141: `8b470d3fd6f60753` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054768`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY NULL ORDER BY FALSE ASC NULLS FIRST GROUPS BETWEEN UNBOUNDED PRECEDING AND CU
```

---

## Crash 142: `9d1defde3c676453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054912`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_DATE) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 143: `e1df1d60750debf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054969`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT rank() OVER (PARTITION BY NULL ORDER BY FALSE ASC NULLS FIRST GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW); CREATE TABLE seed_a
```

---

## Crash 144: `941eb02cfe63b1c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055102`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT ALL CURRENT_TIMESTAMP AS haz47_kr8a8__8_l71u951gou___2___29_o45wrn_7_s6n_pfm__4_3_j8_e3ags__bs27_c_8_g__z_b0c__9bg FROM p NATURAL JOIN
```

---

## Crash 145: `3c67e8e6417ac082` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055141`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT ALL * FROM json_each('{"a":1}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 146: `f9dee0ee215475b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055148`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT ALL * FROM json_tree('[1,2,3]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 147: `3413e4ff4a0a75fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055170`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT ALL * FROM json_tree(TRUE, '$'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 148: `c1327e5a920d697e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055185`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT ALL * FROM json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURA
```

---

## Crash 149: `f2d5d040917cd990` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055241`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (FALSE | NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INSERT INTO p DEFAULT VAL
```

---

## Crash 150: `8aa5a857745083e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055262`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN SELECT rank() OVER (PARTITION BY CURRENT_TIME, CURRENT_TIMESTAMP) ORDER BY CURRENT_TIME
```

---

## Crash 151: `f88782914f767f40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055277`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (NOT TRUE IS NULL | FALSE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INSERT INTO p
```

---

## Crash 152: `2d90e4c590cf6894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055371`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid, b, c2); INSERT INTO p DEFAULT 
```

---

## Crash 153: `ee0626a2e4d3a215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055414`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 154: `4ef78d1e0578aa75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055589`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, a BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT * FROM (SELECT rank() OVER (), * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a
```

---

## Crash 155: `a84f3b329371cb8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055626`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT * FROM (SELECT rank() OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURRENT_DATE PRECEDING AND CURRENT ROW) FROM p WHERE NULL
```

---

## Crash 156: `67b3bda24798935f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056666`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_DATE OR CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL < TRUE COLLATE NOCASE) AS sub1; C
```

---

## Crash 157: `747d3a815b6f5da0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056675`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE, c2 BLOB UNIQUE, c3 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE NULL < TRUE COLLATE NOCASE) AS sub1; CREATE TABLE
```

---

## Crash 158: `3ae460beda0b8304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057560`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 159: `1ea4f607faffe32d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058519`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME IN (CURRENT_TIMESTAMP) LIKE CURRENT_DATE > NULL / CURRENT_
```

---

## Crash 160: `d950ca15c41a4045` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064036`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_tree('[1,2,3]') GROUP BY CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 161: `37816778e74ff510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064050`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE; CREATE TABLE seed_a(c 
```

---

## Crash 162: `1c36422b991575d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064060`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT rank() OVER (), * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 163: `b7a13abe3a8932ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064068`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM json_tree('[]') NATURAL LEFT JOIN json_each('{}') WHERE CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 164: `beb333048505c6ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064076`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT (SELECT rank() OVER () ORDER BY CURRENT_TIME ASC LIMIT CURRENT_DATE) FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 165: `e58863e2705fc2f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064083`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_each('[{"a":1},{"b":2}]') GROUP BY CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 166: `e39ac6795678654e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064115`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') GROUP BY CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 167: `5d091ca850996ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064238`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 168: `74f966003e9142d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064279`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c2 INTEGER UNIQUE, c1 DATE GENERATED ALWAYS AS (NULL <= FALSE) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT DISTINCT * FROM p NOT INDEXE
```

---

## Crash 169: `f55eeebd221eb0f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064315`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT _rowid_ FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 170: `14253d5a2ec0eb19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064321`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_DATE AS s__7 FROM p NOT INDEXED JOIN json_each('[{"a":1},{"b":2}]') GROUP BY FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 171: `7a87747cbcdf2957` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064486`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('{"a":1}') LEFT JOIN json_tree('{}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 172: `46284b6d66f4623c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070042`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CAST(NOT EXISTS (VALUES (TRUE)) AS NUMERIC)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 173: `72cdc0f3205e631d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070051`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 174: `c7c4c1e36bc1cf9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070062`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CASE WHEN TRUE THEN ~CURRENT_TIME ELSE NOT TRUE OR CURRENT_TIME END); CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 175: `0d3892d83f218316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070072`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (FALSE | '-  -') EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 176: `4232ad664bd63f8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070093`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP IS NOT FALSE NOT IN (FALSE LIKE NULL, CURRENT_TIME, CURRENT_DATE)) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c U
```

---

## Crash 177: `a5707768fad8ae74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070281`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (TRUE NOT IN (CURRENT_DATE, CURRENT_TIME, CURRENT_DATE)) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 178: `02fa122138f0d186` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070507`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (TRUE) EXCEPT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 179: `f1db964fa6866c21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079358`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p WHER
```

---

## Crash 180: `c1bb0125c8facc98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079378`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT json_array_length(json_array_length(changes())) FROM p
```

---

## Crash 181: `adf7c96ca6df610d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079388`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE UNION SELECT DISTINCT * FROM json_each('{}') WHERE CURRENT_T
```

---

## Crash 182: `b344555968e85e24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079396`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p
```

---

## Crash 183: `eafd0297ca26ea23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079408`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (' -xE_8s_') ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p WHERE TRUE; C
```

---

## Crash 184: `2d49e6c73cce2330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079437`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p (_rowid_) VALUES (CURRENT_TIMESTAMP * CURRENT_DATE); SELECT row_number() OVER () FROM p NATURAL JOIN p WHER
```

---

## Crash 185: `098d6215db6c906f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079539`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p WHERE TRUE;
```

---

## Crash 186: `481230f214c23d41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079545`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; SELECT row_number() OVER () FROM p NATURAL JOIN p WHERE TRUE;
```

---

## Crash 187: `8506a39f1484d6f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001688`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 188: `cdd5ef008dd30695` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002174`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 189: `e0aa42ae5670a072` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002211`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 190: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002278`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 191: `e6ff19014ee5c50f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002545`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VAL
```

---

## Crash 192: `92592866c5777822` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VAL
```

---

## Crash 193: `c39f1076424bd47c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002693`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VAL
```

---

## Crash 194: `9a8d0ee72284b4ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002898`

```sql
SELECT substr('', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 195: `f6109df03b740763` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002967`

```sql
SELECT printf('%.*d', -2147483648, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 196: `a93b20de0dabdf40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003016`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 197: `2aa70d28f70815c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004589`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), b TEXT UNIQUE, _rowid_ TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 198: `1a6674622e828cd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005212`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 199: `6e7b13d5ff17ef63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005232`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 200: `50569442515466db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 201: `8306e8c6449c0c88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 202: `18769056d6e0a117` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005372`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[1,2,3]') WHERE CURRENT_TIMESTAMP GROUP BY NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 203: `1aac5689ffbef5d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005459`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(a TEXT GENERATED ALWAYS AS (NULL) VIRTUAL, c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIM
```

---

## Crash 204: `dcb0a1d97b297ee2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005765`

```sql
SELECT printf('%.*g', 4294967296, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 205: `67bc0dd7047d32e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005944`

```sql
SELECT substr('Tp --', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 206: `2ac3685b4990460e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005992`

```sql
SELECT printf('%.*g', 4294967295, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 207: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006008`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 208: `939c5038c466c923` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006265`

```sql
SELECT printf('%.*f', 9223372036854775807, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 209: `3eb1e1fed98a1c24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011148`

```sql
SELECT printf('%.*d', 4294967295, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 210: `1658fb99d22d3956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011161`

```sql
SELECT round(1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 211: `f5fcf81af6c0ad24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011181`

```sql
SELECT printf('%.*s', 4294967295, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 212: `cfdb870e061ae912` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011187`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 213: `685484e5479b1c7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011198`

```sql
SELECT printf('%.*g', 4294967295, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 214: `4d847015f6057bab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011204`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 215: `6e804e67a93552dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011216`

```sql
SELECT substr('', 4294967296, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 216: `d444a2c82fde720e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011224`

```sql
SELECT printf('%.*g', -1, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 217: `9aa34e9367432234` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011230`

```sql
SELECT printf('%.*g', -2147483649, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 218: `51678c724f26ea08` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011237`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; 
```

---

## Crash 219: `ab2001c4eb8e7de9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011250`

```sql
SELECT printf('%x', -2147483648, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE
```

---

## Crash 220: `8eb2799ead101f7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011266`

```sql
SELECT printf('%.*g', 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 221: `608c1fd3e2c85923` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011314`

```sql
SELECT substr('_', 4294967295, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 222: `f0bb873fcac011d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012043`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CASE NULL < TRUE WHEN FALSE THEN CURRENT_DATE END); PRAGMA integrity_check; C
```

---

## Crash 223: `dd4aa5036ecb448d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012142`

```sql
SELECT substr('', 4294967295, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 224: `eb004d4916cfeb46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013359`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 225: `12d0c4236672280a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013367`

```sql
SELECT round(-0.0, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 226: `6ec7ff666677c9f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013402`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR FAIL INTO p VALUES (TRUE AND CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 227: `316044bfa303d143` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013409`

```sql
SELECT printf('%.*s', 4294967296, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 228: `fdb78aa92c68fa83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013417`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 229: `400607d663bee676` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013473`

```sql
SELECT substr('-40- GP7o_ 73_sz-Bz', 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 230: `cb76189176710b82` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016946`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_b(b INTEGE
```

---

## Crash 231: `dba27fe0d5f5c143` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016980`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 232: `e9b1d04c4a3df3da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019204`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[1,2,3]') WHERE CURRENT_TIMESTAMP GROUP BY ~NULL HAVING FALSE; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 233: `94065175db1c934a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019227`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[1,2,3]') WHERE CURRENT_TIMESTAMP GROUP BY NULL IS NULL HAVING FALSE; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 234: `39c2c1a9565cfb16` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019238`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIME ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT CURRENT_DATE OF
```

---

## Crash 235: `82b99a0c77a861a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019258`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); SELECT FALSE >> FALSE AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 236: `e8a6fab18e2eff38` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019286`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[1,2,3]') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME, NULL; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 237: `9042cf17ab6216c3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019300`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY NULL HAVING FALSE WINDOW w1 AS (); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 238: `0a49bb8c23c21a0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019488`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIME ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT CURRENT_DATE; C
```

---

## Crash 239: `cd472bad62bffeb5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019525`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') WHERE FALSE GROUP BY NULL HAVING FALSE WINDOW w1 AS (); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 240: `067ed5039fc0f21e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019539`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIMESTAMP AS w_1y1s_5tu_phhwd94__g4__0a1cr_kiy8b0d9_z_f98__6n25__75__5u31ek0 FROM json_tree('[{"a":1
```

---

## Crash 241: `fa0dfbbc7d937ad0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019615`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP AS a611c___pd1_m_208d0j0___dc_d18_z ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT CURRENT_DATE; CREA
```

---

## Crash 242: `4b6aef51a460d572` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020313`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIME; CREATE TABLE IF NOT EXISTS p(c3 INT GENERATE
```

---

## Crash 243: `f9736fa35475c633` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020446`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 244: `361a82002e1031a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020475`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIME IS NOT FALSE; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 245: `f10bd4bc2693a5c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020494`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT DISTINCT * FROM p ORDER BY TRUE DESC NULLS LAST LIMIT FALSE; SELECT * FROM p JOIN p a ON FALSE 
```

---

## Crash 246: `d141d1ed9430ecfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> -CAST(NOT EXISTS (VALUES (TRUE)) AS NUMERIC); CRE
```

---

## Crash 247: `f23416ab0d729d77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020507`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT count(*) FILTER (WHERE CURRENT_DATE), *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIM
```

---

## Crash 248: `f7e8ccbbfab3158a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_DATE BETWEEN CURRENT_TIME AND FALSE, * FROM p NATURAL JOIN p WHERE TRUE
```

---

## Crash 249: `aecbb20a4c39e227` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020519`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_DATE) FROM p JOIN p a ON FALSE <> CURRENT_TIMEST
```

---

## Crash 250: `85a92516cf7c3e7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020529`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE) UNION VALUES (CURRENT_DATE); SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMEST
```

---

## Crash 251: `0c0f0021a01ef966` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020535`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NU
```

---

## Crash 252: `53686cf37aa194b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020541`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (NULL); SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMESTAMP; CREATE TABLE seed_t
```

---

## Crash 253: `83f50de7847de196` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020548`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_DATE > NULL / CURRENT_TIME; CREATE TABLE seed_t1(c
```

---

## Crash 254: `44245e5f0e479468` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020555`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 255: `b42821762e45b497` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020562`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_DATE LIKE CURRENT_DATE AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__0
```

---

## Crash 256: `02e9e0cdada8bb79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020570`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (CURRENT_TIME); SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c
```

---

## Crash 257: `6ef2482242458094` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020577`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, a BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIMESTAMP
```

---

## Crash 258: `05e698950ce1852c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020586`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_DATE BETWEEN CURRENT_TIME AND FALSE FROM p JOIN p a ON FALSE <> CURRENT
```

---

## Crash 259: `3bb7cffd457fb63e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020602`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP GROUP BY RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; SEL
```

---

## Crash 260: `65fd0c3790587ade` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020609`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p JOIN ((SELECT *) AS a , jsonb_each('[1,2,3]') ON CASE WHEN TRUE THEN ~CURRENT_TIME ELSE NOT TRUE OR C
```

---

## Crash 261: `1a2b831bf9ffbd2c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020615`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON NULL IS NULL >= TRUE IS NULL COLLATE RTRIM <> CURRENT_TIME
```

---

## Crash 262: `7ce275c8dbf26a64` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020621`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE NOT IN (NULL) <> CURRENT_TIMESTAMP; CREATE TABLE see
```

---

## Crash 263: `f98d84d6c7f03fb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> +NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 264: `5ffbbf8a52ba38f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020633`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT * ORDER BY CURRENT_DATE DESC NULLS FIRST, FALSE DESC NULLS FIRST; INSERT INTO p DEFAULT VALUES; SELE
```

---

## Crash 265: `596f3a199a6799e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020648`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE NOT NULL) UNION SELECT * ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; INSERT INTO p DEFAULT VALUES; SELECT * FROM
```

---

## Crash 266: `f6c795d5129fa6b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020661`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL changes() FILTER (WHERE NULL) OVER (PARTITION BY CURRENT_TIME) AS gt_660hbuw58___h_753__e_or___r8_3___q_7_79e___3_a
```

---

## Crash 267: `5bcac2126093777e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020668`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> FALSE <= CURRENT_DATE IN (VALUES (CURRENT_TIME));
```

---

## Crash 268: `176c9a96f5c07574` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020675`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_DATE >> CURRENT_DATE; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 269: `d6fa1bbf90caa690` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020682`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_DATE >> NULL IS NOT NULL <> CURRENT_TIMESTAMP; CRE
```

---

## Crash 270: `0afb770145e6cdbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020688`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CASE NULL WHEN CURRENT_TIME THEN TRUE ELSE CURREN
```

---

## Crash 271: `51d8c7b2914d8a76` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020697`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE se
```

---

## Crash 272: `9933876097164d9e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020743`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b INTEGER NOT NULL DEFAULT X'Be30fe'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> CURRENT_TIME
```

---

## Crash 273: `88fd77c54fbc5674` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020758`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.*, RAISE(IGNORE) ISNULL LIKE CURRENT_TIME NOT IN (VALUES (CURRENT_DATE, FALSE) INTERSECT SELECT *, *, *) > NOT CAST(R
```

---

## Crash 274: `d76d643e241e39e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020815`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> total_changes(); CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 275: `7a972cfa095b566d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020821`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> json_quote(CURRENT_TIMESTAMP); CREATE TABLE seed_
```

---

## Crash 276: `51b2ba6caa48eb09` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020827`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> json_quote(CURRENT_DATE NOTNULL); CREATE TABLE se
```

---

## Crash 277: `b64dadfbd1ce844f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020848`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON json_quote(TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 278: `c617407deb69a981` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020874`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON json_quote(CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 279: `4be7cd54e8783034` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020923`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_DATE IN (VALUES (CURRENT_TIME)); CREATE TABLE seed
```

---

## Crash 280: `93a38e10ba519dc3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020947`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE / CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 281: `5db847840ffe018a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020967`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_DATE) FROM p JOIN p a ON FALSE; CREATE TABLE see
```

---

## Crash 282: `74de423c4c61fc41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020993`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE <> -CAST(CURRENT_DATE AS NUMERIC); CREATE TABLE seed
```

---

## Crash 283: `ae43732d6ea97e2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021059`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT last_insert_rowid() AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1
```

---

## Crash 284: `51d7767302d5815b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021065`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') WHERE FALSE GROUP BY NULL HAVING FALSE WINDOW w1 AS () INTERSECT SELECT * ORDER BY CURRENT_
```

---

## Crash 285: `36d59936414afb30` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021073`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP >= NULL; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 286: `346ed8e93220cd91` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021081`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_DATE), * FROM p JOIN p a ON FALSE; CREATE TABLE 
```

---

## Crash 287: `b6ba07682917c6f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021090`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) INTERSECT SELECT * FROM jsonb_each('{"a":{"b":1}}') WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS
```

---

## Crash 288: `2bc72b9267c9f7c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT count(*) FILTER (WHERE CURRENT_DATE), CURRENT_TIME IN (FALSE) AS a611c___pd1_m_208d0j0___dc_d18_z; INSERT INTO p DEFAUL
```

---

## Crash 289: `b5f0a0b5a40e56fd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021127`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY, c1 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1
```

---

## Crash 290: `5fdec1c2b0c88851` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021134`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE || TRUE); SELECT * FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1(c1 
```

---

## Crash 291: `a7d142697bedd3b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021151`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAM
```

---

## Crash 292: `87e35bd864038550` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021160`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)), t1 AS (VALUES (FALSE)
```

---

## Crash 293: `4922f446e3288f1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT p.* FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 294: `3a001a9ffcbbca67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021230`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT 0.0); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 295: `95f3b7a76755721a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022965`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE
```

---

## Crash 296: `c283bef7ac41065f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, c2 BLOB NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 297: `0c5beb6bc6c54ac5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026038`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 298: `9b08dd3601bc35b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026081`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 299: `587a7c101b84ade7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027054`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CURRENT_TIME <> NULL), c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 300: `c2c5297d977bd7aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027065`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (TRUE)) AS r CROSS JOIN json_each('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP;
```

---

## Crash 301: `b623ea9234ddde73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027084`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 302: `35e0185981e5e1b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027098`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT changes() AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u
```

---

## Crash 303: `85a85530ae2aba87` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP LIKE random() AS k_d__0__2ri_n__4jm5779__9_ik062__0ta
```

---

## Crash 304: `9bb5c8b80c959ebd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033056`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); WITH q AS (SELECT *) VALUES (TRUE) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 305: `d3f60ac10ba527a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033143`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT EXISTS (SELECT * FROM json_each('[1,2,3]')) LIKE CURRENT_TIME COLLATE NOCASE ESCAPE '' COLLATE BINARY AS h_k6 FROM p WHERE EXISTS (VALUES
```

---

## Crash 306: `66d246d6a1cfa5e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035888`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); WITH q AS (SELECT *) VALUES (TRUE) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 307: `5f50cdfff4942b86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036048`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1
```

---

## Crash 308: `a27517196ff6d0ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT CASE NULL WHEN CURRENT_TIME THEN TRUE ELSE CURRENT_TIMESTAMP END AS k_d
```

---

## Crash 309: `badc8e1881986ab1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036886`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_DATE) FROM p JOIN p a ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 310: `b034f1543fff5b7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036994`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT cume_dist() OVER () AS s__7 FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_DATE INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 311: `3fc6af1a7c10c779` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037221`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (FALSE) STORED, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREAT
```

---

## Crash 312: `7bb2ae6d95dd48d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037352`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE TABLE seed_
```

---

## Crash 313: `57006c2b5bbc2c74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037405`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE || TRUE); VALUES (CURRENT_TIME); CREATE TABL
```

---

## Crash 314: `be58728c953c023b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039296`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 315: `9779e562aa87d80e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 316: `1b9dc23f71b0f201` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039341`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT min(CURRENT_TIMESTAMP) AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u; CREATE TABLE 
```

---

## Crash 317: `9313a852d240ccaa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039355`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 318: `2352406ca68bc698` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039381`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NULL; CREATE TABLE IF NOT 
```

---

## Crash 319: `e1986a600d7b5390` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039396`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM jsonb_tree('[{"a":1},{"b":2}]') CROSS JOIN (jsonb_each('{}')) , jsonb_each('[1,2,3]') WHERE C
```

---

## Crash 320: `f75ba6b5cbb8f429` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039402`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT *, * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NU
```

---

## Crash 321: `d79c0a8624c010cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039414`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT rank() OVER () FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS
```

---

## Crash 322: `3d163969eae008b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039435`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 323: `79bcfa347fef08e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039447`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c1 DATE, c3 GENERATED ALW
```

---

## Crash 324: `0cbe3cf850f52b4f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CR
```

---

## Crash 325: `c04460401ba40d0e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039593`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 326: `3d4416c227db0e79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039683`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p NOT INDEXED JOIN (p) WHERE CURRENT_TIMESTAMP INTERSECT SELECT *; SELECT * FROM (SELECT * FR
```

---

## Crash 327: `76dd064d9f0a3576` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039692`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT *, CURRENT_TIME FROM p WHERE NULL) AS sub1; CREATE TABLE seed_b(b INTEGER); INSERT I
```

---

## Crash 328: `cf3dbc5f68aa1269` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039710`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (RAISE(IGNORE))), q AS (SELECT *) SELECT * FROM jsonb_tree('{"a":1}'); SELECT * FROM (SELECT * FRO
```

---

## Crash 329: `658b2f63fb0efc2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039724`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) FROM p WHERE NULL) AS sub1; CREAT
```

---

## Crash 330: `f1f9b07a70f44dd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039735`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP LIKE random()) AS sub1; CREATE TABLE seed_b(b INTEG
```

---

## Crash 331: `bef73034186981af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039754`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) FROM (SELECT * FROM p WHERE NULL) AS sub1; CREAT
```

---

## Crash 332: `497c177a41023db2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039764`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH q AS (SELECT *) VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_
```

---

## Crash 333: `5706af28151b902e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041883`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (NOT TRUE IS NULL) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 334: `e18550bebe4c0e71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042168`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, a BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 335: `0a95076b4012a225` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042206`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM p NOT INDEXED LEFT JOIN p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 336: `b6c8f3a0ecc7d6c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042380`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (NOT CURRENT_DATE) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 337: `da9c574ddb3db205` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047315`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM (SELECT rank() OVER (), * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 338: `74d5143e4592f755` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050487`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME IS NOT FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEG
```

---

## Crash 339: `1f3e49c626087634` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (FALSE) STORED, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 340: `4a66797851b53a5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053410`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (X'') INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGE
```

---

## Crash 341: `8f197bd2798029ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 342: `d50281f5d101e6b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057646`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL)
```

---

## Crash 343: `f6e9f7d86c2c62d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057905`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT FALSE <= CURRENT_DATE IN (VALUES (CURRENT_TIME)) FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 344: `1b3a7c0e92f86e8c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057924`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT CASE WHEN CURRENT_DATE THEN json_array_length(NOT EXISTS (VALUES (TRUE))) ELSE CURRENT_TIMESTAMP END FROM p WHERE NULL) AS
```

---

## Crash 345: `34a89ee6c638f6ce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057932`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE FALSE NOT LIKE NULL >= TRUE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 346: `ef9770b44decbeda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057948`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT -54311449824393150614980670851975276549309931074885783354279298922214357425964419514792776221849748911707674456119438364.94490802433778311240762087
```

---

## Crash 347: `430a7d5205f52d0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057955`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT TRUE AND TRUE, * FROM (SELECT TRUE FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 348: `f716be2a9c46a6cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057968`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE
```

---

## Crash 349: `aff6b29eb777ac41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057986`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT -608189); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 350: `58fdff343bd1b1d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058864`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -608189); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT * FROM p WHERE CASE WHEN CURRENT_DATE THEN json_array_length(NOT EXISTS 
```

---

## Crash 351: `77ea20807429dc6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058896`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CASE WHEN CURRENT_DATE THEN json_array_length(NOT EXISTS (VALUES (T
```

---

## Crash 352: `99f27fc22370e373` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058947`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT rank() OVER () FROM (SELECT * FROM p WHERE CASE WHEN CURRENT_DATE THEN json_array_length(NOT EXISTS (VALUES (TRUE))) ELSE CURRENT_TIMESTAMP
```

---

## Crash 353: `35c45f22c00b3606` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061275`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); INSERT INTO p (c1) VALUES (CURRENT_TIMESTAMP * CURRENT_DATE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 354: `976205ab7ebfed6e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063375`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP >= NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLA
```

---

## Crash 355: `456bc17bcf23024e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063592`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES ((SELECT DISTINCT rank() OVER () FROM json_tree('[1,2,3]') WHERE TRUE))
```

---

## Crash 356: `3ffce528de2260d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063630`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (FALSE > NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 357: `ef41011b88ff6c2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063638`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE, rowid REAL PRIMARY KEY, c1 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAG
```

---

## Crash 358: `61d6079ebd17bbca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063650`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR FAIL INTO p VALUES (FALSE IS NOT CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 359: `b4ad2b7881b3c2dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063667`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB CHECK (FALSE <= FALSE)); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 360: `72ab80ee9fc74fef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063699`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (FALSE) STORED, c1 NUMERIC DEFAULT X'a0c6faEE'); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME
```

---

## Crash 361: `1fb8277504fedf00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063720`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME == CURRENT_DATE); PRAGMA integrity_check; CREATE 
```

---

## Crash 362: `5123a4d612ba7217` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063728`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME - TRUE IS NOT TRUE); PRAGMA integrity_check; CREAT
```

---

## Crash 363: `ba1500408c1f4efa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063760`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT 4.0406267E-716714676, c3 BLOB GENERATED ALWAYS AS (X'') VIRTUAL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES
```

---

## Crash 364: `703b27e33ba41219` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063819`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -5773.76174804979809727679464577020461182103160103232119593808605136098168728261100951971588836407597700542335180); CREATE TABLE IF NOT EXISTS q(c3
```

---

## Crash 365: `19b172d9511f2e11` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, c2 BLOB NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 366: `ee7025f5439879fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064578`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT min(CURRENT_TIMESTAMP) FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 367: `99247abc71ef66c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066098`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT rank() OVER () ORDER BY (VALUES (CURRENT_DATE)) ASC NULLS LAST LIMIT CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 368: `87b0c9517af17048` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066448`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP) UNION VALUES (TRUE)) AS i4k0c0_ WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 369: `e125f570513e1ab5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067481`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (RAISE(IGNORE))), q AS (SELECT *) VALUES (NULL); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE, RAISE(I
```

---

## Crash 370: `ac0b4b15ec735af2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067552`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT CURRENT_DATE + NULL LIKE CURRENT_DATE > NULL / CURRENT_TIME AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u; CREATE TABLE s
```

---

## Crash 371: `901a68c7b8149ad0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067561`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT 70223442138966429174516.386636446873712E+931); CREATE TABLE IF NOT EXISTS q(b BOOLEAN PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_
```

---

## Crash 372: `30330f9050c46dda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067573`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE, RAISE(IGNORE))); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 373: `f6c93a588c993662` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067718`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (FALSE IS NULL)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (WITH q AS (SELECT *) SELECT * FROM json_each('{"a":{"b":1}}'
```

---

## Crash 374: `eff528f09324ffb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067747`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p SELECT DISTINCT CURRENT_TIMESTAMP AS w_1y1s_5tu_phhwd94__g4__0a1cr_kiy8b0d9_z_f98__6n25__7
```

---

## Crash 375: `69832d4c026322ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067939`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count(DISTINCT NULL) FILTER (WHERE FALSE))); CREATE TA
```

---

## Crash 376: `a8026d9aaa26b5e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067985`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT random() AS k_d__0__2ri_n__4jm5779__9_ik062__0tac6__ua__01_hvp__0_q1_u; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---
