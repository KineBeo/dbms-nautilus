# Crash Triage Report

**Total crashes:** 45  
**Unique crash sites:** 45  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 45 | 45 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `20038202245f8a37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000024`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 VALUES ((CURRENT_TIME)); SELECT ~CURRENT_DATE AS q_ FROM r JOIN t3 d ON NULL NOT NULL REGEXP random() COLLATE NOCASE LIKE NULL 
```

---

## Crash 2: `bec8d3a72e412fdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000647`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a) VALUES (CASE CASE FALSE WHEN TRUE = TRUE IS NOT RAISE(IGNORE) GLOB NULL LIKE TRUE ->> NULL THEN NULL << CURRENT_TIMESTAMP ELS
```

---

## Crash 3: `c1b95e2569be2752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001170`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c3, c2); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME IN (VALUES (~CURRENT_TIMESTAMP) LIMIT CURRENT_DATE), (SELECT q.* FROM json_tree(RAIS
```

---

## Crash 4: `c1ac47f8df61f774` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001383`

```sql
SELECT substr('--l  - - H__  6 -T3', 4294967296, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CAST(CURRENT_TIMESTAMP AS DATE) IS TRUE FROM q WHERE EXISTS (WI
```

---

## Crash 5: `304e466ee0b9abe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001670`

```sql
SELECT substr('_-_ -41_1', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT DISTINCT TRUE AS mze, *, t1.*, q.* FROM json_tree(CASE FALSE WHEN FALSE % group_concat(CURRENT_
```

---

