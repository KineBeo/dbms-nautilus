# Crash Triage Report

**Total crashes:** 239  
**Unique crash sites:** 239  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 239 | 239 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d832d82cde4b5784` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000332`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 (c1, a, c2, c3) VALUES (CASE TRUE MATCH RAISE(IGNORE) GLOB random() FILTER (WHERE CASE CURRENT_DATE + NULL WHEN TRUE GLOB NULL 
```

---

## Crash 2: `7b13a19c9804f236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000547`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC GENERATED ALWAYS AS (RA
```

---

## Crash 3: `c33262a1dc7b44df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000555`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); SELECT abs(~NULL != CURRENT_DATE COLLATE BINARY NOT NULL) FILTER (WHERE c3) NOT LIKE -FALSE - CURRENT_TIMESTAMP IS NOT NULL != RAISE(IGNORE
```

---

## Crash 4: `895b3d87cafe1107` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000834`

```sql
SELECT printf('%.*f', -2147483649, 1e308); CREATE TABLE IF NOT EXISTS p(rowid DATE, b GENERATED ALWAYS AS (a) NOT NULL, b TEXT NOT NULL DEFAULT X'86C7BC6eEEBd0'); SELECT s.* FROM (SELECT NOT EXISTS (S
```

---

## Crash 5: `1f4ff2c040ee602d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001155`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(rowid DATE, c1 GENERATED ALWAYS AS (a + 0) ); INSERT OR FAIL INTO q VALUES (CURRENT_DATE, CURRENT_DATE MATCH NULL >= CURRENT_TIM
```

---

## Crash 6: `69614baab1692cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001354`

```sql
SELECT printf('%.*e', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME IS NOT TRUE - (rowid) AS a FROM p NATURAL JOIN q WHERE CASE WHEN -unicode(TRU
```

---

## Crash 7: `883fece9c718f88a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001397`

```sql
SELECT printf('%.*e', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT avg(CURRENT_DATE NOTNULL) ->> TRUE IS DISTINCT FROM CASE WHEN RAISE(IGNORE) THEN CURRENT_TIME COLLA
```

---

## Crash 8: `3a50fb1bbe5c160e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002455`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; WITH RECURSIVE p AS MATERIALIZED (SELECT p.* ORDER BY CURRENT_TIMES
```

---

## Crash 9: `112b7978d47113f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY, c3 BOOLEAN UNIQUE, a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 10: `840ae5abd9df6bdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002514`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (chan
```

---

## Crash 11: `ad93260e193e53a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002520`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY, c2 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 12: `54a4c106dd6744a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002758`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WIT
```

---

## Crash 13: `0998304493b468dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003182`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p
```

---

## Crash 14: `55d3e8877697966b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003371`

```sql
SELECT printf('%.*s', 1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (c3, c3) VALUES (coalesce(FALSE NOTNULL, CURRENT_TIME LIKE TRUE ESCAPE last_insert_rowid()) OVER 
```

---

## Crash 15: `1ad2bc7a593fca4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003842`

```sql
SELECT printf('%u', 2147483647, 'Ia-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (FALSE) ORDER BY ~CURRENT_TIME DESC NULLS LAST LIMIT RAISE(IGNORE) NOT NULL OFFSET CURRENT_TIME
```

---

## Crash 16: `bce12a2153aba357` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003931`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT NOT NULL AS a, p.* FROM q NATURAL JOIN p WHERE +TRUE OR CURRENT_TIME <= N
```

---

## Crash 17: `0246d008065faadd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004006`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE +TRUE OR CURRENT_TIME <= NULL; CREATE VIRTU
```

---

## Crash 18: `f14de6c1e0eb151f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004032`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 19: `c966cca2f999cda3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004038`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP OR CURRENT_TIME <= NULL; 
```

---

## Crash 20: `3eba1cfb2d3e0154` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004144`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (TRUE IS NULL COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSER
```

---

## Crash 21: `8115ba8c9d06beba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004165`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (RAISE(IGNORE))); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t1 DEF
```

---

## Crash 22: `8e7ad1245f250861` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004235`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q INDEXED BY c1 LIMIT RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 23: `964fa639610a6ef5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004269`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q LIMIT RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 24: `2226fa21edf44b59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004275`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED LIMIT RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 25: `0cf4dc6d422de800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004342`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p INNER JOIN p , q AS a INTERSECT VALUES (CURRENT_DATE); VALUES (CURRENT_DATE); SELECT substr('', 
```

---

## Crash 26: `05c41654904d23db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004681`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES ((CURRENT_TIMESTAMP IS NOT CAST(CURRENT_TIMESTAMP | FALSE AS BOOLEAN) IS NULL
```

---

## Crash 27: `aff21242e160f14e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005098`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (CURRENT_DATE) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO q VALUES (quote(TRUE IS NOT DIS
```

---

## Crash 28: `f55ad37f7de3c98a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005487`

```sql
SELECT substr('_V8', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO s VALUES (+NULL NOT IN (CURRENT_TIME <= NULL, CURRENT_TIMESTAMP >= NULL) & FALSE || TRU
```

---

## Crash 29: `fc7700619f065850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006006`

```sql
SELECT substr('0LD9_i w-', 2147483648, -2147483649); SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO r VALUES (NOT EXISTS (VALUES (-CUR
```

---

## Crash 30: `4fb4a62a47474a9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006124`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, c1); INSERT INTO t3 VALUES ((coalesce(CURRENT_TIMESTAMP & FALSE == (SELECT CURRENT_TIME), CURRENT_DATE % CURRENT_T
```

---

## Crash 31: `d842495f2d02a4fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007603`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN, c2 GENERATED ALWAYS AS (a || b
```

---

## Crash 32: `2083fdb1cb5a0a45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007810`

```sql
SELECT printf('%lli', -2147483648, 'x_4-p5F_'); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 33: `16e2ab955510c3c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008523`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) UNION ALL SELECT * FROM p WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS () ORDER 
```

---

## Crash 34: `2811655c77116d50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009035`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%.*s', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); VALUES (NULL);
```

---

## Crash 35: `7ce17930735fffd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013327`

```sql
SELECT substr('__e _mAre  899z', 2147483648, 4294967295); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 36: `ed83436a3ce4b895` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017468`

```sql
SELECT substr(' ', -1, -2147483648); SELECT round(-1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 37: `fb5bd39031622f1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018036`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TA
```

---

## Crash 38: `a8d3e99ebdb4b0b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018737`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 39: `4a4f164406965e6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018848`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 40: `776a86223cd99b23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018859`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 41: `ae4605ea7336ff4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 42: `c4498f5fdd5434e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022620`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE));
```

---

## Crash 43: `23000ba39a2ab1c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022725`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, b); EXPLAIN QUE
```

---

## Crash 44: `6b8830d734393224` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022735`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 45: `66713aa60c55b58f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024374`

```sql
SELECT round(1.0, 2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 46: `1a04cb50db6db2a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027877`

```sql
SELECT printf('%.*s', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0));
```

---

## Crash 47: `1b713746d9055dac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029033`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036
```

---

## Crash 48: `544de7ab0832850d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029277`

```sql
SELECT printf('%.*g', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0));
```

---

## Crash 49: `c276aec80baa79c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029411`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE & CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO
```

---

## Crash 50: `0bbef07429d361eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029433`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL & TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO r VALUE
```

---

## Crash 51: `c863698199eef67a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030509`

```sql
SELECT printf('%.*s', -2147483649, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check;
```

---

## Crash 52: `6533a2ea50fa3528` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030668`

```sql
SELECT printf('%x', 2147483648, ' v-_42B _B '); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 53: `3b41e7ccf24a3904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031722`

```sql
SELECT printf('%.*f', 4294967295, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0));
```

---

## Crash 54: `1a2c6e32ecb3cbde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033998`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT FALSE COLLATE RTRIM FROM p WHERE EXISTS (WITH q AS (SELECT *) VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 55: `0ad636a663b48fb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034118`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT CURRENT_TIME FROM p WHERE EXISTS (VALUES (TRUE)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); S
```

---

## Crash 56: `8206dac15991e717` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034386`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, c3 FLOAT NOT NULL); SELECT CURRENT_TIMESTAMP << CURRENT_DATE IS NOT NULL COLLATE RTRIM FROM p WHERE EXISTS (
```

---

## Crash 57: `21cfb727b996ed08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034799`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EX
```

---

## Crash 58: `c3890fc77d8db4db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EX
```

---

## Crash 59: `079cdb5ca963e952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034815`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EX
```

---

## Crash 60: `1eef7c458896cd7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034823`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EX
```

---

## Crash 61: `f37deccb6b92e090` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036923`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 62: `a196ee9a9c6e33b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038972`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (NULL)); SELECT printf('%.*f', 2147483648, 1.0); SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 63: `453033e7f3edb1f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044558`

```sql
SELECT printf('%f', -2147483649, '   07s-J-- '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0));
```

---

## Crash 64: `95d646770f0695c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045257`

```sql
SELECT printf('%.*g', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT s.*, ~TRUE AS dl_5, CURRENT_TIME -> FALSE, CURRENT_DATE COLLATE BINARY FROM t1 JOIN t1 c_ ON CASE changes() OV
```

---

## Crash 65: `a844fcbdccaa3a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046431`

```sql
SELECT printf('%.*d', -2147483649, 1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 66: `afbab32e4ec4bf13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048774`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM q JOIN q c___nz5_8_z5__5w4ic_1o2zf7212it0_8l_ ON CURRENT_DATE; CREATE VIRTUAL TAB
```

---

## Crash 67: `0d3fa4b3c9257fd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049037`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC DEFAULT -743876159570616589200720931143773050558410451284256987780648992783945261010106016005263748511510007343812870227400.3E-034, c2 FLOAT); CREATE INDEX I
```

---

## Crash 68: `80734ff74c508473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(*) OVER () ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 69: `8b38ab4ee0193f17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056062`

```sql
SELECT substr('Y', 9223372036854775807, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CASE WHEN CURRENT_DATE IS NULL REGEXP NULL THEN CAST(RAISE(IGNORE) AS INT) IS NOT
```

---

## Crash 70: `a0a0fecda9e4ad56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058465`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL CASE WHEN FALSE THEN FALSE ELSE count(*) END AS m1 FROM p NOT INDEX
```

---

## Crash 71: `e085ce76e955ccd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN DEFAULT 3887209.8); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -9223372036854775808); CR
```

---

## Crash 72: `1b2225f72080e019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061014`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -9223372036854775808); CREATE
```

---

## Crash 73: `09ad4848c39e9b5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061491`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 FLOAT NOT NULL); SELECT FALSE FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 74: `7ef5a973adfd076a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064890`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*f', -2147
```

---

## Crash 75: `983aa02449846d17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064962`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP) AS sub1; SELECT round(-1.0, 0); CREA
```

---

## Crash 76: `c44af7622af22e4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065691`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 77: `2cbd04ae83a2fcc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069734`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, b FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE
```

---

## Crash 78: `11cc34a034f337f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069876`

```sql
SELECT printf('%.*d', -2147483649); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 79: `222508a231a4c8f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071312`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO p SELECT ALL count(*) AS m1 FROM q; SELECT * FROM q NATURAL JOIN p WHERE TRUE OR CURRENT_TIME; SEL
```

---

## Crash 80: `c18b952b2943e340` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072377`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT NOT NULL AS a, * FROM q NATURAL JOIN p WHERE NULL LIKE CURRENT_TIME ESCAP
```

---

## Crash 81: `aceff3eb67f43060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073668`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP = CURRENT_TIMESTAMP; CREA
```

---

## Crash 82: `b168571917291e71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074134`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE IN (CURRENT_TIMESTAMP); CREATE
```

---

## Crash 83: `d734bc5c5f8687ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074721`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.*f', -
```

---

## Crash 84: `1a25a2c6e15d2e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074954`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE +TRUE OR +CURRENT_DATE; SELECT printf('%.*g
```

---

## Crash 85: `5e28f732d91137cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075079`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE FALSE OR +CURRENT_DATE; SELECT printf('%.*g
```

---

## Crash 86: `49814e161d90d3b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075141`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 87: `a7f020bb5a79873c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) GENERATED ALWAYS AS (NULL) STORED, c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURA
```

---

## Crash 88: `ec4c5458ee3c0cf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075668`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE FALSE | FALSE; SELECT printf('%.*g', 214748
```

---

## Crash 89: `f24c98c16bd5189e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076535`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT * FROM q GROUP BY CURRENT_TIME ORDE
```

---

## Crash 90: `62cf50c0a460d1d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077100`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE, _rowid_ INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE
```

---

## Crash 91: `7db95b8f2966ea66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078175`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL count(DISTINCT CURRENT_TIME) AS m1 FROM p NOT INDEXED; CREATE VIRTU
```

---

## Crash 92: `e66c114eef5d966a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079218`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (X'6adEAdBBFF15f2'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 93: `aac512d9e5d51894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079695`

```sql
SELECT printf('%s', -9223372036854775808, '_ --_-IW m'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 94: `6aaf81d222259fc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079702`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 95: `20bee6438e087c5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079710`

```sql
SELECT substr(' _- u _', -1, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 96: `b76b8e00cb5bad30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079725`

```sql
SELECT round(1e308, 2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 97: `d66768188abfeb57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079747`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME NOT IN (CURRENT_DATE, FALSE, C
```

---

## Crash 98: `65fff060fccd4ae8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079795`

```sql
SELECT round(1.0, -2147483649); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 99: `1c1b09bfd816c11b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088881`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (NULL IN (CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647
```

---

## Crash 100: `c7b247574c8ac44b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089194`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (_rowid_)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 101: `4f6775550792b1a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091256`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CAST(TRUE AS BLOB); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 102: `c4624e6e4cc1da7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095631`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BLOB PRIMAR
```

---

## Crash 103: `72e7127b87018680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096911`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM q WHERE -FALSE GROUP BY TRUE; PRAGMA integrity_check; SELECT printf('%.*g',
```

---

## Crash 104: `d7fdabcd6c901b83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097509`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT ALL count(*) AS m1 FROM q; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 105: `9b894370296c4ccb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097679`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT ALL count(*) - CURRENT_TIMESTAMP AS m1 FROM q JOIN p AS a; PRAGMA integrity_check;
```

---

## Crash 106: `5442e1869f05b18e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098990`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 107: `327c43b147caf2b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099156`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 108: `0b587dfb21b89fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099531`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 109: `06f38ea69160e679` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100316`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT DISTINCT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 110: `c125c26bf3c9b84b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101709`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUE
```

---

## Crash 111: `77d5b3a8ac904028` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101828`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (CURRENT_DATE) UNION SELECT * FROM p WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 112: `33351d4f42a51fd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102074`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR I
```

---

## Crash 113: `6f283f98f64ae9d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102198`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM p WHERE FALSE UNION VALUES (FALSE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 114: `786e601a28449851` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103645`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (count(*) FILTER (WHERE CURRENT_TIME IS NULL)) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES 
```

---

## Crash 115: `0e6a3c7c09a6ce80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104250`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (count(*) FILTER (WHERE NULL LIKE CURRENT_TIME ESCAPE NULL IS NULL)) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 116: `890559b5c72f5b5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104311`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); VALUES (NULL) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT ALL * FROM t1 EXCEPT VALUES (-FALSE, RAISE(IGNORE) IS
```

---

## Crash 117: `6e59f2e311f4cb6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104770`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR FAIL INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f',
```

---

## Crash 118: `5bffeb0766189b6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123801`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) UNION ALL SELECT total_changes() FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE ROWS BE
```

---

## Crash 119: `8e7e6b528a5b65f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123936`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) UNION ALL SELECT total_changes() FILTER (WHERE CURRENT_DATE) OVER (ORDER BY CURRENT_DATE ROWS BE
```

---

## Crash 120: `f1c29ff4ae76a6c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125283`

```sql
SELECT substr('_', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO r VALUES (+NULL NOTNULL NOT IN (RAISE(IGNORE) ISNULL, FALSE)); EXPLAIN QUERY PLAN SELECT 
```

---

## Crash 121: `a8b04eab425f27a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126129`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t2 (b) AS (VALUES (TRUE)), q AS (SELECT *) VALUES (CURRENT_DATE); VALUES (NULL); SELECT printf('%.*
```

---

## Crash 122: `865fc20ba8fcecaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139868`

```sql
SELECT printf('%.*g', -2147483648); SELECT printf('%.*d', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO t2 VALUES (NOT RAISE(IGNORE)); PRAGMA integrity_c
```

---

## Crash 123: `ee714e012586592e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141881`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 124: `30d5a23e562ded95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 125: `92d246f86e4554e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142243`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 126: `98d08a866c068a88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142249`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 127: `c2d31e54c9bdfb38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142488`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 128: `03caf38550a2e993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144020`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 129: `3e9b7703f21da0b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144476`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY TRUE UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p 
```

---

## Crash 130: `191e464c14a91093` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145398`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIMESTAMP << CURRENT_DATE) UNION VALUES (-1.107041e+652016); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 131: `da0f78eff1214276` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145538`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (TRUE) UNION VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 132: `c466e41b8d28a11c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145547`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (TRUE) UNION VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 133: `72969a20b10b36bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145626`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 134: `22d82f71af66340a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147228`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN p; PRAGMA quick_check; CREATE VIRT
```

---

## Crash 135: `5705ffc4bb04ed59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147324`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT DISTINCT * FROM p; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 136: `710ddd0ed591d669` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148413`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO p SELECT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 137: `c2ed5810ab485ac9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148914`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM q NATURAL LEFT JOIN (SELECT * FROM q) AS aj_g; PRAGMA integrity_check; SELE
```

---

## Crash 138: `4c62e73770ac5430` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150984`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NU
```

---

## Crash 139: `e31fc347de43fcd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154313`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECED
```

---

## Crash 140: `3012c21c4558519e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154467`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT count(*) OVER (); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 141: `9a3ceee52b3479a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156391`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CAST(TRUE AS BLOB); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE P
```

---

## Crash 142: `74f0a5bcd0162da3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156540`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE 
```

---

## Crash 143: `065a7964be4788ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156549`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT FALSE; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); 
```

---

## Crash 144: `6300a6215be41af8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156613`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CAST(CAST(CURRENT_TIME AS BLOB) AS BLOB); PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 145: `c43d4c86c54f89d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT -FALSE; PRAGMA integrity
```

---

## Crash 146: `3a32810767f20e4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157113`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT TRUE || TRUE || TRUE || 
```

---

## Crash 147: `886f3515484f7a37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157163`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT TRUE || TRUE || TRUE || 
```

---

## Crash 148: `fe193ba4c626c231` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159451`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (_rowid_)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 149: `af52e8f4d5871f4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166159`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT GENERATED ALWAYS AS (TRUE) STORED, b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CU
```

---

## Crash 150: `18845a53aeb6d09c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166167`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME > CURRENT_DATE IS NOT TRUE); SELECT printf('%.*g', 2147483647, 0.01
```

---

## Crash 151: `29ad243a328e9246` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.
```

---

## Crash 152: `cb5ec51a31e59665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166189`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT X'8CdFAef16c9B'); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g',
```

---

## Crash 153: `8cad674e9e5e7436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166253`

```sql
SELECT substr('', 4294967296, 0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 154: `4e2977276e839041` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168137`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 155: `b2bb4b0324618ed2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168172`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 156: `252618a2b8c72a66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169989`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT unicode(count(DISTINCT CURRENT_TIME) FILTER (WHERE FALSE)) AS j_5446z_q68
```

---

## Crash 157: `ee2b04c1c89bca79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170419`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE TRUE IS NOT TRUE IS NOT TRUE IS NOT FALSE; 
```

---

## Crash 158: `15ad33915b5be711` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170488`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE TRUE IS NOT CURRENT_DATE; CREATE VIRTUAL TA
```

---

## Crash 159: `15cda836bdad7bf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170709`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT * FROM q GROUP BY NULL HAVING (SELE
```

---

## Crash 160: `78027dba31b0c5bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170895`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 161: `6da2ea5e24c5d215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170903`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT * FROM q GROUP BY NULL HAVING CURRE
```

---

## Crash 162: `a21a362064c93996` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170978`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT * FROM q GROUP BY CURRENT_TIME ORDE
```

---

## Crash 163: `0cd9fe694491bd25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171941`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE IS NULL; CREATE VIRTUAL TABLE 
```

---

## Crash 164: `b01f3157fc43c178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173005`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT (VALUES (CURRENT_DATE)) AS m____50_a__ce78__8_xu__v_d_0____b_5_9w2_3fp4_f
```

---

## Crash 165: `09a39a2d60541adc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175044`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE c2 = CURRENT_TIMESTAMP OR CURRENT_TIME; CRE
```

---

## Crash 166: `492a8459323f145a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175218`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE = CURRENT_TIMESTAMP OR CURRENT
```

---

## Crash 167: `99cf1b0bc1478e70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175274`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE NULL IN (c2) = CURRENT_TIMESTAMP OR CURRENT
```

---

## Crash 168: `b4de7d135d1fa47a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE NULL = CURRENT_TIMESTAMP OR CURRENT_TIME; S
```

---

## Crash 169: `9626d7aa5e76fe3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175432`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE NULL IN (NULL) = CURRENT_TIMESTAMP OR CURRE
```

---

## Crash 170: `c78a0c6918a7db09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175648`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE FALSE > FALSE OR CURRENT_TIME; CREATE VIRTU
```

---

## Crash 171: `4a163258e0520054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178171`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VI
```

---

## Crash 172: `8a4965d5bc6f4f8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178455`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_DATE IN (VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE)) A
```

---

## Crash 173: `3780e5ba322432c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178976`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME IS NOT CURRENT_TIMESTAMP OR CU
```

---

## Crash 174: `f512c621ff7d218f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184912`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_ch
```

---

## Crash 175: `8fb0ff53a6784831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185404`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA qui
```

---

## Crash 176: `9a86978ca2c7fe88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185412`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA qui
```

---

## Crash 177: `ea0f38814446fdbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187036`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR FAIL INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 178: `e75d407457da4571` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188039`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT); INSERT OR ROLLBACK INTO p VALUES (NOT CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 179: `e382734275d0951d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188353`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 180: `95deb07fcf294437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188884`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); SELECT * FROM (SELECT CURRENT_DATE AS i0y_737k0465jf_t_z05__sv5_9_k__g0_c_07___r__0afsxa_32_
```

---

## Crash 181: `4413dfb4d4c36257` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192804`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, c3 FLOAT NOT NULL); SELECT count(DISTINCT CURRENT_DATE IN (VALUES (CURRENT_TIME))) FROM p WHERE EXISTS (VALU
```

---

## Crash 182: `2ecc444575f64d29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194704`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL SELECT FALSE COLLATE BINARY AS x_rtu_592r_5_eh3539_qw_
```

---

## Crash 183: `4e45a79ec7905c05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194898`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL SELECT NULL AS x_rtu_592r_5_eh3539_qw__q__4b0zfn3r9_a_
```

---

## Crash 184: `26af0cf4a1aee4b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197942`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_DA
```

---

## Crash 185: `3ee9ce616776e8f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198635`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL length(CURRENT_TIMESTAMP) AS m1 FROM p NOT INDEXED; SELECT printf('
```

---

## Crash 186: `e53292fe87c8f5f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198860`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL count(*) AS m1 FROM p NOT INDEXED; SELECT printf('%.*f', -214748364
```

---

## Crash 187: `2733283291a6ca30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202114`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(*) OVER (ORDER BY CURRENT_DATE ROWS BETWEEN FALSE PRECEDING AND CURRENT ROW) ORDER BY CURRENT_TIME DESC NU
```

---

## Crash 188: `dde5d9ae6e980c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202270`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(*) OVER (ORDER BY CURRENT_DATE RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) ORDER BY CURRENT
```

---

## Crash 189: `fe5c7d407f0b96a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215350`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC DEFAULT 803237711441011892.029325, c2 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 190: `0bd1a2bf0f7a5bc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219755`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); EXPLAIN QUERY PLAN SELECT ALL * FROM p LEFT OUTER JOIN p NOT INDEXED USING (_rowid_) ORDER BY CURR
```

---

## Crash 191: `de119a6616a45423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224280`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT -743876159570616589200720931143773050558410451284256987780648992783945261010106016005263748511510007343812870227400.3E-034, c2 FLOAT); CREATE INDEX IF N
```

---

## Crash 192: `d8b2d34586479590` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224635`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC DEFAULT X'CAdCEEcFdDaA9b', c2 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 193: `42f800dac1527405` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234960`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(*) OVER () ORDER BY count(*) OVER () ASC, TRUE ASC NULLS FIRST LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 194: `f41656b471555ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235143`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE ORDER BY count(*) OVER () ASC, TRUE ASC NULLS FIRST LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 195: `f33ac0d247ae4de6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238598`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL json((SELECT * FROM p WHERE CURRENT_DATE GROUP BY TRUE)) AS m1 FROM
```

---

## Crash 196: `d0bab5ee5ad45464` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238779`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL changes() AS m1 FROM p NOT INDEXED; SELECT printf('%.*g', 214748364
```

---

## Crash 197: `6f0ff315baeb7a00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238862`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL length(random()) AS m1 FROM p NOT INDEXED; SELECT printf('%.*g', 21
```

---

## Crash 198: `d20da16a11fad73a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238983`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL total_changes() AS m1 FROM p NOT INDEXED; SELECT printf('%.*g', 214
```

---

## Crash 199: `c517ecc4e1bbfc66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240126`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL CASE WHEN count(*) THEN FALSE ELSE count(*) END AS m1 FROM p NOT IN
```

---

## Crash 200: `f20bb19b5f4aa2d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241176`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c3 NUME
```

---

## Crash 201: `88d109dd9a7d410e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241831`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) EXCEPT SELECT count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDE
```

---

## Crash 202: `29db9b9fd95bda94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248836`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA qui
```

---

## Crash 203: `163ca4f58f3758b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249287`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE, c2 GENERATED ALWAYS AS (a + 6002) UNIQUE, a FLOAT GENERATED ALWAYS AS (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE) STORED); INSERT INTO p D
```

---

## Crash 204: `7fafd29044d264c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249430`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT 30955717490107149231919771515658237420843966104199399759412783631106934683568183420055023708105685830848220837127809.957); INSERT INTO p D
```

---

## Crash 205: `54fa23d8e94b91da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255554`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NULL | CURRENT_TIMESTA
```

---

## Crash 206: `031d0c388b4a36ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257435`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VI
```

---

## Crash 207: `fc3aca772bce354e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257994`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT group_concat(CURRENT_TIMESTAMP) FILTER (WHERE FALSE) AS a, * FROM q NATUR
```

---

## Crash 208: `ced496e92a60f7f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258123`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT count(DISTINCT NULL) AS a, * FROM q NATURAL JOIN p WHERE CURRENT_TIME; CR
```

---

## Crash 209: `7d632659265c4123` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY, a INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE c2 = CURRENT_TIMESTAMP; 
```

---

## Crash 210: `8e0d8560ce62351f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260875`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT FALSE, a BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE c2 = CURREN
```

---

## Crash 211: `bcff82783dd69c2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260986`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE c2 = CURRENT_TIMESTAMP; CREATE VIRTUAL TAB
```

---

## Crash 212: `82e8497c692d11db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261198`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE IN (CURRENT_DATE, NULL); CREAT
```

---

## Crash 213: `2798d721c0bd7a8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB DEFAULT 0); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 214: `5461fcbff6722c04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262855`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) GENERATED ALWAYS AS (+CAST(RAISE(IGNORE) AS NUMERIC)) STORED, c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VAL
```

---

## Crash 215: `99bbf09266f01e2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263105`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE X''; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 216: `e1eedd8e6e12cd10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT 803237711441011892.029325); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIM
```

---

## Crash 217: `372f7b9c7a213f4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264272`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c2 F
```

---

## Crash 218: `c6564d33f4075edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264564`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT * FROM q GROUP BY CURRENT_TIMESTAMP
```

---

## Crash 219: `2ade3a59e69dbca2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265070`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE (SELECT count(*) OVER (PARTITION BY NULL) O
```

---

## Crash 220: `1eb59eb3502e5590` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265755`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE, _rowid_ INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE
```

---

## Crash 221: `691d94815ecf0457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267677`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (count(*), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 222: `fd9ece069d84ffff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269660`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT ' ll -d1_ -865 '); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g'
```

---

## Crash 223: `e7e49588f5d890de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269675`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INT); INSERT OR REPLACE INTO q VALUES (FALSE NOT IN (SELECT ALL X'' FROM q NOT INDEXED ORDER BY NULL ASC NULLS FIRS
```

---

## Crash 224: `80abc3d0d047bb93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269681`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; SELECT ALL min(CURRENT_TIME COLLATE BINARY) AS m1 FROM p NOT INDEXED; SELECT p
```

---

## Crash 225: `8032822e05be7211` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269689`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE, c2 GENERATED ALWAYS AS (a = 5) UNIQUE, a FLOAT GENERATED ALWAYS AS (TRUE) STORED); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); SELECT printf('%.*g', 2147483
```

---

## Crash 226: `d66607211f41e837` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277597`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (NULL IN (_rowid_))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 227: `7976ce3ded477a1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279955`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIME AS x48tle96cs_6z210s2_54x664a9_42___f_rtzt9m_hxp_pwlx9v__s_ LIMIT CURRENT_TIME OFFSET TRUE; IN
```

---

## Crash 228: `c6a69689d1e21e1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279979`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY count(*) OVER () ASC LIMIT TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 229: `666ab398fd5c96dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280009`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT TRUE || TRUE || TRUE || 
```

---

## Crash 230: `f374eca0eb98cc26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280017`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT FALSE NOTNULL || TRUE ||
```

---

## Crash 231: `ff4082048bdd8e81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000284838`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 232: `c0856c508e015f36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286182`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 233: `9209decbb21c6357` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286478`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY);
```

---

## Crash 234: `b97d82488866cb34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286622`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 235: `c150dd7b88febae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000287350`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM (VALUES (group_concat(CURRENT_TIMESTAMP, 't8XR__z') FILTER (WHERE CURRENT_D
```

---

## Crash 236: `b356a24d2ea06fb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000287491`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT * FROM (VALUES (TRUE)) AS u0; PRAGMA integrity_check; SELECT printf('%.*g', 214748
```

---

## Crash 237: `0b71ab436de0b179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000288164`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT -FALSE IN (VALUES (CURRENT_DATE)) AS u__1l4_gho FROM p NOT INDEXED; PRAGMA integri
```

---

## Crash 238: `7012ec17c13aad03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000291541`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN (SELECT * FROM p WHERE CURRENT_TIMESTAM
```

---

## Crash 239: `823ca2fe9b9ab4be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000292088`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO p SELECT DISTINCT * FROM q NATURAL LEFT JOIN (SELECT * FROM q) AS aj_g; PRAGMA quick_check;
```

---
