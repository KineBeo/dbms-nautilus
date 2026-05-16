# Crash Triage Report

**Total crashes:** 321  
**Unique crash sites:** 321  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 321 | 321 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9f4f42e715cbb38e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(0)); SELECT printf('%.*f', -1, 1e308);
```

---

## Crash 2: `3e4f30d86b471678` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000303`

```sql
SELECT printf('%.*f', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (NOT EXISTS (SELECT ALL t2.*, p.*, CURRENT_TIME != CURRENT_TIME <> randomblob((CURRENT
```

---

## Crash 3: `43c6287a0747fe97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000413`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT OR ROLLBACK INTO p VALUES (coalesce(CURRENT_DATE NOTNULL, CAST(TRUE COLLATE BINARY AS VARCHAR(255)) COLLATE NOCASE NOT NULL - RAISE(
```

---

## Crash 4: `6b3e9ec6a957f0f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000487`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_TIME << -RAISE(IGNORE) ISNULL * RAISE(IGNORE) BETWEEN TRUE COLLATE NOCASE AND NOT EX
```

---

## Crash 5: `693bf0ac3641b4d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000693`

```sql
SELECT round(-1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT ALL * FROM p NOT INDEXED INTERSECT WITH t1 (_rowid_) AS (VALUES (NULL) EXCEPT SELECT count(NOT c2 IN (CURRENT_TI
```

---

## Crash 6: `bcb352e49ab5e643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000858`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY, c1 TEXT GENERATED ALWAYS A
```

---

## Crash 7: `ee84eb3f7746be8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000964`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, b, c2); WITH RECURSIVE q (c1) AS (SELECT * FROM p WHERE NULL IS NOT NULL INTERSECT SELECT CURRENT_DATE AS apy_2_z_33_b55xba5 FROM p NO
```

---

## Crash 8: `05ba25eec390fd26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001489`

```sql
SELECT round(1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIME = RAISE(IGNORE) LIMIT CURRENT_TIMESTAMP OFFSET 
```

---

## Crash 9: `3c99f16c5662a1b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001667`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_DA
```

---

## Crash 10: `cdb1da8251f905c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001724`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_DATE)); SELECT printf('%.*g', 2147483647, -1.0)
```

---

## Crash 11: `d1853ccee6ad5e7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001872`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE q (c1) AS NOT MATERIALIZED (SELECT *) SELECT CURRENT_TIM
```

---

## Crash 12: `72bd511a008eb3af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003966`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -1); CREATE VIRTUA
```

---

