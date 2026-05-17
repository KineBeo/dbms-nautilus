# Crash Triage Report

**Total crashes:** 124  
**Unique crash sites:** 124  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 124 | 124 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `19b48551a36de08e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000052`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 2: `51f17fb158f11079` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000545`

```sql
BEGIN DEFERRED TRANSACTION; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1);
```

---

## Crash 3: `93c0f7d695552814` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001413`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2, c1);
```

---

## Crash 4: `281ac8b132fb8af3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003525`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1);
```

---

## Crash 5: `af97ed80f04c3e66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003556`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 6: `5aecca81b268065b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006068`

```sql
PRAGMA analysis_limit=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 7: `5832ea32fc6d470f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010782`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 8: `46bfd71b10a44424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011085`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 9: `06efaad6e194ebb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011468`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 10: `026495c8ac8a3517` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011739`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 11: `a4bddf10b58f1b01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012840`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 12: `6c0190f9d5eb0086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012870`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 13: `5d06814c460830b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014031`

```sql
CREATE TABLE t3 (c3 NUMERIC NOT NULL DEFAULT '', _rowid_ FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 VARCHAR(255) UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y
```

---

## Crash 14: `90b59270a2956b8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014464`

```sql
PRAGMA analysis_limit=-86451; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 15: `b02f24157b8046bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016225`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 16: `9e16f321cc73fbc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016263`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 17: `ea945e5be180f18d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016413`

```sql
PRAGMA journal_mode=PERSIST; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c3, _rowid_, c1);
```

---

## Crash 18: `7ad772b99b9f4fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016471`

```sql
PRAGMA integrity_check; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c3, _rowid_, c1);
```

---

## Crash 19: `4f88db2beade7d00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016605`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * EXCEPT SELECT ALL * FROM t3 NATURAL JOIN t3 INDEXED BY rowid , t1 NOT INDEXED LIMIT random() FILTER (WHERE CURRENT_TIME) OVER (), CURRENT_TIME; CREATE VIRT
```

---

## Crash 20: `4681e3970179a70b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016624`

```sql
CREATE TABLE t3 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 21: `be8a8686756ea5c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016652`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `0fe3f1bf40551ff6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016688`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 23: `7b2d9a7986ef023c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016729`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 24: `40595f7e234865c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016741`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE I
```

---

## Crash 25: `b4d122cc84e8db9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016761`

```sql
BEGIN DEFERRED TRANSACTION; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 26: `2f1a7516d5ecd894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017036`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 27: `7bb525eaafa7158c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018042`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 28: `9000a0eb8a23f50f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018558`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT NOT _rowid_ > CASE +CURRENT_TIMESTAMP WHEN EXISTS (SELECT DISTINCT CURRENT_TIMESTAMP) COLLATE RTRIM NOT NULL ISNULL THEN (CURRENT_TIMESTAMP, RAISE(IGNORE)) 
```

---

## Crash 29: `2993160e3f10fdd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019133`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 30: `db4ab7498d460c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019227`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 31: `23379d61052a2375` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019599`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 FLOAT PRIMARY KEY DESC, rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1);
```

---

## Crash 32: `c46460a7054d4790` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021756`

```sql
CREATE VIEW IF NOT EXISTS v1 AS WITH t3 (_rowid_, rowid, rowid, _rowid_) AS (WITH RECURSIVE t2 AS (SELECT ALL *) SELECT DISTINCT *), t1 (c1, c3, rowid) AS (SELECT * FROM t1 WHERE FALSE IS NULL GROUP B
```

---

## Crash 33: `74a116072af2d0f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021808`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 34: `00d7206d52db7761` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027548`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 35: `1232afa2770fe923` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027666`

```sql
PRAGMA foreign_keys=1; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 36: `35abd77eb7def12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027925`

```sql
CREATE TABLE t3 (c1 FLOAT PRIMARY KEY ASC); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 37: `531e2c6cc58e1436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028454`

```sql
CREATE TABLE t1 (c3 FLOAT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); DROP TABLE IF EXISTS t2;
```

---

## Crash 38: `9f47ae642fa24c3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029195`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3);
```

---

## Crash 39: `b8cd96c5d890b500` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029786`

