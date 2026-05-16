# Crash Triage Report

**Total crashes:** 211  
**Unique crash sites:** 211  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 211 | 211 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `e1ca8aeea614d715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 2: `457f06b83e6d436c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000814`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, c2);
```

---

## Crash 3: `02ef108d5bd8fe6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001450`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 4: `bbe427fa11afeb66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002028`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 5: `1f31226a2fc62263` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002034`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 INTEGER PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 6: `9917ff792b03bb60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002045`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 7: `848531ae05d7ea57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006410`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c3, c2, c3, c3);
```

---

## Crash 8: `247d40930e0d7fda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006419`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 9: `17db6f6d2f9a2819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006425`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 10: `4d026391581c5f48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006540`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 11: `8471a91e444d9cf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006571`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 12: `9e8ad98f52be29b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009661`

```sql
VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM (VALUES (FALSE)) AS u; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 13: `43004a6b34859f22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014086`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL NOTNULL, 38; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `024bcb56aec46920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015063`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3);
```

---

## Crash 15: `f9f948cd57da6cff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015445`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 16: `66fd59ad095c215e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015550`

```sql
VACUUM; CREATE TEMP VIEW v1 AS WITH RECURSIVE t2 (rowid) AS (SELECT t2.*) SELECT DISTINCT t3.* LIMIT random() OVER () OFFSET NULL / CURRENT_TIMESTAMP & CURRENT_TIMESTAMP; VACUUM; CREATE VIRTUAL TABLE 
```

---

## Crash 17: `900664b30ef1ae06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015612`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); ANALYZE t2; ATTACH ':memory:' AS db2; REINDEX t
```

---

## Crash 18: `49b0a1342d5cda73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016335`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 19: `fa73fb84ca6c8b93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017486`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 20: `329b9cfca549e8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017652`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 21: `fb9aa27da69c3cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017658`

```sql
CREATE TEMP TABLE t1 (c3 INT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 22: `95301307c6a85583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023222`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid FLOAT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ANALYZE t1;
```

---

## Crash 23: `b0f88a19953d31b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023916`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 24: `a3902b7121adeae2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023950`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 25: `f2fe171f522c2471` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023998`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c2, _rowid_);
```

---

## Crash 26: `a5d7b5d34d5c5543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024070`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c2, _rowid_);
```

---

## Crash 27: `951a154433136247` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024902`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT ALL * UNION SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT OUTER JOIN t3 NOT INDEXED ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 28: `288697475eb6789d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024984`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 29: `8b09f38b150a1790` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026280`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 30: `2ed92196d78575a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026691`

```sql
PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE TABLE t1 (rowid TEXT DEFAULT X'') WITHOUT ROWID, STRICT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(
```

---

## Crash 31: `5e31661fd6541331` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026756`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE TABLE t1 (rowid TEXT DEFAULT X'') WITHOUT ROWID, STRICT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(r
```

---

## Crash 32: `4022467c3d2e6f23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027880`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 33: `84607f7af2ff408f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029086`

```sql
BEGIN; PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 34: `6d2c0596b0c3a6b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032564`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 35: `a17a3785f96574f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032721`

```sql
CREATE VIEW IF NOT EXISTS v1 (rowid) AS VALUES (NULL) UNION ALL SELECT DISTINCT * ORDER BY RAISE(IGNORE) ASC, FALSE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 36: `5efd1de38ae5e1d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033589`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid BLOB PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 37: `35a5b1c255121ba4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034753`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid BOOLEAN DEFAULT -0, c3 BLOB PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); CREATE TRIGGER trg1 BEFORE DELETE ON t2 BEGI
```

---

## Crash 38: `f71134e90e9ff7d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035367`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 39: `534ca889a4221482` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037402`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 INT PRIMARY KEY ASC, c2 REAL COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 40: `19be6e1fb0d40040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038792`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN SELECT CAST(FALSE GLOB CURRENT_TIME AS INTEGER), -TRUE <> RAISE(IGNORE) I
```

---

## Crash 41: `1698564e3d2c8a86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039124`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3, c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 42: `faa3b07eb572bb43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039162`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 43: `53c7dc75c55a95d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040596`

```sql
CREATE VIEW v1 (rowid) AS VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM t2 NOT INDEXED GROUP BY CURRENT_TIME HAVING CURRENT_TIME WINDOW w1 AS () LIMIT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 44: `e365559340aa3aed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041938`

