# Crash Triage Report

**Total crashes:** 167  
**Unique crash sites:** 166  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 164 | 164 | 98% |
| Signal | 2 | 3 | 1% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `8bc28dd6c969fd49` — signal (signal-6)

- **Count:** 2 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037843`

```sql
WITH RECURSIVE t2 AS (VALUES (+-1240.9563689039461985 NOT BETWEEN RAISE(IGNORE) AND NULL * ~CURRENT_TIMESTAMP LIKE CURRENT_TIME * CAST(FALSE == +TRUE AS INT), CASE NULL NOT NULL WHEN NULL <= CURRENT_T
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  yy_reduce
  sqlite3Parser
```

---

## Crash 2: `4d24f1060c86d882` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 3: `272e6f0a573628f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000423`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c2, c2, _rowid_);
```

---

## Crash 4: `329b9cfca549e8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005713`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 5: `2fe2ccd2799f4ac2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005940`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 6: `4a98cd08f9db3319` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006844`

```sql
CREATE TEMP VIEW v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2);
```

---

## Crash 7: `cc9754fb5c5a6390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007349`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 8: `5c5d86b69a9e7c18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007480`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); DROP VIEW IF EXISTS v1;
```

---

## Crash 9: `b3d9466ff7ce1cdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008263`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); BEGIN IMMEDIATE;
```

---

## Crash 10: `2114a71bfafb86e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009536`

```sql
PRAGMA analysis_limit=5; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 11: `2fab4f90d381216a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009565`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 12: `3815f4281ea4bb5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009571`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 13: `ca04cea436679c67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009743`

```sql
VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `d8ed4555540e125f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010236`

```sql
ATTACH DATABASE ':memory:' AS db2; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, _rowid_, c1); DETACH db2; UPDATE t2 SET _rowid_ = NOT CURRENT_TIME COLLATE
```

---

## Crash 15: `48542e71bf192372` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010340`

```sql
CREATE VIEW v1 (c2, c3) AS VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 16: `5ab209a881f159e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010420`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 17: `0d46979df2264827` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011181`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 18: `a18e3564d94903ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011191`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 19: `c1fbe724d1865366` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011302`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 20: `b635b2d13b780e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011333`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 21: `2d5c4f9b93c9d4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011882`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ATTACH ':memory:' AS db2;
```

---

## Crash 22: `53f0cedd71d1e38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012741`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 23: `d99da40fe2cd666d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014203`

```sql
CREATE TABLE t3 (rowid DATE COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PRAGMA quick_check;
```

---

## Crash 24: `1c5ded145b42e229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016825`

```sql
BEGIN TRANSACTION; ROLLBACK TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 25: `4fe4e5b81829f20b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017368`

```sql
BEGIN; CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 26: `202bafc83f0f292d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017481`

```sql
BEGIN; CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP); ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 27: `83e0fcff10f5b604` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022259`

```sql
CREATE TEMP TABLE t3 (c1 BLOB PRIMARY KEY, rowid DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 28: `c96995d0c556c8e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023031`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 29: `aef037e1596f15b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024239`

```sql
CREATE TEMP TABLE t1 (c3 NUMERIC NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c1); ALTER TABLE t3 ADD COLUMN c2 BOOLEAN CHECK (CASE WHEN 
```

---

## Crash 30: `b0de571a3ba841a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026770`

```sql
ANALYZE; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3);
```

---

## Crash 31: `12132124dbe69be3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026905`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3);
```

---

## Crash 32: `8dece2e0979cacbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027141`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, c
```

---

## Crash 33: `f4e869eb04a185b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027194`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); BEGIN IMMEDIATE;
```

---

## Crash 34: `82a29d24f996ef2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030496`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT DISTINCT * FROM t1 NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIMESTAMP ORDER BY TRUE NULLS LAST; CREATE VIRTUAL TABLE I
```

---

## Crash 35: `5cd6dd0a8c016d65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030866`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM (VALUES (RAISE(IGNORE))) AS otx5d79ei_p_5d__63tf_64__q__32p6_xu__408___1sly5_ij4__5v3e_02_s8_l_56_k6_b26afg4__m
```

---

## Crash 36: `89012e226b7b6af4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030878`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t3 NOT INDEXED NATURAL CROSS JOIN (t1 INNER JOIN t3 NOT INDEXED ON TRUE) WHERE NULL GROUP BY FALSE WINDOW w1 AS
```

---

## Crash 37: `d8cba090c518108f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031582`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BOOLEAN NOT NULL DEFAULT CURRENT_DATE, c2 TEXT REFERENCES t1 (c2) ON DELETE NO ACTION); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 38: `8d5b076ba8c55dd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031630`

```sql
DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 39: `fd26d2ebf431c4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032772`

```sql
PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 40: `e023f53965e145cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034466`

```sql
PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c3, c2);
```

---

## Crash 41: `ea92ab8ab5da35c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035039`

```sql
CREATE VIEW IF NOT EXISTS v1 (rowid) AS SELECT * EXCEPT SELECT DISTINCT * FROM t1 NOT INDEXED WHERE TRUE GROUP BY NULL, NULL HAVING TRUE ORDER BY FALSE ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 42: `8337c7d58094b553` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035084`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 43: `fda305e83e5f2223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035561`

```sql
CREATE TABLE t1 (_rowid_ INTEGER, PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 44: `52d121e8e122243f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037590`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT DISTINCT * FROM t2 WHERE TRUE GROUP BY -5.87E+4048077996665057689960824458169028908160088450438254796922560717087542769869007709726501807025696888806025978510693
```

---

## Crash 45: `92973a0bd543d3d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037596`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT * FROM t2 LEFT OUTER JOIN t3 NOT INDEXED USING (c3) WHERE TRUE) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE
```

---

## Crash 46: `692574c8d2d5a6b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037602`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (count(*) FILTER (WHERE EXISTS (SELECT DISTINCT *)), FALSE COLLATE BINARY)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY F
```

---

## Crash 47: `4e174ca247c03e55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037608`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM (SELECT DISTINCT count(*) ORDER BY NOT CURRENT_DATE, CURRENT_DATE) AS z NATURAL LEFT OUTER JOIN t3 NOT INDEXED 
```

---

## Crash 48: `2eb0f8fe7e6e86ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037614`

```sql
WITH t1 AS (VALUES (TRUE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 49: `62db08aa0920b5b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037623`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_TIMESTAMP LIKE CURRENT_DATE ESCAPE CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINA
```

---

## Crash 50: `104ae407d82f1baf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037629`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM (t1 INNER JOIN t3 NOT INDEXED ON TRUE) GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULL
```

---

## Crash 51: `314ee35212fa7c96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037639`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM t1 NOT INDEXED WHERE (CURRENT_TIME, NULL) GROUP BY CURRENT_TIMESTAMP UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w
```

---

## Crash 52: `8e5b9855c67b1171` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037645`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY FALSE / TRUE IS TRUE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 53: `3b84203698c055e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037652`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT * FROM t3 NOT INDEXED WHERE RAISE(IGNORE) GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS (ORDER BY FALSE DESC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AN
```

---

## Crash 54: `3daa4bbe286cacf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037664`

```sql
WITH t2 AS (SELECT *) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 55: `cf4b64271a4183d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037670`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (changes() FILTER (WHERE EXISTS (VALUES (TRUE))), FALSE COLLATE BINARY) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER
```

---

## Crash 56: `473f7e6980a24b4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037678`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT TRUE AS ig49 FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION
```

---

## Crash 57: `12ca22780ad88c4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037696`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY NOT EXISTS (VALUES (RAISE(IGNORE)) UNION ALL SELECT DISTINCT * FROM t3 NOT INDEXED WHERE FALSE GROU
```

---

## Crash 58: `f72ea41ad279b10f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037703`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT * LIMIT TRUE OFFSET TRUE) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 59: `54d2773f84749dfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037713`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) SELECT DISTINCT group_concat(CURRENT_TIMESTAMP, 's_-----') OVER (PARTITION BY c2 ORDER BY NULL DESC NULLS LAST) AS a UNION SELECT * FROM t2 GROUP
```

---

## Crash 60: `20a7df532b555d9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037719`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE << CURRENT_TIME WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSA
```

---

## Crash 61: `bcdef1b50953609d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037726`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (NULL IS NOT NULL) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTIO
```

---

## Crash 62: `244b7ab676c8f3ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037733`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE MATCH NULL || FALSE = CURRENT_DATE ISNULL NOTNULL ISNULL
```

---

## Crash 63: `35f5aa3aa1830240` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037740`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT count(*) OVER (PARTITION BY NULL ORDER BY FALSE IN (SELECT * FROM t2) DESC NULLS FIRST) FROM t2 GROUP BY CURRENT_DATE 
```

---

## Crash 64: `f8eb09d1c0654a17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037747`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY NULL HAVING count(*) OVER (ORDER BY CURRENT_DATE DESC NULLS LAST ROWS BETWEEN CURRENT ROW AND RAISE
```

---

## Crash 65: `806e26e0f26f2c3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037753`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t3 LEFT OUTER JOIN (t3) GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN T
```

---

## Crash 66: `de3951ea879d80ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037759`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (RAISE(IGNORE) NOT IN (RAISE(IGNORE)), TRUE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST
```

---

## Crash 67: `f53503b894132832` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037765`

```sql
WITH RECURSIVE t1 AS (SELECT DISTINCT *), t2 AS (SELECT DISTINCT *) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTI
```

---

## Crash 68: `6326c605a071e784` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037771`

```sql
WITH t3 (c1) AS (SELECT * LIMIT CURRENT_DATE, CURRENT_TIMESTAMP) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 69: `81e2b34325d97cdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037778`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (t1.c1, NULL)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANSACTION;
```

---

## Crash 70: `a7ae30c70e4b4037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037785`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT DISTINCT t1.*, * FROM t2 NOT INDEXED WHERE CASE TRUE WHEN CURRENT_TIME THEN CURRENT_DATE END - CURRENT_TIMESTAMP LIKE RAISE(IGNORE) ESCAPE RAISE(IGNORE) / CURREN
```

---

## Crash 71: `0f685a49e0be46b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037793`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (CURRENT_DATE <= CURRENT_DATE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGI
```

---

## Crash 72: `60200c62a43a4619` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037800`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (CURRENT_DATE NOT LIKE RAISE(IGNORE), CURRENT_DATE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BI
```

---

## Crash 73: `16fc9adb53312ea1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037893`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t1 AS zd2qk00i7554ucd4d_k0_vt0_ CROSS JOIN t3 INNER JOIN t2 AS j73v__ GROUP BY CURRENT_DATE WINDOW w1 AS () ORD
```

---

## Crash 74: `c8d260c314475b6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039383`

```sql
WITH t1 AS (VALUES (TRUE)) VALUES (TRUE) UNION SELECT DISTINCT CURRENT_TIMESTAMP AS f FROM t1 NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC; CREATE VIRTUAL TABLE I
```

---

## Crash 75: `7b6d313f26d3fb3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045495`

```sql
WITH RECURSIVE t1 (_rowid_) AS (SELECT DISTINCT TRUE ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST, CURRENT_DATE) VALUES (TRUE) UNION SELECT DISTINCT * FROM t1 NOT INDEXED WHERE FALSE GROUP BY CURRENT_T
```

---

## Crash 76: `f27bfba1d54f6c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047636`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE t3 AS VALUES (TRUE); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); BEGIN IMMEDIATE
```

---

## Crash 77: `d39dd9c5967fd5b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047921`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY ASC, _rowid_ INTEGER UNIQUE); ANALYZE; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 78: `7de7c96c648245af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049007`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 79: `8047c82bb4adf22c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049971`

```sql
CREATE TABLE t3 (rowid NUMERIC NOT NULL, PRIMARY KEY (rowid), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 80: `8285cba3c749a2ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050223`

```sql
CREATE TABLE t3 AS VALUES ((VALUES (CURRENT_DATE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 81: `dc436eff91818d3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050950`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 INTEGER PRIMARY KEY DESC); CREATE INDEX idx1 ON t2 (c3, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t2 (c2) AS NOT MATERIALIZED
```

---

## Crash 82: `d3b01a2bd0759196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051399`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 INTEGER PRIMARY KEY DESC); CREATE TEMP TABLE t3 (c1 REAL PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 83: `ae59acd4455e39f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053055`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); DELETE FROM t3 WHERE ~CASE CURRENT_TIME / TRUE <= NULL WHEN changes() THEN ~TRUE >> CURRENT_TIMESTAMP IS
```

---

## Crash 84: `b68e4d2d60fc2dda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054908`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY, _rowid_ REAL UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 85: `748e15d3e0cb9fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056601`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); UPDATE t3 SET c3 = RAISE(ABORT, '5_-v_') WHERE (NOT RAISE(IGNORE) ->> NOT NULL >= NULL NOTNULL IS NOT NULL LIKE 
```

---

## Crash 86: `6afbca2a8a4c9a04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056610`

```sql
PRAGMA cache_size=+973; BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); ATTACH ':memory:' AS db2; DETACH db2; INSERT OR FAIL INTO t1 VALUES (CASE -json_extrac
```

---

## Crash 87: `94e8ef2a9edbed79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064897`

```sql
CREATE TABLE t3 (c2 FLOAT PRIMARY KEY DESC, rowid INT NOT NULL, UNIQUE (rowid) ON CONFLICT REPLACE, CHECK (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE UNIQUE 
```

---

## Crash 88: `139ff6f06e53a177` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065545`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 NUMERIC PRIMARY KEY DESC); CREATE TRIGGER trg1 AFTER INSERT ON t3 BEGIN DELETE FROM t3; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 89: `35a5c16a8c8c07ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066675`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ BOOLEAN CHECK (CAST(FALSE AS BLOB) IS NOT NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 90: `e5379e99b1c3e406` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072050`

```sql
CREATE TABLE t2 (_rowid_ BLOB PRIMARY KEY DESC) WITHOUT ROWID; ATTACH DATABASE ':memory:' AS db2; BEGIN DEFERRED TRANSACTION; COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 91: `dcad5224ce60251c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073244`

```sql
CREATE TABLE t3 (c1 REAL CHECK (FALSE), _rowid_ INTEGER UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW IF NOT EXISTS v1 (_rowid_) AS WITH t3 AS NOT MATERIALIZED (SELECT
```

---

## Crash 92: `8e7c904c1afb1e38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074419`

```sql
CREATE VIEW v1 AS SELECT * FROM t2 GROUP BY FALSE WINDOW w1 AS (ORDER BY CURRENT_DATE DESC NULLS LAST ROWS BETWEEN CURRENT ROW AND RAISE(IGNORE) FOLLOWING) UNION ALL SELECT ALL *; CREATE VIRTUAL TABLE
```

---

## Crash 93: `1d1f7822aaa2943e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074562`

```sql
CREATE VIEW v1 AS VALUES (RAISE(IGNORE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 94: `79623e3cea2d56b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074572`

```sql
CREATE VIEW v1 AS SELECT * FROM t2 GROUP BY FALSE WINDOW w1 AS (ORDER BY CURRENT_DATE DESC NULLS LAST RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) UNION ALL SELECT ALL *; CREATE VIRTUAL 
```

---

## Crash 95: `e6f2763807dc0ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077697`

```sql
CREATE TABLE t3 (c1 NUMERIC COLLATE NOCASE, FOREIGN KEY (c1) REFERENCES t3 (c2) DEFERRABLE INITIALLY DEFERRED, CHECK (RAISE(IGNORE))); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 96: `478269469c0d2fe2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077808`

```sql
PRAGMA wal_checkpoint(FULL); PRAGMA cache_size=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 97: `23d3a0484552fe10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077850`

```sql
PRAGMA integrity_check; PRAGMA cache_size=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 98: `8430b315c4e90710` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078856`

```sql
VALUES (count(*) OVER (PARTITION BY TRUE ORDER BY CURRENT_DATE ASC NULLS LAST ROWS UNBOUNDED PRECEDING)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 VALUES (CURRENT_TIME 
```

---

## Crash 99: `22e96704d840bcba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080692`

```sql
CREATE TABLE t3 (c1 BOOLEAN PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); BEGIN IMMEDIATE;
```

---

## Crash 100: `766bc057dbfec5b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081285`

```sql
CREATE TABLE t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); DELETE FROM t1 WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 101: `c4a405854bc81702` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081335`

```sql
CREATE TABLE t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 102: `f9db719bee659be5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081341`

```sql
CREATE TABLE t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); DELETE FROM t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 103: `bae5ee219e6aef17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083127`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); BEGIN IMMEDIATE;
```

---

## Crash 104: `acee551d43ba316c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083418`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE TABLE t3 (rowid INT NOT NULL); SELECT TRUE, * FROM t3 INNER JOIN (SELECT * UNION ALL SELECT t1.* LIMIT CURR
```

---

## Crash 105: `d9c809c80e6d1173` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083536`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA journal_mode=PERSIST;
```

---

## Crash 106: `fcf607fc274056d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084181`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 107: `15e2d52b42004fa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085089`

```sql
ATTACH DATABASE ':memory:' AS db2; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 108: `c1b0a742d6a5a976` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085681`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY, _rowid_ REAL UNIQUE) WITHOUT ROWID; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); WITH RECURSIVE t1 (rowid, c1, c3, 
```

---

## Crash 109: `20f4dce74d0c4b00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091258`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 110: `dfb9eb0c8f11b31e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091769`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY, _rowid_ REAL UNIQUE) WITHOUT ROWID; VACUUM; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 111: `c0aef3baeca558cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092111`

```sql
CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); ANALYZE; ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 112: `69c9b4ec9b7434b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092191`

```sql
CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); ALTER TABLE t1 RENAME COLUMN _rowid_ TO c3; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 113: `50b2621003a6c1d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094132`

```sql
CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); INSERT INTO t1 (_rowid_) VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integrity_check;
```

---

## Crash 114: `c7b7741013517785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094256`

```sql
CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integrity_check;
```

---

## Crash 115: `d59295d6b5256321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094760`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); BEGIN DEFERRED; REINDEX t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA 
```

---

## Crash 116: `8574cb2b5d176d49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094884`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC); BEGIN DEFERRED; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 117: `7520b7e2af4ed450` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095113`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE t3 AS VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); CREATE INDEX 
```

---

## Crash 118: `bf82f592a961b9f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095215`

```sql
BEGIN DEFERRED; CREATE TABLE t3 AS SELECT ALL NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integrity_check;
```

---

## Crash 119: `c24d1a3b9ed0f92c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095234`

```sql
VALUES (-CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integrity_check;
```

---

## Crash 120: `14885098d458c651` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095242`

```sql
VALUES (CURRENT_TIME IS NOT NULL / CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integ
```

---

## Crash 121: `3603096dcdffbaf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095248`

```sql
CREATE TABLE t3 (c1 REAL CHECK (FALSE NOT BETWEEN CURRENT_DATE AND RAISE(IGNORE)), _rowid_ INTEGER UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TA
```

---

## Crash 122: `1cdf18bb3e85e130` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095275`

```sql
CREATE TABLE t3 AS SELECT ALL 62516781679393081567970910156862.58402641281210630; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 123: `7fd5a309251124ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095288`

```sql
BEGIN DEFERRED; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME & TRUE NOT IN (SELECT DISTINCT * LIMIT NULL) DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 124: `ff96366fe929314e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095302`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRAGMA integrity_check;
```

---

## Crash 125: `15be3db03f91413b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095740`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 126: `683b63121af8054b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096865`

```sql
CREATE TABLE t1 (c3 INT NOT NULL REFERENCES t2 (_rowid_) ON DELETE SET DEFAULT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); ROLLBACK TRANSACTION;
```

---

## Crash 127: `3dc200d8b86c6d57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097966`

```sql
CREATE TABLE t1 (c1 FLOAT NOT NULL DEFAULT X'04Bcfff6'); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 128: `b2eac634ee9366db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098058`

```sql
CREATE TABLE t3 (c3 FLOAT UNIQUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 129: `7400abb265bef081` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098066`

```sql
CREATE TABLE t1 (c1 FLOAT NOT NULL DEFAULT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 130: `f605472d3606d260` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099426`

```sql
CREATE TABLE t1 (c1 FLOAT UNIQUE, _rowid_ VARCHAR(255) PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2);
```

---

## Crash 131: `bacf77030aba149c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099831`

```sql
VALUES (CURRENT_DATE NOT LIKE CURRENT_TIME NOT IN (WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLL
```

---

## Crash 132: `744833e61e6a2b45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099922`

```sql
VALUES (CURRENT_DATE NOT LIKE CURRENT_TIME NOT IN (VALUES (TRUE)), CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 133: `762f0ac51e1ff458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100048`

```sql
VALUES (FALSE, CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 134: `58d37a7ca4073b3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100054`

```sql
VALUES (CURRENT_DATE NOT LIKE FALSE, CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 135: `43f462d1515d5def` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100502`

```sql
VALUES (count(DISTINCT CURRENT_TIMESTAMP), CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 136: `05485e03a6cd3166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100563`

```sql
VALUES (changes(), CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 137: `335a41f968d049e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100712`

```sql
VALUES (TRUE LIKE TRUE ESCAPE TRUE, CURRENT_DATE); BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, rowid, c3); UPDAT
```

---

## Crash 138: `e2c165e04bc97d27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101056`

```sql
VALUES (NOT 0.0, CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 139: `4505189ca54501fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101349`

```sql
VALUES (count(*) OVER (PARTITION BY TRUE ORDER BY CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 140: `9fe61a1973011be4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101400`

```sql
VALUES (count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 141: `87074fad8718e912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103277`

```sql
CREATE VIEW v1 (c3) AS SELECT DISTINCT * ORDER BY RAISE(IGNORE) DESC NULLS LAST, FALSE DESC NULLS FIRST LIMIT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 142: `15cf9f7798b5f39d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105924`

```sql
CREATE TABLE t3 (c1 REAL CHECK (TRUE MATCH NULL || FALSE = CURRENT_DATE NOTNULL ISNULL), _rowid_ INTEGER UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 143: `ae95f4d25c043726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106262`

```sql
CREATE TABLE t3 (c1 REAL CHECK (CURRENT_DATE < TRUE), _rowid_ INTEGER UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid
```

---

## Crash 144: `3bb259be9417f334` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107146`

```sql
CREATE TABLE t3 (_rowid_ REAL PRIMARY KEY ASC); INSERT INTO t3 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t1 SET rowid = c1 >= max(RAISE(IGNORE) NOT NULL NOT NULL
```

---

## Crash 145: `d5b538a251cc8896` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108308`

```sql
CREATE TABLE t3 (rowid DATE COLLATE NOCASE); CREATE TRIGGER trg1 AFTER INSERT ON t3 BEGIN DELETE FROM t3; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 146: `b0bef57cc1c5e9bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113286`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c2, c1, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH t3 AS (WITH RECURSIVE t1 AS MATERIALIZED (VALUES (+NULL) OR
```

---

## Crash 147: `bf516ae295c357a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128299`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE TABLE t2 AS VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); PRA
```

---

## Crash 148: `9962050d7d1fd96f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129538`

```sql
CREATE TEMP TABLE t1 (c3 NUMERIC NOT NULL); BEGIN EXCLUSIVE TRANSACTION; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 149: `5b2ff2ad175e2e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130336`

```sql
CREATE TEMP TABLE t1 (c3 NUMERIC NOT NULL); UPDATE OR REPLACE t1 SET c3 = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 150: `fb68d1b0b645a62f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134981`

```sql
WITH t2 AS (SELECT ALL *) SELECT DISTINCT NULL INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 151: `c5dc9c19259b5fa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136118`

```sql
WITH t3 AS (SELECT *) SELECT NULL LIMIT 15551496961209883955.49380E-579825385101298 IS TRUE OFFSET CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 152: `dd71d8bab4135db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136173`

```sql
WITH t3 AS (SELECT *) SELECT NULL LIMIT NULL IS TRUE OFFSET CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 153: `b8c701d407182e5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143398`

```sql
CREATE TABLE t3 AS VALUES (FALSE GLOB CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_);
```

---

## Crash 154: `410b03d79ac32c50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150185`

```sql
CREATE TABLE t3 (c1 DATE COLLATE NOCASE, UNIQUE (c1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 155: `5d554da62b462407` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150943`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT DISTINCT * FROM t1 NOT INDEXED WHERE FALSE IS NOT FALSE GROUP BY CURRENT_TIMESTAMP ORDER BY TRUE DESC; CREATE VIRTUAL 
```

---

## Crash 156: `8f9b19a9fce61d62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150997`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_DATE)) VALUES (TRUE) UNION SELECT DISTINCT * FROM t1 NOT INDEXED WHERE NULL GROUP BY CURRENT_TIMESTAMP ORDER BY TRUE DESC; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 157: `7199d3f073e33f32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155738`

```sql
SELECT DISTINCT last_insert_rowid() AS hn_4__xt_m_n__j__3_663v_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 158: `dc2d89f36ebc4e5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156247`

```sql
SELECT DISTINCT random() AS hn_4__xt_m_n__j__3_663v_; BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 159: `d1c818852f66fc33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156330`

```sql
DROP VIEW IF EXISTS v1; BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 160: `a88d486f52d7965e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156900`

```sql
VALUES (CURRENT_TIMESTAMP OR FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); CREATE INDEX idx1 ON t1 (c2) WHERE NOT ~CASE WHEN upper(CURRENT_TIME COLLATE RTRIM) / CAST(
```

---

## Crash 161: `c56dfaf4ff7f4e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158464`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 NUMERIC PRIMARY KEY ASC) WITHOUT ROWID; CREATE TABLE IF NOT EXISTS t1 (c2 REAL REFERENCES t3 (rowid) ON DELETE NO ACTION, c2 DATE PRIMARY KEY) WITHOUT ROWID; CREATE V
```

---

## Crash 162: `4e5e444c60ebd5d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164636`

```sql
WITH RECURSIVE t3 AS (VALUES (CURRENT_DATE)), t1 AS (SELECT DISTINCT *), t2 AS (SELECT DISTINCT *) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BIN
```

---

## Crash 163: `863cac0468b400cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164662`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (changes() OVER (PARTITION BY CURRENT_TIME ORDER BY FALSE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS))) VALUES (TRUE) UNIO
```

---

## Crash 164: `febb41c9663ab027` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164685`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_TIME)) VALUES (TRUE) UNION SELECT CURRENT_DATE AND 0 FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS LAST; BEGIN TRANS
```

---

## Crash 165: `7afe69d9704d11ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164692`

```sql
WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_TIME)) VALUES (TRUE) UNION SELECT * FROM t1 NATURAL LEFT JOIN t1 NOT INDEXED GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE COLLATE BINARY NULLS L
```

---

## Crash 166: `4a897df9e000b652` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000085914`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 REAL CHECK (EXISTS (WITH RECURSIVE t1 (_rowid_) AS (VALUES (CURRENT_TIME)) VALUES (TRUE) UNION SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY FALSE C
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  sqlite3ExprDeleteNN
  sqlite3ExprDelete
```

---
