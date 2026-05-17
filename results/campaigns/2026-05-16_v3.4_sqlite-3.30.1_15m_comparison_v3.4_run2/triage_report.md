# Crash Triage Report

**Total crashes:** 364  
**Unique crash sites:** 364  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 120 | 120 | 32% |
| Signal | 244 | 244 | 67% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9c3b458aba6c87ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000395`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT INTO r (rowid, c2, c2) VALUES (CASE NULL << NULL IS DISTINCT FROM NULL NOT LIKE RAISE(IGNORE) COLLATE NOCASE > NULL BETWEEN TRUE AN
```

---

## Crash 2: `e731534b88ee3311` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000470`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC DEFAULT X'203ebE1dE024fCF'); CREATE VIEW IF NOT EXISTS v1
```

---

## Crash 3: `9b90d78b525f0738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000654`

```sql
SELECT printf('%f', 2147483648, ' f3ZZr7q0Ps_SaYE_U '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); REPLACE INTO q VALUES (b, (NULL IS CASE WHEN RAISE(IGNORE) THEN TRUE END || C
```

---

## Crash 4: `3308eed456413a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000797`

```sql
SELECT printf('%.*d', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c3, c3); WITH p AS MATERIALIZED (SELECT NULL FROM json_tree('{}') GROUP BY FALSE COLLATE BINARY IS 
```

---

## Crash 5: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000976`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 6: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001628`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 7: `bd1719b87694b06f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002131`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 8: `3cdd7d9412406a90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002143`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 9: `eee0cdcfe40254ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002342`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_
```

---

## Crash 10: `90076acd08669494` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002353`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 11: `dd02d885a9b57567` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003743`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 12: `9fd2161598b128c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004375`

```sql
SELECT printf('%.*s', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 13: `4717e1d3edb62355` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004596`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE OR ~count(*) FILTER (WHERE NULL) OVER () ISNULL LIKE RAISE(IGNORE) ESCAPE CURRENT_DATE != CURRENT_TIME IS NULL)
```

---

## Crash 14: `99236ba457a580e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004604`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE OR ~count(*) FILTER (WHERE NULL) OVER () ISNULL LIKE RAISE(IGNORE) ESCAPE CURRENT_DATE) UNION ALL SELECT *; VAL
```

---

## Crash 15: `782269114b164fe8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004630`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE NOTNULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 16: `eefdd779869250b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004656`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 17: `ac4798016ad0dcc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005474`

```sql
SELECT substr('', -1); SELECT round(0.0, 1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 18: `2c120f7952464040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005892`

```sql
SELECT printf('%x', 0, 'Gu-l1vW'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 19: `a96382b630303c1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005900`

```sql
SELECT printf('%x', 0, 'Gu-l1vW'); SELECT substr(' _', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SEL
```

---

## Crash 20: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007986`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 21: `887f603b2f765549` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008039`

```sql
SELECT printf('%.*s', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); WITH RECURSIVE t3 AS NOT MATERIALIZED (SELECT * ORDER BY EXISTS (VALUES (CURRENT_DATE) UNION VALUES
```

---

## Crash 22: `16b43314301f4505` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010624`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) UNION SELECT * FROM p AS s9tj LEFT JOIN json_tree('[1,2,3]') WHERE CURRENT_DATE ORDER BY NULL DES
```

---

## Crash 23: `49e5ef92d1b3bdf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010646`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) UNION SELECT * FROM p AS s9tj LEFT JOIN json_tree('[1,2,3]') WHERE CURRENT_DATE ORDER BY NULL DES
```

---

## Crash 24: `4adcbbfe0da24070` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010688`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) UNION SELECT * FROM p AS s9tj LEFT JOIN json_tree('[1,2,3]') WHERE CURRENT_DATE ORDER BY NULL DES
```

---

## Crash 25: `2b96d6695cd67bf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010704`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) UNION SELECT * FROM p AS s9tj LEFT JOIN json_tree('[1,2,3]') WHERE CURRENT_DATE ORDER BY NULL DES
```

---

## Crash 26: `95f01a3eb573950a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010710`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE) UNION SELECT * FROM p AS s9tj LEFT JOIN json_tree('[1,2,3]') WHERE CURRENT_DATE ORDER BY NULL DES
```

---

## Crash 27: `5ddf2cb82236b557` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010830`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT dense_rank() OVER () AS a; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 28: `5e63872eb3e1b2c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010989`

```sql
SELECT substr(' _', 0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) 
```

---

## Crash 29: `6b5e833a9e356c09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010997`

```sql
SELECT printf('%.*e', 0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))
```

---

## Crash 30: `d15f1d441f405457` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011005`

```sql
SELECT round(-1.0, -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), 
```

---

## Crash 31: `0f45e29eedd3ecfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011013`

```sql
SELECT substr('qq 3 ', -9223372036854775808, -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT
```

---

## Crash 32: `6a2460a0ea870dec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011019`

```sql
SELECT printf('%lld', -9223372036854775808, '08-Cc-WH7u - l-N- '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELEC
```

---

## Crash 33: `9f3e9c349811b1d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011066`

```sql
SELECT printf('%d', -2147483649, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVE
```

---

## Crash 34: `299baa676864a3a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011072`

```sql
SELECT printf('%.*s', 4294967295, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 35: `c8451bbdb2826288` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011083`

```sql
SELECT printf('%.*s', -1, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 36: `7d64f27226f201c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013701`

```sql
SELECT round(1e308, 9223372036854775807); SELECT round(-1e308, 2147483648); SELECT substr(' _', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c N
```

---

## Crash 37: `23b036b53d2aed9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020350`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 38: `3ce381f92db66701` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020460`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 39: `7abe7733a2cb45c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020491`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 40: `060de180797bba30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021609`

```sql
SELECT printf('%.*f', -9223372036854775808, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 41: `510f624d3684f6dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021621`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(a BOOLEAN PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 42: `8fa54cf58d297c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024987`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE);
```

---

## Crash 43: `6b0cdc171ccf626a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033393`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CREATE TABLE IF
```

---

## Crash 44: `5799f8b8ace1ec03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039629`

```sql
SELECT substr('o-_Q1__F', -9223372036854775808, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELE
```

---

## Crash 45: `4d4fb337205980f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039678`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE, c2 FLOAT UNIQUE, c1 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 46: `e32d96e13e4b0324` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039702`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT ' _s-6 1E'); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 47: `48952e4178cf05b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039734`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT -8043); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 48: `908c3fbb42559835` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039777`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE I
```

---

## Crash 49: `4b43a8b8742b107a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039797`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integ
```

---

## Crash 50: `055704e4a6821a0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039806`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integ
```

---

## Crash 51: `2046edc7da109f86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041303`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM s
```

---

## Crash 52: `72951c419450bdd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041312`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM s
```

---

## Crash 53: `e0b348143c3f4a88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041644`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (FALSE BETWEEN rowid AND CURRENT_TIMESTAMP) IS NOT NULL)); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREAT
```

---

## Crash 54: `7f3c544bebd03863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041682`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT rank() OVER (ORDER BY FALSE DESC ROWS BETWEEN CURRENT_DATE PRECEDING AND CURRENT_DATE FO
```

---

## Crash 55: `84efa412b3581cc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041698`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (changes()) IS NOT NULL)); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT
```

---

## Crash 56: `66e97ee26c5b652e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041708`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT row_number() FILTER (WHERE NULL) OVER w1 AS j__6__oa8_hl_w7w_x_vr__26f2x9gsu_1_0__z__3_8
```

---

## Crash 57: `c855774e5622e6fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041723`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT *) SELECT FALSE || CURRENT_DATE AS a; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 58: `ff6d6a448af5322a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041729`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT ALL * FROM json_tree('[{"a":1},{"b":2}]') LEFT JOIN json_tree('{}') ON CURRENT_DATE) SEL
```

---

## Crash 59: `fb867ee5dbeece62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041735`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 60: `394886e5a95e4d5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041801`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 61: `750983b030ae0772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041842`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 62: `cd6e0f1b7fba0da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042774`

```sql
SELECT round(-1.0, -2147483648); CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM json_tree(CU
```

---

## Crash 63: `55f3425a6fb267cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042974`

```sql
SELECT round(-1.0, -2147483648); CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * FROM s UNION SELECT * FROM jsonb
```

---

## Crash 64: `43495f7c86bd663c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM p JOIN p m_ ON CURRENT_TIME MATCH FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 65: `5ed73bf9f410757b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045694`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE))) SELECT *, *, p.* FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 66: `f8ac9a62723572de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE))) SELECT p.* FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 67: `189d8cabdfb769f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047002`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3, a, b, c2) AS (VALUES (RAISE(IGNORE))) SELECT p.* FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 68: `390f347c82d25ea0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE))) SELECT nth_value(FALSE, TRUE) OVER (), rowid FROM p; CREATE TABLE se
```

---

## Crash 69: `928161c39fcdf1ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047036`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(ROLLBACK, ''), CURRENT_TIME)) SELECT p.* FROM p; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 70: `8aa5646555420a57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047067`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP)) SELECT p.* FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 71: `26db0ab99c506f9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047077`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY TRUE WINDOW w1 AS () LIMIT CURRENT_TIMESTAMP; WITH RECURSIVE t2 (c
```

