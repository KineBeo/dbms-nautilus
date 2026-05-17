# Crash Triage Report

**Total crashes:** 85  
**Unique crash sites:** 85  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 84 | 84 | 98% |
| Signal | 1 | 1 | 1% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `ca516c9bb86230ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000126`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); DETACH DATABASE db2;
```

---

## Crash 2: `b7c377b8548e6c34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000428`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_, c3);
```

---

## Crash 3: `bfbb6f6904e3b031` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000814`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TRIGGER trg1 AFTER UPDATE OF c2 ON t1 BEGIN INSERT INTO t1 VALUES(CASE nullif(TRUE << CURRENT_DATE != TRUE, CURREN
```

---

## Crash 4: `0134be6a657be0f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005069`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c1, _rowid_, c3, c1);
```

---

## Crash 5: `2baed5676b032cea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005523`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 6: `49c9f89bb073a6ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008763`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 7: `a078ff8e003a437f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009028`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 8: `0e0690200b214f57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009037`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 9: `92e5f2dc77474581` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009046`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 10: `5172492f9d20922e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009224`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 11: `4d55e81178d0d8e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009666`

```sql
ANALYZE; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 12: `099b01db4a2724f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010101`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ DATE NOT NULL, rowid INT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 13: `c678e426deb108a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010560`

```sql
CREATE VIEW v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `52ef7f443a4d129c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010907`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 15: `e0960172dbf24b52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010975`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 16: `6f54829f740297ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013622`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 17: `bb9953f6295f1b5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013718`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 18: `3ff16de0a2c1f80b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014766`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 19: `541cfd9a40404bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015242`

```sql
DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3, _rowid_);
```

---

## Crash 20: `b1eb6f8bf79bf9db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015581`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 21: `cb9a1a3b49394410` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017281`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 22: `fc04e738cfccf003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020476`

```sql
CREATE TABLE t3 (_rowid_ INT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, c2, _rowid_, c2, c3); REINDEX t2; PRAGMA synchronous=OFF;
```

---

## Crash 23: `e394a3ac715ca26e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021866`

```sql
CREATE VIEW v1 (_rowid_) AS SELECT DISTINCT t1.*; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DETACH db2; ROLLBACK TRANSACTION; CREATE TEMP TABLE t2 (rowid
```

---

## Crash 24: `73e5cb52b5029084` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022907`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); REINDEX;
```

---

## Crash 25: `6d2d6ce069ec6eb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023274`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 26: `4f249dc7b1186d57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027658`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 FLOAT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 27: `6b3156b306bca2b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028173`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM t1 CROSS JOIN t3 USING (rowid) ORDER BY EXISTS (SELECT ALL *) DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 28: `714673548ac176cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028256`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL * ORDER BY FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 29: `f3742aa5b03dc873` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028262`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL * ORDER BY NULL NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 30: `7b37b8e357498308` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028268`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL * ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 31: `5ec697290b035796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029448`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); DELETE FROM t1 WHERE +-RAISE(IGNORE) ORDER BY (FALSE >> NULL NOT IN (TRUE), CASE WHEN zeroblob(RAISE(IGNORE)) OVER (PARTI
```

---

## Crash 32: `9d2b4a67ba007425` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029625`

```sql
BEGIN EXCLUSIVE; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 33: `4696c98d1c10cf26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030411`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 34: `98358e3d5882fee2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031961`

```sql
ATTACH DATABASE ':memory:' AS db2; PRAGMA foreign_keys=OFF; CREATE TEMP VIEW v1 AS SELECT RAISE(IGNORE) AS t_w_u__0g_5x5_p_____7_9jg___c9m_36yr_w0_7j_24q5il2_ FROM t3 INDEXED BY c2 WHERE count(*) OVER
```

---

## Crash 35: `f9500b67a44c61bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032855`

```sql
PRAGMA cache_size=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 36: `c3dd9a35aa1b5128` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034481`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ATTACH ':memory:' AS db2;
```

---

## Crash 37: `94060f702dce6986` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035454`

