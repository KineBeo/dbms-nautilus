# Crash Triage Report

**Total crashes:** 134  
**Unique crash sites:** 134  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 134 | 134 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `01210571f7b64ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000100`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 2: `71427f3a4fb11d65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000331`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 3: `1b18edde53857f45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000359`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c2);
```

---

## Crash 4: `fdc202b1bd904dc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000540`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); PRAGMA foreign_keys=OFF;
```

---

## Crash 5: `8f789fca86003974` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000952`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2, c2, c3);
```

---

## Crash 6: `e0960172dbf24b52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005189`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 7: `1fc3b021bbf45ed6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005773`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 8: `12deac40bfd1606b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006252`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE INDEX idx1 ON t1 (c1) WHERE CASE CURRENT_TIME NOTNULL + NOT FALSE IS NOT CURRENT_TIME * CURRENT_TIME IS NU
```

---

## Crash 9: `952613cc44535103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006421`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DROP TABLE t2;
```

---

## Crash 10: `fc0166397b80c8f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007980`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, c1, c2, _rowid_, c1, c1, c1, _rowid_);
```

---

## Crash 11: `80e9ae50d0951436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008887`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 12: `ded2a967225313e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008911`

```sql
SELECT count(DISTINCT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 13: `7cf5c77cd7c8dc63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008938`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `b02f24157b8046bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008956`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 15: `92f816f7daf58f0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008963`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 16: `e21d206188fd41da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008986`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 17: `04b06c358ea7ada8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009001`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 18: `1dd2fe2cd7da113c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009516`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 BLOB PRIMARY KEY ASC) WITHOUT ROWID; PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); UPDATE t3 SET rowid = TRUE NOTNULL REGEXP 'S6  
```

---

## Crash 19: `28749780a529fa79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009607`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 BLOB PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 20: `0bf4afff4749e22b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009613`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 BLOB PRIMARY KEY ASC) WITHOUT ROWID; PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); UPDATE t3 SET rowid = TRUE NOTNULL REGEXP 'S6  ' NOT G
```

---

## Crash 21: `ae1f0fedb60ce921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011681`

```sql
CREATE TABLE t3 (rowid DATE PRIMARY KEY ASC, c3 BLOB UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 22: `03c90da5cfe3a051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013646`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 23: `4f2a191bb7fbb161` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013655`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 24: `61f71af373e9e0c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013662`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 25: `1f0c616aee73480c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013773`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 26: `384fc4cbbeaa0848` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013804`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 27: `539ded89ce3d17ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015248`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 28: `6e59a0beeb636393` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016497`

```sql
CREATE VIEW v1 AS SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) UNION ALL SELECT ALL * LIMIT TRUE; CREATE VIRT
```

---

## Crash 29: `cec6101a0e09f7e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020646`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); DROP VIEW IF EXISTS v1;
```

---

## Crash 30: `e51253d32785219a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022406`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 31: `3c2648c63e39a7cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024574`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid REAL PRIMARY KEY); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 32: `5ac906edb15a5cb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024985`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP <= CURRENT_DATE COLLATE RTRIM); CREATE VIRTUAL TAB
```

---

## Crash 33: `0c97cd732cdae072` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025029`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 34: `6882a3ea2299e10d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025037`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 35: `ba56db0585147495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025043`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 36: `6bf77466d84a5c69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025049`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, TRUE COLLATE RTRIM); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 37: `fb5085e81aac238b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025175`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, TRUE OR TRUE <= CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 38: `096c0166f8cb7c68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025555`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 39: `2726ea24ce9cdfc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025831`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, TRUE OR TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 40: `5703f118c8bc1eae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026357`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP <= CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 41: `a34fe05f94cb1043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026861`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (FALSE IS NOT NULL, NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_)
```

---

## Crash 42: `6eb3179fa1f17e7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032019`

```sql
PRAGMA analysis_limit=+0; PRAGMA analysis_limit=0; BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 43: `7794aab400e0fab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032068`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 44: `c5b8097509815af6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035998`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY); ALTER TABLE t3 RENAME TO t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 45: `8cc32af5e848b1fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036861`

```sql
CREATE TABLE t3 AS VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1, c3); CREATE TRIGGER trg1 AFTER INSERT ON t3 BEGIN DELETE FROM t2; END;
```

---

## Crash 46: `32ca0a67dabce863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039161`

```sql
DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowid_);
```

---

## Crash 47: `644de124fbd2743d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039221`

```sql
ATTACH DATABASE ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT DISTINCT NULL ISNULL NOT GLOB CASE TRUE << NOT CURRENT_TIMESTAMP COLLATE BINARY
```

