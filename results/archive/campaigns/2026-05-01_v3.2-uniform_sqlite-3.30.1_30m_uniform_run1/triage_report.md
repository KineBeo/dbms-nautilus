# Crash Triage Report

**Total crashes:** 251  
**Unique crash sites:** 251  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 251 | 251 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `72b8a5833dcac6a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000068`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(b INT, b GENERATED ALWAYS AS (a) UNIQUE, c2 INT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE != CURRENT_TIMESTAMP LIKE R
```

---

## Crash 2: `c225c0f3fb74373a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000244`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO t1 VALUES (~NULL); SELECT * FROM q JOIN p gj03egc11z_9_89_ ON CURRENT_DATE; CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL REGE
```

---

## Crash 3: `deb789429b8f18c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000280`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CASE TRUE ISNULL WHEN RAISE(IGNORE) THEN CURRENT_TIME ELSE CURRENT_TIME END | CURRENT_TIME NOT NULL IS NOT DISTINCT FROM CURRENT_TIMESTA
```

---

## Crash 4: `c0242ceecb57064f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000472`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE ->> RAISE(IGNORE) & NULL COLLATE BINARY IS DISTINCT FROM CURRENT_TIME IS NULL NOT LIKE CU
```

---

## Crash 5: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000699`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 6: `0d801ae5a91860f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000747`

```sql
SELECT substr('3XHpR-J', 4294967296, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO r DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -0); INSERT
```

---

## Crash 7: `a9b1ed2c1818a2c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001024`

```sql
SELECT substr('', -9223372036854775808, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t2.* FROM q NATURAL JOIN p WHERE CURRENT_DATE -> CASE CURRENT_DATE % RAISE(IGNORE
```

---

## Crash 8: `e58ae319b0f24b0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001104`

```sql
SELECT substr('6G _3-m_uh80 ', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q SELECT ALL * FROM t3 UNION SELECT t1.* FROM t2 WHERE NULL NOTNULL ORDER BY CASE WHEN
```

---

## Crash 9: `dc89c2bd83d4aa52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001120`

```sql
SELECT printf('%.*e', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); SELECT FALSE IS NOT CURRENT_DATE < CURRENT_TIMESTAMP = CURRENT_TIMESTAMP, *, * FROM t3 INDEXED BY c3 O
```

---

## Crash 10: `fe7b818dbba0d541` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002637`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VALUES (-CURRENT_TIME); PRAGMA integrity_check;
```

---

## Crash 11: `71916b58af2da26d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s SELECT FALSE AS q437s, FALSE FROM (
```

---

## Crash 12: `058634e3efe7ff3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003507`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO t2 VALUES (FALSE NOT NULL != FALSE); SELECT p.* FROM p NATURAL JOIN r WHERE total_changes() I
```

---

## Crash 13: `0e73cfe60905ddd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004998`

```sql
SELECT printf('%.*f', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY RAISE(IGNORE) HAVING RA
```

---

## Crash 14: `b872f9b25931a627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005452`

```sql
SELECT printf('%u', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t3.*, *, CURRENT_TIMESTAMP AS b9__r8_9 FROM q NATURAL JOIN p WHERE unicode(NULL / NULL IS
```

---

## Crash 15: `41e52d9d85b1ee7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005746`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 16: `dd28ea3643ef333e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005941`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIMESTAMP || TRUE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 17: `2bd43e3ac00b87ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006000`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIMESTAMP || TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 18: `3242cb06082890ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006006`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 19: `ecef197ecd14c52c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006012`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT O
```

---

## Crash 20: `8ae69c4be7371b65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006027`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); I
```

---

## Crash 21: `91326a45c47ca043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 22: `8887099bf105604b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006089`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR IGNORE INTO p VALUES (CASE last_insert_rowid() FILTER (WHERE +RAISE(IGNORE) << FALSE << TRUE) OVER (P
```

---

## Crash 23: `da1f1c69a22e5091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006920`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO p VALUES (+r.c1 ->> NULL > json_extract(NULL, '_a D') FILTER (WHERE group_concat(RAI
```

---

## Crash 24: `ca89c6b98740d488` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007769`

```sql
SELECT printf('%.*g', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t2 VALUES (CURRENT_DATE COLLATE NOCASE) ON CONFLICT DO NOTHING; EXPLAIN Q
```

---

## Crash 25: `cf7afd5166038a2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011922`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE VIRTUAL T
```

---

## Crash 26: `442c660dea7b1d0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012042`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT
```

---

## Crash 27: `f47e0cc7396a16af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012174`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE / NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 28: `12e02bf247c89187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013600`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 29: `0e2f34ffe31b5730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013651`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME); PRAGM
```

---

## Crash 30: `b76c4867b974a73f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013789`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME); PRAGM
```

---

## Crash 31: `af407ff64b851dd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013907`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 32: `f47da5635c810a79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014428`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME); PRAGMA integrity_c
```

---

## Crash 33: `cddc396f407e4ded` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014630`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE NOT BETWEEN CURRENT_TIME AND CURRENT_TIME); PRAGMA integrity_check
```

---

## Crash 34: `3b9c7e74070dda9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015645`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 35: `23436bf935b30966` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017273`

```sql
SELECT substr('k_U1OM', 9223372036854775807, 2147483648); SELECT substr('-3k__Hxu-', 9223372036854775807); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 36: `1e2ecf4d1c884f20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017516`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); INSERT INTO t1 DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 37: `8861b3ac54a0b7e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018801`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q DEF
```

---

## Crash 38: `2fd8deebd84977d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019418`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSER
```

---

## Crash 39: `75d44a408f0f3b57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019986`

```sql
SELECT printf('%x', -1, 'C__-S4we6_5__n_FV_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 40: `0a16ac745b78df53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022762`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, _rowid_); INSERT INTO t1 DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 41: `6e0aa9faff367eb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022768`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 
```

---

## Crash 42: `7c530f1beafedd48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022846`

```sql
SELECT printf('%.*f', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c3, b); WITH RECURSIVE r AS (SELECT ALL CURRENT_TIME IS NOT RAISE(IGNORE) || CURRENT_TIM
```

---

## Crash 43: `2f82293a24ef33d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023190`

```sql
SELECT printf('%.*f', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT INTO p VALUES (upper(TRUE >= RAISE(IGNORE) == NULL) FILTER (WHERE CURRENT_TIMESTAMP | TRUE = RAISE(
```

---

## Crash 44: `e02e4c3630ceb223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023252`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIMESTAMP), c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 45: `16ef9bc074c133d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023845`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); SELECT * FROM p JOIN q vd_n_ ON TRUE NOTNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 46: `25bec47950c4dfc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023938`

```sql
SELECT printf('%.*f', -2147483648, -1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 47: `ee54bd46f8dd60d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032281`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 48: `de826e3fc28825ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032469`

```sql
SELECT printf('%f', 9223372036854775807, 'i_ --Cd39_b-'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 49: `aaa10ba2d814fdc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032585`

```sql
SELECT printf('%.*s', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 50: `ce567d174d52f28d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032609`

```sql
SELECT printf('%.*s', 9223372036854775807, 0.01); SELECT printf('%lli', -9223372036854775808, '61-PL__fRk8Z12'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VALUES (CASE W
```

---

## Crash 51: `11fdf83654287fed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035395`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT IN
```

---

## Crash 52: `f5141d8057c10cbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041585`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (TRUE) INTERSECT SELECT CURRENT_TIME NOT NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 53: `b603f89f7a162019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041913`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT NULL NOT NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 54: `de9b60ed6794e274` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042140`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (NULL) INTERSECT SELECT NULL; SELECT round(1e-308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 VALUE
```

---

## Crash 55: `8bd13a05fde25b51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042470`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (FALSE / CURRENT_TIME) INTERSECT SELECT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q DEFAULT VALUES; PRAGMA
```

---

## Crash 56: `d35c1914a458abe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042799`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (FALSE) INTERSECT SELECT CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 57: `8ba87c6ee797cd4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043264`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (FALSE / CURRENT_TIME) INTERSECT SELECT CURRENT_TIMESTAMP NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE 
```

---

## Crash 58: `dbb01b1c5d8c352d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045850`

```sql
SELECT round(1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT quote(CURRENT_DATE ISNULL IS DISTINCT FROM FALSE COLLATE BINARY < FALSE < CURRENT_TIMESTAMP IS NOT DISTI
```

---

## Crash 59: `2f390c82a928578a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046308`

```sql
SELECT round(-1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 60: `4159edb3435fca7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046841`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE, rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE 
```

---

## Crash 61: `50bb107a2b9ab0e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046936`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE, rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 62: `ecc3687c500656c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047025`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREA
```

---

## Crash 63: `2ffb85fd10175a1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047150`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE, rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE I
```

---

## Crash 64: `22802ec3a485054e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047492`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, c1 INTEGER); INSERT OR FAIL INTO q VALUES (CURRENT_TIMESTAMP OR CURRENT_TIME, NULL); VALUES (CURRENT_
```

---

## Crash 65: `4e803f22f5b95857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047678`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, c1 INTEGER); INSERT OR FAIL INTO q VALUES (CURRENT_TIME, NULL); VALUES (CURRENT_TIMESTAMP); CREATE TA
```

---

## Crash 66: `842f7bb3dd00a296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048415`

```sql
SELECT printf('%.*s', -9223372036854775808); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 67: `204688396b37304c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(*) IS NULL AS a INTERSECT SELECT CURRENT_TIMESTAMP; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 68: `a4800729eff788a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056767`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (FALSE / FALSE) INTERSECT SELECT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO q VALUES (CURRENT_TIMESTAM
```

---

## Crash 69: `ce31c2ceee7d5176` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057390`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (NULL) INTERSECT SELECT * FROM p NOT INDEXED WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, b); SELECT CASE ~-NULL IS
```

---

## Crash 70: `6be4047ab7aa3558` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057521`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT CURRENT_TIMESTAMP; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 71: `8c098f2618f4b753` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058126`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 72: `ae5b0d9629dab918` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065768`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT p.*, * FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 73: `62de3ed7b14b039e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072306`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); REPLACE INTO q VALUES ((SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIME)); EXPLAIN QUERY PLA
```

---

## Crash 74: `da70fde714bc8b8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073835`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, CAST(CURRENT_TIMESTAMP AS REAL))
```

---

## Crash 75: `b9e4be3b4ea84e12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073968`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, CAST(CURRENT_TIMESTAMP AS REAL) 
```

---

## Crash 76: `8a22f93b3fd347bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 77: `1c07dde75492b55d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074162`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, CURRENT_TIMESTAMP IN (NULL, CURR
```

---

## Crash 78: `79bbc9453e1c1f95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074168`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, CAST(CURRENT_TIMESTAMP AS REAL) 
```

---

## Crash 79: `8c7151cf5ed7d157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074918`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP) UNION VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 80: `aff78b51c08ee0ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075449`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, FALSE IN ((VALUES (NULL)))); SEL
```

---

## Crash 81: `821a88938a739413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076427`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, FALSE IN (FALSE IN (FALSE IN (FA
```

---

## Crash 82: `407f4d7cc013c6ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080052`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 83: `ce7964c2f6390717` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080957`

```sql
SELECT printf('%.*f', -2147483648, -1e308); SELECT printf('%.*e', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT (SELECT *, * LIMIT RAISE(IGNORE)) AS rp_pb0
```

---

## Crash 84: `db92db6d1d4298fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081449`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); SELECT * FROM p JOIN q vd_n_ ON FALSE IN (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 85: `d8fd18655f83412c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081775`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 86: `1da8016b165357f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081936`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE, c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p (rowid) VALUES (TRUE) ON CONFLICT(rowid) DO UPDATE SET b = CURRENT_TIM
```

---

## Crash 87: `ed412725d320aa77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082496`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LEFT OUTER JOIN p ON CURRENT_TIMESTAMP
```

---

## Crash 88: `495f92f34134110e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083072`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (VALUES (NULL)) AS c_6____ LEFT OUTER JOIN p NOT IND
```

---

## Crash 89: `ecbce51f0dea52ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083656`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM q WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w
```

---

## Crash 90: `8fb1dc7b8ee22bf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083748`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST LIMIT TRUE); CREATE V
```

---

## Crash 91: `bdfac27397d2fd2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085126`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p.c1))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 92: `3e854825def48516` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087305`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT CHECK (CURRENT_TIMESTAMP), c2 FLOAT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 93: `0f213d7c6def0e5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087565`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 94: `fc0e2996c15f7b33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087914`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 95: `57c6022dee596321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089034`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT 0); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS 
```

---

## Crash 96: `57e69256f79adb0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089518`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * FROM (SELEC
```

---

## Crash 97: `003553b0c8ce4af5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089704`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (CAST(CURRENT_TIMESTAMP AS REAL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, c3, 
```

---

## Crash 98: `2ea477700719f6d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089915`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); VALUES (count(*), NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO q V
```

---

## Crash 99: `dde619f6b0f118b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090469`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT -0); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 100: `3f26c5a13aeab7b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090485`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIMESTAMP, TRUE; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUA
```

---

## Crash 101: `cb873046c2175a4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090494`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q DEFAULT VALUES; PRA
```

---

## Crash 102: `a4bee39f7eea1b7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090624`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT
```

---

## Crash 103: `16e96a63e253f568` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091237`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p V
```

---

## Crash 104: `ca5bfec140c4b935` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093551`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP IS NOT FALSE AS n_t FROM p NOT INDEXED WHERE FALSE LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 105: `afd070d4c6ec164c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093971`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 106: `cd47c5efd0bde447` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093990`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 107: `bf723c5ea1eb1b01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094059`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 108: `64d2ecaebe46dce8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095565`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIME == CURRENT_TIMESTAMP || TRUE; SELECT printf('%.*f', 21474836
```

---

## Crash 109: `a13a35606f6ee914` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095732`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE || TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 110: `87af99875a6e45d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095872`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON TRUE IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid
```

---

## Crash 111: `54bd244f70ccfded` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095995`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON TRUE IS CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 112: `442425f80aa823dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096258`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE NOT LIKE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 113: `2750a0166be25b01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096315`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIME BETWEEN TRUE AND CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF 
```

---

## Crash 114: `00482c2e26edcd14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097083`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR 
```

---

## Crash 115: `bb4b3f0ccbd8fd43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097204`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON TRUE MATCH CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 116: `407a643ac83cec12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097421`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM p JOIN p f90np ON FALSE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 117: `338e85d93634cca0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097595`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT -8.1940974333519E-94); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 118: `ccf39794204cc857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097709`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 119: `78825b385a616fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098185`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 120: `d47e26ebd3423268` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098996`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT X'9BE9'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 121: `040f1685b6a8dab4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099510`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA integrity_chec
```

---

## Crash 122: `f4f2967088a566b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099717`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME % CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 123: `ecdf5b4c0c3bd904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100009`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE LIKE CURRENT_DATE ESCAPE total_changes()); PRAGMA integrity_check;
```

---

## Crash 124: `ca8a447872d9823d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101211`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (''); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 125: `88021dc5392625eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101706`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 126: `1f0803919d001668` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101912`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 127: `8ef444e127ac9ec5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102633`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-~CURRENT_TIME * TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 128: `958730be86e5f9fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103202`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 129: `593c5379a318c223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103427`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME COLLATE
```

---

## Crash 130: `fa0a706b78967657` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103596`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME << FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 131: `e8c120fc51c90572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103804`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE > CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 132: `95ebc639177cb611` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104673`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME IS FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXIS
```

---

## Crash 133: `eb917c7288257cbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104858`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 134: `a146e497f88e4fd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105374`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE >> FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 135: `d40585edb7db323f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105606`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE >> TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 136: `19ea8e32c91d7fc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105955`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-4.655E87097768874255719963366); PRAGMA quick_check; CREATE VIRTUAL TABL
```

---

## Crash 137: `df4c0c7a805a957c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107660`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE T
```

---

## Crash 138: `0becc6198ee6b820` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107678`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); 
```

---

## Crash 139: `558102e5dcd6ca0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107756`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c1 REAL D
```

---

## Crash 140: `7ca87e26cb067e9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112847`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO q VALUES (CURRENT_TIMESTAMP + CURRENT_TIME NOTNULL NOTNULL % FALSE IN (RAISE(
```

---

## Crash 141: `0478f578de1688bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117199`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE CHECK (NULL)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE / CAST(CURRENT_TIMESTAMP AS REAL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 142: `aae36296d293d25a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117353`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE / CAST(CURRENT_TIMESTAMP AS REAL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 143: `e27777ec6bc4d0cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117363`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE CHECK (NULL)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE / NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGN
```

---

## Crash 144: `a3cad9ade3a34111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118475`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 145: `555d33c8bdcbdfdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118730`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (X'Db8DBeFAcbAB4C' NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME); PRAGM
```

---

## Crash 146: `56b5100f8986ea6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118942`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-4.655E87097768874255719963366 NOT BETWEEN CURRENT_TIMESTAMP AND -4.655E
```

---

## Crash 147: `8f03d13a1c5a2a2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119137`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-4.655E87097768874255719963366 NOT BETWEEN CURRENT_TIMESTAMP AND TRUE); 
```

---

## Crash 148: `7ccfb0493f9b5b7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119170`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 149: `9cfe4ec3f02e333a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119442`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (lower(CURRENT_TIME)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 150: `0ca8efa5506a5384` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120478`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_TIME * FALSE); PRAGMA integrity_check; SELECT printf('%.*g', 214
```

---

## Crash 151: `17b48ed9751db30a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122261`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT OR IGNORE INTO p VALUES (-CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 152: `b6e558f838a715a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122648`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (-''); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 153: `3d90375c8c81c7ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122815`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (X'9BE9'); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 154: `ad322fd69f657084` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123328`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (NULL IS TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 155: `e9aa11ebbe89d3de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123646`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || 
```

---

## Crash 156: `a612f6cf1faa0d70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124406`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE); PRAGMA in
```

---

## Crash 157: `04c73318bb7e1282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124857`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (FALSE LIKE CURRENT_DATE ESCAPE CURRENT_TIME % total_changes()); PRAGMA i
```

---

## Crash 158: `b83d12a75289ae8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127808`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON FALSE || FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 159: `37abef9c1006c423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128734`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIMESTAMP OR CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 160: `a74389542afc5622` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129034`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL); SELECT * FROM p JOIN p f90np ON CURRENT_TIME COLLATE NOCASE IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 161: `012897e26088fb11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131155`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (random() COLLATE BINARY || TRUE || TRUE || TRUE || TRUE || TRUE || 
```

---

## Crash 162: `be68bd7004538fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131723`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED WHERE FALSE LIMIT -TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT
```

---

## Crash 163: `dc16a8d034168efc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133522`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); SELECT DISTINCT * FROM p NOT INDEXED JOIN (VALUES (NULL)) AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 164: `4ce386310e4f44d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133711`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(rowid BLOB); SELECT DISTINCT * FROM p NOT INDEXED JOIN q NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 165: `1de6fd1b6161da0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134227`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO p SELECT ALL * FROM q ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST; PRAGMA integrity_check; 
```

---

## Crash 166: `b11cfb044b487047` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137129`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a)
```

---

## Crash 167: `5c6add6b373f4789` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137302`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL, c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 168: `c4db97362048ed7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139044`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p._rowid_))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 169: `9993b17f3dbeee53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139095`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p.c1))); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check;
```

---

## Crash 170: `5a21499a91f5d223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139115`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p.c1))); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME * ~CURRENT_DATE); PRAGMA integrity_check;
```

---

## Crash 171: `5f23f9f068c4adde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139162`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (zeroblob(p.c1))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 172: `d5c4bf31bab3ff80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139194`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(p.c1))))))))))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 173: `321b2935b12f7d24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139216`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(last_insert_rowid()))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 174: `76b76d2fe211dbb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144225`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LEFT OUTER JOIN p ON TRUE <> TRUE NOTN
```

---

## Crash 175: `f5583c1209bb0997` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144741`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (SELECT ALL * FROM q NOT INDEXED) AS e7___3__s46k974
```

---

## Crash 176: `84b52ad10d2db832` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146013`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (NULL IS b IS CURRENT_TIMESTAMP IS FALSE IS CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 177: `bb98a5ed40252a02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146143`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (NULL IS CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP IS FALSE IS CURRENT_TIMESTAMP)); INSERT INTO p DEFAU
```

---

## Crash 178: `c4ce20e188e9f408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147367`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 179: `3b9e506f197d6b93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147375`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE IND
```

---

## Crash 180: `67aa38e328c3a513` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147979`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); SELECT * FROM p JOIN q vd_n_ ON CURRENT_TIMESTAMP IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 181: `5c4889e1af458ed2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148503`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN CHECK (FALSE)); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p SELECT DISTINCT * FROM p WHERE FALSE; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 182: `637b8460c30e05df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149072`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 183: `f81206b94f931074` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149331`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE), c3 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, c3); SELECT NULL > (CURRENT_T
```

---

## Crash 184: `22e3057078d69041` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149416`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY, c2 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p
```

---

## Crash 185: `1902fb9b3d6a1b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149578`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (rowid) VALUES (TRUE) ON CONFL
```

---

## Crash 186: `da263edea5e76f83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE LIKE CURRENT_TIMESTAMP ESCAPE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VA
```

---

## Crash 187: `8d00e492dfc180b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149779`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT NULL COLLATE RTRIM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (rowid) VALUE
```

---

## Crash 188: `5aab346802c95858` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150030`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT *, count(*) FILTER (WHERE CURRENT_TIME) AS u__1lg1_k FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 189: `ba649051f450a577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156678`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT min(CURRENT_DATE) FILTER (WHERE CURRENT_TIME) OVER () AS a UNION VALU
```

---

## Crash 190: `a7afbd66a9bcb0fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156964`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL, c2 DATE UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_DATE GROUP B
```

---

## Crash 191: `611c51de81e0e801` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157349`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, FALSE IN (CAST(FALSE AS VARCHAR(
```

---

## Crash 192: `75e43e5896d4bb11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157486`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC DEFAULT X'8bbbdbdaEA3B', c2 INT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, FALSE
```

---

## Crash 193: `4409f707bfaf6033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158048`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, CAST(CURRENT_TIMESTAMP AS BLOB))
```

---

## Crash 194: `58877049e0dc3990` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158274`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT group_concat(FALSE) AS v5 FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT FALSE); SELECT
```

---

## Crash 195: `b8c2738dbaa14aae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159323`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB PRIMARY KEY); REPLACE INTO q VALUES ((SELECT * FROM q NOT INDEXED GROUP BY TRUE)); EXPLAIN QUERY PLAN VALUES (CURREN
```

---

## Crash 196: `5535453e1e0e71f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159476`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex(zeroblob(-214748364
```

---

## Crash 197: `3099e3f6e3187eaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p.c1))); INSERT INTO p VALUES (X'24D4A1fd9E44') ON CONFLICT DO NOTHING; SELECT *; SELECT hex(zeroblob(1));
```

---

## Crash 198: `17c05adc85be4706` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161328`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIME WINDOW w1 AS () EXCEPT SELECT 
```

---

## Crash 199: `e1c36c3e03a9bdc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168110`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) AS v5, * FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 200: `b38051aed9f3803c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168709`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE I
```

---

## Crash 201: `f908f7806c26b921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169099`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE DEFAULT X'e6dABd15d1FfaA'); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (count(*) OVER ())); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 202: `c77e8caa1bc92523` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171319`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR IGNORE INTO p VALUES (random() COLLATE BINARY || TRUE || TRUE || TRUE || TRUE || TRUE); EXPLAI
```

---

## Crash 203: `256bd725fe87a292` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178168`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO q (rowid) VALUES (random() COLLATE BINARY || TRUE || TRUE || TRUE) ON CONFLICT(c2) DO UPDATE
```

---

## Crash 204: `8ad763fbba240aa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182202`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); VALUES (TRUE) EXCEPT SELECT CURRENT_TIME NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VALUES ((SELECT * FROM q N
```

---

## Crash 205: `161470abef41b282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182799`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (NULL) INTERSECT SELECT * FROM (VALUES (NULL)) AS a WHERE FALSE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 206: `681117e3415b8266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183812`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(*) FILTER (WHERE zeroblob(zeroblob(CURRENT_TIME))) OVER () AS a INTERSECT VALUES (NULL); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 207: `70a894abce39a115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184121`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT min(CURRENT_DATE) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIME ASC NULLS LAST, TRUE DESC) AS a INTERSECT VALUES (NULL); SELEC
```

---

## Crash 208: `938087f5e5285048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184739`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT min(NULL) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY TRUE) AS a INTERSECT SELECT zeroblob(zeroblob(CURRENT_TIME)); SELECT hex(zerobl
```

---

## Crash 209: `8294266e42dda16d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184807`

```sql
SELECT substr('', -1, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 VALUES (CURRENT_TIME NOT NULL, FALSE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE) NOT NULL IN (
```

---

## Crash 210: `5872527a07c8da78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184951`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT random() COLLATE BINARY AS iwfvf5da_25ko11_bqx6_2__ek5on021____b3uy_3p__4___5___n9__w532__3___l_2_393x07mxvzggs_p__l_6420 INTERSECT SELE
```

---

## Crash 211: `7e793d7badbcc1eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186211`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT min(CURRENT_TIMESTAMP) FILTER (WHERE FALSE) OVER () AS a INTERSECT VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 212: `dce0cbe333e523ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186461`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (count(DISTINCT CURRENT_TIME)) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 213: `58914a372a1f4b8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191002`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT rowid FROM (SELECT CURRENT_TIME FROM p WHERE CASE FALSE WHEN FALSE THEN FALSE END) AS sub1; CRE
```

---

## Crash 214: `fac5c207e3bf35a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192680`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP > _rowid_) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT IN
```

---

## Crash 215: `5c86a249a8f4d2ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192845`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE _rowid_ > CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p
```

---

## Crash 216: `7ca42947530e38f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193089`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE > CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT I
```

---

## Crash 217: `de881a8cb6548823` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193151`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP > _rowid_ > CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 218: `40e949f2670e3c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193300`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT *, * FROM p WHERE NULL) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 219: `743ec591bba6e916` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194024`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, c1 INTEGER); INSERT OR FAIL INTO q VALUES (CURRENT_TIME, NULL); VALUES (CURRENT_TIMESTAMP); CREATE TA
```

---

## Crash 220: `1fa52d7daaa4875c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194050`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, c1 INTEGER); INSERT OR FAIL INTO q VALUES (CURRENT_TIME, NULL); VALUES (CURRENT_TIMESTAMP); CREATE TA
```

---

## Crash 221: `7d5685025cff3c9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198573`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p SELECT CURRENT_DATE AS a UNION VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 222: `356e0fce7cf06f7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199463`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, 
```

---

## Crash 223: `f1323187666f031b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200597`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE _rowid_ > total_changes()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p D
```

---

## Crash 224: `ff16f27898f071e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200806`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM p WHERE _rowid_ > TRUE % total_changes() % FALSE % CURRENT_TIME % CURRENT_TIMESTAMP % FALSE % CURRENT_TIME % NULL % 
```

---

## Crash 225: `720e38e060b0c04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202235`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT * FROM (SELECT sum(TRUE) FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 226: `c29e5a46668bda3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209109`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); SELECT TRUE COLLATE RTRIM NOT IN (SELECT * FROM p) AS a INTERSECT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR I
```

---

## Crash 227: `fc578007ffe1d627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209285`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); SELECT NULL NOT IN (SELECT * FROM p) AS a INTERSECT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p V
```

---

## Crash 228: `de26b00d4b69875a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210372`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO q (rowid) VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 229: `29df5aaa5ddcefd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214843`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); INSERT INTO p (c2) VALUES (random() COLLATE BINARY || TRUE || TRUE || TRUE); VALUES (CURRENT_TIME);
```

---

## Crash 230: `7c446f3161f96449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222355`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT group_concat(FALSE, '') AS v5, * FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 231: `2a35207fc6c60623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231138`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQU
```

---

## Crash 232: `bcf0cf36cb8bc93a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231306`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CRE
```

---

## Crash 233: `035ab7ff5f0cec01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231475`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT
```

---

## Crash 234: `9e26a9407fcea08d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231508`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY K
```

---

## Crash 235: `0915235d8c85af6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231691`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY
```

---

## Crash 236: `9183859dd4913684` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234375`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (), (VALUES (FALSE)))); CR
```

---

## Crash 237: `bbf768b748301f63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235002`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LIMIT TRUE, (SELECT DISTINCT * FROM q)); CRE
```

---

## Crash 238: `34a617d01793e0a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235933`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (SELECT min(CURRENT_DATE) FILTER (WHERE CURRENT_TIME) OVER
```

---

## Crash 239: `2be8efd60a481133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236114`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (VALUES (TRUE)) AS e7___3__s46k974_2___t8__p_q569s JOIN p 
```

---

## Crash 240: `c77aa8f4b016ddc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236123`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (SELECT CURRENT_TIMESTAMP AS a ORDER BY TRUE ASC NULLS LAS
```

---

## Crash 241: `22a32ff640f43b7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239837`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (FALSE) INTERSECT VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 242: `12bf4af5317ff1a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240077`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT *, min(CURRENT_TIME) FILTER (WHERE CURRENT_TIME) AS u__1lg1_k FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 243: `97af6368bea4d3de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241334`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL, c3 REAL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (rowid)
```

---

## Crash 244: `86fb5b6844143e88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246746`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (CURRENT_TIMESTAMP IN (FALSE, NULL, FALSE))); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 245: `f8ccb45d98801b14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246982`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (CURRENT_TIMESTAMP IN (CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 246: `b4e9790166a8c9d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247898`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (NULL IS b IS CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 247: `5e76b76e87b74ee4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247974`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL, c2 DATE CHECK (NULL IS b IS CURRENT_TIMESTAMP IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FALSE IS FA
```

---

## Crash 248: `95f2f1a85cba42a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249437`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LEFT OUTER JOIN p ON CURRENT_TIMESTAMP
```

---

## Crash 249: `50e4321e7ace3894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249668`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM q NOT INDEXED LEFT OUTER JOIN p NOT INDEXED NATURAL 
```

---

## Crash 250: `a1f6fc0fb8c68873` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250877`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM (VALUES (CURRENT_DATE) UNION SELECT FALSE AS f) AS c
```

---

## Crash 251: `15237973b628a83e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(p.c1))); INSERT OR IGNORE INTO p VALUES (~NULL COLLATE RTRIM); PRAGMA integrity_check;
```

---
