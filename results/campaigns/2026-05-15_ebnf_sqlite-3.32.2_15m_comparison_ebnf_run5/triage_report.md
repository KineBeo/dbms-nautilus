# Crash Triage Report

**Total crashes:** 93  
**Unique crash sites:** 93  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 93 | 93 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `cd730a8bf2a7d0cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000134`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_);
```

---

## Crash 2: `a71fb986cf7b64f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004853`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT DISTINCT *, * FROM t3 NOT INDEXED WHERE 'e_ _7__ 9-' || FALSE -> CASE random() WHEN FALSE IS DISTINCT FROM NULL
```

---

## Crash 3: `70bb8e7d379c0e61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005499`

```sql
ANALYZE; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 4: `8952c9ea660fb665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005608`

```sql
PRAGMA journal_mode=WAL; PRAGMA analysis_limit=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 5: `32ca0a67dabce863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005618`

```sql
DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowid_);
```

---

## Crash 6: `326de0e2614ed734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005860`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2); DETACH DATABASE db2; ANALYZE t1; ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 7: `a27c48c0086d756b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005973`

```sql
PRAGMA cache_size=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3); ANALYZE t2;
```

---

## Crash 8: `dfc6c81bf37930a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006084`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3, c2, _rowid_); UPDATE t1 SET c1 = EXISTS (SELECT DISTINCT -TRUE GLOB RAISE(IGNORE) <> RAISE(IGNORE) NOTNULL NOTNULL FROM t1 AS g___
```

---

## Crash 9: `cb72132aff926add` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006095`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2, _rowid_, c2, c2);
```

---

## Crash 10: `1afe056fbb764b49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006330`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PRAGMA analysis_limit=-0; DETACH db2; CREATE TABLE t1 (rowid BOOLEAN PRIMARY KEY AUTOINCREMENT) STRICT; PRAGMA cache_s
```

---

## Crash 11: `c7afdde5e10adf76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007983`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 12: `8729d9b8da9c279e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008091`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 13: `c3ba7be58fd9bf50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 14: `0046372dbab19bc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009747`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 15: `f2884aeb43b690e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011834`

```sql
PRAGMA wal_checkpoint(FULL); PRAGMA cache_size=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 16: `05120043ed61a2b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015007`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 17: `6f1d774a588af244` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015072`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 18: `7b48aa9212e16515` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015979`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 19: `8dfb47115195d8d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017602`

```sql
PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 20: `8e168effa7caf6f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021488`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); DETACH DATABASE db2;
```

---

## Crash 21: `a10d8bd57d2d38c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022450`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid DATE CHECK (RAISE(IGNORE)), c1 INTEGER PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); COMMIT;
```

---

## Crash 22: `7cb30e8371034c28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023283`

```sql
CREATE TEMP TABLE t1 (_rowid_ INT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2, c3); CREATE VIEW v1 (rowid, c1, rowid, _rowid_) AS WITH t3 AS MATERIALIZED (SELECT
```

---

## Crash 23: `811f5f31f7e03cb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025133`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 24: `39f49cb0d60a4f5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027069`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 25: `d825d84e1c90017f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028702`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 26: `d21c9ac2ae1756ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033494`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 27: `894a7eca2e8f7892` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033749`

```sql
CREATE TEMP VIEW v1 AS SELECT * FROM t3 GROUP BY FALSE, FALSE LIMIT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 28: `023ef1a6eec4bd5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033798`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 29: `e20f560b547aaba4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036163`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 30: `4444d1975276cd64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040626`

```sql
CREATE TABLE t3 (_rowid_ NUMERIC GENERATED ALWAYS AS (FALSE) VIRTUAL, c1 FLOAT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 31: `36c8fc616e466d82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050456`

```sql
VALUES (TRUE) UNION SELECT DISTINCT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 (_rowid_) VALUES (format('- --_30j Q-d9', CASE CAST(CURRENT_TIME AS REAL) WHEN FALSE 
```

---

## Crash 32: `9b0d01aa06786576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051412`

```sql
VALUES (TRUE) UNION ALL SELECT DISTINCT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 33: `fe58643be57374ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052997`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ VARCHAR(255) PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 34: `a98f563d585ff123` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053962`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ VARCHAR(255) PRIMARY KEY DESC) WITHOUT ROWID; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); BEGIN;
```

---

## Crash 35: `1ba953c13435c28a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062700`

```sql
CREATE TABLE t3 (_rowid_ VARCHAR(255) COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); CREATE INDEX idx1 ON t2 (c1, c2);
```

---

## Crash 36: `684ea3144f8f73c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065236`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid BOOLEAN PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT ALL t3.*, group_concat(CURRENT_TIME IS NOT NULL GLOB R
```

