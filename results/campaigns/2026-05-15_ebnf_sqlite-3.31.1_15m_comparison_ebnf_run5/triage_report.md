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

## Crash 1: `76846cd2e273bbac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000066`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); COMMIT; REINDEX t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 2: `cea3a5e9bfd26c8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000104`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_);
```

---

## Crash 3: `c8cb8e91dcabef01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000816`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 4: `1af9d6af8048766e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001063`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_, _rowid_, c3, c1); ALTER TABLE t2 RENAME TO t2;
```

---

## Crash 5: `64d76fb9af802fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001181`

```sql
PRAGMA cache_size=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t3 AS MATERIALIZED (WITH RECURSIVE t1 (c2) AS (SELECT t3.*) SELECT ALL FALSE UNION ALL SELECT CURRENT_DATE
```

---

## Crash 6: `a64f03979268e8b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001304`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 7: `5275ec8dd8c8ff97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001460`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_, c3); DETACH DATABASE db2; SELECT DISTINCT t3.*, json(EXISTS (WITH t1 AS (SELECT DISTINCT * LIMIT TRUE, RAISE(IGNORE)),
```

---

## Crash 8: `b04149bb9f575162` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002597`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 9: `63f27cda6fccfc74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002603`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 10: `e486d7a5447dd222` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003482`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_);
```

---

## Crash 11: `2cbfab36079fe564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003489`

```sql
VACUUM; CREATE TABLE t2 AS VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_);
```

---

## Crash 12: `b0a976f0a3d8f125` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003677`

```sql
VACUUM; PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_);
```

---

## Crash 13: `c9d19cbad71a32d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003683`

```sql
VACUUM; CREATE TEMP TABLE IF NOT EXISTS t1 (rowid INT PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_);
```

---

## Crash 14: `214a536e5d5576f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006053`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); UPDATE OR ABORT t2 SET rowid = +RAISE(IGNORE) IS TRUE <= NOT FALSE COLLATE BINARY COLLATE NOCASE NOT GLOB (~NOT E
```

---

## Crash 15: `e6bc4b559ba34cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006490`

```sql
BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 16: `c032e7004b960493` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007543`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 17: `debd3c06fad84916` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018180`

```sql
CREATE TABLE t2 AS SELECT ALL +CASE WHEN FALSE THEN NULL END OR CURRENT_TIMESTAMP GLOB FALSE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE
```

---

## Crash 18: `17127501de4cbd40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018810`

```sql
CREATE TABLE t2 AS SELECT ALL CASE WHEN NULL THEN NULL END ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); VACUUM; CREATE INDEX IF NOT EXISTS i
```

---

## Crash 19: `4541f2dc521619e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019765`

```sql
CREATE TABLE t2 AS SELECT ALL +CURRENT_DATE == CURRENT_DATE NOTNULL OR CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 20: `efb85ab88058b60a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020607`

```sql
CREATE TABLE t2 AS SELECT ALL CASE WHEN CURRENT_TIME THEN NULL END ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 21: `b7da6e88fa93fc03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021538`

```sql
PRAGMA cache_size=-5555; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `2ae010dc3459f5ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022139`

```sql
CREATE TEMP TABLE t3 (rowid REAL PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 23: `68e6de767b291d6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029022`

```sql
CREATE TABLE t1 (c1 FLOAT NOT NULL, UNIQUE (c1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 24: `33e395d2b4505773` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029780`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2);
```

---

## Crash 25: `0f3e8bb51406b489` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029860`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1);
```

---

## Crash 26: `50c097dabd3f9378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030789`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1);
```

---

## Crash 27: `5e4e95b1c4b86b50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030854`

```sql
BEGIN DEFERRED; ATTACH DATABASE ':memory:' AS db2; DROP TABLE IF EXISTS t1; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DELETE FROM t1 WHERE -group_concat(-
```

---

## Crash 28: `0dc52ab2f5440714` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031760`

