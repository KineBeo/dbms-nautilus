# Crash Triage Report

**Total crashes:** 49  
**Unique crash sites:** 49  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 49 | 49 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `f0ab1ba7f1b8175d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000058`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL GENERATED ALWAYS AS (~CURRENT_TIME) VIRTUAL, c3 DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO t2 VALUES (-RAISE(IGNORE) & NULL COLLAT
```

---

## Crash 2: `d555657f7acbf779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000142`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB, rowid GENERATED ALWAYS AS (a) ); INSERT INTO p (b, c1, c3) VALUES (ntile(~FALSE >> ~FALSE) OVER (ORDER BY NOT RAISE(IGNORE) DESC NULLS LAST ROWS BETWEEN -NUL
```

---

## Crash 3: `01297d89a76ab6a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000226`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); REPLACE INTO t2 VALUES ((RAISE(IGNORE)), RAISE(IGNORE) GLOB FALSE -> CURRENT_TIME, NU
```

---

## Crash 4: `007d16af3d0e1896` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000276`

```sql
SELECT round(0.0, -2147483649);
```

---

## Crash 5: `af62f06cdd502a59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000419`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(rowid, a, a, _rowid_, c2, rowid, b, c2, a); WITH RECURSIVE p (_rowid_, c1, a, _rowid_) AS NOT MATERIALIZED (VALUES (NULL ISNULL) ORDER BY CURRENT_T
```

---

## Crash 6: `eeb900bd2ca0f220` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000960`

```sql
SELECT substr('', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); INSERT OR REPLACE INTO t3 VALUES (CURRENT_TIME); VALUES (+TRUE >> CURRENT_TIMESTAMP) ORDER BY FALSE / RAISE(IGN
```

---

## Crash 7: `f16355ff19ad9151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001137`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL, c3 BOOLEAN GENERATED ALWAYS AS (-TRUE COLLATE NOCASE REGEXP json_extract(CASE NOT EXISTS (VALUES (FALSE MATCH NULL, count(TRUE) FILTER (WHERE TRUE))) WH
```

---

## Crash 8: `fe6751c96dc13413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001437`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT, a GENERATED ALWAYS AS (c2) UNIQUE, c3 INTEGER GENERATED ALWAYS AS ((VALUES (RAISE(IGNORE) NOT BETWEEN TRUE AND NULL COLLATE NOCASE, TRUE NOTNULL)) << -(CASE WHEN (
```

---

## Crash 9: `04a77cbf27428c3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001463`

```sql
SELECT printf('%.*g', 2147483647, -0.0);
```

---

## Crash 10: `a5c26657fa2929bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000009006`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (last_insert_rowid() FILTER (WHERE NOT FALSE) NOT LIKE CURRENT_TIME + rank() >= CURRENT_TIME MATCH CURREN
```

---

## Crash 11: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011815`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 12: `8e3229248001f98b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000011944`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN GENERATED ALWAYS AS (lag(RAISE(IGNORE) IN (VALUES (TRUE)), CURRENT_TIME) ISNULL / TRUE * CAST(CURRENT_TIME AS FLOAT) IN (TRUE, TRUE) <= NULL COLLATE BINARY <
```

---

## Crash 13: `76c7d1ab2f44a210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011959`

```sql
SELECT substr('', 4294967295, 2147483647); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 14: `935ea575fbebc2cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012002`

```sql
SELECT hex(zeroblob(-1)); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 15: `6859592c1403e98e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000012992`

```sql
SELECT substr(' s oj3_-', 1); SELECT printf('%.*s', -9223372036854775808);
```

---

## Crash 16: `b4088fb5e9dd70ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000013203`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO t3 (c2) VALUES (count(randomblob(CURRENT_TIMESTAMP LIKE TRUE ESCAPE CURRENT_TIME) * CUR
```

---

## Crash 17: `5dbef5cbc360f3f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000013452`

```sql
SELECT printf('%lld', 4294967295, '3 U9');
```

---

## Crash 18: `306855680823bb71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000013505`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a + -0) NOT NULL, c1 REAL NOT NULL); SELECT ~CURRENT_TIMESTAMP NOT IN (FALSE) > CURRENT_TIME % TRUE AS a FROM (SELECT r.* FROM t1 W
```

---

## Crash 19: `73619f3739ae6a42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000014051`

```sql
SELECT printf('%f', 9223372036854775807, '8-_-b p_ G46 '); SELECT hex(zeroblob(1));
```

---

## Crash 20: `d6f7763c86f4742b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000015492`

```sql
SELECT round(1e-308, 4294967295); CREATE TABLE IF NOT EXISTS p(c2 TEXT, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO s DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 21: `0c083568cbc99328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016196`

```sql
SELECT printf('%.*d', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 (b, c1) VALUES (NOT EXISTS (WITH RECURSIVE r AS MATERIALIZED (SELECT * LIMIT
```

---

## Crash 22: `c10d48cf2f8b4f9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000017045`

```sql
SELECT substr(' _ -IbvZ-', 2147483648, -2147483649);
```

---

## Crash 23: `d0e936e907b66b8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020903`

```sql
SELECT substr('e_r', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 VALUES (NOT NOT CURRENT_TIME <= CURRENT_TIMESTAMP / NULL % -CURRENT_TIMESTAMP -> TRUE, CURREN
```

---

## Crash 24: `fbbaad039bd35110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000021302`

```sql
SELECT round(1.0, 1); CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE TABLE IF NOT EXISTS q(rowid TEXT); VALUES (CASE WHEN TRUE -> NULL | NULL NOTNULL <> NOT RAISE(IGNORE) NOT BETWEEN ~CURRENT_DATE IS
```

---

## Crash 25: `4729e46d195df93d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000025402`

```sql
SELECT round(-1.0, 0); SELECT substr('D-jgh_-__ B___', -9223372036854775808); SELECT printf('%x', 2147483647, '-_42q- z ');
```

---

## Crash 26: `c682e6b8988cc9fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000025648`

```sql
SELECT printf('%.*e', -9223372036854775808, 1.0);
```

---

## Crash 27: `ec44ac18bb7507de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000027991`

```sql
SELECT printf('%.*g', 2147483648); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); INSERT OR ABORT INTO t3 VALUES (CURRENT_DATE COLLATE RTRIM); ANALYZE t3;
```

---

## Crash 28: `fdc7d2899793b3dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029419`

```sql
SELECT printf('%.*g', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT DISTINCT TRUE FROM t2 UNION ALL SELECT ALL s.* FROM t3 ORDER BY +CURRENT_TIME IN (VALUES (FALSE)) ->> -4
```

---

## Crash 29: `9c12aac499ec1200` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000029853`

```sql
SELECT printf('%.*e', 4294967296); SELECT printf('%s', -2147483648, '_-1 _--Q- '); CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT FALSE != TRUE <> -CURR
```

---

## Crash 30: `28d09e54a64b241e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030547`

```sql
SELECT substr('-_Cp9', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, a); INSERT INTO t3 VALUES (EXISTS (VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP & NULL)), (FALSE)
```

---

## Crash 31: `6422b0e1335ffdef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000030553`

```sql
SELECT substr('-_Cp9', 4294967295); CREATE TABLE IF NOT EXISTS p(b INT GENERATED ALWAYS AS (c2) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO t3 SELECT ~CURRENT_DATE COLLATE RTR
```

---

## Crash 32: `6aa90c615c9ed1da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000030561`

```sql
SELECT printf('%.*d', -2147483648); SELECT hex(zeroblob(0));
```

---

## Crash 33: `85767c13ce78578b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000035834`

```sql
SELECT printf('%.*s', 0, -1.0);
```

---

## Crash 34: `95336e04f71ce1fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000041669`

```sql
SELECT substr('-_Cp9', 4294967295); CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT NOT +(VALUES (RAISE(IGNORE))) BETWEEN EXISTS (SELECT t2.* FROM s
```

---

## Crash 35: `1e8925ad0f3660c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000044911`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (-lead(TRUE NOTNULL, ~(NULL) COLLATE BINARY IS NOT DISTINCT FROM FALSE * RAISE(IGNORE)) % CURRENT_TIME COLLATE BINARY <= FALSE == -CURRENT_DATE == NULL | CURRE
```

---

## Crash 36: `e747f6710011eaf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000046685`

```sql
SELECT substr('-_Cp9', 4294967295); SELECT round(-0.0, 2147483647);
```

---

## Crash 37: `4ae9ebc556b00a44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047482`

```sql
SELECT round(-1e308, -2147483649); SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*s', 1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2, a); INSERT INTO s VALUES
```

---

## Crash 38: `90fd7ba4cda8f3a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052116`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY, c3 DATE CHECK (-TRUE == +CURRENT_TIMESTAMP NOT BETWEEN RAISE(IGNORE) AND FALSE == CASE WHEN count() OVER w0 THEN NULL BETWEEN (SELECT *, *) AND (RAISE
```

---

## Crash 39: `b9765c45936c4423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052448`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT, b GENERATED ALWAYS AS (coalesce(a, b)) , rowid BOOLEAN CHECK (1072 COLLATE NOCASE)); WITH RECURSIVE s AS NOT MATERIALIZED (WITH p (_rowid_) AS (SELECT p.* INT
```

---

## Crash 40: `c6f2063ee7a765dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052699`

```sql
SELECT printf('%.*g', 4294967296); CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL, rowid BLOB DEFAULT 'W_-Xmn__- X', c2 FLOAT NOT NULL, _rowid_ NUME
```

---

## Crash 41: `5b8c4f68560948c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000053219`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT CURRENT_TIMESTAMP, c2 BLOB GENERATED ALWAYS AS (CASE RAISE(IGNORE) IS NOT NULL / +NULL ->> FALSE <> CURRENT_TIMESTAMP IS NOT NULL REGEXP CURRENT_DA
```

---

## Crash 42: `a3f5b82dd2d5ddb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000060800`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (+dense_rank())); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO t1 DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT EXISTS (VALUES (CURRENT_TIMESTAMP & C
```

---

## Crash 43: `9b53d7d7e8184e81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000066990`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c1, b, rowid, rowid); INSERT INTO t1 VALUES (NULL) RETURNING *; EXPLAIN QUERY PLAN VALUES ((SELECT DISTINCT q.* FROM q NOT INDEXED INTERSECT
```

---

## Crash 44: `9e877b76a2195f34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000069501`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT FALSE, c3 VARCHAR(255) NOT NULL DEFAULT 'i1k G f _1_Wp2', c3 TEXT, a REAL GENERATED ALWAYS AS (CASE CURRENT_DATE -> count(*) | CURRENT_TIME COLLATE NOCA
```

---

## Crash 45: `909873adf4aeeaf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000076656`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); INSERT OR FAIL INTO p VALUES (~NOT EXISTS (VALUES (FALSE <= CURRENT_DATE + -NULL LIKE CURRENT_DATE ESCAPE CURRENT_TIMESTAMP == CAST(TRUE AS DATE) 
```

---

## Crash 46: `b5a116d6f7b56ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000076758`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT GENERATED ALWAYS AS (lead(RAISE(IGNORE) IN (FALSE)) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) < NULL COL
```

---

## Crash 47: `2a98df2a09c37b6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000080572`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT CURRENT_TIME COLLATE NOCASE NOTNULL < TRUE IS NULL NOT NULL GLOB CASE NULL NOT IN (SELECT *) WHEN TRUE NOT
```

---

## Crash 48: `77c5ebf54499a6cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082312`

```sql
SELECT printf('%.*d', 2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, b, _rowid_, _rowid_, c2, c1); INSERT OR REPLACE INTO s VALUES (lead(FALSE IS NULL IS RAISE(IGNORE)
```

---

## Crash 49: `3ce91f775cf455e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000099076`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF 
```

---
