# Crash Triage Report

**Total crashes:** 364  
**Unique crash sites:** 364  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 152 | 152 | 41% |
| Signal | 212 | 212 | 58% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `7df98c797759c317` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000207`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1); INSERT OR FAIL INTO p VALUES (TRUE NOT IN ((~CURRENT_DATE IS DISTINCT FROM TRUE - NULL IS NOT DISTINCT FROM CURRENT_DATE LIKE total_ch
```

---

## Crash 2: `429194b36ad07eee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000458`

```sql
SELECT round(0.01, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, a); REPLACE INTO p VALUES (CASE WHEN CURRENT_DATE THEN FALSE ELSE NULL END COLLATE NOCASE <> FALSE IS 
```

---

## Crash 3: `55b586a126d6783e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001466`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 9743271679436730492523564.0, c1 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN CHECK (abs(CASE WHEN C
```

---

## Crash 4: `ebff440f95423589` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001518`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 5: `446e6c37f25df433` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001626`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c2, c3); WITH RECURSIVE p AS NOT MATERIALIZED (WITH RECURSIVE p AS MATERIALIZED (SELECT *, *), 
```

---

## Crash 6: `7b9f597cb42c9612` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001826`

```sql
SELECT printf('%s', 4294967295, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER
```

---

## Crash 7: `f3d220ad7c85437c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001883`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 8: `4a85f6a4fb6f21cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001910`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 9: `133083a161322767` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001997`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 10: `53519ec3b59dec85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002119`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 11: `568dad6d62fc64db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002145`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%d', 2147483648, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((
```

---

## Crash 12: `9fa12fa3b1d6ea16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002167`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%d', 2147483648, ''); CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT IN
```

---

## Crash 13: `7efe0ebfbc619236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002214`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c1 INTEG
```

---

## Crash 14: `03502cc95c913615` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002238`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 15: `d8d25af6ea410f62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002244`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 16: `6f89fcbe4fd82836` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002296`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 17: `331363bdc63e04bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002960`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 18: `a26948ec4d26f80c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002971`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL
```

---

## Crash 19: `882f5469d861f87e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003329`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME ISNULL); SELECT printf('%.*g', 0, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 20: `2117ca826317eb5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003853`

```sql
SELECT printf('%lld', -9223372036854775808, 'Y11 _'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coal
```

---

## Crash 21: `31490e5b01a47e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004197`

```sql
SELECT printf('%.*d', 2147483648, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 22: `9e503044f710e18c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004550`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH t1 AS (VALUES (CURRENT_TIMESTAMP)) VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 23: `60a8b6fd31b09b72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 24: `7be3ab162301e9bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005474`

```sql
SELECT substr('N 4 b71', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVE
```

---

## Crash 25: `c2d0020fb8a660c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005522`

```sql
SELECT printf('%.*f', 4294967295, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 26: `d1493903c3c10a2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005912`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (RAISE(IGNORE)), a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 27: `9c2f806d79359ace` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006190`

```sql
SELECT printf('%.*e', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 28: `6e390d9a295b9dd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006514`

```sql
SELECT round(0.01, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 29: `2b1c84d686e2dfc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006884`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c3 INT GENERATED ALWAYS AS (NULL) VIRTUAL, c2 BLOB NOT NULL); VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 30: `67b4e4333997f893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006898`

```sql
SELECT round(-1e308, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 31: `911e0b51754162f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007743`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; SELECT -TRUE NOT NULL == RAISE(IGNORE) - CURRENT_TIME NOT BETWEEN dense_rank() 
```

---

## Crash 32: `5804c4615d3407e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007789`

```sql
SELECT printf('%u', 2147483647, '41U__-'); SELECT printf('%.*f', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 VALUES (FALSE == RAISE(IGNORE) NOT NULL <> 
```

---

## Crash 33: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007907`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 34: `77623a1390601d94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007940`

```sql
SELECT substr('-sU 2-1n1bu_', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, c2); VALUES (RAISE(IGNORE)) UNION SELECT q.* FROM s AS a GROUP BY
```

---

## Crash 35: `da7dea8b0ae3fa8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008172`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); SELECT q.*, CASE WHEN length(NULL & FALSE COLLATE NOCASE) FILTER (WHERE --FALSE) IN (WITH RECU
```

---

## Crash 36: `fb18d66a9c8b18f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008932`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(ROLLBACK, '-K ') FROM json_tree('{}') GROUP BY count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC RO
```

---

## Crash 37: `c41ca3dabc84ab21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008940`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(ROLLBACK, '-K ') FROM json_tree('{}') GROUP BY count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC RO
```

---

## Crash 38: `22f7cb0057705864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008949`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(ROLLBACK, '-K ') FROM json_tree('{}') GROUP BY count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC RO
```

---

## Crash 39: `d0f059d50e04666b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008958`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(ROLLBACK, '-K ') FROM json_tree('{}') GROUP BY count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC RO
```

---

## Crash 40: `b9171f6539e42547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008968`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT RAISE(ROLLBACK, '-K ') FROM json_tree('{}') GROUP BY count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC RO
```

---

## Crash 41: `0129d5169e9eca20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009009`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 42: `edd4137216d3c92e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009172`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIME AS ur_4; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 43: `4947b8aa8a3b4fbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009178`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE || CURRENT_TIMESTAMP COLLATE NOCASE * ~CURRENT_TIMESTAMP COLLATE RTRIM COLLATE BINARY AS ur_4; CREATE TA
```

---

## Crash 44: `fcf5579f14bdef91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009197`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT FALSE || FALSE AS ur_4; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 45: `26bd83ba4f5a1f3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009312`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM s WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE, CURRENT_TIME WINDOW w1 AS () LIMIT CURRENT_TIME; EXPLAIN 
```

---

