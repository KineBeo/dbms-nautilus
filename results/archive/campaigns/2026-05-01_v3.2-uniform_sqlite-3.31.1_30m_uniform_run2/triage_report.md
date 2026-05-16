# Crash Triage Report

**Total crashes:** 296  
**Unique crash sites:** 296  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 296 | 296 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `639d48b175f7647c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000036`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER GENERA
```

---

## Crash 2: `8edeaa8f929c6337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000168`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO p VALUES (NULL COLLATE BINARY BETWEEN NULL AND FALSE * NULL + FALSE NOT BETWEEN total_changes() != CASE WHEN NULL THEN NULL || 
```

---

## Crash 3: `1a3b7445d5f10ee3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001291`

```sql
SELECT printf('%.*f', -1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS (VALUES (CURRENT_TIMESTAMP)) INSERT INTO p VALUES (-NULL IS NULL > hex(CURRENT_TIMESTAMP) 
```

---

## Crash 4: `c626aacf22818485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001345`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); INSERT OR ROLLBACK INTO p VALUES (NULL ISNULL); WITH RECURSIVE q AS (SELECT p.*) SELECT CURRENT_DATE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 5: `f23b2ab54aeec299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001785`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO
```

---

## Crash 6: `3f6eeef65251f9d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002122`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 NUMERIC CHECK (CURRENT_TIME), c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE
```

---

## Crash 7: `2214f554cc3939d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002156`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, a BOOLEAN UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 8: `055ee823dfdb5603` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002180`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT s.* FROM p WHERE EXISTS (SELECT DISTINCT t3.* FROM q INDEXED 
```

---

## Crash 9: `942b6571ed933c1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002188`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 10: `5de91b4f1282507d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002226`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, _rowid_ TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 11: `ad18e429fc98f47f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002247`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR ABORT INTO r VALUES (--
```

---

## Crash 12: `de1a0f77fb4ff825` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002253`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES ((CURRENT_TIMESTAMP)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR ABORT INTO r VAL
```

---

## Crash 13: `c36b562c5ccf20a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002259`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES ((CURRENT_TIMESTAMP NOT LIKE TRUE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR AB
```

---

## Crash 14: `c99fa7540576b78f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002315`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR ABORT INTO r VALUES (--+RAISE(IGNORE) IS DISTINCT FROM CURRENT_DATE NOT IN (RAISE(IGNORE) ISNU
```

---

## Crash 15: `dc0d7ebf7748a085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002430`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT +TRUE IS NULL AS a FROM t3 WHERE EXISTS (SE
```

---

## Crash 16: `c2a068f40f12ffcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002859`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TAB
```

---

## Crash 17: `7b861e5a30b3be46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003099`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zerobl
```

---

## Crash 18: `561c480cc4e46ba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003625`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE ORDER BY CURRENT_TIME OR NULL; CREATE VIRTUAL TABL
```

---

## Crash 19: `d67bdf74864310ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003631`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY TRUE ORDER BY CURRENT_TIME OR NULL; CREATE VIRTU
```

---

## Crash 20: `9f4aeadc87d83d36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003637`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ISNULL GROUP BY TRUE ORDER BY CURRENT_TIME OR NULL; 
```

---

## Crash 21: `54d984634a758d96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003643`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME < CURRENT_DATE IS NULL ISNULL GROUP BY TRUE ORDER BY CURR
```

---

## Crash 22: `ed7b7fd684770d5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003649`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE (CURRENT_DATE) < CURRENT_DATE IS NULL ISNULL GROUP BY TRUE ORDER BY CU
```

---

## Crash 23: `8e463859ce3e0422` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003717`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL TAB
```

---

## Crash 24: `8056dff2e6ff1416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003725`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE NULL < NULL ISNULL GROUP BY TRUE ORDER BY TRUE DESC NULLS FIRST; CREAT
```

---