---

## Crash 48: `439a6600454d9c8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041375`

```sql
SELECT DISTINCT TRUE ORDER BY RAISE(IGNORE) NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 49: `57d8d5ed9f549779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041810`

```sql
CREATE TABLE t3 AS SELECT ALL CURRENT_DATE OR CAST(TRUE AS NUMERIC) AS u041; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 50: `6224aaa5b3d46728` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045388`

```sql
CREATE TABLE t3 AS SELECT DISTINCT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1);
```

---

## Crash 51: `c6505154662cb473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045556`

```sql
CREATE TABLE t3 AS SELECT DISTINCT 8574155896280451992038938995065611662994119467971164998760691623466573756.0e-4160; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2);
```

---

## Crash 52: `2b3ba413faf4bcc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046381`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 INTEGER NOT NULL REFERENCES t3 (_rowid_) ON DELETE CASCADE ON UPDATE CASCADE, c1 NUMERIC PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 53: `8300724c1e32409b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046587`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid REAL NOT NULL DEFAULT TRUE, c1 REAL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); BEGIN EXCLUSIVE;
```

---

## Crash 54: `6c0190f9d5eb0086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050144`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 55: `59f7b9dd187f9d1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054151`

```sql
CREATE TABLE t2 (rowid NUMERIC PRIMARY KEY ASC); CREATE TRIGGER trg1 AFTER INSERT ON t2 BEGIN DELETE FROM t1; END; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 56: `b577c04f89106b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055001`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 57: `6afd8beabe5d3ee5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055421`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (-3078351451355781565312694835247269057688917255771849793409180790347113.38285e+64450333994931965087); CREATE
```

---

## Crash 58: `2272f27c92931876` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055827`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (NOT '1 _ q7L24u'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 59: `52d1c3f9bdeba237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057502`

```sql
CREATE TABLE t3 (rowid FLOAT UNIQUE, _rowid_ INTEGER PRIMARY KEY DESC, UNIQUE (rowid) ON CONFLICT ABORT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_, _rowid_);
```

---

