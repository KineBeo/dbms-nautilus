# Crash Triage Report

**Total crashes:** 142  
**Unique crash sites:** 142  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 141 | 141 | 99% |
| Signal | 1 | 1 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `57244cbe6623d8a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO q VALUES (CASE WHEN total_changes() FILTER (WHERE json_array(EXISTS (VALUES (RAISE(IGNORE)) ORDER BY FALSE ASC)) FILTER
```

---

## Crash 2: `28207f7361493089` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000012`

```sql
SELECT printf('%.*e', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE (SELECT CURRENT_TIMESTAMP FROM p INDEXED BY c2 LIMIT NOT EX
```

---

## Crash 3: `709a5eabe90c7d08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000272`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); SELECT CASE WHEN NOT NULL THEN CURRENT_TIME END >> CURRENT_TIMESTAMP >> CURRENT_TIME ->> CURRENT_TIME NOTNULL -> CURRENT_TIME || NOT CURRE
```

---

## Crash 4: `2a637284c65246a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000656`

```sql
SELECT printf('%s', 1, 'z_G-_ic'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q VALUES (-NULL NOT LIKE CURRENT_TIME NOT NULL ->> NOT TRUE > CURRENT_DATE LIKE CASE WHEN 
```

---

## Crash 5: `c28fc4c4806bd353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001785`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO q VALUES (-FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 6: `98ab8ab883b51a91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002193`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 TEXT PR
```

---

## Crash 7: `6f3576e8296e33a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002663`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIMESTAMP IS DISTINCT FROM NULL ->> CASE RAISE(IGNORE) WHEN CURRENT_DA
```

---

## Crash 8: `2c544574d3ba95d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY NOT EXISTS (VALUES (CURRENT_TIME)) DESC, CURRENT_DATE ASC NULLS LAST; PR
```

---

## Crash 9: `853931f42459b18a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002842`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_)
```

---

## Crash 10: `278b9a07b64a6cdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE DESC, CURRENT_DATE ASC NULLS LAST; PRAGMA integrity_check; CREATE V
```

---

## Crash 11: `aa168093817ca3b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002863`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIMESTAMP IS DISTINCT FROM NULL ->> CASE RAISE(IGNO
```

---

## Crash 12: `6e4538a0037111b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002892`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, FALSE NOTNULL NOT IN (NULL, CURRENT_TIMESTAMP) BETW
```

---

## Crash 13: `15a642323c16e4c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002969`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (FALSE, CURRENT_TIMESTAMP)
```

---

## Crash 14: `e84b6d7b73537c9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002994`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 15: `bf71553af92adf6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003001`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIME ASC NULLS LAST; PRAGMA integrity_check
```

---

## Crash 16: `2ef108f275d31efa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003008`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (TRUE) BETWEEN TRUE MATCH 
```

---

## Crash 17: `da53e9328d13b64a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003050`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY NULL ASC NULLS FIRST; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 18: `bddeb4b2df74cec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003330`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_TIMESTAMP & CAST(CURRENT_TIME AS REAL)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIR
```

---

## Crash 19: `85041e5b59337503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003409`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_TIMESTAMP & CAST(CURRENT_TIME AS REAL)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TAB
```

---

## Crash 20: `beeac3d96513b2df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003416`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELE
```

---

## Crash 21: `3bf9e9820021103a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003422`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 22: `933641f7009e25d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003429`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 23: `871e4765f8a9b1fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003448`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT q.* FROM (SEL
```

---

## Crash 24: `33a6e3e47d253a5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004113`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); VALUES (CURRENT_TIME IS NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p AS MATERIALIZED (SELECT t2.*), q AS NOT MATERIAL
```

---

## Crash 25: `5452d97f44880847` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006722`

```sql
SELECT substr('_-4-kM __CI9', -9223372036854775808, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT FALSE ISNULL != RAISE(IGNORE) == CURRENT_TIME IS NOT DISTINCT FROM FA
```

---

## Crash 26: `f3f36a34d10dd494` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006770`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIMESTAMP > CURRENT_DATE IS NOT DISTINCT FROM ~~rowid IS DISTINCT FROM ~RAISE(IGNORE) -> +RA
```

---

## Crash 27: `3839d6e640121dc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006958`

```sql
SELECT substr(' __-', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO s VALUES (FALSE -> NULL != FALSE NOT LIKE NULL * -CURRENT_TIMESTAMP, RAISE(IGNORE) -> C
```

---

## Crash 28: `bd6f5f6427ccf510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007004`

```sql
SELECT printf('%.*f', -2147483649, 1e308); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 DATE, c2 GENERATED ALWAYS AS (a || b) NOT NULL, a VARCHAR(255) GENERATED ALWAYS AS (NOT EX
```

---

## Crash 29: `354f4560763d1b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007156`

```sql
SELECT printf('%.*g', -2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP IS NULL << -~CURRENT_TIMESTAMP IN (FALSE) LIKE CASE 
```

---

## Crash 30: `7b367db7c8cfa450` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007173`

```sql
SELECT round(1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO t3 VALUES ((NOT EXISTS (VALUES (CURRENT_DATE) UNION SELECT DISTINCT p.* FROM (q INDEXED BY c2))) <
```

---

## Crash 31: `5f7b5767922f34d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010852`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 32: `ed98713b5dc510df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010860`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT E
```

---

## Crash 33: `5d49a9ea3bc3b972` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014419`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT CURRENT_TIMESTAMP, c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CRE
```

---

## Crash 34: `ca1fc8ac00817cdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018360`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 35: `8596f4d81890c82a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018834`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE, b VARCHAR(255) UNIQUE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM q NATURAL JOIN p WHERE CURRENT
```

---

## Crash 36: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021501`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 37: `1ad9ee96beeb957e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021753`

```sql
SELECT substr('__--B', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (C
```

---

## Crash 38: `2900baf8986e740b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024648`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, a, c1); IN
```

---

## Crash 39: `4d5d2f6dd669b034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024702`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)
```

---

## Crash 40: `1ae6e8f8e839457c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024715`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)
```

---

## Crash 41: `13d30650ff1774a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024811`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)
```

---

## Crash 42: `d79b1232791b82df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025908`

```sql
SELECT substr('1 4F84 V5 R MVZ', 2147483647, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 43: `5e1e1d6dea638d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026921`

```sql
SELECT printf('%.*g', -2147483649, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 44: `e5327968f7cabb8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027240`

```sql
SELECT printf('%f', 9223372036854775807, 'f2_2 r90_1'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 45: `d923d127d9ab1999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027419`

```sql
SELECT printf('%x', -1, 'ZL9_-j o'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q AS NOT MATERIALIZED (VALUES (TRUE LIKE CURRENT_TIMESTAMP, FALSE NOTNULL NOT NULL) LIMIT 
```

---

## Crash 46: `e5e9a8b9e6646d59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027803`

```sql
SELECT printf('%.*d', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 47: `4481922a306a53d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028552`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (FALSE), _rowid_ NUMERIC CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREAT
```

---

## Crash 48: `f31b3d55937385c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028562`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES;
```

---

## Crash 49: `d1e6e9c599bd8be9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028576`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (~X'BfFCCd2aaf')); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEF
```

---

## Crash 50: `db670280e3915575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028586`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CASE CURRENT_TIME NOT IN (CURRENT_TIMESTAMP) WHEN FALSE GLOB CURRENT_DATE THEN NULL END)); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 51: `490f5d764f17f2d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028601`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; 
```

---

## Crash 52: `4dde662a41218e22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028657`

```sql
SELECT substr('', 9223372036854775807, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 53: `12e8d79fe0fc60f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029135`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE))); EXPLAIN QUERY PLAN 
```

---

## Crash 54: `5c2f9bd76295f831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029187`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex(zeroblob(0
```

---

## Crash 55: `098b705a43e00f6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (FALSE NOT IN (VALUES (CURRENT_DATE))); VALUES (FALSE); CREATE VIRTUAL 
```

---

## Crash 56: `4b1f83d80e1dfb39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031267`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT (NULL NOT NULL) = NOT RAISE(IGNORE) COLLATE NOCASE AS a FROM q NOT INDEXED LEFT JOIN r NOT INDEXED EXCEPT SELECT DI
```

---

## Crash 57: `db84b32c97433228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031541`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT INTO p VALUES (CURRENT_DATE / FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 58: `54eaef651d43ff9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032654`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO r DEFAULT VALUES; SELE
```

---

## Crash 59: `1453c6ee74037077` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034170`

```sql
SELECT printf('%.*f', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 60: `4cefa540dc6fcb05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036696`

```sql
SELECT printf('%.*g', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO q VALUES (FALSE, total_changes()); ANALYZE t3; CREATE TABLE IF NOT EXISTS p(b IN
```

---

## Crash 61: `769e7dc93e777f43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036797`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q VALUES (FALSE) EXCEPT SELECT ALL TRUE FROM p ORDER BY TRUE ASC NULLS FIRST; PRAGMA integrity_check; C
```

---

## Crash 62: `3fb421d166a4aadd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037486`

```sql
SELECT printf('%.*s', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 63: `708777946f938bfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040810`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *; SELECT hex(zerobl
```

---

## Crash 64: `a0985574e63c5df3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041236`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT
```

---

## Crash 65: `f5a9e2fb01839ff1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042682`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CASE CURRENT_DATE WHEN FALSE THEN TRUE END)); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT I
```

---

## Crash 66: `ae45e4a13b55db18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043799`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIME); VALUES (NULL); SELECT printf('%.*g', -21474836
```

---

## Crash 67: `de4643b37e2fc55c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044911`

```sql
SELECT substr('m_', -9223372036854775808, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (_rowid_, c3) VALUES (CURRENT_TIME IS NULL) ON CONFLICT(a) DO UPDATE SET c2 = -TRUE
```

---

## Crash 68: `113380929c2081a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045291`

```sql
SELECT printf('%.*e', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; ANALYZE r; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT
```

---

## Crash 69: `0c57b9335f42437d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045608`

```sql
SELECT printf('%.*g', 2147483647, 1e308); SELECT printf('%.*g', 9223372036854775807, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t3 DEFAULT VALUES; SELECT *, * FROM q 
```

---

## Crash 70: `d4dafab2f48c9788` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045836`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r VALUES (CURRENT_DATE, CAST(NULL NOTNULL COLLATE RTRIM AS REAL) NOTNULL, NOT CURRENT_T
```

---

## Crash 71: `1b3870f439a188db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045963`

```sql
SELECT printf('%.*s', 4294967295, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT RAISE(IGNORE) % (CURRENT_TIME) COLLATE NOCASE AND CURRENT_TIME NOT IN (RAISE(IGNORE) * CURRE
```

---

## Crash 72: `31a5e1d99db55142` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047466`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p VALUES (NULL COLLATE NOCASE COLLATE BINARY > TRUE COLLATE RTRIM IS CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 73: `08732ef7bede6841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047488`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p VALUES (CURRENT_TIME COLLATE RTRIM IS CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSER
```

---

## Crash 74: `18727be69900c489` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047494`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT INTO p VALUES (CURRENT_TIMESTAMP > TRUE COLLATE RTRIM IS CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 75: `fdd5a1f1ca31d4eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047649`

```sql
SELECT printf('%f', 0, '4_2 4-360g YS_0-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, t1.* FROM t2 WHERE EXISTS (SELECT p.*, FALSE AS m__ikd FROM q , p EXCEPT SELECT * FROM (
```

---

## Crash 76: `95bff8d4e4ef093b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049737`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIME); SELECT DISTINCT * FROM p EXCEPT SELECT ALL TRU
```

---

## Crash 77: `dd07078cbcab8113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049897`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); C
```

---

## Crash 78: `7d15b80e8892bdc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049913`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); C
```

---

## Crash 79: `60815860dbb2c523` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051155`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CASE 00653978183318578605784496614147794398296189100798746440219602569011195400755183321322527555095703278688030079160680273374236611162523134412227769771062
```

---

## Crash 80: `939437281a458ea3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052186`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CASE CURRENT_TIME NOT IN (X'FaBCCf') WHEN FALSE THEN NULL END)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('
```

---

## Crash 81: `5d1f1aef27b42196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052451`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (CASE CURRENT_TIME NOT IN (NULL) WHEN FALSE THEN NULL END)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f'
```

---

## Crash 82: `54072ec4ca77aaad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059257`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, a, c3); SELECT CASE CURRENT_TIMESTAMP WHEN RAISE(IGNORE) THEN CURRENT_TIME -> RAISE(IGNORE
```

---

## Crash 83: `cb5f956154ad5b9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060771`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q VALUES (FALSE) EXCEPT SELECT ALL TRUE FROM q NATURAL JOIN q ORDER BY TRUE ASC NULLS FIRST; PRAGMA int
```

---

## Crash 84: `9e5c64c940e8b73b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062692`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT TRUE FROM p; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 85: `bc4060659d75a3a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062716`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT * FROM p; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 86: `44d83c667e363dc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064660`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL X'Ab' FROM p ORDER BY FALSE DESC NULLS LAST; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 87: `727d269d7550af4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066867`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (TRUE IS NOT TRUE) ASC NUL
```

---

## Crash 88: `2734caa812b750bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067704`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL count(*) OVER () AS a FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP DESC NULLS LA
```

---

## Crash 89: `1af6680a1dd430ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067977`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (FALSE IS NOT FALSE) ASC N
```

---

## Crash 90: `9aa4c36ec2b526b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068091`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO q SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST, CURRENT_TIMESTAMP NOT IN (CURRENT_TIME) ASC NULLS L
```

---

## Crash 91: `673afccaca677ae0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068584`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT 's_-7 - S- 1-  '); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 92: `4c27c8c89174318e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072165`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT INTO p VALUES (CURRENT_DATE / CAST(CURRENT_TIME AS REAL)); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 93: `73cc29f95318c8a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072444`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT INTO p VALUES (CAST(CURRENT_TIME AS BLOB)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO 
```

---

## Crash 94: `8a0af70e51fbcfa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073312`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT INTO p VALUES (CAST(CURRENT_TIME AS VARCHAR(255))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSER
```

---

## Crash 95: `d165090e65f8f4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073551`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); INSERT INTO p VALUES (CAST(CURRENT_TIME AS INTEGER)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT IN
```

---

## Crash 96: `0b98ca11e35bdffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074020`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT X'dDEc'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 97: `6e05435ddba3759f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076149`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE NOT IN (VALUES (FALSE))); EXPLAIN QUERY PLAN SELECT * FROM q WHER
```

---

## Crash 98: `030c98ace30a95df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077872`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NATURAL LEFT JOIN p NOT INDEXED; CREATE VI
```

---

## Crash 99: `ebfa363cebeb6c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077962`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_DATE))); SELECT ALL * FROM p NATU
```

---

## Crash 100: `11e328296199886e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT 
```

---

## Crash 101: `6d114c25c42beaff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080523`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, _rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSE
```

---

## Crash 102: `d792d994df31be31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080540`

```sql
SELECT printf('%s', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO r DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 103: `83982fd483a98bbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080567`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE) INTERSECT SELECT ALL TRUE FROM p ORDER BY TRUE ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 104: `72439096ce8ed7f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080593`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT ''); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 105: `d5705f21485055fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082042`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP & CURRENT_TIMESTAMP); SELECT ALL count(*) FILTER (WHERE NULL) OVER () FROM p; CREATE VIRTUAL TABLE
```

---

## Crash 106: `3883868923632fec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084622`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN WITH p AS (VALUES (CURRENT_TIMESTAMP)) VALUES (TRUE); CREATE VIRTUAL TABLE IF
```

---

## Crash 107: `1b95adf4d4bec46b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094857`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); I
```

---

## Crash 108: `a714a26c667a7a4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105356`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CURRENT_DATE <= FALSE; CREATE VIRT
```

---

## Crash 109: `ccca038a201de60a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106597`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON FALSE BETWEEN TRUE AND NULL; CREAT
```

---

## Crash 110: `ec2a5397b77c89fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107310`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON TRUE GLOB CURRENT_DA
```

---

## Crash 111: `a08d398c92bd453a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107453`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CURRENT_TIMESTAMP; C
```

---

## Crash 112: `0b3fb190b2f4079a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107662`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE, b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t
```

---

## Crash 113: `c0ae186459b21ed2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108000`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CAST(FALSE AS BLOB);
```

---

## Crash 114: `3408f228e59cb0f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108150`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON TRUE; SELECT printf(
```

---

## Crash 115: `1c254a947a7aab4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108194`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CAST(FALSE AS BLOB) 
```

---

## Crash 116: `2df366cc85b7a715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108366`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CAST(FALSE AS BLOB) 
```

---

## Crash 117: `56a53769550ee20b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108608`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CURRENT_TIME == FALS
```

---

## Crash 118: `4265b3dcd94217f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108805`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CURRENT_TIME; CREA
```

---

## Crash 119: `528c86b65fe589e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109048`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT NULL NOT BETWEEN NULL AND CURRENT_TIMESTAMP; SELECT printf('%.*g', -2147483649,
```

---

## Crash 120: `58dd379ba1ddc502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109583`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME << NULL OR TRUE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 121: `5baa29fb7093252e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109885`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (CURRENT_TIME LIKE FALSE ESCAPE CURRENT_TIMESTAMP <= CURRENT_TIME NOT IN (FALSE))); INSERT INTO p DEFAULT VA
```

---

## Crash 122: `8844d84ee579acb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110230`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (~NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 123: `873df533fe4e035e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110534`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (FALSE + TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 124: `cf758d5a8cd6f012` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111090`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (CURRENT_TIME LIKE FALSE ESCAPE CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 125: `8b5409b7c6134d79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111515`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INT NOT NULL DEFAULT 0); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 126: `baf9e65612561b28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111693`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 127: `ba4a7132e7ffa1f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113809`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY, c1 DATE UNIQUE, c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 128: `d43fbe6f643215dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120273`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT -08393053159870536600987341399493247135611369695625486718445753338051447219065546586829949668217774578013523505881351114083042833784037346835693.90
```

---

## Crash 129: `4fe05939749b8af8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120395`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 130: `d27e19079a23146d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120534`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL DEFAULT X'D62d9f'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 131: `d1821e0054bf413f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); R
```

---

## Crash 132: `6fbcaadbccae3fae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (-3467478.255391747723423611470341875516449787516049021372600263993835074918358287220632e8862316024690925249
```

---

## Crash 133: `07a264bf128686ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122281`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (~NULL)); INSERT INTO q VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 134: `d69d35099aebf06a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122424`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE PRIMARY KEY); INSERT INTO q VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 135: `d9c2cf9251677b64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (CURRENT_DATE)); INSERT INTO q VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 136: `493c0f7aba3b0692` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122691`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME OR FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 137: `ab2e290cf33dac40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122852`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a INT); CREAT
```

---

## Crash 138: `d4a9237933ef4c81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122947`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMA
```

---

## Crash 139: `732557f94d9d8e3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123278`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON CURRENT_TIME == FALS
```

---

## Crash 140: `99ab5a3abb995e23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123523`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON TRUE - CURRENT_TIMES
```

---

## Crash 141: `6e53eb26b1ebbaf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125046`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p JOIN p k5u38f31__4__h9335v6wn2n3_n__r_3x2e6_l__z5_v4t ON FALSE BETWEEN CURRENT_DATE COLLATE
```

---

## Crash 142: `0ec99606fd930d6c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000080446`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); SELECT (SELECT * EXCEPT SELECT * FROM (SELECT p.*, q.* FROM (p NOT INDEXED) WHERE FALSE GROUP BY EXISTS (SELECT * FROM p NOT INDEXED ORDER 
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  sqlite3SrcListDelete
  clearSelect
```

---
