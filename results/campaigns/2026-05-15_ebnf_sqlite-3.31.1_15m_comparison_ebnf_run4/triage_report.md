# Crash Triage Report

**Total crashes:** 129  
**Unique crash sites:** 129  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 129 | 129 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `a9254fc472652352` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000090`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_); BEGIN IMMEDIATE; COMMIT TRANSACTION; WITH t2 AS MATERIALIZED (SELECT ALL CURRENT_TIME UNION VALUES (CURRENT_TIME)),
```

---

## Crash 2: `a48bb41a7519cedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001177`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 3: `4bb8552d8f2a742e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001217`

```sql
PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 4: `481a5864fc6b0269` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001702`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 5: `fa1e293143a4f0ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001708`

```sql
CREATE TEMP TABLE t2 (c1 VARCHAR(255) PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 6: `2901d621f68cc8ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001718`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, _rowid_ INTEGER, c3 REAL GENERATED ALWAYS AS (TRUE) STORED) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 7: `4df9c0f767e2cf67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001768`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 8: `47c92f64420db2f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001774`

```sql
CREATE TABLE t2 (c3 FLOAT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 9: `2c00001f4459927f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001781`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, c3 BLOB) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 10: `277a13d8dfd4e98f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001790`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, _rowid_ INTEGER, c3 REAL GENERATED ALWAYS AS (FALSE COLLATE NOCASE) STORED) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _row
```

---

## Crash 11: `3d6b79fc51c78df5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001858`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, rowid BLOB UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 12: `35640d8492e52dfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001892`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 13: `04851a2dc02a6091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001939`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 14: `029509c16a529aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001989`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c3 FLOAT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 15: `56c5639c4f939903` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005685`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, c3); PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c2); DELETE FROM t2 WHERE FALSE IS CURRE
```

---

## Crash 16: `f3a0c132a84b1ec6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005713`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL DEFAULT 2, _rowid_ BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ROLLBACK TRANSACTION; REINDEX t3
```

---

## Crash 17: `fdadbee6e53e40ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006030`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 18: `4b1e11bda166dcb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007799`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); COMMIT TRANSACTION; REINDEX;
```

---

## Crash 19: `07cba28494b7b665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012212`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 20: `4bab4713bc358fb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013211`

```sql
VALUES (CURRENT_TIME IS NULL >> CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3);
```

---

## Crash 21: `8d95602631db4903` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014498`

```sql
VALUES (CURRENT_DATE >> TRUE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 22: `85c0b16769a1f71b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014578`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 23: `2292bb17825da072` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014584`

```sql
VALUES (CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 24: `f556de12665629b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015145`

```sql
VALUES (NULL IS NOT NULL >> CURRENT_TIMESTAMP, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c3);
```

---

## Crash 25: `de318054a12dcfa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016901`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_);
```

---

## Crash 26: `3e6d0d4be79f2252` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019750`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_); WITH RECURSIVE t3 AS MATERIALIZED (WITH RECURSIVE t2 (c3, _rowid_) AS (SELECT CURRENT_TIMESTAMP),
```

---

## Crash 27: `b22a36dbaa593cae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019783`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_); WITH RECURSIVE t3 AS MATERIALIZED (WITH RECURSIVE t2 (c3, _rowid_) AS (SELECT CURRENT_TIMESTAMP), t1 AS MAT
```

---

## Crash 28: `b555b59f200c9e86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020533`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1);
```

---

## Crash 29: `de5f1d89dde8f124` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021111`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ANALYZE;
```

---

## Crash 30: `9173e71361a48229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021353`

```sql
ATTACH ':memory:' AS db2; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 31: `b73afad34538cb28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022641`

```sql
BEGIN DEFERRED; PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); DETACH db2;
```

---

## Crash 32: `8825c409515f6354` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022673`

```sql
BEGIN DEFERRED; ROLLBACK TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); DETACH db2;
```

---

