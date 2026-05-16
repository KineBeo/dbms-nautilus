# Crash Triage Report

**Total crashes:** 209  
**Unique crash sites:** 209  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 209 | 209 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `7f1f6e5ae3c42345` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000108`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO q VALUES (NULL); SELECT (VALUES (CURRENT_TIMESTAMP) LIMIT TRUE) FROM p JOIN p l424__76vzqm9_1pfj4453l0g_of_z5j84fl_60if_
```

---

## Crash 2: `61e02783210a6d21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000477`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); SELECT p.*, NOT -CURRENT_TIME NOT IN (CURRENT_DATE / FALSE) IS NOT TRUE % CASE WHEN CURRENT_TIMESTAMP IS NULL IS NOT NULL THEN FALSE == ~C
```

---

## Crash 3: `01ede55355618b4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000598`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s VALUES (FALSE * ~CURRENT_DATE IS DISTINCT FROM NULL || CURRENT_TIME >= RAISE(IGNORE) NOTNULL | TRUE + TRUE * CURRENT_TIME = (CURR
```

---

## Crash 4: `1b76e0c798fe4b9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000756`

```sql
SELECT printf('%llu', -2147483649, '_T'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 DEFAULT VALUES; SELECT * FROM t2 JOIN p ud2p3 ON NULL; SELECT substr(' _1_-4_oCY', 42
```

---

## Crash 5: `cab41cc7d8ec9df9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000925`

```sql
SELECT printf('%.*e', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT OR FAIL INTO p VALUES (json_array(FALSE, TRUE) OVER (ORDER BY ~RAISE(IGNORE) ASC N
```

---

## Crash 6: `b6e40ed038355df3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001161`

```sql
SELECT substr('CB9  -q7 --_ j', -9223372036854775808, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (TRUE NOT IN (SELECT DISTINCT s.* FROM t1 AS m
```

---

## Crash 7: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001312`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 8: `68ed1fb68266d112` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001506`

```sql
SELECT printf('%.*d', 4294967296); SELECT substr('_r', 2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, CURRENT_DATE LIKE RAISE(IGNORE) || NULL ESCAPE ra
```

---