```sql
BEGIN EXCLUSIVE; PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); ANALYZE t2;
```

---

## Crash 38: `7c60f6887b7aa667` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035477`

```sql
BEGIN EXCLUSIVE; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); ANALYZE t2;
```

---

## Crash 39: `d000dfe8ac0545f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035483`

```sql
BEGIN EXCLUSIVE; PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); ANALYZE t2;
```

---

## Crash 40: `e9eb472b04a332a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039263`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT DEFAULT CURRENT_DATE); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 41: `e351bb4dc6d823f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039317`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ REAL PRIMARY KEY DESC); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 42: `b38674bdbd5f1610` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039324`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT DEFAULT CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 43: `9967ff1593f4b7fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040864`

```sql
CREATE TABLE t1 (c2 INTEGER COLLATE NOCASE, UNIQUE (c2), CHECK (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 44: `7c80e0e6ca4aaf55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048626`

```sql
BEGIN; CREATE TABLE t2 AS VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 45: `72e06f774a081ead` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050996`

```sql
CREATE TABLE t1 (c2 INTEGER NOT NULL DEFAULT CURRENT_DATE, UNIQUE (c2), UNIQUE (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 46: `38d46b37c98a1671` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051431`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 NUMERIC PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 47: `807b1a5297ddc8a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051790`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TABLE t3 (_rowid_ NUMERIC PRIMARY KEY ASC, PRIMARY KEY (c3), FO
```

---

## Crash 48: `a6ba3ae375b793e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052180`

```sql
BEGIN DEFERRED; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t1 AS MATERIALIZED (SELECT * ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME) DELETE FROM t
```

---

## Crash 49: `8ca7a257b6d8de40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058219`

```sql
CREATE TABLE t3 (rowid BOOLEAN UNIQUE, c1 TEXT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 50: `08ea9a76dd7f794d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061975`

```sql
SELECT ALL count(*) OVER (ORDER BY NULL ASC ROWS CURRENT ROW); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 51: `bbced461fa285c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063183`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 NUMERIC PRIMARY KEY ASC); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); UPDATE OR FAIL t3 SET _rowid_ = t3.c2; DELETE FROM t3 
```

---

## Crash 52: `7cb77bf6168bce92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068973`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid INT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ALTER TABLE t3 RENAME COLUMN rowid TO c2;
```

---

## Crash 53: `b0cbab203e9366ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072255`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ FLOAT PRIMARY KEY ASC) WITHOUT ROWID; CREATE TABLE IF NOT EXISTS t2 (_rowid_ FLOAT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 54: `a5aba383beb927e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073023`

```sql
PRAGMA wal_checkpoint(RESTART); BEGIN TRANSACTION; PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 55: `0521862743f75439` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082739`

```sql
VALUES (NULL | NULL); PRAGMA synchronous=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ANALYZE t2; BEGIN IMMEDIATE TRANSACTION; COMMIT;
```

---

## Crash 56: `71515d38531ee542` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087581`

```sql
VALUES ((VALUES (FALSE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 57: `fceb6609f9a07110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090421`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 58: `0c7554e3fcd662e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090716`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DROP TABLE t2; BEGIN IMMEDIATE;
```

---

## Crash 59: `5aecca81b268065b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091751`

```sql
PRAGMA analysis_limit=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 60: `7d77a5fec56f943d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099369`

```sql
VALUES (-17482434666756857416628248424610543148638734605326968731455548718016942279154182958151304539914846806667585418071292990047957332807089070182642563275024860147000313739757054910483846105988979
```

---

## Crash 61: `2935baa9f39aaacb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099432`

```sql
VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 62: `7858f79181d5551a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101430`

```sql
WITH t1 AS (VALUES (NULL)) SELECT * FROM t1 AS hh_8w__78myw_8____9jzub_69_0__665bu1_zp1___42 INNER JOIN t1 NOT INDEXED GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY TRUE ASC LIMIT TRUE; CREATE V
```

---

## Crash 63: `74ac2bfb79871a20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104832`

```sql
WITH t1 AS (VALUES (NULL)) SELECT count(*) OVER (ORDER BY NULL ASC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) FROM t1 GROUP BY FALSE, CURRENT_DATE HAVING TRUE WINDOW w1 AS () ORDER BY 
```

---

## Crash 64: `f382180b63cb309e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106335`

```sql
WITH t1 AS (VALUES (NULL)) SELECT * FROM t1 GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY CURRENT_TIMESTAMP ASC LIMIT ~FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 65: `b3a1114eb1e01b51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107453`

```sql
VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); PRAGMA analysis_limit=+-31; ATTACH ':memory:' AS db2;
```

---

## Crash 66: `ceb3899ce17d5e91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107495`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); PRAGMA analysis_limit=+-31; ATTACH ':memory:' AS db2;
```

