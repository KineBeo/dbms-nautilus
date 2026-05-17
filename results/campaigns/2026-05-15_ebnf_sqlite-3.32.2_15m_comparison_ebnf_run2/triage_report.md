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

## Crash 1: `efe26d046434eeb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000534`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 2: `2ef930fe5adef32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000705`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c2, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, rowid);
```

---

## Crash 3: `67e26bbe01218b6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003023`

```sql
CREATE TABLE t3 (c1 VARCHAR(255) COLLATE NOCASE, rowid FLOAT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 4: `b5b58e50e5e5b601` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003090`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 5: `6a7ad766dfbaf38c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003112`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); DELETE FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 6: `8d01ca4c1af2877d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003175`

```sql
CREATE TABLE t3 (c1 VARCHAR(255) COLLATE NOCASE, _rowid_ INT NOT NULL); DELETE FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 7: `6ac1fcb8899e5fad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003189`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 8: `87915f8606143b0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003196`

```sql
CREATE TABLE t3 (rowid FLOAT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 9: `fa95139034bac8a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004292`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 10: `1f951887f137c626` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004914`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN IMMEDIATE; ATTACH ':memory:' AS db2; ALTER TABLE t3 DROP COLUMN c1; I
```

---

## Crash 11: `b3c60d975606a343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005363`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 12: `edf8c6b84a5131cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, 
```

---

## Crash 13: `83dddd305ad407e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008502`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 14: `535d399ef44dceee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008615`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rt
```

---

## Crash 15: `683a6ba403190731` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008890`

```sql
PRAGMA synchronous=NORMAL; VACUUM; BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 16: `fdefa14071235c31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008920`

```sql
VACUUM; VACUUM; BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 17: `2a0a7c75fc774da3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008975`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 U
```

---

## Crash 18: `eed25114d7f4bb9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009856`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, c3);
```

---

## Crash 19: `a99098084824a8ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010324`

```sql
PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 20: `b004caed2cde9649` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010436`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 21: `b8ae83f7aa136068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012636`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 22: `a17a0841fe6894e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013369`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rt
```

---

## Crash 23: `a07fd2af1055d7ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013485`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x
```

---

## Crash 24: `f018601a65bbeb45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013627`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 25: `716100ededc5e346` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016285`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, c2, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 26: `6da740ed15f8d4b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017328`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USI
```

---

## Crash 27: `e3705c9457bc55a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017917`

```sql
VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 28: `4696c98d1c10cf26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020587`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 29: `32ca481d5a4ac280` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022560`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 30: `3d5612a946b54453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025077`

```sql
VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 31: `77030a16b42b43d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026386`

```sql
PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REINDEX t2;
```

---

## Crash 32: `fb57c643e2680343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032031`

```sql
PRAGMA cache_size=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowid_);
```

---

## Crash 33: `3cd02b74c6e4a6a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036171`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); DELETE FROM t2 RETURNING CASE WHEN CURRENT_DATE < total_changes() + TRUE IS NOT DISTINCT FROM NULL THEN RAISE(IGN
```

---

## Crash 34: `70b49b9d969dbf12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036421`

```sql
CREATE TABLE t3 AS VALUES (CASE WHEN CURRENT_DATE THEN CURRENT_TIME ELSE CURRENT_DATE END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 35: `a85a8d9c8837fbcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036452`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 36: `d6ccf4e07a1940e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036461`

```sql
CREATE TABLE t3 AS VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 37: `0eb5fbd81c1dcfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036467`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 38: `92634188de61d3cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040489`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIMESTAMP); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 39: `e39531954ceb1cec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041879`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1,
```

---

## Crash 40: `717d06b42e068be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042065`

```sql
CREATE TABLE t2 (_rowid_ REAL PRIMARY KEY ASC, c1 INTEGER UNIQUE, UNIQUE (_rowid_, c1), CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE I
```

---

## Crash 41: `10fdf0d55f066d7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042205`

```sql
CREATE TEMP TABLE t3 (c1 NUMERIC COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TA
```

---

## Crash 42: `c8a9787b42d35378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042212`

```sql
CREATE TABLE t2 (_rowid_ REAL PRIMARY KEY ASC, c1 INTEGER UNIQUE, UNIQUE (c1), CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 43: `83571631ba4ff30f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047287`

```sql
VALUES (934891732896935385695535894866832.6); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2);
```

---

## Crash 44: `c4bd92a436bf332f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047603`

```sql
VALUES (TRUE || FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 45: `6313d27829a5c520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048690`

```sql
SELECT ALL CURRENT_DATE % FALSE AS sov8o__b_p_66ijs1_n7v_y; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_);
```

---

## Crash 46: `6f957ebe54d82f7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049523`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 WHERE NULL GROUP BY FALSE WINDOW w1 AS (PARTITION BY CURRENT_TIME ORDER BY TRUE ASC NULLS FIRST ROWS BETWEEN CURRENT ROW AND CURRENT_TIMESTAMP FOL
```

---

## Crash 47: `5c0e01e3836c8799` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049635`

```sql
CREATE TEMP VIEW v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 48: `b93c9e4f54db3233` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049643`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 WHERE NULL GROUP BY FALSE WINDOW w1 AS () ORDER BY CURRENT_DATE NULLS FIRST LIMIT RAISE(IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 49: `b8ad6e25fc245e49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049650`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 WHERE NULL GROUP BY FALSE WINDOW w1 AS (PARTITION BY CURRENT_TIME ORDER BY TRUE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW E
```

---

## Crash 50: `a622f06b46fd870c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050211`

```sql
CREATE VIEW v1 AS SELECT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); PRAGMA synchronous=OFF;
```

---

## Crash 51: `edc1231e9c109a8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052926`

```sql
CREATE TABLE t1 (rowid NUMERIC PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 52: `e36d4e3ab3d9c7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053593`

```sql
CREATE TABLE t1 (rowid INTEGER PRIMARY KEY) WITHOUT ROWID; BEGIN TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 53: `14174861f0cb1eca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055927`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, 
```

---

## Crash 54: `45df63f11a85e9fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058224`

```sql
BEGIN; CREATE TEMP TABLE IF NOT EXISTS t1 (c1 DATE PRIMARY KEY); COMMIT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ATTACH DATABASE ':memory:' AS db2; ALTER TABLE t1 ADD COLUMN c2 
```

---

## Crash 55: `763202233bf7b5c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059765`

```sql
SELECT DISTINCT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t1 AS NOT MATERIALIZED (SELECT DISTINCT * ORDER BY NULL ASC NULLS FIRST) SELECT *, * FROM t3 NOT INDEXED 
```

---

## Crash 56: `175d8586ae56f88c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061295`

```sql
CREATE VIEW v1 (c3) AS SELECT total_changes() FILTER (WHERE FALSE) OVER () FROM t2 NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TAB
```

---

## Crash 57: `e7851022b9806797` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064796`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 58: `8a06fdcd93dbb68c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066315`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 59: `e4aba38d66e344f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066544`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 60: `926bf051da720992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068290`

```sql
CREATE TABLE t3 (_rowid_ INT NOT NULL); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 61: `8510b4f47992b8db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068417`

```sql
CREATE TABLE t3 (_rowid_ INT NOT NULL); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT JOIN t3 NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1,
```

---

## Crash 62: `e6630096bbc93083` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073144`

```sql
CREATE TABLE t1 (rowid VARCHAR(255) UNIQUE, _rowid_ NUMERIC UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2)
```

---

## Crash 63: `b1e96bc5e23a214c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077978`

```sql
PRAGMA analysis_limit=-60423; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 64: `af58744669b602ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078049`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 65: `18c347b38e3f1c2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080863`

```sql
CREATE VIEW IF NOT EXISTS v1 (rowid, rowid) AS SELECT DISTINCT ~RAISE(IGNORE) * TRUE GLOB TRUE << TRUE AS e_, *, * EXCEPT SELECT ALL * FROM t3 NATURAL CROSS JOIN t2 NOT INDEXED USING (c2, rowid); CREA
```

---

## Crash 66: `cb3e544d6343ec11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080889`

```sql
BEGIN EXCLUSIVE; CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY TRUE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 67: `cb9a8ecbfb9596b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080903`

```sql
CREATE TABLE t3 AS VALUES (-count(DISTINCT CURRENT_DATE) FILTER (WHERE NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 68: `a376bd8e0c31d71a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080921`

```sql
BEGIN EXCLUSIVE; CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY 934891732896935385695535894866832.6 DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS)); CREATE VIRTUAL TABLE 
```

---

## Crash 69: `6e058f2275073ad9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080935`

```sql
CREATE TABLE t3 AS VALUES (FALSE IS NULL + TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TA
```

---

## Crash 70: `952d260e2dc3029b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080951`

```sql
BEGIN EXCLUSIVE; VALUES (CURRENT_DATE IS TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 71: `ba3f6a2299b88ddc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081018`

```sql
BEGIN EXCLUSIVE; ROLLBACK TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 72: `573919e6371194dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082924`

```sql
CREATE TABLE t3 (c2 INT NOT NULL REFERENCES t3 (_rowid_) ON DELETE CASCADE, UNIQUE (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); BEGIN EXCLUSIVE TRANSACTION; DELETE FROM t2 WHERE NO
```

---

## Crash 73: `30fad073b89f55b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083782`

```sql
CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * ORDER BY FALSE ASC NULLS FIRST, TRUE ASC NULLS LAST LIMIT RAISE(IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 74: `93e29cc60e926a83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084116`

```sql
CREATE TABLE t3 (c3 NUMERIC PRIMARY KEY DESC, FOREIGN KEY (c3) REFERENCES t1 (c2) ON DELETE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 75: `80d19734c4389abb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084587`

```sql
CREATE TABLE t3 (_rowid_ INT PRIMARY KEY DESC, UNIQUE (_rowid_) ON CONFLICT IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 76: `ec0ec25d1eacd73d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087092`

```sql
PRAGMA synchronous=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 77: `c75bb1496000f730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089966`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY ASC, CHECK (CURRENT_TIME >= RAISE(IGNORE))); PRAGMA analysis_limit=+0; BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 78: `549382a4566cb5a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092345`

```sql
CREATE TABLE t3 (c2 REAL COLLATE NOCASE, UNIQUE (c2)); BEGIN IMMEDIATE; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ALTER TABLE t2 RENAME COLUMN c1 TO c3; CREATE TRIGGER trg1 I
```

---

## Crash 79: `e454ae68e7dab4ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092630`

```sql
CREATE TABLE t3 (c2 INT NOT NULL REFERENCES t3 (_rowid_) ON DELETE CASCADE, UNIQUE (c2)); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 80: `298aa1f4f36921a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096540`

```sql
SELECT ALL X'B34f7ADb8EeF'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 81: `8eda3c18cda28952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102284`

```sql
CREATE TABLE t3 (_rowid_ INT NOT NULL); CREATE TRIGGER trg1 AFTER INSERT ON t3 FOR EACH ROW WHEN RAISE(IGNORE) BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 82: `3c867a4683434fdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102496`

```sql
CREATE TABLE t3 (_rowid_ INT NOT NULL); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT JOIN t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, _rowid_);
```

---

## Crash 83: `8b8a5b7fdebdbb03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103010`

```sql
CREATE TABLE t3 (_rowid_ REAL GENERATED ALWAYS AS (NULL) VIRTUAL, c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT JOIN t3 NOT INDEXED; CREA
```

---

## Crash 84: `a3e6be93fe248dc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103493`

```sql
CREATE TABLE t3 (c3 NUMERIC DEFAULT -0); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ALTER TABLE t2 RENAME COLUMN rowid TO c1;
```

---

## Crash 85: `b73690354ccd98a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103595`

```sql
CREATE TABLE t3 (c3 NUMERIC DEFAULT CURRENT_TIME); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ALTER TABLE t2 RENAME COLUMN rowid TO c1;
```

---

## Crash 86: `24d2353f68ed210e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104408`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT JOIN (SELECT ALL *, * FROM t3) AS s_e52o__vmu; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 87: `61154ca353c8c078` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105298`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT * FROM (SELECT ALL * FROM t3) AS s_e52o__vmu; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 88: `09e57c34e6e05e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105848`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT * FROM (VALUES (FALSE)) AS s_e52o__vmu LEFT JOIN t3 ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 89: `fcdb1d69e098b7ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106434`

```sql
CREATE TABLE t3 (c2 INTEGER PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 90: `df94d070777036ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106600`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); CREATE TABLE t1 AS SELECT DISTINCT 0 FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 91: `d90b250996501a9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106846`

```sql
CREATE TABLE t3 (rowid VARCHAR(255) UNIQUE, _rowid_ NUMERIC UNIQUE); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 92: `b56ee16120287cba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110066`

```sql
CREATE TABLE t3 (c2 TEXT PRIMARY KEY); DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 93: `fc587e741a7a6a85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111333`

```sql
CREATE TABLE t3 (c1 VARCHAR(255) COLLATE NOCASE, rowid FLOAT GENERATED ALWAYS AS (FALSE) VIRTUAL); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 94: `50bd5cc408d8561b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112277`

```sql
CREATE TABLE t3 (c3 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 95: `1213455628fced0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113837`

```sql
CREATE TABLE t3 (c1 VARCHAR(255) COLLATE NOCASE, rowid FLOAT GENERATED ALWAYS AS (json_type(NULL)) VIRTUAL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t3 AS (WITH R
```

---

## Crash 96: `32786415455bf61d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118202`

```sql
VALUES (X'BbED43E5'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 97: `098252ed9ca7870f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118898`

```sql
VALUES (FALSE LIKE CURRENT_DATE <= FALSE ESCAPE FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 98: `491a31dfdbefb5a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120992`

```sql
BEGIN; CREATE TEMP TABLE IF NOT EXISTS t1 (c1 DATE PRIMARY KEY); COMMIT; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ROLLBACK; ANALYZE; BEGIN IMMEDIATE 
```

---

## Crash 99: `8199d6a99622acc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123231`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 VARCHAR(255) NOT NULL DEFAULT NULL, rowid TEXT PRIMARY KEY ASC); CREATE TABLE t1 AS SELECT DISTINCT * FROM t3 NOT INDEXED NATURAL LEFT JOIN t3 NOT INDEXED; CREATE VIR
```

---

## Crash 100: `76afbff720651b3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123883`

```sql
CREATE TEMP TABLE t2 (_rowid_ INT PRIMARY KEY DESC); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 101: `8ba1d524c3ebb2b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124290`

```sql
BEGIN EXCLUSIVE; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c1);
```

---

## Crash 102: `9a817df1bacf80da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128259`

```sql
CREATE TABLE t1 (c3 BOOLEAN PRIMARY KEY DESC, rowid BLOB UNIQUE) WITHOUT ROWID; CREATE UNIQUE INDEX idx1 ON t1 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, c3);
```

---

## Crash 103: `ccb3e70accde952f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128329`

```sql
CREATE TABLE t1 (c3 BOOLEAN PRIMARY KEY DESC, rowid BLOB UNIQUE) WITHOUT ROWID; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, c3);
```

---

## Crash 104: `025539b0753bc4f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128438`

```sql
CREATE TABLE t1 (c3 BOOLEAN PRIMARY KEY DESC, rowid BLOB UNIQUE) WITHOUT ROWID; PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 105: `c079f7d55efc6998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130678`

```sql
VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT CURRENT_TIME ORDER BY CURRENT_TIME ASC NULLS LAST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 106: `d13cbd0b65be57b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130949`

```sql
VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT CURRENT_TIME ORDER BY CURRENT_TIME COLLATE RTRIM ASC NULLS LAST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 107: `ed74f0ad2ab84d1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133382`

```sql
SELECT ALL TRUE NOT IN (-42871606581243443681219064989094.67089380770263879463576373556525960888575070709517122611249912758116800269540940212345052094502230917484591987140921779120656E+291202403798089
```

---

## Crash 108: `e7e75c3860039848` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133730`

```sql
SELECT ALL TRUE NOT IN (CURRENT_TIMESTAMP) AS sov8o__b_p_66ijs1_n7v_y; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y
```

---

## Crash 109: `8d5a4b5630a3baab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134557`

```sql
SELECT ALL TRUE NOT IN (NULL, NULL, FALSE) AS sov8o__b_p_66ijs1_n7v_y; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 110: `e8df42ff3bcad535` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136960`

```sql
VALUES (count(*), X'8FCcfF2bcEEd'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2, c3); INSERT INTO t1 VALUES (CASE WHEN substr(CURRENT_TIME, RAISE(IGNORE), CURRENT_TIME) FILTER (WHE
```

---

## Crash 111: `fe61bc4db7fa4ad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141830`

```sql
WITH RECURSIVE t2 AS (SELECT DISTINCT *) VALUES (CURRENT_DATE + FALSE) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN TRANSACTION;
```

---

## Crash 112: `5f356407cedd7db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141945`

```sql
WITH RECURSIVE t2 AS (SELECT DISTINCT *) VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN TRANSACTION;
```

---

## Crash 113: `e59dcff97905d05f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141951`

```sql
WITH RECURSIVE t2 AS (SELECT DISTINCT *) VALUES (TRUE) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN TRANSACTION;
```

---

## Crash 114: `0f409d4defa6d8f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142387`

```sql
WITH RECURSIVE t2 AS (SELECT DISTINCT *) SELECT ALL NULL AS hb_z UNION SELECT ALL 90.40E+178627057171226 AS hb_z; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 115: `def87467fd3b2b45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143143`

```sql
WITH RECURSIVE t2 AS (SELECT DISTINCT *) VALUES (FALSE) INTERSECT SELECT ALL NULL AS hb_z; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 116: `3ab419276ccebfca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151322`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY CURRENT_TIME NOT IN (CURRENT_TIME GLOB CURRENT_TIME) DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS)); BEGIN DEFERRED TRANSA
```

---

## Crash 117: `d99f5af68903a510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151372`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER ()); BEGIN DEFERRED TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK TO SAVEPOINT sp1; DROP TABLE t3; DROP TABLE t2;
```

---

## Crash 118: `a50acda060e253d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151381`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY CURRENT_TIME NOT IN (CURRENT_TIME) DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS)); BEGIN DEFERRED TRANSACTION; CREATE VIRT
```

---

## Crash 119: `12a818db2d4c8957` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153869`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER () NOT BETWEEN CURRENT_DATE AND count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 120: `726a2f411b7b800e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153917`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME NOT BETWEEN CURRENT_DATE AND count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 121: `d49d9cd66be8a99c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154290`

```sql
CREATE TABLE t3 AS VALUES (-2923); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); COMMIT;
```

---

## Crash 122: `628225a3209bf47d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154874`

```sql
CREATE TABLE t3 AS VALUES (NOT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 123: `79f2ef6432c6d733` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157797`

```sql
CREATE TABLE t3 AS SELECT DISTINCT '_ W38c1o '; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 124: `7d84fec0ed9ab500` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157914`

```sql
CREATE TABLE t3 AS SELECT DISTINCT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 125: `1a7e9f6c41385994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158273`

```sql
CREATE TABLE t3 AS SELECT total_changes() << CURRENT_TIMESTAMP % TRUE AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, 
```

---

## Crash 126: `70e01a71e86c25aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159360`

```sql
CREATE TABLE t3 AS VALUES (NULL AND NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 127: `e171098ac5d1c44e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161005`

```sql
CREATE TABLE t3 AS VALUES (-CURRENT_DATE < NULL || CURRENT_TIME % TRUE || FALSE LIKE CURRENT_TIMESTAMP ESCAPE FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 128: `1a5acf4cce7337de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163607`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_DATE + FALSE IS TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE VI
```

---

## Crash 129: `01769dce13cfdcae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163881`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_DATE + NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---