## Crash 13: `2e602971d4df8219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004191`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (char(FALSE ISNULL + RAISE(IGNORE) -> TRUE) FILTER (WHERE NOT EXISTS (VALUES 
```

---

## Crash 14: `70d946ee832a27fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004588`

```sql
SELECT printf('%.*g', 9223372036854775807, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT p.* FROM q WHERE NOT r.c2 
```

---

## Crash 15: `83f994b637d758e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005356`

```sql
SELECT substr('-Z__--   _-z_0y-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT q.* FROM p NATURAL JOIN p WHERE CASE -EXISTS (WITH RECURSIVE s (a) AS NOT MATERI
```

---

## Crash 16: `27fa72974edbd4ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006665`

```sql
SELECT round(1e-308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES ((_rowid_ IS NOT NULL GLOB (VALUES (CURRENT_DATE) UNION ALL SELECT * ORDER BY -total_cha
```

---

## Crash 17: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006881`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 18: `40ae6160554068bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007174`

```sql
SELECT substr('N', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 19: `f5794eaa9e02aa0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008966`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 20: `1d2931f34fa36d81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009075`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 21: `af6572b2a46d64ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009361`

```sql
SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t2 AS NOT MATERIALIZED (WITH r AS (VALUES (CURRENT_TIME AND FALSE | CURRENT_DATE ISNULL, +F
```

---

## Crash 22: `c6b840b2fd3fe087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010001`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) VALUES (TRUE BETWEEN NULL AND TRUE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 23: `6c4fca10d458e012` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010752`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA q
```

---

## Crash 24: `1dfb222d56e4f2c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011140`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (C
```

---

## Crash 25: `a87f43fef24387fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011618`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 26: `cb60202be702ee87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012709`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT -8924452317879851823898241228736954083865352873180757735316350977165244433988912531968517155798008660298357046156575753668.11e3094497603495556); CR
```

---

## Crash 27: `d3b0fa007feef9b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012795`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 28: `864ce809b0ce92fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013102`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE VIR
```

---

## Crash 29: `7e7e158d4adea4f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013186`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL)
```

---

## Crash 30: `a1b9fec8082c0642` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018656`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 31: `b0a51612ad2853b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018802`

```sql
SELECT printf('%.*d', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 32: `a2a3e96fd39c18bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021747`

```sql
SELECT printf('%d', -1, ''); SELECT substr(' -2    _1tg', 1, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.c1 << NOT EXISTS (SELECT r.* FROM p UNION SELECT 
```

---

## Crash 33: `9e9c4362520cdccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022047`

```sql
SELECT printf('%f', 9223372036854775807, 'IJ94_ o-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT hex(zeroblob(21
```

---

## Crash 34: `f958ed6577416cfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022607`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, a NUMERIC UNIQUE, b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 35: `ad5e299a2fa15760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022779`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 36: `ea0859f6662f3f72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025865`

```sql
SELECT substr('', 2147483648, 2147483647); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 37: `d465eda6fd01e33e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026639`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQ
```

---

## Crash 38: `768629bbf5d023da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027313`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIME IS TRUE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO
```

---

## Crash 39: `86ee8e025ccfca95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027626`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (
```

---

## Crash 40: `8265a770d61015e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027826`

```sql
SELECT substr('_PR- m J9192_jR__', -9223372036854775808, 4294967296); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 41: `e541ddf5cf60281d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028304`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p a ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAU
```

---

## Crash 42: `08f709b6d460993e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030337`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (CURRENT_DATE COLLATE RTRIM IS CURRENT_TIMESTAMP); VALUES (
```

---

## Crash 43: `67435f14ff73ec43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030616`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (~CURRENT_DATE COLLATE RTRIM IS CURRENT_TIMESTAMP); VALUES 
```

---

## Crash 44: `a71f5548246d15ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034469`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE > TRUE IS NULL & TR
```

---

## Crash 45: `23be77c2f1b8369a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034939`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS LAST)
```

---

## Crash 46: `07732b3f3658c3c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034945`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_DATE & TRUE ORDER BY FALSE DESC NULLS LAS
```

---

## Crash 47: `507b888e438b6ee8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035613`

```sql
SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (c2, rowid) VALUES (NULL) ON CONFLICT(c1) DO UPDATE SET b = NOT CASE EXISTS (VALUES (CURRENT
```

---

## Crash 48: `892ddec9e53c40c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036415`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM p WHERE TRUE ORDER BY NULL DESC NULLS LAST); CREATE VIRTUAL
```

---

## Crash 49: `f2215db26194c8a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040198`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT
```

---

## Crash 50: `ca6bfab774d1a052` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040235`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT
```

---

## Crash 51: `89d0bc76b409ace8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041079`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 52: `bcf3ea1ba0418244` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); E
```

---

## Crash 53: `4c5ec40146777fd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048540`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(NULL)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO 
```

---

## Crash 54: `91fbd47e237ac3a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048831`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (changes()) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s 
```

---

## Crash 55: `a303d388b99507e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); SELECT count(*) OVER () FROM q WHERE
```

---

## Crash 56: `74cb1b76ddafc486` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049831`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DE
```

---

## Crash 57: `c0e920ace01d462b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049846`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DE
```

---

## Crash 58: `a4d958734a4ccfcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050387`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT 83611611.189906092714529077180991526069); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf(
```

---

## Crash 59: `f16512cf9d71d5fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050968`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (CURRENT_DATE IN (SELECT ALL * FROM p)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s DEFAULT VALUES; PRAGMA quick_check; SELECT 
```

---

## Crash 60: `baab42640ed5bc35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051966`

```sql
SELECT printf('%.*e', 2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO t1 VALUES (CURRENT_DATE COLLATE BINARY, RAISE(IGNORE) NOTNULL >= CURRENT_TIMES
```

---

## Crash 61: `a0d918cfb10ae806` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055365`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * C
```

---

## Crash 62: `fcf78e63792ccc1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056378`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 63: `73007af06c5c0f3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057931`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * FROM p NATURAL JOIN
```

---

## Crash 64: `362519ababaeb500` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057974`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT
```

---

## Crash 65: `6f84773399d110e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058462`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p VALUES (quote(CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR F
```

---

## Crash 66: `e830d5793d51399b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061429`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE CURRENT_DATE NO
```

---

## Crash 67: `dc19b10b8a0d9ff2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE CURRENT_DATE OR
```

---

## Crash 68: `6a7782c48e0d30af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061632`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE CURRENT_TIME % 
```

---

## Crash 69: `42bbe59121a89437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061648`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); VALUES (CURRENT_DATE IN (SELECT ALL * FROM p)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 70: `42960299efb95cc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061958`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE >= CURREN
```

---

## Crash 71: `cfad9302cd281343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062466`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE > TRUE OR
```

---

## Crash 72: `f4b9ce70c95b1973` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062726`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM p WHERE TRUE ORDER BY min(RAISE(IGNORE)) OVER () DESC NULLS
```

---

## Crash 73: `bf38214995d01c58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062815`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM p WHERE TRUE ORDER BY min(RAISE(IGNORE)) OVER (ORDER BY CUR
```

---

## Crash 74: `e6289f3243f08f88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP MATCH CURRENT_TIME << FALSE AS j_7, * FROM q WHERE EXISTS (SELECT * FROM p WHE
```

---

## Crash 75: `6b226e049e228889` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063464`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIME ORDER BY CURRENT_TIMESTAMP
```

---

## Crash 76: `80dcd989c71c0894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063670`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE NOT IN (V
```

---

## Crash 77: `65c24a935899750e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063869`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP, CURRENT_TIME, CURRENT_TIME) IS NOT NULL FROM q WHERE EXISTS (SELE
```

---

## Crash 78: `9a746577999821e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064086`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) IS NOT NULL FROM q WHERE EXISTS (SELECT * FROM
```

---

## Crash 79: `f5747678c1d6e72f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064092`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP, CURRENT_TIME, CURRENT_TIME) IS NOT NULL FROM q WHERE EXISTS (VALU
```

---

## Crash 80: `81258f5e9130520b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064624`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE NULL OR CURRENT_TIME ORDE
```

---

## Crash 81: `3e950710ddb04e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065152`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN (p AS a , p) WHERE CURRENT_TIME ORDER BY FALS
```

---

## Crash 82: `a7868d59ea88655d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066176`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT FALSE << CURRENT_TIME AND FALSE AS a FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE TRUE ORDER BY 
```

---

## Crash 83: `a99a733be0b7e8cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066543`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE TRUE IS NULL & TRUE BETWE
```

---

## Crash 84: `4433319565e62543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073158`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 85: `936183d9788ca986` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE EX
```

---

## Crash 86: `bd1bc2e6d2d8c048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073882`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INT
```

---

## Crash 87: `a0679d66267305dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074001`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); SELECT * FROM p WHERE TRUE GROUP BY NULL HAVING CUR
```

---

## Crash 88: `e8aca9ef1ba13d2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076571`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTIN
```

---

## Crash 89: `ee38d8e8822685c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077111`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP % CURRENT_DATE MATCH CURRENT_DATE AS oj1t_t5794nqq_8f_pf10h_7wo1__958xf8__82n6f FROM p
```

---

## Crash 90: `da78409cbd31f4b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077227`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE FALSE) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN UNBO
```

---

## Crash 91: `897b0d0b2e094d62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077400`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE FALSE) OVER () FROM p JOIN p a ON FALSE; SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 92: `871a3bde103c51d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078101`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CURRENT_TIMESTAMP AS dx6 FROM p WHERE (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 93: `2fbedaf87f6e4e6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078344`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE IN (SELECT ALL * FROM p)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 94: `b6488f3a8e68a619` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078984`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_DATE >> TRUE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO
```

---

## Crash 95: `635eb7e45ded4817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079314`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (TRUE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUE
```

---

## Crash 96: `c4abb1bb85e207bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079533`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT 319658734809562722308382365364341440385352778053775318194780112854021495943119064812903792508080136133703123560993638030191472514882842764587454218425842100
```

---

## Crash 97: `9e308c830789150b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080210`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (NULL NOT LIKE FALSE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 98: `e026c184bd269e0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081040`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, a DATE CHECK (CURRENT_TIME != FALSE IS NOT CURRENT_DATE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 99: `0fbb6db18112ef95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081183`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, a DATE CHECK (CURRENT_TIME != CURRENT_DATE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 100: `65fd01ae66944de3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081387`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIME != rowid), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 101: `7239d1aed764826f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091501`

```sql
SELECT substr(' X-Y_- j8_l_G__ s4D', 4294967295, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 102: `2be9629ce3722414` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094056`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 103: `aeca0c03d5f4c2a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094602`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IN (WITH t2 AS (SELECT *) VALUES (CURRENT_TIM
```

---

## Crash 104: `e40b5cb74f96c325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095079`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT (VALUES (CURRENT_DATE)) AS c_6_0i__5_y4_9r_7q FROM p WHERE NULL) AS sub1; CR
```

---

## Crash 105: `43f0d76f64f79cfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 106: `d6eeb2056a4fc569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095375`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT (SELECT * FROM q NOT INDEXED WHERE TRUE GROUP BY CURRENT_DATE LIMIT TRUE) AS c_6_0i__5_y4_9r_7q, * 
```

---

## Crash 107: `21163f29d0453853` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095584`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT *, * FROM p WHERE NULL) AS sub1; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 108: `23bff9d1c53329cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096313`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT 83611611.189906092714529077180991526069, a REAL UNIQUE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 109: `d20688f0c7ee4b36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097053`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT TRUE | TRUE || FALSE ISNULL AS a FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 
```

---

## Crash 110: `b5501c73c7b2226a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097347`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT FALSE IS NOT NOT CURRENT_DATE AS rhs________l3zp___8ci___r_3_2_eg___h__8_g39y___7ku4_81__m
```

---

## Crash 111: `8662e2834229e8b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097370`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT FALSE IS NOT FALSE AS rhs________l3zp___8ci___r_3_2_eg___h__8_g39y___7ku4_81__m7p1t_ FROM 
```

---

## Crash 112: `2edceec36904de47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097421`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT NOT CURRENT_DATE <= CURRENT_TIME COLLATE RTRIM AS rhs________l3zp___8ci___r_3_2_eg___h__8_
```

---

## Crash 113: `63e251668663c4b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097605`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT NULL || CURRENT_TIMESTAMP <= NULL AS rhs________l3zp___8ci___r_3_2_eg___h__8_g39y___7ku4_8
```

---

## Crash 114: `9462a68a5668b9c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097792`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT NULL IS NOT CURRENT_DATE <= NULL = NULL AS rhs________l3zp___8ci___r_3_2_eg___h__8_g39y___
```

---

## Crash 115: `243f8a51234db7bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098257`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT TRUE IN (CURRENT_TIMESTAMP, CURRENT_TIME) AS rhs________l3zp___8ci___r_3_2_eg___h__8_g39y_
```

---

## Crash 116: `5743e3bb61ea1f1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099532`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (last_insert_rowid()); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 117: `90eebc83f0bc8569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME / CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNO
```

---

## Crash 118: `a95742c32b652adb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 119: `55ed6e45af8c21c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100557`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c2)
```

---

## Crash 120: `ae0aecd3e71871c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE INDEX IF NOT EXISTS idx1
```

---

## Crash 121: `af84a36334a86913` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100658`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME / CAST(FALSE AS BLOB)); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 122: `22e9e3213f466e31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100809`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME / TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 123: `34423fb6f734cfca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101754`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP < CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUE
```

---

## Crash 124: `3f90ae5c1cd55716` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102157`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE MATCH NULL NOT IN (VALUES (TRUE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 125: `526a0533c8dcb23f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102316`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GLOB NULL COLLATE BINARY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEF
```

---

## Crash 126: `6e9ec83322f5ece0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102517`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GLOB TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 127: `b507caa3a197010a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102655`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IS TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, CURRENT_TIME FROM s NATURAL 
```

---

## Crash 128: `398ff697706007e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103226`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE, c2 BOOLEAN PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS (SELEC
```

---

## Crash 129: `c0ed7da643907144` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103411`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 130: `29641b3f081aa84f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105603`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) VALUES (TRUE BETWEEN TRUE BETWEEN TRUE BETWEEN TRUE BETWEEN FALSE AND TRUE AND TRUE AND 
```

---

## Crash 131: `68595953bf612104` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108374`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 132: `e657958580321903` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108540`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 133: `c20d0851ad3b4f81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109309`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 
```

---

## Crash 134: `dabd8d008da02c69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109325`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 
```

---

## Crash 135: `27ed18d8a5f9cd07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109332`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 
```

---

## Crash 136: `b0b34e69faa3e2e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109341`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 
```

---

## Crash 137: `631f49ceddc955d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110279`

```sql
SELECT substr('', 2147483647, 9223372036854775807); SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT (SELECT * LIMIT CURRENT_DATE) ==
```

---

## Crash 138: `eb12023bfee64e2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116443`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAM
```

---

## Crash 139: `de8ae67323e50ca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116808`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHE
```

---

## Crash 140: `3ae476c09d9e912c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117796`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT 89235693367298965032842506161960025670408346116955068798817863544956380568889680551358875729939983683713295026792742.796508815619406648913383432800231153672
```

---

## Crash 141: `9dce831acb8ffe7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117998`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X''); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT substr('  6 o 6 vR__  -3_-', -922337
```

---

## Crash 142: `2e76b029c7bdd741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119501`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO p (c3) VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 143: `a29586a07dcd227e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123367`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); REPLACE INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 144: `dee7d167c492f87b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123730`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); REPLACE INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 145: `4b7af8bba7fa2b2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125653`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 
```

---

## Crash 146: `e30394c8fb47114e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125672`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*s', 4294967296
```

---

## Crash 147: `79cae374932256a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125948`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2
```

---

## Crash 148: `67e8a6b89f9e4306` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131175`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE = NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); 
```

---

## Crash 149: `c86569c303ef3ae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131962`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p WITH RECURSIVE p (c2) AS (VALUES (NULL) UNION SELECT * FROM p WHERE TRUE) SELECT DISTINCT * FROM p; PRAGMA quick_check; SELECT print
```

---

## Crash 150: `bcb81c8a2d85878d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132435`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME / CAST(FALSE AS FLOAT)); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 151: `39d51193a2aff88e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133673`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP / CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 152: `b9db7ed7b88d5cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133825`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP / CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 153: `b07b4aded4e8d39a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134297`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (json_type(TRUE >= CURRENT_TIME)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT 
```

---

## Crash 154: `d40c6fb068649036` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134428`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); INSERT OR FAIL INTO p VALUES (total_changes()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO s DEFAULT V
```

---

## Crash 155: `60b304f7321dca36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135560`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT count(DISTINCT CURRENT_DATE) FILTER (WHERE TRUE) AS a FROM p WHERE NULL) AS
```

---

## Crash 156: `5cc40b726c143778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN UNIQUE); SELECT * FROM (SELECT (SELECT * FROM p WHERE TRUE ORDER BY FALSE DESC NULLS LAST) AS a FROM p WHERE NUL
```

---

## Crash 157: `d2c12c4e7a5f903d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139960`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT 'E3'); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 158: `9fb57d0607e07184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140122`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 159: `d16cc830ed6d4e56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142435`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); WITH RECURSIVE p (a) AS (VALUES (NULL) UNION VALUES (FALSE)) SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS ()
```

---

## Crash 160: `fc39c0060c3d75c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152636`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL CHECK (length(CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 161: `b52cd3ade8930ce5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152805`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL CHECK (length(FALSE))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 162: `28a90e086e497620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153001`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL CHECK (upper(p.rowid))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES
```

---

## Crash 163: `27972a95e4fcdaab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155828`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (~CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_DATE), b DATE UNIQUE); INSERT INTO p DEFAULT VAL
```

---

## Crash 164: `5487d0f711d47ccb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155948`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY, b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 165: `0487585191bcef25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156218`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (TRUE), a DATE CHECK (CURRENT_DATE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 166: `0edeba2a1f2eaafb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156346`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIMESTAMP), b DATE UNIQUE); INSERT INTO p (_rowid_) VALUES (NULL) ON CONFLICT(rowid) DO UPDATE SET _rowid_ = CURRENT_DATE; PRAGMA integrity_check; SE
```

---

## Crash 167: `d84d8ab02e39c6c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159023`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_DATE >> ~CURRENT_TIME), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); W
```

---

## Crash 168: `b870ce4bf2974ec0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159799`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (quote(quote(quote(quote(random())))) >> TRUE), b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 169: `de19540ef839d6da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160350`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (random()) ON CONFLICT DO NOTHING; VALUES (CURRENT_DATE IN (SELECT ALL * FROM p)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 170: `ec8493f66853de05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161160`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE FALSE) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIME IN (VALUES (TRUE)) DESC ROW
```

---

## Crash 171: `4e5be00d7aa5efc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161292`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE FALSE) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIMESTAMP DESC GROUPS BETWEEN UN
```

---

## Crash 172: `095a82b6a367025b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161490`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_TIME COLLATE NOCASE DESC RANGE BETWEEN UNBOUNDED PR
```

---

## Crash 173: `35bb665a20effc38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163481`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, b REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SEL
```

---

## Crash 174: `6706d47f6fc61bf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163987`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP 
```

---

## Crash 175: `f117958534cde04b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164165`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q NOT INDEXED LEFT JOIN (SELECT * FROM p NOT INDEXED
```

---

## Crash 176: `cafa91623a542297` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167796`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(
```

---

## Crash 177: `8d9df25e06bbd53e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167872`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); VALUES (FALSE) EXCEPT VALUES (CURRENT_TIMESTAMP * C
```

---

## Crash 178: `9604ac241dcf0180` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168041`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); VALUES (FALSE) EXCEPT VALUES (CURRENT_TIMESTAMP * T
```

---

## Crash 179: `578a5929be38e96e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170080`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); SELECT count(*) FILTER (WHERE FALSE) OVER () AS a F
```

---

## Crash 180: `11174d0d05c85631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178230`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT count(*) FROM q NOT INDEXED LEFT JOIN (p NOT INDEXED NATURAL JOIN p NOT INDE
```

---

## Crash 181: `1cc290f50daee067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179055`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN (VALUES (TRUE)) AS n622__ WHERE TRUE IS NULL 
```

---

## Crash 182: `0cb9fba6a07bf21e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180406`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_TIMESTAMP FROM p GROUP BY CURRENT_DATE ORDER BY FALSE DESC NULLS LAS
```

---

## Crash 183: `de63fe517dd08ad9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180475`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_TIMESTAMP FROM p GROUP BY CURRENT_DATE ORDER BY FALSE DESC NULLS LAS
```

---

## Crash 184: `1c0e8ba439c53466` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181135`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE ORDER BY CURRENT_DATE ASC NULLS L
```

---

## Crash 185: `e8c3f4b34062bce3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181271`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT DISTINCT * FROM p AS a NATURAL JOIN q AS f1bt__z0q3219w__3_a2o4 NATURAL JOIN q; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 186: `46b7d9bdcb424210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181714`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE NULL IS NOT CURRENT_DATE 
```

---

## Crash 187: `9416b967fee0e7b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182108`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT count(*) OVER (ORDER BY FALSE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO O
```

---

## Crash 188: `1d59998992515428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182233`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT FALSE + FALSE LIKE FALSE AS in_ FROM q WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 189: `3ff63c7bab22ebcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182975`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE c2 ORDER BY FALSE DESC NULLS LAST); SELECT prin
```

---

## Crash 190: `c51c6a423e12e573` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183087`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE c2 ORDER BY FALSE DESC NULLS LAST); SELECT roun
```

---

## Crash 191: `5b89e5795b55ba56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184162`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE NOT IN (S
```

---

## Crash 192: `61b8b74539f351b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184395`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED CROSS JOIN p NOT INDEXED NATURAL LEFT JOIN p 
```

---

## Crash 193: `9aaa69a93a9bcf0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184666`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (RAISE(IGNORE))); CREATE VIRT
```

---

## Crash 194: `09ca2374cc786b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185029`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP MATCH CURRENT_TIME << FALSE AS j_7, * FROM q WHERE EXISTS (SELECT * FROM p WHE
```

---

## Crash 195: `55b14bfe459a4890` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185278`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT CURRENT_TIMESTAMP MATCH CURRENT_TIME << CURRENT_TIMESTAMP AS j_7, * FROM q WHERE EXISTS (VALUES 
```

---

## Crash 196: `b95b005173b2da68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186208`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE > FALSE OR FALSE OR NULL ORDER BY
```

---

## Crash 197: `d595f393fd8628bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186369`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE > FALSE OR TRUE ORDER BY NULL DES
```

---

## Crash 198: `e2ce29fd7f056551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186830`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE TRUE COLLATE RT
```

---

## Crash 199: `d4255d327ab43f12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187048`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NATURAL JOIN q NOT INDEXED NATURAL JOIN q WHERE CURRENT_T
```

---

## Crash 200: `5b36769b2b333c5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187928`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE FALSE IS NOT TR
```

---

## Crash 201: `65448c90fc9c8280` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188087`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER DEFAULT X'FCA4Ec26f9c0db'); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 202: `ef5ab5feeadaa0d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (VALUES (TRUE)) AS n622__ LEFT JOIN p NOT INDEXED WHERE CUR
```

---

## Crash 203: `258c7546ac42f00f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM p WHERE (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GRO
```

---

## Crash 204: `0c2770ccad0142ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188654`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE, CURRENT_TIME ORDE
```

---

## Crash 205: `56f77de2a09f503a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191473`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT NOT EXISTS (VALUES (CURRENT_DATE, TRUE) UNION SELECT p.*, r.* FROM p INDEX
```

---

## Crash 206: `6d1f3999935974c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191511`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT NOT EXISTS (VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE
```

---

## Crash 207: `73a73a8a0c2b729b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195168`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT DISTINCT * FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 208: `4801adb09c559c24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195421`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (min(CURRENT_TIMESTAMP) OVER ()) INTERSECT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 209: `ecccd51dc3f1f491` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197525`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) INTERSECT VALUES (count(*) OVER ()); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 210: `376a711e3e5413cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197644`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 211: `949d13175cdaba0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198496`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) INTERSECT VALUES (CAST(CURRENT_TIME AS BLOB)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 212: `5527d500a4b40367` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199528`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT * FROM q WHERE CURRENT_DATE ORDER BY CURRENT_DATE DESC NULLS L
```

---

## Crash 213: `b8e573df44f2aa1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200444`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL DEFAULT X'cb1697a2B279CE', a DATE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 21474
```

---

## Crash 214: `81317ec0e9475f06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202361`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c3 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 215: `35d96d118c16c7da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202662`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c3 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT -FALSE AS i_6n0z55520_4_xr1nn3__6_omgv__9z42_7wt97tu__v_og__; CREATE VIRTUAL TA
```

---

## Crash 216: `f1af5e34e4522b50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202703`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT -FALSE AS i_6n0z55520_4_xr1nn3__6_omgv__9z42_7wt97tu__v_og__; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 217: `5dcf4430cc59ad79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c3 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT CURRENT_DATE IN (sum(TRUE) OVER (ORDER BY CURRENT_TIME COLLATE NOCASE DESC RANG
```

---

## Crash 218: `23df1438dd2482ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203402`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL HAVING CURRENT_TIMESTAMP) AS n622__ NATURAL JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY FA
```

---

## Crash 219: `dc4cb63e9df162ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203801`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); SELECT * FROM (VALUES (CURRENT_TIME)) AS n622__ LEFT JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 220: `12d7f5544725139a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204976`

```sql
SELECT printf('%.*g', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT FALSE NOT NULL NOTNULL AS f_ FROM p NATURAL JOIN t3 WHERE CURRENT_TIME COLLATE RTRIM NOT IN 
```

---

## Crash 221: `f88270c749776592` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206498`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT 89235693367298965032842506161960025670408346116955068798817863544956380568889680551358875729939983683713295026792742.796508815619406648913383432800231153672
```

---

## Crash 222: `85b1f2db354f6c17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206635`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 223: `b4f800362884bc0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208464`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); SELECT CASE WHEN CURRENT_DATE THEN C
```

---

## Crash 224: `28f87671ec234713` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209931`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); SELECT count(*) OVER (ORDER BY NULL 
```

---

## Crash 225: `cb3b3a230ab4dd53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210320`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (json_type(NULL)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 226: `a2bf2e1aeb0e60f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210457`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (randomblob(CURRENT_DATE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 227: `c868b618cbb148d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210678`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 228: `ee1aa648cb4ea9e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210711`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 229: `b91ccc0c3fa4266e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210859`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 230: `2606a4b760ed7121` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210882`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 231: `677e2b1cddcf4887` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211248`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES ('--_ _G-7-_-6h  _JU') ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 232: `53e66d385d549381` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211468`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (randomblob('--_ _G-7-_-6h  _JU')) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 233: `ee46da724960dc9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211711`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (upper(CURRENT_TIMESTAMP)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 234: `b215be015e6c1184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212622`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(CURRENT_TIMESTAMP)))))))))))))) ON CONFLICT DO NOTHI
```

---

## Crash 235: `b2c92a003b8bca75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212898`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(quote(quote(quote(quote(CURRENT_TIME)))))) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 236: `e1c3902454c23889` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212912`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(changes())))))))))) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE V
```

---

## Crash 237: `c367e63134c62f94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213012`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP AND FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 238: `99549f916d48ab71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213690`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(CURRENT_DATE))))))) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*f', 2147
```

