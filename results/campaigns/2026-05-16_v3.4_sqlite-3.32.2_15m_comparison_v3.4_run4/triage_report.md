# Crash Triage Report

**Total crashes:** 289  
**Unique crash sites:** 289  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 13 | 13 | 4% |
| Signal | 276 | 276 | 95% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `b53c347b2046ef71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, a, _rowid_); INSERT INTO s VALUES (TRUE < CURRENT_TIMESTAMP, RAISE(IGNORE) ISNULL == CURRENT_TIMESTAMP IS NOT NULL IS NULL) RETURNING p.*, -
```

---

## Crash 2: `ab4ede2608530a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001380`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c1, _rowid_); INSERT INTO t1 VALUES (CAST(TRUE COLLATE NOCASE LIKE RAISE(IGNORE) ESCAPE
```

---

## Crash 3: `0767f4b61b169bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008015`

```sql
SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, _rowid_, c1); INSERT INTO p (c2) VALUES (RAISE(IGNORE) COLLATE NOCASE); ANALYZE q; CREATE TABLE IF NOT EXIST
```

---

## Crash 4: `a3e2456b1cb4227c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008144`

```sql
SELECT substr('', 4294967295, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.*, ~CURRENT_TIME NOTNULL IS TRUE IS CASE CURRENT_TIME WHEN NULL THEN (CURRENT_TIME) GLOB 
```

---

## Crash 5: `b2b6e9182383d60e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011338`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT GENERATED ALWAYS AS (TRUE) VIRTUAL, c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES
```

---

## Crash 6: `548949652a18eeb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018412`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (TRUE) UNION ALL SELECT CURRENT_DATE >> TRUE FROM json_each('[{"a":1},{"b":2}]'); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE
```

---

## Crash 7: `5a44334881c3c4c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041809`

```sql
SELECT printf('%x', 9223372036854775807, ''); SELECT round(-1e308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c1, _rowid_); SELECT * FROM jsonb_each('{}') WHERE TRUE ORDE
```

---

## Crash 8: `cf5b33c01ded3a21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042193`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP LIKE NOT EXISTS (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; C
```

---

## Crash 9: `96bf255bc0475070` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 10: `54c788ce78c35c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056820`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 11: `a3987d3117128eac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057032`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); REPLACE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 12: `6d4b6b0281277411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063019`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE <> CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TAB
```

---

## Crash 13: `6e5ba04a671db9fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076514`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) EXCEPT SELECT TRUE FROM json_tree('{"a":1}')) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 14: `698c729d18bb7009` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000000713`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 15: `29a609b801804ca2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001802`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') NATURAL JOIN p INDEXED BY rowid WHERE CURR
```

---

## Crash 16: `a5c119af61978449` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001873`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSER
```

---

## Crash 17: `58523a2c6faf8ba5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001880`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 18: `a8d89c5f1143e0d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001886`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGE
```

---

## Crash 19: `af4a052e7bd3d9c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001895`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 20: `1dd67b9f5e31c17d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001926`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 21: `6f2401de18e40d80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002674`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 22: `20bd6db2d3e160d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003792`

```sql
SELECT substr('', 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c
```

---

## Crash 23: `9944f89e3b82ae74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004022`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 24: `37782b8028a1e83f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004379`

```sql
SELECT substr('9-8 P-__- _4-DC__', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44
```

---

## Crash 25: `d02e11b4587209a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004414`

```sql
SELECT printf('%u', 1, '_E1___-5 md_6-Y_  -'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123
```

---

## Crash 26: `4b62f4f168dbe38a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005035`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 27: `188588adbaa7acd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE, NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 28: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005144`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 29: `e924340a4f879885` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005160`

```sql
SELECT hex(zeroblob(0)); SELECT substr('2 -_9g9--_i3-v _T2 ', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INS
```

---

## Crash 30: `f87e296640a25ef7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006394`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 31: `38a7e92b7f81ab37` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006405`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 32: `09c196474ae17acc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006415`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL VALUES (TRUE); 
```

---

## Crash 33: `afb598727ef1bf8c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006436`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 34: `47638b2dde854385` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007145`

```sql
SELECT substr(' __2 -3 _-E-EM0v', 4294967295, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(4
```

---

## Crash 35: `ee681c8fcc68f807` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007335`

```sql
SELECT substr('  7_Zv-', 2147483647, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 36: `f69a3f7da828fe65` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010350`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1, c2, c3, _rowid_); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 37: `3d645f8e0c987788` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011434`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 38: `5a24376043c0e572` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011450`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 39: `664daf15c3accf87` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011656`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 40: `629088c86f303ffe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011848`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 41: `3945d884af460fdd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012055`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 42: `3d849c52091336e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013907`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 43: `30e5ed60d2eaddfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016303`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 44: `387b6e93999b473c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016313`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 45: `40576b8fa9aefc0e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016319`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 46: `aeb1fa52bb2205f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016327`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_DATE); PRAGMA integrity_check;
```

