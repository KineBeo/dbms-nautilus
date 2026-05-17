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

## Crash 1: `c7b87f92df634ad7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000270`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); REPLACE INTO t2 VALUES (CURRENT_DATE, ifnull(NOT TRUE ISNULL NOT NULL -> CURRENT_DATE NOT LIKE CURRENT_
```

---

## Crash 2: `1b7ea462a88f0631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000453`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); BEGIN DEFERRED;
```

---

## Crash 3: `38943c0036a3388a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001058`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); VACUUM INTO ':memory:'; DELETE FROM t2 RETURNING CASE TRUE << RAISE(IGNORE) LIKE CURRENT_TIMESTAMP COLLATE RTRIM WHEN _r
```

---

## Crash 4: `e54bd4691f937229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001128`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1); VACUUM INTO ':memory:';
```

---

## Crash 5: `99a692c137c3cb6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004731`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1);
```

---

## Crash 6: `d4641d9de21504ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009341`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, c2);
```

---

## Crash 7: `d5a57f8680b4a2e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009496`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); DROP TABLE t3; ANALYZE t1;
```

---

## Crash 8: `44135f462fb23c3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011933`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, c2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id,
```

---

## Crash 9: `f31c7ebe12cefc04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012543`

```sql
BEGIN DEFERRED TRANSACTION; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE TRIGGER trg1 AFTER INSERT ON t1 BEGIN UPDATE t3 SET rowid = +NOT NOT TRUE - CASE 
```

---

## Crash 10: `84cec3f58de85c88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012800`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM INTO ':memory:';
```

---

## Crash 11: `340b6d2501168a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014037`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 12: `091557a6badbff61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014421`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 13: `c52a282f30be7118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020262`

```sql
DROP TRIGGER IF EXISTS trg1; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 14: `a816e0682cc7518e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020695`