## Crash 60: `e9224abf9c249df6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058437`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIME LIKE CURRENT_TIME, TRUE OR TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 61: `87350bc9d94f9245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058965`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid NUMERIC GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, c1 BOOLEAN PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 62: `32e7738904ae7a79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059744`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); DROP TABLE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c2);
```

---

## Crash 63: `69cb240e514acd1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059754`

```sql
CREATE VIEW v1 AS SELECT ALL nullif(NULL, CASE WHEN NULL BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME THEN CURRENT_TIMESTAMP ISNULL WHEN total_changes() OVER () THEN CURRENT_TIME ISNULL ELSE TRUE % RAIS
```

---

## Crash 64: `250e65d3b1923b59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060257`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP IS NOT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 65: `785330266fb0fa79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060471`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE NOT GLOB TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 66: `3d2a7e540d9a6e93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060713`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE <= CURRENT_TIMESTAMP IS NOT TRUE); CREATE VIRTUAL TABLE
```

---

## Crash 67: `f80d6559626b4105` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060772`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE <= NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 68: `d55a4884cb26bbdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060926`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, 134.15E743438150027001809); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 69: `fc45493284188f18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061287`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 70: `ee7ba7299776425b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061789`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid REAL PRIMARY KEY); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 71: `7d6136aa5f80009f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061972`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid REAL PRIMARY KEY); WITH RECURSIVE t2 AS (SELECT *) UPDATE t1 SET _rowid_ = NULL WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 72: `401273274595dfdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062511`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, NULL OR CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 73: `e06b378bcee6d562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062734`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, NULL OR CURRENT_TIME COLLATE BINARY <= NULL); CREATE VIRTUAL TABLE I
```

---

## Crash 74: `a81e13af7e4a6b9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065363`

```sql
CREATE TABLE t1 (_rowid_ BOOLEAN PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 75: `b7510e2aa637a0f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065851`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, NOT EXISTS (VALUES (RAISE(IGNORE)))); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 76: `1195a4b92ab4d3dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066860`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 INTEGER PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowi
```

---

## Crash 77: `09d2ebdc9f0e3051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068569`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); ALTER TABLE t1 ADD COLUMN _rowid_ TEXT NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 78: `630dd6c1d3537a24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069435`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ TEXT UNIQUE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); END;
```

---

## Crash 79: `b2c973645a71edd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069695`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 REAL DEFAULT TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 80: `701af39ec95a54ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070509`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ TEXT UNIQUE); INSERT INTO t1 DEFAULT VALUES; BEGIN EXCLUSIVE TRANSACTION; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VALUES; INSERT INTO t1 DEFAULT VA
```

---

## Crash 81: `511f98ee145de0a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075402`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ FLOAT NOT NULL REFERENCES t3 (c2) ON UPDATE CASCADE, c2 INTEGER NOT NULL REFERENCES t3 (_rowid_) ON DELETE CASCADE ON UPDATE CASCADE, c1 NUMERIC PRIMARY KEY DESC
```

---

## Crash 82: `5de941071c79e8cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075850`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 FLOAT PRIMARY KEY DESC) WITHOUT ROWID; BEGIN IMMEDIATE TRANSACTION; CREATE TEMP TABLE IF NOT EXISTS t1 (c2 DATE NOT NULL); ATTACH ':memory:' AS db2; END; VACUUM; CREA
```

---

## Crash 83: `6e85594401ada3ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076094`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE TRANSACTION; ATTACH ':memory:' AS db2; ANALYZE; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 84: `035b838e86cc2742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076155`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE TRANSACTION; ATTACH ':memory:' AS db2; ANALYZE; END; CREATE TABLE IF NOT EXISTS t3 (c1 REAL UNIQUE); ANALYZE;
```

---

## Crash 85: `b2276e3ba7ddde89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077406`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ALTER TABLE t2 RENAME COLUMN c3 TO c3; WITH RECURSIVE t3 (_rowid_) AS NOT MATERIALIZED (SELECT ALL RAISE(IGNORE)
```

---

## Crash 86: `1f9c029f0a9dc7e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079166`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 87: `89b94f3ba66d2362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080206`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 88: `84fe8b46a3b20f6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080450`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c1, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 89: `e4bd8e8ec9bebd28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083884`

```sql
BEGIN EXCLUSIVE; ATTACH ':memory:' AS db2; END TRANSACTION; BEGIN TRANSACTION; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 90: `c0a3268a9160b9b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084664`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 91: `bda1ae608a9d58be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093245`

```sql
CREATE TABLE t3 AS SELECT DISTINCT CURRENT_TIMESTAMP & CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP / NULL AS f_8_u2_eu4_s5fmzd55g_7g__oiy_990t_4____dq____3_6__sn__8t7g599ux06_e0; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 92: `e39967aee04fab3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093315`

```sql
PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 93: `e36c5a54cc431e00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096161`

```sql
SELECT changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 94: `07c623ca314089ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096760`

```sql
SELECT count(DISTINCT FALSE COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 95: `a1caf224dc5ffbe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098996`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 96: `6fa9fca0c7a67e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099028`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 97: `140fe25f790f4ede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099508`

```sql
SELECT -'-_1_-_--GLv__I-_T_k'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); WITH t2 (c2) AS NOT MATERIALIZED (VALUES (t2._rowid_)) DELETE FROM t3 WHERE ~CASE (NOT EXISTS (SELECT DISTI
```

---

## Crash 98: `7b3a8db580fe4bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099566`

```sql
VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); WITH t2 (c2) AS NOT MATERIALIZED (VALUES (t2._rowid_)) DELETE FROM t3 WHERE ~CASE (NOT EXISTS (SELECT DISTINCT *)) != -CURR
```

---

## Crash 99: `7fce0fec4c3a3805` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099575`

```sql
SELECT -TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); WITH t2 (c2) AS NOT MATERIALIZED (VALUES (t2._rowid_)) DELETE FROM t3 WHERE ~CASE (NOT EXISTS (SELECT DISTINCT *)) != -CURRE
```

---

## Crash 100: `b8386be3212c4756` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101528`

```sql
SELECT json_type(CURRENT_TIMESTAMP ISNULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 101: `03974ca901435338` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104707`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ TEXT PRIMARY KEY, c1 REAL UNIQUE) WITHOUT ROWID; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 102: `90fcaf4ca5622326` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104756`

```sql
CREATE TEMP TABLE t1 (rowid VARCHAR(255) COLLATE NOCASE); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 103: `347f16178a74b6cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106153`

```sql
SELECT FALSE LIMIT TRUE, FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2, c1);
```

---

## Crash 104: `650b60bb03c455d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115166`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE TRANSACTION; ATTACH ':memory:' AS db2; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 105: `40023ee9a2936ceb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120686`

```sql
VALUES (CURRENT_DATE BETWEEN count(*) FILTER (WHERE CURRENT_TIME) OVER () AND count(CURRENT_DATE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 106: `be1fd7510b16f52f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122898`

```sql
CREATE TABLE t3 (c3 INTEGER NOT NULL REFERENCES t1 (rowid) NOT DEFERRABLE INITIALLY IMMEDIATE, PRIMARY KEY (c3), UNIQUE (c3)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 107: `b84847b104b6b5a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124351`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INT); INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 108: `d76d30f43895b9ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124545`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 FLOAT PRIMARY KEY DESC); INSERT INTO t1 DEFAULT VALUES; INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 109: `2fd9a00bbd3504b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124953`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 FLOAT PRIMARY KEY DESC); BEGIN IMMEDIATE TRANSACTION; INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 110: `fbefb389506f1c08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124960`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 FLOAT PRIMARY KEY DESC); INSERT INTO t1 DEFAULT VALUES; ANALYZE; UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_,
```

---

## Crash 111: `eb881ea3b249393c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125091`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 REAL DEFAULT -28013865316.49095e+61); INSERT INTO t1 DEFAULT VALUES; INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABL
```