---

## Crash 47: `6f4e3b10f82fa5b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016335`

```sql
SELECT round(0.01, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 48: `ef0b2d3ff9aaa956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016368`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (RAISE(IGNORE))); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 49: `4aaf09bf01703c67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016377`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT -559.402602874296830112339845359716182968723140907832608870588410654644559841182369031534153241356949596612288588547744357594205173222855189243629181079
```

---

## Crash 50: `22dc5284d0e62804` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016396`

```sql
SELECT round(1.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 51: `7d13df35db656c4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016407`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_DATE BETWEEN NULL AND CURRENT_TIME), c2 VARCHAR(255)); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 52: `db29d081d86ebbf8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016416`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (SELECT *) SELECT *; SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 53: `e9a5bdf0ce1a2c2c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016444`

```sql
SELECT printf('%.*e', 4294967296, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 54: `469217fc3e59b663` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016453`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 55: `a5dfc0adecd7ffc7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016481`

```sql
SELECT printf('%.*g', 1, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 56: `6ba6ae79dbc336b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016489`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN, c3 GENERATED ALWAYS AS (c1) NOT NULL UNIQUE, a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 57: `a39676ca5640f7c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016498`

```sql
SELECT round(0.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 58: `96e9046d776ffebd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016639`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT * FROM (SELECT TRUE IN (FALSE COLLATE RTRIM) AS gb FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 59: `c312194b85a2ce17` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (SELECT *) AS h4s49v334_z44____w_14_8w1y__9a2_rw6_3374338pr_7h__48_0yh1w6_546_ks9_1__pl___u1c___p1_u3nz_8_4_u_t0
```

---

## Crash 60: `5ff7cbc1acaa8c52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016690`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 61: `1d6bebde62285c04` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTA
```

---

## Crash 62: `93db32943053ac62` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016791`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (TRUE) UNION ALL SELECT CURRENT_DATE >> TRUE / CURRENT_TIMESTAMP FROM json_each('[{"a":1},{"b":2}]'); EXPLAIN QUERY PLAN VALUES (CURREN
```

---

## Crash 63: `cd4e9840b49c4468` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016808`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT * FROM (SELECT rank() OVER () AS gb FROM p WHERE NOT EXISTS (VALUES (FALSE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 64: `d76ec25c9198ef18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016819`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 65: `c818e6feb3f538a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019326`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); REPLACE INTO p VALUES ((SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY FALSE ORDER BY TRUE DESC) << (SELECT NULL ORDER BY CURRENT_TIMESTAMP DE
```

---

## Crash 66: `619ad79dda02acf2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019337`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CAST(CAST(CAST(CAST(CAST(CAST(CURRENT_TIME AS INTEGER) AS INTEGER) AS INTEGER) AS INTEGER) AS INTEGER) AS INTEGER)) UNION ALL SELECT F
```

---

## Crash 67: `65ab52090a8ce344` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019345`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (+CURRENT_TIME) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 68: `bd65b768e196e832` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019355`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE) UNION ALL SELECT count() FILTER (WHE
```

---

## Crash 69: `c02bcd3e96d72785` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019365`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 70: `0f042a32456649af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019376`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (count() FILTER (WHERE CURRENT_TIMESTAMP), T
```

---

## Crash 71: `a910b2c20910bf2f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019390`

```sql
SELECT printf('%f', -1, ' e Br4_X_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE
```

---

## Crash 72: `f79db93f24a44edb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019397`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (count() FILTER (WHERE CURRENT_TIMESTAMP)) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE 
```

---

## Crash 73: `a29893d97e37d9e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019414`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) INTERSECT SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 74: `c4d0b055e83f623e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019422`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT min(NULL) OVER () IS TRUE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE se
```

---

## Crash 75: `86be4a5ea2285356` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019431`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN SELECT FALSE / TRUE OR count() FROM p NOT INDEXED; 
```

---

## Crash 76: `a4c367f7c37ea8a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019438`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p VALUES (FALSE) UNION ALL SELECT FALSE / count() FROM p NOT INDEXED; PRAGMA int
```

---

## Crash 77: `cda0c5b5acc8aefc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019453`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 78: `868c1994a760875a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019474`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM p; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 79: `9550abb437e004ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019510`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1
```

---

## Crash 80: `d288cc3ffcd98256` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019542`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT 9); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 81: `9cc719551fd5638d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019554`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('{}'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 82: `af257dce43706f67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019564`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(_rowid
```

---

## Crash 83: `c1e3996fc45cc81f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019571`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(_rowid
```

---

## Crash 84: `ac57fbbdb968ac89` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019578`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT FALSE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(_rowid
```

---

## Crash 85: `bd7c54042bdc8620` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019639`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 86: `27eaa4e564f06fcc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019766`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT CURRENT_TIMESTAMP IS TRUE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE se
```

---

## Crash 87: `ab199f1f159525fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019772`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT count() OVER () IS TRUE FROM json_each('[1,2,3]'); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed
```

---

## Crash 88: `982c640486d420d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019900`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP << CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 89: `6c00deeea6004515` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019921`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 90: `ee78560836a80f37` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019929`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT GENERATED ALWAYS AS (TRUE) VIRTUAL, c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed_
```

---

## Crash 91: `73302bb17cd3a494` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019945`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT TRUE <> 
```

---

## Crash 92: `e94b423e4d6f8a49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019972`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 93: `8cf674b24e0911f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019982`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT TRUE AND CURRENT_TIME FROM json_each('[{"a":1},{"b":2}]') UNION ALL SELECT CURRENT_TIMESTAMP FROM json_each('{"a":1}'); VALUES (CURRENT
```

---

## Crash 94: `105912da48a08eac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019993`

```sql
SELECT substr('', 2147483648, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 95: `34dc969885577986` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020002`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 96: `e64999affce41595` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020008`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 97: `7e9fa40a43c03ae2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020018`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT -6.0763935631971473114e+20); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx6
```

---

## Crash 98: `f6fbc11fd2c40dba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020025`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 99: `4967c9fed351bc93` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020031`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE >> CURRENT_DATE FROM json_each('[{"a":1},{"b":2}]') UNION ALL SELECT CURRENT_TIMESTAMP FROM json_each('{"a":1}'); VALUES (
```

---

## Crash 100: `cf94b96592d6feb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020037`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT NULL IN (VALUES (NULL)) AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELE
```

---

## Crash 101: `2067d6ebc2da2ff6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020069`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ EXCEPT SELECT CURRENT_TIM
```

---

## Crash 102: `e203c73e42a91ec7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020115`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT FALSE); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT 
```

---

## Crash 103: `8a1e72474634ea4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020193`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL VALUES (CURRENT
```

---

## Crash 104: `7ac534edfd6312a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020228`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 105: `84638fdb94cdf726` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020237`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 106: `34a560de26e49ff5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020244`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 107: `810bdead6e51a0fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021162`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (TRUE) UNION ALL SELECT TRUE OR CURRENT_DATE FROM json_tree('{"a":1}'); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE TABL
```

---

## Crash 108: `309fe795ff29889e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021240`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (TRUE) UNION ALL SELECT TRUE OR CURRENT_DATE FROM json_tree('{"a":1}'); EXPLAIN QUERY PLAN SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___3
```

---

## Crash 109: `981e824d68bddec5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021435`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (TRUE) UNION ALL SELECT TRUE OR count() FROM json_tree('{"a":1}'); EXPLAIN QUERY PLAN VALUES (FALSE) UNION ALL VALUES (CURRENT_TIMESTAM
```

---

## Crash 110: `86bdb10d9cb8b0ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021535`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 111: `bb5354ff0e405107` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021718`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT TRUE FRO
```

---

## Crash 112: `dadd465015fcea93` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022789`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT CURRENT_
```

---

## Crash 113: `ddb7d7ae39b0cb85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024596`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT FALSE FR
```

---

## Crash 114: `30e76424fa74a974` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024770`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT FALSE FR
```

---

## Crash 115: `6eb503ab63224e63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028080`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE IN (FALSE >= rank() OVER () COLLATE RTRIM)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE s
```

---

## Crash 116: `ae871bd3dea52377` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028086`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT ALL
```

---

## Crash 117: `f9c326a414f13378` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028095`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP GLOB FALSE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 118: `b3bbbfb0db51c860` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028103`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q; CREATE
```

---

## Crash 119: `5b3b234f6f003422` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028109`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE, _rowid_ INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 120: `1e2784954c46f445` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028116`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT '    bK_'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 I
```

---

## Crash 121: `38fbb52f021bea76` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028127`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (FALSE NOT NULL); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 122: `1e2dd989b0434c48` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT -CURRENT_TIME AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7
```

---

## Crash 123: `f33f71455601e5d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028146`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE + TRUE, CURRENT_TIMESTAMP IS NULL / CURRENT_TI
```

---

## Crash 124: `19070b000e4bf93f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028158`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP IN (CURRENT_DATE)); CREATE TABLE 
```

---

## Crash 125: `89469a69e5610519` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028167`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (FALSE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 126: `2e560dd2aba31317` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE >= NOT CURRENT_TIMESTAMP <> CURRENT_TIMESTAMP 
```

---

## Crash 127: `f3c86f4aa6f28d86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028179`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT 436319426573.68E+296312233551071520308368542070074932007347786788882122398133835175429535753157993786955483301794390); CREATE TABLE IF NOT EXISTS q(c1 INT
```

---

## Crash 128: `ada2e84ba8401c79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028187`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (rank() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS FIRST GROUPS BETWEEN UNBOUNDED PRECEDIN
```

---

## Crash 129: `839cf0a1af95a8d2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP)), NULL AND FALSE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE
```

---

## Crash 130: `4b4aa37cfed17ddf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028200`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (2040.71401654432502785E-946869492372472210220); CRE
```

---

## Crash 131: `876e1b5558b96498` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028218`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT FALSE FROM p NOT INDEXED NATURAL LEFT JOIN json_tree(RAISE(IGNORE) LIKE CURRENT_DATE, '$'); INSERT IN
```

---

## Crash 132: `0294b3c9d9c7c6bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028226`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (VALUES (CURRENT_DATE)), r AS (VALUES (CURRENT_TIME)) VALUES (NULL); INSERT INTO p DEFAULT VALUES
```

---

## Crash 133: `763c664513d2e712` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028232`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CASE RAISE(IGNORE) WHEN CURRENT_DATE THEN X'BCacd6ead8B9' END, CURRENT_TIME); INSERT INTO p DEFAULT VALUES; V
```

---

## Crash 134: `a135d85446067fa0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028244`

```sql
SELECT printf('%.*g', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 135: `3d73297253780c57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028253`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT cume_dist() FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_DATE, FALSE) FROM jsonb_each('{"a":{"b":1}}
```

---

## Crash 136: `cc6e4dd06b1a2759` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028267`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q INDEXED BY a , jsonb_each('{}'); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t
```

---

## Crash 137: `2518ba3d8b9a5f57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028336`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE 
```

---

## Crash 138: `80754bb8c208d18c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028354`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL r.* FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY TRUE ASC NULLS FIRST; INSERT INTO p DEFAULT VALU
```

---

## Crash 139: `b8eb0e320ab38b5c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY
```

---

## Crash 140: `33605a4f80667187` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028386`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q ON FALSE ORDER BY TRUE ASC NULLS FIRST; INSERT INTO p DEFAULT VALUES; VALUES (T
```

---

## Crash 141: `035330f725ceb478` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028655`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIME ASC NULLS FIRST, CURRENT_DATE DESC NULLS LAST, TRUE ASC
```

---

## Crash 142: `dede9349d21675e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028675`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('{"a":{"b":1}}') WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY TRUE DESC NULLS FIRST; 
```

---

## Crash 143: `5d5e3894ea6eee9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028711`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each(NULL > -CURRENT_TIME, '$') ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 144: `9787ae5b333ff163` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028718`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE IS NOT NULL IS NOT NULL IS NOT NULL DESC NULLS FIRST; C
```

---

## Crash 145: `478a3d6091f92330` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028743`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT cume_dist() OVER () FROM json_each('[1,2,3]') ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 146: `ae52fdddf398979b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028765`

```sql
SELECT printf('%.*g', -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed
```

---

## Crash 147: `31dc35ad1e2a8937` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028869`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME FROM json_tree('{}') WHERE NULL UNION ALL VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 148: `0a222f1fef139439` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028876`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME LIKE CURRENT_DATE ESCAPE CURRENT_TIME FROM json_tree('{}') WHERE NULL UNION ALL VALUES (NULL)
```

---

## Crash 149: `56f85d9ed456550b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031957`

```sql
SELECT printf('%.*s', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 150: `10f996645fea99a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031969`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT * FROM (SELECT rank() OVER (PARTITION BY CURRENT_DATE, CASE TRUE WHEN CURRENT_TIMESTAMP THEN NULL END) AS gb FROM p WHERE CURRENT_TIME) 
```

---

## Crash 151: `615f59b76e5b22cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031975`

```sql
SELECT printf('%x', 9223372036854775807, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123)
```

---

## Crash 152: `a6a153bd1863dd50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031995`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 153: `ea527b613d9c140d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032001`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') LEFT JOIN json_each('[1,2,3]') ON CURRENT_DATE WHERE CURRENT_DATE; CREAT
```

---

## Crash 154: `fdbbc91fac3b8b2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032021`

```sql
SELECT printf('%.*e', -9223372036854775808, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 155: `90daf1ab2d179d95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032029`

```sql
SELECT printf('%.*d', -1, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 156: `af009de7b36736ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032049`

```sql
SELECT printf('%.*s', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 157: `c7703b7b22ee9ca0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032060`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123
```

---

## Crash 158: `1cb43ba2213a31e4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032073`

```sql
SELECT printf('%.*g', 0, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 159: `ca2d5b33ffb9cf21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032103`

```sql
SELECT printf('%.*s', 2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 160: `cc7ccd63d104c2be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032621`

```sql
SELECT printf('%.*f', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 161: `1f7012359d846795` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032632`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS gb FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 162: `34bbe92e199b96c5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032638`

```sql
SELECT printf('%.*e', 9223372036854775807, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 163: `5b870fdc416a7ead` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032660`

```sql
SELECT printf('%.*d', 4294967296, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 164: `fcc19b5824139680` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032668`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT * FROM (SELECT FALSE COLLATE RTRIM AS gb FROM p WHERE CURRENT_DATE IS NOT NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 165: `2124730eba15392e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032695`

```sql
SELECT round(-1.0, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 166: `8a9c5d15ec03c355` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036332`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) UNION ALL SELECT CURRENT_TIMESTAMP GLOB CURRENT_DATE >> TRUE / CURRENT_TIMESTAMP FROM json_each('[{"a":1
```

---

## Crash 167: `1a1f5357fe757a1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037062`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ U
```

---

## Crash 168: `6b3fd0feb75b0669` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037303`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_tree(NULL, '$[#-1]') UNION ALL SELECT DISTINCT * FROM p WHERE NULL ORDER BY FALSE ASC NULLS FIR
```

---

## Crash 169: `4d6b6c1f18192453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040873`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE, count(*) FILTER (WHERE TRUE) ASC NULLS FIRST, ran
```

---

## Crash 170: `1627500b2d889633` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040978`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (TRUE) UNION VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 171: `090e6adc141a5df3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041065`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); SELECT FALSE FROM p NOT INDEXED UNION ALL VALUES (FALSE) UNION ALL VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 172: `f044e8937d38f567` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041154`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 173: `bcf6e6938320d8ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042270`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 174: `cb90ae7e09feed02` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042284`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 175: `845fc7b58a729733` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042307`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 176: `8e24439fe2cd36f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042330`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 177: `85fc5e6d5de7abbf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042348`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 178: `42d92298e451f14d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042500`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 179: `1a73599fdda7287f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043036`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b
```

---

## Crash 180: `740a437c6a14fd69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043277`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP LIKE NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a DATE,
```

---

## Crash 181: `ecca8b491a5176ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043432`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 182: `39a2710032992ec4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043964`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a DAT
```

---

## Crash 183: `d6fa793d91520c3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044188`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIME <= CURRENT_DATE > FALSE), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 184: `65837b94e1e1735c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044202`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE CURRENT_TIMESTAMP WHEN FALSE THEN NULL ELSE NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 185: `63827f277c575b1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044209`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (FALSE) STORED, a DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 186: `17198bef041dd5bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044217`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE, c3 BOOLEAN PRIMARY KEY, _rowid_ INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 187: `061dc87a597c9cff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044232`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NOT NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 188: `893d3e6cee54c9c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 189: `e8e531792e86cf1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044368`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE FALSE WHEN NULL THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 190: `37f2845e5cbcdc10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044406`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (FALSE); VALUES (CAST(CURRENT_DATE AS BLOB)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 191: `3698f380733ae50d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049609`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') GROUP BY TRUE ORDER BY CURRENT_TIME DESC NULLS LAST LIMIT TRUE OFFSET TRUE; CREATE TABLE 
```

---

## Crash 192: `c685809b9b95153a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049617`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT TRUE, b NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 193: `2e0e9b641fadf8f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049623`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE, CURRENT_TIMESTAMP / CURRENT_TIMESTAMP IN (CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP)); CREATE TABLE seed_t
```

---

## Crash 194: `345b9ac610082e11` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049642`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE FROM json_tree(CAST(TRUE AS INTEGER) == CURRENT_TIME, '$[#-1]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 195: `7d094477aee4bcb5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049658`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL NOT IN (NULL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 196: `5bbbbd34e3b92007` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049695`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE) UNION ALL SELECT min(FALSE) FROM p NOT INDEXED; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 197: `38bb1d1895036ac1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049709`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT row_number() OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST) / count() FROM p NOT INDEXED; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 198: `0c35d65cd714899a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049731`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b GENERATED ALWAYS AS (coalesce(a, b)) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 199: `1f8c35a9ded95776` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049962`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":{"b":1}}') WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_DATE; CREATE TABLE 
```

---

## Crash 200: `50e338559e60514a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049970`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 201: `6dab181bcdb56fa9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050001`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 202: `d1d98d148a362e93` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053910`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(a REAL UNIQUE); INSERT INTO q VALUES (NULL IS CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 203: `0dd98237dbb714f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054482`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE NOT NULL, CURRENT_TIMESTAMP) UNION ALL SELECT * FROM p ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST) SELECT * F
```

---

## Crash 204: `93db142311955a7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056166`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME, CURRENT_TIMESTAMP) UNION ALL SELECT * FROM p ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST) SELECT * FR
```

---

## Crash 205: `d8b994f497ccff77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057730`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 206: `ebbb8d706486aab1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061548`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT count() 
```

---

## Crash 207: `a63b2fe267313700` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061602`

```sql
SELECT round(1e308, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 208: `aa74c02985aade1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061711`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE FALSE WHEN NULL THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM 
```

---

## Crash 209: `d87ed6b09b05a5ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061846`

```sql
SELECT printf('%lli', -9223372036854775808, '-__Hx m'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),
```

---

## Crash 210: `d48ab7f841b9ffcb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061876`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE +json_patch('[1,2,3]', '[1,2,3]') WHEN NULL THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA in
```

---

## Crash 211: `b54df19c6c39a09f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE FALSE WHEN TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || FALSE THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INT
```

---

## Crash 212: `45a8042722420334` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061920`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || FALSE)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 213: `89a909b7e4b64e6f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061950`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE FALSE WHEN TRUE || NULL THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 214: `9c2c5c81f287a7e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061958`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CASE FALSE WHEN TRUE || TRUE || TRUE || TRUE || CURRENT_TIME THEN NULL END)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUE
```

---

## Crash 215: `d7bf7280f91279fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061996`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE || TRUE || TRUE || TRUE || CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CRE
```

---

## Crash 216: `a66501417e604769` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE || TRUE || TRUE || CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 217: `3daabef109254ddf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062027`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 218: `025a56a190913968` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062049`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE || TRUE || CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 219: `97fbd552e739407a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE >= FALSE)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 220: `221e7a252a3b1c58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062115`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT '    bK_', b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREA
```

---

## Crash 221: `7993f43d83a7fd14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062121`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), c1 NUMERIC DEFAULT X'0A08b7de', b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 222: `9872ce5eb107da27` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062129`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_t1(c1
```

---

## Crash 223: `2f17d64869c6ca0e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062143`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL DEFAULT -0); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 224: `61d31d242bc22471` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062150`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (TRUE NOT LIKE NOT NULL), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 225: `35abfe8d48d8e301` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062158`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (CURRENT_DATE >= CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 226: `b87ce5e504374cba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062170`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (CURRENT_DATE IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL)); CREATE TABLE IF NOT EXISTS q(b N
```

---

## Crash 227: `f9a5634d7aa8a409` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062191`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p SELECT * FROM p; PRAGMA integrity_check; CREATE TA
```

---

## Crash 228: `1665f82d354486ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062199`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (CURRENT_DATE IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL)); CREATE T
```

---

## Crash 229: `3c0886f92e960d8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062243`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), c3 DATE DEFAULT X'AeF6'); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TA
```

---

## Crash 230: `5eb7f701b7717aba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062308`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_TIMESTAMP), b INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 231: `13f44771abae0b51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062767`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (json_type(NULL))); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT,
```

---

## Crash 232: `b1e9398652170c7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066123`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT -559.402602874296830112339845359716182968723140907832608870588410654644559841182369031534153241356949596612288588547744357594205173222855189243629181079
```

---

## Crash 233: `303d192777696bba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066135`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT -559.402602874296830112339845359716182968723140907832608870588410654644559841182369031534153241356949596612288588547744357594205173222855189243629181079
```

---

## Crash 234: `ba5640f8ea1eff7c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067341`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b
```

---

## Crash 235: `6585b78259bb5db6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067539`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b
```

---

## Crash 236: `ddcc05c08733d587` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067773`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL CHECK (TRUE + NULL), c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_t1(c
```

---

## Crash 237: `a376984795135128` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067798`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT DISTINCT
```

---

## Crash 238: `abe9abdc44b3166b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067810`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (CURRENT_TIME); SELECT DISTINCT * FROM json_tree('{"a":1}') WHERE TRUE ORDER BY CURRENT_DATE DESC; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 239: `2c758d746a96bbca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068631`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (FALSE) UNION ALL SELECT FALSE FROM p NOT INDEXED; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 240: `f5e5e20058dfd251` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068660`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (TRUE) UNION ALL SELECT FALSE FROM json_tree(CAST(TRUE AS INTEGER) == CURRENT_TIME, '$[#-1]'); PRAGMA integrity_check; CREATE 
```

---

## Crash 241: `deea6918da90305b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069106`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT CURRENT_DATE AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed__3t0__284o_a576__1771339w17i_1___ UNION ALL SELECT FA
```

---

## Crash 242: `b571616b66af607f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075422`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_DATE) UNION ALL SELECT count() FROM json_tree('{"a":1}') LEFT JOIN json_each('[1,2,3]') ON CURRENT_DAT
```

---

## Crash 243: `4ed4efbcf54117ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075433`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_DATE) UNION ALL SELECT count() OVER () AS uu_36_g3z3dq_tk72___322hb9f8h0_c1g7qx66g_b_j__32_193f07__ed_
```

---

## Crash 244: `9adb22f1be653d53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075472`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY dense_rank() OVER (), min(FALSE) FILTER (WHERE TRUE) ASC NULLS FIRST, C
```

---

## Crash 245: `f738ef292faa8237` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075482`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT DISTINCT CURRENT_TIMESTAMP AS a FROM json_each('{"a":{"b":1}}') CROSS JOIN json_tree(TRUE + CASE WHEN NULL THEN
```

---

## Crash 246: `4bb1c7ced1fe0d15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075586`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_DATE) UNION SELECT * FROM p) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 247: `918101c35c138ded` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075593`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_DATE) UNION SELECT TRUE FROM p) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 248: `569901a6de408908` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075626`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_tree(NULL, '$[#-1]') UNION ALL SELECT DISTINCT * FROM p WHERE NULL ORDER BY FALSE ASC NULLS FIR
```

---

## Crash 249: `b614eebd0360e733` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075673`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_tree(CURRENT_DATE BETWEEN FALSE AND NULL, '$[#-1]') UNION ALL SELECT DISTINCT * FROM p WHERE NU
```

---

## Crash 250: `21b8afd3c5346746` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075682`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_tree(NULL, '$[#-1]') UNION ALL SELECT DISTINCT * FROM p WHERE NULL ORDER BY FALSE ASC NULLS FIR
```

---

## Crash 251: `02462b8e45282d0c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075692`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_each(TRUE AND CURRENT_TIME IS NOT FALSE, '$[#-1]') UNION ALL SELECT DISTINCT * FROM p WHERE NUL
```

---

## Crash 252: `7ed52e20716f645a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075727`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT FALSE FROM json_tree(NULL, '$[#-1]') UNION SELECT DISTINCT * FROM p WHERE NULL ORDER BY FALSE ASC NULLS FIRST) 
```

---

## Crash 253: `1e0a09a69ae5b498` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075929`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); SELECT p._rowid_ FROM p JOIN p v08_93__8084 ON NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 254: `a732d846d03dd67e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076963`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) UNION ALL SELECT CURRENT_DATE FROM json_each('[1,2,3]') NATURAL LEFT JOIN json_each('[{"a":1},{"b":2}]')
```

---

## Crash 255: `5a6de8304d2b4832` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077148`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) UNION ALL SELECT TRUE >= NOT CURRENT_DATE <> CURRENT_TIMESTAMP COLLATE NOCASE & ~CURRENT_TIME ISNULL FRO
```

---

## Crash 256: `65826e1965191a63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077162`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) UNION ALL SELECT ~CURRENT_TIME << CURRENT_TIMESTAMP FROM json_each('[{"a":1},{"b":2}]')) SELECT * FROM p
```

---

## Crash 257: `15592aa973a54c47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077178`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (TRUE) UNION ALL SELECT NULL AND CURRENT_DATE FROM json_each('[{"a":1},{"b":2}]')) SELECT * FROM p; CREATE TABL
```

---

## Crash 258: `e538a7bbfb38c671` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077391`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CASE WHEN NULL AND CURRENT_DATE THEN TRUE ELSE FALSE END AS j1kj1_9rd59___s_a_h9_62_f__tg_6o__w9k1_7n1__on___6877____s
```

---

## Crash 259: `583b4bec3a295271` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078772`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL, b TEXT CHECK (CURRENT_TIMESTAMP)); INSERT INTO p (a) VALUES (CURRENT_DATE) ON CONFLICT(rowid) DO UPDATE SET b = CURRENT_DATE; VALUES (CURRENT_TIME); CREAT
```

---

## Crash 260: `58c6261805f9774c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079765`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT count() FILTER (WHERE TRUE AND FALSE) AS wl_0a_70__k1cs44_5_6_acx_; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) U
```

---

## Crash 261: `f4e72e2fa7ac5aef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081940`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT count() FROM p; PRAGMA integrity_check; CREAT
```

---

## Crash 262: `8cdacd75f48b84b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082567`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT OR ABORT INTO p VALUES (-4815055990512251117833168659587790.2); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 263: `9436515fc639a5da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082579`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p DEFAULT VALUES; SELECT group_concat(CURRENT_TIMESTAMP, 'Y-3-9xo _') FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 264: `86a8da862d52731b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082589`

```sql
SELECT substr('', -9223372036854775808, 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 265: `fa485ce423b14163` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085996`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT row_number() OVER () / count() FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP DESC; CREATE TABLE IF NOT EXISTS p(a I
```

---

## Crash 266: `e28ce5d8e1b78048` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086715`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT FALSE FROM json_each('[{"a":1},{"b":2}]') ORDER BY FALSE DESC) SELECT *
```

---

## Crash 267: `0b92e93d0eca511d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086733`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT min(CURRENT_TIMESTAMP COLLATE NOCASE) OVER () FROM json_tree('{}') WHERE NULL UNION ALL VALUES (NULL); CRE
```

---

## Crash 268: `c14c8371747c98f6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087339`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT AL
```

---

## Crash 269: `6593ca662ddba554` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087346`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM json_each(
```

---

## Crash 270: `add15b5b39886d54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087354`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT ' --o5pyh  S '); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CR
```

---

## Crash 271: `699d902ddb76a45c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087367`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (jsonb_each('[1,2,3]')) WHERE RAISE(IGNORE) ORDER BY RAISE(IGNORE) DESC;
```

---

## Crash 272: `0e976c0df3e19d19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087375`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (rowid % FALSE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed
```

---

## Crash 273: `529a9baf57072ef6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087395`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT row_number() OVER () 
```

---

## Crash 274: `523915268552fbf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087403`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT 822763); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TAB
```

---

## Crash 275: `53b737e04031d632` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087410`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, * FROM json_tree('{"a":1}') GROUP BY FALSE ORDER BY CURRENT_DATE, RAISE(IGNO
```

---

## Crash 276: `dfa01dcb3d573d4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087427`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED 
```

---

## Crash 277: `25346813c82d0728` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087439`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT X'f20caccE'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 278: `fdeb80840eafefd9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087445`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE NOT IN (VALUES (CURRENT_DATE) EXCEPT SELECT FALSE FROM json_tree(
```

---

## Crash 279: `0db335b5cfc032b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087451`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', a TEXT CHECK (RAISE(IGNORE) OR TRUE), b INTEGER CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DE
```

---

## Crash 280: `672d0eedd355fa1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087461`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED 
```

---

## Crash 281: `652407e76e95ce52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087557`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'abBf2AF0', c3 INT DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE 
```

---

## Crash 282: `d00d064975035750` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087607`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT INTO p DEFAULT VALUES; VALUES (
```

---

## Crash 283: `1959d7afedbb747b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT INTO p DEFAULT VALUES; SELECT C
```

---

## Crash 284: `1b28624d5534a3aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087633`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL rank() FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE DESC NULLS F
```

---

## Crash 285: `97edfd0b70c65258` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087641`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY rank() OVER (ORDER BY RAISE(IGNORE) ROWS BETWEEN C
```

---

## Crash 286: `bfaf4b287d65ac57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087662`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT INTO p DEFAULT VALUES; SELECT D
```

---

## Crash 287: `12f4241a0c05fa43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087676`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT INTO p DEFAULT VALUES; SELECT *
```

---

## Crash 288: `9a5c10c7169cf8ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087686`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT INTO p VALUES (~CURRENT_DATE) O
```

---

## Crash 289: `786a12b46d3e556a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000087712`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q LEFT OUTER JOIN q USING (c3, _rowid_) ORDER BY FALSE DESC; INSERT OR ABORT INTO p VALUES (FALSE I
```

---
