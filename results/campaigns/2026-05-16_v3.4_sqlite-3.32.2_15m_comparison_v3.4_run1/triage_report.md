# Crash Triage Report

**Total crashes:** 330  
**Unique crash sites:** 330  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 20 | 20 | 6% |
| Signal | 310 | 310 | 93% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `3402df38e7a32a3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000246`

```sql
SELECT printf('%.*g', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CURRENT_DATE FROM json_tree(CURRENT_TIMESTAMP, '$[#-1]') WHERE NOT CURRENT_TIMESTAMP GROUP BY FALSE IS NULL OR
```

---

## Crash 2: `b655d71fd01de029` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000349`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r VALUES (NULL); ANALYZE q; CREATE TABLE IF NOT EXISTS p(b REAL, c1 INT GENERATED ALWAYS AS (CURRENT_TIMESTAMP COLLATE RTRIM COLLAT
```

---

## Crash 3: `0eb6fdb0550b08f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000603`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT t2.* FROM (SELECT FALSE ISNULL / CAST(CURRENT_TIMESTAMP AS VARCHAR(255)) LIKE (TRUE NOT LIKE FALSE = count()) & CURRENT_TIMEST
```

---

## Crash 4: `5d871a93bf6851f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001383`

```sql
SELECT substr('--  5 -q-S2- S- _', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); INSERT OR REPLACE INTO q VALUES (FALSE IS NOT NULL, percent_rank() OVER (PARTITION BY ~CURRE
```

---

## Crash 5: `44d6b7672d23033a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001534`

```sql
SELECT printf('%.*g', 1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, b); INSERT OR ROLLBACK INTO q VALUES (avg(CAST(NULL || NULL COLLATE BINARY IN (SELECT *) COLLATE NOCASE AS 
```

---

## Crash 6: `783e7058f98b2655` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008284`

```sql
SELECT round(-0.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE s AS NOT MATERIALIZED (VALUES (FALSE IS DISTINCT FROM NULL > CAST(TRUE AS BLOB), RAISE(IGNORE)) ORDER BY 
```

---

## Crash 7: `9265f62f216265a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008565`

```sql
SELECT substr('AeD3kEuU6-_-9 7_', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); SELECT *, * FROM jsonb_tree('[1,2,3]') , json_tree('{"a":{"b":1}}') WHERE NOT ~NO
```

---

## Crash 8: `27a88e45ad482d64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012894`

```sql
SELECT substr('____2_-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, c1); SELECT CASE CURRENT_TIMESTAMP WHEN CURRENT_TIME THEN NOT +TRUE ELSE RAISE(IGNORE) EN
```

---

## Crash 9: `07391c81c6b76b51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016001`

```sql
SELECT printf('%.*s', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (NULL);
```

---

## Crash 10: `581becab5030bc65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016011`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT CURRENT_TIME FROM json_tree('{"a":{"b":1}}') WHERE NULL GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 11: `2aa07e361e5a6e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016064`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (NULL);
```

---

## Crash 12: `5ad5bf6ee7e87021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020433`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 13: `d1f3b144f40c3906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020441`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 14: `34db3fc53971de46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020580`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 15: `33e0bbfd0fd8657e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024561`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); SELECT FALSE != FALSE AS p__w9j__b4_07__wql4_ecc1xz_5c_rv__15_4s_ FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 16: `c7af68c21b761c73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043643`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); INSERT OR FAIL INTO p VALUES (CURRENT_DATE > (FALSE), CURRENT_DATE GLOB CASE WHEN CAST(TRUE << CURRENT_TIM
```

---

## Crash 17: `bf162771b6a4ff35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053209`

```sql
SELECT printf('%.*s', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME LIKE RAISE(IGNORE) ESCAPE NULL COLLATE NOCASE GLOB C
```

---

## Crash 18: `56bb4c76b9281982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055930`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); SELECT CURRENT_DATE FROM json_tree('{"a":{"b":1}}') LEFT OUTER JOIN json_tree('{"a":{"b":1}}') LEFT OUTER JOIN p WHERE NULL GROUP BY CURRENT_TIME 
```

---

## Crash 19: `3dd79873b19a16b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073594`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT * FROM p WHERE CURRENT_TIME; SELECT round(1e308, 2147483648); CREATE 
```

---

## Crash 20: `b4ff4474e4d2069d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080906`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT CURRENT_TIMESTAMP AS y92___c_1__64__7s0_dno4rz__3q7_i5qc1_a1c93s70_c__r__s1_sj___t3, CURRENT_DATE AS a_06e347_
```

---

## Crash 21: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001859`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 22: `e146e4b8be7bc1d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001962`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 23: `fd67e2f4b4d67a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002049`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 24: `5ef98da45e076ec9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002105`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 25: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002117`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 26: `f6ff063a2cb42439` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002577`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (FALSE + CAST(+TRUE AS REAL)), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 27: `2734f671433c21f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002585`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 28: `5481f47887e42685` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002597`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE T
```

---

## Crash 29: `d4c99fa681635602` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003438`

```sql
SELECT printf('%s', 2147483648, 'DgNcT37 J_-z_5-'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 30: `e211c4f7f89a63bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003675`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 31: `8b81e55e2678fd61` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003887`

