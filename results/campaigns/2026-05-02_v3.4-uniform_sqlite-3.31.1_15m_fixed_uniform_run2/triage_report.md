# Crash Triage Report

**Total crashes:** 161  
**Unique crash sites:** 161  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 161 | 161 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `46fb429366c6f203` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000296`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR ROLLBACK INTO s VALUES (CASE CURRENT_DATE COLLATE NOCASE WHEN CAST(c1 IS NOT json(CURRENT_DATE LIKE NULL ESCAPE NULL || FALSE) O
```

---

## Crash 2: `42885f680a5cf269` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000303`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, b, b, c3, c3); INSERT OR ROLLBACK INTO r VALUES (TRUE IS NOT NULL << NULL COLLATE RTRIM IS CASE WHEN RAISE(IGNORE) THEN +CURRENT_DATE IS NUL
```

---

## Crash 3: `1aee4ae82af88f09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000719`

```sql
SELECT printf('%llu', -1, ''); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 4: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001070`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 5: `f9569a608495527f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001416`

```sql
SELECT printf('%.*f', 9223372036854775807, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT INTO r (_rowid_, a) VALUES (NULL NOT IN (CAST(FALSE AS REAL)) | NOT ~FALSE AND js
```

---

## Crash 6: `a7798c9ce43c0fae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001874`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); SELECT CURRENT_DATE FROM q NATURAL JOIN p WHERE -FALSE GLOB CURRENT
```

---

## Crash 7: `8d47ba2ef9a137cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002031`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); SELECT CURRENT_DATE FROM q NATURAL JOIN p WHERE -FALSE GLOB CURRENT_DATE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 8: `7dbc94ccf945ba41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002047`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT p.*, t2.* FROM q AS j NATURAL JOIN p AS a WHERE CURRENT_TIMESTAMP | CURRENT_TIMESTAMP NOT B
```

---

## Crash 9: `3084149de3b70f4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002054`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(a NUMERIC); SELECT CURRENT_DATE FROM q NATURAL JOIN p WHERE -FALSE GLOB CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 10: `efcd1aa5baa9f991` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002060`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT
```

---

## Crash 11: `95028dee6014d1fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002066`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE -FALSE GLOB CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 12: `3dd86511d48dca1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002079`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); SELECT CURRENT_DATE FROM q NATURAL JOIN p WHERE CURRENT_DATE GLOB CURRENT_DATE; CREATE VIRTUAL TAB
```

---

## Crash 13: `55ed39b7dcdcbbf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002095`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN
```

---

## Crash 14: `d74f27f57db8bf3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002133`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO t1 VALUES (sum(CURRENT_TIME IS NOT DISTINCT FROM RAISE(IGNORE) = count(*) == CURRENT_
```

---

## Crash 15: `7139af2c8257a3bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002140`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 16: `b6a97838c85ea562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002337`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM r JOIN p vgups2__41_ ON TRUE; CREATE TABLE IF NOT EXISTS p(b INTEGER GENERATED ALWAYS AS (FALSE ->
```

---

## Crash 17: `89b474082ad86523` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002358`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); CREATE TABLE IF NOT EXISTS p(b INTEGER GENERATED ALWAYS 
```

---

## Crash 18: `178ddd33fd1b89c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002592`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*s', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *; SELECT printf('%.*e', 9223372036854775807, 1e308);
```

---

## Crash 19: `8afee7b3226d64f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002848`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); VALUES (CURRENT_DATE); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 20: `72aabaa0ee5a3999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003133`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE GLOB FALSE COLLATE NOCASE & EXISTS (WITH r (c3) AS (SELECT *) SELECT * FROM p NOT INDEXED LEFT
```

---

## Crash 21: `874188f539e0a4ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003174`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE & RAISE(IGNORE), *, NOT EXISTS (SELECT DISTINCT * FROM p WHERE CURRENT_DATE ORDER BY CURRENT_D
```

---

## Crash 22: `7d22dd9d0e2662ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003180`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE & EXISTS (SELECT *), *, NOT EXISTS (SELECT DISTINCT * FROM p WHERE CURRENT_DATE ORDER BY CURRE
```

---

## Crash 23: `08dedbcd63c39364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003187`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE & EXISTS (WITH p AS (VALUES (FALSE)) SELECT * FROM p NOT INDEXED LEFT JOIN p CROSS JOIN r WHER
```

---

## Crash 24: `de99dd940a207531` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003195`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_DATE & EXISTS (WITH r (c3) AS (SELECT *) VALUES (RAISE(IGNORE))), * FROM t1 NOT INDEXED; VALUES (CU
```

---

## Crash 25: `23c5fd92bd45a2b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003439`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME), c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF N
```

---

## Crash 26: `7728a2635d3dc160` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003488`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL, c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (FALSE) UNION VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 27: `768530a80aca93d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003642`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 28: `870fde1bf298aed7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005455`

```sql
SELECT printf('%d', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (FALSE || CURRENT_DATE NOTNULL OR FALSE IS NOT DISTINCT FROM +CURRENT_TIMEST
```

---

## Crash 29: `cbb548779537f719` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005671`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (~CAST(FALSE NOT IN (format('4V- ', CASE WHEN total_changes() THEN CURRENT_TIMESTAMP REG
```

---

## Crash 30: `be349840a6d7f6b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006915`

```sql
SELECT printf('%.*e', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q SELECT FALSE ORDER BY CASE NULL WHEN FALSE LIKE last_insert_rowid() * NULL IS NOT NULL THEN +l
```

---

## Crash 31: `552ce7756591620b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007935`

```sql
SELECT substr('cjKN X r8i___6--', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); INSERT INTO t2 VALUES (CURRENT_TIME COLLATE RTRIM IS DISTINCT FROM sum(CURRENT_TIMEST
```

---

## Crash 32: `f9324945412dea4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008075`

```sql
SELECT substr('-qdo', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT format('b- _  _K_-VJ ', CURRENT_TIMESTAMP) >= NOT EXISTS (VALUES (+TRUE) LIMIT CURRENT_TIME LIKE FALSE IS DIS
```

---

## Crash 33: `a87437b1c453e6a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008090`

```sql
SELECT printf('%.*s', -9223372036854775808, 1e-308); SELECT printf('%.*s', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT ALL * FROM q NOT INDEXED LEFT JOIN r
```

---

## Crash 34: `dc3b776bdb74aaf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008139`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR IGNORE INTO r VALUES (CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP LIKE CURRENT_TIME > FALS
```

---

## Crash 35: `f028da254f634cb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008254`

```sql
SELECT substr('dZ_--3-_ Sl6', -2147483648, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO t1 VALUES (-TRUE OR NULL NOTNULL IS NULL IS NULL
```

---

## Crash 36: `73b9cfe65dd09e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008337`

```sql
SELECT round(0.01, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR IGNORE INTO p VALUES (TRUE <> unicode(CURRENT_TIME) FILTER (WHERE CURRENT_DATE COLLAT
```

---

## Crash 37: `29ff549f327133b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008739`

```sql
SELECT substr('_28 5', 9223372036854775807, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CAST(CURRENT_DATE COLLATE RTRIM MATCH FALSE -> TRUE IS NOT FALSE AS FLOAT) % CURRENT_TI
```

---

## Crash 38: `4dc2ed11400d25b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 39: `26aba2aea13284ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009616`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 40: `d0ccf7372896480e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009651`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE, c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO s DEFAUL
```

---

## Crash 41: `94c8f2216f252a7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009756`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE, c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, _rowid_); SELECT q.* FROM r NA
```

---

## Crash 42: `973c9df9e29bdfc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010171`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (TR
```

---

## Crash 43: `dc2c170727f32605` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014073`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 44: `2d3731bf0e4a1df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014656`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE FALSE IN (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 45: `fcd7fcaa093bc053` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014806`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE 
```

---

## Crash 46: `da5699b9d0587749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015076`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME * CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 47: `e541a7771ad1c6b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015722`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE > FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 48: `ccc9693f2cd61b60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015964`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT FALSE ISNULL > FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 49: `f5c8b6939bea96f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016495`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT FALSE IS NULL > FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 50: `bf7c3baf9c3c824f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017536`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (+CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP < CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 51: `d4fc53ad44bf64ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018040`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE IS TRUE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `54bfb7eb83ef8537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018413`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE IS CURRENT_TIME COLLATE BINARY); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); E
```

---

## Crash 53: `35a250b5522d3a34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021261`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUE
```

---

## Crash 54: `51feeb8f0e397476` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022410`

```sql
SELECT substr('', -9223372036854775808, 4294967296); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 55: `30989641fb2b9204` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034928`

```sql
SELECT round(-1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 56: `b93e181c734e6916` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035144`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*g', 2147
```

---

## Crash 57: `d67d97c87063c317` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035292`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 58: `20b0fb36769fd8fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME), c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE OR sum(FALSE) FILTER
```

---

## Crash 59: `bedfb0634f6469e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036284`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE OR count(*) FILTER (WHERE TRUE)) INTER
```

---

## Crash 60: `1f724f08099c2cb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037310`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (FALSE)
```

---

## Crash 61: `86da58d8ed57ba69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037318`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (TRUE NOT IN (-NULL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VAL
```

---

## Crash 62: `bc3decde7b178e26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037332`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE TABLE IF NOT EXISTS q(rowid REAL NOT NULL DEFAULT -93.4E16); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QU
```

---

## Crash 63: `04dc9b6e8becb584` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037341`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (~CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 64: `ba809e1aac7ddfa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037355`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP); PRAGMA integrity_check; C
```

---

## Crash 65: `ccb623224e7493a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037390`

```sql
SELECT printf('%.*d', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 66: `0e8c28ce333e9314` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037419`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL DEFAULT ' FF-_T-c-- 9   v', a INTEGER NOT NULL DEFAULT 0); VALUES (CURRENT_TIMESTAMP); CR
```

---

## Crash 67: `f61dfb9ccdb84e15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037430`

```sql
SELECT printf('%.*g', 2147483647, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 68: `5c5b33e5fff3760b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039542`

```sql
SELECT round(0.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t3.*, FALSE IS DISTINCT FROM NOT NULL ->> CURRENT_TIMESTAMP IS NULL, FALSE, TRUE AS x1r479_1_7_1_l4_2v_x7___nw9_0
```

---

## Crash 69: `e284e0f47fdb0a14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039647`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2); SELECT NOT CURRENT_TIME ISNULL IS NULL / (SELECT * FROM q WHERE RAISE(IGNORE) * TRUE), last_insert_
```

---

## Crash 70: `6912a7c3924a1f21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041127`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS
```

---

## Crash 71: `fc7720ed58907525` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041281`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS
```

---

## Crash 72: `678566a60a8b5693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041981`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIME) UNION VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 73: `c713f7f8734ec188` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043622`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); SELECT * FROM p JOIN p a ON CURRENT_DATE IS NOT NULL IS NULL; CREATE V
```

---

## Crash 74: `04cb15ffb269a55d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048430`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 75: `fcf4c1d146e6f8f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048912`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE FALSE; SELECT printf('%.*f', 2
```

---

## Crash 76: `0342322610bd8741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049578`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; SELECT substr('', -2147483649, 2147483647); CREATE VIRTUAL TABLE 
```

---

## Crash 77: `86cd9962b0a3d55d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051149`

```sql
SELECT printf('%.*s', -1); SELECT substr('M_ - - _gl07', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, c2, c2); SELECT (CURRENT_TIMESTAMP) >= +NULL AS ti__hp___5p7v
```

---

## Crash 78: `c03cd3cc21a7fef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051997`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); WITH RECURSIVE s AS (WITH RECURSIVE p (c1) AS NOT MATERIALIZED (SELECT c1, (CURRENT_DATE) IS NUL
```

---

## Crash 79: `ec2a6707f71e9249` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052768`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); INSERT OR REPLACE INTO p VALUES (changes()); EXPLAIN QUERY PLAN VALUES (NULL); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 80: `880bf86789551ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052935`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES ((random())); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); E
```

---

## Crash 81: `61037accaa1d845c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054435`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 82: `e12756fe39761a3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055227`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (NULL); SELECT printf('%
```

---

## Crash 83: `5110582a6b09219c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055911`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT count(*) AS i FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 84: `536b718d99f1e1ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056086`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPL
```

---

## Crash 85: `b63b77fb8bf8a4c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057914`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 86: `f29af9eb88f9c55f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064112`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); VALUES (CURRENT_TIME) UNION SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME DESC NULLS FIRST; SELECT print
```

---

## Crash 87: `d5ff75013667222c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064869`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 88: `7a7abaa1c9ca0d37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065278`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); SELECT DISTINCT *, * FROM q WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 89: `a8cf4ec422343fee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068235`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CAST(TRUE NOT IN (TRUE, CURRENT_TIMESTAMP) AS REAL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 90: `5adf3655078960b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (NULL) ON CONFLICT(c3) DO UPDATE SET rowid = FALSE; PRAGMA quick_c
```

---

## Crash 91: `5775055b31a18f2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068289`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (NULL NOT LIKE FALSE), c2 NUMERIC PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN QUERY PLAN VA
```

---

## Crash 92: `e20d9e4b2c669948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068299`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (NULL + CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN QUERY PLAN V
```

---

## Crash 93: `62aaeae5832fa811` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068315`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES ('' < CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN QUERY PLAN
```

---

## Crash 94: `09577e4fdbf3c663` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME), c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (c1)); SELECT printf('%.*f', 21474
```

---

## Crash 95: `b21ace20e4208a32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069732`

```sql
SELECT round(0.0, 9223372036854775807); SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p SELECT DISTINCT * FROM p NATURAL LEFT JOIN ((q AS u LEFT O
```

---

## Crash 96: `411d9e494e8a16a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070658`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 97: `1207d301ef2e84d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071002`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a + -13) NOT NULL UNIQUE); REPLACE INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT I
```

---

## Crash 98: `05e88e78be234e64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071082`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); REPLACE INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * F
```

---

## Crash 99: `740cfaf921c9d7b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071101`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 100: `97c26e4cd42a1d9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071546`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p VALUES (~FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 101: `bdba0ff9dd2edd82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072176`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); WITH RECURSIVE p AS (VALUES (TRUE)) INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (NULL); CR
```

---

## Crash 102: `5e878098bdfcc22f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072239`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); WITH RECURSIVE p AS (VALUES (TRUE)) INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (NULL); CR
```

---

## Crash 103: `cfcc627e59935984` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072410`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 104: `b6e27c65bea7a1c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072715`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a REAL P
```

---

## Crash 105: `a15f86d2c7ddf27a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072772`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); WITH p AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIMESTAMP); SELECT ALL * FROM p AS p_9yc_ye82_85za
```

---

## Crash 106: `ca97dbed04537b16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073033`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC UNIQUE); WITH p AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIMESTAMP); SELECT ALL * FROM q AS jr8__f2rp_kr88_
```

---

## Crash 107: `1e72cd6d775e51cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080996`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CURRENT_TIME), c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE NULL GROUP BY TRUE WINDOW w1 AS (); SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 108: `2cf5b85106ede42b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081151`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE NULL GROUP BY TRUE WINDOW w1 AS (); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 109: `f79eee46b10197de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092597`

```sql
SELECT printf('%lld', -9223372036854775808, '6qZ 8__'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP AS a, RAISE(IGNORE) IS NOT NULL IS NOT NUL
```

---

## Crash 110: `c7232b2e8371bf1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103816`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (CAST(TRUE AS INT) IS CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 111: `d1875454a3844a19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104422`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_
```

---

## Crash 112: `b8673a0d886d3a3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104666`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE IS CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DE
```

---

## Crash 113: `f1e89eed1a93b9f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104827`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a = 6742) NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 114: `bb0ffc5df458634a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104988`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a = 6742) NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 115: `2c2d51c2f5519039` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106680`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT NULL NOTNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 116: `d1d456a8af2edda8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106850`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 117: `c81e3253832ecb5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107280`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME OR TRUE IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 118: `664ce988871aaaac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107466`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE >= CURRENT_TIME OR TRUE IS NULL; CREATE VIRTUAL TABLE IF N
```

---

## Crash 119: `2e1825a8f2468819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107778`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE TRUE COLLATE NOCASE IS NULL; SELECT printf('%u', 9223372036854775807, '
```

---

## Crash 120: `1e60cd09f9770809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108562`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE _rowid_ IS NULL > FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 121: `6b6879e07d3f313c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109242`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP MATCH CURRENT_TIMESTAMP; SELECT printf('%.*f', 214748
```

---

## Crash 122: `054293d753a547a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110231`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (EXISTS (VALUES (TRUE)) COLLATE NOCASE < count(*) FILTER (WHERE CURRENT_TIME) BETWEEN RAISE(IGNORE
```

---

## Crash 123: `6bb96ee2a122ac34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110697`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE _rowid_ ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 124: `590930767d36724a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110828`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE _rowid_ IS NOT NULL ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 125: `c0aab99bcd1d0b82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111018`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT -0); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 126: `90349b432a579edb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111139`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 127: `99c7339cb41dc7eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111146`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 128: `0dc7f89eff71c5fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112236`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT -91251); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); E
```

---

## Crash 129: `92ccbd334ca36ccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112510`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, c2 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAUL
```

---

## Crash 130: `0e39dd159dbe466d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113765`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (RAISE(IGNORE)), c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 131: `958d030ec07b5e4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114093`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE TRUE <= CURRENT_DATE AND CURRENT_DATE LIKE TRUE COLLATE BINARY; CREATE 
```

---

## Crash 132: `1d213022642fb8d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114279`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE TRUE <= CURRENT_DATE AND CURRENT_DATE COLLATE NOCASE LIKE TRUE IS NOT N
```

---

## Crash 133: `21b3cde879250f8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115176`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL DEFAULT FALSE, rowid VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 134: `591bbd7f55da4731` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116496`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _r
```

---

## Crash 135: `045a8d04228e5cb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117275`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB); SELECT NOT EXISTS (SELECT DISTINCT * FROM p WHERE CURRENT_DATE ORDER BY CURRENT_DATE ASC NULLS LAST LIMIT TRUE) FR
```

---

## Crash 136: `429b5c7f5dca3818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118044`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT *, * FROM q WHERE NULL LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 137: `df966b73f2d73435` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119346`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM q WHERE NULL LIMIT -CURRENT_DATE); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 138: `03017d8f47604455` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124487`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_TIME))))))) ON CONFLICT DO NO
```

---

## Crash 139: `f35d0901f03dc8ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124731`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE)) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 140: `0c55921fe2216967` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125388`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (NULL))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); EXPLAIN 
```

---

## Crash 141: `38e65f9db6531744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125547`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIME))); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 142: `c31b5a14a0fda2a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126285`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INSERT INTO p VALUES (FA
```

---

## Crash 143: `6a4f66c9a344c3c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130800`

```sql
SELECT printf('%.*g', 2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE NOTNULL); CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 144: `f3502f91f5f72533` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131475`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE / CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01)
```

---

## Crash 145: `25b922002bc0ed10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133329`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE, c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p 
```

---

## Crash 146: `e4de52bcc0f5c4c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134365`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CAST(FALSE AS BLOB)))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 147: `04d3899ba284ee72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_DATE))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, 
```

---

## Crash 148: `e481f7e57a320c9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134617`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 149: `a02e4e2bd13dbf20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135663`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p VALUES (CURRENT_DATE IN (' k9-3fPI-o-_sD')) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 150: `18bd532560d4bb9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143070`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP - CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 151: `db188fa1ce080fa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146793`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (NULL) STORED, c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME * CURREN
```

---

## Crash 152: `4e12a8536b5359db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147177`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 153: `b34a91bc9adc7f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147726`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE ' k9-3fPI-o-_sD'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 154: `12550e7d54e92c72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147889`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME < CURRENT_TIMESTAMP COLLATE NOCASE; CREATE VIRTUAL TABLE I
```

---

## Crash 155: `e42dd63ba4d650dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148345`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE NOT FALSE > FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 156: `8775c84874b01178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148482`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT max(CURRENT_DATE) AS ec0_6_716e73_0_r_x__3i3r0_m_5cn_2o_2u_0__8a09zri_60_d7gd1__8xbh5u167_4b4_9___352
```

---

## Crash 157: `ca82b2259186e013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150614`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE RAISE(IGNORE) < NULL AND RAISE(IGNORE) OR TRUE; CREATE VIRTUAL TABLE IF
```

---

## Crash 158: `bac83d014d219ef8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151336`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT GENERATED ALWAYS AS (CAST(TRUE AS INT)) STORED, _rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT * FROM p NATURAL JOIN p WHERE NOT FALSE IS NULL > FA
```

---

## Crash 159: `427eb2423e165b15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151678`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b GENERATED ALWAYS AS (a * a) NOT NULL); INSERT INTO p VALUES (~CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 160: `d58412f0880fa6c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152342`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SE
```

---

## Crash 161: `e22f838e187be69b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153218`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); INSERT OR ROLLBACK INTO p VALUES (FALSE IS FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---
