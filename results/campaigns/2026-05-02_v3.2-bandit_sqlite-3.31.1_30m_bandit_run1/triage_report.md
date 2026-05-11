# Crash Triage Report

**Total crashes:** 241  
**Unique crash sites:** 241  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 241 | 241 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `eccb94fcefbe9c03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000066`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.* FROM q INDEXED BY rowid WHERE ~p.c1 ORDER BY format('-A ___8_6-UC-- V0l', CURRENT_TIME || CURRENT_TIME COLLATE BINARY | CURRENT_TIM
```

---

## Crash 2: `b572946200b4911f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000227`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE RAISE(IGNORE)) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); WIT
```

---

## Crash 3: `f350046dac993f0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000286`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT OR REPLACE INTO r VALUES (CAST(CURRENT_TIME AND +CASE (CURRENT_TIMESTAMP) COLLATE NOCASE WHEN FALSE -> changes() THEN CURRENT_DATE 
```

---

## Crash 4: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000868`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 5: `deb866c8e595b143` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001002`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3); INSERT INTO q SELECT *, *; ANALYZE t3; SELECT substr('x_', 9223372036854775807);
```

---

## Crash 6: `3dce3c53a5e052e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001606`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(rowid REAL GENERATED ALWAYS AS (RAISE(IGNORE) MATCH NULL COLLATE BINARY) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (s
```

---

## Crash 7: `c0b6f5f6d3ecac71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002108`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO q VALUES (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP % (VALUES (TRUE))); PRAGMA quick_check; CREATE TAB
```

---

## Crash 8: `bf71e3bb4bcf9214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002794`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 9: `40f7ad04ed5286ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002841`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (CASE quote(CURRENT_TIMESTAMP) WHEN CURRENT_TIMESTAMP COLLATE RTRIM IS CURRENT_TIMESTAMP GLOB ze
```

---

## Crash 10: `8fe31ad5058ab139` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003048`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q
```

---

## Crash 11: `9449089d95b51be4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003054`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 12: `d9450ebff9956623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 13: `a758152b85851048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003125`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT NULL NOT NULL AS d, RAISE(IGNORE) << NULL IS NOT NULL AS fw16_w____ FROM s JOIN p b ON t3.c3; SELECT
```

---

## Crash 14: `9924b68839780ddc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003132`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 15: `9be5cb0921bed3f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003399`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 16: `0a646e41bfb7dcd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003423`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 17: `c1dea5a4653a39b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004578`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES (-NULL IN (CURRENT_TIME - RAISE(IGNORE) << RAISE(IGNORE) <= FALSE NOT LIKE CURRENT
```

---

## Crash 18: `9e4cff89a861e1f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005117`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, CURRENT_TIMESTAMP >> total_changes() OVER (PARTITION BY RAISE(IGNORE) ORDER BY TRUE DESC NULLS FIRST GROUPS BETWEEN UNB
```

---

## Crash 19: `673e8cd1512bbac9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006184`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (group_concat(FALSE) FILTER (WHERE ~CURRENT_TIME MATCH NOT EXISTS (SELE
```

---

## Crash 20: `7ff5d9867a5f8d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006233`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (CURRENT_TIME || RAISE(IGNORE)); ANALYZE q; CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE 
```

---

## Crash 21: `6af252c0413faf41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006391`

```sql
SELECT printf('%.*s', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT NOT FALSE IS NULL IS NOT DISTINCT FROM CURRENT_TIMESTAMP MATCH CURRENT_TIME >= CURR
```

---

## Crash 22: `e6663f1cc157cb9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007242`

```sql
SELECT printf('%.*e', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO q (a, a, a) VALUES (CASE CURRENT_TIMESTAMP WHEN CURRENT_DATE COLLATE RTRIM THEN up
```

---

## Crash 23: `331605af81c3a957` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007446`

```sql
SELECT printf('%lli', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s DEFAULT VALUES; SELECT FALSE AS a FROM (SELECT q.* FROM s WHERE (NULL) LIKE NULL 
```

---

## Crash 24: `02ac56822704e07e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007577`

```sql
SELECT printf('%.*e', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (c1) VALUES (CASE RAISE(IGNORE) IS NULL WHEN count(DISTINCT CURRENT_DATE) NOTNULL THEN 
```

---

## Crash 25: `8b2fe750258d1014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007722`

```sql
SELECT round(1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (p.c3, CASE WHEN CASE WHEN CURRENT_DATE THEN CURRENT_DATE IS NULL % CURRENT_TIMESTAMP NOT NULL MATCH C
```

---

## Crash 26: `796a1348b6e93d90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008115`

```sql
SELECT round(-0.0, -1); SELECT round(1e-308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT p.*, CASE 913170 WHEN RAISE(IGNORE) THEN CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP 
```

---

## Crash 27: `21191fc3de0ab68a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014570`

```sql
SELECT substr('-Vo-wBc -O -', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, b); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE q AS MATERIALIZED (WITH RECURSIVE p (c3) A
```

---

## Crash 28: `f2f3d79923549fcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015058`

```sql
SELECT printf('%.*g', 9223372036854775807, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN WITH t3 AS MATERIALIZED (SELECT q.* EXCEPT SELECT p.* FROM q WHERE +TRU
```

---

## Crash 29: `ab6952ff769a856d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015357`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON TRUE MATCH EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CAST
```

---

## Crash 30: `e12984361b33517f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015603`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT
```

---

## Crash 31: `83ae2f6a7ad9f5f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016121`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 32: `4de8c2b2fd6256a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016254`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); 
```

---

## Crash 33: `b82adb84651d3d05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016270`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); 
```

---

## Crash 34: `73e33ec8e008db45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016773`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 35: `fb00cef571370791` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016781`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 36: `beaaf6d5f55c698e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016893`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 37: `2cb97ed1c45c8b4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016924`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 38: `7e325bea2d120971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017494`

```sql
SELECT substr('___', 9223372036854775807, 2147483648); SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(4294967295));
```

---

## Crash 39: `71028cde7072d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017517`

```sql
SELECT substr('___', 9223372036854775807, 2147483648); SELECT printf('%.*g', 4294967296, 0.01); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 40: `d539e3f176aaae8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017757`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 41: `1f3fe0a6d4eb8592` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021106`

```sql
SELECT substr('', 4294967296); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 42: `d101ea9e2e511a30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023199`

```sql
SELECT printf('%.*f', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 43: `d2740117945b10f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023909`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL, c3 FLOAT GENERATED ALWAYS AS (TRUE COLLATE RTRIM) VIRTUAL, a VARCHAR(255) DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * LIMIT count(*) FILTER (
```

---

## Crash 44: `f88d0debce5de11d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024330`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * LIMIT RAISE(IGNORE); VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 45: `483ada9c37ae752c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024751`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE IS CURRENT_TIMESTAMP COLLATE RTRIM); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 46: `f4d2fc703cf43725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024996`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSE
```

---

## Crash 47: `e5e3330a96715976` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025024`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT I
```

---

## Crash 48: `2f74e33da79e6686` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025347`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q
```

---

## Crash 49: `45d00eb82c45b6e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025483`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP < TRUE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 50: `85460d54827e0591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025925`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP IS CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 51: `9bd90f64da090e9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026062`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP COLLATE RTRIM); PRAGMA integrity_check; SELECT printf('%.*f', 214748364
```

---

## Crash 52: `50de424035f602f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031123`

```sql
SELECT printf('%u', 4294967295, ' _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, b); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME > NOT EXISTS (SELECT NULL AS h82_902681a_9ns6_uk8
```

---

## Crash 53: `526af869c17b7d98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032034`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN SELECT min(CURRENT_TIMESTAMP) AS a; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 54: `4c858405d64f3186` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034217`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 55: `9fb483f5ac9e95a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034880`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 56: `b476cdbb98617a7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036154`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_row
```

---

## Crash 57: `6cd1b0a49e999ff7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037407`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 58: `c9f8b5c034d0e2b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037524`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY K
```

---

## Crash 59: `9f989ea060d4a5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037573`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 60: `844a887794acd362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037623`

```sql
SELECT round(1e308, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 61: `c1a539bf05e287f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037719`

```sql
SELECT round(1e308, 2147483647); SELECT substr('P  s W_M', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO t1 VALUES (+CURRENT_TIME ISNULL, NULL LIK
```

---

## Crash 62: `5e3f9c56733fbbaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038001`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 63: `8de71b34ecd85829` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042249`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP << NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABL
```

---

## Crash 64: `f26c71ca9b96e828` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042409`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 65: `530cae27eb8907c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042784`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 66: `abab7e9520eca5de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042813`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 67: `3f1eb50af829a72f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043259`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP % CURRENT_TIMESTAMP); PRAGMA integrit
```

---

## Crash 68: `b63ce1862ba2071b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046463`

```sql
SELECT substr('-_-_ 9b8_ 3wq98- _', -1, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c2); SELECT p.* FROM q WHERE EXISTS (VALUES ((CURRENT_TIMESTAMP >= CURRENT_TIMEST
```

---

## Crash 69: `d85800dc6a3a2696` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046470`

```sql
SELECT printf('%.*d', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT OR ABORT INTO p VALUES (NOT -CURRENT_TIME <= TRUE GLOB CURRENT_TIMESTAMP | CURRENT_TIMESTA
```

---

## Crash 70: `336e6d9031ecaf94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047051`

```sql
SELECT printf('%.*d', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE t3 AS MATERIALIZED (VALUES (RAISE(IGNORE))) VALUES (NULL); SELECT prin
```

---

## Crash 71: `b109d62ef763d71d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047786`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE / -FALSE IS TRUE; CREATE VI
```

---

## Crash 72: `5abf9b3867a5020b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047990`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE / -TRUE; SELECT printf('%.*
```

---

## Crash 73: `906370d41d089138` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048335`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON NULL IN (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT DISTINCT t1.* FROM t1 NOT INDEXED CROSS JOI
```

---

## Crash 74: `c90396737762cb72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048588`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO r (c1, c1) VALUES (CURREN
```

---

## Crash 75: `d6415581674eb1aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048683`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 76: `57fc433a31f9df8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048914`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 77: `2f29e15ef8fe4480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048920`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || CURRENT_TIME IN (CURRENT_TIME BETWEEN CURRENT_DATE AND NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 78: `b900cbaf5c9b18e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048926`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NOT FALSE IN (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 79: `7c3c5b983e1575b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052471`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) UNIQUE); VALUES (sum(CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (+TRUE - NOT NULL | FA
```

---

## Crash 80: `70f43408cac7a815` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052553`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) UNIQUE); VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (+TRUE - NOT NULL | FALSE <> CA
```

---

## Crash 81: `0bee8cb403d1a03f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053261`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT); REPLACE INTO q VALUES (-222369513493221912689562097.26416060252740994270861604091E+972863 >= CURRENT_TIMESTAM
```

---

## Crash 82: `4d0194b627c6d75b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053635`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL); INSERT INTO p SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS l9_4 WHERE TRUE GROUP BY CURRENT_DATE W
```

---

## Crash 83: `1a8768cd20b76362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053961`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (NOT EXISTS (SELECT DISTINCT * FROM q NOT INDEXED LIMIT TRUE, CURRENT_DA
```

---

## Crash 84: `4da602b1581ccd00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054307`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOA
```

---

## Crash 85: `80c492d9378eba50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054317`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOA
```

---

## Crash 86: `ef7cc365ca4ac7be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054467`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (' Js7RRL1-' % TRUE); PRAGMA quick_check; SELECT printf('%.*g', 21474836
```

---

## Crash 87: `9bbd54291f6a0544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055051`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT X'EEcCcb9Ee3Be'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 88: `2391d44ee491d8dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055700`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT GENERATED ALWAYS AS (X'D9') STORED, a NUMERIC); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CR
```

---

## Crash 89: `8e3717128bfa5e8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060139`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS BOOLEAN)); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -
```

---

## Crash 90: `bc1040c4b163b034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 91: `c5082e16593880ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064943`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO p VALUES
```

---

## Crash 92: `89e92588277f51b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065128`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 93: `755e638ad7bd5506` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066483`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE
```

---

## Crash 94: `d6c5447bce3fc1a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067160`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 95: `563ec688fa97aff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067304`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT CAST(CURRENT_DATE AS BLOB) AS r_; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 96: `82b5377f07c59838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068564`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 97: `bec8efed0497ad32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068638`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 98: `f6ac5c31134e90f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068883`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT -01.72803929); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 99: `a1799b194fb39086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069310`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME NOT NULL)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 100: `47939c8424806ffd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069720`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 101: `f491d5e4a0379d62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070274`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIME - FALSE)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 102: `000eea0cec276fd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070910`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CURRENT_TIMESTAMP OR NULL)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(row
```

---

## Crash 103: `eb27eaddcf16f528` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071015`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X'EBF0fA5Fd767AF'); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 104: `88e2bd39af2d0424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072367`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); EXPLAIN QUERY PLAN SELECT min(CURRENT_TIMESTAMP COLLATE NOCASE) AS a; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 105: `8ae615d1d44f22bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074224`

```sql
SELECT substr('', -9223372036854775808, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, c1, c1, c3); INSERT OR FAIL INTO s VALUES (NOT EXISTS (SELECT CURRENT_TIME AS a, TRUE AS ck0f6j_
```

---

## Crash 106: `47d34fcad96b5401` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077888`

```sql
SELECT round(-1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t3 AS (SELECT * ORDER BY CURRENT_DATE DESC NULLS LAST), q (_rowid_) AS (VALUES (TRUE NOT NULL
```

---

## Crash 107: `9056a1794ae4fd8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079685`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 108: `a3623762506a62bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084123`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP IS TRUE COLLATE RTRIM); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 109: `c5017b4c6247f93c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084254`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP IS NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); I
```

---

## Crash 110: `59497c05930a48b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085236`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-4850432292664007485802646852899399468094576565261915796528567115883646037926359050118062325915817044408211055
```

---

## Crash 111: `1b3442516e1d8f58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086172`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL IS NULL | NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT 
```

---

## Crash 112: `102bb6c8ed2eb387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086276`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (TRUE))); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 113: `e2ff313026ad8c8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087851`

```sql
SELECT printf('%d', -1, '-_-b I_2o-8_2t'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (CURRENT_DATE -> FALSE | TRUE REGEXP (CURRENT_TIMESTAMP) IS FALSE IS NOT CURREN
```

---

## Crash 114: `2cd0c9eb5013315b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093539`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO q VALUES (FALSE); P
```

---

## Crash 115: `3c0cdbfbd10dfcd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098711`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 116: `3229b31693a62292` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099168`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, b REAL NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF N
```

---

## Crash 117: `96ec1db64e299921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099393`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT 'wx-i-c3 23'); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 118: `603cc217030d1157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099931`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , (VALUES (CURRENT_TIMESTAMP)) AS v NATURAL JOIN p; CR
```

---

## Crash 119: `d3e8442cd0361111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101375`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 120: `1a2ac7364b2786d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101742`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL JOIN q NATURAL JOIN p; CREATE VIRTUAL TABLE IF
```

---

## Crash 121: `ba3a3ac983bd8a09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103210`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 122: `fa7745a620028bc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103849`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q AS r___up_b4n_i3_3d6___7jdbi_h7xk35uu9_7__uz_1dss56bo__7fzcl__z__0_3_3
```

---

## Crash 123: `b3a68cf4781ac5ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105362`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 124: `e990f039c99d52e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106233`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p VALUES (CURRENT_TIME || CURRENT_TIMESTAMP << TRUE); PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 125: `c589d1e39a9d1d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106979`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON TRUE BETWEEN TRUE AND NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO p VAL
```

---

## Crash 126: `65b554174f0cf186` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107115`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON TRUE BETWEEN TRUE AND NULL MATCH TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 127: `5df2d2ca970c2f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107263`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON TRUE IS CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 128: `fd447739896370af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123308`

```sql
SELECT substr(' sT7- M-', -2147483648, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q SELECT DISTINCT * FROM q WHERE CURRENT_TIMESTAMP >> CURRENT_DATE << CURRENT_TIMESTAMP
```

---

## Crash 129: `0a549331bac43b2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124142`

```sql
SELECT printf('%f', 2147483648, '454-_  9R'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH q AS (SELECT *) SELECT *; CREATE TABLE IF 
```

---

## Crash 130: `f9c7f2b9440769c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133750`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON EXISTS (VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 131: `a3441d6053296900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136212`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); SELECT * FROM p JOIN p w4_1g_ ON CURRENT_DATE < TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VALUES (NOT EXISTS
```

---

## Crash 132: `08e9739eb3fbb526` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136940`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p VALUES (total_changes() || CURRENT_TIMESTAMP << TRUE); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 133: `b3dc25a0eb330446` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137082`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p VALUES (random() || TRUE); PRAGMA integrity_check; SELECT hex(zeroblob(2147483648));
```

---

## Crash 134: `6726a1aa37bfc163` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138011`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREAT
```

---

## Crash 135: `8752f90df6f987f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138554`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB NOT NULL DEFAULT 0.0); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 136: `5e1d701aa156658f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138673`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1
```

---

## Crash 137: `736a2e946a98e7c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140231`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT CURRENT_TIME, * FROM p) AS l9_4 , q NATURAL JOIN p; CREATE VIRTU
```

---

## Crash 138: `4cb8b70556a1d35b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140601`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT *, * FROM p) AS l9_4 , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF
```

---

## Crash 139: `f6bd91f7bf9cdd2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141289`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT FALSE, * FROM p) AS l9_4 , q NATURAL JOIN (SELECT * FROM (VALUES
```

---

## Crash 140: `9675d1c4fa177677` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141715`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (TRUE)) AS l9_4 , q NATURAL JOIN (SELECT * FROM (VALUES (CURRENT
```

---

## Crash 141: `4b31dd8a6671decd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144003`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT
```

---

## Crash 142: `fb520541b7cf6e6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144847`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS l9_4 NATURAL LEFT JOIN (SELECT * FR
```

---

## Crash 143: `1eede9809f82d3d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145098`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (p NOT INDEXED , q NATURAL JOIN p) NATURAL LEFT JOIN q; SELECT prin
```

---

## Crash 144: `ba190a015ad10f9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (p) NATURAL LEFT JOIN q; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 145: `9addb168fa9318eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146591`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c3 DATE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p , q NATURAL JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 146: `37a2d76ada1b667b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146712`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, a VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL LEFT JOIN q NATURAL JOIN p; CREATE VIRTUAL TABLE IF 
```

---

## Crash 147: `8f114a9f5881c918` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146966`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (q AS zi_4v_ LEFT OUTER JOIN p NOT INDEXED) , q NATURAL JOIN p; CRE
```

---

## Crash 148: `0e2c4fe8bc1f48b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147545`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED LEFT OUTER JOIN p NOT INDEXED ON NULL; SELEC
```

---

## Crash 149: `5f0d9b0ba5d156b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147707`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 150: `eff399bb1731d70f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147740`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE, c3 INTEGER UNIQUE); EXPLAIN QUERY PLAN SELECT min(CURRENT_TIMESTAMP) AS a FROM p , q NATURAL JOIN p; SEL
```

---

## Crash 151: `4718d8e968688169` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147967`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT min(CURRENT_TIMESTAMP) AS a FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 152: `882f1e1be8be2ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148277`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY CU
```

---

## Crash 153: `e9ba0ff905ea2de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148467`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY CU
```

---

## Crash 154: `d224529747f1fcd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149204`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURRENT_TIME) UNION ALL VALUES (NULL)) AS p0x66o35_v9_
```

---

## Crash 155: `1de8b7b2091550bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 
```

---

## Crash 156: `78a4ef7f9dc7d473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161490`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); INSERT INTO p V
```

---

## Crash 157: `81a4e5ea0c5a48d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT GENERATED ALWAYS AS (X'D9') STORED, a NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 158: `7e5fb80200d83b24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162646`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (64337913364730.12728202788088539480922516095165353769416184474083651273607612314536656434966230738141899422931
```

---

## Crash 159: `58c6ee9578ae7085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162824`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME >> FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSER
```

---

## Crash 160: `88df5ad181067184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167349`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL, a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); REPLACE INTO p VALUES (nullif(CURRENT_TIMESTAMP, CURRENT_TIME), CURRENT_
```

---

## Crash 161: `5429709e4f84f1e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167369`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL, a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); REPLACE INTO p VALUES (last_insert_rowid(), CURRENT_DATE); PRAGMA quick_
```

---

## Crash 162: `5250534f633bd591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171695`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (-CUR
```

---

## Crash 163: `c125d22abc70fc01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179796`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (TRUE OR CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 164: `a576463603ad0f73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180008`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); INSERT OR IGNORE INTO 
```

---

## Crash 165: `ec80d8593ab6bef0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180026`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ INT DEFAULT X'b8ABBC6C', c3 IN
```

---

## Crash 166: `fcc0b7dc6468c79a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181633`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 167: `e32a3f3fb5c1998e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181642`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*d', 42949
```

---

## Crash 168: `935f150f94dbf74f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181684`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 169: `3aae2c0dca44133c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181699`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 170: `e996169432cd21c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181756`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 171: `6dc97585ff123323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184592`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQU
```

---

## Crash 172: `ab5c4ae0fae1c67d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184611`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQU
```

---

## Crash 173: `a17a4cc72539c6d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185531`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); C
```

---

## Crash 174: `fc5bb142d2121e40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186227`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p VALUES (-222369513493221912689562097.26416060252740994270861604091E+972863); PRAGMA quick_check; CREATE 
```

---

## Crash 175: `f47ae99072e03a7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186386`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT -10437); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 176: `f86e39bfaf5ad378` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186553`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE length(CURRENT_TIMESTAMP)) AS sub1; CREATE VIRTUAL TABLE IF N
```

---

## Crash 177: `5a549441532f68e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186829`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT *, count(*) AS a FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 178: `d56d3663ef142bd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187342`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP COLLATE RTRIM IS NULL AS e FROM p WHERE FALSE) AS sub1; CR
```

---

## Crash 179: `b779e7de7f14538f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189564`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (NULL > NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 180: `d0a9aa440c2ee1cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191902`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 181: `affd5b7214096549` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192251`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS FLOAT)); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 182: `1d3dcd5cc7cf6663` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194415`

```sql
SELECT substr('', -1, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 VALUES (hex(CURRENT_DATE) OVER (PARTITION BY RAISE(IGNORE) >> FALSE IS NULL != TRUE
```

---

## Crash 183: `6bea325392d748c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202050`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (FALSE % FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 184: `f2199815ef7cc198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202466`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER PRIMARY KEY); REPLACE INTO q VALUES (' Js7RRL1-' % TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 185: `fae3bb63eb15f7b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202623`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (NOT EXISTS (SELECT DISTINCT * FROM q NOT INDEXED LIMIT TRUE, TRUE)); PR
```

---

## Crash 186: `cd53b961c94a6cef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202763`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (NOT EXISTS (VALUES (CURRENT_DATE))); PRAGMA quick_check; SELECT printf(
```

---

## Crash 187: `55540e46f412b82c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202847`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (NOT EXISTS (SELECT DISTINCT * FROM q NOT INDEXED LIMIT TRUE > CURRENT_T
```

---

## Crash 188: `583897dab2cbd317` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203002`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NUL
```

---

## Crash 189: `423bca600b64c59e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204124`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL); INSERT INTO p SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS l9_4 WHERE TRUE GROUP BY CURRENT_DATE W
```

---

## Crash 190: `42eac358fdecdd07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205032`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT '-  K2  474 45-  i'); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CRE
```

---

## Crash 191: `2e3547e3f8a3fd40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205585`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT); REPLACE INTO q VALUES (-222369513493221912689562097.26416060252740994270861604091E+972863 >= -222369513493221
```

---

## Crash 192: `a94d029cd06e0a25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205970`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); INSERT INTO p SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY C
```

---

## Crash 193: `78feaeecec3f2373` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207655`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (count(DISTINCT CURRENT_DATE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 194: `e7cc2f24408c2d28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207898`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) UNIQUE); VALUES (sum(TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAULT VALUES; ANALYZE p;
```

---

## Crash 195: `7190e6333e7058a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214418`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND EXISTS (VALUES (NULL)) % TRUE); CREATE VIRTUAL TABL
```

---

## Crash 196: `636668a0d566a573` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214581`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 197: `747da212760f2c8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214587`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND CURRENT_TIME % TRUE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 198: `6127956f4442464f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214610`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON TRUE OR CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE q; SELE
```

---

## Crash 199: `df7e411a01074c5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214802`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON CURRENT_TIMESTAMP GLOB FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (FALSE); PRAGMA
```

---

## Crash 200: `5aaf9d4f41584bcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214971`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON NOT EXISTS (VALUES (TRUE) INTERSECT VALUES (CURRENT_DATE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 201: `10389a93eaf4b74c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215372`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT, c1 GENERATED ALWAYS AS (a + 0) NOT NULL, a NUMERIC UNIQUE); SELECT * FROM p JOIN p t9o_ ON NULL IN (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 202: `a696887b7ae5854d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215641`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL T
```

---

## Crash 203: `f5dcc7f4cabd1ab3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215994`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE NULL NOT NULL; CREATE VIRTUAL TABLE IF N
```

---

## Crash 204: `92dac60804c414ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216086`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABL
```

---

## Crash 205: `40ff06464d2c3973` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216236`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE TRUE = TRUE; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 206: `49e0e59d16b3977e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216834`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE -CURRENT_DATE << CURRENT_TIMESTAMP; SELE
```

---

## Crash 207: `05238c72d3ef435b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217243`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE -FALSE IS FALSE IS FALSE; CREATE VIRTUAL
```

---

## Crash 208: `878d11fb48f9eb38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217576`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p GROUP BY NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 209: `7df9d980d113e9d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219205`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC CHECK (CURRENT_TIME IS NOT FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VA
```

---

## Crash 210: `6c4274e2f498e095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220545`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT GENERATED ALWAYS AS (TRUE) VIRTUAL, a VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NA
```

---

## Crash 211: `c77bdd2943a68e17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222062`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 212: `e2edf92862db2e85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222957`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON FALSE IS NOT NULL || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND EXISTS (VALUES (NULL)) % TRUE); CREATE VIRTUAL TABL
```

---

## Crash 213: `733e48a835d10c35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223093`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON FALSE IS NOT NULL || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VALUES (NOT EXIS
```

---

## Crash 214: `dc95bb16a4718a6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223099`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON FALSE IS NOT NULL || CURRENT_TIMESTAMP IN (CURRENT_TIME BETWEEN CURRENT_DATE AND EXISTS (VALUES (NULL)) % TRUE); CREATE VIRT
```

---

## Crash 215: `ef55e774523de92a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223107`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); SELECT * FROM p JOIN p t9o_ ON FALSE IS NOT NULL || NOT FALSE IN (CURRENT_TIME BETWEEN CURRENT_DATE AND CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 216: `cb6669d21c94c9bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226590`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (sum(NULL)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 217: `306f0918ddcbb13e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226840`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) UNIQUE); VALUES (sum(TRUE)); SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSE
```

---

## Crash 218: `443d1cb33c2ad81a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228463`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT); REPLACE INTO q VALUES (1.0590792971900639120727035315692636301224207753895981231585114e+199902402334700357490
```

---

## Crash 219: `f34f5a295511a4f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228809`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT); REPLACE INTO q VALUES (X'b8ABBC6C' >= CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 220: `b3ee87b50be42bbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230552`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); 
```

---

## Crash 221: `35890769d466aaa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231739`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (0.0 % FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 222: `cb33ac4905e91d3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231928`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT UNIQUE); REPLACE INTO q VALUES (0.0 % TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 223: `4f3c718c6860a360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239089`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p VALUES (random() || TRUE); PRAGMA integrity_check;
```

---

## Crash 224: `d3dd2435b1b6d901` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245613`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT (VALUES (count(*) FILTER (WHERE EXISTS (VALUES (CURRENT_TIME))) OVER ())) AS
```

---

## Crash 225: `0f588ca320331f1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245757`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT (VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER ())) AS e FROM p WHERE FA
```

---

## Crash 226: `290ee4efb1a8d7bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246052`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP COLLATE RTRIM AS e FROM p WHERE FALSE) AS sub1; CREATE VIR
```

---

## Crash 227: `be3874815f527d45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246747`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE length(FALSE)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 228: `001b919cd9505a2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247325`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p VALUES ('3  aw-_R 7KR-_lDNI-'); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 229: `f7f7de2c8173373d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247428`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 230: `b97d0a6dbd5100e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249863`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); SELECT CAST(CURRENT_DATE AS BOOLEAN) AS r_; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 231: `a8eff2555783336d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250587`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT CAST(TRUE AS TEXT) AS y; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 232: `d26e742015495199` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251858`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE, rowid BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 233: `08510fbc5f654d86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252901`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL << NULL - total_changes() - CURRENT_TIME - TRUE - CURRENT_TIMESTAMP - CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAU
```

---

## Crash 234: `1afd00c90ef565f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253023`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL << CURRENT_TIME - CURRENT_TIME - TRUE - CURRENT_TIMESTAMP - CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 235: `4db77f3683ded2f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253305`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL << total_changes() - total_changes() - CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 236: `47844fe2ad6c7c67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253424`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL << total_changes() - TRUE - CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE 
```

---

## Crash 237: `aa47b483a08f1a9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253546`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (TRUE - total_changes() << TRUE - total_changes())); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VI
```

---

## Crash 238: `805fb9e76a3d77a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253646`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (TRUE - total_changes() << NULL)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 239: `f3191438d2d00480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253846`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); INSERT INT
```

---

## Crash 240: `f3a3a83ba3773952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253869`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); INSERT OR IGNORE INTO 
```

---

## Crash 241: `b635670aa35b301d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253882`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE 
```

---
