# Crash Triage Report

**Total crashes:** 76  
**Unique crash sites:** 76  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 76 | 76 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9b369f39aec2d70c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000012`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT p.* FROM t2 INNER JOIN p NOT INDEXED USING (b, c3) WHERE RAISE(IGNORE) IN (FALSE, CURR
```

---

## Crash 2: `e41df39b1d38a854` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000261`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r (c3) VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP >> FALSE))) ON CONFLICT(b) DO UPDATE SET c1 = randomblob(-NULL) OVER (PARTITIO
```

---

## Crash 3: `0629e7da9513df04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000436`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); WITH RECURSIVE p AS NOT MATERIALIZED (SELECT FALSE AS a) INSERT INTO s VALUES (FALSE * RAISE(IGNORE)); SELECT t2.* FROM q NATURAL JOIN q WH
```

---

## Crash 4: `028a6883a3d5d9b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000462`

```sql
SELECT substr('6v U_', 9223372036854775807, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r DEFAULT VALUES; SELECT FALSE IS NOT NULL < CURRENT_TIME | FALS
```

---

## Crash 5: `850db31797101c9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000932`

```sql
SELECT round(1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH r (rowid) AS (VALUES (TRUE COLLATE BINARY * RAISE(IGNORE))) INSERT INTO t1 VALUES (ntile(-RAISE(IGNORE) IS NOT NULL
```

---

## Crash 6: `bd26b3c712b9a066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001120`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); SELECT +CURRENT_DATE AND ~CURRENT_TIMESTAMP > CURRENT_DATE IS NULL >= NULL NOT NULL AS a FROM p JOIN p g_d52pn17p_p
```

---

## Crash 7: `adc68c524bb6ee51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001231`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, _rowid_, c1, _rowid_); INSERT INTO t2 DEFAULT VALUES; SELECT *, t3.* FROM r WHERE EXISTS (SELECT changes() - CURRENT_TIME, RAISE(IGNORE) IS N
```

---

## Crash 8: `b137fc2a9b1f2676` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001345`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s SELECT t1.* FROM t1 GROUP BY FALSE HAVING FALSE != NULL IS NOT NULL UNION ALL SELECT 
```

---

## Crash 9: `d6b99f999c63e32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001583`

```sql
SELECT printf('%f', -1, '--RxW g _ 5 _k'); SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, _rowid_, a, a); INSERT INTO r (b) VALUES (NULL) ON CONFLICT(rowid)
```

---

## Crash 10: `9274cc5ac092df4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004029`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO t1 VALUES (CASE WHEN NULL THEN CURRENT_TIME ELSE NULL END, CURRENT_DATE ISNULL, NULL); SELECT NULL < NULL
```

---

## Crash 11: `6266ccac8fcae76b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004099`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (NOT EXISTS (VALUES (CURRENT_DATE))); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 12: `6c435bb184341f76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004120`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 13: `cd0c5c2cc11d39a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006576`

```sql
SELECT substr('-_ZW679 v7_', 2147483647, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c2); INSERT OR ABORT INTO r VALUES (NOT EXISTS (VALUES (-TRUE, RAISE(IGNORE))) A
```

---

## Crash 14: `ae1819a095ac072c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006623`

```sql
SELECT round(0.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, b, _rowid_); INSERT OR ABORT INTO t2 VALUES (CASE WHEN +TRUE THEN substr(+(CURRENT_TIMESTAMP) COLLATE RTRIM, 
```

---

## Crash 15: `9d7ce02b818e7b23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006839`

```sql
SELECT substr('_8', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIMESTAMP << CURRENT_DATE IS NOT DISTINCT FROM NULL BETWEEN FALSE AND RAISE(IGNORE) & CURRENT_
```

---

## Crash 16: `65e8c9d9350bfb37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007071`

```sql
SELECT printf('%.*g', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO r VALUES (char(sum(group_concat(FALSE COLLATE RTRIM GLOB CURRENT_TIME) FILTER (
```

---

