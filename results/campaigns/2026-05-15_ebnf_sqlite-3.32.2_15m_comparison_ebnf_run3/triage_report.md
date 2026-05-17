# Crash Triage Report

**Total crashes:** 116  
**Unique crash sites:** 116  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 116 | 116 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `65dfba6fbb68a5c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000498`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 2: `4f4a5eeab7be3195` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000661`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3, c2);
```

---

## Crash 3: `f7661b34fa8aa70d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000896`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 4: `f2572358e917b2bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002564`

```sql
CREATE TEMP TABLE t3 (_rowid_ INTEGER PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 5: `1817bc8aeab5021c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002570`

```sql
CREATE TABLE t2 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 6: `82b467c5ad5bb9ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002577`

```sql
CREATE TABLE t2 (c1 REAL NOT NULL REFERENCES t3 (_rowid_) ON UPDATE CASCADE, rowid DATE PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 7: `6708a2c634455704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002593`

```sql
PRAGMA page_size; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 8: `c2c3c6642ca405d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002914`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 9: `6fc5b4dec582b147` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002927`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 10: `fa0b234a87fea7bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002933`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 11: `e067a5cf599e9e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009394`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ANALYZE t1;
```

---

## Crash 12: `e1de56b52129066f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009517`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); REINDEX;
```

---

## Crash 13: `5a7dbfd7af19537f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017797`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 14: `83fde65715b3778d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017967`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 15: `83a9e1fdd0c56211` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018037`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 16: `52fc9db88afb765e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018295`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); COMMIT TRANSACTION;
```

---

## Crash 17: `2d53746a389aa9ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018487`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 18: `0e760d53ad28b7d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018974`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 19: `702d100e6f4f3f68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020469`

```sql
VACUUM; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 20: `5380eedeff494237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022062`

```sql
CREATE TABLE t2 (c1 BLOB PRIMARY KEY DESC); ALTER TABLE t2 ADD COLUMN c3 DATE NOT NULL REFERENCES t3 (_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUA
```

---

## Crash 21: `ba41dd53069e585f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022270`

