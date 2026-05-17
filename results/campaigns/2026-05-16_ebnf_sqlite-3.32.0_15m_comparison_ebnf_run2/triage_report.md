# Crash Triage Report

**Total crashes:** 100  
**Unique crash sites:** 100  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 100 | 100 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `4d24f1060c86d882` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 2: `0b8c10d58888f4b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000178`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c2, c1); DETACH db2;
```

---

## Crash 3: `c499f07a9b439d24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001266`

```sql
PRAGMA analysis_limit=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); PRAGMA journal_mode=TRUNCATE;
```

---

## Crash 4: `b61f940aaeda0adc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006700`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 5: `93c8a6c0486666ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007002`

```sql
BEGIN DEFERRED; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 6: `bd03f0017169184a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008406`

```sql
CREATE TABLE t1 (_rowid_ INTEGER CHECK (CURRENT_DATE >= CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 7: `6a41cd50c1759e23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011716`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 8: `af97ed80f04c3e66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014104`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 9: `3b3065bcafdb3832` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015613`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIEW v1 AS SELECT * FROM t2 NOT INDEXED EXCEPT SELECT ALL CURRENT_DATE % RAIS
```

---

## Crash 10: `75001bd018066541` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015763`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, c1, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); PRAGMA wal_checkpoint(FULL); END TRANSACTION;
```

---

## Crash 11: `8ab857916e863906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016353`

```sql
CREATE TEMP VIEW v1 AS VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_);
```

---

## Crash 12: `4b23139d7bc548c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016421`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 13: `7b924e9f2d6a42c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016517`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); VACUUM;
```

---

## Crash 14: `8c2fb7fd7bf53c20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016563`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 15: `5832ea32fc6d470f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016643`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 16: `b9067b4dc09e9431` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020654`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (c3 INTEGER UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 17: `c4cfd4341d2c8ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020745`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 18: `809ab8fcc7315b65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022014`

```sql
ATTACH DATABASE ':memory:' AS db2; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT ALL t1.* LIMIT RAISE(IGNORE) << TRUE >
```

---

## Crash 19: `6cc7c7a4f8fa5ce0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022717`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2, c3, c2, c3, c1);
```

---

## Crash 20: `d0649e15905d5225` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023031`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 21: `cd164142eebc7452` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023961`

```sql
CREATE TABLE t1 (c3 INT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `5f103e7c8a97a19e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025622`

```sql
VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 23: `5e977bff906fc31b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026144`

```sql
BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3);
```

---

## Crash 24: `eb3738e4fd91de4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026526`

```sql
PRAGMA cache_size=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); ROLLBACK TO sp1; ANALYZE t2;
```

---

## Crash 25: `1405a10d616ba660` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029942`

```sql
DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, c3); CREATE TABLE IF NOT EXISTS t3 (c1 VARCHAR(255) PRIMARY KEY ASC, rowid INT REFERENCES t1 (c3
```

---

## Crash 26: `86750ebfb42479ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032645`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c3, c3, c3, c1); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 27: `8a0538fef069c28d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033159`

