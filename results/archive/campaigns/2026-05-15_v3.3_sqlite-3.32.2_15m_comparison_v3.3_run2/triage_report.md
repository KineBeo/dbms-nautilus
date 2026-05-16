# Crash Triage Report

**Total crashes:** 36  
**Unique crash sites:** 36  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 36 | 36 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9a33d0b1147b8ea1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000201`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT INTO q VALUES (-7.9007856122e-078411651477452210470699860256149924490578 + NULL OR RAISE(IGNORE) IS CURRENT_TIME % CURRENT_TIME IS N
```

---

## Crash 2: `77e2270387d7d61f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000730`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2, c1, c3); INSERT INTO q VALUES ((+FALSE >= c1 -> NOT EXISTS (WITH RECURSIVE p (c1) AS (SELECT *, * ORDER BY FALSE COLLATE BINARY <= FALS
```

---

## Crash 3: `d89a469474349cf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005070`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * FROM jsonb_tree('[{"a":1},{"b":2}]') GROUP BY NULL != RAISE(IGNORE) HAVING CURRENT_TIMESTAMP UNION 
```

---

## Crash 4: `50f9f13614d49337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009080`

```sql
SELECT round(0.01, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.* FROM (SELECT t1.*, FALSE FROM q WHERE +typeof(NULL = +CURRENT_TIME < +CURRENT_DATE ISNULL NOT IN (RAISE(IGNO
```

---

## Crash 5: `e6595ab4e3b5b0a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009657`

```sql
SELECT printf('%s', 2147483647, 'F-2__-_U-_O 9U'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_DATE NOTNULL >= json_valid(NULL) OVER (ORDER BY CURRENT_TIME + RAISE(IGNORE)
```

---

## Crash 6: `a2361237442e70d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010035`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, b); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(1));
```

---

## Crash 7: `3fb4bacd1382e299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010049`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob
```

---

## Crash 8: `556265abac979934` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010060`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT
```

---

## Crash 9: `a2885b8268453b4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026427`

```sql
SELECT round(1.0, -2147483649); SELECT printf('%.*f', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO t2 VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check
```

---

## Crash 10: `9a89c7df67eb948c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026598`

```sql
SELECT round(1.0, -2147483649); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO t2 VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; SELECT hex(zer
```

---

## Crash 11: `ba2cfdbffcba1b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026704`

```sql
SELECT round(-1.0, 1); SELECT printf('%.*g', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT INTO q VALUES (FALSE -> ~-FALSE IS CASE WHEN CASE FALSE WHEN CURRENT_TIME
```

---

## Crash 12: `1bdb2cd39e4ff829` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026882`

```sql
SELECT printf('%f', 2147483648, ''); SELECT substr('', -1, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT s.*, FALSE -> NULL <> TRUE, t3.* FROM jsonb_tree('{"a":{"b
```

---

## Crash 13: `f33a2383edec818c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028261`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (TRUE IS NOT NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 14: `647074db5131a313` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028412`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 15: `2471139d404afab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028419`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 16: `55a23019afefde26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035284`

```sql
SELECT printf('%.*f', 1, -0.0); SELECT printf('%.*g', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (NULL IS NOT NULL > CURRENT_DATE -> CURRENT_TIMESTAMP IS NOT N
```

---

## Crash 17: `d2f5fde1e455169a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036082`

```sql
SELECT printf('%.*g', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r (_rowid_) VALUES (CASE FALSE AND NULL WHEN (VALUES (FALSE)) THEN NULL == RAISE(IGNORE) END * NULL IS 
```

---

## Crash 18: `edb48be5a11b919b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038745`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT NULL AND TRUE - CURRENT_TIMESTAMP FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c
```

---

## Crash 19: `c22e485e34412fc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038797`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT * FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c2, c3, c3); SELECT CURRENT_TIMES
```

---

## Crash 20: `a7d0b39efa12297c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038805`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT NULL AND CURRENT_TIMESTAMP FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c2, c3, 
```

---

## Crash 21: `4d086c2aded091ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040005`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT CURRENT_TIMESTAMP AND CURRENT_TIME FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3,
```

---

## Crash 22: `4654530ca1042ee2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040060`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c1, a); INSERT INTO q VALUES (CURRENT_DATE OR CURRENT_TIME) EXCEPT SE
```

---

## Crash 23: `370e1a269a1ddfa0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045732`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); SELECT * FROM q WHERE EXISTS (VALUES (FALSE) UNION SELECT CURRENT_TIME FROM q WHERE CURRENT_TIME)
```

---

## Crash 24: `f9a5477fe213acbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048571`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c2 GENERATED ALWAYS AS (c1) UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a INT, b AS
```

---

## Crash 25: `5450b108f326e23a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058451`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE r AS NOT MATERIALIZED (SELECT DISTINCT CURRENT_TIME <> -CURRENT_DATE AS l_9___o__7_sw9
```

---

## Crash 26: `10dd963c89391a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058551`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); INSERT OR ROLLBACK INTO p VALUES (FALSE, CAST(NOT NULL != FALSE REGEXP CURRENT_DATE IN (SELECT 
```

---

## Crash 27: `beb48b3aaf940ace` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058735`

```sql
SELECT substr('_-  -p -_3 1', 2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 VALUES (group_concat(TRUE * TRUE IS NOT DISTINCT FROM CASE WHEN CURRENT_TIMESTAM
```

---

## Crash 28: `4921dd5cea65efc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058944`

```sql
SELECT printf('%.*d', 2147483648); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT NOT NOT +CURRENT_DATE - CURRENT_TIME COLLATE RTRIM >= CUR
```

---

## Crash 29: `ca34a0b4973e1616` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059020`

```sql
SELECT printf('%.*e', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT NULL COLLATE BINARY & CURRENT_DATE NOTNULL FROM p JOIN p z__5698____xs ON ~CASE WHEN json_rem
```

---

## Crash 30: `0e765a88a9b6f858` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059056`

```sql
SELECT substr('-f-w-4- vJ', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT NULL OR RAISE(IGNORE) IS NOT DISTINCT FROM CURRENT_DATE IS NOT DISTINCT FROM CURRENT_TIMESTAMP COLLATE
```

---

## Crash 31: `20d6af97a6837f52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062681`

```sql
SELECT printf('%.*d', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p SELECT p.* FROM (jsonb_tree('{}')) INTERSECT SELECT NULL LIKE TRUE ESCAPE CU
```

---

## Crash 32: `d68dafe6d237ca3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074115`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c2 GENERATED ALWAYS AS (c1) UNIQUE); INSERT INTO p VALUES (-CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 33: `69c5397f657283f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080111`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 34: `97684a7e5e4e9d99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084742`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE FALSE) OVER () FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a);
```

---

## Crash 35: `871718cfeecb122c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108527`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE, c2 BLOB UNIQUE, _rowid_ VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREA
```

---

## Crash 36: `dee1d698ff0a8b0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115857`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TAB
```

---