```sql
CREATE TABLE t2 (_rowid_ BOOLEAN UNIQUE, c2 REAL PRIMARY KEY); ALTER TABLE t2 ADD COLUMN c3 DATE NOT NULL REFERENCES t3 (_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 22: `ec36fb6a5e04f4c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022466`

```sql
CREATE TABLE t2 (_rowid_ FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PRAGMA optimize;
```

---

## Crash 23: `22833e81260653b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023842`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 24: `3086177f0e3820ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027563`

```sql
CREATE TEMP VIEW v1 AS SELECT * FROM t3 NOT INDEXED JOIN t1 AS a ON CASE WHEN TRUE THEN NULL END GROUP BY NULL HAVING FALSE LIMIT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 25: `b30598bf2bd05eac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027638`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 26: `0b76b52036c8ac6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027644`

```sql
CREATE VIEW v1 AS VALUES (RAISE(IGNORE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 27: `595c6ea38c5cced4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027650`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 28: `3cfddc4990a67777` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027763`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid NUMERIC DEFAULT CURRENT_TIMESTAMP, c2 VARCHAR(255) PRIMARY KEY DESC, c1 NUMERIC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, _rowid_, c3);
```

---

## Crash 29: `aa0d921a6888a97d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027916`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 30: `48eeb6ab90507de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028000`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 31: `7ef11e30e6a6276b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028006`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 32: `818b1b51f45ffadb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031474`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA cache_size=+0; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 33: `24173462cb178334` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034397`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c3, _rowid_);
```

---

## Crash 34: `147176cfc8a3e420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037001`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 BLOB PRIMARY KEY DESC, c1 REAL UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 35: `949774c18561939f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045202`

```sql
SELECT DISTINCT CURRENT_TIME ORDER BY RAISE(IGNORE) DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 36: `7b90502b433064a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047413`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 INTEGER COLLATE NOCASE); CREATE TABLE IF NOT EXISTS t2 (rowid NUMERIC DEFAULT CURRENT_TIMESTAMP, c2 INT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 37: `7a6d56c3ecbde15c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048798`

```sql
CREATE TABLE t2 (rowid BLOB COLLATE NOCASE, UNIQUE (rowid), CHECK (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE 
```

---

## Crash 38: `c6e122cb07c5c8f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049826`

```sql
PRAGMA analysis_limit=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 39: `6118a7533911d19a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049930`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 40: `8588b63a00bafd3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053402`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TA
```

---

## Crash 41: `d45961b8a921ceeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054408`

```sql
CREATE TABLE t2 (_rowid_ VARCHAR(255) CHECK (CURRENT_DATE), c2 REAL PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 42: `da5e463af1277d96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054865`

```sql
CREATE TABLE t2 (c2 BLOB PRIMARY KEY DESC); ALTER TABLE t2 RENAME TO t1; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 43: `6354ded2c21a1609` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055073`

```sql
CREATE TABLE t2 (_rowid_ BLOB NOT NULL DEFAULT NULL, c2 FLOAT NOT NULL); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); DETACH db2; WITH RECURSIVE t2 AS (SE
```

---

## Crash 44: `de3e644f751b27b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055271`

```sql
CREATE TABLE t2 (c3 BOOLEAN NOT NULL); ALTER TABLE t2 RENAME COLUMN c3 TO c2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 45: `d7c3cfecfc303069` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055441`

```sql
ANALYZE; BEGIN EXCLUSIVE TRANSACTION; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 46: `17afc2022d6e87eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055721`

```sql
CREATE TABLE t2 (_rowid_ FLOAT UNIQUE); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 47: `3d54cc57a50483e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058680`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_);
```

---

## Crash 48: `260fc096cf5d775f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058958`

```sql
CREATE TEMP VIEW v1 AS SELECT * UNION ALL SELECT DISTINCT * ORDER BY EXISTS (VALUES (CURRENT_TIME, RAISE(IGNORE))) NULLS LAST, -TRUE ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 49: `01652b967ae52332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059077`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 50: `91cdb989696db11d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059084`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 51: `8a15b9e7946ddfbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059091`

```sql
CREATE TEMP VIEW v1 AS SELECT * UNION ALL SELECT DISTINCT * ORDER BY CURRENT_TIME ASC NULLS FIRST, -TRUE ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 52: `e059f47bfae5c17c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059438`

```sql
VACUUM; BEGIN EXCLUSIVE TRANSACTION; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 53: `4f43f012fca5cbf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060528`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); ALTER TABLE t2 ADD COLUMN c1 DATE NOT NULL DEFAULT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 54: `f6d00cbaf3f20bd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060947`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t2 ADD COLUMN c1 DATE NOT NULL DEFAULT FALS
```

---

## Crash 55: `6811f3d3379d99c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061124`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 56: `20b582f59407cb6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061999`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ FLOAT UNIQUE, rowid BLOB PRIMARY KEY DESC); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 57: `2489a0f8787b3c70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065534`

```sql
CREATE TABLE t3 (rowid TEXT NOT NULL DEFAULT TRUE, c3 BLOB UNIQUE, CHECK (FALSE), CHECK (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 58: `50a03e1a0490c86c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065540`

```sql
BEGIN DEFERRED TRANSACTION; PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 59: `8e8e74d2a5280068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065559`

```sql
BEGIN DEFERRED TRANSACTION; SELECT * FROM (VALUES (CURRENT_TIME)) AS a GROUP BY FALSE, CURRENT_TIME HAVING FALSE ORDER BY CURRENT_TIMESTAMP ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 60: `54b517d657274bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065597`

```sql
BEGIN DEFERRED TRANSACTION; SELECT * FROM (VALUES (CURRENT_TIME)) AS a WHERE FALSE >> CURRENT_TIME INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 61: `ad34ff4c6405eaa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065626`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c3, c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 62: `9f02c7781829320c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065647`

```sql
BEGIN DEFERRED TRANSACTION; PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 63: `37386453bb345a54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079663`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT *; CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN SELECT * FROM t1; END; PRAGMA cache_size=-6; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREAT
```

---

## Crash 64: `f616222d1f54b612` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080277`

```sql
ATTACH ':memory:' AS db2; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t3 (c2) VALUES (c3, CURRENT_DATE / NULL ISNULL = +CURRENT_TIME COLLATE RTRIM > CASE WHEN (CASE r
```

---

## Crash 65: `3870ab73d94abcc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080374`

```sql
BEGIN EXCLUSIVE TRANSACTION; PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, _rowid_);
```

---

## Crash 66: `eae170d1c4861661` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085265`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 BLOB NOT NULL); VACUUM; REINDEX t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, * FROM t3 INNER JOIN t1 WHERE CURRENT_DATE > TRUE ORDER BY NUL
```

---

## Crash 67: `05a9661895ca99bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092006`

```sql
BEGIN DEFERRED; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2); ROLLBACK TO sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3);
```

---

## Crash 68: `1ee34c87dce72c5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092435`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 69: `dd9c8f44158a9c64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104496`

```sql
BEGIN EXCLUSIVE TRANSACTION; PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 70: `0547b81d94dd431c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104586`

