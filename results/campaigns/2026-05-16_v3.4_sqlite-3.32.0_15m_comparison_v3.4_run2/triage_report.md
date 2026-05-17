# Crash Triage Report

**Total crashes:** 359  
**Unique crash sites:** 359  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 187 | 187 | 52% |
| Signal | 172 | 172 | 47% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `676157563077a040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_); INSERT INTO q VALUES (TRUE COLLATE BINARY REGEXP CURRENT_TIME NOTNULL LIKE CASE WHEN CASE CURRENT_DATE NOT IN (FALSE, CURRENT_DAT
```

---

## Crash 2: `c620fdc18de44c9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000423`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c3, a, c3, c1, c2, c2); EXPLAIN QUERY PLAN SELECT ALL q.*, (NOT EXISTS (SELECT p.* FROM p NOT INDEXED WHERE CASE FALSE NOTNULL WHEN FALSE TH
```

---

## Crash 3: `add40b909b294860` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001048`

```sql
SELECT substr('L_ s35- xte-_', -9223372036854775808, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALUES (FALSE <> CURRENT_TIMESTAMP OR TRUE OR RAISE(IGNORE), C
```

---

## Crash 4: `1b78f673efd4db3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001309`

```sql
SELECT round(1e-308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, b, c2, c1); SELECT CASE WHEN CURRENT_DATE COLLATE BINARY THEN NOT TRUE ELSE NULL END MATCH EXISTS (SELECT *) NOT IN
```

---

## Crash 5: `a08c7b3b0285f760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001456`

```sql
SELECT printf('%.*s', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p (a) AS NOT MATERIALIZED (VALUES ((VALUES (RAISE(IGNORE)
```

---

## Crash 6: `74740285ca25564e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001684`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 7: `089cba0ba5199bec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001902`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p
```

---

## Crash 8: `bef0bf3bb28b93db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002110`

```sql
SELECT printf('%.*f', 0, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 9: `08967775719fd463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002496`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 10: `f812ca20a984457a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 11: `df1bdc50fc65a0ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002998`

```sql
SELECT printf('%x', 4294967295, '_ ___B2TvzE 4n-x  '); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coa
```

---

## Crash 12: `ec762fb602640dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003185`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 13: `8e020e79700b2519` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003263`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 14: `ba7e83cc9376e772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003432`

```sql
SELECT printf('%.*e', 1, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 15: `b6f71e4f14a71732` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003545`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UN
```

---

## Crash 16: `697a199158ef7531` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003551`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE COLLATE NOCASE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 17: `75f19ffd6998fa17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003557`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (TRUE)) << FALSE COLLATE NOCASE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 18: `392d29befcd5d3c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003564`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (TRUE)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_
```

---

## Crash 19: `0c7057d50cb14c67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003570`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 20: `4c439875cddaaa76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003578`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE TRUE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL
```

---

## Crash 21: `a8b4263fe0045b40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003590`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_
```

---

## Crash 22: `37dc460a1daed79b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003615`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE << FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 23: `8b98f69055a87a09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003624`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURA
```

---

## Crash 24: `a66ebe7660f44443` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003725`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -TRUE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 25: `7b496a53be82b278` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003744`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIMESTAMP < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 26: `8332bb71a24b2e41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004185`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p 
```

---

## Crash 27: `6c7c7fd6b16aa9a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004193`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT q.*, * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT I
```

---

## Crash 28: `95fffd1a10a3cc7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004199`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT q.*, * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN 50 COLLATE NOCASE END; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 29: `b686353e45ec086b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004260`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN CURRENT_DATE THEN 50 COLLATE NOCASE END; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 30: `a15d034fafba39bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004780`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 31: `296671eb7cded282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004846`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 32: `95a4d654c48c440b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005568`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME)); PRAGMA integrity_check; CREATE
```

---

## Crash 33: `38157614ed588f57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005574`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME NOT IN (CURRENT_TIME)); PRAGMA integrity_check; CREATE 
```

---

## Crash 34: `d2a8b86064f66729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005580`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 35: `fb60d63752863c6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005586`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 36: `24541f331b58a006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005955`

```sql
SELECT printf('%.*g', -2147483648, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 37: `af9093533ef54766` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006103`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL * FROM json_tree('[]') ORDER BY TRUE DESC NULLS LAST, TRUE ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 38: `d14be2d24f3d6817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007807`

```sql
SELECT substr('', 2147483648, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP ->> TRUE / FALSE AND TRUE IN (CURRENT_DAT
```

---

## Crash 39: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007930`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008442`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 41: `4abe975587876238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009106`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 42: `447f5084bc73b8f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009123`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 43: `583c7c305ae56942` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009177`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 44: `8d89a9ac8188f6fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009384`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 45: `838e5a638fd90b23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013919`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN see
```

---

## Crash 46: `df99a5821dc159f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016386`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL *, * FROM json_tree('[]') ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); I
```

---

## Crash 47: `f8d3d0ed92abe22e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018814`

```sql
SELECT printf('%.*f', -2147483648, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 48: `07a4a931193930f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018822`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(
```

---

## Crash 49: `a3179aa509e486a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018836`

