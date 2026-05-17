# Crash Triage Report

**Total crashes:** 113  
**Unique crash sites:** 113  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 113 | 113 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `20b0546387bde50a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c3);
```

---

## Crash 2: `a273eb5621a195d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000418`

```sql
PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c2);
```

---

## Crash 3: `1fec33bbec2f3d27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000518`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK;
```

---

## Crash 4: `4c1b43dd1adc79a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001072`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX t2;
```

---

## Crash 5: `b6193a2ee09dfdca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001331`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT t1.* FROM t2 NOT INDEXED WHERE FALSE NOTNULL LIKE (CURRENT_DATE, RAISE(IGNORE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 6: `26942ea38721b152` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001405`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_);
```

---

## Crash 7: `0984aa82475f120a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002192`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX t2;
```

---

## Crash 8: `6c9469ffcd028772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002198`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX t2;
```

---

## Crash 9: `253b051f2adfb844` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002693`

```sql
CREATE TABLE t2 (_rowid_ FLOAT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 10: `f83d2286fa8a7173` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003100`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK;
```

---

## Crash 11: `274587de0e1f3ef0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003216`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c2);
```

---

## Crash 12: `bf1ab13a36b1116e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007477`

```sql
CREATE VIEW v1 AS VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ALTER TABLE t3 RENAME TO t1; WITH RECURSIVE t1 AS MATERIALIZED (SELECT t3.*), t2 (rowid) AS (SELECT N
```

---

## Crash 13: `53f0cedd71d1e38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008460`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 14: `8a46aaa48fdad2f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011144`

```sql
VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 15: `ef38654b38194f0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014220`

```sql
CREATE TABLE t2 (c2 INTEGER PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 16: `0f441b07dceac0ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014608`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INT CHECK (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 17: `1cd74122dbf47cb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015097`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1);
```

---

## Crash 18: `d48482894ccc73b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015994`

```sql
BEGIN TRANSACTION; COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 19: `8c2fb7fd7bf53c20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017351`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 20: `5e0a1c88418e0c51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018820`

```sql
ATTACH ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DETACH DATABASE db2; VACUUM; DROP TABLE IF EXISTS t1; PRAGMA analysis_limit=+0;
```

---

## Crash 21: `907bf6a8990925e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019290`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 22: `beaf66d56bc5b291` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019366`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 23: `dbbdcd9180f59325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019593`

```sql
CREATE TABLE t3 (c1 FLOAT COLLATE NOCASE, UNIQUE (c1) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c3);
```

---

## Crash 24: `ad9288cb1c28206c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020205`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 25: `3a7d282f5d9fc041` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025278`

```sql
CREATE TABLE t2 (c1 INTEGER DEFAULT CURRENT_DATE, c3 NUMERIC UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2);
```

---

## Crash 26: `919cfda609e60082` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026708`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 27: `ede39a79f6093a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027151`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TRIGGER trg1 AFTER INSERT ON t2 WHEN changes() OVER (PARTITION BY FALSE ORDER BY RAISE(IGNORE) >= FALSE DESC
```

---

## Crash 28: `beb3c2a877cf3e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028791`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY DESC, c3 FLOAT UNIQUE, c2 REAL UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, _rowid_, c2);
```

---

## Crash 29: `03c9da7724be11ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028912`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 30: `bf667d16b6e33fdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032443`

```sql
PRAGMA analysis_limit=-7474; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 31: `17adc0c1d2b401c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033833`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY DESC, c1 NUMERIC COLLATE NOCASE) WITHOUT ROWID; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 32: `e520014bff4c84e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035015`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); ATTACH ':memory:' AS db2; ROL
```

---

## Crash 33: `5a9e4525020ef1a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035627`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK;
```

---

## Crash 34: `c019c2097c9be0c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037808`

```sql
CREATE TABLE t2 (c1 TEXT PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); DETACH db2;
```

---

## Crash 35: `215678e96023dc38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037840`

```sql
CREATE TABLE t2 (c1 TEXT PRIMARY KEY ASC); DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 36: `c598aa70bb026248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039674`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid REAL NOT NULL DEFAULT FALSE, c2 INTEGER); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 37: `46a317091dc39a67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039825`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid REAL NOT NULL DEFAULT 0, _rowid_ REAL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 38: `aed52618ca04d884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045444`