```sql
PRAGMA cache_size=+0; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK TO sp1; DETACH db2; INSERT OR ROLLBACK INTO t3 VALUES (json_extract(CURRENT_TIMESTAMP, 'Ous1qqjzx') FIL
```

---

## Crash 45: `a1b406be97ace6b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043690`

```sql
BEGIN EXCLUSIVE TRANSACTION; SAVEPOINT sp1; ROLLBACK TO sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 46: `922e890c0922694a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044355`

```sql
BEGIN TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t2 (rowid INTEGER PRIMARY KEY DESC); CREATE TEMP TABLE IF NOT EXISTS t1 (c2 INT UNIQUE); COMMIT; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF
```

---

## Crash 47: `72eb3829c94e3944` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047531`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 48: `933285137bec5929` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047803`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TABLE t3 AS VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 49: `8fcfa61694fe1b1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048751`

```sql
BEGIN EXCLUSIVE TRANSACTION; PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 50: `d33d781aa63d1daf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050011`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); END TRANSACTION; CREATE TABLE t1 (_rowid_ BOOLEAN PRIM
```

---

## Crash 51: `a063b673b94523f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050120`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 52: `40ce950d5ef69b49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053637`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE FALSE GROUP BY TRUE HAVING NULL EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 53: `a699a2cbeffdd0c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054287`

```sql
VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 54: `fc72ff7d5f577831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056478`

```sql
PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ANALYZE t1; DETACH db2; REINDEX t2; COMMIT;
```

---

## Crash 55: `24888623acccb912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058388`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DETACH DATABASE db2;
```

---

## Crash 56: `80c375a68c70f24d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069256`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3); DETACH DATABASE db2;
```

---

## Crash 57: `b2d2f2dbfa01fc38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071727`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || TRUE AS b821qtuwb ORDER BY NULL LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 58: `e364db7a5095bbbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072482`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_DATE MATCH ~CAST(CURRENT_DATE < TRUE AS TEXT), FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 59: `b6ac0b99933b479d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072805`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(CURRENT_DATE < TRUE AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid
```

---

## Crash 60: `95f7610c98d72242` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072943`

```sql
CREATE TABLE t2 (c2 INTEGER PRIMARY KEY); REINDEX t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 61: `b029435bfdfb1aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073125`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE, last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 62: `8ab3cecbf4bfed61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073322`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE, printf('3', FALSE NOT GLOB FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c
```

---

## Crash 63: `2feb291565b525f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073740`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS TEXT) IS 38, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 64: `c063175ea8404009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073969`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE IS CAST(TRUE AS TEXT), TRUE; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 65: `6f33b6588aa8b01f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074026`

```sql
DROP INDEX IF EXISTS idx1; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN TRANSACTION; CREATE TABLE IF NOT EXISTS t1 (c2 DATE CHECK ((TRUE == FALSE & CURRENT_
```

---

## Crash 66: `92c5414be9f341c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074039`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE IS CURRENT_TIMESTAMP, TRUE; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 67: `a6486e841cb07f76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075020`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 68: `294fac62ccde64b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075194`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * CURRENT_TIME, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TABLE t1 (c3
```

---

## Crash 69: `0d236a88f4855918` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075399`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * CAST(TRUE AS FLOAT) IS CURRENT_TIME, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 70: `79b605d02cff7a8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075734`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * ~TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 71: `45cb7fbcdf1905ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077813`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL IS TRUE * NULL, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 72: `784521a9acfccf3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077883`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 73: `6ae96ecfef0092f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078260`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE - FALSE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, _rowid_);
```

---

## Crash 74: `019cf4e9fb66b4ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078785`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL IS TRUE COLLATE BINARY, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 75: `0697f4a8d34c12e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078897`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL IS CURRENT_TIMESTAMP, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 76: `79bd106025acdf00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079346`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIMESTAMP IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 77: `452a5f991d1449e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079520`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIME IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 78: `350d6ed7a8c3f75f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079697`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIME ISNULL IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 79: `a5fd833109db8b31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080072`

```sql
CREATE TABLE t2 AS SELECT +NULL AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE IS TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 80: `e21043ff15087063` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080819`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 81: `e2691c745aa1afe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081907`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 82: `22d04613a3397ede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082027`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY (FALSE, FALSE) ASC NULLS LAST LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1);
```

---

