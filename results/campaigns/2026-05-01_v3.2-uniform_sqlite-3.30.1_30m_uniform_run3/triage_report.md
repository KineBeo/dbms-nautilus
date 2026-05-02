# Crash Triage Report

**Total crashes:** 277  
**Unique crash sites:** 277  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 277 | 277 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `717a9355c55c5c6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000063`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CASE -CURRENT_TIME COLLATE BINARY WHEN NULL THEN CURRENT_TIME NOT NULL ELSE CURRENT_DATE IS NOT NULL / +NULL END COLLATE BINARY = RAISE
```

---

## Crash 2: `a3790538fb7183c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000363`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, c3, c2, c3, b, c3); WITH s (c2, b, c3, a) AS NOT MATERIALIZED (SELECT TRUE AS ra6o FROM p AS z38 GROUP BY CURRENT_TIMESTAMP, NULL NOT N
```

---

## Crash 3: `eb1bcaeb93c84178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000942`

```sql
SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR ABORT INTO s VALUES (TRUE | NULL + RAISE(IGNORE) IS DISTINCT FROM RAISE(IGNORE) IS NULL AND CURREN
```

---

## Crash 4: `7d7d6065c1c17a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001920`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT DISTINC
```

---

## Crash 5: `32455c1ed4b2d6ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002211`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t1 DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid FLO
```

---

## Crash 6: `555e0b751cf5e634` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003233`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME BETWEEN FALSE AND TRUE); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-1)); CR
```

---

## Crash 7: `dee490da90e43a62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003980`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NULL COLLATE NOCASE, r.*, CURRENT_TIME * random() AS o86e, FALSE COLLATE RTRIM <= CURRENT_TIME != RAI
```

---

## Crash 8: `6aea3e78ae08f0e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005171`

```sql
SELECT printf('%lld', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CASE CASE WHEN CURRENT_TIME THEN TRUE NOTNULL NOT NULL ELSE TRUE NOTNULL END WHEN ~CASE WHEN FALSE COLLAT
```

---

## Crash 9: `dee6af1dd31a4fde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005588`

```sql
SELECT printf('%.*g', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NULL, CURRENT_DATE FROM t3 WHERE EXISTS (SELECT CURRENT_TIME FROM t3 INDEXED BY _rowid_ JOIN r A
```

---

## Crash 10: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006862`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 11: `b8a6d8e27eba1185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006873`

```sql
SELECT printf('%.*f', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (c1) VALUES (a); SELECT q.*, RAISE(IGNORE) LIKE CURRENT_TIMESTAMP AS y_, CAST(CURRENT_T
```

---

## Crash 12: `65cd00074ce7bb88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006888`

```sql
SELECT printf('%f', 4294967296, '-j_ g-S UP'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT OR IGNORE INTO p VALUES (p.c3); SELECT *, RAISE(IGNORE) BETWEEN CURRENT_TIME AND FALS
```

---

## Crash 13: `d6124ac8ab89ff3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006946`

```sql
SELECT printf('%.*g', -9223372036854775808, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT +NULL == ~CURRENT_TIMESTAMP IS NOT EXISTS (SELECT CURRENT_DATE IS NULL) COLLATE NO
```

---

## Crash 14: `cb4c3709f28a4b1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007405`

```sql
SELECT substr('-m-__y4', 2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE p AS (SELECT CASE WHEN FALSE IS NULL THEN FALSE != NOT EXISTS (SELEC
```

---

## Crash 15: `c579682094238ef5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009402`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT O
```

---

## Crash 16: `403481510971d4a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009592`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (TRUE); VALU
```

---