```sql
BEGIN DEFERRED TRANSACTION; ROLLBACK TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 15: `9fcb810f94a11d48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021491`

```sql
CREATE TABLE t3 (c2 NUMERIC PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT OR REPLACE INTO t1 VALUES (-FALSE REGEXP CURRENT_TIMESTAMP ->> +CURRENT_TIMESTAMP NOT
```

---

## Crash 16: `094c2a4ba7a1983a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022042`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 17: `89387c2ae0f59818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022115`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 18: `9334ceb5041b95f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023252`

```sql
ATTACH DATABASE ':memory:' AS db2; PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 19: `09fc4ffdf96199a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023286`

```sql
ATTACH DATABASE ':memory:' AS db2; PRAGMA journal_mode=MEMORY; SAVEPOINT sp1; DETACH db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); SELECT ALL CURRENT_TIMESTAMP LIMIT NULL; VACUUM 
```

---

## Crash 20: `fc26d60b91111132` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023721`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 21: `916f9f6519957a6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026431`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 22: `9956e98c2a3d9f81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026558`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 23: `8cf5f6bd8c6a9dfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029235`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 VARCHAR(255) UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 24: `23776373a23c54ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029621`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT t3.*; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW v1 (rowid) AS SELECT DISTINCT ~RAISE(IGNORE) COLLATE BINARY NOT LIKE TRUE IS DISTINCT
```

---

## Crash 25: `351117949e127e0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029725`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, _rowid_); DROP TABLE t2;
```

---

## Crash 26: `ea9f6f60c8cd4d24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030339`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 VARCHAR(255) NOT NULL REFERENCES t2 (c2) MATCH c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 27: `b30598bf2bd05eac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031242`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 28: `fde70bde46b307d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031251`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 VARCHAR(255) NOT NULL REFERENCES t3 (_rowid_) ON DELETE SET DEFAULT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 29: `eaf5ef0ce1da291f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032192`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE TEMP TABLE t2 (c3 BOOLEAN NOT NULL, rowid DATE NOT NULL); ANALYZE t3; SELECT (CURRENT_TIME NOT NULL) <= FALSE IN (CURR
```

---

## Crash 30: `cc594a52d264313d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033419`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 31: `0bec7dc9f7e0bbaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036492`

```sql
SELECT DISTINCT NULL | NULL AS j__suz9_h_9na_k_ha4_4id6_25; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 32: `f09f6faa61ca8239` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036598`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 33: `67ff1638d1d974ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037795`

```sql
CREATE TEMP TABLE t1 (c2 TEXT REFERENCES t3 (c2) DEFERRABLE INITIALLY DEFERRED, rowid REAL DEFAULT NULL, c3 TEXT NOT NULL); UPDATE OR FAIL t1 SET c3 = c3; ATTACH DATABASE ':memory:' AS db2; CREATE VIR
```

---

## Crash 34: `e16e1e26c31179bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037911`

```sql
CREATE TEMP TABLE t1 (c1 VARCHAR(255), c2 BOOLEAN, c3 TEXT NOT NULL); UPDATE OR ABORT t1 SET _rowid_ = CURRENT_DATE; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 35: `f18a17c82b4e8148` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037917`

```sql
CREATE TEMP TABLE t1 (c1 VARCHAR(255), c2 BOOLEAN, c3 TEXT NOT NULL); UPDATE OR FAIL t1 SET c3 = FALSE; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 36: `4d9c5714489a33d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037938`

```sql
CREATE TEMP TABLE t1 (c1 VARCHAR(255), c3 BOOLEAN PRIMARY KEY DESC); UPDATE OR FAIL t1 SET c3 = FALSE; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 37: `4753a074b1d952a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037945`

```sql
CREATE TEMP TABLE t1 (c1 VARCHAR(255), c2 BOOLEAN, c3 TEXT NOT NULL); ANALYZE; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 38: `9fe3cecf654e1668` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041404`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ BLOB PRIMARY KEY ASC, rowid REAL COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK TO sp1;
```

---

## Crash 39: `6d088aafa789ec99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046344`

```sql
VALUES (CURRENT_DATE % NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 40: `dfdb5bd7fcbf9b64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047001`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT *, * FROM t3 NOT INDEXED , t3 NOT INDEXED GROUP BY FALSE, NULL << RAISE(IGNORE) WINDOW w1 AS (ORDER BY +(CURRENT_TIMESTAMP) DESC) UNION ALL SELECT t2.* ORDER BY 
```

---

## Crash 41: `b45dad0013b3a360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049512`

```sql
VALUES (count(CURRENT_TIMESTAMP) FILTER (WHERE TRUE) OVER (PARTITION BY CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); DELETE FROM t1 WHERE CASE WHEN CASE WHEN RAIS
```

---

## Crash 42: `01abe2ebfb05e34d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049876`

```sql
SELECT 0.0 AS e66g0___n_s3_08z_3__i32_i2___8_9z_gu2__563cla4_019; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 43: `0c3caa600312221d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049962`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 44: `7041fc2b58645398` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057077`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC, c1 BLOB UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 45: `25ed2a024156003a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057216`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC, c1 BLOB UNIQUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 46: `4ba83344c61c1afb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059047`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ BLOB PRIMARY KEY ASC, rowid REAL COLLATE NOCASE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 47: `82e92f04b279d4a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061027`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 DATE PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 48: `34ffa51d2b100dce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062372`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 49: `bdf3657e180f7892` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062751`

```sql
CREATE TABLE t3 (rowid NUMERIC UNIQUE, PRIMARY KEY (rowid) ON CONFLICT ABORT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 50: `5f2d952da3501fbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063391`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 51: `6ce630c630e4390b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063981`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REINDEX;
```

---

## Crash 52: `f253b4f1182bf338` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064010`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 53: `5d09122793d31cbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064177`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA quick_check; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE
```

---

## Crash 54: `9dba4fd5ff14f378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064364`

```sql
ANALYZE; BEGIN TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REINDEX; ANALYZE; ROLLBACK TO SAVEPOINT sp1;
```

---

## Crash 55: `03c25b68b43a4fd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064373`

```sql
ANALYZE; BEGIN TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); REINDEX; ANALYZE; CREATE VIRTUAL TABLE IF N
```

---

## Crash 56: `6e1bd99b86cbed8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067134`

```sql
CREATE TABLE t1 AS SELECT ALL count(*) AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3, c1);
```

---

## Crash 57: `b6b8e7dde9667894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067270`

```sql
CREATE TABLE t1 AS VALUES (CURRENT_TIMESTAMP); ATTACH DATABASE ':memory:' AS db2; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 58: `bda75bacb63dbde1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069717`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _ro
```

---

## Crash 59: `1e858f0e07c7244f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069862`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c3);
```

---

## Crash 60: `60894933e02b112c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070150`

```sql
CREATE VIEW v1 AS SELECT * FROM t2 WHERE TRUE GROUP BY random() OVER (PARTITION BY FALSE ORDER BY RAISE(IGNORE) NULLS FIRST ROWS CURRENT_TIME PRECEDING) INTERSECT SELECT ALL * ORDER BY CURRENT_TIMESTA
```

---

## Crash 61: `fd66215c9c802927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071705`

```sql
VACUUM; PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PRAGMA wal_checkpoint(RESTART); DELETE FROM t1; ALTER TABLE t1 RENAME TO t1;
```

---

## Crash 62: `4771b47e6992421d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079480`

```sql
CREATE TABLE t2 (_rowid_ TEXT CHECK (TRUE MATCH CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 63: `7594757fad5f9b65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082802`

```sql
PRAGMA foreign_keys=1; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t3 (c3) AS (VALUES (RAISE(IGNORE)) LIMIT RAISE(IGNORE) OFFSET NULL) S
```

---

## Crash 64: `6233afe3f90fdc25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086996`

```sql
BEGIN IMMEDIATE; PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 65: `a00e1b78fb889943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095360`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TRIGGER trg1 AFTER INSERT ON t1 WHEN TRU
```

---

## Crash 66: `a661cd9108dad4be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095623`

```sql
CREATE TABLE t3 (c1 DATE UNIQUE, _rowid_ NUMERIC PRIMARY KEY ASC, UNIQUE (c1) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 67: `e1e1a7a02781b80b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100103`

```sql
CREATE TABLE t1 AS VALUES (CURRENT_TIME * CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 68: `8dc033a69b995146` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101109`

```sql
CREATE TABLE t1 AS VALUES (FALSE <= CAST(CURRENT_TIME AS VARCHAR(255)), NULL); ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 69: `37bdbcf9ba0fcc7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101892`

```sql
CREATE TABLE t1 (rowid NUMERIC PRIMARY KEY DESC) WITHOUT ROWID; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TABLE IF NOT EXISTS t3 (c2 FLOAT NOT NULL REFERENCES t1 (
```

---

## Crash 70: `ef5bd8b423705639` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102756`

```sql
CREATE TABLE t1 AS SELECT CURRENT_TIMESTAMP COLLATE RTRIM >= CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 71: `71c7fcefede94d9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103595`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); BEGIN TRANSACTION; ATTACH DATABASE ':memory:' AS db2; REINDEX; ANALYZE; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PR
```

---

## Crash 72: `bb4c537f6a079fb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105364`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT NOT NULL DEFAULT X'1a'); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 73: `63a6fc9aa88d740a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105392`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT NOT NULL DEFAULT FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 74: `169e3448c6262eae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105854`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BLOB NOT NULL DEFAULT 632); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 75: `f4cd7e11cda3e447` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105912`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 FLOAT PRIMARY KEY DESC); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 76: `231f0d8916fd5e0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106403`

```sql
CREATE TABLE t3 (rowid BLOB COLLATE NOCASE, PRIMARY KEY (rowid) ON CONFLICT ABORT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 77: `ff9f6cf4dcee5855` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106600`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 78: `74d131bd1394216a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109326`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ TEXT CHECK (CURRENT_TIMESTAMP IS NOT NULL < FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c2); ATTACH ':memory:' AS db2; WITH R
```

---

## Crash 79: `00185191d1d95c28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109946`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN NOT NULL DEFAULT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2);
```

---

## Crash 80: `c202c0b55bce5399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110121`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 TEXT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 81: `ab1a28060c6afb93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110171`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 FLOAT UNIQUE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 82: `a3b4c42cac177101` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111653`

```sql
CREATE VIEW v1 AS SELECT * FROM t3 NOT INDEXED WHERE RAISE(ROLLBACK, '-9-_Y') GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS () UNION SELECT ALL * ORDER BY NULL ASC NULLS FIRST, RAISE(IGNORE) DESC;
```

---

## Crash 83: `3813d43a8c27fe22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113892`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 INTEGER CHECK (rowid)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2);
```

---

## Crash 84: `bf5c54347375e1bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114361`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ TEXT CHECK (NULL)); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 85: `646fd9ab9ccc8f6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115321`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ REAL); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 86: `36c4061a733bd49c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115371`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 FLOAT PRIMARY KEY DESC, c1 BLOB UNIQUE); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 87: `933dbbce7c9b7961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117277`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 NUMERIC PRIMARY KEY); ATTACH ':memory:' AS db2; BEGIN IMMEDIATE TRANSACTION; INSERT INTO t2 DEFAULT VALUES; COMMIT TRANSACTION; INSERT INTO t2 DEFAULT VALUES; INSERT 
```

---

## Crash 88: `134225f7f1493181` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123539`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT NOT CURRENT_TIMESTAMP AS c3t_d_7pz754__fn_6m_ FROM t3 GROUP BY TRUE, NULL WINDOW w1 AS (PARTITION BY TRUE COLLATE RTRIM, (RAISE(IGNORE))) ORDER BY +CASE WHEN CUR
```

---

## Crash 89: `bf058174ed31427a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125683`

```sql
SELECT -434625418332548993007485371330.5369646e-46712294 AS e66g0___n_s3_08z_3__i32_i2___8_9z_gu2__563cla4_019; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 90: `b2c516d23a04f1b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127518`

```sql
VALUES (CURRENT_TIME AND CURRENT_TIME); DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); BEGIN IMMEDIATE; REINDEX t1;
```

---

## Crash 91: `4144a3a24269161b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128334`

```sql
ATTACH ':memory:' AS db2; CREATE TEMP VIEW v1 AS SELECT DISTINCT X'' AS m35_ FROM t3 NOT INDEXED WHERE TRUE GROUP BY CURRENT_DATE EXCEPT SELECT DISTINCT * ORDER BY CURRENT_TIMESTAMP NULLS LAST; CREATE
```

---

## Crash 92: `0ad0629147739039` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129021`

```sql
CREATE TABLE t3 (c1 VARCHAR(255) NOT NULL DEFAULT -118486); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1);
```

---

## Crash 93: `7065a1c3c6d328be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130187`

```sql
VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 94: `1ec3df67f7b0c19b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136501`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 INTEGER PRIMARY KEY ASC); CREATE UNIQUE INDEX idx1 ON t3 (c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 95: `1f7463f322aff5ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137573`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 FLOAT PRIMARY KEY ASC); CREATE INDEX idx1 ON t3 (c2) WHERE NULL IS TRUE NOTNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN IMMEDIATE;
```

---

## Crash 96: `d157ce8656a542be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138525`

```sql
PRAGMA cache_size=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); UPDATE t1 SET c1 = CAST(-CURRENT_TIME AS NUMERIC) WHERE NOT FALSE NOTNULL NOT IN (SELECT * INTERSECT SELECT DIST
```

---

## Crash 97: `66d27f49fd34be4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139027`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 BLOB UNIQUE); UPDATE OR ABORT t3 SET rowid = NULL IS TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 98: `70145c62d24c565c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139155`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 TEXT NOT NULL, c2 TEXT PRIMARY KEY ASC); CREATE INDEX idx1 ON t3 (c2) WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ANALYZE t2; BEGIN IM
```

---

## Crash 99: `680bd6cd56e42b9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139453`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 TEXT NOT NULL DEFAULT X'6Be9D6a26FfEFC', rowid REAL COLLATE NOCASE); UPDATE OR ABORT t3 SET rowid = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 100: `5ddc8271b30c0e2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139516`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 FLOAT PRIMARY KEY, rowid REAL COLLATE NOCASE); UPDATE OR ABORT t3 SET rowid = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 101: `d2a8fee9926f6bbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139522`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 TEXT NOT NULL DEFAULT TRUE, rowid REAL COLLATE NOCASE); UPDATE OR ABORT t3 SET rowid = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 102: `51eaed792a4b3439` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141075`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT NOT NULL); UPDATE OR ABORT t3 SET c3 = (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2, _rowid_, _rowid_, c3); DROP TABLE 
```

---

## Crash 103: `4b9c3aea2a7dd9c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145187`

```sql
CREATE TABLE t2 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 104: `86a84a406e1894d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146161`

```sql
CREATE TABLE t1 (c1 VARCHAR(255) NOT NULL REFERENCES t2 (c2) DEFERRABLE INITIALLY DEFERRED, rowid VARCHAR(255) PRIMARY KEY ASC, UNIQUE (rowid, c1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 105: `b587d6be1225ac7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150876`

```sql
SELECT DISTINCT FALSE NOT BETWEEN CURRENT_DATE AND FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ALTER TABLE t1 RENAME COLUMN c3 TO c2; COMMIT TRANSACTION;
```

---

## Crash 106: `2f54f39d5847c294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151681`

```sql
VALUES (count(DISTINCT CURRENT_TIME) FILTER (WHERE FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 107: `6a0c7621b606bebb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151742`

```sql
VALUES (count(*) FILTER (WHERE FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 108: `f388d6a617174929` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152280`

```sql
VALUES (~NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c1); CREATE TABLE t3 (rowid NUMERIC NOT NULL);
```

---

## Crash 109: `f9aca62de4a883ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152657`

```sql
VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP OR CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 110: `c7cbda41293c97f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152672`

```sql
VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP OR CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3, rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, c3, _rowid
```

---

## Crash 111: `1109a3200159730d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161947`

```sql
VALUES (CURRENT_TIME + CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c2);
```

---

## Crash 112: `148e792dc9b69a9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168829`

```sql
PRAGMA journal_mode=WAL; BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---