## Crash 83: `2f9f7138bd1e4380` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082335`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); DROP TABLE t1; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ANALYZE t2; PRAGMA synchronous=NORMAL; ALTER 
```

---

## Crash 84: `2458fc0addd4ae89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091302`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_DATE, 0.0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 85: `49965f00cb1e395e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092811`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY CURRENT_DATE ASC, RAISE(IGNORE) DESC LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 86: `1d02d837327b3a6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093402`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP) UNION VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3);
```

---

## Crash 87: `ec972deb7d78312e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094800`

```sql
CREATE TABLE t3 (rowid INTEGER UNIQUE, c1 BOOLEAN, PRIMARY KEY (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 88: `f55cabb04238d6da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098831`

```sql
VALUES (-FALSE) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, _rowid_, c1, c1);
```

---

## Crash 89: `3615f196277506ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100203`

```sql
VALUES (FALSE << TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 90: `aba780d1ebb5f3ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100731`

```sql
VALUES (CURRENT_DATE < TRUE COLLATE BINARY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 91: `0618cfe138fde5a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100962`

```sql
VALUES (FALSE LIKE NULL || CURRENT_TIMESTAMP ESCAPE NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 92: `2dc58bbd31a885bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107223`

```sql
CREATE VIEW IF NOT EXISTS v1 (rowid, c2, rowid) AS WITH RECURSIVE t3 AS (VALUES (FALSE IS NULL) UNION ALL SELECT *) SELECT DISTINCT t1.* FROM t1 LIMIT CURRENT_TIME NOT LIKE CAST(RAISE(IGNORE) NOT NULL
```

---

## Crash 93: `53872d16fa255abc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110031`

```sql
VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM (SELECT * FROM (SELECT * FROM (VALUES (TRUE)) AS u) AS u) AS u; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, c1, c1); DETACH DATABASE
```

---

## Crash 94: `b8d84fa22685315b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114748`

```sql
VALUES (FALSE << -70); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_); DETACH db2; CREATE TEMP VIEW IF NOT EXISTS v1 AS VALUES (NOT CURRENT_DATE < TRUE IS NOT DISTINCT FROM
```

---

## Crash 95: `e1b474923ebac021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114843`

```sql
VALUES (FALSE << CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_); DETACH db2; CREATE TEMP VIEW IF NOT EXISTS v1 AS VALUES (NOT CURRENT_DATE < TRUE IS NOT DIST
```

---

## Crash 96: `8c1af74af162e463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114849`

```sql
VALUES (FALSE << CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_); DETACH db2; CREATE TEMP VIEW IF NOT EXISTS v1 AS VALUES (NOT CURRENT_DATE < TRUE IS NOT DIST
```

---

## Crash 97: `677ff8959cda3a86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114920`

```sql
VALUES (FALSE << X''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 98: `cb2572605dd4cf17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117481`

```sql
SELECT CURRENT_TIMESTAMP * ~TRUE * ~TRUE * CURRENT_TIMESTAMP AS b821qtuwb UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM; SELECT DISTINCT * FROM t2 WHERE NULL G
```

---

## Crash 99: `dafec9d7d2363c88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117534`

```sql
SELECT TRUE AS b821qtuwb UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM; SELECT DISTINCT * FROM t2 WHERE NULL GROUP BY CURRENT_TIME UNION ALL SELECT +RAISE(IGNO
```

---

## Crash 100: `a237eca6cbdf6342` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117540`

```sql
SELECT CURRENT_DATE * CURRENT_TIMESTAMP AS b821qtuwb UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM; SELECT DISTINCT * FROM t2 WHERE NULL GROUP BY CURRENT_TIME 
```

---

## Crash 101: `5b83bcabbe7750f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117546`

```sql
SELECT CURRENT_TIMESTAMP * ~TRUE * CURRENT_TIMESTAMP AS b821qtuwb UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM; SELECT DISTINCT * FROM t2 WHERE NULL GROUP BY 
```

---

## Crash 102: `2dafd8810f0d95e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117552`

```sql
SELECT CURRENT_TIMESTAMP * CURRENT_TIME * ~TRUE * CURRENT_TIMESTAMP AS b821qtuwb UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM; SELECT DISTINCT * FROM t2 WHERE
```

---

## Crash 103: `e075ce7cde4802db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117614`

```sql
VALUES (-31134239440595203669.2087) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 104: `51ef6928460e9150` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117714`

```sql
VALUES (NULL) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 105: `2f75b3c9fa57febb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118126`

```sql
VALUES (NULL) UNION SELECT 80188372101745119093333954828340829876966889207932790434690403619668884571131513624788099148216243920878986073394171446094695051568837201.5E72166342366; CREATE VIRTUAL TABLE
```

---

## Crash 106: `fbd651fd88dd24c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118184`

```sql
VALUES (NULL) UNION SELECT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 107: `3a3f8d202684f8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119746`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 NUMERIC REFERENCES t3 (c3) ON DELETE NO ACTION); ANALYZE t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM; VACUUM INTO ':memory:';
```

---

## Crash 108: `990cc1035000469b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119809`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 VARCHAR(255) UNIQUE); ANALYZE t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM; VACUUM INTO ':memory:';
```

---

## Crash 109: `49f454c5f68d7ad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119888`

```sql
CREATE TABLE t3 (c1 INTEGER, PRIMARY KEY (c1) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); END TRANSACTION;
```

---

## Crash 110: `7c70fe30e6c21715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124375`

```sql
CREATE TABLE t2 (rowid DATE NOT NULL DEFAULT 91.18875387568936324685335414e-503793065484477310743969092828672072314617902496120500854547782411); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 111: `4d6bb96b2baf2e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127441`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid VARCHAR(255) PRIMARY KEY ASC); BEGIN DEFERRED; CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME | TRUE ISNULL) UNION ALL SELECT RAISE(IGNORE) FROM t1 NOT INDEX
```

---

## Crash 112: `6c6bf543867c8854` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128866`

```sql
CREATE TABLE t2 AS SELECT 41.233426045462783E96 AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 113: `f6c8428ef7bbeb06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132756`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; BEGIN DEFERRED TRANSACTION; INSERT INTO t1 DEFAULT 
```

---

## Crash 114: `c2611abd467a902b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134907`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); REPLACE INTO t1 VALUES (TRUE); INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 115: `79b749e44338080e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134952`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); REPLACE INTO t1 VALUES (TRUE); INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; VACUUM; REPLACE INTO t1 VALUES (CURRENT_DATE % tota
```

---

## Crash 116: `f9814e7700e68d47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135287`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); REPLACE INTO t1 VALUES (TRUE); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); INSERT 
```

---

## Crash 117: `50f1bec82fa28bfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137202`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL, -13273415869503817571399844.8726694134E-1104670476256611093695548288218265140093891190; CREATE VIR
```

---

## Crash 118: `657026fed82045ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141444`

```sql
CREATE TABLE t2 AS SELECT * FROM (SELECT * FROM (VALUES (FALSE)) AS u) AS u ORDER BY count(*) FILTER (WHERE NULL) OVER () LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 119: `883395a00152b069` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141996`

```sql
CREATE TABLE t2 AS SELECT FALSE IN (SELECT * FROM (VALUES (FALSE)) AS u ORDER BY TRUE ASC NULLS FIRST) AS a ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 120: `3a2ecb214289eb47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142435`

```sql
CREATE TABLE t2 AS SELECT FALSE IN (VALUES (CAST(NULL AS FLOAT))) AS a ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 121: `eaa28983a146e577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143849`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * CAST(TRUE AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, c3);
```

---

## Crash 122: `3dc1dda62683429c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144007`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_DATE * CAST(TRUE AS FLOAT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c
```

---

## Crash 123: `5b463347f2f6597e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144428`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT NULL IS TRUE IS CAST(TRUE AS FLOAT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 124: `5496d371e0ba7dba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144778`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS REAL) IS TRUE * CURRENT_TIME, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 125: `af7832f808eda02e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144916`

```sql
CREATE TABLE t2 AS SELECT min(CURRENT_TIMESTAMP) FILTER (WHERE FALSE) AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT TRUE * TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 126: `15c2d5ef78df60ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145919`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS NUMERIC) IS CAST(TRUE AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 127: `02c5b6b06891a3b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146115`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS TEXT) IS CAST(TRUE AS DATE), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 128: `1877fb7eadb71d6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146173`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE IS CAST(TRUE AS DATE), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 129: `160960666f3ee992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146179`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS TEXT) IS FALSE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 130: `57c661213e6f58d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147770`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE, X'EFFafd' NOT GLOB FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 131: `b6cbdcbfd6b9c1e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148959`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT ~CAST(CURRENT_TIMESTAMP AS BLOB), FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 132: `8c4683b21bb509a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150273`

