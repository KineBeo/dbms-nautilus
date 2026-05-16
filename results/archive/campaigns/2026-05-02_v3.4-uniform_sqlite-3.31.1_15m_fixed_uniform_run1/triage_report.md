# Crash Triage Report

**Total crashes:** 139  
**Unique crash sites:** 139  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 139 | 139 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `cee3ae034b77876f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000272`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, c2, a); SELECT RAISE(IGNORE) IN (SELECT TRUE) == abs(FALSE) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIME) NOT IN (FALSE 
```

---

## Crash 2: `6abad443142946ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000364`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c1, c2); SELECT NOT random() NOT LIKE NOT NULL < EXISTS (WITH p AS MATERIALIZED (VALUES (TRUE)) SELECT *) NOT NULL -> json_object('Mdu_
```

---

## Crash 3: `6736665f7384294c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000675`

```sql
SELECT substr('_v_5zI__VX6a', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; ANALYZE r; CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERA
```

---

## Crash 4: `a76c1a4bbe409b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000944`

```sql
SELECT round(-1.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT OR ROLLBACK INTO q VALUES (CASE RAISE(IGNORE) WHEN ++(TRUE) >> TRUE IS NOT NULL AND CASE WHEN -RAIS
```

---

## Crash 5: `5188051122b9a27b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001202`

```sql
SELECT printf('%.*g', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CASE RAISE(IGNORE) WHEN FALSE THEN CURRENT_TIME ELSE lower(RAISE(IGNORE)) END NOT NULL NOT IN (SELECT DISTINC
```

---

## Crash 6: `2bc5958802730e26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001481`

```sql
SELECT round(0.01, 4294967295); SELECT printf('%.*f', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (~NULL -> FALSE NOTNULL >> CURRENT_TIMESTAMP >= NULL NOT BETWEEN
```

---

## Crash 7: `bf30b330aa46cf56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001523`

```sql
SELECT printf('%s', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CAST(CURRENT_TIME >= CURRENT_DATE = TRUE COLLATE BINARY AS TEXT) NOT LIKE CASE CASE WHEN CURRENT_T
```

---

## Crash 8: `4a0d51a186605d64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001565`

```sql
SELECT substr('d _f 84z j-  f-_YoB', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c3, c1); WITH RECURSIVE p AS NOT MATERIALIZED (SELECT * FROM p NOT INDEXED WHERE TRUE LIMI
```

---

## Crash 9: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001601`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 10: `56efed464993a7fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003168`

```sql
SELECT substr('', -2147483648, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE t3 AS NOT MATERIALIZED (SELECT DISTINCT CURRENT_DATE -> CURRENT_DATE AS t_ FROM t2 
```

---

## Crash 11: `35193279362770c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003353`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p JOIN t2 u3 ON sum(count(*) OVER ()) FILTER (WHERE +CURRENT_TIMESTAMP) OVER () * CURRENT_DATE / CURREN
```

---

## Crash 12: `eb5306785cf836c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004069`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT 8.3); INSERT INTO p DEFAULT VALUES; SELECT *, * FROM (SELECT CURRENT_TIMESTAMP LIKE TRUE FROM p WHERE CURRENT_TIMESTAMP <> +CURRENT_TIMESTAMP) AS sub1; 
```

---

## Crash 13: `d38a04df831e99ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004379`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT s.* UNION ALL VALUES (NULL COLLATE NOCASE) ORDER BY FALSE BETWEEN last_insert_rowid() AND FALSE NOTNULL IS NUL
```

---

## Crash 14: `6bebcaf40b297534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004622`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) EXCEPT VALUES (RAISE(IGNORE))); CREATE TABLE I
```

---

## Crash 15: `95f67341c37f7838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005136`

```sql
SELECT round(1.0, 4294967295); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CASE NULL WHEN -NULL THEN CURRENT_DATE << TRUE ELSE 
```

---

## Crash 16: `733d2099ba00a35d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005229`

```sql
SELECT round(1.0, 4294967295); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 17: `c1b60320663cb94b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005513`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO q VALUES (q.c2, CASE WHEN -RAISE(IGNORE) THEN NULL ELSE (VALUES (FALSE)) REG
```

---

## Crash 18: `32fb220c75596348` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005551`

```sql
SELECT printf('%.*f', 2147483647, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT t2.* FROM p , q NOT INDEXED WHERE total_changes() FILTER (WHERE CURRENT_DATE
```

---

## Crash 19: `8d62b38cad202e6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005613`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS (PARTITION BY CURRENT_TIME, CURRENT_DATE CO
```

---

## Crash 20: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007239`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 21: `3631a791d4cf3df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007251`

```sql
SELECT printf('%.*f', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); WITH RECURSIVE t1 (c2) AS NOT MATERIALIZED (SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () AS qo FROM p
```

---

## Crash 22: `042b4e957cea5f26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007353`

```sql
SELECT round(1e308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q (c1) VALUES (CURRENT_DATE LIKE ~FALSE, CURRENT_DATE) ON CONFLICT(rowid) DO UPDATE S
```

---

## Crash 23: `ff7521b50bac809f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007748`

```sql
SELECT printf('%.*g', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM t1 NOT INDEXED WHERE CURRENT_DATE GROUP BY RAISE(IGNORE) WINDOW w1 AS () LIMIT CURRENT_TIMESTAM
```

---

## Crash 24: `0edcce00899f5315` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007856`

```sql
SELECT printf('%.*d', 9223372036854775807, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r DEFAULT VALUES; ANALYZE r; SELECT printf('%.*g', -1, 1.0);
```

---

## Crash 25: `eed2bf22e73e5034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013989`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT count(CURRENT_TIMESTAMP / TRUE -> -TRUE > RAISE(IGNORE) COLLATE RTRIM), TRUE ISNULL LIKE (VALUES (N
```

---

## Crash 26: `eec864288fde73ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018054`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP IS NOT CURRENT_TIMESTAMP) AS sub1; SELECT pri
```

---

## Crash 27: `86c785d9b4d71b43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018395`

```sql
SELECT printf('%.*d', 0, -1e308); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 28: `b95a7d1578ba47ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019097`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); INSERT INTO t2 DEFAULT VALUES; SELECT q.*, 'N- G - 3b' COLLATE NOCASE FROM t2 WHERE EXISTS (SELE
```

---

## Crash 29: `7fbc66b3acd2b545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019661`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NUL
```

---

## Crash 30: `0e648ac64258bced` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019671`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NUL
```

---

## Crash 31: `62d83f2c676baf3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020126`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUE
```

---

## Crash 32: `afcac96760c0b03f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020626`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE << TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT q.*, C
```

---

## Crash 33: `ad8ec24aa1a562f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022360`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROL
```

---

## Crash 34: `fc329acc91ac1725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024683`

```sql
SELECT printf('%.*f', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 35: `c4522ee28f2af7f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024904`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTU
```

---

## Crash 36: `33f6ef370c10aa01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026774`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT 8.3); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP <> CURRENT_TIME) AS sub1; SELECT printf('%.*f', 2147483647, 1
```

---

## Crash 37: `be1216e15d82e105` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027704`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP <> TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 38: `cd67d954a3ac9521` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027930`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 39: `fa5b70c3f62d5cd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028044`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT TRUE FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 40: `0121ad32458bc096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030296`

```sql
SELECT printf('%.*s', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 41: `3ea03b48b5750e06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032196`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO
```

---

## Crash 42: `1510428371079ec9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032812`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK IN
```

---

## Crash 43: `512c2f4410fd1495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034163`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 44: `2bd0d798a0e626e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039179`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 45: `e5c51e0c3b37ebed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039449`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); INS
```

---

## Crash 46: `2a8af59dcf6ceb28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039859`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 47: `3b65ad49474e4457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040005`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(ze
```

---

## Crash 48: `306fed20ac698422` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040013`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(ze
```

---

## Crash 49: `8b87fd0463a884b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040024`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(ze
```

---

## Crash 50: `475a10cbdc6ffdcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040936`

```sql
SELECT printf('%f', -2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 51: `69d8fa2f5954aa70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041305`

```sql
SELECT substr('  X - 8 -', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); ANALYZE p;
```

---

## Crash 52: `9f890255c1e2e662` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042604`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROL
```

---

## Crash 53: `e403c10b3fb2f905` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043460`

```sql
SELECT printf('%llu', 4294967296, '_7 -j135U'); SELECT printf('%s', 2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO q VALUES (TRUE ISNULL IS RAISE(IGNOR
```

---

## Crash 54: `65eb94dc7b106d5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043914`

```sql
SELECT substr('__L', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO q VALUES (RAISE(IGNORE)); ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY
```

---

## Crash 55: `54e81e71f6beb9a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044813`

```sql
SELECT substr('i gXW obi_-_Hr3 3', 2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); ANALYZE p; SELECT hex(zeroblob(-
```

---

## Crash 56: `b1d638191ccdea31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045326`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR
```

---

## Crash 57: `12cacd453be4224d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045645`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY TRUE ASC NULLS LAST; CREATE VIRTUAL TABLE 
```

---

## Crash 58: `7171a517edb35a41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045813`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT CURRENT_TIMESTAMP AS a FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 59: `75e6ebca3630e256` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046009`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p INNER JOIN p AS l; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 60: `c07cc72da7d5db13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046239`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VAL
```

---

## Crash 61: `69894a842b4e5b49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047742`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); ANALYZE p; SELECT hex(zeroblob(-1));
```

---

## Crash 62: `5948c4e44f4dcbc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048003`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO q (a) VALUES (NULL) ON CONFLICT(rowid) DO UPDATE SET b = TRUE; PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 63: `91f782cff603f0ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048211`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, b DATE PRIMARY KEY, a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 64: `22e545dc9180b2f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048333`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 65: `56419df269a711e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048368`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, b DATE PRIMARY KEY, a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 66: `2477a036cd099249` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048579`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, c3 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 67: `81c0d0c6dbfa5235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050598`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); WITH RECURSIVE q (c2) AS (VALUES (NULL)) SELECT * FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 68: `2420608ece91df29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055186`

```sql
SELECT substr('6vUhe_Xb- 75 6LN 8', 4294967295, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT RAISE(IGNORE) REGEXP -CURRENT_TIME IS NULL OR RAISE(IGNORE) NOT BETWEEN FALSE 
```

---

## Crash 69: `d51ecadd26192322` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055673`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) EXCEPT VALUES (sum(NULL) FILTER (WHERE CURRENT_
```

---

## Crash 70: `dc16a656e1813e1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055933`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(DISTINCT FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 71: `b35226c92b0b24ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056086`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK I
```

---

## Crash 72: `10b1d291568d2cac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056276`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (''); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSER
```

---

## Crash 73: `20e6b6182a000fe5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058644`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_TIME AS FLOAT) OR 0.0); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 74: `12cbbd609bcb9372` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058851`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_TIME AS FLOAT) OR CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 75: `671fa28ab4fe460b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059065`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, c2 VARCHAR(255) CHECK (NULL)); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 76: `737eb6af203969a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059190`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a + -37352) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR 
```

---

## Crash 77: `55b6449d03a675b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059373`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 78: `8c1502b1c6f657c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060129`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBA
```