```sql
ANALYZE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 40: `99edbfd6066fb224` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030368`

```sql
CREATE TABLE t2 AS SELECT CURRENT_DATE; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 41: `ec14d88a753c7570` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030506`

```sql
PRAGMA quick_check; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 42: `5bc191efc2a749ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030513`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 43: `3642ef1a2b4a3cf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033252`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT TRUE AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m ORDER BY CURRENT_TIMESTAMP NULLS LAST LIMIT TRUE OFFSET TRUE; CREATE VIRTUA
```

---

## Crash 44: `34e7274f7761fedd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033570`

```sql
PRAGMA wal_checkpoint(FULL); PRAGMA journal_mode=MEMORY; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ANALYZE t1; ALTER TABLE t2 ADD COLUMN c3 BOOLEAN GEN
```

---

## Crash 45: `e4255ccabe309e5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035430`

```sql
PRAGMA journal_mode=DELETE; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 46: `53f0cedd71d1e38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036276`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 47: `9e519355f0c40977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042081`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT TRUE AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m ORDER BY CURRENT_TIMESTAMP DESC LIMIT CURRENT_TIME + TRUE OFFSET TRUE; BEGI
```

---

## Crash 48: `8619b2b2b8a75239` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042406`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT TRUE AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m ORDER BY CURRENT_TIMESTAMP DESC LIMIT FALSE; BEGIN EXCLUSIVE TRANSACTION; C
```

---

## Crash 49: `07e68333a724cf20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046668`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTU
```

---

## Crash 50: `061cb83fb4ee9cad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047797`

```sql
CREATE TABLE t1 (c3 BOOLEAN, CHECK (CURRENT_TIMESTAMP NOTNULL), CHECK (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 51: `7f44268af02e7ae4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048752`

```sql
CREATE TABLE t1 (c3 BOOLEAN, CHECK (CURRENT_DATE), CHECK (TRUE IS TRUE)); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE I
```

---

## Crash 52: `9e0244697588652e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050693`

```sql
CREATE TABLE t1 (c3 FLOAT PRIMARY KEY) WITHOUT ROWID; DROP TABLE IF EXISTS t1; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TA
```

---

## Crash 53: `3f411571530cc1b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051646`

```sql
CREATE TABLE t3 (rowid FLOAT NOT NULL REFERENCES t2 (c3) ON UPDATE RESTRICT); ALTER TABLE t3 RENAME COLUMN rowid TO c1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 54: `15094aa4de749147` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053045`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); WITH RECURSIVE t3 AS MATERIALIZED (WITH RECURSIVE t1 (c2, c3, c
```

---

## Crash 55: `7d5de9c7efd72979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056018`

```sql
SELECT CURRENT_DATE LIKE TRUE - TRUE AS jz LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 56: `a688dec8b12aa745` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056381`

```sql
SELECT CASE WHEN CURRENT_DATE LIKE TRUE - NULL THEN CURRENT_DATE ELSE NULL END NOTNULL AS jz LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK TO SAVEPOINT sp1; DELETE FRO
```

---

## Crash 57: `3ddb180da422e924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057271`