```sql
CREATE TABLE t2 (c2 BOOLEAN PRIMARY KEY, c3 NUMERIC UNIQUE) WITHOUT ROWID; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2, c2, c3);
```

---

## Crash 133: `55ae5a11e2268453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150389`

```sql
CREATE TABLE t2 AS SELECT * FROM (VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM (VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE)) AS u) AS u ORDER BY NULL LIMIT TRUE; ATTACH ':memory:' AS db2; CR
```

---

## Crash 134: `aa917c4e0742e57d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151798`

```sql
CREATE TABLE t2 AS SELECT count(*) OVER (), * FROM (VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE)) AS u ORDER BY NULL LIMIT TRUE; PRAGMA analysis_limit=+0; CREATE TRIGGER trg1 BEFORE UPDATE ON t2 BE
```

---

## Crash 135: `1e6c090f3406c2d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154467`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME); UPDATE OR ROLLBACK t2 SET rowid = EXISTS (SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIME); CREATE VIRTUAL TABLE IF 
```

---

## Crash 136: `02814aaa5347c5dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155042`

```sql
CREATE TABLE t2 AS SELECT DISTINCT -26.4038834144049713552729619E64; UPDATE OR ROLLBACK t2 SET rowid = CURRENT_DATE & CURRENT_TIMESTAMP; REINDEX t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 137: `b08bf2fbe46fc483` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155451`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ INTEGER NOT NULL DEFAULT X'7b0FeA3DFCBa9F'); UPDATE OR ROLLBACK t2 SET rowid = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 138: `63af662b53402ad5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155549`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid INTEGER PRIMARY KEY DESC); UPDATE OR ROLLBACK t2 SET rowid = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 139: `95acb4a9b05b25d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155555`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 REAL NOT NULL); UPDATE OR ROLLBACK t2 SET rowid = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 140: `b73bb9bbffd05fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155561`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ INTEGER NOT NULL DEFAULT CURRENT_DATE); UPDATE OR ROLLBACK t2 SET rowid = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 141: `1571913683eacfc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156931`

```sql
CREATE TABLE t2 AS SELECT count(*) OVER (PARTITION BY NULL, CURRENT_TIMESTAMP) ORDER BY NULL LIMIT CURRENT_DATE AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 142: `e214fd42c669ef65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156994`

