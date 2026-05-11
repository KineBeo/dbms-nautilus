# Crash Triage Report

**Total crashes:** 291  
**Unique crash sites:** 291  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 291 | 291 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `c6e6a3092c927b6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR REPLACE INTO p VALUES (CASE -TRUE IS NULL OR (FALSE & CURRENT_DATE NOT IN (SELECT *, *) >> ~NULL BETWEEN CURRENT_DATE AND CURRENT
```

---

## Crash 2: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000519`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 3: `9a46a0e496c927fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000768`

```sql
SELECT substr('-A6_', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); SELECT ALL CASE WHEN (TRUE | +FALSE) < TRUE <> FALSE COLLATE BINARY NOTNULL THEN FALSE NOT NULL || RAISE
```

---

## Crash 4: `c12f8fbffcb7d160` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001015`

```sql
SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); SELECT CURRENT_DATE FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP LIKE NOT RAISE(IGNORE) AS s28 FRO
```

---

## Crash 5: `51a008f788499050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001176`

```sql
SELECT printf('%.*f', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP NOTNULL << +char(0) OVER (ORDER BY -NULL == -TRUE ASC)
```

---

## Crash 6: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001203`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 7: `55868c8f4a53350d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001801`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES ((TRUE), NULL) RETURNING r.*; EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) INTERSECT SELE
```

---

## Crash 8: `a19ccb72bbecc4ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001885`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (p.c1 < CURRENT_TIME ->> CURRENT_TIME < EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p
```

---

## Crash 9: `ec202e5995a2dec0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); VALUES (TRUE) UNION ALL VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t2 DEFAULT VALUES; EXPLAIN QUERY PLAN
```

---

## Crash 10: `a33f6df247283116` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003645`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT p.* FROM t2 INDEXED BY b WHERE NULL LIMIT c2 * CASE WHEN CURRENT_DATE TH
```

---

## Crash 11: `f31c2100b12e1f0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004206`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE COLLATE RTRIM); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 12: `db58e438e091a768` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004343`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q WHERE NULL GROUP BY RAISE(IGNORE) WINDOW w1 AS (), w2 AS () INTERSECT SELECT * FROM s NOT INDEXED WHE
```

---

## Crash 13: `6ea6a92db774c896` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004362`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.*, 
```

---

## Crash 14: `e377142688e6359b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004368`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM s NOT INDEXED WHERE CURRENT_DATE GROUP BY NULL, CURRENT_TIME; VALUES (CURRENT_TIME);
```

---

## Crash 15: `6a73d4e5731ae640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005294`

```sql
SELECT printf('%.*g', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO q VALUES (NULL ISNULL & +char(typeof(FALSE < CURRENT_DATE) FILTER (WHERE RAISE(
```

---

## Crash 16: `92b5520743a018ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005728`

```sql
SELECT printf('%.*d', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES (CURRENT_TIME IS NULL, TRUE, RAISE(IGNORE), random(), ~CURRENT_TIME COL
```

---

## Crash 17: `4a31b42cc2edc9a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005909`

```sql
SELECT substr('- 2_5_-B O ', 0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO t2 VALUES (CURRENT_DATE ISNULL <= max(CURRENT_DATE) > ~CURRENT_TIMESTAMP <
```

---

## Crash 18: `dc57b45c6978b501` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006345`

```sql
SELECT printf('%x', -2147483648, '_   pk M _cQ_uM'); SELECT substr('NO-RX _ _-_', 2147483648); SELECT substr('', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p V
```

---

## Crash 19: `793c5b348e2d78e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006452`

```sql
SELECT substr('-T_-g- ', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q (c3, b) AS (SELECT q.* UNION ALL SELECT '4-1jUAq_8' + NULL COLLATE BINARY OR 
```

---

## Crash 20: `151bdc04c99bb3a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006917`

```sql
SELECT substr(' -5 82 _q_8cWd1', -2147483648, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t2 AS MATERIALIZED (SELECT NULL) INSERT INTO q VALUES (FALSE); 
```

---

## Crash 21: `debf950f6a9e0e0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007121`

```sql
SELECT round(0.01, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO r VALUES (~c2 != -++TRUE != CASE WHEN CURRENT_TIMESTAMP COLLATE BINARY IS NULL COLLATE BINARY T
```

---

## Crash 22: `6a4de2af17c7c940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007310`

```sql
SELECT substr(' 07-', -9223372036854775808, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM r WHERE EXISTS (SELECT * ORDER BY CURRENT_TIME COLLATE RTRIM LIMIT TRUE
```

---

## Crash 23: `526b4e4c89db8ede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007549`

```sql
SELECT substr('aQ_-g ', 2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES (CAST(-CASE NULL >> FALSE COLLATE RTRIM WHEN EXISTS (WITH p AS NOT MATE
```

---

## Crash 24: `2703f2209fd730b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009290`

```sql
SELECT round(1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO q DEFAULT VALUES; SELECT *;
```