```sql
BEGIN EXCLUSIVE TRANSACTION; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 71: `3354a0cb12392c69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105249`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT *; CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); COMMIT TRANSACTION;
```

---

## Crash 72: `34b34ba11fd6f1c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106078`

```sql
CREATE TABLE t2 (_rowid_ REAL, UNIQUE (_rowid_) ON CONFLICT IGNORE); ALTER TABLE t2 RENAME TO t1; REPLACE INTO t1 VALUES (NULL); REPLACE INTO t1 VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 73: `485f0122d5e3a8f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106596`

```sql
CREATE TEMP VIEW v1 AS WITH t2 AS (SELECT ALL *) SELECT * FROM t1 NOT INDEXED GROUP BY 649.0669577703219525156186408024457799704193540506278798688903611189108104565978915250399085547390198001721548500
```

---

## Crash 74: `bbfecb72b0b34106` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106716`

```sql
CREATE TEMP VIEW v1 AS SELECT *; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 75: `187fe320c2d604db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125345`

```sql
PRAGMA synchronous=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); VACUUM; CREATE TABLE t3 (c3 VARCHAR(255) CHECK (~CURRENT_TIMESTAMP < CURRENT_TIMESTAMP IS NOT DISTINCT FROM CASE 
```

---

## Crash 76: `863bf726f1cba1d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129468`

```sql
CREATE TEMP TABLE t2 (_rowid_ INTEGER NOT NULL); PRAGMA analysis_limit=594233; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, rowid,
```

---

## Crash 77: `63a79904b7997b1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129768`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE TRIGGER trg1 AFTER UPDATE OF rowid ON t2 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_r
```

---

## Crash 78: `6ffdf6808c9f237b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130773`

```sql
PRAGMA cache_size=0; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 79: `024b2f30edeab0e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130914`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); ALTER TABLE t2 RENAME TO t1; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); C
```

---

## Crash 80: `a8e00ca4b7950b3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132614`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); ALTER TABLE t2 RENAME TO t1; REPLACE INTO t1 VALUES (NULL); REPLACE INTO t1 VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 81: `628475645eb7085a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133230`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ REAL NOT NULL); ALTER TABLE t2 RENAME TO t1; REPLACE INTO t1 VALUES (EXISTS (VALUES (NULL))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 82: `c5522f6e4064b598` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133441`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 83: `fc45e7d0abb85d29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133569`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid TEXT NOT NULL DEFAULT 44500806703061193087933113408707729159.790e+6578735617289258156422284307477271293758738293593253860972); ALTER TABLE t2 RENAME TO t1; CREATE 
```

---

## Crash 84: `4ff22bf4bfad3a76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134522`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid NUMERIC DEFAULT CURRENT_TIMESTAMP, c2 REAL NOT NULL); ALTER TABLE t2 RENAME TO t1; BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); 
```

---

## Crash 85: `51d20617e68b576a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134681`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid NUMERIC GENERATED ALWAYS AS (TRUE LIKE TRUE IS NOT RAISE(IGNORE)) VIRTUAL, c3 INT PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSER
```

---

## Crash 86: `a525178f38939400` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135102`

```sql
CREATE TABLE t2 (c2 INTEGER DEFAULT 626, c1 TEXT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, _rowid_); CREATE TEMP VIEW IF NOT EXISTS v1 AS WITH RECURSIVE 
```

---

## Crash 87: `82056205769ef952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135911`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t2 ADD COLUMN c1 DATE NOT NULL DEFAULT 8127
```

---

## Crash 88: `f322a5aa596157d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138388`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1, c1, rowid) AS VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_);
```

---

## Crash 89: `d74c75c9283a6fb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139093`

```sql
CREATE TABLE t3 (rowid TEXT NOT NULL DEFAULT CURRENT_DATE, c3 BLOB UNIQUE, PRIMARY KEY (rowid) ON CONFLICT REPLACE, CHECK (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _row
```

---

## Crash 90: `82adfe7ea830c378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140023`

```sql
CREATE TABLE t2 (c3 FLOAT); ALTER TABLE t2 RENAME TO t1; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 91: `e880285983d1f64a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141005`

```sql
CREATE TABLE t2 (_rowid_ TEXT PRIMARY KEY ASC); ALTER TABLE t2 RENAME TO t1; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 92: `6eaaf74d8c4a4983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141080`

```sql
CREATE TABLE t2 (_rowid_ TEXT PRIMARY KEY ASC); ALTER TABLE t2 RENAME TO t1; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES;
```

---

## Crash 93: `424e344c37fb0419` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142598`

```sql
CREATE TABLE t2 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 94: `07bb20a552065be5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144760`

```sql
CREATE TABLE t2 (_rowid_ VARCHAR(255) CHECK (CURRENT_DATE), c2 REAL PRIMARY KEY); CREATE UNIQUE INDEX idx1 ON t2 (c2); DROP INDEX IF EXISTS idx1; PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 95: `a5e427fc63492d96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145133`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC) WITHOUT ROWID; ALTER TABLE t2 RENAME TO t1; REPLACE INTO t1 VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 96: `26c1bf4abf43463e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145495`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC) WITHOUT ROWID; ALTER TABLE t2 ADD COLUMN c1 INTEGER GENERATED ALWAYS AS (TRUE) VIRTUAL; ALTER TABLE t2 ADD COLUMN c2 DATE; CREATE VIRTUA
```

---

## Crash 97: `ab0a9650d7dcffc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145897`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 INTEGER PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ALTER TABLE t2 RENAME TO t1; CREATE INDEX IF NOT EXISTS idx1 ON
```

