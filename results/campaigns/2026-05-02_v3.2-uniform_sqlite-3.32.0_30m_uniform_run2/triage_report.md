# Crash Triage Report

**Total crashes:** 320  
**Unique crash sites:** 320  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 320 | 320 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `a4a469519a0f2040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000042`

```sql
SELECT printf('%lli', 2147483647, '_O_Y-k  oU'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BOOLEAN GENERATED ALW
```

---

## Crash 2: `53b28bcbdd5d04e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000158`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (FALSE REGEXP TRUE, CASE CURRENT_DATE WHEN NULL ISNULL THEN CURRENT_TIME IS FALSE END, FALSE); ANALYZE p; SELECT 
```

---

## Crash 3: `447f6a780d236936` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000754`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO r VALUES (CURRENT_DATE + CURRENT_DATE BETWEEN CURRENT_TIME AND CURRENT_DATE NOT IN (VALUES (CURRENT_DATE COLLATE RTRIM)), +CASE
```

---

## Crash 4: `f59465f8c61e9118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000916`

```sql
SELECT printf('%.*e', 4294967296, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, q.*, avg(NULL) AS q10__v_c___wd9rn_, p.*, TRUE << CURRENT_TIMESTAMP IN (SELECT CURRENT_DA
```

---

## Crash 5: `6e56f9c62d50ea16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000977`

```sql
SELECT round(1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (b, a) VALUES (q.c2); SELECT CURRENT_TIMESTAMP IS NOT (NULL NOTNULL IN (NOT EXISTS (SELECT *, *
```

---

## Crash 6: `08ebd2b0593557db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001064`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, _rowid_, b, c1, c2, c2); INSERT OR ROLLBACK INTO p VALUES (RAISE(FAIL, 'w_- _  _') + t2.c2 BETWEEN CURRENT_DATE NOT IN (SELECT NULL AS m ORD
```

---

## Crash 7: `c1e0b132c311274f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001153`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (TRUE, CURRENT_DATE NOT NULL == CURRENT_TIMESTAMP IS NULL <> CASE WHEN CURRENT
```

---

## Crash 8: `e66b546316b2e023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001765`

```sql
SELECT substr('', -1, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 VALUES (RAISE(IGNORE) IS CURRENT_DATE ISNULL) RETURNING RAISE(IGNORE) AS f2d; SELECT (SELECT
```

---

## Crash 9: `cf2ef69178413dc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT TRUE FROM t1 NOT INDEXED WHERE CAS
```

---

## Crash 10: `6a8820e84d18696d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002739`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT, r
```

---

## Crash 11: `d3f2252018527b5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003216`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT p.* ORDER BY CURRENT_TIME LIKE CURRENT_TIMESTAMP ESCAPE ~CURRENT_TIMESTAMP - CURRENT_TIMES
```

---

## Crash 12: `b56bd249c28581e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003943`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT ALL RAISE(IGNORE) FROM r NOT INDEXED ORDER BY CURRENT_TIME ASC LIMIT NOT
```

---

## Crash 13: `19c5f713c4d0cc8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004117`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%.*f', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT ALL * FROM t2 NOT INDEXED; SELECT q.*, p.*, * FROM p
```

---

## Crash 14: `1199608ee98c5167` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004140`

```sql
SELECT round(-1.0, 4294967295); SELECT printf('%.*f', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (TRUE); SELECT q.*, p.*, * FROM p NATURAL JOI
```

---

## Crash 15: `ddf82bcb5e4d6622` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004717`

```sql
SELECT printf('%.*f', 9223372036854775807, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (ifnull(CASE RAISE(IGNORE) NOTNULL WHEN CURRENT_DATE NOT BETWEEN NULL A
```

---

## Crash 16: `cb91e5d7f2eff021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005882`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO p VALUES (NULL); EXPLAIN QUERY PLAN SELECT ALL NULL | CURRENT_DATE | NULL NOT NULL AS
```

---

## Crash 17: `d0197b71f488a38f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007507`

```sql
SELECT printf('%.*g', -2147483649, 0.01); SELECT printf('%u', -2147483649, '-P_nht-- c8_U h');
```

---

## Crash 18: `69f7ce282bae415f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007557`

```sql
SELECT printf('%.*g', 9223372036854775807, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO t3 VALUES ((CURRENT_TIMESTAMP)); SELECT (CURRENT_TIME) LIKE NULL ESCAPE
```

---

## Crash 19: `2cf47534a7748357` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008206`

```sql
SELECT printf('%.*f', 9223372036854775807, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1, c2); VALUES (FALSE); SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 20: `1b4281b617788031` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009880`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM q CROSS JOIN p NOT INDEXED ON -CURRE
```

---

## Crash 21: `77a60b175e109a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010170`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT V
```

---

## Crash 22: `cd24414e092977de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011477`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(-CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 23: `b0979f86a9c9b4e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011711`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SE
```

---

## Crash 24: `472997d46fe943b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011753`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES (RAIS
```

---

## Crash 25: `811a97865f03501b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012065`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE FALSE WHEN CURRENT_TIME <= CURRENT_TIMESTAMP NOTNULL THEN CURRENT_TIMESTAMP END; 
```

---

## Crash 26: `a4b9e3cc03585f67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014100`

```sql
SELECT printf('%.*g', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 27: `ba69f954e6451763` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014845`

```sql
SELECT substr('_0-_-- _-K _c_ -', 0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); CREATE TABLE IF NOT EXISTS p(c1 INT, c1 GENERATED
```

---

## Crash 28: `fed1238fc1349113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016491`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0
```

---

## Crash 29: `0fdaa9c2067fc5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017473`

```sql
SELECT substr(' ___o-a', -1, 4294967295); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p INDEXED BY c2 WHERE CURRENT_TIME IS NOT NULL UNION ALL SELECT CURRENT_TI
```

---

## Crash 30: `c6a6d65809cffc30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018264`

```sql
SELECT round(0.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 31: `636fd3e48c5e7a9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018413`

```sql
SELECT printf('%.*s', 2147483648); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 32: `a9ae7bc344f4cf94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020365`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUE
```

---

## Crash 33: `15d69b301b88f193` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020579`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFA
```

---

## Crash 34: `b5c439e0d10cbc60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020929`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL IS NULL >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); SELECT un
```

---

## Crash 35: `57c03499dca28047` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021400`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE % NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFAULT VALUE
```

---

## Crash 36: `a4071db21c543f86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021740`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE random() NOT LIKE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 37: `fdaf7cd2b5a51f29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022140`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPL
```

---

## Crash 38: `1e40bfa4aabe6b64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022329`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES;
```

---

## Crash 39: `40e6009f95dc4bee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022615`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUER
```

---

## Crash 40: `efcd8177a1a22d3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022743`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE NOT LIKE TRUE >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO 
```

---

## Crash 41: `083c5b2c1695670b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023207`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE NOT LIKE NULL == TRUE >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 42: `b3865b604ff2c2f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024161`

```sql
SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE, c2 DATE PRIMARY KEY, c3 TEXT NOT NULL, c2 VARCHAR(255)); SELECT NOT TRUE NOT IN (CURRENT_DATE) % -NULL IS NOT 
```

---

## Crash 43: `c12b1ad63584e579` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024783`

```sql
SELECT round(-1.0, -2147483649); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 44: `cdea7eff123829e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026537`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT 
```

---

## Crash 45: `bddaac43cf1ce670` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026596`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(a DATE P
```

---

## Crash 46: `00fa311190166dd8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026605`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(a DATE P
```

---

## Crash 47: `edf3b8cbf0189bc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026614`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(a DATE P
```

---

## Crash 48: `ab06b1af09ff39b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028073`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT NULL, * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 49: `db05a8ae013d5bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028877`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 50: `074b5c37e4b9f14a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029240`

```sql
SELECT round(-1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT OR ABORT INTO t1 VALUES (+TRUE OR (VALUES (FALSE COLLATE RTRIM)) IN (CURRENT_TIMESTAMP <> RAISE(IGNORE) NOTN
```

---

## Crash 51: `47d2ad54583cf1fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033422`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 52: `cc8873d1a0d85e6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033877`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 53: `4399257f5cffa474` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033982`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (+FALSE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); ANALYZE p; SELECT printf('%.*f', -21474
```

---

## Crash 54: `f9907ca1b0cdb531` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034102`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 55: `8887c4e91c222fc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034119`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 NU
```

---

## Crash 56: `f20c22e2621046e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034425`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483648)); SELECT hex(
```

---

## Crash 57: `bb296c47ae8df31e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035226`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 58: `1524af74368a8fef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035721`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 D
```

---

## Crash 59: `a015f5c1a5870c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 60: `5c764bec2f68b800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036124`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (changes()); ANALYZE p; SELECT hex(zeroblob(-92233720368
```

---

## Crash 61: `4cba61715c5c671f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036140`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (total_changes()); PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 62: `25cfac1ce9c6a59e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036807`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 63: `5070f49a92865fa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037998`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC CHECK (CURRENT_DATE OR TRUE), c2 FLOAT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 64: `8edbdbc34059f7ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038068`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT CURRENT_TIMESTAMP); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRE
```

---

## Crash 65: `de04d362c97e630f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038154`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; 
```

---

## Crash 66: `9a3a6dfe33c70e4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038993`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 67: `32c4610734ee9069` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039218`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 68: `959e704d9d5ce102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041613`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS VALUES 
```

---

## Crash 69: `35b42511a9d22330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041799`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELE
```

---

## Crash 70: `8125d43d766e55aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045148`

```sql
SELECT printf('%u', 2147483647, ' __Q-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q (c1) VALUES (NOT FALSE COLLATE BINARY % NOT random() FILTER (WHERE RAISE(IGNORE) || CU
```

---

## Crash 71: `b2c34a012fbc594b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045353`

```sql
SELECT substr('3wm-2vI', 4294967296, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO s VALUES (CURRENT_TIMESTAMP ->> -RAISE(IGNORE) ->> RAISE(IGNOR
```

---

## Crash 72: `b2475ab0a8705c95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053193`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT X'8cA9FBf1'); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 73: `714a683fd8d326a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053440`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN NULL THEN FALSE ELSE CURRENT_TIMESTAMP END); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 74: `68614e7c396fd6e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053842`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 75: `8397ffb0b01633ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055800`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 76: `f89f75e4c30849db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056166`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_TIMESTAMP), rowid NUMERIC CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_chec
```

---

## Crash 77: `5fc9a40091e033db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056313`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_TIMESTAMP), a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf
```

---

## Crash 78: `20ff3de0fa952748` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058630`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 79: `b949ef97a5e0ba54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059554`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 80: `52faff8b0a345d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059636`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (changes()); ANALYZE p; CREATE TABLE IF NOT EXISTS p(a D
```

---

## Crash 81: `ff193a5b258e2441` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059893`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); ANALYZE p; CREATE TABLE IF NOT EXIS
```

---

## Crash 82: `4efef9a6b13c4a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059900`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (changes()); PRAGMA quick_check; CREATE TABLE IF NOT EXI
```

---

## Crash 83: `8d399bbdf1774c30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060347`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 I
```

---

## Crash 84: `f739c242ff4e3607` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060609`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 V
```

---

## Crash 85: `ef0c3011d6e818ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060864`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_TIME <= CURRENT_TIME <= CURRENT_TIME <= FALSE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA qu
```

---

## Crash 86: `44cb07cc4b7d483e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063370`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 87: `18d02f62e05f9db8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063376`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 88: `1f6df9f03946de07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063383`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_TIME <= CURRENT_TIME <= CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_
```

---

## Crash 89: `5057a16828aff3af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064695`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 90: `1dd911103991c03d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CAST(TRUE AS VARCHAR(255))); PRAGMA integrity_check; SELECT
```

---

## Crash 91: `6f319876ac03e2db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065265`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CAST(CURRENT_TIME AS VARCHAR(255))); PRAGMA integrity_check
```

---

## Crash 92: `1bd752611846dca1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066180`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p (c3) VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 93: `c8e08b7e0cc41860` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072448`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN p NATURAL LEFT JOIN p NOT IND
```

---

## Crash 94: `5b30629846ef87c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072686`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (VALUES (CURRENT_DATE)) AS a 
```

---

## Crash 95: `9dd7c53c82baf9f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT * FROM p NOT INDEXED)
```

---

## Crash 96: `b99891795fd23262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073461`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM p NOT INDEXED WH
```

---

## Crash 97: `551aeec315fb24e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077405`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 98: `fc3f8f9561c42a56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079984`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); VALUES (count(NULL) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 99: `89d4e74d8c3222af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082672`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME GLOB CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IG
```

---

## Crash 100: `c64abae000a7d2d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082857`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE COLLATE NOCASE >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 101: `fef8ce730adb375d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083094`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT _rowid_ AS t90_gk_329mf6_9qf6__0_fe_1_q___6_2f_4_d_oh_be0msc163_14t_ FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 102: `b3e4625c7dd92635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083396`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_DATE AS INT)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO 
```

---

## Crash 103: `732e30627c6c8299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083716`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT X'a52f'); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); INSERT INTO s VALUES (
```

---

## Crash 104: `e25e778cae63b375` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084075`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE > NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFAULT VALUES; PRAG
```

---

## Crash 105: `21d555ca8abc9403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084344`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL <= (FALSE > NULL)) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 106: `2596d6814453bdd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084693`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 107: `dec2f03fdcad3993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084906`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE random() NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAM
```

---

## Crash 108: `7b5e9af52fb91d12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085088`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 109: `3a7a2b7ef1890757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085099`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIME
```

---

## Crash 110: `a9b501c82e4e21e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085476`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE % CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r (c2) 
```

---

## Crash 111: `ef380cbefab32178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE % FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO p VA
```

---

## Crash 112: `76c522c4f476bbe2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085853`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL NOT LIKE changes()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT q.*, * FROM p NA
```

---

## Crash 113: `cf6f3451596bcbd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087111`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IS NULL >= CURRENT_DATE) AS sub1; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 114: `8d3f27c31b6416e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087351`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS REAL) >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 115: `8a9824df1a843d5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087970`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT TRUE FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r DEFAULT VALUES; EXPLAIN 
```

---

## Crash 116: `f5fc4f7f54afb138` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE >> FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (b) VALUES (substr(N
```

---

## Crash 117: `d22656979415338f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088329`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE < CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO p VAL
```

---

## Crash 118: `341e1e2a3128e5ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094206`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'', c3 INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT
```

---

## Crash 119: `a8e22504748c2ad9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094361`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, c3 INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 120: `26f121b8c7ddcbb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094367`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP, c3 INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT 
```

---

## Crash 121: `03ed9e0c1882b479` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095352`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR IGNORE INTO p VALUES (NULL BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE); PRAGMA quick
```

---

## Crash 122: `0888347ff627a912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095506`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p SELECT * FROM p NOT INDEXED ORDER BY NULL ASC NULLS LAST; PRAGMA quick_check; CR
```

---

## Crash 123: `0ac6d5dff5bc2e33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097945`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 124: `4aa5948d9ff59712` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098935`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 125: `139cf2dd426d2cae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102664`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY, c1 TEXT UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO
```

---

## Crash 126: `254b95b71c27a944` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103468`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE FALSE OR NULL WHEN NULL THEN CURRENT_TIMESTAMP END; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 127: `32c157a43f04b880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103519`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 128: `8260ef7f5165c694` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103722`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(CURRENT_TIME IS FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 129: `bcc355ad9095a19e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105074`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE json_type(-CURRENT_DATE) WHEN json_type(-CURRENT_DATE) THEN CURRENT_TIMESTAMP END
```

---

## Crash 130: `733ee2976e2d28dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105147`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE CURRENT_TIMESTAMP WHEN json_type(-CURRENT_DATE) THEN CURRENT_TIMESTAMP END; CREAT
```

---

## Crash 131: `94b659d0c0be4958` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105154`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE json_type(FALSE) WHEN json_type(-CURRENT_DATE) THEN CURRENT_TIMESTAMP END; CREATE
```

---

## Crash 132: `1e00c339c2f61923` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE json_type(-CURRENT_DATE) WHEN TRUE THEN CURRENT_TIMESTAMP END; CREATE VIRTUAL TAB
```

---

## Crash 133: `fa554c721c14bf84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105231`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(~CURRENT_DATE OR NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 134: `f4ff07517f0af958` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105944`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE TRUE >> TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *, FALS
```

---

## Crash 135: `b327d0e6ba509fa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE length(CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT 
```

---

## Crash 136: `906e65dfd11b3666` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107469`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CAST(CURRENT_TIME AS NUMERIC); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 137: `15cf18f7eadbd9fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108198`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE FALSE WHEN CURRENT_DATE COLLATE NOCASE THEN CURRENT_TIMESTAMP END; SELECT printf(
```

---

## Crash 138: `58ac80c6b2756605` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR I
```

---

## Crash 139: `5f28be4acc11296f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= ''; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR
```

---

## Crash 140: `6ea864c1db0e10d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108858`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= CAST('' AS REAL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 141: `95090fc298fb4545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109706`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNO
```

---

## Crash 142: `5f1ad128ff5313bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109886`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO 
```

---

## Crash 143: `0b51edc0e417b2c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110282`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT -4310236792136462420540404058582304232527769658380687413418077.777996330530715289108044866268201526082328819149998188845590460897249916225967996989
```

---

## Crash 144: `0d040acff659edd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110356`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELEC
```

---

## Crash 145: `668d575f31939989` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110603`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE TRUE NOT IN (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 146: `98c0eb37ff159c39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110748`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE OR TRUE NOT IN (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 147: `1634ff448a1a7fc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110861`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE OR TRUE NOT IN (CURRENT_TIMESTAMP); SELECT substr('__DX  ', 9223372036854
```

---

## Crash 148: `a3cac15690e1d6c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110952`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE OR TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 149: `e8cf789a3b9276cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111006`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(CURRENT_DATE OR TRUE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 150: `9aee9bf94dac3a22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT -CURRENT_DATE AS a FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSER
```

---

## Crash 151: `8f4aea668ac9b220` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112202`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE TRUE IN (c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p D
```

---

## Crash 152: `99b2b57c12bf2062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME / FALSE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 153: `bdd9cbcaa6f1dba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112590`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE FALSE WHEN TRUE THEN TRUE IN (VALUES (CURRENT_TIMESTAMP)) END; CREATE VIRTUAL TAB
```

---

## Crash 154: `a2fe0594774cfcc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113851`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE NULL WHEN CASE NULL WHEN changes() THEN CURRENT_TIMESTAMP END THEN CURRENT_TIMEST
```

---

## Crash 155: `1459b16a542daca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115521`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_DATE ELSE TRUE IN (VALUES (CURRENT_TIMESTAMP)
```

---

## Crash 156: `adae80a3b203b718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115926`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= FALSE OR NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 157: `ce4b6a7ee5f1fe87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116036`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE NULL LIKE CURRENT_DATE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 158: `7121ddc8dd6ed7ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116302`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE NULL LIKE NOT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 159: `66cea16d30ebc21d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116581`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE FALSE NOT BETWEEN FALSE AND TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 160: `7b69358d690d9a5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117949`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT DISTINC
```

---

## Crash 161: `98f04d6b9d786d28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); SELECT * FROM q CROSS JOIN p NOT INDEXED ON CURRENT_DATE WHER
```

---

## Crash 162: `674edcff9a32d430` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118914`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= CURRENT_TIME <= CURRENT_TIME <= CURRENT_TIME <= CURRENT_TIME <= CURREN
```

---

## Crash 163: `0873347b7f098b9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120757`

```sql
SELECT substr('-0 -ZXCqk-__8X__', 2147483647, 4294967296); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT *,
```

---

## Crash 164: `5bf707ce2304d683` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121374`

```sql
SELECT printf('%.*g', 0); SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT DISTINCT +NOT RAISE(IGNORE) IS NULL IS NOT NULL AS e9 FROM p WHERE -change
```

---

## Crash 165: `6915512325bcfc0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124264`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 FLOAT DEFAULT -56.5196931e-312); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 166: `d6ec92c650410091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 167: `1f20d7200b6e2caf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124785`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE FALSE NOT BETWEEN -FALSE AND TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 168: `2271cdf470a97f41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE NULL LIKE c2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNO
```

---

## Crash 169: `68db1a223d015cfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126956`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE NULL << NULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 170: `1a99cfc2954cad14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127383`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME / CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 171: `3640d6ed8522c7a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127526`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE c2 IN (NULL); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 172: `f1f115c3f899689d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127765`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE c2 IN (c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DE
```

---

## Crash 173: `e9e813028cd81da3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127936`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE c2 IN (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p 
```

---

## Crash 174: `975fbfc7041ffd47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129219`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE TRUE NOT IN (CURRENT_TIMESTAMP) OR CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 175: `d5429f8c99f653cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129344`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 176: `326a4b409d2bf102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129611`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT CURRENT_TIME IN (58372, FALSE) FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 177: `e49c5ad81446b6d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT 'e 6__ -'); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 178: `1096965a1f09a842` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130220`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 179: `d61b4a92d2466577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130798`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE FALSE LIKE TRUE || TRUE ESCAPE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 180: `e205e7b01a971745` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131190`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE FALSE LIKE FALSE ESCAPE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 181: `6785f23a5db07d59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(~CASE TRUE WHEN CASE FALSE WHEN CASE TRUE WHEN CASE CURRENT_DATE WHEN CASE T
```

---

## Crash 182: `0b517864e9f2e004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133601`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE json_type(~CASE TRUE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP END OR NULL); CREAT
```

---

## Crash 183: `963d690e6a88f4dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133652`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE json_type(FALSE) WHEN json_type(CURRENT_TIMESTAMP != FALSE) THEN CURRENT_TIMESTAM
```

---

## Crash 184: `85ac5d6381bfc340` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134401`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CASE NULL WHEN CURRENT_TIME <= FALSE COLLATE NOCASE THEN CURRENT_TIMESTAMP END; CREATE
```

---

## Crash 185: `7bd0847c33009a83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134816`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= json_type(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 186: `b3a459ada3dc7bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135059`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= FALSE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 187: `f6b57b22f0989782` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136078`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c2 GENERATED ALWAYS AS (a) , a BLOB NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR 
```

---

## Crash 188: `3616c178c51a2545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140934`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (count(*) OVER (ORDER BY CURRENT_TIME ASC NULLS FIRST, CURRENT_
```

---

## Crash 189: `18f61a0a4334a3fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141074`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (count(*) OVER ())); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 190: `fe3fbb6777b11067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143341`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR IGNORE INTO p VALUES (EXISTS (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM p NOT IN
```

---

## Crash 191: `89c0076b8da68014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(NULL AS INTEGER)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALU
```

---

## Crash 192: `c26dbf18f533323a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151274`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME BETWEEN RAISE(IGNORE) AND CURRENT_DATE OR TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 193: `b0b5f69b12cc8afa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151474`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS REAL) >= length(CURRENT_TIME)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSE
```

---

## Crash 194: `7022663db44240dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151731`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS REAL) >= FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE IN
```

---

## Crash 195: `2ec040cce3022e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152326`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE NULL IS NULL >= CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 196: `437c7f132a83b8bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152759`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (VALUES (count(FALSE) OVER (PARTITION BY CURRENT_TIME)))) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 197: `2c35ba858b699e34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152922`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (VALUES (count(FALSE) OVER ()))) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSE
```

---

## Crash 198: `83dcc01308e1a2b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154897`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN DEFAULT X'19DaDF1a0D'); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SEL
```

---

## Crash 199: `2cecad78e03c55ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT _rowid_ AS t90_gk_329mf6_9qf6__0_fe_1_q___6_2f_4_d_oh_be0msc163_14t_ FROM (SELECT sum(CURRENT_DATE) OVER (), * FROM p WHERE FALSE) AS sub1; CREAT
```

---

## Crash 200: `6745965eb4a0b141` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155501`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT _rowid_ AS t90_gk_329mf6_9qf6__0_fe_1_q___6_2f_4_d_oh_be0msc163_14t_ FROM (SELECT *, * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 201: `1bbc4235292ee988` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155507`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT _rowid_ AS t90_gk_329mf6_9qf6__0_fe_1_q___6_2f_4_d_oh_be0msc163_14t_ FROM (SELECT CURRENT_TIME, * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TAB
```

---

## Crash 202: `ba6c76f6e9472a84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NOT FALSE NOT LIKE NULL == TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE
```

---

## Crash 203: `a7a480b0004f1d79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156636`

```sql
SELECT printf('%.*s', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c1, c3); SELECT X'' GLOB CURRENT_DATE IN (VALUES (NULL, TRUE) ORDER BY ifnull(CURRENT_TIMESTAMP, CU
```

---

## Crash 204: `86c8d572553d4fc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157624`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); VALUES (group_concat(CURRENT_DATE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 205: `43493a74fe254006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159936`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 206: `99e22f1bb52c9bf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166685`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (SELECT * FROM p
```

---

## Crash 207: `4491ae69f7ad6e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166904`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) UNION ALL SELECT * FROM p NOT INDEXED WH
```

---

## Crash 208: `40550691d867e5fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167929`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT NULL LIKE FALSE COLLA
```

---

## Crash 209: `1f2156da73bc0da0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168462`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (avg(NULL))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 210: `59e923f3f794b121` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168830`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT * FROM p WHERE CURREN
```

---

## Crash 211: `3bf29d39ede0abe7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169918`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (random()); PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e30
```

---

## Crash 212: `f50666738203dcf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170570`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (CURRENT_DATE), c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c3
```

---

## Crash 213: `9ed040120fa3896d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170696`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE, c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c3 = FALSE; PR
```

---

## Crash 214: `445c16f90e5b75bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180862`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CAST(-4.81621940130871E348794983555651293875310213 AS VARCH
```

---

## Crash 215: `9b744ca4553fa790` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181143`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL DEFAULT ' 2 W_8H2c'); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('
```

---

## Crash 216: `34c3a1a5ff590f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181514`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL DEFAULT -2939520380374267817884009341470337549459689671483731.98); INSERT OR IGNORE INTO p VALUES (CURRENT_D
```

---

## Crash 217: `707177ee25659b5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181728`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 218: `584f875188db4841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182126`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_TIMESTAMP <> CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VI
```

---

## Crash 219: `9e4df473287ce82c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184866`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VA
```

---

## Crash 220: `c2767c49534ecc4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185052`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 221: `e67f4df1d6b485de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185152`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 222: `1213e1b26d1dd9cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185430`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 T
```

---

## Crash 223: `c910ed9e17e115ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185638`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (NULL)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 224: `91942874d513d159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f', 
```

---

## Crash 225: `e07c3a2d6a248520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186377`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT 
```

---

## Crash 226: `2704d8062c3bc456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187070`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 227: `ba9fddceab261c99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187086`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 228: `17d0bb0fe33ee4ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187387`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BOO
```

---

## Crash 229: `ed821860324b725d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188221`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR IGNORE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE IN (SELECT * FROM p)); SELECT print
```

---

## Crash 230: `699db6022bbbd023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188479`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE FALSE NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTA
```

---

## Crash 231: `d6a89b645c11ab6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188629`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE), c2 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 232: `48201da7405a5245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188636`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE FALSE NOT LIKE CURRENT_TIMESTAMP), c2 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 233: `ac67e84f06117f9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188644`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE TRUE NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAM
```

---

## Crash 234: `ee212be1ebc3f773` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189135`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_
```

---

## Crash 235: `abd145c61be52e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189983`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (json(FALSE)); PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 236: `77b6eb1c92b9c58c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM q ORDER BY CURRENT_TIME ASC NULLS LAST LIMIT CURRENT_TIME; CREATE VIRT
```

---

## Crash 237: `5c30b5ebbadea139` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193061`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL DEFAULT 32593290307394388270550332979731102049767245569157638424253858982081736281585099366975420706647941805080752595926072920036.54122037190); CREATE 
```

---

## Crash 238: `b4a1bbe6a4338f27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193194`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 239: `5241f67718c15f1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193851`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT round(0.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 240: `db00a58fa2b1c46f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195463`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (min(CURRENT_TIMESTAMP), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (X'') EXCEPT 
```

---

## Crash 241: `ac67a2e228951838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (min(TRUE), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 VALUES (RAISE(IGNORE) COLLATE NOC
```

---

## Crash 242: `a29c14a371b2ccb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196478`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*), min(NULL), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; PRAGMA 
```

---

## Crash 243: `18bde606cc90d4bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197068`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE TRUE) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UN
```

---

## Crash 244: `f0bb3a4f81588814` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197711`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT 
```

---

## Crash 245: `a6fe69d23cb368ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197886`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p ORDER BY
```

---

## Crash 246: `22d4e692a37821e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198168`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT X'8cA9FBf1'); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT 
```

---

## Crash 247: `d3b48cc98deb35aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198326`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT CURRENT_TIMESTAMP AS r ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST, CURRENT_TIMES
```

---

## Crash 248: `52600863d22c3839` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198574`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM (VALUES (NULL)) AS v_k____ua_1u__y45cjy___54cj9_q__wquu___l26z____9g______
```

---

## Crash 249: `bd8cf8899dbf8e7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203226`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p SELECT CURRENT_TIME AS a FROM (SELECT * FROM (VALUES (FALSE)) AS v_k____ua_1u__y45cjy___54cj9_q__wquu
```

---

## Crash 250: `d2ce403dd46b7c8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203314`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 251: `f0ec6bebb731c1c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203328`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p SELECT CURRENT_TIME AS a FROM (SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIME ASC) AS v_k____ua_1u
```

---

## Crash 252: `44d1b2681090f068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203356`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p SELECT CURRENT_TIME AS a FROM p ORDER BY CURRENT_TIME ASC; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE 
```

---

## Crash 253: `53701c21969d9f36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206833`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM q AS p_ EXCEPT SELECT CURRENT_TIME AS a FROM p ORDER BY CURRENT_T
```

---

## Crash 254: `cbb7c2900f691b5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208041`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e
```

---

## Crash 255: `7e915c43948186f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208203`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 256: `d733548f1f156320` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208209`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 257: `99242c9d573ccd25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209987`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP, NULL) EXCEPT VALUES (NULL, CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1e
```

---

## Crash 258: `8a4f6d35660ca73a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210440`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP, CAST(CURRENT_TIMESTAMP == CURRENT_TIME AS BLOB)) UNION VALUES (NULL, CURRENT_DAT
```

---

## Crash 259: `8b15c8cd898e4b5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210557`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP, CAST(CURRENT_DATE AS BLOB)) UNION VALUES (NULL, CURRENT_DATE); CREATE VIRTUAL TA
```

---

## Crash 260: `7b9a9ad89953f533` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213419`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT CURRENT_TIMESTAMP AS r ORDER 
```

---

## Crash 261: `259639959935e8e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213977`

```sql
SELECT substr('8l', 1, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); INSERT INTO s (rowid, c1) VALUES (CURRENT_TIME LIKE +CURRENT_DATE ESCAPE CURRENT_TIME, NULL, FALSE ISNUL
```

---

## Crash 262: `68aa6d68d7736fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214283`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*s', 2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c3, c1); REPLACE INTO q VALUES (nullif(FALSE NOTNULL, NOT
```

---

## Crash 263: `472d71d3f3daa359` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214862`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT FALSE AS r ORDER BY CURRENT_T
```

---

## Crash 264: `37668dec326549fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217374`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP, NULL) UNION VALUES (CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP + FALSE, CURREN
```

---

## Crash 265: `f0245b201b27babd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217475`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP, NULL) UNION VALUES (NULL + FALSE, CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 266: `332e192bf838a96e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT sum(CURRENT_DATE) OVER () ORDER BY CURRENT_TIMESTAMP ASC; CREATE VIRTUAL TABLE I
```

---

## Crash 267: `ffc5a8ac4a8fc110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225526`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE TRUE) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN TR
```

---

## Crash 268: `a82dc740dfed3b32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225829`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE NULL) OVER (ORDER BY FALSE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE 
```

---

## Crash 269: `6e89391a82f47cb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226011`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE NULL) OVER ()); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 270: `7567188c50a90d8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226025`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (lower(NULL), TRUE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 271: `f5842b1785c7f67c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226222`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (last_insert_rowid(), TRUE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 272: `dc389907e698c96a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226254`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (lower(FALSE), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; SELECT min(TRU
```

---

## Crash 273: `a7e8bdf1ac32f2ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230492`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIME ASC; PRAGMA integrity
```

---

## Crash 274: `19c5efff718a8e4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231068`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE IS NOT FALSE), c2 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREA
```

---

## Crash 275: `fc97496554e13729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231233`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE FALSE NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTA
```

---

## Crash 276: `86445318c2c483eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231404`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (FALSE NOT LIKE CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_
```

---

## Crash 277: `8ea2cac709041ff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233343`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 278: `cd8ec1f09670f5ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234203`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 279: `780ee5d87db6e8bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234312`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KE
```

---

## Crash 280: `260ed299e4e84a84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF 
```

---

## Crash 281: `3ccf4aaa1382f266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238351`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VA
```

---

## Crash 282: `4a74d509949813ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252112`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (c2), c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c3 = FALSE; 
```

---

## Crash 283: `f57b504662c6ee5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252325`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC CHECK (FALSE NOT LIKE CURRENT_TIME >= CURRENT_DATE), c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TR
```

---

## Crash 284: `867f8b4270bf62c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252434`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c3 = FALSE
```

---

## Crash 285: `d7820e3e9a1dbb4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252522`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c2 = FALS
```

---

## Crash 286: `ea0e057866d963e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET rowid = FALSE; PRAGMA quick_check
```

---

## Crash 287: `34768417763306d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253148`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (random()); PRAGMA quick_check; SELECT printf('%.*f'
```

---

## Crash 288: `9007331aa40627e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253491`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); CREATE VI
```

---

## Crash 289: `1f51b6552fccc4b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253917`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP) NOT BETWEEN CURRENT_DATE || T
```

---

## Crash 290: `1877f1bf0170d0b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254345`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT avg(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP) NOT BETWEEN CURRENT_DATE || T
```

---

## Crash 291: `9c5dfc5e4859d06d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254494`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT TRUE NOT BETWEEN CURRENT_DATE || TRUE AND CURRENT_TIME AND CURRENT_DATE AS a FROM p W
```

---

## Crash 292: `20b8899eaf12b3fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254534`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (VALUES (CURRENT_DATE) INTERSECT SELECT * FR
```

---

## Crash 293: `142ba5e08b352339` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254702`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (VALUES (CURRENT_DATE) INTERSECT VALUES (TRU
```

---

## Crash 294: `0cb2d9f8e22eb2e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT ALL * FROM (SELECT AL
```

---

## Crash 295: `b70b9b07d934ffd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254914`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT ALL * FROM (VALUES (T
```

---

## Crash 296: `9457d9ca170f6d37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255189`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT TRUE AS a FROM p ORDER BY CURRE
```

---

## Crash 297: `dd03f798151db325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255543`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT CURRENT_TIME AS a FRO
```

---

## Crash 298: `932384f2dcb6ca6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255759`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT FALSE COLLATE NOCASE 
```

---

## Crash 299: `382efbb74ad0068e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255906`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (VALUES (CURRENT_TIMESTAMP)) 
```

---

## Crash 300: `199cd182d6bc48e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255915`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT CURRENT_DATE AS a FRO
```

---

## Crash 301: `6af00198677edc61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255924`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT FALSE COLLATE NOCASE 
```

---

## Crash 302: `61b7136ebf4734b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255982`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NATURAL JOIN (SELECT ALL * FROM q NATURAL 
```

---

## Crash 303: `4786803afc72606a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256523`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count(NULL) OVER (PARTITION BY CURRENT_TIMESTAMP, TRUE
```

---

## Crash 304: `ee3ef849f604c0c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256776`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (NOT EXISTS (VALUES (CURRENT_TIME) EXCEPT SELECT DISTIN
```

---

## Crash 305: `143022186f5adf4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257390`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (NOT EXISTS (VALUES (CURRENT_TIME) EXCEPT SELECT DISTIN
```

---

## Crash 306: `e5c03572336201f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257829`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) UNION ALL VALUES (RAISE(IGNORE))); CREATE VIRTUAL TA
```

---

## Crash 307: `56484c36b075b6a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258766`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMES
```

---

## Crash 308: `afe609e4fce79aae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259346`

```sql
SELECT printf('%x', -9223372036854775808, '   3g_M71_-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (NULL IS NOT CURRENT_DATE * TRUE COLLATE BINARY ->> EXI
```

---

## Crash 309: `59c96ba0fccdd26d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260719`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p SELECT ALL * FROM (SELECT FALSE COLLATE NOCASE AS a FROM p) AS v_k____ua_1u__y45cjy___54cj9_q__wquu___l26z____9g______4x1vzoz9_yb_3y___7
```

---

## Crash 310: `067a1878b285b2f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264709`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (random()); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 311: `8ec397c4257abcde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264920`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME * CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 312: `0d7309d5655e6915` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265170`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME * CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*f', -2147
```

---

## Crash 313: `fa47d45de03cffe4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268614`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); VALUES (group_concat(NULL) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INT
```

---

## Crash 314: `66301a05275d4ce4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268734`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); SELECT * FROM q AS p_ EXCEPT SELECT CURRENT_TIME AS a FROM p ORDER BY CURRENT_TIME DESC; CREATE VIRTUAL TABL
```

---

## Crash 315: `d3107a70299c17e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000273251`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE >> FALSE || CURRENT_DATE) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 316: `a977d609c011d9e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000273769`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME <= c2; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 317: `79540f04995d9f74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274325`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE >= CURRENT_TIMESTAMP >= CAST(FALSE AS VARCHAR(255)) >= CAST(FALSE AS REAL)) AS sub1; CREATE VIRTUAL TA
```

---

## Crash 318: `f517fb0851869acc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274953`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS VARCHAR(255)) >= length(CURRENT_TIME)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 319: `9bac4bfe82837e33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275731`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE >> FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); INSERT OR REPLACE INTO p VALUE
```

---

## Crash 320: `34eb71c85ba8eb5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE COLLATE NOCASE < CURRENT_TIME) AS sub1; SELECT printf('%.*f', -2147483649, -1e308);
```

---
