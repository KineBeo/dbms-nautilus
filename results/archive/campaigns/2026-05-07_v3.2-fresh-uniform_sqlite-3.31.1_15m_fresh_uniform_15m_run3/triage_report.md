# Crash Triage Report

**Total crashes:** 128  
**Unique crash sites:** 128  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 128 | 128 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9bbb8eb99d2b37e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000054`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 (c3) VALUES (CURRENT_TIMESTAMP IS NULL AND RAISE(IGNORE) == char(+substr(sum(CURRENT_TIME) FILTER (WHERE TRUE), CURRENT_DATE NO
```

---

## Crash 2: `2637b6ebcea467c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); SELECT s.* FROM t1 JOIN t3 cz63_f1_u_4__a_eu990ry1a4gi0 ON CURRENT_DATE COLLATE RTRIM LIKE CURRENT_TIMESTAMP ESCAPE RAISE(IGNORE) % a
```

---

## Crash 3: `ad19117ebdcf8f3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000236`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT DISTINCT *, FALSE FROM t2 AS a WHERE -CURRENT_TIME <= FALSE != NOT FALSE COLLATE BINARY LIMIT RAISE(IGNORE) + TRUE IN (RAISE(IGNORE)) NO
```

---

## Crash 4: `b8d88303e91b7d40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000598`

```sql
SELECT substr('-9 _2-_ A-y-_ C30-6', 0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, b, c1); INSERT OR IGNORE INTO r VALUES (TRUE & TRUE IS NOT NULL NOT NULL << CURRENT_TIMES
```

---