---

## Crash 72: `c0ba8149197ac57e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047083`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (changes() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS 
```

---

## Crash 73: `c46e4fa76b2202d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047097`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (FALSE NOT IN (VALUES (RAISE(IGNORE))), FALSE)) SELECT p.* FROM p; CREATE TABLE seed_
```

---

## Crash 74: `8a5fe28453778303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047108`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE) LIKE TRUE NOT LIKE NULL ESCAPE CURRENT_DATE != NULL)) SELECT p.* FROM 
```

---

## Crash 75: `4be7664323571164` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047184`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT NULL, b REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE))) SELECT p.* FROM p; CREA
```

---

## Crash 76: `9e2179757771b981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047203`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE t2 (c3) AS (VALUES (RAISE(IGNORE))) SELECT p.* FROM p; CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE IND
```

---

## Crash 77: `2bd8d47f71aca876` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050196`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM p JOIN p m_ ON CURRENT_TIME MATCH json_patch('[]', '[]'); CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 78: `4f81f51313cf1f8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050202`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT rank() OVER (ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS g FRO
```

---

## Crash 79: `bd71e766bba1a050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050223`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM p JOIN p m_ ON CURRENT_TIMESTAMP <= NULL MATCH FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 80: `a930af619b472d58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM p JOIN p m_ ON CURRENT_TIME MATCH CASE CURRENT_TIME WHEN TRUE THEN CURRENT_TIMESTAMP AND CUR
```

---

## Crash 81: `d8cd9f6e1d71f560` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050236`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT (VALUES (CURRENT_TIME)) AS g6x_lv1___6hm_kq8nv8____v__kx9___e12jaj0i0_3__5gx__05l_05j54480869_2d_o9
```

---

## Crash 82: `cf3b37587de53b45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050248`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY NULL WINDOW w1 AS () LIMIT CURREN
```

---

## Crash 83: `d3f038830c7a378c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050274`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP 
```

---

## Crash 84: `16a58a31bb6a538e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050280`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ABORT INTO p VALUES (json_extract(NULL, '$[#-1]')); PRAGMA quick_check; CREATE TABLE
```

---

## Crash 85: `dde0bc63670285eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050294`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP), * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_TIME 
```

---

## Crash 86: `4df4ebd902edd8c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050301`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT nth_value(FALSE, TRUE) OVER (), rank() OVER (ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING A
```

---

