# Crash Triage Report

**Total crashes:** 337  
**Unique crash sites:** 337  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 134 | 134 | 39% |
| Signal | 203 | 203 | 60% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `e95f86856fa70520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000142`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE LIKE CURRENT_TIMESTAMP IS NOT NULL MATCH CURRENT_DATE, ~X'E9ecb7BAA0d4fAb' / jsonb_patch('[]', '{
```

---

## Crash 2: `5d57e908203655e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000896`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), c3 GENERATED ALWAYS AS (c1) ); SELECT CASE CURRENT_TIMESTAMP IN (NULL) WHEN FALSE NOTNULL THEN +~RAISE(IGNO
```

---

## Crash 3: `ad142bf3e84d8cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO q VALUES (CASE FALSE OR CURRENT_TIMESTAMP * FALSE NOT NULL >= TRUE NOT IN (VALUES (NULL)) WHEN ~q.c3 THEN FALSE + RAISE(I
```

---

## Crash 4: `7afd9e4e97908808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001225`

```sql
SELECT substr('', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO t3 VALUES (+CASE CASE RAISE(IGNORE) NOT NULL WHEN +RAISE(IGNORE) <= +CURRENT_TIME THEN CURRENT_TIME END W
```

---

## Crash 5: `3f4a42c597d0a479` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001282`

```sql
SELECT substr(' K- h p- G_W_', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (CURRENT_TIME * NULL | 0 OR p._rowid_ COLLATE RTRIM) RETURNING t2.
```

---

## Crash 6: `c3675d6634621b64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001391`

```sql
SELECT printf('%d', 2147483647, '  2nV_-_M-j     l'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); WITH RECURSIVE p AS (VALUES (RAISE(IGNORE)) UNION SELECT DISTINCT * FROM json_tree('
```

---

## Crash 7: `a09281244f7a516e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001756`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3, c3, c3); WITH RECURSIVE q (c3) AS NOT MATERIALIZED (SELECT q.*, * FROM t3 AS a LEFT OUTER JOIN (VALUES (TRUE) ORDER BY CURRENT_TIMESTAM
```

---

## Crash 8: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001929`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 9: `42d2b75f7cf78f23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002107`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 10: `afb8dbd310c6f83b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002341`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 11: `d2f3a88a0a18f783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004857`

```sql
SELECT substr('9_k3 -43__A__-', 4294967296, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT 
```

---

## Crash 12: `4ec1dfa01520718a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004870`

```sql
SELECT printf('%llu', 1, '10__V HdBUa -'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 13: `ffd4ad694e2e5fbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005382`

```sql
SELECT printf('%.*s', 0, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 14: `4972a1a5a4838f5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005453`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))
```

---

## Crash 15: `947362fd26a02094` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005583`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(
```

---

## Crash 16: `3da837bbcacc92fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005597`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 17: `023ae62b56ecc837` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005779`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 18: `21d0c825a16ada76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005786`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 19: `f663004ffde5ac5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005792`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c N
```

---

## Crash 20: `174ab6c7edf4b6ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005806`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 21: `e29727bfa0de9639` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006015`

```sql
SELECT printf('%.*e', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 22: `ff184d27166b5cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006636`

```sql
SELECT printf('%.*d', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 23: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007652`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 24: `acd2e1cda72574ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007973`

```sql
SELECT printf('%.*f', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 25: `8112bc25ee3dcf02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007985`

```sql
SELECT printf('%.*d', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 26: `a4f98a1356df14e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007991`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 27: `b80d69ea566ac5fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007997`

```sql
SELECT printf('%.*g', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 28: `8c0ede7489846927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008009`

```sql
SELECT round(-1e308, 1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 29: `ecebab7864d638ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008015`

```sql
SELECT printf('%.*s', 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 30: `1e2bd96d051bd620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008024`

```sql
SELECT printf('%.*g', 4294967295, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 31: `2b485f5c24683e0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008038`

```sql
SELECT printf('%.*e', -2147483648, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 32: `5a9c31da332d6853` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008052`

```sql
SELECT printf('%.*d', -1, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 33: `b1b09d2638b02d48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008071`

```sql
SELECT substr('Lk- 9  r e', 2147483648, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coal
```

---

## Crash 34: `3c8a7e36c3496f98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008078`

```sql
SELECT substr('', -2147483648, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 35: `400d866c85055dd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008089`

```sql
SELECT printf('%x', -2147483649, '_-u -  '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 36: `53b2bf1e36534d1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008106`

```sql
SELECT printf('%.*g', -9223372036854775808, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 37: `820b54060e9ebb91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008128`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 38: `29f6cebedc47c4ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008163`

```sql
SELECT printf('%.*d', 4294967296, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 39: `4c68c0209dc1a0b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009720`

```sql
SELECT printf('%.*e', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 40: `a5cdf0a83c7556ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009736`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL + NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 41: `051f1ab09290274d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009750`

```sql
SELECT printf('%.*g', -2147483648, 1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 42: `7b13d150e0339001` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009894`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('{"a":{"b":1}}') LIMIT CURRENT_DATE, TRUE); C
```

---

## Crash 43: `3b26b7770fe09897` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009943`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('{"a":{"b":1}}') LIMIT FALSE AND NULL, FALSE)
```

---

## Crash 44: `ef81a206e85bc3e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010652`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 45: `f4e7719a9aa89201` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010941`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIME NOT IN (WITH q AS (SELECT *), t3 (a) AS (VALUES (NULL)) VALUES (CURRENT_TIME)) AS p7_t2_8s FROM p WHERE TRUE) A
```

---

## Crash 46: `03c0241efd0ce624` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010950`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 47: `7b09b0c990dcd17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010965`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CU
```

---

## Crash 48: `33d50c3cdcf30dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010976`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE TABLE seed
```

---

## Crash 49: `08a8e75aaf4d5135` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010993`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE, TRUE AS a FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 50: `4b199381b291144c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011022`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME NOT IN (WITH q AS (SELECT *), t3 (a) AS (VALUES (NULL)) VALUES (CURRENT_TIME)) AS p7_t2_8s FROM (SELECT * FROM p WHERE TRUE) A
```

---

## Crash 51: `04bb471e97dbb706` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011028`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT
```

---

## Crash 52: `2246ed83f54c053d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011113`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT NULL AND NULL NOT NULL AS xoi_0_800y_7__7ladlcu__1u FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 53: `a5f138e436bb8b5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011127`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT X'' FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 54: `b706a8b7b9e653f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011167`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT NULL AND NULL AS xoi_0_800y_7__7ladlcu__1u FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 55: `0bfdc729d0d68c6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011331`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT CURRENT_TIMESTAMP OR FALSE % TRUE > CURRENT_TIME + CASE WHEN TRUE ISNULL THEN
```

---

## Crash 56: `81e59d4c881a2a7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011337`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 57: `88681471fb3f6e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011358`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT TRUE AS h7ck, * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 58: `c2ac0d850349ac66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011366`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE BETWEEN TRUE AND CURRENT_TIMESTAMP < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 59: `7896c3aeaf295145` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011380`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT cume_dist() OVER (PARTITION BY FALSE ORDER BY FALSE DESC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWI
```

---

## Crash 60: `104ffced159e3407` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011396`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 61: `959836eb579a4965` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011403`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE == CURRENT_TIME) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 62: `9d1f509857880bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011418`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE FALSE + TRUE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 63: `0927810b20b96ae5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011426`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE p.b < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed
```

---

## Crash 64: `c68074090c79b015` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011440`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP OR FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 65: `aab4bd38f4b457a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011451`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT E
```

---

## Crash 66: `44652ff36614bca0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011458`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X'CB', c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) A
```

---

## Crash 67: `5e904dbc9d243863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011470`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_TIME COLLATE NOCASE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 68: `b00a3e19ec527510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011485`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE -CURRENT_TIME >= FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 69: `9ac930d14414ff44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011526`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 70: `4a06292b95d77057` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011532`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 71: `9c80daf5657e1228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011542`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CAST(CURRENT_DATE AS REAL) AS a FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 72: `0998091e129decec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011599`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL < NULL <
```

---

## Crash 73: `53c755c6aeebd5a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011605`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT
```

---

## Crash 74: `7d23fe75b62726bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011614`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < 
```

---

## Crash 75: `03883b26f6222f2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012294`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT * FROM p WHERE p.b < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 76: `7c35da804276c863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012333`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_DATE IN (CURRENT_TIME) FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 77: `d3d4abd92fddf8fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012361`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT cume_dist() OVER () FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 78: `9e29cdeeb84d370f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012441`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT FALSE % TRUE > CURRENT_TIME + CASE WHEN TRUE ISNULL THEN random() == FALSE EL
```

---

## Crash 79: `dfe7207971dcad42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012447`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT FALSE % FALSE + CASE WHEN TRUE ISNULL THEN random() == FALSE ELSE CURRENT_DAT
```

---

## Crash 80: `a464f8a1afe57868` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012460`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT FALSE % TRUE > CURRENT_TIME + CASE WHEN CURRENT_DATE THEN CURRENT_TIMESTAMP E
```

---

## Crash 81: `409dcc7af323970a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012469`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 82: `c20b4473ccec955b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012475`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE % TRUE > CURRENT_TIME) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 83: `0b3681eba4e19769` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012554`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < FALSE IS NOT FALSE % FALSE + CURRENT_TIME) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 84: `0ceb3647c6145428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014346`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 85: `33cea79c10570157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014358`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 86: `3603eff337f17bd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014367`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 87: `3b85b3afdd31ff87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014377`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE TRUE NOT IN (TRUE) < CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 88: `37d5c6eaa50a98b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014383`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 89: `81a064409cefd19e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014389`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_DATE < CURRENT_DATE < TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 90: `5cbefad82c6ffe5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014396`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 91: `be31becb0d945b42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014405`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE TRUE / CURRENT_TIME IS NOT NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 92: `2d413ccc0a57eb82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014421`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t2 AS (SELECT *) VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE T
```

---

## Crash 93: `c398e07662815425` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014432`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 94: `9e2a2b62cccb33b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014466`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WH
```

---

## Crash 95: `c7c28345b284beed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014515`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURR
```

---

## Crash 96: `29d512ea6fc5183b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014521`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURR
```

---

## Crash 97: `60c1efc0ade5832d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015846`

```sql
SELECT printf('%f', 4294967295, '__zn169-__V_'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(
```

---

## Crash 98: `1fc3dd9ee1c22852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016660`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP < TRUE * FALSE >> NULL AND NULL NOT LIKE CURRENT_TIMESTAMP AS y3we801_ov4__9
```

---

## Crash 99: `9b30fdd050fbff75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016867`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN see
```

---

## Crash 100: `e1c5f10f5204dcf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016884`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE + last_insert_rowid())); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 101: `d2d4e568804b9c7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018165`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, c2 GENERATED ALWAYS AS (c1) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE OR CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 102: `d06c641e3b9419b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018270`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); REPLACE INTO p VALUES (CURRENT_DATE OR CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 103: `9c9984ff7a7f97a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018301`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE OR CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 104: `257072c6c15b82f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018345`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); REPLACE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL 
```

---

## Crash 105: `0c4159076e45bfd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, c2 GENERATED ALWAYS AS (c1) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 106: `b3eded0c56e1c71d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018861`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(
```

---

## Crash 107: `e3a28c03b124fbca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020314`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p CROSS JOIN json_tree('{}') USING (b) UNION ALL VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_DA
```

---

## Crash 108: `6c30ac4b8177aaad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022784`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 109: `7576fea2e67181cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032767`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 110: `68c11cc22eb984d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032904`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 111: `23d57da42ce112f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034414`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 112: `f037e58388065384` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035276`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN c1 PRECEDING AND CURRENT ROW) FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_
```

---

## Crash 113: `86640347a9300e28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035304`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]')); CREATE TAB
```

---

## Crash 114: `235d23f83efef4a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036826`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); WITH RECURSIVE p (b) AS (VALUES (FALSE)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 115: `6721be199f3f2bd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040257`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT * FROM p WHERE EXIS
```

---

## Crash 116: `4a266e5ab2f04796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043134`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL)
```

---

## Crash 117: `4e25cad05b137284` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045967`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT 'y4'); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 118: `4f6b1e416cfbfa1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046313`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (NULL < NULL < NULL) STORED, a TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIM
```

---

## Crash 119: `1f997c2cfc82a484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046349`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (FALSE AND NULL) STORED, a TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTA
```

---

## Crash 120: `656b07407d2e009e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046410`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL DEFAULT 8.2590858020224645356970882276180454011058468284641183667585193345502177513320035366290581546381779190393521909420644693921374319815036975692
```

---

## Crash 121: `63fa714f0cdaaced` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046463`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 122: `7221e81027031992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049141`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM json_tree('{"a
```

---

## Crash 123: `dde7496d6a2a0ad8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053311`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (NULL IS NOT FALSE) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 124: `11203bfd5257b733` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053329`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 125: `00bf489024ae166b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053515`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME >= FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 126: `9e8589c7673c65ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053750`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, c2 BOOLEAN UNIQUE); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET c2 = CURRENT_DATE; VALUES (TRUE); CREATE TABLE seed_a
```

---

## Crash 127: `9309fe1ca97c168b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053859`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET c2 = CURRENT_DATE; VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 128: `1a2253dbd80a5fc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET c2 = CURRENT_DATE; VALUES (TRUE); CREA
```

---

## Crash 129: `92b3d417aca867f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053911`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET r
```

---

## Crash 130: `0c899c1b6c718c14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053962`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET b
```

---

## Crash 131: `19b37ee51982fbe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053969`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT INTO p (b) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET c2 = CU
```

---

## Crash 132: `9f80569a2e669a19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057805`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (count() FILTER (WHERE CURRENT
```

---

## Crash 133: `a37930482a15d66b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073263`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 134: `db001c4ba2562370` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073304`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE TRUE NOT IN (TRUE)) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 135: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001912`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 136: `2074e0a819e9bcda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001949`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 137: `5d23565c30145f95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002246`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CU
```

---

## Crash 138: `b50a59eda64d072b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002258`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); EXPLAIN QU
```

---

## Crash 139: `47894fc06e878cc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002529`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (NOT CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); I
```

---

## Crash 140: `6f310cd59f8d49c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002594`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO 
```

---

## Crash 141: `2f1f9efd6cfaa00d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002662`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO s
```

---

## Crash 142: `f15738de91a1011d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002833`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 143: `b9a33b9f566ad96f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003636`

```sql
SELECT substr(' _-R-_Ha382-4-_-_p', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(1
```

---

## Crash 144: `4d847015f6057bab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004068`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 145: `a93b20de0dabdf40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004078`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 146: `da50fe3bc3129dad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004249`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 147: `8fd7fa40392ec5b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004508`

```sql
SELECT printf('%d', -9223372036854775808, 'gUVq xK__--_v_k2 -'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VA
```

---

## Crash 148: `6e3d8a6ff49e26e4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004592`

```sql
SELECT substr('-6XH', 2147483648, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(12
```

---

## Crash 149: `84da15586368eb70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004815`

```sql
SELECT printf('%lld', -2147483649, '_--7To_ __-A39- _'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44)
```

---

## Crash 150: `7c9f015d4bce7a7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005498`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 151: `c6dece959b7aa49d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005518`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE INDEX IF
```

---

## Crash 152: `8e61e9775becffdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005658`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE, c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 153: `a39676ca5640f7c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006103`

```sql
SELECT round(0.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 154: `c71c83cf34c06c24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006721`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 155: `29004b3eb7ae1b2b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011476`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE CURRENT_DATE < NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); CREATE TABLE IF NOT EXIS
```

---

## Crash 156: `44fd8b2f0cbf4e54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014057`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS 
```

---

## Crash 157: `17e1aa88fba40d3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014067`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS 
```

---

## Crash 158: `9ce92e07845bc705` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014297`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 159: `cb5a21e720ceb39d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014593`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); C
```

---

## Crash 160: `b7f6e20eb87c294e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014813`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE INDEX IF
```

---

## Crash 161: `bc201bdb34f172a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014873`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT ro
```

---

## Crash 162: `f85de88cba0ef785` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014885`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE, c1 NUMERIC); CREATE
```

---

## Crash 163: `4dd2a71e1176750e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015308`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 164: `192d71a38775ced2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000015555`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1
```

---

## Crash 165: `d615c37793bae41d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016435`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, c2 GENERATED ALWAYS AS (c1) NOT NULL); REPLACE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 166: `7921efa65808eb65` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016447`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_DATE NOT BETWEEN TRUE >> TRUE AND FALSE AS y3we801_ov4__9_4bnc2_018298____60b3__atj_jiz_5e025o49_ztn94_89h_oy____5q8
```

---

## Crash 167: `412a2a861b453fd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016503`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH q AS (SELECT *), p AS (SELECT *) VALUES (CURRENT_TIME); REPLACE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (T
```

---

## Crash 168: `9f5e0e072cc07c0f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016513`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE EXISTS (SELECT *) GROUP BY CURRENT_DATE ORDER BY RAISE(IGNORE) DESC NULLS LAST; REPLAC
```

---

## Crash 169: `b30a080eca887995` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016526`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT, c3 TEXT GENERATED ALWAYS AS (NULL IS NULL COLLATE RTRIM) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_DATE ASC NULLS LAST, CURRENT_TIME ASC 
```

---

## Crash 170: `533b766ab64d79ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016550`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT DEFAULT 0); REPLACE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 171: `02db39653629970e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016645`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT, c3 TEXT GENERATED ALWAYS AS (NULL IS NULL) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (TRUE); CRE
```

---

## Crash 172: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017029`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 173: `1c32699566e4c904` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019470`

```sql
SELECT round(1e308, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 174: `1658fb99d22d3956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019498`

```sql
SELECT round(1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 175: `d71411f27ac4b0e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020630`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_DATE BETWEEN TRUE AND CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 176: `07136998366676c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020648`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 177: `8be86735b311e657` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020669`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (TRUE NOT IN (TRUE) > ~TRUE || FALSE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 178: `2f05481e3f048a34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020694`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP NOT LIKE TRUE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 179: `21644f5231b5827b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020719`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 180: `061cfd5564b1ebaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020732`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (min(NULL)) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 181: `da11d9d7eec7819f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020831`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (random()) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 182: `7d6247da6ae054d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020857`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 183: `f65828765a5149f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020892`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || TRUE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 184: `d0b787d728eee704` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020899`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 185: `2bfd3ade1c3b153d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020906`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 186: `68f43a39adf30237` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020936`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 187: `0a49f1282b7dcd79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020945`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 188: `78532bfb00d644e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020962`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || NULL) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 189: `b8afd4dd8bc15478` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021070`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL <> RAISE(IGNORE) + +NULL NOT BETWEEN last_insert_rowid() AND RAISE(IGNORE))); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES;
```

---

## Crash 190: `61bdfff13f4ff34d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022467`

```sql
SELECT round(-1.0, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 191: `8ead127ac0d4f25c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022479`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 192: `972424572016721b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023588`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM (SELECT TRUE * FALSE >> NULL AS y3we801_o
```

---

## Crash 193: `a1142d409a3c79d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023620`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE CURREN
```

---

## Crash 194: `8defcfa1732a2614` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023633`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}'); 
```

---

## Crash 195: `3e2cc2c7cf2eb040` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023642`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('
```

---

## Crash 196: `82da63461e2477ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023794`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT ALL * FROM json_tree('[1,2,3]
```

---

## Crash 197: `b2ab3e9a78935986` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026253`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (FALSE) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INT
```

---

## Crash 198: `4fdbcd0633812b6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035809`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL > TRUE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 199: `ccc60486841f9393` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036483`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, rowid NUMERIC NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 200: `3b30c170734daaed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039117`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (NULL) EXCEPT SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 201: `8a8e71d08924dbbb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039172`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 202: `bca4d07ed5a8d854` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040780`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT * FROM (SELECT -3228383132549325364416938416233675274372064432222377959910365675746143818305039406258629311751383832920173868113516850811478
```

---

## Crash 203: `d5578c22a0d83eb7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040820`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC GENERATED ALWAYS AS (FALSE) VIRTUAL); VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 I
```

---

## Crash 204: `30a99956926d4cbb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040836`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (FALSE IS NOT CURRENT_TIMESTAMP OR FALSE % TRUE > CURRENT_TIME + random()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 205: `33d34dd2c331cb55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040847`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT X'984Ba3EcBCf9fD'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 206: `467915387fdef0f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040863`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT X'df7a45'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 207: `0ee7661c26b31946` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040876`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL IS NULL COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 208: `107b469323b4ecb8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041029`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN DEFAULT X'c1'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 209: `e5156d79e9579733` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041042`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); SELECT ALL * FROM json_tree('[{"a":1},{"b":2}]') ORDER BY FALSE ASC; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 210: `34e19943fd473a60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041206`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 211: `de80a064dab38d00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042247`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT rank() OVER () AS w; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 212: `ae6cc3879b12670a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042254`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE 
```

---

## Crash 213: `3fa876ca825ef67f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042276`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') NATURAL 
```

---

## Crash 214: `e3d74942d7171362` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042290`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (b) AS (SELECT CURRENT_TIME NOT IN (WITH t3 (a) AS (VAL
```

---

## Crash 215: `6fb0a78b770dbd14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043071`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM (SELECT *) AS a CROSS JOIN s WHERE CURRENT_TIME EXCEPT VALUES (TRUE); INSERT INTO p DEFAULT
```

---

## Crash 216: `1fdca49af9e3da66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043077`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY, c1 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 217: `0be2676d3ed6d2b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043084`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT rank() OVER () AS w; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 218: `dd6c9934d883ebe9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043092`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL CURRENT_DATE NOT LIKE CURRENT_TIMESTAMP FROM json_each('[{"a":1},{"b":2}]'); INSERT INTO p DEFAULT VALU
```

---

## Crash 219: `c16e6a276520f7d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043100`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b TEXT, c3 TEXT GENERATED
```

---

## Crash 220: `9720178fc284cfd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043110`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(IGNORE) NOT IN (VALUES (RAISE(IGNORE)) UNION ALL SELECT * ORDER BY CURRENT_TIMESTAMP) AS w, *; INSERT
```

---

## Crash 221: `8c4da2bf60ea1d1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043116`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 222: `4e16acb8c52b8616` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043144`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (), *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE T
```

---

## Crash 223: `576a80d09c5a9cf2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043151`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('{"a":1}') JOIN jsonb_each('{"a":1}') INNER JOIN q INDEXED BY c2 WHERE CURRENT_TI
```

---

## Crash 224: `908894e22900bc53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043162`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('[]') CROSS JOIN q NOT INDEXED LEFT JOIN json_each(RAISE(IGNORE), '$') WHERE FALS
```

---

## Crash 225: `8a8d2fd2cbeee635` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043170`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (-322838313254932536441693841623367527437206443222237795991036567574614381830503940625862931175138383292017386811351685081147861172620620196301
```

---

## Crash 226: `9e4aa260d0cd9441` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X'CB'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 227: `46f4112999160e75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043241`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.c2, q.* FROM p LEFT OUTER JOIN s JOIN json_each('[]'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; 
```

---

## Crash 228: `fe0abe7443f96181` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047271`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b TEXT, c3 TEXT GENERATED ALWAYS AS
```

---

## Crash 229: `3c275a2d38520fad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048541`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CAST(NULL AS TEXT))); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 230: `15dadac9c28daf88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049645`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT 47392); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 231: `13e1d3dd878635a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049671`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT 47392); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT CURRENT_TIME & NULL NOT BETWEEN TRUE >> CURRENT_TIMESTAMP < TRUE * CURRENT_TIME ISNULL >> NULL AN
```

---

## Crash 232: `80141447697be1e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049692`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT 47392); INSERT INTO p DEFAULT VALUES; SELECT p.* FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 233: `2be01b78c1259e12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049727`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT 47392); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{}') WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 234: `5c54a24aee3d366e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049736`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 235: `4e05151222da1cde` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049844`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN FALSE PRECEDING AND CURRENT ROW); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 236: `9671ac92914bd958` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051001`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE CHECK (~NULL), c3 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 237: `5381783353510405` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051197`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + count()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 238: `d0bf458340396a6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051205`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + random()) INTERSECT VALUES (FALSE IS NOT CURRENT_TIME % TRUE > CURRENT_TIME + random()); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 239: `3255f797805b4169` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051237`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + CURRENT_TIMESTAMP + last_insert_rowid() + NULL + CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 240: `055fb8799b488dea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051258`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + random()) INTERSECT VALUES (-CURRENT_TIME >= FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 241: `48cdf91499c9a90f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051277`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + count(DISTINCT CURRENT_DATE)) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 242: `45fd598bf2e59761` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051284`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + char(NULL)) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 243: `530b360eb836ea42` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051302`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + total_changes()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 244: `c18668e7e18c9130` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051308`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (row_number() OVER ()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 245: `1292a841503e4aa0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051347`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + json_remove('{}', '$.c')) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 246: `4f6c9523a21cf346` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051419`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + random() + random() + random() + random() + random() + random() + random() + random() + random() + random() + random() + ran
```

---

## Crash 247: `99cc726b9beeabc9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051552`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + json_remove('{}', '$[#-1]')) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 248: `c2f566e60751e3b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051634`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + changes()) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 249: `52e41bd94f739ffc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051695`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE + random()) INTERSECT VALUES (CURRENT_TIME + random()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 250: `4d019475b08e0e8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054437`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[1,2,3]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 251: `f09da435fc3f9117` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054460`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 252: `2b881b2424d938c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054468`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER () FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1
```

---

## Crash 253: `0322e4e886537cb9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054475`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('{"a":{"b":1}}') NATURAL LEFT JOIN json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TAB
```

---

## Crash 254: `7f8e6e5787f7f47e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054484`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 255: `4d35c9baf2afe799` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054502`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_each(CAST(TRUE AS DATE), '$.key[7561]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 256: `634539e652ad0cb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054508`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL *, * FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 257: `dad88d239c296046` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054526`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[]') ORDER BY CURRENT_TIME COLLATE NOCASE COLLATE NOCASE DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 258: `3ef475897e2b490f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054539`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCL
```

---

## Crash 259: `4cae702996208e4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054637`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL
```

---

## Crash 260: `df0f2e38598d6f0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054658`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (), * FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1
```

---

## Crash 261: `113551e5abab2114` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054709`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT ALL * FROM json_each('{"a":1}') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 262: `6f41d2cbdc43d1ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055207`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME IS NOT NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 263: `0c20740dec7bfaf7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055218`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{"a":{"b":1}}') NATURAL JOIN json_each('{"a":1}') ORDER BY CURRENT_DATE; CREATE TABLE seed_t1(c1
```

---

## Crash 264: `a3bab88a8a8428d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056605`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT count() OVER (PARTITION BY TRUE, NULL) AS d FROM json_tree('{}') WHERE FALSE EXCEPT VALUES (CURRENT_DATE); C
```

---

## Crash 265: `92132ba1e7e12828` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058926`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM json_tree('{"a":
```

---

## Crash 266: `1fbffe3f786d0e19` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059064`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, c2 BOOLEAN UNIQUE); INSERT INTO p (c2) VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 267: `04e9c67e329494ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059726`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 268: `f8eb5c3837d8fb84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059736`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT OR REPLACE INTO p VALUES ('' NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 269: `8d89dfe5152c91f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059796`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count() OVER (PARTITION BY (VALUES (FALSE)), NULL) AS d FROM json_tree('{}') WHERE FALSE EXCEPT VALUES (CURRE
```

---

## Crash 270: `909347f76cae249f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059904`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count() OVER (PARTITION BY NULL NOT NULL, NULL) AS d FROM json_tree('{}') WHERE FALSE EXCEPT VALUES (CURRENT_
```

---

## Crash 271: `a9897869cb04f922` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078387`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT DISTINCT TRUE AS d FROM json_
```

---

## Crash 272: `03bcd182b781f25e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078393`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each(TRUE * C
```

---

## Crash 273: `3654240d9ce4b20e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078405`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT ALL * FROM (json_each('{}') C
```

---

## Crash 274: `8c62cb21aab31f0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078437`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT ALL * FROM (json_tree('[{"a":
```

---

## Crash 275: `839822893d95ce13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078455`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT ALL * FROM (SELECT FALSE AS g
```

---

## Crash 276: `bd1ff271b40ceea1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078461`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE CURREN
```

---

## Crash 277: `e9f81fb051a83388` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078830`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH t3 (a) AS (VALUES (NULL)) VALUES (CURRENT_TIME) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 278: `fe1e76498ce908b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078865`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT OR REPLACE INTO p VALUES (8.259085802022464535697088227618045401105846828464118366758519334550217751332003536629058154638177919039352190942064469392137431
```

---

## Crash 279: `2fc2846d7d3d8e33` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079013`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each(C
```

---

## Crash 280: `2d194d62a0c77aa7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079047`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM (S
```

---

## Crash 281: `e2da105f8e340b7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079060`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR IGNORE INTO p VALUES (FALSE); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('{"a":{"b":1}}
```

---

## Crash 282: `4e0ce385a462031b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079068`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT * FROM (SELECT DIS
```

---

## Crash 283: `723c7efa7bf12964` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079097`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT percent_rank() OVER () AS w FROM q WHERE EXISTS 
```

---

## Crash 284: `fcbc80ab8af021fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079139`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL NOT NULL DEFAULT X''); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT 
```

---

## Crash 285: `8ade3758632fe7f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079178`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL DEFAULT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT * FROM
```

---

## Crash 286: `62ba8fdcd08fd68e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079191`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('
```

---

## Crash 287: `2939295b7c16ddf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079251`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) INSERT INTO p VALUES (''); EXPLAIN QUERY PLAN SELECT count(*) FI
```

---

## Crash 288: `3db57af00eba5a1a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079324`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) INSERT INTO p VALUES (''); EXPLAIN QUERY PLAN SELECT count(*) OV
```

---

## Crash 289: `86f54962d853577d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081484`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE FROM p WHERE TRUE / FALSE == CURRENT_TIME IS NOT NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 290: `398855af6a69dc67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000081729`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT DISTINCT * FROM p NOT INDEXED; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 291: `7f9aa592cef7569a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083624`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{}') WHERE FALSE EXCEPT SELECT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 
```

---

## Crash 292: `b0f315a0966dcbc0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083830`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO p SELECT ALL TRUE AS h7ck FROM json_each('{"a":{"b":1}}') NATURAL JOIN p NOT INDEXED; PRAGMA qui
```

---

## Crash 293: `816c549e99dc75c3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084054`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (count(DISTINCT CURRENT_TIME))) AS q0_4_64 , json_each('[1,2,3]') WHERE CURRENT_TIMESTAMP ORD
```

---

## Crash 294: `43b0cb257f522649` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084215`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL * FROM json_tree('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIMESTAMP + random(), CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_t1(c1 I
```

---

## Crash 295: `2fdc66150f957977` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084620`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL DEFAULT -0); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 296: `b66f3b310bd7b25c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084629`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIME) UNION VALUES (FALSE == CURRENT_DATE >> FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 297: `e303597d3d0f110f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084673`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 298: `9e27d5f92c44e997` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084771`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CU
```

---

## Crash 299: `1ae9767819856411` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084779`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CURRENT_TIME || CU
```

---

## Crash 300: `45a5c869328ac06a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084789`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_T
```

---

## Crash 301: `7e7202bc8029b23b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085196`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT X'8E6FDAce', c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 302: `1a57c983ff528411` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085221`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || NULL) UNION SELECT count() FILTER (WHERE CURRENT_DATE) * FALSE AS zt31l053k44u17m2_a6b__hy___1__yz2k55_28__3_53l7r
```

---

## Crash 303: `a73f0ebae5af2427` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085232`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || NULL) UNION SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY FALSE ORDER BY FALSE DESC NULLS FIR
```

---

## Crash 304: `e4d76e824ed2d912` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085240`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (67211236903697774959176252648547768059239273026.13620004E-9880087210710149825170218269537085263873) UNION VALUES (CURRENT_TIME); CREATE
```

---

## Crash 305: `3c7da05cca7bde35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085262`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT count() OVER (PARTITION BY NULL NOT NULL, NULL) AS d FROM json_tree('{}') WHERE FALSE EXCEPT VALUES (CURRENT_DATE) UNION VALUES
```

---

## Crash 306: `1ae340073acd6a6a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085404`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE) UNION SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER () FROM json_each('[1,2,3]'); CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 307: `306d92e32ec60573` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085451`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (cume_dist() OVER (PARTITION BY FALSE ORDER BY FALSE DESC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) || FALS
```

---

## Crash 308: `619289eb101664fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085468`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 GENERATED ALWAYS AS (c1) NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE | FALSE); VALUES (CASE WHEN NULL THEN FALSE ELSE CURRENT_DATE END); CREATE TABLE se
```

---

## Crash 309: `394ec04e83156a2f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085489`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM) UNION SELECT ALL count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN FALSE PRECEDING AN
```

---

## Crash 310: `ad43a35eaffb77d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085509`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE CHECK (~CURRENT_DATE + random() + random() + CURRENT_TIMESTAMP + CURRENT_TIMESTAMP), c3 VARCHAR(255)); INSERT I
```

---

## Crash 311: `bc0493fa4783e7b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085537`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP + last_insert_rowid() || FALSE COLLATE RTRIM) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 312: `0d4c0cfbf2dfa8a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085631`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM || FALSE COLLATE RTRIM || FALSE COLLATE RTRIM) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_
```

---

## Crash 313: `d10b02e0d5464bfb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085644`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_T
```

---

## Crash 314: `cbbee8b19db2b57d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085711`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (sum(FALSE) IS NOT FALSE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 315: `6745e4b669394804` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085721`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP + random() + CURRENT_DATE + FALSE + NULL) UNION VALUES (CURRENT_TIME); 
```

---

## Crash 316: `0203a037f89c94aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085733`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL LIKE RAISE(IGNORE))); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP) UNION VALUES
```

---

## Crash 317: `58d0c6a91753ba90` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085740`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP) UNION SELECT ALL TRUE AS h7ck FROM json_each('{"a":{"b":1}}') NATURAL 
```

---

## Crash 318: `4ebb9139ab4a6268` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085776`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL rank() OVER () AS w FROM json_each('[1,2,3]') UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 319: `0aa38758f7c55968` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085807`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB CURRENT_TIMESTAMP) UNION SELECT ALL percent_rank() OVER () AS w FROM json_tree('[{"a":1},
```

---

## Crash 320: `250e81858c490dbb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085813`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT *, * FROM (VALUES (CURRENT_TIMESTAMP)) AS a WHERE CURRENT_TIMESTAMP ORDER BY FALSE ASC NULLS FIRST; CREATE T
```

---

## Crash 321: `575b624df255bca9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085921`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP || FALSE COLLATE RTRIM GLOB FALSE COLLATE RTRIM GLOB FALSE COLLATE RTRIM GLOB FALSE COLLATE RTRIM GLOB FALSE COLLATE 
```

---

## Crash 322: `2b6d326fd1d86657` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086025`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (TRUE IS NOT FALSE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 323: `23d276c2a66940bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086095`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p (b) AS (SELECT dense_rank() OVER () AS p7_t2_8s) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 324: `c2ae843cd8c4e86b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086120`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE == CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 325: `7200fa5d76af7a23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086249`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c2 GENERATED ALWAYS AS (c1) NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 326: `8f089eaf2c4206a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086263`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP <= CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 327: `2bdb6c9d9a91364d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086289`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE AND NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 328: `4533e42224e82e76` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086307`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('[]') LEFT OUTER JOIN json_each('[1,2,3]') ON CURRENT_TIME GROUP BY CURRENT_DATE, NULL LIMIT perc
```

---

## Crash 329: `d4ab1a768f4f5371` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086320`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 330: `4d6cc7f64062dab9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086447`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p (b) AS (SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY NULL DESC, TRUE DESC)) SELECT * FROM p; CREATE TABLE seed_t
```

---

## Crash 331: `0870610f4a602428` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086469`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY CURRENT_DATE ASC NULLS LAST, CURRENT_TIME ASC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 332: `907d959f75ba7923` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086607`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (nullif(TRUE, NULL))); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 333: `6f049415b8b2c622` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086660`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP NOT LIKE TRUE) UNION SELECT CURRENT_TIMESTAMP AS zt31l053k44u17m2_a6b__hy___1__yz2k55_28__3_53l7r2_3g8c_29e2_u3wv_h_0
```

---

## Crash 334: `bdffcb6d8e2a7f4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086676`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT TRUE AS h7ck FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 335: `1941d4bea71fd6cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086691`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT cume_dist() OVER (PARTITION BY FALSE ORDER BY FALSE DESC NULLS FIRST ROWS BETWEEN CUR
```

---

## Crash 336: `cb0b3613bba0776d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086699`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP NOT LIKE CAST(67211236903697774959176252648547768059239273026.13620004E-9880087210710149825170218269537085263873 AS T
```

---

## Crash 337: `a72a0cd4c9186997` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000086705`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP NOT LIKE TRUE) UNION SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_TIME DESC ROWS BETWEEN UN
```

---