## Crash 6: `ba2f28ed84ad1a33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004286`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t1 AS MATERIALIZED (SELECT RAISE(IGNORE) FROM json_tree('{"a":1}') ORDER BY FALSE IS DISTINC
```

---

## Crash 7: `e75dc6dbc5d79d84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004636`

```sql
SELECT printf('%.*f', 4294967296); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (last_value(TRUE) FILTER (WHERE NULL = C
```

---

## Crash 8: `744a7a506d4b97eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007817`

```sql
SELECT substr('M u ', 4294967296, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO s VALUES (FALSE COLLATE NOCASE); WITH RECURSIVE r (c3, c3) AS NOT MATERIALIZED (SEL
```

---

## Crash 9: `e9203f4e73f8f5ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008415`

```sql
SELECT substr(' O5 9--', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT INTO q VALUES (CAST((NULL) AS BOOLEAN) & CURRENT_TIME IN (SELECT * ORDER BY RAISE(IGN
```

---

## Crash 10: `90bc03a0fbfd56e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008544`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, a, a, a, c3, _rowid_, c3); INSERT INTO p (b) VALUES ((RAISE(IGNORE)), FALSE) ON CONFLICT(c1) DO UPDATE SET c3 = ntile(CURRENT_TIME REGEXP TRU
```

---

## Crash 11: `03bef2911f465072` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017195`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT
```

---

## Crash 12: `d2fc7f2d5f1c69ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017204`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, _rowid_); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 13: `0b812872191da57f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017749`

```sql
SELECT substr('A2l42  h-___D _x7_', 4294967295, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT INTO r VALUES (CASE ~~-CURRENT_TIMESTAMP COLLATE BINARY <= RA
```

---

## Crash 14: `4d90b8962796bc24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019349`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP / TRUE / FALSE IS NOT NULL NOT IN (CURRENT_TIME)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 15: `47cdc29d88250e7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025194`

```sql
SELECT printf('%.*e', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (rowid, rowid, _rowid_) VALUES (~CURRENT_TIMESTAMP IS NOT NULL, CURRENT_TIMESTAMP == ~NULL AND 
```

---

## Crash 16: `0d74dd038ded0387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027306`

```sql
SELECT round(0.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VALUES (+CURRENT_TIME | FALSE OR FALSE COLLATE NOCASE, CASE FALSE IS NULL WHEN TRUE IN (rank()) THEN CURR
```

---

## Crash 17: `a7e2c1795e54aa76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028816`

```sql
SELECT printf('%.*s', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT OR FAIL INTO p VALUES (typeof(-(TRUE) NOT BETWEEN CURRENT_DATE AND CASE NOT ntile(+TRUE OR CURRENT_DATE GL
```

---

## Crash 18: `56ea663734091ea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030710`

```sql
SELECT substr('_BNe_C_--76-__ z', 2147483647, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, a); SELECT NOT (CURRENT_TIMESTAMP) IN (SELECT DISTINCT * FROM p AS a ORDER BY NUL
```

---

## Crash 19: `fb9bca4758e9dec6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032020`

```sql
SELECT printf('%.*d', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1, a); INSERT INTO q VALUES (CASE WHEN +NULL IS DISTINCT FROM CASE CURRENT_TIMESTAMP WHEN CURRENT
```

---

## Crash 20: `8459c1e946a669ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035946`

```sql
SELECT round(0.01, 4294967296); SELECT round(1e-308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c1); INSERT INTO p VALUES (FALSE - NOT FALSE, RAISE(IGNORE) IS NOT NULL NOT IN (js
```

---

## Crash 21: `9794d3b1d623fc30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037113`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 22: `2b1f37477523e498` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044903`

```sql
SELECT printf('%.*g', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM q AS i__14gmb_44__o6____g2__u WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (), w2 AS (
```

---

## Crash 23: `30a6479508290e12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049669`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN SELECT NULL IS NOT NULL AS i3psj_f07o FROM j
```

---

## Crash 24: `b2bd23bf22e88249` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051789`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO p
```

---

## Crash 25: `e1469e24500edcb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052957`

```sql
SELECT printf('%s', 4294967296, 'f6'); SELECT printf('%.*g', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE p (c1, c1) AS NOT MATERIALIZED (SELECT RAISE(IGNORE) UNI
```

---

## Crash 26: `43a11f33eaeeddf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053224`

```sql
SELECT printf('%.*s', 2147483647, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); WITH q (b) AS (WITH RECURSIVE p AS MATERIALIZED (SELECT *) VALUES (CURRENT_DATE)) INSERT INTO t2 VA
```

---

## Crash 27: `12cd17e26323eda9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053366`

```sql
SELECT printf('%lli', -9223372036854775808, 'Oei7wG----0VE_kN Q'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, b, c1); SELECT t3.*, CURRENT_TIMESTAMP | CURRENT_DATE != CURRENT_TIMESTA
```

---

## Crash 28: `7a6addc640acee81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059208`

```sql
SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE - FALSE); SELECT *; SELECT hex(zeroblob(9223372036854775807))
```

---

## Crash 29: `7f2cb5784c638490` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061819`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE) INTERSECT SELECT DISTINCT TRUE FROM json_each('[1,2,3]') LEFT OUTER JOIN (VALUES (CURRENT_TIME)) AS a INNER JOIN json_tree('[]')
```

---

## Crash 30: `40459a97376b89f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065694`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC GENERATED ALWAYS AS (FALSE IS NOT FALSE ISNULL) VIRTUAL, b DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE FALSE IS NOT NU
```

---

## Crash 31: `aee1b354d58ccc39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067185`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT '   -', rowid DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 32: `077576f46eb7c7fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067213`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c3);
```

---

## Crash 33: `ccceb8b8da3b5d7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067219`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE, rowid DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 34: `04403c8f882c0307` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067225`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT TRUE, rowid DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 35: `3bdc8180de052332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081535`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UN
```

---

## Crash 36: `4a6bfcb215f02a09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083090`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 37: `fea830c79d98b015` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084462`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY count(*) OVER (), TRUE DESC LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 38: `5ab85ad4a0d2960f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084852`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY CURRENT_TIMESTAMP COLLATE NOCASE ASC LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 39: `915b1633076b8813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084954`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY TRUE DESC NULLS FIRST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 40: `39a11556b4c349ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096195`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT OR FAIL INTO r VALUES (format('-W_0V- N_-0P6', CAST(CURRENT_TIMESTAMP COLLATE RTRIM LIKE NULL ESCAPE rowid A
```

---

## Crash 41: `d66962141236a0ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104070`

```sql
SELECT printf('%.*d', -2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT * UNION SELECT +-CURRENT_DATE ORDER BY FALSE DESC NULLS FIRST; EXPLAIN QUERY PL
```

---

## Crash 42: `42b13d97a845b734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108452`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); INSERT INTO p DEFAUL
```

---

## Crash 43: `56b54df8a5ed76ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108827`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) CHECK (b)); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 44: `8955d5d634c11338` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109009`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 45: `d7f7ac9a598934dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110622`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); INSERT OR ABORT INTO p VALUES (CURRENT_DATE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---