## Crash 87: `118ea457df5b972a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050319`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT p.* FROM p JOIN p m_ ON CURRENT_TIME MATCH FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 88: `bed55fa2591e435c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050331`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT NOT NULL); SELECT * FROM p JOIN p m_ ON p.c1 MATCH FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 89: `b77da172e54c893e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050461`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 90: `6198469b24d5a776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050475`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[1,2,3]') WHERE CURRENT_DATE GROUP BY NULL WINDOW
```

---

## Crash 91: `07699c89cbdd3acf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050941`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); INSERT OR ABORT INTO p VALUES (last_insert_rowid()); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 92: `a127b2471991eb6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050975`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); INSERT INTO p WITH t2 AS (VALUES (CURRENT_DATE)) VALUES ('2'); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 93: `154ca5a3710a662d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053186`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT nth_value(FALSE, TRUE) OVER (), rank() OVER (ORDER BY FALSE DESC RO
```

---

## Crash 94: `645191ab0afca620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053196`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM json_each('{}') WHERE CURRENT_DATE GROUP BY N
```

---

## Crash 95: `ad70de7bb514fd2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053224`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM (json_each('[{"a":1},{"b":2}]') LEFT OUTER JO
```

---

## Crash 96: `33c1f8c9a2fbb4d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053237`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT percent_rank() OVER () UNION SELECT * FROM json_each('{}') WHERE CU
```

---

## Crash 97: `0d073499785f74ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053246`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM json_each('{}') WHERE CURRENT_DATE GROUP BY N
```

---

## Crash 98: `15338b28240d03fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053268`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT rank() OVER (ORDER BY FALSE DESC ROWS BETWEEN CURRENT_DATE PRECEDIN
```

---

## Crash 99: `4301dda066eeeb21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053274`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT r.* FROM (SELECT RAISE(IGNORE)) AS s2ows2_88gep____u_o4t_90f__qbh_3
```

---

## Crash 100: `d20aea903a971742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053298`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM p AS s9tj LEFT JOIN r INDEXED BY a WHERE CURR
```

---

## Crash 101: `d49656813316864f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053310`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM json_each('{}') WHERE CURRENT_DATE GROUP BY N
```

---

## Crash 102: `f8dfbb859a71d22f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053317`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT nth_value(FALSE, TRUE) OVER (ORDER BY CURRENT_TIMEST
```

---

## Crash 103: `1802c002227d99fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053355`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO q SELECT * UNION SELECT * FROM jsonb_each('{}') , q INDEXED BY c3 CROSS JOIN
```

---

## Crash 104: `c1f4cf5de04fb2a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055078`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) UNION ALL SELECT * FROM (VALUES (NULL)) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_pteda1__; PRAGMA integrity_check;
```

---

## Crash 105: `dee5018ef916f23f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055096`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREA
```

---

## Crash 106: `48465a6f9766093f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055104`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (CAST(CURRENT_TIMESTAMP AS VARCHAR(255))) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 107: `b4d25e79162a8c9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055118`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY F
```

---

## Crash 108: `14d5c57aa2c1513c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055125`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (CAST(FALSE AS BOOLEAN)) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 109: `f77d17ef8dc88054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055145`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP
```

---

## Crash 110: `ee52f91f13ba6c07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE BETWEEN rowid AND CURRENT_TIMESTAMP IS NOT NULL)); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c 
```

---

## Crash 111: `f5b3aff948feb651` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055163`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 112: `3a1f446d799b7ecb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055177`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME IS TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 113: `342a9154fc1ca054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055183`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) INTERSECT VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 114: `f671a479d24a3be9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055302`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE T
```

---

## Crash 115: `2a632868fbe219ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055419`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED NATURAL JOIN (json_tree('[]')) USING (b, rowid) GROUP BY CURRENT_TIMESTAMP ORDER BY CU
```

---

## Crash 116: `82959c5c02f4997f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055426`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'6DFe41aCe6'); INSERT INTO p VALUES (FALSE) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 117: `310ec96724e27652` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055460`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p VALUES (X'' * CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UN
```

---

## Crash 118: `0c084ee06590b56b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065025`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); REPLACE INTO p VALUES (CURRENT_DATE); SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE IF
```

---

## Crash 119: `c8216ed7e0104912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066636`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL dense_rank() OVER (PARTITION BY NULL O
```

---

## Crash 120: `bef29a876a6c0b08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081156`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT * FROM json_tree('[{"a":1},{"
```

---

## Crash 121: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001622`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 122: `ae2bca0784380d7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001960`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 123: `62d1a6d613ae1df3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001968`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3)
```

---

## Crash 124: `b6fd2b678e3b2a2d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002012`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) IS NOT NULL AS a; ANALYZE p; CREATE TABLE see
```

---

