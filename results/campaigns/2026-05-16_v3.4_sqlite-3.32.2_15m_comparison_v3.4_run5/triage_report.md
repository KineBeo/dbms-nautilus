# Crash Triage Report

**Total crashes:** 350  
**Unique crash sites:** 350  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 14 | 14 | 4% |
| Signal | 336 | 336 | 96% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `5a86d10c11af12b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000389`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CASE FALSE != +~TRUE WHEN CURRENT_TIME THEN jsonb(FALSE) OVER () END >= CURRENT_TIMESTAMP IS NULL FROM (SELECT TRUE REGEXP NULL AS a FR
```

---

## Crash 2: `232030a9fa8d5563` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000858`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); WITH RECURSIVE p (rowid) AS NOT MATERIALIZED (SELECT r.* FROM jsonb_each('[]') WHERE ((WITH RECURSIVE q (c1, c3, b) AS (SELECT * ORDER BY 
```

---

## Crash 3: `e3346ab8282aff23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000965`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); REPLACE INTO t2 VALUES (jsonb(FALSE NOT NULL) >= NULL NOT NULL NOT BETWEEN CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND CURRENT_TIME
```

---

## Crash 4: `ab7cf2399fccb0d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001628`

```sql
SELECT printf('%.*f', 2147483648, 1e308); SELECT printf('%u', -9223372036854775808, '_U_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO t1 VALUES (EXISTS (VALUES (NULL 
```

---

## Crash 5: `c94f9487b20e8d33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001799`

```sql
SELECT round(0.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIMESTAMP AS a, r.* FROM jsonb_tree('{
```

---

## Crash 6: `467650947d0dd048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008593`

```sql
SELECT printf('%.*f', -2147483648, 1.0); SELECT substr('', 4294967295, 4294967296); SELECT printf('%.*f', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO q DEFAULT V
```

---

## Crash 7: `e29ab00e6ae2a615` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008932`

```sql
SELECT substr('-s5R__ y-V667--', -2147483648, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); SELECT +CURRENT_TIMESTAMP % TRUE MATCH CAST(CURRENT_TIMESTAMP AS BLOB) = (NULL) MATCH RAI
```

---

## Crash 8: `1d5cbeeedd882381` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018559`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c1, c1) VAL
```

---

## Crash 9: `21b918928345d693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019062`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE BETWEEN CURRENT_TIME AND NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 10: `1d05550b319503a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019812`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *;
```

---

## Crash 11: `c1a613ba7b482764` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034227`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE < CURRENT_DATE COLLATE NOC
```

---

## Crash 12: `6f53a98a268a0834` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070081`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED LEFT OUTER 
```

---

## Crash 13: `5f0ac5d65d809271` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075351`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (CURRENT_TIME IS CURRENT_DATE NOTNULL IS NULL)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (NOT EXISTS (SE
```

---

## Crash 14: `ab19e5928b6bd0cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087971`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE V
```

---

## Crash 15: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001881`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 16: `64ae4e760d9067ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001985`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 17: `eeacfde1dc1ddcbb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001991`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 18: `a9bb1e67a612e968` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002173`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER
```

---

## Crash 19: `ce8c168820ca8246` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002303`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 20: `3266b15c2176bb5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002325`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 21: `1e438447c3230ae2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002600`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 22: `bf103cd0548e177c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002618`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO see
```

---

## Crash 23: `08f53db1b4cd7ebc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002624`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 24: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002636`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 25: `b34abac11a345232` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002642`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed
```

---

## Crash 26: `fd67e2f4b4d67a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002796`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 27: `d2f3ad358f582a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004024`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 28: `f897da57b29bf626` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 29: `743037cb6bfc7b35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004040`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_tree(NULL, '$[#-1]')); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 30: `68f4ee9c8b087d36` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004046`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 31: `06a90eabcc797d24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004061`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 32: `9415e0cb8cd5a602` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004079`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 33: `3f1981bf5b77e88e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004842`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 34: `52c6d3bfa3767cd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004888`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL); PRAGMA integrity_check; CREATE T
```

---

## Crash 35: `e8ee7c6a02f3dbc9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005245`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY NULL DESC, CURRENT_DATE DESC; CREATE TABLE seed_t
```

---

## Crash 36: `e5b49d3ef2ad433c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005258`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY NULL ASC; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 37: `81837ad16450b4cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005285`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE FALSE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed
```

---

## Crash 38: `e32eef0d12c19d4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006113`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 39: `9d8302610fe556ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006329`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT p.* FROM q NATURAL JOIN p WHERE CAST(FALSE IS NULL AS INT) <> +TRUE != FALSE & NULL / TRUE
```

---

## Crash 40: `4277ec76fec95fb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006342`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT p.* FROM q NATURAL JOIN p WHERE CAST(FALSE IS NULL AS INT) <> +TRUE != FALSE & NULL / TRUE
```

---

## Crash 41: `d215393f194b7027` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006461`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT) <> CURRENT_TIMESTAMP != FALSE
```

---

## Crash 42: `0a97bf40eb913354` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006468`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP <> CURRENT_TIMESTAMP != FALSE COLLATE NOCA
```

---

## Crash 43: `138d18144ec0030a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006474`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP != FALSE COLLATE NOCASE; CREATE TABLE seed
```

---

## Crash 44: `5b49f7b302c319f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006490`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT) <> TRUE; CREATE TABLE seed_t1
```

---

## Crash 45: `6373be6328d2d3b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006620`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW 
```

---

## Crash 46: `757e219f09127e84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006634`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW 
```

---

## Crash 47: `a3d53cc22976822a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007726`

```sql
SELECT printf('%lli', -2147483648, 'yU '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 48: `f7bba6f15e8cdb99` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008472`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE, c3 FLOAT PRIMARY KEY, c1 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 49: `43981ba6d93dcf0c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008478`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE, c3 FLOAT PRIMARY KEY, c1 BOOLEAN CHECK (-TRUE IS NOT NULL >= TRUE)); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (FALSE); CREATE TABLE seed_t1(c1 IN
```

---

## Crash 50: `ad37571a49a50149` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010488`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY FALSE BETWEEN TRUE AND FALSE WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS FI
```

---

## Crash 51: `a1641103f0eec496` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010504`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c
```

---

## Crash 52: `b58f4affc25e3c79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010533`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 53: `445cb67f4adbf410` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010547`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 54: `f2a6987d20072773` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010568`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE FALSE & CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 55: `9c131c9770279cf8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010582`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (CURRENT_TIMESTAMP IS FALSE)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTA
```

---

## Crash 56: `9821647f8778a6ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010700`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE TA
```

---

## Crash 57: `58b3de44188c2421` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010706`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 IN
```

---

## Crash 58: `27ca7f46bec19c7c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010717`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 
```

---

## Crash 59: `cfb91e2145cf207d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011394`

```sql
SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 60: `c11a65afc78ea5e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011400`

```sql
SELECT printf('%x', -2147483648, 'yU '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 61: `a4048537c2853c41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011411`

```sql
SELECT substr('G__I6 -4-_ _', 2147483647, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),
```

---

## Crash 62: `ffb87761521910a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011418`

```sql
SELECT printf('%f', -2147483648, 'yU '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 63: `e6115c1cf152d932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011430`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 64: `dd871d6b92a6d9ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011436`

```sql
SELECT substr('', 2147483647, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 65: `c46897f5621dd97b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011447`

```sql
SELECT round(0.01, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 66: `50321840c9cd9a0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011454`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (NOT EXISTS (VALUES (NULL))); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 67: `9dc227d2ce45f5e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011468`

```sql
SELECT printf('%.*d', 4294967296, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 68: `1069ffa1f2054b54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011477`

```sql
SELECT substr('_6--s-V ', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREAT
```

---

## Crash 69: `32b590506c3debed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011484`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 70: `7766a6820809757b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011502`

```sql
SELECT printf('%s', -2147483648, 'yU '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 71: `4773cb326546f4f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011508`

```sql
SELECT printf('%.*e', 2147483648, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 72: `a1101cd2b2e2de53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011519`

```sql
SELECT round(-1e308, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 73: `ed848c1c24d65473` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011525`

```sql
SELECT printf('%lli', -9223372036854775808, 'yU '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 74: `45fbb6b465be5a12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011534`

```sql
SELECT substr('_7 -0 1B_l28-4', 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 75: `b4c942a28a464a68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011544`

```sql
SELECT round(-1.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 76: `8f37c2be329c7fb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011550`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 77: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017056`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 78: `233e5a1b8ba43e02` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018035`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p SELECT TRUE; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 79: `22cd084661be8919` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018147`

```sql
SELECT printf('%.*e', 0, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 80: `56f85d9ed456550b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018186`

```sql
SELECT printf('%.*s', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 81: `b9bdf286b6600cee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019997`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 82: `ce0cfcf5342af565` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020685`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 83: `a382e69122325c4c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020740`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 84: `c990a169415d9063` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020746`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 85: `12a81efdba4a413c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020910`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 86: `d475fddec6ae77d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021088`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM jsonb_each('[{"a":1},{"b":2}]') , p INDEXED BY rowid ORDER BY RAISE(IGNORE) ASC NULLS FIRST; I
```

---

## Crash 87: `a4bf2ac520313693` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021096`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME % CURRENT_TIME >> RAISE(IGNORE), NULL, FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 88: `e3922934ac4c7e5d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021107`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (); INSERT INTO p DEF
```

---

## Crash 89: `432677dfa7f680c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021119`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY -FALSE BETWEEN TRUE AND FALSE WINDOW w1 AS (); INSER
```

---

## Crash 90: `5fa4aeca3e5b6ed1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021127`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE) COLLATE RTRIM LIKE CURRENT_TIME ESCAPE CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 91: `fbe5246d2330d8c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021138`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE
```

---

## Crash 92: `c0fa8921b28f292a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021145`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('{}') GROUP BY CURRENT_DATE, RAISE(IGNORE) EXCEPT VALUES (FALSE); INSERT INTO p DEFAULT VALUE
```

---

## Crash 93: `b316ae4e63ad070c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021153`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (CURRENT_DATE IS NOT NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 94: `dbda4fb10c2a706f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021172`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (TRUE BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP IS FALSE); PRAGMA integ
```

---

## Crash 95: `8d885e846a42e350` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021178`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (c1) AS (SELECT count() OVER ()) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 96: `55d057226d3d2a9a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021184`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 97: `c0a15bc66a150c86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021190`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 98: `1611385bb1ce2582` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021206`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p AS m08__10_92318___zfk_6g____4n___trz45s_2_53w_01__6171js_4__k_ GROUP BY CURRENT_DATE EXCEPT VALUES (
```

---

## Crash 99: `08c135b75c77b97e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021212`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') ORDER BY FALSE ASC LIMIT TRUE; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 100: `c0bff22a7b72c36b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021225`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (percent_rank() OVER (ORDER BY CURRENT_DATE DESC ROWS BETWEEN CURRENT ROW AND TRUE FOLLOWING))) SELECT * FROM p; 
```

---

## Crash 101: `62cc125cbcfd27bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021232`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL DEFAULT ' -_o5_M s_'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 102: `162bfdab1256e589` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021249`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA integrit
```

---

## Crash 103: `eabf63237eb6ba2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021255`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (p.b)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 104: `1290bde0a608b9c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021271`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL t2.* FROM p NOT INDEXED CROSS JOIN jsonb_each('[{"a":1},{"b":2}]') , s INDEXED BY c3; INSERT INTO p DEFAUL
```

---

## Crash 105: `b49982667b5154f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021305`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL DEFAULT -0); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 106: `9b40ccb8bc393cd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021343`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)
```

---

## Crash 107: `36ebabcba5d844f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021354`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)
```

---

## Crash 108: `8e8b0d9cca93e3a4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021366`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 109: `36aad0c1555670b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021766`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c
```

---

## Crash 110: `f81f5e355b51c9e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022555`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME <> CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXIST
```

---

## Crash 111: `7e9318efe8165b76` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023009`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); WITH RECURSIVE s AS (SELECT *) SELECT count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE DES
```

---

## Crash 112: `23703ea4c6de0340` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023015`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST RANGE BETWEEN UNB
```

---

## Crash 113: `8eab7e8e07a17e9b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT, c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT) 
```

---

## Crash 114: `4c454a314f473ab3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023033`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC, a NUMERIC NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT
```

---

## Crash 115: `ff0fa2f4723f70c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023040`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME == CURRENT_TIMESTAMP IS NULL; CREATE TABLE seed
```

---

## Crash 116: `3c35503a8eb8c014` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023046`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NOT EXISTS (VALUES (FALSE)) <> CURRENT_TIMESTAMP; CREATE TAB
```

---

## Crash 117: `aed4776adae13750` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023052`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS TEXT) <> CURRENT_TIMESTAMP; CREATE
```

---

## Crash 118: `2b3835037189e39c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023067`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE TRUE - NULL <> CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 119: `11661a3464daa44b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023073`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE COLLATE NOCASE <> CURRENT_TIMESTAMP; CREATE TAB
```

---

## Crash 120: `c5420631d098d4d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023083`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC, a NUMERIC NOT NULL DEFAULT CURRENT_TIME); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT)
```

---

## Crash 121: `52beea758694165a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023089`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(TRUE || CURRENT_TIMESTAMP IS NOT NULL AS INT) <> CURREN
```

---

## Crash 122: `f411518f06f43024` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023096`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE CAST(CURRENT_TIMESTAMP AS INT) <> CURRENT_TIMESTAMP; CREATE 
```

---

## Crash 123: `4dcf12745bd1ed9f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023103`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_TIMESTAMP), c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE C
```

---

## Crash 124: `e40956764bd86985` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023109`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE, _rowid_ BLOB GENERATED ALWAYS AS (0.0 ISNULL) STORED); SELECT * FROM q NATURAL JOIN p WHERE CAST(CUR
```

---

## Crash 125: `4154bad9fefa8016` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023119`

```sql
SELECT printf('%.*g', 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 126: `9facaf8a55273e36` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS DATE) <> CURRENT_TIMESTAMP; CREATE
```

---

## Crash 127: `2406c2c6666ae680` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023137`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE C
```

---

## Crash 128: `4c63b2c81ef37cff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023152`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, _rowid_ REAL UNIQUE, rowid TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIM
```

---

## Crash 129: `1479f6e27d0dbe13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023177`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BET
```

---

## Crash 130: `0b40a114c82666de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023184`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT CURRENT_TIMESTAMP AS s, CURRENT_DATE | CURRENT_TIME AS a FROM q NATURAL JOIN p WHERE CAST(
```

---

## Crash 131: `3ec811ab85d83735` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023239`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT) <> CURRENT_TIMESTAMP; CREATE 
```

---

## Crash 132: `2348f7a72d94e2e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023251`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS FLOAT) <> CURRENT_TIMESTAMP; CREAT
```

---

## Crash 133: `1acea7e5750bc243` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023283`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS INT) <> CAST(CURRENT_TIMESTAMP AS 
```

---

## Crash 134: `7ee8948b7aa8a9d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026086`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT count() AS s, * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 135: `fb1e99982d87d7db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL DEFAULT 12.3674145105659489065850617422810069202935716200176490199249160384472573942644459400646867217902858
```

---

## Crash 136: `c52a622d44884156` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026123`

```sql
SELECT substr('', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 137: `fb160758ecc0398a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026251`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); SELECT count() AS s FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 138: `3d918d4bf87eafb5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026386`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 139: `f7e7f3fb1ed1cdfe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026420`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 140: `639b80c07f30a149` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026431`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE p (c1) AS (VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 141: `215d86618bdc8820` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026584`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 142: `1d9ff126c56775e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026752`

```sql
SELECT printf('%.*e', 2147483648, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 143: `6671038d911d482c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030034`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 144: `bc7adc097911a6e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030103`

```sql
SELECT printf('%.*s', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 145: `4d1626ba1c421f4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030566`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE -50.55E483 <> CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE DESC NULL
```

---

## Crash 146: `5afe21de1b5fc111` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030589`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL NOT IN (VALUES (CURRENT_TIME)) GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE DESC 
```

---

## Crash 147: `c32a8e91779ea287` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030606`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_each('[1,2,3]') WHERE CURRENT_DATE GROUP BY TRUE WINDOW w1 AS (), w2 AS (ORDER BY CURRENT_DATE DESC ROWS BETWEEN UNBOUNDED PR
```

---

## Crash 148: `b19fab7f23997ca9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030758`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY CURRENT_DATE HAVING TRUE WINDOW w1 AS () ORDER BY NULL ASC; CREATE TABLE seed_t
```

---

## Crash 149: `4e49b1c9960db5b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030766`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE DESC, CURRENT_TIME, CURRENT_TIME COLLATE RT
```

---

## Crash 150: `960fa1689656ba8e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030773`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY TRUE, NULL WINDOW w1 AS () ORDER BY NULL ASC; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 151: `bb3bf1718ed0a4b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030779`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY FALSE IN (TRUE) WINDOW w1 AS () ORDER BY NULL ASC; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 152: `47c3bb29c1da8649` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030791`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN _rowid_ PRECEDING AND FALSE FOLLOWING) FRO
```

---

## Crash 153: `cb5d3ab8279ea77f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030804`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM (VALUES (TRUE)) AS c_c_ INNER JOIN json_tree('{}') NATURAL JOIN json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY FALSE WINDOW w1 A
```

---

## Crash 154: `793dee3d5763f3b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030816`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 155: `49c6cec26bb3841e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030827`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY NULL ASC;
```

---

## Crash 156: `1da45246e30523a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030836`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count() AS s; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INT
```

---

## Crash 157: `00e08a118ee329c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030847`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS s, * FROM 
```

---

## Crash 158: `91bce6620770e7c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030994`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIME NOT BETWEEN min(CURRENT_TIMESTAMP) N
```

---

## Crash 159: `6be513fed66cded4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031003`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY min(CURRENT_TIMESTAMP) ASC; CREATE TABLE seed_t1(
```

---

## Crash 160: `e641e89004fad527` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031060`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM 
```

---

## Crash 161: `172fa991e03543d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033933`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (''); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 162: `31cb761508985940` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033949`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 163: `8538c8347afc0e1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033957`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); WITH RECURSIVE s AS (SELECT *) SELECT CURRENT_TIMESTAMP AS s, NOT EXISTS (VALUES (CURRENT_DATE)) AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 164: `c7703b7b22ee9ca0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033967`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123
```

---

## Crash 165: `0471a91fef622df1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033997`

```sql
SELECT substr('0_i __j2-0T t', -1, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44)
```

---

## Crash 166: `3ae17d38708a57d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034006`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count() FILTER (WHERE NULL) OVER () AS s FROM json_tree('{"a":1}') ORDER BY NULL DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 167: `b3e0bfb21beb7f83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034016`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_tree('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 168: `2a7297ac7a973bad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034024`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIMESTAMP DE
```

---

## Crash 169: `de91de44d5e35017` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034640`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE < CURRENT_DATE); PRAGMA qu
```

---

## Crash 170: `a2433e15013fc4d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035813`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY TRUE, NULL WINDOW w1 AS () ORDER BY NULL DESC NULLS LAST, TRUE; CREATE TABLE s
```

---

## Crash 171: `f755dcd5c98ea2d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036260`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT
```

---

## Crash 172: `393f557ef8ecf172` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037166`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE) UNION ALL VALUES (CURRENT_TIME) UNION VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 173: `7e073c886df51eaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037672`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree(CURRENT_TIMESTAMP, '$[#-1]') LEFT OUTER JOIN json_each('{"a":{"b":1}}') ON CURRENT_TIMESTAMP WHERE NULL GROUP BY FALSE W
```

---

## Crash 174: `e75de03da6fde6ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039334`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM t1 AS n71987_1l_vu_m3i__v WHERE CURRENT_TIMESTAMP; INSERT INTO p SELECT TRUE; PRAGMA int
```

---

## Crash 175: `e908121e55ae072e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039592`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 176: `aca10e37a3588767` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039760`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM p NOT INDEXED); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 177: `312163ff8c57c170` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039770`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL FALSE / count() AS s, CURRENT_DATE | CURRENT_TIME AS a FROM json
```

---

## Crash 178: `082584af243a68ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039780`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL FALSE / count() AS s FROM json_tree(NULL, '$[#-1]')); CREATE TAB
```

---

## Crash 179: `00e99fccd251ee86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039787`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UNB
```

---

## Crash 180: `f9d8b8a077fd28e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039799`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') JOIN p NOT INDEXED ON CUR
```

---

## Crash 181: `85deaa1bec13c2c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039809`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM (VALUES (TRUE)) AS c_c_ INNER JOIN q NATURAL JOIN json_tr
```

---

## Crash 182: `6085723ba46598c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039815`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT FALSE / count() AS s FROM q WHERE EXISTS (SELECT ALL * FROM json_tree(NULL, '$[#-1]')); CREATE TAB
```

---

## Crash 183: `96bb00e7f681a8ce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED LEFT OUTER JOIN json_tree('[{"a":1},{"
```

---

## Crash 184: `009d27d40f0acace` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039842`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT X'07Cdecea'); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_tree(NULL, '$[#-1]')); CREATE TABLE seed_
```

---

## Crash 185: `901e0c401f264543` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039848`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT count() FILTER (WHERE NULL) OVER () AS s, * FROM json_tree('{"a":1}'
```

---

## Crash 186: `5988b31e46cd777b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039869`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL DEFAULT 0223656679770848608759699700279425912322737331964540368109.6); INSERT INTO q DEFAULT VALUES; PR
```

---

## Crash 187: `a0832ad06d2d41c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039878`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_tree(NULL, '$[#-1]')); CREATE TABLE seed_t1(c1
```

---

## Crash 188: `366b54480dfc3492` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039884`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p AS m08__10_92318___zfk_6g____4n___
```

---

## Crash 189: `5b69763201f359c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039897`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_tree(NOT EXISTS (SELECT * FROM json_each('{"a":{"b":
```

---

## Crash 190: `dbe2c7697a8287d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039905`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 191: `3d8e6d53de5f1472` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040007`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 192: `709e02eb446e9c2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040050`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 193: `449b484dbd9a23a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040057`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY -CURRENT_DATE DESC NU
```

---

## Crash 194: `14c7592b9879bc79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 195: `15ee958bc278da67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040076`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY RAISE(IGNORE) DESC NU
```

---

## Crash 196: `e8666f3dfb7b69db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040095`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 197: `e3e65bacb1742cf7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 198: `c563e2721170001c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040126`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT TRUE, b REAL UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CU
```

---

## Crash 199: `6368af9c3e691ac5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040143`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM (VALUES (TRUE)) AS c_c_ INNER JOIN json_tree('{}') NATURA
```

---

## Crash 200: `2e9ef7dcd9fbf23a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040150`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 201: `569342b62a76f5b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040162`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 202: `16bda47d1e7f5b8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040278`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 203: `d83ff6b15cc39df2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040312`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 204: `d516585f43770131` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040398`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 205: `57d92fc1e1cc71bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040407`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 206: `ec76d8d4e2b2a8f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040538`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 207: `7b17ed37172e8fef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040565`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 208: `b37115306a4531c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047615`

```sql
SELECT printf('%.*g', -2147483648); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE T
```

---

## Crash 209: `e52b2e9d763aca97` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050566`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (TRUE > FALSE) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 210: `d6abf450919c0b52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050603`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT VALUES (count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 211: `2fcb34643ac8872d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050620`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_TIMESTAMP), c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') WHERE row_number() FILTER 
```

---

## Crash 212: `2d092d222854a6ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050675`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) EXCEPT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 213: `751d7c4a0c948a12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050745`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT ~CURRENT_TIME AS a UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 214: `6098eff35b8b4d7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050760`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE BETWEEN TRUE AND CAST(CURRENT_TIMESTAMP AS FLOAT) <> TRUE AS a UNION ALL VALUES (CURRENT_DATE); CRE
```

---

## Crash 215: `0c390de3c1ce8350` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050773`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (NULL IS NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 216: `a98f5d76a6505ec3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050780`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CAST(CURRENT_TIMESTAMP AS INT)); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 217: `006566b9f882b8cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050820`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE | CURRENT_DATE AS a UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 218: `dc311c1e5650a202` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050826`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) UNION VALUES (FALSE) INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 219: `34211f2808281baa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050840`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME IS TRUE - CURRENT_TIMESTAMP IS FALSE IS FALSE IS CURRENT_TIME IS CURRENT_TIMESTAMP) INTERSECT SELECT CURRENT_TIME AS a UNIO
```

---

## Crash 220: `f80d17c64b92d03d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050846`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN GENERATED ALWAYS AS (NULL) VIRTUAL, c1 BOOLEAN CHECK (NULL), c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIME) INTE
```

---

## Crash 221: `a4b67f24b9eba552` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050854`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_DATE COLLATE BINARY BETWEEN CURRENT_TIMESTAMP AND TRUE) INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CURRENT_DATE); CREA
```

---

## Crash 222: `e19b34e1463d97ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050865`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT X'07Cdecea', b REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CURRENT_D
```

---

## Crash 223: `7f1cec11afef6189` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050975`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE IS FALSE IS FALSE IS CURRENT_TIME IS CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 224: `43aa95d583c7ceff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050998`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (NULL IS FALSE IS CURRENT_TIME IS CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 225: `b6f566d0971a8784` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051019`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE FROM json_each('{}') GROUP BY CURRENT_DATE UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1
```

---

## Crash 226: `60a9afb5c47a70b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051246`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM json_tree('[1,2,3]') GROUP BY FALSE HAVING FALSE LIKE FALSE ESCAPE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 227: `e178e5ac9d85e216` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051786`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NUL
```

---

## Crash 228: `e0e81254305ba9cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051792`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE NOTNULL); PRAGMA quick_check; CREATE TABLE see
```

---

## Crash 229: `9557c36715a6d2cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051803`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]') NATURAL LEFT JOIN json_tree
```

---

## Crash 230: `83cc6988843df598` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051817`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL NOT LIKE CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 231: `c675b13777d412c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051849`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE s AS (SELECT *) SELECT count() FILTER (WHERE NULL) OVER (ORDER BY 
```

---

## Crash 232: `fb3d36068c47a2dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053380`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 233: `435335040bc1e677` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053439`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 234: `fe9e97aef8288cb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053512`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 235: `f54543008b234148` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054183`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 236: `6b535c5af7d182dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056105`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); SELECT DISTINCT FALSE AS y4 FROM p WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 237: `28f7c6098c8986e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056173`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 238: `ce7a899c3e527a49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056639`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM r INTERSECT SELECT DISTINCT * FROM json_each(TRUE, '$[#-1]') ORDER BY RAISE(IGNORE) ASC; INSE
```

---

## Crash 239: `6891bb44c4d46a47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057912`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY, rowid BOOLEAN, c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 240: `6107cb2130079ad6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060688`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree(CURRENT_TIMESTAMP IS NULL, '$[#-1]') ORDER BY NULL DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 241: `cd19ba8779ebdcd5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060694`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, _rowid_ BLOB GENERATED ALWAYS AS (0.0 ISNULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREA
```

---

## Crash 242: `02401b02cb05ff92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060720`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_TIMESTAMP), c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE
```

---

## Crash 243: `b1138dd61265f6f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060728`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE) IN (CURRENT_DATE, 0), CURRENT_TIME); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE s
```

---

## Crash 244: `99e02b042bb21f0f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060737`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP NOT IN (RAISE(IGNORE))); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c
```

---

## Crash 245: `bae9173873a867b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060745`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('{}') LEFT OUTER JOIN (json_tree('[{"a":1},{"b":2}]') NATURAL LEFT JOIN json_tree
```

---

## Crash 246: `9ec0ec93e1e02761` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060754`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT X'07Cdecea', b REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 247: `53c70a77ee46bcb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060774`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) UNION ALL SELECT count() OVER () ORDER BY TRUE DESC NULLS LAST, CURRENT_TIMESTAMP DESC NULLS FIRST,
```

---

## Crash 248: `068113a51bfba852` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060791`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('{"a":1}') ORDER BY CURRENT_TIME COLLATE RTRIM; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 249: `bb5cb618240d1af5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060800`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (NOT EXISTS (SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GR
```

---

## Crash 250: `62c329323853df28` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060883`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREA
```

---

## Crash 251: `2da3a02308c4c038` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060891`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREA
```

---

## Crash 252: `1439f5ab6eb21ba2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060897`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREA
```

---

## Crash 253: `3ac29ede761fc0e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060996`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT FALSE, b REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 254: `255c50ee55ad92c3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061012`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_TIMESTAMP), c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_chec
```

---

## Crash 255: `4e245f5859963b03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061070`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 256: `2d69546151d79abd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063615`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 257: `42deba4b14aff4cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063622`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 258: `45b6da06c9794c52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063650`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME)), RAISE(IGNORE)); INSERT OR 
```

---

## Crash 259: `8da9f3f7311d6642` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063664`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH q (c3) AS (SELECT *), r AS (SELECT *) INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integ
```

---

## Crash 260: `d72369c9b5c6238f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063684`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 261: `c9000939c3ea638f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063701`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, _rowid_ BLOB GENERATED ALWAYS AS (0.0 ISNULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TR
```

---

## Crash 262: `61c2ec4c9a317fd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063716`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, a FLOAT GENERATED ALWAYS AS (NULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check
```

---

## Crash 263: `3babb2b9eb660868` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063792`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 264: `38c962e1e20a890a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063856`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC
```

---

## Crash 265: `cb61e5d637a5589f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063900`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (X'') ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 266: `e2f3d1fc0438bd50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064062`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (X'') ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 267: `479c787b587b2abd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064079`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE T
```

---

## Crash 268: `a5b005d9b33db675` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064089`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (X'') ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 269: `e06aafcf1f22776a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067501`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT 71681576372339627375.715599571671); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE p (c1) AS (VALUES (percent_rank() OVER (ORDER BY C
```

---

## Crash 270: `6d9798bce7cb2b19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067550`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR FAIL INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 271: `4ffae923a17927a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067561`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT 71681576372339627375.715599571671); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM json_each('{"a":1}') WHERE CURRENT_TIMESTAMP; CREAT
```

---

## Crash 272: `cf47fc75d06fc9a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067570`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT 71681576372339627375.715599571671); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE FALSE; CREATE T
```

---

## Crash 273: `67ed8088f9074dc0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067577`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT 71681576372339627375.715599571671); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE p AS (SELECT * FROM json_each('[{"a":1},{"b":2}]')
```

---

## Crash 274: `d6e5a3e9f814911e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067585`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT 71681576372339627375.715599571671); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT DISTINCT * FROM json_each('[]') WHERE CURRENT_TIME; CREATE
```

---

## Crash 275: `389afec02aef40a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068070`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT FALSE / TRUE AS s INTERSECT SELECT CURRENT_TIME AS a UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 276: `91ecc1632974c56f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068244`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE FROM json_each('{}') GROUP BY CURRENT_DATE, FALSE LIKE FALSE ESCAPE FALSE UNION ALL VALUES (CURRENT
```

---

## Crash 277: `4381ccdb00be1fa5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068270`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE FROM json_each('{}') GROUP BY -FALSE BETWEEN TRUE AND FALSE UNION ALL VALUES (CURRENT_DATE); CREATE
```

---

## Crash 278: `f1a3c18ca980b027` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068436`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT SELECT FALSE FROM json_tree('{}') LEFT OUTER JOIN (json_tree('[{"a":1},{"b":2}]') NATURAL LEFT JOIN json_tree('[
```

---

## Crash 279: `070d4161a2568e95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068470`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_TIME) UNION ALL SELECT FALSE FROM json_each('{}') GROUP BY CURRENT_DATE UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1
```

---

## Crash 280: `32cf495e4dc24724` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068500`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT -67.70372971598910019911299E-356636667895); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (FALSE IS FALSE IS FALSE) INTERSECT VALUES (TRUE); C
```

---

## Crash 281: `e462c0ee00e3f30c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068510`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (X'4aa47CdAbEE7aE') INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 282: `658cbec7483de7e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068526`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE IS NULL % CURRENT_DATE IS FALSE) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 283: `768510905a9dee26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068546`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (min(CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 284: `1ba0a942d77f3873` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068557`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE IS FALSE IS -50.55E483) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 285: `1caabe67d9d125ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068565`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE IS FALSE IS TRUE - FALSE) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 286: `75817f8665fe29bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068586`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_DATE COLLATE BINARY IS FALSE) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 287: `c63e9f60e1da004e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068701`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS F
```

---

## Crash 288: `0a9782e70d7ec397` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068730`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (-50.55E483) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 289: `893e40c9c75e2a04` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069961`

```sql
SELECT substr('f6_-', -9223372036854775808, 4294967296); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (X'') ON CONFL
```

---

## Crash 290: `30abee6643c9d4c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075927`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (NULL NOT LIKE FALSE)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE TABLE IF NOT EXI
```

---

## Crash 291: `211b04b5683ef000` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076143`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (TRUE IS NOT CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE TABLE 
```

---

## Crash 292: `2f88327e9b86a235` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079790`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 293: `a6bfdf657a18ff8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079994`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 294: `41d957d32ffa8d0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080008`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM json_tree('{"a":1}') ORDER BY TRUE DESC NULLS LAST, CURRENT_TIMESTAMP DESC NULLS FIRST, FAL
```

---

## Crash 295: `600cb33f35ae8ec2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080025`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (ORDER BY CURRENT_DATE DESC ROWS BETWEEN UNBOUNDED 
```

---

## Crash 296: `ec5678bfb06f9216` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080041`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT dense_rank() OVER (), * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY
```

---

## Crash 297: `54ab89a962980d64` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080058`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP / CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 298: `e06ffc5ba1ddcd15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080071`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY count(DISTINCT TRUE) 
```

---

## Crash 299: `874626d097077c41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080158`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE 
```

---

## Crash 300: `541c8b259f94f374` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080191`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 301: `c83edb5365991fed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080272`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 302: `26f67adbd745b5d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080308`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 303: `c1b8985669f2c579` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080321`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 304: `3e7ebb0e7eab01e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080467`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BLOB DEFAULT -55.155, c1 INTEGER PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') 
```

---

## Crash 305: `15f759cf38c077b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080474`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_TIME FROM json_tree('[{"a":1},{"b":2}]') UNION ALL VALUES (C
```

---

## Crash 306: `5b3bd1910513fdd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080492`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE >> CURRENT_DATE GROUP BY NULL WINDOW w1 AS () ORD
```

---

## Crash 307: `7aa1ce02dad1ab18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080504`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 308: `50033984eb224f65` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080542`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL row_number() OVER () FROM json_each('{"a":{"b":1}}') ORDER BY CU
```

---

## Crash 309: `5f02ff75ab739850` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080552`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NUL
```

---

## Crash 310: `79a167213ffaa98f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080761`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT DISTINCT *, *, *, * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 311: `24c99dc823e52536` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080902`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT *, count() OVER (), * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDE
```

---

## Crash 312: `ff08e04df50995fd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080908`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 313: `5833e09b1720a9f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080915`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 314: `a857f50e8b8cdfda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080931`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_DATE IS NOT NULL >= ~count(DISTINCT NULL) FILTER (WHERE TRU
```

---

## Crash 315: `8cfd108a878eec31` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080939`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER DEFAULT '-  s 0Vr  _x6-6M -k', b REAL UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION B
```

---

## Crash 316: `b550928fa780378c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080945`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 317: `9922f35da1141afd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080959`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN GENERATED ALWAYS AS (NULL) VIRTUAL, c1 BOOLEAN CHECK (NULL), c2 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS
```

---

## Crash 318: `770125cc329d00e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080974`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY NULL NOT IN (VA
```

---

## Crash 319: `1ec427ee49ff8d7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081080`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 320: `15eb66285e4e94fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081105`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTA
```

---

## Crash 321: `d52a64498cd4e24e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081147`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (PARTITION BY CURRENT_TIME ORDER BY count() ASC NUL
```

---

## Crash 322: `21f1f5563a5846a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081194`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL count() OVER (), FALSE / count() AS s FROM q); CREATE TABLE seed
```

---

## Crash 323: `787e43d55e819bfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081200`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT ALL FALSE / count() AS s FROM q); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 324: `c118c75debab1b7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081462`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT DISTINCT * FROM p NOT INDEXED; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 325: `46d324fecd2b4b28` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081475`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); SELECT count() FILTER (WHERE NULL) OVER () AS s, * FROM json_tree('{"a":1}'); CREATE TABLE seed_a(c UNIQU
```

---

## Crash 326: `355cd61deb7cad33` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081497`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 327: `be7df2906ff8e301` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081503`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE EXCEPT VALUES (FALSE); CREATE TABLE seed_a(c UN
```

---

## Crash 328: `008c937525c6b021` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081513`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 329: `9a7f9bc86077317a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081524`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 330: `cd2040438138f74b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081534`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 331: `6fa0ea495597993a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081557`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 332: `5e75665bff8eb7cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081567`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 333: `2b1a08b7c3693944` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081801`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, rowid TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM t1 AS n71987_1l_vu_m3i__v WHERE CURRENT_TIMESTAMP; INSERT INTO p 
```

---

## Crash 334: `27c4f47dc202ee1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081834`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM t1 AS n71987_1l_vu_m3i__v WHERE CURRENT_TIMESTAMP; INSERT OR ABORT INTO p VALUES (FALSE 
```

---

## Crash 335: `d0a9f5b277d33d03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081849`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, a FLOAT GENERATED ALWAYS AS (NULL >= FALSE) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM t1 AS n71987_1l_vu_m3i__v WHERE CURRENT_TIMES
```

---

## Crash 336: `bd7f056cad67c979` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083448`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_DATE + count() ASC NULLS FIRST, TRUE; CRE
```

---

## Crash 337: `f11f0679fed49cdf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083471`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT NULL AS a FROM q NOT INDEXED LEFT O
```

---

## Crash 338: `1ef04cb3f5455949` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084397`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT '9  '); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNI
```

---

## Crash 339: `d1c53dd650fdb944` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084411`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (NULL >= FALSE), b VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1
```

---

## Crash 340: `a1941faf3fc62331` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084436`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree(CURREN
```

---

## Crash 341: `bf031b1a18b6e60a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084442`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT X'5c8F93da'); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NO
```

---

## Crash 342: `cc81ba3dc71d36bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084449`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_DATE DESC NULLS LAST LIMIT CURRENT_TIMESTAMP OFFSET FALSE & T
```

---

## Crash 343: `984429708f2ceded` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084582`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL T
```

---

## Crash 344: `0832d509b651b972` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084633`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); EXPLAIN QUERY PLAN VALUES (FALSE, CURRENT_TIMES
```

---

## Crash 345: `088e01aa49d3e09c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088043`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM p NOT INDEXED; PRAGMA qu
```

---

## Crash 346: `be313c864051eddd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088439`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (X'4aa47CdAbEE7aE' BETWEEN CURRENT_TIME AND NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 347: `7e5bfb18056fecda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088454`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 348: `46a966e37c4fa52f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088460`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); VALUES (FALSE) INTERSECT VALUES (percent_rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 349: `fb00ea00c62361b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088467`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER CHECK (RAISE(IGNORE) OR TRUE)); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 350: `7ca4b8bd6b99d4f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000088495`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM json_tree('[1,2,3]') ORDER BY NULL DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---
