# Crash Triage Report

**Total crashes:** 264  
**Unique crash sites:** 264  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 264 | 264 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `893c00be740e1f89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000216`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO q VALUES (CASE (NOT CURRENT_DATE COLLATE NOCASE IS NOT DISTINCT FROM CURRENT_TIME NOT LIKE CURRENT_TIME REGEXP CURRENT
```

---

## Crash 2: `3d114d82f6a63e7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000275`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT TRUE = CURRENT_TIMESTAMP - FALSE IS NOT CURRENT_TIMESTAMP * max(CASE RAISE(IGNORE) WHEN FALSE MATCH TRUE THEN TRUE ELSE count(*) END), *
```

---

## Crash 3: `efc722f03d0021a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000324`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); WITH RECURSIVE p AS MATERIALIZED (SELECT * FROM q WHERE NOT FALSE ORDER BY CAST(TRUE AS VARCHAR(255)) & -CASE CURRENT_TIMESTAMP WHEN NULL TH
```

---

## Crash 4: `e55ebab46669195d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000684`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN GENERATED ALWAYS AS (CURRENT_TIMESTAMP NOTNULL = trim(NULL) NOTNULL % TRUE IS CURRENT_DATE IS NOT DISTINCT FROM RAI
```

---

## Crash 5: `5b64afc5b9f2e31f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000753`

```sql
SELECT substr('7RM--9gT--_o_4-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CASE WHEN NULL BETWEEN CURRENT_TIME = TRUE AND CURRENT_DATE / TRUE THEN NULL % F
```

---

## Crash 6: `54e0212a46f3249e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000896`

```sql
SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 7: `b4268690c675c319` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001390`

```sql
SELECT round(1.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT VALUES; ANALYZE r; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SEL
```

---

## Crash 8: `a1feeee7db3cd0fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001583`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC GENERATED ALWAYS AS (~CURRENT_TIME <> NOT RAISE(IGNORE) MATCH RAISE(IGNORE) >> NULL | ~CAST(FALSE AS VARCHAR(255)))
```

---

## Crash 9: `6c8c66fe0f4b4914` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001648`

```sql
SELECT printf('%lli', 2147483647, 'w70 2p 5B7M  d9-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (-typeof(+FALSE) FILTER (WHERE CURRENT_TIMESTAMP NOTNULL) IS DISTIN
```

---

## Crash 10: `bc4681677fb28b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002348`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT TRUE AND NULL OR TRUE AS a FROM r NO
```

---

## Crash 11: `14757dca684587ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002375`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CU
```

---

## Crash 12: `6eea324c7881c468` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002387`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELE
```

---

## Crash 13: `e608f4cec5b4ffca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002395`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 14: `5dc62beb0bc560d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002901`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); S
```

---

## Crash 15: `70d8e0e905afecee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003823`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 16: `cdd1eef76607d545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004325`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 17: `e5611b0275f01296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004501`

```sql
SELECT substr('7_', 4294967296, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO q VALUES ((CURRENT_TIME / NULL NOT BETWEEN NOT RAISE(IGNORE) GLOB -FALSE IS NOT DISTI
```

---

## Crash 18: `c31a87599246bcd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004805`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b
```

---

## Crash 19: `39ea866943d09306` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004812`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT NULL FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 20: `4fe00e28a96dc618` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004818`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | NULL COLLATE RTRIM IN (VALUES (NULL)) >> TRUE FROM p; CREATE
```

---

## Crash 21: `e0d55583443bc84b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004824`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | FALSE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 22: `593d704d7d7d9d18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004830`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIMESTAMP >> TRUE FROM p; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 23: `b82bad1a7edc7133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004836`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIME IN (VALUES (NULL)) >> TRUE FROM p; CREATE VIRTU
```

---

## Crash 24: `71b1ed7ae1d7501e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004883`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIME IN (VALUES (NULL)) >> CURRENT_TIME FROM p; CREA
```

---

## Crash 25: `5b9bbacdc085fb1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004961`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_DATE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 26: `d700bea4c9fca023` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006915`

```sql
SELECT substr('Z_6Qy - ', 1); SELECT printf('%.*g', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q AS (VALUES (CURRENT_TIME)), t1 AS (SELECT * FROM t1 AS eo CROSS J
```

---

## Crash 27: `d9a588190ba43eb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007056`

```sql
SELECT substr('', 1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT VALUES; VALUES (+FALSE NOTNULL); SELECT printf('%f', 2147483647, 'j_ _-  6H7_');
```

---

## Crash 28: `791aec6760a1fa11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007095`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, c3, c3, c3, b); INSERT OR ROLLBACK INTO s VALUES (NOT FALSE COLLATE BINARY <> NULL = RAISE(IGNORE) IS NOT NOT RAISE(IGNORE) >> TRUE <> 
```

---

## Crash 29: `3b95064ee76b81c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007206`

```sql
SELECT printf('%.*f', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c2, _rowid_); WITH RECURSIVE p AS NOT MATERIALIZED (VALUES (CURRENT_TIME % TRUE) INTERSECT SELECT DISTINCT
```

---

## Crash 30: `792593e740a22c99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007515`

```sql
SELECT printf('%u', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); INSERT OR FAIL INTO p VALUES (c2 IS NOT NULL > NULL NOT NULL > length(NULL) FILTER (WHERE FALSE) << FALSE NOT 
```

---

## Crash 31: `27ad06e7ace5dd3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007619`

```sql
SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); REPLACE INTO s VALUES (CURRENT_TIMESTAMP COLLATE RTRIM >> FALSE); EXPLAIN QUERY PLAN SELECT *; CREATE TABLE IF NOT
```

---

## Crash 32: `32808a3a840aaee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007694`

```sql
SELECT substr('-N', -2147483649, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3, _rowid_, b); INSERT INTO q (c3) VALUES (group_concat(CURRENT_TIMESTAMP COLLATE RTRIM <= last_
```

---

## Crash 33: `69ab17517edc6729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007803`

```sql
SELECT printf('%.*e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c3); VALUES (NULL COLLATE BINARY) EXCEPT VALUES (FALSE) ORDER BY +CURRENT_TIME DESC NULLS FIRST UNION ALL SELECT q
```

---

## Crash 34: `d105734977bced7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007870`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT r.* FROM (SELECT -iif(total_changes(), changes(), NULL / CURRENT_TIMESTAMP) OVER (PARTITION BY 
```

---

## Crash 35: `e86afb45d0810b07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007929`

```sql
SELECT printf('%.*g', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); EXPLAIN QUERY PLAN WITH RECURSIVE t2 (rowid, c1, b) AS (VALUES (CURRENT_DATE, NULL) LIMIT
```

---

## Crash 36: `47a3959497af8ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009605`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CASE CURRENT_TIME WHEN NULL THEN CURRENT_DATE GLOB FALSE ELSE NU
```

---

## Crash 37: `6c595571f582348b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009964`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (FALSE); EXPLAIN QUERY PLAN VA
```

---

## Crash 38: `ded5cb4e66224285` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010256`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL 
```

---

## Crash 39: `8eaacccc0efbbe60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020354`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 40: `d964d5278b50bfe7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020390`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 41: `b72fa2125cebfcbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020818`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL + FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 42: `cfb19697426e7bbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021776`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INT
```

---

## Crash 43: `eeae43809c2bd204` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021984`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); SEL
```

---

## Crash 44: `1ec5cad3b3b68445` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023092`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP >> CURRENT_TIME FROM p; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 45: `9dfbdb5c4bcaa967` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023495`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIME IN (VALUES (NULL)) FROM p; CREATE VIRTUAL TABLE
```

---

## Crash 46: `e704cf1896805e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024387`

```sql
SELECT printf('%.*g', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 47: `9bec161611aba810` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024602`

```sql
SELECT printf('%.*s', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, a); SELECT p.*, '' AS j674_o76o0_5r, q.*, t1.*, (+iif(CURRENT_TIME -> CURRENT_TIME, (+json_array(FAL
```

---

## Crash 48: `f31183db5ffaa157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025620`

```sql
SELECT printf('%.*d', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); SELECT NOT '' >> CASE CURRENT_TIMESTAMP & CURRENT_TIMESTAMP NOTNULL NOTNULL WHEN (CURR
```

---

## Crash 49: `1e4ea90d521bfaec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026133`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT X'3a'); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 50: `c56779d66ecaff66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026297`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), _rowid_ GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); INSERT INTO p DEFAULT
```

---

## Crash 51: `204a9562c4561427` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026668`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CURRENT_TIMESTAMP); SELECT substr('', 4294967295, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT V
```

---

## Crash 52: `ca36261a85bca469` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_TIME), c2 INT); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSE
```

---

## Crash 53: `cda25c538bf7b555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027497`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, c1 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 54: `fc2cba75d6756ca2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027562`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, c1 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('--R', 4294967295, -1); CREATE 
```

---

## Crash 55: `93b68dd4400e7f32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027746`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE INDEX IF NOT EXISTS i
```

---

## Crash 56: `6a60456b6046ce8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029228`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC CHECK (CURRENT_DATE), c2 REAL); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649,
```

---

## Crash 57: `b47093a0e6696438` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030629`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE
```

---

## Crash 58: `000fae57c239d8b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030676`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER CHECK (TRUE IS NOT CAST(RAISE(IGNORE) AS FLOAT)), a DATE PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE 
```

---

## Crash 59: `66fc25c9f01cac7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030684`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT -0, c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); I
```

---

## Crash 60: `880108b6ad93ec4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031028`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 61: `9e0aa7a2d5e85c62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036519`

```sql
SELECT printf('%x', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(4294967296));
```

---

## Crash 62: `d2e0b0c2c77d2ee4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036663`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); SELECT hex(zeroblob(0));
```

---

## Crash 63: `d8fce36d5e0560f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036796`

```sql
SELECT printf('%s', -2147483649, 'jK-5-__-_ _'); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 64: `18a9242c3bf3890a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042979`

```sql
SELECT printf('%.*d', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(4294967296));
```

---

## Crash 65: `71ede784b70e5f79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043574`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 66: `19a0d5d5a14dd5e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043772`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE IS NOT CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 67: `db858a2297c96259` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043938`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 68: `b29b4b536c0f7e9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044647`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IS FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 69: `c3b60db87ac78e56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045980`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT p.* FROM p WHERE EXISTS (SELECT * FROM p AS c6yd_q ORDER BY FALSE ASC NULLS FIRST); SELE
```

---

## Crash 70: `0599a8bc6852ab7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046299`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED ORDER BY NULL DESC); CREATE VIRTUAL T
```

---

## Crash 71: `6493ae896a6c09e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046451`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p ORDER BY CURRENT_DATE IN (SELECT CURRENT_DATE NOT
```

---

## Crash 72: `afe383a82ba53b21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049856`

```sql
SELECT round(0.01, 9223372036854775807); SELECT round(0.0, 1); SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p (c2) AS (SELECT * ORDER BY
```

---

## Crash 73: `24353703675f8843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050303`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 74: `3a1471770b6dee58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051255`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(4294967296));
```

---

## Crash 75: `7c24ddb315654d7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051482`

```sql
SELECT substr('8_-Z', 0, 4294967296); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 76: `3a3b989d62ba1be0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053766`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP LIKE CURRENT_TIME); PRAGMA int
```

---

## Crash 77: `5401a8b50e279fe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053875`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE LIKE CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 78: `6783bc88acd1f706` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053910`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE V
```

---

## Crash 79: `c26c9940a40a6841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054100`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 80: `65290b2e6eda4fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054123`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP LIKE CURRENT_DATE); PRAGMA quick_check; SELECT prin
```

---

## Crash 81: `0bcdaf76cf319549` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056672`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT (VALUES (CURRENT_DATE)) NOT LIKE count(*) INTERSECT VALUES
```

---

## Crash 82: `33372e0df4c8472e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059874`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q WHERE FALSE GROUP BY TRUE WINDOW w1 AS () INTERSE
```

---

## Crash 83: `928527eb948ad906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061031`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATURAL LEFT
```

---

## Crash 84: `5b3b9803bddf9e2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061307`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED ORDER
```

---

## Crash 85: `8eb7e6f04fe9d48b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061865`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED ORDER BY count(DISTINCT CURRENT_DATE)
```

---

## Crash 86: `dc1d6389cb1df5a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063679`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM p; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick
```

---

## Crash 87: `3ff34e0ccf10011c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063847`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_
```

---

## Crash 88: `936024f62a13542d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064303`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT DISTINCT * FROM p NATURAL JOIN p NOT INDEXED WHERE TRUE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 89: `44e534efbb188a72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065188`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT CURRENT_TIME AS e78_7er; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p (c3, c1) A
```

---

## Crash 90: `99d656f44d9e8d60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065521`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT 0); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; P
```

---

## Crash 91: `21fe117c79d2ffc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065612`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAUL
```

---

## Crash 92: `69805d4795d3ce35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066034`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 93: `4d888a88d366f797` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066604`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_DATE))); PRAGM
```

---

## Crash 94: `1d9d415f0b40de30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066825`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (~TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 95: `af20d3b1007634eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067123`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 96: `e990c685e684d079` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067529`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 NUMERIC 
```

---

## Crash 97: `89e58ff0e1e908df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067940`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 98: `b59482efd3510be9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068622`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 99: `0bc5b83a53f05ea8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068656`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a + -0) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649,
```

---

## Crash 100: `f6273611085c2f3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072495`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (VALUES (FALSE)) AS xx8l6z NATURAL JOIN p NOT INDEX
```

---

## Crash 101: `4eb54b8f87d5140d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075569`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 102: `a5541bf552fcf1aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076652`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (count(DISTINCT CURRENT_DATE) FILTER (WHERE NULL)) UNION ALL VALUES (CURRENT_TIMESTAMP); CREATE VI
```

---

## Crash 103: `e5098dca15207c21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078695`

```sql
SELECT printf('%.*f', 2147483648, 1.0); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q (a) AS (SELECT q.*, FALSE AS t___9_ra, * FROM p OR
```

---

## Crash 104: `2896c3b9b154af79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079747`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE, a TEXT GENERATED ALWAYS AS (NULL) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); 
```

---

## Crash 105: `3a96c38c291f1752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085962`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC CHECK (CURRENT_DATE), c2 INTEGER CHECK (TRUE IS NOT CURRENT_DATE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check
```

---

## Crash 106: `de09cddd1930ece9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086056`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC CHECK (CURRENT_DATE), c2 INTEGER CHECK (TRUE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('__4
```

---

## Crash 107: `12d39a701f71d099` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086372`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT X'c28a08b4D4'); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 108: `5a7c1127aeefb2ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087225`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CAST(NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIME AS BOOLEAN))); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick
```

---

## Crash 109: `ab5ed02f1fa4418d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CAST(TRUE AS BOOLEAN))); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 110: `09f59cccf06c81fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087796`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, c1 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 111: `e6eec2e0cd94fa31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (-FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 112: `23c350f4a3304f45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090419`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (-FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 113: `ed718f6f9c9e7d71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092135`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CASE NULL OR NULL WHEN TRUE % total_changes() THEN TRUE END); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 114: `43ce525e92a5feba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094764`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT count(*) FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 115: `6a5c75bb4a1c284c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094970`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT count(*) LIKE NULL FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 116: `b4364be394703215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095300`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIME IN (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY NUL
```

---

## Crash 117: `75895c8321a36a64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096022`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 118: `7818b219d944ce6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096283`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT X'a0BDAE'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 119: `56271479446e6a42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096576`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP >> CURRENT_TIMESTAMP FROM p; CREATE VIRTUAL TABLE 
```

---

## Crash 120: `740b661785b9ac29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097777`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT * FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 121: `1a45a25c26adb9f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097982`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIMESTAMP <= CAST(CURRENT_TIMESTAMP AS FLOAT) FROM p
```

---

## Crash 122: `100bcec2db8e154a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098495`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE IN (VALUES (NULL)) | NULL IN (VALUES (NULL)) FROM p; CREATE VI
```

---

## Crash 123: `c18f0d290f3039ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099053`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, _rowid_ GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 124: `1a2300665837d201` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100724`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL + TRUE IS NOT TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 125: `379df9c367f9b335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100854`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE 
```

---

## Crash 126: `e41624b720c052ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101019`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 127: `48d33f75eb610048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101511`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL >= TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 128: `7b257f2c3c8cf6f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED WHERE NULL GROUP BY NULL, CURRENT_TIME WINDOW w1 AS (); INSERT INTO p DEFAULT VALUES; VALUES (NULL); 
```

---

## Crash 129: `c16c2a6061045caa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101929`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN CHECK (CURRENT_DATE), c2 VARCHAR(255) CHECK (CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 130: `b79064c058c225e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102063`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 131: `0a072d82df9b6128` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102350`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT TRUE, a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 132: `fc3d1ede01aaabbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102465`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT X'FecdBe'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 133: `c8b4f4badecf700b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119253`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CURRENT_TIME <> NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE 
```

---

## Crash 134: `a2f5aad8800282b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120294`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (EXISTS (VALUES (NULL) UNION ALL VALUES (CURRENT_TIMESTAMP))); EX
```

---

## Crash 135: `2f7da179e9d5f610` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121644`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EX
```

---

## Crash 136: `14a2bbb195efbbe7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122204`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CURRENT_DATE GLOB CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL
```

---

## Crash 137: `f4d422a4f4b050ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123756`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (NULL); VALUES (NULL NOT IN (SELECT * FROM q WHERE NULL GROUP BY 
```

---

## Crash 138: `113553e38e9bcfe5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126406`

```sql
SELECT printf('%f', -2147483649, '_-jK-aQUn'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, c1, a); SELECT * UNION VALUES (~CURRENT_TIME) ORDER BY RAISE(IGNORE) <= TRUE DESC NULLS FIRST
```

---

## Crash 139: `9a04b46457efdabd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128754`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME / CURRENT_TIME / FALSE); SELECT printf('%.*
```

---

## Crash 140: `f6f0df3f22cfe4db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130671`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (typeof(NULL)); CREATE VIRTUAL TABLE I
```

---

## Crash 141: `3f1666015822cea5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131326`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CURRENT_DATE); VALUES (TRUE) UNION SELECT * FROM q NOT INDEXED O
```

---

## Crash 142: `12509c67cdc4a792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141852`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE + FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 143: `cd9e235e959f252d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143930`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, _rowid_ GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 144: `5f134a4d039f4b81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144071`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT NULL IN (VALUES (_rowid_)) FROM p; SELECT printf('%.*g', -2147483649
```

---

## Crash 145: `3c19bec0c773ec5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144777`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIMESTAMP <= CAST(CURRENT_TIMESTAMP AS VARCHAR(255))
```

---

## Crash 146: `ca724b98af958e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144919`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT FALSE | CURRENT_TIMESTAMP <= TRUE FROM p; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 147: `26679c9f1f0c4fad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146107`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT TRUE << FALSE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 148: `4a6baf79714923e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146627`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP >> ' 6- 8-E 71Kng5 _9c' FROM p; SELECT printf('%.*
```

---

## Crash 149: `602b94c9a5a6a9dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146893`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP >> -9.01 FROM p; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 150: `10e83a15d472ee59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148374`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT -16.162554881690747041415056 IN (VALUES (TRUE)) FROM p; SELECT print
```

---

## Crash 151: `947220f2f2fed964` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148484`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_DATE IN (VALUES (TRUE)) FROM p; SELECT printf('%.*g', -21474
```

---

## Crash 152: `c9b5b63309d28ae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148520`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIME IN (SELECT NULL FROM p NOT INDEXED WHERE TRUE GROUP BY 
```

---

## Crash 153: `33244ea4041b88d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149614`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q AS (SELECT *) SELECT min(TRUE) FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 154: `0210251f69c5f56c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150949`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC DEFAULT X'4c6bFdE6Dfc6dA'); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT V
```

---

## Crash 155: `582285add0c6094f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CASE NULL OR 'u7 -M-0 - ' WHEN group_concat(CURRENT_TIME, '0  _00p v -7-F 1') THEN CURRENT_TIMESTAMP END); SELECT printf('%.*f', 2147483647, 1e30
```

---

## Crash 156: `b1a2dce5b49ccd85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152111`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); VALUES (CASE CURRENT_TIME WHEN group_concat(CURRENT_TIME, '0  _00p v -7-F 1') THEN CURRENT_TIMESTAMP END); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 157: `25efe225a93a508e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153115`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT X'3a'); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), 
```

---

## Crash 158: `6943129d4e40a67d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154781`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 159: `b25c746035a63d80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157070`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER GENERATED ALWAYS AS (EXIST
```

---

## Crash 160: `fc40b5f376426fdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157850`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CAST(FALSE NOT BETWEEN TRUE AND TRUE AS VARCHAR(255)))); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE 
```

---

## Crash 161: `1d61b3f26f203a95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166641`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE, a BLOB GENERATED ALWAYS AS (NULL) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 162: `77bea2928b79e5bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE), b BLOB PRIMARY KEY); INSERT INTO p (c2) VALUES (CURRENT_TIME) ON CONFLICT(b) DO UPDATE SET c2 = TRUE; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 163: `6d7a9619e7be7f61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167222`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (TRUE), b BLOB PRIMARY KEY); INSERT INTO p (c2) VALUES (CURRENT_TIME) ON CONFLICT(b) DO UPDATE SET rowid = TRUE; PRAGMA quick_check; CREATE VIRTUAL TABLE 
```

---

## Crash 164: `a6769d988e7ee55c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170858`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS WITH q (c2) AS (VALUES (NULL)), t1 AS (VALUES (CURRENT_TIME)) SELECT *; SELECT CAST(CURRENT_DATE AS INT) AS e0; CREATE VIRTUAL TA
```

---

## Crash 165: `78e767fb19874d28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170958`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS WITH q (c2) AS (VALUES (NULL)), t1 AS (VALUES (CURRENT_TIME)) SELECT *; SELECT NOT EXISTS (SELECT TRUE AS o_s9 ORDER BY NULL ASC 
```

---

## Crash 166: `afa565c81c258f7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171752`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (min(FALSE) FILTER (WHERE NULL)) UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 167: `1b4ffcd40e99ea83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173557`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); SELECT DISTINCT count(*) OVER () AS a, * FROM (VALUES (FALSE)) AS xx8l6z NATURAL JOIN p NOT INDEXED 
```

---

## Crash 168: `af7c4387b46cfa9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (SELECT * FROM p NATURAL JOIN p) AS xx8l6z NATURAL 
```

---

## Crash 169: `45ceff23f8f09411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177462`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE; CREATE VIRTUAL TA
```

---

## Crash 170: `0f3c8c9d35f6223e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177470`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS xx8l6z NATURAL JOIN p NO
```

---

## Crash 171: `dcfee9a29e6057bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177477`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (SELECT * FROM p) AS xx8l6z NATURAL JOIN p NOT INDE
```

---

## Crash 172: `16d5c71e4c7b2c9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177757`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (SELECT min(FALSE) OVER ()) AS xx8l6z NATURAL JOIN 
```

---

## Crash 173: `478e9ba850445b90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177962`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (SELECT CURRENT_DATE) AS xx8l6z NATURAL JOIN p NOT 
```

---

## Crash 174: `29d461d98a378512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177968`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (SELECT count(*) OVER ()) AS xx8l6z NATURAL JOIN p 
```

---

## Crash 175: `110e184a47de3912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178177`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT count(*) OVER () AS a, * FROM (VALUES (FALSE)) AS xx8l6z N
```

---

## Crash 176: `5319921fe2787118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178314`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, * FROM (VALUES (FALSE)) AS xx8l6z NATURAL JOIN p NOT IN
```

---

## Crash 177: `1f030fe030f0f92e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178320`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT FALSE AS a, * FROM (VALUES (FALSE)) AS xx8l6z NATURAL JOIN
```

---

## Crash 178: `2ce4f568a18dcc2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182722`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (-240481474.159680973055); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 179: `50e2f3735bc0c12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182857`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (~random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 180: `c0681816d9951318` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183194`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 181: `9bb39042fd728368` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183357`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (changes()); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e30
```

---

## Crash 182: `54e2476cdc6b1665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183480`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 183: `70d3eadc826cce9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184431`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_r
```

---

## Crash 184: `a8ca2cc69a86736b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184575`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (~TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 185: `442ccb09afe6ca29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185496`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c2 GENERATED ALWAYS AS (a + -4) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 186: `2798037b420b9152` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186374`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 187: `e0b1247d9271d425` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188166`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p SELECT FALSE AS a; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALU
```

---

## Crash 188: `6a1042bf8edd68b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188577`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NATURAL JOIN p NOT INDEXED WHERE NULL; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 189: `7f4c4b6c2a06cdd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189842`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM (VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_TIMESTAMP)) AS d8j GROUP BY FALSE; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 190: `a8137eed46bcfed5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190015`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM p GROUP BY FALSE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUE
```

---

## Crash 191: `be3b9d713a3962ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190029`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM (SELECT * FROM p NOT INDEXED) AS d8j GROUP BY FALSE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 192: `557a4ecec989ae13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190251`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM (SELECT count(CURRENT_TIME) OVER () AS a) AS d8j GROUP BY FALSE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 193: `56e033f0bdf22e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190676`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT CURRENT_TIME AS a FROM p; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); SELECT * FROM p JOIN p 
```

---

## Crash 194: `db1d350f390e4d45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192014`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT min(FALSE) OVER (PARTITION BY CURRENT_TIMESTAMP, TRUE) INTERSECT VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 195: `65ca96163d78763e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192563`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p VALUES (count(*) FILTER (WHERE NULL)) UNION ALL VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 196: `e9dacca963b3be75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193185`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT DISTINCT * FROM p WHERE TRUE ORDER BY NULL ASC NULLS LAST LIMIT FALSE OFFSET NULL; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 197: `5df85a642d82e7ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194318`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL DEFAULT X'B27fD534fCfD'); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p ORDER BY FALSE ASC NULLS FIRST)
```

---

## Crash 198: `420ae80f000e0a27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194928`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT sum(TRUE) FROM (VALUES (CURRENT_TIME)) AS tok9tvdd_0a___g4
```

---

## Crash 199: `8e02a8c94a6ef0b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195564`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT FALSE ORDER BY FALSE COLLATE NOCASE ASC, FALSE); CREATE VI
```

---

## Crash 200: `c374212c776751de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195856`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED ORDER BY RAISE(IGNORE) DESC NULLS FIR
```

---

## Crash 201: `31ec86d58cc10214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196430`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); WITH RECURSIVE r (a) AS (VALUES (CURRENT_DATE)) SELECT CASE CURRENT_DATE WHEN -TRUE THEN FALSE 
```

---

## Crash 202: `9765fafac2ca2b60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196638`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATURAL LEFT
```

---

## Crash 203: `bc991c1592f52e2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197312`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATURAL JOIN
```

---

## Crash 204: `8daaefa58834f184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197490`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATURAL LEFT JOI
```

---

## Crash 205: `b3936cbfc8cacd34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199461`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p ORDER BY c2 ASC NULLS LAST); SELECT printf('%.*f', 2147483647, 1e
```

---

## Crash 206: `7cd06e125cbbe694` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200545`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q WHERE TRUE IN (VALUES (TRUE)) GROUP BY TRUE WINDO
```

---

## Crash 207: `b6719ccbf99f3da3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201685`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (CASE CURRENT_TIME WHEN NULL > CURRENT_DATE > 
```

---

## Crash 208: `c3b82f35f85ed048` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201891`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (CURRENT_TIME) INTERSECT VALUES (CURRENT_DATE)
```

---

## Crash 209: `8cdd5c6b8c2e4a3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (TRUE NOT IN (TRUE NOT IN (TRUE NOT IN (CURREN
```

---

## Crash 210: `53e0e9b165a4f93e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202947`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE UNION ALL VALUES (CURRENT_DATE)); CREATE VIRTUAL TABL
```

---

## Crash 211: `1c4ff1d300e499e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203685`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE COLLATE RTRIM AS m FROM p ORDER BY CURRENT_TIME ASC);
```

---

## Crash 212: `bea11a28a1c3b242` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206693`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q WHERE ~NULL); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 213: `20d8ecc141ef321c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206840`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM (VALUES (CURRENT_TIME)) AS tok9tvdd_0a___g
```

---

## Crash 214: `08d9547c09bdb17b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207334`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(DISTINCT CURRENT_DATE) INTERSECT VALUES (CURRENT_DAT
```

---

## Crash 215: `0dd30ce17d5cb76d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207578`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT FALSE NOT LIKE char(NULL) INTERSECT VALUES (CURRENT_DATE))
```

---

## Crash 216: `7e9154a5825f4455` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207754`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT FALSE NOT LIKE changes() INTERSECT VALUES (CURRENT_DATE));
```

---

## Crash 217: `83f5d25d9c241540` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207912`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT char(NULL) INTERSECT VALUES (CURRENT_DATE)); CREATE VIRTUA
```

---

## Crash 218: `516fef534bf410ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208503`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT group_concat(CURRENT_DATE) OVER (ORDER BY TRUE DESC NULLS 
```

---

## Crash 219: `4fe95cdfa586392a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209090`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT (SELECT count(*) INTERSECT VALUES (CURRENT_DATE)) NOT LIKE
```

---

## Crash 220: `98af57fad349ff35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211157`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT min(FALSE) OVER (PARTITION BY CURRENT_TIMESTAMP, TRUE) INT
```

---

## Crash 221: `7d7cf7bbda64d6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212719`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), _rowid_ GENERATED ALWAYS AS (a) NOT NULL); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 222: `64b03382f570e110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216047`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, b, c1, c1); SELECT CAST(FALSE | CURRENT_TIMESTAMP MATCH CURRENT_DATE LIKE CURRENT_TIME IS NOT TRUE AS NUM
```

---

## Crash 223: `ff3b793888a39785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221008`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_DATE NOT BETWEEN FALSE AND CURRENT_DATE INTERSECT 
```

---

## Crash 224: `0b2a7a1c1d13eefb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222078`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT NULL || CURRENT_TIMESTAMP NOT NULL INTERSECT VALUES (CURRE
```

---

## Crash 225: `ce093fa435a1c36e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222461`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT (SELECT * FROM q) NOT LIKE count(*) INTERSECT VALUES (CURR
```

---

## Crash 226: `6b44009767ffdeba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226059`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT typeof(NULL) INTERSECT VALUES (CURRENT_DATE)); CREATE VIRT
```

---

## Crash 227: `9157da0c6586c162` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (FALSE, FALSE, CURRENT_TIMESTAMP) INTERSECT VA
```

---

## Crash 228: `6fc766142ec83715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226436`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (FALSE, NULL) INTERSECT VALUES (CURRENT_DATE))
```

---

## Crash 229: `caf2dd9579672c2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226835`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP LIKE CURRENT_DATE ESCAPE FALSE INTERSECT
```

---

## Crash 230: `b1b77419c9b86f21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227713`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE NOT IN (0) INTERSECT VALUES (CURRENT_DATE)); CREATE V
```

---

## Crash 231: `3d7069be5aa88179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228717`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q WHERE FALSE GROUP BY NULL, CURRENT_TIME WINDOW w1
```

---

## Crash 232: `d25f62c8ffc59c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q WHERE CURRENT_TIMESTAMP COLLATE NOCASE <= CURRENT
```

---

## Crash 233: `53a27a87883ede4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230118`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p) 
```

---

## Crash 234: `6c44c479294fec18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230212`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT FALSE ORDER BY -CURRENT_TIMESTAMP ASC NULLS FIRST); CREATE
```

---

## Crash 235: `0a81c11709a36d83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231117`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT sum(TRUE) FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATU
```

---

## Crash 236: `087880862d62e5c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED INNER JOIN p NOT INDEXED NATURAL LEFT
```

---

## Crash 237: `ac2a0781ccfe47d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231865`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p VALUES (TRUE) UNION SELECT * FROM p NOT INDEXED ORDER BY TRUE ASC; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 238: `468d50fb3d6fb353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233024`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p WITH p AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM p NATURAL JOIN p NOT INDEXED WHERE CURRENT_TIME; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 239: `33e49540a2ce9b2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233203`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT count(*) OVER (PARTITION BY CURRENT_TIMESTAMP, NULL NOT IN (FALSE)) INTERSECT VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT pr
```

---

## Crash 240: `02eeaffcecfa0673` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234534`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM (SELECT * FROM p NOT INDEXED) AS d8j GROUP BY NULL, CURRENT_TIME; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 241: `91ecf7a32221d805` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234584`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p SELECT * FROM (VALUES (TRUE)) AS d8j GROUP BY NULL, CURRENT_TIME; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 242: `c46873187b87eefe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239785`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSER
```

---

## Crash 243: `061a99eed55437a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241340`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 244: `77111ba8f8076516` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241411`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 245: `f3e5b277c6efb9ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245726`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT p.* FROM (VALUES (FALSE)) AS xx8l6z NATURAL JOIN p NOT IND
```

---

## Crash 246: `ba8dc06f60974cc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245828`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT p.* FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED WHERE CU
```

---

## Crash 247: `85785b171f74ca42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT min(CURRENT_DATE IN (SELECT min(FALSE) OVER () UNION ALL VALUES (CU
```

---

## Crash 248: `d9200ff8fde34f17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246865`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT min(CURRENT_DATE IN (SELECT min(FALSE) OVER () UNION ALL VALUES (CU
```

---

## Crash 249: `4e2d6db1e05bf6de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248084`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, *, *, *, *, *, * FROM (VALUES (FALSE)) AS xx8l6z LEFT J
```

---

## Crash 250: `adcd7ca7eb1ec08c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248559`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM (VALUES (FALSE)) AS xx8l6z LEFT JOIN p NOT INDEXED 
```

---

## Crash 251: `c193a145b8860b11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249505`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT I
```

---

## Crash 252: `ed12f9cc94e7f031` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249536`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE 
```

---

## Crash 253: `ae7506ac42121adf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249556`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT X'FecdBe'); 
```

---

## Crash 254: `8a613394ff151c3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249565`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT 'eI2'); INSERT
```

---

## Crash 255: `ff9b735f1ced1c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251512`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); SELECT DISTINCT count(*) OVER () AS a, count(CURRENT_TIME) OVER () AS a, * FROM p NOT INDEXED WHERE 
```

---

## Crash 256: `e18c9d9ddf844625` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251699`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); SELECT DISTINCT *, count(CURRENT_TIME) OVER () AS a, * FROM p NOT INDEXED WHERE CURRENT_DATE; CREATE
```

---

## Crash 257: `003e080fa26e692d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251705`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); SELECT DISTINCT CURRENT_DATE AS a, count(CURRENT_TIME) OVER () AS a, * FROM p NOT INDEXED WHERE CURR
```

---

## Crash 258: `c4f191b3fe178b8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253581`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 259: `994af5bf29d20baf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253896`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 260: `7d38bf982c37ad02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259842`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL, b BLOB PRIMARY KEY); INSERT INTO p (c2) VALUES (CURRENT_TIME) ON CONFLICT(b) DO UPDATE SET rowid = TRUE; PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 261: `10245bffa8efce59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260220`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER CHECK (CURRENT_DATE IS NOT _rowid_ IS NOT NULL), b BLOB PRIMARY KEY); INSERT INTO p (c2) VALUES (CURRENT_TIME) ON CONFLICT(b) DO UPDATE SET c2 = TRUE; PRAGMA qu
```

---

## Crash 262: `b544ee4afdf9ae94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260389`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSE
```

---

## Crash 263: `83acedeae6d64632` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260791`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE, a BLOB GENERATED ALWAYS AS (NULL) STORED); INSERT INTO p SELECT NULL INTERSECT VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647,
```

---

## Crash 264: `366c2f96ddce7c36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262128`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c2); SELECT t3.* FROM s WHERE EXISTS (SELECT p.*, p.* FROM q AS a WHERE NULL ->> ++TRUE != TRUE >= FALSE 
```

---