```sql
BEGIN; PRAGMA foreign_keys=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 58: `c4186485a960c2ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062368`

```sql
CREATE TABLE t2 (c3 BOOLEAN PRIMARY KEY DESC, rowid FLOAT REFERENCES t2 (rowid) DEFERRABLE INITIALLY DEFERRED, UNIQUE (rowid), CHECK (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING r
```

---

## Crash 59: `08a4efd654975ff5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064151`

```sql
CREATE TABLE t1 (rowid REAL DEFAULT NULL, c3 NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 VARCHAR(255) UNIQUE, PRIMARY KEY (c1)); CREATE VI
```

---

## Crash 60: `68fc656b522fbdb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064338`

```sql
CREATE TABLE t1 (rowid REAL DEFAULT NULL, c3 NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 VARCHAR(255) UNIQUE, FOREIGN KEY (_rowid_) REFERE
```

---

## Crash 61: `4e792b3a8ae4379b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064668`

```sql
BEGIN EXCLUSIVE TRANSACTION; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2, c2);
```

---

## Crash 62: `ceed5e647525a7b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068184`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 INTEGER NOT NULL); CREATE TEMP TABLE IF NOT EXISTS t3 (c2 FLOAT PRIMARY KEY DESC, rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP); BEGIN EXCLUSIVE TRANSACTION; CR
```

---

## Crash 63: `6fcc695abdcfb654` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068350`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 INTEGER NOT NULL); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 TEXT COLLATE NOCASE); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtre
```

---

## Crash 64: `fcea4deec49a0da4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075622`

```sql
CREATE TABLE t3 (c3 NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 VARCHAR(255) UNIQUE); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 65: `1903821eb2a6c3c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082480`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; ALTER TABLE t3 RENAME COLUMN rowid TO c1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2); PRAGMA synchronous
```

---

## Crash 66: `9d4500f130182e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082646`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; ALTER TABLE t3 ADD COLUMN c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 67: `ebb8d247423fe86a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082652`

```sql
CREATE TABLE t3 (rowid REAL DEFAULT -21344350.69119735826333e233299286992117885393165349683303560); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y
```

---

## Crash 68: `1e0db4c5145840ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082660`

```sql
CREATE TABLE t3 (_rowid_ REAL NOT NULL REFERENCES t3 (c1) NOT DEFERRABLE INITIALLY IMMEDIATE); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); C
```

---

## Crash 69: `b02888fec709dbab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082669`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; CREATE TABLE t1 (c1 REAL NOT NULL DEFAULT 0, CHECK (CURRENT_TIMESTAMP NOTNULL), CHECK (CURRENT_DATE)); CREATE VIRTUAL TABLE IF
```

---

## Crash 70: `9fbbfbde40b0794c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082679`

```sql
CREATE TABLE t3 (rowid NUMERIC REFERENCES t1 (_rowid_) ON DELETE NO ACTION); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABL
```

---

## Crash 71: `3b0cf04059ec907b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082688`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); INSERT INTO t3 VALUES (FALSE), (CURRENT_DATE), (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTU
```

---

## Crash 72: `c08a524fbcf9f96d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082700`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 73: `fe13709b7cead786` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082738`

```sql
CREATE TABLE t3 (c1 FLOAT REFERENCES t3 (_rowid_) MATCH c2); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 74: `1c936f898606a7aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082747`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, rowid); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 75: `70540c2561d8431d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082761`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); ANALYZE t3; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 76: `eff992e2c4fa2de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082785`

```sql
CREATE TABLE t3 (c2 TEXT NOT NULL REFERENCES t1 (rowid) ON UPDATE SET NULL); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABL
```

---

## Crash 77: `02ebbeab5bc41408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082822`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 78: `b1d306b00fbd0e83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083201`

```sql
ATTACH DATABASE ':memory:' AS db2; BEGIN DEFERRED TRANSACTION; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 79: `a2dc51f5d804dc8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084670`

```sql
ATTACH ':memory:' AS db2; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); PRAGMA integrity_check;
```

---

## Crash 80: `99bbb14f9f1889d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085131`

```sql
BEGIN IMMEDIATE TRANSACTION; PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c3);
```

---

## Crash 81: `d04aa67b572d353c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085218`

```sql
BEGIN IMMEDIATE TRANSACTION; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c3);
```

---

## Crash 82: `9bc9dee7a063d60a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085696`

```sql
CREATE TABLE t1 AS VALUES (CURRENT_TIME); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH t1 AS MATERIALIZED (WITH t2 AS MATERIALIZED (SELECT ALL t2.* EXCEPT SE
```

---

## Crash 83: `76e0b7e356882c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091564`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 NUMERIC NOT NULL REFERENCES t1 (c1) ON DELETE SET DEFAULT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 84: `d83f779eea58c9cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094370`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW v1 AS SELECT DISTINCT FALSE LIKE RAISE(IGNORE) ESCAPE TRUE BETWEEN RAISE(IGNORE) IS NOT NULL | CURRENT_TI
```

---

## Crash 85: `b43e2989dd5899b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099553`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ DATE PRIMARY KEY DESC); INSERT INTO t3 VALUES (FALSE), (CURRENT_DATE), (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3,
```

---