```sql
PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 29: `e96f1fca66946fdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032658`

```sql
CREATE TABLE t2 (c3 REAL NOT NULL REFERENCES t3 (c3) ON UPDATE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3);
```

---

## Crash 30: `e0867a35ec877266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033336`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 31: `fd2292e48011bde3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035037`

```sql
DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 32: `2d53746a389aa9ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035490`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 33: `332090c1b2505949` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035924`

```sql
PRAGMA cache_size=94; CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK TRANSACTION; ROLLBACK TRANSACTION;
```

---

## Crash 34: `8e9aa797ea9db9bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041342`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 35: `b8b333f83e60a71e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044858`

```sql
VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIMESTAMP))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 36: `82b5e93e94df0588` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046358`

```sql
PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 37: `65e1a7ce7f8b6c39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048435`

```sql
CREATE TEMP TABLE t1 (c3 INT UNIQUE, c1 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 38: `a78a5d334ce30436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050424`

```sql
CREATE TEMP TABLE t2 (c2 FLOAT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 39: `495bb37d175e15d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051541`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 40: `a6f668a8b4f60424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053079`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN DEFAULT CURRENT_TIMESTAMP, _rowid_ FLOAT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 41: `a49e232dd0c2902f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054086`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ROLLBACK TRANSACTION; ANALYZE; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN COLLATE NOCASE); CREATE VIRTUAL TABLE IF
```

---

## Crash 42: `dad9d58cd8fd758e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059749`

```sql
CREATE TABLE t2 AS SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIMESTAMP) ORDER BY CURRENT_TIMESTAMP ASC, CURRENT_TIMESTAMP NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 43: `2f01077505de8d2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060543`

```sql
CREATE TABLE t2 AS SELECT ALL 8858847032792517590.027577442810680 ORDER BY TRUE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c3);
```

---

## Crash 44: `ebafb197d700c211` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060900`

```sql
CREATE TABLE t2 AS SELECT ALL NULL ORDER BY count(*) OVER (PARTITION BY CURRENT_TIMESTAMP, NULL) ASC NULLS FIRST, CURRENT_TIME ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 45: `b665fdbd2392b9b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063793`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 TEXT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 46: `e2b5bdb816b86b24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064298`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid BLOB PRIMARY KEY, c2 INT UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 47: `6a40bb0e9f6c2277` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065279`

```sql
CREATE TABLE t2 AS SELECT ALL NULL NOTNULL ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 48: `fcacd3b2c770bc1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065417`

```sql
CREATE TABLE t2 AS SELECT ALL count(DISTINCT TRUE) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 49: `d00b3c0a4148822d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065627`

```sql
CREATE TABLE t2 AS VALUES (NULL) INTERSECT SELECT TRUE AS p64___736_s5_6_7270__r8____53___; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 50: `301d79ddef42bc72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066732`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIME ORDER BY -RAISE(IGNORE) ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 51: `25ee7d87fbf31494` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066847`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 52: `b0ff80a5ecf1515d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066853`

```sql
CREATE TABLE t3 (rowid VARCHAR(255) PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 53: `adf4db1930a1c178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066863`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIME ORDER BY RAISE(IGNORE) ASC; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 54: `a7dce41edbe2ed3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066941`

```sql
CREATE TABLE t2 AS SELECT ALL FALSE ORDER BY +CURRENT_DATE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 55: `56df75ad90797dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068072`

```sql
CREATE TABLE t2 AS SELECT ALL NULL - NULL ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 56: `23d4b73018d09696` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068943`

```sql
CREATE TABLE t2 AS SELECT ALL ~0.50034151902684E+2680521 ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 57: `8714b1041c787786` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069099`

```sql
CREATE TABLE t2 AS SELECT ALL ~CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 58: `048489758ddedcf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069132`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIME AND TRUE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 59: `af2ce1eea2af6a26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070611`

```sql
CREATE TABLE t2 AS SELECT ALL -CURRENT_DATE IS NOT FALSE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 60: `f936904dcc70e241` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070759`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INT PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 61: `1bb1d6e8b92ca79a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070770`

```sql
CREATE TABLE t2 AS SELECT ALL -CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 62: `1d1a40e14cd1334f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071751`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIME IS TRUE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 63: `cadc8262f6932bd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073155`