## Crash 5: `731df941ac5490be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001135`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2, b, c2, c1, b, _rowid_, _rowid_); INSERT INTO p VALUES (CURRENT_TIMESTAMP IS NOT CURRENT_TIMESTAMP >> -CURRENT_TIME > CURRENT_TIME -> NU
```

---

## Crash 6: `498c20bab2bf5215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001244`

```sql
SELECT printf('%lld', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO r VALUES (trim(-RAISE(IGNORE) NOT BETWEEN TRUE AND ~FALSE REGEXP CURRE
```

---

## Crash 7: `6b0fff272646a5d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001375`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES ((--TRUE OR TRUE)); PRAGMA integrity_check; SELECT printf('%.*e', 2147483648); SELECT he
```

---

## Crash 8: `958880c65e0dd095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001415`

```sql
SELECT substr(' - _6- 2', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIMESTAMP COLLATE NOCASE NOT BETWEEN NULL IS NOT NULL AND 
```

---

## Crash 9: `a76a9482a97fac40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001501`

```sql
SELECT substr('U-7gu ', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO t3 VALUES ((SELECT *, * FROM s WHERE CURRENT_DATE % +
```

---

## Crash 10: `a9e181db7af9f1b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001521`

```sql
SELECT round(0.0, 2147483648); SELECT printf('%f', 4294967295, 'J4'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t2 (_rowid_, c2, c2) VALUES (CASE WHEN max(-last_insert_rowid
```

---

## Crash 11: `a1b42fdc7d29b399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001642`

```sql
SELECT printf('%.*d', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT p.*, s.*, group_concat(~CURRENT_DATE BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP COLLATE NOCASE ->
```

---

## Crash 12: `a890575550455c8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001784`

```sql
SELECT round(-0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT r.* FROM s LEFT OUTER JOIN p NOT INDEXED CROSS JOIN (SELECT t3.* UNION ALL
```

---

## Crash 13: `25103eacfe8d8977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004126`

```sql
SELECT hex(zeroblob(0)); SELECT substr('-wHU- 6gF _ ', 9223372036854775807, -2147483648); SELECT round(-1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR FAIL INTO t3 V
```

---

## Crash 14: `c84e5238b3f37aab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006391`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 15: `a74875445f3d3423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006397`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 16: `03924241cec88dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006448`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 17: `cc921f25603a838b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007210`

```sql
SELECT round(1e308, 4294967296); SELECT printf('%.*s', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH t1 AS (SELECT CURRENT_TIME ORDER BY NULL ASC, FALSE DE
```

---

## Crash 18: `e33d4c5599c1bcba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007279`

```sql
SELECT printf('%.*s', 0, -1e308); SELECT printf('%.*s', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE MATCH RAISE(IGNORE)
```

---

## Crash 19: `3de1bebe39cd298c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011224`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT 
```

---

## Crash 20: `8cf489fb16db949d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012553`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, _rowid_); VALUES (FALSE);
```

---

## Crash 21: `9d78592f3bfbf580` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012559`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 22: `121a319973f024be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012568`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 23: `405d3b773eac2e72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013027`

```sql
SELECT printf('%lli', -2147483649, '- 6_ '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO r VALUES (RAISE(IGNORE) IS NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT IN
```

---

## Crash 24: `a2b9de60251d1032` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015205`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, a, a); INSERT INTO t3 VALUES (CAST(CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP > CURRENT_TIME COLLATE RTRIM A
```

---

## Crash 25: `3a3b0e65efb664dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020061`

```sql
SELECT printf('%.*e', -2147483649, -1e308); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 26: `cf1abb8101c87107` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020132`

```sql
SELECT printf('%.*f', -2147483649, -1e308); SELECT printf('%.*g', -9223372036854775808, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 27: `8691f9e3db875013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021929`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH t3 (c2, _rowid_) AS (SELECT * ORDER BY FALSE DESC, FALSE AND CURRENT_TIMESTAMP DESC NULLS FIRST), r AS (VALUES (TRU
```

---

## Crash 28: `cd5a2058ffea2d65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024412`

```sql
SELECT substr('_-Lf-', -1, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, b, c3); INSERT INTO t2 DEFAULT VALUES; VALUES (RAISE(IGNORE)); SELECT hex(zeroblob(-1));
```

---

## Crash 29: `a91e1097e0513c09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024460`

```sql
SELECT substr('_-Lf-', -1, -1); SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t2 DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (~lag((CAST(CURRENT
```

---

## Crash 30: `80d11af55c31f254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024517`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, b, c3); INSERT INTO t2 DEFAULT VALUES; VALUES (RAISE(IGNORE)); SELECT hex(zeroblob(-1));
```

---

## Crash 31: `24ed71b7d6f0c2f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025534`

```sql
SELECT printf('%.*f', 1, -1e308); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 32: `c5ecde67497d034d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026100`

```sql
SELECT printf('%x', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME);
```

---

## Crash 33: `16d84087e07bfdcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026772`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL NOT NULL) UNION VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 34: `3d5d7c515a3b193f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029151`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 35: `c67d0426f0025f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029230`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t2 (c3, _rowid_, b) VALUE
```

---

## Crash 36: `56ecb75bda7e6778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030099`

```sql
SELECT printf('%.*s', -9223372036854775808); SELECT printf('%.*d', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s VALUES (trim(CASE WHEN +changes() FILTE
```

---

## Crash 37: `7a5926f44d494f5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030366`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL DEFAULT CURRENT_TIMESTAMP, c3 BOOLEAN DEFAULT ''); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 38: `d3ae32a1a90d95dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030761`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 39: `513895f51db6b5d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030946`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIME GLOB CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check;
```

---

## Crash 40: `fcceaab187da829e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030970`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIME GLOB CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check;
```

---

## Crash 41: `98ddae15a87d9d33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030989`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIME GLOB CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check;
```

---

## Crash 42: `d8c592c004857b24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031339`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 43: `407ac91edf371731` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032747`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `3550de12779637b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033331`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE total_changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 45: `7727661cf26d3d1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033789`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); S
```

---

## Crash 46: `172b410db2ced166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033943`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 47: `3922f652e67cae35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036180`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CU
```

---

## Crash 48: `783134c1e20b80e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037419`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 49: `ee9af2bf8e789455` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037708`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT OR FAIL INTO q VALUES (CURRENT_TIME > FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 50: `c7a5e96a318b901a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038647`

```sql
SELECT printf('%f', 9223372036854775807, 'y'); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 51: `825237e7bcbf4c14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO t2 VALUES (~CASE CURRENT_
```

---

## Crash 52: `b6c7c2df569a47d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044596`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); INSERT INTO p (rowid) VALUES (FALSE == TRUE); PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 53: `87b66baa3ba4b3dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049677`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT '- -u61___Xi 2Y', b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f'
```

---

## Crash 54: `07a63009610318a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049836`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 55: `bb9fc230454d26b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049843`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT TRUE, b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -214748364
```

---

## Crash 56: `3dcb18ac5824ff8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050282`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT OR FAIL INTO q VALUES (CURRENT_TIME IS NULL > CAST(TRUE AS DATE)); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 57: `7ff3107b5293dc3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050323`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT OR FAIL INTO q VALUES (TRUE > CAST(TRUE AS DATE)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 58: `0fd2875045c1af03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051243`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 59: `b182ab6b2657c932` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051442`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP)) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT TRUE); CREATE TAB
```

---

## Crash 60: `fe5fd8faf3c2faf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051665`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME COLLATE NOCASE) UNION VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 61: `096eff265bcd05fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052369`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES ((VALUES (NULL))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q VALUES ((c3) << 
```

---

## Crash 62: `97b8e328a79fea35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052872`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 63: `ba100da792ca1967` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054556`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT TRUE != CURRENT_TIMESTAMP + TRUE AS d_gl9__9a0txq5__65_kpa_0mp_h_k_m__0873q_kgc6_80_4___1_rl_35_5lriz0
```

---

## Crash 64: `8e1fcf0eb9c95b5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054726`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT TRUE AS d_gl9__9a0txq5__65_kpa_0mp_h_k_m__0873q_kgc6_80_4___1_rl_35_5lriz0e_a1nh05laboe___1_0w__zs8k_5
```

---

## Crash 65: `5210b90cd7b35433` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056500`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE * NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 66: `707565ca23edf279` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057364`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT, c2 VARCHAR(255) DEFAULT TRUE, a DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 67: `2185fdbae76e740b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059550`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT ' 2gzZ4 __-t Ue--'); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%
```

---

## Crash 68: `20a9487a1bd144b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059774`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01); SEL
```

---

## Crash 69: `29484314e8cba085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060610`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) CHECK (CURRENT_TIMESTAMP)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 70: `34f37a4e7982d12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060978`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL DEFAULT X'Cb3FAfFc'); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO q VALUES (TRUE) ON CONFLICT DO NOTHING; PRAGMA quick_check
```

---

## Crash 71: `19b8c29e4fe8d53b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061164`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIME = CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SE
```

---

## Crash 72: `688ed4172c75e5ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061598`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NO
```

---

## Crash 73: `b78e5eab42d533ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062230`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q VALUES (0266.91609E308) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 74: `670437df52851030` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062660`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 75: `a0f88e3376a6c051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063211`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLA
```

---

## Crash 76: `db6fa946ed4cb119` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063518`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL DEFAULT CURRENT_TIMESTAMP, c3 BOOLEAN DEFAULT ''); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', -21474
```

---

## Crash 77: `bb6757ebf6bdd739` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064177`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN DEFAULT 3.93768947507E277092314101453715825620539587713102531118519769094767); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VI
```

---

## Crash 78: `d50a7e701c31cd60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072939`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE > CURRENT_DATE IN (SELECT * ORDER BY CURRENT_TIMESTAMP IS NULL
```

---

## Crash 79: `404c896a47254bc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073261`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BLOB); SELECT * FROM (SELECT *, * FROM q WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 80: `5afb44cd07a7ea38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077009`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT *, *, * FROM q WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*f', -2147483
```

---

## Crash 81: `bf2f8b8cc3ff4744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077087`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT *, *, * FROM q WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*g', 1); CREA
```

---

## Crash 82: `2549d74986acf253` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077302`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT FALSE, * FROM q WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 83: `9dd0f1b823fc33c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077689`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE NOT IN (VALUES (CURRENT_TIMESTAMP))) AS sub1; SELECT p
```

---

## Crash 84: `20cddbaba01d162c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078013`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE - CURRENT_DATE - CURRENT_DATE ISNULL % CURRENT_TIMESTA
```

---

## Crash 85: `29abaf4b5df725da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078063`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 86: `789bfc134fe78993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078069`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE NULL - CURRENT_DATE ISNULL % CURRENT_TIMESTAMP) AS sub1; CR
```

---

## Crash 87: `5cadfd7bcab53f9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078483`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE NULL IS NULL) AS sub1; SELECT printf('%.*f', -2147483649, -
```

---

## Crash 88: `61ffbf3c6c7f922b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080408`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); VALUES (NULL) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 (c3, c3, rowid, c
```

---

## Crash 89: `abd96646a1b39881` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080560`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH t3 (c3) AS (VALUES (CURRENT_TIME)), r AS (VALUES (TRUE)) SELECT *; VALUES (TRUE OR TRUE) UNION ALL VALUES (CURRENT_
```

---

## Crash 90: `e210f8c1e94fd5ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081258`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (CURRENT_DATE || CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 91: `1c2955c581b15807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082588`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (TRUE) INTERSECT VALUES (cume_dist() OVER ()); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 92: `fa10182f67bd05c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082598`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_DATE ISNULL); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 93: `d3949777e05981c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082609`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIMESTAMP / FALSE) INTERSECT VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 94: `80882a9f6e7b4e9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082622`

```sql
SELECT printf('%.*d', -2147483649, -1e308); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 95: `3b482208c9abb5a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082932`

```sql
SELECT printf('%.*e', -2147483649, -1e308); SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CASE WHEN ((RAISE(IGNORE))) IN (CURRENT_
```

---

## Crash 96: `d93dd03aa7ab7033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085328`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP * NULL * NULL * NULL * NULL *
```

---

## Crash 97: `98e0cbf8cb0c2ddb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085620`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT NULL * NULL; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 98: `a94826ec3e59ce48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089140`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g',
```

---

## Crash 99: `a16b2d6e6d1b74af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089333`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', 21474
```

---

## Crash 100: `61ff403990860d16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099228`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY, c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 101: `bdf8a567d7a45738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 102: `c92c3cf77a213323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101314`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT X'b8EfDc4FbfdEcB'); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 103: `a0774e192e0eac35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101643`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT q
```

---

## Crash 104: `c53e9d06c1908e17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102280`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); 
```

---

## Crash 105: `66bd3b365bd30ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102861`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 106: `17c41254f320012e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106345`

```sql
SELECT printf('%.*f', 4294967295); SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 (a, _rowid_, rowid, c2) VALUES (max(NULL), NOT TRUE NOT I
```

---

## Crash 107: `f84a5213ae24dc5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107700`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); 
```

---

## Crash 108: `add5a0ecefb70b05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110629`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL DEFAULT '-'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 109: `0c486afd4b46da3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111001`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 110: `c705ac8ba76b73b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124636`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE CURRENT_TIME; SELECT pr
```

---

## Crash 111: `28625b22703123f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127515`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (cume_dist() OVER (ORDER BY TRUE RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING), cume_dist() OVER (), CURRENT_DATE); CREATE 
```

---

## Crash 112: `9562c3a2f1cbf2ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127774`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT ALL * FROM (VALUES (CURRENT_TIME)) AS i_h_ ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL 
```

---

## Crash 113: `912dcfd5ba9a5582` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128046`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT DISTINCT * FROM p NOT INDEXED UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 114: `c75988f7db2be14d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129946`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE - CURRENT_DATE - CURRENT_DATE ISNULL % CURRENT_TIME) A
```

---

## Crash 115: `1fb77e8aad455ca1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130145`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE - CURRENT_DATE - FALSE) AS sub1; SELECT printf('%.*g',
```

---

## Crash 116: `5436fd19d2396259` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130265`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT count() FILTER (WHERE TRUE) AS ap_____1 FROM (SELECT * FROM q WHERE CURRENT_DATE) AS sub1
```

---

## Crash 117: `5070d2580c09baa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131334`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT * FROM q WHERE TRUE NOT IN (SELECT DISTINCT * FROM q WHERE CURRENT_TIME)) 
```

---

## Crash 118: `0eefe8312feb1428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131699`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME COLLATE NOCASE, * FROM q WHERE FALSE) AS sub1; SELECT printf(
```

---

## Crash 119: `22dbb49ae3260a64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131940`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS f030r83v_kq6o6zg1____h_895ac08___s8_280u__90j0_e_3__0
```

---

## Crash 120: `96d253d3579c78ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132125`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT NULL >= NOT CURRENT_TIMESTAMP COLLATE BINARY AS o2w6_79__2_o_1_0x4e2d_9 FR
```

---

## Crash 121: `e38666c9dd4dac04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132395`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL); SELECT * FROM (SELECT *, cume_dist() OVER () AS w0, * FROM q WHERE CURRENT_TIME) AS sub1; CREATE
```

---

## Crash 122: `e6f66d6d6bf6a025` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133006`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE t3 AS (VALUES (count() OVER ())) SELECT * FROM t3; SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 123: `86340a578c82d621` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133426`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE t3 (c3) AS (VALUES (CURRENT_TIME)) SELECT * FROM t3; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 124: `8cc11bd50948b088` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136069`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BLOB); SELECT * FROM (SELECT *, CURRENT_TIMESTAMP, * FROM q WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*f', -2147483649
```

---

## Crash 125: `833b3b698ca2e295` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136560`

```sql
SELECT printf('%.*e', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT OR ABORT INTO r VALUES (CAST(-NOT EXISTS (VALUES (~CASE FALSE || TRUE COLLATE BINARY WHEN CURRENT_DATE + 
```

---

## Crash 126: `bd0647f626c601e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137497`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE) UNION VALUES (count() OVER () OR dense_rank() OVER ()); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 127: `43e0f2c226734dfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142850`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 VALUES (EXISTS (SELECT ALL group_concat(FALSE > FALSE LIKE TRUE LIKE CURRENT_TIME) OVER (PARTITI
```

---

## Crash 128: `c7675742a4b06895` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144894`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_DATE || TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---