## Crash 86: `c33bf9f58a51183f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099909`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid DATE UNIQUE); INSERT INTO t3 VALUES (FALSE), (CURRENT_DATE), (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REINDEX; PRAGMA in
```

---

## Crash 87: `9d9666d3375537f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099938`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid DATE UNIQUE); INSERT INTO t3 VALUES (FALSE), (CURRENT_DATE), (CURRENT_TIMESTAMP); ATTACH ':memory:' AS db2; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 88: `f1949cbeee83d9f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100304`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid DATE UNIQUE); INSERT INTO t3 VALUES (FALSE), (CURRENT_DATE), (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 89: `e92f87ec61e9f6e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101160`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 BOOLEAN PRIMARY KEY DESC, _rowid_ VARCHAR(255) COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 90: `32539c60eef2eaaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101624`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 BOOLEAN PRIMARY KEY DESC, _rowid_ VARCHAR(255) COLLATE NOCASE); INSERT INTO t3 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 91: `1ffc9b8ab4a11c4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103198`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); CREATE TRIGGER trg1 AFTER UPDATE OF c1 ON t3 BEGIN DELETE FROM t1; END; DELETE FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 92: `4eaa0f09083c347e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104172`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TRIGGER trg1 AFTER INSERT ON t2 WHEN NULL IS DISTINCT FROM RAISE(IGNORE) COLLATE BINARY LIKE NULL 
```

---

## Crash 93: `a849cbd192aa9cef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104283`

```sql
BEGIN EXCLUSIVE TRANSACTION; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 94: `b388bf8126d50325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104560`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS a ORDER BY CURRENT_DATE NOT IN (SELECT ALL TRUE AS hk__0_956_ir9__3_) ASC NULLS LAST; CREATE VIRTUAL TABL
```

---

## Crash 95: `27c87e42f3f8ecda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104586`

```sql
CREATE TABLE t3 (c2 VARCHAR(255) NOT NULL REFERENCES t3 (c3) ON UPDATE CASCADE); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL 
```

---

## Crash 96: `798f35ccdee55554` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104603`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM t3 NOT INDEXED GROUP BY TRUE ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE OFFSET TRUE; BEGIN EXCLUSIVE TRANSACTION; CREATE V
```

---

## Crash 97: `76a2a2ce865cc415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104610`

```sql
CREATE TABLE t3 (rowid NUMERIC PRIMARY KEY); BEGIN EXCLUSIVE TRANSACTION; WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT TRUE AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m O
```

---

## Crash 98: `f78275bbb6ff5d3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104675`

```sql
CREATE TABLE t3 (c3 TEXT DEFAULT TRUE); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 99: `a28009d1eddc9982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106813`

```sql
CREATE TABLE t1 (rowid TEXT UNIQUE, _rowid_ NUMERIC PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 100: `17cc0a0f7f00dd1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107533`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 NOT INDEXED WHERE (SELECT * FROM t1 NOT INDEXED GROUP BY NULL HAVING RAISE(IGNORE)) ORDER BY CURRENT_TIMESTAMP NULLS FIRST; CREATE VIRTUAL TABLE I
```

---

## Crash 101: `21bf3221eeeea6f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107907`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 102: `b1eb6f8bf79bf9db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108600`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 103: `fa6a9636246c267c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111216`

```sql
SELECT DISTINCT TRUE ORDER BY CAST(RAISE(IGNORE) AS FLOAT) NULLS LAST, RAISE(IGNORE) LIMIT TRUE NOT BETWEEN FALSE AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 104: `e077d25341af1e59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111395`

```sql
CREATE TABLE t2 AS SELECT DISTINCT * FROM (VALUES (CURRENT_TIME)) AS a ORDER BY TRUE ASC NULLS FIRST LIMIT -CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 105: `703e5d56673f3012` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122464`

```sql
CREATE TABLE t2 (rowid REAL DEFAULT NULL, c2 BLOB PRIMARY KEY DESC); DROP TABLE t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 106: `ac3041d49a5bdd04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122613`

```sql
CREATE TABLE t2 (rowid REAL DEFAULT NULL, c2 BLOB PRIMARY KEY DESC); CREATE INDEX idx1 ON t2 (c2, rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c2); BEGIN IMMEDIATE TRANSACTION;
```

