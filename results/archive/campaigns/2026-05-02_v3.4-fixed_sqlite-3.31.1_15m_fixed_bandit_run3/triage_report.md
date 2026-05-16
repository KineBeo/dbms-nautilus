# Crash Triage Report

**Total crashes:** 141  
**Unique crash sites:** 141  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 141 | 141 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `ac3e68c040d5a30e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000259`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO p VALUES (NOT NULL & count(*) IS NOT -CURRENT_DATE > CURRENT_DATE); SELECT RAISE(IGNORE) LIMIT CURRENT_TIME > CURRENT_DA
```

---

## Crash 2: `35c266c82cad3150` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000282`

```sql
SELECT substr('17U9', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT INTO p (c2, c3) VALUES (CASE TRUE ISNULL NOT IN (NULL) <> TRUE IS NOT DISTINCT FROM CURRENT_TIME
```

---

## Crash 3: `7fba8758af7f34b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000567`

```sql
SELECT printf('%.*d', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (FALSE NOTNULL IS NOT DISTINCT FROM RAISE(IGNORE) IS CURRENT_DATE, RAISE(IG
```

---

## Crash 4: `74259540c7dce985` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000844`

```sql
SELECT printf('%.*g', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN 
```

---

## Crash 5: `d4cf4780ea9b3a91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000920`

```sql
SELECT substr('M0', 0, -9223372036854775808); SELECT printf('%.*e', -2147483648, 0.0); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p VALUES (ifn
```

---

## Crash 6: `0fa8822f21ef9f05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001030`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (FALSE + CURRENT_DATE IS NOT CURRENT_DATE > FALSE & CURRENT_TIMESTAMP = CURRE
```

---

## Crash 7: `1bff81425c7b6fe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001111`

```sql
SELECT printf('%.*f', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c2); INSERT INTO p DEFAULT VALUES; SELECT NOT c1 IS NOT NULL IS NULL IS NOT NULL, CURRENT_TIME NOTN
```

---

## Crash 8: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001159`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 9: `edcd6c2488dd50b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001322`

```sql
SELECT printf('%.*g', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO s VALUES (nullif(CASE WHEN NULL THEN total_changes() ELSE RAISE(IGNORE) COLLATE NOCASE END <= N
```

---

## Crash 10: `56c6b47b11e9ae5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001357`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN r s4e_9beq ON TRUE COLLATE BINARY COLLATE RTRIM; CREATE 
```

---

## Crash 11: `0cc0afbc96f81e70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001391`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c1, c2, c3, _rowid_); INSERT INTO t2 VALUES (RAISE(IGNORE) = -RAISE(IGNORE) IS NOT NULL, ~CURRENT_TIME NOT IN (RAISE(IGNORE)) IN (TRUE, CUR
```

---

## Crash 12: `d8290ac0f0149b3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001470`

```sql
SELECT printf('%lld', -9223372036854775808, 'X_U 9--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1); WITH r AS MATERIALIZED (VALUES (CURRENT_TIME)), p AS MATERIALIZED (SELECT *) I
```

---

## Crash 13: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001513`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 14: `881beda1b64f6a0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001720`

```sql
SELECT printf('%.*g', 9223372036854775807, 1.0); SELECT printf('%.*g', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT OR FAIL INTO r VALUES (c2); EXPLAIN QUER
```

---

## Crash 15: `db1778941d6be964` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001876`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP < CURRENT_TIMESTAMP NOT NULL > TRUE); CREATE VIRTUAL T
```

---

## Crash 16: `462519631e4a14b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002071`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUE
```

---

## Crash 17: `3b070b7749b445db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002744`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 18: `8cb3e7df3eab2946` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002859`

```sql
SELECT round(-1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (CURRENT_TIME AND CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT NULL); CREATE 
```

---

## Crash 19: `4055f1f52d6bbda3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002872`

```sql
SELECT round(-1e308, -2147483648); CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); VALUES (CURRENT_TIME AND CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO p
```

---

## Crash 20: `ae976f586929ddfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003103`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 21: `7afc3196e6de0457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003142`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 22: `0615e3e47495fee0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003987`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * LIMI
```

---

## Crash 23: `47609dd1530e09d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004005`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * 
```

---

## Crash 24: `14e8700701e18cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004036`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); VALUES (~FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * 
```

---

## Crash 25: `b8c4f639350e4850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004529`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE DEFAULT -057037.140751560237903e+9773, c1 REAL PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); CREAT
```

---