## Crash 46: `865a41aad2ec7f14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013906`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3
```

---

## Crash 47: `747ffc7da1b12056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013917`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 48: `1ed43f9951e11f49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013928`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIME > RAISE(IGNORE) IS NOT CURRENT_DATE), a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE); CREATE TABLE
```

---

## Crash 49: `e9ab4f982698c0ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013935`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a
```

---

## Crash 50: `a47587a846859c12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013960`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL (VALUES (NULL)) AS f_4_wu_ FROM json_each('[1,2,3]'); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 51: `b961bd72ba81dfe5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015940`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); ANALYZE q; CREATE TABLE seed_a(c UN
```

---

## Crash 52: `db52e36a04874ba2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015946`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (FALSE))); PRAGMA integrity_check; CREATE TABLE
```

---

## Crash 53: `89e8590b0862cfa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015953`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT FALSE); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 54: `3b7374c82736460b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016006`

```sql
SELECT round(-1.0, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 55: `6a183f101e071e1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016013`

```sql
SELECT printf('%.*g', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 56: `4fb9af624cddcc38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016517`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE count(*) FILTER (WHERE TRUE) OVER (); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 57: `ec762fb602640dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016541`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 58: `ba7f84b3639743a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016582`

```sql
SELECT printf('%f', 9223372036854775807, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lea
```

---

## Crash 59: `2e4d2821be4a577e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019151`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (CURRENT_TIME)); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 60: `13d71bbc68be712b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022281`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) UNION ALL VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 61: `b4821bc01fbdeab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022289`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) UNION VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 62: `cc70bc3f41c31ef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022298`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (NOT CURRENT_DATE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 63: `168b331d6ed057d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022314`

```sql
SELECT printf('%x', -2147483648, 'wd_-_ -'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 64: `d2cbb97af240553e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022331`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 65: `d526da2b79869de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022341`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH t1 AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM json_tree('{"a":{"b":1}}'); CREATE TABLE s
```

---

## Crash 66: `ce6a002825587d49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022350`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL GROUP BY CURRENT_DATE WINDOW w1 AS () INTERSECT VALUES
```

---

## Crash 67: `c6968198070f3245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022378`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed
```

---

## Crash 68: `1a52ed8a736a5569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022395`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (CAST(CURRENT_DATE IS NULL & CURRENT_DATE AS BLOB)) EXCEPT VALUES (TRUE); CREATE TABLE s
```

---

## Crash 69: `56080913b7fa2b9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022401`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIME ORDER BY CURRENT_TIME ASC; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 70: `ab293d4f24b15c7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022408`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE COLLATE BINARY) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 71: `1d8b70b105562051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022416`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY NULL NOT NULL NOT IN 
```

---

## Crash 72: `67be3a280107a8ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022426`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (max(CURRENT_TIME) OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 73: `09fabbafad829f26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022451`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c3 GENERATED ALWAYS AS (a = -150242) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 74: `a5fd69215f5fd233` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022461`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 75: `0d280b1275c0406d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022498`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT X''); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 76: `c7cfff0c02e609f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022537`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT I
```

---

## Crash 77: `3e29cb4fb0c8604a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022555`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 78: `c50f2c70e60c1d70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022590`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH t1 AS (VALUES (CURRENT_TIMESTAMP)) VALUES (CURRENT_TIME) INTERSECT VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE TABL
```

---

## Crash 79: `cdc212e999319170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022690`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT TRUE IS NOT NULL AS a, * FROM json_tree(CURRENT_TIMESTAMP & CURRENT_TIME, '$[#-1]') WHERE a; CREATE TABLE see
```

---

## Crash 80: `8744d78ae06f37d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022706`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE FALSE GROUP BY CU
```

---

## Crash 81: `8315f44447079841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022897`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (p NOT INDEXED NATURAL LEFT JOIN json_tree('[1,2,3]')) IN
```

---

## Crash 82: `cb56dcdc807da4b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022922`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) UNION SELECT TRUE FROM json_tree('[{"a":1},{"b":2}]') WHERE FALSE GROUP BY CURREN
```

---

## Crash 83: `548aa2a7ec9f5b74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q (c3) VALUES (CURRENT_TIME / CURRENT_TIME); SELECT * FROM (p NOT INDEXED NATURAL LEFT JOIN p) NATURA
```

---

## Crash 84: `76a9299e60d7779f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026088`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q (c3) VALUES (CURRENT_TIME / CURRENT_TIME); VALUES (CURRENT_TIMESTAMP, CURRENT_TIME BETWEEN TRUE AND
```

---

## Crash 85: `3cbc60b0fa3fcb27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026235`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (p NOT INDEXED NATURAL LEFT JOIN p) NATURAL LEFT JOIN json_tree('[1,2
```

---

## Crash 86: `8814cdd9778ac48a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026249`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q (c3) VALUES (CURRENT_TIME / CURRENT_TIME); SELECT * FROM (json_each('{"a":1}')) NATURAL LEFT JOIN j
```

---

## Crash 87: `af1be4db5d76a75a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026990`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); REPLACE INTO p VALUES (NULL LIKE FALSE ESCAPE TRUE COLLATE BINARY); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 88: `007f6bf1bb09dcd8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028005`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 89: `20eb70ef813dbe8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028028`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 90: `d42e8602a8c35ee4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028222`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 91: `bb02c79dec768fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028250`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 92: `fa40e64335af35a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028266`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 93: `e975de69b22a22d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028277`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, b
```

---

## Crash 94: `8a310dab2bf644da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028438`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (CURRENT_DATE IS NOT NULL)); CREATE TABLE IF NOT EXISTS q(rowid REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c
```

---

## Crash 95: `da738cd8937777a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031767`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIMESTAMP > TRUE), a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME, CAST(CURRENT
```

---

## Crash 96: `4a7a48e9ce1eebb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031784`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIMESTAMP > TRUE), a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p SELECT ALL p.* FROM p NOT INDEXED ORDER BY F
```

---

## Crash 97: `bf03d094377ba4bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031835`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 98: `01caeaad38e46940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031845`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIMESTAMP > TRUE), a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME, CAST(CURRENT
```

---

## Crash 99: `e350d6cb92792f25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032358`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT -8351527711.56487063288955360); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 100: `f29a19aea9a9d18b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032736`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_DATE)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); SELECT * FROM p JOIN p s ON CURRENT_TIMEST
```

---

## Crash 101: `0a35f85516afa3fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032766`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_TIMESTAMP OR CURRENT_TIME)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); VALUES (CURRENT_TIMES
```

---

## Crash 102: `d7694816e7bea6de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032772`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_DATE)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); VALUES (CURRENT_TIME, CAST(CURRENT_DATE AS
```

---

## Crash 103: `35a65d5f034b9daf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032812`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_DATE)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); SELECT * FROM json_each('[{"a":1},{"b":2}]
```

---

## Crash 104: `ae5f4f20788d7809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032913`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_DATE)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE I
```

---

## Crash 105: `8e01f0864c674e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032934`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE TRUE 
```

---

## Crash 106: `ecf20573cdcade13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037891`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT NULL); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 107: `9db071819c61242e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038412`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (-75913713.6e-598451762381486) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 108: `d13821c5615700e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038430`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); SELECT TRUE IS NOT NULL AS a FROM p JOIN p s ON CURRENT_TIMESTAMP MATCH CURRENT_TIME; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 109: `1f20fe73901fbb36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038453`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q INDEXED BY c1; SELECT * FROM p JOIN p s ON CURRENT_TIMESTAMP MATCH CURRENT_TIME; CREATE TABL
```

---

## Crash 110: `18ed44cfa9d0e2d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038464`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT GENERATED ALWAYS AS (RAISE(IGNORE) || FALSE) STORED, a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); SELECT * FROM p JOIN p s ON CURRENT_TIMEST
```

---

## Crash 111: `184b4fa1c96dece3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038477`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w
```

---

## Crash 112: `00e2612087d78aec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038558`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT * FROM p JOIN p s ON CURRENT_TIMESTAMP MATCH CURRENT_TIME; CREATE TABLE seed_a(c UNI
```

---

## Crash 113: `26ef7b2810d9e706` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038899`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE FALSE GROUP BY RAISE(IGNORE) WINDOW w1 AS (
```

---

## Crash 114: `6e3f3af95a1627b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038922`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT rank() FILTER (WHERE NOT EXISTS (SELECT *)), * FROM json_tree('{"a":1}') GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; VA
```

---

## Crash 115: `a9d529dffbf73d65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038932`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT NULL LIKE NULL ESCAPE RAISE(IGNORE) AS w_d_ogjb862 FROM json_tree('[]') WHERE RAISE(IGNORE) UNION ALL SEL
```

---

## Crash 116: `7b2cceb2378b6e74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038962`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') GROUP BY +RAISE(IGNORE) LIMIT TRUE; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 117: `9dc1e736b49d61a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038971`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') GROUP BY CURRENT_TIMESTAMP LIMIT count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_D
```

---

## Crash 118: `bfbb2f6cbfd2a400` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038989`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN (json_tree('[1,2,3]') INNER JOIN json_tree('{"a":1}')) WHERE TRUE GROUP BY 
```

---

## Crash 119: `432b071a65249ed1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039006`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{}') , json_each('[]') USING (c3) GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; VALUES (NULL); CREATE T
```

---

## Crash 120: `0f61c5306d9fa944` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039027`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CAST(RAISE(IGNORE) <= ~CASE WHEN CURRENT_TIME THEN +CURRENT_TIMESTAMP END AS BOOLEAN) ISNULL AS m__ FROM 
```

---

## Crash 121: `551fbd10efecbc78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039037`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE < CURRENT_TIME <= CASE NULL WHEN CURRENT_TIMESTAMP THEN (NULL) END & NULL COLLATE NOCASE ISNULL == ~N
```

---

## Crash 122: `7a6805890abb4cac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039111`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b R
```

---

## Crash 123: `ed848a65fcbd465b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041490`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (VALUES (count() FILTER (WHERE FALSE) OVER ())) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 124: `034c97ddba1d2848` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041641`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (WITH p AS (SELECT *) VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 125: `1f10af9a09fe2270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044763`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 126: `fd6a2c5b77258cb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045168`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 127: `a3460931a3b53c82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045484`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQ
```

---

## Crash 128: `3f6b0f2c6006f3b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047241`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) UNION ALL VALUES (count(*) FILTER (WHERE FALSE) OVER (ORDER BY 
```

---

## Crash 129: `cfc9aa5d95d40c69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052290`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN, c2 BOOLEAN NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME, FALSE); SELECT NOT CURRENT_TIME; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 130: `463011eb2b0c6885` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054795`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL IS NOT NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a
```

---

## Crash 131: `085decf41ae3b808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NUL
```

---

## Crash 132: `c1c320a36fba12f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054830`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (dense_rank() OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST, TRUE ASC NULLS FIRST)); CREAT
```

---

## Crash 133: `a566a60a0d02d62c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054917`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT N
```

---

## Crash 134: `14089482d69490cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055653`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS
```

---

## Crash 135: `7e695c9e428edc62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055826`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 028.5E4754621173497); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 136: `de77ddb41068d4b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056015`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT 62251698136505207626644430018369409284.298574356695524911054967074056828784001473972653795337430342237994987164617050727333156436801857173343581981
```

---

## Crash 137: `47e0824bfc340bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056120`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS
```

---

## Crash 138: `a7ef28c6237bf60c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056363`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE INDEX 
```

---

## Crash 139: `39a0e7589ab5c355` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056604`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p SELECT ALL * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS FIRST LIMIT FALSE; PRAGMA integrity
```

---

## Crash 140: `b459c12b3187ca96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059666`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT CURRENT_TIMESTAMP IS FALSE AS g7ty___ FROM p WHERE EXISTS (VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3
```

---

## Crash 141: `2e744e9b103e46fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060402`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (VALUES (count() FILTER (WHERE (SELECT NULL AS j_6___z)) OVER ())) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 142: `714e394e73dba153` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060414`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (SELECT TRUE FROM json_each('{}') WHERE CURRENT_TIME << CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS ()) SELECT
```

---

## Crash 143: `7a3451c7a5961edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060422`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (VALUES (count() FILTER (WHERE FALSE) OVER ())) SELECT p.c3, * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 144: `9b68d1d532e411de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060467`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); WITH RECURSIVE p (c3) AS (VALUES (count() FILTER (WHERE FALSE) OVER ())) SELECT CURRENT_DATE, count(*) FILTER (WHERE CURRENT_TIME) OVER () AS j_
```

---

## Crash 145: `3d55f4dec178bb41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061826`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 146: `eb38b2d940250c2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063323`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT X'aDdaee'); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 147: `434bd5f98da3b0f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065530`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT 8361769158311026647185654610971625249336189911782486843396467207729436857002.2700204490701279350204230923070071029890291832215519282708936606399
```

---

## Crash 148: `98f5950d54eb6e78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065554`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT TRUE IS FALSE IS FALSE AS g7ty___ FROM p WHERE EXISTS (VALUES (NULL)); CREATE TABLE 
```

---

## Crash 149: `ab8d2a36517f9248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065571`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT * FROM p JOIN p s ON RAISE(IGNORE) IS NULL AND FALSE OR NULL; CREATE TABLE seed_a(c 
```

---

## Crash 150: `fec4f8a0f2c332b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065577`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT *, count(*) FILTER (WHERE CURRENT_TIME) OVER () AS j_9_8_nx2_r_q__32a__p0_6e_4923_ry
```

---

## Crash 151: `33210c5fac195ef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065599`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); SELECT * FROM p JOIN p s ON FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 152: `6eb68fdaf7a640c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065621`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM p INNER JOIN (json_tree('{}') , json_e
```

---

## Crash 153: `cd531a791575a8dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001265`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 154: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001860`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 155: `3335d55cd625430e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002138`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 156: `653460eb2dbf8b51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002198`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 157: `6c03293f36de47ce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002488`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT, rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1
```

---

## Crash 158: `37167a095c9c2394` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002539`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE, rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CR
```

---

## Crash 159: `0e5b854e5714f64c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002557`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 160: `26070b11b201575f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002564`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE, rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 161: `d249dcf4ab247d30` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002577`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 162: `2e82da405ee64df6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002585`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 163: `188721c2d822ae4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003320`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME ISNULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 164: `3e9ac90dc2c09fc4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003651`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL <> CURRENT_TIME)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN Q
```

---

## Crash 165: `c24b47dcf2d2e2a4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003658`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CRE
```

---

## Crash 166: `b6300c25cb2f06a5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003664`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CURRENT_TIME)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTA
```

---

## Crash 167: `65e4c3fbec7ffd1f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003675`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE see
```

---

## Crash 168: `d3063d787f8fb8ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003682`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_
```

---

## Crash 169: `e4a03009a31e349b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003704`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 170: `d94e6df69d4354b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004037`

```sql
SELECT printf('%.*g', 2147483648, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 171: `2889b31276c2f305` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004277`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (FALSE COLLATE BINARY COLLATE NOCASE GLOB FALSE = CURRENT_TIMESTAMP COLLATE BI
```

---

## Crash 172: `3e288c1511b7fb34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (FALSE GLOB FALSE = CURRENT_TIMESTAMP COLLATE BINARY IS NOT NULL IS NULL); PRA
```

---

## Crash 173: `4f873937f0a0a17f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004305`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (TRUE = CURRENT_TIMESTAMP COLLATE BINARY IS NOT NULL IS NULL); PRAGMA quick_ch
```

---

## Crash 174: `e0b5feafd8fc0b94` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004312`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = CURRENT_TIMESTAMP COLLATE BINARY IS 
```

---

## Crash 175: `6edefee9cde43d92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (FALSE COLLATE BINARY COLLATE NOCASE GLOB FALSE = NULL); PRAGMA quick_check; C
```

---

## Crash 176: `f72a92fcaee188b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004344`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (NULL GLOB FALSE = NULL); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 177: `dabef448fc71b713` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004380`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE = TRUE); PRAGMA quick_check; CREATE TABLE seed_t1
```

---

## Crash 178: `b6b48c42c8560f00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004452`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME = CURRENT_TIMESTAMP COLLATE BINARY IS NOT NULL IS NULL); PRAGMA 
```

---

## Crash 179: `7dc6a36f95e5d1c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004460`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME = CURRENT_TIMESTAMP COLLATE BINARY IS NOT NULL); PRAGMA integrit
```

---

## Crash 180: `d7cc4f04cc81c0d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004467`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME = CURRENT_TIMESTAMP IS NULL); PRAGMA integrity_check; CREATE TAB
```

---

## Crash 181: `2e665ef4000bc894` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004892`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 182: `39804f4c0167e993` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004898`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE NULL IS NOT FALSE
```

---

## Crash 183: `33f48cf47c1d8a7e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004904`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE FALSE GROUP BY CU
```

---

## Crash 184: `3ee8d6e1ec2f7fc7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004916`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 185: `ff4402938a5d4652` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004925`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL IS NOT FALSE GROUP BY CURRENT_
```

---

## Crash 186: `1aa926fed45542f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004931`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE GROUP BY CURRENT_DATE 
```

---

## Crash 187: `81b65e6105c2abad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004937`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE TRUE GROUP BY CURRENT_DATE WINDOW w
```

---

## Crash 188: `a7dee3559c72e31a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004951`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 189: `f2cbee4312c59e79` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005233`

```sql
SELECT printf('%.*e', -9223372036854775808, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 190: `03484d6001e67260` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005951`

```sql
SELECT printf('%.*s', -2147483648, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 191: `755ca0b56edeb3c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005970`

```sql
SELECT printf('%.*f', -2147483648); SELECT substr('uQ-v-Z _1-', -2147483649, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSER
```

---

## Crash 192: `a753a40ee9531f95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013606`

```sql
SELECT substr('uQ-v-Z _1-', 9223372036854775807, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(5
```

---

## Crash 193: `b3b7d10cffb86ce5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013623`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) CHECK (FALSE IS NOT TRUE)); CREATE TABLE IF NOT EXISTS q(b NUMERIC); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 194: `10ba75ea272a8064` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013629`

```sql
SELECT substr('uQ-v-Z _1-', -9223372036854775808, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 195: `8dea63516a3e1d91` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013662`

```sql
SELECT substr('uQ-v-Z _1-', -2147483649, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 196: `56f85d9ed456550b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013709`

```sql
SELECT printf('%.*s', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 197: `8688e5a497ef7e7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013755`

```sql
SELECT printf('%.*g', -2147483648, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 198: `3e651992c6343a4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013777`

```sql
SELECT printf('%.*s', -2147483649, -0.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 199: `7a47a917d2818e8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013785`

```sql
SELECT round(-1.0, -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3
```

---

## Crash 200: `fd630297824fe71e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013800`

```sql
SELECT substr('', -1, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 201: `19f8fc2e6923602e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013806`

```sql
SELECT printf('%.*d', -1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed
```

---

## Crash 202: `7841f2a1fb26a01c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013813`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT X''); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 203: `fbab02c5c880ff6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013838`

```sql
SELECT printf('%.*s', -2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 204: `f9c0acd32604a92b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013873`

```sql
SELECT printf('%.*s', -2147483648, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 205: `7c5cedd36bddcbb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019957`

```sql
SELECT printf('%.*d', -9223372036854775808, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 206: `b0d5c961b5a94c29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019981`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN FALSE PRECEDING AND CURRENT_DATE FOLL
```

---

## Crash 207: `7f32cb304426983f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019991`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT ''); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 208: `6239d64ae1bcd177` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020001`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('[1,2,3]') NATURAL LEFT JOIN json_tree('{"a":1}') WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS () O
```

---

## Crash 209: `ad22bd5ce62a83fe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022082`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); INSERT INTO p DEF
```

---

## Crash 210: `c16e43912d2458e0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022970`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 211: `865bafc4aec43fd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022998`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE NULL - CURRENT_TI
```

---

## Crash 212: `d8e82406acf5e6f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023008`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 213: `c8df99037a892e63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023018`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"
```

---

## Crash 214: `e7661940a0a53c5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023032`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CASE CURRENT_TIME
```

---

## Crash 215: `d90b1a8d718422b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023042`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 216: `c8db4b9f50bf3885` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023050`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT OR FAIL INTO p VALUES (TRUE IN (VALUES (FALSE))); VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1
```

---

## Crash 217: `c3e410480d77a8ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023062`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN (p) WHERE CURRENT_TIMESTAMP IS NOT FALSE GRO
```

---

## Crash 218: `ce3e993f7b0f36c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_tree('{}') , p AS i5_5g_zh86_033__m_y_6l_8945h_____u
```

---

## Crash 219: `1e25159edb348def` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023075`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (p NOT INDEXED NATURAL LEFT JOIN (p NOT INDEXED NATURAL L
```

---

## Crash 220: `21398e14a946af23` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023095`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":{"b":1}}') WHERE CURRENT_TIM
```

---

## Crash 221: `e4f6b753938a6844` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023142`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('[{"a":1},{"b":2}]') WHERE CURRENT
```

---

## Crash 222: `1c97f01d66bc3ca7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023165`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT p.* FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP 
```

---

## Crash 223: `b30fa2fbeae5b352` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023189`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 224: `7509ff34056f8775` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023199`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE CURRENT_TIMESTAMP
```

---

## Crash 225: `667abdae9ef4ab20` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023231`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 226: `2923aaff03eb2141` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023342`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{"a":1}') WHERE CURRENT_TIMESTAMP IS NOT TRUE 
```

---

## Crash 227: `1a1ef9faa13865a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023378`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_tree('[]') INNER JOIN json_each('{"a":1}') WHERE CUR
```

---

## Crash 228: `e9b3195faa29e573` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023384`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (json_tree('[{"a":1},{"b":2}]')) INNER JOIN json_each('{"
```

---

## Crash 229: `10fd211e52e2bcab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023391`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (p NOT INDEXED NATURAL LEFT JOIN (json_each('{}'))) INNER
```

---

## Crash 230: `b2bf556b6c0a77b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023397`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (p NOT INDEXED NATURAL LEFT JOIN (p NOT INDEXED NATURAL L
```

---

## Crash 231: `8b0b4e6013241ef4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023403`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p NOT INDEXED NATURAL LEFT JOIN (p NOT INDEXED NATURAL LE
```

---

## Crash 232: `8d2e01d3ee9f64fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023410`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED WHERE CURRE
```

---

## Crash 233: `23aba76fa741e26a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023544`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE BETWEEN CURRENT_TIMEST
```

---

## Crash 234: `ace339e04ff4722c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023593`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT -75913713.6e-598451762381486 / (CURRENT_DATE) FROM json_each('{}') 
```

---

## Crash 235: `8713b38cf656ed5a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023603`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (percent_rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 236: `dfc3e7ef6eef09ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023622`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL IS NOT CURRENT_TIMESTAMP > TRU
```

---

## Crash 237: `332d5c27c3af0333` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023636`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (NULL IS NOT FALSE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL IS NOT FALSE GROU
```

---

## Crash 238: `dfaa16181b748b40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023647`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (SELECT *), q AS (VALUES (FALSE)) SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) E
```

---

## Crash 239: `c6750937e26d2be2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023661`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_TIMESTAMP COLLATE BINARY IS
```

---

## Crash 240: `0b86e98d3b5a33a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023670`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('[1,2,3]') WHERE NULL IS NOT FALSE GROUP BY CUR
```

---

## Crash 241: `b82f3b04906c2a2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023676`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL IS NOT CURRENT_TIME MATCH TRUE
```

---

## Crash 242: `2db2fc357bd75146` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023693`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT FALSE NOT IN (TRUE) FROM json_each('{}') WHERE NULL IS NOT FALSE GR
```

---

## Crash 243: `f169b5119a9b99d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023705`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p NOT INDEXED NATURAL LEFT JOIN (json_tree('[1,2,3]') NAT
```

---

## Crash 244: `49a14e83e482704c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023823`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL IS NOT NULL IS NOT NULL IS NOT
```

---

## Crash 245: `1c2a736488341257` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023899`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_TIMESTAMP > TRUE GROUP BY C
```

---

## Crash 246: `18955048cc0d74df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023948`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (NULL - CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME) EXCEPT SELECT TRUE FROM
```

---

## Crash 247: `c8e693c9f24a2d26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023955`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (FALSE || FALSE) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE GROUP BY CUR
```

---

## Crash 248: `62645c70e82292db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023970`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT 22295851.10716044E+24); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT
```

---

## Crash 249: `b3424c366004c182` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023992`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME * FALSE); VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_D
```

---

## Crash 250: `c4cd74f73d4b55d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024001`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT FALSE); INSERT INTO p SELECT ALL * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS FIRST LIMIT FALSE
```

---

## Crash 251: `a64f4da90034286f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024018`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE NULL - CURRENT_TIME BETWEEN CURRENT
```

---

## Crash 252: `e8692abfcaa318d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024037`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE GROUP BY CURRENT_DATE 
```

---

## Crash 253: `c1d85dad4f99c0bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024115`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT 0.0); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE GROUP BY CURRENT_DA
```

---

## Crash 254: `be6fa5ba5ac664c5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024213`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT EXISTS (SELECT CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE TRUE GRO
```

---

## Crash 255: `2ce8a85ca9af4812` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024225`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIMESTAMP > TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE TRUE GROUP BY C
```

---

## Crash 256: `d0f98b119e479c36` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024233`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 257: `885053d76fcd42cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024255`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM (p NOT INDEXED NATURAL LEFT JOIN p) NATURAL LEFT JOIN (js
```

---

## Crash 258: `7d724f3e4ca93d01` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024262`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p VALUES (NULL < CURRENT_DATE); VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE TRUE GROUP BY CURRENT
```

---

## Crash 259: `857bfa63fb95a8e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024288`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM json_each('{}') WHERE TRUE GROUP BY CURRENT_DATE WINDOW w
```

---

## Crash 260: `22b5497a8f514d37` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024309`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT FALSE >= CURRENT_DATE FROM json_each('{}') WHERE TRUE GROUP BY CURR
```

---

## Crash 261: `7bf8aa445211dfe5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024452`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p NOT INDEXED NATURAL LEFT JOIN p WHERE TRUE GROUP BY CUR
```

---

## Crash 262: `f823627ca319dc84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024484`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN UNBOUNDED PRECEDIN
```

---

## Crash 263: `ca7344fdf4d3d295` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024491`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) EXCEPT SELECT TRUE FROM p INNER JOIN json_each('{"a":1}') WHERE X'b4' GROUP BY CU
```

---

## Crash 264: `3fc5e01a84067a8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024527`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 265: `473cd9d28746044a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024543`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED INNER JOIN (json_tree('[1,2,3]') NATURAL LEFT JOIN json_tree('{"a":1}'))
```

---

## Crash 266: `87a0e9d57ce96484` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024560`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (count() FILTER (WHERE FALSE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 267: `f615eb6918215a7c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025808`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 268: `db04b2669f816fcc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025838`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT -8351527711.56487063288955360); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREA
```

---

## Crash 269: `112ff706bbac14da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000025859`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP IS NOT FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 270: `348ee93d6aca0462` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027208`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL DEFAULT -997672); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 271: `a6b32851c2856099` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028019`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 272: `bf9ba5d1b93f264b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028776`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP >> CURRENT_TIMESTAMP = TRUE); PRAGMA quick_check; CREATE TA
```

---

## Crash 273: `97c85436d5472038` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028789`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = CURRENT_DATE & NULL % NULL < CURRENT
```

---

## Crash 274: `a0e9c87fcdbb5014` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028826`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = TRUE); ANALYZE q; CREATE TABLE seed_
```

---

## Crash 275: `7744838aef16d9cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028841`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB (SELECT * FROM q NOT INDEXED) = TRUE); PRAGM
```

---

## Crash 276: `3c99b0c385075ab5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028876`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CASE NULL WHEN CURRENT_DATE THEN FALSE END = TRUE); PRAGMA quick_check; CREAT
```

---

## Crash 277: `df6892faf0733698` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028921`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT X''); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = TRUE); PRAGMA quick_check
```

---

## Crash 278: `e1e161195065e395` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028935`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (NOT 305.74 COLLATE BINARY = TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c
```

---

## Crash 279: `c77933b0a10545b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028982`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'EADaFA8a'); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = TRUE); PRAGMA quick
```

---

## Crash 280: `c4ba8d23a74fe8e2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028994`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = TRUE = TRUE = TRUE = TRUE = TRUE = T
```

---

## Crash 281: `2e9060e87e8c00fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029012`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE NOCASE GLOB FALSE = TRUE); PRAGMA quick_check; CREATE TA
```

---

## Crash 282: `13fe4899068f9dbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029073`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP GLOB FALSE = TRUE % NULL < CURRENT_TIMESTAMP); PRAGMA quick
```

---

## Crash 283: `292e5dcb6576f84d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP GLOB FALSE = TRUE % CURRENT_TIME); PRAGMA quick_check; CREA
```

---

## Crash 284: `ef1b37c10d7a6214` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029137`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (TRUE BETWEEN CURRENT_TIME AND FALSE GLOB FALSE); PRAGMA quick_check; CREATE T
```

---

## Crash 285: `58363486755c1d45` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029147`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) EXCEPT SELECT * ORDER BY CURRENT_TIME ASC NULLS LAST; INSERT OR REPLACE INTO p VALUES (NULL GLOB FALSE); PRAGMA quic
```

---

## Crash 286: `bc4e75db62764b60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029201`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL DEFAULT -0); INSERT OR REPLACE INTO p VALUES (NULL GLOB FALSE); PRAGMA quick_check; CREATE TABLE seed_t1
```

---

## Crash 287: `48468504bf042b77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029219`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL GLOB FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 288: `78cdc6fb6b4844f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029290`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (NULL GLOB FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 289: `8661059a8986fc09` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029329`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT -88775380514096849426210492799947690082274793000099.3702055735); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1
```

---

## Crash 290: `5742eddbc1b3ceba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029440`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('[]') LIMIT count(TRUE) FILTER (WHERE CURRENT_TIMESTAMP) OVER () OFFSET CURRENT_DATE; INSERT OR REPLA
```

---

## Crash 291: `385b11128f1fe400` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029492`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT OR REPLACE INTO p VALUES (0.0 GLOB FALSE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 292: `0d2a0f6dedd7ce5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{}') , p AS i5_5g_zh86_033__m_y_6l_8945h
```

---

## Crash 293: `2c62abe507a6b1d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031138`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, a FLOAT UNIQUE, c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid REAL UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE
```

---

## Crash 294: `cf5aef1e5a2ed732` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033492`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CASE WHEN TRUE THEN NULL ISNULL ELSE CURRENT_TIMESTAMP END)); INSERT OR FAIL INTO q VALUES (CURRENT_DAT
```

---

## Crash 295: `d8a05b2895da27f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033500`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL < CURRENT_TIMESTAMP)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CUR
```

---

## Crash 296: `5e73db589f8be94c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033521`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT GENERATED ALWAYS AS (RAISE(IGNORE) || FALSE) STORED, a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL <> CURRENT_TIME)); INSERT OR FAI
```

---

## Crash 297: `c57a3e547c4a0f5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033529`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL <> CURRENT_TIME)); INSERT OR REPLACE INTO p VALUES (-CURRENT_DATE IN (VALUES (FALSE))); EXPLAIN QU
```

---

## Crash 298: `247f0bbf63ef2bb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033540`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER GENERATED ALWAYS AS (NULL >= RAISE(IGNORE) | NULL AND RAISE(IGNORE)) VIRTUAL, c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL <> CURREN
```

---

## Crash 299: `1f50196a3f6cbb8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033565`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL <> CURRENT_TIME)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT
```

---

## Crash 300: `e5dca70998ca5dd3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL)); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM json_each('{"a":1}'); CREATE TABLE seed_t1
```

---

## Crash 301: `ac760cdc3932bcbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL)); INSERT OR ABORT INTO q VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); C
```

---

## Crash 302: `6113f0b588911f2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034077`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (TRUE OR CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_each('[{"a"
```

---

## Crash 303: `304e05937378de81` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034087`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (TRUE OR CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}')
```

---

## Crash 304: `792f332ee9e7e49e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034116`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (TRUE OR CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; SELECT ALL * FROM p NOT INDEXED ORDER BY FALSE DE
```

---

## Crash 305: `1f02c04ee2aa1e3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034130`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (TRUE OR CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (json_tree('[1,2
```

---

## Crash 306: `36013aa18f8fc83f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040684`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE) INTERSECT SELECT TRUE FROM json_each('{}') WHERE CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE
```

---

## Crash 307: `4136f75fa5b61a4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042110`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 308: `455071c544a0ca21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042310`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); REPLACE INTO p VALUES (NULL LIKE FALSE ESCAPE NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 309: `03ad7e960a9df4c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042332`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP OR CURRENT_TIME); PRAGMA integrity_check; CREATE 
```

---

## Crash 310: `e211a3422977b736` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042355`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT OR FAIL INTO p VALUES (-75913713.6e-598451762381486 / CURRENT_DATE); PRAGMA integrity_check
```

---

## Crash 311: `ebcc1340a6f79753` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC GENERATED ALWAYS AS (TRUE) STORED, c3 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRA
```

---

## Crash 312: `b22a0f2bc3b3b406` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042617`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREA
```

---

## Crash 313: `54c07b99d5cfb537` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042626`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); WITH RECURSIVE s AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_DATE); 
```

---

## Crash 314: `fd103fe80b8588fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043050`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (CAST(TRUE AS BLOB) <> CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE s
```

---

## Crash 315: `45f737ce641ffef2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043058`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT INTO q (rowid) VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 316: `f9ca6438493da935` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043086`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'dcfb2beE602c'); CREATE TABLE IF NOT EXISTS q(rowid FLOAT PRIMARY KEY, c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREA
```

---

## Crash 317: `d88ce2eef1261d52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044433`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 318: `19e0a6fa124e64ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045141`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE IN (VALUES (FALSE)) IN (VALUES (FAL
```

---

## Crash 319: `6ccdbf00cce70503` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045149`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP IS NOT TRUE); PRAGMA integrity
```

---

## Crash 320: `6c4d56b5f440cf35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045159`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 'e4____e4kV_C  -jv '); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 321: `c73e7b41e29026d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045179`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 322: `ff0871181fb0149d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045189`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT -88775380514096849426210492799947690082274793000099.3702055735); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 323: `7146ace538c31659` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 324: `e99ed65bdd0abfd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 028.5E4754621173497); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 325: `d7c1ce4e3a2d17ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045279`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT 62251698136505207626644430018369409284.298574356695524911054967074056828784001473972653795337430342237994987164617050727333156436801857173343581981
```

---

## Crash 326: `b6c1579e7fc05e99` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045321`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 327: `e1e2b982b508de29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 328: `be514a012b17c82a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046286`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); WITH p AS (SELECT *), r AS (VALUES (FALSE)) SELECT ALL * FROM json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 329: `f7683a4d787d0cea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047850`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIME, TRUE <= TRUE | CURRENT_TIMESTAMP NOTNULL, TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 330: `5eef2310745f2446` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048038`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT '-Htm_W__Bg1'); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 331: `0b3012f7e8a93b78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051945`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT X'826ccE'); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 332: `800e9042f130d50c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052001`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT '-Htm_W__Bg1'); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT count(*) FILTER (WHERE TRUE) OVER (), count(*) FILTER (WHERE CURRENT_TIME) OVER () AS j_9_8_n
```

---

## Crash 333: `8bf36ca94a2bd1ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052016`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT '-Htm_W__Bg1'); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN (json_tree('[1,2,3]') NATURAL LEFT JOIN json_tree('{"a":1}')) W
```