## Crash 125: `d690fc557f992a1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002019`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) AS a; ANALYZE p; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 126: `de0f3292a820d07b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002031`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) AS a; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 127: `86334aef3ab29ebc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002038`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p VALUES (FALSE); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); IN
```

---

## Crash 128: `374cc7b73a6118bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002047`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT NULL AS a; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 129: `14567d0df292e928` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002053`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 130: `296635a5d563f1f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002060`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CURRENT_TIMESTAMP AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 131: `37de9971d46ce942` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002073`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 132: `316b20c2fc25fe18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002081`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT TRUE AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 133: `85c389518936b9d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002100`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) AS a; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 134: `f4d037252e8a9bfc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002174`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT *) VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 135: `af951d2437912f6f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002220`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p WITH s AS (SELECT *) VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 136: `7a6daad53da04778` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002233`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); INSERT INTO p WITH s AS (SELECT *) VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 137: `eee9774ee9389387` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002239`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 138: `2499236f9190ccd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002250`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 139: `bab3bbe51f4484ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002256`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 140: `b4c942a28a464a68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002434`

```sql
SELECT round(-1.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 141: `71facf58d5e1c1d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002444`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 142: `074db05713cf8bbf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002455`

```sql
SELECT printf('%.*d', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 143: `cd1e13f5df6c46ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003116`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p UNION ALL VALUES (TRUE); CREATE TA
```

---

## Crash 144: `8a9e6f3c7b624c2c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003127`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 145: `c8d18f8bb76eb8cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003134`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CREATE TABLE se
```

---

## Crash 146: `829cb5d904a5fe38` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003152`

```sql
SELECT round(-0.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 147: `53aed94d3fb3b3bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003694`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 148: `6af5557971ac8afc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003701`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 149: `3329ed8eddd8a0c1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003707`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 150: `49792349f8e2f860` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003714`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 151: `45926ecd7884fc6a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003803`

```sql
SELECT substr('8_Y2bF__29', 4294967295, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(5
```

---

## Crash 152: `f15850743b5e79bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003836`

```sql
SELECT printf('%.*s', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 153: `4edfac52f43f0a35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004112`

```sql
SELECT substr('KqCM_j ', 2147483648, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(4
```

---

## Crash 154: `9b9583a9b3bc3daf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004297`

```sql
SELECT round(1e-308, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 155: `826656862954ac2b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004452`

```sql
SELECT substr('', -2147483648, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 156: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004518`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 157: `de736c63732c4c51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004715`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 158: `278945817e3b6bc9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004751`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 159: `85e8cd9c435868cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005556`

```sql
SELECT round(1e308, 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 160: `e9d028665fdea2d0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006162`

```sql
SELECT printf('%.*g', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 161: `19ba97575721e5ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006434`

```sql
SELECT substr('9', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 162: `2b2fa7fe40143c5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010174`

```sql
SELECT printf('%.*g', 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 163: `a135d85446067fa0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010180`

```sql
SELECT printf('%.*g', -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 164: `6a0f11675accc6b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010193`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 165: `daff8764ebcc0e60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010209`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p WITH s AS (SELECT *) VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 166: `8672c141456a6048` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010219`

```sql
SELECT printf('%f', -9223372036854775808, '08-Cc-WH7u - l-N- '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VA
```

---

## Crash 167: `797ca31aeb8d02c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010225`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION SELECT * FROM p INDEXED BY c3 WHERE FALSE GROUP BY FALSE; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 168: `61d6b2c4b969c54f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010235`

```sql
SELECT printf('%.*e', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 169: `00974a6b1d38c9bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010243`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 170: `0c5beb6bc6c54ac5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010303`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 171: `f9c841f4729ab97b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012020`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY NULL WINDOW w1 AS () LIMIT CURRENT_DATE, NULL NOT BET
```

---

## Crash 172: `c885e89efe96afcf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012045`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); SELECT *, FALSE FROM p JOIN p di ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 173: `5aee07ca01d7c1c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012054`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (VALUES (FALSE)) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_pteda1__ OR
```

---

## Crash 174: `feb4a7917468e20e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012084`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR FAIL INTO p VALUES (FALSE IS NOT FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 175: `9e5cd81b7fa02990` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012096`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) INTERSECT SELECT * FROM (p NOT INDEXED) WHERE CURRENT_DATE GROUP BY CURRENT_DATE ORDER BY CURRENT_DATE A
```

---

## Crash 176: `d2bd5ad1f5eb305f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012276`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR FAIL INTO p VALUES (changes() NOT IN (+TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 177: `b6030d6d57492982` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012328`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); SELECT * FROM p JOIN p di ON CURRENT_DATE LIKE TRUE ESCAPE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 178: `d94cf14506e80d52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012348`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT '- _-3  v_o'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 179: `12754fcb7bb39d61` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012411`

```sql
SELECT printf('%.*e', 0, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 180: `6697a0240e216857` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012665`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS () EXCEPT VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 181: `2e893c145e6eb9fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013300`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT 48827559641518826521216578473279403951126370020480.564E+273828386692969503007); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VAL
```

---

## Crash 182: `99dc4891501f64b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013460`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY CURRENT_TIMESTAMP | NULL, CURRENT_TIMESTAMP WINDOW w1 AS (); CREATE TABLE seed
```

---

## Crash 183: `444b8879434111c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014293`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 184: `c6cc9ae410c3407c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024525`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); WITH t2 AS (VALUES (CURRENT_DATE)) VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 185: `9e810108c2c6942e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024547`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (FALSE) UNION ALL VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 186: `a0fb9f9e14c71197` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024560`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT (VALUES (CURRENT_TIME)) AS g6x_lv1___6hm_kq8nv8____v__kx9___e12jaj0i0_3__5gx__05l_0
```

---

## Crash 187: `ad5f727808a966ef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024571`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_each('[]') WHERE CURRENT_DATE GROUP BY NULL; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 188: `5954263dc64d4643` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024586`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_tree('{"a":{"b":1}}') GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_t1(
```

---

## Crash 189: `e80ff472fbde7de8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024592`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_each('{"a":{"b":1}}') WHERE CURRENT_DATE GROUP BY NULL WINDOW w1 AS ();
```

---

## Crash 190: `f2ba285903898f11` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024623`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_each(FALSE, '$.a[0]') WHERE CURRENT_DATE GROUP BY NULL WINDOW w1 AS ();
```

---

## Crash 191: `af3c507ed23c6c55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024670`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT DEFAULT -84); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CASE WHEN CURRENT_TIMESTAMP + NULL % CURRENT_TIMESTAMP THEN CASE WHEN NULL THEN CUR
```

---

## Crash 192: `0465f134be680a3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024737`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CASE WHEN CURRENT_TIME % CURRENT_TIMESTAMP THEN CASE WHEN NULL THEN CURRENT_DATE E
```

---

## Crash 193: `447e926ace8fc628` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024744`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIME % CURRENT_TIMESTAMP AS a; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 194: `4980f6b84b33900e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026835`

```sql
SELECT substr(' mR--8_ _C--', 4294967295, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(
```

---

## Crash 195: `b3a34b60a81b9e57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026862`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GROUP BY CURREN
```

---

## Crash 196: `85b3b69e06890f28` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027620`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 197: `000a531e39d3af12` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027626`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT FALSE, c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 198: `e26bede3d8d7c46c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027641`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME)); INSERT INTO p DEFAUL
```

---

## Crash 199: `b0e180782afea637` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027647`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p VALUES (NULL) EXCEPT SELECT * FROM (VALUES (FALSE)) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_pteda1__
```

---

## Crash 200: `3779e44918ceb20d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027661`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (row_number() OVER () != CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 201: `530f92f382184da4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027674`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT percent_rank() FILTER (WHERE CURRENT_TIMESTAMP / NULL), * FROM json_each(CURRENT_TIMESTAMP, '$'); INSERT INTO 
```

---

## Crash 202: `d063fd88b0a4fe67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027681`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE NOT LIKE NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 203: `f081437befdd1bec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027688`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > CAST(CURRENT_DATE AS NUMERIC) OR CURRENT_DATE NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 204: `4ebb6d1b3bd30fa9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE, c1 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 205: `04f7b12647fe0d46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027717`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP GROUP 
```

---

## Crash 206: `4f498e4b202b2748` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027739`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (CURRENT_DATE) IS NOT NULL), a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 207: `ad8e08608f8a3e0f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027778`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN DEFAULT ''); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 208: `951d6100fdd6334c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027835`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT LIKE CURRENT_DATE));
```

---

## Crash 209: `f5b2cf179996e5f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027867`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 210: `f76933dbb827d5a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027874`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL NOT LIKE CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 211: `ae29716856b2d4b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027908`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (FALSE OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 212: `1806395381523789` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027924`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 213: `40a2de28ce7b36f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027984`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); VALUES (FALSE) INTERSECT VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 214: `427b033ad888a6db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028019`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM json_tree('{"a":{"b":1}}') GROUP BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME DESC; CREATE T
```

---

## Crash 215: `3b70af065eb1c64e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028049`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL NOT BETWEEN TRUE AND FALSE >= CURRENT_DATE * CURRENT_DATE IS NULL COLLATE BINARY)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE s
```

---

## Crash 216: `e304889ea08ee150` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000028154`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL * FALSE COLLATE BINARY)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 217: `f3d14413836d0801` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033305`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION VALUES (TRUE); CREATE TABLE seed_t
```

---

## Crash 218: `384851d7f657b004` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033314`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (NULL), a TEXT CHECK (RAISE(IGNORE))); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UN
```

---

## Crash 219: `0cc6103c8b9a4912` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033321`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL SELECT * FROM q WHERE TRUE GRO
```

---

## Crash 220: `2de35dcb11c28075` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033369`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CREATE TABLE seed_t
```

---

## Crash 221: `1e6b4ef6f33b6cb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033383`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL DEFAULT 677315); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 222: `1fcb9a2db181129f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033471`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT DEFAULT X'4f'); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CRE
```

