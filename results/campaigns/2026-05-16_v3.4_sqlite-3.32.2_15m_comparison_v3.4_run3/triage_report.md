# Crash Triage Report

**Total crashes:** 243  
**Unique crash sites:** 243  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 5 | 5 | 2% |
| Signal | 238 | 238 | 97% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `4ecb3a542ca3aa41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000268`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT p.* FROM json_tree('[{"a":1},{"b":2}]') LEFT JOIN r INDEXED BY b ON NOT CASE FALSE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME ELSE CURRENT
```

---

## Crash 2: `11d1dea15b2267bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000576`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT q.* FROM t1 WHERE EXISTS (SELECT ran
```

---

## Crash 3: `11e66d362f1aa4fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001163`

```sql
SELECT round(1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO p VALUES ((CURRENT_DATE) COLLATE RTRIM IS NOT +CURRENT_TIME IS NOT ~CURRENT_TIMESTAMP == 
```

---

## Crash 4: `5f0633d976967cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001796`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, _rowid_); SELECT q.*, (TRUE) LIKE CASE WHEN FALSE THEN -CURRENT_DATE + NULL > CURRENT_DATE = TRUE ELSE CURRENT_DATE COLLATE RTRIM E
```

---

## Crash 5: `64d3773c251a19cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008509`

```sql
SELECT printf('%x', 2147483647, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT q.*, t2.* FROM p INDEXED BY a GROUP BY CASE TRUE NOT NULL WHEN CURRENT_TIME THE
```

---

## Crash 6: `c1dda7b5e068952c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000000227`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 7: `11a8afd5cd872b86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003400`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 8: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003530`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 9: `7d3dbcddf7493779` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003538`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 10: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003556`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 11: `7fed3becf13ed97e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003762`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 12: `fd67e2f4b4d67a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003772`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 13: `446bbf6e36362ae2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003781`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 IN
```

---

## Crash 14: `3a4969a081893930` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 15: `cc7ccd63d104c2be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003964`

```sql
SELECT printf('%.*f', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 16: `293d2868dda45ece` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003972`

```sql
SELECT printf('%.*f', 2147483647); SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(
```

---

## Crash 17: `527e1793956a2aa7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004026`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 18: `352aa11c9ca18bbd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004946`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 19: `b26065e7e11e8250` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005363`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 20: `fb67b7ece44f9cdd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005409`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 21: `7b00aa7a828aa574` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005455`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 22: `57be96c15380582a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006468`

```sql
SELECT printf('%.*s', 1, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 23: `d76ec25c9198ef18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006478`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 24: `e5e8c298913e0a68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006635`

```sql
SELECT printf('%llu', 2147483647, 'k -_ 5-h2zH--_-_g0s'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44
```

---

## Crash 25: `c8a8b130877260e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006649`

```sql
SELECT substr('-f G_T62-j_bz--b3', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(12
```

---

## Crash 26: `a53778376b1a3096` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006803`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT FALSE AS a FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 27: `6622fbc466b30fc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007384`

```sql
SELECT printf('%.*g', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 28: `977b30e43e92efce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007426`

```sql
SELECT substr('- 32gq--7M', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 29: `83df2e41e211e035` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007732`

```sql
SELECT printf('%.*e', 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 30: `d6ae11042b034977` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008989`

```sql
SELECT printf('%.*f', 2147483648, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 31: `b28c77ee4907decb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016210`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 32: `e75ae6986f1b18cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016315`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 FLOAT GENERATED ALWAYS AS (FALSE GLOB NULL < FALSE) VIRTUAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 33: `143792dc85447af2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016647`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL CURRENT_TIMESTAMP, lag(CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME, FALSE), FALSE AS z_ FROM json_tree('{"a":{"b":1}}'); CREATE TAB
```

---

## Crash 34: `d00c0e7a8c90034c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016716`

```sql
SELECT substr('X- - __z_ ', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(
```

---

## Crash 35: `067979de7c6e0cfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017072`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 36: `5056b667a04721a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018537`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, c3 INT NOT NULL DEFAULT '-'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_t
```

---

## Crash 37: `9231862a454e434f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018824`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, c3 INT NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed
```

---

## Crash 38: `876239207075a882` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018842`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, c3 INT NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TAB
```

---

## Crash 39: `5963f0df62870052` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019602`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL percent_rank() OVER (), * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 40: `6ebea3693ead00c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019725`

```sql
SELECT printf('%.*d', -9223372036854775808, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 41: `f82759cc52802ab9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019924`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, c3 INT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE 
```

---

## Crash 42: `0b2e32e138234ee8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019933`

```sql
SELECT printf('%.*s', 1, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 43: `20a311ed0d31f7b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019940`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT FALSE, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT * FROM p JOIN q s_ ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 44: `8e07571e18633ead` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019949`

```sql
SELECT printf('%.*s', 0, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 45: `bc7adc097911a6e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019955`

```sql
SELECT printf('%.*s', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 46: `8699d79c7f60a98f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019964`

```sql
SELECT substr(' 1 6FMt-', 0, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 47: `85b65d38988af95d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019970`

```sql
SELECT printf('%.*f', 1, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 48: `a63b2fe267313700` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019976`

```sql
SELECT round(1e308, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 49: `35dcf2339fa1660d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019994`

```sql
SELECT round(-1.0, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 50: `76c5666b0e966a47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020005`

```sql
SELECT printf('%.*s', 1, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 51: `de3a68da45de7401` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020011`

```sql
SELECT printf('%d', -9223372036854775808, '-'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(12
```

---

## Crash 52: `1b13550c4466801b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020017`

```sql
SELECT printf('%f', 1, 'w__i8_n---_-2-d__w'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123)
```

---

## Crash 53: `6356ca26d369a4c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020033`

```sql
SELECT substr('', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 54: `5fe30a13eecd3b42` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020043`

```sql
SELECT substr('dz_XB4H_4', -9223372036854775808, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUE
```

---

## Crash 55: `8bdf25dae7a7ca58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023230`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 56: `540d7f48b882a7d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023244`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL CURRENT_TIME IS NOT TRUE, * FROM json_each('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 57: `2f365e9f37aa7596` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023544`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW
```

---

## Crash 58: `903c5c3579fa0b7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023554`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW
```

---

## Crash 59: `6915084e24b7e98d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024318`

```sql
SELECT printf('%.*g', -2147483648, -0.0); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE);
```

---

## Crash 60: `dc5b1d5532361cdf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027548`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 61: `84c6efcbfce2a80e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027556`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(NULL NOT IN (VALUES (CURRENT_TIMESTAMP
```

---

## Crash 62: `0f5e97211e52ee47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027562`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(NULL NOT IN (VALUES (CURRENT_TIMESTAMP
```

---

## Crash 63: `515bb2b93d65b801` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027572`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 64: `c46cc09c53abfee9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027580`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , p LEFT OUTER JOIN json_tree('[]'); CREATE TABLE 
```

---

## Crash 65: `5919d3f1e5851a83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027653`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 66: `e69eee214af6d665` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027708`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 67: `6bbc3e84efc4f711` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027809`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 68: `29dc5027ca5a2a66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027823`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(NULL NOT IN (VALUES (CURRENT_DATE) UNI
```

---

## Crash 69: `73d084811c1715cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027829`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CASE WHEN TRUE THEN CURRENT_TIMESTAMP END GLOB CURRENT_TIME AS v___
```

---

## Crash 70: `eb0b1da4c8e633d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027835`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(CASE WHEN TRUE THEN CURRENT_TIMESTAMP 
```

---

## Crash 71: `fdfa784924e411a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027842`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(NULL NOT IN (VALUES (CURRENT_DATE NOT 
```

---

## Crash 72: `084fe66475952dfb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027863`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT TRUE AS v___yt78f_ls_8 FROM json_tree('[{"a":1},{"b":2}]'); CREATE 
```

---

## Crash 73: `dcd964846167f289` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027877`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 74: `f6a0294cb520adc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028078`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT lag(NULL NOT IN (CURRENT_DATE = NULL < CURRENT_TIMESTAMP IS NOT NULL == TRUE AND FALSE | CURRENT_DATE COLLATE BINARY)) OVER () FRO
```

---

## Crash 75: `ff803c64c0757fc0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028084`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('[1,2,3]') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 76: `b736f75182ddd796` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028091`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT lag(FALSE COLLATE RTRIM) OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_DATE) FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LI
```

---

## Crash 77: `ba2ed1c16f169734` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 FLOAT GENERATED ALWAYS AS (FALSE) STORED); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1
```

---

## Crash 78: `2215d3414c4c9b3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028103`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIME % CURRENT_DATE, * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 79: `68fb7e78aece41ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028117`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT dense_rank() OVER (PARTITION BY NULL, FALSE), * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t
```

---

## Crash 80: `3221ad818c660695` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028128`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT CURRENT_TIME <= CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 81: `9ba5ee6d53c50bb5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028134`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT lag(FALSE == CURRENT_DATE COLLATE BINARY) OVER () FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed
```

---

## Crash 82: `a76b44e759fc1b73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028155`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('{}') GROUP BY CURRENT_TIME LIMIT CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 83: `b0d5ab7399dd3c8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028166`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT NULL & CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP) FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE se
```

---

## Crash 84: `f978aae3797428b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028182`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT *, * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 85: `e471f342a8017d34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028188`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT * FROM json_tree('[1,2,3]') WHERE NULL <= FALSE ORDER BY TRUE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 86: `c640f0a9ae32282f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM jsonb_tree('[1,2,3]') ORDER BY CURRENT_DATE ASC NULLS LAST, RAISE(IGNORE) DESC, FALSE ASC NULLS F
```

---

## Crash 87: `99022b64d96f495b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028200`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT cume_dist() OVER () FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 88: `29688e2337dcec69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028207`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT 3.22e+43956802423650548911128958740541613438873); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE; CREATE TABLE see
```

---

## Crash 89: `7c26b7e9fa097192` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028267`

```sql
SELECT printf('%.*g', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 90: `afdf5ead0d89e0a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028385`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 91: `62a2ee9734c8621d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028432`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 92: `0c80376e0bad4f1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028440`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT TRUE NOT LIKE FALSE OFFSET TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 93: `0f1d7be3ac2cde53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028479`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE LIMIT CURRENT_DATE >> TRUE OFFSET TRUE; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 94: `9ad85c2fbdb76f31` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030385`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME LIKE json_remove('{"a":1}', '$.c.a'), CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 95: `f231e63f89e2dac1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030429`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT '-'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(DISTINCT CURRENT_TIME)); CREATE TABL
```

---

## Crash 96: `df00742c7ae238f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030705`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT 3.22e+43956802423650548911128958740541613438873, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT * FROM p JOIN q s_ ON CURR
```

---

## Crash 97: `409e3b800fab6e59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030901`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, c2 BOOLEAN NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT dense_rank() OVER (PARTITION BY NULL, CURRENT_TIM
```

---

## Crash 98: `973c25e1ba8d777a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031478`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL D
```

---

## Crash 99: `d688299f33488cbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031545`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQ
```

---

## Crash 100: `6c77c8de91669a70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031672`

```sql
SELECT printf('%.*s', -2147483649); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREAT
```

---

## Crash 101: `cc10c35b6212bbd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038283`

```sql
SELECT substr('--__V_S 4 _ ', 2147483648, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),
```

---

## Crash 102: `ad1a970ba7d891c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038305`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 103: `cab3db443bca8e61` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038334`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, b FLOAT); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT * FROM p JOIN q s_ ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 104: `439c1228f689c043` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038351`

```sql
SELECT printf('%.*d', -2147483649, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 105: `53b564cc0866f79e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038368`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_tree('{}') GROUP BY CURRENT_DATE, TRUE); CREATE TABLE seed_t1(
```

---

## Crash 106: `fe9f4c7c620415f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038385`

```sql
SELECT round(-1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 107: `c7d597740ebfa9c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038438`

```sql
SELECT substr('1q ', 9223372036854775807, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 108: `999e8e291534ef55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038937`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (TRUE) UNION ALL VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 109: `0b8caf4845c82b4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038943`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL percent_rank() OVER (), CURRENT_TIMESTAMP AS z_ FROM p AS n; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 110: `2eceb79ed19439e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038952`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEG
```

---

## Crash 111: `9944f89e3b82ae74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038961`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 112: `129534cf3b625faa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038969`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_DATE)), CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 113: `c46897f5621dd97b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038977`

```sql
SELECT round(0.01, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 114: `1f98401280da8131` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038985`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT 3.22e+43956802423650548911128958740541613438873); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 115: `3df4db1299c8391b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039160`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME LIKE FALSE >> -CURRENT_DATE != FALSE NOT BETWEEN FALSE AND CURRENT_DATE NOT NULL NOTNULL, TRU
```

---

## Crash 116: `c89c7f0a78d7e47f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039174`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> CURRENT_DATE != FALSE, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 117: `c4e202df23eaa249` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039196`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME LIKE FALSE >> -NULL NOT BETWEEN FALSE AND CURRENT_DATE NOT NULL NOTNULL, TRUE); VALUES (CURRE
```

---

## Crash 118: `27ba7379a78d55b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039251`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME LIKE TRUE, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 119: `d76629792b344775` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039277`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL) UNION ALL SELECT DISTINCT *, * FROM json_each('{"a":1}') LEFT OUTER JOIN json_tree(NULL, '$') WHERE TRUE; INS
```

---

## Crash 120: `fad2f8ac63204b33` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039297`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 121: `e07e6d292eff032d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039305`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_TIME)); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 122: `d916c286a6bf6a09` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039329`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); VALUES (NULL) UNION ALL SELECT ALL CURRENT_TIMESTAMP FROM json_tree('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIMESTAMP 
```

---

## Crash 123: `ade9ce03c0648ac2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039344`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL *, percent_rank() OVER (), * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 124: `72875e92220f1d6a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039367`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -98751331.81); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 125: `93219f01385d2aa5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039874`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 NUME
```

---

## Crash 126: `b508f4e9f77b36b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040193`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT 
```

---

## Crash 127: `04b776e845bc004f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040335`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT OR REPLACE INTO p VALUES (CASE WHEN CURRENT_DATE IS NOT NULL COLLATE BINARY THEN NULL END); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 128: `611af9c85b236ed2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040349`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES ((VALUES (TRUE))); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 129: `8d5ce21c71b9d961` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040369`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (NULL IS FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 130: `40e6645d77d4c167` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040384`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL CHECK (CURRENT_TIMESTAMP)); INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 131: `c50340f220a38faf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME BETWEEN CASE WHEN NULL THEN CURRENT_DATE COLLATE BINARY ELSE TRUE END AND FALSE); PRAGMA quick_check; CREATE TABLE see
```

---

## Crash 132: `a806f74e9d1ba7b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040515`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (FALSE << NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 133: `50be1044d9e91854` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040530`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('{"a":1}', '$[#-1]')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 134: `b1ceac695d84a86c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIME NOT NULL)); INSERT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 135: `0c2abbe80b44aeb7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040548`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 136: `b143ab4a345360d2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040571`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-341061); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 137: `9e489a64c3c07163` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040577`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VAL
```

---

## Crash 138: `0b836bc0d39e36a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040583`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (TRUE || CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 139: `62ded93e2e4c21d8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040599`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 140: `6d957b3945a208d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040632`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT NULL, _rowid_ INTEGER PRIMARY KEY); INSERT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE se
```

---

## Crash 141: `7dae3cef0960aace` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040650`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 142: `f1af391492541231` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040739`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 143: `f26df591d125bf92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040757`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-last_insert_rowid()); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 144: `45e44dd40db7356c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040803`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (CURRENT_DATE || NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 145: `2bbaba0943edc931` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040814`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL NULL NOT IN (FALSE) IS NOT TRUE, CURRENT_TIMESTAMP AS z_ FROM p AS n; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 146: `3898f4757eb2d90e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040861`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT count(*) OVER (PARTITION BY CURRENT_TIME, FALSE) FROM p JOIN q s_ ON CURRENT_TIMESTAMP; CREATE TABLE seed_
```

---

## Crash 147: `841eeb9ae3eb5f21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041291`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 148: `dcce56fb31bee344` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043613`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); WITH
```

---

## Crash 149: `c3a58b39f611050b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044117`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('{}') GROUP BY CURRENT_TIME LIMIT CURRENT_TIME; INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA
```

---

## Crash 150: `b279046908ef646b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057441`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT -0, c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE 
```

---

## Crash 151: `12f714dbdcc270b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057964`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT FALSE, c3 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY CURRENT_TIME, NULL; INSERT INTO p DEFAULT VALU
```

---

## Crash 152: `26659ab7d1af20d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057973`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -98751331.81); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 153: `6ae80f29062c7195` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057989`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN, c3 DATE UNIQUE, c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY CURRENT_TIME, NULL; INSERT INTO p DE
```

---

## Crash 154: `86745068fa5cac0e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058014`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 FLOAT GENERATED ALWAYS AS (FALSE) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY CURRENT_TIME, NULL; INSE
```

---

## Crash 155: `32327643f4519965` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058023`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (CURRENT_TIME), a DATE CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(a INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 156: `2c7701c344d248da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058036`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT -6.794573268604986e8); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY CURRENT_TIME, NULL; INSERT INTO p DEFAULT VALUE
```

---

## Crash 157: `9a1ee0b0ee494568` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058046`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT -0); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY CURRENT_TIME, NULL; INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 158: `600d3781fdff4c5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058053`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME AND CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 159: `eea873b1e7652330` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058505`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 160: `9fac16515f884d20` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058527`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(CURRENT_DATE >> TRUE, '$[#-1]') LEFT O
```

---

## Crash 161: `0af7c7329d1bc582` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058544`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (TRUE) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 162: `557836ea7e9347e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058564`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT *, lag(CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME, FALSE) FROM p JOIN q s_ ON CURRENT_TIMESTAMP; CREATE
```

---

## Crash 163: `34b44019d0210ff4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059047`

```sql
SELECT printf('%f', 9223372036854775807, '1_-bz -_'); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE s
```

---

## Crash 164: `a9d003f105db0e78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000074725`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS 
```

---

## Crash 165: `76f1b367ea655b75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078452`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 166: `1dad78b287833a1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078473`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 167: `b3f1649bac88b9ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078479`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 168: `a14dc8b614214c47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078501`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 169: `47a96f9bf2f7cad2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078708`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (NOT TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 170: `278c7b9da0e06450` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078733`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER DEFAULT -29807894865.4354460338781540840590894986048827910184442871995724E19); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (last_insert_rowid(
```

---

## Crash 171: `141203aa12e12bee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078745`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL row_number() OVER (), * FROM json_tree('[1,2,3]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 172: `dc036d55f576ce7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078753`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL * FROM (SELECT ALL CURRENT_DATE COLLATE RTRIM FROM json_tree('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP) AS a NATURAL JOIN json_tree
```

---

## Crash 173: `e778ad5becd6fd16` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078787`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); WITH RECURSIVE t1 AS (SELECT CURRENT_TIME AS a FROM p) SELECT * FROM t1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 174: `6c8a25ebe87fdd8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078793`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER DEFAULT X'ebC5ce52BbD2'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (last_insert_rowid()); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 175: `e2951569ff14670b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078805`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (last_insert_rowid()); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE NULL ORDER BY CURRENT_TIMESTAMP DES
```

---

## Crash 176: `cc5b5b93984ab2ae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078891`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (last_insert_rowid()); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (last_insert_rowid()); 
```

---

## Crash 177: `e19665b8b29827a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078958`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('{"a":1}', '$.c[#-1]')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 178: `1aa0fd4e390eccc1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078964`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('{"a":1}', '$[0].a')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 179: `bad628f1b8aca724` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078980`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('[{"a":1},{"b":2}]', '$[#-1]')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 180: `0a036853cb0897f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078996`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('{"a":1}', '$')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 181: `9c4eed53ba390db1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('[1,2,3]', '$[#-1]')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 182: `ae3d4cc7ecb4dd1a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079018`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_DATE || FALSE COLLATE RTRIM); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 183: `9f5d2ac455b74e7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-json_remove('[]', '$[#-1]')); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 184: `99dc9d5dbb4261fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079126`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-CAST(CURRENT_DATE <= FALSE AS INTEGER) COLLATE BINARY); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 185: `36c19982796cafdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-total_changes()); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 186: `fde3f3fb0ec63013` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079227`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-random()); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 187: `ecfb015f98eb0793` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079240`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 188: `eebf57329c798664` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079248`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 189: `f6175f8386228e6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079254`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 190: `d5957fefa261dd1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079261`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 191: `54d8870cc3a74caa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079267`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 192: `f4325a7cf1e3f428` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079275`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT ' _- qt__PL C-  7a'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(
```

---

## Crash 193: `4339bbe88c72bda4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079292`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT X'a5b3eAa6'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 194: `5cf380ac3971ada1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079303`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT X'db'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 195: `8ea2d9f4b78928ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079309`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 196: `a89a9a6c77778400` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079327`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT X'A190'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 197: `3b1090101895ee90` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079360`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -68468365302493502689124700430473.45684138660558413514891972161195326037501467855637368478745852019230624078e7); CREATE VIEW IF NOT EXISTS v1 AS SE
```

---

## Crash 198: `382f3fbf757d5456` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079385`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT -2963.1); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 199: `d50a9c4ec9a502e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079499`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT ''); INSERT INTO p VALUES (341061); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 200: `3b5dc4741ab39f47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079521`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, b FLOAT); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT DISTINCT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 201: `478d9c157dd1ec23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079530`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME BETWEEN CURRENT_TIME AND CAST(CURRENT_TIME COLLATE RTRIM AS VARCHAR(255))); PRAGMA quick_check; CREATE TABLE seed_t1(c
```

---

## Crash 202: `e05119a2787b5414` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079536`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (341061); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 203: `fe46c0a426b80163` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079546`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (X'eED00F'); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 204: `764590a64da67d49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079564`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t1 AS (VALUES (RAISE(IGNORE))) VALUES (CURRENT_DATE); INSERT INTO p VALUES (341061); PRAGMA quick_chec
```

---

## Crash 205: `210528f1a2483e20` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079588`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c2 FLOAT GENERATED ALWAYS AS (FALSE GLOB CAST(TRUE AS DATE)) VIRTUAL); INSERT INTO p VALUES (341061); PRAGMA quick_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 206: `2763eb304cbe27c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079597`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE || NULL IS NOT NULL COLLATE RTRIM); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 207: `6c083d2baa35f0aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079616`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-48.60343925614732356757305162378052419653407707461475895111891050014205727218227171695492662671870047060545354495165033643419086650
```

---

## Crash 208: `ae91c75d0cbbca7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079671`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, _rowid_ GENERATED ALWAYS AS (a = -0) ); INSERT INTO p VALUES (341061); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 209: `cfdfe11b69a49416` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079726`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT lag(CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME, FALSE) FROM p)); P
```

---

## Crash 210: `b98ca7e6ca94db6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079740`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 211: `ebca84b15e89d1d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079755`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 212: `b945e0e21e67c235` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079765`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (FALSE GLOB NULL COLLATE RTRIM < FALSE) UNION SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE TABLE seed
```

---

## Crash 213: `0a8ea9ec66fe0430` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079812`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (typeof(FALSE)) UNION SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 214: `45ef6790429a7228` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079838`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE ISNULL)); PRAGMA quick_check;
```

---

## Crash 215: `1009392bfd636f6c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p VALUES (-NULL NOT IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * FROM p) NOT IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * 
```

---

## Crash 216: `c75d73c6167dd20f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081339`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR ROLLBACK INTO p VALUES (TRUE, CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 217: `bb87bfb933d19859` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081359`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR ROLLBACK INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIME NOT IN (SELECT DISTINCT * FROM (VALUES (RAISE(IGNORE))) AS j_3 WHERE FAL
```

---

## Crash 218: `d03bbb0b5459e443` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081382`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT * FROM json_each('{"a":1}') WHERE json_type(FALSE) GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 219: `89559540020fddb3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081402`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (-NULL, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 220: `5025a2af7723418c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081541`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -NOT TRUE, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 221: `946466f44daa9435` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081548`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CURRENT_TIMESTAMP > CURRENT_DATE ISNULL); CREATE TABLE seed_t1(c1 I
```

---

## Crash 222: `eb30abd77280f95f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081562`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CAST(FALSE AS REAL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 223: `613c1123de92cd5d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081571`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS VARCHAR(255)), TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 224: `c0501a22f2658b52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIME NOT NULL), c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 225: `a1175a36fa0d064a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081589`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (CASE WHEN CURRENT_DATE NOTNULL THEN CURRENT_DATE IS NOT NULL COLLATE BINARY ELSE TRUE END, TRUE); VALUES (
```

---

## Crash 226: `7cc2cd6d2faf7f12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081609`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (json_patch('[{"a":1},{"b":2}]', '{"a":{"b":1}}'), TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 IN
```

---

## Crash 227: `f8c886337f3cb48b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081621`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, c3 INT NOT NULL DEFAULT '-'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CURRENT_TIM
```

---

## Crash 228: `6d12d6c162506803` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081628`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CAST(FALSE AS REAL), TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 229: `82abda0e3d0ea4b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081647`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CURRENT_TIM
```

---

## Crash 230: `a9cdcfa21cefe4f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081659`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (TRUE LIKE CURRENT_TIMESTAMP ESCAPE NULL); CREATE TABLE seed_t1(c1 I
```

---

## Crash 231: `33d580fae358c930` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081667`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 
```

---

## Crash 232: `8f108779fa37cf0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081673`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CAST(TRUE AS DATE) ISNULL, NULL); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 233: `f0a08c7600d88f1c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081681`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT CURRENT_TIMESTAMP OR count(*) AS a FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 234: `9241a3f323a72eb4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081695`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, _rowid_ FLOAT CHECK (NULL)); INSERT OR REPLACE INTO p VALUES (FALSE >> -CURRENT_DATE, TRUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 235: `ba93bfa49cea950c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081796`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >> FALSE >
```

---

## Crash 236: `1b08da37d59c2481` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081867`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -TRUE, TRUE); SELECT DISTINCT TRUE GLOB CURRENT_TIME AS v___yt78f_ls_8 FROM p AS h; CREATE TABLE 
```

---

## Crash 237: `4594206a27a40f72` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081881`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -TRUE, TRUE); SELECT ALL * FROM p NOT INDEXED LEFT OUTER JOIN json_tree('[]'); CREATE TABLE seed_
```

---

## Crash 238: `58def3f74535485b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081935`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -TRUE, TRUE); SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDIN
```

---

## Crash 239: `2d2ad7717342af8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081952`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL, c1 FLOAT); INSERT OR REPLACE INTO p VALUES (FALSE >> -TRUE, TRUE); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE NULL < CURRENT_TIMESTAMP; C
```

---

## Crash 240: `46d19cae225f1c92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082097`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT TRUE FROM json_tree('{}') , json_each(CURRENT_DATE >> FALSE, '$.c[#-1]') LEF
```

---

## Crash 241: `0df2fd8ab116e128` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082129`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('{"a":1}') LEFT OUTER JOIN json_tree(TRUE LIKE CURRENT_TIMESTAMP ESCAPE NULL, '$') WHERE TRUE; CREATE TABLE see
```

---

## Crash 242: `569796785d72c930` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082369`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL CAST(FALSE AS BLOB), * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 243: `521c3bb957d90ee9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000082396`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT ALL json_patch('{"a":1}', '[1,2,3]'), * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---
