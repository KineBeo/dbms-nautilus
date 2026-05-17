# Crash Triage Report

**Total crashes:** 131  
**Unique crash sites:** 131  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 131 | 131 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `8610b23c47e94d66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000092`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c3); BEGIN EXCLUSIVE TRANSACTION; INSERT INTO t1 VALUES (CASE NOT EXISTS (SELECT DISTINCT *, NULL AS a LIMIT CURRENT_DATE OFFSET 
```

---

## Crash 2: `c81b6bf25a0e6534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001106`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ALTER TABLE t3 DROP COLUMN c2; REINDEX t3;
```

---

## Crash 3: `b119b1d2d88addf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001268`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH t1 (c2, c2) AS NOT MATERIALIZED (SELECT ALL NULL MATCH CURRENT_TIME ISNULL, +CURRENT_TIMESTAMP / CURRENT_DAT
```

---

## Crash 4: `46c1d7dfecb4ec18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002596`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 5: `2011410e2da5b574` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002602`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 6: `805364a97624c6cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002616`

```sql
REINDEX; PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 7: `802216705b25ad78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002622`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 8: `36d8ae4c2ae71fde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004608`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 9: `7524727654e06081` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004662`

```sql
VACUUM; BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DROP TABLE t3; ALTER TABLE t3 RENAME TO t3;
```

---

## Crash 10: `5e48e826fa5d49e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005101`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); WITH t2 AS (SELECT ALL CURRENT_TIMESTAMP) UPDATE t1 SET c3 = count(*) WHERE CURRENT_TIMESTAMP; CREATE
```

---

## Crash 11: `e4c1cf1ab3886e32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008684`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c1); ANALYZE;
```

---

## Crash 12: `5c0e2340e176c25b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009087`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 13: `20ed1d7256aa7e5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010110`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); ALTER TABLE t2 DROP COLUMN rowid;
```

---

## Crash 14: `c4c92e99df1bbca5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011017`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); PRAGMA quick_check;
```

---

## Crash 15: `f3174c38a3f90ffd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011193`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 16: `df1d51248f4409fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012902`

```sql
VACUUM; PRAGMA wal_checkpoint(RESTART); ATTACH ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 17: `f15c0c2e7e693beb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016548`

```sql
CREATE TABLE t3 (c2 DATE PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); PRAGMA cache_size=-0;
```

---

## Crash 18: `26413d962a87e9f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018242`

```sql
PRAGMA cache_size=-0; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 (c1, rowid) VALUES (CASE WHEN CASE WHEN TRUE & RAISE(IGNORE) COLLATE NOCASE NOT BETWEEN TRUE ISNU
```

---

## Crash 19: `ea09020d76779e2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018284`

```sql
PRAGMA quick_check; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 (c1, rowid) VALUES (CASE WHEN CASE WHEN TRUE & RAISE(IGNORE) COLLATE NOCASE NOT BETWEEN TRUE ISNULL
```

---

## Crash 20: `4b5aa268805c4dbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019149`

```sql
VACUUM; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t3 AS MATERIALIZED (WITH t3 AS (SELECT ALL t1.*) SELECT * FROM t3 NOT INDEXED GROUP BY TRUE UNION SELECT t3.*, 
```

---

## Crash 21: `329b9cfca549e8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020328`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 22: `b0784db51d1b8151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023612`

```sql
CREATE TABLE t2 (c2 NUMERIC PRIMARY KEY DESC); BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REINDEX t1;
```

---

## Crash 23: `ce387648808a41cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025550`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 INNER JOIN t1 NOT INDEXED CROSS JOIN t3 WHERE RAISE(IGNORE) NOT IN (CURRENT_TIME) GROUP BY NULL HAVING FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 24: `3a274393240f4b8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026108`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 BLOB NOT NULL REFERENCES t2 (rowid) ON DELETE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 25: `032cf75d23d21ed6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027028`

```sql
CREATE TEMP TABLE t2 (c2 INTEGER COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 26: `80e81cafcd633023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027035`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ BLOB PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 27: `d325f197778b9b79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030052`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ TEXT PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, _rowid_);
```

---

## Crash 28: `2a8045be2653ca09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030254`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL * ORDER BY TRUE DESC, TRUE ASC LIMIT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1);
```

---

## Crash 29: `753464c0b5f191f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031001`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c3, c1); ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 30: `3538083fa22bd31d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036449`

```sql
CREATE TABLE t3 (c1 FLOAT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN; UPDATE t1 SET c3 = NOT CURRENT_DATE NOT LIKE CURRENT_DATE NOT BETWEEN CURRENT
```

---

## Crash 31: `11f73a864ad2752e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039712`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 NUMERIC UNIQUE, c3 TEXT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 32: `b043664650d18a4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043050`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE t1 AS VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 33: `a254711bce9a29d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043152`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 34: `9e7faf4256dfa8fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043481`

```sql
CREATE TABLE t3 (_rowid_ REAL COLLATE NOCASE, PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 35: `67b2c9e8c81d0332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044138`

```sql
PRAGMA cache_size=+0; CREATE VIEW IF NOT EXISTS v1 (c3, c1) AS WITH RECURSIVE t1 AS (VALUES (FALSE COLLATE NOCASE) EXCEPT SELECT t3.* ORDER BY CURRENT_TIME COLLATE RTRIM ASC LIMIT RAISE(IGNORE) COLLAT
```

---

## Crash 36: `e21043ff15087063` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044378`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 37: `5e24aa14a5f7f6cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045265`

```sql
CREATE TABLE t3 (c2 INTEGER PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 38: `3f6e018080936ce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045994`

```sql
CREATE TABLE t3 (_rowid_ FLOAT NOT NULL DEFAULT NULL, PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 39: `396a95c90b8baad8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046760`

```sql
CREATE TABLE t3 (c2 VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); ALTER TABLE t2 DROP COLUMN c1; PRAGMA synchronous=NORMAL;
```

---

## Crash 40: `9661d5a5355d0219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054975`

```sql
CREATE TABLE t3 AS SELECT ALL NULL NOT IN (-CURRENT_DATE) AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 41: `6484efcc50a02ea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055387`

```sql
CREATE TABLE t3 AS SELECT ALL total_changes() AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c1);
```

---

## Crash 42: `3f14bf5b41eaba94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055471`

```sql
CREATE TABLE t3 AS SELECT ALL TRUE AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c1);
```

---

## Crash 43: `be9feee827f8cee1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055580`

```sql
CREATE TABLE t3 AS SELECT ALL ~random() AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 44: `8907c1c09eac1000` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055634`

```sql
CREATE TABLE t3 AS SELECT ALL CURRENT_TIMESTAMP AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 45: `c1a2244e1a8ed065` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055640`

```sql
CREATE TABLE t3 AS SELECT ALL ~CURRENT_TIME AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 46: `e3e0215e7b07df9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057089`

```sql
CREATE TABLE t1 (c2 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS t1 (c1 INTEGER DEFAULT CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE 
```

---

## Crash 47: `46c231cdc15dee72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057223`

```sql
CREATE TABLE t1 (c2 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS t1 (_rowid_ INT PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF N
```

---

## Crash 48: `bee5fddf6351273f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058911`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); UPDATE OR ABORT t1 SET _rowid_ = CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 49: `be015f4374446a3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059099`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); UPDATE OR ABORT t1 SET rowid = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 50: `47373fa08e0ad635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059159`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 51: `74c9e4cdf027217d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059492`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); REINDEX t1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 52: `c558870e028e074e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059609`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 53: `638557a6ae2f6700` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060626`

```sql
CREATE TABLE t3 (c2 FLOAT CHECK (RAISE(IGNORE))); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 54: `d04c9d6c9f4c1e93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060663`

```sql
CREATE TABLE t3 (c2 INTEGER UNIQUE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 55: `45fae2782dff0e22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060669`

```sql
CREATE TABLE t3 (c2 NUMERIC NOT NULL); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 56: `b5449a475336fcdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061590`

```sql
VALUES (CURRENT_DATE) UNION VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 57: `9390ef518e3db7c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061932`

```sql
VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 58: `d71785515d5118fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062991`

```sql
VALUES (TRUE || CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 59: `7e5ca324284fc6fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065677`

```sql
VALUES (FALSE IS NOT NULL - CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 60: `9eb0ef5ca6df30a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068012`

```sql
VALUES (CAST(CURRENT_TIME AS TEXT), CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX t1; END; ATTACH ':memory:' AS db2; ANALYZE
```

---

## Crash 61: `9bba7bb2be7ed3d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068194`

```sql
VALUES (CURRENT_DATE, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 62: `e3a34644cacac872` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069196`

```sql
VALUES (CURRENT_DATE) EXCEPT VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 63: `1d65150388b2b03b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078098`

```sql
BEGIN IMMEDIATE; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1);
```

---

## Crash 64: `f6ec8038876d1f44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079460`

```sql
BEGIN DEFERRED TRANSACTION; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 65: `3e8f2b29c67c344a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079773`

```sql
BEGIN DEFERRED TRANSACTION; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 66: `ccb9f843587ce85b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082101`

```sql
SELECT DISTINCT FALSE AS l___npra__541_b4x94mjo_62____iy_18epxp1xf0_7z___y_889_g__x_w82__; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ATTACH ':memory:' AS db2; CREATE TABLE t1 (c1 DATE 
```

---

## Crash 67: `6deae78a702a31aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082467`

```sql
PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c3, _rowid_); VACUUM INTO ':memory:';
```

---

## Crash 68: `c3140f9a52d78f2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083618`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 69: `dcfe828e23a68da4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083624`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 70: `b552712bd756d26b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097703`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 71: `14fe5aa3fc880cc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098710`

```sql
CREATE VIEW v1 (rowid) AS VALUES (TRUE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 72: `20a6d6138324a857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098771`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL *; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 73: `d58da15970f1b56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099635`

```sql
CREATE TABLE t3 (rowid NUMERIC NOT NULL DEFAULT CURRENT_TIME, c3 TEXT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE I
```

---

## Crash 74: `0f933f214fa0ac9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099868`

```sql
CREATE TABLE t3 (c1 FLOAT PRIMARY KEY ASC) WITHOUT ROWID; CREATE TRIGGER trg1 BEFORE UPDATE ON t3 BEGIN DELETE FROM t3; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 75: `4b5c5d8108353326` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102271`

```sql
WITH t1 (c3) AS (SELECT ALL *) VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 76: `bb8123fbf2fe1122` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105496`

```sql
VALUES (CURRENT_DATE, CURRENT_TIME - CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 77: `201464ae960cde6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106773`

```sql
VALUES (random(), CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 78: `e5c1be41b29460db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107382`

```sql
VALUES (CURRENT_TIME - FALSE, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DETACH db2;
```

---

## Crash 79: `a6fb0741a48f58c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108002`

```sql
VALUES (CURRENT_DATE << FALSE - CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 80: `fcadec0e3a8f0478` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108710`

```sql
VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (min(CURRENT_DATE) FILTER (WHERE NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 81: `6decd6ad5ec03543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108811`

```sql
VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (count(*) FILTER (WHERE NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 82: `6ecc413c682e19a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110135`

```sql
VALUES (TRUE, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, ~NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 83: `7728dd1eb95e3757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111157`

```sql
VALUES (-4); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 84: `44d748945c0fc2f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111587`

```sql
VALUES (NULL IS CURRENT_TIME NOT BETWEEN CAST(FALSE AS VARCHAR(255)) AND FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3);
```

---

## Crash 85: `2f68072bd09aeb1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111885`

```sql
VALUES (TRUE || NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 86: `347dcd178242129f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112165`

```sql
VALUES (TRUE || sum(CURRENT_DATE)); VACUUM INTO ':memory:'; BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_, c3, _rowid_); END TRANSACTION;
```

---

## Crash 87: `b9a5870975965ca2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112228`

```sql
VALUES (TRUE || count(*)); VACUUM INTO ':memory:'; BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_, c3, _rowid_); END TRANSACTION;
```

---

## Crash 88: `4a851633b9bf745d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112416`

```sql
VALUES (TRUE || sum('iH')); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 89: `61acb32c9ecf90c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112981`

```sql
VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1);
```

---

## Crash 90: `a05ec1def37549d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115457`

```sql
CREATE TABLE t3 (c2 FLOAT CHECK (TRUE COLLATE BINARY)); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 91: `50cbaa799ef41210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116212`

```sql
CREATE TABLE t3 (c2 DATE PRIMARY KEY); ALTER TABLE t3 ADD COLUMN _rowid_ INTEGER COLLATE NOCASE; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); ATTACH ':me
```

---

## Crash 92: `99f724ac3e5c4f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117096`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); VACUUM; PRAGMA cache_size=0; WITH RECURSIVE t1 AS (VAL
```

---

## Crash 93: `38be3bcd5b8fc79c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118162`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ FLOAT PRIMARY KEY ASC); UPDATE OR ABORT t1 SET _rowid_ = CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 94: `0683f42ff3e70a37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120044`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); CREATE UNIQUE INDEX idx1 ON t1 (rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTU
```

---

## Crash 95: `0c42770a2e56a216` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120190`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INTEGER PRIMARY KEY AUTOINCREMENT); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 96: `d1e98b5701fee051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123615`

```sql
CREATE TABLE t3 (c2 DATE, _rowid_ FLOAT NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS t3 (_rowid_ INT NOT NULL) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1
```

---

## Crash 97: `8a8458405cd62583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124159`

```sql
CREATE TEMP TABLE t1 (rowid TEXT UNIQUE, c2 BLOB UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 98: `a921a75bc509839c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125047`

```sql
CREATE TABLE t3 AS SELECT ALL CAST(FALSE AS INTEGER) AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 99: `d1dd088605abc510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126633`

```sql
CREATE TABLE t3 AS SELECT ALL -CURRENT_DATE LIKE NULL AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO t1 VALUES (-NOT TRUE MATCH 4900.02716 NOTNULL NOT IN (NOT 
```

---

## Crash 100: `98bb0922681db577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126819`

```sql
CREATE TABLE t3 AS SELECT ALL count(*) FILTER (WHERE NULL) OVER (ORDER BY CURRENT_TIMESTAMP DESC GROUPS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS a; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 101: `bfba4fdb7219d8dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129989`

```sql
SELECT * FROM (VALUES (TRUE) INTERSECT VALUES (FALSE)) AS jwg_z__506 INTERSECT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE INDEX idx1 ON t2 (_rowid_, _rowid_);
```

---

## Crash 102: `d99f562bc8ab8bbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139575`

```sql
BEGIN IMMEDIATE TRANSACTION; PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 103: `a55bdb0d84be787a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141867`

```sql
CREATE TABLE t3 (_rowid_ INTEGER COLLATE NOCASE, PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 104: `c38c89731b8135ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143427`

```sql
SELECT ALL count(*) OVER (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1, _rowid_);
```

---

## Crash 105: `2b30081a963eb744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143808`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 WHERE ~NULL UNION ALL SELECT t3.* FROM t3 NOT INDEXED CROSS JOIN t2 GROUP BY FALSE, (RAISE(IGNORE) != CAST(CURRENT_TIMESTAMP AS VARCHAR(255)), CURRENT_
```

---

## Crash 106: `cbc48a86363c61bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144068`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 107: `871fb8ab900eafbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146060`

```sql
SELECT DISTINCT TRUE << CURRENT_TIME AS l___npra__541_b4x94mjo_62____iy_18epxp1xf0_7z___y_889_g__x_w82__ ORDER BY CURRENT_DATE NULLS FIRST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING r
```

---

## Crash 108: `94e2614dca1b45c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146069`

```sql
BEGIN TRANSACTION; VALUES (NULL) UNION SELECT DISTINCT NULL AS l___npra__541_b4x94mjo_62____iy_18epxp1xf0_7z___y_889_g__x_w82__ ORDER BY NULL DESC NULLS FIRST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 109: `29f8fdada7bcb749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146078`

```sql
BEGIN TRANSACTION; VALUES (TRUE, CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE, ~66.0e+823719194283248368000373368350582887049432738523838556); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 110: `695c48ff02a9a85a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146098`

```sql
VALUES (CURRENT_DATE) EXCEPT VALUES (CAST(FALSE AS INTEGER) NOT IN (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 111: `76afba8a5e7109b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146113`

```sql
BEGIN TRANSACTION; VALUES (CURRENT_TIME - CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) EXCEPT VALUES (CAST(TRUE AS BLOB), FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 112: `72e7d9b694ec267e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146129`

```sql
BEGIN TRANSACTION; WITH t2 AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM t2 GROUP BY CURRENT_DATE, FALSE HAVING TRUE ORDER BY CURRENT_DATE DESC NULLS LAST, FALSE DESC NULLS LAST LIMIT CURRENT_DATE < C
```

---

## Crash 113: `a51ab18f589dc63b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146143`

```sql
BEGIN TRANSACTION; CREATE TABLE t3 AS SELECT ALL ~sum(CURRENT_DATE) AS jbp_0_y9y_x_2s32_ge_8b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 114: `f7c57a7df37cdcc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146167`

```sql
BEGIN TRANSACTION; END TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 115: `80a2c561f1733f0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146212`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 116: `977f8e12051cd01d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146794`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 INT COLLATE NOCASE); CREATE TABLE t1 AS SELECT * FROM t2 GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 117: `8df397d19323c133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151127`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 GROUP BY last_insert_rowid() FILTER (WHERE CURRENT_DATE) MATCH FALSE, CURRENT_DATE WINDOW w1 AS (PARTITION BY CURRENT_TIMESTAMP NOT NULL), w2 AS (
```

---

## Crash 118: `ee1e14f2e42de2a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152157`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ INTEGER); CREATE TRIGGER trg1 AFTER INSERT ON t2 FOR EACH ROW WHEN NULL BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_row
```

---

## Crash 119: `6869b1fa85f1f9b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152376`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 BLOB REFERENCES t2 (c1) ON UPDATE SET NULL, c3 TEXT DEFAULT (TRUE), _rowid_ FLOAT NOT NULL DEFAULT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_r
```

---

## Crash 120: `8ff2d729b065f5d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152453`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 BLOB REFERENCES t2 (c1) ON UPDATE SET NULL, rowid INTEGER PRIMARY KEY AUTOINCREMENT); UPDATE OR FAIL t2 SET c1 = CURRENT_DATE / CURRENT_TIMESTAMP ISNULL; CREATE 
```

---

## Crash 121: `cd63831bbf7e5634` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152577`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 BLOB REFERENCES t2 (c1) ON UPDATE SET NULL, rowid INTEGER PRIMARY KEY AUTOINCREMENT); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y
```

---

## Crash 122: `8bc44f696d40e32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153154`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 BLOB REFERENCES t2 (c1) ON UPDATE SET NULL, rowid INTEGER PRIMARY KEY AUTOINCREMENT); ALTER TABLE t2 RENAME COLUMN c1 TO c1; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 123: `05db0ea691351727` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153234`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT, c1 INTEGER PRIMARY KEY AUTOINCREMENT); ALTER TABLE t2 RENAME COLUMN c1 TO c1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y
```

---

## Crash 124: `a4fd32eac807bde0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153331`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT, c1 INTEGER PRIMARY KEY AUTOINCREMENT); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE
```

---

## Crash 125: `c50bf0c57d7d38fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156643`

```sql
CREATE TABLE t1 (rowid NUMERIC PRIMARY KEY, c1 VARCHAR(255) UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL) UNION SELECT 
```

---

## Crash 126: `f111d7eab6ced4fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160576`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL *; PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 127: `05120043ed61a2b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160884`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 128: `00139e783ed8521d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164842`

```sql
SELECT DISTINCT CURRENT_DATE COLLATE NOCASE ORDER BY FALSE ASC LIMIT CURRENT_TIMESTAMP, FALSE AND FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 129: `057c685c2f7e5bcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170521`

```sql
SELECT DISTINCT NULL AS o_8_17 ORDER BY FALSE ASC LIMIT TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 130: `3a276c620eeea99a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170614`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 131: `be26b7243ba33487` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172392`

```sql
CREATE TABLE t1 (rowid INT PRIMARY KEY DESC, _rowid_ DATE) WITHOUT ROWID; CREATE INDEX idx1 ON t1 (_rowid_, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---
