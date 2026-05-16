# Crash Triage Report

**Total crashes:** 159  
**Unique crash sites:** 159  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 159 | 159 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `b6a9307105c73ea8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000024`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%llu', 9223372036854775807, ' -F5 h _ 39l-eb-'); CREATE
```

---

## Crash 2: `0162fc03ca92ae8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000117`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, c2); WITH RECURSIVE p AS (SELECT * ORDER BY RAISE(IGNORE) ASC NULLS FIRST, FALSE NOT LIKE (RAISE(IGNORE)) ASC) INSERT INTO q VALUES ((N
```

---

## Crash 3: `067d414b1c8d1f25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000194`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT INTO q (a) VALUES (NOT CURRENT_DATE BETWEEN CURRENT_TIMESTAMP - CURRENT_DATE AND randomblob(CURRENT_TIME) || NULL << RAISE(IGNORE) L
```

---

## Crash 4: `e293011e0fd448fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000885`

```sql
SELECT printf('%.*e', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT OR FAIL INTO q VALUES (-NULL LIKE RAISE(IGNORE) ISNULL ESCAPE CURRENT_TIMESTAMP); ANALYZ
```

---

## Crash 5: `3ff76de2284a08e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000947`

```sql
SELECT printf('%llu', 2147483648, 'XKu_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q VALUES (CURRENT_DATE || TRUE % (CURRENT_TIME) IN (SELECT * FROM t3 NOT INDEXED WHERE 
```

---

## Crash 6: `8295a176f3d3d51a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001459`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VALUES (-NULL | CURRENT_DATE COLLATE NOCASE - CURRENT_DATE IS NOT RAISE(IGNORE) OR FALSE <> CURR
```

---

## Crash 7: `7ed3e335b99ee37b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001514`

```sql
SELECT round(0.01, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s (_rowid_, b, b, c2, b) VALUES (CASE +CURRENT_TIME WHEN NULL % NULL THEN -CURRENT_TIMESTAMP END REGEXP c3,
```

---

## Crash 8: `752fbfd1c5127c7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001614`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * LIMIT NULL; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 9: `ad930ab08a43d94e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001648`

```sql
SELECT printf('%.*s', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; CREATE TABLE IF NOT EXISTS p(b TEXT NOT NU
```

---

## Crash 10: `8b672d2a35eb9ccf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002747`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (EXISTS (SELECT CASE NULL WHEN -CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP NOTNULL ELSE R
```

---

## Crash 11: `cba808f9d97ead97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002775`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; C
```

---

## Crash 12: `6c2718af97c43953` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002848`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE T
```

---

## Crash 13: `4276bdd9f8333b81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002862`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIME);
```

---

## Crash 14: `2fd88f2531d5c6d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002892`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 15: `26ab4910b8f64344` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002910`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY, c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL IN
```

---

## Crash 16: `6812b5a8d5853575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003089`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); VALUES (-NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_TIME NOT NULL, q.* FROM q NATURAL JOIN q WHERE (SELECT -CURRENT_DATE = 
```

---

## Crash 17: `b54dab445477714c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003108`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_TIME NOT NULL, q.* FROM q NATURAL JOIN q WHERE (SELECT -CURRENT_
```

---

## Crash 18: `1b758d6f9b85f636` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003246`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 19: `813eb4c71209448e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004238`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT q.* FROM q NATURAL JOIN q WHERE +CAST(X'2C' AS INTEGER) OR +CASE WHEN CURRENT_TIMESTAMP THEN (CURREN
```

---

## Crash 20: `8331a2964805d224` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004493`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHERE +CURRENT_DATE;
```

---

## Crash 21: `f766eecd790f1ab0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005845`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; ANALYZE s; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `c31d0e46e8b22788` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005851`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 23: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007287`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 24: `46c271741310b0c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008169`

```sql
SELECT printf('%.*g', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, c1); SELECT *, * LIMIT ~+RAISE(IGNORE) ISNULL % NULL NOT LIKE FALSE IS DISTINCT FROM CURRENT_DATE B
```

---

## Crash 25: `b077f9aee6d23751` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011540`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p AS f LEFT JOIN q NOT INDEXED WHERE
```

---

## Crash 26: `2845db42c72c0a12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017330`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, a, a, a, a, c1); INSERT INTO t3 DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT hex(zeroblob(-1));
```

---

## Crash 27: `240b604e2ac4bcb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017373`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, a, a, a, a, a, a, a, a, c1); INSERT INTO t3 DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT hex(zeroblob(-1));
```

---

## Crash 28: `957431eb8a3fd1ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017462`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 29: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020004`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 30: `a65a0ba3a47909d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021413`

```sql
SELECT substr('  _ __', 0, 0); SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (CURRENT_DATE >= FALSE -> RAISE(IGNORE) > CURRENT_TIME IS NULL) STORED);
```

---

## Crash 31: `24c29b8dec52bd0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022056`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p 
```

---

## Crash 32: `f81606f39c7f0e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023493`

```sql
SELECT printf('%.*s', -2147483649); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 33: `2165f914288fd8cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023658`

```sql
SELECT printf('%.*d', 2147483647, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE);
```

---

## Crash 34: `99fe8bb9793b15dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024860`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST) AS e_j3csukbk__w
```

---

## Crash 35: `7d806ddff1f20fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027221`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT, a GENERATED ALWAYS AS (a || b) , c1 DATE DEFAULT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT 
```

---

## Crash 36: `f32494594e64a651` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027244`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT 1517435704091279973241760225511658007162362.07197698); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRT
```

---

## Crash 37: `770d1e85d00f2b3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027256`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB GENERATED ALWAYS AS (FALSE) STORED, c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SEL
```

---

## Crash 38: `876cd55a3d2a65fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027309`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (CURRENT_TIME)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN Q
```

---

## Crash 39: `bed0c3ed676ab049` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027372`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (CASE FALSE WHEN (TRUE) THEN CURRENT_TIME NOT BETWEEN NULL AND CURRENT_TIMESTAMP ELSE CURRENT_TIMEST
```

---

## Crash 40: `d261522c97fa80b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (RAISE(IGNORE) BETWEEN q._rowid_ AND TRUE), b DATE NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL 
```

---

## Crash 41: `7d7e987f3fd91fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029211`

```sql
SELECT printf('%.*s', -9223372036854775808); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 42: `de919dffff5da501` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030497`

```sql
SELECT round(-1.0, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 43: `a952ea4dab8e61b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031333`

```sql
SELECT substr('b_q7f-_ 7 --3d6id', 1, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); WITH p AS NOT MATERIALIZED (SELECT RAISE(IGNORE)) INSERT INTO t2 VALUES (+TRUE); ANALYZE
```

---

## Crash 44: `e9bb35c3c290d332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033120`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 45: `d9007c4d4b68728a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036614`

```sql
SELECT printf('%.*d', 1, -1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 46: `32cedda7304cd2d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041150`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERAT
```

---

## Crash 47: `3f25bbf5064bf88a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041920`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 48: `e654e7f04ed5b38f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042829`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 49: `6075a67da8e47f15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047583`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); SELECT * FROM (SELECT * FROM q WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 50: `452d3c3fed32a16f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048022`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT 'a-  B -- '); SELECT * FROM (SELECT * FROM q WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 51: `90fb2e6d6e24bc41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048623`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL); SELECT hex(zeroblob(-2147483
```

---

## Crash 52: `808134ea4963781b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050243`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT FALSE, c2 BOOLEAN GENERATED ALWAYS AS (NULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (~CURRENT_TIME); A
```

---

## Crash 53: `0199b5c50531fa52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050260`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (~CURRENT_TIME); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 54: `55ae2dc8146acac7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050266`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL, c2 BOOLEAN GENERATED ALWAYS AS (NULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (~CURRENT_TIME); ANALYZE p; C
```

---

## Crash 55: `039b1f8e116bbaeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050276`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT FALSE, c2 BOOLEAN GENERATED ALWAYS AS (NULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA in
```

---

## Crash 56: `f803b593d3cfca9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051159`

```sql
SELECT printf('%.*g', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT ALL *, *, * FROM q AS t7_ INNER JOIN p NOT INDEXED USING (c1, c3) ORDER BY TRUE <= CURREN
```

---

## Crash 57: `8242d4c91289e9b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051247`

```sql
SELECT substr('-_wR-_ - 069 _', 2147483647, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT q.* F
```

---

## Crash 58: `3eec448fda1bea82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051536`

```sql
SELECT printf('%.*d', 1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 (rowid) VALUES (p.rowid = json_extract(0, '_ Rq') ->> count(*) AND p.b NOT BETWEEN NULL IS DIS
```

---

## Crash 59: `1a1121467a9f97cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052415`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (TRUE) EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR 
```

---

## Crash 60: `5dd68100fb661601` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054152`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 61: `161c696b6764ae32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054313`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP >> FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 62: `924c78d20446a3d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054499`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP >> CURRENT_TIME == FALSE OR CURRENT_TIMESTA
```

---

## Crash 63: `01f404b78c6f8489` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054825`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT FALSE, c2 BLOB GENERATED ALWAYS AS (NULL) STORED); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); ANALY
```

---

## Crash 64: `9ac8d89ddaa1acf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055058`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); VALUES (NULL) UNION VALUES (X'A89a'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK
```

---

## Crash 65: `81664e6160a80af7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055209`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); VALUES (NULL) UNION VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK IN
```

---

## Crash 66: `f515559a39407264` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055216`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); VALUES (NULL) UNION VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK IN
```

---

## Crash 67: `18e2a2fe17603e09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056336`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT X'' AS a FROM q NOT INDEXED WHERE TRUE UNION VALUES (CURRENT_TI
```

---

## Crash 68: `8a40a0857e45e1bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058579`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM q WHERE X'A89a') AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 69: `7fa0abbeae1cc087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () AS a FROM (SELECT * FROM q WHERE NULL) AS sub1;
```

---

## Crash 70: `5ba9d1a94cb1be0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060365`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO 
```

---

## Crash 71: `b69da85dfc55c240` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062028`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT 
```

---

## Crash 72: `49e57da284f1e939` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062224`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a + -60723) UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSE
```

---

## Crash 73: `8a6bb3ffa359183b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065983`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 74: `5281365223d83333` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066159`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zero
```

---

## Crash 75: `3e4a3c225d3acd06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066169`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zero
```

---

## Crash 76: `4841d775d4e4efc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066209`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zero
```

---

## Crash 77: `1b3b918ba3d6fd67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066365`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a) UNIQUE, a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF
```

---

## Crash 78: `f49fefc2d25ec90a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067975`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 79: `3cbaea43b2f9d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068163`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); 
```

---

## Crash 80: `e9d6c9f1df8cabf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068667`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BOOL
```

---

## Crash 81: `d4e1a2762eb20887` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068966`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERAT
```

---

## Crash 82: `f32743d30ecf1680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069522`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 83: `86bcf0459a099890` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070365`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); SELECT json_valid(CURRENT_TIME) AS j53_o1_ FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 84: `a7f4c3ac4136d64f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070650`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); SELECT last_insert_rowid() AS j53_o1_ FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 85: `0de4867c35742616` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071020`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); SELECT json_valid(-0.48) AS j53_o1_ FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 86: `5b3f26b381b19d60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074220`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT 1517435704091279973241760225511658007162362.07197698); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 87: `49a301bd960c7236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074584`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT X'3D'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 88: `764c1d95106c881e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074597`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 89: `6ff52a32d13b4b79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074641`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); 
```