---

## Crash 334: `64399b67e90b7754` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052151`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, count(*) FILTER (WHERE CURRENT_TIME) OVER () AS j_9_8_nx2_r_q__32a__p0_6e_4923_ry_o9v62_128i9j4s8_
```

---

## Crash 335: `139a608ddc9b080c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052173`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 336: `8990af051fe59d87` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000052205`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT '-Htm_W__Bg1'); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') ORDER BY FALSE, CURRENT_TIME, CURRENT_DATE DESC; CREATE
```

---

## Crash 337: `ad06eae565f0e37f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053227`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_DATE | CURRENT_TIME, CURRENT_TIME, CAST(NULL AS DATE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 338: `8f20be9349ab440c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053240`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CAST(FALSE AS BOOLEAN) IS CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 339: `ea6ae4bfc65e8f38` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053277`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (count(TRUE) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 340: `0900c68f196fd350` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053289`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_DATE | FALSE || CURRENT_TIME, TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 341: `c11b5894f5534455` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055616`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT -47188); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 342: `50b5f480aa856bae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'fc6DdE3feA'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 343: `d7f387f3eb041ffc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055728`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER N
```

---

## Crash 344: `e52cf936020c7c01` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055816`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 028.5E4754621173497); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 345: `1d9a94eb2a391722` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055855`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM json_each('{"a":{"b":1}}') WHERE RAISE(IGNORE) GROUP BY CURRENT_TIME WINDOW w1 AS (), w2 AS (); 
```

---

## Crash 346: `153d46adfde23c7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055928`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 028.5E4754621173497); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 347: `df3d140efd3f3b8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056763`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE INDEX IF NOT EXISTS i
```

