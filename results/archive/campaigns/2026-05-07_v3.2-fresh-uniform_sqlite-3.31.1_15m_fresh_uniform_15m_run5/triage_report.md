# Crash Triage Report

**Total crashes:** 112  
**Unique crash sites:** 112  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 112 | 112 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `a5dabbfff64a90bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000084`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_, c2); INSERT INTO t2 VALUES (CASE WHEN +CURRENT_TIMESTAMP / (NULL) THEN CAST(FALSE AS FLOAT) < TRUE NOTNULL - CURRENT_DATE OR TRUE 
```

---

## Crash 2: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000324`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 3: `ec466d33616e754c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000361`

```sql
SELECT round(-1e308, 2147483647); SELECT substr('-c', -1, 1); SELECT substr('4a_-z-8V6_h_', -2147483649, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO t1 VALUES (NOT EXISTS
```

---

## Crash 4: `b59b20fe9e0b92a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000496`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (c1) VALUES (RAISE(IGNORE) NOT LIKE CURRENT_TIMESTAMP) ON CONFLICT(a) DO UPDATE SET c
```

---

## Crash 5: `4ea8c065088a9e52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000577`

```sql
SELECT printf('%.*f', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR ROLLBACK INTO t2 VALUES (-FALSE BETWEEN FALSE IS NOT NULL AND RAISE(IGNORE) COLLATE RTRIM REGEXP count(
```

---

## Crash 6: `1a9cfd4a7930b597` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000840`

```sql
SELECT substr('', -9223372036854775808, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE p AS (WITH p AS MATERIALIZED (SELECT r.*) SELECT t1.*, * FROM p AS
```

---

## Crash 7: `1726554d1615ebdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001067`

```sql
SELECT printf('%.*e', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT OR ROLLBACK INTO p VALUES ((TRUE NOT BETWEEN NULL AND TRUE IS NOT CURRENT_DATE) * CUR
```

---

## Crash 8: `01ee213c61069898` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001120`

```sql
SELECT printf('%d', -9223372036854775808, ''); SELECT substr('j_u_ cM', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, b); INSERT OR FAIL INTO t3 VALUES (sum(CURRENT_DATE) F
```

---

## Crash 9: `2ca1d246b448d117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001156`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_, c1, b, b, _rowid_, c2, c3); INSERT OR FAIL INTO p VALUES (EXISTS (WITH RECURSIVE q AS NOT MATERIALIZED (SELECT s.* INTERSECT 
```

---

## Crash 10: `6cc4eb9c55cc6831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001353`

```sql
SELECT printf('%.*d', 4294967295, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO t2 VALUES (count(*) FILTER (WHERE RAISE(IGNORE)) OVER (PARTITION BY TRUE) IS
```

---

## Crash 11: `af6db6742e7f7d4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001515`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CASE FALSE <= NULL - CURRENT_TIME / ~RAISE(IGNORE) OR (TRUE) > NOT EXISTS (SELECT * UNION VALUES
```

---

## Crash 12: `ae59f1537f02c80c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001581`

```sql
SELECT printf('%.*d', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 (b, c3) VALUES (X'' >= CURRENT_TIME & NULL != (RAISE(IGNORE)) COLLATE RTRIM <> lag(RAI
```

---

## Crash 13: `c60e6566537f8ee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001615`

```sql
SELECT printf('%.*d', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT INTO t1 SELECT CURRENT_TIME FROM t3 NOT INDEXED WHERE CURRENT_DATE NOT LIKE CURRENT_DATE GROUP BY
```

---

## Crash 14: `adecec7cbcf9ec1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004954`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%f', 0, 'V_ f vE9   0D'); SELECT printf('%.*g', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t3 VALUES (~CU
```

---

## Crash 15: `0a99a53d2183100e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004963`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%f', 0, 'V_ f vE9   0D'
```

---

## Crash 16: `17e31824770f3ca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004969`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%f', 0, 'V
```

---

## Crash 17: `f663fdbb26b5cd97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004996`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%f', 0, 'V_ f 
```

---

## Crash 18: `075181e321650101` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005906`

```sql
SELECT printf('%.*s', 2147483647); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO s VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CRE
```

---

## Crash 19: `913da1232c5067a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005926`

```sql
SELECT printf('%.*s', 2147483647); CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CASE WHEN TRUE THEN CURRENT_TIMESTAMP ELSE TRUE END, * FROM s NATURAL LEFT JOI
```

---

## Crash 20: `19573524aa4d195b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005947`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT
```

---

## Crash 21: `5d5c5e647a1830ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005953`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF 
```

---

## Crash 22: `55120fce0b0496a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005961`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t1 NOT INDEXED; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUA
```

---

## Crash 23: `4c25c8a6b4f7d5f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005969`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM s NATURAL LEFT JOIN (q NOT INDEXED) LEFT JOIN q; EXPLAIN QUERY PLAN VAL
```

---

## Crash 24: `9c9de1296e3636b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007845`

```sql
SELECT round(1e-308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, b); INSERT INTO t1 VALUES (CURRENT_TIMESTAMP) RETURNING CURRENT_DATE; SELECT * FROM p JOIN p a ON 'fh-  c__
```

---

## Crash 25: `a8fffbfaa6d8e6d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008045`

```sql
SELECT printf('%.*e', -2147483649, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT (FALSE) NOT BETWEEN NULL AND TRUE NOT LIKE FALSE AS a FROM s JOIN p a ON unicode(RAISE(IGNORE
```

---

## Crash 26: `79d7361526f8888c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020229`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, c1); WITH t2 AS NOT MATERIALIZED (SELECT DISTINCT * FROM q ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP ISNULL 
```

---

## Crash 27: `453c638c3febc816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021810`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 28: `918a75377c2e1111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022698`

```sql
SELECT printf('%.*g', -2147483648); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 29: `564b042ff0da0cbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025722`

```sql
SELECT printf('%.*d', -2147483649, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT RAISE(IGNORE) COLLATE BINARY BETWEEN CASE WHEN CURRENT_DATE THEN CURRENT_TIMESTAMP COLLATE NOC
```

---

## Crash 30: `45acc452644cf71a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027032`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL - TRUE IS NOT NULL); PRAGMA quick_check; SELECT printf('%.*f', 21474836
```

---

## Crash 31: `56a043fa0602ec15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027536`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP > TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 32: `62a63ed6d0894b88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031425`

```sql
SELECT printf('%.*d', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT *, * FROM (SELECT q.* FROM r WHERE CAST(~CURRENT_TIMESTAMP COLLATE NOCASE AS BLOB)) AS sub1; CREATE TA
```

---

## Crash 33: `af2cc0eb7b52ddfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032103`

```sql
SELECT round(-1.0, -2147483649); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 34: `7f4c8804d39da7cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032912`

```sql
SELECT substr('35', 0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT INTO t2 (b) VALUES (CURRENT_TIME >= CURRENT_TIMESTAMP NOT IN (~RAISE(IGNORE) OR CURREN
```

---

## Crash 35: `9025ea310174829a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033408`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL) UNION VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r VALUES (CURRENT_DATE) ON CON
```

---

## Crash 36: `570b473f5077a0bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE upper(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 37: `c1334c2c68bbd6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036018`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NULL ELSE NOT TRUE END; CREATE VIRTUAL TABLE IF 
```

---

## Crash 38: `7294d7a7a9dbce96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036146`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NULL ELSE NOT NULL END; SELECT printf('%.*f', 2147483
```

---

## Crash 39: `6865bd70afa0b2be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036470`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); 
```

---

## Crash 40: `d2c85442e1d11ed3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036611`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INS
```

---

## Crash 41: `b56807c7e91015ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036734`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NULL >> FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 42: `379010e056e8465d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037368`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NULL ELSE NOT FALSE GLOB CURRENT_TIMESTAMP END; CRE
```

---

## Crash 43: `7bd9156b91eed549` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048294`

```sql
SELECT printf('%.*g', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p VALUES (NULL) RETURNING CURRENT_TIME; EXPLAIN QUERY PLAN VALUES (NULL) LIMIT RAISE(
```

---

## Crash 44: `cae0016dc40b5d8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048432`

```sql
SELECT printf('%.*e', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); WITH RECURSIVE p AS (WITH RECURSIVE s AS MATERIALIZED (SELECT r.*) SELECT * FROM t2 NOT INDEXED JOIN t2 NO
```

---

## Crash 45: `30a1f76be902fd43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048537`

```sql
SELECT printf('%.*d', -2147483648, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO q VALUES (dense_rank() FILTER (WHERE CURRENT_DATE NOT NULL) OVER ()); EXPLAIN 
```

---

## Crash 46: `306391f616453a46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049953`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL DEFAULT 0, a VARCHAR(255) UNIQUE); SELECT * FROM (SELECT * FROM p WHERE last_insert_rowid()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 47: `22c172a67d027ba4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY RAISE(IGNORE) DESC, row_number() OVER (PARTITION BY TRUE ORDER BY CURRENT_TIMESTAMP ASC NULLS FI
```

---

## Crash 48: `0f3bc08b984ec3b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052662`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, c3 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (CURRENT_TIMESTAMP, FALSE); PRAGMA quick_check; CREATE VIR
```

---

## Crash 49: `2b1aaaa58d4cb2be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054261`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE s AS (SELECT *) VALUES (CURREN
```

---

## Crash 50: `ff3a8268294dd013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054700`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE s AS (SELECT *) VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b)
```

---

## Crash 51: `d1d28a51eb5842a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054925`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); INSERT I
```

---

## Crash 52: `a27e60ff24d815f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059039`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, c1, c1, c2, c3, _rowid_); EXPLAIN QUERY PLAN SELECT t2.* FROM (SELECT *, * UNION VALUES (NULL M
```

---

## Crash 53: `98457a1b54b98265` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064510`

```sql
SELECT substr(' __ - ', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO s VALUES (CASE CURRENT_TIME << -RAISE(IGNORE) OR RAISE(IGNORE) COLLATE BINARY ISN
```

---

## Crash 54: `76b7770350586808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065619`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT CURRENT_TIMESTAMP, c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF N
```

---

## Crash 55: `dce45f9b0876c645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067598`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE, _rowid_ VARCHAR(255), a DATE, b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NU
```

---

## Crash 56: `3a74cee8a1bedb96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067711`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NULL ELSE NOT FALSE END; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 57: `fcfa473670cb32cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067717`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE, _rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN NULL THEN NULL ELSE NOT FALSE END; CRE
```

---

## Crash 58: `dba6c3923b5d4847` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068394`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP * CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 59: `bca02ee5d6afde12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069088`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 60: `67efdcd1ddfb343b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE upper(CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 61: `b847e8c2b8b57d53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071413`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN p WHERE changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 62: `e5dc1f6085f76591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071853`

```sql
SELECT substr('-T  -_', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 VALUES (-printf('9-7-6_', FALSE) BETWEEN CURRENT_TIME <> NOT RAISE(IGNORE) IS 
```

---

## Crash 63: `dea63f8ed5687085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 64: `4baa882ff24ee810` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074275`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT TRUE, b DATE NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH t1 (a) AS (SE
```

---

## Crash 65: `8a0039e011fc45f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075944`

```sql
SELECT printf('%s', -2147483648, '-  0-t--_ '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO t3 VALUES (NOT CASE FALSE BETWEEN NULL AND RAISE(IGNORE) WHEN CURRENT_TIM
```

---

## Crash 66: `eb5ffcdea7049dc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077473`

```sql
SELECT printf('%f', -2147483648, 'k _n_   -  -'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 VALUES (CURRENT_TIME) RETURNING NOT (SELECT FALSE AS s, CURRENT_TIME FROM t3 
```

---

## Crash 67: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077482`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 68: `8ba926da947e0c3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079056`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 WHERE TRUE AND 0; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647
```

---

## Crash 69: `e3fc22c9fde833bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079659`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) EXCEPT VALUES (CAST(TRUE AS REAL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); INSERT INTO p VALUES (CURR
```

---

## Crash 70: `7b159abcd09952b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080241`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) EXCEPT VALUES (row_number() OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); INSERT INTO r DEF
```

---

## Crash 71: `d2b6365931969c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080372`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO s DEFAULT VALUES;
```

---

## Crash 72: `4d12c89275e86400` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080939`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME LIKE FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 73: `8753da070b884ce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082719`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE IN (FALSE, CURRENT_TIME)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 74: `74485126dffefaaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082846`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(FALSE AS TEXT)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 75: `f07ed06434d09fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(TRUE AS TEXT)); PRAGMA quick_check; SELECT printf('%.*f', 214748364
```

---

## Crash 76: `88733fd9f28dd44c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 77: `c8dbcbb4e8daa11b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084043`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (SELECT CURRENT_TIME)); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 78: `c5e6d43342d2d4e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084149`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (VALUES (NULL))); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 79: `f58b8a75c2a8dc73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085041`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL - X'DDFcFbBC'); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 80: `6a01a98f05dc91d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086482`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(CURRENT_TIMESTAMP AS NUMERIC)); PRAGMA quick_check; CREATE VIRTUAL TABL
```

---

## Crash 81: `fc2e188c9e90af64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087164`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE | NULL); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 82: `67aab189b5281b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087369`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (7498645366210321.4802E-20686080294844); PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 83: `3c6f64ac5ed536b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087792`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES ((SELECT * FROM p WHERE TRUE GROUP BY NULL WINDOW w1 AS () LIMIT FALSE OFFSET
```

---

## Crash 84: `552f6698ca583149` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087868`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE > CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 2147
```

---

## Crash 85: `748761127bb56184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088110`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE > CURRENT_TIME COLLATE RTRIM); PRAGMA quick_check; CREATE VIRTU
```

---

## Crash 86: `913adb116f6d0faa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088183`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE > NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 87: `613b0dac1daa7191` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088312`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(CURRENT_TIMESTAMP AS INT) > CURRENT_TIME); PRAGMA quick_check; CREATE V
```

---

## Crash 88: `c122ac2fb658400b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088627`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME IS FALSE); PRAGMA quick_check; SELECT printf('%.*g', 214748364
```

---

## Crash 89: `3e91478fcc93e86e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088923`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME % CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE 
```

---

## Crash 90: `852b4033b4d76392` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089046`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(TRUE AS FLOAT) > TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 91: `b111cdef6fff0703` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089175`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(CURRENT_TIMESTAMP AS FLOAT) > TRUE); PRAGMA quick_check; SELECT printf(
```

---

## Crash 92: `b948f0e2e79782cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089475`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(FALSE AS NUMERIC)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 93: `a52fbb447bf8709d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089829`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE + CAST(CURRENT_TIMESTAMP AS REAL)); PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 94: `d55355ef0889ee2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091261`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT -869845); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 95: `05aca5b9e178eec5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092575`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, rowid BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 96: `4fca888af487938f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092809`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 97: `d21222804e52189a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092955`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -92233720368547758
```

---

## Crash 98: `e3a1327afdd3ff0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093042`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT 417.55E98616434000567243777586605977101466816191059241689161044059314934384616352536163); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSE
```

---

## Crash 99: `f269789d0ed35bcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094267`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 100: `51e2b1567f882050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095111`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_TIME OR FALSE)); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483
```

---

## Crash 101: `4120596fabde751b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096296`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 102: `fcbc7548f76b759a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (changes())); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g
```

---

## Crash 103: `122e8cd66fccf805` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096531`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', 2
```

---

## Crash 104: `29494b4591daac2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096544`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g
```

---

## Crash 105: `7a35efd7f6f42fd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097209`

```sql
SELECT printf('%.*g', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT +FALSE IS NOT NULL NOT IN (VALUES (+CURRENT_TIME) LIMIT FALSE COLLATE NOCASE, FALSE) <= EXISTS (SELECT q
```

---

## Crash 106: `8a7d0eb22c2c0be5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097906`

```sql
SELECT substr('r8_ -4H_ _', -1, -2147483648); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 107: `05762bb52b0200c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106749`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY, b NUMERIC DEFAULT X'EaE6ddcc', c3 BOOLEAN NOT NULL DEFAULT -23896.603); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; E
```

---

## Crash 108: `fb505d47c0da6c0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118665`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT, c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 109: `171820701a60d3a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119931`

```sql
SELECT printf('%.*e', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH r (c1) AS NOT MATERIALIZED (SELECT * EXCEPT SELECT DISTINCT * FROM s LEFT JOIN t2 NOT IN
```

---

## Crash 110: `ecc66e04865eb5a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120106`

```sql
SELECT printf('%.*s', -1, -0.0); SELECT substr('9_abL9_ -_', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, b, c2); VALUES (CAST(NULL AS VARCHAR(255)) << count() LIKE FALSE IS FALSE 
```

---

## Crash 111: `a2362987aba0c6cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122244`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT * FROM q JOIN q a ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, 
```

---

## Crash 112: `f5083b61598e66ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129212`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT '', c3 BOOLEAN NOT NULL DEFAULT -23896.603); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CRE
```

---
