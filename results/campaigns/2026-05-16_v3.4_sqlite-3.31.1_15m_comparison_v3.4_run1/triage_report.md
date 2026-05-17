# Crash Triage Report

**Total crashes:** 47  
**Unique crash sites:** 47  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 27 | 27 | 57% |
| Signal | 20 | 20 | 42% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `af844976c3a1dab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000392`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN UNIQUE, c3 TEXT GENERATED ALWAYS AS ((~~CURRENT_TIMESTAMP IS NOT NULL >= -FALSE IS NOT DISTINCT FROM CURRENT_DATE <> CURRENT_DATE)) VIRTUAL, a INTEGER GENE
```

---

## Crash 2: `49e8cb667a0896bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000615`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT * FROM p JOIN q a ON lag(RAISE(IGNORE) OR CURRENT_TIMESTAMP, NULL IS RAISE(IGNORE) COLLATE RTRIM NOT LIKE (SELECT t3.*), -random() == NU
```

---

## Crash 3: `225b891d0aa1d513` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001054`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY, c2 INT GENERATED ALWAYS AS (RAISE(IGNORE) + avg(CURRENT_TIMESTAMP) FILTER (WHERE +CURRENT_TIME) != FALSE != ~CURRENT_TIMESTAMP BETWEEN TRUE AND FALSE 
```

---

## Crash 4: `f17bcf499c9aa133` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001339`

```sql
SELECT substr('_-jw-7', -2147483648, 0);
```

---

## Crash 5: `d84c4fc62c636dd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001545`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (c3 AND CURRENT_TIMESTAMP REGEXP CURRENT_TIMESTAMP IS NOT NULL -> jsonb_object('H-y7_ _ ', CASE FA
```

---

## Crash 6: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001642`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 7: `2c3ab78aed765e01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000001652`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME = NOT RAISE(IGNORE) / RAISE(IGNORE) < ~jsonb_remove('[]', '$[0].c') FILTER (WHERE 919 COLLATE BINARY) COLLATE RTRIM FROM p WHE
```

---

## Crash 8: `d3c9facce7780fb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003062`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 9: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `5_000004254`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 10: `d236a1421a31a1f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000006435`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT GENERATED ALWAYS AS (-RAISE(IGNORE)) STORED, c2 INT UNIQUE, c3 NUMERIC UNIQUE, c1 FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) STORED); CREATE VIEW IF NOT EXISTS v1 A
```

---

## Crash 11: `1c8fe9863764d728` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013264`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN SELECT *, * FROM json_tree('{"a":{"b":1}}') GROU
```

---

## Crash 12: `db99a0e539b8bc59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000018052`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY, rowid DATE GENERATED ALWAYS AS (FALSE NOT IN (NOT c2 NOT IN (CURRENT_DATE NOTNULL NOT IN (VALUES (RAISE(IGNORE)) ORDER BY FALSE ASC NULLS FIRST)) IN
```

---