---

## Crash 348: `54bc69d3bce4de51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057724`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'dcfb2beE602c'); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 349: `72d77f440fc84bd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057819`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT ' 5i_3  9'); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 350: `380f3873871f564c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058294`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT OR ABORT INTO p VALUES (X'BDba45'); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 351: `53c4329a09bd5431` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058362`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL DEFAULT X'Cddec2CdEA67'); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP OR CURRENT_TIME); PRAGM
```

---

## Crash 352: `10ba313f0ac4b5ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058465`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT TRUE IS NOT NULL AS a FROM p WHERE EXISTS (SELECT DISTINCT * FROM p INNER JOIN (json_tree('{}') , p AS i5_5g_zh86_033__m_y_6l_8945h___
```

---

## Crash 353: `8ea499315518b2d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059074`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) FILTER (WHERE CURRENT_TIME) OVER () AS j_9_8_nx2_r_q__32a__p0_6e_4923_ry_o9v62_128i9j4s8_s36p0r87
```

---

## Crash 354: `e120ea96fbbdfe94` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060200`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE TABLE IF NOT EX
```

---

## Crash 355: `154389ff3ed0239b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065543`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, b GENERATED ALWAYS AS (a = -914) NOT NULL UNIQUE, a NUMERIC NOT NULL); SELECT * FROM p JOIN p s ON FALSE; CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL
```

