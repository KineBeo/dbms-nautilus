# Crash Triage Report

**Total crashes:** 123  
**Unique crash sites:** 123  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 123 | 123 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `3b052b6a45fc5d55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000150`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (hex(FALSE AND CURRENT_DATE IS NULL) FILTER (WHERE NOT last_insert_rowid() || +last_value(NOT CURRENT
```

---

## Crash 2: `5ed43bdc6a90536e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000168`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3); INSERT OR ABORT INTO q VALUES (CURRENT_TIME -> changes() IS NOT NULL <> FALSE ->> NULL >> RAISE(IGNORE) -> CURRENT_TIME COLLATE RTRIM,
```

---

## Crash 3: `6dc20cf6cb502864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000467`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (CASE CURRENT_TIME COLLATE BINARY WHEN CURRENT_TIME THEN +TRUE END, -CURRENT_TIME COLLATE BINARY > 0.0, CURREN
```

---

## Crash 4: `e1ad483086f1b7ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000946`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c2, c1, b, c1); INSERT INTO p (_rowid_, c1) VALUES (NULL AND NULL + NULL MATCH CURRENT_TIMESTAMP ISNULL & CASE CURRENT_DATE >> CASE WHE
```

---

## Crash 5: `13910361a85e9a7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001106`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO p (c2) VALUES (+RAISE(IGNORE) COLLATE NOCASE, CURRENT_TIME) ON CONFLICT(c1) DO UPDATE SET c1 =
```

---

## Crash 6: `77ad39d75bbb75c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001245`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (typeof(TRUE) FILTER (WHERE NULL) * (WITH RECURSIVE p AS NOT MATERIALIZED (
```

---

## Crash 7: `813887901924b234` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001311`

```sql
SELECT printf('%.*s', 2147483647, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIMESTAMP + CURRENT_TIMESTAMP AS l3_5, * FROM json_each((NULL), '$.a[#-1]') CROSS JOIN 
```

---

## Crash 8: `9c63b4b13d58fb55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007077`

```sql
SELECT substr('hj W__--', 4294967296); SELECT substr(' _', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO s VALUES (CASE (CURRENT_DATE) WHEN CURRENT_TIMES
```

---

## Crash 9: `55d4ebce6da1cb6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007221`

```sql
SELECT substr('8V54Mp', 0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * LIMIT (FALSE) IS DISTINCT FRO
```

---

## Crash 10: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007589`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 11: `06cbc68d59ba5923` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007787`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO q VALUES (+CAST(RAISE(IGNORE) / ~TRUE COLLATE BINARY -> CURRENT_TIMESTAMP == FALSE AS VA
```

---

## Crash 12: `d6af88c4e3546a05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010633`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CAST(CURRENT_TIMESTAMP AS REAL)) 
```

---

## Crash 13: `16fe19bd5ac28f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011752`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 14: `8c19432c7d1b4610` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016075`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE >= -CURRENT_DATE < FALSE, CURRENT_DATE); EXPLAIN QUERY PLAN VALU
```

---

## Crash 15: `d72d156eef933c71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018230`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE FALSE || TRUE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 16: `cbe22015a035a4df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019034`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); SELECT DISTINCT TRUE AS x, RAISE(IGNORE) NOTNULL AS g3___aat8_c0e5xt1q9__48fe0, r.* FROM json_ea
```

---

## Crash 17: `20ab5fd76d86b6b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019107`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN PRIMARY KEY); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT -TRUE NOT BETWEEN
```

---

## Crash 18: `64bec6103f0763cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019471`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 19: `498633cba2f3b6cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019541`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (+CURRENT_DATE << NOT NULL | RAISE(IGNORE) IS NOT NULL % -NULL LIKE CURRENT_DATE > CAS
```

---

## Crash 20: `cefe09d48bcd7ee7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020335`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE = NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 21: `f6dbc624019b1f0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020487`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 22: `bb17d398bcb83da7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020803`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY, c3 BOOLEAN UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT substr('5hg_ 7iR9', 2147483647)
```

---

## Crash 23: `cf6668e57bb497e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020873`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT substr('5hg_ 7iR9', 2147483647); CREATE VIRTUAL TABLE I
```

---

## Crash 24: `38fe550d59b8dae1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021212`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 25: `7b276659d1e15775` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021849`

```sql
SELECT printf('%.*f', 2147483647, -1e308); SELECT hex(zeroblob(2147483647));
```

---

## Crash 26: `5b0a75f69847bb42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022108`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c3); INSERT INTO t3 DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 27: `1cf049546aefd5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022115`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 28: `439b634daefa9599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022122`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 29: `ea12235b4e27a875` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022234`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 30: `6c922d5b699fb594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022265`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 31: `6a0cf29f43fc65f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022608`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('[]') INNER JOIN jsonb_each('[{"a":1},{"b":2}]') USING (_rowid_) LIMIT CURRENT_DATE;
```

---

## Crash 32: `096105c5918acc94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022738`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('[]') INNER JOIN jsonb_each('[{"a":1},{"b":2}]') USING (_rowid_) LIMIT CURRENT_DATE;
```

---

## Crash 33: `60e7024ab681a741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023249`

```sql
SELECT printf('%x', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT OR FAIL INTO q VALUES (NOT EXISTS (SELECT RAISE(IGNORE) AS hy, t1.* FROM t3 LEFT OUTER JOIN p 
```

---

## Crash 34: `e0efe6a59ae66b47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025228`

```sql
SELECT substr(' -66H 8Z_--_6_7  ', 9223372036854775807, 9223372036854775807); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 35: `0a196bcd2524b78a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030237`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.0); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 36: `8503016dd4411456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030437`

```sql
SELECT printf('%.*e', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); INSERT INTO t2 VALUES (FALSE IS DISTINCT FROM CURRENT_DATE IS DISTINCT FROM CURRENT_TIME != NULL <
```

---

## Crash 37: `02ad9f2e8756d2ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030631`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 38: `418ee72fdc50a5ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030874`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM json_each('{}'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); WITH r (c2) AS NOT MATERIAL
```

---

## Crash 39: `31cf778dd9e25e47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043179`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN SELECT * EXCEPT SELECT p.*, * FROM jsonb_each('{"a":1}') LEFT OUTER JOIN jsonb_tree('[]')
```

---

## Crash 40: `d59c19c2f24baa39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043510`

```sql
SELECT substr('_8--i h56_-1 _', 0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT CASE CURRENT_DATE ISNULL WHEN RAISE(IGNORE) IS RAISE(IGNORE) NOTNULL != CURRENT_DAT
```

---

## Crash 41: `4d242279ffbdaff4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047314`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_each('[]') GROUP BY FALSE, CURRENT_DATE; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 42: `eda30738d7a91e40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053489`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE GENERATED ALWAYS AS (+TRUE) STORED, a REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 43: `bb9c04104baee681` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059018`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL DEFAULT TRUE); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 44: `bf46b40fbeaf571f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059094`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 45: `6b960d326cf2a61b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059100`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH
```

---

## Crash 46: `c1f5d6bddfd2a923` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059375`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB,
```

---

## Crash 47: `d927ce4f1616aa05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059936`

```sql
SELECT printf('%.*g', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); SELECT DISTINCT p.* FROM p NATURAL LEFT JOIN json_tree(CURRENT_DATE, '$.b.c') USING (c1) WHE
```

---

## Crash 48: `b1841a899697edfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060750`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME); ANALYZE q; CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT 
```

---

## Crash 49: `fcb68cece89f35d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061314`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL DEFAULT X'Fe'); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647,
```

---

## Crash 50: `e408f53601be5a68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062117`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 51: `5e28833268370273` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065908`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 52: `5b6ad59878571fbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068246`

```sql
SELECT printf('%.*d', 2147483648, 1e308); SELECT printf('%.*f', 2147483647, 0.0); SELECT printf('%.*g', 2147483647, 0.01); SELECT printf('%.*e', 4294967296);
```

---

## Crash 53: `a046d75296282921` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073637`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT); INSERT INTO q SELECT * FROM p NOT INDEXED; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 54: `0be434cadfa9f316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074243`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (FALSE)) AS a; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 55: `915f18efabda5393` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074482`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE AS nn_0qjg_h3_n_847r__afgf9l19_7_5_idyf0e64s1q__i1s_6_g__6i_2____b1g1_6tl29_o_9w_3cp___n54__n
```

---

## Crash 56: `61a27e052cf5b929` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075510`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC GENERATED ALWAYS AS (FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 57: `6f99ea9ff4d5c02c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075617`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC GENERATED ALWAYS AS (FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 58: `e218ef7bc61eb3e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077905`

```sql
SELECT substr('E-o9s i5', -2147483648, -2147483648); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 59: `54a62cfd8cd6597e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085051`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY, c3 BOOLEAN UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT printf('%.*g', 2147483647, 0
```

---

## Crash 60: `b5c5a221424b8174` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085385`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); SELECT * 
```

---

## Crash 61: `883e9b250863529d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087580`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT -1261, c1 FLOAT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; SELECT printf('%.*f
```

---

## Crash 62: `9a8db25a59bea3d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087747`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT FALSE, c1 FLOAT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; SELECT printf('%.*f
```

---

## Crash 63: `e2d91131313f9e72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088595`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER NOT NULL, c3 BLOB); SELECT * FROM p NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 64: `6ff87bca6ea04415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088726`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER NOT NULL, c3 BLOB); SELECT * FROM q NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 65: `51cd7a6942adf7b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088855`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT NOT NULL); SELECT * FROM q NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 66: `184ef08a6354823d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090371`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME IN (VALUES (FALSE)); SELECT printf('%.*g', 214748
```

---

## Crash 67: `d68424f8be8ecd65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091196`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (RAISE(IGNORE)), a FLOAT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP; SELECT printf('%.
```

---

## Crash 68: `cace704e5cef6f91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099248`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE * FALSE, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); SELEC
```

---

## Crash 69: `5b2bd85633ee59fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100037`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (count(*) 
```

---

## Crash 70: `b504219ce0b82e44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE I
```

---

## Crash 71: `ead1997e5ebaa57b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105456`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 72: `0d7177661d502115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106132`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CASE WHEN CURRENT_DATE / TRUE > NULL THEN NULL END)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELE
```

---

## Crash 73: `7c8bb2ec3e2c4a07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106951`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIMESTAMP NOT IN (NULL))); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2
```

---

## Crash 74: `92f94948f8e7d8ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107197`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIMESTAMP NOT IN (NULL) / TRUE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 75: `9f0494c1adadddbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107601`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE > TRUE ISNULL)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 76: `ca5d308ad3a15084` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107657`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 77: `77a92d5eeb721951` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107665`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE > TRUE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 78: `d2fe001640bf41b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110742`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (NULL == CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483
```

---

## Crash 79: `96dc7b0163012920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112044`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (CURRENT_DATE < FALSE), a FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%
```

---

## Crash 80: `8621bae0d468cf08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112393`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL DEFAULT 8.77E+845388997734853017); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*
```

---

## Crash 81: `1bda8d399454f137` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112771`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_,
```

---

## Crash 82: `bc77f72edaeb3b1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112819`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 83: `ec777190ec29b5f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114123`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT (VALUES (CURRENT_TIME)) AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1;
```

---

## Crash 84: `0ceb858caa00a9a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116469`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT count(DISTINCT CURRENT_TIMESTAMP) AS nn_0qjg_h3_n_847r__afgf9l19_7_5_idyf0e64s1q__i1s_6_g__6i_2____b1g1_6tl29_o_9w_3cp___n54
```

---

## Crash 85: `438c8c3b08accdb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117581`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, rowid DATE GENERATED ALWAYS AS (TRUE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT NULL NOT NULL AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi
```

---

## Crash 86: `6a09b37c3a92cce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118544`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT FALSE AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE -CAST(TRUE AS FLOAT)) AS sub1; SELECT pr
```

---

## Crash 87: `01340e1563a2d031` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119310`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES 
```

---

## Crash 88: `ba40c12eca37e964` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119594`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_DATE AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CAST(NULL AS BLOB)) AS sub1; SELE
```

---

## Crash 89: `b09b0c4cb8d58ff3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119769`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_DATE AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CAST(FALSE AS BLOB)) AS sub1; SEL
```

---

## Crash 90: `f3a8d0eeb73dffd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120147`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT rowid AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 214
```

---

## Crash 91: `96e3bdffe84decde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121698`

```sql
SELECT round(0.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT *, q.* FROM p NATURAL JOIN p WHERE CASE char(CURRENT_DA
```

---

## Crash 92: `9bd8b2304d978345` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121957`

```sql
SELECT printf('%.*d', -1); SELECT substr('_ N __- Yu--f-', 2147483647, 0); SELECT printf('%.*s', -9223372036854775808, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s VALU
```

---

## Crash 93: `37b5bfba07a99256` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122570`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT DISTINCT * FROM t2 NOT INDEXED ORDER BY -CURRENT_TIMESTAMP < RAISE(IGNORE) NOT IN (VALUES (NULL)) IS RAISE(IG
```

---

## Crash 94: `c2b570372c483a73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124548`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_DATE AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CAST(-469359106858445145823402497
```

---

## Crash 95: `cfdf5a4950f84db3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124991`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT NULL NOT BETWEEN CURRENT_TIMESTAMP GLOB FALSE AND FALSE AS k5_ql_c5_5_k75_2f3_w55s___bv8c6dhya_mn___dxu419a7__q28f_e__gvy40a
```

---

## Crash 96: `18a0c60b91870e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126274`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); SELECT max(FALSE) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UNBOUNDE
```

---

## Crash 97: `1a6cd8ebdb0a910b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126393`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM (SELECT CURRENT_TIME % FALSE COLLATE RTRIM AS xv0 FROM p WHERE json_patch('{"a":1}', '[]')) AS sub1; SELECT printf('%.*f', 214748364
```

---

## Crash 98: `9f61946db9df5043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127911`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE CAST(CURRENT_TIMESTAMP AS BLOB)) 
```

---

## Crash 99: `bcd5375cb584b61b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128715`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE json_array_length(FALSE)) AS sub1
```

---

## Crash 100: `f75f89daefcde4a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128924`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT CURRENT_TIME AS hnexgz5091_1____e90_____3i__44d__4e3_0zvmi81_zat2___4__vcr57v FROM (SELECT * FROM p WHERE random()) AS sub1; SELECT printf(
```

---

## Crash 101: `2e7829a73f187e7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130903`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE OR FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 102: `ba7623646517b4fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131762`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE, _rowid_ TEXT GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO q DEFAULT VALUES; PRAGMA quick
```

---

## Crash 103: `da281e8117741e4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132044`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) N
```

---

## Crash 104: `c2bfe637416514ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132054`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE, _rowid_ TEXT GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO q DEFAULT VALUES; PRAGMA quick
```

---

## Crash 105: `6c58f96156c95d38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132061`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT UNIQUE, _rowid_ TEXT GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO q DEFAULT VALUES; PRAGMA quick
```

---

## Crash 106: `cee12e8394f31968` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133726`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE MATCH CURRENT_TIMESTAMP <> FALSE <> FALSE <> FALSE <> FALSE <> FALSE <> FALSE <> FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO 
```

---

## Crash 107: `60cd52c796904db4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133827`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_DATE <> FALSE <> FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 108: `0d9d03eb17a86fdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134071`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE IS _rowid_ <> FALSE <> FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f'
```

---

## Crash 109: `381a175570afd2be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134241`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE IS CURRENT_DATE <> FALSE <> FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('
```

---

## Crash 110: `ae7c5056ecc01308` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134576`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN NOT NULL DEFAULT -7.0297215829594349E649701); CREATE TABLE IF NOT EXISTS q(rowid BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELEC
```

---

## Crash 111: `a92298faf2e4a0d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134673`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(rowid BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 21474
```

---

## Crash 112: `f7b02893ae553182` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134836`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (FALSE > TRUE % CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 113: `87b79ba73b4c7073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134863`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 114: `d8f1d4ff010cb6ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135046`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_DATE <> CASE WHEN TRUE MATCH CURRENT_TIMESTAMP NOT IN (FALSE) / TRUE THEN FALSE END)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q
```

---

## Crash 115: `a361b4618bfa16e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135238`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_DATE <> CASE WHEN CURRENT_TIME NOT IN (FALSE) / TRUE THEN FALSE END)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES;
```

---

## Crash 116: `27e0f1004cede1b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135730`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_DATE / FALSE)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 117: `378a7bf8ad1e7a6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138027`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE, CURRENT_DATE); VALUES (count(*) FILTER (WHERE FALSE) OVER ()); 
```

---

## Crash 118: `d94f8f0875d06f91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141101`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CAST(CURRENT_TIMESTAMP AS REAL) >= CAST(CURRENT_TIMESTAMP AS REAL), CU
```

---

## Crash 119: `e63ea7cfb6cb500f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141916`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NOT EXISTS (SELECT NULL LIMIT CURRENT_DATE OFFSET TRUE), CURRENT_DATE)
```

---

## Crash 120: `ac047d304819b643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141979`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NOT EXISTS (SELECT NULL LIMIT FALSE), CURRENT_DATE); EXPLAIN QUERY PLA
```

---

## Crash 121: `c7091882c955f4ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP, CURRENT_DATE); EXPLAIN QUERY PLAN SELECT * FROM jso
```

---

## Crash 122: `c63b6c33287931fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143408`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE * CURRENT_DATE, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE)
```

---

## Crash 123: `cb399b85d9d1a08c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143888`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY, a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL || FALSE, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); CR
```

---