---

## Crash 25: `79bb1fb9e309df6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011515`

```sql
SELECT printf('%.*d', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p NATURAL JOIN t2 WHERE RAISE(IGNORE); CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c1 GENERATED ALWAYS AS
```

---

## Crash 26: `41d9012d38e3f1d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011873`

```sql
SELECT printf('%.*s', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT NOT p.c1, NULL IS NOT NULL == CURRENT_TIMESTAMP = -a COLLATE BINARY NOTNULL NOT BETWEEN CASE W
```

---

## Crash 27: `d755950ac0c90123` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012208`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSI
```

---

## Crash 28: `0a88eb5029832204` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012403`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 29: `921965b4bb31062e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013113`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zero
```

---

## Crash 30: `0ecf7fc5f22784a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013207`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-92
```

---

## Crash 31: `752e7917064fa077` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CU
```

---

## Crash 32: `639045a85493085c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014013`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (-1179.3790870217812208348100286302706571044067666670712453692915780264327147068884308684128345983704005133250334665232096854668415
```

---

## Crash 33: `8750e6c307bf9463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014282`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_DATE); 
```

---

## Crash 34: `c7072949c84c13da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014300`

```sql
SELECT round(0.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); REP
```

---

## Crash 35: `d26a3ecbe491ae26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015178`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p NATURAL JOIN p WHERE CURR
```

---

## Crash 36: `81168cb70e23c23f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019626`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE TRUE IS NOT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFA
```

---

## Crash 37: `57a150afe4142594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019977`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 38: `ce37b2b98b422387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019983`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA 
```

---

## Crash 39: `47f02d9001914514` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020011`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE FROM p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p 
```

---

## Crash 40: `e5a6fe8825304551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023723`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO 
```

---

