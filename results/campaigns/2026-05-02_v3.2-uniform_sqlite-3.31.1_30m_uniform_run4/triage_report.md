# Crash Triage Report

**Total crashes:** 188  
**Unique crash sites:** 188  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 175 | 175 | 93% |
| Signal | 13 | 13 | 6% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 2: `87f4d214bcb540cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000280`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT RAISE(IGNORE) LIKE TRUE COLLATE RTRIM AS yi2_9_h_, *, *, FALSE AS x FROM s WHERE EXISTS (VALUES (CURRENT
```

---

## Crash 3: `8106e593177b59c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000296`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); INSERT INTO t1 (c3, _rowid_) VALUES (FALSE LIKE CURRENT_DATE << unicode(CURRENT_TIMESTAMP NOT LIKE CURRENT_DATE ISNULL IS TRUE = NULL IS N
```

---

## Crash 4: `ecc4f4962b56f15d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000347`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER, b GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, b INT CHECK (EXISTS (VALUES (CURRENT_DATE)) OR NULL IS NULL IS
```

---

## Crash 5: `ab51e9c28aec2a72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000378`

```sql
SELECT printf('%.*g', 1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t1.*, CASE CURRENT_TIME COLLATE NOCASE || CURRENT_TIMESTAMP <= count(*) BETWEEN -RAISE(IGNORE) IS TRUE
```

---

## Crash 6: `cf3a51d26b3d3977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000452`

```sql
SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INTEGER, c1 GENERATED ALWA
```

---

## Crash 7: `0f761012522bc290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000630`

```sql
SELECT printf('%.*e', -2147483649, -1.0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 8: `d90f995bd7f12f2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000684`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO r VALUES (char(coalesce(CURRENT_TIME MATCH CURRENT_TIME BETWEEN FALSE AND NULL || TRUE, ~CURRENT_TIME || CURRENT_TIME C
```

---

## Crash 9: `632096e55e7d7e74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000993`

```sql
SELECT printf('%.*s', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT NOT (-RAISE(FAIL, '9d_-Ka2-d-_ 64')) * CURRENT_TIME - FALSE IS NULL, q.* FROM q JOIN t
```

---

## Crash 10: `8133090d29a482e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001610`

```sql
SELECT substr('p6-kh-K-_--c', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); SELECT * ORDER BY total_changes() ASC LIMIT count(*) EXCEPT SELECT CURRENT_TIME ISNULL AS a17_ofs12tfb__
```

---

## Crash 11: `709a2dbde5708a10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001821`

```sql
SELECT substr('D2  - VZa 3c', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE t1 (c1) AS NOT MATERIALIZED (SELECT CURRENT_TIMESTAMP FROM p WHERE CURRENT_DATE ->> 
```

---

## Crash 12: `c578162466ad6b48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001907`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p (b, c1) VALUES (upper(~TRUE IS NULL % CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP COLL
```

---

## Crash 13: `68bd31fe0b630f1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003819`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT, b GENERATED ALWAYS AS (a IS NULL) , a BOOLEAN NOT NULL DEFAULT CURRENT_TIME); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 14: `a3ac0717bee59d2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003892`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM q JOIN q p ON CURRENT_TIME || NULL; CREATE TABLE IF NOT EXISTS p(c2 DATE, b GENERATED ALWAYS AS (a + -6
```

---

## Crash 15: `98f8d69436c7eff4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003899`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255), a GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 16: `d83c608836bfacac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003905`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255), a GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM q J
```

---

## Crash 17: `5d063ca46aa52087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005158`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE 
```

---

## Crash 18: `0b5963da7addba25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005299`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 19: `1cab0b2c40b5d75b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005312`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 20: `2eb2d7ae517c45c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005368`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (NOT NULL, NULL) EXCEPT VALUES (CURRENT_DATE) ORDER BY RAISE(IGNORE) > random() IS NOT NULL
```

---

## Crash 21: `5ec2d9e4b1c7e8ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005971`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT TRUE % TRUE FROM r WHERE EXISTS (SELECT * FROM r NOT INDEXED INNER JOIN t3 NOT INDEXED USIN
```

---

## Crash 22: `0de6366b8b89fde3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006013`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT TRUE % TRUE FROM r WHERE EXISTS (SELECT * FROM r NOT INDEXED INNER JOIN t3 NOT INDEXED USING (c2) ORDER BY p.
```

---

## Crash 23: `c0cf2adcaed6a495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006305`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 24: `bc094754e37f6d41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007643`

```sql
SELECT printf('%.*g', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (b) VALUES ((RAISE(IGNORE)) != RAISE(IGNORE) NOT NULL != CURRENT_DATE COLLATE RTRIM ->> NULL +
```

---

## Crash 25: `1e978c43a49700dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008105`

```sql
SELECT substr('', 2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE p AS (VALUES (CURRENT_TIME - CURRENT_DATE ISNULL != RAISE(IGNORE) COLLATE R
```

---

## Crash 26: `d0161ce87d186e1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008297`

```sql
SELECT printf('%x', 0, 'SC- n'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE LIKE RAISE(IGNORE) ESCAPE FALSE = ~FALSE NOTNULL OR RAISE(IGNORE
```

---

## Crash 27: `5a908b59387ba7a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012971`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL) INTERSECT SELECT ~NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1); INSERT INTO
```

---

## Crash 28: `9d0cd302c90abb3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013214`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE AND CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 29: `f31443d94a91a961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013427`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 30: `24aead0efc86e04b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013438`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 31: `7635ba2e6603b26e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013547`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 32: `52a02f18f5abc562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013578`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 33: `0a4203ae6c4a609a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014819`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (NULL COLLATE NOCASE - CURRENT_DATE >= CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 34: `9f23589386f48add` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014841`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME >= CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 35: `982988cfa89c276c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014919`

```sql
SELECT round(0.01, 0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 36: `e60340114767b447` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015422`

```sql
SELECT substr('h7_G7--S--tp', 2147483648, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT FALSE LIKE NULL AS skrh, t1.* FROM p NATURAL JOIN t1 WHERE +RAISE(IGNORE) == NUL
```

---

## Crash 37: `a8fd31fa483847b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015675`

```sql
SELECT substr('9 k_0F-z4-0_428b_', -1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT q.*, CASE WHEN TRUE T
```

---

## Crash 38: `37a79111d2e37bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021837`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p SELECT * FROM p NOT INDEXED LEFT OUTER JOIN (SELECT * ORDER BY CURRENT_TIMESTAMP) AS xn_j_5__0
```

---

## Crash 39: `dfb17e591e19ec7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022117`

```sql
SELECT printf('%.*e', 1, 1e-308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `d9ee7bf0f9f1bd5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022758`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p (_rowid_) VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 41: `26c3eef766495195` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024280`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 42: `37ea95fe51a0ee69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025458`

```sql
SELECT printf('%.*g', 4294967296, -0.0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 43: `2d7d76365a4da767` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025884`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); WITH q AS MATERIALIZED (WITH p (a, c2) AS
```

---

## Crash 44: `8e779506b6f156e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027218`

```sql
SELECT round(-1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3); INSERT INTO t3 VALUES (FALSE IS DISTINCT FROM TRUE -> NULL IS NOT NULL GLOB CURRENT_DATE COLLATE NOCAS
```

---

## Crash 45: `47cca661953cfb98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029408`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zer
```

---

## Crash 46: `6d7da5f69ecc1a14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029416`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zer
```

---

## Crash 47: `42d3a98065bdba7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029686`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT p.* FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 48: `2368ebcfac23287d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029890`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); SE
```

---

## Crash 49: `9ca96549d98f0a61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030425`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CASE WHEN RA
```

---

## Crash 50: `5ca56036b9e09c38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031056`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; SELECT * FROM q JOIN q b_gtwo6ly0n ON CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXIST
```

---

## Crash 51: `b3ff9513e946623e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031845`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (a) VALUES (zeroblob(FALSE) FILTER (WHERE NOT FALSE / TRUE COLLATE NOCASE)) ON CONFLICT(rowid
```

---

## Crash 52: `e3a7c4c9e997dcd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031959`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT, b GENERATED ALWAYS AS (a IS NULL) , a BOOLEAN NOT NULL DEFAULT CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 DATE, c1 
```

---

## Crash 53: `05a6cf9606ad6d0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033127`

```sql
SELECT printf('%f', 1, 'd e_- -WSq_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 54: `eac78538056b9b8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034566`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (_rowi
```

---

## Crash 55: `092132b65b351249` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044321`

```sql
SELECT printf('%lli', -9223372036854775808, 'TCtK-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT DISTINCT q.* FROM p NATURAL JOIN p INDEXED BY b WHERE CURRENT_TIME NOTNULL <
```

---

## Crash 56: `002ae0a961bc2282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047277`

```sql
SELECT printf('%.*d', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH p AS (VALUES (NULL)) INSERT INTO p VALUES (RAISE(IGNORE) IS NOT DISTINCT FROM TRUE / CU
```

---

## Crash 57: `4440e54600503635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048399`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL DEFAULT 386655337917604307798.609); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE 
```

---

## Crash 58: `1b7ac9dd226ae201` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048840`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, CURRENT_TIMESTAMP || NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIM
```

---

## Crash 59: `27dfa7f4cee1494c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066776`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 60: `7c0e29160f6c1796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066899`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELEC
```

---

## Crash 61: `c8f1a9b267cd651a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066932`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 62: `f271dfee0a80a96b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069229`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP) UNION SELECT count(*) OVER () AS a; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 63: `ed3a6d6a6225f5c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071337`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT, b GENERATED ALWAYS AS (a IS NULL) , a BOOLEAN NOT NULL DEFAULT -6483241051747.7110589405e+3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF N
```

---

## Crash 64: `867efd8105e2732a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT, b GENERATED ALWAYS AS (a IS NULL) , a BOOLEAN NOT NULL DEFAULT CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 DATE, c1 
```

---

## Crash 65: `e53980aac3b6cd16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE > TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 66: `19afd0be877795d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073899`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b TEXT NOT NULL DEFAULT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%llu', -21474836
```

---

## Crash 67: `d6588f6827573d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074551`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT group_concat(NULL) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIME) AS e6__0v_02k010v_44_8_m73c__8838_z_008mc____461_r858_80278_29__9_c_
```

---

## Crash 68: `5824dccc44226d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074732`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT (WITH p AS (VALUES (NULL)) VALUES (group_concat(NULL) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIME))) AS e6__0v_02k010v_44_8_m73c__88
```

---

## Crash 69: `b0163508fdd8fe8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074909`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a * a) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p 
```

---

## Crash 70: `a0aeccd57c1c1ede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075649`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT INTO p VALUES (-CURREN
```

---

## Crash 71: `db5b2bd0886631fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075664`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%.*d', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM 
```

---

## Crash 72: `06fecc3b1355921e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075702`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a + -2812) UNIQUE); EXPLAIN QUERY PLAN VALUE
```

---

## Crash 73: `e6361b9893056e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(c3 FLOAT GENERATED ALWAYS AS (NULL <= FALSE) STORED); CREATE TABLE IF NOT EXIS
```

---

## Crash 74: `8aef475f118066aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075825`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT substr('WV10JF--_-6Ia38Z', -2147483648, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 75: `89f5144b1812bcbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076292`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT ''); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHER
```

---

## Crash 76: `284706a9928e3c9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079244`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SEL
```

---

## Crash 77: `6b69f705e349a7df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079693`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (CURRENT_TIME IS FALSE IS NULL COLLATE NOCASE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 78: `e759bf62696c1aed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079837`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL IS FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHER
```

---

## Crash 79: `67d1a45489f11675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079944`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL IS FALSE); SELECT printf('%.*d', 1, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELE
```

---

## Crash 80: `988bdb3be2716f22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080986`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (json_array(NULL) IS FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL 
```

---

## Crash 81: `a54c97a5383df4db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081110`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (last_insert_rowid() IS FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATUR
```

---

## Crash 82: `c261ef461453f3ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083711`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (CURRENT_DATE NOT IN (CURRENT_DATE, TRUE, CURRENT_TIMESTAMP)) ON CONFLICT DO NOTHING;
```

---

## Crash 83: `53b1ed3df642be33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083823`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (CURRENT_DATE NOT IN (NULL)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT p
```

---

## Crash 84: `3a30bfa45cf528e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083829`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (CURRENT_DATE NOT IN (CURRENT_DATE, NULL)) ON CONFLICT DO NOTHING; PRAGMA integrity_c
```

---

## Crash 85: `b0d53cc7c831759e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083883`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_DATE >= NULL)); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VI
```

---

## Crash 86: `9c8600dbd3dbe353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085844`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 87: `d7f5480d9f248ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085850`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 88: `47f57eb52581b362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085950`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (CURRENT_TIME OR CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT
```

---

## Crash 89: `28061f354fa598ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086097`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a INTEGER UNI
```

---

## Crash 90: `20584af3976aa4e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086578`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'eF'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABL
```

---

## Crash 91: `bb924a251f1d7335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088845`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE COLLATE RTRIM, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF
```

---

## Crash 92: `df6d56a7bf0c6d2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104775`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01)
```

---

## Crash 93: `be01ed574c17a492` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105279`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a = -250377) UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 94: `836dac6e49265db9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105451`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a = -250377) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 95: `fe4545d266cf207e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106415`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (ORDER BY NULL ASC NULLS LAST ROWS BETWEEN RAISE(IG
```

---

## Crash 96: `10d7f068715150d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106546`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS (ORDER BY NULL ASC NULLS LAST GROUPS BETWEEN UNBOUN
```

---

## Crash 97: `1033ad931c942efd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106867`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); EXPLAIN QUERY PLAN SELECT count(*) OVER (PARTITION BY CURRENT_TIMESTAMP) FROM p NOT INDEXED WHERE T
```

---

## Crash 98: `352528096d32f9b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107826`

```sql
SELECT substr('2cJ2Wz- _U79 C', -1, -2147483649); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 99: `5d68cbf945479212` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109191`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL) UNION ALL SELECT ~NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFA
```

---

## Crash 100: `ed88e9b079d58367` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109499`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL) INTERSECT SELECT ~group_concat(CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 101: `61b68db73fe4a325` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109764`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL) EXCEPT SELECT NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 102: `1f75ea23a38f9de0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110442`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE CHECK (_rowid_)); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 103: `c108b73e817a9e2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110659`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 104: `981db8a6142c07b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111080`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (NULL) INTERSECT SELECT NULL BETWEEN changes() AND NOT CURRENT_TIME AS m1rn3b_2gjy__x24__6_hy_m8w___71z13___7y5_r5b___j; SELECT printf('
```

---

## Crash 105: `b3cda613b142f083` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113471`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GROUP)
```

---

## Crash 106: `2bb273cb0dcbb6b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113625`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT * FROM p WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS () INTERSECT VALUES (TRUE); SELECT printf('%.*g', 21
```

---

## Crash 107: `ec29b678beec1aac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119637`

```sql
SELECT substr(' p Bz-N7-H__-__- ', -9223372036854775808, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (TRUE IS NOT NULL, TRUE NOT NULL); 
```

---

## Crash 108: `ac15140f2b4ca2c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120740`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT X'C9c0BbF92eE49f'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSER
```

---

## Crash 109: `9054011f6d0781b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123499`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT count(*) FILTER (WHERE FALSE), * FROM (SELECT * FROM p WHERE EXISTS (VALUES (FALSE LIKE CURRENT_TIME ESCAPE FALSE))) AS sub1; CREATE VIRTUAL T
```

---

## Crash 110: `877d05e0ef2f5100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129199`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL
```

---

## Crash 111: `5397d86c17838552` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL) INTERSECT SELECT FALSE NOT IN (VALUES (NULL) EXCEPT SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY N
```

---

## Crash 112: `a19da69b56b96200` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132988`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); EXPLAIN QUERY PLAN SELECT count(*) OVER (PARTITION BY ' _1_5X vno__2') FROM p NOT INDEXED WHERE TRU
```

---

## Crash 113: `17fcdd42201e233b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134139`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 114: `252d912d578ba4c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136009`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE, c3 INTEGER UNIQUE, b TEXT UNIQUE, a VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE
```

---

## Crash 115: `e04b29157ff53cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136176`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE, c3 INTEGER UNIQUE, b NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 116: `6e7f59195a38af71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154043`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL);
```

---

## Crash 117: `5d97f7b0483f02a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155685`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_DATE IS NOT NULL % NOT CURRENT_TIME LIKE random() ESCAPE FALSE)); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 118: `938d4521d213be4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156232`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 119: `b40a5dbcc60c4770` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160454`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS a;
```

---

## Crash 120: `588a399de0951d5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160641`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (0.0); VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 121: `089ba46848842538` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161170`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATU
```

---

## Crash 122: `e57ab723e460a3ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161352`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHERE FAL
```

---

## Crash 123: `e9a51c10d4695d3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161607`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (min(CURRENT_DATE) IS FALSE COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 124: `3329c5e9106ab21e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161760`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT NULL)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 125: `e5698af78a5f3e36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161999`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (max(TRUE)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 126: `6daf5a62d538c2c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162931`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE NOT IN (SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME LIMIT TRUE)); SELECT printf('%.*g', 2147
```

---

## Crash 127: `3c71dad6dffaae83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163132`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE / CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 128: `8b5f39560557f296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163423`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE / ' _1_5X vno__2'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH p AS MATERIALIZED (SE
```

---

## Crash 129: `79c9db06a4d414aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163527`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE / NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH p AS MATERIALIZED (SELECT ~NULL,
```

---

## Crash 130: `9897cddbaf36e189` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166098`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CURRENT_TIMESTAMP FROM p ORDER BY CURRENT_DATE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 131: `6206868cc5deaa00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166806`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 132: `dbf1a2624a3b3fa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166965`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 133: `23d0d9e64adfe6d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167004`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT -87.813842148098614499001950017427731324E395294721059669170136859); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 134: `3fa39612a495fae9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167348`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 135: `61bc90e5a86293ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167510`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 136: `dcd76460c481a456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167516`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 137: `973819f3e6b7a0a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167886`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, c1 DATE NOT NULL); INSERT INTO p (c2) VALUES (NULL) ON
```

---

## Crash 138: `cf45f876d1768305` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167917`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(b REAL CHECK (FALSE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUA
```

---

## Crash 139: `047fadec21434675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167927`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME << CURRENT_TIME); V
```

---

## Crash 140: `45604db50c8a6de0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168035`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), c3 GENERATED ALWAYS AS (a * a) UNIQUE, c2 INTEGER NOT NULL DE
```

---

## Crash 141: `d3157eaa0e1e4d59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168255`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT 48253613543967.14807593010308179898966900060598003637862692132899266525396741E-770, rowid VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALS
```

---

## Crash 142: `8681c4b0a754a4aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168425`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB DEFAULT -0); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 143: `f3bd359b0e64f415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168602`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT group_concat(NULL) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIMESTAMP COLLATE NOCASE ASC NULLS LAST) AS e6__0v_02k010v_44_8_m73c__8838
```

---

## Crash 144: `6bb4bbf9a56033b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIMESTAMP COLLATE NOCASE ASC NULLS LAST) AS e6__0v_02k010v_44_8_m73c__8838_z_008mc__
```

---

## Crash 145: `8bef96917945cedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY NOT EXISTS (VALUES (FALSE))) AS e6__0v_02k010v_44_8_m73c__8838_z_008mc____461_r858_80278_29_
```

---

## Crash 146: `d595b2aab28794a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169356`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT (WITH p AS (VALUES (NULL)) SELECT * FROM p WHERE CURRENT_TIME GROUP BY FALSE WINDOW w1 AS ()) AS e6__0v_02k010v_44_8_m73c__8838_z_008mc____461_r
```

---

## Crash 147: `8cb5b664d0f7fb53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177270`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH p AS (VALUES (NULL)) VALUES (group_concat('7 q_ -NcA98wyLg') FILTER (WHERE CURRENT_TIME) OVER ()) UNION VALUES (FALSE); SELECT printf(
```

---

## Crash 148: `091b97992a5e9b8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179707`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p SELECT CURRENT_TIMESTAMP; PRAGMA quick_check; SELECT printf('%.*f', 21474836
```

---

## Crash 149: `38e2550b5097f2a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181134`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN SELECT NULL AS i__z_es0a__t1g4cnz1__8r3_l5_a___7 INTERSECT SELECT count(*) OVER (ORDER BY TRUE ASC N
```

---

## Crash 150: `312527f29a4226c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181336`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN SELECT NULL AS i__z_es0a__t1g4cnz1__8r3_l5_a___7 INTERSECT SELECT * FROM p NOT INDEXED WHERE TRUE GR
```

---

## Crash 151: `141b89425e3b95dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211704`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, CURRENT_TIMESTAMP || FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TI
```

---

## Crash 152: `1276ac17866d24ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214610`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid, c1); VALUES (TRUE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 153: `9d8ddd9ebf7c0c19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214833`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a + 0) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); 
```

---

## Crash 154: `8ec2d80c2dd432a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214918`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a * a) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); 
```

---

## Crash 155: `f82bde64fbd7b403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214996`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, NOT EXISTS (SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIM
```

---

## Crash 156: `b30c55324a79226e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215514`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL, c1 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE, CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CURRENT_TIMESTAMP || CUR
```

---

## Crash 157: `04e499afa28a622d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245083`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (X'bACEBeFAC7bb') UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 158: `82806450bd014cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245213`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 159: `648a8181848f0688` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246904`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE); SELECT * FROM (SELECT * FROM p WHERE CUR
```

---

## Crash 160: `b9fea5c91c096cf9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249488`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC PRIMARY KEY); INSERT INTO q WITH RECURSIVE t2 AS (SELECT *) SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY TRUE
```

---

## Crash 161: `f9c5114927b12e67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251389`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT group_concat(NULL) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 162: `ca9eabbecad53ae4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252312`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT NULL AS i__z_es0a
```

---

## Crash 163: `84b84ea1ad485a7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253062`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT -6483241051747.7110589405e+3); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(
```

---

## Crash 164: `e8e6307395bb5b4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253489`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT 5373210916419197262203355485.72E080); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 165: `803b903368d93993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253830`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAU
```

---

## Crash 166: `11a9a503b15b404a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256457`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME << CURRENT_TIME); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p
```

---

## Crash 167: `a2d03e73e48f2ba9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257478`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (FALSE / ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p WHERE FA
```

---

## Crash 168: `e5d29ff0258d3383` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258140`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); VALUES (NUL
```

---

## Crash 169: `0b507ad53df73e51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258233`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); VALUES (NULL) EXCEPT SELECT DISTINCT * FROM p ORDER BY NULL DESC NULLS LAS
```

---

## Crash 170: `0bbf4677d6c986ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259416`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT X'bACEBeFAC7bb')); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEF
```

---

## Crash 171: `c52c2417bd2a9d7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261644`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL) EXCEPT SELECT DISTINCT * FROM p ORDER BY NULL DESC NULLS LAST, NULL ASC NULLS FIRST; CREATE VIRTUAL TAB
```

---

## Crash 172: `c48e7287499bebb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267269`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483648)); CREATE TABL
```

---

## Crash 173: `c04e1164892e145c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267399`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 174: `7a19fde3865f1964` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268050`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY, c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TIME; CREATE VIRTU
```

---

## Crash 175: `8094e30ee32ee9cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268107`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT *, count(*) OVER () FROM q NOT INDEXED WHERE CURRENT_TIME; CREATE VIR
```

---

## Crash 176: `28956217593de634` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000147696`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VA
```

---

## Crash 177: `84446f1586ad91da` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000227448`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE (WITH p AS (SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP 
```

---

## Crash 178: `f81fccc51258109f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000257870`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT OR REPLACE INTO p VALUES (~FALSE); EX
```

---

## Crash 179: `fd862f8bdd578317` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000261008`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHER
```

---

## Crash 180: `31a7b9b280eb52a2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273407`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(FALSE IS NOT CURRENT_DATE COLLATE BINARY) NOT IN (VALUES (CURRENT_DATE)) ASC NULLS LAS
```

---

## Crash 181: `25b5f267efd196bf` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273413`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER (PARTITION BY CURRENT_TIMESTAMP) ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VALUES (CURREN
```

---

## Crash 182: `faf93329e411f901` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273419`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VALUES (CURRENT_DATE)) ASC NULLS LAST LIMIT 
```

---

## Crash 183: `8635aede4072230d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273427`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(NOT FALSE < TRUE COLLATE BINARY) NOT IN (VALUES (CURRENT_DATE)) ASC NULLS LAST LIMIT F
```

---

## Crash 184: `8daf28b343183afe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273440`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2, c1); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VALUES (CURRENT_DATE)) ASC NULLS LAST LI
```

---

## Crash 185: `7de2086bb90e0812` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273450`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VALUES (NULL NOT LIKE FALSE = TRUE)) ASC NUL
```

---

## Crash 186: `8ce850e79c687d00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273470`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER (ORDER BY CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN 
```

---

## Crash 187: `ef91e91ff36e6f52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273481`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (VALUES (CURRENT_DATE)) ASC NULLS LAST LIMIT 
```

---

## Crash 188: `40fa593e38751e97` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000273592`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT count(*) OVER () ORDER BY max(CURRENT_TIMESTAMP COLLATE BINARY) NOT IN (SELECT count(*) OVER () ORDER BY max(CURRENT
```

---