```sql
CREATE TABLE t2 AS SELECT ALL CASE WHEN TRUE THEN NULL END ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 64: `88a68dff41791b4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073700`

```sql
CREATE TABLE t2 AS SELECT ALL NOT CURRENT_DATE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 65: `9201263ce77a0e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074027`

```sql
CREATE TABLE t2 AS SELECT ALL avg(NULL) FILTER (WHERE CURRENT_TIME) OR CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 66: `50a2950260f6c51d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075426`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIME IS CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF
```

---

## Crash 67: `47874920b48b2e09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076048`

```sql
CREATE TABLE t2 AS SELECT ALL NULL ORDER BY count(*) FILTER (WHERE FALSE) OVER () ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DETACH db2;
```

---

## Crash 68: `4658c50462ac080e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077682`

```sql
PRAGMA analysis_limit=+441; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 69: `01210571f7b64ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079470`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 70: `9322993d6e82ea64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087106`

```sql
CREATE TABLE t2 AS WITH RECURSIVE t2 AS (VALUES (TRUE)) SELECT NULL AS w_b ORDER BY CURRENT_TIME ASC NULLS LAST, NULL COLLATE RTRIM DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 71: `ee7bf9e86060f939` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087678`

```sql
CREATE TABLE t2 AS WITH RECURSIVE t2 AS (VALUES (TRUE)) SELECT CURRENT_DATE COLLATE RTRIM AS w_b ORDER BY CURRENT_TIME ASC NULLS LAST, NULL COLLATE RTRIM DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 72: `301f5014687ff670` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087843`

```sql
CREATE TABLE t2 AS WITH RECURSIVE t2 AS (VALUES (TRUE)) SELECT CAST(CURRENT_DATE AS BLOB) COLLATE RTRIM | CURRENT_TIME AS w_b ORDER BY CURRENT_TIME ASC NULLS LAST, NULL COLLATE RTRIM DESC NULLS LAST; 
```

---

## Crash 73: `e3e19a5a5c2e6023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087951`

```sql
CREATE TABLE t2 AS WITH RECURSIVE t2 AS (VALUES (TRUE)) SELECT TRUE AS w_b ORDER BY CURRENT_TIME ASC NULLS LAST, FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); CREATE TRIGGER trg
```

---

## Crash 74: `14d882816451552b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092243`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION;
```

---

## Crash 75: `7a75107f9420fb3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092256`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ATTACH ':memory:' AS db2; DELETE FROM t3 RET
```

---

## Crash 76: `d2df8fd6824b8c66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092334`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION;
```

---

## Crash 77: `d5c12cc097e9a503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093282`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH t1 AS (WITH RECURSIVE t1 AS (VALU
```

---

## Crash 78: `458f9f3ce6cf73e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093495`

```sql
CREATE TEMP TABLE t1 (c1 BOOLEAN REFERENCES t1 (_rowid_) ON DELETE SET DEFAULT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 79: `b8ae83f7aa136068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093563`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 80: `4132caeb943ee010` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093699`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS rtree
```

---

## Crash 81: `24502aed4603ebd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093838`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ATTACH ':memory:' AS db2; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); 
```

---

## Crash 82: `e3ab53c8b11946e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094955`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 83: `6bc7494281822874` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099040`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN EXCLUSIVE; COMMIT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c2, _rowid_, c3); COMMIT; CREA
```

---

## Crash 84: `7012b44694fe78ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099663`

```sql
CREATE TABLE t2 (c3 VARCHAR(255) DEFAULT TRUE); ALTER TABLE t2 RENAME TO t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); REINDEX t3; DETACH DATABASE db2; CREATE VIEW IF NOT EXISTS v1
```

---

## Crash 85: `d4b6c0c016f4eda5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104880`

```sql
WITH RECURSIVE t2 AS (VALUES (TRUE)) SELECT DISTINCT * FROM t2 WHERE CURRENT_DATE GROUP BY NULL ORDER BY count(*) FILTER (WHERE FALSE) ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 86: `28f5d831e894fbb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110123`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL *; CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); DETACH db2; ANALYZE t2;
```

---

## Crash 87: `faf8fcd7815c2a4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110178`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL *; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); DETACH db2; ANALYZE t2;
```