## Crash 17: `33495d84263e1564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010261`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 18: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010465`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 19: `0c1fbd7838df846e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011535`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT max(TRUE COLLATE NOCASE > RAISE(IGNORE) IS NOT FALSE >= CASE WHEN CURRENT_TIME THEN CURRENT_TIMESTA
```

---

## Crash 20: `192a8af735dec6ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013255`

```sql
SELECT substr(' 5g ', 9223372036854775807, -2147483648); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 21: `d05a0bb0b43f9946` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014046`

```sql
SELECT substr('- r30MSWl-', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH t2 (b) AS (VALUES (FALSE) ORDER BY FALSE ->> CURRENT_TIMESTAMP) 
```

---

## Crash 22: `a8bb0309b71505a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014319`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, a); INSERT INTO q DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(9223372036854775807
```

---

## Crash 23: `bcf807d3f895459f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014331`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3); INSERT INTO q DEFAULT VALUES; SELECT *; SELECT hex
```

---

## Crash 24: `375a10939b5e6d60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018328`

```sql
SELECT printf('%.*e', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, b); INSERT OR ABORT INTO q VALUES (CASE WHEN NOT TRUE COLLATE BINARY IS DISTINCT FROM F
```

---

## Crash 25: `4cd431a539f1cc20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020362`

```sql
SELECT printf('%.*f', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO r VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIME ASC 
```

---

## Crash 26: `1961c06c6be8e29d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020611`

```sql
SELECT printf('%.*s', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *;
```

---

## Crash 27: `894d83f646b9531e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020961`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a);
```

---

## Crash 28: `bb5ef2ce5c04cfe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021596`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO s VALUES (CASE -TRUE N
```

---

## Crash 29: `e68a7c836793d01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022874`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, b, c3, c3); INSERT OR ROLLBACK INTO t2 VALUES (CASE WHEN CURRENT_DATE AND NOT EXISTS (VALUES (R
```

---

## Crash 30: `e881ea52c6c24937` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023087`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION ALL SELECT ALL * FROM q; SELECT pri
```

---

## Crash 31: `201bdeee2482529f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025890`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT round(-1e308, -1); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 32: `d6c3fb55f2da658f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027371`

```sql
SELECT printf('%.*s', 9223372036854775807, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (RAISE(IGNORE) REGEXP abs(RAISE(IGNORE) NOT IN (CURRENT_DATE)) OR NULL 
```

---

## Crash 33: `b10bab690a5c5b81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030044`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 34: `253c96ae8edf2faf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030301`

```sql
SELECT printf('%.*g', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p AS (VALUES (CURRENT_DATE)) SELECT q.* FROM p; SELECT hex(zeroblob(-1));
```

---

## Crash 35: `303e29502e27b473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032625`

```sql
SELECT printf('%.*d', -9223372036854775808); SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS MATERIALIZED (SELECT * LIMIT (TRUE)) SELEC
```

---

## Crash 36: `48dfae5f325c6b97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039188`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (TRUE <> CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 37: `9d86e74305786fba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039487`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIMESTAMP NOT LIKE TRUE)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL T
```

---

## Crash 38: `c295cf9605ec9d6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040187`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); S
```

---

## Crash 39: `ec70dbb84ecc570c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIMESTAMP <> CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL
```

---

## Crash 40: `9647f4d037d9a97c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040606`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 41: `ed04de8fa9d24fd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041065`

```sql
SELECT printf('%.*d', 4294967296, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p WITH RECURSIVE t2 AS MATERIALIZED (SELECT q.*, CURRENT_TIME AS a UNION VALUES (~CURRE
```

---

## Crash 42: `73b95bc32b2ae6f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044254`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 43: `7bde9b9179868af9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044342`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGM
```

---

## Crash 44: `88e51ac1f8ffd189` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044632`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 45: `1ac1991a91bb6904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048872`

```sql
SELECT substr(' -4', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, c3, b); WITH RECURSIVE r (c1) AS NOT MATERIALIZED (VALUES (+CURRENT_TIME AND NOT TRUE ISNULL > CURREN
```

---

## Crash 46: `9c6507fe33e23ec6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051048`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_DATE), c1 DATE CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 47: `d260cb78e60cb5e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051445`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE TRUE NOTNULL EXCEPT SELECT DISTINCT TRUE BETWEEN CURRENT
```

---

## Crash 48: `cd5140a8e0c74a12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055565`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (p._rowid_)); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e3
```

---

## Crash 49: `c61515f30940987d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055680`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 50: `e142bba50cc8989e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 51: `fe85c12eed9c4a98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056155`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 52: `2dede4f8eb67294f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056248`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE, a BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 53: `40cd65915aa6148f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056284`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL DEFAULT X'BCa6'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 54: `0b4a0b7155d6d057` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056435`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 55: `51a9f87c01983dcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059553`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (TRUE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 56: `3b929816c454d537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059783`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (TRUE); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF
```

---

## Crash 57: `8fdd92b7725a2cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060623`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (c2)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 58: `c89625037a5fc0ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060737`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIMESTAMP IS NOT CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (TRUE); VALUES (CURRENT_TIMESTAMP); SELECT prin
```

---

## Crash 59: `1b8e048aa57bf7c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062354`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL * FROM p NOT INDEXED; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 60: `1af91a7df91c08aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL FALSE FROM (SELECT DISTINCT typeof(FALSE), * FROM p NOT INDEXED) AS a; VALUES (CU
```

---

## Crash 61: `8fb79bf13e2a9e53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063404`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 62: `d13b3bba4c0a6729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063411`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL * FROM q; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 63: `e2bbc80d4781a6b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063420`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL * FROM (VALUES (TRUE)) AS a; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 21
```

---

## Crash 64: `f3d6ca40052d5f58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL * FROM (SELECT DISTINCT * FROM p NOT INDEXED) AS a; VALUES (CURRENT_TIMESTAMP); S
```

---

## Crash 65: `fe4ea5890966244d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064345`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 66: `61b80f98bd3095f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064446`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_DATE < CURRENT_TIMESTAMP COLLATE RTRIM)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); S
```

---

## Crash 67: `c2eff398a2e7e4ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066227`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (TRUE >= NULL)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 68: `b8b1101f8d386b1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066447`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS (); SELECT prin
```

---

## Crash 69: `009b7a23f1caf252` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066793`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT
```

---

## Crash 70: `84ec5fcc49ab0cae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070138`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); VALUES (CURRENT_DATE) UNION ALL SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 71: `66db9f4f9e4a7709` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070973`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); SELECT * FROM (p NOT INDEXED NATURAL LEFT JOIN p) NATURAL LEFT JOIN p WHERE FALSE GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 72: `bb04c4eb5ea51f96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071938`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) INTERSECT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 73: `ba5eafe8f48b67aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072115`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (FALSE) INTERSECT SELECT * FROM p WHERE FALSE GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 74: `c7e621c2189adfd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072346`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT X''); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 75: `f7d8f48de0020c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073454`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY, c2 TEXT); INSERT INTO p (rowid) VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p 
```

---

## Crash 76: `c6b5f94d89666718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076367`

```sql
SELECT printf('%.*e', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 77: `1d1883a298709283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076373`

```sql
SELECT substr('_w   _--V_3wQ2B-y', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(2147483
```

---

## Crash 78: `55cc723f25907943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076910`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT CURRENT_TIMESTAMP
```

---

## Crash 79: `90f698678568844f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077148`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUA
```

---

## Crash 80: `ebd06ca072af5e7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078703`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 81: `b2ebf17d0814ad56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079621`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE % CURRENT_TIMESTAMP); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO 
```

---

## Crash 82: `858ae4426716b843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080054`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES 
```

---

## Crash 83: `7757be0148014750` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080128`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (725.585268E8 <> FALSE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DE
```

---

## Crash 84: `1fb7364576e06216` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080283`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (TRUE <> FALSE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VA
```

---

## Crash 85: `23e1fa86cf070ac3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080738`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p (rowid) VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, 
```

---

## Crash 86: `b3c901de557c38b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080937`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (CURRENT_DATE << CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 87: `aca5f76908612aaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081087`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT IN
```

---

## Crash 88: `4012df060be8b7b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081098`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT IN
```

---

## Crash 89: `e3b5347bfdf0f854` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085274`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT * FROM q NOT IN
```

---

## Crash 90: `03bff0a8a66776d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087900`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED NATURAL LE
```

---

## Crash 91: `dd8666eae23d650f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088301`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT DISTINCT * FROM p UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; ANALYZE q; CRE
```

---

## Crash 92: `3dc256546316e9ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088402`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; ANALYZE q; C
```

---

## Crash 93: `83291552ddeaf6a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088768`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIME ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE
```

---

## Crash 94: `e8ecc432136d8906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089079`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT ~(NULL - NULL -> randomblob(CURR
```

---

## Crash 95: `cba3209825bb57c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089550`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE zeroblob(TRUE)) AS sub1; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 96: `9225e79c1403d7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089855`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT FALSE LIKE FALSE ESCAPE FALSE, FALSE LIKE FALSE ESCAPE FALSE, * FROM q WHERE TRUE) AS 
```

---

## Crash 97: `07f32bf66d8efa26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090030`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE changes()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 98: `0c3a29f2951a1ee2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091214`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM (VALUES (CURRENT_DATE)) AS a WHERE FALSE GROUP BY CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1
```

---

## Crash 99: `508387d879bbf2f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091471`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT *, * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 100: `4b0ccdf20e7c96e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091597`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 101: `278a13db892704bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091957`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p WHERE FALSE GROUP BY CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 102: `20a2ac680c4ad51a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092276`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY FALSE HAVING (VALUES (CURRENT_DATE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 103: `affed755c0111937` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092426`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY FALSE HAVING CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 104: `92aa20eff1131004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093074`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY FALSE < CURRENT_TIME >> CURRENT_DATE HAVING CURRENT_TIMESTAMP); CREATE VIRTUAL 
```

---

## Crash 105: `ec2b02487aec61a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093399`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY CURRENT_TIME >> CURRENT_TIME IN (FALSE) HAVING CURRENT_TIMESTAMP); CREATE VIRTU
```

---

## Crash 106: `e52be1d0b67a2736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093769`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649,
```

---

## Crash 107: `4dd03e698416f042` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094887`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP, FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 108: `7271b65c6234eba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095578`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT rowid FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; A
```

---

## Crash 109: `ac204ba15ee97ac9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102971`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c2 NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABL
```

---

## Crash 110: `4b2744d7db123b27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108078`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) EXCEPT VALUES (RAISE(IGNORE)); SELECT CURRENT_TIME <= CURRENT_DATE FROM p
```

---

## Crash 111: `7cb97d5b049aee66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109012`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE OR zeroblob(FALSE)); PRAGMA integrity_check;
```

---

## Crash 112: `54e44934a28c8c0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112981`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); REPLACE INTO p VALUES (TRUE - FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (TRUE - 
```

---

## Crash 113: `72ffd1066e1de152` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118395`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_TIMESTAMP | CURRENT_TIMESTAMP AS REAL)) AS sub1; CREATE VIRTUA
```

---

## Crash 114: `7b5b88b3db714fa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE IN (VALUES (CURRENT_TIME)) IS NULL) AS sub1; CREATE VIRTUAL TA
```

---

## Crash 115: `036d5be60d86d628` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CASE WHEN FALSE > CURRENT_TIME THEN CURRENT_DATE ELSE CURRENT_TIMESTAMP END
```

---

## Crash 116: `c135579b95962697` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119378`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT 879472472508792540480280431286720645402440991546163588461419114124467977068121568859662860
```

---

## Crash 117: `62b93538ea59697a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120238`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE
```

---

## Crash 118: `ab49b99b0af498ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120346`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIME ASC NULLS LAST ROWS BETWEEN U
```

---

## Crash 119: `852b3437b01bdcd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120388`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIME ASC NULLS LAST ROWS BETWEEN U
```

---

## Crash 120: `315c9be6de5e4dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120559`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT FALSE <= CURRENT_TIMESTAMP IS NOT CURRENT_TIMESTAMP FROM (SELECT * FROM p WHERE NULL) AS sub1; CREA
```

---

## Crash 121: `e81b8c81068376c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120800`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT NULL IS NOT FALSE FROM (SELECT * FROM p WHERE NULL) AS sub1; SELECT printf('%.*g', -2147483649, 0.0
```

---

## Crash 122: `d3e41e4fdc300844` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121618`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE NULL / CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 123: `0520bf68eef7b43f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121899`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE NULL IS NOT CURRENT_TIMESTAMP / CURRENT_TIME) AS sub1; CREATE VIRTUAL 
```

---

## Crash 124: `40bb266ef5107898` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122683`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE, c3 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 125: `f7f6b35c48b0633d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT *, * FROM p WHERE zeroblob(CURRENT_TIME)) AS sub1; SELECT hex(zeroblob(-9223372036854
```

---

## Crash 126: `c219cef9afee7182` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT 0); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 127: `f4ba9ed93c23a846` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT FALSE, a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUA
```

---

## Crash 128: `b3cde5e60b4d2a16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125120`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 129: `279f312ec3a8625c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125467`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 130: `9bb516f1d6bb7794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128360`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / ~FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 131: `9cb450c3c8836765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / 8794724725087925404802804312867206454024409915461635884
```

---

## Crash 132: `ca17994167efcca9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128919`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / CURRENT_DATE / zeroblob(zeroblob(zeroblob(zeroblob(zero
```

---

## Crash 133: `47d0ec7d8f199f1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE / CURRENT_DATE / zeroblob(zeroblob(NULL))) AS sub1; SELEC
```

---

## Crash 134: `d90b4f3672e336f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129904`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP OR TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 135: `75491b7f308e180e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131778`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zeroblob(2147483647));
```

---

## Crash 136: `0f240aa1c7f63f39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132096`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_DATE IN (VALUES (_rowid_)) AS qx_0k410q1i_o9h_ FROM p WHERE TRUE) AS sub1; CREATE 
```

---

## Crash 137: `e0a90534d6cb6f2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132404`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CASE NULL WHEN NULL THEN NULL END, * FROM p WHERE zeroblob(zeroblob(NULL))) AS sub1; SELEC
```

---

## Crash 138: `ab9308a161a5ffe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132569`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE FALSE > CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 139: `c5e26c0a220c488e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132822`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE c2 IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 140: `6483abbac8cba24a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133043`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE c2 NOT NULL IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 141: `cb5d98d5e5b0f8a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133152`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL NOT NULL IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 142: `c855d6c1bfc9db4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133185`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CAST(NULL AS REAL) IS NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 143: `6df0c340fcee6202` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CAST(NULL AS REAL) IS NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 REAL U
```

---

## Crash 144: `764e3fe8f1bea96b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138618`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE); REPLACE INTO p VALUES (TRUE - TRUE - TRUE - CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 145: `3a86c6d98243dfbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139337`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER CHECK (NULL <> changes() <> zeroblob(zeroblob(NULL)) <> TRUE <> CURRENT_DATE <> CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSER
```

---

## Crash 146: `d3618f3e80c0687b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141991`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT OR REPLACE INTO q VALUES (CAST(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(
```

---

## Crash 147: `8f5189d3ab18a068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146203`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (TRUE) UNION SELECT zeroblob(zeroblob(NULL)) AS a ORDER BY a ASC NULLS LAST;
```

---

## Crash 148: `f27ff342fa4cbe56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148328`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); VALUES (group_concat(CURRENT_TIME, '_C1YPa-_Qoj ___-LNl') OVER ()); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 149: `d378e6939d8484e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148853`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DE
```

---

## Crash 150: `2bb02870850b73a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156395`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY FALSE DESC NULLS FIRST, CURRENT_DATE ASC NULLS FIRST
```

---

## Crash 151: `13e9b92482897e9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156565`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () FROM p WHERE FALSE GROUP BY CURRENT_TIMESTAMP, FALSE); CREA
```

---

## Crash 152: `92610904ae6b264f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156572`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY FALSE DESC NULLS FIRST, CURRENT_DATE ASC NULLS FIRST
```

---

## Crash 153: `0a7572d674fbed25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159467`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p WHERE CURRENT_TIME IS NULL COLLATE RTRIM GROUP BY CURRENT_DATE); CRE
```

---

## Crash 154: `3aee0bdd3d56e640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159619`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p WHERE CURRENT_TIME COLLATE RTRIM GROUP BY CURRENT_DATE); CREATE VIRT
```

---

## Crash 155: `297b8a3c34a0ac38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161867`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 156: `d6841193e2111537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162090`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 157: `5bf8cef9f1442c0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162096`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 158: `cf6a489341357522` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162596`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 159: `5dbac848e27d9ba1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162696`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY FALSE DESC NULLS FIRST, CURRENT_DATE ASC NUL
```

---

## Crash 160: `485564c57ba69355` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162836`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE abs(CURRENT_TIME)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 161: `bf4d1a6e10b1da22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163460`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT FALSE * NULL IS NOT CURRENT_TIMESTAMP FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT he
```

---

## Crash 162: `ac462386231a7a47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163467`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT FALSE LIKE FALSE ESCAPE NULL, * FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zero
```

---

## Crash 163: `a01aef38dd4de6ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163476`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT CURRENT_TIME IN (-0) FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zeroblob(922337
```

---

## Crash 164: `1fc0ed3d50cfaa1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163505`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT lower(~FALSE) | TRUE MATCH CURRENT_DATE AS y FROM q WHERE zeroblob(FALSE)) AS sub1; SE
```

---

## Crash 165: `9c37172409ab2608` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163533`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT CURRENT_DATE IS TRUE COLLATE RTRIM FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(z
```

---

## Crash 166: `18aea115f1fa2d29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163540`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT *, count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY TRUE ORDER BY CURRENT_TIMESTAMP DESC 
```

---

## Crash 167: `b8d11363c6dd091f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163546`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY, a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zeroblob(9223372
```

---

## Crash 168: `4acb668353d18a05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163558`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT FALSE * NULL IS NOT CURRENT_TIMESTAMP, * FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT
```

---

## Crash 169: `de85820f967fb2a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163565`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT NULL = count(*) FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zeroblob(92233720368
```

---

## Crash 170: `27b98c05e5b0f0f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163571`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT lower(FALSE) | TRUE MATCH TRUE AS y FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(
```

---

## Crash 171: `efe14cfd71fab757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163583`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT CURRENT_TIME IN (CURRENT_DATE, CURRENT_DATE, CURRENT_DATE) FROM (SELECT * FROM q WHERE zeroblob(FALSE
```

---

## Crash 172: `80ba4f4d32e858ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163636`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); SELECT * FROM (SELECT * FROM q WHERE zeroblob(FALSE)) AS sub1; SELECT hex(zeroblob(9223372036854
```

---

## Crash 173: `c3a77b16c09d93ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163647`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL DEFAULT CURRENT_TIME, a NUMERIC NOT NULL DEFAULT NULL); SELECT * FROM (SELECT * FROM q WHERE zeroblob
```

---

## Crash 174: `99c1e28bb2b21682` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165100`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIME ORDER BY zeroblob(zeroblob(NULL)) RANGE BETWEEN UNBOUNDED PRECEDING
```

---

## Crash 175: `6a0b7acdc3086328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165441`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY changes() ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GR
```

---

## Crash 176: `f63b309f6106d8eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165872`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 177: `bcbbe135430dad2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166445`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT DISTINCT * FROM p UNION VALUES (FALSE); SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAU
```

---

## Crash 178: `15be4367e0f1e552` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166543`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (TRUE) UNION VALUES (FALSE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 179: `a9fe6fb3e96fda14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167249`

```sql
SELECT printf('%u', 2147483647, '_ u-7-UdX'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE q AS (VALUES ((TRUE), ~NOT (NOT EXISTS (SELECT p.*) LIKE CURRENT_DATE BETWEEN TRUE
```

---

## Crash 180: `515d274e0d972691` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167750`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS FALSE IS FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT 
```

---

## Crash 181: `b9b1a6c03f04a23f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168507`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_TIMESTAMP || CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CU
```

---

## Crash 182: `31ded2e9480dc118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171011`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); INSERT INTO p VALUES (TRUE GLOB CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY P
```

---

## Crash 183: `5ab7e8030a437098` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171336`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT q.* FROM p NOT INDEXED INNER JOIN (p NOT INDEXED NATURAL
```

---

## Crash 184: `9439f143cae8de0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171421`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT q.* FROM p NOT INDEXED INNER JOIN (p NOT INDEXED) CROSS 
```

---

## Crash 185: `c4ebddb836c6e191` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172217`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT FALSE IN (SELECT zeroblob(zeroblob(NULL))) AS a FROM p WHERE EXISTS 
```

---

## Crash 186: `c84dcc9465aec94b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175694`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 187: `f42a91e14f5f24fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176169`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (725.585268E8 <> CURRENT_DATE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR
```

---

## Crash 188: `d19a99a78ad2a132` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176248`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (NULL <> CURRENT_DATE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL IN
```

---

## Crash 189: `3fca04c1c1cf6215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176384`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT X'c2CbbcAAf1ae'); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR FAIL INTO q 
```

---

## Crash 190: `ba92fde24716e4f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176442`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT OR FAIL INTO q VAL
```

---

## Crash 191: `4644c319ad9dfa30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176462`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); INSERT INTO p (rowid) VALUES (725.585268E8); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (rowid) VAL
```

---

## Crash 192: `9196c5b2f1b9c4f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180708`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT FALSE, CURRENT_TI
```

---

## Crash 193: `3273de2a7fdec5ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180958`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT TRUE); CREATE TAB
```

---

## Crash 194: `1aecf28781104494` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181832`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN q NOT INDEXED WHERE CURRENT_DATE GROUP 
```

---

## Crash 195: `98b6b914a0ad1bc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183443`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY TRUE <= CAST(CURRENT_DATE IN (VALUES (CURRENT_TIME)) AS 
```

---

## Crash 196: `b0eba7e56705a251` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183605`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*g', 21474836
```

---

## Crash 197: `8ac506a76c458169` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183614`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY TRUE <= CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBOUND
```

---

## Crash 198: `db5aff3e4479689a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183620`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY TRUE <= CAST(TRUE AS REAL) ASC NULLS LAST ROWS BETWEEN U
```

---

## Crash 199: `2a86a9f9b1bde4ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184757`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p (_rowid_) AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 200: `a8a12592c8bf0501` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185562`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF
```

---

## Crash 201: `b87ac0dcba2d5266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186070`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT -295038); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO q VA
```

---

## Crash 202: `e3c03d45b3849fdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188699`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL LEFT JOIN (VALUES (CURRENT_TIMESTAMP)) AS a WHERE FALSE GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 203: `a78a63faca229472` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190210`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE zeroblob(FALSE); EXPLAIN QUERY PLAN SELECT gro
```

---

## Crash 204: `5ed3eae2cdc73267` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195101`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'eBEF4DBfB198'); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -214748
```

---

## Crash 205: `4d31f7764546f4b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195309`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIME NOT LIKE _rowid_ NOT NULL)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VI
```

---

## Crash 206: `53f0096c5f1184c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195821`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 207: `c626fa4e24754f88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196220`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_TIME | lower(FALSE) | TRUE)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUA
```

---

## Crash 208: `553088046b19220d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197359`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (CURRENT_DATE < X'D4')); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 209: `d0347e613455a27c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198481`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT * FROM q; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 210: `41e9f201ef3d926a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198879`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL * FROM q; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 211: `6da7da33305b4544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN p NATURAL LEFT JOIN q; VALUES (CURRENT_TIM
```

---

## Crash 212: `0eddcb2db267a775` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203855`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM q ORDER BY CURRENT_TIMESTAMP COLLATE R
```

---

## Crash 213: `feff07bf93729326` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203906`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p NOT INDEXED CROSS JOIN p NOT INDEXED
```

---

## Crash 214: `28d147d89cdc9ea4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205120`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE)
```

---

## Crash 215: `b542f701fd003e21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206222`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT X'D4'); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES (CURRENT_DATE) UNION ALL SELECT AL
```

---

## Crash 216: `b508a562f5f6872d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206693`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (TRUE); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN q; CREATE VIRTUAL TABLE IF
```

---

## Crash 217: `592513d18a406c17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207030`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE 
```

---

## Crash 218: `0b086cc225999fd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211455`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE, a NUMERIC UNIQUE, b NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT substr('', 922
```

---

## Crash 219: `c9a6f1690152fb84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211665`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY, a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT NOT NULL); INSERT INTO p (rowid) VALUES (725.585268E8); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 220: `7281506d719a057d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211824`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY, a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB DEFAULT X'EA6fFa900a'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 221: `28bee3bf3deb9d72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220658`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_DATE), c1 DATE CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * 
```

---

## Crash 222: `9b33aca4acd8e952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220942`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSER
```

---

## Crash 223: `01c9c2f7ec8c3c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221135`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); SELECT count(*) OVER () FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 224: `c6b2f0a4d01ff6a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222412`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT 'MD_Hy-l T-Hn '); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE FALSE IS NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 225: `a602cbb09f382195` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223148`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL
```

---

## Crash 226: `c19296e3c3a03bbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225072`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CAST(NULL AS REAL) NOT IN (FALSE, CURRENT_TIME); CREATE VIRTUAL TA
```

---

## Crash 227: `609c968f597d8dc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225272`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE NOT IN (FALSE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 228: `3e1101ab9a1e031c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225600`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF
```

---

## Crash 229: `3d09b43aab6bfee7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232159`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); INSERT INTO p SELECT count(*) OVER () AS a ORDER BY zeroblob(zeroblob(NULL)) ASC NULLS LAST; SELECT 
```

---

## Crash 230: `d1d8518749708b8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232827`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT count(*) OVER (ORDER BY CURRENT_TIME ASC ROWS 
```

---

## Crash 231: `c777fb6ab1dc0133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233018`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT NOT NULL DEFAULT ' d-_2_ 312'); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY a AS
```

---

## Crash 232: `7c01dffa3d238e87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237344`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE 
```

---

## Crash 233: `b18c1b3cd928aeb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE 
```

---

## Crash 234: `89cd91e6d79cb821` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238991`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (SELECT DISTINCT * FROM q NOT INDEXED UNION ALL SELECT
```

---

## Crash 235: `7bf046017bcb75af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240004`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM q 
```

---

## Crash 236: `aea038c38aa5090f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240231`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT count(*) FROM p; SELEC
```

---

## Crash 237: `0ff8648bc7916267` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241165`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM q ORDER BY CURRENT_TIMESTAMP; VALUES (
```

---

## Crash 238: `e4c9bd7f21b8c4ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241286`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY count(*)
```

---

## Crash 239: `1dec269cfab8d718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241294`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM t1 WHERE CURRENT_DATE GROUP BY RAISE(I
```

---

## Crash 240: `13b2bc77ae5e9786` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241313`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_DATE) INTERSECT SELECT * FROM p WHE
```

---

## Crash 241: `941969f17551860b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241323`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a NATU
```

---

## Crash 242: `78abe2c899d46a05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241333`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM (p AS s NATURAL LEFT JOIN p) WHERE CUR
```

---

## Crash 243: `0a9a2f1ca0fea851` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241341`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IG
```

---

## Crash 244: `9a73a5d3277e1675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241348`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVE
```

---

## Crash 245: `7ec8d39bb0e04364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241357`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM (SELECT CURRENT_DATE ORDER BY CURRENT_
```

---

## Crash 246: `3348abbffb06c114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241367`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT group_concat(c3, '_C1YPa-_Qoj ___-LNl') FILTE
```

---

## Crash 247: `09036fc2ebe3a3b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241373`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE changes() OR TRUE LIKE FALSE E
```

---

## Crash 248: `0ca9c678fa89b1d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241379`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IG
```

---

## Crash 249: `35306e61594cade2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241394`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (TRUE = CURRENT_TIME + TRUE >= NULL ISNULL > NULL, CURRENT_DATE, NULL) INTERSECT S
```

---

## Crash 250: `bbfdd0491da391a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241405`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM (VALUES (NULL) UNION ALL SELECT * FROM
```

---

## Crash 251: `8d38c6ada7c8ff8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241412`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IG
```

---

## Crash 252: `1d6eb13121900636` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241418`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE random() FILTER (WHERE CURRENT
```

---

## Crash 253: `4a7d6db3cee36c56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241427`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (RAISE(IGNORE) IN (SELECT * FROM p WHERE CURRENT_DATE)) INTERSECT SELECT * FROM p 
```

---

## Crash 254: `7fae988d02ed15d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241438`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE IN (VALUES (CURRE
```

---

## Crash 255: `3298b991c5a1384a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241445`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_DATE, CURRENT_DATE, CURRENT_DATE, CURRENT_DATE, CURRENT_DATE, CURRENT_DAT
```

---

## Crash 256: `89a595cb1052df45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241456`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IG
```

---

## Crash 257: `3e18408f40456e31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241462`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT NULL) FILTER (WHERE RAISE(IGNO
```

---

## Crash 258: `89f180a8c91316cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241487`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM (SELECT CURRENT_DATE FROM (VALUES (NUL
```

---

## Crash 259: `7ed3d84c53c09b31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241505`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM q INDEXED BY _rowid_ WHERE CURRENT_DAT
```

---

## Crash 260: `a10c6fe61ea90d29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241519`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM q NATURAL JOIN (VALUES (FALSE)) AS o__
```

---

## Crash 261: `352ca48c7977eb92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241554`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IGNOR
```

---

## Crash 262: `669a8c2374faaae2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241574`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURRENT_DATE GROUP BY RAISE(IG
```

---

## Crash 263: `0a135e7a870ac4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242690`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT DISTINCT * FROM q AS a NATURAL JOIN p NATURAL JOIN p; VALUES (CURRENT_TIMESTAMP); CRE
```

---

## Crash 264: `38d40cab09d44d5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242923`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p SELECT ALL min(CURRENT_DATE) AS vaena1etotf_ FROM p NOT INDEXED; VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 265: `0d966b3036fd9916` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245978`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p (rowid) VALUES (725.585268E8); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p; SELECT printf('%.
```

---

## Crash 266: `958caea3c0f858c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246162`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT 677034362501940493617103521721815208467046383715887860879712.45); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 267: `c7c88273d0bb3b39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246359`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT '-e-0 _---6-c7_Rj2'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TAB
```

---

## Crash 268: `271c503450c2b33f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246452`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT '-e-0 _---6-c7_Rj2'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*
```

---

## Crash 269: `8415baeca8f4a719` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247224`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB CHECK (json(TRUE))); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p WHERE CURREN
```

---

## Crash 270: `40d875eeb40b8860` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249261`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 
```

---

## Crash 271: `9baf3f656f04bae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249590`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c2 
```

---

## Crash 272: `5f340a42b68a71f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254850`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL LEFT JOIN p WHERE FALSE <= CURRENT_TIMESTAMP GROUP BY TRUE; SELECT printf('%.*e', 2147483647, 0.01); CREATE VIRTUAL TABLE 
```

---

## Crash 273: `44cdcde813a36955` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255478`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); SELECT * FROM (((((((((p NATURAL LEFT JOIN p) NATURAL LEFT JOIN p) NATURAL LEFT JOIN p) NATURAL LEFT JOIN p) NATURAL LEFT JOIN p) NATURAL LEFT JOI
```

---

## Crash 274: `92710b7d2a9346b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256443`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 275: `980361594c022b26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256919`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (FALSE) INTERSECT SELECT * FROM p WHERE FALSE GROUP BY rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 276: `6dac17dea5a97d64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257554`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL) INTERSECT SELECT * ORDER BY FALSE DESC NULLS LAST, CURRENT_TIME DESC NULLS LAST; INSERT INTO p VALUES (
```

---

## Crash 277: `a23583d0459ee079` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260202`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (json_array(NULL)); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---