---

## Crash 107: `593faebba2e9f8e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124151`

```sql
CREATE TABLE t2 (rowid TEXT UNIQUE, c2 BLOB PRIMARY KEY DESC) WITHOUT ROWID; CREATE INDEX IF NOT EXISTS idx1 ON t2 (rowid); BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING
```

---

## Crash 108: `b668d24a092f54cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124447`

```sql
CREATE TABLE t2 (_rowid_ BLOB GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c2 BLOB PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 109: `b2a01489e2550b58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126657`

```sql
VALUES (group_concat(CURRENT_TIME, '-_iC-k- z0__2y') FILTER (WHERE CURRENT_TIMESTAMP) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 110: `f1dac9a3febf2c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127755`

```sql
SELECT * FROM (VALUES (X'CACFAA')) AS a GROUP BY CURRENT_DATE WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_, c2, c1); END; CREATE INDEX IF NOT EXISTS idx1 ON t3
```

---

## Crash 111: `918ebeeee83edcd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134485`

```sql
SELECT * FROM (SELECT * FROM (SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a WHERE TRUE) AS a WHERE TRUE) AS a WHERE TRUE UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 112: `37b85ba22a80d673` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134515`

```sql
SELECT * FROM (SELECT * FROM (VALUES (FALSE)) AS a WHERE TRUE) AS a WHERE TRUE UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 113: `913d4381f63bb91d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135859`

```sql
SELECT DISTINCT CURRENT_TIME UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TABLE t3 AS WITH RECURSIVE t3 AS NOT MATERIALIZED (SELECT ALL *), t1 AS M
```

---

## Crash 114: `6efb652f2e80d099` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136060`

```sql
VALUES (-5.312569e-9641) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 115: `220920f958435921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141266`

```sql
SELECT CASE WHEN NOT EXISTS (VALUES (CURRENT_DATE)) LIKE NULL THEN CURRENT_DATE ELSE NULL END AS jz LIMIT TRUE; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x
```

---

## Crash 116: `04a1a9a325a15ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141437`

```sql
SELECT CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_DATE ELSE NULL END AS jz LIMIT TRUE; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRT
```

---

## Crash 117: `5e5f2f5e314500cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144151`

```sql
SELECT TRUE BETWEEN CURRENT_TIMESTAMP AND NULL AS jz LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_);
```

---

## Crash 118: `ed148915116a9a24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148672`

```sql
CREATE TABLE t3 (c1 FLOAT PRIMARY KEY ASC); CREATE TABLE IF NOT EXISTS t3 (c1 NUMERIC UNIQUE, rowid FLOAT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREAT
```

---

## Crash 119: `2400ab81454dd157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152562`

```sql
CREATE TABLE t1 (c3 BOOLEAN PRIMARY KEY DESC, c2 VARCHAR(255) UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); END TRANSACTION;
```

---

## Crash 120: `bde56ad1068a2294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155075`

```sql
CREATE TABLE t1 (c3 BOOLEAN, UNIQUE (c3) ON CONFLICT REPLACE, CHECK (RAISE(IGNORE) IS FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); CREATE TABLE t1 (c3 FLOAT CHECK (RAISE(IGNO
```

---

## Crash 121: `ef4b8f5aa0b60ef9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156406`

```sql
CREATE TABLE t1 (c3 BOOLEAN, CHECK (FALSE NOT IN (CURRENT_TIME)), CHECK (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 122: `54027edf3dd31be5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160067`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY ASC) WITHOUT ROWID; INSERT INTO t3 VALUES (FALSE), (CURRENT_TIME), (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 123: `d2fdbdfae5c5b45c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165251`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT TRUE AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m ORDER BY CURRENT_TIMESTAMP DESC LIMIT CAST(FALSE AS INTEGER) OFFSET TRUE; C
```

---

## Crash 124: `a5518f52eee5fcf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174232`

```sql
WITH t3 AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT min(NULL) OVER () AS u_36073y7__4__74fx6___4j1qz8a___f_m_h7_mn_1_m ORDER BY CURRENT_TIMESTAMP NULLS LAST LIMIT FALSE; CREATE VIRT
```

---