## Crash 17: `e9f865def3d2e654` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007447`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO t2 VALUES (CASE WHEN +NOT EXISTS (SELECT FALSE IS NULL AS e9) NOT LIKE lag(NULL >= TR
```

---

## Crash 18: `c3b95c06e654e0c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008384`

```sql
SELECT printf('%.*s', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO t3 VALUES (a, ~length(NULL) IS DISTINCT FROM CURRENT_TIMESTAMP - RAISE(IGNORE)
```

---

## Crash 19: `f03c48ac66439007` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008409`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (NULL NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH p AS (SELECT TRUE >> C
```

---

## Crash 20: `c441d94f4df60d06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012374`

```sql
SELECT printf('%.*s', 9223372036854775807, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s (b) VALUES (CURRENT_TIME, CURRENT_DATE IS TRUE COLLATE RTRIM % ~CASE WHEN ~CURR
```

---

## Crash 21: `890cc2aae797e14a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016036`

```sql
SELECT substr('', -2147483649, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO p VALUES (CASE ~CURRENT_TIME COLLATE RTRIM WHEN CURRENT_TIMESTAMP COL
```

---

## Crash 22: `98274148724f2ed7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016628`

```sql
SELECT printf('%.*s', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO t3 VALUES (CASE WHEN (VALUES (CASE CURRENT_DATE WHEN ~TRUE THEN lead(NOT CURRENT_TI
```

---

## Crash 23: `6d49c824ed5eb3c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017190`

```sql
SELECT printf('%x', 2147483647, '-K'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT OR FAIL INTO q VALUES (CURRENT_DATE >> CURRENT_DATE IS NOT DISTINCT FROM FALSE < NULL); ANALY
```

---

## Crash 24: `d168f957cbfb12b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018612`

```sql
SELECT round(-1e308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); EXPLAIN QUERY PLAN SELECT * FROM t2 NOT INDEXED CROSS JOIN q LIMIT CURRENT_TIMESTAMP OFFSET (VALUES (CURRENT_TIME)
```

---

## Crash 25: `275c823b9bfc1bfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020924`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, a); INSERT INTO
```

---

## Crash 26: `87f1eda2607a63c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020933`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT hex(
```

---

## Crash 27: `366fa808ca71506d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020939`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 28: `cc0f1bf1208147e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021077`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 29: `403b1080ac65ada5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022359`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 30: `cf40482c68520db1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022915`

```sql
SELECT printf('%.*f', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); SELECT json_valid(CURRENT_DATE) FILTER (WHERE (SELECT * FROM s WHERE NULL ISNULL GROUP BY NULL WI
```

---

## Crash 31: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023631`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 32: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024312`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 33: `1213535e14144063` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025625`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 VALUES (count(*) == (VALUES (TRUE, CURRENT_TIMESTAMP) LIMIT sum(CURRENT_TIMESTAMP NOT NULL) O
```

---

## Crash 34: `f106d806de07579d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025732`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); EXPLAIN QUERY PLAN SELECT *; SELECT hex
```

---

## Crash 35: `c04a3295704e92a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026569`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); SELECT DISTINCT +CURRENT_TIMESTAMP NOT IN (CURRENT_TIME) ->> CASE WHEN CURRENT_TIME THEN N
```

---

## Crash 36: `cb594211c533dfce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029723`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); SELECT printf('%.*g',
```

---

## Crash 37: `dc476226a3241fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030177`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CASE CURRENT_DATE WHEN CURRENT_TIMESTAMP THEN TRUE END); 
```

---

## Crash 38: `9376cc8374186f1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037682`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE t3 AS (SELECT *, NULL FROM q INNER JOIN t3 NATURAL LEFT 
```

---

## Crash 39: `263d99279860761f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038550`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CASE TRUE WHEN NULL THEN NULL ELSE NULL END); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 40: `ff7f97bb8ca0be9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041923`

```sql
SELECT printf('%.*f', 4294967296, 1e308); SELECT substr('', 9223372036854775807, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, _rowid_, c2, a, c1, c3); INSERT OR ROLLBACK INTO s
```

---

## Crash 41: `a29f4dbb7201db5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042564`

```sql
SELECT substr(' _3-H6_4--3G ', -2147483649, 2147483648); SELECT substr('', -2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO s VALUES (CURRENT_DATE, RAISE(IGNO
```

---

## Crash 42: `55adc3759af48d13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046909`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (cume_dist() OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO t1 VALUES (FALSE 
```

---

## Crash 43: `9e19d9efb2aba0ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047299`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME MATCH dense_rank() OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c2); INSERT OR AB
```

---

## Crash 44: `2eecc381eed3e612` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048208`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CAST(CURRENT_TIME AS INTEGER)); SELECT printf('%.*d', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 45: `84c33f02378fae44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049228`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (NULL = CURRENT_TIME AND CURRENT_DATE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 46: `412b6ab4801643bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049538`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (CURRENT_TIME AND CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c3, c2); SELECT p.* FROM (SELECT r.*, r.*, 
```

---

## Crash 47: `a7d2b1948b1d3108` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052564`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (rank() OVER (PARTITION BY NULL ORDER BY FALSE DESC NULLS FIRST)) UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 48: `bf1007b7bf7cbea0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052775`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 49: `20048ab34aee4880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052781`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (CURRENT_TIME) UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 50: `6a2bdb1acbee7a47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052787`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (rank() OVER ()) UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 51: `1b51b8d5679558c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053301`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (CURRENT_TIMESTAMP + CURRENT_TIME) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (
```

---

## Crash 52: `81a66078aa9781f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053354`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (FALSE) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (NULL ISNULL) EXCEPT VALUES 
```

---

## Crash 53: `a3da27fa8f0c521a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053436`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (lead(FALSE, CURRENT_DATE, CURRENT_TIME) OVER ()) UNION VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 54: `a761f2ca0c63877b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053600`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (dense_rank() OVER ()) UNION VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 55: `d5499d40c3938a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061368`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 56: `5d26bc1d85d29246` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062608`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT X'cE804Be1'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE VIRTUAL 
```

---

## Crash 57: `f0f009a876351e4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062645`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 58: `3bbdb3b727573058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 59: `45ca432ee8ed7da9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062933`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT 4439477549347694.948 AS k_; CREATE VI
```

---

## Crash 60: `9831b1bbd009b486` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070511`

```sql
SELECT round(1e-308, 4294967295); SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); INSERT INTO p VALUES (-~CURRENT_TIMESTAMP - TRUE / FALSE BETWEEN CAS
```

---

## Crash 61: `546d627152619607` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076271`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); 
```

---

## Crash 62: `e988e28cdea3c413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078652`

```sql
SELECT substr('_9w_C9-0S', 4294967295, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (CURRENT_DATE) INTERSECT SELECT RAISE(IGNORE) FROM r INDEXED BY a EXCEPT SELECT ALL * FROM 
```

---

## Crash 63: `50357e120f942d83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089859`

```sql
SELECT substr('8_P', 4294967296, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); WITH RECURSIVE t2 AS (SELECT RAISE(IGNORE) COLLATE BINARY AS f__e2_or_2_a_8h3b_81k_l3_o9_j_1
```

---

## Crash 64: `dc8b24fac8aa5301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089914`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (random()); VALUES (TRUE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 65: `39220f73b2fc4f84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090443`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (FALSE); VALUES (TRUE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 66: `9ce3987cdc67f725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090449`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); VALUES (TRUE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 67: `959210e9396e51d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102615`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); VALUES (FALSE) INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); EXPLAIN QUERY PLAN SELECT *; SELECT 
```

---

## Crash 68: `b1ffa32a4ced3734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113146`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, c2 INT GENERATED ALWAYS AS (FALSE IS NOT FALSE >= FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integ
```

---

## Crash 69: `e4fbb752024f08eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116959`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, c2 INT GENERATED ALWAYS AS (FALSE IS NOT FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 70: `0a6d635717318a6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117025`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, c1 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 71: `c4275da23474ca03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133965`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL
```

---

## Crash 72: `2f13b9d8a9df2093` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134108`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (random()); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); I
```

---

## Crash 73: `a51b6d53a25c01d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134245`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); REPLACE INTO p VALUES (random()); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); I
```

---

## Crash 74: `29226a298bb9e2c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135000`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT); REPLACE INTO p VALUES (random()); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE I
```

---

## Crash 75: `cad5bcd7837d1092` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141621`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (count(DISTINCT FALSE) FILTER (WHERE CURRENT_TIME)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 76: `8035ff67ef153048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142088`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, rowid GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME, CURRENT_TIMESTAMP) EXCEPT SELECT * FROM p WHERE TRUE ORDER BY CURR
```

---