```sql
CREATE TABLE t2 AS SELECT count(*) OVER () ORDER BY NULL LIMIT CURRENT_DATE AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 143: `a6d2f6c40aeeab82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177670`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS t3 (rowid INTEGER GENERATED ALWAYS AS (CURRENT_TIMESTAMP) VIRTUAL, _rowid_ DATE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 144: `e028a5d75a68a17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181253`

```sql
CREATE TEMP TABLE t2 (_rowid_ INTEGER PRIMARY KEY); UPDATE OR ROLLBACK t2 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 145: `efe69ccf6664bad7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181978`

```sql
CREATE VIEW v1 AS SELECT ALL *; CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 146: `54c374adbfd0b7d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182000`

```sql
CREATE VIEW v1 AS SELECT ALL *; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 147: `3fabfa0f121febb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182792`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 148: `6d2dc8337f18cd21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184159`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE FALSE GROUP BY CURRENT_TIME UNION VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 149: `c1654222cb7c79f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184379`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE CURRENT_TIMESTAMP LIKE CURRENT_TIME GROUP BY CURRENT_DATE EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VACUUM 
```

---

## Crash 150: `de09d01cef390940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184433`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE CURRENT_TIME GROUP BY CURRENT_DATE EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VACUUM INTO ':memory:'; WITH t
```

---

## Crash 151: `67e9c2b5b7ee52ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184710`

```sql
VALUES (CURRENT_TIME NOT GLOB FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 152: `55cf95966c2d7d3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190294`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (c3 REAL NOT NULL DEFAULT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 153: `300cc31adc0b2155` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190519`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 154: `95e559a4850fc0fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194667`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid BLOB PRIMARY KEY ASC) WITHOUT ROWID; DROP TABLE t1; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 155: `bec717422c425ec9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194749`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid BLOB PRIMARY KEY ASC) WITHOUT ROWID; DROP VIEW IF EXISTS v1; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 156: `10ec6dff56af242c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196063`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INT UNIQUE, c3 BLOB PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3); ROLLBACK;
```

---

## Crash 157: `78717583b291bf0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197193`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c1 BLOB PRIMARY KEY ASC); CREATE TRIGGER trg1 BEFORE DELETE ON t2 BEGIN UPDATE t1 SET c2 = CURRENT_TIMESTAMP; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 158: `731812f0b55c5fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197459`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 INT NOT NULL REFERENCES t3 (c3) ON UPDATE CASCADE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 159: `f4400d203e4a5c5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206726`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid INT PRIMARY KEY ASC); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN INSERT INTO t1 VALUES(CURRENT_TIME); END; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF 
```