---

## Crash 223: `8b1091d73abd6b3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033477`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CREA
```

---

## Crash 224: `f6e12ec4516e940a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033492`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) UNION ALL VALUES (TRUE); CREATE TABLE IF
```

---

## Crash 225: `295a6e9c08f6a1df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033536`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p UNION ALL VALUES (TRUE); CREATE TA
```

---

## Crash 226: `75e497360b07aa34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033546`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INT CHECK (NULL NOT BETWEEN CURRENT_TIME AND NULL), a NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELEC
```

---

## Crash 227: `8401ee6fbc57e766` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033554`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NATURAL JOIN p UNION ALL VALUES (T
```

---

## Crash 228: `5aec862ea3c2625f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033572`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE - TRUE WINDOW w1 AS 
```

---

## Crash 229: `a72ec279b4d7672d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033601`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p UNION ALL VALUES (TRUE BETWEEN TRU
```

---

## Crash 230: `480e78bccdd967fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033610`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY 
```

---

## Crash 231: `abd4687776e3fd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000033618`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INT CHECK (CURRENT_TIME IN (NULL)), a NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p U
```

---

## Crash 232: `50b09e6cef734758` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034254`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p (a) VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 233: `e750d41afac65a00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034315`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE T
```

---

## Crash 234: `6252b02e37bfc392` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034330`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED NATURAL JOIN jsonb_each('[1,2,3]') USING (b, rowid) GROUP BY CURRENT_TIMESTAMP ORDER B
```

---

## Crash 235: `cd684ce79d79495e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034339`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (CURRENT_TIMESTAMP COLLATE BINARY < NULL NOTNULL)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TAB
```

---

## Crash 236: `bb9ed25eeab2a996` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034353`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (json_valid(CURRENT_DATE))); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 237: `d94b5a01395afd66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038821`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (NULL) ON CONFLICT(c3) DO UPDATE SET c3 = CURRENT_TIME; PRAGMA integr
```

---

## Crash 238: `82ca9afad66c6c9a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038838`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (CURRENT_TIME)); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 239: `7d6a016c70bac8a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038947`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[{"a":1},{"b":2}]') WHERE FALSE ISNULL GROUP BY N
```

---