---

## Crash 356: `5f9edfb6f12dde59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069349`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM (p NOT INDEXED NATURAL LEFT JOIN p) NATURAL LEFT JOIN json
```

---

## Crash 357: `48d4e895f30fd53e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069368`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CAST(CURRENT_TIME AS INT) != p._rowid_)); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{"a":{"b"
```

---

## Crash 358: `c9a862038937a4de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069390`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM (json_tree('[1,2,3]') NATURAL LEFT JOIN json_tree('{"a":1}
```

---

## Crash 359: `112d83ef8df5beb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069399`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN (p AS a NATURAL LEFT JOIN 
```

---

## Crash 360: `d1c992b36e3d7d46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069409`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO p SELECT CURRENT_DATE AS b1e2__5_d598__oa6b___8f_2_ UNION SELECT TRUE FROM p INNER JOIN json_each('
```

---

## Crash 361: `66ae01cfb1727524` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069416`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p AS o_qk0______k15___7yh8__8xi82dn79m5_9_d4n_47_4 WHERE C
```

---

## Crash 362: `fd7f1e66cd4bdbd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069444`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p INNER JOIN json_each('{"a":{"b":1}}') WHERE CURRENT_TIME
```

---

## Crash 363: `c86bc907b721b2f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070284`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (NULL < CURRENT_TIMESTAMP)); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); SELECT * FROM json_tree('[{"a"
```

---

## Crash 364: `3cc07ad06ca780b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000070453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER CHECK (~NULL)); INSERT INTO q DEFAULT VALUES; SELECT TRUE FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_DATE 
```

---
