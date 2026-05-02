# Crash Triage Report

**Total crashes:** 50  
**Unique crash sites:** 50  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 50 | 50 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d558acf254a0ce91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000219`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE INDEX IF NOT
```

---

## Crash 2: `8a1825b67f483726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000445`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); VALUES (CASE CASE WHEN ~~TRUE + TRUE THEN RAISE(IGNORE) NOT IN (RAISE(IGNORE)) < FALSE || NULL IS NULL LIKE NULL ELSE FALSE END WHEN CURRE
```

---

## Crash 3: `b103eadafeaad72f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000541`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT -RAISE(IGNORE) AND CURRENT_TIME IN (CURRENT_TIME) COLLATE BINARY AS be1dbm__6c22_s285124svuv1_
```

---

## Crash 4: `77066b052c2fc8cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000724`

```sql
SELECT substr('_-_- _lz_ -', -2147483648, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, a); REPLACE INTO p VALUES (CURRENT_TIME, FALSE); EXPLAIN QUERY PLAN SELECT RAISE(IGN
```

---

## Crash 5: `7258ec22f9866459` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000945`

```sql
SELECT substr(' ---', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_TIME; CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT CU
```

---

## Crash 6: `748ab8f9d5dee7a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001272`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); VALUES ((CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO p 
```

---

## Crash 7: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001455`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 8: `6d6f0980df4c1149` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001516`

```sql
SELECT printf('%.*d', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT *; CREATE TABLE IF NOT EXISTS p(a BLOB GENERATED ALWAYS AS (CURRENT_DATE COLLATE 
```

---

## Crash 9: `e83713319354ff53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002072`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIMESTAMP != NOT NULL IS NULL AS 
```

---

## Crash 10: `093e2739f8107fc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002738`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO p VALUES (NULL >= CAST(CURRENT_TIME / CURRENT_TIMESTAMP AS BOOLEAN) || CURRENT_DATE 
```

---

## Crash 11: `2896bb45dd544411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002984`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE q (rowid, c3) AS NOT MATERIALIZED (SELECT RAISE(IGNORE) AS t9_7_s3_rjus__l0jqs_x4nbqn62o0__6
```

---

## Crash 12: `2b6cb9667524a110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003014`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE COLLATE NOCASE << CURRENT_TIME, CASE WHEN RAISE(IGNORE
```

---

## Crash 13: `5fe310229917f99c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003381`

```sql
SELECT printf('%.*f', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO t3 VALUES (EXISTS (VALUES (RAISE(IGNORE)) ORDER BY CURRENT_DATE ASC NULLS FIRST LIMIT RAISE(IG
```

---

## Crash 14: `1b8f38d08ca1f5d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004821`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL)); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS 
```

---

## Crash 15: `3961ebec1432ce6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004836`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MATE
```

---

## Crash 16: `c7f374c4c749678f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004842`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MAT
```

---

## Crash 17: `b93abedcaae05dee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004848`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MATERIA
```

---

## Crash 18: `a3b5b96ab15a900c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004854`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MATERIALIZED (WIT
```

---

## Crash 19: `6613e1560057ed3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004866`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MATERI
```

---

## Crash 20: `3b772021dcfa5117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004872`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r AS MATERIALIZED (WITH p
```

---

## Crash 21: `71a43f2ef83b8bbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006651`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 22: `c2f38452656efc1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007148`

```sql
SELECT substr('e m8_0', 2147483647, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT q.*, * FROM q JOIN r a ON json_valid((CURRENT_TIMESTAMP COLLATE RTRIM <> NOT CASE CURRENT_DATE 
```

---

## Crash 23: `f2860fe83dbd8df6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007245`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c2, c3, _rowid_, c2, c3, c2); INSERT INTO q VALUES (CASE FALSE COLLATE NOCASE WHEN b || TRUE IS CURRENT_DATE < FALSE >= RAISE(IGNORE) NOT NU
```

---

## Crash 24: `bbddeb5eb09010e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007313`

```sql
SELECT round(0.01, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT OR IGNORE INTO p VALUES ((RAISE(IGNORE) COLLATE BINARY == FALSE REGEXP last_insert_rowid() 
```

---

## Crash 25: `9869bd2cc810880d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007427`

```sql
SELECT printf('%.*e', 4294967296, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO t1 VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT
```

---

## Crash 26: `1bb65a6adec181a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007456`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (b) VALUES (NULL); WITH RECURSIVE q 
```

---

## Crash 27: `9bc7fe3e5cbb8978` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007982`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT r.* EXCEPT SELECT * FROM q INDEXED BY c1 WHERE CURRENT_TIME NOTNULL + (last_insert_rowid()) COLLATE 
```

---

## Crash 28: `fa597ab4751d4e4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008025`

```sql
SELECT substr('', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO q VALUES (nullif(CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME ELSE CURRENT_DATE END, TRUE IS NOT NUL
```

---

## Crash 29: `1dd957566054c03e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008109`

```sql
SELECT substr('w 7 __t2_', 2147483647, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_TIME ISNULL FROM p NATURAL JOIN p WHERE (NULL IS NOT DISTINCT FROM CURRENT_TIME); CRE
```

---

## Crash 30: `443c8aa55e468463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008121`

```sql
SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); SELECT p.* FROM q WHERE EXISTS (SELECT t2.* FROM p AS a LEFT JOIN ((p INNER JOIN (p NATUR
```

---

## Crash 31: `1f82725918386a79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009907`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 32: `70726f1d71b909f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010308`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 33: `0b802303a2eaf653` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010323`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 34: `d8d85f73b82d7234` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019555`

```sql
SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, b, c1); INSERT INTO t1 VALUES (CASE WHEN substr(NULL LIKE TRUE OR CURRENT_DATE ESCAPE CURRENT_DATE -> CUR
```

---

## Crash 35: `278b00bb51d5cb09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019865`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEF
```

---

## Crash 36: `4bd88fcfc8f9187c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020213`

```sql
SELECT substr('', 1, 4294967295); SELECT substr('', 4294967296, -9223372036854775808); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 37: `fdb3952d5261b84f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021794`

```sql
SELECT printf('%.*g', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 38: `2d42c29116996c8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021902`

```sql
SELECT printf('%.*d', 1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT OR ABORT INTO q VALUES (RAISE(IGNORE), count(*) FILTER (WHERE CURRENT_TIME) OVER ()); SELECT CURREN
```

---

## Crash 39: `af552d475eacc7ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 40: `83734a5ee1653a44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025070`

```sql
SELECT printf('%.*s', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, a, c2); SELECT p.* FROM p WHERE EXISTS (SELECT DISTINCT p.* FROM p AS ib6_2__349_mj__h2sh_k7_v23_8stl55d79__
```

---

## Crash 41: `2ac412e966cf9937` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025763`

```sql
SELECT round(0.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT p.* FROM p JOIN p bo7f8__9_ ON (random() FILTER (WHERE TRUE IS FALSE NOT NULL == NULL) OVER (ORDER BY CU
```

---

## Crash 42: `bf26817d6026fcd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027252`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE VIRTUAL 
```

---

## Crash 43: `af5ab89da479b89d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028863`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (FALSE) VIRTUAL, c1 INTEGER CHECK (CURRENT_TIME), rowid TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); REPLACE INTO 
```

---

## Crash 44: `e8778a95e3137414` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029007`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (FALSE) VIRTUAL, c1 INT UNIQUE, rowid TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 45: `bd1d1562c9adb35d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029319`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (NULL) VIRTUAL, _rowid_ VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 46: `b5ab6f5405b4b154` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031050`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 47: `b8f44af63e7d41c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036726`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c2); VALUES (TRUE, FALSE IS NULL) INTERSECT SELECT TRUE LIKE CURRENT_TIME ESCAPE CURRENT_DATE NO
```

---

## Crash 48: `5cfa6c3062542ff3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037712`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (c1) VALU
```

---

## Crash 49: `1ca9072ada77f1b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040179`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 50: `6eb8a0d172ae28cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040687`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (FALSE IN (CURRENT_TIMESTAMP)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---
