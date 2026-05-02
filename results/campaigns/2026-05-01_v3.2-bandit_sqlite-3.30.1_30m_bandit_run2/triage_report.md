# Crash Triage Report

**Total crashes:** 278  
**Unique crash sites:** 278  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 277 | 277 | 99% |
| Signal | 1 | 1 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `3193a159dd0528a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000110`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(rowid TEXT GENERATED ALWAYS AS (length(CASE WHEN CURRENT_TIMESTAMP THEN
```

---

## Crash 2: `0c12a1922b76a2b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000266`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3); SELECT FALSE > RAISE(IGNORE) AS d FROM (SELECT q.* FROM t1 WHERE +CURRENT_DATE OR CURRENT_TIME GROUP BY CURRENT_TIME HAVING c3 IS NOT 
```

---

## Crash 3: `65db0e5aa7da875f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000404`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT RAISE(IGNORE) -> FALSE = NULL IN (NULL) FROM (SELECT * FROM t3 WHERE FALSE = RAISE(IGNORE) ISNULL | total_changes() OVER () IS NOT NULL)
```

---

## Crash 4: `461f5a42b4d912c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000712`

```sql
SELECT printf('%.*f', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT total_changes() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_TIMESTAMP ASC) IN (VALUE
```

---

## Crash 5: `931af3489e76c0fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000937`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q SELECT DISTINCT p.*, TRUE AS zjn, RAISE(IGNORE) FROM p INDEXED BY b , r AS 
```

---

## Crash 6: `4e586a7ed88af225` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001130`

```sql
SELECT round(-1.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t3.*, NULL MATCH FALSE >> RAISE(IGNORE) AS a FROM p JOIN p fw ON RAISE(IGNORE) LIKE NULL ESCAPE FALSE I
```

---

## Crash 7: `7cc250de5108a1df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001494`

```sql
SELECT substr('D  W3-g-2I -_6', -2147483649); SELECT round(0.01, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT OR FAIL INTO t2 VALUES (a <= CAST(~~FALSE * NULL == tr
```

---

## Crash 8: `d3a27a24776a88c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001633`

```sql
SELECT printf('%.*f', -9223372036854775808, 1.0); SELECT substr('-8- LP--iM_-  D1', -2147483648, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT (WITH RECURSIVE s AS MATER
```

---

## Crash 9: `e57ff823d440e32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001812`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r VALUES (count(
```

---

## Crash 10: `6a3afc79b8953068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001914`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r VALUE
```

---

## Crash 11: `e124ea4258b85859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001929`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r V
```

---

## Crash 12: `4d0e1b66e8b65cf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002201`

```sql
SELECT substr('Qz', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (NOT NULL ISNULL != RAISE(IGNORE) REGEXP CURRENT_TIMESTAMP < FALSE ->
```

---

## Crash 13: `13795c99b4daad8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004268`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT t3.*, NULL MATCH FALSE >> RAISE(IGNORE) AS a FROM p JOIN p fw ON RAISE(IGNORE) LIKE NULL ESCAPE FALSE IS NOT D
```

---

## Crash 14: `0feda992bf2851cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005135`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES (NULL + CURRENT_DATE ->> CASE WHEN CASE WHEN FALSE THEN FALSE END THEN FALSE END, tot
```

---

## Crash 15: `fc9b566ed199018f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007135`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid
```

---

## Crash 16: `e2827aff76d981c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL, c2 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON CASE CURRENT_TIME WHEN CURRENT_D
```

---

## Crash 17: `3cb7b7f5c2c4d273` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008155`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON CASE CURRENT_TIME WHEN CURRENT_DATE THEN las
```

---

## Crash 18: `856304c03c481fe6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008161`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 19: `f6631516640e9961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008168`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON CASE CURRENT_TIME WHEN CURRENT_DATE THEN NUL
```

---

## Crash 20: `702e1ec10f4f247c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008174`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON CASE CURRENT_TIME WHEN CURRENT_DATE THEN TRU
```

---

## Crash 21: `ac48f32b9d261791` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008675`

```sql
SELECT printf('%.*s', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) LIMIT CURRENT_DATE; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC G
```

---

## Crash 22: `947b5344a3bb01e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008699`

```sql
SELECT printf('%lli', -1, '-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1); INSERT OR ROLLBACK INTO p VALUES (sum(CASE WHEN CAST(FALSE AS INT) ISNULL THEN CASE WHEN NULL -> +-RAI
```

---

## Crash 23: `9a7bfd9e65a430b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009031`

```sql
SELECT printf('%u', 2147483647, '3 -'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO s VALUES (group_concat(CURRENT_TIME NOT BETWEEN CURRENT_DATE AND total_changes() 
```

---

## Crash 24: `e2f91648ab0a0073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009101`

```sql
SELECT printf('%.*e', 1); SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO t2 VALUES (CAST(TRUE AS NUMERIC) IS NOT DISTINCT FROM p.b 
```

---

## Crash 25: `d9a27b942881469b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009144`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, b, b, b); INSERT OR FAIL INTO p VALUES (RAISE(IGNORE), changes() FILTER (WHERE TRUE)); EXPLAIN QUERY PLAN WITH t1 AS NOT MATERIALIZED 
```

---

## Crash 26: `e8fc1cbf12bc746f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009295`

```sql
SELECT printf('%.*s', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (b) VALUES (CASE WHEN typeof(~-RAISE(IGNORE)) FILTER (WHERE last_insert_
```

---

## Crash 27: `c28db05e28da66ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009402`

```sql
SELECT printf('%.*f', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (FALSE, NULL) RETURNING RAISE(IGNORE), q.*; ANALYZE q; CREATE TABLE 
```

---

## Crash 28: `774ecd80a9f302a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 29: `4d9c4befd48be492` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p mm ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 30: `08334520a0aaa0ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010877`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EX
```

---

## Crash 31: `0166ba6a76901ea2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011019`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 32: `4099dcd7ffc9deee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011160`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREAT
```

---

## Crash 33: `1627f8d4a66582a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011318`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF 
```

---

## Crash 34: `4cf8f50513a76156` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011346`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); C
```

---

## Crash 35: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011449`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 36: `a66f04e01653a53c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011519`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); INSERT INTO s VALUES (CURRENT_DATE IN (SELECT *) -> NULL * FALSE / CAST(p.b AS TEXT) IS NULL || json_type(RA
```

---

## Crash 37: `74d0f0eff189e5a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012767`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (VALUES (CURRENT_DATE))); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE I
```

---

## Crash 38: `bdc91d57470df550` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012825`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 39: `01f154baa18e80d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015012`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 40: `c51336a5650fcf22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015021`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c2); EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(-1));
```

---

## Crash 41: `d112ef27c7b6d066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015028`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 42: `b5c158988438bdf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015142`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 43: `4db8d0e3b1861460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015173`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 44: `29bc4024c7952749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015889`

```sql
SELECT printf('%f', 2147483647, ''); SELECT substr(' ', 4294967295, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 45: `30717ae9b27c15d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016794`

```sql
SELECT printf('%.*s', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 46: `3ed1c9949e5e281f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017553`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); 
```

---

## Crash 47: `c022f6b90065513c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018088`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.*g', -21
```

---

## Crash 48: `22e3d1757bc1621d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019628`

```sql
SELECT printf('%.*s', 4294967296); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 49: `458fe25409b1826b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019845`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 50: `9fe8c50da752d919` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020613`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST LIMIT CURRENT_DATE, total_changes() FILTER (WHERE RAISE(IGNORE)); EXPLAIN QUER
```

---

## Crash 51: `85ecbf6acb10dec4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020754`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST LIMIT TRUE; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 52: `678f45392667ba8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026223`

```sql
SELECT round(1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 53: `21232f2d4cb31b22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026571`

```sql
SELECT printf('%.*s', -2147483649); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 54: `a3728b53c7dde646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027348`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE NOT BETWEEN CURRENT_TIME AND TRUE & NULL NOTNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 55: `461c34e4fb85d883` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027905`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE NOT BETWEEN CURRENT_TIME AND FALSE & NULL NOTNULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 56: `d456fbaef0322a76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028995`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NOT FALSE >= TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (json_type(CURRENT_DATE
```

---

## Crash 57: `843919407862fd97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT *, * FROM p WHERE NULL || CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 58: `f04394b4d808fa6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030881`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT *, * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 59: `a3ddb9e6593ea2fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031056`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT *, CURRENT_DATE FROM p WHERE NULL == NULL) AS sub1; SELECT printf('%.*g', 9223372036854775807
```

---

## Crash 60: `60caa4564d896943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031164`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT CURRENT_DATE, CURRENT_DATE FROM p WHERE TRUE || CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.
```

---

## Crash 61: `222ff2eb8b3f7558` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031700`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * ORDER BY changes() OVER (PARTITION BY CURRENT_DATE ORDER BY NULL ASC NULLS LAST ROWS BETWEEN UNBOUNDED
```

---

## Crash 62: `2ec52b63c9cfc216` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031726`

```sql
SELECT printf('%.*f', 2147483647, 1e308); SELECT hex(zeroblob(2147483647));
```

---

## Crash 63: `0162295ccb76897b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034261`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (TRUE IN (FALSE) BETWEEN FALSE AND CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 64: `3392fd1804d5fb62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034487`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE, c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH p AS (V
```

---

## Crash 65: `2a20a69634b2bb13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034566`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT
```

---

## Crash 66: `ba2bc4551ddd0b27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034654`

```sql
SELECT printf('%.*d', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT_DATE REGEXP CURRENT_DATE COLLATE BINARY NOT BETWEEN TRUE AND CURRENT_TIME != RAISE(IGNORE) IS N
```

---

## Crash 67: `b205c958b66c8258` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034850`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NULL * NULL LIKE CURRENT_DATE COLLATE RTRIM == +CURRENT_DATE NOT IN (CURRENT_DATE) / 
```

---

## Crash 68: `2f249b8125bc8af0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036196`

```sql
SELECT substr('-F 0yj', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME LIKE NULL * CURRENT_TIMESTAM
```

---

## Crash 69: `3d465b69cede5038` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039128`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c2); REPLACE INTO p VALUES
```

---

## Crash 70: `b9497963371294c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039414`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN NOT NULL); REPLACE INTO p VALUES (-FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT RAISE(IGNORE), *, p.* F
```

---

## Crash 71: `49058c377b922091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039609`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN NOT NULL); REPLACE INTO p VALUES (-CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO q VALUES (C
```

---

## Crash 72: `8889a270345e9ff4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039703`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN NOT NULL); REPLACE INTO p VALUES (-CURRENT_DATE >> CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 73: `c68b1bc0ac19a612` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040438`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (
```

---

## Crash 74: `f0f4ed7329accb2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040454`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURREN
```

---

## Crash 75: `82fc6eee3204f035` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040822`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); INSERT IN
```

---

## Crash 76: `0abb07abc2dce386` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041074`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE TRUE ESCAPE TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 77: `9273a97c7401aa61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041096`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (NULL LIKE NULL ESCAPE NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p
```

---

## Crash 78: `d498214080ed3c1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041303`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP | FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q D
```

---

## Crash 79: `8312d74a2239e61c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041503`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZ
```

---

## Crash 80: `6507a0fb7ee2badc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041687`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUE
```

---

## Crash 81: `1e71a790c0dc46dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041967`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP NOT NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a); INSERT 
```

---

## Crash 82: `0675be231714bdfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042621`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT FALSE); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAUL
```

---

## Crash 83: `b54512cbca1ef349` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL, b REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 84: `ab88372a3cbc463b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044535`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE >> CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 85: `e5cf9892d4201721` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046373`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (NOT CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 86: `dd4fb628048507d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046986`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (NOT CURRENT_TIME <> NULL IS NOT FALSE <> NULL); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 87: `937b5e17724ec05b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047029`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IS NOT FALSE <> NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 88: `b9a4dd98ef2a38d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047036`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (NOT CURRENT_TIME <> NULL IS NOT CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 89: `09a22140c6226c2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047635`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IS NOT NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 90: `73352c41c3271364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049423`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p SELECT CURRENT_DATE ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE OFFSET NULL OR CURRENT_TIMESTAMP; EXPLAIN QUERY PLAN SELECT DIST
```

---

## Crash 91: `483d5a21f7bc500d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050720`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 92: `d40eec9eaeac887a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052192`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (NULL NOTNULL); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*g', -214748364
```

---

## Crash 93: `a0c377bc92b8a4a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053102`

```sql
SELECT printf('%.*s', 2147483647); SELECT substr('82SX A-y x_-__-_', 9223372036854775807, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_DATE IS NULL AS a, q.* FROM (SEL
```

---

## Crash 94: `26c39699c92bfb4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053440`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE I
```

---

## Crash 95: `491ab1f6d9af4e20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053455`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 96: `8e818b8938bc52c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055354`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE, a BLOB NOT NULL); VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 97: `0c3596c82a9c39f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055524`

```sql
SELECT substr('_64-_7r7 -  _pyf2 ', -9223372036854775808, -9223372036854775808); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 98: `7650d534aca3a8ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056284`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); WITH RECURSIVE q AS MATERIALIZED (SELECT * FROM p ORDER BY CURRE
```

---

## Crash 99: `1503256f3e5c1283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056812`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); REPLACE INTO p VALUES (~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 100: `c671b1f6bc6fa298` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056950`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE >> ~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 101: `7aab9bfdc7a22ec2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057127`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE >> TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 102: `d20422f05c7edad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058561`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, b BLOB PRIMARY KEY, a FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; ANALYZE p; C
```

---

## Crash 103: `a10335362dd2ab53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058578`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, b BLOB PRIMARY KEY, a FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA integ
```

---

## Crash 104: `7cdac5b1b9099f29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059066`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 105: `0ea9e4739decf93c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061470`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT FALSE, * FROM p NOT INDEXED ORDER BY FALSE ASC NULLS LAST LIMIT CURRENT_TIME OFFSET
```

---

## Crash 106: `1f04687cfb98a337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061740`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT FALSE, * FROM p NOT INDEXED ORDER BY FALSE ASC NULLS LAST LIMIT CURRENT_TIMESTAMP; 
```

---

## Crash 107: `2dfaa50c405ff91c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063063`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT NULL AS a FROM p NOT INDEXED ORDER BY FALSE ASC NULLS LAST LIMIT CURRENT_DATE; CREA
```

---

## Crash 108: `404275b36998e5da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064202`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 109: `4c03b43e42b05f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064771`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL DEFAULT X'9CBcCc34BECCAe'); INSERT INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 21
```

---

## Crash 110: `104c47fcf55f1880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064922`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL DEFAULT X'9CBcCc34BECCAe'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 21
```

---

## Crash 111: `20933bcf0f8c04b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064968`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (FALSE IS NOT FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 112: `a4ad69ef82c82b9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065201`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 113: `c771380b10d246ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066812`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL, b REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT FALSE FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 114: `240cf43f418003aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068830`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT 596.5); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUE
```

---

## Crash 115: `ad7abfb2283e1a58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068973`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT X'aeEFFc0f'); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DE
```

---

## Crash 116: `b777aa773f109c17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069163`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (FALSE LIKE 8518541427798162.8E+369508 ESCAPE TRUE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 117: `170c8554531d3935` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069359`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (FALSE LIKE FALSE ESCAPE TRUE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 118: `e834efc4bcadfb3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069504`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (FALSE LIKE CURRENT_TIME ESCAPE TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, c1, b, 
```

---

## Crash 119: `95de04cc846f27f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069988`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (FALSE GLOB CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 120: `09dfab6907f3f262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070561`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (X'c9DFFb1A'); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c2, c2); INSERT OR ABORT I
```

---

## Crash 121: `1da27aef98433f76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071307`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 122: `279ff51cb2d3c254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071704`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (NULL LIKE NULL ESCAPE FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO 
```

---

## Crash 123: `b23d9d4aecf53fe5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071829`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE >> ~CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 124: `8989da373035a289` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079328`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (NULL BETWEEN FALSE AND CURRENT_TIMESTAMP)); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*f', 2147
```

---

## Crash 125: `788f58bcb79f14d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079523`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 126: `15cfcf69e8d982ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080753`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CASE WHEN FALSE THEN CURRENT_DATE ELSE CURRENT_DATE END); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 127: `c9677c2d984536d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081182`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP)) AS sub1; CREATE VIRT
```

---

## Crash 128: `0518753c5c3f685b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081383`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT FALSE == CURRENT_TIMESTAMP COLLATE BINARY FROM p WHERE TRUE || CURRENT_TIMESTAMP) AS sub1; CR
```

---

## Crash 129: `61af0d9e9c17d103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081678`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT *, CURRENT_DATE FROM p WHERE CURRENT_TIME IN (VALUES (count(*) FILTER (WHERE CURRENT_TIME) OV
```

---

## Crash 130: `5aef65285cbe0f09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081849`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP COLLATE BINARY AS a FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*f
```

---

## Crash 131: `6a427ac185882f15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082290`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CASE WHEN CURRENT_DATE IN (TRUE, CURRENT_TIME, CURRENT_TIME) COLLATE NOCASE THEN CURRENT_TIME END AS a FROM 
```

---

## Crash 132: `43e67df3aa3411ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082438`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CASE WHEN CURRENT_DATE IN (NULL) COLLATE NOCASE THEN CURRENT_TIME END AS a FROM (SELECT * FROM p WHERE NULL 
```

---

## Crash 133: `e2f5c270f31a663e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082445`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CASE WHEN CURRENT_DATE IN (TRUE, CURRENT_TIME, CURRENT_TIME) COLLATE NOCASE THEN CURRENT_TIME END AS a FROM 
```

---

## Crash 134: `566f358c5d5dd7f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082568`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CASE WHEN CURRENT_DATE IN (CURRENT_DATE, CURRENT_TIME, CURRENT_TIME) COLLATE NOCASE THEN CURRENT_TIME END AS
```

---

## Crash 135: `95e7c7470b3fff62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082758`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CASE WHEN CURRENT_DATE IN (CURRENT_DATE, FALSE) COLLATE NOCASE THEN CURRENT_TIME END AS a FROM (SELECT * FRO
```

---

## Crash 136: `ba055666777070b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084779`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE IS CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (CURRE
```

---

## Crash 137: `fba95f9b05811923` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085111`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER DEFAULT ' '); SELECT * FROM p JOIN p a ON NOT FALSE >= TRUE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 138: `6bcd1034f2f98cb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085783`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CAST(CURRENT_TIME AS VARCHAR(255)) NOT BETWEEN CURRENT_TIME AND TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 139: `adfb927eafc126b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086049`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON total_changes() NOT BETWEEN CURRENT_DATE AND TRUE NOT BETWEEN CURRENT_TIME AND TRUE <> CURRENT_TIMESTAMP & NULL NOTNULL;
```

---

## Crash 140: `2df51cc9f72b8d45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086309`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE IS NULL; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 141: `435a6c3efab83002` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086455`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE << CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CURR
```

---

## Crash 142: `b47d368eed88ee07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086628`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE IS NOT NULL << CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT V
```

---

## Crash 143: `2269e23430db86fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086951`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE & CAST(FALSE AS VARCHAR(255)); SELECT substr('T8D_E_D _-I-', 0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 144: `59d2b240fda3df8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087015`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT ~NULL | json_array(FALSE) + CURRENT_TIME - FALSE AS h_w FROM p JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 145: `6606a2bbd2800aa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087254`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT ~NULL | NULL + CURRENT_TIME - FALSE AS h_w FROM p JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q D
```

---

## Crash 146: `962dbe32b1f1d1e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088638`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT X'3EEEBDA1cB2dC4' AS cw2yb__0jb FROM p JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALU
```

---

## Crash 147: `68118c3c03ab9c5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089212`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_TIME IN (VALUES (min(NULL) FILTER (WHERE CURRENT_TIME) OVER ())) NOT BETWEEN CURRENT_TIME AND TRUE; CREATE VIRTU
```

---

## Crash 148: `671d02226714a34e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089434`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_TIME IN (VALUES (FALSE)) NOT BETWEEN CURRENT_TIME AND TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 149: `51cd7ad98e580598` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089604`

```sql
SELECT printf('%.*g', 0); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 150: `8e34201d4fdc1914` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089681`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NULL = CURRENT_TIME; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 151: `26c95d96a72d55df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089934`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NOT NULL = CURRENT_TIME; SELECT round(1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT INTO 
```

---

## Crash 152: `4ea4e238eae05de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090798`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE MATCH FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); P
```

---

## Crash 153: `2bb5a07bf2f45ad2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090958`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NULL OR CURRENT_TIMESTAMP; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 154: `9ad960a65ffd3c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093907`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT ALL * FROM p NOT INDEXED LIMIT CURRENT_TIMESTAMP > CURRENT_DATE IN (SELECT t2.* F
```

---

## Crash 155: `d14b759051fe4be5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093963`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT * LIMIT CURRENT_TIMESTAMP > CURRENT_DATE IN (SELECT t2.* FROM (SELECT ALL * FROM 
```

---

## Crash 156: `c3b9174ba06d6cdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093979`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT * LIMIT FALSE IN (SELECT * FROM (SELECT * UNION SELECT * FROM p WHERE CURRENT_TIM
```

---

## Crash 157: `cdf8dad43da20665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093996`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT * UNION SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY
```

---

## Crash 158: `1310acf4b3e3b8e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094032`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 159: `5dc5032beef3c32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098697`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT * UNION SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDE
```

---

## Crash 160: `362bcb65850ee17c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108290`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (SELECT DISTINCT * FROM p NO
```

---

## Crash 161: `e5faefaecba4fea6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108493`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE 
```

---

## Crash 162: `73285c3b565e7776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108748`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VI
```

---

## Crash 163: `f19ed6af0a83f4ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109901`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY, a FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRT
```

---

## Crash 164: `c89f41d72a99bc76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110184`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF
```

---

## Crash 165: `0edddde778033eda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110365`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUA
```

---

## Crash 166: `6d622d652ba7e12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110739`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY, b INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED; SELECT printf('%.*f', 2147483647,
```

---

## Crash 167: `1f3adf57a03c76d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113886`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 168: `d6d316c0f502a6bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114653`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT X'', a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; SELECT * UNION SELECT * FROM p WHERE TRUE GROUP
```

---

## Crash 169: `a16b764f2355bdd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117598`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -91829); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 170: `5ff5dd39931f209f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117778`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CAST(FALSE AS REAL)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF N
```

---

## Crash 171: `305a16efe1260517` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118525`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES ((SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST)); EXPLAIN QUE
```

---

## Crash 172: `4b855814522d681e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119566`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (), NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 173: `3aa39efb7f0cf58b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119744`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_DATE G
```

---

## Crash 174: `465c2b2f0f2609c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121462`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (SELECT * FROM p NOT INDEXED ORDER BY TRUE ASC)); VALUES (CURRENT_TIMESTAMP)
```

---

## Crash 175: `03baef858ec618b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121883`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p sd_6_b_3z___3l4___4___5__e3_ ON CURRENT_TIME / TRUE; CREATE VIRTUAL TABL
```

---

## Crash 176: `939c404341eea286` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122380`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM q NOT INDEXED)); V
```

---

## Crash 177: `bf23616b2fa2d772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122629`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) VALUES (TRUE))); VALUES (CURRENT_TIM
```

---

## Crash 178: `2b8eb39995db2976` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123339`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT *, * FROM q LIMIT TRUE); CREATE VIRTUAL 
```

---

## Crash 179: `33c43ecd7adb87e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT * FROM q LIMIT FALSE OFFSET NULL * NULL 
```

---

## Crash 180: `f047029a477b299f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123873`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM q WHERE EXISTS (SELECT * FROM q LIMIT FALSE OFFSET TRUE); SELEC
```

---

## Crash 181: `abbdf751706499af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124729`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b FLOAT CHECK (FALSE MATCH
```

---

## Crash 182: `1095d76da2e7d028` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127741`

```sql
SELECT printf('%.*e', 9223372036854775807, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT t1.*, CURRENT_TIME AS v3z_73cr___8_2_gmk_hb6 FROM p WHERE EXISTS (SELECT p.* FROM p 
```

---

## Crash 183: `f5e8bb3e0a1c0f2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130236`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB CHECK (total_changes() NOT BETWEEN CURRENT_DATE AND TRUE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 184: `864726c3b712a056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133116`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE)) UNION ALL SELECT NULL ORDER BY NU
```

---

## Crash 185: `1c8999f832697323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133686`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (WITH p AS (WITH p AS (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * F
```

---

## Crash 186: `18e1e84766fd80cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134051`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIME COLLATE NOCASE IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * F
```

---

## Crash 187: `deabb77f2edf80ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134094`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIME COLLATE NOCASE IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) VALUES (CURREN
```

---

## Crash 188: `5deee252d9190a10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135484`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO q VALUES (FALSE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 189: `937c82105904f39d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136235`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_DATE G
```

---

## Crash 190: `62145727ce1edfb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136447`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (), count(*) OVER (), NULL); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 191: `eb3932c6e3466357` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136860`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY TRUE DESC NULLS LAS
```

---

## Crash 192: `71f2e19082451fc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137413`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (group_concat(FALSE, '6 8_') OVER (), NULL); CREATE VIRTUAL TABLE IF N
```

---

## Crash 193: `3f0c7f8e061335b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139467`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES ((SELECT * FROM (VALUES (CURRENT_TIME)) AS l_9a_5_6__26b_____4cy__f___nx98xh_6v_12i_3_
```

---

## Crash 194: `61fe6f2ab0522cae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139619`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (VALUES (8518541427798162.8E+369508))); EXPLAIN QUERY PLAN VALUES (CURRENT_D
```

---

## Crash 195: `90978760da1438ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE PRIMARY KEY); INSERT INTO q VALUES (FALSE IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM p NATURAL JOIN p N
```

---

## Crash 196: `fc13073723edae65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145103`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER UNIQUE, b BLOB PRIMARY KEY, a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 197: `6073233c32fef783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146862`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY, b INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL JOIN p NATURAL LEFT JOIN p NOT INDEXED
```

---

## Crash 198: `aa6b906a849000c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147452`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT avg(CURRENT_DATE) AS a FROM p WHERE CURRENT_DATE) AS
```

---

## Crash 199: `433920eaee34571a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147568`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT changes() AS a FROM p WHERE CURRENT_DATE) AS sub1; C
```

---

## Crash 200: `8ad2c03cd75be819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161478`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER DEFAULT X'e1edBBEbdA', c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT
```

---

## Crash 201: `e680847290ede062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163069`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 202: `b6dfbc03f7d791e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163076`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p NATURAL JOIN p NATURAL JOIN (SELECT * FROM p NOT IN
```

---

## Crash 203: `3545bce11ca177b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163082`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME HAVIN
```

---

## Crash 204: `bf0c525eb09973b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163098`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (min(CURRENT_TIME <= CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) OVER () > CUR
```

---

## Crash 205: `cdcc7c2615527974` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163106`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 206: `ee2634477ca398b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163114`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p NOT INDEXED CROSS JOIN q NOT INDEXED LEFT OUTER JOI
```

---

## Crash 207: `bbfce44245f0810a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163130`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE NOT IN (CURRENT_TIMESTAMP)) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP 
```

---

## Crash 208: `6709d3579c5e4fba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163139`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (CURRENT_DATE), _rowid_ BLOB CHECK (CURRENT_TIMESTAMP)); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p
```

---

## Crash 209: `1d5cf8f27311ce84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163145`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 210: `2c60c0988f684e31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163151`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 211: `700cee80a45076af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163160`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY NOT EXISTS (VALUES
```

---

## Crash 212: `cea4feb3cd809b9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163166`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (CURRENT_TIME IN (VALUES (count(*) OVER (ORDER BY NULL, CURRENT_TIMESTAMP), NULL)
```

---

## Crash 213: `7a55554bb15c5ad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163189`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME COLLATE NOCASE DE
```

---

## Crash 214: `7c64480e9ba329d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163196`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (TRUE IN (SELECT p.*)) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CUR
```

---

## Crash 215: `bd9bb50c3d5f6bce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163202`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p NOT INDEXED JOIN p AS oy0o22_35_2f_7t1_3xb19 USING 
```

---

## Crash 216: `d7fbfd674c08103c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163215`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM (VALUES (TRUE)) AS zk_4_1910wmf_q WHERE CURRENT_TIMES
```

---

## Crash 217: `99a5238b04b7cd3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163222`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 218: `41b1f4f650f3d236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163228`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM r NOT INDEXED JOIN p NOT INDEXED NATURAL JOIN (t1 NOT
```

---

## Crash 219: `5c67186d1d7a74df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163234`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY EXISTS (SELECT * UNION SELECT AL
```

---

## Crash 220: `982631070c12f710` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163242`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLA
```

---

## Crash 221: `1fc62078ca1b41a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163250`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT p.* FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WIN
```

---

## Crash 222: `f474157aca39a367` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163256`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p SELECT RAISE(IGNORE) IS NULL & CASE CURRENT_DATE WHEN RAISE(IGNORE) THEN CASE RAISE(IGNO
```

---

## Crash 223: `734f04291891b56c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163263`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM t3 INDEXED BY c2 WHERE CURRENT_TIMESTAMP GROUP BY CUR
```

---

## Crash 224: `04439d56a9c630ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163297`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM (p INDEXED BY c2 CROSS JOIN p NOT INDEXED USING (rowi
```

---

## Crash 225: `734a005ff95d1ec0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163348`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT NOT NULL); INSERT INTO p VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDO
```

---

## Crash 226: `687277366b49f62b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167090`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON FALSE OR CURRENT_TIMESTAMP; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 227: `8e05eb6c788fa0b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167629`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NULL OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c2); EXPLAIN QUERY PLAN WITH p AS NOT MATERIA
```

---

## Crash 228: `deb6ac726b51fabc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168492`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON (SELECT * FROM p NOT INDEXED ORDER BY -TRUE ASC NULLS LAST, CURRENT_DATE DESC NULLS LAST) & (SELECT * FROM (SELECT * FRO
```

---

## Crash 229: `4c4b4bd0a2791e17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170280`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT ~min(CURRENT_TIME) AS h_w FROM p JOIN p a ON NULL; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 230: `a5d602111ea57349` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170493`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT json_array(CURRENT_TIMESTAMP, NULL) AS h_w FROM p JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); WITH RECURSIV
```

---

## Crash 231: `f08234607fe1255c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172170`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT group_concat(FALSE, '-_e--_-4q_97 _R_7-') AS h_w FROM p JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT
```

---

## Crash 232: `64c07ee70fc712d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173305`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CAST(TRUE AS FLOAT) NOT BETWEEN CURRENT_DATE AND TRUE NOT BETWEEN CURRENT_TIME AND FALSE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 233: `9f739b8ca016ea32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173832`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON CAST(CURRENT_TIME AS NUMERIC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CURRENT_
```

---

## Crash 234: `f49eae02dac0bb66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174001`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE NOT BETWEEN CURRENT_TIME AND CAST(CURRENT_TIME AS VARCHAR(255)) NOT BETWEEN CURRENT_TIME AND FALSE; CREATE VIRTUAL 
```

---

## Crash 235: `b86e36445e559704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174146`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON TRUE NOT BETWEEN CURRENT_TIME AND FALSE NOT BETWEEN CURRENT_TIME AND FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 236: `1c82e4694a66569a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175449`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); SELECT * FROM p JOIN p a ON NOT CURRENT_DATE IS CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 237: `33e9114f40c71aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176161`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q NOT INDEXED JOIN t3 ON CURRENT_TIMESTAMP; INSERT INTO p SELECT * UNION SELECT * FROM p WHERE TRUE GROUP BY
```

---

## Crash 238: `d79fb442ecacca9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CURRENT_TIMESTAMP IS NOT FALSE COLLATE NOCASE AS a FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL
```

---

## Crash 239: `253306b9e8e31a45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178926`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT count(NULL) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY FALSE) AS a FROM (SELECT * FROM p WHERE TRUE
```

---

## Crash 240: `4cea7d210a3856ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179826`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT avg(CURRENT_DATE) AS a FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 241: `d18ec0a4e113b725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181449`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP HAVING TRUE)) AS sub1;
```

---

## Crash 242: `d36f1a7caab28152` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192807`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); INSERT INTO p DEFAULT VAL
```

---

## Crash 243: `8a8d06a60fd61ac9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192975`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); INSERT INTO p DEFAULT VAL
```

---

## Crash 244: `3c5ec7cfe52cefc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193106`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME >> ~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR AB
```

---

## Crash 245: `61f8d93359d39d7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195114`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 246: `73a6bee7e043d2ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195521`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_DATE),
```

---

## Crash 247: `4264774ff80daf7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195547`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE
```

---

## Crash 248: `e4e39a221aa1670c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195584`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT CURRE
```

---

## Crash 249: `dbf972d40f45107a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196657`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); REPLACE INTO p VALUES (-65.515004966432387343363558148E-6); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); WI
```

---

## Crash 250: `a4d548c9098c2fef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199048`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT '-'); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 251: `215bb0baee65aeb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199855`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT OR REPLACE INTO p VALUES (NOT EXISTS (VALUES (NULL) UNION ALL SELECT NULL ORDER BY NULL ASC NULLS LAST)); EX
```

---

## Crash 252: `1d4a47f0a85e7785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201599`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL, b REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT min(FALSE) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE RANGE 
```

---

## Crash 253: `0a4ae65b29cc47a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202231`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS BOOLEAN)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 254: `471002f102b4349c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202544`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME COLLATE NOCASE IN (CURRENT_TIME)) AS sub1; CREATE VIRTUAL TABLE IF
```

---

## Crash 255: `481ac88a150da04a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204210`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (X'3EEEBDA1cB2dC4' IS NOT FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 256: `2f7903df4755e8ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (rowid)); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 257: `b1c372566cd656af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205257`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM 
```

---

## Crash 258: `76e1089017a421ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207308`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p SELECT ALL * FROM p NATURAL LEFT JOIN p NATURAL JOIN p NOT INDEXED; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 259: `ef550ea32bea59cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212872`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); SELECT * FROM p JOIN p a ON (SELECT * FROM p NOT INDEXED ORDE
```

---

## Crash 260: `38a8bf0d74efd648` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216242`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO q (_rowid_) VALUES (NULL) ON CONFLICT(rowid) DO UPDATE SET rowid = NULL; PRAGMA integrit
```

---

## Crash 261: `bb57a2a0696305e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216927`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO q (_rowid_) VALUES (NULL) ON CONFLICT(rowid) DO UPDATE SET c1 = NULL; PRAGMA integrity_c
```

---

## Crash 262: `6c7ebf648d1ba927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217406`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMAR
```

---

## Crash 263: `de2a9823f687827d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217499`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAUL
```

---

## Crash 264: `fade68efa42c63d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO p (_rowid_) VALUES (NULL) ON CONFLICT(rowid) DO UPDATE SET rowid = NULL; PRAGMA integrit
```

---

## Crash 265: `353ad43f55a7badc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224377`

```sql
SELECT substr('O_ 2-d_X _', -1, -2147483648); SELECT printf('%d', -9223372036854775808, ''); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT IN
```

---

## Crash 266: `2d11d72b90c4738c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226499`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); SELECT *, min(CURRENT_TIME) AS h_w FROM p JOIN p a ON TRUE; C
```

---

## Crash 267: `9d35cf3e675665cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226657`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; SELECT *, random() AS h_w FROM p JOIN p a ON TRUE; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 268: `307e195d48a7c3b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227851`

```sql
SELECT round(-1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (count(*) COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 269: `9919635845ea989d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231921`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (FALSE) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE RTRIM DES
```

---

## Crash 270: `e62a009337038118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232297`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IS NOT TRUE <> NULL); PRAGMA integrity_check; SELECT printf('%.*g', -2147
```

---

## Crash 271: `f100bf8832b97012` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232587`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN DEFAULT CURRENT_TIME, _rowid_ INT); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 272: `8e8b1aa18e99c2eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232625`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL q._rowi
```

---

## Crash 273: `3cb9d63d336745dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235436`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS VARCHAR(255))) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 274: `f5529b37cd9cc9e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241073`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT); SELECT ~min(CURRENT_T
```

---

## Crash 275: `c56768ee546b8c91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241125`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT
```

---

## Crash 276: `49ca92937a7841c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241203`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%x', 1, 'v  SQ-_E75--2E__'); CREATE VIRTUAL
```

---

## Crash 277: `a8e2f64234b06c17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241826`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); WITH RECURSIVE q (a) AS (VALUES (FALSE) UNION SELECT * FROM p) SELECT * FROM q; CREATE VIRTUAL TA
```

---

## Crash 278: `24cb8086d4e4ccd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000241335`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, _rowid_ FLOAT CHECK ((SELECT t2.* FROM t1 UNION SELECT RAISE(IGNORE) FROM r NOT INDEXED JOIN r NOT INDEXED WHERE NULL COLLATE NOCASE GROUP BY TRUE 
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  sqlite3ExprDeleteNN
  sqlite3ExprDeleteNN
```

---