```sql
SELECT substr('S--8 sJVH', 9223372036854775807, 0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 50: `9275bf2bc4c6533c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018843`

```sql
SELECT substr('Z-737P', -2147483648, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce
```

---

## Crash 51: `d39a7566a3c52c6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018850`

```sql
SELECT printf('%.*g', 2147483647, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 52: `f0792cc9bc527a75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018856`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIMESTAMP NOT LIKE NULL), rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQU
```

---

## Crash 53: `d5eb514e8584528a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018862`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE TRUE IS NULL / FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 54: `35c7d20af943ac78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018885`

```sql
SELECT printf('%.*g', -2147483648, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 55: `a6f25696c8d18ab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018895`

```sql
SELECT printf('%.*g', -2147483648, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 56: `176a32b9b0ea8924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018901`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (TRUE >= CASE CURRENT_TIMESTAMP WHEN TRUE THEN TRUE END COLLATE NOCASE NOT IN (TRUE) NOTNULL), rowid NUMERIC); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); E
```

---

## Crash 57: `cff37eb0359e2b90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018913`

```sql
SELECT printf('%.*d', -2147483648, 0.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 58: `80e237135e9c7219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021879`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME * CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TI
```

---

## Crash 59: `ef2818a2d4f32c86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021889`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME)); ANALYZE p; CREATE TABLE seed_a
```

---

## Crash 60: `f71226b11721af2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021920`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME IS NOT CURRENT_TIME)); PRAGMA int
```

---

## Crash 61: `f8a0730aece359e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021928`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY, c2 INTEGER UNIQUE, rowid FLOAT CHECK (CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT 
```

---

## Crash 62: `737232ce8de77ee5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021934`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-FALSE LIKE TRUE NOT IN (CURRENT_TIME)); PRAGMA integrity_check; CRE
```

---

## Crash 63: `096395ef95849976` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021962`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE IN (VALUES (TRUE)) << FALSE COLLATE NOCASE NOT IN (CUR
```

---

## Crash 64: `2345a50fe2ef6a32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021997`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL DEFAULT TRUE); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME)); PRAGMA integrity
```

---

## Crash 65: `fc937faa5b99c653` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022056`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (-CURRENT_TIME NOT IN (-CURRENT_TIME NOT IN (-C
```

---

## Crash 66: `b696b8a39b6538a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022097`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME * CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TIM
```

---

## Crash 67: `f2b779501d29a131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022105`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TIME); PRAGMA inte
```

---

## Crash 68: `3afa60706351b075` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022166`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (TRUE)); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 69: `cacc9d1ed2ea9897` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022222`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME >> TRUE)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME)); PRAGMA integ
```

---

## Crash 70: `0d57a6046a79b113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022228`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME > NULL >> TRUE)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME NOT IN (CURRENT_TIME)); PRAGM
```

---

## Crash 71: `7d2bea9f0714199d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022254`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME > NULL >> TRUE)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c U
```

---

## Crash 72: `4fb96f6a302f0a56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022261`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME >> TRUE)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 73: `de7b13f5bcb9e088` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022268`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 74: `ab8a4472f00afff6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022282`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 75: `9c8d8f86e68f0b10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024276`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a + -0) UNIQUE); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 76: `afae19ea88045979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024292`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL, c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE see
```

---

## Crash 77: `c224f70ff95a16d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024318`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (NULL) INTERSECT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN se
```

---

## Crash 78: `bf7d301b6a4e3ab1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024326`

```sql
SELECT round(-1.0, 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 79: `894b5640d7f5b98f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024379`

```sql
SELECT printf('%.*d', 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 80: `1c01f998d7e0d857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024388`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT NOT NULL); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 81: `76061bb5ee5133bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024394`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT CURRENT_DATE); WITH RECURSIVE r AS (SELECT t1.* LIMIT TRUE IS NOT CURRENT_TIME & CURRENT_DATE, (TRUE) MAT
```

---

## Crash 82: `3d00a8c99bb6321a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024407`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SE
```

---

## Crash 83: `b3d251f398d350dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027120`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME % TRUE || NOT CURRENT_DATE == rank() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 84: `d158b636ebd4d73e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027517`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_TIME = CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE NULL) AS sub1; 
```

---

## Crash 85: `5d195c839d5875b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027555`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED GROUP BY FALSE LIMIT CURRENT
```

---

## Crash 86: `c85c920155bc9925` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027588`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a + -0) UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE NULL) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FR
```

---

## Crash 87: `00cc97d8551da94a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027603`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE GENERATED ALWAYS AS (NULL) STORED, c1 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 88: `b8d38b9d60b0eb06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027739`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT dense_rank() OVER () AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_a(c
```

---

## Crash 89: `94c4a6a4bc3a05df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027755`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[1,2,3]') ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 90: `f688799b1ed1ca53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027762`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT count(*) OVER (PARTITION BY CURRENT_DATE, CURRENT_TIMESTAMP) AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE N
```

---

## Crash 91: `dd994726631f1375` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027768`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (FALSE); ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 92: `5d9d6cfe6ede42ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027781`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE COLLATE NOCASE LIKE 
```

---

## Crash 93: `ac64f2a406990448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027796`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT ALL * FROM json_tree('[]') ORDER BY CURRENT_DATE DESC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 94: `3acef00b48fcf0c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027812`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_TIME = ~CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c U
```

---

## Crash 95: `bfdedf6127bb52c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027818`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE +NOT NULL IS NULL IS NOT FALSE) AS sub1; CRE
```

---

## Crash 96: `55a25035f9392fa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027825`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE NOT FALSE IS NOT FALSE) AS sub1; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 97: `a9fdbaa9ccc3fc9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027839`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CASE CURRENT_TIMESTAMP WHEN TRUE NOTNULL THEN TRUE END COLLATE
```

---

## Crash 98: `84a90374ac56b3d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027847`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP NOT IN (FALSE)) AS sub1; C
```

---

## Crash 99: `49d4c9513703b1de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027864`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE NULL) AS sub1; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 100: `9f425d837a8a0193` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027873`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE IS NOT FALSE LIKE NULL) AS sub1; CREATE TABLE see
```

---

## Crash 101: `1945bf73cd294ba1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027883`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT *, dense_rank() OVER () AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ F
```

---

## Crash 102: `a30fc920acc94e19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027898`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE X'aE0C12BFdCB5' LIKE NULL) AS sub1; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 103: `ed1b1b2b362ebf0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027978`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE LIKE CURRENT_DATE LIKE CURRENT_DATE LIKE CURRENT_
```

---

## Crash 104: `df489d12ef5cc1c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028012`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE X'aE0C12BFdCB5') AS sub1; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 105: `43db5eb40aeea7dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028048`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS x5nx725___93j_t_6p0_l_2_9_ FROM p WHERE CURRENT_DATE IS NOT FALSE) AS sub1; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 106: `a23273a1692908cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033166`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME NOT BETWEEN count(DISTINCT NULL) FILTER (WHERE CURRENT_TIMESTAMP) AND TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 107: `324fe6d4d124b92d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033183`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (TRUE); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 
```

