# Crash Triage Report

**Total crashes:** 59  
**Unique crash sites:** 59  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 59 | 59 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `420d3f62b2073891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000256`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT INTO p VALUES (last_insert_rowid() IN (CURRENT_TIMESTAMP NOT NULL COLLATE RTRIM) > TRUE < RAISE(IGNORE) COLLATE RTRIM NOT LIKE TRUE 
```

---

## Crash 2: `d64b2cbcb074bfe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000463`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (a, c1) VALUES (NULL NOTNULL IS NOT DISTINCT FROM NULL | 75.78 <> (NULL IS NULL NOTNULL < (CAST(FALSE 
```

---

## Crash 3: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000666`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 4: `0d903f99a9617972` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000925`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c3, c2, a, c2); SELECT CASE CAST(NULL AS VARCHAR(255)) COLLATE NOCASE WHEN CURRENT_TIME THEN RAISE(IGNORE) IN (VALUES (RAISE(IGNORE) COLLAT
```

---

## Crash 5: `680c592fda24f01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001093`

```sql
SELECT printf('%.*s', -2147483648, 1e308); SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP ISNULL) LI
```

---

## Crash 6: `07221997bfadc818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001195`

```sql
SELECT printf('%.*e', 2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (c2, c2) VALUES (CASE WHEN total_changes() REGEXP (+CURRENT_TIME < RAISE(IGNORE) | RAISE(
```

---

## Crash 7: `631d10e76e99329d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001445`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NOT CAST((EXISTS (VALUES (CURRENT_DATE, NULL) INTERSECT SELECT ALL * FROM p INDEXED BY c3)) AS INT), 
```

---

## Crash 8: `85531eba4b742d78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004842`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE, c3 NUMERIC UNIQUE, _rowid_ INT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); SEL
```

---

## Crash 9: `575eea72ca923293` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004855`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); SELECT DISTINCT * FROM json_each('[{"a"
```

---

## Crash 10: `3aaaab9c628e869c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004861`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2
```

---

## Crash 11: `b1fa97efee5c849b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007856`

```sql
SELECT round(0.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2); EXPLAIN QUERY PLAN SELECT TRUE >> FALSE == CURRENT_TIME AND TRUE NOTNULL AS uue_pt, TRUE NOT N
```

---

## Crash 12: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008039`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 13: `879d76fa62b3b1b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008266`

```sql
SELECT substr('', 9223372036854775807, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO s VALUES (NULL IS NOT CASE NOT EXISTS (SELECT *, CURRENT_DATE << p.a 
```

---

## Crash 14: `f0dccde6fe92ce7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015317`

```sql
SELECT printf('%.*d', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT r.*, TRUE IS NULL AS a, p.* FROM q NATURAL JOIN p WHERE NOT TRUE - FALSE LIKE (CURRENT_DATE
```

---

## Crash 15: `8ba59b81ee1eb6b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021906`

```sql
SELECT printf('%f', 4294967295, ''); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 16: `b71891d705a8e2bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023620`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT CASE WHEN CURRENT_TIMESTAMP >> CURRENT_DATE IS DISTINCT FROM RAISE(IGNOR
```

---

## Crash 17: `fcf8bdae78c5f485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023648`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT CASE WHEN CURRENT_TIMESTAMP >> CURRENT_DATE IS DISTINCT FROM RAISE(IGNOR
```

---

## Crash 18: `163d85b277af2e7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026197`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c3, c3); SELECT percent_rank() OVER (ORDER BY ~NULL DESC) COLLATE NOCASE NOT BETWEEN TRUE NOTNULL
```

---

## Crash 19: `377689b26fb2762f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033706`

```sql
SELECT printf('%u', 2147483647, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c3, c3); SELECT p.*, q.*, CURRENT_TIME ->> CURRENT_TIMESTAMP < CURRENT_DATE ISNULL AND CURRENT_TIME COL
```

---

## Crash 20: `24da9dc8d7df8481` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035587`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN WITH s AS (SELECT *) VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VAL
```

---

## Crash 21: `c969040dd19ffe9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043909`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c1); R
```

---

## Crash 22: `91cd9fba3dce6fab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047165`

```sql
SELECT printf('%.*d', 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 23: `9fbced05547feff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047340`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, b, a, c3, _rowid_, c1); SELECT CURRENT_TIME NOT NULL & CASE WHEN CURRENT_TIME THEN ~NULL END, RAISE(IGNORE) / CURRENT_TIME COLLATE NOCA
```

---

## Crash 24: `6c28f10894384823` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050336`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 25: `1794a7a9dfb3f952` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055225`

```sql
SELECT printf('%x', 4294967296, '7 8Q--wD -0_l_lwY_K'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 26: `ca11b0b72a7046b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055889`

```sql
SELECT printf('%f', -9223372036854775808, 'Q -_'); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 27: `700f2ce499d41290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059325`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 28: `2f18400b79ead036` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060239`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP < CURRENT_TIME); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 29: `f74c20f8403b3b12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062005`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 30: `d63aae2bf5bd6e2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062727`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT DISTINCT CURRENT_DATE LIKE CURRENT_DATE ESCAPE FALSE FROM p WHERE TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 31: `829dec4ca0d10391` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065978`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') NATURAL JOIN
```

---

## Crash 32: `c12da2c5a20014d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066165`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 33: `a0cc6fd126a196bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066174`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('{}') WHERE CURRENT_TIMESTAMP GROUP BY CU
```

---

## Crash 34: `28bbd1d92a9609e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066726`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 35: `114618ae9f4214f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070558`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 36: `28c10acd94436715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070875`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL
```

---

## Crash 37: `883f98c4a28831b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076520`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (NULL IS NULL < CURRENT_DATE); VALUES (TRUE); SELECT printf('%.*f', 2147483
```

---

## Crash 38: `61d4d17c5ae78781` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076904`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (json_quote(NULL)); VALUES (TRUE); SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 39: `35134e1c5b5c2455` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079319`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (FALSE IN (CURRENT_TIMESTAMP < (FALSE IN (CURRENT_TIMESTAMP < TRUE NOTNULL)
```

---

## Crash 40: `8c20cfc54a2709fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079360`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (FALSE IN (NULL) NOTNULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 41: `353ac4973809c330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (FALSE IN (CURRENT_TIME) NOTNULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 42: `54439ea4146a3b91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096486`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE)) SELECT * FROM t3; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 43: `7eb9409bdcf4e0c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097183`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (SELECT DISTINCT *, * FROM json_tree('{}')) SELECT * FROM t3; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `a2bd5e4bcbd8ce80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097656`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (SELECT DISTINCT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS v6k980_31xoh_r_n1_50_3_n20ezd7_k5__8i32_bn3i1
```

---

## Crash 45: `ddd9fc529403a6e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097795`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (SELECT DISTINCT CURRENT_TIMESTAMP FROM json_each('{"a":1}') WHERE NULL) SELECT * FROM t3; SELECT printf('%.*f', 21
```

---

## Crash 46: `d515fdaa7bbc3fdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098989`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (VALUES (count(*) FILTER (WHERE NULL) OVER (), NULL)) SELECT * FROM t3; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 47: `c4027b92e49d434c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099457`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); WITH RECURSIVE t3 AS (VALUES (count(*) FILTER (WHERE NULL) OVER (ORDER BY TRUE DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CUR
```

---

## Crash 48: `e4fac0fe01a01495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103381`

```sql
SELECT printf('%.*g', -2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO p VALUES (lag((VALUES (TRUE != TRUE)) NOT LIKE CAST(CURRENT_TIME AS FLOAT) NOT 
```

---

## Crash 49: `3ab00418e8c293ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111625`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT typeof(CASE WHEN typeof(CURRENT_TIMESTAMP) THEN TRUE END AND NULL) FROM p; SELECT printf('%.*f'
```

---

## Crash 50: `a378b376f3546a01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112217`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT _rowid_ FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 51: `5bad2b1ff82696ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112808`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT count(*) GLOB NULL * -CURRENT_TIMESTAMP FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 52: `9cfb7228e73c1fbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113415`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT CURRENT_TIME GLOB TRUE FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 53: `77f34cdb186a4922` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113572`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT * FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 54: `025337064aa4a4bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113905`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT count(*) FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 55: `364ef976fc8473b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114149`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT count(*) FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 56: `b4fa993a5cd41d71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114918`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_DATE)) SELECT dense_rank() OVER () GLOB CURRENT_TIME FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 57: `59ddaf11c2033779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116667`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); WITH RECURSIVE t1 (c2) AS (VALUES (CURRENT_TIMESTAMP)) SELECT TRUE GLOB TRUE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, a
```

---

## Crash 58: `30298fbe22faa96f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139066`

```sql
SELECT printf('%.*e', 4294967296, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT zeroblob(total_changes()), CURRENT_TIMESTAMP NOTNULL FROM p NATURAL JOIN q WHERE FALSE; CREA
```

---

## Crash 59: `edd41be3a091ff8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147666`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q (c3, c1, b) VALUES (CURRENT_TIMESTAMP NOT BETWEEN (VALUES (TRUE) LIMIT CURRENT
```

---
