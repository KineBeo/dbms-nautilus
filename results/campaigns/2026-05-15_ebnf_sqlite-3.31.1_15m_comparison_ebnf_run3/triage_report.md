# Crash Triage Report

**Total crashes:** 78  
**Unique crash sites:** 78  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 78 | 78 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d987716a2db92de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REINDEX t3; ANALYZE t1; DELETE FROM t1 WHERE group_concat(-NULL IN (TRUE) MATCH (WITH t1 AS (VALUES (CURRENT_TIMESTAMP) LIMIT FALSE) VALU
```

---

## Crash 2: `661a8b4647ceddd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000923`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); ROLLBACK; DELETE FROM t2 WHERE unicode(RAISE(IGNORE) >= NULL) FILTER (WHERE FALSE) != trim(FALSE) FILTER (WHERE CURRENT_TIMESTAMP) OVER (P
```

---

## Crash 3: `ba562bac9f93fdeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000944`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION; COMMIT;
```

---

## Crash 4: `7794aab400e0fab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001141`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 5: `6a4eb4297ae97a29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002173`

```sql
CREATE TABLE t2 (_rowid_ DATE NOT NULL REFERENCES t3 (rowid) ON UPDATE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 6: `ab95bdad56f68d0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002210`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid DATE PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 7: `13f7d1a24b837247` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002401`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION; COMMIT;
```

---

## Crash 8: `224bcb6ea0e2d34e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002407`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION; COMMIT;
```

---

## Crash 9: `b29ce76480ee6356` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002413`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION; COMMIT;
```

---

## Crash 10: `421ef7ee24a96119` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005121`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 11: `52ccd3ff616565e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005219`

```sql
BEGIN TRANSACTION; PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); UPDATE t2 SET c1 = CASE WH
```

---

## Crash 12: `c886ed608c1f3520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005276`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 13: `63c4c7c3a57b2427` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008217`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid BLOB DEFAULT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `931d9911d5fbf013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013167`

```sql
PRAGMA analysis_limit=+3; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1);
```

---

## Crash 15: `0c421611e9450530` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016729`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 BLOB, rowid BLOB PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 16: `61b54447d0079d9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019006`

```sql
CREATE TABLE t3 (c1 NUMERIC GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c3 VARCHAR(255) PRIMARY KEY ASC, CHECK (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 17: `dde7cb347cedaa5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019511`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (rowid DATE PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 18: `37368c1a6801b430` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020888`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); BEGIN IMMEDIATE; SELECT CASE WHEN CURRENT_DATE THEN (CURRENT_DATE) ELSE CURRENT_DATE END, * FROM t1 GROUP BY TRUE WINDOW w1 AS ()
```

---

## Crash 19: `42c1be25bb9bafd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023900`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 20: `af487bbb35dcd185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027575`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VACUUM; COMMIT TRANSACTION;
```

---

## Crash 21: `8d2ce9cb27a71cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028083`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL REFERENCES t2 (c2) ON DELETE NO ACTION); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 22: `0a4e489a08590fa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028299`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 FLOAT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 23: `b0638c7fde453e91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031279`

```sql
PRAGMA cache_size=+78; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 24: `bf23b5b8f2ade114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032814`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 25: `2cdf136107f4d971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034062`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ANALYZE;
```

---

## Crash 26: `7d48d659edfcddcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040446`

```sql
CREATE TABLE t2 (c3 INTEGER PRIMARY KEY DESC); CREATE TRIGGER trg1 AFTER INSERT ON t2 BEGIN SELECT * FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE VIEW v1 AS VALU
```

---

## Crash 27: `da96e37d45ecc9dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057693`

```sql
CREATE TABLE t2 (c2 VARCHAR(255) COLLATE NOCASE, _rowid_ FLOAT PRIMARY KEY ASC, CHECK (NULL), UNIQUE (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3, c1, _rowid_);
```

---

## Crash 28: `bd2991d22fe2873e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058125`

```sql
CREATE TABLE t2 (c2 BOOLEAN PRIMARY KEY, CHECK (NULL), UNIQUE (c2) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 29: `690571816208818d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058560`

```sql
CREATE VIEW v1 AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 30: `f01c3a7f2873f0c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058895`

```sql
BEGIN TRANSACTION; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DETACH db2; ALTER TABLE t3 DROP COLUMN rowid; BEGIN DEFERRED TRANSACTION; ROLLBACK TRANSACTION;
```

---

## Crash 31: `1797cd2bbf22ae30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064723`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 DATE PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2); VACUUM INTO ':memory:';
```

---

## Crash 32: `6cfdbf9374e07416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065819`

```sql
ATTACH ':memory:' AS db2; DETACH db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 33: `18546460ba77b1f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076279`

```sql
PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); BEGIN DEFERRED TRANSACTION; DROP TABLE IF EXISTS t2;
```

---

## Crash 34: `fa2ea694933ef7d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076957`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 INTEGER NOT NULL); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); ANALYZE t2; ATTACH DATABASE ':memory:' AS db2; SELE
```

---

## Crash 35: `3a34602725090179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077232`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; ROLLBACK; BEGIN IMMEDIATE TRANSACTION; COMMIT; ATTACH ':memory:' AS db2; BEGIN TRANSACTION; CREATE TABLE IF NOT EXISTS t1 (c2 BOOLEAN); CREATE 
```

---

## Crash 36: `30322e30beb5faba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077714`

```sql
ANALYZE; ATTACH ':memory:' AS db2; BEGIN TRANSACTION; ROLLBACK; BEGIN TRANSACTION; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); BEGIN IMMEDIATE TRANSACTION;
```

---

## Crash 37: `783fdebf5a0de66f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077867`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; ROLLBACK; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); ATTACH DATABASE ':memory:' AS db2; DETACH db2; ATTACH DATABASE ':memory
```

---

## Crash 38: `306db5572b0fdf13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077932`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; ROLLBACK; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); ATTACH DATABASE ':memory:' AS db2; DETACH db2; ATTACH DATABASE ':memory
```

---

## Crash 39: `c78b7f8c5ae696ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078314`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 40: `f3d629072dbf0610` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079134`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK TRANSACTION;
```

---

## Crash 41: `9309b13e39ec3c27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082618`

```sql
CREATE TABLE t3 (_rowid_ INTEGER DEFAULT (TRUE), rowid INT NOT NULL DEFAULT FALSE); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN SELECT 42756819654674233863666.5101420994332514186369018307095772386897
```

---

## Crash 42: `986d5c8c406b646e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082688`

```sql
CREATE TABLE t3 (_rowid_ INTEGER DEFAULT (TRUE), c3 NUMERIC NOT NULL); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 43: `724636c7cb96bd10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082695`

```sql
CREATE TABLE t3 (_rowid_ INTEGER DEFAULT (TRUE), c3 NUMERIC NOT NULL); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 44: `e377c43104d517f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082701`

```sql
CREATE TABLE t3 (_rowid_ INTEGER DEFAULT (TRUE), c3 NUMERIC NOT NULL); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; DROP TRIGGER trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 45: `3a664492f9142d22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082749`

```sql
CREATE TABLE t3 (_rowid_ BLOB UNIQUE); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 46: `548a3f21f82062fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082759`

```sql
CREATE TABLE t3 (_rowid_ BLOB UNIQUE); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 47: `529342f8a0530700` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082903`

```sql
CREATE TABLE t1 AS VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 48: `8a99b78fbf6aea89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086625`

```sql
CREATE TABLE t1 (_rowid_ REAL PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, c2);
```

---

## Crash 49: `80ad36cfd0a0d262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086684`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_); BEGIN;
```

---

## Crash 50: `a12dc9ea30f58ebe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087233`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); REINDEX t3; ATTACH ':memory:' AS db2;
```

---

## Crash 51: `631548d7d8725dc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087292`

```sql
DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DROP TABLE t1;
```

---

## Crash 52: `0fcc99370d613335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090357`

```sql
CREATE TABLE t3 (rowid INT NOT NULL DEFAULT X'4acb5BcD3a'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 53: `a7b7561a2bbf4b8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095420`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE IF NOT EXISTS t1 (rowid BLOB PRIMARY KEY DESC); REINDEX
```

---

## Crash 54: `884da37646a376ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096142`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); ATTACH DATABASE ':memory:' AS db2; DETACH db2; CREATE TEMP TABLE IF NOT EXISTS t3
```

---

## Crash 55: `f06e21e1f17421b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096184`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); ATTACH DATABASE ':memory:' AS db2; DETACH db2; DROP INDEX IF EXISTS idx1; CREATE 
```

---

## Crash 56: `1ff291e96f0daa11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096191`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); ATTACH DATABASE ':memory:' AS db2; DETACH db2; CREATE TEMP TABLE IF NOT EXISTS t3
```

---

## Crash 57: `867d92946733a1e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096779`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; ROLLBACK; BEGIN IMMEDIATE TRANSACTION; COMMIT; PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3);
```

---

## Crash 58: `e4a8c1057ba66762` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096854`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; DETACH db2; ROLLBACK; BEGIN IMMEDIATE TRANSACTION; COMMIT; BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CR
```

---

## Crash 59: `bdfb92a2ff11af25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117123`

```sql
CREATE TABLE t3 (c3 BLOB REFERENCES t3 (c2) ON DELETE SET DEFAULT, _rowid_ TEXT PRIMARY KEY ASC, CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 60: `8d9047461769fecf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117204`

```sql
CREATE TABLE t3 (_rowid_ VARCHAR(255) NOT NULL, CHECK (RAISE(IGNORE) IS NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 61: `bcd6614c0caebe55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120256`

```sql
CREATE TABLE t3 (c3 VARCHAR(255) PRIMARY KEY ASC, CHECK (CURRENT_TIMESTAMP)); DROP TABLE IF EXISTS t3; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, _
```

---

## Crash 62: `b5d20170d1f2b2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120372`

```sql
CREATE TABLE t3 (c3 VARCHAR(255) PRIMARY KEY ASC, UNIQUE (c3) ON CONFLICT ROLLBACK); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (CASE WHEN CURRENT_TIME THEN NULL WHEN FALSE ISNUL
```

---

## Crash 63: `7ae29ea05659a544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122632`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3);
```

---

## Crash 64: `114447b629be3053` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124176`

```sql
CREATE VIEW v1 (c1, c1) AS SELECT t3.* FROM t2 WHERE FALSE GROUP BY TRUE, TRUE HAVING CURRENT_DATE INTERSECT SELECT * FROM t1 NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_,
```

---

## Crash 65: `b8a7351639a9d8c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125634`

```sql
CREATE TABLE t2 (c2 BOOLEAN PRIMARY KEY, FOREIGN KEY (c2) REFERENCES t3 (_rowid_) ON DELETE RESTRICT, CHECK (CURRENT_TIME)); CREATE TABLE t3 (c3 BOOLEAN UNIQUE); ATTACH ':memory:' AS db2; CREATE VIRTU
```

---

## Crash 66: `21468f7fae79772c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129082`

```sql
CREATE TABLE t3 (_rowid_ TEXT PRIMARY KEY ASC, UNIQUE (_rowid_, _rowid_)); DROP TABLE t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 67: `f678a10636490d3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146017`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 VARCHAR(255) NOT NULL DEFAULT 9807943853979885.69183e+48385679); PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2); CREAT
```

---

## Crash 68: `370c20fa6adcbf79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149871`

```sql
PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 69: `6c0190f9d5eb0086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149952`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 70: `75d4bb24836f4b9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149978`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 71: `7ff0a829d71f9f18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156051`

```sql
BEGIN IMMEDIATE; ROLLBACK TRANSACTION; ATTACH ':memory:' AS db2; BEGIN IMMEDIATE TRANSACTION; ROLLBACK; CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ REAL); CREATE TEMP TABLE IF NOT EXISTS t3 (c3 INTEGE
```

---

## Crash 72: `3f10afb21f424b9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156221`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ INT PRIMARY KEY ASC); BEGIN IMMEDIATE; DROP TABLE t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 73: `12e9e4445c3675aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158457`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); UPDATE OR ROLLBACK t1 SET c3 = EXISTS (SELECT *, * 
```

---

## Crash 74: `94600857d198a0a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159787`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BLOB PRIMARY KEY DESC, rowid FLOAT UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 75: `d276d5ef4c65ed49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161150`

```sql
VALUES (NOT CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 76: `8a46aaa48fdad2f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161239`

```sql
VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 77: `38c3e28d6634d986` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161854`

```sql
SELECT DISTINCT count(*) FILTER (WHERE FALSE) OVER () AS ihc__3t8_k_w_3_6_gveg_u_g7o__496_s9_d4_p_5h491_0_3h__6_2zdzd___e_5e1j__4u_2q_68h0_0d_h97rxwv8b_p53_p_4_8____665_c9b3x95_pv5q36_61wo_8h_j71_2qk2
```

---

## Crash 78: `59a7843f628ca663` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161938`

```sql
SELECT DISTINCT FALSE AS ihc__3t8_k_w_3_6_gveg_u_g7o__496_s9_d4_p_5h491_0_3h__6_2zdzd___e_5e1j__4u_2q_68h0_0d_h97rxwv8b_p53_p_4_8____665_c9b3x95_pv5q36_61wo_8h_j71_2qk23_i0m__11da__6_b_23_9__ig_g79j__
```

---
