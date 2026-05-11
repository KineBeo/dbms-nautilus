# Crash Triage Report

**Total crashes:** 233  
**Unique crash sites:** 233  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 233 | 233 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `5ce7a4df878a0dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 VALUES (NULL, FALSE); EXPLAIN QUERY PLAN VALUES (FALSE IN (SELECT *), CURRENT_TIME OR TRUE <> b NOT NULL) ORDER BY TRUE DESC, C
```

---

## Crash 2: `07066330e5d46611` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000424`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT INTO q (c1, c1) VALUES (FALSE IS -CURRENT_TIME COLLATE RTRIM) ON CONFLICT(b) DO UPDATE SET c2 = changes() OVER () NOT LIKE FALSE LIK
```

---

## Crash 3: `1f74bd49e8a7d8d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001508`

```sql
SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (-TRUE <> CASE WHEN (CURRENT_TIME) THEN total_changes() ELSE CURRENT_DATE END != CAST
```

---

## Crash 4: `a853c06f86093b71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002299`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c2 INTEGER GENERATED ALWAYS AS (FALSE >= TRUE NOT IN (NULL)) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (NULL)
```

---

## Crash 5: `111c57cfc2b9ea55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002502`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; SELECT * FROM q WHERE EXISTS (SELECT NOT EXISTS (SELECT CURRENT_DATE COLLATE 
```

---

## Crash 6: `9fb37f1ff2d029bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002793`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (TRUE); SELECT hex(zeroblob(-1));
```

---

## Crash 7: `7870cf2f3509df70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002968`

```sql
SELECT printf('%s', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 SELECT -CURRENT_TIMESTAMP AS a, *, TRUE NOTNULL AS a, * UNION SELECT *, NULL FROM
```

---

## Crash 8: `8af7e15f21389917` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003748`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); WITH RECURSIVE q 
```

---

## Crash 9: `5cc9c11078530dbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003757`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); WI
```

---

## Crash 10: `ea04799b2004dbf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003985`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO q VALUES (NOT format('7mt _T-Ogk9_pw_G1w', NOT EXISTS (SELECT FALSE REGEXP CURRENT_TI
```

---

## Crash 11: `7c57af0b43b253e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004628`

```sql
SELECT round(-1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES ((FALSE IS NOT NULL) IS NOT NOT NULL LIKE NULL | CURRENT_TIME) ORDER BY +substr(CURRENT_TIMESTAMP, TRUE) OVER ()
```

---

## Crash 12: `224069fd74e14dc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004731`

```sql
SELECT substr('', -9223372036854775808, 2147483648); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (NOT EXISTS (SELECT ALL *
```

---

## Crash 13: `99600df5b524178e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005451`

```sql
SELECT printf('%.*d', 2147483647); SELECT printf('%x', 4294967295, 'Jz v2 _Sd --cO'); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO
```

---

## Crash 14: `4685b86276bbd7bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005978`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR A
```

---

## Crash 15: `a20679dee253aa11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005996`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INT
```

---

## Crash 16: `ebc76c09204d942c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007203`

```sql
SELECT round(1.0, 9223372036854775807); SELECT printf('%.*g', 4294967296, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT q.*, t2.* FROM r WHERE EXISTS (VALUES (abs(NOT min(+CU
```

---

## Crash 17: `8e5d98e6dbd44867` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007224`

```sql
SELECT round(1.0, 9223372036854775807); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT q.*, t2.* FROM r WHERE EXISTS (VALUES (abs(NOT min(+CURRENT_TIME % FA
```

---

## Crash 18: `349c2543df90f987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007307`

```sql
SELECT substr('  h  _cf_ y__a -', -9223372036854775808, 0); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT DISTINCT p.*, * FROM (WITH
```

---

## Crash 19: `dac640907ae4d5e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007948`

```sql
SELECT substr('', -2147483648, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO r VALUES (RAISE(IGNORE) GLOB NULL, FALSE NOT BETWEEN TRUE AND TRUE IS DISTINCT 
```

---

## Crash 20: `bf77bb83d1f5ef25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008026`

```sql
SELECT round(1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO s VALUES (CURRENT_TIME MATCH NULL NOT IN (SELECT ALL * FROM q INDEXED BY a ORDER BY NOT NULL 
```

---

## Crash 21: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008074`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 22: `ac3d3cb0ba86e4ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008711`

```sql
SELECT substr('  -__-  0-  --3', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT +typeof(char(RAISE(IGNORE)) OVER () GLOB NULL IS NOT NULL % FALSE NOT LIKE +CUR
```

---

## Crash 23: `7037c142d89d8891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008737`

```sql
SELECT printf('%d', -1, '-__8r'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS NOT MATERIALIZED (VALUES (CURRENT_DATE NOT NULL)) SELECT CURRENT_DATE, t1.* FROM r; SELE
```

---

## Crash 24: `cb7a16ba72ef1260` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008848`

```sql
SELECT printf('%.*g', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO r VALUES (count(DISTINCT (SELECT *) | CURRENT_TIMESTAMP IS NOT NULL = CASE ~CURRENT_D
```

---

## Crash 25: `f83313a25dffbb3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009459`

```sql
SELECT printf('%.*s', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_TIME COLLATE RTRIM < CURRENT_TIME IS NOT CURRENT_DATE IS NOT DISTINCT FROM a FROM s I
```

---

## Crash 26: `142bb056f32ac157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010020`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 27: `404ef4a0204512f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010077`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 28: `cd3a00a1383a208d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010090`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UN
```

---

## Crash 29: `feab3ce3ada6d528` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010099`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UN
```

---

## Crash 30: `4eaf1ea97e551399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010168`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UN
```

---

## Crash 31: `49bf3309a13339f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010222`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-
```

---

## Crash 32: `bbc39cf88f0bbe5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010246`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); CRE
```

---

## Crash 33: `64b7fa2f078d6a55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010510`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); IN
```

---

## Crash 34: `2908308bb5a8cb1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010560`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 35: `eb1c3fa34fa15825` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012388`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFA
```

---

## Crash 36: `2c917707eee9adf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012913`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 37: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017669`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 38: `437a164d76522394` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022400`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABOR
```

---

## Crash 39: `7ca44d03ee4963ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022644`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL, b BOOLEAN GENERATED ALWAYS AS (TRUE) STORED); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 40: `aceaf9681e890d69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022888`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR 
```

---

## Crash 41: `faee90302425e1a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022894`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL, c3 DATE UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 42: `05bbe2373179dae6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024412`

```sql
SELECT substr('', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT q.* FROM (SELECT CASE (FALSE LIKE RAISE(IGNORE) ESCAPE CURRENT_TIME -> -TRUE) WHEN FALSE MATCH NULL ->> C
```

---

## Crash 43: `490134da73ecefbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024874`

```sql
SELECT round(-1e308, -1); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 44: `c9f929c7aab8a583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025054`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 45: `15aa1856ca263aa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025194`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 46: `e45f31b617bb10f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026032`

```sql
SELECT printf('%.*f', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (~TRUE GLOB NOT TRUE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CRE
```

---

## Crash 47: `190d8b623dd1065e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034941`

```sql
SELECT printf('%.*e', -2147483648, 1e-308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 48: `c8bb57a22fc7bec8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037218`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (_rowid_) VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 49: `6c8f8fde16865aaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037610`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 50: `e692112f3fc368ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040883`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY, c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-922
```

---

## Crash 51: `308d34e968d669be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042631`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 52: `868a837bf570ef50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043579`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c2 INTEGER GENERATED ALWAYS AS (NULL >= NULL) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUA
```

---

## Crash 53: `d404a568e042567e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044377`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT INTO r DEFAULT VALUES; VALUES
```

---

## Crash 54: `f2a52940b72d954a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044587`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM q NOT INDEXED NATURAL JOIN t1 USING (_rowid_, rowid) ORDER BY FALSE ASC NULLS FIRST; SELECT * FROM p WHERE 
```

---

## Crash 55: `74897b23ab51d939` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048477`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO s (b) VALUES (FALSE * CURRENT_DAT
```

---

## Crash 56: `8859ad3800378261` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049670`

```sql
SELECT printf('%.*d', 4294967295, -1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 57: `4790c47a33acef37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051502`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_D
```

---

## Crash 58: `c5482c8da04d742b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053507`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c2 INTEGER GENERATED ALWAYS AS (TRUE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT TRUE AS d_413222k, CURRENT_TIMESTAMP FROM p WHER
```

---

## Crash 59: `ed20ba09d11deae8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053711`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c2 INTEGER GENERATED ALWAYS AS (TRUE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT *, CURRENT_TIMESTAMP FROM p WHERE EXISTS (VALUES
```

---

## Crash 60: `28a5e06e1264eea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053803`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 61: `53cd2dbaac4ff5bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054577`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); VALUES
```

---

## Crash 62: `25b40bfa596c7c9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054920`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p , p AS w8; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES
```

---

## Crash 63: `7a9f9e65c921b339` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056332`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY, c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INTEGER); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 64: `6d6741b86cbf5014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060894`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 65: `28b43db045f2cc53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061249`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 66: `70800bf6fa987ed7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068091`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED LEFT OUTER JOIN p USING (c1, a); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 67: `539a87981d076137` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068399`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 68: `8ad90c2840faaeec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071496`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (FALSE)) SELECT count(*) OVER (), * FROM q; CREATE VIRTUAL TABLE 
```

---

## Crash 69: `b2956a3e072eed42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071769`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (CURRENT_D
```

---

## Crash 70: `fb1a28ba2c996f07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077157`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); VALUES (CURRENT_DATE)
```

---

## Crash 71: `11685a2dfcb6310b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078139`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VAL
```

---

## Crash 72: `6a0b8f1f8949c83f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078231`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, -4.39458406231109 < FALSE)
```

---

## Crash 73: `e52f0e891b66ed87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078602`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 74: `c39580f85f4bacc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082545`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL, c1 INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 75: `d66dceb1b1aa85dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082631`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL, c2 INT); SELECT * FROM q NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT
```

---

## Crash 76: `c749e45eb31cef9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083442`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT DEFAULT ' l_L'); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 77: `1a6cb607b27211e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083581`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT DEFAULT FALSE); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 78: `f84064d8dceb55f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084060`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 79: `4f3cb37426499fda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084394`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT FALSE, c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 80: `4e0e50e3dd11801d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084720`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE TRUE ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALU
```

---

## Crash 81: `73c5322ceb4d3661` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084835`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT -8.430); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 82: `41cbf208e5af0d02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085249`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 83: `b45b1ca0b180c2b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085503`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME COLLATE BINARY > CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.
```

---

## Crash 84: `78e443168c00a732` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085550`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 85: `d7074a062fac4045` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085556`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME > CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 86: `de658d5a16a9837c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085571`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 87: `1b11903513be84b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085920`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT count(*) OVER (), * FROM q NATURAL JOIN p WHERE TRUE; CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) GENERATED A
```

---

## Crash 88: `6108a1d51335759c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086028`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT ''); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 89: `742c8abf23fed7fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086322`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE, rowid TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 90: `e48b5af49584d45d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086716`

```sql
SELECT printf('%.*f', 4294967296); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE UNIQUE); SELECT CURRENT_TIME NOT NULL BETWEEN CURRENT_TIMESTAMP AND C
```

---

## Crash 91: `179a1a71289c9855` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104240`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3,
```

---

## Crash 92: `c8d01fd4c79fee6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104263`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q VALUES (CURRENT_TIMESTAMP); SELECT max(CURRENT_TIMESTAMP) FROM p JOIN p j_jg21x_9m_4121_6_83_o
```

---

## Crash 93: `b10577159548a117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL
```

---

## Crash 94: `dcab77f9ba87036e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104773`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (NULL || CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 95: `b0f7c59e3d1f934a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107109`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); SELECT DISTINCT NOT EXISTS (VALUES (CURRENT_DATE)) FROM p NOT INDEXED UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -1, -1.0); CREAT
```

---

## Crash 96: `ca3f4131931cafec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107206`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); VALUES (FALSE) UNION VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 97: `1441b2abcf6ab181` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107649`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIME, NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 98: `7bd572042e744aaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108007`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); SELECT DISTINCT * FROM p NOT INDEXED EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 99: `8fc7d660c4a6957f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108167`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); VALUES (TRUE) INTERSECT VALUES (TRUE) UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 100: `40a03726ccd2fd2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108654`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); SELECT DISTINCT p.* FROM p NOT INDEXED UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 101: `da1cab26cd4f56b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109379`

```sql
SELECT printf('%.*e', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (--CURRENT_DATE < CURRENT_DATE = RAISE(IGNORE)); WITH RECURSIVE t2 (b, c2, _rowi
```

---

## Crash 102: `c5caea67d6abd5ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110178`

```sql
SELECT printf('%.*d', -2147483649); SELECT substr('_', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME AS c50__p2_0_bamgc_x940x2_45uc9lukh_m1i95_h_v8t__h588_
```

---

## Crash 103: `4c7bd0852ceb3428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110272`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p
```

---

## Crash 104: `3b92bc42f3036d78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111026`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIME ESCAPE NULL, FALSE); SELECT printf('%.*g', 21474
```

---

## Crash 105: `42bc95f6d1c13f67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112816`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_TIME LIKE CURRENT_TIME), _rowid_ TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check
```

---

## Crash 106: `75a3055cc6ba2d0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113131`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, _rowid_ TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 107: `b343ae88a21a5f72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114525`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT 068298923635268518439386282847714324934706747057025.22484294e+284713); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES
```

---

## Crash 108: `b3a5e49661203b4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT round(1e-308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 109: `f2ec3fa49a3d653a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114618`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (TRUE LIKE CURRENT_TIMESTAMP ESCAPE FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 110: `4e69bbec6d808ddb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116423`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT '-'); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 111: `99af6c2401c8aae2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116531`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 112: `45dfad610e06c9e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116542`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT X'e55b'); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 113: `6e573872e3e05bec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116715`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 114: `4a1a6af9fbe95433` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117262`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABL
```

---

## Crash 115: `48d28fdc5ba6620a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117319`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT 
```

---

## Crash 116: `e6b9b9c1c600b811` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117478`

```sql
SELECT printf('%.*s', 4294967296, 0.0); SELECT printf('%.*f', 2147483647, -1e308); SELECT hex(zeroblob(4294967295));
```

---

## Crash 117: `1a7e1d497c31c06e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121741`

```sql
SELECT printf('%.*s', 4294967296, 0.0); SELECT printf('%.*s', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p (b) AS (VALUES (CURRENT_TIMESTAMP != TRUE NOTNULL 
```

---

## Crash 118: `9745c2a76c6d0ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122220`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY)
```

---

## Crash 119: `89ca7d654f77426a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122471`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT X'cDe9'); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 120: `3dfdd6b4d34fc9e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123039`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, a BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, CURRENT_DATE); PRAGMA quick_check;
```

---

## Crash 121: `c99c9ff2106833cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124287`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p SELECT * FROM q NOT INDEXED; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 122: `78ce967003190c70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124626`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE; 
```

---

## Crash 123: `c7e0d9bcd3be28e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125831`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 124: `285cc99715c0f0bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126037`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT substr('  -IH4_9E3Twt__r25-', -2147483649); CREATE 
```

---

## Crash 125: `a04ce10e986eee2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126678`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_TIMESTAMP IS NOT CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP)), _rowid_ TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT IN
```

---

## Crash 126: `09949f177a26c149` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130648`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (typeof(CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 127: `4d9f7003c15486de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130760`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (total_changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT O
```

---

## Crash 128: `70cf72b15dbf1db4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130843`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (last_insert_rowid()); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 129: `2dcce8ba8cb8355f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131532`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_DATE INTERSECT SELECT TRUE AS d_413222k,
```

---

## Crash 130: `0e60d42f77956640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131960`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p ORDER BY CURRENT_TIME ASC LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 131: `c32635d55bd655f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132206`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIME ESCAPE FALSE, FALSE); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 132: `20af2c6f10b086b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132718`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 133: `1c57359d0ceb5266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133082`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALU
```

---

## Crash 134: `af9962a4d325b650` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133910`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) UNION ALL VALUES (FALSE IS TRUE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 135: `f5cf4b4188056b7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135086`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); SELECT DISTINCT * FROM p UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALU
```

---

## Crash 136: `a7dc0c8690dec6d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138641`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (randomblob(CURRENT_DATE)) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 137: `ef95c3c8f855546d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138682`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 138: `334ec945133fcb16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138689`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (count(*)) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 139: `0292c44ee40ffeed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138695`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (randomblob(FALSE)) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 140: `f4d8270fe091ca78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138915`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (randomblob(NULL)) UNION ALL VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 141: `08955053264b60bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139946`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (FALSE OR FALSE OR TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 142: `150e4afccb9ba974` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158848`

```sql
SELECT substr(' 4FK7P_md _0z', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1); INSERT OR ABORT INTO t3 VALUES (CURRENT_TIMESTAMP | CURRENT_TIME OR CASE FALSE / json(
```

---

## Crash 143: `1101a7de827e32b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160140`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1); 
```

---

## Crash 144: `67ead8167a49f03a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160913`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT '4 '); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a);
```

---

## Crash 145: `c95e997d247e6f50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161266`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE c3 COLLATE BINARY > CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 146: `d006a1320b6a0866` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163120`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP BETWEEN TRUE AND FALSE; SELECT printf('%.*g', 2147483647,
```

---

## Crash 147: `5ddec57c3a553dc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163673`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE TRUE IS NOT TRUE IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 148: `68011aebfe7f20bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163861`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL MATCH CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 149: `4ba45e76b98f5a2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165092`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE '-_ M_-_g6  Q_--'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 150: `8aaacbb366621333` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165471`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE <= p.rowid; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 151: `f8858432702fc571` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB GENERATED ALWAYS AS (NULL) VIRTUAL, a BLOB NOT NULL, c3 BOOLEAN); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 152: `55fef09800b950b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171484`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, CURRENT_DATE < CURRENT_DAT
```

---

## Crash 153: `fbcf1a499b9a602d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172415`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); SELECT * FROM q NATURAL 
```

---

## Crash 154: `17ec9ea15c3fd8a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173240`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b INT NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); SE
```

---

## Crash 155: `5f27a77dc2bc8a55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182503`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (FALSE)) SELECT count(*) OVER (), NOT EXISTS (VALUES (CURRENT_DAT
```

---

## Crash 156: `2178efc3e50bbbdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183105`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (CURRENT_DATE COLLATE RTRIM)) SELECT count(*) OVER (), * FROM q; 
```

---

## Crash 157: `8e373020450e48d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183252`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (FALSE)) SELECT *, count(*) OVER (), * FROM q; CREATE VIRTUAL TAB
```

---

## Crash 158: `c69d3f62695a4dd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184544`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (TRUE) UNION VALUES (TRUE)) SELECT * FROM q; CREATE VIRTUAL TABLE
```

---

## Crash 159: `f3eae80c15a5feb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184911`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DAT
```

---

## Crash 160: `8bae7a84b1dfebd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187859`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER (), * FROM p NOT INDEXED LEFT OUTER JOIN p USING (c1, a); CREATE VIRTUAL TABL
```

---

## Crash 161: `2dc1d467cfd47f53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188329`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p , (VALUES (CURRENT_DATE)) AS v_c_d_5b__ic_8_1_b7_4_z0_nh75_y___5__dc_z3ndariyvdn8_
```

---

## Crash 162: `41369c195c636ff7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196565`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 REAL, c3 G
```

---

## Crash 163: `0e547c7041b6531a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196586`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT GENE
```

---

## Crash 164: `07a26113e87e9364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197845`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (CURRENT_DATE << TRUE - CURRENT_DATE, FALSE); PRAGMA integrity_check; CREATE V
```

---

## Crash 165: `fa440f748a10b6f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197922`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (CURRENT_DATE << FALSE, FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 166: `a6c8065109deff6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197991`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (rowid, c3) VALUES (CURRENT_DATE << CURRENT_TIME, FALSE); PRAGMA integrity_check; SELECT print
```

---

## Crash 167: `8ef8ca92d9bca73d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198156`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (CURRENT_DATE << CURRENT_TIME, FALSE); PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 168: `bdc8d92e02bd1525` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198426`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c
```

---

## Crash 169: `bfd7486199b518f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203955`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY, c1 INT UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, -5); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 170: `e76cfd9f3277692d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204492`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p , p AS w8; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 171: `50f55854921382df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204791`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALU
```

---

## Crash 172: `71418f5fe713f48b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204853`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, a BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 173: `182bdd38440c8478` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205087`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LEFT OUTER JOIN p AS w8; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p 
```

---

## Crash 174: `667cebb92e3dfdbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205297`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p , p AS w8; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (CURRENT_DATE) UNION ALL S
```

---

## Crash 175: `a43b906b0275c6a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206569`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CU
```

---

## Crash 176: `59d7320156ca5484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207263`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 177: `17a1042804224a9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207391`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (a) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT I
```

---

## Crash 178: `fe0d5dfed7b5c49a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208933`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT NOT EXISTS (VALUES (FALSE) UNION VALUES (CURRENT_TIMESTAMP)) FROM p NOT INDEXE
```

---

## Crash 179: `e9362621112c35f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209600`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM (SELECT * FROM (VALUES (CURRENT_DATE)) AS u_gfq4 WHERE TRUE GROUP BY CU
```

---

## Crash 180: `f232e383b13d13dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210898`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_DATE) UNION ALL SELECT CURRENT_TIME ORDER BY CURRENT_DATE ASC NULLS LAST; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 181: `e0ed221c5c9b6684` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211389`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (CURRENT_DATE) INTERSECT SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST; 
```

---

## Crash 182: `6e43990b38ff8270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211693`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM q ORDER BY CURRENT_DATE ASC NULLS LAST; CREATE VIRTU
```

---

## Crash 183: `0797e05cfb81de99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214332`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (SELECT count(*) OVER ()) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VAL
```

---

## Crash 184: `641961c3dbfad64e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214990`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); VALUES (FALSE) UNION SELECT * FROM q NOT INDEXED NATURAL LEFT JOIN q NOT INDEXED; CREATE VIRTUAL T
```

---

## Crash 185: `ce2a3b6a85fbe74f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216334`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST; SELECT prin
```

---

## Crash 186: `bb1cfbf0834a579e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216440`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST; SELECT print
```

---

## Crash 187: `de8ab2e46829aeed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217100`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT substr('D4-j_VB', 4294967295, 2147483648); CREATE VIRTUAL TABLE 
```

---

## Crash 188: `19d93ed93fff5a40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217461`

```sql
SELECT round(1e308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (p.c2, TRUE, p.b, (CURRENT_TIME)); SELECT RAISE(IGNORE) LIKE RAISE(IGNORE) >> j
```

---

## Crash 189: `e2deccc8d247dc48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219361`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT sum(CURRENT_TIMESTAMP) 
```

---

## Crash 190: `2a51363c8be677f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219556`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT sum(FALSE IN (VALUES (c
```

---

## Crash 191: `02837a4016e873d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219739`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT changes() AS k FROM p; 
```

---

## Crash 192: `5eddfa02179cbe6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219746`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT sum(FALSE IN (VALUES (C
```

---

## Crash 193: `46d672f4a90dc82a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219903`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT min(FALSE), * FROM p; C
```

---

## Crash 194: `4556b7d86aeb426b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220105`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (RAISE(IGNORE))) SELECT count(*), * FROM p; CRE
```

---

## Crash 195: `cefe30ce16515ea6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); VALUES (CURRENT_DATE) UNION SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST; CREA
```

---

## Crash 196: `adb56b88a9e1e570` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224153`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_DATE <= p.rowid OR CURRENT_TIME GROUP BY CURRENT_DATE);
```

---

## Crash 197: `2fce3d172f7e682b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224333`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE TRUE OR CURRENT_TIME GROUP BY CURRENT_DATE); CREATE VIRTUAL TAB
```

---

## Crash 198: `59de19d2324fb328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224339`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_DATE <= CURRENT_TIME OR CURRENT_TIME GROUP BY CURRENT_D
```

---

## Crash 199: `8c5c08472938eeda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224746`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED LEFT JOIN (SELECT ALL * FROM p ORDER BY TRUE ASC NULLS FI
```

---

## Crash 200: `20da2acc37a551f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225709`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c2 INTEGER GENERATED ALWAYS AS (TRUE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT json_type(FALSE) AS d_413222k, * FROM p WHERE EX
```

---

## Crash 201: `5724d7277b80ba05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226492`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, _rowid_ GENERATED ALWAYS AS (a + -0) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 202: `69896f669913d25a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226654`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, _rowid_ GENERATED ALWAYS AS (a) NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 203: `289b2ac134b7dff3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234230`

```sql
SELECT substr('I_ i-SVh5', 2147483647, 2147483647); SELECT printf('%.*e', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN VA
```

---

## Crash 204: `51d993828d9ac76d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234328`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (TRUE - FALSE, FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 205: `f081829ec4a058b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234533`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (TRUE - TRUE - TRUE - TRUE, FALSE); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 206: `e63e2ee4bf72b1e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234729`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3, c3) VALUES (TRUE - TRUE - FALSE, FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 207: `377fe54b67848595` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236773`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p (c3) VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, _rowi
```

---

## Crash 208: `3629dfc5973d70f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238656`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME, FALSE) EXCEPT SELECT DISTINCT * FROM p JOIN q ON CURRENT_TIMESTAMP ORD
```

---

## Crash 209: `b6131bf4474d5b45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242912`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (p JOIN (VALUES (CURRENT_DATE)) AS u_gfq4 ON CURRENT_TIMESTAMP) , (VALUES (CURRENT_D
```

---

## Crash 210: `f549863006d3c1e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243032`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER (), NOT EXISTS (SELECT ALL * FROM p), * FROM p NOT INDEXED LEFT OUTER JOIN p 
```

---

## Crash 211: `96a0eb36bd705fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243193`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER (), CURRENT_TIMESTAMP, * FROM p NOT INDEXED LEFT OUTER JOIN p USING (c1, a); 
```

---

## Crash 212: `0cc824c382464be1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243606`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (p JOIN (VALUES (CURRENT_DATE)) AS u_gfq4 ON NULL ISNULL) LEFT OUTER JOIN p USING (c
```

---

## Crash 213: `ae4400a86d32a468` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244744`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER (ORDER BY CURRENT_DATE DESC NULLS LAST, NULL ASC NULLS LAST) FROM (SELECT ALL
```

---

## Crash 214: `e507b69db4bc741b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245025`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (min(CURRENT_DATE), FALSE)) AS u_gfq4 JOIN p NOT INDEXED ON TRUE; SELECT pri
```

---

## Crash 215: `f4d4c6d562918a03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246332`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE q (c3) AS (VALUES (TRUE) UNION SELECT DISTINCT * FROM q NOT INDEXED) SELECT * FROM 
```

---

## Crash 216: `f3babead07c0fe04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247390`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT count(*) OVER (), count(*) OVER (PARTITIO
```

---

## Crash 217: `3752b0f19af6b97e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247587`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT count(*) OVER (), count(*) OVER (), * FRO
```

---

## Crash 218: `e33e79805d2b4387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255470`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); VALUES (CURRENT_DATE)
```

---

## Crash 219: `1f1393edc62470a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257377`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); SELECT * FROM p 
```

---

## Crash 220: `8990b20b42ad3722` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257533`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_TIME GROUP BY C
```

---

## Crash 221: `66b5fda681be4e63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258179`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); SELECT * FROM q NATURAL 
```

---

## Crash 222: `7c8dc0b1ad8b64a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258717`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); SELECT DISTINCT
```

---

## Crash 223: `5dd2ab0724a4c07a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258849`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL, c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT q.* FROM q; SELECT printf('%
```

---

## Crash 224: `bab9453c785cef4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259665`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, c1 GENERATED ALWAYS AS (a) NOT NULL, a DATE NOT NULL DEFAULT CURRENT_TIME); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, 536448555760061032466.999772033802
```

---

## Crash 225: `ca6b058b46bafe89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, c1 GENERATED ALWAYS AS (a) NOT NULL, a DATE NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE I
```

---

## Crash 226: `85c706834802127c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260138`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 227: `de5df5883568d9a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265877`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE <= p.b; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 228: `1db7d7d40ebdd82d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266133`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE b <= TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 229: `93a43a112c0c63a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266241`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE b <= p.rowid; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 230: `759abd0760a22a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266429`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 231: `36c629ad8dbb64a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266435`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE TRUE <= p.rowid; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 232: `50d66712444b01d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266702`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE <= p.rowid <= CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE I
```

---

## Crash 233: `83af3675dafab956` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266874`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY, b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); SELECT count(*) OVER (), * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TA
```

---