---

## Crash 88: `c8473ec00ba11aeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111706`

```sql
CREATE TABLE t2 AS SELECT ALL TRUE % CURRENT_TIME ORDER BY CURRENT_TIME ASC NULLS LAST; REINDEX t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); DELETE FROM t1 WHERE CASE WHEN RAISE(I
```

---

## Crash 89: `69efe69877d35c13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112326`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_DATE GLOB CURRENT_DATE - CURRENT_DATE - TRUE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INT
```

---

## Crash 90: `89765c778224a241` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113965`

```sql
CREATE TABLE t2 AS SELECT ALL X'' OR FALSE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH t3 AS (SELECT *, NULL REGEXP NULL UNION ALL SELECT DISTI
```

---

## Crash 91: `1fab46997d208e40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116169`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_DATE OR X'' ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 92: `2ed6a6225d2279cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116335`

```sql
CREATE TABLE t2 AS SELECT ALL FALSE GLOB CURRENT_DATE NOT IN (changes()) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 93: `69bcceb7c2322522` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116434`

```sql
CREATE TABLE t2 AS SELECT ALL FALSE GLOB NULL ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 94: `a836305c82226d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116440`

```sql
CREATE TABLE t2 AS SELECT ALL FALSE GLOB CURRENT_DATE NOT IN (CURRENT_DATE) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 95: `b9fbb047c9bf4861` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116770`

```sql
CREATE TABLE t2 AS SELECT ALL sum(CURRENT_TIME) OVER () / CURRENT_TIMESTAMP GLOB FALSE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c1); C
```

---

## Crash 96: `c8878512aff6b130` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116921`

```sql
CREATE TABLE t2 AS SELECT ALL FALSE / CURRENT_TIMESTAMP GLOB FALSE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c1); CREATE VIRTUAL TABLE 
```

---

## Crash 97: `448b8daf5ed519a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118032`

```sql
CREATE TABLE t2 AS SELECT ALL sum(CURRENT_TIME) OVER () / count(*) OVER (ORDER BY NULL ASC NULLS FIRST) <> FALSE AS u63q_3_gdpnne__qlj_____0390____l ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUA
```

---

## Crash 98: `fd20e2441a3ca0fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118669`

```sql
CREATE TABLE t2 AS SELECT ALL CASE WHEN CURRENT_TIME < CURRENT_DATE THEN FALSE END ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); DETACH DATABASE db2;
```

---

## Crash 99: `d0caffd55132b869` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118958`

```sql
CREATE TABLE t2 AS SELECT ALL CASE WHEN X'' THEN CURRENT_TIME END ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); END TRANSACTION; ANALYZE t3;
```

---

## Crash 100: `7523cbb6dc502f52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119537`

```sql
CREATE TABLE t2 AS SELECT ALL CAST(TRUE AS TEXT) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 101: `88b4ddba2a2df901` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120189`

```sql
CREATE TABLE t2 AS SELECT ALL min(NULL) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 102: `5c04b24ec08f98f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120391`

```sql
CREATE TABLE t2 AS SELECT ALL total_changes() ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 103: `fac922cecb312ca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121235`

```sql
CREATE TABLE t2 AS SELECT ALL zeroblob(CURRENT_TIME) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 104: `a7fe4026e8e9fb4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121334`

```sql
CREATE TABLE t2 AS SELECT ALL count(*) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 105: `620502d3fc31f9d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122654`

```sql
CREATE TABLE t2 AS SELECT DISTINCT TRUE LIKE CURRENT_DATE ESCAPE NULL AS n4_30jtn2s68n_k2mz__ ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_
```

---

## Crash 106: `c860acf1a2361d74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128530`