---

## Crash 67: `f7964c03cad2ed8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108768`

```sql
WITH t1 AS (VALUES (NULL)) SELECT * FROM t1 GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY NULL NULLS LAST LIMIT (SELECT DISTINCT * FROM (VALUES (FALSE)) AS a_617ei__u0c608441m8h3eg902bq WHERE CU
```

---

## Crash 68: `1fe75fb4cc501edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111854`

```sql
ANALYZE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 69: `0d085f8177c95cd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114009`

```sql
CREATE TABLE t2 (c1 INTEGER NOT NULL DEFAULT TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c1); ROLLBACK; UPDATE OR REPLACE t1 SET c3 = NOT EXISTS (SELECT * FROM t1 NOT INDEX
```

---

## Crash 70: `2e9c1c7ce7317559` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114751`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ DATE NOT NULL, rowid INT PRIMARY KEY) WITHOUT ROWID; CREATE INDEX idx1 ON t2 (_rowid_, rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 71: `1ebfc9779116f525` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116555`

```sql
CREATE TABLE t2 (c3 INT CHECK (c3)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 72: `3adf46d2fc8832ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118788`

```sql
CREATE VIEW v1 AS SELECT count(*) OVER (ORDER BY NULL ASC ROWS BETWEEN CURRENT ROW AND CURRENT_TIME FOLLOWING), *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW v1 (c2, c3) AS 
```

---

## Crash 73: `5af1cfc0ff022633` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120263`

```sql
PRAGMA analysis_limit=-2677; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 74: `ab273d8f7a8121fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125533`

```sql
CREATE TEMP TABLE t3 (rowid BLOB PRIMARY KEY); CREATE TRIGGER trg1 AFTER UPDATE OF c1 ON t3 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 75: `dfe6eece425b838e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126252`

```sql
SELECT ALL count(*) OVER (ORDER BY NULL ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 76: `01a9543e6dab0622` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126447`

```sql
SELECT ALL count(*) OVER (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 77: `53e69ed5aa80f503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128558`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ FLOAT PRIMARY KEY ASC) WITHOUT ROWID; INSERT INTO t2 VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 78: `ebce3b99fd8bee61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129686`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ VARCHAR(255) DEFAULT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); PRAGMA synchronous=OFF;
```

---

## Crash 79: `9219015e77fdc3da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129954`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); REINDEX;
```

---

## Crash 80: `45ece3a5e612f196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146333`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1);
```

---

## Crash 81: `7af61e0a1f4a4581` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146438`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 82: `4ed700c02530d361` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146510`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 83: `199b8043d21eda39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146766`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid TEXT PRIMARY KEY DESC, c3 INT UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 84: `384f4cdb2daf725b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147528`

```sql
CREATE TABLE t1 (c2 INTEGER NOT NULL DEFAULT CURRENT_DATE, UNIQUE (c2) ON CONFLICT ROLLBACK, UNIQUE (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK TO sp1;
```

---

## Crash 85: `8bc28dd6c969fd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033513`

```sql
CREATE TABLE t1 AS SELECT DISTINCT CURRENT_TIMESTAMP UNION SELECT count(*) OVER (ORDER BY NULL ASC ROWS BETWEEN CURRENT ROW AND TRUE FOLLOWING) FROM t1 GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER
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