## Crash 26: `bb021e1d8df59040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004547`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 27: `b3fbdcea33271423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004554`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE DEFAULT NULL, c1 REAL PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 28: `f4eba43db5635bfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005705`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_DATE ASC NULLS FIRST LIMIT NOT CURRENT_TIMESTAMP NOT IN (SELECT * INTERSECT SELECT * FROM r N
```

---

## Crash 29: `495219f0c270472f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006667`

```sql
SELECT substr('-1 SI- _3q4P _-  ', 2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p (c3, b, c2) VALUES (+CURRENT_TIME NOT IN (VALUES (TRUE IS NULL, TRUE LIKE FA
```

---

## Crash 30: `634fcc463177d2e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007066`

```sql
SELECT printf('%x', 1, 'S78_ '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); INSERT INTO t3 VALUES (RAISE(IGNORE) IS NOT DISTINCT FROM NOT EXISTS (SELECT p.* FROM (SELECT ALL * 
```

---

## Crash 31: `405cfd3559994a2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007588`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT FALSE -> CURRENT_TIMESTAMP AS a_ FROM p WHERE EXISTS (SELECT DISTINCT r.*, FALSE == CURREN
```

---

## Crash 32: `61e2355ca00a661f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010828`

```sql
SELECT substr('-_ 6 - E', -9223372036854775808); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR REPLACE INTO r VALUES (FALSE COLLATE BINARY 
```

---

## Crash 33: `af4d1184c2e49ca7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013550`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT CURRENT_DATE, c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 34: `f87ee3ea5a569aeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013835`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 35: `4106b6901bff5add` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016188`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM r NOT INDEXED INNER JOIN p NOT INDEXED ON TRUE; VALUES (typeof(CURRENT_TIMESTAMP)); CR
```

---

## Crash 36: `6ef31f1214b9c5a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016207`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p
```

---

## Crash 37: `281c8372c3d640cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017043`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 
```

---

## Crash 38: `3716ee384dbd59e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019456`

```sql
SELECT round(-0.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 DEFAULT VALUES; SELECT *; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE I
```

---

## Crash 39: `39355d98bbe977c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024516`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_TIME IN (RAISE(IGNORE)))); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT round(0.01, -9223
```

---

## Crash 40: `e7e2b397801dc58f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028743`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a)
```

---

## Crash 41: `396605b1bf39dc06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028751`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a)
```

---

## Crash 42: `1e84199e7ffa91b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028815`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, * FROM p NOT INDEXED ORDER BY CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 43: `5e002e7684c17e04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029197`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 44: `28662b5c710b3178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030112`

```sql
SELECT printf('%lli', -2147483648, ' _ -w__ 1FSt-P- 8'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (CURRENT_DATE LIKE CURRENT_TIMESTAMP, CURRENT_TIME NOTNULL, (CURR
```

---

## Crash 45: `8951e1993f138cb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030418`

```sql
SELECT substr('_ 0 _ _-X -G- 7d', -1, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO t2 VALUES (NULL COLLATE NOCASE); SELECT ALL p.* FROM t1 CROSS JOIN q 
```

---

## Crash 46: `26ec8919dac5ff95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033830`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE 
```

---

## Crash 47: `174b3dbc1c66794e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033968`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT 
```

---

## Crash 48: `3d073edc0958bc27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034702`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN VALUES (NULL) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 49: `a148f917849927a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035395`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT -3454.61045710483392634180791666); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 50: `42ce332fbb168d95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER DEFAULT '--7ROX_9'); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 51: `056eea2d35718228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036314`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIME)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 52: `7ff69400a008e8c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 53: `093536108e44f601` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039570`

```sql
SELECT round(1.0, 2147483647); SELECT printf('%.*e', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (_rowid_, _rowid_, b, c3) VALUES (total_changes() | lower(
```

---

## Crash 54: `3ed32a83ca3411fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP < CURRENT_TIMESTAMP); SELECT printf('%.*f', -214748364
```

---

## Crash 55: `f95c57c27a0f979c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043407`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (TRUE) EXCEPT VALUES (NULL > TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 56: `d0800d3fbfc2717a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044777`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); VALUES (TRUE) EXCEPT VALUES (TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 57: `254cfd44ceca1786` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046057`

```sql
SELECT round(1e308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t1 DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (CURRENT_TIME)) SELECT * FROM p; SELECT hex(zeroblo
```

---

## Crash 58: `9070e23d68b67d4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051980`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL DEFAULT -0); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 59: `8f953473837b8136` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054783`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT r.* FROM q WHERE EXISTS (VALUES (+(WITH RECURSIVE p (c1) AS (SELECT CURRENT_DATE IS NULL) SELECT FALSE F
```

---

## Crash 60: `2bbe2f818fb172bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058998`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO t1 VALUES (TRUE COLLATE RTRIM IS NOT CURRENT_DATE + FALSE -> CURRENT_TIMESTAMP NOTNUL
```

---

## Crash 61: `3660e513f38c90e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060079`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT E
```

---

## Crash 62: `3cd71da11a42e9ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060131`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) GENERATED ALWAYS AS
```

---

## Crash 63: `a49e7e53791ee8cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060149`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); CREATE INDEX IF NOT 
```

---

## Crash 64: `a356f831f2888f9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060185`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT X'E73AA9c9FD'); CREATE
```

---

## Crash 65: `a249e91f11f4aadb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060199`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(b FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB, c2 GENERATED ALWAYS AS (a IS NUL
```

---

## Crash 66: `53f717ff3559e058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060588`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL, b TEXT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 67: `63e047f11bf7b277` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060737`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (-changes() OVER (PARTITI
```

---

## Crash 68: `66253380d04994a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061023`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); SELECT DISTINCT * FROM p AS nh_eb3_3hp_72g_u9_1_0l_45_l630p5_45_f6_u713cfn66q1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEF
```

---

## Crash 69: `d403aef790bef4c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061038`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 70: `1443227cef55f3d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061773`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE DESC NULLS FIRST, N
```

---

## Crash 71: `644ce855158929c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061963`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST); SE
```

---

## Crash 72: `028f657c2f73cd00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062940`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (SELECT ALL count(*) AS a FROM p); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 73: `3b094005d55b8f1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062982`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (SELECT ALL CURRENT_TIMESTAMP AS a FROM p); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 74: `63bae8b42173ee12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063725`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM q WHERE EXISTS (VALUES (FALSE, count(*))); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 75: `44e9e2e23bf940e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064071`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 76: `a23cad340fced05f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065505`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE DEFAULT -057037.140751560237903e+9773, c1 REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 77: `bff1f7269cde3319` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065756`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT 291.6e-3197); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 78: `c21b53d92012b382` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066400`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT -3454.61045710483392634180791666); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NO
```

---

## Crash 79: `14e8a6ed51b92347` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066423`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT);
```

---

## Crash 80: `3c306db5f091bfa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066526`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 81: `d0b1db48ddc5bff0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067545`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CRE
```

---

## Crash 82: `6c9556a204de003c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068103`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (count(*) OVER (PARTITION BY TRUE ORDER BY FALSE DESC NULLS FIRST GROUPS BETWEEN UNBOUNDED PRECEDING AND UN
```

---

## Crash 83: `9c15be2a0b38d54d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068123`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (count(*) OVER (), TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *; SELECT hex(ze
```

---

## Crash 84: `215c593368703fcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069347`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(b INT); INSERT OR FAIL INTO p VALUES (87734184925472915875651411107520051418076502757950824720509874020012205628409250281101845.7
```

---

## Crash 85: `bca89b59c0d21f36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a INT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); CREATE VIRTU
```

---

## Crash 86: `18fa809781bdf999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069589`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a INT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE
```

---

## Crash 87: `94f7ed7353461d95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071387`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 88: `9a338f020eb97875` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074153`

```sql
SELECT substr('', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (json_type(-99 IN (SELECT ALL * FROM p ORDER BY +CURRENT_DATE COLLATE BINARY DESC NULLS 
```

---

## Crash 89: `3361e33c9f3e30c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074626`

```sql
SELECT printf('%.*d', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT OR FAIL INTO s VALUES (-FALSE COLLATE NOCASE << (NULL) / NULL IS NOT EXISTS (SELECT RAISE
```

---

## Crash 90: `3a048fc100b340ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074708`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a) NOT NULL); INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 91: `d0f4979bbc2ae935` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075308`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 92: `4ac8bc3b604657ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075421`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (~FALSE - CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 93: `730a5dbec1ba5704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075587`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (~CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT I
```

---

## Crash 94: `c575ff14bd1f2c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077724`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_DATE; CREATE VIRTUAL TABL
```

---

## Crash 95: `0cf766c2ae093943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084758`

```sql
SELECT printf('%.*s', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT OR FAIL INTO t2 VALUES (FALSE NOT IN (VALUES ((CURRENT_TIMESTAMP))) NOT IN (CAST
```

---

## Crash 96: `b6a915cc437a745b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086984`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE DEFAULT TRUE, c1 REAL PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 97: `be242f404fc4e196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089071`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE CURRENT_TIME LIKE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); SELECT q.*,
```

---

## Crash 98: `9787ee167730d0e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089516`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE NULL LIKE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q AS (VAL
```

---

## Crash 99: `0aef0835d4a37208` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089748`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE CURRENT_DATE LIKE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q
```

---

## Crash 100: `36d3db35c5b742cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090158`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE FALSE OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); VALUES (+FALSE, CU
```

---

## Crash 101: `ad61ed3092a72cc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091374`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (NULL NOT BETWEEN CURRENT_TIME AND TRUE) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO
```

---

## Crash 102: `ef0c4dba901c6fd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091429`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s VALUES (+FALSE NOT BETW
```

---

## Crash 103: `25cab397be214e5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091435`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s VALUES (+FALSE NOT BETWEEN CURR
```

---

## Crash 104: `aff4ecfb33176b3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091481`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (CURRENT_DATE << FALSE) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 105: `e967238d0aaf13f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091888`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (CURRENT_DATE << CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 106: `eac552646c2114c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093074`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND NULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 107: `3562be60eab9b9ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093305`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND NULL NOT NULL; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 108: `73c6c7407518b8e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093464`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE AND CURRENT_DATE == CURRENT_TIMESTAMP; CREATE VIRTUA
```

---

## Crash 109: `5960954b4602cbb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093570`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check
```

---

## Crash 110: `2c801b2be31ecf1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094173`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); VALUES (TRUE) INTERSECT SELECT DISTINCT CASE CURRENT_TIMESTAMP WHEN TRUE AND TRUE THEN NULL ELSE NULL END FROM p WHERE CURRENT_DATE; CREATE VIRTUAL TA
```

---

## Crash 111: `9a4f54c3bf092fc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102561`

```sql
SELECT printf('%f', -9223372036854775808, '_2y'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM p JOIN t2 a ON CURRENT_DATE == CURRENT_TIMESTAMP OR CURRENT_DATE ISNULL NOT IN
```

---

## Crash 112: `edaaa7e410383217` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102952`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 113: `7a782c64aa7f9b30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107509`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 114: `4253928f45de3304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108525`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE < CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF N
```

---

## Crash 115: `df5c67b003f01f59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108751`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT 0); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 116: `1cd8322be9e7b421` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109389`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL DEFAULT FALSE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_
```

---

## Crash 117: `17919586483e06e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109590`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1)
```

---

## Crash 118: `dbea2e920865e1d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110325`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO q VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f',
```

---

## Crash 119: `f7e3ead93347b1ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111532`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT ''); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 120: `7d5e300b935b9784` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115612`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (NOT EXISTS (VALUES (NULL)), CURRENT_TIME) EXCEPT SELECT CURRENT_DATE AS a, CURRENT_TIME AS p8lvw1_q___; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 121: `72438bc95ecc6ffc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115854`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (TRUE * CURRENT_TIMESTAMP) EXCEPT VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 122: `aa164752d53c9ab5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116508`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CASE TRUE WHEN CURRENT_TIMESTAMP THEN FALSE END) EXCEPT VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 123: `e551e239f1f47539` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119061`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_TIMESTAMP OR ~CURRENT_TIME) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 124: `2f690a5b2eba06fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119438`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME | TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 125: `af85311ad03c8459` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119567`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (total_changes()) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 126: `7ebb6bb5d22c5ca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119788`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (avg(NULL)) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_chec
```

---

## Crash 127: `1d2900626d67f0bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120236`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (CURRENT_DATE) UNION VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (json_extra
```

---

## Crash 128: `ffe8ab9aec7e5001` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121460`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (-FALSE) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 129: `8a47fd662c05698b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126866`

```sql
SELECT round(1e-308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p (c1, _rowid_, b) AS (SELECT NOT FALSE >> CURRENT_TIME IS NULL COLLATE BINARY || ~NULL -> CURRENT_TIM
```

---

## Crash 130: `edbf06f5c9a06ed6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129146`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_TIMESTAMP % FALSE) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 131: `4e540dc58b39b51f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130025`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (CURRENT_DATE) EXCEPT SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE DESC NULLS FIRST, CURRENT_DATE DESC NULLS FIRST; CREATE VIRTUAL T
```

---

## Crash 132: `1cb60374ee05a413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131134`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (X'7A8b9D') EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 133: `a8692c0957775995` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); VALUES (NULL) EXCEPT SELECT CURRENT_DATE LIKE CURRENT_DATE ESCAPE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, c2, c2); INSERT INTO
```

---

## Crash 134: `e9d4d71915a6461a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (c1), c1 DATE GENERATED ALWAYS AS (TRUE) VIRTUAL); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELEC
```

---

## Crash 135: `cf69832937e2b2ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137307`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT INTO p DEFAULT VALUES; SELECT FALSE GLOB TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT I
```

---

## Crash 136: `b06fc674293fd95e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137416`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 137: `c84d551ba882862e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139307`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 138: `679b1dc23f652118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139666`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE > TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 139: `9552e88baeff55df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139817`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 140: `f1a9998a0f23db5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140774`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 141: `0a7a85cb457ae4cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144047`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(DISTINCT NULL)); SELECT printf('%.*f', -2147483649, -1e308);
```

---