---

## Crash 239: `66ad852347633134` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214387`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); SELECT CURRENT_TIME COLLATE BINARY ORDER BY RAISE(IGNORE) DESC, TRUE ASC NULLS FIRST; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 240: `411b50bf44801f7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215423`

```sql
SELECT printf('%u', -2147483648, '--R_  2-__ GD Ot-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t1 (a) VALUES (json(-TRUE) FILTER (WHERE ~FALSE) OVER (ORDER BY CURRENT_TIME
```

---

## Crash 241: `eec99db503e661e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217619`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(CURRENT_TI
```

---

## Crash 242: `7f415a93ba7d9c5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217856`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (upper(NULL NOTNULL)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 243: `927667f570bc3ace` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217999`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (upper(TRUE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 244: `36f538a0aab5ed95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218139`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (upper(X'')) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUER
```

---

## Crash 245: `9ab033ccc31c447d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218534`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 246: `f0d649ba6df8d089` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218625`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 247: `8a47f6acd54b2fca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218642`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 248: `8f88f0e253bb10e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218652`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING
```

---

## Crash 249: `c48e687aa4c92e40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219612`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_T
```

---

## Crash 250: `98c31fcf0c155c5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219811`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); SELECT * FROM q WHERE EXISTS (VALUES
```

---

## Crash 251: `5fbf929f83339c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219872`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE); SELECT * FROM q WHERE EXISTS (VALUES
```

---

## Crash 252: `f33d6b1ed58cbb9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220226`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM q WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 253: `9c85c34fae2cb2fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220232`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM q WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 254: `531054d071dea53b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221191`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN (SELE
```

---

## Crash 255: `f90268aa5a478094` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221346`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE TRUE ORDER BY CURRENT_DA
```

---

## Crash 256: `98e64893bfc131a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221353`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN (VALU
```

---

## Crash 257: `7707bc97ccee20eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221361`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN (SELE
```

---

## Crash 258: `660f7e1ed3886e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221368`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN (SELE
```

---

## Crash 259: `d27c7df3f14dc023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222117`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP) IN (SELECT ALL * FROM p)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 260: `d4a6af50bf57b608` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222377`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (CAST(FALSE AS TEXT) IN (SELECT ALL * FROM p NOT INDEXED)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT 
```

---

## Crash 261: `5bd2802f25bf26d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222532`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (CAST(FALSE AS TEXT) IN (VALUES (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT count(*) O
```

---

## Crash 262: `e302de69a3994a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222621`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (count(*) OVER () IN (SELECT ALL * FROM p NOT INDEXED)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO s DEFAULT VALUES; PRAGMA q
```

---

## Crash 263: `41d262c8e98d9dda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222799`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (count(*) OVER () IN (VALUES (FALSE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO s DEFAULT VALUES; PRAGMA quick_check; SELEC
```

---

## Crash 264: `b895367447fe1d86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223136`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); VALUES (CURRENT_DATE IN (SELECT ALL CURRENT_DATE AS k FROM p)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT OR ABORT INTO p VALUES (CURREN
```

---

## Crash 265: `ffcde1bb56a60757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223383`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); SELECT * FROM (SELECT * FROM (VALUES (FALSE)) AS n622__ NATURAL JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS LAST) AS n622__ NATURAL JOIN 
```

---

## Crash 266: `d2d701cc529c8d99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224129`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL HAVING CURRENT_TIMESTAMP) AS n622__ NATURAL JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY CA
```

---

## Crash 267: `12c14280c2f052f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224787`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT sum(TRUE) OVER (ORDER BY CURRENT_TIMESTAMP != CURRENT_TIMESTAMP COLLATE NOCASE DESC RANGE BETWEEN UNBOUND
```

---

## Crash 268: `fd1af30bf8fbe248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227486`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) INTERSECT VALUES (CAST((VALUES (TRUE) EXCEPT VALUES (TRUE)) AS BLOB)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 269: `4c8af877bdd86a4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228864`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) INTERSECT VALUES (quote(CURRENT_TIMESTAMP) * CURRENT_TIMESTAMP * NULL); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 270: `212aa4b38b76b0b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229259`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CURRENT_DATE) UNION VALUES (NULL) UNION VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 271: `ac794c8d45e1c539` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232590`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (min(CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS LAST RO
```

---

## Crash 272: `f6fa4480d663797d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232852`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(CURRENT_TIMESTAMP)))))))))) INTERSECT S
```

---

## Crash 273: `d789ee2b6585f365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233039`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (quote(quote(quote(quote(quote(quote(count(*)))))))) INTERSECT SELECT DISTINCT * FROM q; SELEC
```

---

## Crash 274: `30fbf46d58759207` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233232`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT DISTINCT CURRENT_DATE - FALSE NOT LIKE CURRENT_DATE AS ok3y8_g
```

---

## Crash 275: `a81907a27b03383f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233961`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE, b DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER DEFAULT ' - mzC U1_g'); CREATE TAB
```

---

## Crash 276: `ead4c71f681115b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234250`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY CURRENT_TIME
```

---

## Crash 277: `fb4ff822d2add658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234257`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p VALUES (FALSE) UNION VALUES (CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT V
```

---

## Crash 278: `a0547e0c2512343b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236394`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE FALSE) OVER () FROM p WHERE TRUE ORDER BY cou
```

---

## Crash 279: `5c24aa1d31f4f4e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP FROM p WHERE TRUE ORDER BY count(*) OVER () DESC N
```

---

## Crash 280: `ceb52502ffc76fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236885`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE FALSE) OVER () FROM p WHERE TRUE ORDER BY min(
```

---

## Crash 281: `50804982efb08865` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237298`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE (VALUES (CURRENT_DATE)) > TRUE; EXPLAIN QUERY PLAN VALUES (RAISE(
```

---

## Crash 282: `70f0df47e2a67454` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237304`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY RAISE(IGNORE) DESC, group_conca
```

---

## Crash 283: `96bec2a50bd85803` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237313`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT CURRENT_TIMESTAMP AS dx6 FROM p AS d___p_6l WHERE CURRENT_TIMESTAMP; EXPLAIN QUERY PLAN VALUES (RAISE(IGNOR
```

---

## Crash 284: `2f9f8c78b95b2067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237323`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM (SELECT count(*) FILTER (WHERE FALSE) 
```

---

## Crash 285: `d0fea4f1f7652fdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237330`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED LEFT JOIN (VALUES (TRUE)) AS n622__ WHERE TRUE IS NULL ORDER BY FALSE DESC NULLS LAST; EXPLAIN 
```

---

## Crash 286: `9c54219a1d09cbb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237354`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY FAL
```

---

## Crash 287: `0e985d379f56a89d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237362`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM (VALUES (CURRENT_TIME)) AS n622__ WHER
```

---

## Crash 288: `1417c83845ade65e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237371`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME == TRUE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GROU
```

---

## Crash 289: `01ad2e7af4891d44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237380`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY +CU
```

---

## Crash 290: `3b9369bdde16f581` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237394`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE OR RAISE(IGNORE), RAISE(IGNORE) | FALSE, NULL); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM
```

---

## Crash 291: `4e73aa9a1c334bc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237438`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM p NOT INDEXED , q AS a USING (a, b) WH
```

---

## Crash 292: `0ca144267caf0564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237477`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT -69); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GRO
```

---

## Crash 293: `51745cc5228a10c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237491`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT +EXISTS (SELECT CURRENT_TIMESTAMP AND CURRENT
```

---

## Crash 294: `144c2a1d5df740a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237497`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT NULL AS i_, t3.* FROM p NATURAL JOIN t1 INDEXED BY c2; EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)) UNION SELECT * FROM
```

---

## Crash 295: `583bd8d8af25b5be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239560`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT p.* FROM q NOT INDEXED LEFT JOIN (q NOT INDEXED LEFT JOIN p) WHERE NU
```

---

## Crash 296: `b28b6428a9873365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239646`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT p.* FROM q NOT INDEXED LEFT JOIN p WHERE NULL ORDER BY CURRENT_DATE);
```

---

## Crash 297: `76dab2b67931fb09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239652`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT p.* FROM q NOT INDEXED LEFT JOIN (p NOT INDEXED) WHERE NULL ORDER BY 
```

---

## Crash 298: `c6ce416daa81c90b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240223`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (VALUES (RAISE(IGNORE)) UNION SELECT * FROM q NOT INDEXED WHERE FALSE GROU
```

---

## Crash 299: `c630d97fc79cdc68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240429`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY CURRENT_D
```

---

## Crash 300: `2f7587476f75ea92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242485`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (VALUES (CURRENT_TIME)) AS n622__ WHERE rowid ORDER BY NULL
```

---

## Crash 301: `f598066e3f59ccaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242666`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT count(*) FILTER (WHERE FALSE) OVER () FROM p WHERE TRUE ORDER BY m
```

---

## Crash 302: `41ac96986dca505a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242828`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT count(*) FILTER (WHERE FALSE) OVER () FROM p WHERE TRUE ORDER BY m
```

---

## Crash 303: `caad384a763cd4c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243066`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_DATE AS k FROM p GROUP BY CURRENT_DATE ORDER BY min(RAISE(
```

---

## Crash 304: `dfa7d826102c61c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244485`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS z_ W
```

---

## Crash 305: `e442cf725b060788` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246831`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b DATE UNIQUE); SELECT DISTINCT * FROM p AS a NATURAL JOIN q AS f1bt__z0q3219w__3_a2o4 NATURAL JOIN q; CREATE
```

---

## Crash 306: `9598c73a481a9e74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247007`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b DATE UNIQUE); SELECT DISTINCT * FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSE
```

---

## Crash 307: `2713d7562a8b4f68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247013`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b DATE UNIQUE); SELECT DISTINCT * FROM q NATURAL JOIN q AS f1bt__z0q3219w__3_a2o4 NATURAL JOIN q; CREATE VIRT
```

---

## Crash 308: `30866fc944a1980d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247932`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (SELECT * FROM p NATURAL JOIN p NOT INDEXED WHERE FALSE) AS n622__ LE
```

---

## Crash 309: `8900fd0e1b9e5024` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248083`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM (VALUES (FALSE)) AS n622__ LEFT JOIN (VALUES (TRUE)) AS n622__ WHERE 
```

---

## Crash 310: `7a9bf3b03294d187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248321`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT * FROM q NOT INDEXED JOIN (VALUES (TRUE)) AS n622__ WHERE TRUE IS NULL & NUL
```

---

## Crash 311: `921e864254227666` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249314`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (VALUES (FALSE)) AS n622__ WHERE CURRENT_DATE ORDER BY CURRENT_DATE DESC NULLS LAST; SELECT prin
```

---

## Crash 312: `74dcb3a00780ec98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249625`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); VALUES (CURRENT_DATE) UNION SELECT * FROM q WHERE CURRENT_DATE ORDER BY CURRENT_DATE DESC NULLS LAST; CREATE VIRT
```

---

## Crash 313: `3703f373354a789c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256517`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); SELECT *, * FROM p NOT INDEXED WHERE CURRENT_TIMEST
```

---

## Crash 314: `b8dd6f0eefc6a49e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256829`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); SELECT count(DISTINCT CURRENT_TIMESTAMP) FILTER (WH
```

---

## Crash 315: `c7d8ffd291325818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259674`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(
```

---

## Crash 316: `e93a1207903c9b2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259967`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(CURRENT_DATE))))))) ON CONFLIC
```

---

## Crash 317: `0c8cbff617f81c7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259982`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(quote(
```

---

## Crash 318: `e43e4c4aa3a26734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262643`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q NOT INDEXED LEFT JOIN p NOT INDEXED WHERE TRUE BET
```

---

## Crash 319: `5a21ba8624495c40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262876`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q NOT INDEXED WHERE FALSE IS NOT TRUE; CREATE VIRTUA
```

---

## Crash 320: `2bdffb1417fe52ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263546`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM ((VALUES (FALSE)) AS n622__ LEFT JOIN q NOT INDEXED)
```

---

## Crash 321: `2e05c2e9429be7ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263706`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q NOT INDEXED LEFT JOIN (SELECT * FROM q NOT INDEXED
```

---