```sql
CREATE TABLE t2 AS SELECT ALL count(DISTINCT X'') ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 107: `70c3f5118b64b60f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128617`

```sql
CREATE TABLE t2 AS SELECT ALL count(DISTINCT NULL) ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 108: `3e98a930270b3cad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129876`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ REAL UNIQUE, rowid REAL CHECK (RAISE(IGNORE)), c1 BLOB PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 109: `77769eab28ccd992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130467`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid DATE PRIMARY KEY DESC, c3 FLOAT REFERENCES t2 (_rowid_) DEFERRABLE INITIALLY DEFERRED) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_,
```

---

## Crash 110: `cbdd6e5506d26452` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130704`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 BLOB NOT NULL DEFAULT CURRENT_TIME, c3 REAL PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN DEFERRED TRANSACTION;
```

---

## Crash 111: `51624074cf1d032f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132238`

```sql
CREATE TABLE t2 AS SELECT ALL -55840509696811234771786482803619466929219870821.3631e+732 == CURRENT_DATE ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, 
```

---

## Crash 112: `d72c0e7391e4b718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132668`

```sql
CREATE TABLE t2 AS SELECT ALL X'cfdad5EFAAeb' ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 113: `151b7cc25486a371` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133778`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); BEGIN EXCLUSIVE TRANSACTION;
```

---

## Crash 114: `ce0f63a1e17c6803` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134457`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_DATE NOT LIKE NULL ORDER BY count(*) OVER () ASC NULLS FIRST, CURRENT_TIME ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 115: `164afebe7024f691` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135100`

```sql
CREATE TABLE t2 AS SELECT ALL -25447250529929572376310794330287172176.0973693602736e+202 ORDER BY CURRENT_TIMESTAMP ASC, count(*) FILTER (WHERE FALSE) OVER () ASC NULLS LAST; CREATE VIRTUAL TABLE IF N
```

---

## Crash 116: `eaadf13614122ec5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135264`

```sql
CREATE TABLE t2 AS SELECT ALL CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP ASC, count(*) FILTER (WHERE FALSE) OVER () ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 117: `e05ff44a0f5d0a89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136064`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ INTEGER PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 118: `587841b0d3e53f32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137894`

```sql
SELECT ALL TRUE ORDER BY TRUE NOT IN (VALUES (FALSE)) ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 119: `ee316f20ce20fb4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138709`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 120: `ac33a24100ddccd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139169`

```sql
PRAGMA journal_mode=TRUNCATE; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 121: `211e787e2e9a7071` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139220`

```sql
PRAGMA quick_check; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 122: `a7386ac265682ed3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141814`

```sql
BEGIN; ATTACH DATABASE ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 123: `ba3a37ee5e59b2ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142537`

```sql
BEGIN; END TRANSACTION; ATTACH DATABASE ':memory:' AS db2; DETACH DATABASE db2; CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ BLOB PRIMARY KEY DESC); CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ VARCHAR(
```

---

## Crash 124: `dfce7941783736ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143001`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ROLLBACK TRANSACTION; ANALYZE; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN COLLATE NOCASE); CREATE VIRTUAL TABLE IF
```

---

## Crash 125: `628fe9a2b2832972` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143014`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ROLLBACK TRANSACTION; ANALYZE; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN COLLATE NOCASE); CREATE VIRTUAL TABLE IF
```

---

## Crash 126: `ddd3619eb668d115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143293`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid BLOB PRIMARY KEY, c2 INT UNIQUE) WITHOUT ROWID; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 127: `1fe75fb4cc501edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143386`

```sql
ANALYZE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 128: `4a2fb9652a01549f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143392`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 INTEGER NOT NULL); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 129: `999e46f4f27e900c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144740`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 REAL PRIMARY KEY); UPDATE OR ABORT t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 130: `33f7257c0fb3eb4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144903`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (rowid DATE PRIMARY KEY DESC, c2 REAL, _rowid_ FLOAT GENERATED ALWAYS AS (NULL) VIRTUAL); UPDATE OR ABORT t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 131: `40e0a504af90e026` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145728`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 BOOLEAN DEFAULT CURRENT_TIMESTAMP, _rowid_ FLOAT GENERATED ALWAYS AS (NULL) VIRTUAL); UPDATE OR ABORT t2 SET c2 = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIST
```

---
