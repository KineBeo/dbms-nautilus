# Crash Triage Report

**Total crashes:** 53  
**Unique crash sites:** 53  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 53 | 53 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `31cb55acd16c04f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000118`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); REPLACE INTO t1 VALUES (~RAISE(IGNORE) IS FALSE IS NOT NULL -> CURRENT_DATE & NULL COLLATE RTRIM GLOB FALSE NOT NULL / NULL COLLATE BINARY IS N
```

---

## Crash 2: `7817a2724d8124f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000187`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a) VALUES (CURRENT_TIME IS NOT total_changes() NOT LIKE NOT EXISTS (VALUES (CURRENT_TIMESTAMP IS NULL)) > RAISE(IGNORE) LIKE RAI
```

---

## Crash 3: `1a4ff6f8788d4ffd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001380`

```sql
SELECT printf('%.*g', 2147483647); SELECT printf('%.*g', -2147483649, -1.0); CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); INSERT INTO r VALUES (CURRENT_DATE COLLATE RTRIM, RAISE(IGNORE), TR
```

---

## Crash 4: `44d17ee181fa0930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001561`

```sql
SELECT substr('__  _8v', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_, _rowid_); INSERT INTO t1 VALUES (RAISE(IGNORE) NOTNULL != CURRENT_TIMESTAMP ISNULL |
```

---

## Crash 5: `a2371042302b44ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000005843`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (CASE NULL = CURRENT_DATE COLLATE BINARY * NULL IS NOT DISTINCT FROM TRUE BETWEEN +RAISE(IGNORE) ISNULL AND FALSE - RAISE(IGNORE) IS NOT NULL <
```

---

## Crash 6: `eef05167d5ea8544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000005955`

```sql
SELECT printf('%.*g', -9223372036854775808);
```

---

## Crash 7: `ef571306b351636e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000009355`

```sql
SELECT printf('%.*d', -2147483648, 0.0);
```

---

## Crash 8: `fd53d4f3193ba4e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000010361`

```sql
SELECT substr('-aF4', -1);
```

---

## Crash 9: `24f6a5ad919c7056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000010374`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (CURRENT_TIME)), r AS NOT MATERIALIZED (SELECT * LIMIT CURRENT_TIME, CURRENT_DATE) INSERT INTO t3 VALUES (-CURRENT_
```

---

## Crash 10: `b170df68e10ac927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010727`

```sql
SELECT substr('_65_51 vZd5 ', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t2 (rowid) AS (SELECT CURRENT_TIME ORDER BY +FALSE LIMIT (VALUES (FALSE COLLAT
```

---

## Crash 11: `8c09c0d1d0dd0fdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000012305`

```sql
SELECT round(-0.0, -2147483649);
```

---

## Crash 12: `3a32ab14ed62f6fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000021619`

```sql
SELECT substr('', -2147483648); SELECT round(-0.0, 0);
```

---

## Crash 13: `d9d0370238c0cbb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036109`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); INSERT INTO p (rowid) VALUES (RAISE(IGNORE) - CURRENT_DATE > RAISE(IGNORE)); SELECT *;
```

---

## Crash 14: `70c8a4d487393d30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000036838`

```sql
SELECT round(1e-308, 4294967295); CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) ORDER BY (CURRENT_TIMESTAMP) DESC LIMIT NULL; SELECT RAISE(IG
```

---

## Crash 15: `21612b66ec37335d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000037533`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT (TRUE IS NOT NULL NOT BETWEEN NOT NULL NOT NULL COLLATE RTRIM AND CURRENT_DATE >> CURRENT_DATE <> CURRENT_DATE) || CUR
```

---

## Crash 16: `73f1f07cbf96a2d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000044233`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) DEFAULT CURRENT_TIMESTAMP, c3 FLOAT NOT NULL DEFAULT 3, b REAL GENERATED ALWAYS AS (C
```

---

## Crash 17: `7cc4bd6f5b449209` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000044431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NOT EXISTS (WITH t2 AS MATERIALIZED (SELECT *, * ORDER BY ~NULL DESC NULLS LAST), q AS (VALUES (CURRENT_TIMESTAMP COLLATE NOCASE, CURRENT_TIMESTAMP)) SELECT
```

---

## Crash 18: `743f717423cda352` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052058`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (last_insert_rowid() NOT NULL ->> -FALSE > CURRENT_TIMESTAMP NOT LIKE FALSE <> CURRENT_DATE COLLATE RTRIM) VIRTUAL); CREATE VIEW IF NOT EXISTS v
```

---

## Crash 19: `26599a2b091878bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052862`

```sql
SELECT round(1.0, -1); SELECT hex(zeroblob(-1));
```

---

## Crash 20: `bf05d39aecbc82af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000052901`

```sql
SELECT round(1e308, 4294967295); SELECT hex(zeroblob(-1));
```

---

## Crash 21: `1754d107314f8490` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000053536`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB GENERATED ALWAYS AS (CASE WHEN CAST(CURRENT_TIMESTAMP AS FLOAT) REGEXP TRUE COLLATE BINARY THEN CURRENT_DATE != CURRENT_TIME AND NOT CURRENT_TIME ELSE NOT CURRENT_T
```

---

## Crash 22: `2928eb55ccd54299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000054657`

```sql
SELECT round(-1.0, 2147483648); CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT 0.0); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); INSERT INTO t3 SELECT * ORDER BY TRUE LIMIT TRUE, 
```

---

## Crash 23: `72b7ceda3d1ef557` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000058946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (first_value(NULL COLLATE NOCASE << NOT RAISE(IGNORE) LIKE dense_rank() FILTER (WHERE CURRENT_TIMESTAMP) <= NULL REGEXP CURRENT_DATE) OVER (ORDER BY -80.84848
```