## Crash 240: `7b3c4178bc3df27a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038970`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK ('2')); CREATE TABLE IF NOT EXISTS q(c3 FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 241: `96297b0fb1ce0928` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040478`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT INTO p SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS (); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 242: `779e4f5713180034` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040498`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM p JOIN p di ON TRUE NOT IN (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 243: `bb8ba62b77d0bb89` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); INSERT INTO p SELECT count() ORDER BY RAISE(IGNORE) DESC NULLS LAST; EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 244: `747f569d8c0ef94c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040514`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT OR FAIL INTO p VALUES (NOT TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 245: `088164ca24a7497d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040530`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (CURRENT_TIMESTAMP < CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 246: `e104cd9a702ddf66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040542`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM json_each('{"a":1}') GROUP BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME DESC; CREATE 
```

---

## Crash 247: `d7377b89bed20e74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040557`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM p JOIN p di ON CURRENT_DATE LIKE NULL ESCAPE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 248: `4f9d42d440807198` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040574`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (-TRUE)); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 249: `635816becb6243fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040585`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (NULL)), a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 250: `7a88f3b44611735b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040602`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 251: `b0a025bdd7142de6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040642`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT X'', c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 252: `492302d78abc340e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040710`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'7E9CB1ABfd68'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 253: `ec54cff0635ae019` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040729`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT 6.5); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 254: `e6ff883634c11b3c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040739`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT -1374656361739234410709433624486807100184407427929564663079349108108327052564140867512161863868828753336494096865769412.1486); INSERT INTO p
```

---

## Crash 255: `2c611936af8e0643` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040755`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'Ca'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 256: `b2fb1c0d359941f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040761`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'2FeCAfabafFf9E'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 257: `3d3f3b665c2db246` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040767`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 258: `79f7418550a17c10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040785`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_tree('{"a":1}') GROUP BY p._rowid_, CASE WHEN RAISE(IGNORE) THEN CURRENT_DATE ELSE CURR
```

---

## Crash 259: `7d4cbb77e61258bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040791`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'e7bc04'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 260: `43ae17b83ba36208` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040801`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT X'848cbDd7FBff'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 261: `378a197ba267c6de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040813`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT OR FAIL INTO p VALUES (changes() NOT IN (+TRUE)); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 262: `60e8e28747c30ef2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040821`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT -84); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 263: `7587bd3022bb954c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040839`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY, a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 264: `b5c2ec31ae4c6650` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040907`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURREN
```

---

## Crash 265: `507a1f662662bc00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040913`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL DEFAULT CURREN
```

---

## Crash 266: `0adc82951048a7ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041051`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT (VALUES (CURRENT_TIME)) AS g6x_lv1___6hm_kq8nv8____v__kx9___e12jaj0i0_3__5gx__05l_05j54480869_2d_o91_6_4__4k3l___7_78q__18
```

---

## Crash 267: `e42085c997e8f9eb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041058`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH RECURSIVE q AS (WITH RECURSIVE p (a) AS (VALUES (CURRENT_DATE)) VALUES (CURRENT_TIMESTAMP)) VALUES (CURRENT_TIMESTAMP); PRAGMA integrit
```

---

## Crash 268: `40046f53c8cfe77b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041075`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT * EXCEPT SELECT ALL * FROM (SELECT *) AS i28__ymvi03r__cry46_78n8y_792__52__7h18tki8is_dr5x_0qg_f8__j_j_29_qpi_rs730k_g8o_
```

---

## Crash 269: `412b59144372c494` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041093`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NATURAL JOIN (p) WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP LIMIT FALSE; INSERT INTO p WITH 
```

---

## Crash 270: `5ab8bc9043ff834a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041117`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT NULL IN (SELECT count() LIMIT NULL) AS v8a FROM json_tree('{"a":{"b":1}}') WHERE FALSE GROUP BY CURRENT_TIMESTAMP WINDOW w
```

---

## Crash 271: `f3c192bc51c63112` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041125`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT * FROM q NOT INDEXED NATURAL LEFT JOIN jsonb_tree('[{"a":1},{"b":2}]') CROSS JOIN json_tree(CURRENT_TIMESTAMP, '$[#-1]') G
```

---

## Crash 272: `8fce4408bd07477b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041150`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT *) VALUES (-TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 273: `6e6f2390684f28ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041162`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS () INTERSECT VALUES (FALSE); CREATE TABLE 
```

---

## Crash 274: `40e44c4de597709b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041206`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT p.*) VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 275: `088ea0c0ffa4699d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041218`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT last_insert_rowid() FILTER (WHERE RAISE(IGNORE) NOTNULL) OVER () + NULL > q.b > +NULL >= TRUE >> FALSE NOTNULL IS NOT NULL
```

---

## Crash 276: `40703ac3b4a10a8c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041238`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p WITH s AS (SELECT ~CURRENT_TIME + CURRENT_DATE = nullif(CURRENT_DATE, CURRENT_DATE) FILTER (WHERE CURRENT_TIMESTAMP > abs(NULL) FILTER (WHER
```

---