## Crash 9: `e272db661c633ee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001639`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c1, _rowid_, a, c1); SELECT EXISTS (WITH RECURSIVE q AS MATERIALIZED (SELECT CURRENT_TIMESTAMP UNION ALL SELECT CURRENT_DATE ORDER BY TRUE) 
```

---

## Crash 10: `9eb50e60be9cf2b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001658`

```sql
SELECT round(0.01, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, b); INSERT OR REPLACE INTO s VALUES (CAST(TRUE AS BLOB) NOT IN (SELECT q.* FROM (p AS a) INTERSECT SELECT * 
```

---

## Crash 11: `cccdf9364d62996b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001710`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO p VALUES ((json_array(CURRENT_DATE MATCH ~CURRENT_TIME * CASE CURRENT_DATE WHEN
```

---

## Crash 12: `314a4c6a96db0757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001871`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); SELECT TRUE ISNULL FROM p JOIN q ai__r33j6_n9s_w1_s__g6__lf8e1a_q ON CURRENT_TIMESTAMP; SELECT hex(zerobl
```

---

## Crash 13: `cd0877a6b7fa4bb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001934`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); VALUES (CURRENT_DATE); SELECT hex(zeroblob(1)); SELECT printf('%.*g', -2147483648, 1e308); CREATE VIRTUAL
```

---

## Crash 14: `fbe5dd48d19cb050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001969`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); SELECT * FROM p JOIN q ai__r33j6_n9s_w1_s__g6__lf8e1a_q ON CURRENT_TIMESTAMP; SELECT hex(zeroblob(1)); SE
```

---

## Crash 15: `c3308c41fb635c3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001992`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLA
```

---

## Crash 16: `9cb877571c736809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002166`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME
```

---

## Crash 17: `95720275016a2f03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002266`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHERE TRUE; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 18: `1162bd87d3fffa26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004550`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NATURAL LEFT JOIN (VALUES (CURRENT_TIMESTAMP)) AS w_bc_dv_ WHERE CURRENT
```

---

## Crash 19: `2d439bab4f8b49ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004571`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TA
```

---

## Crash 20: `e5f6d42e93117d32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004581`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TA
```

---

## Crash 21: `a91a2070d25d573d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004639`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE)
```

---

## Crash 22: `24fc5660cdb7e8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004647`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(b
```

---

## Crash 23: `f0e9bb175a78821d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004683`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CUR
```

---

## Crash 24: `0d72d520fbbbbedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004697`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TA
```

---

## Crash 25: `37bdb75a4cd24715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004714`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 26: `ab23ae1282a7f807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004846`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY TRUE AND random() FILTER (WHERE NULL) OVER () IS RAISE(IGNORE) DESC NULLS FIRST; INSERT INTO p DEFAULT VAL
```

---

## Crash 27: `1eac228fd097cadd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004884`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY TRUE ASC NULLS LAST; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 28: `9264163f8581b2aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005736`

```sql
SELECT printf('%x', 4294967295, 'X - _7_Cx9Z-E_6'); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME >= CURRENT_TIMESTAMP AS z FROM t3 C
```

---

## Crash 29: `8b291219860c6095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005747`

```sql
SELECT printf('%x', 4294967295, 'X - _7_Cx9Z-E_6'); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a INTEGER DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (NULL); CREATE VIRTUAL 
```

---

## Crash 30: `e1e1e360c27f2441` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005766`

```sql
SELECT printf('%x', 4294967295, 'X - _7_Cx9Z-E_6'); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 31: `824de35bd15a2339` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006422`

```sql
SELECT printf('%.*d', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (EXISTS (VALUES (CURRENT_DATE == RAISE(IGNORE))) IS +TRUE LIKE RAISE(IGN
```

---

## Crash 32: `1f3880004cdca235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006682`

```sql
SELECT substr('Z  N2m_', 4294967295, 4294967296); SELECT printf('%.*e', 1, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT_TIMESTAMP LIKE CASE WHEN NULL THEN CURRE
```

---

## Crash 33: `1af58de892c20c5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008529`

```sql
SELECT printf('%.*g', 2147483648, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH q AS MATERIALIZED (VALUES (RAISE(IGNORE))) INSERT INTO q VALUES (TRUE, NULL); EXPLAIN QUERY PLAN
```

---

## Crash 34: `a929f441d0b6cb35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009017`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c3 DATE, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p VALUES (CASE NOT ~FALSE IS NULL > TRUE ISNULL NOTNULL NOTNULL
```

---

## Crash 35: `76da372fa25ed337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009109`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR FAIL INTO r VALUES (CASE CURRENT_TIMESTAMP <> RAISE(IGNORE) WHEN ifnull(CURRENT_TIM
```

---

## Crash 36: `c879f02c6e8296a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009468`

```sql
SELECT substr('6_', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CASE (VALUES ((CURRENT_DATE % random() COLLATE NOCASE)) INTERSECT VALUES (CURRENT_TIMESTAMP OR upper(
```

---

## Crash 37: `159922be72e07ac7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014584`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE ORDER BY CURRENT_DATE DESC NULLS FIRST; PRAGMA integrity_check; SELECT printf('%.*g', 21
```

---

## Crash 38: `c28d3f4c61f8a4f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014778`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p (_rowid_) AS (SELECT D
```

---

## Crash 39: `71b880f4d8a5b817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015471`

```sql
SELECT substr('8', -2147483649); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `fb25c2c57eb116da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015615`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP COLLATE RTRIM = CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (NULL)
```

---

## Crash 41: `8cdbf5eb76beae83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015914`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP = CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE VIRTU
```

---

## Crash 42: `f6e64bcdfb2857b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT IN
```

---

## Crash 43: `d8847c3228008b96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015990`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 44: `6144529a4d8bccbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016077`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 45: `29443db48c8329f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE = CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE VIRTUAL TA
```

---

## Crash 46: `aca2cb19713d7ed0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016377`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE AND CURRENT_TIME) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL 
```

---

## Crash 47: `d7d01937a3c56a4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016846`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE, a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 48: `4f49c889d53c51d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017061`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 49: `acc4228b98365ba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE T
```

---

## Crash 50: `43b901bf1dba6062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017140`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE T
```

---

## Crash 51: `3e0b9234342b2854` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019617`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT +FALSE > CURRENT_TIME FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT V
```

---

## Crash 52: `a1e14da5aa0a55d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020570`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT CURRENT_TIME || CURRENT_DATE NOT BETWEEN CURRENT_DATE AND NULL FROM p JOIN p n ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 53: `742a07441b2e5741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022999`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT q.*, p.* FROM p JOIN q a ON NULL NOT IN (CASE NOT RAISE(IGNORE) COLLATE NOCASE ->> CURRENT_DATE 
```

---

## Crash 54: `e6fa7bad55734734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023408`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_r
```

---

## Crash 55: `98167a6e77db8d4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026960`

```sql
SELECT printf('%lli', -2147483649, '  k7 zRAS -B'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEF
```

---

## Crash 56: `a330805d9e175454` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027372`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY FALSE WINDO
```

---

## Crash 57: `39aed64ef2b2c17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027536`

```sql
SELECT printf('%.*e', -2147483648, 0.01); SELECT printf('%.*d', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEX
```

---

## Crash 58: `f4e2444875c51859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027681`

```sql
SELECT printf('%.*d', -2147483649, -1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 59: `563c7d3c64e82960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028300`

```sql
SELECT printf('%.*s', 0); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 60: `a8fa4c36bb6b054d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033459`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 61: `0f77467e90bdcc41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033884`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH q AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM q NOT INDEXED; SELECT printf('%.*g', 21474
```

---

## Crash 62: `8810f7b5516172d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035479`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 63: `99b8ee43055e047d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041385`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); WITH RECURSIVE t1 AS (SELECT *) SELECT p.* FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 64: `9819325d305a6b47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049106`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GLOB NULL | CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE 
```

---

## Crash 65: `2d9285f14b0ed775` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049315`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GLOB CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t1.*, TRUE, q.*
```

---

## Crash 66: `0778048fa9bbe561` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049379`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t1.*, TRUE, q.* FROM (SELECT p.* INTERSECT SE
```

---

## Crash 67: `47acc5e29c8498c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050346`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) EXCEPT SELECT RAISE(IGNORE) ORDER BY -CURRENT_DATE IS TRUE; EXPLAIN QUERY PLAN VALUES (NULL); C
```

---

## Crash 68: `2a0e35d2d76ae850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050392`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 69: `dfa3f8e3afd64a74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050415`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT
```

---

## Crash 70: `f018a958cef385ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050487`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT V
```

---

## Crash 71: `ff0b5ebddc9a616b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052450`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 72: `2b7b97d6cd945959` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053076`

```sql
SELECT printf('%.*s', 0, 1e308); SELECT substr('qGR_ d ', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM t2 NATURAL JOIN q WHERE CURRENT_TIME; CREATE 
```

---

## Crash 73: `cad09f0cd1a3fc50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055901`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 74: `966418de9a6d0462` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057541`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); 
```

---

## Crash 75: `4c5b7a4c4778f56b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057786`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 76: `8dea72deb56e741c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058785`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT DEFAULT X'EeDca549EdDfd4', c3 TEXT NOT NULL); SELECT * FROM p JOIN q ai__r33j6_n9s_w1_s__g6__lf8e1a_q ON NULL; SELECT
```

---

## Crash 77: `a246d2f1d4985457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058873`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT DEFAULT NULL, c3 TEXT NOT NULL); SELECT * FROM p JOIN q ai__r33j6_n9s_w1_s__g6__lf8e1a_q ON NULL; SELECT printf('%.*g
```

---

## Crash 78: `f4e752d5029cc0d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_DATE DESC; PRAGMA in
```

---

## Crash 79: `77336500744cc819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060058`

```sql
SELECT printf('%.*f', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 80: `511a18145655e9a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060102`

```sql
SELECT printf('%.*f', 4294967296, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 81: `2c69ced62a1d4566` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061126`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE FALSE GLOB FALSE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c1); INSERT INTO 
```

---

## Crash 82: `94765c1b2c8d1ae7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063598`

```sql
SELECT substr(' T', -1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 83: `08bd34c3594e131d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081693`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE (VALUES (NULL))) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 84: `9af959a11f97f20b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082094`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT *, *, * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; ANAL
```

---

## Crash 85: `8ce1d94e85573f28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083041`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT avg(FALSE) OVER (PARTITION BY TRUE ORDER BY FALSE DESC ROWS BETWEEN CURRENT_TIMESTAMP PRECEDING AND CURRENT ROW) AS hlke9_wu83x__
```

---

## Crash 86: `e9202a1725fbd2fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085491`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT -59325832365017604674430.64041220049866384515195103544628400417); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES 
```

---

## Crash 87: `0e004ab65bdf9719` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085502`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT -59325832365017604674430.64041220049866384515195103544628400417); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES 
```

---

## Crash 88: `6a05d4b3c79b826c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085676`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_ro
```

---

## Crash 89: `c1b537075dac380c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085682`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 90: `d1d769fe288de0c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085924`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL DEFAULT -44154); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 91: `373970e96bdda68a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085940`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL DEFAULT -44154); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 92: `3efe73b067fe9910` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086338`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT 0.0); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 93: `77c3e7340d2489ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086419`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT CURRENT_DATE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649
```

---

## Crash 94: `fc07b16c14960ae6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086478`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p , p AS sb WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT I
```

---

## Crash 95: `80b7c3e2c7f470d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086797`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB, a BOOLEAN PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 96: `5496678424afedc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087049`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); 
```

---

## Crash 97: `16cd5696df802b7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087701`

```sql
SELECT substr('73B_ o  -_  ', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, c1); INSERT OR IGNORE INTO t1 VALUES (CASE WHEN CURRENT_DATE COLLATE BINARY == RAISE(IGNORE)
```

---

## Crash 98: `f9d8be2643e2e971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093535`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, c3 VARCHAR(255) DEFAULT CURRENT_TIMESTAMP, c2 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 99: `7bb64bc6055f32d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097677`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL DEFAULT X'7cE8aDbfAE'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 100: `a2c68aa45dd0646e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101005`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 101: `35058f057492ddde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104900`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT FALSE <> NULL % NULL FROM p JOIN p n ON FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 102: `8e31ca10762e733f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106251`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT FALSE NOT BETWEEN CURRENT_TIME + CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT
```

---

## Crash 103: `35f5c861564a0e79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106531`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT (VALUES (CURRENT_TIME) UNION SELECT TRUE AS a) FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3)
```

---

## Crash 104: `c93e72f28346e17e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108917`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p VALUES (CURRENT_TIME) INTERSECT SELECT ALL * FROM q; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 105: `520ba836a52b562b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CAST(CURRENT_DATE AS BLOB)) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE VIR
```

---

## Crash 106: `893a89bb74563e07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111127`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CAST(TRUE AS BLOB)) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*
```

---

## Crash 107: `a61232357c1c0744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111598`

```sql
SELECT printf('%.*f', 4294967295); SELECT substr('', -9223372036854775808, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (c1) VALUES (CASE b WHEN NULL != RAISE(IGNORE) BE
```

---

## Crash 108: `2573f4ff4d8eecd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112473`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 109: `88e12ab17e8b857c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE IF NOT EXISTS p(_rowid_ DATE); CREATE VIEW IF NOT EXIS
```

---

## Crash 110: `9fce7b1fd03d498e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113080`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP = CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (NULL); CREATE TABLE
```

---

## Crash 111: `13b26f9fd1844aa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113968`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP ASC N
```

---

## Crash 112: `1ebdd6f16520ae5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114247`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED ORDER BY FALSE DESC
```

---

## Crash 113: `cca99e2e5fcb4e7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (CURRENT_TIME)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TA
```

---

## Crash 114: `f6b0198888095ad8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116400`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT '_W__g47 1 '); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DE
```

---

## Crash 115: `34a66fcb56d798b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIMESTAMP < CURRENT_DATE >= NULL DESC NULLS FIRST, CURRENT_DATE DESC NULLS FIRS
```

---

## Crash 116: `a25703366ec9c168` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117308`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, rowid TEXT UNIQUE, a REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 117: `5995d93f5ee0db39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118000`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM p NOT INDEXED WHERE TRUE ORDER BY count(*) DESC NULLS FIRST, CURRENT_DATE DESC NULLS FIRST; 
```

---

## Crash 118: `f59184b3ce50c25d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118484`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM p NOT INDEXED WHERE TRUE ORDER BY count(NULL) DESC NULLS FIRST, CURRENT_DATE DESC NULLS FIRS
```

---

## Crash 119: `579e2f3c695d0bc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119569`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY FALSE * FALSE || FALSE >> CURRENT_DATE DESC NULLS FIRST, X'01bFe1Faff99' DESC; PRAGMA i
```

---

## Crash 120: `b8475cc994bba57d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY FALSE * 6.2634434996084734e189535368691674932690728535370141655764304952747858901264705
```

---

## Crash 121: `7b69e03efa73a159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120645`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME ASC NULLS FIRST; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649
```

---

## Crash 122: `67d39579c21537b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120651`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME DESC, CURRENT_TIME ASC; PRAGMA integrity_check; SELECT printf('%.*g', -214
```

---

## Crash 123: `e6f1230fbef5a3e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 124: `78d744fc4be7b00c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121315`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY FALSE * CURRENT_TIMESTAMP || FALSE >> TRUE DESC NULLS FIRST, count(*) FILTER (WHERE TRU
```

---

## Crash 125: `397470d2e6920b9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121626`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (CURRENT_TIME)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME ASC NULLS LAST
```

---

## Crash 126: `4716a95c6f49e54b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121761`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (CURRENT_TIME)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 127: `6276aa5f68df23aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122928`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP)) AS w_bc_dv_ WHERE TRUE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; PRAGMA integrity_check; CR
```

---

## Crash 128: `aeecb1ecf5b51ea3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123120`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP)) AS w_bc_dv_ WHERE TRUE ORDER BY NULL ASC NULLS LAST, NULL ASC NULLS LAST; PRAGMA integrity_c
```

---

## Crash 129: `bdc40bb94fe30672` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY FALSE * CURRENT_TIMESTAMP || TRUE - FALSE >> TRUE DESC NULLS FIRST, NULL ASC NULLS LAST
```

---

## Crash 130: `cab8d215ce09be63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME IS TRUE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 131: `228f8c4e083e6a43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126565`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 132: `28944292de04ccea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126719`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT NULL FROM p NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q DEFAULT VALU
```

---

## Crash 133: `80318661f0f27986` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127408`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS FIRST; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 134: `27a860b9acec01b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132511`

```sql
SELECT printf('%f', -9223372036854775808, 'H_Y_ _h_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q (b, _rowid_) VALUES (json_type(min(NOT CURRENT_TIME / CURRENT_DATE COLLAT
```

---

## Crash 135: `d43fe2c79a4e5303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137446`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY, c3 NUMERIC UNIQUE); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY json_array(TRUE); PRAGMA integrity_check; SELECT pr
```

---

## Crash 136: `ed05ef5008db28f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139304`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT * FROM (VALUES (CURRENT_DATE)) AS t___7____k87ydn_44__m__8b465___ WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (); PRAGMA integrity_che
```

---

## Crash 137: `982595d3fffb20c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139974`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT FALSE & NOT CURRENT_TIME AS o FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_DATE; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 138: `e6293aa2c67905a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT CURRENT_DATE AS o FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_DATE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 139: `f7b4dac35d2b8d57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140958`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM (VALUES (CURRENT_TIME) UNION VALUES (FALSE)) AS f9_owjea_p WHERE TRUE ORDER BY FALSE DESC NULLS LAST, count(*) FILTER (WH
```

---

## Crash 140: `a7fab6ebfca61f61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141006`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM (VALUES (CURRENT_TIME) UNION VALUES (FALSE)) AS f9_owjea_p WHERE TRUE ORDER BY FALSE; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 141: `a7fe1260ef9f509e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141616`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT group_concat(CURRENT_TIMESTAMP, '') AS a FROM p NOT INDEXED WHERE TRUE ORDER BY TRUE DESC; PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 142: `cf6c33c38f328de3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142124`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE IN (VALUES (NULL)) ORDER BY _rowid_ DESC NULLS FIRST, CURRENT_DATE DESC; PRAGMA integrity_check;
```

---

## Crash 143: `3c9b813da4d2987b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142540`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY TRUE DESC NULLS LAST, CURRENT_DATE NOT IN (+CURRENT_TIMESTAMP) DESC; PRAGMA integrity_c
```

---

## Crash 144: `488eaef5840eb50b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY TRUE DESC NULLS LAST, CURRENT_DATE NOT IN (NULL) DESC; PRAGMA integrity_check; SELECT p
```

---

## Crash 145: `89ea410d97979694` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT count(*) OVER (PARTITION BY FALSE ORDER BY FALSE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURREN
```

---

## Crash 146: `e31c42cc72f57317` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143508`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME DESC NULLS LAST; PRAGMA integrity_check; CREA
```

---

## Crash 147: `11273aa84af61034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM p NOT INDEXED WHERE TRUE ORDER BY count(*) OVER () DESC NULLS FIRST, CURRENT_DATE DESC NULLS
```

---

## Crash 148: `8e1d14dca6086617` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144744`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, a TEXT); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY FALSE ASC NULLS FIRST, length(c1) DESC NULLS LAST; PRAGMA integrity
```

---

## Crash 149: `1536b44929e485f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145093`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, rowid TEXT UNIQUE, a REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(
```

---

## Crash 150: `e5bb84eede680e40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146573`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT ' 2Eyb--z- _'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 151: `8ebef4245c4d8019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146746`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE BETWEEN CURRENT_DATE AND TRUE ORDER BY CURRENT_DATE DESC NULLS FIRST; PRAGMA integrity_check; CR
```

---

## Crash 152: `a17f28aa4e00dd41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146871`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 153: `4cf149cae0794ed9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148639`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; SELECT DISTINCT CURRENT_TIME AS f_om0_27__v0sn_
```

---

## Crash 154: `3d4b1986ea6a9304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150370`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; SELECT min(NULL) AS a FROM (SELECT * FROM p WHE
```

---

## Crash 155: `2db69ef8a99612c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150679`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABL
```

---

## Crash 156: `03ce7f0ff2f3f5b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151467`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME COLLATE RTRIM = CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; SELECT DISTINCT * 
```

---

## Crash 157: `b1f9aa89203bc164` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152851`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p VALUES (CURRENT_TIME) INTERSECT SELECT ALL * FROM q; PRAGMA quick_check; CREA
```

---

## Crash 158: `e37fbf6d06cb61d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153803`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR IGNORE INTO p VALUES ((VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIMESTAMP * CURRENT_TI
```

---

## Crash 159: `0845040ed6f81583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153878`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT *, count(*) OVER () AS gn9z_e6u_0 FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VA
```

---

## Crash 160: `db12c124d63d8376` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154133`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT TRUE - CURRENT_TIME + ~FALSE > TRUE FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q
```

---

## Crash 161: `76f68e5962357a5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154231`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT CURRENT_TIMESTAMP + ~FALSE > TRUE FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q D
```

---

## Crash 162: `6083917c911e28ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154834`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p JOIN p n ON CURRENT_TIME; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 163: `d796c48c7a4b69a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154986`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT * FROM p JOIN p n ON CURRENT_TIMESTAMP < CURRENT_DATE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT I
```

---

## Crash 164: `7f1e8d74ab6f89b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155156`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT (SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY FALSE HAVING FALSE UNION SELECT TRUE AS a) FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUAL 
```

---

## Crash 165: `ef1e4377f1e9fe2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156216`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT max(TRUE COLLATE RTRIM) OVER () FROM p JOIN p n ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT INTO p (c2) VAL
```

---

## Crash 166: `6ebafc367c2d0f10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160567`

```sql
SELECT substr('', 9223372036854775807); CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c2); SELEC
```

---

## Crash 167: `4ac6784cc04c37fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165554`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p VALUES (CAST(TRUE AS FLOAT)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*e', -21
```

---

## Crash 168: `0235da2914656c6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167309`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME ASC NULLS LAST; SELECT pri
```

---

## Crash 169: `1925e4681cc92b61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168578`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED CROSS JOIN p AS l_ USING (c2) WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS
```

---

## Crash 170: `4ca4857248ba6f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176491`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (-325387325859119410606649.49); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 171: `fb6e5f7171a21a30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IS TRUE) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 172: `5099894f53dd484a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181009`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT avg(FALSE) OVER (PARTITION BY (VALUES (NULL)) ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES) 
```

---

## Crash 173: `d548b95ed880e1fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME COLLATE RTRIM, * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 174: `adc3c630bb4507c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181571`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT NULL, * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 175: `1b4457f4cad49738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181645`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME COLLATE RTRIM IS NOT CURRENT_DATE, * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 176: `6b4ff508c09ffa36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182204`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a) UNIQUE); SELECT * FROM (SELECT count(DISTINCT NULL) FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 177: `956649272ecd6381` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182515`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, 
```

---

## Crash 178: `6e0ee37b24694a14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT count(*) IS NOT min(NULL) | _rowid_ AS a FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 179: `e0daa50da87f56f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184427`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME NOT IN (SELECT CURRENT_TIMESTAMP FROM p NOT INDEXED) FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 180: `b59a1d821003de77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210025`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 181: `4deb598a90c97023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211880`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM (SELECT * FROM p WHERE rowid ISNULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO q VALUES (CA
```

---

## Crash 182: `408e1da422b57571` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE (SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM p , p AS sb WHERE TRUE ORDER BY CURRENT_TIME DESC); CREATE VIRTU
```

---

## Crash 183: `51eee9f82d694bff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213355`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); WITH RECURSIVE q AS (VALUES (NULL)) INSERT INTO p VALUES (NULL IN (SELECT DISTINCT * FROM p NOT INDEXED)); PRAGMA quick_check; CREATE VIRTUAL TABLE I
```

---

## Crash 184: `371c7bd1b6d8acba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215365`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT '  HN-_ _0 x1_ A-', c3 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT avg(FALSE) OVER (PART
```

---

## Crash 185: `695effcb8850b79e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217766`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT * FROM p JOIN p n ON CURRENT_TIME; CREATE VIRTUA
```

---

## Crash 186: `375dd065674b5850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224653`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAU
```

---

## Crash 187: `846ebd4b7f177970` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224757`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAU
```

---

## Crash 188: `139f42aabba2d46f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226271`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE TA
```

---

## Crash 189: `40684e666d2ec12d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229820`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); SELECT * FROM (SELECT * FROM p WHERE rowid ISNULL ISNULL ISNULL ISNULL ISNULL ISNULL ISNULL ISNULL ISNULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 190: `907ab2aaa7747bcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230940`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT * FROM 
```

---

## Crash 191: `9142bea1a68c17d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235095`

```sql
SELECT printf('%.*g', 0, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH r AS MATERIALIZED (SELECT *) INSERT INTO p VALUES (~CURRENT_TIME, FALSE); ANALYZE p; CREATE TABLE IF NOT E
```

---

## Crash 192: `76ad68c628c4ba20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254740`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME NOT IN (SELECT DISTINCT count(*) OVER () AS gn9z_e6u_0 FROM (VALUES (CURRENT_TIMESTAMP)) AS t___7____k87ydn_44__m__8
```

---

## Crash 193: `239361a7528f147b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254763`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT TRUE FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM r JOIN t3 a ON CURRENT_T
```

---

## Crash 194: `9354a8fc575f6332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254833`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT X'01bFe1Faff99' NOT IN (SELECT CURRENT_TIMESTAMP FROM p NOT INDEXED) FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 2147483647
```

---

## Crash 195: `5e1bb70adbe5ce60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT X'01bFe1Faff99' NOT IN (SELECT * FROM p NOT INDEXED) FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 196: `4e0cb84859080eaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255596`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT max(CURRENT_TIME) IS NOT min(NULL) | _rowid_ AS a FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 197: `d6ca46afa64200cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT max(CURRENT_TIME) IS NOT CURRENT_TIME | _rowid_ AS a FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 198: `4b2d0c6a90710552` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255766`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT max(CURRENT_TIME) IS NOT CURRENT_TIME | CURRENT_DATE AS a FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 199: `20e763832682db2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256080`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM (SELECT avg(FALSE) AS a FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALU
```

---

## Crash 200: `ae8261a8e191b8c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262720`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH q AS (VALUES (CURRENT_TIME) UNION SELECT * FROM (SELECT * FROM p ORDER BY CURRENT_DATE DESC NU
```

---

## Crash 201: `db04c557210b1738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262836`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH q AS (VALUES (CURRENT_TIME) UNION VALUES (CURRENT_DATE)) SELECT ALL * FROM q NOT INDEXED; CREA
```

---

## Crash 202: `e9e96db1de2c653b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263636`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH q AS (SELECT *) SELECT ALL * FROM (VALUES (FALSE)) AS f9_owjea_p NATURAL LEFT JOIN p AS sb; CR
```

---

## Crash 203: `a56e45e2402472a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264873`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN GENERATED ALWAYS AS (NULL) STORED, c1 BOOLEAN); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 204: `78db981c65683432` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000271038`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2);
```

---

## Crash 205: `897c7ce894be5a13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p VALUES (CAST(CAST(FALSE AS BLOB) AS BLOB)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 206: `a4ac49779cbdf6d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275842`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p VALUES (CAST(TRUE AS BOOLEAN)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 207: `e43f573839ede998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000276074`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p VALUES (CAST(TRUE AS VARCHAR(255))) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*
```

---

## Crash 208: `d216aa5233cc8ad5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286171`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT max(CURRENT_DATE) OVER () LIKE CURRENT_TIMESTAMP ESCAPE (SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY CURRENT_TIME DESC) FROM p 
```

---

## Crash 209: `4f04f69320e1eb2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286218`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); SELECT count(*) OVER () LIKE CURRENT_TIMESTAMP ESCAPE CURRENT_DATE FROM p JOIN p n ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---