```sql
VALUES (1228355657.5212980226983477911986255950823199433209114971552224884663953675449344662838473166362967267175490114508003976541184539855982104957115835263270640612626009402262328272648262230205180
```

---

## Crash 39: `13819bdcd058d6fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047403`

```sql
CREATE TABLE t3 (c1 BLOB PRIMARY KEY DESC, UNIQUE (c1) ON CONFLICT REPLACE); ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); UPDATE t2 SET c2
```

---

## Crash 40: `8b316fe02bd35e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048710`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 NUMERIC REFERENCES t2 (c1) ON UPDATE SET NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT;
```

---

## Crash 41: `12f7dbce81cb4c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051760`

```sql
PRAGMA foreign_keys=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 42: `4d79b7771c989647` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053299`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL PRIMARY KEY); REPLACE INTO t3 VALUES (TRUE); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 43: `d5e7f62e8d512a6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054742`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INT CHECK (CURRENT_TIME)); REPLACE INTO t3 VALUES (TRUE); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 44: `f418569dedb52324` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055363`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid TEXT UNIQUE); REPLACE INTO t3 VALUES (TRUE); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 45: `86d0ff3f1b8651d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055369`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 INT PRIMARY KEY DESC); REPLACE INTO t3 VALUES (TRUE); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 46: `31206a511a718dae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055607`