---

## Crash 160: `710848076c6d3e2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208122`

```sql
CREATE VIEW v1 (c3) AS SELECT * FROM t2 INDEXED BY rowid JOIN t2 GROUP BY NULL WINDOW w1 AS (), w2 AS () ORDER BY TRUE DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 161: `8801260f1639afd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210296`

```sql
VALUES (NULL) UNION SELECT * FROM (VALUES (FALSE)) AS a WHERE CURRENT_TIMESTAMP GROUP BY NULL ORDER BY NULL COLLATE RTRIM COLLATE RTRIM NULLS FIRST; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE I
```

---

## Crash 162: `8b600751415ec082` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213368`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INT UNIQUE, c3 BLOB PRIMARY KEY DESC) WITHOUT ROWID; REINDEX; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 163: `e4421e3cd51fb8b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218397`

```sql
CREATE TABLE t1 (rowid INT NOT NULL DEFAULT NULL); INSERT OR IGNORE INTO t1 VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TRIGGER trg1 AFTER INSERT ON t3 FOR EACH RO
```

---

## Crash 164: `a61632ddd16ccd79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218462`

```sql
CREATE TABLE t1 (c3 FLOAT COLLATE NOCASE); INSERT OR IGNORE INTO t1 VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TRIGGER trg1 AFTER INSERT ON t3 FOR EACH ROW BEGIN 
```

---

## Crash 165: `535f4819b219bd05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219231`

```sql
CREATE TABLE t3 AS VALUES (CAST(NULL AS FLOAT)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 166: `52dfe4822c8d04d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223548`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 167: `79ada5e2c98963d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225039`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE CURRENT_DATE < CURRENT_DATE OR TRUE GROUP BY NULL EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); CREATE VIEW
```

---

## Crash 168: `4ce46f0e7dce7f99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225534`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE NOT TRUE < TRUE GROUP BY NULL EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 169: `297140a3ccc57078` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225719`

```sql
SELECT * FROM (VALUES (FALSE)) AS a WHERE CURRENT_DATE < TRUE GROUP BY NULL EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 170: `6aac89a095c89397` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226545`

```sql
CREATE VIEW v1 AS SELECT ALL *; CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; PRAGMA analysis_limit=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); CREATE UNIQUE INDEX idx1 
```

---

## Crash 171: `bd7c3e2f16879f97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256616`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, _rowid_, c3, c1);
```

---

## Crash 172: `28461987764f1ad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259689`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP) UNION SELECT min(CURRENT_TIMESTAMP) OVER () FROM (VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE)) AS u; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 173: `8fbdaa13f876b7e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262643`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE, CURRENT_DATE NOT GLOB X'EFFafd'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 174: `b8522bc98c39ecad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262963`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS TEXT) IS CURRENT_TIME COLLATE NOCASE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 175: `d0ad4327705e0611` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263062`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIME IS CURRENT_TIME COLLATE NOCASE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 176: `e59452b9b04d3917` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263175`

```sql
CREATE TABLE t2 AS SELECT -FALSE ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS DATE) IS 38, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 177: `28f38faac8f68814` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263260`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS DATE) IS 38, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 178: `d636bdaaccdf514c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264215`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS NUMERIC) IS CAST(-874527243.6 AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 179: `8794d10085956113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264301`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS NUMERIC) IS CAST(NULL AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 180: `101121d9e9e5baec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264307`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS NUMERIC) IS CAST(CURRENT_TIMESTAMP AS TEXT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 181: `2dcbc6201d3ab306` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264800`

