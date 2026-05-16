# Crash Triage Report

**Total crashes:** 67  
**Unique crash sites:** 67  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 67 | 67 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `970a1302910a4c3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000463`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3); INSERT OR REPLACE INTO p VALUES (CASE +NULL IS RAISE(IGNORE) + CURRENT_DATE NOT NULL WHEN 0 THEN CAST(TRUE LIKE ~FALSE > TRUE NOT NULL
```

---

## Crash 2: `5997ab856186d89c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000714`

```sql
SELECT printf('%.*d', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, a, c1, c2); INSERT INTO q (b, c2, c3, c2, a, c3) VALUES (CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_DATE ELSE T
```

---

## Crash 3: `fe4cfe9b1f0ba9f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001382`

```sql
SELECT substr('6-_ b-HP_76_g-', -2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.*, p.*, q.* FROM t1 NATURAL JOIN t2 WHERE TRUE NOT BETWEEN (FALSE) AND NULL REGEXP 
```

---

## Crash 4: `07e0617543e17d63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001777`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3, c1, _rowid_); INSERT INTO p VALUES (count(*) IS DISTINCT FROM +jsonb_patch('{"a":{"b":1}}', '[]') OVER (PARTITION BY CURRENT_TIMESTAMP,
```

---

## Crash 5: `685d835d959069ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003226`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 6: `f92066341025e1a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003248`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT CURRENT_DATE, c2 INTEGER NOT NULL); CREATE TABLE IF NOT EX
```

---

## Crash 7: `8777ab4b5da6dbe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003265`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT rou
```

---

## Crash 8: `503ab90a40e6392a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003271`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER); EXPLAIN QU
```

---

## Crash 9: `47f1be19e88ffeb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003288`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-9223372036854775808)); SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 10: `2bb84390368cc49d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003296`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); VALUES
```

---

## Crash 11: `9a646d94d8c28243` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003416`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME); SELECT round(0.0, 2147483647); CREATE VIRTUAL TA
```

---

## Crash 12: `5bbca9f5c504ef1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003491`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE); SELECT round(0.0, 2147483647); CREATE VIRTUAL TA
```

---

## Crash 13: `b9a45a8b0a63598f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007260`

```sql
SELECT printf('%llu', -9223372036854775808, '-_I'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CASE WHEN CASE RAISE(IGNORE) WHEN RAISE(IGNORE) THEN CURRENT_DATE END NOT NULL THEN 
```

---

## Crash 14: `0e4b16ad454afbac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007272`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CASE WHEN CASE RAISE(IGNORE) WHEN RAISE(IGNORE) THEN CURRENT_DATE END NOT NULL THEN CURRENT_TIME OR TRUE ELSE C
```

---

## Crash 15: `b0e15ddf0e340a59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008190`

```sql
SELECT printf('%.*f', -2147483648, 0.0); SELECT substr('R Qy88_g-Mh', 2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT +CURRENT_TIME UNION 
```

---

## Crash 16: `94a02119a3193b4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008249`

```sql
SELECT printf('%f', 9223372036854775807, '-Fr--_a--b87IZ _B'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2); SELECT q.* FROM (SELECT CURRENT_TIMESTAMP AS f_vr_auy___a_yl_je__d_1s7v
```

---

## Crash 17: `bcaef559f37d6373` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008778`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 18: `4cf8cc058ce5d0d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009225`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 19: `0b9f83f1d708a502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009248`

```sql
SELECT printf('%.*f', -9223372036854775808, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, b); SELECT ALL TRUE <> -RAISE(IGNORE) IS NULL AS c FROM json_tree('{"a":{"b":1}}') , (SELE
```

---

## Crash 20: `5a7fd2b055c29ad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017592`

```sql
SELECT substr('1---W-N356', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT ALL NULL, p.*, q.*, RAISE(IGNORE) COLLATE BINARY ->> NULL AS v FROM jsonb_tr
```

---

## Crash 21: `f9c833a36053e053` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019350`

```sql
SELECT substr('9 i-_yE_ 6z__QSu-_T', 4294967295, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (CURRENT_DATE & CASE WHEN CURRENT_DATE THEN NULL END NOT IN (FALSE C
```

---

## Crash 22: `a070b44c7061060d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020250`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, c2); SELECT EXISTS (SELECT C
```

---

## Crash 23: `f5e1521c0798ecf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022042`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (NULL) UNION ALL SELECT FALSE AS s0lw_i6s_325_s63v_1_5__d1g_ta_93a_ob_g9_a_5_568q2ahh0___1i_409_q___18_u____9u3r6x569i5lakl_di_0_04___e__52
```

---

## Crash 24: `83db0de28a71c0da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027098`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 VALUES (CURRENT_TIMESTAMP != (TRUE NOT IN (CURRENT_TIME) NOT LIKE CURRENT_TIMESTAMP %
```

---

## Crash 25: `75ea104877cbe5a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028966`

```sql
SELECT printf('%.*f', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES ((unicode(-NULL NOT BETWEEN NULL NOTNULL AND ~TRUE IS NOT NULL) FILTER (WHERE 
```

---

## Crash 26: `1433c1aa38ac5afc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030217`

```sql
SELECT printf('%.*e', 9223372036854775807, 0.01); SELECT substr('CQrAyY-U ', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT FALSE LIKE TRUE COLLATE RTRIM, t2.*
```

---

## Crash 27: `75d76a1a733c1965` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030891`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, *, CURRENT_TIME FROM (SELECT *) AS a GROUP BY (CURRENT_TIME) IS DISTINCT FROM CURRENT_TIMESTAMP UNION
```

---

## Crash 28: `fd5b85d6681a89bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032702`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN VALUES (FALSE);
```

---

## Crash 29: `4f9da7b860c3820a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039277`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 30: `1449c4ab42d6d1ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039449`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (NULL)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 31: `e5334e0a84ce270e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040492`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_, c1, b, c1, c3, c1, _rowid_); REPLACE INTO r VALUES ((NULL) AND RAISE(IGNORE) << +FALSE < CURRENT_TIMESTAMP NOTNULL LIKE FALSE ESCAPE FA
```

---

## Crash 32: `d0715dd27052f724` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043761`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUE
```

---

## Crash 33: `090f1845bfc7de0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044489`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 34: `feb1e5b2e09b22b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044596`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.*d', -9223372036854775808, -1e3
```

---

## Crash 35: `028c34ec2867bac3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049276`

```sql
SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); SELECT * FROM jsonb_each('[]') WHERE RAISE(IGNORE) GROUP BY NULL WINDOW w1 AS () LIMIT RAISE(IGNORE) AND
```

---

## Crash 36: `046189270bfde1f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052751`

```sql
SELECT substr(' _J9 1rG 7o  I2l', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (c2, CAST(CASE WHEN NOT ~CURRENT_TIMESTAM
```

---

## Crash 37: `aa10d8b0de893384` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055410`

```sql
SELECT printf('%s', -2147483648, 'R_ nI'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, c2); EXPLAIN QUERY PLAN VALUES (NULL ISNULL >> CURRENT_DATE COLLATE RTRIM == +CURRENT_DATE COLLAT
```

---

## Crash 38: `8ab187e6c169e522` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056799`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (X''); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); SELECT DISTINCT q.*, CASE WHEN NULL TH
```

---

## Crash 39: `d554970b4c7565d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056913`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE NOT BETWEEN X'' AND CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, 
```

---

## Crash 40: `84c36a86f15d4198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057081`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (CAST(TRUE AS BOOLEAN) NOT BETWEEN FALSE AND CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 41: `649b270627d9ee92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057286`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); SELECT *;
```

---

## Crash 42: `885887c8d48200d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057293`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (TRUE NOT BETWEEN FALSE AND CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); SE
```

---

## Crash 43: `eef14ba30f38cb89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058233`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (-FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT DISTINCT * FROM json_tree('[
```

---

## Crash 44: `0379f2c470d3feb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060668`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM q WHERE X'Dd7aDc') AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 45: `99096a00bc7d06c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062632`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE, c1 NUMERIC UNIQUE); SELECT * FROM (SELECT FALSE FROM q WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF
```

---

## Crash 46: `d9085c4fd9da7cf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063188`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM q WHERE NULL IS NOT TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 47: `ae14b548126ad602` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063235`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM q WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 48: `5a3b7bc9bc84442a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067928`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (FALSE >= -89.019027058252e21332045892)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TA
```

---

## Crash 49: `ba621933d9286646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068036`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 50: `039fdb2d9a814d72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068386`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT -68764691176738181766895947046947355879798.3e-2605202664946231324717431408366610221095085224529112008735117378786934722701842802311040984044419997
```

---

## Crash 51: `45888da82588dd50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072788`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('[{"a":1},{"b":2}]') GROUP BY TRUE; CREATE VIRTUAL TA
```

---

## Crash 52: `d64cc96c6266d7e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083428`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT FALSE AS u8 FROM json_each('{"a":{"b":1}}') ORDER BY FALSE DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 53: `57eea75d8e7412b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083690`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CASE CURRENT_TIME WHEN FALSE THEN NULL ELSE CURRENT_DATE END AS u8 FROM json_each('{"a":{"b":1}}') ORDER BY F
```

---

## Crash 54: `939ac6477b9255e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095314`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT FALSE FROM p JOIN p w5_6 ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT OR REPLACE INTO s VAL
```

---

## Crash 55: `6712acc5cc6b0b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102794`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); EXPLAIN QUERY PLAN SELECT ALL -47
```

---

## Crash 56: `eb3dd90bf594e7c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103520`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE NOT LIKE NULL) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, c1); INSERT INT
```

---

## Crash 57: `d687009093501e3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105543`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); SELECT CASE WHEN NOT CURRENT_DATE AND CURRENT_DATE NOTNULL THEN NOT ~RAISE(IGNORE) END MATCH (VALUES (CURRENT_TIMES
```

---

## Crash 58: `eb8e87c341d55ad0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111746`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); SELECT percent_rank() OVER () FROM (SELECT * FROM p WHERE last_insert_rowid()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 59: `de800360255d9d11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116048`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r VALUES (CURRENT_TIMESTAMP <> TRUE * FALSE COLLATE BINARY LIKE +-FALSE REGEXP ~RAISE(IGNORE) COLLATE NO
```

---

## Crash 60: `f4d5334bb12398af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116250`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 61: `50ea9ab2948d71bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116607`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE IF NOT EXIST
```

---

## Crash 62: `6541cd3f914ab38f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119245`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); SELECT *;
```

---

## Crash 63: `e38941d2292c107c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120279`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); SELECT CURRENT_DATE IN (NULL) AS i FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPL
```

---

## Crash 64: `e0030e66a99b5135` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT X''); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 65: `e85e1ef067c630ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130111`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a
```

---

## Crash 66: `4966a8f653d322b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131150`

```sql
SELECT substr(' - ', -1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO t2 VALUES (-(CURRENT_TIME COLLATE NOCASE ISNULL == TRUE IN (SELECT DISTINCT r.* FROM p NOT
```

---

## Crash 67: `a4336ac6d149caf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131975`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p VALUES (CAST(NULL AS REAL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---