```sql
CREATE TABLE t2 AS VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 47: `7ae759ee21a5a862` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057080`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c3);
```

---

## Crash 48: `e6b031f3d471b399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058101`

```sql
VALUES (X'fb'); PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); UPDATE t3 SET _rowid_ = CASE WHEN CASE CURRENT_DATE WHEN rowid THEN NULL END THEN +CURRENT_TIME COLLA
```

---

## Crash 49: `ce4ebc288f070b32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059425`

```sql
VALUES (CURRENT_TIME NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); VACUUM;
```

---

## Crash 50: `091a0d67b31435b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061276`

```sql
VALUES (23.00935168250772, NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c1, c3); ANALYZE t3; CREATE INDEX idx1 ON t2 (c2, c1); CREATE VIEW v1 (_rowid_, _rowid_, c3, c3, rowi
```

---

## Crash 51: `ba9f47fdfa4340b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062782`

```sql
VALUES (CASE CURRENT_TIME WHEN CURRENT_DATE THEN TRUE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); ANALYZE t2; INSERT INTO t2 VALUES (c3) RETURNING json_array(CASE WHEN NULL <= 
```

---

## Crash 52: `d6e76c2b0e7baec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065889`

```sql
VALUES (CASE WHEN count(*) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST, CURRENT_DATE ASC) THEN NULL WHEN NULL THEN CURRENT_DATE ELSE NULL END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 53: `b3a724f8aa450905` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066204`

```sql
WITH RECURSIVE t2 AS (VALUES (FALSE)) VALUES (TRUE / CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 54: `22733c89360eb15a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066293`

```sql
WITH RECURSIVE t2 AS (VALUES (FALSE)) VALUES (TRUE) INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 55: `b2653ce075447bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066299`

```sql
WITH RECURSIVE t2 AS (VALUES (FALSE)) VALUES (NULL) INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 56: `68aed3bc8e5e92a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068527`

```sql
WITH RECURSIVE t2 (c3) AS (VALUES (TRUE)), t3 AS (SELECT *) VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); CREATE TRIGGER trg1 INS
```

---

## Crash 57: `a75c355e011c266d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068595`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN UPDATE t3 SET _rowid_ = EXISTS (WITH t1 AS MATERIALIZED (SELECT DISTINCT t3.*) 
```

---

## Crash 58: `f47a6333d931318b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069981`

```sql
WITH t2 AS (VALUES (CURRENT_DATE)) SELECT TRUE ORDER BY RAISE(IGNORE) ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ALTER TABLE t1 RENAME COLUMN c3 TO c1; UPDATE t2 SET ro
```

---

## Crash 59: `609ae96684d5a102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071557`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid TEXT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1, c3);
```

---

## Crash 60: `048e20a85c4ed704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072389`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 BLOB DEFAULT -7828082058296.001151E-992790866506672231981, c3 REAL PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, _rowid_); ALTER TA
```

---

## Crash 61: `56ece96a0a9f73f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072888`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 INT UNIQUE); PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c2, c1);
```

---

## Crash 62: `cd4503067fa5efb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073955`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid INT PRIMARY KEY ASC); CREATE TEMP TABLE t1 (_rowid_ TEXT PRIMARY KEY ASC); BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(i
```

---

## Crash 63: `a7c3df370fd417a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079284`

```sql
CREATE TABLE t3 (_rowid_ DATE PRIMARY KEY DESC) WITHOUT ROWID; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ANALYZE t1; DELETE FROM t1;
```

---

## Crash 64: `2fb29714127a65fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081286`

```sql
WITH RECURSIVE t1 AS (SELECT *) SELECT DISTINCT CURRENT_DATE != CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(rowid, _row
```

---

## Crash 65: `a7350cea2cd6fcd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082829`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c1, _rowid_, c1);
```

---

## Crash 66: `04d2c02596e3c9a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082917`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DELETE FROM t2 WHERE FALSE MATCH RAISE(IGNORE) NOT NULL || CURRENT_TIMESTAMP * CURRENT_TIMESTAMP IS NULL NOT IN 
```

---

## Crash 67: `2dbad333d19725c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083262`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3, _rowid_, c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 68: `e0c7ca18117dc276` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084833`

```sql
WITH RECURSIVE t1 AS (SELECT *) SELECT DISTINCT 700934994781838.53e+5; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2, c3, c2, c3);
```

---

## Crash 69: `ec67d1c2091cb73c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085810`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL); PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t2 AS (WITH t1 AS MATERIALIZED (SE
```

---

## Crash 70: `12eaad1ab9063d72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089208`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL); REPLACE INTO t3 VALUES (CURRENT_TIME COLLATE BINARY >= FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_)
```

---

## Crash 71: `af6939a67dd4c05e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089389`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL); REPLACE INTO t3 VALUES (CAST(CURRENT_DATE AS INTEGER) >= CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, 
```

---

## Crash 72: `c5d2a9c6a551ed3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091043`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (_rowid_);
```

---

## Crash 73: `6b04c968805edab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093724`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ INT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, rowid REAL PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3);
```

---

## Crash 74: `a66339aeec9cef2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096581`

```sql
CREATE VIEW IF NOT EXISTS v1 (rowid, rowid) AS SELECT * FROM t2 GROUP BY CURRENT_DATE WINDOW w1 AS () LIMIT TRUE REGEXP CURRENT_DATE OFFSET TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 75: `03434b4da56fe9a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098168`

```sql
WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)) SELECT * FROM t2 NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 76: `24b87f5fd207c21c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098961`

```sql
WITH RECURSIVE t2 (c3) AS (SELECT _rowid_ AS a FROM (VALUES (CURRENT_DATE)) AS a WHERE NULL GROUP BY FALSE WINDOW w1 AS ()), t3 AS (SELECT *) VALUES (FALSE) INTERSECT SELECT * FROM t2 NOT INDEXED NATU
```

---

## Crash 77: `af6415d6526d9f7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099059`

```sql
WITH RECURSIVE t2 (c3) AS (VALUES (CURRENT_TIMESTAMP)), t3 AS (SELECT *) VALUES (FALSE) INTERSECT SELECT * FROM t2 NOT INDEXED NATURAL LEFT OUTER JOIN t2 NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 78: `d68f1066478a0cc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099066`

```sql
WITH RECURSIVE t2 (c3) AS (SELECT * FROM (VALUES (CURRENT_DATE)) AS a WHERE NULL GROUP BY FALSE WINDOW w1 AS ()), t3 AS (SELECT *) VALUES (FALSE) INTERSECT SELECT * FROM t2 NOT INDEXED NATURAL LEFT OU
```

---

## Crash 79: `ce92fefe9ed2bde2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099073`

```sql
WITH RECURSIVE t2 (c3) AS (SELECT CURRENT_DATE AS a FROM (VALUES (CURRENT_DATE)) AS a WHERE NULL GROUP BY FALSE WINDOW w1 AS ()), t3 AS (SELECT *) VALUES (FALSE) INTERSECT SELECT * FROM t2 NOT INDEXED
```

---

## Crash 80: `fcea37f57e267840` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104530`

```sql
WITH RECURSIVE t3 AS (SELECT *) VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 81: `0b83225360fd0d8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106086`

```sql
WITH RECURSIVE t2 AS (VALUES (23.00935168250772, NULL)) SELECT * FROM t2 INTERSECT SELECT * FROM t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK TRANSACTION;
```

---

## Crash 82: `cee957c422d99a41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110572`

```sql
VALUES (substr(CURRENT_TIME, CURRENT_TIMESTAMP, TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 83: `5249fec7863a205e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110698`

```sql
VALUES (CAST(CURRENT_TIMESTAMP ISNULL AS REAL) >> random() NOTNULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 84: `57e0fa7d32a029cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111555`

```sql
VALUES (X'fBd2'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c3);
```

---

## Crash 85: `71629dc6ed5024f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111915`

```sql
VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REINDEX t3; VACUUM INTO ':memory:'; REINDEX t1; BEGIN IMMEDIATE TRANSACTION; 
```

---

## Crash 86: `d74146b50067346c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112418`

```sql
SELECT ALL count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY TRUE, CURRENT_TIME) AS at__2m_2ky2__3_1b_209_ti7_mp04im43_8_7_0b7n7__bwb3nw5_s__85_t5er2c0__0sg_0h37q_82tb_j_1yz__xikv_724_qp1n_
```

---

## Crash 87: `56f11d26416d72ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114155`

```sql
VALUES (count(*) FILTER (WHERE TRUE) OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_
```

---

## Crash 88: `2f936f1f0d1d592e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114188`

```sql
VALUES (count(*) FILTER (WHERE TRUE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ROLLBACK; ALTER TABLE t2 DROP COLUMN c3; PRAGMA journal_mode=DELETE;
```

---

## Crash 89: `009e2a53bfc2307e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115438`

```sql
VALUES (0684932291.98e5); CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL t3.* FROM t1 NOT INDEXED , (t3 INDEXED BY rowid) USING (rowid) ORDER BY FALSE DESC NULLS FIRST, NOT TRUE BETWEEN RAISE(IGNORE)
```

---

## Crash 90: `b83c12fd17d3ad04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115605`

```sql
VALUES (805.31785257543299590030230977332655559709648153888732238684194291760594518459298560767803026373886637025071719524410715840892637787991011610310409699078556085134823639869880234817279715351738
```

---

## Crash 91: `c119578d20fedcef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116040`

```sql
VALUES (json(FALSE)); ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); BEGIN;
```

---

## Crash 92: `9d874f37674fccc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116101`

```sql
VALUES (random()); ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); BEGIN;
```

---

## Crash 93: `d5ad378bb314c55f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118192`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); REINDEX t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 94: `72bd7045f725ed7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120659`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL); INSERT INTO t3 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 95: `5a69a1db0e7ee9ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122497`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL PRIMARY KEY); REPLACE INTO t3 VALUES (TRUE); REPLACE INTO t3 VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c3);
```

---

## Crash 96: `f9211816b53f2db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122916`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INTEGER NOT NULL DEFAULT CURRENT_DATE); REPLACE INTO t3 VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 97: `4b38476500ed737c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122993`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL NOT NULL); REPLACE INTO t3 VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 98: `a52e01ddddaffc22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123000`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INTEGER NOT NULL DEFAULT CURRENT_DATE); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 99: `056f2f06a7f59a33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124900`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL PRIMARY KEY); INSERT INTO t3 DEFAULT VALUES; REPLACE INTO t3 VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); REINDEX; B
```

---

## Crash 100: `3bd3312143c70096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126826`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA cache_size=-0; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 101: `4f9641f15a2a3c28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126885`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); PRAGMA optimize; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 102: `67061d68604cb1f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133252`

```sql
CREATE TABLE t3 (c1 FLOAT COLLATE NOCASE, CHECK (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 103: `b03b72902c22b6ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133542`

```sql
CREATE TABLE t3 (c1 FLOAT COLLATE NOCASE, UNIQUE (c1) ON CONFLICT FAIL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1, _rowid_, c2);
```

---

## Crash 104: `361f4cf8c532f40c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135592`

```sql
CREATE TABLE t3 (c1 INTEGER DEFAULT CURRENT_DATE, _rowid_ BLOB UNIQUE, PRIMARY KEY (c1)); UPDATE t3 SET _rowid_ = CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIEW v1
```

---

## Crash 105: `40cb0ec9fee85d26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136346`

```sql
VALUES (X'd58C0cAE'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 106: `3db3cc5af10a1d74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136891`

```sql
SELECT ALL count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY TRUE, CURRENT_TIME) AS at__2m_2ky2__3_1b_209_ti7_mp04im43_8_7_0b7n7__bwb3nw5_s__85_t5er2c0__0sg_0h37q_82tb_j_1yz__xikv_724_qp1n_
```

---

## Crash 107: `ce9da142f3026c76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137735`

```sql
SELECT ALL max(NULL) FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS at__2m_2ky2__3_1b_209_ti7_mp04im43_8_7_0b7n7__bwb3nw5_s__85_t5er2c0__0sg_0h37q_82tb_j_1yz__xikv_724_qp1n_88_dw_a3_z340_kfzeg_7c_ LIMIT 
```

---

## Crash 108: `0104f27998c3e291` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138067`

```sql
SELECT ALL count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS at__2m_2ky2__3_1b_209_ti7_mp04im43_8_7_0b7n7__bwb3nw5_s__85_t5er2c0__0sg_0h37q_82tb_j_1yz__xikv_724_qp1n_88_dw_a3_z340_kfzeg_7c_ LIMIT -
```

---

## Crash 109: `fe4f6a0633907763` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150281`

```sql
CREATE TABLE t2 (rowid INTEGER PRIMARY KEY DESC, CHECK (RAISE(IGNORE) IS NULL COLLATE BINARY)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c1);
```

---

## Crash 110: `159a3abb1c086f09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160438`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t1 (rowid) AS NOT 
```

---

## Crash 111: `dbc925e7909c7341` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161172`

```sql
CREATE TABLE t3 (c1 INTEGER DEFAULT CURRENT_DATE, _rowid_ BLOB UNIQUE, UNIQUE (c1) ON CONFLICT REPLACE, UNIQUE (c1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 112: `3ac2d2c9cb9546d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162729`

```sql
CREATE TABLE t3 (c1 NUMERIC PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 113: `b2238810dfbb980b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170309`

```sql
VALUES (TRUE) UNION SELECT ALL TRUE ORDER BY TRUE DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---
