# Crash Triage Report

**Total crashes:** 300  
**Unique crash sites:** 300  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 300 | 300 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `7e1e78ed4c756800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000102`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT random() AS h_kn7m, +CURRENT_TIME NOTNULL COLLATE NOCASE COLLATE NOCASE FROM p JOIN s et___r__idx_0_cy84 ON CASE WHEN FALSE AND CURRENT_
```

---

## Crash 2: `abc08ae413b939d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000132`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, b); SELECT p.*, +CASE NOT CURRENT_DATE IS NOT CURRENT_DATE | CURRENT_TIMESTAMP IS NULL WHEN CURRENT_TIMESTAMP - CURRENT_DATE <> RAISE(IGNOR
```

---

## Crash 3: `d211d325a5f782a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000667`

```sql
SELECT substr('7M', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3); INSERT OR ROLLBACK INTO q VALUES (CASE WHEN (FALSE COLLATE RTRIM * FALSE COLLATE NOCASE <= CASE WHEN
```

---

## Crash 4: `99ea676a49f0bb7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000761`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, c2, a, a, c1, b); SELECT RAISE(IGNORE) FROM q WHERE EXISTS (SELECT CURRENT_TIME AS pt50__r961_h_1_1a2xx_9_85ze_se2__3x_q6_t6s503__ql0h8_3714
```

---

## Crash 5: `e4382e98fc8c94e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000885`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c3, c2, b, b, b, b, c3); WITH RECURSIVE p (c3) AS NOT MATERIALIZED (SELECT DISTINCT ~RAISE(IGNORE) % RAISE(IGNORE) AS i_____ FROM p NOT INDE
```

---

## Crash 6: `eeeb6fe3e75dc1c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001812`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 7: `b7c907de44707e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001818`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_TIME AS a FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*s'
```

---

## Crash 8: `2db017c0ac3b9295` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001824`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT *, FALSE AS e4258_____l__6qzj FROM (SELECT CURRENT_TIME AS a FROM p WHERE CURRENT_DATE) A
```

---

## Crash 9: `321cb5d717afb43a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001831`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT NULL ISNULL, FALSE AS e4258_____l__6qzj FROM (SELECT CURRENT_TIME AS a FROM p WHERE CURRE
```

---

## Crash 10: `3d50580514f3b939` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001837`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT CURRENT_TIMESTAMP IS NOT NULL ISNULL, FALSE AS e4258_____l__6qzj FROM (SELECT CURRENT_TIM
```

---

## Crash 11: `883911aabf51f635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001885`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r (c1) VALUES (FALSE) ON CONFLICT(rowid) DO UPDATE S
```

---

## Crash 12: `7a6f423332187a3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001893`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*s', 4294967296); C
```

---

## Crash 13: `39bbaacef4864db0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001899`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; SELECT printf('%.*s', 4294967296); CREATE VI
```

---

## Crash 14: `839f83938fa353ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001924`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*s', 429496729
```

---

## Crash 15: `426e29a04d996d4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001948`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (TRUE); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 16: `dcacdf18b4a50baa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001958`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT FALSE IS NOT NULL ISNULL, * FROM (SELECT CURRENT_TIME AS a FROM p WHERE CURRENT_DATE) AS 
```

---

## Crash 17: `9af0268d398f80ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002038`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); VALUES (CURRENT_TIME); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 18: `a12437f1f5402882` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002049`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT NULL ISNULL, * FROM (SELECT * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*s', 42949672
```

---

## Crash 19: `0902947b73b5db95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002066`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r (c1) VALUES (FALSE) ON CONFLICT(rowid) DO UPDATE SET c2 = CURRENT_TIM
```

---