---

## Crash 79: `bc3c2e5ac23f8524` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060790`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a = -0) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLL
```

---

## Crash 80: `7b9b1f00547c4b2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062946`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY TRUE ASC NULLS LAST, RAISE(IGNORE) ASC; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 81: `85b1b1eca3cc7ff2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065069`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_DATE = CURRENT_TIMESTAMP AS TEXT)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 82: `683d68158cbe38b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065797`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT CURRENT_DATE AS tl FROM p WHERE TRUE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 83: `c333ee253ede4b00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066428`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT INTO p
```

---

## Crash 84: `e1e01bb68db17ca8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066636`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROL
```

---

## Crash 85: `6ab402c8fb62bdd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066751`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT count(*) OVER (PARTITION BY c1 ORDER BY CURRENT_DATE ASC NULLS LAST) AS a FROM p WHERE CURRENT_TIME
```

---

## Crash 86: `f3ce167ff1bd7901` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066771`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT count(*) OVER () AS a FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 87: `3d89f96dfb7f9a1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ASC NULLS LAST) AS a FROM p WHERE CU
```

---

## Crash 88: `27832a750b0899af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066989`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT *, *, * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 89: `cab98cc4d36df836` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067566`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT *, * FROM (SELECT NULL & FALSE COLLATE RTRIM << FALSE FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 90: `c5ff9511e467f49a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067792`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE TRUE OR CURRENT_DATE) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 91: `8f661f84fc33f2c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068211`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE TRUE NOTNULL OR CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 92: `21e0a7a88b56202f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068358`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT rowid AS tl, * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c3); 
```

---

## Crash 93: `28b559dc9c996f32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068475`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT CURRENT_TIMESTAMP LIKE NULL FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 94: `5175888d7d370e8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069644`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP <> CURRENT_TIME OR CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE I
```

