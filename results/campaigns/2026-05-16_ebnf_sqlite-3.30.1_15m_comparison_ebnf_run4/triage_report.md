# Crash Triage Report

**Total crashes:** 103  
**Unique crash sites:** 103  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 102 | 102 | 99% |
| Signal | 1 | 1 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `0bbb09d3bd8149dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000068`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 2: `04642b00ce7ab8d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000726`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3, _rowid_, c2);
```

---

## Crash 3: `c66a8a7c5b21f84a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001178`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ATTACH DATABASE ':memory:' AS db2; CREATE TRIGGER trg1 AFTER INSERT ON t1 BEGIN SELECT t2.*, t1.*, tri
```

---

## Crash 4: `3aa4d17d187358e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001507`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 5: `341e53bef79154f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002477`

```sql
REINDEX; REINDEX; ATTACH DATABASE ':memory:' AS db2; DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); UPDATE t3 SET rowid = CASE WHEN (NULL) THEN (NULL) WHEN CURRENT_
```

---

## Crash 6: `1ee34c87dce72c5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005409`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 7: `c886ed608c1f3520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005695`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 8: `89ecf687723d0cd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005726`

```sql
CREATE VIEW v1 (c1) AS SELECT t3.*, CURRENT_TIME FROM t1 NATURAL LEFT OUTER JOIN t1 INDEXED BY c3 WHERE TRUE % CURRENT_TIMESTAMP EXCEPT SELECT t1.* LIMIT TRUE COLLATE BINARY OFFSET NULL REGEXP +RAISE(
```

---

## Crash 9: `2475c6b2bbe2317f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006113`

```sql
DROP TABLE IF EXISTS t2; PRAGMA cache_size=+6707; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 10: `9e88af569d57b64c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007265`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, c1, c2);
```

---

## Crash 11: `1d453b6582e13bbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007296`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 12: `f25a805752a90712` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007302`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 13: `56827c41558558e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007310`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 14: `c3f40f621c515405` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007489`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 15: `492100c3dc1671ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008546`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); COMMIT;
```

---

## Crash 16: `9c12cbe8b8fa1be4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009788`

```sql
CREATE VIEW v1 (c3) AS SELECT ALL * UNION SELECT DISTINCT * FROM t2 WHERE EXISTS (SELECT ALL *) ORDER BY RAISE(IGNORE) DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT
```

---

## Crash 17: `141c6afa66392dae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009877`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (ifnull(RAISE(IGNORE) > CURRENT_DATE COLLATE NOCASE NOT NULL, TRUE <> CURRENT_DATE ISNULL) / CURRENT_DATE COLLA
```

---

## Crash 18: `88ac9dfa264f2808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009883`

```sql
CREATE VIEW v1 AS VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (ifnull(RAISE(IGNORE) > CURRENT_DATE COLLATE NOCASE NOT NULL, TRUE <> CURRENT_D
```

---