---

## Crash 98: `c78ac5a93553012c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146191`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY ASC) WITHOUT ROWID; ALTER TABLE t2 ADD COLUMN _rowid_ VARCHAR(255) CHECK (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 99: `cad551e446ff0a14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146849`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c3 DATE UNIQUE); ALTER TABLE t2 ADD COLUMN c1 BOOLEAN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 100: `199cfded18136635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149727`

```sql
SELECT * FROM (VALUES (CURRENT_TIME)) AS a WHERE CURRENT_DATE LIKE CURRENT_TIME INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ROLLBACK;
```

---

## Crash 101: `838afc922aa2bd01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151798`

```sql
SELECT * FROM (VALUES (CURRENT_TIME)) AS a WHERE TRUE < NULL INTERSECT VALUES (CURRENT_TIMESTAMP); BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH t2 (r
```

---

## Crash 102: `811b5efe641ea872` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151832`

```sql
SELECT * FROM (VALUES (CURRENT_TIME)) AS a WHERE CURRENT_DATE INTERSECT VALUES (CURRENT_TIMESTAMP); BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH t2 (
```

---

## Crash 103: `5fdeab37d9e93f41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151983`

```sql
VALUES (CURRENT_DATE >> CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 104: `1f5cf6f7ca049e94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152143`

```sql
SELECT * FROM (VALUES (count(*) OVER ())) AS a WHERE CURRENT_DATE INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TABLE t1 AS SELECT ALL (+CURREN
```

---

## Crash 105: `5d543e9e8a91efc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152192`

```sql
SELECT * FROM (VALUES (NULL)) AS a WHERE CURRENT_DATE INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TABLE t1 AS SELECT ALL (+CURRENT_DATE IS DI
```

---

## Crash 106: `6f1d774a588af244` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155558`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 107: `ab7f93d267ee9379` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156095`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 VARCHAR(255) PRIMARY KEY DESC, _rowid_ VARCHAR(255) CHECK (CURRENT_DATE)); UPDATE OR FAIL t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 108: `8dcd53f6ebfa7a79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156135`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 VARCHAR(255) PRIMARY KEY DESC, c3 BLOB UNIQUE); UPDATE OR FAIL t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 109: `e4954cd448110354` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156254`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 VARCHAR(255) PRIMARY KEY DESC, c1 DATE NOT NULL DEFAULT TRUE); UPDATE OR FAIL t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 110: `0c9d0a07bc34f016` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156954`

```sql
PRAGMA foreign_keys=ON; CREATE TABLE t2 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DROP INDEX IF EXISTS idx1;
```

---

## Crash 111: `19a7682447eaf668` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157024`

```sql
PRAGMA foreign_keys=ON; CREATE TABLE t2 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM INTO ':memory:';
```

---

## Crash 112: `50fe75c9f20141c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157073`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE TABLE t2 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); ALTER TABLE t2 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM INTO ':memory:';
```

---

## Crash 113: `797cdae7859107b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157083`

```sql
PRAGMA foreign_keys=ON; CREATE TABLE t2 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM INTO ':memory:';
```

---

## Crash 114: `15a57021d6c86238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157156`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 115: `ae2d6310a14e793c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159095`

```sql
SELECT DISTINCT CURRENT_TIMESTAMP, NULL ORDER BY RAISE(IGNORE) DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 116: `baa5b88262fa6588` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161707`

```sql
VALUES (X'ffeBaD'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_, c1, c2, _rowid_); VACUUM;
```

---