---

## Crash 95: `ed25f5498751a949` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069844`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INT
```

---

## Crash 96: `ea01ea113137fd7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069875`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE FALSE IN (VALUES (FALSE))) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 97: `c90627db545e7b46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME > TRUE COLLATE RTRIM) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 98: `4d152692534d595d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070554`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE FALSE BETWEEN CURRENT_TIME AND CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*g', -214
```

---

## Crash 99: `66252052e9868e81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070759`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE FALSE BETWEEN NULL AND CURRENT_TIMESTAMP <> CURRENT_TIME) AS sub1; SELECT printf('%.*
```

---

## Crash 100: `a7b044ba2269713e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071137`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT 0.0); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 101: `d2ee23c837f55ea0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071343`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 102: `94d0d15ebef5b0a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071844`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) UNION SELECT CURRENT_TIME 
```

---

## Crash 103: `5786dd49d0f6a3d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072223`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL) INTERSECT VALUES (TRUE) UNION SELECT CURRENT_TIME 
```

---

## Crash 104: `a41afa333d9adb3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073059`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VIRTU
```

---

## Crash 105: `d5d2ae7f73389103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073245`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT count(*) OVER (PARTITION BY NULL ORDER BY CURRENT_DATE RA
```

---

## Crash 106: `2dbc301bd73254bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074049`

