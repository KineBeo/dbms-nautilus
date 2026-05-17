# Crash Triage Report

**Total crashes:** 362  
**Unique crash sites:** 362  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 161 | 161 | 44% |
| Signal | 201 | 201 | 55% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `590c24d534733a69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000215`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME IS NULL IS CASE CURRENT_TIME WHEN CURRENT_DATE THEN TRUE END IS NOT DISTINCT FROM CAST(TRUE COLLA
```

---

## Crash 2: `a8b6cef1592a6cb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000429`

```sql
SELECT substr('xDtD-', 2147483647, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES ((RAISE(IGNORE) AND CURRENT_DATE + CURRENT_DATE) * TRUE ISNULL ==
```

---

## Crash 3: `9da334553e6e2ff1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000567`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(c2 FLOAT GENERATED ALWAYS AS (CASE WHEN (TRUE IN (CURRENT_DATE)) REGEXP RAISE(IGNORE) < CURRENT_TIME < CURRENT_DATE = CURRENT_DATE
```

---

## Crash 4: `a1eee2576b5a9fea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000779`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT INTO q VALUES (~CURRENT_TIME, CURRENT_TIME ISNULL << NULL) RETURNING t2.*; SELECT CURRENT_TIMESTAMP FROM q WHERE EXISTS (SELECT * FR
```

---

## Crash 5: `83cc96153953fcdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000922`

```sql
SELECT printf('%s', -2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES ((NULL LIKE NULL >> RAISE(IGNORE) COLLATE RTRIM COLLATE NOCASE ESCAPE NUL
```

---

## Crash 6: `1a1330c05045c4d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001134`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 7: `8e75430a497a388f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001291`

```sql
SELECT printf('%lld', 2147483647, 'm__    _6 _N--_T'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO q VALUES (NULL, CURRENT_DATE NOT NULL * CURRENT_TIME -> TRUE IS NULL
```

---

## Crash 8: `a959ac330dacf906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001928`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT, b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 9: `07bff0847e3ef9d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001942`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 10: `3cf86c94737973a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001990`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 11: `f047472407eac043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002402`

```sql
SELECT printf('%llu', -2147483648, '-5_-e30h-n_scz l_o'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT 
```

---

## Crash 12: `2b7cfcb3b147d905` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002451`

```sql
SELECT printf('%f', 9223372036854775807, 'F_-W_7_K _ '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT c
```

---

## Crash 13: `becb2bf7d29f6212` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002482`

```sql
SELECT printf('%f', 9223372036854775807, 'F_-W_7_K _ '); CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA quick_c
```

---

## Crash 14: `c4f065fee6648855` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002535`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE AND TRUE); PRAGMA integrity_check; CRE
```

---

## Crash 15: `a86ab5907929d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002591`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 16: `cdf9efebe133114a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002991`

```sql
SELECT printf('%.*s', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 17: `604d86aad20f33e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003317`

```sql
SELECT round(1e308, 2147483647); SELECT printf('%.*d', -1, 1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(
```

---

## Crash 18: `1fa5fc6d50d3be4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003551`

```sql
SELECT printf('%.*g', 2147483647, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 19: `51037e4f0ab477b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003634`

```sql
SELECT round(0.01, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 20: `faec8666593f04a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004088`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 21: `0fcf42f5c84e5819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004166`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 22: `fbd9737303153d6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004258`

```sql
SELECT printf('%.*s', 9223372036854775807, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce
```

---

## Crash 23: `d29c9210d7c5e217` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004266`

```sql
SELECT printf('%.*s', 9223372036854775807, 0.01); SELECT substr('s9aQ- ---a-_ o', -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHER
```

---

## Crash 24: `c23fe584052fb8c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004462`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP IS NOT NULL, * FROM json_each(TRUE, '$[#-1]') W
```

---

## Crash 25: `f0fc4ca56b6907e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004470`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP IS NOT NULL, * FROM json_each(CASE TRUE WHEN CU
```

---

## Crash 26: `f53543ef208619dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004508`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 27: `3e77a19bb9b435d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004516`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_tree('{"a":1}') WHERE NOT CURRENT_TIMESTAMP IN (TRUE)
```

---

## Crash 28: `fb4ecf70688824ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004526`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN CURRENT_TIMESTAMP THEN FALSE < CU
```

---

## Crash 29: `279a0c1bd1550783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004532`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN CURRENT_TIMESTAMP THEN FALSE < CU
```

---

## Crash 30: `f604fc0a7c2a68c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004538`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN CURRENT_TIMESTAMP THEN FALSE < CU
```

---

## Crash 31: `373d5652f39de39f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004858`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) =
```

---

## Crash 32: `b78ec444aa3e04b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004871`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP IS NOT NULL, * FROM json_each('[{"a":1},{"b":2}
```

---

## Crash 33: `8457edd5fbd0e184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004877`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP IS NOT NULL, * FROM json_each('[{"a":1},{"b":2}
```

---

## Crash 34: `41a14d03822c92cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005053`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_DATE), c3 INTEGER); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 35: `dbd2b843eb60e42c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005398`

```sql
SELECT printf('%.*g', 1, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 36: `9f1dc114acc7dce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014567`

```sql
SELECT printf('%.*f', 1, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 37: `f5be2db149490e2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014587`

```sql
SELECT printf('%.*d', 1, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 38: `d0a3f686cae7cbf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014631`

```sql
SELECT substr(' G9_8I Rb1_Q- 35', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(le
```

---

## Crash 39: `df606e9027d052cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015046`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH p AS (SELECT *), q AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM json_each('[1,2,3]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 40: `e0043f3b5dbef026` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015569`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_tree('[1,2,3]') WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 41: `da3f789c42b8fdd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015575`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_each('{"a":{"b":1}}') WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 42: `cf3d33f4714d9094` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015599`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_tree('{}') WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 43: `c37e70619968ff40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015605`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 44: `e48787f60c2cda4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018140`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 45: `c4fcb1f48374fb02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018172`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT 0.0, c1 INTEGER); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE WINDOW w1 AS ()); CREATE TABL
```

---

## Crash 46: `de71089975f2ec1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018178`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 47: `36425cad6fcb5b1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018184`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE q AS (SELECT *) SELECT *; SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') W
```

---

## Crash 48: `31fec5bc9cd95206` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018191`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIME AS i8, CURRENT_DATE AS h_ele_8h97___9__9o__6a__o_q04
```

---

## Crash 49: `6654087af0b6b2b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018203`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 50: `b618ecb633abe1cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018210`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 51: `53d33f1a6b0750eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018221`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 52: `a7ad1bd8aacdcde0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018238`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT TRUE LIKE RAISE(IGNORE) ESCAPE NULL, * FROM json_each('[{"a":1},{
```

---

## Crash 53: `4dea66d538a36a05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018249`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (TRUE >> RAISE(IGNORE), CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIM
```

---

## Crash 54: `59cd05be67ac3859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018339`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 55: `4b23d14bf7c729e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018378`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS NULL COLLATE BINARY GROUP BY 
```

---

## Crash 56: `ea0a75dee871f816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018403`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_DATE IS FALSE GROUP BY CURRENT_TIME, CURRE
```

---

## Crash 57: `7b01f685f9a53777` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018456`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIME IN (NULL > CURRENT_TIMESTAMP OR CURRE
```

---

## Crash 58: `d5def9891dc413a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018699`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (TRUE || NULL)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 59: `c02f91f6121d0cb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018878`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT '  1 4oNx-T_-i'); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE TABLE seed_a(c U
```

---

## Crash 60: `4642b362dd80fa1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019224`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CURRENT_TIMESTAMP IS NOT CURRENT_DATE, '$[#-1]')
```

---

## Crash 61: `02bb072fdf6038ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019292`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CURRENT_TIMESTAMP IS NOT CURRENT_DATE, '$[#-1]')
```

---

## Crash 62: `04692b153e12093b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019369`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIME GROUP BY CURRENT_D
```

---

## Crash 63: `0d891f2bc50a3b55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019376`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIME GROUP BY NULL & CU
```

---

## Crash 64: `432dfb9a0e5afcbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020192`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(FALSE % CURRENT_TIMESTAMP IS NOT TRUE NOTNULL, '
```

---

## Crash 65: `7bd72293df8cc131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020225`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CURRENT_TIMESTAMP IS NOT TRUE NOTNULL, '$[#-1
```

---

## Crash 66: `7bc77437cbde0407` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020239`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{"a":1}') WHERE NULL; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 67: `8e36bd7a48952d20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020251`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CURRENT_TIMESTAMP IS NOT TRUE NOTNU
```

---

## Crash 68: `84dc3881ded831fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020271`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(NULL > -NULL IS NOT TRUE NOTNULL, '$[#-1]') WHER
```

---

## Crash 69: `9cc990a15b84a720` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020403`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE WHEN TRUE THEN CAST(CURRENT_TIMESTAMP NOT I
```

---

## Crash 70: `3fee87cf835c12a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020410`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE WHEN NULL << CURRENT_DATE THEN CAST(CURRENT
```

---

## Crash 71: `3111357b33ff73ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020470`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE WHEN NULL << CURRENT_DATE THEN CURRENT_TIME
```

---

## Crash 72: `56deb1ad61e6fc69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020515`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE WHEN TRUE THEN CAST(CURRENT_TIME AS TEXT) E
```

---

## Crash 73: `f4032da23fe20f76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020546`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE WHEN TRUE THEN CAST(CURRENT_TIME AS TEXT) E
```

---

## Crash 74: `304f4a1a8308c68f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021338`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIME GROUP BY CURRENT_TIME; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 75: `eea5a929b66ed15b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021345`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP > NULL)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 76: `ee471623cabbc58d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021352`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (last_insert_rowid(), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 77: `fb5197e9b3b66d60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021430`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (row_number() OVER (ORDER BY NULL DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE 
```

---

## Crash 78: `19b2d9642e9fdb50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021440`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (NULL > CURRENT_TIMESTAMP OR CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 79: `431ce6f8c3268599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021457`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CASE WHEN FALSE % CURRENT_TIMESTAMP THEN CURRENT_TIME >> FALSE END, NULL); CREATE TABLE seed_a(
```

---

## Crash 80: `0bf60a8b9c46ac45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021494`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 81: `803ee8564bb80f17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p V
```

---

## Crash 82: `df88d786c194d29d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021649`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (row_number() OVER (), NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 83: `a693f72d1af08af6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021692`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 84: `ee2184290c6a1c40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022038`

```sql
SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check;
```

---

## Crash 85: `18ec80b9a3993c94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022487`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 86: `8a808900ac92e9f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022506`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE NOT FALSE; CREATE TAB
```

---

## Crash 87: `b7e04716cbc974be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023278`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 88: `24a631e39bc025a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023848`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE, c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 89: `9196c34266ae28e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026613`

```sql
SELECT printf('%.*d', -1, 1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 90: `ef4c64526dfafc6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027843`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 91: `0392ae79c7431f19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029967`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO 
```

---

## Crash 92: `ae974ce6cc4f3d6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029982`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO 
```

---

## Crash 93: `c53d7077ce199713` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030021`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (rank() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c N
```

---

## Crash 94: `25fc84b00ff927d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032498`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRI
```

---

## Crash 95: `f547bc3f3936b88a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032536`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL DEFAULT -91581159521921808830.78E+528694); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE AND TRUE); PRAGMA integrity_c
```

---

## Crash 96: `99f90854ac5fe910` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032543`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE AND TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 97: `ab2a80b7111a7a6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032592`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP << CURRENT_TIMESTAMP AND TRUE); PRAGMA integrity_check; CREA
```

---

## Crash 98: `b903ad049abc1440` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032603`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(RAISE(IGNORE), '$[#-1]') WHERE dense_rank() OVER (PARTITION BY TRUE ORDER BY FALSE DESC NULLS 
```

---

## Crash 99: `7fb5a6c7c942d6dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE AND TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PR
```

---

## Crash 100: `54ca2fe43f28bb74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032797`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 101: `04fabf05f2ea200b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032869`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 102: `fe0aa2c212d2113f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033020`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 103: `ad0655e74b2a0858` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035398`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 104: `fb290a642d290917` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037548`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC DEFAULT X'a6deEd'); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 105: `a569d7b84ea4b163` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037554`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 106: `d395640ce483310a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037569`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c 
```

---

## Crash 107: `956fe1aa002e1850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037595`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (TRUE = TRUE), b VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TA
```

---

## Crash 108: `a607011c7ecac0a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037603`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (FALSE MATCH CURRENT_TIME), c3 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 109: `df9ee1a8b1a00891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039404`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a FLOAT NOT 
```

---

## Crash 110: `d6b76b041d0d5deb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040751`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NA
```

---

## Crash 111: `13ea5a0f64ce848f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040842`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREA
```

---

## Crash 112: `681835ae8fb8563b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042442`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE TRUE NOT IN (NULL) = TRUE COLLATE BINARY IS NULL); EX
```

---

## Crash 113: `4f52da0f1b228eb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042469`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); SELECT * FROM p WHERE EXISTS (SELECT * FROM js
```

---

## Crash 114: `5fbe9210a4e75734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042484`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 115: `392a910005d2dcd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042506`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (TRUE = TRUE)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 116: `21504b33242a9d9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042526`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); EXPLAIN QUERY PLAN VALUES (count(*), CURRENT_T
```

---

## Crash 117: `41f11b9e1fbf1737` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042675`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); REPLACE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE
```

---

## Crash 118: `617b7a619f9a0f58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042813`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); WITH q AS (VALUES (CURRENT_TIMESTAMP)) INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_
```

---

## Crash 119: `a04d60ced235f26a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045580`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM q ORDER BY NULL ASC NULLS FIRST LIMIT TRUE; CREAT
```

---

## Crash 120: `9049d3b14542f843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046147`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY 
```

---

## Crash 121: `3799be0554becb59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048504`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME GLOB CURRENT_TIME); PRAGMA integrity_check; CREATE 
```

---

## Crash 122: `bbbbf2b355d6ca7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048515`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (-TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 123: `5e1b019a0c0bec1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048568`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO q VALUES ((SELECT DISTINCT * FROM q AS s_64____8lfh__0m_e351695_s94__c_l_189w___856y_
```

---

## Crash 124: `1d12af0f2d5f2537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053338`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE, * FROM p NOT INDEXED WHERE CURRENT_TIME ORDER BY FAL
```

---

## Crash 125: `36e6e99b3f39b998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057105`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(NULL, '$') WHERE TRUE GROUP BY NULL WINDOW w1 AS ()); CREATE TABLE IF NOT
```

---

## Crash 126: `f9cc90dab988c79b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057233`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT * FROM json_tree('[1,2,3]') WHERE TRUE GROUP BY NULL WINDOW w1 AS ()); CREATE TABLE IF NOT
```

---

## Crash 127: `ed75d0bfff43f71d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057840`

```sql
SELECT printf('%f', 9223372036854775807, 'F_-W_7_K _ '); CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME AND TRUE
```

---

## Crash 128: `c0661a93bee2ba75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057859`

```sql
SELECT printf('%f', 9223372036854775807, 'F_-W_7_K _ '); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE TRUE
```

---

## Crash 129: `62706edb81333480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058170`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (json_remove('[{"a":1},{"b":2}]', '$.key')); PRAGMA integrity_check; CREATE TAB
```

---

## Crash 130: `44b32aa942436813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058188`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (json_remove('[{"a":1},{"b":2}]', '$')); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 131: `a877ea460a6f84de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058562`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE); CREATE T
```

---

## Crash 132: `ac8a0b11c9d5f9ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058568`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY 
```

---

## Crash 133: `ff69dfa3bbb3ace0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058586`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMAR
```

---

## Crash 134: `794cac618292cafd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058722`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KE
```

---

## Crash 135: `2ccda71089a32ea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059236`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRI
```

---

## Crash 136: `a19d8e57bc740d5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059297`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRI
```

---

## Crash 137: `5ed307ec403ac539` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059450`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 138: `e48a234967b43179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061543`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_each('{"a":1}') LEFT OUTER JOIN json_tree('[1,2,3]') ON F
```

---

## Crash 139: `d29a65624f61b428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062262`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (rank() OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST, CURRENT_TIMESTAMP DESC NULLS FIRST)); CREATE TABLE seed
```

---

## Crash 140: `0593e36f8790d9b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062281`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (rank() OVER (ORDER BY FALSE DESC NULLS LAST ROWS BETWEEN RAISE(IGNORE) PRECEDING AND CURRENT_TIMESTAMP FOLL
```

---

## Crash 141: `d552913e715e3330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062295`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (percent_rank() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 142: `ca9da206057a80bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062315`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (rank() OVER (PARTITION BY TRUE ORDER BY FALSE DESC NULLS FIRST)); CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 143: `f2ab1467a238f21f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062709`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO 
```

---

## Crash 144: `0a3dfb198bd459e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062731`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q INDEXE
```

---

## Crash 145: `6a862d2ca624fb71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062869`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO 
```

---

## Crash 146: `b781390cc5e23eac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064596`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); INSERT INTO p VALUES (' ') ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = 
```

---

## Crash 147: `0828f4b42afd23a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064613`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (CURRENT_TIME), b NUMERIC CHECK (NOT CURRENT_TIMESTAMP IN (TRUE))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; C
```

---

## Crash 148: `866e3fc9dc369dff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068523`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM json_each('{"a":1}') NATURAL LEFT JOIN json_each('{}') NATURAL JOIN (p AS i);
```

---

## Crash 149: `313b08e0556f2553` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068543`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM json_each('{"a":1}') NATURAL LEFT JOIN json_each('{}') NATURAL JOIN (json_eac
```

---

## Crash 150: `e1ed41142d78eba9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068559`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 151: `83e41be5ae2668a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071645`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (CURRENT_DATE NOT BETWEEN TRUE AND FALSE); SELECT * FROM p JOIN p vm1 ON CURRENT_T
```

---

## Crash 152: `e21a3a7e4c97c79a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071671`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); SELECT * FROM p JOIN p vm1 ON X'd7F52f'; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 153: `111224bee1e6d09c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071688`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC DEFAULT -0129928435.2); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (FALSE); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TA
```

---

## Crash 154: `26dbcecfa347e624` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); VALUES (changes()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SE
```

---

## Crash 155: `3912a8de669c6d75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071799`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); SELECT X'1A' FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_a(
```

---

## Crash 156: `cea2fa9cd58d8495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071847`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL > CURRENT_TIMESTAMP OR CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRE
```

---

## Crash 157: `76e70b4b9072aa9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071880`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT 400); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 158: `c0f0ea18976e8fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071887`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME ORDER BY FALSE
```

---

## Crash 159: `782465b28f1202e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL NOT IN (FALSE, CURRENT_TIME, TRUE))); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURREN
```

---

## Crash 160: `0af46759943b1d6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071953`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT 95656.541261216889453364407355822E-0893156296); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE
```

---

## Crash 161: `ccdcb1a1bccd2ca2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072830`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE GROUP BY
```

---

## Crash 162: `361160ec0a8a6b43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000000097`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 163: `ca9fa72bcaf22603` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001801`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 164: `3f4d8b9b6a276ec4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001839`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT CURRENT_TIME, b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABL
```

---

## Crash 165: `c3cc76d321770dc6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002357`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 166: `bb41e70ee388d524` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002519`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 167: `2ae5846da3fe91d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002571`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREA
```

---

## Crash 168: `355945fa66f90182` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003310`

```sql
SELECT round(1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 169: `4766bf3451fcff6a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003336`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 170: `310fbdc928fb1d92` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004021`

```sql
SELECT printf('%.*f', 0, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 171: `a996908d22a25353` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004153`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 172: `b2d55b7508c9d6da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004368`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 173: `9df8f8e9e5901687` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004730`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) =
```

---

## Crash 174: `75da0dd4e489992f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005472`

```sql
SELECT printf('%.*g', 0, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 175: `4bf5353e7b167728` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005529`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT * FROM jsonb_each('[1,2,3]') LEFT OUTER JOIN (json_tree('{"a":{"b":1}}') INNER JOIN jsonb_
```

---

## Crash 176: `4320a3d03acd4a9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005569`

```sql
SELECT substr('e- a A_ 4', -2147483649, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 177: `5dba5b370ea79056` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005678`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 178: `427c40e9abaacd9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005690`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (CURRENT_TIME) * CURRENT_TIMESTAMP NOT NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 179: `36057c5181dd20f6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005712`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); I
```

---

## Crash 180: `e996da3644198575` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005728`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (CURRENT_TIME == TRUE NOT IN (VALUES (CURRENT_TIMESTAMP))) * CURRENT_TIMESTAMP NOT NULL; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 181: `307468ab64a109f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005750`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (CURRENT_TIME == NULL) * CURRENT_TIMESTAMP NOT NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 182: `d71590931445be8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005772`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (NULL) * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 IN
```

---

## Crash 183: `6622fbc466b30fc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006203`

```sql
SELECT printf('%.*g', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 184: `c9217acf9c3a77a7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011406`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP > NULL), c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 185: `9da81824b6c2b9d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011419`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL MATCH CURRENT_TIME)); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 186: `24fa9842e1f0f580` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011436`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_DATE, c1 DATE); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 187: `3d20c057754fdbbd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011448`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_DATE IS RAISE(IGNORE))); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 188: `3a86cdf46b9784af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011474`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT CURRENT_TIME AS i8, CURRENT_DATE AS h_ele_8h97___9__9o__6a__o_q04x0_2__5_9a_qwk30896__72084fix67a9_mc__s_z_t_7____7c43__28m8__3_390_v__26a56_y_
```

---

## Crash 189: `4e2ee39a6bd2e899` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011499`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (RAISE(ROLLBACK, ''))); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 190: `b33bab243fcc0bbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011505`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CASE TRUE WHEN TRUE THEN FALSE < CURRENT_DATE ELSE CURRENT_TIMESTAMP IS NOT FALSE END; CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 191: `1d94fd6917592fd9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011513`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT NOT NULL DEFAULT -91581159521921808830.78E+528694, c1 INTEGER UNIQUE); SELECT * FROM p JOIN p vm1 ON CURRENT_TI
```

---

## Crash 192: `ef75f0b1aae4aa8c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011545`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT p.* FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 193: `0c44d83f3bdb9a88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011591`

```sql
CREATE TABLE IF NOT EXISTS p(a INT DEFAULT -0); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 194: `a3d2259305ed2441` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011608`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CR
```

---

## Crash 195: `18bc08180495bf5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011650`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT CURRENT_TIME GLOB FALSE - CURRENT_DATE IS NOT -FALSE COLLATE BINARY FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 196: `3a894ab4306f9067` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011690`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT FALSE - CURRENT_DATE IS NOT FALSE COLLATE BINARY FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 197: `0deeaacc00a3863c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011756`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT CURRENT_TIME GLOB CURRENT_TIME IS NOT -FALSE COLLATE BINARY FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 198: `820bf11d49f394c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011769`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT -FALSE COLLATE BINARY FROM p JOIN p vm1 ON CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CR
```

---

## Crash 199: `052a8592c7363ea8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011825`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON FALSE < CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t
```

---

## Crash 200: `e1a47a246e692967` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011833`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); 
```

---

## Crash 201: `319307ba07b0be86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011882`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT CURRENT_TIMESTAMP << CURRENT_TIMESTAMP AS i8; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 202: `eca3c85454a7b624` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011890`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT FALSE IS CURRENT_TIMESTAMP << ~TRUE AS i8 FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 203: `61ef81079c72db1c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011920`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP IS NOT FALSE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 204: `5185503cd41b482b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011936`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * +CURRENT_TIMESTAMP IS NOT NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 205: `6815442550fc99b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011944`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 206: `65ec59e9c52d2ba4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011950`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP > TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 207: `db5ed4c3774f10fd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011957`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT CURRENT_TIME AS i8, CURRENT_DATE AS h_ele_8h97___9__9o__6a__o_q04x0_2__5_9a_qwk30896__72084fix67a9_mc__s_z_t_7____7c43__28m8__3_390_v__26a56_y_
```

---

## Crash 208: `831e7347de2442a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011981`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * FALSE << TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 209: `37a3759cb89c13d7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011988`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL DEFAULT -91581159521921808830.78E+528694); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 210: `402d17796b888a08` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012041`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT DEFAULT FALSE); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 211: `551973a172f9f190` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012050`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT +(NULL) < CURRENT_DATE NOTNULL LIKE NULL IS NOT NULL NOT NULL IN (CURRENT_TIMESTAMP + TRUE ISNULL COLLATE RTRIM ISNULL) COLLATE NOCASE IN (CURR
```

---

## Crash 212: `bbf872ecdc8a428d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012075`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT -6998.130e83591951524916346032585700280915533959221312324798458127280336711005443159008902353598653967089447981766630803890098827501720081705166966
```

---

## Crash 213: `147018fc5374383e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012099`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * 
```

---

## Crash 214: `a26b6d43c6db5e21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012107`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRE
```

---

## Crash 215: `ad1872942fb0ea75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012627`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE CURRENT_DATE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 216: `24996a0176392d60` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012655`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE NOT FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 217: `8e240c8a1eb5d50c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012673`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON NOT FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGE
```

---

## Crash 218: `8a51486882e8b737` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012689`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP MATCH FALSE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 219: `651e205d3acc9ed5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012695`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE NOT CURRENT_DATE MATCH FALSE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 220: `0d2c705181ebc057` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012701`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE NOT TRUE AND CURRENT_TIMESTAMP MATCH FALSE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 221: `06de39e70f1d8be2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012707`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME NOT LIKE NOT NULL AND FALSE AND CURRENT_TIMESTAMP MATCH FALSE * CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 
```

---

## Crash 222: `c0f16855e857b6d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012792`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP IS NOT FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 223: `586b4ddf96cc7897` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (NULL MATCH CURRENT_TIME), b NUMERIC CHECK (CURRENT_TIME)); SELECT * FROM p JOIN p vm1 ON NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 224: `b1f99a4dc74468b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012874`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY, a BLOB UNIQUE); SELECT * FROM p JOIN p vm1 ON NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 225: `e83b71d3066b4cdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012886`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIME >= CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 226: `3cbbf3454e35b0f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012904`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE | FALSE << ~NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 227: `d56537fa64595da9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012912`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (NOT CURRENT_DATE < TRUE GLOB TRUE) + CASE TRUE WHEN +CURRENT_TIMESTAMP IS NOT NULL THEN TRUE END / TRUE; CREATE TABLE s
```

---

## Crash 228: `8c093fa40c8a0191` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012919`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (NULL) = TRUE COLLATE BINARY IS NULL COLLATE NOCASE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 229: `8d3a88818e439bd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012928`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_DATE, c1 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) INTERSECT SELECT * FROM t3 AS a WHERE CURRENT_DATE ORDER BY NULL ASC, NULL
```

---

## Crash 230: `f3e7916f4e480c20` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012934`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC DEFAULT X'a6deEd', rowid FLOAT PRIMARY KEY); SELECT * FROM p JOIN p vm1 ON NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 231: `f69d5a696a93f08e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012945`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON NULL * CURRENT_TIME ISNULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 232: `f5de167718d33b71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012974`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT TRUE); SELECT * FROM p JOIN p vm1 ON NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 233: `0d1e875a86e9f9e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012991`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); SELECT * FROM p JOIN p vm1 ON NULL * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 I
```

---

## Crash 234: `ad50a7418492da63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013017`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON '  B-3-fS k -_7G-_3O' * TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 235: `569b95839e3c754a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013119`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON '  B-3-fS k -_7G-_3O'; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 236: `9fea13b759bdda7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013197`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON (WITH p AS (SELECT *) VALUES (CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 237: `d4968a48c9c70b7b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013237`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON FALSE IS NULL COLLATE NOCASE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 238: `88226173bff03752` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013251`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (NULL) = CURRENT_TIMESTAMP COLLATE NOCASE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 239: `6f60b2272fdda1bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013259`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON NULL IS NULL COLLATE NOCASE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 240: `e40b29c9a8404072` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013363`

```sql
SELECT printf('%.*g', 2147483648, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 241: `313bdb6028704552` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013379`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM jsonb_tree('{"a":1}') JOIN json_each('{"a":{"b":1}}') USING (rowid, c2) ORDER BY CURRENT_TIMESTAMP 
```

---

## Crash 242: `37416e771442a63d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013422`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 243: `4ea9b0b3be5733e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013441`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('[1,2,3]') WHERE CURRENT_TIMESTAMP GROUP BY FALSE WINDOW w1 AS () INTERSECT SELECT *; INSERT INTO
```

---

## Crash 244: `7a2a040b9837e6f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013459`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM r INDEXED BY a ORDER BY CURRENT_TIME DESC NULLS LAST LIMIT NULL; SELECT * FROM p JOIN p vm1 ON TRUE NO
```

---

## Crash 245: `7e049b3c7bd69aee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013495`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON ''; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INS
```

---

## Crash 246: `9de918b85c858014` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013535`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (VALUES (CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 247: `946a98ade59f2c4c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013559`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VALUES (CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 248: `a546129600a456ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013566`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN (VALUES (CURRENT_TIMESTAMP)) NOT IN 
```

---

## Crash 249: `d158ef7c9d57e34f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013636`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON TRUE NOT IN (SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME ORDER BY FALSE ASC NULLS FIRST); CREATE TABLE seed_
```

---

## Crash 250: `40d4f79c414a5378` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013666`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT NULL NOT IN (VALUES (FALSE)) AS h_ele_8h97___9__9o__6a__o_q04x0_2__5_9a_qwk30896__72084fix67a9_mc__s_z_t_7____7c43__28m8__3_390_v__26a56_y_6z3p
```

---

## Crash 251: `645abeec98ee4d02` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013718`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm1 ON CURRENT_TIMESTAMP IS NOT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 252: `41e571a62cd7f5f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013885`

```sql
SELECT substr('e- a A_ 4', -2147483649, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 253: `c52a622d44884156` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013892`

```sql
SELECT substr('', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREA
```

---

## Crash 254: `52966c3e9e92a103` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013900`

```sql
SELECT substr('e- a A_ 4', -1, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 255: `3f945313537714af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013907`

```sql
SELECT substr('e- a A_ 4', -2147483649, 4294967296); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 256: `b1fca720931ab737` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013914`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 257: `2124730eba15392e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013921`

```sql
SELECT round(-1.0, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 258: `a2ec076c64f873f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013931`

```sql
SELECT substr('e- a A_ 4', 4294967296, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 259: `b7a332acc958c2da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013962`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 260: `c24d369d7d90abe9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013982`

```sql
SELECT printf('%x', 4294967296, 'lY-_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 261: `9c1f6aba63ad80aa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014021`

```sql
SELECT printf('%.*e', -1, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 262: `2bceb8f63f87a2f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014226`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT * FROM jsonb_each('[1,2,3]') LEFT OUTER JOIN (json_tree('{"a":{"b":1}}') INNER JOIN jsonb_
```

---

## Crash 263: `c17a3d9503ca7de5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014282`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT * FROM jsonb_each('[1,2,3]') LEFT OUTER JOIN (p NOT INDEXED) GROUP BY RAISE(IGNORE) ORDER 
```

---

## Crash 264: `741a16e0164fb95d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014410`

```sql
SELECT printf('%.*s', 0, 1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 265: `36c71dfc035f541c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014417`

```sql
SELECT printf('%.*g', 0, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 266: `b132628365fe196f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014431`

```sql
SELECT substr('', 4294967296, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55
```

---

## Crash 267: `fe9f4c7c620415f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014455`

```sql
SELECT round(-1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 268: `32b590506c3debed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000014463`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE T
```

---

## Crash 269: `757acfecd803ffd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018938`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE, b FLOAT UNIQUE, a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE T
```

---

## Crash 270: `0e9bd9d15422503d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018975`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN TRUE THEN FALSE < CURRENT_DATE EL
```

---

## Crash 271: `6779d76b0eb3f361` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018984`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE CURRENT_TIME <= CURRENT_DATE WHEN TRUE THEN
```

---

## Crash 272: `089ec74dfeaf0366` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019014`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN TRUE THEN TRUE NOT IN (SELECT DIS
```

---

## Crash 273: `94cb4478008f2346` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019025`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count())); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 274: `6cda7db5317f0d4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019124`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each(CASE TRUE WHEN TRUE THEN FALSE < CURRENT_DATE EL
```

---

## Crash 275: `ed8fca95bb9746f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000019155`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME ORDER BY FALSE A
```

---

## Crash 276: `de6f9cb1aedebb42` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 277: `8ca314ff8d365140` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021408`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JOIN p vm
```

---

## Crash 278: `ff1f91ed6a46f98d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024837`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE, b INT, c3 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (CURRENT_TIME, FALSE << TRUE, TRUE); PRAGMA integrity
```

---

## Crash 279: `d9a0f0dd424331b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024848`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC CHECK (rowid)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 280: `7b39e912c8636517` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024971`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); SELECT * FROM p JO
```

---

## Crash 281: `3c0751b6615c30a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030995`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY TRUE ORDER BY FALSE ASC RANGE 
```

---

## Crash 282: `73c186dff6997dd5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032263`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 283: `90a2484ba47ca105` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032271`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('{"a":1}') GROUP BY last_insert_rowid() OVER (PARTITION BY CURRENT_DATE, NULL); INSERT OR FAI
```

---

## Crash 284: `4f2c5bf97e9cf3e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032289`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE, *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 285: `9881ca2dde639774` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032298`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 286: `6fbea640a03b2aa1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA integrity_check; CREATE TABL
```

---

## Crash 287: `b103ce568558b0f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032313`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT FALSE IS CURRENT_TIMESTAMP << ~TRUE AS i8; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check;
```

---

## Crash 288: `d0993ccff7b9d5ef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032334`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT FALSE IS CURRENT_TIMESTAMP << ~TRUE AS i8, dense_rank() FILTER (WHERE RAISE(IGNORE)) OR RAISE(IGNORE) & NULL NO
```

---

## Crash 289: `3022c00a3d92510c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032340`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT TRUE LIKE RAISE(IGNORE) ESCAPE NULL; INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREAT
```

---

## Crash 290: `06e4718a7bc253d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032346`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME NOT BETWEEN CURRENT_DATE AND CURRENT_DATE); PRAGMA integrity_
```

---

## Crash 291: `32231b0050c82f46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032357`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); VALUES (count(DISTINCT CURRENT_DATE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 292: `aec6fd6a4c71ea29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032760`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 293: `9d28f34b7bf631e7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032768`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 294: `df553045f5b3bcc6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032812`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 295: `e99e62087677eefe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000032922`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 296: `9af4c6e78bd730ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034914`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT OR IGNORE INTO p VALUES (-3413394037515171483478886.521648877646077968232E-4); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 297: `fc7a9f2331377daf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035374`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM p NATURAL JO
```

---

## Crash 298: `d90342c7f5e0b012` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038079`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 299: `eecb9ce438e343fd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040713`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (-CURRENT_DATE >> FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 300: `43a9c194bb4c19ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041992`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT CURRENT_DATE, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 301: `ad1ab1118321005e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042000`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (TRUE NOT IN (NULL) = CURRENT_DATE IS NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE see
```

---

## Crash 302: `6a549a73502775b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042018`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIME), b NUMERIC CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE
```

---

## Crash 303: `edbd66d484b677e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042025`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (FALSE < CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 304: `7dc3ea96656b251f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042067`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (_rowid_)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 305: `a31d48145d6392ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042107`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (c3)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 306: `b6d0078b01d3b700` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043465`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (TRUE NOT IN (NULL) = CURRENT_DATE IS NULL COLLATE NOCASE >> FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 307: `3177db48c6fc0814` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043498`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE NOT BETWEEN TRUE AND FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 308: `ee55b540b4190e68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043504`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE), a VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 309: `6a0cfeaf95655e51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043521`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (-p._rowid_ >> FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 310: `e177e3ad4530183b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043562`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_TIMESTAMP >> FALSE)); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 311: `7b141b3d2fc4217c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043571`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT 4939.6e583184042253769958734209505710882678192416228109510629528180445610406423261640406331374733601596978132); CREATE INDEX IF NOT EXISTS idx1 ON
```

---

## Crash 312: `75425b6b7d754811` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043661`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_TIMESTAMP >> FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_TIMESTAMP >> FAL
```

---

## Crash 313: `1ee11b0a63cab7f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043704`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (-p._rowid_)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 314: `2e9dfe02f26283de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043780`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (-CURRENT_TIMESTAMP IS NOT TRUE NOTNULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 315: `13f80333a8e883e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047681`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (CURRENT_TIME), b NUMERIC CHECK (CURRENT_TIME IN (TRUE))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TAB
```

---

## Crash 316: `d450a4207d3a6626` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053090`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION ALL SELECT * FROM jsonb_each('[1,2,3]') GROUP BY count(DISTINCT TRUE) FILTER (WHERE TRUE) ORDER BY NU
```

---

## Crash 317: `08c5329143864cb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053099`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM q NATURAL JOIN p WHERE CURRENT_DAT
```

---

## Crash 318: `336539a645398759` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053113`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT CURRENT_DATE, rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM p 
```

---

## Crash 319: `93912b99ed95251f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053125`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 320: `e0d3f24cebeaee61` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053132`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); VALUES (total_changes()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 321: `b0040ef4acc1abe9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053159`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT, c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM p NATURAL JOIN p W
```

---

## Crash 322: `d809e19d14998c34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053175`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT 0.0, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT TRUE AS ud6e0_6_31t1_3y4t__6o7p1l_r5675_56_9____2_25m_9 FROM p NATURAL JOIN p W
```

---

## Crash 323: `30e1cbeeca842e58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053283`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 324: `8ce0cac3ebd1352e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053934`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p SELECT * FROM p WHERE CURRENT_DATE GROUP BY NULL IS NOT NULL, NULL > FALSE WINDOW w1 AS (); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TA
```

---

## Crash 325: `1ee75379ebd8e2a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054320`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 326: `03908a662c369815` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054326`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 327: `d8a0519984147900` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054396`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (CURRENT_TIME IN (CURRENT_TIME NOT IN (last_insert_rowid())))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CRE
```

---

## Crash 328: `b8f6e1b1e670692b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054473`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p VALUES (CURRENT_DATE) UNION SELECT CURRENT_TIME AS i8 FROM json_tree('[]') WHERE NULL ORDER BY CURRENT_TIME ASC NULLS FIRST; EXPLAIN QUERY PLAN
```

---

## Crash 329: `9f9aa8a0901a9a3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054630`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC DEFAULT X'a6deEd'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 330: `9cc0c98c5d59a4c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054852`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (-78.8742900006471904453073282629 < CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 331: `7369a665f206c5b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055249`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL SELECT CURRENT_TIME AS u_jn__4znht4347_73_a ORDER BY CURRENT_TIME ASC NULLS FIRST; EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 332: `3feb4d73783c69e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058236`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p NOT INDEXED WHERE FALSE BETWEEN NULL AND CURRENT_DATE GROUP BY CURRENT_TIMESTA
```

---

## Crash 333: `ea874ae8b5e511bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058245`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CUR
```

---

## Crash 334: `b9f18626bb45058b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT 8403993661087250125007475.98674); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TA
```

---

## Crash 335: `237d52b352e21fd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058285`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KE
```

---

## Crash 336: `2151fe258baf5aec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058450`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_DATE); PRAGMA integrity_check; CREATE TA
```

---

## Crash 337: `67d9958c6081711f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058456`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * TRUE); PRAGMA integrity_check; CR
```

---

## Crash 338: `01611ad29e59b6e5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058472`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CUR
```

---

## Crash 339: `b9ca2d62d7d79264` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058478`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXIS
```

---

## Crash 340: `0eccc203cd486f54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058775`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 341: `bf0511a845d3dc59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058782`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 342: `042f0f116fdf4f7a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058819`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 343: `3139317f6329a0c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058851`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (CAST(json_patch('[1,2,3]', '[1,2,3]') AS INTEGER))); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TA
```

---

## Crash 344: `ce9bca40e82c23e1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058892`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREA
```

---

## Crash 345: `8c29dfa52daf8ee6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000059119`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 TEXT CHECK (CURRENT_TIME), b NUMERIC CHECK (CURRENT_TIME IN (FALSE, CURRENT_TIME, TRUE))); INSERT OR FAIL INTO p VALUES (CURRENT_T
```

---

## Crash 346: `758a02f634b576b9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060726`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY TRUE ORDER BY FALSE ASC RANGE 
```

---

## Crash 347: `aef60f21e30be9b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060749`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT 4939.6e583184042253769958734209505710882678192416228109510629528180445610406423261640406331374733601596978132); CREATE INDEX IF NOT EXISTS idx1 ON
```

---

## Crash 348: `6bb6eb1a8189aa4d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (ORDER BY TRUE ASC NULLS LAST ROWS BETWEEN C
```

---

## Crash 349: `82fee4d48667d6b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060766`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (RAISE(IGNORE) <> CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE 
```

---

## Crash 350: `33a733e93b02e829` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060778`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY NULL NOT IN (SELECT CURRENT_TIME AS u_jn__4znht4347_73_a LIMIT NULL) WINDOW
```

---

## Crash 351: `f723ccba3e9009f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060788`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT *, *, * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY TRUE ORDER BY FALSE ASC 
```

---

## Crash 352: `29827008bc9d9062` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060797`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]')) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 353: `1cb901ca34191992` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060803`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY TRUE ORDER BY FALSE ASC ROWS B
```

---

## Crash 354: `53ea372258a59877` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060909`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT * FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 355: `6cee365cc5e22eac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061631`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 356: `45714b1ac82cdf29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068175`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY percent_rank() FILTER (WHERE FALSE) OVER (ORDER BY FALSE DESC NULLS LAST ROWS BETWEEN RAISE(IGNO
```

---

## Crash 357: `71db1d22e9b100c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068210`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(b NUMERIC CHECK (CURRENT_TIME IN (CURRENT_TIME NOT IN (last_insert_rowid() NOT IN (TRUE))))); INSERT INTO p DEFAULT VALUES; PRAGMA qu
```

---

## Crash 358: `0d5da14e6cb34788` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068952`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_TIME AND NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 359: `863998f1837f02af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073073`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_DATE GROUP BY 
```

---

## Crash 360: `1f0cf5f1f614d71d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073109`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE G
```

---

## Crash 361: `36168bc2d59672f6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000073246`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR FAIL INTO p VALUES (FALSE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_DATE GROUP BY 
```

---

## Crash 362: `23d4b10443388708` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000074655`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIME AS i8 FROM json_each('[1,2,3]') , json_eac
```

---
