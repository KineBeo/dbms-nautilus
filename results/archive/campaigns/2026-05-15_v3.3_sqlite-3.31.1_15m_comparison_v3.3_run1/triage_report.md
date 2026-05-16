# Crash Triage Report

**Total crashes:** 78  
**Unique crash sites:** 78  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 78 | 78 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `8584db75079c38a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000060`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT INTO t2 (c2, b) VALUES (FALSE) ON CONFLICT(c1) DO UPDATE SET b = FALSE IS RAISE(IGNORE) COLLATE NOCASE MATCH CURRENT_DATE AND CURREN
```

---

## Crash 2: `de6559c06b2d34fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000557`

```sql
SELECT substr('', 4294967296, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c3, c1) VALUES (RAISE(IGNORE) COLLATE BINARY / TRUE = -FALSE IS NOT NULL NOT
```

---

## Crash 3: `b10404cf27523f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000722`

```sql
SELECT substr(' 6 J5-__ _', 2147483647, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR FAIL INTO s VALUES (CASE CURRENT_TIMESTAMP >> TRUE = -CURRENT_DATE ->> chang
```

---

## Crash 4: `45f84dd0f0fdba75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001299`

```sql
SELECT printf('%.*g', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); INSERT INTO p VALUES (FALSE > NULL IS NOT NULL >> CASE WHEN FALSE THEN NULL END != TRUE LIKE RAISE(IGNOR
```

---

## Crash 5: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001305`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 6: `7f5a75e745eca593` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001321`

```sql
SELECT printf('%.*g', 4294967295, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NULL == CURRENT_TIME REGEXP -CURRENT_TIMESTAMP || NOT CURRENT_TIMESTAMP IS NULL IS DISTINCT FROM
```

---

## Crash 7: `9897c2b4f4b4a566` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001428`

```sql
SELECT substr(' lb-ZE', 2147483647, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); WITH RECURSIVE q AS (VALUES (FALSE) INTERSECT SELECT *) INSERT INTO q VALUES ((CURR
```

---

## Crash 8: `74ec8e95eaa17931` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001502`

```sql
SELECT substr(' ', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT CURRENT_TIME - RAISE(IGNORE) COLLATE NOCASE > -FALSE COLLATE BINARY LIKE CURRENT_TIME IS NOT DISTINCT FROM C
```

---

## Crash 9: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001575`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 10: `f48c86981799bc35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008121`

```sql
SELECT printf('%.*e', 4294967295, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (FALSE >= -+TRUE IS DISTINCT FROM RAISE(IGNORE) AND TRUE BETWEEN TRUE 
```

---

## Crash 11: `85cb6c77d7049466` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008556`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, c1, c2, c1, c2, a); INSERT OR FAIL INTO q VALUES ((WITH RECURSIVE p (c2) AS (SELECT CURRENT_TIME INTERSECT VALUES (CURRENT_TIME, (CURRE
```

---

## Crash 12: `daecf52b28b1c424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017903`

```sql
SELECT printf('%.*g', 1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, c1); WITH q AS NOT MATERIALIZED (VALUES (NULL) EXCEPT SELECT CURRENT_DATE) INSERT INTO q VALUES (CASE W
```

---

## Crash 13: `9042bf7126110aea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022870`

```sql
SELECT printf('%.*d', -1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT p.* FROM p WHERE EXISTS (WITH RECURSIVE r (c1) AS (SELECT q.*, r.* FROM r WHERE CASE WHEN CASE WHEN TRU
```

---

## Crash 14: `bd8103d9b22d516a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025242`

```sql
SELECT substr('77F-- 1_ t u1', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE q (c1, a, a, b, c3, c2, c2) AS NOT MATERIALIZED (WITH t2 AS NOT MATERIALIZED (VALUE
```

---

## Crash 15: `f44999047d0ad365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026653`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_tree('{"a":1}') GROUP BY CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 16: `75e3dbcbbc42f26f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028677`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 17: `b0d72dbccaeefaea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028831`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 18: `83110baf7b109a98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029496`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (NULL); ANALYZE p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 19: `fcf2e900cf56d78d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029637`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (FALSE); ANALYZE p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 20: `5cfb9dd99f48cc55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029643`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 21: `386069dbd68f4a73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029869`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 22: `a64e985c7cbebed5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029978`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 23: `0454d79592da1da8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031695`

```sql
SELECT substr('_--_j-euH  ', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT ~FALSE LIKE ~CURRENT_TIME ISNULL ESCAPE CURRENT_DATE != CURRE
```

---

## Crash 24: `b49d8d7d719ef716` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034879`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT ALL count() OVER (PARTITION BY NULL, TRUE) AS x5_9jcb_zf_649_ FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF
```

---

## Crash 25: `7cc3a035985c74cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038998`

```sql
SELECT round(1e308, -2147483649); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 26: `286bca8c43eb034d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039259`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, _rowid_); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p 
```

---

## Crash 27: `f24bf217a129819f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041155`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; SELECT q.* FROM t1 NATURAL JOIN p WHERE 'Av-rj___nUU_____T' NOT NULL;
```

---

## Crash 28: `a31e2796813c1d94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048479`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIME)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 29: `8990854ef4e5381d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050711`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 30: `85275f54f1ed0394` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050935`

```sql
SELECT printf('%llu', -1, ' M _ _x'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO r VALUES (TRUE ISNULL IS NOT DISTINCT FROM jsonb_replace('{"a":1}', '$.a', CURRENT_TIMESTAM
```

---

## Crash 31: `5e22da99a881dc70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053026`

```sql
SELECT round(-1e308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, a); WITH RECURSIVE q AS NOT MATERIALIZED (SELECT * FROM q INDEXED BY _rowid_ WHERE hex(RAISE(IGNORE)) GROUP BY CURRE
```

---

## Crash 32: `decd25c65379fe94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053640`

```sql
SELECT round(1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_); SELECT (NULL) AS hq2a0a_rm5 FROM t1 INDEXED BY c2 LEFT JOIN json_tree('[{"a":1},{"b":2}]') USING (c1, c2) WHERE
```

---

## Crash 33: `cd4b032fd7beb592` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053733`

```sql
SELECT printf('%.*g', 2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO s VALUES (min(length(CASE WHEN CURRENT_TIME COLLATE RTRIM ->> (RAISE(IGNORE)) 
```

---

## Crash 34: `a22230634054668c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057944`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, c1 GENERATED ALWAYS AS (b) NOT NULL UNIQUE, c3 REAL PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 35: `653c396fb057a4ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060831`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM json_each('{"a":1}') WHERE FALSE GROUP BY NULL HAVING TRUE OR
```

---

## Crash 36: `577bffd7136acaa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061084`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM q JOIN p a ON NULL IS NOT _rowid_; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 37: `a0207bfc1efc062b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061152`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM q JOIN p a ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGN
```

---

## Crash 38: `0a70af0b8f21f170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061158`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM q JOIN p a ON NULL IS NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 39: `3359d7f9ad830cf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063586`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') LIMIT X'1A7e'; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 40: `f0a31a0289057fec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064422`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('[{"a":1},{"b":2}]') LIMIT CURRENT_DATE, CURRENT_TIME; SELECT printf('%.*g', 214748364
```

---

## Crash 41: `18159ae4a6b1f990` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064575`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 42: `eaa0e76b83499c13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064581`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 43: `d088a0d5f9204bf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064587`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `583b05cd1091b3ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073895`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT ALL count() OVER () IS NOT (VALUES (NULL)) AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*f', 2
```

---

## Crash 45: `4febae2ad627ff07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074037`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT ALL CURRENT_TIMESTAMP AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 46: `e5d698d037429b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075345`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT ALL TRUE AS x5_9jcb_zf_649_ FROM json_each('{"a":1}') LEFT OUTER JOIN json_each('{"a":{"b":1}}') JOIN jso
```

---

## Crash 47: `34de47665e8247b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076027`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_DATE IN (VALUES (FALSE))); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 48: `d12df54235157fa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076341`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (avg(TRUE)) INTERSECT VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 49: `9e230f638e70bf1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076489`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (NULL) INTERSECT VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 50: `6bdc0b46633bc060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076495`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (changes()) INTERSECT VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 51: `7e5687f4554767f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077359`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (max(NULL)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `f5bea4a71caa1f47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077381`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 53: `4b160c4b4892dcd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082112`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT SELECT ALL count() OVER () IS NOT count(*) AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT round(0.01, -2147483648
```

---

## Crash 54: `770af0e02f3ef255` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083398`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CURRENT_DATE 
```

---

## Crash 55: `57f15144cc04c31d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083871`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (95.9E+0); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 56: `c1f8b2ed95ee62f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084054`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_DATE) INTERSECT VALUES (rank() OVER ()); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 57: `62f8b24854688377` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084435`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (CURRENT_TIME COLLATE RTRIM) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 58: `2c9ddfa4f1c77c87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084594`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 59: `dd4c933ab24a1e23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084601`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 60: `ef16893b347b2893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084887`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); VALUES (count() IS NOT TRUE) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 61: `f96e4fd2f1ba7cc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085585`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 AS(c1) UNIQUE); VALUES (CURRENT_DATE) INTERSECT SELECT ALL json(NULL) AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 62: `49be5002d0ee6780` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085942`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_DATE) INTERSECT SELECT ALL NULL IS NOT TRUE COLLATE NOCASE AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*g', 2147483647
```

---

## Crash 63: `82b6578045e47b81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086077`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_DATE) INTERSECT SELECT ALL NULL IS NOT FALSE AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 64: `45ad6cca1591a712` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086151`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_DATE) INTERSECT SELECT ALL json_array_length(NULL) AS x5_9jcb_zf_649_ FROM p NOT INDEXED; SELECT printf('%.*f', 2147483647, -1e308
```

---

## Crash 65: `6d15bcdc5a88818b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087311`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_DATE) INTERSECT SELECT ALL NULL IS NOT char(CURRENT_TIMESTAMP) NOT LIKE CURRENT_DATE > FALSE AS x5_9jcb_zf_649_ FROM p NOT INDEXED
```

---

## Crash 66: `1b81cc41ef933d9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090694`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF 
```

---

## Crash 67: `986447f96fbe1b82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093222`

```sql
SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT q.*, CASE WHEN NULL THEN CURRENT_TIMESTAMP COLLATE NOCASE NOT NULL ELSE FALSE END IS DISTINCT FROM CURRE
```

---

## Crash 68: `e42c90a77beadcf9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096081`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); SELECT * FROM json_tree('[1,2,3]') GROUP BY CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 69: `e4c6709983c482de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105463`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE, TRUE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 70: `f16f3e1178bda8ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110935`

```sql
SELECT printf('%lld', -2147483649, ''); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 71: `4d9d3043849fbd0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110985`

```sql
SELECT printf('%lld', -2147483649, ''); CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE, a TEXT DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, q.* FROM s NATURAL LEFT JOIN json_
```

---

## Crash 72: `df431f837fdf3d2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111101`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT * FROM jsonb_tree('[{"a":1},{"b":2}]') CROSS JOIN (p) NATURAL JOIN p ORDER BY CURRENT_TIMESTAMP ASC;
```

---

## Crash 73: `c381a962c1053b40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114153`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT 264135255851226542920242799115101780411197182358093509700760890208539155.6); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f',
```

---

## Crash 74: `804228f1512e6b92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117009`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('[1,2,3]'); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 75: `0d840b91d61462a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117621`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c3); INSERT OR ROLLBACK INTO p VALUES (
```

---

## Crash 76: `659f7a6e045bbfd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131220`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT OR ABORT INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE 
```

---

## Crash 77: `eb2bfde24057bbfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132367`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT OR ABORT INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE 
```

---

## Crash 78: `519d81bf7159b7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133371`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC PRIMARY KEY); INSERT OR ABORT INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE 
```

---