---

## Crash 37: `61ac1a1cdafa8aed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067758`

```sql
CREATE TABLE t3 (_rowid_ BLOB NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, _rowid_); SELECT
```

---

## Crash 38: `1a0c692c1cf21d15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068411`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 39: `4d5d85444516f198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070407`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; PRAGMA cache_size=-0; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 40: `4394a6af2eb2b649` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072716`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 41: `c790d679505243dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073403`

```sql
CREATE VIEW v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 42: `b7dda64b44dbb843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076471`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 43: `63d68456f1e322db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078840`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid DATE CHECK (RAISE(IGNORE)), c1 INTEGER PRIMARY KEY DESC) WITHOUT ROWID; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 44: `1c05fa6f76b49be0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079345`

```sql
BEGIN IMMEDIATE TRANSACTION; ROLLBACK TRANSACTION; BEGIN IMMEDIATE; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REINDEX t1;
```

---

## Crash 45: `f8cc36ab753fc6db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079813`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN IMMEDIATE; CREATE TEMP TABLE t1 (c1 REAL PRIMARY KEY DESC); CREATE TABLE IF NOT EXISTS t3 (c3 TEXT PRIMARY 
```

---

## Crash 46: `6025fcdd59679bb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080709`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 47: `4b05621b6dbd63b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082766`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 48: `f9bb45bd65c6ea79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082814`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 49: `657a4e1fc7c71358` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084928`

```sql
SELECT ALL TRUE % TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); END;
```

---