## Crash 33: `00eb7bd590ebc91b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024827`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); WITH RECURSIVE t3 (_rowid_, c2, c2, c1) AS (WITH RECURSIVE t1 AS MATERIALIZED (SELECT ALL *) VALUES (NULL) ORDER BY CURRENT_
```

---

## Crash 34: `a40fa5c354941684` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025456`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 35: `4b13179f055ed04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027257`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 36: `24dd8d7a1f89ff04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030489`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, rowid BLOB UNIQUE) WITHOUT ROWID; DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE TABLE t2 (rowid BLOB NOT NULL, c1 
```

---

## Crash 37: `531573bcef4769e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034135`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL *, CURRENT_TIMESTAMP REGEXP (VALUES (CURRENT_TIME)) AS a ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST LIMIT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 38: `dae88f7a62fc82dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036232`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 INT UNIQUE, _rowid_ BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ROLLBACK TRANSACTION; REINDEX t3; PRAGMA journal
```

---

## Crash 39: `38cab8d0ffd94a24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036238`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL DEFAULT TRUE, _rowid_ BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ROLLBACK TRANSACTION; REINDEX
```

---

## Crash 40: `ec110f1e247339af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036244`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 INTEGER NOT NULL DEFAULT 2, _rowid_ VARCHAR(255) COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ROLLBACK TRANSACTION; REINDEX t3; PRAG
```

---

## Crash 41: `9e8018a895fa58d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036259`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 INT UNIQUE, _rowid_ VARCHAR(255) COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ROLLBACK TRANSACTION; REINDEX t3; PRAGMA journal_mode=
```

---

## Crash 42: `92092db94d81d667` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037886`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2, c1, c2, c2) AS SELECT DISTINCT ~CASE WHEN FALSE NOT GLOB CURRENT_TIME THEN sum(CURRENT_TIMESTAMP) WHEN FALSE NOT IN (SELECT *, * ORDER BY CURRENT_DATE NULLS FIRST) TH
```

---

## Crash 43: `71922a8c4381dce8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039293`

```sql
CREATE TABLE t2 (c1 INTEGER COLLATE NOCASE); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 44: `6e8aeeb4eb79dd3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040712`

```sql
CREATE TABLE t1 (c2 BLOB PRIMARY KEY, CHECK (CURRENT_DATE), CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_);
```

---

## Crash 45: `82663fec08943954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043585`

```sql
CREATE TABLE t1 (c2 TEXT PRIMARY KEY ASC, rowid BLOB UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 46: `0527529710023765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048203`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX;
```

---

## Crash 47: `ff29161477034584` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048538`

```sql
CREATE TABLE t3 (c2 TEXT REFERENCES t2 (_rowid_) ON UPDATE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ATTACH ':memory:' AS db2;
```

---

## Crash 48: `1352fd349f9bd8eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049791`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE TEMP TABLE t3 (_rowid_ INT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); ATTA
```

---

## Crash 49: `12d2e6d9d49a2796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051713`

```sql
CREATE TABLE t3 (_rowid_ DATE NOT NULL, UNIQUE (_rowid_) ON CONFLICT ROLLBACK); PRAGMA cache_size=+706444; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE OR REPLACE t3 SET c2 = CASE 
```

---

## Crash 50: `222e3c386238d524` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054296`

```sql
SELECT DISTINCT CURRENT_TIMESTAMP AS v22_______64___4q_v75a5__o_lq__4_s_l_8d___8___ka_j33__4___c3__8_96_o1t___fp217ckvmn__37k4___endw5__lc3e_c21m97_q3tq___70_j_2p75_95b4oj7_7__7___rf_b_o90__n_vv6364__
```

---

## Crash 51: `8f11c48da16d0294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056542`

```sql
PRAGMA journal_mode=PERSIST; PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 52: `effa9a3f31e9411b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056571`

```sql
PRAGMA quick_check; PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 53: `07d2ed89e6db3378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058510`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; SAVEPOINT sp1; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); VACUUM;
```

---

## Crash 54: `968caee925e0307e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058524`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 55: `94ca92202b041b73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058983`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 56: `64484be75683b466` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061732`

```sql
CREATE TABLE t1 (_rowid_ FLOAT UNIQUE, CHECK (CURRENT_DATE), PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ROLLBACK;
```

---

## Crash 57: `0a480a041d15066e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063294`

```sql
BEGIN DEFERRED; PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); INSERT INTO t2 (_rowid_) VALUES (CASE WHEN CAST((CURRENT_DATE, TRUE) * TRUE < FALSE NOT
```

---

## Crash 58: `de3909124edd2558` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064732`