## Crash 277: `3a8f6840f8ce6657` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041326`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM s
```

---

## Crash 278: `daf7a9fe4856fcd9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041902`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CURRENT_TIMESTAMP COLLATE BINARY < NULL NOTNULL AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 279: `86f9ed511ec8607f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041910`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 280: `397f2d6eadcc3930` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041916`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP AS FLOAT) AS a; PRAGMA integrit
```

---

## Crash 281: `5b070ebf4eb5f982` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041941`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS INT) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 282: `a3ab0f30973a6ff2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041948`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT * FROM p NOT INDEXED NATURAL JOIN (json_tree('[]')) USING (b, rowid) GROUP BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP A
```

---

## Crash 283: `f4904ddca65e8081` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041971`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST((VALUES (CURRENT_TIME)) AS FLOAT) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 284: `94172dd6b6b62313` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042061`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS BLOB) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 285: `f385470cdd1814f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT (VALUES (CURRENT_TIME)) AS g6x_lv1___6hm_kq8nv8____v__kx9___e12jaj0i0_3__5gx__05l_05j54480869_2d_o91_6_4
```

---

## Crash 286: `4724db215931ca5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042368`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT quote(TRUE) ORDER BY RAISE(IGNORE) ASC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 287: `1e3a5133e5709307` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042388`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT dense_rank() OVER () AS a FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS () INTERSECT VALUES (
```

---

## Crash 288: `d67b61301dcf30c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053983`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT rowid FROM (SELECT * FROM json_each('[]')) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_pteda1__ GROUP BY C
```

---

## Crash 289: `401e1f8f6c8fdd74` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053994`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT percent_rank() OVER (); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 290: `cbd20a7db716a17d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054004`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT nth_value(FALSE, TRUE) OVER (); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 291: `71532fd90bfd9d88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054029`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT nth_value(FALSE, TRUE) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRE
```

---

## Crash 292: `1fba2c9d81a44de7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054037`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT count(*) OVER (ORDER BY CURRENT_TIMESTAMP < CURRENT_DATE DESC); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 293: `737c5a61f66f7189` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054045`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH p AS (SELECT ALL * FROM p LEFT OUTER JOIN json_tree('[{"a":1},{"b":2}]') CROSS JOIN json_each('{"a":{"b":1}}')), s AS (VALUES (CURRENT_DA
```

---

## Crash 294: `0395565bd5eb3245` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054080`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_DATE NOT IN (WITH p AS (VALUES (CURRENT_TIMESTAMP)), s AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * F
```

---

## Crash 295: `ce7b27bbb2a89483` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054087`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP < X'' AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 296: `ed4c984f16b85e38` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054094`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(EXISTS (VALUES (TRUE)) AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 297: `98ac2bb0bcbcc763` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054201`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP)) AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 298: `d3516e76fa640354` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054209`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_DATE NOT IN (WITH s AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM p) AS VARCHAR(255)) AS a; PRAGM
```

---

## Crash 299: `24dc81e797c5edd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054215`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_DATE NOT IN (VALUES (CURRENT_DATE)) AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 300: `e5f189445cbb22e4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054255`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(NULL AS VARCHAR(255)) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 301: `114f9341f3b70831` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054330`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT cume_dist() OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCL
```

---

## Crash 302: `4d639d762122c38e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054373`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('[1,2,3]') WHERE RAISE(IGNORE) GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS (); INSERT INT
```

---

## Crash 303: `e43fa68f354cd56f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054400`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURR
```

---

## Crash 304: `6dab6b0db03047a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054409`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE); VALUES (CURRENT_DATE) INTERSECT VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 305: `d122201865e69e80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054450`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT CURRENT_TIMESTAMP NOT BETWEEN CURRENT_DATE COLLATE NOCASE AND FALSE AS a FROM p JOIN p di ON FALSE;
```

---

## Crash 306: `a1f838d0b9a52a91` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054496`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS INT) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 307: `336b3263a0007cce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054567`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIME * CURRENT_TIME * FALSE AS INT) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 308: `e95df8c5e96b1e6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054626`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_TIMESTAMP AS BLOB) AS a; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 309: `97a5797a3ba5e5f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054656`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CURRENT_DATE LIKE CURRENT_TIMESTAMP ESCAPE FALSE AS BLOB) AS a; PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 310: `34febca7a4b56228` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054687`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT ALL * FROM (SELECT *) AS i28__ymvi03r__cry46_78n8y_792__52__7h18tki8is_dr5x_0qg_f8__j_j_29_qp
```

---

## Crash 311: `39a7306856069028` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054711`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); SELECT rowid FROM (VALUES (CURRENT_TIME)) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_pteda1__ GROUP BY CURRENT_TIME LIMIT FALSE; CREATE TAB
```

---

## Crash 312: `7657ad875f0ab793` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054798`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); INSERT INTO p WITH s AS (SELECT *) SELECT CAST(CAST(CAST(CAST(CAST(CURRENT_TIMESTAMP AS BLOB) AS BLOB) AS BLOB) AS BLOB) AS BLOB) AS a; PRAGMA integrity_che
```

---

## Crash 313: `204ff6e9a4c8021b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056296`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT OR ABORT INTO p VALUES (X'd07FFfAA08'); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 314: `c79041b5246d8c06` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056463`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); 
```

---

## Crash 315: `8092eefb1507d47b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066866`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); WITH RECURSIVE p (c3) AS (SELECT count(*) OVER (ORDER BY CURRENT_TIMESTAMP < CURRENT_DATE DESC)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 316: `7522f39b3fcc44bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066872`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); WITH RECURSIVE p (c3) AS (WITH s AS (SELECT *) SELECT nth_value(FALSE, TRUE) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND
```

---

## Crash 317: `7f663d772b23e0bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066881`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); WITH RECURSIVE p (c3) AS (SELECT rank() OVER (ORDER BY FALSE DESC ROWS BETWEEN CURRENT_DATE PRECEDING AND CURRENT_DATE FOLLOWING) AS g) SELECT * FROM p; CREATE TA
```

---

## Crash 318: `67d291557cb3bc0b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067018`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); WITH RECURSIVE p (c3) AS (SELECT CURRENT_TIME AND CASE WHEN NULL NOT NULL THEN -TRUE BETWEEN (-NULL) AND CURRENT_DATE ELSE CURRENT_TIME IS NOT NULL END AS j__mjf_
```

---

## Crash 319: `0f80d33167976ef6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067449`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT nth_value(FALSE, TRUE) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS 
```

---

## Crash 320: `a41ffcd1c95bf112` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077532`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (TRUE OR FALSE IS NULL COLLATE BINARY)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 321: `db6b653c1584cd85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077552`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP AND CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 322: `80dff05fa7ad4942` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077560`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 323: `353f700395c00aff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077583`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT FALSE || FALSE || CURRENT_DATE AS a FROM p JOIN p di ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 324: `b62fb5591194e714` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077598`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP | NULL)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 325: `cc1bb9b349722b45` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077748`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p (a) VALUES (CURRENT_TIME IS NOT NULL <= CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_
```

---