```sql
CREATE TABLE t2 AS SELECT group_concat(FALSE, '-u') AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT -70; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 182: `ff1787c623f4071b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265508`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CAST(TRUE AS FLOAT) IS CAST(TRUE AS FLOAT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 183: `4e10eaae51d5da65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265675`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIMESTAMP + TRUE * CAST(TRUE AS FLOAT), TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 184: `48674576e9bf6fe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265764`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_TIMESTAMP + TRUE * CURRENT_TIMESTAMP, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 185: `44e469bc3e5bd1cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266724`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT ~CURRENT_TIMESTAMP + TRUE * ~TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 186: `550f998137785a22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266830`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT ~CURRENT_TIMESTAMP * ~TRUE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 187: `c80965db7d8fbe3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266836`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT ~CURRENT_TIMESTAMP + TRUE * CURRENT_TIME, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 188: `6104b65b7811eb8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267774`

```sql
CREATE TABLE t2 AS SELECT 41.233426045462783E96 IN (VALUES (CAST(NULL AS FLOAT))) AS a ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 189: `501a7854410e5607` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269166`

```sql
CREATE TABLE t2 AS VALUES (FALSE); ALTER TABLE t2 ADD COLUMN rowid BOOLEAN DEFAULT -0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 190: `9269299de202ef5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269202`

```sql
CREATE TABLE t2 AS VALUES (FALSE); ALTER TABLE t2 ADD COLUMN rowid BOOLEAN DEFAULT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 191: `b8a6525638506ce8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000276107`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid TEXT PRIMARY KEY); REPLACE INTO t1 VALUES (json_type(~CURRENT_TIMESTAMP)); DROP TABLE t1; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 192: `613d3e1f0718f398` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277021`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 FLOAT); REPLACE INTO t1 VALUES (random()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 193: `465d250377044501` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000278742`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 194: `2b3e204fa326eba9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280204`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 BOOLEAN PRIMARY KEY DESC, c3 VARCHAR(255) UNIQUE); UPDATE OR IGNORE t1 SET _rowid_ = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 195: `3f8b2e7e1505eb64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280318`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 TEXT PRIMARY KEY DESC, _rowid_ INT COLLATE NOCASE); UPDATE OR IGNORE t1 SET _rowid_ = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 196: `bbab2e8d9fa0163e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000287104`

```sql
CREATE TABLE t2 AS SELECT count(*) OVER () ORDER BY count(*) FILTER (WHERE NULL) OVER () LIMIT FALSE, ~FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 197: `c148c3bdb12be2be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000287845`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE AS b821qtuwb ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE, 0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 198: `b02f24157b8046bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000289124`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 199: `a7e6565c5b3dcb05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000289510`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME COLLATE RTRIM); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 200: `361a8599838fad64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000289707`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE COLLATE RTRIM); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 201: `107cf5c813b83c26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000292403`

```sql
CREATE TABLE t3 (rowid FLOAT UNIQUE, c1 BOOLEAN, PRIMARY KEY (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK; ANALYZE t3; ATTACH ':memory:' AS db2;
```

---

## Crash 202: `0e39002646dc5300` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000293014`

```sql
CREATE TABLE t3 (rowid INTEGER UNIQUE, c1 BOOLEAN, PRIMARY KEY (rowid)); INSERT INTO t3 DEFAULT VALUES; CREATE INDEX idx1 ON t3 (rowid) WHERE t3.rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 203: `4e7b1d2510bedc76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000293266`

```sql
CREATE TABLE t3 (c1 BOOLEAN, PRIMARY KEY (c1) ON CONFLICT REPLACE); INSERT INTO t3 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 204: `c8d3e0a65c4b5139` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000293744`

```sql
CREATE TABLE t3 (c1 INTEGER, PRIMARY KEY (c1) ON CONFLICT REPLACE); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c1); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3,
```

---

## Crash 205: `e1152e8a5c162bcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000297077`

```sql
VALUES (count(*) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES)) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 206: `027a0d317658417b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000298109`

```sql
VALUES (FALSE) UNION VALUES (CAST(CAST(TRUE AS BLOB) AS BLOB)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 207: `a4207c9f96444dea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000298157`

```sql
VALUES (FALSE) UNION VALUES (CAST(CURRENT_DATE AS BLOB)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 208: `df930e276dbd1399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000300114`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ INTEGER REFERENCES t3 (c1) ON DELETE SET NULL, rowid INT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN TRANSACTION; DROP TAB
```

---

## Crash 209: `8cd0e600cac9a95b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000301074`

```sql
VALUES (CURRENT_TIME * 41.233426045462783E96 || CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 210: `6f73f6b9b106028f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000301311`

```sql
VALUES (CURRENT_TIME * ~41.233426045462783E96 || CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 211: `247fbef23d098460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000301355`

```sql
VALUES (CURRENT_TIME * ~NULL || CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---