## Crash 25: `11a84c8cf43fa7ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003752`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY TRUE ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL TABL
```

---

## Crash 26: `046b2ea1fb3db300` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003828`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE ORDER BY CURRENT_TIMESTAMP DESC; CREATE VIRTUAL TA
```

---

## Crash 27: `19fed64d918918d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004776`

```sql
SELECT printf('%.*g', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS MATERIALIZED (SELECT p.*, NOT EXISTS (SELECT *, -TRUE) FROM r WHERE CAST(
```

---

## Crash 28: `d17d1488d5e68c9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005863`

```sql
SELECT substr('o  0o66uH-', 2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE r AS (SELECT *, FALSE IS NOT DISTINCT FROM CURRENT_TIMESTAMP AS q_y1_2h__
```

---

## Crash 29: `6edfaeb2db1ebfd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006195`

```sql
SELECT printf('%lld', 4294967295, 'QG9 P '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, CASE RAISE(IGNORE) NOT NULL WHEN random() OVER () NOTNULL THEN zeroblob(~CURRENT_TIME
```

---

## Crash 30: `006f2a1b22461930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006229`

```sql
SELECT printf('%lli', 2147483648, ''); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT RAISE(IGNORE) COLLATE NOCASE >> CURRENT_TIME >= FALSE AS a, quote(CASE 
```

---

## Crash 31: `4a98ddc14f49d79c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006236`

```sql
SELECT printf('%lli', 2147483648, ''); CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF 
```

---

## Crash 32: `ae5ceb00943ba49b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007319`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c2, c2, a, c3, c2, c1); INSERT INTO q (c2, c3, _rowid_, c2, a) VALUES (printf('', TRUE ->> CURRENT_DATE LIKE TRUE COLLATE NOCASE IS CURRENT_
```

---

## Crash 33: `9b7870ebee7c30a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008315`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT printf('%.*d', 2147483647, 0.0);
```

---

## Crash 34: `f89415650b34b2e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008393`

```sql
SELECT printf('%.*g', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH q (b) AS (VALUES (TRUE) UNION ALL SELECT s.* ORDER BY NULL ISNULL), p (c3) AS (VALUES (TRUE, CUR
```

---

## Crash 35: `4bbbc01d79a15cf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013684`

```sql
SELECT printf('%.*s', 4294967296, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 36: `3c959d7bbb9fce58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016067`

```sql
SELECT printf('%.*f', -2147483649, 1e308); CREATE TABLE IF NOT EXISTS p(c2 FLOAT GENERATED ALWAYS AS (FALSE COLLATE NOCASE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); WITH s (rowid, b) AS (VAL
```

---

## Crash 37: `1e807b2e3e067ec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024450`

```sql
SELECT printf('%.*d', -9223372036854775808); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 38: `8cad674e9e5e7436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024577`

```sql
SELECT substr('', 4294967296, 0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 39: `bd197ec7878639d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028346`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `cee9786ecee8ed19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028790`

```sql
SELECT printf('%.*f', 2147483647, -1e308); SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 41: `3853b41da5d05a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028828`

```sql
SELECT printf('%.*d', 2147483647, -1e308); SELECT printf('%.*e', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); INSERT OR IGNORE INTO t3 VALUES (NULL > CURRENT_TIMESTAMP 
```

---

## Crash 42: `8f925394dbd94c54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029146`

```sql
SELECT printf('%lld', -1, ''); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 43: `70737e2fd17c7f03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030030`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE < NULL GROUP BY TRUE ORDER BY NULL; CREATE VIRTUAL TABLE 
```

---

## Crash 44: `79edc41ed0f6097f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE < NULL GROUP BY TRUE ORDER BY NULL; SELECT substr('', 429
```

---

## Crash 45: `2101485fa3b35405` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035372`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT r.*, CURRENT_TIMESTAMP NOT BETWEEN NULL AND (CURRENT_DATE REGEXP NULL) - +FALSE REGEXP CURRENT_TIMESTAMP ISNULL
```

---

## Crash 46: `aab926d2fbae2f78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037460`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIM
```

---

## Crash 47: `20fad8364be1c552` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037745`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF N
```

---

## Crash 48: `112cb0407441253d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037766`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF N
```

---

## Crash 49: `cb9def9bddb62bde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039633`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA integrity_check; SELECT printf
```

---

## Crash 50: `fab6d9cde3edbd29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040667`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIM
```

---

## Crash 51: `2842782604c2efcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040866`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN 
```

---

## Crash 52: `c9c595b16dcf8408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040891`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 53: `45630bb8feebf51e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040981`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT OR ABORT INTO q VALUES (FALSE << FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 54: `e409b116e7581fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041274`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT OR ABORT INTO q VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 55: `6d1304de38de6e6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041284`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR ABORT INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 56: `f1f96f0781fabbb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041478`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR ABORT INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 57: `1787630d216f6fe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041852`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT FALSE); INSERT OR ABORT INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 58: `8c9850d165a91403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, c1, c1); SELECT * FR
```

---

## Crash 59: `46bb0ab651372380` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (changes() NOT LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VAL
```

---

## Crash 60: `295d3b01eeb70caa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046359`

```sql
SELECT printf('%f', 0, 'b-2y  c'); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 61: `4425d1a95dc59440` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048047`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT IN (VALUES (TRUE))) AS sub1; CREATE VIRTUAL TABLE
```

---

## Crash 62: `af6df10eb53a5877` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE t1 AS (VALUES (CURRENT_TIMESTAMP)), q AS (SELECT *) SELECT *; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VI
```

---

## Crash 63: `92d338cc2d557daf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048910`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 64: `a886795f8c466dbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048927`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (+NULL < CURRENT_TIMESTAMP NOT IN (NULL) != CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA 
```

---

## Crash 65: `52722ecd01bfc6a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048966`

```sql
SELECT substr('5M2_Q3', -2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 66: `be5c9f92bfebda7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048972`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, a GENERATED ALWAYS AS (a = 234859) NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VA
```

---

## Crash 67: `108deb21e6a3ce43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049671`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 68: `b25d4dc4574e8086` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050283`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT DISTINCT q.*, NULL AS z8 FROM q INDEXED
```

---

## Crash 69: `9d5aaab697b321f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050365`

```sql
SELECT printf('%.*g', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME ISNULL); SELECT * FROM q NATURAL JOIN t1 WHERE json_extract(
```

---

## Crash 70: `44114ecf410b2cfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050663`

```sql
SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CURRENT_TIMESTAMP IS NOT NULL MATCH NULL NOTNULL | RAISE(IGNORE) COLLATE RTRIM <> ~F
```

---

## Crash 71: `0d1599c7ea204d78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050822`

```sql
SELECT printf('%.*g', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT t1.* ORDER BY q.rowid INTERSECT SELECT NOT CURRENT_DATE > (CURRENT_TIMESTAMP ISNULL) AS le, q
```

---

## Crash 72: `629087cc7e9bf555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050840`

```sql
SELECT round(0.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT ((last_insert_rowid())) FROM t3 WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY RAISE(IGN
```

---

## Crash 73: `802068adc8eed8bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051025`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(c1 INT DEFAULT FALSE, a INT PRIMARY KEY); WITH RECURSIVE r (c1) AS (SELECT ALL *, * FROM p AS if___m9_ EXCEPT SELECT CURRENT_TIME OR 
```

---

## Crash 74: `939393de1eeceb30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051179`

```sql
SELECT substr('uNIZ_45 ', 4294967295, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); SELECT t2.* FROM p JOIN p s__ ON upper(NULL != -CURRENT_TIMESTAMP LIKE CURRENT
```

---

## Crash 75: `74a87652942f5f36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053589`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS
```

---

## Crash 76: `9b6fbf9d24bd1b8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054337`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (), NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO 
```

---

## Crash 77: `0f579cc6d50232a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054428`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (X'EBEfDbAbfBcD'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAU
```

---

## Crash 78: `864e2944c5f1c47f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP COLLATE BINARY AS g0_4a9x9h_q7 ORDER BY CURRENT_DATE COLLAT
```

---

## Crash 79: `a17ead255654f3ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME COLLATE NOCASE < CURRENT_TIMESTAMP) AS sub1; CREATE V
```

---

## Crash 80: `0cccf336c16062e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055030`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE OR RAISE(IGNORE)) AS sub1; SELECT printf('%.*f', -2147483649,
```

---

## Crash 81: `7430d31c905d8c0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055534`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIM
```

---

## Crash 82: `59437e299e8816b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056745`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT count(*) OVER () AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_r780_u_1cu_98_98__3_rcic_217i__e
```

---

## Crash 83: `b4e4324c040bbd66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057359`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN TRUE AND CURRENT_TIME) AS sub1; SELECT pr
```

---

## Crash 84: `3c3c04527ed04779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057694`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT -49061700399859.5695452180872605652294754737168978401855037896720742621653296208478134090255782486379662970647184752784757047050046931654672513274178814426
```

---

## Crash 85: `df40ea6d7ac4eb50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058219`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 86: `5b651e990afac899` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058593`

```sql
SELECT substr('-sx_ -c Na -h ', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c3, c1); SELECT FALSE LIKE FALSE AS i FROM t3 WHERE EXISTS (SELECT * FROM t1 INNER JOIN t1 NOT
```

---

## Crash 87: `755cb88fc57e2d10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060890`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 
```

---

## Crash 88: `6b6ccac577789d91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060941`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT round(-1e308, 0); CREATE 
```

---

## Crash 89: `f8282e8537a36fc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060995`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*f', -214748364
```

---

## Crash 90: `6cfa9bc58e8853c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061001`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b F
```

---

## Crash 91: `01907034725593cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061060`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 
```

---

## Crash 92: `c749bf232a512654` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061085`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT 
```

---

## Crash 93: `cde35729431270a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061755`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (last_insert_rowid()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 94: `487b80908ef8f1d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061889`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (last_insert_rowid()); PRAGMA quick_check; SELECT printf('%x', 2147483648, '_1qp - _ 6-u 6j __ '); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 95: `6f8d7f9c6acd7c14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062031`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, rowid GENERATED ALWAYS AS (a) NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); IN
```

---

## Crash 96: `227553b9205e4b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062153`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (char(NULL) NOT LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VA
```

---

## Crash 97: `f3e7fc9e4de8a319` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062301`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (total_changes() NOT LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAU
```

---

## Crash 98: `6b8d95336a9a80ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062679`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT LIKE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 99: `c1a1cc2f3ab8a67a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063106`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 100: `7c4c202f9d51fb24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063679`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT -7255423084591324945087681714187123153014764223574097014592745294747862531320266699223167324791238013984899650100404431035245565077220646984.878
```

---

## Crash 101: `795e474f3ace580e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064583`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL DEFAULT -0); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 102: `a2615386bed50d10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064724`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 103: `d9507b3fbe8c383a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064856`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 104: `aba05fa1f15ca629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065747`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 105: `378f354bbae3caa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065782`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRI
```

---

## Crash 106: `bc5186a0392c8963` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066974`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (SELECT CURRENT_TIMESTAMP UNION SELECT CURRENT_DATE ORDER B
```

---

## Crash 107: `d59e0b9fc2a0cde8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067188`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (SELECT CURRENT_TIMESTAMP UNION SELECT CURRENT_DATE ORDER B
```

---

## Crash 108: `04c2e493041fe7e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067579`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 109: `c0aa80b53828ddbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067899`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (VALUES (CURRENT_TIMESTAMP) UNION SELECT CURRENT_DATE ORDER
```

---

## Crash 110: `07dfe2486db043e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068016`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT OR ABORT INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 111: `c77c8a8c1cc69a99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073923`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) VALUES (FALSE NOT BETWEEN FALSE AND FALSE NOT BETWEEN FALSE AND
```

---

## Crash 112: `28d75f81e69f32fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080450`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CAST(CURRENT_TIMES
```

---

## Crash 113: `931dbf02b2c32b39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080675`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_DATE IS NO
```

---

## Crash 114: `2b60e31695e5a689` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080853`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIME + CUR
```

---

## Crash 115: `d579983833cec17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080891`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING count(*) FILTER (W
```

---

## Crash 116: `99c01f5da02945f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081302`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIME)) GROUP BY TRUE ORDER BY TR
```

---

## Crash 117: `8740d15e73f19c22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081554`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE TRUE BETWEEN NULL AND CURRENT_TIMESTAMP GROUP BY TRUE ORDER BY TRUE DE
```

---

## Crash 118: `1a03ef258cfe9797` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082025`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE '' GROUP BY TRUE ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL TABLE 
```

---

## Crash 119: `5a362a60a6ef91d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083480`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 TEXT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT count(*) OVER () AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_r780_u_1cu_9
```

---

## Crash 120: `a774ae00b9be91e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083747`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL == CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 121: `d7c71805991074ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084074`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT GENERATED ALWAYS AS (FALSE) STORED, rowid DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VI
```

---

## Crash 122: `eaddfc40e7fbb03d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084357`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT
```

---

## Crash 123: `910f97d952ca8c1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084467`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (TRUE) STORED, c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTU
```

---

## Crash 124: `765e8c45466275f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084859`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (CURRENT_DATE), b BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAUL
```

---

## Crash 125: `d5602b08facc516d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096973`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (CURRENT_TIME LIKE CURRENT_DATE OR TRUE); PRAGMA integrity_check; SELECT printf('%
```

---

## Crash 126: `59a4e701214aa83c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097180`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (CURRENT_TIME - FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 127: `11c68bd526da8879` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097349`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (CURRENT_DATE OR TRUE == CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 128: `838b3e7b28f9f8c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097771`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); SELECT * FROM (SELECT p.* FROM p WHERE CURRENT_TIME) AS sub1; CREATE TABLE IF NOT EXISTS p(a DATE, c2 GENERATED ALWAYS AS (coalesce(a, b)) ); INSERT INTO 
```

---

## Crash 129: `b5357807801eabfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098173`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 130: `90397c79cf78d7ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098361`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-2696.98540809212866282108054857756194413524981986976766375767541232669437613610307
```

---

## Crash 131: `a6f88d25b92f685d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098499`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN VALUES (CURRENT_T
```

---

## Crash 132: `0e53bbe1d576a765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099412`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-413); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 133: `04b2c8d0d8c94e71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099469`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (SELECT FALSE % CURRENT_TIME)); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE
```

---

## Crash 134: `f0fbe83fbbe9e893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099694`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (SELECT CURRENT_TIMESTAMP FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_T
```

---

## Crash 135: `98eadc7c646f79ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099954`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (SELECT * FROM p GROUP BY CURRENT_TIMESTAMP)); EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 136: `83261da61f6da68d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100295`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIME))); VALUES (TRUE); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 137: `07edb84e6b744af1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101829`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); INSERT OR REPLACE INTO p VALUES ((SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY FALSE WINDOW w1 AS ())); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 138: `08bd3cf8403b8921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101840`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE, a GENERATED ALWAYS AS (a) NOT NULL); SELECT CURRENT_TIMESTAMP UNION ALL SELECT CURRENT_DATE AS g0_4a9x9h_q7 ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST; CREATE VIRT
```

---

## Crash 139: `dc1e56dc04a151b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101871`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL total_changes() OVER (ORDER BY CURRENT_TIME DESC NULLS LAST ROWS BETWEEN CURRENT_TIME PRECEDING AND NULL FOLL
```

---

## Crash 140: `c4670afd29617cd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110671`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE p AS (VALUES (CURRENT_TIME) EXCEPT SELECT CURRENT_TIME) SELECT * FROM p; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 141: `cc96f2e7190fb584` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114641`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL, b NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); WITH RECURSIVE t2 AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 142: `5b7d3073f65012cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115915`

```sql
SELECT substr('', -2147483649, 9223372036854775807); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 143: `5fc204aef83eace2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118647`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) EXCEPT SELECT FALSE | CURRENT_DATE COLLATE RTRIM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INS
```

---

## Crash 144: `122dc0917c14e942` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118804`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) EXCEPT SELECT FALSE / CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL I
```

---

## Crash 145: `a9fa4a2f23f14d60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119216`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME > FALSE) EXCEPT SELECT TRUE BETWEEN NULL AND CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 146: `2cbbd5a21ccf60d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119383`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () EXCEPT SELECT CURRENT_DATE; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 147: `563a6bdfca943eba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119595`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); EXPLAIN QUERY PLAN VALUES (TRUE) INTERSECT SELECT CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 148: `b0d4108fe75a01f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119951`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TI
```

---

## Crash 149: `45424c1d4c72bc6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126800`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_DATE ->> TRUE > CURRENT_TIMESTAMP NOT NULL AS t_od FROM p WHERE EXISTS (SELECT DISTINCT
```

---

## Crash 150: `39b7580505d8e58c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128046`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT FALSE >> CURRENT_DATE IS NOT FALSE ORDER BY CURRENT_DATE ASC NULLS LAST; CREATE VIRTUAL TABLE 
```

---

## Crash 151: `02f009b52aea59d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135395`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); WITH RECURSIVE t2 AS (SELECT *) SELECT CURRENT_TIMESTAMP AS g_f__ FROM p; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 152: `652056c9f00af1cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143510`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT CURRENT_DATE || NULL AS r_8___e___1m9_di60caft23_0pi95_0__k6_3___4unm8_877_pv_mo0ml___v_ UNION ALL SELECT CURRENT_DATE AS g0_4a9x9h_q7 
```

---

## Crash 153: `f8fff50475ae3943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144431`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (NULL) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (min(FALSE)); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 154: `99e59c9bf56fe3ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144582`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (NULL) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 155: `d183d5b918a648b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145352`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT 5092733011042654156582870086161136879438981605685354486370992241601318183832796.9e+0472); SELECT CURRENT_TIMESTAMP UNION ALL SELECT CURRENT_DAT
```

---

## Crash 156: `83846dadf87847de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145371`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (random() FILTER (WHERE TRUE)) EXCEPT SELECT * ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; SELECT CURRENT_TIMESTA
```

---

## Crash 157: `c2ae155dc5ee0d22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145400`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (NULL) STORED, c2 INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT CURRENT_TIMESTAMP UNION ALL SELECT CURRENT_DATE AS g0_4a9
```

---

## Crash 158: `9a703f46518500ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146194`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); SELECT DISTINCT max(NULL) AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_r780_u_1cu_98_98__3_rcic_217i__e_2_m340_3g8507ww_lzz62_32312c7t_1_949__g__8z_
```

---

## Crash 159: `32bf7aec2db4a2cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146361`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); SELECT DISTINCT * FROM p NOT INDEXED UNION ALL VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 160: `b975e7dad9caaccf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146368`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); SELECT DISTINCT FALSE AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_r780_u_1cu_98_98__3_rcic_217i__e_2_m340_3g8507ww_lzz62_32312c7t_1_949__g__8z__22h
```

---

## Crash 161: `f1d4c0d7aca32ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147202`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (SELECT FALSE % count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS LAST ROWS B
```

---

## Crash 162: `533882389aa963b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147401`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE); VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 163: `a69b524bedd68e1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147638`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_TIMESTAMP); VALUES (CURRENT_DATE); CREATE VIRTUAL TA
```

---

## Crash 164: `f9a18d8875e262ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148568`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); SELECT CASE +RAISE(IGNORE) >= CURRENT_DATE + CURRENT_TIME == RAISE(IGNORE) IS NOT NULL NOT BETWEEN FALSE
```

---

## Crash 165: `aa8b41303c8bc8e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149609`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-2696.98540809212866282108054857756194413524981986976766375767541232669437613610307
```

---

## Crash 166: `75f5ace0b58e375e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150023`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (X'' IN (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE V
```

---

## Crash 167: `60f3fb69363e2100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150192`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 168: `72e18774905009f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150549`

```sql
SELECT printf('%.*s', 4294967295); SELECT hex(zeroblob(-2147483648)); SELECT printf('%.*d', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); WITH RECURSIVE r AS (WITH R
```

---

## Crash 169: `9b821e3498dbb994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151355`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (X'Ee63DaBEabFc3d' == CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 170: `da918fc403fcdb67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156370`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT max(NULL) AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_r780_u_1cu_98_98__3_rcic_21
```

---

## Crash 171: `e2a5f9b6d2975573` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); SELECT count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS o4_8_v4____pe156h_n1wssh31_7k98431_8u16_pll_
```

---

## Crash 172: `2ff4a8cfb4a24ce6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165847`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (TRUE) STORED, c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE 
```

---

## Crash 173: `59966c553b42b599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165973`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 174: `65e69dd288a28e47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166002`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY, a INTEGER); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE FALSE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 175: `1379c7e9694e5de3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166169`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE FALSE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 176: `ead5665dd204af51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166228`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT
```

---

## Crash 177: `c2baa2bd28909415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166386`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, a VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 178: `5d6fa47076ae5398` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166772`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE TABLE IF NOT EXISTS q(a INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP LIKE CURRENT_TIME ESCAPE NULL; CREATE VIRTUAL TABLE I
```

---

## Crash 179: `ad546ac1e9d6014a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167906`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY TRUE ORDER BY CURRENT_TIMESTAMP LIKE CURREN
```

---

## Crash 180: `e75645c0a6c1024a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168989`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE NULL LIKE CURRENT_DATE GROUP BY TRUE ORDER BY CURRENT_TIMESTAMP DESC N
```

---

## Crash 181: `10a6680e83a3352b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169722`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_DATE AS td__0_8__641_ti_u69odxm_267_9___7_cg__ FROM p NOT INDEXED WHERE FALSE GROUP BY TR
```

---

## Crash 182: `8a78e27931284e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT *, *, *, *, *, *, *, *, *, *, * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE ORDER BY TRUE DESC N
```

---

## Crash 183: `1fda86b78bee1db3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170540`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY _rowid_ LIKE CURRENT_TIME ESCAPE TRUE HAVING NULL ORDER 
```

---

## Crash 184: `f73b619225147ba1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171491`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CAST(CURRENT_TIMES
```

---

## Crash 185: `8b0cd0c1ac639826` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171669`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING FALSE ORDER BY NUL
```

---

## Crash 186: `c7ae21ed02654802` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181352`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE != CURRENT_TIMES
```

---

## Crash 187: `b399d102ba8f787d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIME), FALSE)) SELECT * FROM p NOT INDEX
```

---

## Crash 188: `811b9c859fbfc46f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182174`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE) UNION SELECT CURRENT_DATE ORDER BY FALSE) SELECT * FROM p NOT IN
```

---

## Crash 189: `1faf0d5db6ba5290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182854`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (count(*) OVER (), NULL)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE
```

---

## Crash 190: `8ca8c31ab423b78e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183235`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p LEFT OUTER JOIN q NOT INDEXED ON CURRENT_TIMEST
```

---

## Crash 191: `60718503d0dd7eba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183507`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (WITH p AS (VALUES (FALSE)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP
```

---

## Crash 192: `dfca3047570b0483` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183779`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (NULL) STORED, c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p (c2) VALUES (TRUE) ON CONFLICT(c2) DO UPDATE SET _rowid
```

---

## Crash 193: `4ccfdcb038726715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185134`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 194: `125df9cbb090228e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191885`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (NULL), c3 NUMERIC CHECK (CURRENT_TIME), c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL DEFAULT FALSE); INSERT OR ABORT INTO q VALUES (
```

---

## Crash 195: `a5468fd94d2b102d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192527`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE << -CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE 
```

---

## Crash 196: `cd12128ede4f9ac4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192628`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE << FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 197: `58006ad715a0d404` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192863`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (SELECT CURRENT_TIMESTAMP UNION SELECT CURRENT_DATE ORDER B
```

---

## Crash 198: `b5c62e43f69c5510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193058`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (VALUES (TRUE))); PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 199: `7129878b824563e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193307`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO q VALUES (FALSE IN (SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE UNIO
```

---

## Crash 200: `28aef894a2f361e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195363`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (EXISTS (VALUES (NULL)) * CURRENT_DATE); PRAGMA integrity_check; SELECT pr
```

---

## Crash 201: `2fa623698344fc00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195718`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 202: `5a33ebf6c0e139d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195744`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 203: `f0fd79113ca62576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195761`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 204: `8bd277f48074dee1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195959`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRI
```

---

## Crash 205: `8b328571f2c646ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196076`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRI
```

---

## Crash 206: `afb8b79a208d5ecc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196198`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 IN
```

---

## Crash 207: `bf3cf36869cda110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196351`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (randomblob(randomblob(CURRENT_TIMESTAMP))); PRAGMA integrity_check; CREAT
```

---

## Crash 208: `dc7440a68c876117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196373`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (randomblob(CURRENT_TIMESTAMP)); PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 209: `401b152ee0a004a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196471`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(25
```

---

## Crash 210: `afd534a155f8c526` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196781`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 211: `1f5ce3a0ffc48377` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197111`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREA
```

---

## Crash 212: `5f70e7b795fc27fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198149`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT -7255423084591324945087681714187123153014764223574097014592745294747862531320266699223167324791238013984899650100404431035245565077220646984.878621
```

---

## Crash 213: `1f500fc4996be926` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198701`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X'23Edbcd8F6'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 214: `980988813c5eb1cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198855`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT 5092733011042654156582870086161136879438981605685354486370992241601318183832796.9e+0472); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 215: `39b56291c94c1fda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200320`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (trim(FALSE) NOT LIKE changes()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INT
```

---

## Crash 216: `fb34c7a89f3c8808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201126`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE NOT LIKE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p
```

---

## Crash 217: `42846ab8c6f45047` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201471`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, rowid GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 218: `0caddac9dd6d3254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201705`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 219: `3eed074c6d7e6bf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201852`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, rowid GENERATED ALWAYS AS (a = -0) NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 220: `fb5ecd4d679ff9a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202668`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (NULL IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 221: `e514c768a52933ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202833`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (TRUE IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 222: `0998daa7ceb4b7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203061`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (char(CURRENT_TIMESTAMP) IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO 
```

---

## Crash 223: `2359b68411a638e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203263`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); REPLACE INTO r VALUE
```

---

## Crash 224: `49478b9445b89281` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203779`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 
```

---

## Crash 225: `1a6515038e798194` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204751`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, a DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIME NOT I
```

---

## Crash 226: `19002320c5f48054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206075`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; SELECT group_concat(CURRENT_TIME, 'os1Q-') FILTER (WHERE FALSE) 
```

---

## Crash 227: `01d95262f3e166dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN TRUE AND changes()) AS sub1; CREATE VIRTU
```

---

## Crash 228: `6294bb186c151b0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208462`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT -49061700399859.5695452180872605652294754737168978401855037896720742621653296208478134090255782486379662970647184752784757047050046931654672513274178814426
```

---

## Crash 229: `a1b0bfbfac9de56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208632`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT CURRENT_TIMESTAMP); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VAL
```

---

## Crash 230: `fab695aa7d04e66d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS LAST ROWS BETWEEN FALSE PRECEDING AND CURRENT_TI
```

---

## Crash 231: `b26d469d3e400b80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209228`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS LAST RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOU
```

---

## Crash 232: `2e8edf2d6e827c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210545`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_TIME COLLATE RTRIM AS a FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE
```

---

## Crash 233: `a075a8d7b05a841c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210731`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_DATE AS a FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 234: `8128ea83f71fa39f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210830`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_TIME COLLATE RTRIM IS NOT NULL AS a FROM p WHERE FALSE) AS sub1; CREATE V
```

---

## Crash 235: `48b6e08088bfcb9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT IN (VALUES (max(NULL)))) AS sub1; CREATE VIRTUAL 
```

---

## Crash 236: `ace5c0e314974e95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE IS NOT FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 237: `e4a8072b3e4bd20e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212895`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIM
```

---

## Crash 238: `2465a71d8d9ab8fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213265`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE FALSE IN (VALUES (FALSE) UNION SELECT CURRENT_DATE ORDER BY FALSE 
```

---

## Crash 239: `7dec698c414f19ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213736`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE OR RAISE(IGNORE) OR RAISE(IGNORE) OR RAISE(IGNORE) OR RAISE(I
```

---

## Crash 240: `87a9b142f6c9084b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_TIMESTAMP AS BOOLEAN) < CURRENT_TIMESTAMP) AS sub1; C
```

---

## Crash 241: `44ace50194e1b7a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214605`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); EXPLAIN QUERY PLAN SELECT CURRENT_DATE AS g0_4a9x9h_q7 ORDER BY TRUE COLLATE NOCASE DESC NULLS FIRST; SELECT printf('%.*f', 2147483647, -1e308)
```

---

## Crash 242: `9a1b453ce3d8ad5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214726`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT CURRENT_DATE AS g0_4a9x9h_q7 ORDER BY CURRENT_DATE COLLATE NOCASE DESC NULLS 
```

---

## Crash 243: `53347135ca3052d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216082`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (ORDER BY (VALUES (NULL)) ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CUR
```

---

## Crash 244: `dbb674ab39900dda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216640`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (), count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

---

## Crash 245: `d166bb0044002905` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216822`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (), count(*) OVER (), NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 246: `0691cfb2e6317892` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217211`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS
```

---

## Crash 247: `db68fd331db13b63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217382`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (CURRENT_DATE, count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXC
```

---

## Crash 248: `46f341b75741a3a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (count(*) OVER (ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS
```

---

## Crash 249: `9558cb64f1e72aaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225385`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME OR FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 250: `7aac74a60ce28475` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225620`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE FALSE IN (VALUES (FALSE) UNION SELECT count(*) ORDER BY FALSE DESC
```

---

## Crash 251: `e67a4d760af097e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227040`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT IN (VALUES (p.c2))) AS sub1; CREATE VIRTUAL TABLE
```

---

## Crash 252: `272918b250d574aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232113`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, *, *, *, *, *, *, *, *, *, *, *, * FROM p NOT INDEXED; CREATE VIRTUAL TA
```

---

## Crash 253: `e08aa27bf09c2661` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232864`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 TEXT NOT NULL DEFAULT -93375435560104974801464411205563433704082159089607885822692321364458418179194423542343221764945121789780099625658409481411795054800211
```

---

## Crash 254: `6c17dab2ea7a6359` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233000`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CR
```

---

## Crash 255: `3448028978c3ab2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234193`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (NULL), c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 256: `3320cafd6f3931e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234577`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b T
```

---

## Crash 257: `08d2b6d7ca0c611a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234683`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b T
```

---

## Crash 258: `b4dcb92e33c50cfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235428`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (json_type(TRUE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (CUR
```

---

## Crash 259: `97e33d980e1808cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237296`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP NOT LIKE changes() NOT LIKE randomblob(randomblob(CURRENT_DATE))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 260: `ec748827afe51011` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237462`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (trim(NULL)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (NULL); P
```

---

## Crash 261: `ef2d7ac928abaa54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237646`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (trim(randomblob(randomblob(CURRENT_TIMESTAMP))) NOT LIKE changes()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 262: `fc86a2fa9ae08885` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238614`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT OR REPLACE INTO p VALUES (random() NOT LIKE changes()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p
```

---

## Crash 263: `8a05f68657bb6567` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239106`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNI
```

---

## Crash 264: `afa5e7d2d69738ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239183`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (CAST(RAISE(IGNORE) AS FLOAT)) STORED
```

---

## Crash 265: `cd8b88e2d0cccd29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239365`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) GENERATED ALWAYS AS (RAISE(ROLLBACK, '
```

---

## Crash 266: `264b24b4e2b22d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239859`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL DEFAULT 5092733011042654156582870086161136879438981605685354486370992241601318183832796.9e+0472); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 267: `6fc01d661a889f9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242939`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NO
```

---

## Crash 268: `6e1289b5c56e1925` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243121`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER NO
```

---

## Crash 269: `bd8a3f6895ff5e68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243359`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(25
```

---

## Crash 270: `ac6f47a10babc975` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243530`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (randomblob(CURRENT_TIMESTAMP)); PRAGMA integrity_check; CREATE TABLE IF N
```

---

## Crash 271: `ccfdd67bce17a217` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243707`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KE
```

---

## Crash 272: `3c7f10b062c43893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243719`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KE
```

---

## Crash 273: `b65602d8ccaead53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243731`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KE
```

---

## Crash 274: `91e4556c53f1c515` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243745`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KE
```

---

## Crash 275: `b9e3dc0740353840` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243763`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KE
```

---

## Crash 276: `6f5e7ab6a0c69548` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244186`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (randomblob(CURRENT_TIMESTAMP)); PRAGMA
```

---

## Crash 277: `6ad384cbdd32b742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244468`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (randomblob(randomblob(CURRENT_TIMESTAMP))); PRAGMA integrity_check; CREAT
```

---

## Crash 278: `1cf799770ee8d631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244608`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLO
```

---

## Crash 279: `60e20213dc6a48af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244630`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 IN
```

---

## Crash 280: `6bfca674bd927a7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245206`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE); INSERT OR FAIL INTO p VALUES ((SELECT ALL * FROM q ORDER BY TRUE ASC LIMIT TRUE, TRUE)); PRAGMA integri
```

---

## Crash 281: `02cf6a0fa9d85c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247437`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 282: `e56f5f4e95ec0849` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253477`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 283: `48329998b44d3a86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255304`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (WITH p AS (VALUES (FALSE)) SELECT DISTINCT * FROM p NOT INDEXED) SELECT * FROM 
```

---

## Crash 284: `36605ec7f42acd19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255539`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM ((VALUES (CURRENT_TIME)) AS a LEFT JOIN p) NATURA
```

---

## Crash 285: `0acb92ba632b41ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255897`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM q NATURAL JOIN p NOT INDEXED WHERE CURRENT_DATE G
```

---

## Crash 286: `c491e4ce01a2c485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p LEFT OUTER JOIN q NOT INDEXED ON CURRENT_TIMEST
```

---

## Crash 287: `8d5e775b0500a869` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p LEFT OUTER JOIN q NOT INDEXED O
```

---

## Crash 288: `315b80ea189b0f69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256536`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p LEFT OUTER JOIN q NOT INDEXED ON TRUE != CURREN
```

---

## Crash 289: `c874763766d2f61e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256766`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (CURRENT_TIME, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 
```

---

## Crash 290: `a437456d2581b44c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257465`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(a REAL); INSERT INTO p DEFAULT VALUES; WITH p AS (VALUES (FALSE)) SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY -2696.9
```

---

## Crash 291: `48dd3f8055b3d206` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269085`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP COLLATE BINARY HAVING CUR
```

---

## Crash 292: `88aa5aa594d55c27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269240`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING quote(FALSE) ORDER
```

---

## Crash 293: `0b3ff1424c9b1cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269430`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING changes() ORDER BY
```

---

## Crash 294: `451eba2cce5ecf68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269480`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP HAVING CAST(CAST(CURRENT_
```

---

## Crash 295: `d94463db7a3a98bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000270882`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p CROSS JOIN (SELECT TRUE LIMIT FALSE) AS a NATURAL LEFT JOIN p WHERE TRUE BETWEEN NULL AN
```

---

## Crash 296: `ace24f4bec98415e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000272047`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE X'72dC24' GROUP BY TRUE ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL
```

---