## Crash 50: `9e1effd43c17b334` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084973`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); END;
```

---

## Crash 51: `658055bbc6c9babb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085263`

```sql
SELECT ALL TRUE + FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TRIGGER trg1 AFTER DELETE ON t2 BEGIN UPDATE t3 SET _rowid_ = CAST(CAST(CURRENT_TIMESTAMP AS DATE) == json_ext
```

---

## Crash 52: `a5a8d344ce1e0f2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085416`

```sql
SELECT ALL length(TRUE % +FALSE + FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 53: `df7d442c088df34d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085476`

```sql
SELECT ALL CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 54: `e556bea7a61a9d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085482`

```sql
SELECT ALL changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 55: `1f7feec8b9da0695` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085488`

```sql
SELECT ALL length(FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 56: `9384302f15dbc59c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085495`

```sql
SELECT ALL length(TRUE % CURRENT_TIME + FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2);
```

---

## Crash 57: `56a6ffbf1f49a014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085785`

```sql
SELECT ALL avg(CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 58: `7b67c40ad18c0e3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086394`

```sql
SELECT ALL count(CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 59: `5852b0121495ceb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086493`

```sql
SELECT ALL CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 60: `654b14607cb128f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086499`

```sql
SELECT ALL total_changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 61: `a6c79dae7e666405` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086765`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 62: `caa54bb8a6efd93e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088589`

```sql
ANALYZE; CREATE TEMP TABLE IF NOT EXISTS t3 (c2 DATE NOT NULL); BEGIN IMMEDIATE; CREATE TEMP TABLE IF NOT EXISTS t3 (c3 NUMERIC REFERENCES t1 (c3) ON DELETE CASCADE ON UPDATE CASCADE); CREATE VIRTUAL 
```

---

## Crash 63: `872b024d12bbbcc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088893`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c2 DATE NOT NULL); CREATE TEMP TABLE IF NOT EXISTS t3 (c3 FLOAT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, _rowid_);
```

---

## Crash 64: `cf2b0ca5acda8c82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089332`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 65: `f32f3daab8fa778c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097819`

```sql
BEGIN EXCLUSIVE TRANSACTION; PRAGMA analysis_limit=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ANALYZE t2;
```

---

## Crash 66: `bcbed2cce4e92390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098619`

```sql
PRAGMA analysis_limit=44; BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); ATTACH ':memory:' AS db2;
```

---

## Crash 67: `a7e8d1b2f56c768a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099124`

```sql
ATTACH ':memory:' AS db2; BEGIN TRANSACTION; END; CREATE TABLE IF NOT EXISTS t2 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE TABLE IF NOT EXISTS t2 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIR
```

---

## Crash 68: `b80fce48587cc8a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123132`

```sql
SELECT ALL count(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); DETACH db2; DELETE FROM t3 WHERE json_type(+CURRENT_TIMESTAMP MATCH CURRENT_DATE) OVER (PARTITION BY c2 ORDER
```

---

## Crash 69: `2b09ed55cb0272aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123233`

```sql
SELECT ALL last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); DETACH db2; DELETE FROM t3 WHERE json_type(+CURRENT_TIMESTAMP MATCH CURRENT_DATE) OVER (PARTITION BY 
```

---

## Crash 70: `bcbf82d87637c6d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124156`

```sql
SELECT ALL abs(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 71: `6927d21b16255843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124209`

```sql
SELECT ALL count(*); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 72: `a99f97f8f2c4153c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124841`

```sql
SELECT ALL avg(TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 73: `790522e56f89f849` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125398`

```sql
SELECT ALL hex(TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 74: `bd4d409f918c5388` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126203`

```sql
SELECT ALL length(CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 75: `68cb210a9cb9169d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126236`

```sql
SELECT ALL random(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 76: `0f2d2629da3b2114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127242`

```sql
SELECT ALL CASE CURRENT_DATE WHEN FALSE THEN TRUE END IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 77: `3a88b3af755f542c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127346`

```sql
SELECT ALL CURRENT_TIME IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 78: `87d0fe3af6a49813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128078`

```sql
CREATE TABLE t2 (c2 FLOAT COLLATE NOCASE, CHECK (NULL), CHECK (RAISE(IGNORE))); ALTER TABLE t2 RENAME TO t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 79: `5370aa8ac5747b54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128867`

```sql
CREATE TABLE t2 (c3 BLOB COLLATE NOCASE, c1 FLOAT PRIMARY KEY DESC, CHECK (RAISE(IGNORE)), UNIQUE (c3) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 80: `6adb378ebd96aff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130007`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE; COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); REINDEX t1; PRAGMA wal_che
```

---

## Crash 81: `d388004a8e0b1144` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130531`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE TABLE IF NOT EXISTS t1 (_rowid_ TEXT PRI
```

---

## Crash 82: `4311bae77020ccad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132161`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid DATE CHECK (CASE WHEN CURRENT_DATE THEN FALSE END ISNULL GLOB RAISE(IGNORE)), c1 INTEGER PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 83: `b6d340e4479e2f64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134632`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid DATE CHECK (CURRENT_TIME BETWEEN FALSE AND CURRENT_TIMESTAMP), c1 INTEGER PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 84: `45c50e3407b8f77e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135219`

```sql
CREATE TEMP TABLE t1 (c2 VARCHAR(255) GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, rowid INTEGER PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 85: `cd956a03362eaccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136187`

```sql
ATTACH ':memory:' AS db2; DETACH DATABASE db2; BEGIN TRANSACTION; ROLLBACK; CREATE TEMP TABLE IF NOT EXISTS t3 (rowid BLOB COLLATE NOCASE); CREATE TABLE t2 (c1 VARCHAR(255) PRIMARY KEY DESC) WITHOUT R
```

---

## Crash 86: `63eccd232b407304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136416`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c3 VARCHAR(255) NOT NULL DEFAULT NULL, c2 INT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, _rowid_, _rowid_);
```

---

## Crash 87: `3adb542199b3527b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137096`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 88: `8d61d6f10aba09c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142110`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN;
```

---

## Crash 89: `7172a4a764fd54f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142158`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE V
```

---

## Crash 90: `97fbd560ac7415ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142185`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, _rowid_ INT UNIQUE) WITHOUT ROWID; DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREA
```

---

## Crash 91: `a34545d87520de7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154372`

```sql
CREATE TABLE t1 (_rowid_ BOOLEAN UNIQUE, PRIMARY KEY (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 92: `f06c78f5ccf36388` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154429`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 93: `6ba978c0aff860f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155066`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY DESC, c3 VARCHAR(255) DEFAULT (RAISE(IGNORE))) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---