```sql
CREATE TABLE t3 (c3 BLOB COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 28: `e9a023ff284793ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035262`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 29: `8ba20c94ebe1f93e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037450`

```sql
CREATE TABLE t1 (_rowid_ NUMERIC PRIMARY KEY ASC, c1 DATE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 30: `c10b5029ab205648` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037988`

```sql
CREATE VIEW v1 (c3) AS VALUES (RAISE(IGNORE)) UNION ALL SELECT DISTINCT * ORDER BY CURRENT_DATE ASC NULLS FIRST, RAISE(IGNORE) NULLS LAST LIMIT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 31: `5e0f012500178b85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039065`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ALTER TABLE t1 ADD COLUMN _rowid_ BOOLEAN REFERENCES t3 (_rowid_, c1); CREATE TRIGGER trg1 AFTER INSERT ON t2 FOR EACH
```

---

## Crash 32: `fd4f80118c600b47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040199`

```sql
CREATE TABLE t2 (_rowid_ TEXT UNIQUE, c1 VARCHAR(255) NOT NULL DEFAULT FALSE); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 33: `4740b75b5ccffc68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040224`

```sql
REINDEX; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 34: `e7154276773d0c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040230`

```sql
CREATE TEMP TABLE t3 (c3 NUMERIC COLLATE NOCASE); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 35: `40c1852216a1e4d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040236`

```sql
CREATE TABLE t2 (c3 BLOB NOT NULL); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 36: `34b05c4e462259d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040242`

```sql
CREATE TABLE t2 (_rowid_ TEXT UNIQUE, c3 BLOB COLLATE NOCASE); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 37: `df583791e2ea3f2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040248`

```sql
CREATE TABLE t2 (_rowid_ TEXT UNIQUE, c1 INT UNIQUE); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 38: `4d3faac8e721d0db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049154`

```sql
CREATE TABLE t1 (_rowid_ INT PRIMARY KEY, c3 TEXT UNIQUE, rowid INTEGER NOT NULL, c2 DATE NOT NULL) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 39: `77e8d1f5bd4e57f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054803`

```sql
ATTACH ':memory:' AS db2; DETACH db2; ATTACH DATABASE ':memory:' AS db2; DETACH db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); BEGIN IMMEDIATE TRANSACTION; END; CREATE VIRTUAL TABL
```

---

## Crash 40: `a8b93c1bd11c256e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054872`

```sql
ATTACH ':memory:' AS db2; DETACH db2; ATTACH DATABASE ':memory:' AS db2; DETACH db2; CREATE TABLE IF NOT EXISTS t1 (rowid TEXT NOT NULL); BEGIN IMMEDIATE TRANSACTION; END; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 41: `7b69ee85cb512b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056610`

```sql
SELECT ALL CURRENT_DATE AS a ORDER BY FALSE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 42: `dc5053a09f043464` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057011`

```sql
VALUES (TRUE IN (VALUES (FALSE)), CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 43: `721318cbd3b4f6be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057175`

```sql
VALUES (count(DISTINCT NULL) FILTER (WHERE TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 44: `4bcdfab39a96d921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057261`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 45: `fccec3053fb34a09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057270`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 46: `29e8b18f2c40469c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060951`

```sql
CREATE TABLE t3 (c3 INT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 47: `8fa2902a1ec9ecb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062059`

```sql
CREATE TABLE t2 (c1 NUMERIC PRIMARY KEY DESC, CHECK (FALSE MATCH RAISE(IGNORE) COLLATE NOCASE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 48: `6c86a36d6ffcb44f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062308`

```sql
CREATE TABLE t2 (rowid VARCHAR(255) PRIMARY KEY) WITHOUT ROWID; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); DROP TABLE t2;
```

---

## Crash 49: `cd7436dba0f49e7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062440`

```sql
CREATE TABLE t2 (c1 NUMERIC PRIMARY KEY DESC, CHECK (CASE WHEN RAISE(IGNORE) THEN CURRENT_TIMESTAMP END)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 50: `520025d08cc0417c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066162`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * INTERSECT SELECT DISTINCT * FROM (SELECT ALL *) AS pv0_9___7__76jd_p9_0736_c819__o___82g0_2z230____1_08__2 NATURAL INNER JOIN t2 ORDER BY CURRENT_DATE; CRE
```

---

## Crash 51: `cd8ec1ba20422f3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066288`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * INTERSECT SELECT DISTINCT * FROM t2 NOT INDEXED ORDER BY CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 52: `c98c0cd51df08935` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077358`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * ORDER BY RAISE(IGNORE) DESC NULLS FIRST, 0 DESC LIMIT RAISE(IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); CREATE VIEW v1 (c3, rowi
```

---

## Crash 53: `6a790aa1dc200039` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078967`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE TABLE IF NOT EXISTS t2 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 54: `72ce5dd1af134749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079138`

```sql
CREATE TABLE t2 (_rowid_ REAL PRIMARY KEY DESC, c2 TEXT UNIQUE, CHECK (CURRENT_TIMESTAMP), CHECK (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 55: `1029200e27fa7782` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080965`

```sql
CREATE TABLE t2 (c2 INT UNIQUE, c3 NUMERIC NOT NULL, CHECK (RAISE(IGNORE)), UNIQUE (c2) ON CONFLICT IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 56: `b07aa7fe00c113e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081585`

```sql
CREATE TABLE t2 (c2 NUMERIC COLLATE NOCASE, UNIQUE (c2) ON CONFLICT IGNORE, PRIMARY KEY (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 57: `732cbccb7e373e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082177`

```sql
CREATE TABLE t2 (c2 INTEGER COLLATE NOCASE, CHECK (RAISE(IGNORE)), PRIMARY KEY (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 58: `620b047a3b0c0f5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084209`

```sql
PRAGMA analysis_limit=-52172; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN DEFERRED; CREATE TABLE t2 (rowid REAL UNIQUE, rowid BOOLEAN PRIMARY KEY AUTOINCREMENT, c3 BOOLEAN PRIMARY 
```

---

## Crash 59: `c8255ea0a92831b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084265`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN DEFERRED; CREATE TABLE t2 (rowid REAL UNIQUE, rowid BOOLEAN PRIMARY KEY AUTOINCREMENT, c3 BOOLEAN PRIMARY KEY AUTOIN
```

---

## Crash 60: `aec15e9d1eb32d7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084458`

```sql
PRAGMA journal_mode=PERSIST; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 61: `8d944962d9bf9588` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084597`

```sql
CREATE TABLE t2 (c1 NUMERIC PRIMARY KEY DESC, CHECK (FALSE)); DROP TABLE t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 62: `cde927b18a996c1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093138`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 63: `3c5e87c128b0e948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097304`

```sql
CREATE TABLE t1 (_rowid_ VARCHAR(255) NOT NULL); ATTACH ':memory:' AS db2; CREATE TRIGGER trg1 BEFORE UPDATE ON t1 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 64: `dfbd4d0643e22ec4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097406`

```sql
CREATE TABLE t1 (_rowid_ VARCHAR(255) NOT NULL); ATTACH ':memory:' AS db2; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK;
```

---

## Crash 65: `8f8a38ba883fcd07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097834`

```sql
CREATE TABLE t1 (_rowid_ INTEGER CHECK (RAISE(IGNORE) IN (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c3, c3);
```

---

## Crash 66: `3a925e60679b2c93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099475`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 DATE PRIMARY KEY DESC, _rowid_ BOOLEAN UNIQUE); DROP TABLE t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 67: `17ae941bb2e71c93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100623`

```sql
CREATE TABLE t2 (c2 NUMERIC COLLATE NOCASE, CHECK (FALSE), PRIMARY KEY (c2)); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 68: `77a89c6a07c5d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100751`

```sql
CREATE TABLE t2 (c3 NUMERIC NOT NULL, CHECK (RAISE(IGNORE)), UNIQUE (c3) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 69: `d57dd57a70268379` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102036`

```sql
CREATE TABLE t2 (c3 DATE PRIMARY KEY ASC, CHECK (CURRENT_TIMESTAMP), CHECK (_rowid_)); PRAGMA foreign_keys=ON; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ATTAC
```

---

## Crash 70: `327fe26d6ef3a1fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104348`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ FLOAT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); DETACH db2;
```

---

## Crash 71: `ab39692b6b049f5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104468`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ FLOAT COLLATE NOCASE); ANALYZE; ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 72: `4b076a2368f71c15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104657`

```sql
CREATE TABLE IF NOT EXISTS t1 (_rowid_ FLOAT COLLATE NOCASE); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 73: `1824d77c8c448dbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104685`

```sql
CREATE VIEW v1 AS WITH t2 AS (SELECT ALL *) SELECT RAISE(IGNORE) AS xdi__8_06_w5_chm_____4____r3w_n FROM t3 NOT INDEXED LIMIT CURRENT_TIME LIKE TRUE, CAST(RAISE(IGNORE) AS TEXT) ISNULL; CREATE VIRTUAL
```

---

## Crash 74: `ff75f6ef775ea15c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121939`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ATTACH ':memory:' AS db2;
```

---

## Crash 75: `b9840633defb4eaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121986`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 76: `6969f7581b0e3279` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122034`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 77: `37099264e2aa877e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123048`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 78: `60aafc1e77b6bc9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123141`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 79: `94257d9a36ddf5e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124243`

```sql
CREATE TABLE t2 (c1 NUMERIC PRIMARY KEY DESC, CHECK (CURRENT_TIME)); INSERT INTO t2 VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, 
```

---

## Crash 80: `83e17a70befabf06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125117`

```sql
CREATE TABLE t2 (c1 NUMERIC PRIMARY KEY DESC, CHECK (CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 81: `190465993428a037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125559`

```sql
CREATE TABLE t2 (_rowid_ DATE NOT NULL DEFAULT 16208, CHECK (RAISE(IGNORE) COLLATE NOCASE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 82: `5c59533539ee01b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126541`

```sql
CREATE TABLE t2 (rowid INTEGER PRIMARY KEY ASC, c2 INT GENERATED ALWAYS AS (c2) STORED, CHECK (CURRENT_TIME)); REINDEX t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABL
```

---

## Crash 83: `eee5e6f018ba4142` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126568`

```sql
CREATE TABLE t2 (rowid INTEGER PRIMARY KEY ASC, c2 INT GENERATED ALWAYS AS (c2) STORED, CHECK (CURRENT_TIME)); DELETE FROM t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE 
```

---

## Crash 84: `b84f2c1ad71cd36f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136542`

```sql
SELECT ALL CURRENT_DATE AS a ORDER BY CURRENT_DATE DESC, +RAISE(IGNORE) DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 85: `cfd936952f6417f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136618`

```sql
SELECT ALL CURRENT_DATE AS a ORDER BY CURRENT_DATE DESC, CURRENT_TIME DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 86: `b98012b3d6a4d1a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137335`

```sql
SELECT ALL TRUE || NULL ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 87: `fbce3e39d87bf86d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138626`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 88: `e177373985c8671b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139325`

```sql
ATTACH ':memory:' AS db2; DETACH db2; CREATE TABLE t3 (c1 NUMERIC PRIMARY KEY DESC) WITHOUT ROWID; ATTACH DATABASE ':memory:' AS db2; CREATE UNIQUE INDEX idx1 ON t3 (c1); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 89: `0e1305715e415d7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150629`

```sql
CREATE TABLE t1 (_rowid_ INT PRIMARY KEY, c3 TEXT UNIQUE, c2 DATE NOT NULL) WITHOUT ROWID; DELETE FROM t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 VALUES (~NULL << TRU
```

---

## Crash 90: `590e90a23701d66b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153466`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid FLOAT NOT NULL REFERENCES t1 (c2) NOT DEFERRABLE INITIALLY IMMEDIATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DELETE FROM t2 WHERE CASE WHEN CAS
```

---

## Crash 91: `de025151b9a94cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156804`

```sql
CREATE TABLE t3 (c1 BLOB GENERATED ALWAYS AS (TRUE) STORED, rowid BOOLEAN PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, _rowid_, c3);
```

---

## Crash 92: `69a202f3558b14a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158697`

```sql
CREATE TABLE t1 AS SELECT 14480.4752292E+34; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 93: `37794462a4911c10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158732`

```sql
CREATE TABLE t1 AS SELECT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 94: `fa7e6c9b433d1a6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158738`

```sql
CREATE TABLE t1 AS SELECT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 95: `7429c7c967acdb83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165605`

```sql
CREATE TABLE t2 (_rowid_ TEXT UNIQUE, c2 INT GENERATED ALWAYS AS (c2) STORED); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 96: `c5595ceff6ef25e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166215`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DROP INDEX IF EXISTS idx1;
```

---

## Crash 97: `2c87a7bcd8d36d10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166780`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (rowid FLOAT NOT NULL REFERENCES t1 (c2) NOT DEFERRABLE INITIALLY IMMEDIATE, c1 INTEGER NOT NULL); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 98: `2806a01e7adb32b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170461`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c1);
```

---

## Crash 99: `df0b69413d6e48c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176608`

```sql
CREATE TABLE t1 AS SELECT CURRENT_TIME NOT IN (CURRENT_TIMESTAMP IN (VALUES (CURRENT_DATE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 100: `a0c104a96cb6e325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176706`

```sql
CREATE TABLE t1 AS SELECT CURRENT_TIME NOT IN (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---