---

## Crash 90: `cacb5de5e308c03e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074674`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL)
```

---

## Crash 91: `5664008e85873547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076006`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT -2668256961210407529.15); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT
```

---

## Crash 92: `b8884c41b9823cba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079214`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 DATE PRIMARY KEY); INSERT INTO p (b) VALUES (CURRENT_TIMESTAMP) ON CONFLICT(rowid) DO UPDATE SET _rowid_ = CURRENT_TIME; EXPLAIN Q
```

---

## Crash 93: `8f3eee4ec9bc6893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080689`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (FALSE IS NOT _rowid_)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 94: `696d69e092d1cb1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081761`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 95: `3589b75e606a2047` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081767`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (FALSE IS NOT CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 96: `7ff79bcd2e587392` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081817`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 97: `904069eb70a71e90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081915`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT substr('--_-J_O_6 k', -9223372036854775808); CREATE VIRTU
```

---

## Crash 98: `eb350a7d267a70cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084599`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT -236047284.211250434019965941024462171635986268107266995384038394793371352935542527966680767399655e-9); INSERT INTO p DEFAULT VALUES; PRAGMA in
```

---

## Crash 99: `9902deb49af56b17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086560`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 100: `29f1df95d84d8365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086746`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 101: `8be9c534ee089fd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089036`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL DEFAULT -890); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); EXPLAIN Q
```

---

## Crash 102: `5fb4d7ef8ce69c7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089056`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL) UNION SELECT ALL FALSE FROM p ORDER BY FALSE COLLATE BINARY ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 103: `0a9b922a77062cc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089085`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); INSERT OR IGNORE INTO q VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE V
```

---

## Crash 104: `20f52b0964fc9bec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089172`

```sql
SELECT substr('__4__s5-  1--', 2147483648, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 105: `d790143147e46cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090988`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT CURRENT_TIME LIKE TRUE ESCAPE NULL, * FROM p NATURAL JOIN q WHERE ~NULL; CREATE VIRTUAL TABLE
```

---

## Crash 106: `9cd5d584bd1edb42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091172`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT 24586.53E+433569099328669620499 || CURRENT_TIME IS NULL, * FROM p NATURAL JOIN q WHERE NULL; 
```

---

## Crash 107: `deada1df585e42a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091383`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT NULL IS NULL, * FROM p NATURAL JOIN q WHERE NULL; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 108: `6a0950b4931a6dc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091389`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT CURRENT_TIME || CURRENT_TIME IS NULL, * FROM p NATURAL JOIN q WHERE NULL; SELECT printf('%.*f
```

---

## Crash 109: `3c6fc2230e963b61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093246`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT '-_Kk lm7 -1--'); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE FALSE; SELECT printf('%.*g', 2147483647, 
```

---

## Crash 110: `1d4adb28fde59461` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093920`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT 649677108283044473359601282118937649867584765827200247794017127797881386587159005586785152045013205.974411948
```

---

## Crash 111: `375ebc949cd83611` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094065`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 112: `1ee2079e36892cf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094072`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT CURRENT_DATE); SELECT * FROM p NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 113: `6d512f906da01ac6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094625`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT *, count(*) OVER () AS e_j3csukbk__w__r1u1_i7yq_9on1r1_t57gx_24_j_03b6apdy8__7df71_0_qj13__9o
```

---

## Crash 114: `2ebd9c17125ae0c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095624`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME OR FALSE; SELECT printf('%.*f', 2147483647, 1e308)
```

---

## Crash 115: `b70fa7ffc0a5f8b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096378`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE IN (NULL); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 116: `2a91d4b3d2ae3009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096559`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE, b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 117: `81a19db2944156f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096788`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE 
```

---

## Crash 118: `828c97979f2caeff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097135`

```sql
SELECT round(0.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; SELECT hex(zeroblob(-922337203685477
```

---

## Crash 119: `cf521ed96fec4954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097613`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p NATURAL JOIN p AS a WHERE TRUE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 120: `58575ca52ee51930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101956`

```sql
SELECT printf('%f', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (-NULL, NOT EXISTS (SELECT *, FALSE UNION SELECT +CURRENT_TIMESTAMP COLLATE B
```

---

## Crash 121: `dca086d3177394e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102649`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ABORT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL LEFT JOIN p WHERE CURR
```

---

## Crash 122: `fb97e3772b230b23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106980`

```sql
SELECT substr('--__-lm4-132 iC', 9223372036854775807, -1); SELECT substr('- U -_1 L_ _', 4294967295, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALUES (FALSE
```

---

## Crash 123: `7b5cf54fb9f8b8e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115538`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE); EXPLAIN QUERY PLAN SELECT ALL * FROM p NATURAL JOIN p NOT INDEXED ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL
```

---

## Crash 124: `a2e8459776b957ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115980`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE); EXPLAIN QUERY PLAN SELECT ALL * FROM p NATURAL LEFT JOIN p ORDER BY FALSE IS CURRENT_DATE COLLATE BINARY ASC NU
```

---

## Crash 125: `bd3704e1cdc4535b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116120`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_DATE COLLATE NOCASE IS CURRENT_DATE ASC NULLS LAST; SEL
```

---

## Crash 126: `4d311d49edfe30ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116982`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY NULL / CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 127: `809722ad860b28f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117908`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT -236047284.211250434019965941024462171635986268107266995384038394793371352935542527966680767399655e-9); CREATE TABLE IF NOT EXISTS q(c3 INT PRI
```

---

## Crash 128: `28df38aec65b79bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118093`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN WITH t2 AS (SELECT *) SELECT DISTINCT * FROM p WHERE TRUE; CREATE VIRTUAL T
```

---

## Crash 129: `ae8e233cf1685e2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118613`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE NOT LIKE CURRENT_TIME GROUP BY CURRENT_TIME WI
```

---

## Crash 130: `dea423eafd9d499f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120295`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (+CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM q WHERE TRUE; CREATE VIRTUAL T
```

---

## Crash 131: `29026b9988ac9b34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120616`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); INSERT OR REPLACE INTO p VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 132: `6020f57f1ba42450` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120909`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p NOT INDEXED INNER JOIN q NOT INDEX
```

---

## Crash 133: `2470235d0144f08b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121365`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM q WHERE CURRENT_TIMESTAMP < TRUE; SE
```

---

## Crash 134: `a1a00ca697123576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121636`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM q WHERE TRUE LIKE FALSE ESCAPE CURRE
```

---

## Crash 135: `9a5aaeec60376143` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122221`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT FALSE = CURRENT_TIME % FALSE IS NOT FALSE C
```

---

## Crash 136: `82ceda8749e40a42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124003`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p AS f LEFT JOIN q NOT INDEXED WHER
```

---

## Crash 137: `f1afc8cd80ea2060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125025`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (WITH q AS (VALUES (CURRENT_DATE)) SELECT DISTINCT TRUE - NULL % NOT FALSE AS a FRO
```

---

## Crash 138: `7d0c59a364a454c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125393`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (WITH q AS (VALUES (CURRENT_DATE)) SELECT DISTINCT TRUE - NULL % NOT FALSE IS NOT F
```

---

## Crash 139: `474a2bfa513c48d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125960`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM q AS f LEFT JOIN q NOT INDEXED WHERE TRUE; SELECT printf('%.*f', 2
```

---

## Crash 140: `447578b0b1a66ed9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128648`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL LEFT JOIN p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY NU
```

---

## Crash 141: `e274858c75b76b2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130112`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q (c3) AS (WITH q (c3) AS (VALUES (CURRENT_TIME)) SELECT DISTINCT CURRENT_DATE IN (TRUE)
```

---

## Crash 142: `666d0865f539f537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137046`

```sql
SELECT printf('%.*g', 4294967295, 1e-308); SELECT substr('1- K-93i-0 y', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES (coalesce(NOT EXISTS (SE
```

---

## Crash 143: `93d96766d61cbf9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137177`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; ANALYZE s; CREATE TABLE IF NOT EXISTS p(rowid NUMERIC DEFAULT CURRE
```

---

## Crash 144: `c5aa690f2460907e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137406`

```sql
SELECT substr('__- ', 2147483648); SELECT round(0.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CURRENT_TIME NOT IN (NULL), CURRENT_TIMESTAMP IS NOT
```

---

## Crash 145: `19689691e30642f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138528`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (X'A89a' OR CURRENT_DATE); VALUES (CURRENT_DATE); SELECT printf('%.*f', 214748364
```

---

## Crash 146: `c90ba45acbbc6214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138741`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME OR CURRENT_DATE); VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147
```

---

## Crash 147: `4aec4b4d868ff0ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138747`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE OR CURRENT_DATE); VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147483647,
```

---

## Crash 148: `277efe49eb9923d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139075`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM q AS f NATURAL JOIN (q NATURAL 
```

---

## Crash 149: `1562ccbd765c55e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139173`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM q AS f NATURAL JOIN (q NOT INDE
```

---

## Crash 150: `d7e7f5614226bc49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143912`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q (c3) AS (SELECT ALL * FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST) S
```

---

## Crash 151: `e5acdbf01830642f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144153`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT CURRENT_TIME, NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 152: `7116784056c627d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144259`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 153: `f2f968405a1c1f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144334`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (SELECT DISTINCT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST RO
```

---

## Crash 154: `79c1c6c8c06a887c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144432`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (SELECT DISTINCT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST RO
```

---

## Crash 155: `edeed6a33fbd89e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144510`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH RECURSIVE p AS (VALUES (TRUE)) SELECT DISTINCT * FROM p NOT INDEXED LEFT JOIN q NOT INDE
```

---

## Crash 156: `f9c0f7934ad85118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144520`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (SELECT DISTINCT * FROM p NOT INDEXED ORDER BY NULL ASC NULLS FIRST LIMIT
```

---

## Crash 157: `0d9dc808adf6e769` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144526`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (SELECT DISTINCT *, * FROM p NOT INDEXED ORDER BY NULL ASC NULLS FIRST LI
```

---

## Crash 158: `a1dc343d012eeca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144557`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT count(*) FILTER (WHERE CURRENT_DATE) F
```

---

## Crash 159: `5afa94f5226e594d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146011`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); EXPLAIN QUERY PLAN WITH q AS (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM p AS f LEFT JOIN q NOT INDEXED WHERE
```

---