## Crash 19: `2c9becb43feab857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011730`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, c1);
```

---

## Crash 20: `531f9cd4be5b811c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016400`

```sql
PRAGMA journal_mode=MEMORY; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3); INSERT OR IGNORE INTO t1 VALUES (CASE ~RAISE(IGNORE) NOT BETWEEN CURRENT_DATE
```

---

## Crash 21: `4f2b9f8fb306f785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016438`

```sql
PRAGMA quick_check; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3); INSERT OR IGNORE INTO t1 VALUES (CASE ~RAISE(IGNORE) NOT BETWEEN CURRENT_DATE COLLATE
```

---

## Crash 22: `9dbf64e676ad904e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017101`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 23: `faa3b07eb572bb43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018377`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 24: `fdd823914c25e00d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018775`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED ON changes() FILTER (WHERE RAISE(IGNORE)) OVER (ORDER BY RAISE(IGNORE) ASC NULLS FIRST RANGE BETWEE
```

---

## Crash 25: `01652b967ae52332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018797`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 26: `ed595baec9364787` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018803`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 27: `0506868453378f16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018813`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED USING (_rowid_) ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 28: `55dac3e51e2efda1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018820`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED ON changes() FILTER (WHERE RAISE(IGNORE)) OVER () ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 29: `2d5d098ca3239645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018935`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED USING (_rowid_) ORDER BY NULL NULLS LAST; VACUUM; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 30: `c53413e2201d8dde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019243`

```sql
CREATE VIEW IF NOT EXISTS v1 (c1) AS SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED ON changes() FILTER (WHERE RAISE(IGNORE)) OVER (ORDER BY RAISE(IGNORE) ASC NULLS FIRST ROWS BETWEEN
```

---

## Crash 31: `01210571f7b64ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019511`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 32: `b3c60d975606a343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019787`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 33: `03c9da7724be11ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020167`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 34: `03af8948b33926ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022814`

```sql
CREATE TABLE t3 (rowid INTEGER PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 35: `e334f1763a31073b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025769`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE TEMP VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t2 AS (SELECT DISTINCT *) SELECT DISTINCT NULL AS a, * ORDER BY RAISE(IGN
```

---

## Crash 36: `2236a79daafba596` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030013`

```sql
CREATE TABLE t2 (rowid INT UNIQUE, c2 TEXT PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 37: `7d040ae41cbf1f4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034083`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, rowid); PRAGMA cache_size=-8; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c3);
```

---

## Crash 38: `aea2aafd6266c6bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038137`

```sql
VALUES (count(DISTINCT FALSE) FILTER (WHERE CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 39: `d3e7cf99079012ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038189`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 40: `3855be5c10bb17f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039405`

```sql
CREATE TABLE t2 (c1 INT CHECK (RAISE(IGNORE)), c2 TEXT PRIMARY KEY DESC); VACUUM INTO ':memory:'; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 41: `b1eb6f8bf79bf9db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044794`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 42: `bf76fc71d1ba9fd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044923`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 43: `852f4431e9d71823` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049001`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); REINDEX t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); CREATE INDEX idx1 ON t1 (rowid) WHERE CASE WHEN (VALUES 
```

---

## Crash 44: `037d4658ad2d3abd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049189`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid TEXT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 45: `a931896e68805a07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051428`

```sql
WITH t3 AS (SELECT *) VALUES (TRUE) UNION ALL SELECT ALL CURRENT_TIMESTAMP AS hf1_f585a_812_1l3__p4_r964__2___5__7_98__xoi__89_1_1_d_7a_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 46: `771cf6b3c9f6e17c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054023`

```sql
CREATE TABLE t2 (c1 INT CHECK (CURRENT_TIMESTAMP), c2 TEXT PRIMARY KEY DESC); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 47: `bcd9c81b464dc56d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055140`

```sql
CREATE TEMP TABLE t2 (c2 REAL PRIMARY KEY, c1 TEXT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 48: `a9e7972ac1d455c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055618`

```sql
CREATE TABLE t3 (rowid VARCHAR(255) COLLATE NOCASE, c1 REAL, FOREIGN KEY (rowid, c1) REFERENCES t3 (c3, c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1);
```

---

## Crash 49: `69e9684827dff0a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055687`

```sql
CREATE TABLE t3 (rowid VARCHAR(255) COLLATE NOCASE, c1 REAL, CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1);
```

---

## Crash 50: `3b17d15de04fc70e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056553`

```sql
CREATE TABLE t3 (rowid TEXT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 51: `e2a4c9e701b38774` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058179`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 52: `0eb7e0fc066aad67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064862`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); WITH RECURSIVE t1 AS (WITH RECURSIVE t1 (rowid) AS (SELECT DISTINCT *) VALUES (CURRENT_DATE) UNION VALUES 
```

---

## Crash 53: `1c37b8153273ba8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079940`

```sql
BEGIN DEFERRED; ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c3);
```

---

## Crash 54: `f3f72583ae595270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080928`

```sql
CREATE TEMP TABLE t2 (c3 FLOAT PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); VACUUM INTO ':memory:';
```

---

## Crash 55: `b7978fddb0aaed2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081473`

```sql
CREATE TEMP TABLE t2 (c3 TEXT NOT NULL REFERENCES t1 (_rowid_) ON UPDATE SET NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK TO sp1; CREATE TRIGGER trg1 AFTER INSERT ON t2 FO
```

---

## Crash 56: `abbe414b51306dfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084089`

```sql
CREATE TEMP TABLE t2 (c2 VARCHAR(255) PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 57: `1992caae5a5df57f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086573`

```sql
WITH t1 AS (VALUES (FALSE)) SELECT ALL * FROM t1 INTERSECT SELECT TRUE AS n1_n5__27___65_zqp7_ne_4_c__5 ORDER BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---

## Crash 58: `53a9af887d0a8446` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091846`

```sql
PRAGMA journal_mode=TRUNCATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 59: `557d00b79732f1cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115012`

```sql
CREATE TABLE t3 (_rowid_ INT UNIQUE, PRIMARY KEY (_rowid_)); CREATE TRIGGER trg1 AFTER INSERT ON t3 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK;
```

---

## Crash 60: `a98dd00997020c6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115647`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid BLOB PRIMARY KEY DESC); REPLACE INTO t3 VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c3);
```

---

## Crash 61: `dbdcf896b183ed3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118731`

```sql
CREATE TABLE t2 (_rowid_ REAL); UPDATE OR FAIL t2 SET rowid = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 62: `81f62c8e41e7fbcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118762`

```sql
CREATE TABLE t2 (_rowid_ REAL); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 63: `0a13c193fab70029` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122657`

```sql
WITH t3 AS (SELECT *) VALUES (TRUE) INTERSECT SELECT ALL CURRENT_TIMESTAMP AS hf1_f585a_812_1l3__p4_r964__2___5__7_98__xoi__89_1_1_d_7a_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 64: `a74a208d2199590d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124652`

```sql
CREATE TABLE t3 (rowid INT UNIQUE, c2 TEXT PRIMARY KEY DESC) WITHOUT ROWID; REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2, c2, c3);
```

---

## Crash 65: `c8a9e7d6131914a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129792`

```sql
WITH RECURSIVE t2 AS (VALUES (RAISE(IGNORE))) SELECT ALL (CASE ~CAST('_ETAD-FR a72-L--- 8' COLLATE NOCASE AS VARCHAR(255)) NOT NULL IS NOT NULL WHEN (CURRENT_DATE, RAISE(IGNORE) >= NULL IS CURRENT_TIM
```

---

## Crash 66: `4e032b2541529678` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129879`

```sql
WITH RECURSIVE t2 AS (VALUES (RAISE(IGNORE))) SELECT ALL RAISE(IGNORE) NOT IN (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BI
```

---

## Crash 67: `988ab30579c519b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129887`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 68: `d5fe2235a63b1e15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130662`

```sql
VALUES (434.3414694993E-04209556102019421196087406333724134490611308998588209122450595197933977814198597259117961798418386806874073797250103760924); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 69: `dcc1ee2973994a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135815`

```sql
CREATE TEMP TABLE t3 (_rowid_ DATE NOT NULL DEFAULT -317518); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 70: `af2a2a42f3f499c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135824`

```sql
CREATE TEMP TABLE t3 (_rowid_ DATE NOT NULL DEFAULT -317518); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 71: `6bbdd6ec0e31a18c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147835`

```sql
CREATE TEMP TABLE t1 (_rowid_ BLOB NOT NULL DEFAULT -97794836044974861780956695561749648314344068960064834755518514732645403883490388377069922709608983.85883252460715472185e+20474684808996257097757531
```

---

## Crash 72: `1c5d197cb5ad1bb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148359`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 73: `b068068b520d1b8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148501`

```sql
BEGIN IMMEDIATE TRANSACTION; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 74: `8a47a2ebf8586449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150146`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; ROLLBACK TO SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 75: `5a5d3c94a9fe0ca9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151058`

```sql
CREATE TABLE t2 (_rowid_ DATE PRIMARY KEY ASC, UNIQUE (_rowid_) ON CONFLICT ROLLBACK); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2);
```

---

## Crash 76: `47f45e0ce24b532a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151450`

```sql
PRAGMA cache_size=+0; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); PRAGMA foreign_keys=1; PRAGMA analysis_limit=+651;
```

---

## Crash 77: `cf314fdf8fc04a57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151820`

```sql
CREATE TABLE t3 (c1 NUMERIC NOT NULL REFERENCES t1 (c3) ON UPDATE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 78: `fe3cc270fc0152ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157230`

```sql
VALUES (count(DISTINCT 434.3414694993E-04209556102019421196087406333724134490611308998588209122450595197933977814198597259117961798418386806874073797250103760924) FILTER (WHERE CURRENT_DATE)); CREATE 
```

---

## Crash 79: `49efd2c90f672f57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157298`

```sql
VALUES (count(DISTINCT NULL) FILTER (WHERE CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 80: `4ed2edfa9007151f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158972`

```sql
CREATE TABLE t2 (c3 FLOAT UNIQUE); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 81: `1fb6cb4acef5b968` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159130`

```sql
CREATE TABLE t2 (c3 FLOAT UNIQUE); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c1, c1, c3, _rowid_, c3);
```

---

## Crash 82: `2d43b7c75162b5d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160286`

```sql
CREATE TABLE t2 (c1 INT CHECK (NULL MATCH NULL), rowid INTEGER PRIMARY KEY AUTOINCREMENT); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2); PRAGMA foreig
```

---

## Crash 83: `f3970760c66e7efc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162617`

```sql
CREATE TABLE t2 (_rowid_ REAL CHECK (FALSE)); DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 84: `7cfb1697d966f2f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164194`

```sql
CREATE TEMP TABLE t3 (_rowid_ DATE NOT NULL DEFAULT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 85: `863450f89136121d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172321`

```sql
SELECT DISTINCT * FROM t1 NOT INDEXED CROSS JOIN t2 NOT INDEXED ON changes() FILTER (WHERE RAISE(IGNORE)) OVER () INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNOR
```

---

## Crash 86: `8940765aa293b092` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172327`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) == CASE CURRENT_TIMESTAMP WHEN RAISE(IGNORE) THEN FALSE END COLLATE BINARY ASC; COMMIT;
```

---

## Crash 87: `7a1499ed38be7449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172334`

```sql
VALUES (CURRENT_TIMESTAMP / FALSE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 88: `be81d7d8f6773e3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172343`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t1 , t1 USING (c2, _rowid_) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 89: `19acfd9f7dae526f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172350`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY changes() FILTER (WHERE RAISE(IGNORE)) OVER (ORDER BY RAISE(IGNORE) ASC NULLS FIRST ROWS RAISE(IGNORE) 
```

---

## Crash 90: `d70c56d874290f07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172364`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t1 NOT INDEXED NATURAL LEFT JOIN t3 USING (c2, c1) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 91: `643e555b4772053a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172370`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY CURRENT_DATE NOT BETWEEN TRUE AND FALSE AND 0 COLLATE BINARY ASC; COMMIT;
```

---

## Crash 92: `4b757835449e67ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172376`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t1 AS ny781_6_72_244n_____mxb6tq_9n_8oi9i41ussdzm4_j1_s___2x6z_m55d_7z4c GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC;
```

---

## Crash 93: `c51279a586c95e1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172397`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (SELECT ALL *) AS c___ GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 94: `4a1a24e4380dc40b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172403`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (t2) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 95: `b520ba9b4f38a1a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172412`

```sql
VALUES (count(*) NOT LIKE count(*)) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 96: `731d45b066a1edee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172424`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS (), w2 AS (ORDER BY CURRENT_TIME ROWS BETWEEN CURRENT_TIMESTAMP PRECEDING AND CURRENT ROW) ORDER BY RAISE(IGNORE) C
```

---

## Crash 97: `257c3d1decd1afa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172438`

```sql
SELECT * FROM t3 NOT INDEXED LEFT JOIN t1 NOT INDEXED ON FALSE WHERE CURRENT_TIMESTAMP GROUP BY TRUE, CURRENT_DATE HAVING RAISE(IGNORE) INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS (
```

---

## Crash 98: `6bdfc0b6620f5572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172498`

```sql
SELECT (CASE WHEN RAISE(IGNORE) IN (SELECT * FROM t3 NOT INDEXED WHERE RAISE(IGNORE) NOTNULL) + NULL NOT BETWEEN CURRENT_TIMESTAMP AND NULL THEN NULL COLLATE BINARY END >= CASE TRUE WHEN CURRENT_TIMES
```

---

## Crash 99: `9b317595de8dd779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172527`

```sql
SELECT t3.* FROM t2 NOT INDEXED CROSS JOIN t3 NOT INDEXED INNER JOIN t2 NOT INDEXED INTERSECT SELECT * FROM t3 GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 100: `94366659a00a933d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172539`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM t1 NOT INDEXED NATURAL CROSS JOIN t3 NOT INDEXED GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE BINARY ASC; COMMIT;
```

---

## Crash 101: `872ef5d6617e517f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175431`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); CREATE TABLE t3 (c3 BOOLEAN PRIMARY KEY ASC, rowid BLOB REFERENCES t1 (c2) ON UPDATE SET NULL) WITHOUT ROWID,
```

---

## Crash 102: `b1bcd915f780a4a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178424`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2);
```

---

## Crash 103: `8bc28dd6c969fd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000172475`

```sql
VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (SELECT t2.*, t3.* FROM t2 INDEXED BY rowid WHERE upper(CURRENT_TIMESTAMP = CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP NOTNULL) OVER (ORDER BY CUR
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  yy_reduce
  sqlite3Parser
```

---