## Crash 41: `49d1601512818044` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023877`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 42: `297f5f07a8f704dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024073`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW 
```

---

## Crash 43: `2af8457ade574477` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024123`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); REPLACE INTO p VALUES (~CURRENT_TIMESTAMP); VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY CURRENT_TIMESTAMP, CURRENT_TIME; CREATE VIRTUAL TABLE IF
```

---

## Crash 44: `8d69cc8102eacc90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024138`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, _rowid_ FLOAT UNIQUE, rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 45: `e9431152e66dea92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024165`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES ((VALUES (TRUE) UNION SELECT * FROM p)); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 46: `cc0d207140ab64ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024180`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (NULL NOT LIKE NULL != CURRENT_DATE MATCH FALSE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 47: `4f3501b8a57ca1d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024676`

```sql
SELECT printf('%.*g', 4294967296, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 48: `ac4e1a6833228587` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024811`

```sql
SELECT printf('%d', -1, '_ d  0khT'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c
```

---

## Crash 49: `b22b42cb130ff84c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025944`

```sql
SELECT printf('%.*d', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 50: `b7d2e61f92591a72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026490`

```sql
SELECT substr('aX-  _vype _', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT hex(zeroblob(1));
```

---

## Crash 51: `732ea6a5678f53cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027100`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME LIKE TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 52: `d1e63eaf800bf254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028116`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (TRUE LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 53: `9454ddb27a1a4368` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028867`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (FALSE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF N
```

---

## Crash 54: `3a6c2b1a799c7a5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (NULL >= CURRENT_DATE == NULL); VALUES (CURRENT_TIMESTAMP); CR
```

---

## Crash 55: `689a973fa3b0728a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029711`

```sql
SELECT printf('%.*s', 2147483647, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 56: `55696b92516d4e2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030770`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL, c1 FLOAT NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 57: `9837add4058f6139` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030992`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b BOOLEAN NOT NULL, c1 FLOAT NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -214748364
```

---

## Crash 58: `275e4fe48c2d5a0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032499`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (PARTITION BY CURRENT_
```

---

## Crash 59: `2db53ac542387405` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032800`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, rowid NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p V
```

---

## Crash 60: `886a7b703d679da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); VALUES (TRUE) UNION ALL VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CU
```

---

## Crash 61: `e35f8a45b04ba406` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037669`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (last_insert_rowid()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO 
```

---

## Crash 62: `71b3b2783422a0ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041763`

```sql
SELECT printf('%f', 9223372036854775807, '36W-_  - h-As'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE 
```

---

## Crash 63: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041896`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 64: `5a3f019bce1484f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045194`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (_rowid_) VALUES (FALSE) ON CONFLICT(c2) DO UPDATE SET c2 = abs(NULL) OVER (PARTITIO
```

---

## Crash 65: `be15f6173a2d6ba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048526`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY
```

---

## Crash 66: `78e7a97dc221fb53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055933`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (lower(CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO 
```

---

## Crash 67: `30dcdd2cc0b10343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056169`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (
```

---

## Crash 68: `acbb7ec2c2f1735c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059511`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN NULL IS NOT TRUE THEN CURRENT_TIMESTA
```

---

## Crash 69: `b448e88bc931a10b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN CURRENT_DATE IS NULL THEN TRUE END AS
```

---

## Crash 70: `8247471bfc9f84ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061525`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 71: `8814936374c2aa60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061700`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); VALUES (TRUE) EXCEPT VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 72: `fd677a3cfc9b50bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063793`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, rowid NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CUR
```

---

## Crash 73: `03d36061597c3c19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063966`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, rowid NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 74: `6d73ea7cc38299a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063994`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, rowid NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL
```

---

## Crash 75: `b816c5c79043ba8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064369`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT avg(CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP DESC R
```

---

## Crash 76: `deca5c83927686a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064375`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b, c3); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE C
```

---

## Crash 77: `298382dc95b89de6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064383`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE COLL
```

---

## Crash 78: `9de59bb842c1a4c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064390`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT +count(CURRENT_TIME) OVER () AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_8yvl UNION VALUES (CURRENT_TIMESTAMP) UN
```

---

## Crash 79: `60529da4870e3748` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064399`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE COLL
```

---

## Crash 80: `a46a407ef9ccd493` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064406`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT 0.0, c2 INT DEFAULT -0); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY
```

---

## Crash 81: `4b0d8c147305472b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064413`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE EXISTS (VALUES (CURRENT_DATE) INTERSECT SELECT *) GROUP BY NULL WIN
```

---

## Crash 82: `e1382fcbc052f134` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064425`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY NULL ISNUL
```

---

## Crash 83: `5b60724829c78983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064434`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM (t2) WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE CO
```

---

## Crash 84: `2ad9dff041f96a30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064441`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT CURRENT_TIME OR FALSE AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_8yvl, * UNION VALUES (CURRENT_TIMESTAMP) UNION 
```

---

## Crash 85: `f3439b0457ff2dce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064448`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (last_insert_rowid() FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY RAISE(IGNORE) ORDER BY FALSE DESC ROWS BETWEEN CURRE
```

---

## Crash 86: `cd2b994861f527dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064456`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (PARTITION BY CURRENT_
```

---

## Crash 87: `2ecd4cc5826cdb45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064469`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM r INDEXED BY c3 LEFT OUTER JOIN p INDEXED BY rowid ON CURRENT_TIME WHERE CUR
```

---

## Crash 88: `4293502614755cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064475`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (PARTITION BY TRUE % C
```

---

## Crash 89: `3fcd14784c8bac67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064485`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM p NOT INDEXED LEFT JOIN q NOT INDEXED ON CURRENT_TIME WHERE CURRENT_TIMESTAM
```

---

## Crash 90: `4158beefac33e21e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064495`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT TRUE IS NOT NULL > CURRENT_TIMESTAMP AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_8yvl, TRUE IS NOT NULL > NULL / 
```

---

## Crash 91: `49cebe580856a20b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064501`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (TRUE NOT IN (TRUE NOT IN (CURRENT_TIME), NULL), NULL) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL 
```

---

## Crash 92: `eba8decb4a8bc196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064507`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY RAISE(IGNO
```

---

## Crash 93: `add1fd18e2a4930e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064516`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE FALSE / CURRENT_DATE - FALSE GROUP BY NULL WINDOW w1 AS () ORDER BY
```

---

## Crash 94: `b0ad7f076d9d2a53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064524`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * ORDER BY NULL DESC NULLS FIRST UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE
```

---

## Crash 95: `95293c04d46ade46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064536`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM (VALUES (CURRENT_TIME)) AS q435_13_j3c5iz WHERE CURRENT_TIMESTAMP GROUP BY N
```

---

## Crash 96: `e8f2921115283230` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064545`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT ALL * FROM q NOT INDEXED , t3 NOT INDEXED ON EXISTS (VALUES (CURRENT_DATE) INTERSECT SELECT *) UNION VALUES (CURRENT_TIMESTAMP) UNION A
```

---

## Crash 97: `fb00d29f6461e1f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064552`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS (PARTITION BY CURRENT
```

---

## Crash 98: `ac7337d1a9f7ce46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064575`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT t1.* UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE C
```

---

## Crash 99: `6575ef7d2472cf34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064593`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM q INNER JOIN r WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER B
```

---

## Crash 100: `d2fda35319670e5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064614`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION SELECT s.*, NULL LIKE (CURRENT_TIMESTAMP) ESCAPE CURRENT_DATE != ~RAISE(IGNORE) NOT LIKE CURRENT_TIME IN ((NULL), CURRENT_DATE)
```

---

## Crash 101: `579a1e0777b5a56e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064641`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY, _rowid_ BLOB NOT NULL); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE 
```

---

## Crash 102: `725edaad4ca71bd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064659`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT p.* FROM r NOT INDEXED LEFT JOIN q NOT INDEXED USING (c1) UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIM
```

---

## Crash 103: `b50c304bed9043c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064703`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM r NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY TRUE HAVING RAISE(IGNORE) WIN
```

---

## Crash 104: `2f1808f6e2381e1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066391`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT, c3 GENERATED ALWAYS AS (a = -474503
```

---

## Crash 105: `8a8292b63c149397` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066617`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT X'49dcCcAc5c6c'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 106: `6475c7e61887d44e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066817`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 107: `5673487bbaca27ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066838`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL, c1 FLOAT NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 108: `8851008561ec2747` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067134`

```sql
SELECT printf('%.*e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); VALUES (CURRENT_DATE, TRUE) ORDER BY RAISE(IGNORE) DESC NULLS LAST INTERSECT SELECT CURRENT_TIMESTAMP IS DISTINCT FR
```

---

## Crash 109: `fd2d73c7a2b19b5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069416`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME << CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEF
```

---

## Crash 110: `60ef3b97d06a7178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069819`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT ' - V_ N55c - _'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p V
```

---

## Crash 111: `94b50bc61694962b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069948`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMES
```

---

## Crash 112: `1daba056b9420b42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069955`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUE
```

---

## Crash 113: `6244b9b0ac02c68c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069964`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (FALSE LIKE X''); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; AN
```

---

## Crash 114: `8664837f0e56cc57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070592`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 115: `6a88d881827635bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071061`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME, CURRENT_TIME ASC NULLS LAST; SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TAB
```

---

## Crash 116: `454ad7a0ee767368` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071844`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 117: `ab4423f57b1d0489` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072046`

```sql
SELECT substr('', 9223372036854775807, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT ~NOT +CURRENT_DATE IN (VALUES (CURRENT_DATE)), TRUE COLLATE RTRIM LIKE RAISE(IGNORE
```

---

## Crash 118: `22285372a7bc4c7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073716`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); WITH RECURSIVE q (c3) AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT NULL IN (CURRENT_TIME) = json
```

---

## Crash 119: `259cfd193b95fdd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074600`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL NOT BETWEEN FALSE AND CURRENT_TIMESTAMP), b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); VALUES (CURRENT_TIME); CREATE VIR
```

---

## Crash 120: `4f95a0461e1edfd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074619`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME);
```

---

## Crash 121: `d7db06618fd880e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074786`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEF
```

---

## Crash 122: `1c9e61fc49a0c060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078043`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN UNBOUNDE
```

---

## Crash 123: `557b61ad66ee11cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078143`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 124: `59986ad1eb9d93f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078151`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT count(*) OVER () AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_8yvl FROM p
```

---

## Crash 125: `ec233c0d2e27566c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078435`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT *, count(*) OVER () AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_
```

---

## Crash 126: `8919f5ca3222bd81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082323`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT TRUE IS NOT NULL > CURRENT_TIMESTAMP AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__
```

---

## Crash 127: `fe3e29d6cc2e253a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082634`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT +count(CURRENT_TIME) OVER () AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_
```

---

## Crash 128: `42f813f1d078c6d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083728`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 129: `a16c282f738e8eaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085282`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT *, min(TRUE) AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 130: `3c8e8e11dae35af7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085453`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT *, min(TRUE) AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 131: `c74fe00155594444` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085463`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT *, total_changes() AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 132: `75990f629fd22f6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085481`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT *, count(*) AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 133: `1fce2a97e54cd24f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE FROM (VALUES (CURRENT_TIME)) AS q435_13_j3c5iz WHERE TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 134: `ce3da6c77050a60d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086964`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT CURRENT_TIME, c2 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE FROM p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 135: `722828d5a9be1cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087196`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p AS lh8768_5iq9_5he__e__e4y_385___zq0_z8__8__hvcr9__7z6_l6t_p3h_9g0h_z_59_ym9_1_q5wtv_v_6______o_a__8_e678af5
```

---

## Crash 136: `8900809e6e0fe11b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087940`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAU
```

---

## Crash 137: `4adc9d4d4202d59f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088087`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, rowid INT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT
```

---

## Crash 138: `bbfe752acfbb0def` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088484`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE NULL NOT LIKE NULL; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 139: `fa6e7f459f4be8f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088746`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b BOOLEAN NOT NULL, _rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); IN
```

---

## Crash 140: `571175150982832e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088986`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE TRUE IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CU
```

---

## Crash 141: `b1c51a4715b35e31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089474`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c3 INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO 
```

---

## Crash 142: `f9b2e1903b43ad9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089729`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 143: `300ea832612bd33c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089769`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 144: `bc4251f36dffb1e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091878`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE
```

---

## Crash 145: `70cbca782128feba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097251`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY TRUE IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFA
```

---

## Crash 146: `7effb5ae6178947b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097439`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY -NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CU
```

---

## Crash 147: `9bc2c6936bff7629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (0.0); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 148: `215511f455773863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100458`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT OR FAIL INTO p VALUES (NULL); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 149: `d1db7d3f3c07f9c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100572`

```sql
SELECT substr('CnX5p- E -4_ -_', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT r.* FROM r UNION ALL SELECT FALSE IS NOT NULL FROM q , (VALUES (CURRENT_DATE)) A
```

---

## Crash 150: `f6d5f3f9f23353c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100646`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL NOT BETWEEN FALSE AND CURRENT_TIMESTAMP)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 151: `a3af4c3f3b995acf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X'Ea'); REPLACE INTO p VALUES (NULL); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 152: `30b5dcc30d30aa37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (TRUE NOT BETWEEN CURRENT_TIMESTAMP AND TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLAC
```

---

## Crash 153: `6982219132420439` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101305`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (random()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quic
```

---

## Crash 154: `88771ac2788ec503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT ''); REPLACE INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_DAT
```

---

## Crash 155: `51111f6a5f7521e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT IN
```

---

## Crash 156: `acb41174c932eb16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102244`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALU
```

---

## Crash 157: `a8d60c57e7cf1627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102402`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (EXISTS (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p 
```

---

## Crash 158: `2550dd4fad82b8f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102988`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE
```

---

## Crash 159: `400230b5bdab0b41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103918`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP & CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (
```

---

## Crash 160: `28343cfbfe56a72e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104461`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GR
```

---

## Crash 161: `6224e1303f2e7507` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104473`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (NULL)); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_
```

---

## Crash 162: `b6cd571f856c7a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114803`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 DATE); INSERT INTO q VALUES ((VALUES (TRUE)) LIKE TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE I
```

---

## Crash 163: `9b8332063130c0b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115123`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (TRUE NOT BETWEEN CURRENT_TIMESTAMP AND FALSE NOT NULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY 
```

---

## Crash 164: `a8fb7fe2a065ee87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115967`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (TRUE NOT BETWEEN NULL AND FALSE NOT NULL)); INSERT INTO q VALUES (NULL); EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 165: `f8c2470907d4a447` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116347`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (NULL NOT LIKE NULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE 
```

---

## Crash 166: `78648e3e5a10bdf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117290`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 167: `1a7e8b2be065afdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117946`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY TRUE; CREATE TABLE IF NOT EXISTS p(c1 F
```

---

## Crash 168: `2b115d883aef1645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119454`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CAST(TRUE AS REAL)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -21474
```

---

## Crash 169: `8f9bd8265c13bd2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119655`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p JOIN q skx ON CURRENT_DATE LIKE CURRENT_TIMESTAMP; SELECT printf('%.*g', -214748
```

---

## Crash 170: `d52a20de46c0d5a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119979`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); SELECT * FROM q NATURAL LEFT JOIN q WHERE CURRENT_TIMESTAMP GROUP BY TRUE; CREATE VIRTUAL TABLE IF N
```

---

## Crash 171: `8048c687779496ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121238`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (CURRENT_TIMESTAMP != CURRENT_TIME)); INSERT INTO q VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_
```

---

## Crash 172: `6033de74ad1778a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121379`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (CURRENT_TIMESTAMP)); INSERT INTO q VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VI
```

---

## Crash 173: `a37fe7c0e9a40e65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121821`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 DATE); INSERT INTO q VALUES ((VALUES (CURRENT_TIME) UNION SELECT * FROM p WHERE TRUE ORDER BY CURRENT_TIME ASC NULLS FIRS
```

---

## Crash 174: `fb3db49df3e4063b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126303`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); REPLACE INTO p VALUES (TRUE IS FALSE COLLATE NOCASE); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP 
```

---

## Crash 175: `80d7feae1785048d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126489`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); REPLACE INTO p VALUES (TRUE IS CURRENT_TIMESTAMP); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 176: `b1d49ff5049da1a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128447`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURR
```

---

## Crash 177: `0806db8f7d570ab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129331`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO
```

---

## Crash 178: `f6cc17122227fa76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT TRUE, c3 INTEGER NOT NULL); CREATE TABLE IF NOT E
```

---

## Crash 179: `78e4abd05c99b8b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130335`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (random()); PRAGMA quick_check; CREATE VIRT
```

---

## Crash 180: `65e191d284859cd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132226`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES ((SELECT DISTINCT * FROM p WHERE FALSE)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 181: `ed9603290662b861` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133095`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (TRUE NOT IN (TRUE NOT IN (_rowid_, NULL), NULL))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 182: `9a501cd1d88257d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (TRUE NOT IN (CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFA
```

---

## Crash 183: `963a0263912c057e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134078`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (TRUE NOT IN (TRUE NOT IN (_rowid_, NULL), NULL) NOT BETWEEN FALSE AND CURRENT_TIMESTAMP)); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CR
```

---

## Crash 184: `fb0cdcf804e92023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134911`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) CHECK (random())); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 185: `c866be980fe6c517` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); REPLACE INTO p VALUES (-1179.37908702178122083481002863027065710440676666707124536929157802643271470688843086841283459837040051332503346652320968546684154
```

---

## Crash 186: `fd6a52811c050d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135720`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VALUES (X'Bf47dcBc'); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (CURRENT_DATE); P
```

---

## Crash 187: `6b1572514b726931` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136051`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); WITH p AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VAL
```

---

## Crash 188: `f4137bb3f1d7516a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137145`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY NOT EXISTS (SELECT * FROM (SELECT TRUE LIMIT CURRENT_DATE) AS a WHERE TRUE GROUP BY CURREN
```

---

## Crash 189: `56c9372d03c47e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137377`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY NOT EXISTS (SELECT * FROM (VALUES (TRUE)) AS a WHERE TRUE GROUP BY CURRENT_TIME); CREATE V
```

---

## Crash 190: `af46cf964a84aac6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137453`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY NOT EXISTS (VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM p NOT INDEXED ORDE
```

---

## Crash 191: `65de4100aecf0e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142039`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT CAST(CURRENT_TIMESTAMP * CURRENT_TIME AS BLOB); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VA
```

---

## Crash 192: `8e09371a18cd4c8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT CAST(NULL AS BLOB); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (random()); PRAGMA quic
```

---

## Crash 193: `5f92884242891e37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143133`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT CAST(CAST(CURRENT_TIME AS BLOB) AS BLOB); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VA
```

---

## Crash 194: `8eec3ff86de664d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145595`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS ()); CREATE VIRTUAL TABLE 
```

---

## Crash 195: `eb3f2fb70158ad3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146047`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE (SELECT DISTINCT * FROM p WHERE FALSE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 196: `4783b9b5b48ce949` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146183`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p
```

---

## Crash 197: `571c2ee955695df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147129`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY); SELECT count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY TRUE DESC NULLS LAST) AS ic_73x5gw_un_jml_1_y_32m0285dlsh_i4_n_rqtz7y__h_6b_76_4_m_43_u_8
```

---

## Crash 198: `61c1cdb8bc2a6771` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT NULL LIKE CASE WHEN FALSE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE THEN CURRENT_TIME END ESCAPE CURRENT_D
```

---

## Crash 199: `4d41ce955e199680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148247`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE FALSE MATCH CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p SELECT DISTINCT
```

---

## Crash 200: `a7110e68ba67ae9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148656`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (count(*) OVER ())) AS q435_13_j3c5iz WHERE TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 201: `90964cceb72bda1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149048`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (SELECT * FROM p GROUP BY CURRENT_DATE) AS q435_13_j3c5iz WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 202: `30eaf5d89630f1e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149580`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 203: `2c9dcc915657cc79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149932`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p LEFT OUTER JOIN p NOT INDEXED USING (c1); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 204: `53295cc32b5bd4ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152979`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE NOT IN (-5056922.11E-0363159379445149280433892755064758211386232888746543265756844588885, FALSE, CURREN
```

---

## Crash 205: `df5a89c18f723ef7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153040`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE NOT IN (NULL, FALSE, CURRENT_DATE))) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 206: `38fd9c0318a69fdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153046`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE NOT IN (CURRENT_TIMESTAMP, FALSE, CURRENT_DATE))) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0
```

---

## Crash 207: `6ee9cb4470fc4eff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153052`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (TRUE NOT IN (-5056922.11E-0363159379445149280433892755064758211386232888746543265756844588885, CURRENT_TIME)
```

---

## Crash 208: `cd2e9ba03ef317cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153844`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT NOT CURRENT_TIME AS a FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 209: `5c048c1a3d83835b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154192`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL)) SELECT group_concat(CURRENT_DATE, ' WqQ-c') AS a FROM p; SELECT 
```

---

## Crash 210: `6717f9da553651e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154314`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (FALSE)) SELECT group_concat(CURRENT_DATE, ' WqQ-c') AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 211: `71a8777ff6cbda48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155592`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIME)) SELECT max(CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_DATE ORDER BY TRUE DESC NULLS LAST) 
```

---

## Crash 212: `be3fea1dea0530ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164697`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (c2) AS (SELECT count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY (VALUES (TRUE)) DESC NULLS LAST) AS ic_73x5gw_un_jml_1_y_32
```

---

## Crash 213: `b7c25e44c9d0616f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165603`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW 
```

---

## Crash 214: `8ad7b32b7cfa5ff3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168668`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT TRUE, rowid INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); EXPLAIN QUER
```

---

## Crash 215: `c7176c6e8a303214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168832`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT TRUE, rowid INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); EXPLAIN QUER
```

---

## Crash 216: `2e7f1fcc62d12479` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168969`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT TRUE, rowid INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); SELECT * FRO
```

---

## Crash 217: `e97815fdd8567b0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169505`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (count(DISTINCT CURRENT_DATE) FILTER (WHERE NULL)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 218: `6cccc7a3bfd2904a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171141`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (json_type(FALSE)); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 219: `50655f4528cc151a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171337`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (random()); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 220: `fc456c1fe63509e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171367`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_D
```

---

## Crash 221: `3175169aa310be63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173253`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEF
```

---

## Crash 222: `f24c6a26fe0b324a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173460`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT X'b3c9aAE8365472'); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 223: `a2555aad4545e4c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174819`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); REPLACE INTO p VALUES (NULL IN (SELECT * FROM p)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VA
```

---

## Crash 224: `a145797cbbffb8a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174972`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (NULL IN (SELECT * FROM p NATURAL JOIN p NOT INDEXED)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 225: `d3acbd024fd452d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175108`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (NULL IN (SELECT * FROM p)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 226: `39c30f8c043d6872` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176227`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p VALUES (FALSE LIKE NULL ESCAPE NULL); VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP DESC GROUPS BETWEEN UNBOU
```

---

## Crash 227: `5dfcd38f30dfc35c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177351`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT -529082623846990769841580927004537930196346471525254538064120789812.7403980554337225771572417); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES 
```

---

## Crash 228: `42df70dab32b2edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177960`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (min(CURRENT_TIMESTAMP)); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 229: `79ba2cbfa2009800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181770`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (ORDER BY NULL ASC NUL
```

---

## Crash 230: `ce65b245e7fc719e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181790`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT avg(CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME ORDER BY count(*) FILTER (WHERE NULL) ASC RANGE BETWEEN UNBOUNDED PRECEDING AND CURRE
```

---

## Crash 231: `210978bff78ac08f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181808`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY +count(FALSE) OVER (PARTITION BY TRUE % 
```

---

## Crash 232: `141c72b818fdb81c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181830`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIME << (CURRENT_TIME) NOT IN (VALUES (RAISE(IGNORE) + RAIS
```

---

## Crash 233: `a98ee0bd14486932` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181844`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TI
```

---

## Crash 234: `6b68eb767265b63b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181850`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (changes() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING A
```

---

## Crash 235: `755995f1899f5d49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181902`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM (t1 LEFT OUTER JOIN (p) LEFT JOIN p AS k_____) WHERE CURRENT_TIMESTAMP GROUP
```

---

## Crash 236: `f00dee3b5c62e074` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181950`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a, c1, c3); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS () ORDER BY FAL
```

---

## Crash 237: `ac5252a32189ac29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182234`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 238: `d5a6685a0b1ab168` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182610`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY CURRENT_TIME
```

---

## Crash 239: `99f4d4f23229e770` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182621`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY RAISE(IGNORE
```

---

## Crash 240: `dc429ba843bb792a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); WITH RECURSIVE t3 AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP * FALSE) UNION ALL VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 241: `4797eec50fa697a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186263`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0
```

---

## Crash 242: `8be06de207771c5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (NULL), b VARCHAR(255) CHECK (TRUE), c3 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (NULL); PRA
```

---

## Crash 243: `932a8faf9d1532f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187033`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WH
```

---

## Crash 244: `cafad8db8471dc0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187231`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN TRUE IS FALSE THEN CURRENT_TIMESTAMP 
```

---

## Crash 245: `823a55ea71b33493` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187445`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN TRUE IS FALSE IS NOT TRUE THEN CURREN
```

---

## Crash 246: `ada330e636890b17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188938`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT TRUE AS ic_73x5g
```

---

## Crash 247: `77488d6f0751eeae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189355`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) INTERSECT SELECT * FROM q NOT
```

---

## Crash 248: `6837e3f58783b1ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190377`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB, rowid INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED , q AS 
```

---

## Crash 249: `348bbec0e1fbc9d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191270`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (CURRENT_TIME)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED NATURAL LE
```

---

## Crash 250: `6db2f4cbfdbdd4e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192798`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (CURRENT_DATE - NULL)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED LEF
```

---

## Crash 251: `0b80f6b62459607b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193079`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (CURRENT_TIME)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (FALSE)) AS a NA
```

---

## Crash 252: `3fe11021a80be8e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193258`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (SELECT TRUE LIMIT CURRE
```

---

## Crash 253: `5631a9a48385ca3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194256`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (max(NULL)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 254: `3e7d5d9a5879e451` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194614`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (lower(NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAUL
```

---

## Crash 255: `73287c05a4dc5227` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195022`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (json_array(NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p V
```

---

## Crash 256: `8b2466c4a3f81519` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202130`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE); SELECT * FROM q ORDER BY CURRENT_TIME LIMIT TRUE; CREATE VIRTUAL TA
```

---

## Crash 257: `33f7c27908a0ab3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202444`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE) UNION VALUES (CURRENT_TIME); VALUES (X'Ae1c059C9b14Ac'); CREATE VIRT
```

---

## Crash 258: `ae96bab8849bfef8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203258`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p SELECT * FROM p NOT INDEXED; VALUES (json(NULL), NULL); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 259: `a276a9fbfd9028ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204875`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p SELECT * FROM q ORDER BY CURRENT_TIME LIMIT FALSE, TRUE; EXPLAIN QUERY PLAN VALUES
```

---

## Crash 260: `9572c120efad28a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211248`

```sql
SELECT printf('%.*s', 9223372036854775807); SELECT printf('%d', 2147483648, '0S__-rBH U9jB- M6 '); SELECT printf('%.*f', -1, 1e-308); SELECT substr('W d_', 9223372036854775807, -1); CREATE VIRTUAL TAB
```

---

## Crash 261: `32c3303a601ae9e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211887`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE, * FROM t2 NOT INDEXED WHERE RAISE(IGNORE) COLLATE RTRIM BETWEEN TRUE AND +FALSE INTERSEC
```

---

## Crash 262: `c7100ebea6067f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217475`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p SELECT * FROM q ORDER BY CURRENT_TIME LIMIT 850; EXPLAIN QUERY PLAN VALUES (TRUE);
```

---

## Crash 263: `cd05ea5ffeb5da74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220150`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p NOT INDEXED ORDER BY CURRENT_TIME LI
```

---

## Crash 264: `97f15e663b47251d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226200`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED NATURA
```

---

## Crash 265: `cad796a2dfa70452` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226324`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP
```

---

## Crash 266: `546c9a49db6cdd11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226764`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (json_array(FALSE, FALSE)); CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); REPLACE INTO p VAL
```

---

## Crash 267: `f665eb6acef5934d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229041`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (lower(lower(lower(lower(lower(lower(lower(lower(lower(random())))))))))); CREATE VIRTUAL TAB
```

---

## Crash 268: `a9b88f7933a9f17b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229249`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (lower(lower(lower(lower(lower(lower(count(*)))))))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 269: `765406e623a3d5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230952`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (SELECT * FROM p AS f_ CROSS JOIN p) AS a
```

---

## Crash 270: `b70960aabd010cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231409`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURRENT_TIME) UNIO
```

---

## Crash 271: `66ca01a069f7cda0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233349`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (-5056922.11E-0363159379445149280433892755064758211386232888746543265756844588885 / FALSE)); INSERT INTO
```

---

## Crash 272: `1dafd8c807cd6420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233509`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (CURRENT_DATE / FALSE)); INSERT INTO q DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 273: `4e92322325c6ab58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233742`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED , (VALUES (FALSE)) AS a GROUP B
```

---

## Crash 274: `7777cfe20ae03a0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233980`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIME AS ic_73x5gw_un_jml_1_y_32m0285
```

---

## Crash 275: `beafb564327fb017` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235667`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT * FROM (VALUES (
```

---

## Crash 276: `37198d29d51aa40d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT * FROM (VALUES (
```

---

## Crash 277: `ba6de28d636afc5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235863`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT * FROM (VALUES (
```

---

## Crash 278: `44b85016b892a752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236826`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN CURRENT_TIME NOT IN (VALUES (TRUE)) I
```

---

## Crash 279: `857727bff062d0c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236973`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN FALSE IS NOT TRUE THEN CURRENT_TIMEST
```

---

## Crash 280: `99b2c25fe97a2091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238298`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); WITH RECURSIVE t3 AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTU
```

---

## Crash 281: `fdf0847ccf0a5c0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239285`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); WITH RECURSIVE t3 AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE) EXCEPT VALUES (CURRENT
```

---

## Crash 282: `0df408d88a573bd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239457`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); WITH RECURSIVE t3 AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP) UNION 
```

---

## Crash 283: `b6be37c14b36425d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242594`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT X'4BBEebeD'); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM t2 WHERE CURRENT_TIMESTAMP 
```

---

## Crash 284: `5f76d955795ff1a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242651`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * UNION VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM ((q JOIN (SELECT p.*) AS zh LEFT JOIN p NOT INDEXED) LEFT JOIN (t2 AS a NATU
```

---

## Crash 285: `d8e314ee3fbba710` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246520`

```sql
SELECT printf('%.*g', 2147483648, 1.0); SELECT printf('%d', 2147483647, ' x07 -Q'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO q VALUES (FALSE, FALSE IS NOT
```

---

## Crash 286: `a7eb04ce559c0ecf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252886`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); SELECT rowid, * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 287: `a9b3abf83f09c85a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253291`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); REPLACE INTO p VALUES (json_type(-464389)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p SELECT DISTIN
```

---

## Crash 288: `3bf75ec35f97f27c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253802`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME, CURRENT_TIME ASC NULLS LAST; SELECT DISTINCT avg(CURRENT_TIME) OVER () AS ic_73x5gw_u
```

---

## Crash 289: `12bddbfe48c8064f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255475`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); SELECT * FROM p N
```

---

## Crash 290: `1e991b1d64d72133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256054`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT TRUE, rowid INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT -CURRENT_TIMESTAMP << CURRENT_TIMESTAMP AS
```

---

## Crash 291: `158eb7f6b50a243b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY, rowid INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---