```sql
SELECT substr('', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (b, c3) VALUES (CASE WHEN (CURRENT_TIME NOT NULL) ->> TRUE COLLATE NOCASE THEN (NULL)
```

---

## Crash 107: `2322869e201619cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074243`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (total_changes()) INTERSECT VALUES (CURRENT_TIMESTAMP); C
```

---

## Crash 108: `648faedf7caf34df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074422`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIMESTAMP); CREA
```

---

## Crash 109: `fa35696c04233c1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074451`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (abs(CURRENT_TIMESTAMP)) INTERSECT VALUES (CURRENT_TIMEST
```

---

## Crash 110: `f6b9439f15ceddba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074769`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (random()) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE V
```

---

## Crash 111: `f5ba606d95d89315` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075047`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (abs(NULL)) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE 
```

---

## Crash 112: `ea69566f24054432` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075124`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (changes()) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE 
```

---

## Crash 113: `083aa8a145a3c1d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075286`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME OR sum(FALSE) FILTER (WHERE CURRENT_TIME)) 
```

---

## Crash 114: `3346c49665101c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075369`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME OR sum(FALSE) FILTER (WHERE TRUE IS NULL)) 
```

---

## Crash 115: `38d519f8927d2645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076320`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (NULL) INTERSECT SELECT * FROM p WHERE FALSE GROUP BY CUR
```

---

## Crash 116: `7d0613dbdb08c0ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE FALSE GROUP BY NULL WINDOW w1 AS () ORDER BY NULL DESC NULLS LAST); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 117: `553d2161126198cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078937`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE ORDER BY CURRENT_TIME ASC LIMIT FALSE OFFSET -FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 118: `ea58bf4e34d9f41b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079133`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE ORDER BY CURRENT_TIME ASC LIMIT TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 119: `1f3ccc3ef10f741e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079166`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) EXCEPT VALUES (FALSE / CURRENT_DATE IS NOT NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 120: `b2bd95a2762ad6c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079880`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT ALL *, * FROM p NOT INDEXED); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO 
```

---

## Crash 121: `7505a8697cd41f78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080610`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE) EXCEPT SELECT count(*) OVER () AS a FROM p WHERE FALSE GROUP BY CURRENT_DATE WINDOW w1 AS ()); CR
```

---

## Crash 122: `a28a35e75a25a957` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084275`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE << TRUE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 123: `af14048e706019fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084418`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 124: `e1686551d561c364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084459`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT 
```

---

## Crash 125: `44bf6deba872674f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084635`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_TIMESTAMP AS BOOLEAN)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_row
```

---

## Crash 126: `6f0a9d2f78df0cc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE << CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowi
```

---

## Crash 127: `73ecc8ad00a6ef1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088626`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE -(TRUE LIKE FALSE ESCAPE FALSE)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 128: `464790dc6f40e1af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088818`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE -CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INS
```

---

## Crash 129: `4a920299fcab2569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089887`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 130: `e04539c0802686ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090051`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT NULL <= CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 131: `6d3cf72f7c721002` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090213`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE FALSE <= CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 132: `967da398f132f41a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090573`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE NULL MATCH NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 133: `33d6f8d98e0cd38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090748`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE FALSE LIKE CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 134: `72423d1332985a99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091523`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT * FROM (SELECT * FROM q WHERE NULL >= NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 135: `b2fb5f814cd3c7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098201`

```sql
SELECT printf('%.*d', 4294967295); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 136: `875eaa59df9f0d55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120336`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p (c1, b) AS (VALUES (RAISE(IGNORE), CURRENT_DATE NOTNULL IS NOT TRUE != TRUE
```

---

## Crash 137: `01a3b9b424d3b6d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121198`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); INSERT OR FAIL INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p 
```

---

## Crash 138: `5775234308acb0e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138158`

```sql
SELECT printf('%lli', -2147483648, ''); SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(b DATE, b GENERATED ALWAYS AS (a = 0) ); SELECT p.*, FALSE IS ~TRUE NOT NULL ISNULL <> CU
```

---

## Crash 139: `4c6daa1403d029b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143141`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a INTEGER); SELECT (VALUES (count(*) OVER (PARTITION BY NULL ORDER BY CURRENT_DATE ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING))
```

---
