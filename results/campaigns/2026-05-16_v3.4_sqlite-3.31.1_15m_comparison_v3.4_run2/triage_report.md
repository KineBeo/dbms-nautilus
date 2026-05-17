# Crash Triage Report

**Total crashes:** 340  
**Unique crash sites:** 340  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 162 | 162 | 47% |
| Signal | 178 | 178 | 52% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `2767aa8aa34565e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000109`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, * EXCEPT WITH RECURSIVE p AS (SELECT * ORDER BY TRUE) SELECT p.*; CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (TRUE AND NOT EXISTS
```

---

## Crash 2: `fd7a87ebea373998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000323`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, b, c1); WITH RECURSIVE p (_rowid_, c2) AS NOT MATERIALIZED (SELECT s.* FROM p AS a WHERE -NULL ORDER BY CURRENT_TIME LIKE TRUE == NULL MATC
```

---

## Crash 3: `67882c0cd6674a6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000421`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q VALUES (NOT EXISTS (VALUES (TRUE COLLATE BINARY IS NOT NULL)) = random() IN (SELECT * INTE
```

---

## Crash 4: `e5c96e27a8218f3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000892`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 5: `79eda8fb1a78cdb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001149`

```sql
SELECT substr(' --Z', 4294967296, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT TRUE, * FROM t2 WHERE EXISTS (SELECT * FROM json_tree('[{"a":1},{"b":2}]')); CREATE TABLE
```

---

## Crash 6: `3f9baa10a9cd8efe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001517`

```sql
SELECT substr('P1_O', 9223372036854775807); SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER GENERATED ALWAYS AS (CURRENT_DATE COLLATE RTRIM >= FALSE == TRUE NOT 
```

---

## Crash 7: `62f5ecac22d21b29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002107`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM (jsonb_tree('{"a":{"b":1}}') INNER JOIN json_tree('{}') LEFT OUTER JOIN p INDEXED BY c2) NATURAL
```

---

## Crash 8: `dc2fdbd12a67e491` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002113`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM jsonb_tree('{"a":{"b":1}}') INNER JOIN json_tree('{}') LEFT OUTER JOIN p INDEXED BY c2; EXPLAIN 
```

---

## Crash 9: `f3d220ad7c85437c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002390`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN
```

---

## Crash 10: `f81aa51429f6258d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002487`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT 
```

---

## Crash 11: `2b1aff0f546cf462` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002592`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(
```

---

## Crash 12: `8aa355477b914fa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002870`

```sql
SELECT substr('_m-1 b- -- -_ -__2 ', 0, -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coal
```

---

## Crash 13: `0339b2a6b77875a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003660`

```sql
SELECT printf('%s', 4294967296, 'j-J e7_U_y'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(le
```

---

## Crash 14: `b9e362eca107eb7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004734`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 15: `ec762fb602640dbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004865`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c)))
```

---

## Crash 16: `175044134012979f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004968`

```sql
SELECT substr('_', 9223372036854775807, 1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 17: `820b54060e9ebb91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005108`

```sql
SELECT printf('%.*d', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 18: `9b1d66402d04694d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006715`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME), c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP >= FALSE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTA
```

---

## Crash 19: `59f10a3a8c1ece83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME), c2 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP >= FALSE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTA
```

---

## Crash 20: `2105c566be0c03fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006961`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL 
```

---

## Crash 21: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007368`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 22: `2d7c8958be6bd453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007448`

```sql
SELECT printf('%.*s', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT OR IGNORE INTO t3 VALUES (FALSE NOT IN (CURRENT_DATE IS NOT DISTINCT FROM NULL <= (VALUES (RAISE(IG
```

---

## Crash 23: `e6684aa4fa429fcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007543`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); INSERT INTO t3 (c3, rowid) VALUES (EXISTS (SELECT r.* ORDER BY CURRENT_TIME ASC NULLS FIRST) & CASE 
```

---

## Crash 24: `66a4c1a12895b22e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007665`

```sql
SELECT round(1e308, 4294967296); SELECT printf('%.*e', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t3 VALUES (CURRENT_DATE IS NOT NULL) RETURNING p.*; ANALYZ
```

---

## Crash 25: `0a5b4ba77c5b85ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007823`

```sql
SELECT round(-0.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c1, _rowid_); INSERT OR FAIL INTO p VALUES (CURRENT_DATE LIKE NULL ESCAPE RAISE(IGNORE),
```

---

## Crash 26: `561e1da9be603b7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010288`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 27: `de642fa4f5957f6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010296`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN
```

---

## Crash 28: `0c77ad7019e97461` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010302`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 29: `8a80262217d830e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010323`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL J
```

---

## Crash 30: `2d6e01d2ca9b1f70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010344`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 31: `77199ce6e277494f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010357`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.
```

---

## Crash 32: `8cb2fa8a2436f8e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010364`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 33: `3f718f05533cf286` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010378`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 34: `5a302f26fcfeee1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010388`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE, _rowid_ DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 35: `cdf9efebe133114a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010395`

```sql
SELECT printf('%.*s', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 36: `a4ff1ba5f9f7f10a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010401`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 37: `5b360bb5c04f3982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010426`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_each('{}') JOIN t1 NOT INDEXED USING (b) ORDER BY TRUE; INSERT INTO p DEFAULT VALUES; PRAGMA quick_che
```

---

## Crash 38: `9e5f16ea74d8875b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010433`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL 
```

---

## Crash 39: `58bbc0dd71ab53c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010459`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JO
```

---

## Crash 40: `5fa6c52af169eab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010467`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 41: `6a183f101e071e1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010482`

```sql
SELECT printf('%.*g', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 42: `f17644d5d39e1816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010497`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 43: `4f72a170281c7f0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010507`

```sql
CREATE TABLE IF NOT EXISTS p(a INT DEFAULT -9668.35291524e-2697945799972973980000); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 44: `86a1e21a83fef3e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010531`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JO
```

---

## Crash 45: `bd7db1ff93aca733` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010550`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT 184618); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed
```

---

## Crash 46: `d485e3b0bc8ad092` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010563`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 47: `7b9e57896fcd4149` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010569`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 48: `ea095d192275fafd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010578`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 49: `5061853363c1dd02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010596`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 50: `ff41bf8b5d34c904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023171`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(le
```

---

## Crash 51: `2f7b6537bff8e481` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023180`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 52: `b27bba7cebcae56a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023195`

```sql
SELECT printf('%.*s', -2147483648, -1e308); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 53: `7ce8d759f354b926` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023208`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (TRUE <= CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = se
```

---

## Crash 54: `3eede4fa141c4283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023216`

```sql
SELECT printf('%.*d', 4294967296, -1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 55: `bc00861e3743be0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023614`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO q VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIME); PRA
```

---

## Crash 56: `ca97363f648a654c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023804`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT ''); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 57: `c8c6fe75813275b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023810`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (), CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 58: `29c6b857f51cafba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023839`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP)))
```

---

## Crash 59: `2a9b79e39f3f5ebe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024758`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT X'03DA175fFBbb', c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 60: `e422e43afb8777ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024764`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT 'h', c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 61: `a60bb6c2d179f00b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024771`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); 
```

---

## Crash 62: `d05bb651e462a4ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024779`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c3 FLOAT NOT NULL, c1 BOOLEAN GENERATED ALWAYS AS (RAISE(IGNORE)) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE);
```

---

## Crash 63: `25898887d37a2564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024795`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT 432.3853563735e-7, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 64: `483b4baf2de98d14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024807`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT -24088816421732944948.0E+81, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 65: `e426eb1cda133756` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024813`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IS CURRENT_TIMESTAMP); CREATE TABLE seed_a(c UNIQU
```

---

## Crash 66: `f4f9cffc928cf783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024835`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE IN (NULL) == CURRENT_TIME IS TRUE); CREATE TABLE seed_a(c 
```

---

## Crash 67: `e434037a95819715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024841`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 68: `c509a0c173829ae0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024852`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (CURRENT_TIMESTAMP OR NULL), c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELEC
```

---

## Crash 69: `aceb4c02cbb14e52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024873`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE = CAST(CURRENT_DATE AS INT)); CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 70: `1595d0d1fa25aaa6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024905`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT s
```

---

## Crash 71: `f0a8f46a505553d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024916`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT NULL, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_
```

---

## Crash 72: `38edcd220d65d41a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024997`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT X'dd69BecD2A', c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 73: `ac8f843cd5a43562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025003`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 IN
```

---

## Crash 74: `c9de087484f4aa09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026540`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH RECURSIVE p (c2) AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b
```

---

## Crash 75: `097c94af8b5647a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 76: `229d8627c1a0b6ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028245`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 77: `6e56b0650a2d2d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028261`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 78: `ffc2003d84552ed1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032329`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIME, TRUE WINDOW w1 AS () INTERSECT SELECT * FROM json_tree('[{"a":1},{"b":2}]');
```

---

## Crash 79: `f44d9eabb0125cdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032339`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIME, TRUE WINDOW w1 AS () INTERSECT SELECT ALL * FROM (json_tree('{}')); CREATE T
```

---

## Crash 80: `e065bb9706294043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032348`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT CURRENT_DATE ORDER BY RAISE(IGNORE) DESC NULLS LAST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_
```

---

## Crash 81: `29be2b75d8ef36a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032480`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_each('{"a":{"b":1}}'); 
```

---

## Crash 82: `00509afb06a394d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033205`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT FALSE, c2 REAL); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 83: `91508b81f954d7f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033542`

```sql
SELECT printf('%.*f', 4294967296, -1e308); CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SEL
```

---

## Crash 84: `e4a03708362244ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034606`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); SELECT * FROM (SELECT percent_rank() OVER () AS w_n_7nq FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 85: `146dd58da66d39d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035099`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT 2.794376690349); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c U
```

---

## Crash 86: `02c94cd340f3f9f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037259`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_b(b INTEGER); INSE
```

---

## Crash 87: `3f741b93303692a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037272`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_b(b INTEGER); INSE
```

---

## Crash 88: `f9b671873a0ee5b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039897`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) EXCEPT SELECT * FROM q WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (); VALUES (TRUE); CREATE
```

---

## Crash 89: `1254dea334303e6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039907`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) EXCEPT SELECT * FROM json_tree('{"a":{"b":1}}') INNER JOIN (q) ON RAISE(IGNORE) WHERE CURRENT_TIMES
```

---

## Crash 90: `efa8a8a308b5dff7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040659`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOI
```

---

## Crash 91: `d87c1f223c20607c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040693`

```sql
SELECT substr('', -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) F
```

---

## Crash 92: `5117d26c4bed809a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042586`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT -CURRENT_TIMESTAMP, -CURRENT_TIMESTAMP FROM (SELECT CURRENT_TIME FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); 
```

---

## Crash 93: `f6b8b85f6fe6f0f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042611`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT +FALSE <= FALSE FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 94: `1c19a3375e9514c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042623`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP ELSE CURRENT_DATE END) AS sub1; CREATE TABLE 
```

---

## Crash 95: `f7523ea17332f69c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042630`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIMESTAMP BETWEEN TRUE % 0 AND NOT CURRENT_DATE FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNI
```

---

## Crash 96: `87900fb993dc1256` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042637`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE json_array(FALSE)) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed
```

---

## Crash 97: `3568cc2bed757e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042679`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X'fDBaA61Abbe4', c1 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREA
```

---

## Crash 98: `9a94092cce1114db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042686`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (changes(), CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a W
```

---

## Crash 99: `8dd94f69b74ff4fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042692`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT EXISTS (VALUES (CURRENT_TIMESTAMP)) FROM (SELECT CURRENT_TIME FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SEL
```

---

## Crash 100: `ee20bf707df79c57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042712`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, c3 GENERATED ALWAYS AS (c1) NOT NULL UNIQUE, c1 TEXT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c U
```

---

## Crash 101: `f55fb41781fb99b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042848`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT a FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 102: `65551b8c879ad0ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042916`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p DEF
```

---

## Crash 103: `fa2b6f29ffe1651f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042934`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); WITH p 
```

---

## Crash 104: `ca8f8499ec2972fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042959`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT 
```

---

## Crash 105: `9bcbca4a2e7c0ef3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043442`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); VALUES (FALSE || NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_
```

---

## Crash 106: `a2918690fb318320` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047020`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT '-C 01', c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELE
```

---

## Crash 107: `d67d3049dc681849` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050023`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT -0, c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON
```

---

## Crash 108: `98a2a34536f2a346` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050052`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT '-C 01', c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT +CURRENT_TIMESTAMP NOT IN (VALUES (NULL)) FROM json_each('[]'); CREATE TABLE se
```

---

## Crash 109: `546794af6f990cc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050083`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT '-C 01', c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT DISTINCT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE TABLE seed_a(c UNIQUE); 
```

---

## Crash 110: `cbcd4c40dc4ed40b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050121`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT DEFAULT '  -tN', c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a
```

---

## Crash 111: `985020bc9ac861a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050220`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(NULL AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN see
```

---

## Crash 112: `89cc2c58066ac8ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050227`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(CURRENT_DATE <= NULL AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c 
```

---

## Crash 113: `83ea190e5ecd5528` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050235`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(CURRENT_DATE <= CURRENT_DATE & NULL >> CURRENT_DATE AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 114: `351b5fa30abdab52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050258`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(CURRENT_TIMESTAMP AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NAT
```

---

## Crash 115: `6a3f36f0d8a8f198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050264`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(CURRENT_DATE <= FALSE AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 116: `59286afc635bd08a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050270`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); VALUES (CAST(CURRENT_DATE <= CURRENT_TIMESTAMP >> CURRENT_DATE AS DATE), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 117: `b5f05dbacdf552f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050929`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (NULL IS NOT CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a
```

---

## Crash 118: `ace2869b27ad52ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051763`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (TRUE <= CURRENT_TIMESTAMP)); INSERT INTO p VALUES ((SELECT CURRENT_TIME FROM json_each('{"a":1}') LEFT OUTER JOIN json_tree('{"a":{"b":1}}') LEFT JOIN p WHER
```

---

## Crash 119: `5056f09bd279bebe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052362`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT X'f74FF59C0eDd'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a F
```

---

## Crash 120: `50a711c891683799` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053334`

```sql
SELECT printf('%.*e', -2147483649); CREATE TABLE IF NOT EXISTS p(b TEXT CHECK (random())); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 121: `596a137e72675e4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055486`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); VALUES (NOT NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 =
```

---

## Crash 122: `0fb4c1254efa1e2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055831`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE | FALSE NOT LIKE CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NA
```

---

## Crash 123: `ee800ded65f84fc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055854`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (FALSE || FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed
```

---

## Crash 124: `b5422afaeb6ba293` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058295`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE json_quote(CAST(CURRENT_DATE AS INT))) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c F
```

---

## Crash 125: `a7f7560496f16419` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058305`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE json_array(92.01E+38, CURRENT_DATE)) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 126: `14e2ec15f590e4ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058311`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT 0); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c
```

---

## Crash 127: `ecf2ee469997bc5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058343`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE changes()) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 
```

---

## Crash 128: `be5adad5ecfbaff6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058351`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE json_replace('[1,2,3]', '$[#-1]', NULL)) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 129: `4515b0279726ea92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058483`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE json_array(json_array(FALSE))) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 130: `675ef1ba1a40bf9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058559`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT p.a FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3
```

---

## Crash 131: `97b4a95b4e410322` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058618`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME COLLATE RTRIM FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM se
```

---

## Crash 132: `24c3ea346e6b2ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 BLOB); SELECT * FROM (SELECT * FROM p WHERE NULL IS NOT CURRENT_DATE) AS sub1; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 133: `0d62c57ecfe96246` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058756`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 134: `5691f6ad34260006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058762`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); SELECT DISTINCT CURRENT_TIMESTAMP FROM json_tree('{"a":1}') INTERSECT VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_a
```

---

## Crash 135: `94477afe7b518736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059174`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP 
```

---

## Crash 136: `21f2fd08809eaf7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061396`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, c1 FLOAT PRIMARY KEY); INSERT INTO p (c3) VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NOT INDEXED LEFT JOIN json_tree('[{"a":1}
```

---

## Crash 137: `627f98379fc350e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061737`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); INSERT INTO
```

---

## Crash 138: `060259960810b254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063836`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p CROSS JOIN json_tree(NULL, '$') NATURAL JOIN json_each('[1,2,3]') ORDER BY TRUE DESC NULLS LAST LI
```

---

## Crash 139: `dfbf7aeefed10ecd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063851`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) EXCEPT SELECT * FROM json_tree('{"a":{"b":1}}') INNER JOIN (q) ON random() OVER (ORDER BY CURRENT_T
```

---

## Crash 140: `6a2ee27cfdd8bb77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063858`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) EXCEPT SELECT * FROM json_tree('{"a":{"b":1}}') INNER JOIN (q) USING (a, c3) WHERE CURRENT_TIMESTAM
```

---

## Crash 141: `767a256a18db5f3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063865`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE) EXCEPT SELECT * FROM json_tree('{"a":{"b":1}}') INNER JOIN (q) ON EXISTS (SELECT * FROM json_tree('
```

---

## Crash 142: `eb732826a66abe58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063911`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED LEFT JOIN json_tree('[{"a":1},{"b":2}]') ON TRUE WHERE RAISE(IGNORE) GROUP BY NULL WIN
```

---

## Crash 143: `cc8b312111426ce3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067529`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a TEXT,
```

---

## Crash 144: `2d941c8aa8ea9ca1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068181`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT -88913762816214056768128.265e518215); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE 
```

---

## Crash 145: `188795046e03936b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070663`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X'7dDbe9D3bc', c1 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(_r
```

---

## Crash 146: `d2c5246353b3310d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077285`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () UNION ALL SELECT * FROM json_tree('[{"a":1},{"b":2}]'); 
```

---

## Crash 147: `e7ce9655a7bc8a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077299`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]') NATURAL JOIN (json_tree('[]')) WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELEC
```

---

## Crash 148: `ffad32439676752b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077308`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM (SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS ()) AS a WHERE NULL GROUP BY CURRENT_TIMESTA
```

---

## Crash 149: `abfae09624aa789a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077347`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELECT * FROM json_tree('[{"a":1}
```

---

## Crash 150: `05cceedaadf10e1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077476`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_tree(NULL, '$'); CREATE
```

---

## Crash 151: `ab22e16f45a8d799` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077501`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE EXISTS (VALUES (NULL)) >= CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELECT ALL *
```

---

## Crash 152: `535cec5a0a177be7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077512`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY RAISE(IGNORE) ORDER BY CURRENT_DATE RANGE BET
```

---

## Crash 153: `294ccc6638f367ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077527`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE HAVING CURRENT_DATE WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_each('{"
```

---

## Crash 154: `710b9e1e06befc0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077663`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NOT FALSE AND FALSE / NULL GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_t
```

---

## Crash 155: `f638b7f4d00eb5e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077697`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE HAVING FALSE WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_tree('{}'); CRE
```

---

## Crash 156: `b8cd9a8f755850bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077719`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE HAVING FALSE AND FALSE WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_tree(
```

---

## Crash 157: `235947e6408aaa31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077743`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') WHERE NULL GROUP BY NOT TRUE > FALSE WINDOW w1 AS () INTERSECT SELECT ALL * FROM json_tree('{}'); CREATE TABLE
```

---

## Crash 158: `db7fc311687b5880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085544`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT sum(CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN CURRENT_TIME PRECEDING AND TRUE FOLLO
```

---

## Crash 159: `baa365a4713992bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085551`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT -CURRENT_TIMESTAMP, -CURRENT_TIMESTAMP FROM p NOT INDEXED WHERE RAISE(IGNORE) GROUP BY CURRENT_DATE HAVING FALSE WIND
```

---

## Crash 160: `02b1261751804b21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085904`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (CURRENT_TIMESTAMP), b TEXT CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; C
```

---

## Crash 161: `03570c5096eba90a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086314`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (FALSE || FALSE > CURRENT_DATE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN s
```

---

## Crash 162: `a9a150a35f3a5c7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087282`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) NOT NULL); SELECT CURRENT_TIME AS a FROM p WHERE EXISTS (SELECT * FROM json_each(CAST(CURRENT_DATE AS DATE) >> NULL + FALSE, '$[#-1]')); CREATE TABLE se
```

---

## Crash 163: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001938`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 164: `654274cc95b1fa6f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002139`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM (jsonb_tree('{"a":{"b":1}}') INNER JOIN json_tree('{}') LEFT OUTER JOIN p INDEXED BY c2) NATURAL
```

---

## Crash 165: `1e581fdd5b2717ff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 166: `982f778ccbf8254c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002220`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (~FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO s
```

---

## Crash 167: `e52ded4f7e04bc66` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002253`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT 
```

---

## Crash 168: `146398a16d8a096a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002430`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed
```

---

## Crash 169: `3819107da81b199e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002442`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 170: `6451de3410dd71bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002479`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT 
```

---

## Crash 171: `7a9c77bd6e9ef58c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002635`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT 
```

---

## Crash 172: `1c34dfaa6f6a6d9f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004125`

```sql
CREATE TABLE seed_t0 (c0 INTEGER, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0)); INSERT INTO seed_t0(c0) VALUES (0); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372
```

---

## Crash 173: `8dd0c7b106c37b83` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005611`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 174: `e41c97810c98eeb4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006239`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER);
```

---

## Crash 175: `121c1cad1d2406a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000006440`

```sql
SELECT round(1e308, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 176: `2c04dd8b1eba6f5a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME != CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 
```

---

## Crash 177: `7b18583c3676c025` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008333`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(
```

---

## Crash 178: `bdab642d5bf27614` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008340`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 179: `d5caecbfed769055` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE T
```

---

## Crash 180: `1bfbb545d91cb02a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008385`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT -CURRENT_TIMESTAMP, TRUE AS ck2__4_x6k7_lx37p_nmwl_o_xa_; CRE
```

---

## Crash 181: `f40e6479cca98a40` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008400`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP NOT NULL AS x; CREATE TABLE seed_t1(c1 INTE
```

---

## Crash 182: `5feab0d6c979c201` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008418`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq
```

---

## Crash 183: `c4394fe932f7ebb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008435`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY NULL WINDOW w
```

---

## Crash 184: `79d20773e86dee5d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008442`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE FALSE GROUP BY CURRENT_DATE HAVING NULL; CREAT
```

---

## Crash 185: `3af0d0c6a8f85139` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008583`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE FALSE GROUP BY CURRENT_DATE HAVING NULL; CREATE TABLE seed_t1(c1
```

---

## Crash 186: `be985a7ddcc8e6cf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008612`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY NULL WINDOW w1 AS (
```

---

## Crash 187: `f720fa6a27745993` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008618`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY NULL WINDOW w1 AS (
```

---

## Crash 188: `3a7790dc1b140fe2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008662`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h5
```

---

## Crash 189: `1d897bdb233d8989` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008687`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT -CURRENT_TIMESTAMP, TRUE AS ck2__4_x6k7_lx37p_nmwl_o_xa_; CREATE TABLE seed_t1(c1 
```

---

## Crash 190: `35d6b3004c5484c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000008744`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME != CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 191: `c3e49a8e30f5747f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010416`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE
```

---

## Crash 192: `275fb888a989f67a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012590`

```sql
SELECT printf('%.*g', 2147483648, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 193: `4d847015f6057bab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012596`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 194: `cf5a5170317e01af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012615`

```sql
SELECT printf('%.*d', -2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 195: `5f2c7ee1f1653f35` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012623`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 196: `bfaed22d4dc86453` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012631`

```sql
SELECT round(1e308, -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TAB
```

---

## Crash 197: `e0eb8be67fba7269` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012657`

```sql
SELECT printf('%llu', -2147483649, 'P_ B___t  -_-_'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(5
```

---

## Crash 198: `aca4d2266bcd128e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012674`

```sql
SELECT substr('Xqh5 Y 2 M-', -2147483649); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 199: `eae90b02d4fa7670` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012734`

```sql
SELECT printf('%.*s', 1); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_
```

---

## Crash 200: `ff17af1400224ddd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013186`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT count() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND C
```

---

## Crash 201: `36fe63f45a1e237d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013248`

```sql
SELECT substr('', -2147483648, -2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 202: `2af69cf2dfe7c21f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013372`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM json_each('[]') ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 203: `ca6578ef305cfd10` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013380`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT count() OVER () FROM json_each('[]') ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE TABLE seed_t1(
```

---

## Crash 204: `c2fa9596342dc750` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013471`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT cume_dist() OVER () FROM json_each('[]') ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE TABLE seed
```

---

## Crash 205: `d8522238fb46227a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013478`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 206: `249aaeff630525f5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000013490`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP < CURRENT_TIME FROM p NOT INDEXED LEFT JOIN json_tree('[{"a":1},{"b":2}]') ON TRUE ORDER BY CURRENT
```

---

## Crash 207: `13c1f0516f0a5218` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016375`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each(CURRENT_DATE, '$[#-1]') ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE T
```

---

## Crash 208: `f1203e1783fffebc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016426`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT 81260); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 209: `f3f98f1705f374e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016449`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM (json_tree('{}')) ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 210: `9945762ed1b8029b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016566`

```sql
SELECT printf('%.*e', 9223372036854775807, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 211: `e31a04516a85421d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017466`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE << row_number() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 212: `9573694ae58c9af6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017473`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME <= CURRENT_TIMESTAMP, CURRENT_TIME, CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 213: `0d8b9276325008a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017480`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT cume_dist() OVER (ORDER BY TRUE DESC NULLS LAST, CURRENT_TIMESTAMP ASC NULLS LAST) FROM json_each('[]'); CREATE TABLE se
```

---

## Crash 214: `a5e5944c50452bd5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017486`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IN (TRUE)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 215: `035c135e3fb53dd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017508`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE << CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP ELSE FALSE END); CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 216: `8bd4cdaf5225da14` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017541`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE << CURRENT_DATE > NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 217: `c1680cbc5f899ad4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017549`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (count(DISTINCT FALSE) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 218: `3fccb199b6b34e2a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017568`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE IS NOT NULL | CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 219: `8b0227f9507e3322` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017600`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE << NULL IS NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed
```

---

## Crash 220: `9cfd54b6204aed8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017702`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (X'C13a'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGE
```

---

## Crash 221: `fb31325e40643d15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017728`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME = CURRENT_DATE < CURRENT_TIME MATCH CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 222: `ee31ac19c61bd1c5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017749`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(123
```

---

## Crash 223: `c46897f5621dd97b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020119`

```sql
SELECT round(0.01, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 224: `ffbadcc363f10c8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020175`

```sql
SELECT printf('%.*e', -2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); 
```

---

## Crash 225: `13a39495c2300639` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020186`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT CURRENT_TIMESTAMP, c1 FLOAT PRIMARY KEY); INSERT INTO p (c3) VALUES (CURRENT_TIMESTAMP); VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 226: `1af7ac4bbba8f73c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020591`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL DEFAULT X'3e5D'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 227: `446fbe46d0500fc2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024824`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT FALSE, c2 INT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); 
```

---

## Crash 228: `192a003fb72252f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026870`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p (c1) VALUES (CURRENT_TIME) ON CONFLICT(c1) DO UPDATE SET _rowid_ = 
```

---

## Crash 229: `ddeb383b358c2fb0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026902`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 230: `3be210be72986e13` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000026948`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT CURRENT_TIMESTAMP, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 231: `1866fc56bc9c6cd8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035328`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE % CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 232: `40b46b32157ca987` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000035335`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT -24088816421732944948.0E+81); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE
```

---

## Crash 233: `de41832a013b6579` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040483`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_DATE IS NOT NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t
```

---

## Crash 234: `615f59b76e5b22cc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040492`

```sql
SELECT printf('%x', 9223372036854775807, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123)
```

---

## Crash 235: `5230de4e64bb09c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040506`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('[]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(
```

---

## Crash 236: `a96155d314dd37a9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040523`

```sql
SELECT substr('', -9223372036854775808, -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALU
```

---

## Crash 237: `a7e781ff05d144dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041800`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 238: `67c0a3d52fa91bb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041847`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 239: `f5aa3dce5b7e7d55` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041853`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 240: `14923b4ab77bda24` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041884`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (TRUE IN (NULL) == CURRENT_TIME IS TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE
```

---

## Crash 241: `83f4ffaf65096900` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041926`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) NOT NULL, a NUMERIC DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 242: `ba023fcf5068da1d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041976`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) NOT NULL, a TEXT); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 243: `da1b8d447edf4362` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043345`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT TRUE AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc6__1_7ux6_66_2zt22__g1ef_
```

---

## Crash 244: `3052e0a1fe54e3b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043537`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 245: `14dffc970ea68eae` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043545`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 246: `7d5cd6a678916ad0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043554`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 247: `0fedc6d3952b46e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043576`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 248: `05107b9feff6a197` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043582`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS 
```

---

## Crash 249: `fa93c3a6cf443ff5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043589`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125_n__26r491zn___pxc
```

---

## Crash 250: `5199c302ad790e58` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043605`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_DATE IN (CURRENT_TIMESTAMP) IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1_125
```

---

## Crash 251: `a97372d5dc45492a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043629`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT CURRENT_TIMESTAMP IS NOT NULL AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6
```

---

## Crash 252: `88ded246820e5db9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000043732`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT CURRENT_TIMESTAMP IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL
```

---

## Crash 253: `2bb0b7b63c383860` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044439`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (row_number() OVER (ORDER BY TRUE DESC NULLS LAST, CURRENT_TIMESTAMP ASC NULLS LAST)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 254: `09b8cca9a7985737` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044448`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER);
```

---

## Crash 255: `a07cf3459bbee98f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044462`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (FALSE) VIRTUAL, rowid INT); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INT
```

---

## Crash 256: `ff4cf34f1b8ac05d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044468`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (TRUE = CAST(CURRENT_DATE AS INT), CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE 
```

---

## Crash 257: `7c758b0e780d61b1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044474`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CAST(CURRENT_DATE AS INT), CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 258: `fba83313837bafd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044498`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (dense_rank() OVER (), EXISTS (VALUES (FALSE))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 259: `7840e4f984456918` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044504`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT ALL * FROM json_each('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 260: `fd2b10e8cb68f06e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044524`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (-FALSE = CURRENT_TIME, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_
```

---

## Crash 261: `dd2d79da0849b4f6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044546`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 262: `2773bcaf07360554` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000044610`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE / NULL, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INT
```

---

## Crash 263: `8a23f17e15a08829` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049550`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP < -TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER
```

---

## Crash 264: `e6a82ac755caa969` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053879`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (sum(CURRENT_TIMESTAMP) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2
```

---

## Crash 265: `16c897dd5dea4a54` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053886`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (row_number() OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW)); 
```

---

## Crash 266: `9e185933c6665fd3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053897`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (cume_dist() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); 
```

---

## Crash 267: `eaf6ce0e24e27924` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053904`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (max(NULL) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); IN
```

---

## Crash 268: `dcd275c253ebe863` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053910`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (row_number() OVER (PARTITION BY CURRENT_TIME ORDER BY NULL ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS)); CREATE
```

---

## Crash 269: `c10f2f5145434c59` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053926`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a, rowid, c1); VALUES (row_number() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 270: `caa8e5b65557dee9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053951`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT dense_rank() FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECE
```

---

## Crash 271: `3d549f472c438132` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053961`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (percent_rank() OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER
```

---

## Crash 272: `ee8cd203d043340b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000053978`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (count(DISTINCT CURRENT_TIME), CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABL
```

---

## Crash 273: `260224ade0b117c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054140`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IS TRUE IN (NULL, CURRENT_DATE) == CURRENT_TIME IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 274: `89b12f4eab29a71a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054149`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a IS NULL) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 275: `4c2c0ef1f64d3394` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054157`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (X'62A12f' IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); IN
```

---

## Crash 276: `04a59f1e65489773` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054171`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IS CURRENT_DATE GLOB FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 277: `b37eed11b3bed6f0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054188`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM json_tree('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CRE
```

---

## Crash 278: `1366b8ca6eca34b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054195`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE * CURRENT_TIMESTAMP IS CURRENT_TIMESTAMP IS NULL IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123)
```

---

## Crash 279: `67b2e0a075c50ab1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054208`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (RAISE(IGNORE) LIKE RAISE(IGNORE))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME IS TRUE); CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 280: `e40379f8e9ca181a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054222`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (-FALSE AND FALSE IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEG
```

---

## Crash 281: `04c4a4f99e511b41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054345`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS TRUE IS
```

---

## Crash 282: `471fb006457b2285` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054353`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT_TIME IS CURRENT
```

---

## Crash 283: `15587c50711c0a64` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054395`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (TRUE IS FALSE IS TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER)
```

---

## Crash 284: `ea0b78150e53bafe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054761`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') NATURAL LEFT JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 285: `3f9fdc3076a11416` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054768`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT CURRENT_TIMESTAMP, * FROM json_each('[1,2,3]') , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUE
```

---

## Crash 286: `527b29e20bd26b57` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054787`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('{"a":1}') , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 287: `16589ed2b46b1b43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054795`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[{"a":1},{"b":2}]') , json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 288: `4a5c14ecbd4caaf7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054819`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') LEFT OUTER JOIN json_tree('{"a":{"b":1}}'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12)
```

---

## Crash 289: `d30bfb3cc05fec67` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054836`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_DATE) EXCEPT SELECT sum(CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN CURRENT_TIME PRECEDING AND 
```

---

## Crash 290: `c69ddd77828de7a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054866`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT * FROM json_each('[1,2,3]') , json_tree('[1,2,3]'); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREAT
```

---

## Crash 291: `dce843ce2a8ca745` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000054988`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT -CURRENT_TIMESTAMP, -CURRENT_TIMESTAMP FROM json_tree('[]') JOIN json_tree('{"a":{"b":1}}') NATURAL JOIN p NOT INDEXED; CREATE TABLE see
```

---

## Crash 292: `00ca86879336c82c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055002`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X'7dDbe9D3bc', c1 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 293: `f3af7154edf0a2fa` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055147`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (EXISTS (SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST LIMIT FALSE, TRUE)); CREATE TABLE se
```

---

## Crash 294: `054ab3068d9cc2f3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055159`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE / CURRENT_DATE COLLATE BINARY, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 295: `e06ddecac12002b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055166`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIME COLLATE RTRIM) EXCEPT VALUES (CURRENT_TIMESTAMP))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 296: `ee745c990723d128` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055202`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (NULL IS NOT CURRENT_DATE / NULL, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 297: `967b94e1428fb230` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055208`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (max(CURRENT_TIMESTAMP)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER
```

---

## Crash 298: `6782cfc70f7de525` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055238`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (NOT FALSE AND FALSE <= CURRENT_DATE / NULL, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234
```

---

## Crash 299: `547f668aa12ec085` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055355`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (FALSE / NULL / NULL / NULL, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 300: `43480658d09af6fb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055393`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_tree('[]') WHERE -CAST(CURRENT_TIME AS BLOB); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123
```

---

## Crash 301: `8c046483cc9accc0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055403`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT NULL != CURRENT_TIMESTAMP - ~CURRENT_TIME AS a FROM json_tree('[]') WHERE -CAST(CURRENT_TIME AS BLOB); CREATE TABLE seed_t1(c1 
```

---

## Crash 302: `0a7782a4a0d66e33` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055409`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT NULL != NOT EXISTS (VALUES (FALSE)) - ~CURRENT_TIME AS a FROM json_tree('[]') WHERE -CAST(CURRENT_TIME AS BLOB); CREATE TABLE s
```

---

## Crash 303: `2237326a24822061` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000055520`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); VALUES (NOT FALSE AND FALSE <= CURRENT_DATE, CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREA
```

---

## Crash 304: `a4ca02608b7f86a8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000056874`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIMESTAMP OR NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEG
```

---

## Crash 305: `7542854c54b96ccc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057021`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT EXISTS (SELECT * FROM json_tree('[1,2,3]') WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY percent_rank() OVER (ORDER BY CURRENT_DATE D
```

---

## Crash 306: `0beaf823da810875` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057031`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (ORDER BY FALSE ROWS BETWEEN TRUE PRECEDING AND c3 FOLLOWING) AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__u
```

---

## Crash 307: `10d2e9782fe323f8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057043`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS 
```

---

## Crash 308: `68d33f991a66a57a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057053`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY TRUE IN (NULL, CURRENT_DATE) == CURRENT_TIME IS TRUE ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDIN
```

---

## Crash 309: `e1918a34ec79bef6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057087`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS 
```

---

## Crash 310: `fe63e37a1e08386a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057097`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY TRUE COLLATE RTRIM ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHER
```

---

## Crash 311: `798df0c99546f762` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057105`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS 
```

---

## Crash 312: `da0ba39319e94b70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057111`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN CURRENT ROW AND CURRENT_DATE FOLLOWING) AS a9_nnn___991_0_5e_04
```

---

## Crash 313: `1830046915868cd0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057120`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS 
```

---

## Crash 314: `254d01036c09aef0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057126`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT rank() OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_DATE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS) AS a9_nn
```

---

## Crash 315: `f67bc6715286d4c4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000057143`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c1 AS(c1) UNIQUE); SELECT cume_dist() OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST ROWS BETWEEN CURRENT_TIME PRECEDING AND TRUE FOLLOWING) AS a9_nnn___991_0_5e_04_
```

---

## Crash 316: `c4bf664f57171c1b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE TRUE > FALSE COLLATE RTRIM; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 317: `643040c959e1c53b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060371`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) UNIQUE, a NUMERIC DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 318: `9b1cf1f5f84c2869` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060381`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a NUMERIC DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 319: `b55e1c5ff4aee01f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060391`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), b GENERATED ALWAYS AS (a) NOT NULL, a NUMERIC DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 320: `292555ed8a72f790` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060416`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) NOT NULL, a NUMERIC DEFAULT -3881.9); SELECT p.*, * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 321: `60b1988c1bad441b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060444`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a) NOT NULL, a BLOB DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 322: `c7f63688fedc5877` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060497`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER, b GENERATED ALWAYS AS (a + 426010) NOT NULL, a NUMERIC DEFAULT -3881.9); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 323: `f34a954450daf668` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000061226`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, c1 AS(c1) UNIQUE); WITH RECURSIVE q (c2) AS (SELECT *) SELECT CURRENT_DATE AS a9_nnn___991_0_5e_04______eq0__r57mko0h548h5_96h___5__uyv___0_9___dy6_____9d_0q_i1
```

---

## Crash 324: `4abaea572f7e8508` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062789`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT CURRENT_DATE FROM json_each('[]') ORDER BY CURRENT_DATE ASC NULLS LAST; CREATE TABLE seed_t1(c1 IN
```

---

## Crash 325: `2ef90aae76353146` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000064116`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_DATE AS x FROM p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 326: `395496953321b1b8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066898`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIME COLLATE RTRIM) EX
```

---

## Crash 327: `55917fdcfed64173` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067134`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIMESTAMP) EXCEPT VALU
```

---

## Crash 328: `19e2903e0514805b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067140`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IN (VALUES (NULL) EXCEPT VALUES (CURRENT_T
```

---

## Crash 329: `d117e0eee2e9498b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067769`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NU
```

---

## Crash 330: `e2572d5315ca2360` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068267`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b)
```

---

## Crash 331: `87bff7a114de53dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068343`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (TRUE IN (NULL) == CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE 
```

---

## Crash 332: `841e9e46c26a8a99` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072469`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP FROM p NOT INDEXED LEFT JOIN json_tree('[{"a":1},{"b":2}]') ON CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 333: `bfb312da1d2f1d08` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000072491`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); VALUES (FALSE NOT BETWEEN NULL AND CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE
```

---

## Crash 334: `4994e94f45406a0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075842`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT 81260); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); INSE
```

---

## Crash 335: `141a1afb5783984e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075957`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); I
```

---

## Crash 336: `80dd74897475dbb2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084286`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (count(DISTINCT CURRENT_TIME), count(DISTINCT CURRENT_TIME), FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 337: `e480c5e337d87e85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084530`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (count(), count(DISTINCT CURRENT_TIME), count(DISTINCT CURRENT_TIME), CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 338: `30981c75c0f1d8e8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084906`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIME FROM json_each('{"a":1}') LEFT OUTER JOIN json_tree('{"a":{"b":1}}') LEFT JOIN p WHERE CURRENT_DATE; CRE
```

---

## Crash 339: `03f08ec27cf0a3b6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084950`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') ORDER BY TRUE DESC NULLS LAST LIMIT TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO s
```

---

## Crash 340: `841b398408c07505` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000084956`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_TIME FROM json_each('{"a":1}') NATURAL JOIN json_tree('{"a":{"b":1}}') LEFT JOIN p WHERE CURRENT_DATE; CREATE
```

---