---

## Crash 112: `c43bb4489044088c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125121`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 REAL DEFAULT -28013865316.49095e+61); INSERT INTO t1 DEFAULT VALUES; INSERT OR FAIL INTO t1 VALUES (TRUE); ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 113: `c138ec0b4b8b4a90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125359`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INT PRIMARY KEY); INSERT INTO t1 DEFAULT VALUES; INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 114: `1e38a58ed4228e73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125365`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 REAL DEFAULT FALSE); INSERT INTO t1 DEFAULT VALUES; INSERT OR FAIL INTO t1 VALUES (TRUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 115: `ff6db64756c448da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125452`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 REAL DEFAULT ''); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 116: `ecc61b71e0691bd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131065`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE IN (SELECT 85741558962804519920389389950656116629941194
```

---

## Crash 117: `e31121f4b6211c84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131171`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE IN (VALUES (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 118: `5ea8aaef5677002e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131180`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE IN (SELECT FALSE FROM t1 GROUP BY NULL WINDOW w1 AS ())
```

---

## Crash 119: `dfc11e66f6afcfdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133643`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 FLOAT DEFAULT NULL); UPDATE OR FAIL t1 SET rowid = CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 120: `7a274ef617bf3645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134822`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, FALSE OR TRUE <= NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 121: `59f50d568d5a8472` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135217`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN NOT NULL DEFAULT -45.2953408642483226705955836155551460459E7); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 122: `ab5add1d76ea8129` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135422`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ REAL COLLATE NOCASE, rowid BOOLEAN UNIQUE); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 123: `60d8592dc7640137` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135572`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid REAL PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (-3078351451355781565312694835247269057688917255771849793409180790347113.38285e+64450333994931965087); REINDEX t1;
```

---

## Crash 124: `d8ca9e89fae1f9e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135825`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INTEGER PRIMARY KEY ASC); UPDATE OR IGNORE t1 SET _rowid_ = TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, _rowid_);
```

---

## Crash 125: `9d672efb80f5d3cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136469`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ DATE CHECK (c2), c2 BOOLEAN PRIMARY KEY); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 126: `39ef928e2bf85a13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136574`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ DATE CHECK (CURRENT_TIME), c2 BOOLEAN PRIMARY KEY); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 127: `3e429f23f6fe5f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136581`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ DATE CHECK (c2), c2 BOOLEAN PRIMARY KEY); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 128: `67a99a3003bc8393` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136714`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE TRIGGER trg1 BEFORE UPDATE ON t1 BEGIN UPDATE t1 SET rowid = FALSE; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 129: `4c61810e5dc5d3d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137608`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, -8281); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 130: `a5760086429221ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138630`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL, c1 VARCHAR(255) PRIMARY KEY); INSERT OR FAIL INTO t1 VALUES (CURRENT_TIMESTAMP, CURRENT_DATE IS NULL IS NOT FALSE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 131: `4b0b083ba1f3a44b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139137`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ INT PRIMARY KEY, c2 BLOB DEFAULT FALSE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_);
```

---

## Crash 132: `1a50a5af3d22e6cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139291`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) UNIQUE, _rowid_ TEXT PRIMARY KEY); DROP TABLE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 133: `debb4e6137e2bdcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139450`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); DROP TABLE t1; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW IF NOT EXISTS v1 (c1, c1, c1) AS S
```

---

## Crash 134: `295ed4ea9877c17a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139506`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) PRIMARY KEY); DROP VIEW IF EXISTS v1; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIEW IF NOT EXISTS v1 (c1, c1,
```

---
