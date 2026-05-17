# Crash Triage Report

**Total crashes:** 337  
**Unique crash sites:** 337  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 176 | 176 | 52% |
| Signal | 161 | 161 | 47% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `368a779f80e932fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 VALUES (NULL >> RAISE(IGNORE) MATCH RAISE(IGNORE) || +CURRENT_TIME IS NOT NULL NOT IN (++FALSE REGEXP CURRENT_DATE) - (FALSE) < 
```

---

## Crash 2: `e0fe043f211f6594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000517`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; VALUES (RAISE(IGNORE) NOTNULL LIKE (CURRENT_TIMESTAMP) / CASE WHEN CURRENT_T
```

---

## Crash 3: `9999e4893eba5867` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000541`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p VALUES (random(), ntile(json_array_length(quote(+CURRENT_TIME) NOT IN (NULL, NULL IS DISTINCT FROM CURRENT_DATE) COLLATE BIN
```

---

## Crash 4: `bbf5b7ff316d14de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000814`

```sql
SELECT printf('%.*g', 2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CAST(CASE RAISE(IGNORE) WHEN CURRENT_TIMESTAMP IS NOT NULL BETWEEN FALSE COLLATE RTRIM AN
```

---

## Crash 5: `38fa8fde653e3b88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000896`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 6: `aae28e75fc9d539f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000928`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, c1); REPLACE INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME COLLATE BINARY NOT NULL IS NULL); PRAGMA quick_check; 
```

---

## Crash 7: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000934`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 8: `64468a9825a80689` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001344`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 9: `099345af273f4664` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001427`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1, c3, c3, c2); VALUES (CAST(FALSE OR TRUE AS BLOB) IN (-FALSE <= NOT CURRENT_DATE NOT BETWEEN CURRENT_DATE AND TRUE IS CURRENT_TIMESTAMP 
```

---

## Crash 10: `e0b6a44e7953efc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002018`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 11: `337be29af70a2096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002050`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 12: `0c51fc4142efa954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002121`

```sql
SELECT printf('%x', -2147483648, '-971w'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 13: `42a3a067a2f5d15b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003037`

```sql
SELECT round(-1e308, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(),
```

---

## Crash 14: `1e5ebaf5df916863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003079`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))
```

---

## Crash 15: `8658b1faa4e2f0d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003229`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT OR ABORT INTO p VALUES (EXISTS (WITH RECURSIVE r (c1) AS (SELECT *) VALUES (CURRENT_TIME))); PRA
```

---

## Crash 16: `49c19dd7803afd62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003331`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 17: `ad72170bcb858f2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003614`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 18: `4e97c7bdc0675d49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003626`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 19: `a1afbf691f63307c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004260`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN CURRENT_DATE END == NULL), c2 DATE UNIQUE); INSERT INTO p DEFAULT V
```

---

## Crash 20: `0ca24d1e0f264209` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004266`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN CURRENT_DATE END), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 21: `3c4f93bdd35b9d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004272`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP COLLATE BINARY), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 22: `57b9726c6e50154c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004279`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE WHEN FALSE THEN CURRENT_DATE END), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 23: `29ae05425f634092` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004288`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a 
```

---

## Crash 24: `8035ee41b9933a65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (TRUE), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 25: `d2a4010fd060f13a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004338`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY, c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 26: `c8f8d45089e5704e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004373`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN TRUE END == NULL), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE T
```

---

## Crash 27: `0512f0de685eda1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004393`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY, c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 28: `1ea73132bfd07399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004519`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY, c3 INTEGER GENERATED ALWAYS AS ((NULL NOTNULL)) VIRTUAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 29: `f3ddd7039ba3e461` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004573`

```sql
SELECT printf('%.*d', -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(
```

---

## Crash 30: `b194c0d98aee2b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004719`

```sql
SELECT substr('  _f  -8vb', -1, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 31: `31b625e09c985301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004814`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 32: `b7e06584f89660e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004829`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT substr(' - Zi', -1, 4294967295); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE s
```

---

## Crash 33: `bcd42f7ca80fba49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005434`

```sql
SELECT substr('  - 39p___', 2147483648, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 34: `2f070933ff03831f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005475`

```sql
SELECT printf('%.*e', 2147483648, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 35: `3022f792d3e84fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005843`

```sql
SELECT round(1.0, -2147483649); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 36: `cb5c4a72cd662eb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006135`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP), c3 REAL CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 37: `3b6710b468e8bcbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006609`

```sql
SELECT substr('', 2147483648); SELECT printf('%s', 4294967296, '3--NL-6__T'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.
```

---

## Crash 38: `83d07b2dd0b62713` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007082`

```sql
SELECT substr('j', 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 39: `fcaa215ca106ce2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007762`

```sql
SELECT printf('%u', 4294967295, 'zy-Qlb   4c-al0p- -'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `b57b85523a916d3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008337`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_each('{"a":1}') GROUP BY CURRENT_TIMESTAMP HAV
```

---

## Crash 41: `b7f21fba0aa38ad0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008344`

```sql
SELECT printf('%.*g', 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 42: `0bd02cdac828cc61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008371`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b 
```

---

## Crash 43: `24fac072336d2f0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008949`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_each('{"a":1}') GROUP BY FALSE ORDER BY CURREN
```

---

## Crash 44: `df5968f3b492fa0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009146`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 45: `3926dce6bc7e0673` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009221`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 46: `ee30e2456b75ed64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009230`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 47: `b2792da8dad450b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011201`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) CHECK (TRUE IN (CURRENT_DATE, FALSE)), c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE
```

---

## Crash 48: `2c69dc75b9643156` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011236`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL
```

---

## Crash 49: `eba8e23720bf69c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011247`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (~NULL), a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 50: `2e88505c294ad520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011254`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT 0.0); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 51: `72289857074507df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011283`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3, b, c2); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 52: `571417cf7fa8532b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011309`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a
```

---

## Crash 53: `981e89f1bab2e747` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011351`

```sql
SELECT printf('%.*s', 0, 0.01); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), S
```

---

## Crash 54: `b98a59c4658696a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012416`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 55: `cbbe7bc29572e02e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012457`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE, a DATE UNIQUE); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (-633316.68004); PRAGMA integrity_check;
```

---

## Crash 56: `51037e4f0ab477b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012534`

```sql
SELECT round(0.01, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 57: `e6e00420505dcf0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012628`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_a(c 
```

---

## Crash 58: `8f4bc2ab0295111a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012635`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 59: `8766d1c237be63ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018014`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE, a DATE UNIQUE); INSERT OR REPLACE INTO q VALUES (FALSE, FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(
```

---

## Crash 60: `31490e5b01a47e76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018020`

```sql
SELECT printf('%.*d', 2147483648, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 61: `b05473102ed7369c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018032`

```sql
SELECT printf('%.*e', 4294967295, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 62: `a74c4d441ea3d3f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018045`

```sql
SELECT printf('%.*e', 2147483648, 1e-308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2
```

---

## Crash 63: `12739e3f8a9d7fa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018075`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, rowid INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL, TRUE) ON CONFLICT DO NOTHING; SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE TABLE
```

---

## Crash 64: `49d7abd5730d74af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018098`

```sql
SELECT substr('D__- c S5', 4294967296, 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coales
```

---

## Crash 65: `a8f99cb090b21de9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018104`

```sql
SELECT substr('d-4_ - _6z-  pQ ', 1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVE
```

---

## Crash 66: `b9729bb477ca6e49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020835`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 67: `03c3fb2364f18634` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022792`

```sql
SELECT printf('%lld', -9223372036854775808, 'G00-'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 68: `74e34d447553085e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023878`

```sql
SELECT substr('', -9223372036854775808, 4294967296); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coale
```

---

## Crash 69: `c07c0e0209e6dba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023931`

```sql
SELECT round(1e308, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2)
```

---

## Crash 70: `433ccf5af6148067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024331`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -41098); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = see
```

---

## Crash 71: `bf5746e725b33bf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024355`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c2 FLOAT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE, NULL << NULL) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQ
```

---

## Crash 72: `e803ed0d9d818d8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024369`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = s
```

---

## Crash 73: `3c45f8cd046239a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024380`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE IS NOT NULL NOT LIKE CURRENT_DATE), c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 74: `8702c250aaf560cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024391`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE WHEN FALSE THEN TRUE ELSE CURRENT_TIME END IS NOT FALSE ISNULL IN (FALSE BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP, TRUE <> NULL)), c2 FLOAT UNIQUE); I
```

---

## Crash 75: `163c346df8895e0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024414`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (NULL GLOB NULL % FALSE), c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 76: `1bfab579c3d651db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024421`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), _rowid_ VARCHAR(255) CHECK (NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 77: `0e6cf54fe0fa1dd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024464`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c3 TEXT NOT NULL DEFAULT ''); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 78: `4a24f40991be6956` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024524`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c2 FLOAT UNI
```

---

## Crash 79: `2ed01651ce105029` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024587`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE + CURRENT_TIMESTAMP), c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_
```

---

## Crash 80: `201ae8cefafd2de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024606`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIMESTAMP NOT LIKE CURRENT_DATE), c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 81: `e0129301a392544d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024622`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 82: `6418a5cf2eaca0fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025189`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIME + TRUE IS NULL WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 83: `d1f536f2449e2695` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >> FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE 
```

---

## Crash 84: `f7e1d9aac027aeed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025220`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (NULL + TRUE IS NULL), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 85: `f7306d002ba1412e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIME < CURRENT_DATE < CURRENT_DATE COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 86: `8bd01a0685cef579` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025251`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE), c2 BOOLEAN); INSERT INTO p DEFAULT VALU
```

---

## Crash 87: `bea6cbaebbcdeb92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025260`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE | FALSE IS NULL WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 88: `291a19e2a91badb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025267`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP NOT IN (TRUE) COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 89: `dc68eec6aba15372` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE IS NOT FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_che
```

---

## Crash 90: `608a540282e9d1ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025296`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIME + TRUE IS NULL COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE
```

---

## Crash 91: `eb679839ff4bd292` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DA
```

---

## Crash 92: `c3019810126e2289` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025317`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIME >> CURRENT_DATE WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 93: `4e3a7d189b585979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025405`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN FALSE THEN TRUE END), a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 94: `1847b41178a88321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025425`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLA
```

---

## Crash 95: `eb4b3821714a2131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025431`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN C
```

---

## Crash 96: `fd32ad3c26d7a295` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025439`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >= FALSE >=
```

---

## Crash 97: `bcd1dd8cb8f327bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025453`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= CURRENT_TIMESTAM
```

---

## Crash 98: `d8b223a1b82d33c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025460`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE WHEN CASE FALSE WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY WHEN CASE FALSE >= 
```

---

## Crash 99: `f7490e02e59a40cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025531`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE WHEN CASE FALSE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE CURRENT_DATE WHEN CASE NULL WHEN CURRENT_TIME THEN TRUE END THEN TRUE END THEN TRUE
```

---

## Crash 100: `cec50108d577c455` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025570`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE WHEN CURRENT_TIME THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 101: `c61791ce30a3cb9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025757`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLL
```

---

## Crash 102: `26626c33443b605b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026074`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLA
```

---

## Crash 103: `efa09a499f8167d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026113`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLA
```

---

## Crash 104: `9977b7d465de229b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026514`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLA
```

---

## Crash 105: `3d851de593cd5c58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028146`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CUR
```

---

## Crash 106: `f96c04b51f0ba6d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028171`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE >= CURRENT_TIME + NULL COLLATE BINARY WHEN FALSE THEN TRUE END), c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 107: `65ec2236e584cfa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028216`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), c2 TEXT CHECK (rowid)); INSERT INTO p DEFAULT VALUES; PRAGMA in
```

---

## Crash 108: `386a4a1e84d17299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028223`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), c2 TEXT CHECK (p.c3), c3 FLOAT UNIQUE); INSERT INTO p DEFAULT V
```

---

## Crash 109: `e35ba756e8731c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028230`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_DATE COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE BINARY COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE TH
```

---

## Crash 110: `17995297920ef463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028243`

```sql
SELECT round(-1.0, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 111: `91c515957a452fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028261`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIME < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE WHEN FALSE THEN CURRENT_DATE
```

---

## Crash 112: `22421608c5abaf15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028294`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= ~CURRENT_TIME >> FALSE IS NULL >> +CURRENT_TIME WHEN FALSE THEN CURRENT_DATE END), c2 DATE UNIQUE); INSERT INTO p DE
```

---

## Crash 113: `25fb8465b2cf7480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028310`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE NULL GLOB NULL % FALSE COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA inte
```

---

## Crash 114: `a8cae8f1a41ea89f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028317`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), c3 FLOAT NOT NULL DEFAULT -71924202.40, a REAL); INSERT INTO p 
```

---

## Crash 115: `0ccde93658365e36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE <= NULL END), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 116: `8eeba453d7588613` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028400`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), b NUMERIC DEFAULT 973913379316686101805437410143302836396028963
```

---

## Crash 117: `15d8fc0b26633c2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028459`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE FALSE GLOB CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIMESTAMP WHEN FALSE THEN CURRENT_DATE END), c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGM
```

---

## Crash 118: `b4c543941c721db5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028507`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIMESTAMP COLLATE NOCASE >= CURRENT_TIME < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE < CURRENT_DATE), c2 DATE UNIQUE); INSERT INTO p 
```

---

## Crash 119: `e379aecaeb2328de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028578`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT ''); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 120: `6b6e024c64952b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028657`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -71924202.40); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3
```

---

## Crash 121: `a646edd6e133dc4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032176`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT X'AdAf7cB4bAbF'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 122: `859c29a3daba7acc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032191`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, c1 INT CHECK (CURRENT_DATE COLLATE NOCASE >= CURRENT_TIMESTAMP), c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TAB
```

---

## Crash 123: `5a127ecc0b1fc07c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032229`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TA
```

---

## Crash 124: `13bd4e972ddc6ff9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032242`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (NULL, NULL || CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 125: `57304c5c068a670f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032256`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE NULL GROUP BY FALSE WINDOW w1 AS (), w2 AS (); VALUES (FALSE); CREATE TABLE seed_a(c UNIQU
```

---

## Crash 126: `3a151ef4b64350e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032264`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT *, TRUE FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE
```

---

## Crash 127: `ba0156893d2d45aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032271`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CASE NULL WHEN FALSE THEN NULL END); CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 128: `c4feb3e6594d3f2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032292`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT -71924202.40, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 129: `17b0cbc46197dff3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032299`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM json_each('{"a":1}') GROUP BY NULL; CREATE TABLE seed_a(c UNIQU
```

---

## Crash 130: `ab3f295064f99a7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032311`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 131: `3f38c523482f22e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032397`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY, b BLOB NOT 
```

---

## Crash 132: `d175294374432a72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035115`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (FALSE == total_changes()), a VARCHAR(255) UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_c
```

---

## Crash 133: `bf76ac58e1897b2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035200`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -99051.61918092106461832080835176179971070096138973175612E-4670649873770780199092916622731562672377466364529); CREATE TABLE IF NOT EXISTS q(a VARC
```

---

## Crash 134: `46f5f827dbb35929` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035859`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE);
```

---

## Crash 135: `7d27f2a652358071` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040239`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT * FROM json_each('{"a":1}') GROUP BY TRUE, FALSE; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 136: `19bec71a902bacca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040251`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT count(*) & TRUE AS a FROM p NOT INDEXED LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 137: `d7bf9ca635bbc86d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040282`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c2 GENERATED ALWAYS AS (a = 373665) , a TEXT DEFAULT CURRENT_DATE); SELECT DISTINCT * FROM p NOT INDEXED LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE see
```

---

## Crash 138: `229545e693258e25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040314`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('[1,2,3]') LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 139: `e8de99db6a74431f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040320`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (TRUE NOT IN (SELECT ALL * FROM (VALUES (TRUE)) AS d3__jc4__l243os_057x_1__c9_1__45t86fk2jl_yq4____88g_y2_sa3_dh__7r_8sid3p8uew523_v__jo4
```

---

## Crash 140: `779d8dd5d7a81a9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040371`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT NULL); SELECT DISTINCT * FROM p NOT INDEXED LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 141: `7094d60f835d24d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040444`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree('[1,2,3]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JO
```

---

## Crash 142: `912f06dd3674c31e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040466`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('{}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN se
```

---

## Crash 143: `9dc37ee9e2420cce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040724`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (NULL, TRUE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE 
```

---

## Crash 144: `5345be00d8a9a5ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040822`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 145: `6b27745273edb9a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040886`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATU
```

---

## Crash 146: `3e326865d2bf8871` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040905`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (VALUES (TRUE)) AS l_5_vb_5l1 LEFT JOIN json_tree('[]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN 
```

---

## Crash 147: `03f348719950442e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046132`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CAST(CURRENT_TIME AS FLOAT)), a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM 
```

---

## Crash 148: `630bf8234fed7bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046150`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (TRUE) EXCEPT VALUES (TRUE) INTERSECT VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a
```

---

## Crash 149: `ba7f84b3639743a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046242`

```sql
SELECT printf('%f', 9223372036854775807, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lea
```

---

## Crash 150: `8b800d965f8bfd66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058895`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('[]') NATURAL LEFT JOIN json_each(CURRENT_DATE, '$') LEFT OUTER JOIN json_tree('[{"a":1},{"b":2}]'); CREATE TAB
```

---

## Crash 151: `44878e51340c8413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059133`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP ASC LIMIT TRUE) AS l_5_vb_5l1 LEFT JOIN jso
```

---

## Crash 152: `568a422b00036eaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059139`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP ASC LIMIT TRUE OFFSET TRUE) AS l_5_vb_5l1 L
```

---

## Crash 153: `7e6942e9594d7977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059191`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (avg(FALSE) FILTER (WHERE FALSE) OVER (PARTITION BY NULL ORDER BY NULL COLLATE NOCASE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AN
```

---

## Crash 154: `e92ab0f8ebc3c64a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059227`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (VALUES (TRUE)) AS d3__jc4__l243os_057x_1__c9_1__45t86fk2jl_yq4____88g_y2_sa3_dh__7r_8sid3p8uew523_v__jo4p___s1_v_r2rao3_
```

---

## Crash 155: `ccba3d0be1e8bc9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059252`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') ORDER BY FALSE ASC NULLS LAST LIMIT +CURRENT_DATE NOT IN (VALUES (CURR
```

---

## Crash 156: `5e3914dcd105fa55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059420`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree(FALSE, '$'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL J
```

---

## Crash 157: `f64773c0d3764fa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059428`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT *, *, *, *, *, *, *, *, *, * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 158: `05fa0f703575c946` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059606`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree(TRUE IN (VALUES (NULL)), '$[#-1]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 159: `3b1484a8d226afcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059793`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree(TRUE, '$[#-1]'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATUR
```

---

## Crash 160: `a9831ef6a75af51a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060413`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_DATE GROUP BY CURRENT_TIME; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JO
```

---

## Crash 161: `23cbfca8af23ae3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060461`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_tree(FALSE, '$') NATURAL LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 162: `ef6243938e1c10d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060524`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT group_concat(NULL, 'NCD_  -00- _ - O') FROM json_tree(FALSE, '$') LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UN
```

---

## Crash 163: `794cdb9b145713d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060545`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT changes() FROM json_tree(FALSE, '$') LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 164: `eca516f0fe368754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060560`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT * FROM json_each('{"a":1}') GROUP BY TRUE, FALSE ORDER BY NULL ASC NULLS LAST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 165: `6d0a25e4f79ef529` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060574`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, b BLOB NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT DISTINCT * FROM p NOT INDEXED LEFT JOIN json_each(CURRENT_DATE, '$'
```

---

## Crash 166: `4b5b514249ec3b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060736`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, c1 VARCHAR(255) NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT DISTINCT * FROM p NOT INDEXED; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 167: `8a7034ab7b325de9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060771`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT *, *, *, *, *, *, *, *, *, *, *, *, *, * FROM json_each('[1,2,3]') LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c U
```

---

## Crash 168: `689c8b1001eeac9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060800`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('[1,2,3]') LEFT JOIN (SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIMESTAMP ASC LIMIT TR
```

---

## Crash 169: `2c3c5760fcae3add` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060810`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT count(*) AS a, * FROM json_each('[1,2,3]') LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 170: `51f3214b30795ecb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060972`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c2 GENERATED ALWAYS AS (a = 373665) , a NUMERIC DEFAULT -71924202.40); SELECT DISTINCT * FROM p NOT INDEXED , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c
```

---

## Crash 171: `6babdc42fc605bf9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (random()), c2 TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 172: `58270bc82d876d11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061036`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_
```

---

## Crash 173: `6dd3bc97e744d1f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061139`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT * FROM json_each('[1,2,3]') LEFT JOIN json_tree('{"a":1}') ON CURRENT_TIMESTAMP; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c 
```

---

## Crash 174: `4d4100ebcd62f401` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061285`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE), c2 FLOAT UNIQUE); SELECT DISTINCT * FROM p NOT INDEXED LEFT JOIN p AS b_6n2_74_wuy6_mbr__zz_d_2z_20__a_sgji9___b__99____h_3rai755gc_9_l6m768__
```

---

## Crash 175: `0484e52a705851af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061328`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT count(*) & TRUE AS a FROM p NOT INDEXED LEFT JOIN p AS b_6n2_74_wuy6_mbr__zz_d_2z_20__a_sgji9___b__99____h_3rai755gc_9_l6m768__z
```

---

## Crash 176: `3e34fdf4a1211482` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061385`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); SELECT DISTINCT CURRENT_DATE AS a FROM p NOT INDEXED LEFT JOIN p AS b_6n2_74_wuy6_mbr__zz_d_2z_20__a_sgji9___b__99____h_3rai755gc_9_l6m768__zh9i
```

---

## Crash 177: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001849`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 178: `a4ab5dcc7f947d6d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001970`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 179: `29d9f89fe4884f6e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002005`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p
```

---

## Crash 180: `7aaf1b1a7b6031de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002027`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 181: `f2566b5fc20fbbcc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002068`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 182: `95044ace4419ea0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002091`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT, c1 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 183: `aaa72612757c0568` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002337`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (WITH t3 AS (VALUES (CURRENT_TIMESTAMP)) VALUES (NULL)) <> CURRENT_TIMESTAMP) AS sub1; CREATE 
```

---

## Crash 184: `1221a6b1d8ff39ec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002398`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 185: `1bf4c4c9f62ccb99` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002411`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (WITH t3 AS (VALUES (CURRENT_TIMESTAMP)) VALUES (NULL))) AS sub1; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 186: `2665925fdcdbe93e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002417`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 187: `4620fe39485321c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002423`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_TIMESTAMP)) <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 188: `11e9cd46ea8364bc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002429`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 189: `5c6167b4bb22d6d3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002435`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 190: `55e4d3e9789dcd50` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002445`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 191: `6c6ca51f31aaef3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002464`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 192: `603bfad6d5f139de` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002476`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSER
```

---

## Crash 193: `3df24779705bf8ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002484`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 194: `6d9dfa6d88e9e643` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002506`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIME) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 195: `a4628a4c32fec93a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002512`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 196: `ce0481c9e1487dd5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002519`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 197: `48ce6b20c1ce445c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003116`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM (VALUES (TRUE)) AS d3__jc4__l243os_057x_1__c9_1__45t86fk2jl_yq4____88g_y2_sa3_dh__7r_8sid3p8uew523_v__jo4p__
```

---

## Crash 198: `e413abe9c6f99823` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003277`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 199: `ed86936bbe411baa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003288`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 200: `3d4bd8fe0d7ee158` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003707`

```sql
SELECT printf('%f', 2147483647, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE 
```

---

## Crash 201: `12d0c4236672280a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003718`

```sql
SELECT round(-0.0, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 202: `7ae284c96980e45f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004599`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, a INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 203: `bd9ca03fec1d12bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004999`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 204: `2941e9c10b433b43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005010`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 205: `f3ff9e5fd4bb6a6b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005673`

```sql
SELECT printf('%.*e', 2147483647, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 206: `f9241ca41a4e6cd9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000009251`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 207: `22e3cc027dc7f653` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010514`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 NOT INDEXED LEFT OUTER JOIN json_each('{"a":{"b":1}}') ON EXISTS (SELECT ALL * FROM jsonb_each('{}'
```

---

## Crash 208: `98ea76404a23107f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010573`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 NOT INDEXED LEFT OUTER JOIN json_each('{"a":{"b":1}}') ON EXISTS (SELECT ALL * FROM jsonb_each('{}'
```

---

## Crash 209: `1deeaddf60e9e825` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010814`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM json_each('[]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 210: `fe0974e6389fec0a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012690`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (CURRENT_TIMESTAMP / CURRENT_TIME)); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_chec
```

---

## Crash 211: `0846a6afc3f6e7a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012701`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE, c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 212: `a6e2d7e09195e72b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012715`

```sql
SELECT printf('%.*s', -9223372036854775808, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 213: `4274c3b7e929108f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012850`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 214: `03315c64c51d2720` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012857`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (FALSE)); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 215: `deba29ab53c2f89b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017588`

```sql
SELECT round(1e-308, 9223372036854775807); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 216: `3398e0455db80287` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021113`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 217: `6d53c34adc9d993d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021161`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (FALSE > CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 218: `234f4498cbee6079` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021271`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (-FALSE OR -FALSE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 219: `388d095dd145cf03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021279`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE, RAISE(IGNORE) OR CURRENT_DATE | FALSE IS NULL COLLATE RTRIM); INSERT INTO p DEFAULT VALUES; ANALYZE 
```

---

## Crash 220: `d8b374d40bd6f624` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021289`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('{"a":1}') GROUP BY RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c
```

---

## Crash 221: `730643881ee93385` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021295`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE) LIKE CURRENT_TIME GLOB CURRENT_TIME ESCAPE NULL, CURRENT_TIME); INSERT INTO p DEFAULT VALUES; ANALYZ
```

---

## Crash 222: `39e5b70769525822` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021303`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) CHECK (NULL / CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 223: `ee7931a920e151d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021328`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE, FALSE + TRUE IS NULL COLLATE RTRIM); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c
```

---

## Crash 224: `961a267ec59a549a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021336`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each(RAISE(IGNORE), '$[#-1]') , json_tree('{}') USING (rowid) WHERE CURRENT_DATE; INSERT INTO 
```

---

## Crash 225: `0fa2cf9cadc1e970` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021345`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CASE format('zRt_Vr_v-ZG2 _', CURRENT_TIME) WHEN -NULL % random() FILTER (WHERE CURRENT_DATE) THEN +FALSE NOT IN (
```

---

## Crash 226: `d8adcdc8373eb4f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021360`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM json_each('{"a":1}') GROUP BY TRUE, FALSE; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 
```

---

## Crash 227: `baf1d2247c3db6df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021370`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q CROSS JOIN json_tree('[1,2,3]') CROSS JOIN jsonb_tree('{"a":{"b":1}}') WHERE CURRENT_DATE UNION ALL SELECT
```

---

## Crash 228: `6ceb5535fdb93d88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021378`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) EXCEPT SELECT q.* ORDER BY CURRENT_TIME ASC NULLS FIRST; INSERT INTO p DEFAULT VALUES; ANALYZE p; C
```

---

## Crash 229: `efc4e750c8e7cba9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (X''); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 230: `ccdcc19dda44f24e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021399`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP IN (t2.a), count(DISTINCT CURRENT_DATE) FILTER (WHERE TRUE)); INSERT INTO p DEFAULT VALUES; ANAL
```

---

## Crash 231: `8e204bdba00e2533` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021478`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT
```

---

## Crash 232: `53c553d8ffcbe79a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021503`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT E
```

---

## Crash 233: `e61d044bd52a985e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021509`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT E
```

---

## Crash 234: `3d77d5a2af6cf0b5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021533`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED A
```

---

## Crash 235: `c5fcace7736fc8a4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021542`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED A
```

---

## Crash 236: `c15e846b22f1b675` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021999`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE
```

---

## Crash 237: `de34b8df4bc1d609` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE
```

---

## Crash 238: `7d5f814833c5a8d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022045`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (X''); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 239: `5aec0f1ff1db5023` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022252`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 240: `f102a8c7bd490a86` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022258`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 241: `611ecf352f0af523` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022264`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 242: `ff2737ad0ad12859` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022278`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 243: `67619ab61504d5a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022296`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 244: `85aaa73c413b9044` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022315`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 245: `d15e13bc9e987879` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022325`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 246: `383894aacd188be9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022337`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 247: `72b3166a43223184` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022355`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) CHECK (-CURRENT_TIMESTAMP / CURRENT_TIME)); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA integrity_c
```

---

## Crash 248: `6556f4c3a809e583` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022364`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT EXISTS (SELECT * EXCEPT SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GROUP BY TRUE HAVI
```

---

## Crash 249: `e70dbf5a45aa913a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000022447`

```sql
SELECT printf('%.*d', 2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 250: `13f69194f30d0dd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023668`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT -41098); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 251: `a8b5389a34f03685` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023713`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (RAISE(IGNORE) GLOB NULL << NULL) VIRTUAL, a INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 252: `3cda82e4ab8e5412` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT OR REPLACE INTO q VALUES (TRUE NOT IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 253: `d4996e65e43b12f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034826`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 254: `61b7b4ac1f1efa39` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034843`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIMESTAMP / CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 255: `8f1e2d131c384f07` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035658`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CASE NULL WHEN FALSE THEN NULL END == CASE CURRENT_DATE WHEN NULL THEN TRUE END)); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT OR ABORT INTO p VAL
```

---

## Crash 256: `717ad9ef8515b9ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035671`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_TIMESTAMP IS NULL >> CURRENT_DATE), a BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE
```

---

## Crash 257: `8f6d0f7630ad5050` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035697`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'AdAf7cB4bAbF'); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE seed_t1
```

---

## Crash 258: `2e8cc75a43330206` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035717`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP << TRUE); PRAGMA quick_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 259: `b741372343c91bd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035736`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT INTO p SELECT ALL * FROM (VALUES (TRUE)) AS d3__jc4__l243os_057x_1__c9_1__45t86fk2jl_yq4____88g_
```

---

## Crash 260: `3e02edee778fe5d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035893`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); INSERT INTO p SELECT ALL * FROM p NOT INDEXED; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 261: `3b208f881dbd5fac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000037069`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (-CURRENT_TIMESTAMP / CURRENT_TIME >> CURRENT_DATE), a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 262: `e256154a3c159c1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000038293`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 263: `053e7e31bc6af37a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042459`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q (a) AS (SELECT *) SELECT count(*) & TRUE AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 264: `bb0248973f546d7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042654`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT count(*) & TRUE AS a FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 265: `e8c93c731fd67293` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042667`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (TRUE) EXCEPT VALUES (TRUE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 266: `30c7985f9a655092` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042687`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT *, *, *, *, *, *, *, *, *, *, *, *, *, *, * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_
```

---

## Crash 267: `3788c82f1fc0fa55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042705`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB, b GENERATED ALWAYS AS (b) NOT NULL UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 268: `3e9b761beb97125d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042713`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CASE NULL WHEN CASE CURRENT_TIME WHEN FALSE COLLATE BINARY THEN TRUE END THEN TRUE END) AS sub1; CREATE TA
```

---

## Crash 269: `f063ff21d4eb6b5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042739`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (FALSE) STORED, a BLOB PRIMARY KEY); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE))) AS sub1; CREATE TABLE seed_t1
```

---

## Crash 270: `c997475787822d3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042746`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (TRUE) EXCEPT SELECT TRUE AS x_t_w024_q_ FROM json_each('{"a":1}') GROUP BY NULL)) AS 
```

---

## Crash 271: `3d6f4fd170c45a27` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042754`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(FALSE AS VARCHAR(255))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 272: `86438cbc50a50b9c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042851`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (CURRENT_DATE)) NOT IN (VALUES (CURRENT_DATE)) NOT IN (VALUES (CURRENT_DATE)) NOT IN (
```

---

## Crash 273: `fe7b1b9e37e1a61a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042939`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE FALSE > CURRENT_TIME) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 274: `16c4f85bb7e90d3c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042948`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIMESTAMP NOT BETWEEN RAISE(IGNORE) AND CURRENT_TIMESTAMP NOT BETWEEN RAISE(IGNORE) AND CURRENT_TIMESTAMP NOT BETWEEN RAISE(IGNORE) AND CURRENT_TIMES
```

---

## Crash 275: `7c73c9f0c4b9d647` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042961`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT count(*) & TRUE AS a FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 276: `a2daae0b590aa550` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042974`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT, c2 GENERATED ALWAYS AS (a + 199890) NOT NULL UNIQUE, a TEXT NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t
```

---

## Crash 277: `e16d764cccc7aa29` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042980`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE FALSE IS NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 278: `7828544945e0998f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042986`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE >= CURRENT_TIMESTAMP COLLATE BINARY FROM p WHERE NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 279: `50c0a745f9b1a574` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042992`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIME < CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 280: `d45b1ed82a2e1bf8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043039`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE -FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 281: `75c66d4b917c7a56` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043051`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_DATE <= NULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 282: `8710f5220743b737` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043271`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT CASE TRUE WHEN CASE CURRENT_DATE WHEN CASE NULL WHEN CURRENT_TIME THEN TRUE END THEN TRUE END THEN TRUE END FROM p WHERE TRU
```

---

## Crash 283: `bf08505a5347ca84` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043310`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT ~json_patch('{"a":1}', '[1,2,3]') FROM p WHERE TRUE <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 284: `9a7fc2996e1ede96` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043327`

```sql
SELECT printf('%.*f', 2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 285: `bc2b6be03fb9e23e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043380`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT p._rowid_ AS fp5u_x__s3c580_1_h5_1_l2 FROM p WHERE TRUE <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 286: `b273e7c744ce5b4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043469`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP <> FALSE IS NOT TRUE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 287: `ae2fa253287427d4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043527`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT FALSE >> FALSE IS NOT FALSE ISNULL FROM p WHERE CURRENT_TIMESTAMP <> CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 288: `ef3e2d7e9502724b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043533`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP <> json_remove('[{"a":1},{"b":2}]', '$[#-1]')) AS sub1; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 289: `8248b564b12bdd88` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043541`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CURRENT_TIMESTAMP <> NULL GLOB NULL % FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 290: `4b5e35ac36b739ba` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043654`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 291: `bba44bb811cdb646` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043667`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') ORDER BY FALSE ASC NULLS LAST LIMIT CURRENT_TIME; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 292: `ba85b0b5ea895752` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043712`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP, TRUE <> NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 293: `a3740b1cd8e8efce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043840`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') NATURAL JOIN json_tree('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 294: `25048e51cf4c63b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043872`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE COLLATE RTRIM FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 295: `d5440c11a9a9f80a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044269`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (FALSE) STORED, a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 296: `242ee8707996c8a6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, a REAL UNIQUE); INSERT INTO p VALUES (NULL, CURRENT_DATE % CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 297: `586918146b3e1d14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044460`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (random()), c2 TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 298: `ab3014d340c64495` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044483`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE == total_changes()), a VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 299: `57a5942a2a8a336f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044619`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); WITH RECURSIVE q (a) AS (SELECT *) SELECT count(*) AS a FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 300: `df617668469e39fc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044644`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 301: `30902990d6a47ef9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044838`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP COLLATE NOCASE) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); 
```

---

## Crash 302: `0590fbb0fd11c50b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044861`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 303: `dfcbb4c51f09dff8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044870`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT DISTINCT count(*) AS a FROM json_each('{}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 304: `b9938d29b9b48bf4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046334`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -71924202.40); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 305: `d43d41c9d22dc88b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046350`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); INSERT OR FAIL INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 306: `d9df20a5c8c1d130` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000046375`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (X'2dbdfCFfd7'); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),
```

---

## Crash 307: `b93557d966369a4c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053450`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT rank() OVER () FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1
```

---

## Crash 308: `1d628d35939f4051` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053456`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT rank() OVER () FROM p WHERE TRUE NOT IN (VALUES (FALSE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 309: `a8bc312e70d22874` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053499`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c2 GENERATED ALWAYS AS (a = 373665) , a TEXT DEFAULT CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE IS NULL COLLATE NOCASE) AS sub1; CREATE TABLE see
```

---

## Crash 310: `cc2d0524dec1a2ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053679`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL, c3 FLOAT UNIQUE); SELECT * FROM (SELECT * FROM p WHERE FALSE >= CURRENT_TIMESTAMP COLLATE BINARY) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 311: `2e6e26241bcea876` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053722`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 312: `94ee25ade8013dc5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053882`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_DA
```

---

## Crash 313: `1ca74187d2316ca3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054083`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT DISTINCT *, *, *, *, *, *, *, * FROM json_tree('{}') ORDER BY CURRENT_TIME DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 314: `3db1587fe7848bdb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054100`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (~NULL), a DATE UNIQUE); SELECT * FROM (SELECT * FROM p WHERE FALSE BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 315: `8dea0431d033c453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054455`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT sum(CASE FALSE GLOB CURRENT_TIMESTAMP COLLATE NOCASE WHEN FALSE THEN CURRENT_DATE END) FILTER (WHERE CURRENT_TIME) AS spf FROM (SELECT * FR
```

---

## Crash 316: `1546834e62e67add` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054479`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIME) AS spf FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 317: `2ed1eac7e1fde808` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054534`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT count(DISTINCT CURRENT_DATE) FILTER (WHERE CURRENT_TIME) AS spf FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t
```

---

## Crash 318: `88f1813c3e545df9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054663`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT count() FILTER (WHERE CURRENT_TIME) AS spf FROM (SELECT rank() OVER () FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 319: `c6b165c313b1fafd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054742`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT p._rowid_ AS fp5u_x__s3c580_1_h5_1_l2 FROM p WHERE TRUE IN (VALUES (NULL))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 320: `4201eae626bc430a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054755`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT NOT NULL DEFAULT NULL); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 321: `28d2a80d7b8d7260` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055055`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT GENERATED ALWAYS AS (RAISE(FAIL, 'f _QJ2 _')) VIRTUAL, a TEXT); SELECT * FROM (SELECT * FROM p WHERE CURREN
```

---

## Crash 322: `949cf5cdf31b0db5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055107`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 323: `ef85243217da614c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055134`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 324: `ceba018854b18e3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055575`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (SELECT DISTINCT CURRENT_TIMESTAMP LIKE CURRENT_DATE ESCAPE FALSE FROM json_tree('{}'))) AS su
```

---

## Crash 325: `56c498cfb1b27df1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055643`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE TRUE NOT IN (VALUES (NULL IS TRUE COLLATE NOCASE))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 326: `03322a1c74a18de0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056019`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(++++++++++++NULL AS VARCHAR(255))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 327: `a5182aacf56deeaa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056032`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(FALSE AS INT)) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234)
```

---

## Crash 328: `33072bd88d93e641` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056043`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(X'2dbdfCFfd7' AS VARCHAR(255))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 329: `b6d198467f47f43b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056055`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP LIKE CURRENT_DATE ESCAPE FALSE FROM json_tree('{}') ORDER BY CURRENT_TIME DESC NULLS FIRST; CREATE TABLE seed_t1
```

---

## Crash 330: `292f003d65247186` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056073`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(-8515633512403047907961519.81867985192030745299052486971209603118139726256802041134537832820355349794
```

---

## Crash 331: `823a3bd74fc14f39` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056080`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(FALSE AS BLOB)) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 332: `6a48972959a67d78` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056100`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(X'4ABbafDDc6aFfc' AS VARCHAR(255))) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 333: `337a3cf8a789bab6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056107`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(FALSE AS DATE)) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 334: `aaf1e500dd7ebdc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056216`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * FROM (SELECT TRUE FROM p WHERE CAST(CURRENT_TIME AS DATE)) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 335: `cc0e1b4a77c45712` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056298`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE, c1 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE GLOB CURRENT_TIMESTAMP COLLATE NOCASE
```

---

## Crash 336: `2295fc91b98d6932` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056368`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_DATE MATCH FALSE), a BLOB PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE FALSE GLOB CURRENT_TIMESTAMP COLLATE NOCASE) AS sub1; CREATE TABLE seed_
```

---

## Crash 337: `3eb1e1fed98a1c24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065146`

```sql
SELECT printf('%.*d', 4294967295, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---