## Crash 20: `aae8608ca8944827` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002216`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 21: `f170106aff9362c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002240`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; S
```

---

## Crash 22: `08b5d33a356e0be0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002407`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (TRUE) STORED, c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 23: `e3f4b975871e8472` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002454`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN VALUES (TRUE IS NULL); SELECT round(-1.0, -1); SELECT printf('%.*f', 0);
```

---

## Crash 24: `e1ba631e74acb240` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002461`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN VALUES (TRUE
```

---

## Crash 25: `24f39e1fdbe9b884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006670`

```sql
SELECT round(0.01, 0); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (-02109.57207393160709696079666681286384540837795192
```

---

## Crash 26: `b1197f87edb24b3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006804`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL *, NULL IS NOT NULL NOT LIKE FALSE IS TRUE NOT
```

---

## Crash 27: `722e3a23ecf37103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007370`

```sql
SELECT substr('', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q SELECT DISTINCT * FROM q WHERE TRUE NOTNULL ORDER BY (NULL) IS DISTINCT FROM RAISE(IGNORE) * CUR
```

---

## Crash 28: `2a900556bd2591a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007451`

```sql
SELECT printf('%s', -1, '  i'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, b); WITH RECURSIVE s AS (WITH RECURSIVE p AS NOT MATERIALIZED (SELECT * LIMIT TRUE) SELECT json_object(
```

---

## Crash 29: `e1b6c5f41d9492e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007786`

```sql
SELECT substr('  ', -9223372036854775808, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO p VALUES (FALSE); SELECT *, CURRENT_TIMESTAMP AS yko__cb9_c_b_t_
```

---

## Crash 30: `19f376ee0ba08b6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007967`

```sql
SELECT substr('_-8 4-W 1', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO t1 VALUES (CAST(TRUE AS INT), t1.c2); EXPLAIN QUERY PLAN SELECT ALL CURRENT_TIMES
```

---

## Crash 31: `8fdf940b529e3675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008108`

```sql
SELECT printf('%.*s', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); INSERT OR FAIL INTO p VALUES (FALSE NOT NULL = CURRENT_TIMESTAMP == CASE total_changes() FILTER (WHERE CURR
```

---

## Crash 32: `b819ece938a6fb27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008203`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT FALSE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT NOT C
```

---

## Crash 33: `6a62875b21417b8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008223`

```sql
SELECT printf('%.*g', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', -2147483649, 0.01); CREATE TABLE IF NOT EXIS
```

---

## Crash 34: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008318`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 35: `c4dee75a3c2790ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010854`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL TRUE NOT BETWEEN CURRENT_TIMESTAMP AND NULL <> CURRENT_TI
```

---

## Crash 36: `b2ca0ccad6206b63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011660`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (CURRENT_DATE), c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick
```

---

## Crash 37: `0b0c658f5b44c6cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011679`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (CURRENT_DATE), c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick
```

---

## Crash 38: `c853ad61d187d574` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011703`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483648)
```

---

## Crash 39: `73f119fd2f4b88a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011709`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY, c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; S
```

---

## Crash 40: `26f8a21dfcf04e55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012643`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((VALUES (TRUE))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 41: `99a01e6e2412e37a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012724`

```sql
SELECT round(1.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE q (c3) AS NOT MATERIALIZED (VALUES (NULL) ORDER BY CURRENT_DATE ASC NULLS LAST, RAISE(IGNORE) >> RAISE(IG
```

---

## Crash 42: `2522cc638639d64d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012733`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((VALUES (TRUE))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 43: `66791b1e0eee9f56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016326`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 44: `83100027b4b62c9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016436`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS LAST LIMIT FA
```

---

## Crash 45: `c170030d95688157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020612`

```sql
SELECT round(1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO t1 DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT +~+FALSE GLOB '' GLOB FALSE NOT NULL, t3.*, CURRENT_TIMES
```

---

## Crash 46: `f25bff49e9c8c12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020889`

```sql
SELECT substr('_-  -zzI2 _lS -Nt', 4294967295, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 47: `a940d988345cd551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022405`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 48: `a6e2c252528ecc2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022794`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(-92233
```

---

## Crash 49: `83b7c468cd87b263` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023095`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1
```

---

## Crash 50: `8dc8af9bc60bfe54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024229`

```sql
SELECT printf('%x', 0, ' xE j7_7X_9e '); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 51: `f3368894871c5e09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026441`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 TEXT CHECK (TRUE)); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 52: `6bfdd47c5e578f44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027144`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 53: `898cd9cbd5b4230f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030416`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); INSERT INTO q (c2) VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 54: `8532d97c2a0c1627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030611`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); INSERT INTO q (c2) VALUES (CURRENT_TIMESTAMP); ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a,
```

---

## Crash 55: `020e32018b64d2b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032349`

```sql
SELECT substr(' _f - -L6_-_   -L', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 56: `00f26d467866b3c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033177`

```sql
SELECT round(-1e308, 0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 57: `3863e69d8e27a59e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033853`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (VALUES (CURRENT_DATE)), q AS (VALUES (TRUE)) SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 58: `9d081fd2949723f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034111`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH t3 AS (SELECT *) SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 59: `537758b5a128e659` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034172`

```sql
SELECT printf('%.*g', 0, -1e308); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 60: `2c966521bd7c3f84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035056`

```sql
SELECT printf('%f', -9223372036854775808, 'x_j_G'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); VALUES (CURRENT_DATE);
```

---

## Crash 61: `b38b398e7674dff2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036175`

```sql
SELECT printf('%.*e', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CASE FALSE << FALSE NOT NULL WHEN NOT EXISTS (SELECT FALSE LIMIT TRUE) THEN count(*) ELSE (VALUES (RAISE(IGNOR
```

---

## Crash 62: `ffeb26dc77d4f12e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039287`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT CURRENT_TIMESTAMP, * FROM q NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 63: `564b4e3dd5e57c05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040107`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND FALSE; CREATE VIRTUAL TABLE IF N
```

---

## Crash 64: `06bbf6d679a036ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040281`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE FALSE | CURRENT_TIME BETWEEN TRUE COLLATE NOCASE AND FALSE; CREATE VIRTUAL 
```

---

## Crash 65: `dae8fe24fbf779ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040448`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 66: `298213ae0aa9de7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041313`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (TRUE) STORED, c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC 
```

---

## Crash 67: `6c9425eb965c43d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041633`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (TRUE) STORED, c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a BLOB CHECK (
```

---

## Crash 68: `b7773c29a09cfdf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042049`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 69: `1f26de1ce69f387d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045678`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT NO
```

---

## Crash 70: `bc51749862fe51ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045823`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a) NOT NULL); VALUES (NULL); SELECT substr('- 4_-Pm9_i15 ', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 71: `ae4cc54d9e4ab61f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045831`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a) NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); SELECT substr('- 4_-Pm9_i15 ', -9223372036854775808); CREATE VIRTUAL TABLE IF N
```

---

## Crash 72: `4bd89c6636812b06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046258`

```sql
SELECT printf('%.*d', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE t1 AS MATERIALIZED (SELECT * INTERSECT VALUES (TRUE, FALSE) ORDER BY -TRUE ASC NULLS FIRST),
```

---

## Crash 73: `06d96b1e8afe3809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046307`

```sql
SELECT printf('%.*g', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO t2 (c3) VALUES (CURRENT_TIME) ON CONFLICT(a) DO UPDATE SET a = CASE WHEN NULL THEN CURRENT
```

---

## Crash 74: `5e79d07d55050272` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046535`

```sql
SELECT printf('%.*d', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE NOT NULL << CURRENT_DATE - CURRENT_DATE + FALSE || CASE
```

---

## Crash 75: `2c16ef0a66774746` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046580`

```sql
SELECT round(-1.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE r AS NOT MATERIALIZED (SELECT DISTINCT FALSE AS a FROM t2 LEFT OUTER JOIN (p NOT INDEXED) JOIN 
```

---

## Crash 76: `417343d14d4d6002` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048094`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (CURRENT_DATE AND TRUE OR FALSE)); INSERT INTO p VALUES (NULL); VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 77: `408b93a9d14274ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048288`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (NULL)); INSERT INTO p VALUES (NULL); VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 78: `518bfe3c595ae31a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049976`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 79: `1d85095dd84680c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050708`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT min(NULL) FILTER (WHERE FALSE), * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1;
```

---

## Crash 80: `87d677bd36731389` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051836`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT TRUE NOT BETWEEN CURRENT_TIMESTAMP AND NULL AS x_e0p_ FROM (SELECT * FROM p WHERE FALSE) 
```

---

## Crash 81: `9beac204e5c6a69f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051990`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE NULL; CREATE V
```

---

## Crash 82: `18fc361cab76746b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052346`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 83: `79b75256ba0d6705` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052561`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (count(*)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 84: `160b214955bc5bdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053176`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (077345029077614816317134512984377825757251101639199666875343860923710776177714436049922393633324672491450854744
```

---

## Crash 85: `5d0fc42106ecd29a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053484`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE NULL ORDER BY NULL DESC NULLS FIRST; PRAGMA quick_check; CREATE VI
```

---

## Crash 86: `c7039525bf18270c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053894`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p NOT INDEXED; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 87: `fc4f676dccfda0d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054411`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p GROUP BY NULL LIMIT CURRENT_DATE; SELECT 
```

---

## Crash 88: `8b1bd92ffb77bbcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054607`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY);
```

---

## Crash 89: `22935a76b03d1188` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054755`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE, c2 GENERATED A
```

---

## Crash 90: `4a746ff0321a495c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057031`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CAST(CURRENT_TIMESTAMP AS BOOLEAN); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 91: `c449132a7f41e6f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057231`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE MATCH NULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 92: `0863d2c404a968e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057754`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c3 BLOB, c2 TEXT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 93: `ec2778e656b1ff20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058046`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NOT EXISTS (VALUES (RAISE(IGNORE))) BETWEEN NULL AND NULL; SELECT round(0.0
```

---

## Crash 94: `fdc3cd7aaf560c9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058458`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(b TEXT DEFAULT X'cE'); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 95: `82d641f637341ab0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255), c3 FLOAT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 96: `f1df6882b024d847` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE, c3 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 97: `50f9ca8e656ef532` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060287`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 98: `54b363d2c12a7db6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061006`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY NULL HAVING NU
```

---

## Crash 99: `7ba28a27fb872674` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061287`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE + CURRENT_TIME; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 100: `cce8be53b6e68b0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061293`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE IS NULL + CURRENT_TIME; SELECT printf('%.*g', -2147483649, 0.0
```

---

## Crash 101: `eedd0d8ceebdfffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061438`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 102: `fa7d6971e06ee17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061911`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS FIRST LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 103: `59dfc7297ac004f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063506`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NOT INDEXED LIMIT -CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 104: `f622fd1d07dd28a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064222`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO q VALU
```

---

## Crash 105: `9b875742f4c7d9f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT 
```

---

## Crash 106: `49ab04d959fbfffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070821`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); INSERT INTO q (a) VALUES (NULL ->
```

---

## Crash 107: `b60bb156e252ca1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072992`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INT PRIMARY 
```

---

## Crash 108: `ac778a25289595bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075137`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT ''); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 109: `caa352a91a069f90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075169`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT CHECK (CURRENT_TIME IS TRUE), c3 INTEGER NOT NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 110: `d0c56f63355beb72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075225`

```sql
SELECT round(-1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 111: `b47d1c1ff17e4d34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078129`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); EXPLAIN 
```

---

## Crash 112: `6a45db1f3f1bddc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078511`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); EXPLAIN 
```

---

## Crash 113: `26e789d0005c981b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081428`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT p.* FROM p JOIN q g_71 ON +CURRENT_TIMESTAMP < changes() ->> typeof(TRUE * NOT CURRENT_TIME NOT IN (TRUE
```

---

## Crash 114: `c24800a1d6e2c79c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083078`

```sql
SELECT printf('%.*e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, b); SELECT CURRENT_TIMESTAMP - FALSE IS NOT DISTINCT FROM FALSE < TRUE, CURRENT_TIME IS NOT NULL AS a, t1.*, NOT
```

---

## Crash 115: `9336b04304f444ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083255`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 TEXT CHECK (CURRENT_TIME OR TRUE)); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 116: `54578cfad8a22e19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083520`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT ALL *, count(DISTINCT TRUE) FILTER (WHERE FALSE) AS x_e0p_ FROM p NOT I
```

---

## Crash 117: `a86501ea3ad36692` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089862`

```sql
SELECT printf('%x', 0, ' xE j7_7X_9e '); SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c3, a); SELECT t3.* FROM t2 NATURAL JOIN t3 WHERE NOT CASE (FALS
```

---

## Crash 118: `06b7695a67b2e180` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090554`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 119: `7f80b5d613e4ae42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090786`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (-FALSE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 120: `792e7d179fd05b4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090940`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NULL IN (CURRENT_TIMESTAMP))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 121: `18a59d6f370138d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093938`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (-TRUE + CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 122: `5d83e2b53f9c11a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094019`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (-CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 123: `20d0f786b3cf4922` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -214748
```

---

## Crash 124: `e4626c7adf118a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094616`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (FALSE NOT BETWEEN FALSE AND NULL > CURRENT_TIMESTAMP | TRUE / CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAU
```

---

## Crash 125: `35bfb8371ae4a775` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095250`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (FALSE NOT BETWEEN FALSE AND CURRENT_TIME | TRUE / CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 126: `a6d2ae82aee0129c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095632`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE > FALSE NOT NULL | CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 127: `afcb1886b04c815c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095664`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_DATE > FALSE | CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 128: `800a7a03f6fc0740` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096247`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 129: `c8e3a8e786a7c8cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105004`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS LAST LIMIT TR
```

---

## Crash 130: `fa85016a40a2c1e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105245`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (NOT EXISTS (VALUES (CURRENT_DATE))); PRAGMA quick_check; CREATE VIRTUAL TABLE I
```

---

## Crash 131: `23d20d34a2698700` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106070`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 132: `42c78a700e8bff36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106370`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIME AS BLOB)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 133: `27bcd47d11cfdedd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107211`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE, c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALU
```

---

## Crash 134: `844cac5360562761` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107637`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -6, a INT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 135: `fbccda4bbf3bbfa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110044`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL IS TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 136: `e39c6cad946fb6c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110324`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL IS (VALUES (TRUE))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 137: `ea38e6350117f669` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110432`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS BOOLEAN) IS FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 138: `1f5932335200a9ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110780`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE IS TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 139: `66db385f21ed6dd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110794`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 (b, b) VALUES (substr(CURRENT_DATE IS NOT DISTINCT FROM RAISE(IGNORE), NULL LIKE CURRENT_TIMESTAMP CO
```

---

## Crash 140: `70fe4e576c55eaf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111360`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 141: `1ebfe264a38e2360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111973`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE IS TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 142: `4559790355f86c58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112632`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE IS NULL COLLATE RTRIM GLOB NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 21474
```

---

## Crash 143: `28c7b16d0af89059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112804`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 144: `e99af07c7166d47d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112881`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((VALUES (NULL OR FALSE))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 145: `685f123a06f3de19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113135`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((SELECT ALL * FROM p NOT INDEXED LIMIT CURRENT_TIME)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTU
```

---

## Crash 146: `1a3bc4bd02a56983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113347`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((SELECT ALL * FROM p NOT INDEXED LIMIT -CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRT
```

---

## Crash 147: `07972106a25be6df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113602`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (-TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 148: `f9f178332126a10d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114216`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CAST(CURRENT_DATE MATCH NULL AS BOOLEAN) = FALSE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 149: `e5c1d8233743a5ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115160`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); SELECT * FROM p GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFA
```

---

## Crash 150: `07e589e3b8493f8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116182`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT FALSE); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT s.*, abs(N
```

---

## Crash 151: `a8ba9984ea92b745` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116290`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CAST(TRUE AS INT)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; S
```

---

## Crash 152: `8380e65c837cb7bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118107`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (p.c1), c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 153: `925302cdcd6ac402` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118263`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE, c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR REPLACE INTO p VALUES (NULL, CURRENT_TIME); PRAGMA quick_check; SELECT p
```

---

## Crash 154: `da0905901f1a489a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118434`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (CURRENT_DATE), c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR REPLACE INTO p VALUES (NULL, CURRENT_TIME); PRAGMA quick_
```

---

## Crash 155: `ae8ad7a4b9a62020` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118981`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL DEFAULT -78841); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 156: `ba2de1af614f504b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119086`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 157: `a8b24ba1b07440c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119218`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT -3872.09709848127933697458406060419855510105131347202350443844415307627151305884802569914766333108597152526881516811222303777904104217); CREAT
```

---

## Crash 158: `ea3f1fd704ab17ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119269`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 159: `c0eb1348af8c1b27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126896`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (TRUE % CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 160: `7261b36f80aad55f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127039`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (TRUE % CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 161: `afbb5cf9657bc553` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127390`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); SELECT * FROM (SELECT * FROM p WHERE TRUE NOT NULL) AS sub1; SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 162: `dc2292d25980dddf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131649`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY P
```

---

## Crash 163: `6f7dceaedf674632` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132424`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSERT INTO p DEFAULT VALUES; VALUES
```

---

## Crash 164: `f86dc027ffb978b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132597`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSERT INTO p DEFAULT VALUES; VALUES
```

---

## Crash 165: `4230d08473d246a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132711`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); SELECT ALL count(*) AS a3_2__5_1_mibn_49em_z78_lk FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 166: `96510ccd4c5a5235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133118`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); SELECT ALL CURRENT_TIME COLLATE RTRIM NOT BETWEEN CURRENT_TIMESTAMP AND NULL AS x_e0p_, * FROM p NOT INDEXE
```

---

## Crash 167: `f38eef44c4a6dd29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133257`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(*) OVER (ORDER BY NULL ASC NULLS FIRST ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOW
```

---

## Crash 168: `36078c7467193a63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133444`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p
```

---

## Crash 169: `4f5cbf14310f3a29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133480`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (min(NULL COLLATE NOCASE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 170: `4434bdf226018ae1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133706`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (min(TRUE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 171: `1d306939ec866cc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134904`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES ((SELECT DISTINCT * FROM p WHERE TRUE ORDER BY NULL DESC NULLS FIRST)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAM
```

---

## Crash 172: `0bd7d1a0176d62a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135755`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP ESCAPE NOT CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); 
```

---

## Crash 173: `111f70aead647d5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136192`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE IS NULL IN (CURRENT_DATE, CURRENT_DATE, TRUE) IS TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE
```

---

## Crash 174: `d360f4c162f5943c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136221`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE IS NULL IN (NULL) IS TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 175: `e30a198970d7d7f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136333`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (NULL) UNION ALL SELECT * FROM p NOT INDEXED ORDER BY NULL DESC; EXPLAIN QUERY PLAN V
```

---

## Crash 176: `e523cd084b0bdb4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136845`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + CURRENT_TIMESTAMP + CURRENT_TIMESTAMP + CURRENT_TIMESTAMP + CURRENT_TIMESTAMP + CURRENT_TIMEST
```

---

## Crash 177: `af5c67c081bdd6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141381`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 178: `37ea246b2842097a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141485`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 179: `ebe3d9a27e1eb970` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147527`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NULL <> CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 180: `4aa17c49216cf13a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147717`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid IN
```

---

## Crash 181: `d239495c769ca196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147966`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p NATURAL LEFT JOIN p NOT INDEXED; PRAGMA q
```

---

## Crash 182: `0bf8eb8d6075580e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147973`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGE
```

---

## Crash 183: `d56579f538d73f8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148041`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT 'e 4D_ -Y9--_a _T'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 184: `0d295e370cfb137e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148727`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (TRUE / TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 185: `d3d60a7c63a5114b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150818`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NULL IS NOT FALSE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 186: `b075bd98faa2de49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158043`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY NULL HAVING NOT EXISTS (SE
```

---

## Crash 187: `94a6b4cbc7fba3e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158152`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY NULL HAVING RAISE(IGNORE);
```

---

## Crash 188: `0f4839f3d1db74ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158646`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY CASE WHEN NULL IS NOT FALS
```

---

## Crash 189: `079b8b54bb8ea778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT -59081532219410120388054958964266072125793989448153795834948182586867201144394623942673995738496114479167191088021557458.44683858); INSERT INTO p D
```

---

## Crash 190: `1bb650ecded3286e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169334`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 191: `16a032487ae42754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169381`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL TRUE NOT BETWEEN +CURRENT_DATE AND NULL AS x_e0p_, * FROM p NOT INDEXED LIMIT CURRENT_DATE; CR
```

---

## Crash 192: `a3d7f028f157aed8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169419`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT ALL * FROM q NATURAL LEFT JOIN p NOT INDEXED; CREATE VIRTUAL TABLE I
```

---

## Crash 193: `1e8f8e17815e1bc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169432`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED ORDER BY FALSE COLLATE RTRIM ASC NULLS LAST, CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL TABLE I
```

---

## Crash 194: `af46ac4c3e02bd54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172572`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT NOT NUL
```

---

## Crash 195: `92cb92357157db8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172600`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255
```

---

## Crash 196: `cea812f89bb4b0fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172610`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INTEGER PRIM
```

---

## Crash 197: `bf9878fb46fff4c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172755`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (NULL IN (CURRENT_DATE, CURRENT_DATE, TRUE))); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELEC
```

---

## Crash 198: `414f20da329af02c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172845`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 
```

---

## Crash 199: `83e2cd4a71680724` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175827`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) INTERSECT VALUES (sum(CURRENT_DATE) FILTER (WHERE CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 200: `efc5c66a36117fff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176088`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) INTERSECT VALUES (sum(NOT CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 201: `cc341a430e0a70ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176590`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT X''); INSERT INTO p DEFAULT VALUES; VALUES (FALSE) EXCEPT SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (); SELECT pri
```

---

## Crash 202: `675c7a7136b8dbfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176932`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE NULL ORDER BY FALSE DESC, count(*) OVER (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 203: `db8da5a7f3fe610c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177202`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NATURAL LEFT JOIN (SELECT ALL * FROM p NOT INDEXED) AS dp0_d26_o5_3qq__z8f89_t4__z0_5__kn__r3_1_mm6_0 WHER
```

---

## Crash 204: `46d0778c9ea8b4f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT ALL count(*) FILTER (WHERE FALSE) AS x_e0p_ FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 205: `85c95d1376d36484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181679`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p NATURAL LEFT JOIN p AS uw_0_iz_i0__96b_mjq_g___6_mrj4_u0_f_0_3rjv_z0b__9zy_a_0
```

---

## Crash 206: `e5f9e9d859038a2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT ALL * FROM p NOT INDEXED) AS dp0_d26_o5_3qq__z8f89_t4__z0_5__kn__r3_1_mm6_0 JOIN p NOT INDEXED GROUP BY CURRE
```

---

## Crash 207: `41624bec2cf22412` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185168`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (ORDER BY TRUE DESC NULLS LAST, NULL DESC NULLS FIRST)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 208: `7cf1fa788a8d75a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY count(DISTINCT TRUE) FILTER (WHERE FALSE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 209: `99d89e51b1faef98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187376`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY NULL DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXC
```

---

## Crash 210: `6d70f4a0da7a9960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190501`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM (VALUES (NULL)) AS dp0_d26_o5_3qq__z8f89_t4__z0_5__kn__r3_1_mm6_0 NATURAL LEFT JOIN p NOT INDEXED ORD
```

---

## Crash 211: `8f87a6f10f192d5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190717`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) UNION SELECT * FROM p NOT INDEXED ORDER BY NULL DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 212: `045e5a695ab47b12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191225`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM (SELECT ALL * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS FIRST LIMIT TRUE) AS dp0_d26_o5_3qq__z8f89
```

---

## Crash 213: `d6af93ff9eb5c95f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192050`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE q.c1 IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 214: `a8576e1f0925f36b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192263`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY NULL HAVING CU
```

---

## Crash 215: `e69e1357e49f781f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192618`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NOT EXISTS (VALUES (NULL)) IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL 
```

---

## Crash 216: `9f5dbc2dedf5b562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193219`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 217: `15c2653d1df34778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193434`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE, c3 DATE UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 218: `d3afeb6fdb8cabb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193475`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 FLOAT NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); S
```

---

## Crash 219: `c148eb5628e66d62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193555`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CAST(TRUE OR NOT FALSE BETWEEN CURRENT_DATE AND FALSE AS INT) - CUR
```

---

## Crash 220: `5756d8221363c69e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193697`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CAST(TRUE OR NOT FALSE BETWEEN CURRENT_DATE AND FALSE AS INT) - NUL
```

---

## Crash 221: `38237ca3ef00fdff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193703`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CAST(TRUE OR NOT FALSE BETWEEN CURRENT_DATE AND FALSE AS INT) - CUR
```

---

## Crash 222: `79933e87bec31626` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193804`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255), c2 BLOB NOT NULL DEFAULT TRUE, a INT); SELECT * FROM q NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 223: `7327e84a8c391226` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194136`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB DEFAULT X'ABeeCE'); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 224: `af703560aff64629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194770`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE LIKE CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP ESCAPE TRUE; CREATE VIRTUA
```

---

## Crash 225: `24b3861f152e3c7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194990`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NULL < CURRENT_DATE; SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 226: `ecb90219cc250871` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195262`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(b TEXT DEFAULT X'cE'); SELECT * FROM q NATURAL JOIN q WHERE ~NULL IN (CURRENT_DATE, NULL); SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 227: `02d3bcac3c0cb981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195474`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE == FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 228: `fa9a93f17e1071dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196712`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE, b INTEGER PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CAST(CURRENT_TIMESTAMP AS BOOLEAN); CREATE VIRTUAL TA
```

---

## Crash 229: `269e8021bc3612b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196913`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CAST(CURRENT_TIMESTAMP AS TEXT); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 230: `6f7916f438e24f2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197085`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE FALSE IS NULL COLLATE RTRIM OR TRUE; SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 231: `88a01495f491d553` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197250`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE OR TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 232: `28208b90e4eccd2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197387`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE typeof(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, c
```

---

## Crash 233: `f71f110ab2b98826` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197441`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE total_changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b
```

---

## Crash 234: `8b1935cda81e4096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197486`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC PRIMARY KEY, c2 DATE GENERATED ALWAYS AS (X'aBF09cDE') VIRTUAL); SELECT * FROM q NATURAL JOIN q WHERE NULL; CREATE VIR
```

---

## Crash 235: `5a297b4b6c568aa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198064`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME IN (VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 236: `083b70d7d55eba51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198851`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE AND TRUE OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 237: `3f9667ce5fce9ef9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200214`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO 
```

---

## Crash 238: `3454f89af9f56c18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201506`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p (rowid) VALUES (FALSE) ON CONFLICT(b) DO UPDATE SET c2 = TRUE; PRAGMA integri
```

---

## Crash 239: `18935d4ded6a5e9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202681`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED INNER JOIN p AS ct_2tap__3g0a
```

---

## Crash 240: `b4232800ee4864f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203212`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ~NULL IN (CURRENT_DATE, NULL) AS x1_y66_5x__42v_12j8e9_3c8y_1a; CREATE VIRTUAL TABLE I
```

---

## Crash 241: `23d554f94920f87e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204334`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE NULL IS NOT NULL ORDER BY NULL DESC NULLS FIRST; PRAGMA quick_chec
```

---

## Crash 242: `94fd4bc709f2c367` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204874`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE NULL ORDER BY FALSE DESC, EXISTS (VALUES (CURRENT_DATE) UNION ALL 
```

---

## Crash 243: `e4bee1bf8c31d572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204938`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL ORDER BY FALSE DESC, EXISTS (VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME
```

---

## Crash 244: `78ac688c908a39d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205248`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE CASE WHEN CURRENT_DATE THEN CURRENT_TIMESTAMP END ORDER BY NULL DE
```

---

## Crash 245: `fb692357b3aca0ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206294`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) UNION VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 246: `d48f7e11a3bf9786` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206768`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (min(CURRENT_DATE)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 247: `e7b713e518bb6676` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207799`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT CHECK (39056769593293083780386981626747118930905036966384367896160722778444691008744426011151346301234427892310.4
```

---

## Crash 248: `b8d2b6cd301c8754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208634`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (SELECT ALL * FROM p NOT INDEXED) AS dp0_d26_o5_3qq__z
```

---

## Crash 249: `2b594d770a0dfa99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208981`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (p AS z INNER JOIN p AS ct_2tap__3g0av_b_il_zd__t9x4_p
```

---

## Crash 250: `8e6b7f9b777637e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209454`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE NULL; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 251: `5348cd5288a7d67c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209618`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT sum(TRUE) FILTER (WHERE NULL) AS x_e0p_ FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREAT
```

---

## Crash 252: `2a604b68ebae41f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210924`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT min(NULL COLLATE NOCASE) FILTER (WHERE FALSE), * FROM (SELECT * FROM p WHERE CURRENT_TIME
```

---

## Crash 253: `42f5099b4a966943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211108`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT min(NULL) FILTER (WHERE FALSE), min(NULL) FILTER (WHERE FALSE), * FROM (SELECT * FROM p W
```

---

## Crash 254: `bcb0e7bce07e93de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212279`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT -3872.09709848127933697458406060419855510105131347202350443844415307627151305884802569914766333108597152526881516811222303777904104217); CREATE INDEX IF NOT
```

---

## Crash 255: `e0594f8b817d24ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212419`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 256: `e165d207f4b76983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219980`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a) NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM p GROUP BY CURRENT_TIMESTAMP, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 257: `798a4fd2ac0c7062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220879`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAU
```

---

## Crash 258: `8e6773e740f0cc1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221056`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE INDEX IF NOT EXI
```

---

## Crash 259: `70beedd1faabb144` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221081`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN); CREATE INDEX IF NOT EXI
```

---

## Crash 260: `ec2f3d45b4b49fe2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221373`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL NOT IN (rowid)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES
```

---

## Crash 261: `ab643fc7ca869e6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221488`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL NOT IN (FALSE)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES
```

---

## Crash 262: `fbb2a7696c5bed82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221732`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IS TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 263: `13ca34dbbbe3d3af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221884`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT min(NULL COLLATE NOCASE) FILTER (WHERE FALSE), min(NULL) FILTER (WHERE FALSE), * FROM (SE
```

---

## Crash 264: `d4fcd72cf28836d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222062`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT *, min(NULL) FILTER (WHERE FALSE), * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS su
```

---

## Crash 265: `9c16c51deeaf459d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222069`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT count(*) FILTER (WHERE FALSE), min(NULL) FILTER (WHERE FALSE), * FROM (SELECT * FROM p WH
```

---

## Crash 266: `4c45555ca78b0529` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223529`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (p LEFT OUTER JOIN (p AS z INNER JOIN p AS ct_2tap__3g
```

---

## Crash 267: `2c6b2e13e77efd13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223744`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p AS z INNER JOIN p NOT INDEXED NATURAL JOIN (VALUES (
```

---

## Crash 268: `7014f3bb192d9738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223989`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE CURRENT_TIMEST
```

---

## Crash 269: `672d4d0c69aac8d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224708`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (count(DISTINCT CURRENT_DATE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 270: `7d4b6678689ccf0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224841`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (total_changes()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 271: `61c69ba7f69902e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225042`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME IS TRUE) INTERSECT VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 272: `d226c53edc805310` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225661`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) UNION VALUES (random()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 273: `b5e6db2e8bbd189b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226049`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) UNION VALUES (json_type(NULL)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 274: `88da9c6f88e2b68b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230003`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p (rowid) VALUES (FALSE) ON CONFLICT(b) DO UPDATE SET b = TRUE; PRAGMA integrity_check; CREATE
```

---

## Crash 275: `82959204eb0b0818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230572`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (TRUE), b INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p (rowid) VALUES (FALSE) ON CONFLICT(b) DO UPDATE SET _rowid_ = TRUE; P
```

---

## Crash 276: `e8dfafc92afb9807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230628`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p (rowid) VALUES (FALSE) ON CONFLICT(b) DO UPDATE SET _rowid_ = TRUE; PRAGMA integrity_ch
```

---

## Crash 277: `ecb6752bb5a0573e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231065`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (CAST(FALSE AS TEXT)) STORED, c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 278: `fa37a5ab017fa3e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233321`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE q.c1 IS NULL OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 279: `dd43d902d3cb6f34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233362`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE FALSE IS NULL OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 280: `405425ff16c93602` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234777`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB DEFAULT CURRENT_DATE, b DATE NOT NULL, c2 FLOAT NOT NULL, rowid DATE NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE
```

---

## Crash 281: `bcbfeac876e8b2d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236436`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE NOT EXISTS (SELECT ALL * FROM (SELECT ALL * FROM p NOT INDEXED) AS dp0_d26_
```

---

## Crash 282: `c30dac216ef65423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236589`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE == CAST(TRUE AS TEXT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 283: `744fc5cede80e00a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237185`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME NOT IN (SELECT * FROM q NOT INDEXED); CREATE VIRTUAL TABL
```

---

## Crash 284: `1935eea753954b55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE q.c1 IS NULL IS NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 285: `27f15a299812c25f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240473`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p DEFAULT VALUES; SELECT ALL * FR
```

---

## Crash 286: `f7e917dd175876d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT ALL CASE WHEN CURRENT_DATE THEN CURRENT_TIME END AS x_e0p_ FROM p NOT INDEXED LIMIT -CURRENT_DATE; CREATE VIRTUAL TABLE IF N
```

---

## Crash 287: `4a2f7eab299c4c93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245438`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (min(NOT EXISTS (VALUES (CURRENT_TIME))) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); SELECT t2.* F
```

---

## Crash 288: `6d2e1f1144167997` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248460`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (group_concat(CURRENT_DATE, 'lB-') OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); WITH RECURSIVE p (
```

---

## Crash 289: `b302683c92fa23b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249541`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS));
```

---

## Crash 290: `e37436e79cafcc06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253511`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE NULL ORDER BY rowid, count(*) OVER (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 291: `16ef0fe7c6347f89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255053`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP + CURRENT_DATE) INTERSECT VALUES (sum(CURRENT_DATE) FILTER (WHERE CURRENT_DATE)); CREATE VIRTUAL TABLE IF
```

---

## Crash 292: `5d8145a78a45b38f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256529`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); WITH RECURSIVE p (c2) AS (VALUES (FALSE)) SELECT NULL || group_concat(NULL, '9_17') FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 293: `a03189a0f3c79114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE TRUE LIMIT TRUE OFFSET CURRENT_
```

---

## Crash 294: `ee31031b9aa86780` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262438`

```sql
SELECT substr('_', 4294967296, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 295: `b94f897643e8fa52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262487`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p VALUES (-CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 296: `1da79589297309e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266404`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); EXPLAIN 
```

---

## Crash 297: `5455724a5a9f9b83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274115`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 TEXT CHECK (CURRENT_TIMESTAMP IS NOT CURRENT_DATE COLLATE RTRIM)); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); C
```

---

## Crash 298: `44ba0f42f16ca534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275604`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_DATE AS f__ex_6_a3 FROM q NOT INDEXED WHERE FALSE GROUP BY C
```

---

## Crash 299: `c64a301bde5d9c81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000278360`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (NULL IN (CURRENT_DATE, CURRENT_DATE, TRUE))); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); INSERT INTO p VALUES (NULL) UNION ALL SELECT * FROM p NOT I
```

---

## Crash 300: `9e7a25464c8d0c6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000284236`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_TIMESTAMP >= TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf(
```

---