```sql
VALUES (NULL IS NOT NULL >> CURRENT_TIMESTAMP, CASE NULL WHEN TRUE THEN CURRENT_TIMESTAMP ELSE TRUE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 59: `970686660537b187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064987`

```sql
VALUES (TRUE >> CURRENT_TIME NOT IN (CURRENT_DATE), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 60: `defdf217f56a0e8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065284`

```sql
VALUES (TRUE >> CURRENT_TIMESTAMP, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 61: `7199f6b315aac081` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065508`

```sql
VALUES (CURRENT_TIMESTAMP >> 1981424.22023870e+06039272495929179, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c3, c2);
```

---

## Crash 62: `fbefb1de5407e987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065885`

```sql
VALUES (EXISTS (VALUES (CURRENT_TIME)), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 63: `ce9fef8027e41c46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066188`

```sql
VALUES (CURRENT_DATE >> CURRENT_TIME, count(*) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 64: `544b42a37d4c6c1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066473`

```sql
VALUES (CURRENT_DATE >> 3.2768437783737006110088181997370343706953802708914421063492065407644778521632755857911235771670205226628184666377505020731735E-9903877939, CURRENT_TIME); CREATE VIRTUAL TABLE 
```

---

## Crash 65: `a150a3efe8dce362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066620`

```sql
VALUES (-09712383785208092759420439886.04911589751293418210587044282043230344727071382806217673984868700923753835484249095784303090758514446279743327110456422071057696938368858124709765681337030052622
```

---

## Crash 66: `4cff7b5b1800a097` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066989`

```sql
VALUES (CASE WHEN NULL THEN CURRENT_TIMESTAMP WHEN CURRENT_TIME THEN CURRENT_DATE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 67: `fca4239621d1001d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067275`

```sql
VALUES (CURRENT_TIME < TRUE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 68: `734111a2bd3cdc15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068557`

```sql
VALUES ((VALUES (CURRENT_TIME)) IS NULL >> CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 69: `12007bab37cb7681` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069000`

```sql
VALUES (CURRENT_TIME | FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_);
```

---

## Crash 70: `8a681906b45fbcc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070985`

```sql
VALUES (-CURRENT_TIME); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c1, c2); ALTER TABLE t1 RENAME TO t2;
```

---

## Crash 71: `506e77695134202d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072240`

```sql
VALUES (NULL >> CURRENT_TIME >= CURRENT_TIME, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 72: `52582543fb1c8699` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072578`

```sql
VALUES (FALSE IS NOT TRUE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 73: `7882594478cf79d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073104`

```sql
VALUES (~CURRENT_TIME >> CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowid_, _rowid_, c3); CREATE TRIGGER trg1 AFTER INSERT ON t2 WHEN NOT substr(~TRUE A
```

---

## Crash 74: `3a388405dc783327` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078076`

```sql
CREATE TABLE t1 AS VALUES (NULL); BEGIN IMMEDIATE TRANSACTION; ANALYZE; COMMIT TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ NUMERIC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 75: `b5830769cf9ed97c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078158`

```sql
CREATE TABLE t1 AS VALUES (NULL); BEGIN IMMEDIATE TRANSACTION; ANALYZE; COMMIT TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ NUMERIC); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(
```

---

## Crash 76: `b28e50d6b46b5de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079066`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE TABLE t3 (c3 INT COLLATE NOCASE); CREATE TEMP TABLE IF NOT EXISTS t1 (c2 INTEGER PRIMARY KEY ASC); PRAGMA int
```

---

## Crash 77: `5fd328dfcf80adfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080005`

```sql
ATTACH ':memory:' AS db2; BEGIN EXCLUSIVE; END TRANSACTION; DETACH DATABASE db2; CREATE TEMP VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 78: `ebf204b12835df7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095060`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ INT PRIMARY KEY DESC); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_); ATTACH ':memory:' AS db
```

---

## Crash 79: `6ced8625df7a7dcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095166`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ INT PRIMARY KEY DESC); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ALTER TABLE t2 RENAME COLUMN c1 TO c3;
```

---

## Crash 80: `5f196ec7270b78b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095333`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (_rowid_ INT PRIMARY KEY DESC); BEGIN IMMEDIATE; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ATTACH ':memory:' AS db2;
```

---

## Crash 81: `6bdf8ef352bd5061` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096654`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, _rowid_, rowid); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 82: `763b97d5d1089c37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097165`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 83: `4f76b8a74d6fb421` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100512`

```sql
VALUES (count(*) + count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); INSERT OR IGNORE INTO t2 VALUES (NOT CURRENT_TIMESTAMP NOTNULL -> CURRENT_TIMESTAMP == CURRENT_DATE IS N
```

---

## Crash 84: `447b969a7b90e618` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100581`

```sql
VALUES (CURRENT_DATE + count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); INSERT OR IGNORE INTO t2 VALUES (NOT CURRENT_TIMESTAMP NOTNULL -> CURRENT_TIMESTAMP == CURRENT_DATE 
```

---

## Crash 85: `69233147e03e5d79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101098`

```sql
VALUES (CURRENT_DATE NOT IN (CURRENT_DATE, TRUE, CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 86: `51ff5973adb22155` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101457`

```sql
VALUES (CURRENT_DATE NOT IN (FALSE, TRUE, CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE OR TRUE NOT NULL) UNION VALUE
```

---

## Crash 87: `260def9dacfd2341` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102287`

```sql
VALUES (TRUE LIKE FALSE ESCAPE NULL, CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3, _rowid_, c1, c2); REINDEX t3
```

---

## Crash 88: `fd46bf180351d56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105692`

```sql
VALUES (CURRENT_TIME LIKE CURRENT_DATE COLLATE BINARY, CURRENT_TIME LIKE CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT CURRENT_DATE NOT NULL, * FROM (VALUES (CURRENT_TIMESTA
```

---

## Crash 89: `fe5ee7e5f8ec0751` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107118`

```sql
VALUES (hex(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c3);
```

---

## Crash 90: `2461a462f88d91d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108301`

```sql
VALUES (CAST(CURRENT_TIME AS DATE) != CURRENT_TIMESTAMP, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c3); PRAGMA analysis_limit=--0;
```

---

## Crash 91: `39479784d92d386a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108583`

```sql
VALUES (X'e72103e93A3e', CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1);
```

---

## Crash 92: `fb492dad7f915d26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109037`

```sql
VALUES (CAST(FALSE AS DATE), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t2 SET c2 = CASE RAISE(IGNORE) WHEN CURRENT_DATE ISNULL THEN TRUE NOT GLOB CURRENT_DATE IS 
```

---

## Crash 93: `809ddb9166860c3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112863`

```sql
VALUES (CASE WHEN TRUE IS NULL THEN CURRENT_TIMESTAMP WHEN CURRENT_TIME THEN CURRENT_DATE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 94: `f3eee68fde6f0819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113490`

```sql
VALUES (CASE WHEN CURRENT_DATE IS NOT TRUE THEN CURRENT_TIMESTAMP WHEN CURRENT_TIME THEN CURRENT_DATE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1, c3, c2, c3, c1);
```

---

## Crash 95: `874a2498bfb35a7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113759`

```sql
VALUES (CASE WHEN TRUE THEN CURRENT_TIMESTAMP WHEN CURRENT_TIME THEN CURRENT_DATE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1, c3, c2, c3, c1);
```

---

## Crash 96: `3d69db40b67c6727` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114353`

```sql
VALUES (count(*), count(*) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 97: `9e244b21cf93512c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114866`

```sql
VALUES (min(CURRENT_TIMESTAMP) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 98: `a805fc6b871062a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115045`

```sql
VALUES (count(*) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GROUP), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 99: `de6b3e3596e5edb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115428`

```sql
VALUES (count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY FALSE ASC NULLS FIRST), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 100: `458a5f8948cd8fdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115711`

```sql
VALUES (count(*) OVER (), count(*) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 101: `9125c385c9e7372e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116039`

```sql
VALUES (CURRENT_TIMESTAMP >> group_concat(FALSE), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 102: `105c45abd6215e38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116140`

```sql
VALUES (CURRENT_TIMESTAMP >> total_changes(), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 103: `3093076d21ba4785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116229`

```sql
VALUES (CURRENT_TIMESTAMP >> X'2b', CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, _rowid_);
```

---

## Crash 104: `314c63be26c461a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116431`

```sql
VALUES (CURRENT_TIMESTAMP >> X'', CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 105: `92b376ed8bac9004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116603`

```sql
VALUES (CURRENT_TIMESTAMP >> -238876, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 106: `0c7b6f3538823c80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116913`

```sql
VALUES (CURRENT_TIME NOT IN (FALSE NOT IN (VALUES (CURRENT_TIMESTAMP))), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 107: `94b5c1baa44fb121` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117110`

```sql
VALUES (TRUE >> CURRENT_TIME NOT IN (CURRENT_DATE), TRUE >> CURRENT_TIME NOT IN (CURRENT_DATE), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 108: `2f6928fb1c5250ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117450`

```sql
VALUES (NULL & CURRENT_TIME NOT BETWEEN CURRENT_TIME AND CURRENT_DATE, NOT CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_);
```

---

## Crash 109: `c09b09de924ebf03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117716`

```sql
VALUES (NULL & CURRENT_TIME NOT BETWEEN CURRENT_TIME AND CURRENT_DATE, NOT ' o8 V_4   _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 110: `0bd92b878def8167` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123882`

```sql
BEGIN DEFERRED; SAVEPOINT sp1; ROLLBACK TO sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK TRANSACTION;
```

---

## Crash 111: `7837107b0ead14b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130705`

```sql
SELECT DISTINCT X'' AS q1__k3w_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 112: `61eb7291f8d447ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130802`

```sql
SELECT DISTINCT group_concat(CURRENT_TIME) AS q1__k3w_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 113: `6990f5e32a3e18f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137894`

```sql
CREATE TEMP TABLE t3 (c1 BOOLEAN UNIQUE); INSERT INTO t3 (c1) VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_);
```

---

## Crash 114: `efab20a9bed5320d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141188`

```sql
CREATE TABLE t1 (rowid BOOLEAN PRIMARY KEY, c2 INTEGER NOT NULL DEFAULT NULL) WITHOUT ROWID; BEGIN IMMEDIATE; ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 115: `771f19ae03dded82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145741`

```sql
CREATE TABLE t1 (c2 DATE PRIMARY KEY DESC, rowid BLOB UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 116: `3a3cb1ddd7164beb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145892`

```sql
CREATE TABLE t1 (c2 FLOAT PRIMARY KEY ASC, rowid BLOB UNIQUE) WITHOUT ROWID; DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 117: `b983be33396efa8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151477`

```sql
CREATE VIEW v1 AS SELECT ALL *; VACUUM; DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 118: `15219893b797b91e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152643`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 119: `301b86da3b67372a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154878`

```sql
CREATE TABLE t2 (_rowid_ DATE COLLATE NOCASE, rowid INTEGER PRIMARY KEY AUTOINCREMENT, UNIQUE (rowid), UNIQUE (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 120: `878801198bc1314b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155336`

```sql
CREATE TABLE t2 (_rowid_ NUMERIC NOT NULL REFERENCES t3 (c3) NOT DEFERRABLE INITIALLY IMMEDIATE, rowid INTEGER PRIMARY KEY AUTOINCREMENT, UNIQUE (rowid), UNIQUE (_rowid_)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 121: `05bc6764bc18e852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156297`

```sql
CREATE TABLE t2 (_rowid_ NUMERIC UNIQUE, UNIQUE (_rowid_) ON CONFLICT REPLACE, UNIQUE (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 122: `7f1340a9976e47c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160200`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BOOLEAN DEFAULT CURRENT_TIMESTAMP); CREATE TRIGGER trg1 BEFORE UPDATE ON t3 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c
```

---

## Crash 123: `21738e71eba3a4f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165765`

```sql
CREATE TABLE t3 (c2 FLOAT PRIMARY KEY ASC, _rowid_ FLOAT UNIQUE, UNIQUE (_rowid_) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE 
```

---

## Crash 124: `3c8e78ef028f3eb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165788`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 125: `1dfd741096b2bf3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165794`

```sql
BEGIN DEFERRED; CREATE TABLE t1 AS SELECT +CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 126: `612596715ee2cd99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165802`

```sql
BEGIN DEFERRED; VALUES (CURRENT_TIME LIKE X'2b', CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 127: `0c7d22636212fd1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165809`

```sql
VALUES (CURRENT_DATE NOT IN (NULL, TRUE, CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 128: `44b0e12e95570be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165832`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2); WITH t1 AS MATERIALIZED (SELECT A
```

---

## Crash 129: `a880484afcf12d6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165905`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---
