# Crash Triage Report

**Total crashes:** 21  
**Unique crash sites:** 21  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 20 | 20 | 95% |
| Signal | 1 | 1 | 4% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `b3ffbf437ee9bc0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000178`

```sql
SELECT printf('%llu', 9223372036854775807, '-k6 94_V_-2g-__-2'); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL DEFAULT CURRENT_DATE, c3 INTEG
```

---

## Crash 2: `5192d5060c1fff73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000244`

```sql
SELECT substr('BIX- --M -_', 1);
```

---

## Crash 3: `ffa0bc3e3aeca9c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000314`

```sql
SELECT round(-1.0, 4294967295);
```

---

## Crash 4: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001850`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 5: `2b8b07654c317a73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001864`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR IGNORE INTO p VALUES ((FALSE COLLATE NOCASE) >> b ->> avg(rank() OVER (PARTITION BY CURRENT_TIMESTAMP) >> ~RAISE(IGNORE) AND FALS
```

---

## Crash 6: `e643d7ee63d5a6e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002000`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR IGNORE INTO p VALUES ((jsonb_array(-RAISE(IGNORE) + TRUE OR FALSE, CURRENT_DATE ISNULL NOTNULL, TRUE NOT BETWEEN FALSE AND CURREN
```

---

## Crash 7: `9da3932255e51982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000007721`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_
```

---

## Crash 8: `58b440b3b550088b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000016068`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*s', 4294967296);
```

---

## Crash 9: `7e65058c23aca77c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000016227`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN SELECT cume_dist() OVER (PARTITION BY NULL) << TRUE ISNULL - CASE WHEN CURRENT_TIME THEN NULL IS NULL END AS q_t9m1y8_f_r_tc_
```

---

## Crash 10: `c8d1358624ca8b0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041336`

```sql
SELECT substr('0aN-t-V-2 P', 0, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 11: `370878cc9e80c7b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041343`

```sql
SELECT round(1e308, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 12: `1606991e2c6cd577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000041392`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 13: `544dbbbf9b462a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041442`

```sql
SELECT substr('0aN-t-V-2 P', 0, -9223372036854775808); SELECT substr('0aN-t-V-2 P', 0, -9223372036854775808); SELECT substr('0aN-t-V-2 P', 0, -9223372036854775808); SELECT substr('0aN-t-V-2 P', 0, -92
```

---

## Crash 14: `b05fc387c396eff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062738`

```sql
SELECT printf('%s', 2147483647, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER
```

---

## Crash 15: `224f2a22773291f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062754`

```sql
SELECT substr('0aN-t-V-2 P', 0, 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 16: `d9d698527fd1f219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063990`

```sql
SELECT printf('%s', 9223372036854775807, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lea
```

---

## Crash 17: `c98b28be667eb1c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000064030`

```sql
SELECT printf('%s', 2147483647, ''); CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT NOT FALSE <= TRUE ISNULL >> CURRENT_TIMESTAMP IS NOT lead(RAISE(IGNOR
```

---

## Crash 18: `48d0ff6c4e34acde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064376`

```sql
SELECT substr('0aN-t-V-2 P', 0, 4294967295); SELECT substr('0aN-t-V-2 P', 0, 4294967295); SELECT substr('0aN-t-V-2 P', 0, 4294967295); SELECT substr('0aN-t-V-2 P', 0, 4294967295); SELECT substr('0aN-t
```

---

## Crash 19: `7838423e6be512ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074575`

```sql
SELECT substr('k 3i5_-N0_E', -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 20: `cb48e89ef78b7416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000080078`

```sql
SELECT printf('%.*g', 2147483648, -1e308); SELECT round(1e308, 2147483648); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((S
```

---

## Crash 21: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001615`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---