```sql
SELECT printf('%.*g', 9223372036854775807, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 32: `fb7fb12c94d4e43e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004100`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES
```

---

## Crash 33: `702c5b9cb04669b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004151`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_DATE)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 34: `3e7216548e2aaaf2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004296`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TI
```

---

## Crash 35: `41080c36be2b9031` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004388`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN
```

---

## Crash 36: `c2779d3cb3092181` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004394`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 37: `768a9c322b267937` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004507`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 38: `7b0e5205f09e382f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004608`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE FALSE NOTNULL) SELECT q.* FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 39: `0802221df58dd8c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004621`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT q.* FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 40: `b83ba2f7dd58aac4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004634`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (FALSE)) SELECT q.* FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 41: `9ddab8f7205924e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004706`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 42: `6249e1de0cdefcb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004740`

```sql
SELECT substr('L2_ -19jf  M w', 9223372036854775807, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 V
```

---

## Crash 43: `909051eae9654481` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005337`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT 
```

---

## Crash 44: `25f30255e890e84b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005411`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE TABLE IF NOT 
```

---

## Crash 45: `ec8cea9c47ad2af5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005567`

```sql
SELECT substr('_7-nJ  -cvh J_-AM', -2147483649, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_
```

---

## Crash 46: `4db52c0880b42bef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005642`

```sql
SELECT substr('', 2147483648, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 47: `a407663eed6c98ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005725`

```sql
SELECT printf('%.*d', -2147483649, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 48: `aeac308ef3ab71d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005989`

```sql
SELECT printf('%lld', -2147483649, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 49: `4912cf6bd454b070` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006010`

```sql
SELECT round(-1.0, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 50: `b5e2a1ccd45b9b06` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006022`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 51: `40c46fcce1643852` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008673`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (FALSE + TRUE), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREAT
```

---

## Crash 52: `34ad0fad6b03cd48` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008687`

```sql
SELECT printf('%x', -1, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE se
```

---

## Crash 53: `918f934776748a5d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008695`

```sql
SELECT substr('tk', 4294967295, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123)
```

---

## Crash 54: `c858178ce7609429` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008705`

```sql
SELECT printf('%.*d', 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 55: `77cc88185a0ee32e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008712`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 56: `df21469d47f4eb57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008718`

```sql
SELECT substr('', 0, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 57: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008724`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 58: `1ff26b2c63df856d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008730`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE, rowid BLOB NOT NULL DEFAULT CURRENT_TIME, c3 VARCHAR(255) DEFAULT X'CC7Fd8Fa7D0b'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE 
```

---

## Crash 59: `381b820ed78002a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008740`

```sql
SELECT printf('%.*f', 2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 60: `78098d5e542c234f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008746`

```sql
SELECT round(-1.0, 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(
```

---

## Crash 61: `9ab91324fa8851eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008776`

```sql
SELECT printf('%.*e', 0, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 62: `d87d19f8050dfc4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008783`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree(TRUE, '$') WHERE CURRENT_TIMESTAMP) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 63: `6a0f11675accc6b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008795`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 64: `9be4df3029999871` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008801`

```sql
SELECT printf('%.*s', -9223372036854775808, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 65: `84df0847dc19525a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008861`

```sql
SELECT round(-1e308, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 66: `80bc25a54bd93189` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009301`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (NULL) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGE
```

---

## Crash 67: `d2024b8ba50ac27b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013877`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (NULL > CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 68: `70c84f3e89387c26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019224`

```sql
SELECT printf('%lld', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(1
```

---

## Crash 69: `ed39cf0f84a3bd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019231`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (~NULL ISNULL)); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 70: `23421a778b0bdcc5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_TIMESTAMP > CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE see
```

---

## Crash 71: `dfb511c2c2b2d949` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019268`

```sql
SELECT substr('-Qr', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 72: `ea88c29c041b5437` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019277`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 73: `19640c4c211dfe44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019303`

```sql
SELECT substr('wqSb_ Wd_9 7_j_  2', 0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUE
```

---

## Crash 74: `034552ca858adbda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021540`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (X'a2'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO se
```

---

## Crash 75: `2a11e418f283577d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021580`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 76: `b7dc9dde052e5b51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022084`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count(DISTINCT TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 77: `59254a010ff44c05` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022091`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 78: `935606879dff73d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022102`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT FALSE COLLATE RTRIM AS a_06e347_910t20_73_gy_7i6 FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 79: `2c6daa9c919b9006` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022112`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT CURRENT_TIMESTAMP AS y92___c_1__64__7s0_dno4rz__3q7_i5qc1_a1c93s70_c__r__s1_sj___t3 FROM json_each('[{"a":1},{"b":2}]'); CREATE 
```

---

## Crash 80: `6b3b7acf98925763` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022126`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM (json_tree('[{"a":1},{"b":2}]')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 81: `00072636651209f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022136`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); VALUES (NULL) UNION VALUES (TRUE) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 82: `7fcc351380a5d8fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022161`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('[]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 83: `2702fa5877b5d2fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022175`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count(DISTINCT TRUE) NOT LIKE CURRENT_TIMESTAMP < NULL NOT IN (TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p
```

---

## Crash 84: `1f912c9efa05f70f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022258`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('{}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 85: `f07835856400f453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022275`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT DISTINCT * FROM json_each(
```

---

## Crash 86: `e8e3952c19e77526` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT PRIMARY KEY); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_
```

---

## Crash 87: `32a9927fa044631d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT PRIMARY KEY); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 88: `379f9afbb61cb1a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023173`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT CASE CURRENT_TIMESTAMP WHEN TRUE THEN CURRENT_TIME END FROM json_each(NULL, '$[#-1]') JOIN p NOT INDEXED WHERE FALSE; CREATE TABLE
```

---

## Crash 89: `81c75865cf55ccac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023214`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT DISTINCT CASE CURRENT_TIMESTAMP WHEN TRUE THEN CURRENT_TIME END FROM p WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 90: `9bb9c1cb87b9b0d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023519`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL J
```

---

## Crash 91: `44f6342704149ea1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026737`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[1,2,3]') WHERE TRUE) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 92: `f2d5c59ab98bd7cb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026749`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) EXCEPT VALUES (NULL)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 93: `d1deecbe08c661b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026769`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT *, q.* FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 94: `785004d7c0717689` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026776`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT FALSE COLLATE RTRIM AS a_06e347_910t20_73_gy_7i6 FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT * FROM q; CR
```

---

## Crash 95: `6e63951bbaebb8e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026786`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP + NULL OR TRUE || FALSE) SELECT * FROM q; CREATE TABLE
```

---

## Crash 96: `09f918647fa50c14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026793`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE) SELECT * FROM
```

---

## Crash 97: `69f53aed53670acc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026806`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT CURRENT_TIMESTAMP, c1 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]'
```

---

## Crash 98: `02ccbaf34cb00228` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026826`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT *, CURRENT_TIMESTAMP AS a FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT * FROM q; CREATE TABLE seed_t1(c1 I
```

---

## Crash 99: `a4aa2bfb073cfc6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026838`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL NOT BETWEEN TRUE AND NULL) SELECT * FROM q; CREATE TABLE seed_t1(c1
```

---

## Crash 100: `a38df4107ecbcae0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026846`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":{"b":1}}') WHERE TRUE GROUP BY NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 101: `343422d3759f37fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026864`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT NULL, c1 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE)
```

---

## Crash 102: `7c2b2272e6781015` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026873`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME AS a FROM p WHERE CURRENT_TIME NOT LIKE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 103: `21428f86984e4bf2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026896`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, c3 NUMERIC GENERATED ALWAYS AS ((NULL AND TRUE)) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"
```

---

## Crash 104: `8e4e45c837b6e3db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026916`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE 7.011E4356484342751240132020891211242461225539137291871284807) SELECT * 
```

---

## Crash 105: `c3c5bbfb5a5527a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027034`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP + FALSE) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 106: `383135099195f010` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027074`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE) UNION ALL VALUES (NULL)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 107: `d80b19edfc12ce0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027104`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree('{"a":{"b":1}}') WHERE TRUE GROUP BY NULL) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 108: `592f8c551c257daf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027153`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_each(CAST(CURRENT_DATE AS INTEGER), '$[0].c') WHERE NULL) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 109: `3161160da95b17ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027794`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT count(DISTINCT TRUE) NOT LIKE CURRENT_TIMESTAMP < NULL IN (CURRENT_TIME) NOT IN (TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t8
```

---

## Crash 110: `a07d027aa2a9cb77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027815`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_TIMESTAMP)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 111: `5eec80812dfb2a4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027972`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT FALSE NOT LIKE CURRENT_TIMESTAMP < NULL IN (CURRENT_TIME) NOT IN (TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_
```

---

## Crash 112: `5210d204cf7f9855` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027981`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT count(DISTINCT TRUE) NOT LIKE CURRENT_TIMESTAMP AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p WHERE EXISTS (
```

---

## Crash 113: `3a1886c95c36ec8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028386`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM jsonb_tree('{"a":{"b":1}}') INNER JOIN (json_tree('[{"a":1},{"b":2}]')) ORDER BY NULL; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 114: `8bc06ffd7307b896` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028405`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP << NULL ISNULL > CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE I
```

---

## Crash 115: `4fdfc6c326a78a5b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028417`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP == CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (
```

---

## Crash 116: `4b7e551ed4be1227` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028426`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); INSERT OR
```

---

## Crash 117: `b593af93fb67e4e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028436`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT -4283222576047319459117546052653854273000982868804962893907
```

---

## Crash 118: `d990bd2880e621e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028456`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IN (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CUR
```

---

## Crash 119: `a8e5fc1677e36152` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028497`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT_D
```

---

## Crash 120: `6d905b3cf8645b94` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028503`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE count(*) OVER () ORDER BY CURRENT_DATE ASC; EXPLAIN QUERY PLAN VALUES (CURRENT
```

---

## Crash 121: `6983231d2957c816` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028509`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 122: `e7f1ce3fc7606996` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028531`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); A
```

---

## Crash 123: `38e171edf30de1c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028553`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), rowid GENERATED ALWAYS AS (a IS NULL) UNIQUE, c3 NUMERIC NOT NULL D
```

---

## Crash 124: `af6eede7c4b250d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028566`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT '4'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT 
```

---

## Crash 125: `d579a226a18ae0fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028575`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c3 INTEGER, rowid GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR REPLACE INTO p VA
```

---

## Crash 126: `3ae470e83c4e2b6f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028622`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 127: `0786993cc8759d11` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028629`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 128: `e4b761fc77f9809f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028647`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); 
```

---

## Crash 129: `dd4f1c39d6ed253b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028660`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); 
```

---

## Crash 130: `9d69417b68f73107` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028678`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); 
```

---

## Crash 131: `0aba1f511a64f8ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028699`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); 
```

---

## Crash 132: `3699102f3c89c44a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029368`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 133: `c96210e3e7d7c13f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029383`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 134: `171020b9120d71a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029395`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 135: `fdedab85a8df1f20` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029432`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 136: `283b3852b87389ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029462`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 137: `10aba2eff9968789` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029600`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREA
```

---

## Crash 138: `947d862d7ac78979` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029684`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 139: `a17c58b1e3257670` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029698`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 140: `529d28cc2d85411e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029718`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 141: `e91516d36d2456a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029895`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 142: `17df9e52b72cdd2f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030626`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN(
```

---

## Crash 143: `be4cf6c155be8f80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031609`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 144: `5025e13d3232f258` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031625`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 145: `1f3b4fb5cfe55500` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032612`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (NULL IN (VALUES (CURRENT_TIMESTAMP))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 146: `8b750e0383805e2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033071`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURRENT ROW AND UNBOUND
```

---

## Crash 147: `7936e31ccb9446ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033584`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, _rowid_ GENERATED ALWAYS AS (a * a) ); WITH p AS (VALUES (RAISE(IGNORE))) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 148: `90ec9f880004c987` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034134`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE, c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE 
```

---

## Crash 149: `7904b74f5b8b91eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034140`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN CHECK (CURRENT_DATE + CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREA
```

---

## Crash 150: `504e0da003f9ac7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034162`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN CHECK (FALSE + CAST(CASE WHEN TRUE THEN FALSE END AS REAL))); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGM
```

---

## Crash 151: `7632682db07216af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034181`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 152: `8408e4e112c5b3dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034190`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE, c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed
```

---

## Crash 153: `4cc961084da9a52f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034201`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT -42832225760473194591175460526538542730009828688049628939079906253169325887083062789123770365.89601566413896185867937710183047232021725456385373262
```

---

## Crash 154: `ddd73d81b0a2cd4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034266`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT X''); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1
```

---

## Crash 155: `b3eebf9723b4690c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034289`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'eCEDe8fDBc84'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE
```

---

## Crash 156: `1136f110a66627d2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034706`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('{"a":1}') ORDER BY FALSE ASC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 157: `2aecb43858347d99` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039949`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (CURRENT_TIME + CAST(CASE WHEN CURRENT_TIME THEN FALSE END AS REAL)), c2 BLOB UNIQUE); INSERT INTO q D
```

---

## Crash 158: `ff869c501cf8ba7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040193`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (NULL + TRUE), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMES
```

---

## Crash 159: `ddc639a17245751f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041083`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 160: `f29e33c04fcd3589` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042537`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE TRUE = TRUE COLLATE RTRIM GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 161: `c233800fcbced8ef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042555`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, c2 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME / NULL); EXPLAIN QUERY PLAN V
```

---

## Crash 162: `0b6cf13fe8db9e1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042574`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL < last_insert_rowid())); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c
```

---

## Crash 163: `ac0b75d2ee3e7d1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042597`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (TRUE <> CURRENT_TIMESTAMP), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN V
```

---

## Crash 164: `00a46f1283406a57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042605`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, rowid BLOB NOT NULL DEFAULT -941021.958, c3 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES;
```

---

## Crash 165: `3b8eceb1045bc80c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042612`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); VALUES (count(), TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT 
```

---

## Crash 166: `7966e4814958228a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042622`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (~NULL ISNULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c
```

---

## Crash 167: `9d4df2a178744245` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042629`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL IS NOT NULL
```

---

## Crash 168: `0d3a0f0e42600911` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042641`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE - C
```

---

## Crash 169: `b69bf23b25c8cc10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042708`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE, c1 REAL GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES
```

---

## Crash 170: `fa8377d1bc8d8706` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042749`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (TRUE = TRUE COLLATE RTRIM), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES 
```

---

## Crash 171: `a3a765b5300f3dc5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042787`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT DEFAULT 'w_'); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 172: `00da5a5353f01ac7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042796`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (NULL IS NULL COLLATE RTRIM - CURRENT_TIME), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QU
```

---

## Crash 173: `5b8f5f0d2c43328a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042825`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT DEFAULT '4'); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 174: `3a12ed7388bf1ef2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042832`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (-42832225760473194591175460526538542730009828688049628939079906253169325887083062789123770365.8960156
```

---

## Crash 175: `406683551c8698dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042849`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (FALSE NOT BETWEEN CURRENT_TIME AND -CURRENT_DATE OR +json_array_length(TRUE)), c2 BLOB UNIQUE); INSER
```

---

## Crash 176: `d2346645c24e791f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042905`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (TRUE), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE
```

---

## Crash 177: `2242fad1977a4197` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 178: `f2035c55ed5c1ff6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049599`

```sql
SELECT printf('%f', -9223372036854775808, '-3_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 179: `ad1a970ba7d891c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052832`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 180: `6eb5a584f8639f8e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052857`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT -42832225760473194591175460526538542730009828688049628939079906253169325887083062789123770365.89601566413896185867937710183047232021725456385373262
```

---

## Crash 181: `03aa38c3909fbe1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057250`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 182: `100137775373e564` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060076`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT count(DISTINCT TRUE) NOT LIKE CURRENT_TIMESTAMP NOT IN (TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p WHERE 
```

---

## Crash 183: `42e50a9735b12dd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060101`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (-61.666462077282e+860), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FAL
```

---

## Crash 184: `999476abc4bdb0f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060152`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (-0296736380864833594.965), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 185: `9f4084eaa1fbaea4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060162`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM json_tree('{"a":1}')) AS a GROUP BY FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 186: `1311dbc5fd67d9ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060219`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL DEFAULT 247, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREA
```

---

## Crash 187: `3ce026b79a73173e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060329`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB NOT NULL DEFAULT -20964.0472E-6426, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 188: `ec70ba10a2a8ef4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060358`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (CURRENT_TIME IS NOT NULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TAB
```

---

## Crash 189: `f4117a067ddeb46c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061462`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (FALSE || CURRENT_DATE), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE 
```

---

## Crash 190: `a251675b75e1ec19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061698`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT DEFAULT -61.666462077282e+860, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TA
```

---

## Crash 191: `ce07373d5b1fb295` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062207`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 192: `729a3b54023beeb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062217`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXI
```

---

## Crash 193: `61840f8178587bb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062235`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 194: `8dca3e91b96678b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062255`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE (VALUES (N
```

---

## Crash 195: `4feafbe611bb1d03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062263`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 196: `f25579e2cd2b70a4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062294`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (rank() OVER (), FALSE); CREATE TABLE IF
```

---

## Crash 197: `0eee1b8dbaf0e536` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062305`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 198: `969553baca0776b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062317`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 199: `58dea7e8bb4cb4ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062328`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXIS
```

---

## Crash 200: `29d62d9d99c9727e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062415`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, _rowid_ REAL NOT NULL DEFAULT 0); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE 
```

---

## Crash 201: `fa74c6c4b30a35a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063583`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); INSERT OR IGNORE INTO p VALUES (TRUE IS FALSE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b A
```

---

## Crash 202: `adbe307d58290801` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000063820`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (CAST(CURRENT_TIME AS INTEGER)), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (NULL); CREATE 
```

---

## Crash 203: `f0c8a56058865416` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071872`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE I
```

---

## Crash 204: `0fdce15f8f9cd39d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072012`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL FALSE COLLATE RTRIM AS a_06e347_910t20_73_gy_7i6 FROM json_tree('{"a":1}') ORDER BY FALSE ASC NULLS LAST; CREATE T
```

---

## Crash 205: `c59789aae655e974` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072020`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('{"a":1}') ORDER BY FALSE DESC; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 206: `e272234de721a460` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072089`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('[{"a":1},{"b":2}]') INNER JOIN json_each('[1,2,3]') ORDER BY FALSE ASC NULLS LAST; CREATE TABLE 
```

---

## Crash 207: `c3f416947d6bb5e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072100`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('{"a":1}') ORDER BY +CURRENT_TIME DESC NULLS LAST, CURRENT_TIME, CURRENT_TIME DESC; CREATE TABLE 
```

---

## Crash 208: `797ff016a8b7b1b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072109`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT GENERATED ALWAYS AS (FALSE IS NOT c2) VIRTUAL, c2 VARCHAR(255) DEFAULT CURRENT_DATE, c1 NUMERIC NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('{"a":1}'
```

---

## Crash 209: `92d2c260c79a1932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072432`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'eCEDe8fDBc84'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE - CURRENT_TIME); PRAGMA 
```

---

## Crash 210: `5d236cb74162bb22` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072452`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'eCEDe8fDBc84'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE IS FALSE); PRAGMA quick_c
```

---

## Crash 211: `43fe7df0650b9793` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072467`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT -0296736380864833594.965); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CRE
```

---

## Crash 212: `f23e51613ac5428b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072478`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT -1231075165888479427807133672870.6); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_
```

---

## Crash 213: `3e28bfbf41918083` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072484`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT '-E _--P _R-7a_'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABL
```

---

## Crash 214: `fe55a3405fa5866b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072513`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_
```

---

## Crash 215: `5e57c19fd3880673` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072525`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'eCEDe8fDBc84'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(
```

---

## Crash 216: `2e0dffa79d372abb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072582`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'8A7bBBEaFC'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 217: `20e44b26313c8e5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072592`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT -8); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 218: `c32265dfb690d8fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072604`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'eCEDe8fDBc84'); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE
```

---

## Crash 219: `e0bab0a0a4639fb9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072620`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1
```

---

## Crash 220: `66d12cdca22cff1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073193`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP << NULL, TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 221: `d61fe29ad284072c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073199`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (~TRUE IN (VALUES (CURRENT_TIMESTAMP))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 222: `28152fb10e060661` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073208`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (NULL IN (SELECT count(DISTINCT TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr)); CREATE TABLE seed_t1(c1 IN
```

---

## Crash 223: `fcf1827072dc5c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073232`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT * FROM jsonb_tree('[{"a":1},{"b":2}]') INNER JOIN jsonb_tree('{"a":{"b":1}}') U
```

---

## Crash 224: `5a90e2c5d5cfab58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073251`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (NULL IS NULL != CAST(CURRENT_DATE AS NUMERIC) IN (VALUES (CURRENT_TIMESTAMP))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 225: `a0726c5c30d619c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073265`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (-CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER);
```

---

## Crash 226: `4f7b13c5bc484818` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073284`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (NULL IN (VALUES (NULL IS NULL COLLATE RTRIM > CURRENT_DATE))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 227: `a8be51eaf6954ee2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073290`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 228: `b90b6f13c7876328` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073307`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); VALUES (count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOW
```

---

## Crash 229: `3733e8645fb6fcd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073738`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM p WHERE FALSE GROUP BY CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP)) WINDOW w1 AS ())
```

---

## Crash 230: `bf04270502168197` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073774`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a GROUP BY FALSE) AS a GROUP BY FALSE) SE
```

---

## Crash 231: `603cde955ccff777` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073896`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) UNION ALL SELECT * FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS ()) SELECT * FROM q; CREATE TABLE 
```

---

## Crash 232: `3a48390de234697b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075029`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT CURRENT_DATE FROM json_tree('{"a":{"b":1}}') LEFT OUTER JOIN json_tree('{"a":{"b":1}}') NATURAL LEFT JOIN p WHERE NULL GROUP BY CURRENT_TIME
```

---

## Crash 233: `74b570b210569483` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075050`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT DISTINCT FALSE COLLATE RTRIM AS a_06e347_910t20_73_gy_7i6 FROM json_tree('{"a":{"b":1}}') LEFT OUTER JOIN json_tree('{"
```

---

## Crash 234: `1cb272fa523fec04` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075067`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_DATE - FALSE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 235: `aae82af1f2084a41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075078`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (CURRENT_DATE + TRUE), c2 BLOB UNIQUE); WITH RECURSIVE q AS (SELECT DISTINCT p.* FROM json_tree('{"a":
```

---

## Crash 236: `47cd42fc30a0080c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075102`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); WITH RECURSIVE q AS (SELECT DISTINCT p.* FROM json_tree('{"a":{"b":1}}') LEFT OUTER JOIN json_tree('{"a":{"b":1}}') , p) SELECT * FROM q; CREATE TA
```

---

## Crash 237: `2412fdcfc4b2c179` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075111`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (count(DISTINCT FALSE) FILTER (WHERE CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 238: `1b9cc0cefcecf77f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075126`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL, _rowid_ GENERATED ALWAYS AS (c1) UNIQUE, c1 INTEGER PRIMARY KEY); WITH RECURSIVE q AS (SELECT DISTINCT p.* FROM json_tree('{"a":{"b":1}}') LEFT OUTER JOIN json
```

---

## Crash 239: `7a47a917d2818e8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075142`

```sql
SELECT round(-1.0, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3
```

---

## Crash 240: `8aa446420b8166fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076158`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE - CURRENT_TIME); PRAGMA in
```

---

## Crash 241: `99377eb23a571014` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); VALUES (CURRENT_DATE); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((
```

---

## Crash 242: `74ec06ccb172d8a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076584`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (CASE NULL WHEN CURRENT_TIME COLLATE RTRIM THEN TRUE ELSE NULL END IS NOT NULL - FALSE, FALSE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 243: `390eab2c7b6681c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076590`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (X'7e' NOT BETWEEN CURRENT_TIME AND TRUE OR CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 244: `9207a975e58d8c23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076600`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM json_each(CURRENT_DATE - CURRENT_DATE - CURRENT_DATE,
```

---

## Crash 245: `c1644d20928093bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076607`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_object('', NULL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 246: `f44d504de84ec6ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076624`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE IN (CURRENT_TIME) OR CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 247: `190d44d16cd2d488` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076637`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.b[#-1]')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 248: `9696dfcbd83fcf7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076651`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$[0].b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 249: `a34c3e437f211992` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076661`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_each('{}') NATURAL LEFT JOIN p AS tx L
```

---

## Crash 250: `730ec94cf1b55aea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076667`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (CAST(CURRENT_TIME AS BLOB)), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (NULL); CREATE TAB
```

---

## Crash 251: `47d61eb67a34fd42` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076683`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$[#-1]')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 252: `b1b289692c6334bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076696`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB DEFAULT 0, c3 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (json_remove('{"a":{"b":1}}', '$')); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 253: `4876ad1897bc4ed1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076715`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.b.b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 254: `16e159b4cb200b08` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076734`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_patch('{"a":1}', '{}')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t
```

---

## Crash 255: `9e7ca67bf2739207` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076861`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (changes()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INS
```

---

## Crash 256: `b7ca01616ab8bae5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076880`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree(EXISTS (SELECT * FROM json_tree('{"a":1}') WHERE TRUE GROUP BY FALSE HAVING TRUE COLLATE BINA
```

---

## Crash 257: `9575c315e4eb34e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076893`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (random()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSE
```

---

## Crash 258: `f6722f4b7dc4826a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076910`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE + X'7e'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 IN
```

---

## Crash 259: `9a7438dfc3fa51aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076916`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CAST(CURRENT_TIME AS VARCHAR(255))); CREATE TABLE seed
```

---

## Crash 260: `e170a0260954b819` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076928`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE, rowid BLOB NOT NULL DEFAULT CURRENT_TIME, c3 VARCHAR(255) GENERATED ALWAYS AS (CAST(TRUE AS VARCHAR(255))) VIRTUAL); INSERT INTO p DEFAULT VALUES; VALUES (
```

---

## Crash 261: `2a1eab7169cf5706` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076934`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (count(*)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSE
```

---

## Crash 262: `b6755f665b2ca16d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076940`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":1}', '$.b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 263: `66a2b54068d6d399` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076950`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (CURRENT_TIMESTAMP IS NOT TRUE, TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 264: `da957a97e08b1ba4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076956`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree(TRUE, '$[0].b') WHERE FALSE NOTNULL) SELECT q.* FROM q; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 265: `16fb415eb55c38b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076982`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('[1,2,3]', '$.b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 266: `4c787261fc4633d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076991`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT 0.0); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (json_remove('{"a":{"b":1}}', '$.b')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 267: `26033e213cc491fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076998`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE IN (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 268: `6bb86297b1dd9068` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077023`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.a.a')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 269: `bef589cebc7f6df3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077036`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.key')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 270: `965e26db409108b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077080`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (json_remove('{"a":{"b":1}}', '$.a')); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 271: `f037e10184de1ede` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078832`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_che
```

---

## Crash 272: `2dae3383979f7dbe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078957`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p JOIN p nokk_7f_4_3___2w8_ll1_s_2___5w4s_92522n_c80__budtl0fqn_y3940bf5_3_ur_h7_n_i010g_8r__5_9500_e_34p9_p_jp6t_244_k2_64ahzga3l___w_p_i132
```

---

## Crash 273: `25ef1614f521eae0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078968`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 274: `2a2cc06a55bad2f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078976`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 275: `758ba4f8700b0c69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079014`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 276: `c7a0ed06a341453f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079020`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 277: `229e43ce894a7848` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079039`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 278: `41eb9f6683cc4a6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079061`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 279: `36865a75d9f0c18d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079076`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 280: `27f5266d443285a1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079116`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 281: `0c91e82e189a2e69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079181`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 282: `2995af5c0573b9ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079766`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, _rowid_ GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); INSERT 
```

---

## Crash 283: `f19b041a3294f3c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080664`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, _rowid_ GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree('{}') WHERE CURRENT_DATE) SELECT * FROM q; CREATE TABLE IF NOT 
```

---

## Crash 284: `8cfcfb0ae732effd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081236`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT
```

---

## Crash 285: `2586a06ba4e20212` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081259`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT count(DISTINCT TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p WHERE EXISTS (VALUES (rank() OVER (), ran
```

---

## Crash 286: `63afd39f78635c0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081285`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (TRUE), b BOOLEAN CHECK (CURRENT_DATE), c2 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT count(DISTINCT TRUE) AS t__7___26wsz_p_k__x
```

---

## Crash 287: `d57b1e7ce506fb9e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081299`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT count(DISTINCT TRUE) AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p WHERE EXISTS (VALUES (nth_value(CURRENT_T
```

---

## Crash 288: `3682128f34411859` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081363`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT _rowid_ AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE TABLE see
```

---

## Crash 289: `e5ccb27226feefba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081479`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ABORT INTO p VALUES (CURRENT_TIME / FALSE); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 290: `892d903fff0558cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081486`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_DATE NOT NULL)) SELECT * FROM q; CREATE TABLE seed_t1(c1
```

---

## Crash 291: `6d30f03520b19263` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081496`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (TRUE), b BOOLEAN CHECK (CURRENT_DATE), c2 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREA
```

---

## Crash 292: `617ca4db32a13806` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081508`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT_DATE ESC
```

---

## Crash 293: `ba6608753d47ccdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081526`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIMESTAMP OR json_array_length(TRUE))) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 294: `4ff4f7bf53d5107b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081532`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - NULL, CURRE
```

---

## Crash 295: `c8da1973bcc4ba93` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081550`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (TRUE))))) SELECT * FROM q; CREATE TABLE seed_t
```

---

## Crash 296: `85bc3f8ddef60045` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081566`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH q AS (SELECT *) SELECT * FROM jsonb_each('{"a":{"b":1}}') WHERE CURRENT_TIME GROUP BY FALSE, TRUE; WITH RECUR
```

---

## Crash 297: `0c25bca38c94e940` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081580`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_TIMESTAMP)) SELECT TRUE, * FROM q; CREATE TABLE seed_t1(
```

---

## Crash 298: `e8f66fe9d4e8d7e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081586`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE GLOB CURRENT_DATE NOT NULL, CURRENT_TIMESTAMP)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 299: `2c5ca13cb2dced90` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081652`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE NOT NULL NOTNULL ISNULL IS NOT NULL, CURRENT_TIMESTAMP)) SELECT * FROM 
```

---

## Crash 300: `8a5f444f914a2214` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081696`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_TIME LIKE CURRENT_TIME ESCAPE FALSE, CURRENT_TIME LIKE C
```

---

## Crash 301: `efc3dc3fc06a7c51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083531`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_each('{}') NATURAL LEFT JOIN json_tree
```

---

## Crash 302: `4e724f2114d6e22c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083561`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE TRUE GROUP BY CURRENT_DATE - CURRENT_DATE - CURRENT_TIMESTAMP WINDOW w1 AS (); CREATE TABLE seed_t1
```

---

## Crash 303: `2b15007df734d5c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083569`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (percent_rank() OVER ())) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 304: `779b977058c8d6db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083588`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q AS (WITH q AS (VALUES (FALSE)), p (a) AS (VALUES (CURRENT_TIMESTAMP)) VALUES (CURRENT_DATE)) SELECT * FROM q; CREATE TABLE seed_t
```

---

## Crash 305: `faf7c0ceca274d4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083688`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(CURRENT_TIMESTAMP, '$') WHERE CURRENT_TIMESTAMP LIMIT CURRENT_DATE OFFSET NULL; WITH RECURSIVE q AS (V
```

---

## Crash 306: `e74726f6c30acb2d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083696`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN CHECK (CAST(TRUE AS NUMERIC)), c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE 
```

---

## Crash 307: `5df6ef2fdd5f4ef7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083705`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT ALL *, CURRENT_TIMESTAMP AS a FROM json_tree('{"a":1}') ORDER BY FALSE ASC NULLS LAST) SELECT * FROM q; CREATE TABLE
```

---

## Crash 308: `fe37f34eecc572ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083716`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME <= CURRENT_DATE)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 309: `0e08c0e3c69dd408` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083724`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (CURRENT_DATE) EXCEPT VALUES (CAST(FALSE AS REAL) > CURRENT_DATE)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 310: `5dcd5783bb6d659d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083914`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT *, *, *, *, *, * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 311: `f21ba2e391619983` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083922`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT CURRENT_TIMESTAMP + NULL OR TRUE AS a_06e347_910t20_73_gy_7i6 FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT
```

---

## Crash 312: `ad01c2ded1b26ecf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083939`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT sum(CURRENT_DATE) COLLATE RTRIM AS a_06e347_910t20_73_gy_7i6 FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT 
```

---

## Crash 313: `4954093b9926ee55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083951`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT *, *, *, *, *, *, *, *, *, *, *, *, * FROM json_tree('[{"a":1},{"b":2}]') WHERE TRUE) SELECT * FROM q; CREATE TABLE 
```

---

## Crash 314: `a5307355e5f7889a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084081`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP > CURRENT_DATE > CURRENT_DATE > CURRENT_DATE > CURRENT
```

---

## Crash 315: `898a188fc9b51f85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084088`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE json_array_length(TRUE)) SELECT * FROM q; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 316: `674a2895e7927465` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084096`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE
```

---

## Crash 317: `9495cfb34a1f3d96` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084150`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM (VALUES (TRUE)) AS d1__098_8_7____p0x7k8_5z_2r5_8__184_97nf9____1w_0__h_r2_7u6_1f3_e181cb36_t_z__ys_3dy_06_6p
```

---

## Crash 318: `32f4e9bdcd9c90cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084158`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[1,2,3]') JOIN (VALUES (TRUE)) AS d1__098_8_7____p0x7k8_5z_2r5_8__184_97nf9____1w_0__h_r2_7u6_1f3_
```

---

## Crash 319: `45a90b28790e6004` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084291`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); SELECT dense_rank() OVER () AS fi34gr3___216_5__0d_cv4; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 320: `2028734669e400a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084297`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT -1693.1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 321: `6d2e825a6007a43d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084345`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT CURRENT_TIMESTAMP AS y92___c_1__64__7s0_dno4rz__3q7_i5qc1_a1c93s70_c__r__s1_sj___t3 FROM json_tree('{"a":{"b":1}}') 
```

---

## Crash 322: `da4b35fa0a736f03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084483`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL NOT BETWEEN TRUE << TRUE - TRUE - TRUE - TRUE - TRUE - TRUE AND NUL
```

---

## Crash 323: `84dd1a93aaea819a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084511`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL NOT BETWEEN CAST(FALSE AS BLOB) AND NULL) SELECT * FROM q; CREATE T
```

---

## Crash 324: `db51cfe342096f12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084527`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP)) WINDOW w1 AS (); CREA
```

---

## Crash 325: `85fc1e1134ef754f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084613`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE NULL NOT BETWEEN TRUE AND NULL NOT BETWEEN TRUE AND NULL NOT BETWEEN TRU
```

---

## Crash 326: `f9b6255e3157dd03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084680`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 327: `b647dc2502cd0324` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084882`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); VALUES (CURRENT_DATE) UNION ALL SELECT changes() AS t__7___26wsz_p_k__x_904m4_3tt__gq__6_1_t87_25038x07whty_qr; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 328: `0294ea076468d830` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084987`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_each('[1,2,3]') LEFT JOIN p WHERE TRUE) SELECT CURRENT_DATE AS a_06e347_910t20_73_gy_7i6 FROM q; CREATE 
```

---

## Crash 329: `0e2f94177801873b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085032`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH RECURSIVE q AS (SELECT * FROM json_tree(EXISTS (SELECT * FROM json_tree('{"a":1}') WHERE TRUE GROUP BY FALSE HAVING TRUE COLLATE BINARY), '
```

---

## Crash 330: `dbb97aa5d12da840` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085141`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a) , _rowid_ FLOAT PRIMARY KEY); WITH RECURSIVE q AS (SELECT * FROM json_each('[1,2,3]') LEFT JOIN p WHERE TRUE) SELECT * FROM q; CREATE TA
```

---