## Crash 326: `c1c0181996c19c4b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077779`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_DATE IS NULL)); INSERT INTO p WITH s AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM p; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 327: `33ccbbe2a527a5b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000077797`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (TRUE BETWEEN rowid AND CURRENT_TIMESTAMP) IS NOT NULL), a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 328: `56f52ba522b9b2c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078174`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT INTO p DEFAULT VALUES; VALUES (row_number() OVER (ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN CURRENT ROW AND NULL FOLLOWING)); CREATE TABLE seed_t1(c
```

---

## Crash 329: `94e3d9c658098e4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078207`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS (), w2 AS (PARTITION BY CURRENT_TIME ORDER BY NULL ASC ROWS BE
```

---

## Crash 330: `151d73b981160e53` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078215`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT -09400827019746681896075687267952595938039745359357778907617258045426795686136720321421516574859561330896465652953003736749125925708717059194732278997960955
```

---

## Crash 331: `103615d158bb9684` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078223`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT OR ABORT INTO p VALUES (json_valid(CURRENT_DATE)); VALUES (row_number() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 332: `e956ffe0a0747a8b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078236`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree(CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP COLLATE BINARY < NULL NOTNULL >= 0.0, '$') WHERE CURRENT_DATE GRO
```

---

## Crash 333: `24033809ff45e2ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078259`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP), * FROM p JOIN p di ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 334: `2fb2514d702c8ff8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078271`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME IN (-NULL))); INSERT INTO p DEFAULT VALUES; VALUES (row_number() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 335: `6d9b08a1f45297ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078281`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT json_remove('[{"a":1},{"b":2}]', '$.b[-0]') ORDER BY RAISE(IGNORE) DESC NULLS LAST; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 336: `1ef7d00c96aa71e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078402`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (FALSE OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT NULL IN (SELECT quote(TRUE) LIMIT NULL) AS v8a FROM json_tree('{"a":{"b":1}}') WHERE FALSE GRO
```

---

## Crash 337: `ced4e5c237eec5e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078411`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CAST(CAST(FALSE AS BLOB) AS BLOB) OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 338: `98f5a5f6d8a3ad2f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078443`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (FALSE OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p di ON CURRENT_DATE LIKE FALSE ESCAPE FALSE; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 339: `a7b2e4d8a0b57e5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078454`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (FALSE != NULL)); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 340: `42c17bae0af21156` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078582`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FAL
```

---

## Crash 341: `3ca83b902c47994f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p di ON CURRENT_TIME << CURRENT_TIME << CURRENT_DATE; CREATE 
```

---

## Crash 342: `6b1a6124b3548302` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078644`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT CAST(CURRENT_TIMESTAMP AS FLOAT) IN (SELECT quote(TRUE) LIMIT NULL) AS v8a 
```

---

## Crash 343: `6fd8b7c684f7e70c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078651`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT nth_value(FALSE, TRUE) OVER (), dense_rank() OVER (PARTITION BY NULL ORDER 
```

---

## Crash 344: `d5515f70ce2d1324` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078668`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM (VALUES (NULL)) AS s2ows2_88gep____u_o4t_90f__qbh_318b__0c_3_2_q__6_
```

---

## Crash 345: `7dd6075b06bf6314` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078685`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT OR ROLLBACK INTO p VALUES (TRUE IS TRUE); VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 346: `c36f6495b836fe5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078694`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIME * CURRENT_TIMESTAMP > CAST(CURRENT_DATE AS NUMERIC))); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 347: `34643406b647715d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078709`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 348: `ce8573cdf0eaa60e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078721`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP;
```

---

## Crash 349: `80753420d2d9bdb8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078731`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (CURRENT_TIMESTAMP > NULL OR CURRENT_DATE & CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 350: `952c140c3b34ee35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000078843`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 351: `b622097ca04e8d5f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079529`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT NOT EXISTS (SELECT * FROM json_tree('[1,2,3]')) AS a FROM p JOIN p di ON FALSE; CREATE TABLE seed_t
```

---

## Crash 352: `0bee0369dd9600c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000079546`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT rank() OVER () AS g FROM json_tree('[{"a":1},{"b":2}]'); CREAT
```

---

## Crash 353: `03ed413bb27f4725` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083637`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 354: `b1e0f10ac54a3b67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083646`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p ORDER BY CURRENT_TIME ASC, EXISTS (SELECT * LIMIT CURRENT_DATE) DESC NULLS LAST, CURRENT_TIMESTAMP; S
```

---

## Crash 355: `ee051ed88ee3009b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083659`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_tree(CURRENT_TIMESTAMP > CAST(CURRENT_DATE AS NUMERIC) OR CURRENT_DATE
```

---

## Crash 356: `161ef726d1ca887a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083669`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p JOIN p di ON CURRENT_DATE LIKE NULL ESCAPE '2'; CREATE TABLE seed_t1(c1 I
```

---

## Crash 357: `b75fde5aee4c7259` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083675`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH s AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM p; SELECT CURRENT_TIME % CURRENT_TIMESTAMP AS a; CREATE TABL
```

---

## Crash 358: `4498908c7cefad72` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083685`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (count(*) FILTER (WHERE NULL) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 359: `7c0a9890312b6a50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083699`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE NOT IN (WITH s AS (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM p)); PRAGMA integrity_check; CREATE TABLE seed_t
```

---

## Crash 360: `a22b15710109fda8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083726`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIME % X'd07FFfAA08' AS a; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 361: `5a6e1f7a7baca45d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIMESTAMP NOT BETWEEN FALSE || CURRENT_DATE COLLATE NOCASE AND FALSE AS a;
```

---

## Crash 362: `1424207861f232d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083745`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIME % dense_rank() OVER (PARTITION BY CURRENT_TIMESTAMP, NULL) AS a; CREA
```

---

## Crash 363: `01d359e108919cd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083754`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p (a) AS (VALUES (CURRENT_DATE)) VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIME % CURRENT_TIMESTAMP A
```

---

## Crash 364: `9d5016d0f3fa1c69` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000083854`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_TIME % CURRENT_TIMESTAMP AS a; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT
```

---