## Crash 13: `d0e2a8a8e3bd2dc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000026362`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN, c1 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL); SELECT NULL IS NOT DISTINCT FROM RAISE(IGNORE) << FALSE NOT LIKE CURRENT_TIMESTAMP >= FALSE AND FALSE ISN
```

---

## Crash 14: `3c8e86ca5a4166d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000026677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, a GENERATED ALWAYS AS (a || b) UNIQUE, b FLOAT UNIQUE); INSERT INTO p SELECT p.* FROM (jsonb_tree('{"a":{"b":1}}') CROSS JOIN json_tree('{}') ON c2 * CASE WHEN (V
```

---

## Crash 15: `27e53e18dcc95ae5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000027249`

```sql
SELECT printf(''%.*f'', 2147483647, -CASE '2_-y' WHEN CURRENT_TIMESTAMP NOTNULL IN (CURRENT_DATE <= CURRENT_DATE >= FALSE IS NULL) MATCH CURRENT_DATE COLLATE RTRIM IS NOT NULL + CURRENT_TIMESTAMP ISNU
```

---

## Crash 16: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029283`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 17: `3a4a55de3ed86b3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029901`

```sql
SELECT substr('_P WS8- F-_Il', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 18: `2caaac91f2e85313` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `5_000035213`

```sql
SELECT substr('', 9223372036854775807, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 19: `63bf504bacee4c06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082904`

```sql
SELECT substr('_P WS8- F-_Il', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 20: `598c1d00c16b8d30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000001898`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT *; CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT b, q.* FROM json_
```

---

## Crash 21: `61b62d6df02a9724` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004272`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 22: `ba1d127405e841cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000004282`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 23: `9fb465ed610bb93c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007484`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT NULL AS l_gz_mkg8b_08v5066__8_hb_7q_b0_uz562__to2__36
```

---

## Crash 24: `8e55cb75617e5ef9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000007513`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); SELECT printf('%llu', 4294967296, 'i_3--a_o-U
```

---

## Crash 25: `c874c0046ebb03bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000007553`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CASE WHEN CURRENT_TIME THEN RAISE(IGNORE) NOTNULL END); VALUES (TRUE); CREA
```

---

## Crash 26: `58966e231b358bc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000007772`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT * INTERSECT VALUES (-CURRENT_TIMESTAMP > CURRENT_TIME
```

---

## Crash 27: `117d8634b2d11c78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007780`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT NULL AS l_gz_mkg8b_08v5066__8_hb_7q_b0_uz562__to2__36
```

---

## Crash 28: `81046e15a2be182d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007794`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT NULL AS l_gz_mkg8b_08v5066__8_hb_7q_b0_uz562__to2__36
```

---

## Crash 29: `4224ddb761c12186` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007877`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_DATE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 30: `1673ab7dc37edfe2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008097`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) CHECK (NULL BETWEEN (CURRENT_DATE) COLLATE BINARY - TRUE NOTNULL AND CAST(CURRENT_TIMESTAMP AS BLOB
```

---

## Crash 31: `67ae95fb55c1b392` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008137`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_DATE / CURRENT_DATE / CURRENT_DATE / CURRENT_DATE / 
```

---

## Crash 32: `bee42c802317aa39` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008189`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid INT PRIMAR
```

---

## Crash 33: `f87bc9342ec48df3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008230`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid INT PRIMAR
```

---

## Crash 34: `aef2c41caa38da6c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013928`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid INT PRIMAR
```

---

## Crash 35: `3dee375e362523d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014093`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TAB
```

---

## Crash 36: `52854fd5847d72c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000014184`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE / CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(r
```

---

## Crash 37: `74efdce7adc1a994` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014490`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP COLLATE RTRIM >= NOT TRUE AND CURRENT_TIMESTAMP / CURRENT
```

---

## Crash 38: `40212b32c9dcc34c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014651`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (FALSE >= NOT TRUE AND CURRENT_TIMESTAMP / CURRENT_DATE / CURRENT_DATE / CUR
```

---

## Crash 39: `dd0119ae25589536` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000015625`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT NULL AS l_gz_mkg8b_08v5066__8_hb_7q_b0_uz562__to2__36
```

---

## Crash 40: `a3d62ccc42831971` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020624`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY, a REAL GENERATED ALWAYS AS (~-(TRUE) IS NULL) STORED); INSERT INTO p VALUES (CURRENT_DATE)
```

---

## Crash 41: `aa6f7695e08c10c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000021145`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY, c1 BLOB GENERATED ALWAYS AS (NULL IN (count() OVER (PARTITION BY TRUE) AND count(*), NULL ISNULL = FALSE != CURRENT_DATE)) VIRTUAL, c1 FLOAT UNIQUE)
```

---

## Crash 42: `4a9331d6e223c626` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021621`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME / CURRENT_DATE / CURRENT_DATE / CURRENT_DATE / CURRENT_DATE / 
```

---

## Crash 43: `113c95ca90397a4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000030049`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) CHECK (NULL BETWEEN CURRENT_TIMESTAMP - TRUE AND p.a + CASE WHEN ~TRUE GLOB CASE NULL IS NULL WHEN 
```

---

## Crash 44: `6356ca26d369a4c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032028`

```sql
SELECT substr('', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 45: `2ca36d356b749d68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039742`

```sql
SELECT printf('%.*g', 4294967296, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 46: `7de5ff4fd1e12eb6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000076002`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIME); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMAR
```

---

## Crash 47: `2140cb8383be0f39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `6_000084804`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP COLLATE RTRIM >= NOT TRUE AND CURRENT_TIMESTAMP / CURRENT
```

---