---

## Crash 24: `98a801ac6d2531a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000060754`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT *, s.*, p.*, CURRENT_TIMESTAMP LIKE ~char(CURRENT_TIME NOTNULL) OVER () ISNULL AS a FROM t2 NATURAL JOIN s WHERE EXISTS (SELECT ~TRUE NOT
```

---

## Crash 25: `bd758000b20e4cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000068528`

```sql
SELECT printf('%.*e', 2147483648, 0.01); CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL DEFAULT FALSE); INSERT OR ROLLBACK INTO r VALUES (CURRENT_DATE
```

---

## Crash 26: `cf7a48c16d96c30a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000070069`

```sql
SELECT substr('__  _8v', 2147483648, 2147483648); SELECT printf('%.*e', 9223372036854775807, 0.0);
```

---

## Crash 27: `08e7908a94211bcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000071880`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE GENERATED ALWAYS AS (json_quote(+CURRENT_TIMESTAMP ->> CURRENT_DATE / NULL COLLATE NOCASE NOT NULL IN (VALUES (TRUE COLLATE BINARY) ORDER BY CURRENT_TIME ASC NULLS 
```

---

## Crash 28: `c7ed49d365b96bb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000072194`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT s.*, CURRENT_DATE GLOB CURRENT_TIME GLOB NULL FROM jsonb_t
```

---

## Crash 29: `91b0878a338c5ded` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000072920`

```sql
SELECT substr('1A-h _ _c', -9223372036854775808, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO t3 VALUES (rank() FILTER (WHERE lag(NOT FALSE IS NOT TRUE) FILTER (WHERE CURR
```

---

## Crash 30: `8f43c3363f3c8bb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000077345`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC GENERATED ALWAYS AS (CURRENT_DATE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (-length(CASE CURRENT_DATE & RAISE(IGNORE) ->> -
```

---

## Crash 31: `f1af9e9fd70d2520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000082849`

```sql
SELECT round(-0.0, -2147483649); SELECT hex(zeroblob(-1));
```

---

## Crash 32: `3f6736d6b15bd62a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000083037`

```sql
SELECT printf('%.*e', 2147483648, 0.01); SELECT printf('%s', 0, '');
```

---

## Crash 33: `2bd1b5cf7e9d6d54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000083482`

```sql
SELECT substr('c  _-7_31P _', 4294967296); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 34: `b0c17295190d8463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000084370`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); INSERT OR IGNORE INTO s VALUES (CURRENT_DATE AND NULL <= CURRENT_TIMESTAMP, CURRENT_TIME COLLATE NOCASE LIKE FALSE ESCAPE CASE WHEN NULL THEN C
```

---

## Crash 35: `56ad88356c363e4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085653`

```sql
SELECT round(-1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO s VALUES (TRUE LIKE RAISE(IGNORE) & NULL GLOB NOT CURRENT_TIME IS NOT NULL, NOT EXISTS (V
```

---

## Crash 36: `f6bf9922aa7efda3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000086510`

```sql
SELECT hex(zeroblob(9223372036854775807)); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 37: `f8d55d11b86816bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000094052`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT *; INSERT INTO r VALUES (+typeof(NULL) FILTER (WHERE FALSE) OVER (PARTITION BY CURRENT_DATE) IS DISTINCT F
```

---

## Crash 38: `d25174958454273a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000098524`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE, c1 INTEGER CHECK (((CURRENT_TIMESTAMP)))); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO t2 (rowid) VALUES (CURRENT_TIME NOT BETWEEN FALSE A
```

---

## Crash 39: `c68c3e2381e2892e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110641`

```sql
SELECT printf('%f', 2147483647, ' -t C _ _8_GOk_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT format(' c_r  ', +CASE ~NULL WHEN FALSE THEN +TRUE != CURRENT_TIME ISNULL COLLATE N
```

---

## Crash 40: `9ed0175e7639c416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000110879`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT NULL, c3 BOOLEAN); SELECT q.*, p.*, TRUE, RAISE(IGNORE) AS h4_z_3__38m9fb51_p1t_p0_v8_uz_ki_082, t3.* FROM json_each(CURRENT_TIMESTAMP COL
```

---

## Crash 41: `b814edd0608a2cd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000129470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, b REAL CHECK (TRUE LIKE RAISE(IGNORE) OR FALSE IS NULL), c2 VARCHAR(255) UNIQUE, c1 INTEGER GENERATED ALWAYS AS (~CAST(+-NOT EXISTS (VALUES (TRUE) 
```

---

## Crash 42: `7e153b7a0c921449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000138855`

```sql
SELECT printf('%.*e', 0, -1.0);
```

---

## Crash 43: `3b30b02b282f8faf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000145640`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%.*d', -9223372036854775808, -0.0); SELECT printf('%.*d', 2147483647, -1e308);
```

---

## Crash 44: `f0d23b326356f562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000151519`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT, c3 REAL GENERATED ALWAYS AS (FALSE NOTNULL >> TRUE) STORED); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); C
```

---

## Crash 45: `de630a2f455cbe0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160157`

```sql
SELECT printf('%.*g', 2147483648, 0.01); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 46: `f1204ecc6ecf02a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000160690`

```sql
SELECT printf('%.*s', -2147483649, -1.0);
```

---

## Crash 47: `f79d33103be8c6ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000163026`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE t1 AS (SELECT *) INSERT INTO s VALUES (0.0, R
```

---

## Crash 48: `c79af9ea416ced27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000163627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR IGNORE INTO t3 VALUES (EXISTS (VALUES (RAISE(IGNORE))) <= CURRENT_TIME + CURRENT_DATE IS DISTI
```

---

## Crash 49: `66f8b7cd11367131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000184522`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL, c3 INT DEFAULT FALSE, c2 INT GENERATED 
```

---

## Crash 50: `4665947b1d457c85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226734`

```sql
SELECT round(-1e308, 1); SELECT printf('%llu', -1, 'A_5 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, a, b, a, c2, c3); INSERT INTO q VALUES (CASE CURRENT_DATE MATCH NULL LIKE 
```

---

## Crash 51: `63d4a124e0ec065b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000231922`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT substr('--y--_- v', 4294967295, 1);
```

---

## Crash 52: `9fe35964870a253b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000288844`

```sql
SELECT printf('%.*d', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t2 AS NOT MATERIALIZED (SELECT t2.*) SELECT CURRENT_DATE IS DISTINCT FROM FALSE MATCH CURRENT_TIMESTA
```

---

## Crash 53: `b75695a8ed4af6b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000295291`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT X'b3cB4A', a BLOB GENERATED ALWAYS AS (printf('o 5N3 r9y--0e', last_value(~NULL) OVER (PARTITION BY TRUE ORDER BY percent_rank() FILTER (WHERE NOT EXISTS (V
```

---