---

## Crash 108: `b8fdaf130063f814` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033370`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_
```

---

## Crash 109: `63e5606182c56601` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033381`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE p AS (VALUES (TRUE)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c N
```

---

## Crash 110: `6020980a3cd6d37b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033430`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (TRUE)) < CAST(CURRENT_DATE AS INT); CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 111: `d0822723473b3354` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033447`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') GROUP BY CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 112: `07c4fce59df63a85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033458`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE BETWEEN CURRENT_DATE AND NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 113: `e7ad832402a8d3c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033473`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (TRUE)) < CASE CURRENT_TIMESTAMP WHEN TRUE NOTNULL THEN TRUE END COLLATE NOCAS
```

---

## Crash 114: `8f80fa37f6aa8aa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033509`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME NOT BETWEEN count() FILTER (WHERE CURRENT_TIMESTAMP) AND TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 115: `20c3346e103adc93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033626`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE _rowid_ IN (VALUES (TRUE)) < NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN see
```

---

## Crash 116: `45acfb22d85d4304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033632`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE _rowid_ IN (VALUES (TRUE)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b O
```

---

## Crash 117: `4b32918e96ce44f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033668`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE _rowid_ < NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 118: `80420863433d253d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033738`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIME IN (CURRENT_TIMESTAMP, FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 119: `1f8680fb481b6a6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033748`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); WITH RECURSIVE t2 (c2, c1) AS (SELECT *) VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 120: `1254d27731258924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033756`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL IS NULL; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 121: `1c7f7e61aef59efd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033766`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE TRUE COLLATE NOCASE < CASE CURRENT_TIMESTAMP WHEN TRUE NOTNULL THEN TRUE END COLLATE NOCASE NOT IN (CU
```

---

## Crash 122: `dfe27ce2de1b6628` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033775`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') WHERE TRUE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 123: `f946fcb86964aca1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033783`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{}') WHERE TRUE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 124: `da6a6c246001e4aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033793`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_TIME DESC, FALSE DESC LIMIT row_number() FILTER (WHERE TRUE) OFFSET CURRENT_TIME; INSER
```

---

## Crash 125: `82263d767fc9180d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033802`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE) UNION ALL SELECT NULL AS re_03_1__9 ORDER BY NULL ASC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 126: `93bd6ac2f9879c63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033808`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE TRUE COLLATE NOCASE < FALSE COLLATE BINARY; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 127: `e9b707f04dee8029` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033815`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('{"a":1}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL J
```

---

## Crash 128: `cd2ed147b34df886` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033832`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT *, dense_rank() OVER () AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM json_tree('{"a":1}') WHERE TRUE COLLATE NOCASE < CURREN
```

---

## Crash 129: `f45b64a1b27e770c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033850`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE, c3 FLOAT NOT NULL); SELECT * FROM json_tree('{"a":1}') WHERE TRUE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_
```

---

## Crash 130: `caa581471b6bb336` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033870`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each(NULL, '$[#-1]') WHERE TRUE COLLATE NOCASE < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 131: `23375044a73929d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033934`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE X'' < CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3
```

---

## Crash 132: `15073564a1abe17e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033960`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE TRUE COLLATE NOCASE < CURRENT_TIMESTAMP < CURRENT_TIMESTAMP < CURRENT_TIMESTAMP < CURRENT_TIMESTAMP < 
```

---

## Crash 133: `2dde4fecca921eb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033988`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE X''; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL 
```

---

## Crash 134: `11e34babfcc45821` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034023`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT dense_rank() OVER () AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM json_tree('{"a":1}') WHERE CURRENT_TIME; CREATE TABLE seed
```

---

## Crash 135: `21c3d38785173cd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035438`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME) UNION SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER () AS wn8i9o1fs1uk6sko5_u860_x FROM json_tree('[]'); CREATE TA
```

---

## Crash 136: `3de17751574b5f21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035468`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (NOT +CURRENT_DATE == ntile(CURRENT_DATE) OVER (PARTITION BY CURRENT_TIME))) <
```

---

## Crash 137: `48257b250e075d33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035480`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (CURRENT_TIME NOT BETWEEN count() FILTER (WHERE CURRENT_TIMESTAMP) AND typeof(
```

---

## Crash 138: `1f87b4d5c80915cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035504`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a + -0) UNIQUE); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 139: `5eb6d6c6c43639cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035511`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (TRUE)) << NOT FALSE IS NOT FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 140: `133c66ac78212f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035533`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each(NULL, '$[#-1]') , json_each('{"a":{"b":1}}') USING (c1) EXCEPT SELECT EXISTS (VALUES (CURRENT_TIME
```

---

## Crash 141: `32f6c5eb43a19258` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035645`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (CURRENT_TIME)) << FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 142: `9f1bb61ebb5eb66f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035653`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (SELECT ALL CURRENT_DATE AS wn8i9o1fs1uk6sko5_u860_x FROM json_tree('[]')) << FALSE; C
```

---

## Crash 143: `c21daf0a4c73c6d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035715`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (CURRENT_TIME NOT BETWEEN count() FILTER (WHERE CURRENT_TIMESTAMP) AND count(*
```

---

## Crash 144: `13000f6df35002ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035816`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (count(*) OVER (ORDER BY NULL ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW), FALSE); CREATE TABL
```

---

## Crash 145: `8b6268c2faf0c48e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035889`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES ((VALUES (CURRENT_TIMESTAMP)) <= CURRENT_DATE >= CURRENT_DATE)); CREATE TABLE 
```

---

## Crash 146: `a2174a9351a22bfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038867`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 AS kdy471__p_fe_8r__1_56l_sg9___3_2o628___bh_u_2fgh_6xn7_6o_43_ti656____z_np0 WHERE NULL
```

---

## Crash 147: `d6a7766fddd9585a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038884`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY, c1 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP, rowid FLOAT CHECK (CURRENT_TIME * CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TIME)); CREATE VIEW IF
```

---

## Crash 148: `4e1fd4fd93042eec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038972`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT CURRENT_TIMESTAMP, c2 NUMERIC DEFAULT X'', _rowid_ BLOB NOT NULL DEFAULT FALSE, a BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 AS kdy471
```

---

## Crash 149: `e177a4c3251c90d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042671`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL DEFAULT -94136856487285846944640929352371348411748297484268565879599063786884903559821405296297238727122200820040920897879129357343850488648577066773136981601446766
```

---

## Crash 150: `6fa3b72279858b4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042682`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT X'c98b01'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TAB
```

---

## Crash 151: `502dad433fce3981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043918`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (FALSE), b FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNI
```

---

## Crash 152: `98a18507054bb988` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043930`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY CURRENT_D
```

---

## Crash 153: `b326297b35e0fa65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043938`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE) EXCEPT SELECT CASE WHEN CURRENT_TIME IS NULL THEN FALS
```

---

## Crash 154: `3a7b63097410a1bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043959`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY, c2 INTEGER UNIQUE, rowid TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed
```

---

## Crash 155: `289dd0b9259d7248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043981`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (cume_dist() OVER ()); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 156: `b549a909d38869d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043987`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY percent_rank() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_DATE ROWS BETWEEN NULL PRECEDING AND CUR
```

---

## Crash 157: `5d180f72f50765d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT '-t_-9 R-_', rowid BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_a(c 
```

---

## Crash 158: `94c934e4ac1badf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044076`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT FALSE MATCH NULL, avg(RAISE(IGNORE) % NULL) FILTER (WHERE TRUE) OVER (PARTITION BY FALSE ORDER BY CU
```

---

## Crash 159: `50fede82f8185c54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055431`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN GENERATED ALWAYS AS (CAST(NULL AS NUMERIC)) VIRTUAL, _rowid_ TEXT); INSERT INTO q DEFAULT VALUES; EXPLAIN QUER
```

---

## Crash 160: `94bd5b6a9a4f9498` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055547`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN GENERATED ALWAYS AS (FALSE) VIRTUAL, _rowid_ TEXT); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (F
```

---

## Crash 161: `883a0e8de85d6198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056427`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count() AS x_71gb_z3__o41___lv3h_302bm5___73_e__73_u7ch__, CURRENT_TIME | TRUE FROM p; CREATE TABLE s
```

---

## Crash 162: `ddebf575955a43ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056438`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL DEFAULT -94136856487285846944640929352371348411748297484268565879599063786884903559821405296297238727122200820040920897879129357343850488648577066773136981601446766
```

---

## Crash 163: `b376535a04e422e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056454`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (NULL) EXCEPT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a
```

---

## Crash 164: `a33cb6e227d33927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056622`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ROWS 
```

---

## Crash 165: `b9c78a08a04e0ef7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056664`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CASE WHEN NULL IS NULL THEN RAISE(IGNORE) END > NULL >> TRUE), b FLOAT NOT NULL); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT p.c3 AS x_71gb_z3__o41___lv3h_3
```

---

## Crash 166: `4208dbd5dd603cf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056815`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT X'5B3F770c' FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = s
```

---

## Crash 167: `61e11ddbf6e11fda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058473`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{"a":{"b":1}}', '$[#-1]'); CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"
```

---

## Crash 168: `cd717d4adf4a1cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063126`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE FALSE OR TRUE; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 169: `e546c461d9c60458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063138`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE TRUE NOTNULL OR FALSE; CREATE TABLE seed_
```

---

## Crash 170: `f4fb97329eb15130` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[1,2,3]') WHERE CURRENT_TIME GROUP BY CURRENT_DATE HA
```

---

## Crash 171: `851e0d5e214c923c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063203`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (cume_dist() OVER (ORDER BY CURRENT_TIME ASC NULLS LAST ROWS BETWEEN CU
```

---

## Crash 172: `38a63a4b0e0b8b8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065180`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT ' Hd 69D_USo m6', rowid DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN V
```

---

## Crash 173: `2c4a7127ebb93658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065276`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT 24); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE
```

---

## Crash 174: `d02e8bad72f06975` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070542`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); SELECT * FROM p NATURAL JOIN p WHERE json_remove('[]', '$[#-1]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURA
```

---

## Crash 175: `451ceeec04e836dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070554`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 AS kdy471__p_fe_8r__1_56l_sg9___3_2o628___bh_u_2fgh_6xn7_6o_43_ti656____z_np0 WHERE NULL GROUP BY TRUE
```

---

## Crash 176: `0ba74b975c92bc60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073200`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL (SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER () AS wn8i9o1fs1uk6sko5_u860_x FROM json_tree('[]') ORDER BY CURRENT_DATE LIMI
```

---

## Crash 177: `11be0fc9ae201260` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073435`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[]') NATURAL JOIN json_each(CURRENT_DATE IS NULL, '$.c[0]') WHERE TRUE MATCH CURRENT_TIME; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 178: `800803d405ea8f53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073531`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES ((VALUES (FALSE) UNION ALL SELECT NULL AS re_03_1__9 ORDER BY NULL ASC NULLS F
```

---

## Crash 179: `bd4f336f5a7281c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073554`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE EXISTS (SELECT DISTINCT * FROM json_tree('{}') ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT FALSE); CRE
```

---

## Crash 180: `65e0b2789bc39cff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073564`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * ~CURRENT_DATE << FALSE; CREATE TABLE seed_
```

---

## Crash 181: `2641c87e3e062fb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073570`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE ~CURRENT_DATE * ~CURRENT_DATE * ~CURRENT_DATE * ~CURRENT_DATE * ~CURRENT_DATE * ~CURRENT_DATE << FALSE
```

---

## Crash 182: `a31ed22882dbdec6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073706`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (count(*) OVER (ORDER BY NULL ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW), NOT CURRENT_TIME ==
```

---

## Crash 183: `5eb7d72a15b61a39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073810`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (count(*) OVER (ORDER BY NULL ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW), row_number() OVER (
```

---

## Crash 184: `bfe9f8dfc9f91852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073879`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY FALSE ORDER BY CURREN
```

---

## Crash 185: `964fdd6b44de1ee3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073904`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (max(FALSE) OVER (PARTITION BY CURRENT_TIME))); CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 186: `9ae141251bef6003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073913`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE BETWEEN CURRENT_DATE AND NULL IN (VALUES (count() OVER (PARTITION BY CURRENT_TIME))); CRE
```

---

## Crash 187: `252ba55a8e04e3ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073971`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (count() OVER (PARTITION BY 0 COLLATE BINARY))); CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 188: `501a5e3f1b244804` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000000856`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 189: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001886`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 190: `e48601d70ae6d94e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001993`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 191: `d11413e9beb93c49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002042`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 192: `db0a1ea2bb7fb9d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002048`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 193: `c8bfe081ae574c2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003287`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 194: `f15850743b5e79bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003312`

```sql
SELECT printf('%.*s', 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TA
```

---

## Crash 195: `4a696daaa71f5bef` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003448`

```sql
SELECT printf('%.*s', 4294967296, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 196: `1ae2149e332c8d83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003656`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -TRUE << FALSE < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 197: `17fb9d257d2d4705` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003662`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -FALSE < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 198: `b9058cb1c4110951` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003678`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 199: `12d556cffc8a8cc2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003695`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 200: `ad2887adaed397f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004053`

```sql
SELECT printf('%.*f', -2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 201: `d76ec25c9198ef18` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004063`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 202: `db5f864a90a5a200` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004360`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 203: `0fbf36dd10d40e34` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004417`

```sql
SELECT printf('%f', 9223372036854775807, '5-d _kE -OKlE --_-'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VAL
```

---

## Crash 204: `46959c1432d7dbaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004618`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%s', -9223372036854775808, 'N -qb-_X -3o 9_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); 
```

---

## Crash 205: `495e5c8c340d2fdc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004877`

```sql
SELECT round(0.0, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 206: `9ee1c6283e7eea83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005630`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 207: `b20e1bd777864b03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005686`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (json_each('[]')) CROSS JOIN jsonb_each('{"a":1}') NATURAL LEFT JOIN json_each('{"a":{"b":1}}') WHERE NU
```

---

## Crash 208: `ed429aacb5728fb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005722`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE);
```

---

## Crash 209: `7f6abe9da2b59665` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000007233`

```sql
SELECT substr('', 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 210: `8e50eeeca21f4012` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009132`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 211: `7c89cae280fc3e26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009150`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 212: `6d124b18ed95807e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009169`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT
```

---

## Crash 213: `581129d197ba2caf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013102`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (EXISTS 
```

---

## Crash 214: `afd91127321f9383` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013172`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL
```

---

## Crash 215: `7976241856f76c22` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000018672`

```sql
SELECT substr('_dw_r7 ', -9223372036854775808, -9223372036854775808); CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_
```

---

## Crash 216: `843393258468bc46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021181`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, c1 GENERATED ALWAYS AS (c2) NOT NULL); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_DATE FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 217: `52c9aa3451c22982` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021192`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); SELECT ALL count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS wn8i9o1fs1uk6sko5_u860_x FROM json_tree('[]') ORDER BY CURRENT_TIME ASC 
```

---

## Crash 218: `ccd641e89d81caaf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021203`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (count(*) OVER (ORDER BY NULL ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRE
```

---

## Crash 219: `606db79a9f804225` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021215`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT ALL count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME ROWS BET
```

---

## Crash 220: `2a8c1094ac98260d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021222`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT TRUE LIKE TRUE NOT LIKE CURRENT_DATE ESCAPE NULL AS a FROM p; CREATE TABLE seed_t1(c
```

---

## Crash 221: `cea045910a1b81f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021229`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT ALL count(*) FILTER (WHERE (SELECT * UNION ALL SELECT * ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST)) OVER ()
```

---

## Crash 222: `7321450c3190461f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021240`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_DATE > FALSE)) SELECT CURRENT_DATE FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 223: `cc5382d795bf33a3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021246`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT (VALUES (NULL) INTERSECT VALUES (NULL)) FROM p; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 224: `0dd97952d1407239` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021258`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (FALSE IS NULL << NULL << RAISE(IGNORE) >= CASE CURRENT_TIMESTAMP WHEN TRUE NOTNULL THEN NULL COLLATE RTRIM 
```

---

## Crash 225: `788c16f74d77f1e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021264`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT ALL * FROM t2 NOT INDEXED) SELECT CURRENT_DATE FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 226: `bb7f55c24a4a4885` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021271`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT DISTINCT FALSE AS zn_l1_d06_02s9_6__ FROM jsonb_each('{"a":{"b":1}}') LEFT JOIN t2 ON CURRENT_TIMESTAMP WHER
```

---

## Crash 227: `60387ac0c06bbdd2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021289`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT FALSE MATCH CURRENT_TIME FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 228: `5a239de08253a5e9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021298`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT -CURRENT_TIMESTAMP IS NOT NULL FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 229: `5cca4d55f54f94a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021309`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (FALSE LIKE last_insert_rowid() > RAISE(IGNORE) <> NULL IS CURRENT_DATE, NULL & CURRENT_DATE)) SELECT CURREN
```

---

## Crash 230: `9851a07837651d3e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021316`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT * FROM jsonb_tree('{"a":{"b":1}}') WHERE FALSE GROUP BY FALSE LIMIT TRUE OFFSET NULL) SELECT CURRENT_DATE FR
```

---

## Crash 231: `4b005f191796c058` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021327`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT CASE -CURRENT_TIME WHEN CURRENT_TIME THEN CASE FALSE WHEN CURRENT_TIME THEN FALSE EN
```

---

## Crash 232: `fb1d1a97390a9b40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021346`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, c1 GENERATED ALWAYS AS (b) UNIQUE, b NUMERIC DEFAULT 84.8378); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_DATE FROM p; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 233: `6f4e3b10f82fa5b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021352`

```sql
SELECT round(0.01, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 234: `1096f6cdb666ed5c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021370`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (SELECT DISTINCT (SELECT *, * ORDER BY TRUE DESC NULLS LAST, c1 >= CURRENT_TIME GLOB -NULL IS NOT NULL LIKE CURRENT_
```

---

## Crash 235: `7ed5afa68a66a5af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021397`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT FALSE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_DATE FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 236: `9b32328c5e8bf9b2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021492`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE); WITH RECURSIVE r AS (VALUES (RAISE(IGNORE))) SELECT CASE CURRENT_TIME WHEN CURRENT_TIME THEN CURRENT_TIMESTAMP ELSE CURRENT_DATE >> FALS
```

---

## Crash 237: `4f1bf20ff9cacbcd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021551`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 238: `a51f67d5055c5f71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021565`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); ANALYZE q; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 239: `4e947b01ce782767` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021571`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 240: `5ad0c5b3fad1d660` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021589`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIMESTAMP ISNULL)); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE 
```

---

## Crash 241: `c82b121272843a29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021607`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN DEFAULT CURRENT_DATE, rowid INT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK
```

---

## Crash 242: `4c64035cefbf0ef0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021613`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL, c3 TEXT CHECK (FALSE), b FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integr
```

---

## Crash 243: `23cb8789eb50880f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021623`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE CHECK (FALSE < CURRENT_TIMESTAMP)); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREA
```

---

## Crash 244: `98447265799fad00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021635`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 245: `38e9c998a8ebaa85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021642`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 246: `00a73a969224030a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021654`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE GENERATED ALWAYS AS (NULL) STORED, c1 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGM
```

---

## Crash 247: `6dcd8fa1729a8888` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021669`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME GROUPS BETWEEN UNBOUNDED PRECEDING AND CU
```

---

## Crash 248: `b84048ee7388a531` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021679`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL, rowid INT DEFAULT CURRENT_TIMESTAMP, c1 VARCHAR(255) NOT NULL DEFAULT '3I __ -_oDRx', b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT 
```

---

## Crash 249: `4c44c24f911c7624` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021690`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CR
```

---

## Crash 250: `82d7a17b20912503` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021701`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 251: `2d18ea14cce147ea` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021716`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 252: `17fd3d5c567bd85a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021730`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 I
```

---

## Crash 253: `62d7e43897f1114d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021741`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) DEFAULT X''); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1
```

---

## Crash 254: `95e072f457a92043` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021786`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 255: `2935819d8c5b9e49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021808`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 256: `e183525f48d0fd4f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022612`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (NOT EXISTS (SELECT * FROM json_tree('[{"a":1},{"b":2}]') GROUP BY FA
```

---

## Crash 257: `07793d7a96660b3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023510`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (TRUE IS NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 258: `d11e3e4bfa8238b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023530`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p VALUES (CURRENT_TIME) UNION VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(
```

---

## Crash 259: `687464ba0bd79242` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023667`

```sql
SELECT round(1e308, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 260: `2844b19dd925a81e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023709`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (NOT EXISTS (SELECT * FROM p AS f9562_o___pzs2e6e8q3 NATURAL LEFT JOI
```

---

## Crash 261: `f9c46a882125a068` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023748`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (NOT EXISTS (SELECT * FROM json_each('{"a":{"b":1}}') NATURAL LEFT JO
```

---

## Crash 262: `4bcccba0275645c7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026677`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL * FROM json_each('{"a":1}') ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 263: `cf0b2b176222cb77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026684`

```sql
SELECT round(-1e308, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 264: `3f2beb10d11529fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026707`

```sql
SELECT substr('kaw-5u', 0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE see
```

---

## Crash 265: `7c0a3651e40b05a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027023`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME % TRUE || NOT CURRENT_DATE == ntile(CURRENT_DATE) OVER ()); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 266: `9968ad012b0dc2b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027031`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME || NOT CURRENT_DATE == ntile(CURRENT_DATE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 267: `a188de80afe238b7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027039`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME % TRUE || CURRENT_DATE == ntile(CURRENT_DATE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 268: `a8033ff35a23e2c2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027045`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (CURRENT_TIME % TRUE || NOT CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 269: `01764ac244b87ffe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027062`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p AS (VALUES (CURRENT_TIME)) VALUES (NULL || NOT CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 270: `e70dbf5a45aa913a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029122`

```sql
SELECT printf('%.*d', 2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 271: `f8f6c8be11c4cf21` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029140`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL * FROM json_tree('{"a":{"b":1}}') ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 272: `2b57cc1c81726d45` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029164`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (NULL, NULL); PRAGMA integrity_check; CREATE
```

---

## Crash 273: `a8dcf4724c027bbc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029173`

```sql
SELECT printf('%.*d', 1, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 274: `b4c942a28a464a68` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029197`

```sql
SELECT round(-1.0, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 275: `5c0efbfbcbaf7ddc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029445`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT CURRENT_TIMESTAMP, * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 276: `4155b3294f1c108f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029451`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN q WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 277: `370ac72efdb589bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029457`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE TRUE / FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 278: `cdc904416362739d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029463`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 279: `ed35381f7f288560` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029471`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP % NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 280: `e1b01fd56bf1908a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029484`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT NOT NULL DEFAULT FALSE, rowid FLOAT CHECK (RAISE(IGNORE) * CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_TIME))
```

---

## Crash 281: `5dcab10d41b01d51` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029491`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE IS NULL THEN TRUE END; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 282: `a494625ee81cba85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029501`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN TRUE LIKE TRUE NOT LIKE CURRENT_DATE ESCAPE NULL THEN TRUE END; CRE
```

---

## Crash 283: `8874abc27abffdb7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029507`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN json_array_length(FALSE, '$') THEN TRUE END; CREATE TABLE seed_t1(c
```

---

## Crash 284: `fa040edf5404cb48` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029531`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 285: `5c039138b9ed0353` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029539`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT ALL * FROM json_tree('[]') ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST, EXISTS (SELECT DISTINCT * FROM json_t
```

---

## Crash 286: `c2c03222435cf52d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029558`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN CURRENT_TIME IN (CURRENT_TIMESTAMP, FALSE) END; CREATE T
```

---

## Crash 287: `77b656b1e01539ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029565`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1
```

---

## Crash 288: `b74c47c8f047368a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029571`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) CHECK (TRUE BETWEEN CURRENT_DATE AND TRUE), b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE
```

---

## Crash 289: `590c73d10348a821` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029582`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL, rowid NUMERIC, c2 INT, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE
```

---

## Crash 290: `bead25ed18619287` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029596`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL DEFAULT -94136856487285846944640929352371348411748297484268565879599063786884903559821405296297238727122200820040920897879129357343850488648577066773136981601446766
```

---

## Crash 291: `365c7aa060095b04` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029607`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIME AND CURRENT_TIME; CREATE TABLE see
```

---

## Crash 292: `a2755c2db08fb39b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL DEFAULT '2'); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c1 I
```

---

## Crash 293: `8967f72d0d395e10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029654`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT X'5cBf5893'); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN FALSE THEN TRUE END; CREATE TABLE seed_t1(c
```

---

## Crash 294: `57e9fbbeb8e920c9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029673`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL DEFAULT -8.2514e74215674335830268577702201614304518855285364181082353703824516265322455); SELECT * FROM q
```

---

## Crash 295: `bb529c97e91410ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029711`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WH
```

---

## Crash 296: `c623c62b9d540670` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000029834`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM q NATURAL JOIN p WHERE json_array_length(FALSE, '$'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 297: `b5261739441ac3f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034124`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":{"b":1}}') NATURAL LEFT JOIN json_tree('[]') WHERE NULL; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 298: `af7d1fa80a6b2b59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034249`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM (SELECT *) AS cv NATURAL LEFT JOIN jsonb_tree('[1,2,3]') ON FALSE WHERE CURRENT_TIME GROUP BY TRUE 
```

---

## Crash 299: `46f4e00896fad2fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 300: `810ec5b4f57ae8cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034265`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (NULL > NULL, NULL); PRAGMA integrity_check;
```

---

## Crash 301: `2d7552f113151e14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034282`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('[1,2,3]') WHERE CURRENT_TIME GROUP BY CURRENT_DATE HAVING CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 302: `197f7094de0bdf73` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034299`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, * ORDER BY CURRENT_TIMESTAMP ASC LIMIT NULL; SELECT * FROM json_tree('{"a":1}') WHERE NULL < CURRENT_TIME
```

---

## Crash 303: `d7cab18f3cdac439` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034306`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT CURRENT_TIME | TRUE FROM json_tree('{"a":1}') WHERE NULL < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 304: `d341d19fb6669de8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034314`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * FROM json_tree('{"a":1}') WHERE NULL < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 305: `867e55153a0cbac8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034320`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY, c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (FALSE LIKE last_insert_rowid(), NULL); PRAG
```

---

## Crash 306: `740032eb3c532809` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034437`

```sql
SELECT substr(' _f--', 9223372036854775807, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44
```

---

## Crash 307: `317bb65c6bff5ddc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034448`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT *, *, dense_rank() OVER () AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM json_tree('{"a":1}') WHERE -FALSE; CREATE TABLE seed
```

---

## Crash 308: `b3516514a73911ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034454`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 309: `b53f2c7547093607` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034464`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CAST(CURRENT_DATE AS INT)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTE
```

---

## Crash 310: `3ea4db7b9f720050` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034475`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL *, count(*) FILTER (WHERE (VALUES (NULL))) OVER () AS wn8i9o1fs1uk6sko5_u860_x FROM json_tree('[]'); CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 311: `505617723ec298e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034484`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE > FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 312: `3a2cdc444844cb4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034536`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT CASE +CURRENT_TIMESTAMP WHEN CURRENT_TIMESTAMP LIKE NULL COLLATE BINARY THEN FALSE END AND FALSE OR FALSE || CURRENT_TIMESTAMP + FALSE &
```

---

## Crash 313: `a5705765e3b76a78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034563`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -''; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 314: `f2e67527f77e0b13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034662`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES ((VALUES (CURRENT_TIMESTAMP)) | TRUE)) << FALSE < CURRENT_TIMESTAMP; CREATE T
```

---

## Crash 315: `a761ea3157f39cba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034694`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << -CURRENT_DATE IN (VALUES (TRUE)) << FALSE < CURRENT_TIMESTAMP; CRE
```

---

## Crash 316: `6cf8f479fca2452d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034733`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (FALSE LIKE last_insert_rowid() > NULL IS CURRENT_DATE)) << FALSE < CURRENT_T
```

---

## Crash 317: `55923ebe31bb460b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034836`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE << FALSE << FALSE << FALSE << FALSE << FALSE << FALSE << FAL
```

---

## Crash 318: `7c0a206d8dbdda2b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034845`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE < CURRENT_TIMESTAMP < CURRENT_TIMESTAMP < CURRENT_TIMESTAMP 
```

---

## Crash 319: `44b99da56935feeb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034853`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << CURRENT_DATE IN (VALUES (TRUE)) << CURRENT_DATE IN (VALUES (TRUE))
```

---

## Crash 320: `8ac97721276af7f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034872`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -TRUE << CURRENT_DATE IN (VALUES (TRUE)) << CURRENT_DATE IN (VALUES (TRUE)) << CURRENT_DATE IN (VALUES
```

---

## Crash 321: `7975e3969f7c49ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034879`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -TRUE << CURRENT_TIME << CURRENT_DATE IN (VALUES (TRUE)) << CURRENT_DATE IN (VALUES (TRUE)) << CURRENT
```

---

## Crash 322: `f2ca46d28b8eb99f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035301`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE -FALSE << -CURRENT_TIME < CURRENT_TIMESTAMP; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 323: `67793454ce9f88f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035341`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') NATURAL LEFT JOIN json_tree('[]') WHERE -CURRENT_DATE IN (VALUES (TRUE)) << FALSE < CURRENT_TIMESTAMP; CREAT
```

---

## Crash 324: `816ccd7a7c489f54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035395`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP)) << FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 325: `f789e8d14984a30e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (-CURRENT_TIME = CURRENT_TIME NOTNULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE 
```

---

## Crash 326: `e5e1bf892ff67c1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000036778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT -01.1126239045864203626344036058269073281850355115935599200884845828997621667033260971819800916609765602834191309898331485443509281260509462047
```

---

## Crash 327: `52d323a593c42e56` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037473`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH t2 (c2, c1) AS (SELECT *) VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 328: `d8bcde87f01f7086` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037490`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (SELECT * FROM p INDEXED BY b NATURAL LEFT JOIN json_tree('[]') GROUP BY FALSE) VALUES (CU
```

---

## Crash 329: `927304e341c631cd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037496`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (SELECT * FROM json_tree('[]') WHERE NULL NOT IN (SELECT * EXCEPT VALUES (RAISE(IGNORE))) IN (TRUE) GROUP BY CUR
```

---

## Crash 330: `596d3a80fbca46c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037502`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (NULL)) VALUES (NULL IN (NULL IN (NULL IN (NULL IN (NULL IN (RAISE(IGNORE)))))) LI
```

---

## Crash 331: `7bb4b61a436177a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037510`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (CURRENT_DATE IN (SELECT * FROM jsonb_each('{"a":{"b":1}}') WHERE FALSE GROUP BY C
```

---

## Crash 332: `c02ff0c17f3ad33f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037528`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP); VALUES (row_number() OVER (PARTITION BY CURREN
```

---

## Crash 333: `403102bcdde49bf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037555`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE last_inse
```

---

## Crash 334: `bec7b4efcae84037` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037675`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (NULL)) VALUES (CURRENT_TIMESTAMP); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 335: `7645886f080dbcbf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043758`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT ALL count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIME ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

---

## Crash 336: `c17ca323c0b87605` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051217`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY CURRENT_DATE > FALSE ORDER BY CURRENT_TIME GR
```

---

## Crash 337: `1cf75d85d7c4776f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051364`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count() FILTER (WHERE CURRENT_TIMESTAMP) AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FROM p; 
```

---

## Crash 338: `796a6d34dc0e44da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056955`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT count() FILTER (WHERE CURRENT_TIMESTAMP) AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ FRO
```

---

## Crash 339: `87fe456efe5ac066` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056972`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count() FILTER (WHERE CURRENT_TIME IS NOT CURRENT_TIME) AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4
```

---

## Crash 340: `8f388864705e8fff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056985`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE NOT BETWEEN CURRENT_TIME / CURRENT_TIME AND RAISE(IGNORE), CURRENT_DATE BETWEEN NULL AND RAISE(ABORT, 'Mwf_Hp0
```

---

## Crash 341: `a07e6171c017f857` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057015`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT, b GENERATED ALWAYS AS (b) NOT NULL UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count() FILTER (WHERE CURRENT_TIMESTAMP) AS o2r4_4_0z1__e_79y_g1_o___7_j2hl
```

---

## Crash 342: `b015e150c5eb5408` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057178`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT *, count() FILTER (WHERE CURRENT_TIMESTAMP) AS o2r4_4_0z1__e_79y_g1_o___7_j2hl__x92k_eez4_w__t_ 
```

---

## Crash 343: `0c3d48d7a0971ffa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057255`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME / CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 344: `e8feb51aee24967a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057286`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT *, count() FILTER (WHERE CURRENT_TIMESTAMP) AS o2r4_4_0z1__e_79y_g1
```

---

## Crash 345: `1a6d290a8372323b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057388`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY _rowid_ IN (VALUES (TRUE)) ORDER BY CURRENT_T
```

---

## Crash 346: `f13c4f6a6b32756a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057406`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (NULL)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIME GROUPS BETWE
```

---

## Crash 347: `16fce0597407a33a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057439`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY FALSE ORDER BY EXISTS (SELECT DISTINCT * FROM
```

---

## Crash 348: `890ac10094594d08` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057445`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (SELECT * FROM json_tree('{}') JOIN (t3 AS chkh6_h_5_a_u_iu9_o_6y_552f2_149_41_x2f05911__) WHERE TRUE GROUP BY NULL WINDOW w
```

---

## Crash 349: `f8766ef36d1ec2c3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057470`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY FALSE ORDER BY lower(-TRUE) COLLATE RTRIM GRO
```

---

## Crash 350: `ee314a64c11d7dd1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057520`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY FALSE ORDER BY CURRENT_TIME ROWS BETWEEN CURR
```

---

## Crash 351: `5c41a6d91fc48420` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057675`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT ALL *, * FROM json_tree('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 352: `35ea2d3c5c51dd27` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057702`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, a GENERATED ALWAYS AS (c2) NOT NULL UNIQUE, c2 INTEGER PRIMARY KEY); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT *, *, dense_rank() OVER () AS o2r4_4_0z1__e_79y
```

---

## Crash 353: `8da2ba45faca7911` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057825`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE q AS (VALUES (TRUE)) SELECT group_concat(TRUE) FILTER (WHERE CURRENT_DATE) OVER () AS dl9_, dense_rank() OVER () AS o2r4_4_0z1__e
```

---

## Crash 354: `8c6650543fb8ebe9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058774`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); SELECT * FROM p NATURAL JOIN p WHERE json_remove('{"a":{"b":1}}', '$.a.b'); CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c2) AS (VAL
```

---

## Crash 355: `1d2b490d67846ec9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000058933`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT X'D2e6'); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); WITH RECURSIVE p (c2) AS (
```

---

## Crash 356: `8eb287b37f762f1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000071987`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (TRUE) UNION ALL SELECT ALL * FROM t2 , p INDEXED BY c1), r AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAM
```

---

## Crash 357: `78cf6a085974e83d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072035`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP); SELECT * FROM json_tree('[1,2,3]') WHERE CURR
```

---

## Crash 358: `95946ca18c65e264` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072041`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (VALUES (FALSE)) VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE TRUE OR 
```

---

## Crash 359: `1d0dfc6a1590c0b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072125`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (NULL)), r AS (SELECT DISTINCT json_pretty(NULL NOTNULL & CASE WHEN NULL THEN CURRENT_TIMESTAMP ELSE CUR
```

---
