# Crash Triage Report

**Total crashes:** 264  
**Unique crash sites:** 264  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 264 | 264 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `c95a31f12f6e3f20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN, c3 GENERATED ALWAYS AS (a) NOT NULL, c2 REAL GENERATED ALWA
```

---

## Crash 2: `77433fd6b2a4073e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000098`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO p VALUES (last_insert_rowid() IS NOT FALSE | TRUE COLLATE RTRIM MATCH CASE CURRENT_TIMESTAMP WHEN TRUE NOTNULL IN (CURREN
```

---

## Crash 3: `9a34e68ea2356ed4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000105`

```sql
SELECT substr('-5_', 0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT ~CURRENT_DATE < NOT FALSE || -CURRENT_DATE IN (SELECT DISTINCT * FROM p
```

---

## Crash 4: `7d77fd2cc455bc89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000661`

```sql
SELECT printf('%.*f', 0, 1.0); SELECT substr('-Q--y70-- R 4', -2147483648, 4294967296); SELECT substr('', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO 
```

---

## Crash 5: `92991b375a342316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000700`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); SELECT EXISTS (VALUES (CURRENT_DATE, TRUE)) <> EXISTS (WITH RECURSIVE q (c1, c1, b, c1) AS NOT MATERIALIZED (SELECT p.* FROM t1 NOT INDEXE
```

---

## Crash 6: `a1a27b7628dcde4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000952`

```sql
SELECT substr('1 2-Mw__c038_', -2147483649, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; SELECT s.* FROM p NATURAL JOIN t3 WHERE +CURRENT_TIMESTA
```

---

## Crash 7: `a42779f3aba70824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001164`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t1 VALUES (CURRENT_TIME OR CURRENT_TIME IS NOT NULL & NULL BETWEEN RAISE(IGNORE) 
```

---

## Crash 8: `3b28c2971bc06c22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001404`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, b, c1, a, c3, a); INSERT OR FAIL INTO p VALUES (NULL AND NULL NOT LIKE NOT FALSE IS NULL IN (CURRENT_TIMESTAMP) NOT LIKE group_concat(CAST(CU
```

---

## Crash 9: `3f112fdb9af9375d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001637`

```sql
SELECT printf('%.*f', -2147483649, 1e308); CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL); SELECT +CURRENT_TIMESTAMP IS N
```

---

## Crash 10: `f36b7274e53521de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001733`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CASE WHEN NULL THEN TRUE END >> CAST(NULL AS VARCHAR(255)) AS a FROM p WHERE EXISTS (SELECT CURRENT_TIME IS NOT NULL ORDER BY NULL COLLATE RTRIM 
```

---

## Crash 11: `b4abc3e9a447f0d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001957`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP AS a FROM p WHERE EXISTS (SELECT CURRENT_TIME IS NOT NULL ORDER BY NULL COLLATE RTRIM DESC NULLS LAST, CURRENT_TIMESTAMP ASC NU
```

---

## Crash 12: `8cd6deab2804c816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001963`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CAST(NULL AS VARCHAR(255)) AS a FROM p WHERE EXISTS (SELECT CURRENT_TIME IS NOT NULL ORDER BY NULL COLLATE RTRIM DESC NULLS 
```

---

## Crash 13: `3ea2880e28ba5a09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001975`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CASE WHEN NULL THEN TRUE END >> FALSE AS a FROM p WHERE EXISTS (SELECT CURRENT_TIME IS NOT NULL ORDER BY NULL COLLATE RTRIM DESC NULLS LAST, CURR
```

---

## Crash 14: `0be60c1925febec2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CASE WHEN NULL THEN TRUE END >> CAST(NULL AS VARCHAR(255)) AS a FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY NULL COLLATE RTRIM DESC NU
```

---

## Crash 15: `ca46f29c9a2ca561` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001993`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CASE WHEN NULL THEN TRUE END >> CAST(NULL AS VARCHAR(255)) AS a FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_DATE DESC NULLS LA
```

---

## Crash 16: `e963a004658989a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002022`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY NULL ASC NULLS LAST); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT IN
```

---

## Crash 17: `9f046afe7346e715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY FALSE DESC, CURRENT_TIMESTAMP ASC NULLS FIRST); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 18: `074108c9d1651478` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002045`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN
```

---

## Crash 19: `2f78f7eb91f07148` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002051`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUE
```

---

## Crash 20: `086f17cad05a55a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002065`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME, CURRENT_DATE) ORDER BY FALSE ASC NULLS FIRST, 
```

---

## Crash 21: `6425404a85dbae71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002077`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME, C
```

---

## Crash 22: `8fd390791fb24aa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002156`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CASE WHEN NULL THEN NULL END >> FALSE AS a FROM p WHERE EXISTS (SELECT NULL ORDER BY NULL COLLATE RTRIM DESC NULLS LAST, CURRENT_TIMESTAMP ASC NU
```

---

## Crash 23: `32b8dbeb5d6e2aee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002227`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN 
```

---

## Crash 24: `8f6cc1277328b0c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002254`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CURRENT_DATE AS a FROM p WHERE EXISTS (SELECT CURRENT_TIME IS NOT NULL ORDER BY NULL COLLATE RTRIM DESC NULLS LAST, CURRENT_
```

---

## Crash 25: `631836c487e8e7d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002320`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP AS a FROM p WHERE EXISTS (SELECT RAISE(IGNORE) ORDER BY NULL COLLATE RTRIM DESC NULLS LAST, CURRENT_TIMESTAMP ASC NULLS FIRST);
```

---

## Crash 26: `381e8ef45f0e5085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002415`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 27: `7147b0b095f15059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002933`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE q (c3) AS (WITH RECURSIVE t3 AS (VALUES (FALSE, CURRE
```

---

## Crash 28: `ac9e4df7e889628a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003045`

```sql
SELECT printf('%.*g', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT t2.* FROM (SELECT q.*, q.* FROM q WHERE (+EXISTS (SELECT r.* LIMIT RAISE(IGNORE)) REGEXP CURRENT_DAT
```

---

## Crash 29: `ad37a1013dd4b920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005533`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT TRUE A
```

---

## Crash 30: `534410f4d5bac353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005614`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT TRUE AS f7u2_ux5n4y_4nu_0rf
```

---

## Crash 31: `592954425f94950f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006445`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT p.* FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (RAISE(IG
```

---

## Crash 32: `120ece1b7001f6ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (RAISE(IGNORE) -> N
```

---

## Crash 33: `01c19ea7cb9777d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006668`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a IS NULL) NOT NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT * UNION ALL V
```

---

## Crash 34: `9644457088f45591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007589`

```sql
SELECT substr('  __r-_- 6', -9223372036854775808, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO p DEFAULT VALUES; SELECT NOT RAISE(IGNORE) NOTNULL AS f_e_0bc8gt_0__f3_7
```

---

## Crash 35: `d522a97018cbfc84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007619`

```sql
SELECT printf('%.*f', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT RAISE(IGNORE) * CURRENT_DATE AS x_eums3_8_1k_w_1_
```

---

## Crash 36: `e636409d868dcaf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007766`

```sql
SELECT printf('%llu', 4294967296, '-w'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT t3.* FROM q NATURAL JOIN p WHERE NOT EXISTS (SELECT ALL * FROM p) MATCH total_changes() FILTER
```

---

## Crash 37: `871225a2feb63360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007949`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); EXPLAIN QUERY PLAN VALUES (q.c3 IN (SELECT *, * FROM p AS a CROSS JOIN q INDEXED BY c3 , q AS p WHERE q.c1 IS NO
```

---

## Crash 38: `979651f2883957ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007996`

```sql
SELECT printf('%.*e', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, a); INSERT OR FAIL INTO s VALUES (json(RAISE(IGNORE) COLLATE NOCASE) FILTER (WHERE CURRENT_TIMESTAMP) IS NULL); EX
```

---

## Crash 39: `da22531b3a329b57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008022`

```sql
SELECT round(1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT * FROM t2 NOT INDEXED GROUP BY FALSE, RAISE(IGNORE) COLLATE BINARY UNION VALUES
```

---

## Crash 40: `4221a7453efde8e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008060`

```sql
SELECT round(1e-308, 4294967296); SELECT printf('%.*e', 9223372036854775807, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c2); SELECT * FROM t3 INDEXED BY b WHERE q.c3 GROUP BY +
```

---

## Crash 41: `d022d75192b1ef70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008420`

```sql
SELECT printf('%s', -2147483649, 'R- 3 --_-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (c2, b, c2) VALUES (RAISE(IGNORE) NOTNULL NOT IN (RAISE(IGNORE) & CURRENT_TIMESTAM
```

---

## Crash 42: `80b7cba9387833e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008570`

```sql
SELECT printf('%lld', 2147483647, '_zs_ t42T8_0    _R'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); SELECT TRUE UNION ALL SELECT q.*, CURRENT_DATE MATCH -CURRENT_TIMESTAMP IS NOT RAIS
```

---

## Crash 43: `29262bb76d8a0d0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008648`

```sql
SELECT printf('%f', -9223372036854775808, 'y_588o--R2 _-ykK -2'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3); REPLACE INTO s VALUES (-RAISE(IGNORE) COLLATE BINARY >> NOT EXISTS (
```

---

## Crash 44: `18b9016e9a22df13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008673`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3, c3, b, c2, _rowid_); SELECT CASE EXISTS (SELECT FALSE) WHEN CURRENT_TIME NOT NULL MATCH CURRENT_DATE IN (CURRENT_TIMESTAMP) THEN NULL N
```

---

## Crash 45: `02772b939d9e01ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008795`

```sql
SELECT printf('%.*f', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT TRUE REGEXP CURRENT_TIMESTAMP REGEXP -FALSE IS NOT ~CURRENT_DATE | CURRENT_DATE % iif(CURR
```

---

## Crash 46: `aeb7753d489761d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012346`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 
```

---

## Crash 47: `ae0e4759ceb73ecd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012399`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_DATE AS DATE)) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 48: `fbdeca09b4bbaf24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013039`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 49: `36debef7ac52b575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013291`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 50: `07e95f120567d2e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016594`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (TRUE); SELECT hex(zeroblob(0)); SELECT h
```

---

## Crash 51: `a154d3cb716b0a13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016903`

```sql
SELECT printf('%.*g', -2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); VALUES (NOT count(*) | -(CURRENT_TIME) LIKE ~FALSE ESCAPE CURRENT_DATE >= FALSE ->> FALSE NOT IN (
```

---

## Crash 52: `92092a09cfd91645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017187`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1));
```

---

## Crash 53: `aeb25651e361b1ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019304`

```sql
SELECT substr('_HF3 m-KP2  --_', -2147483649); SELECT printf('%.*f', 4294967296, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SE
```

---

## Crash 54: `33114007f390f984` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020580`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT X'', c1 BLOB NOT NULL); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integr
```

---

## Crash 55: `c7c32d20d12dcf9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020841`

```sql
SELECT printf('%.*s', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (min(FALSE ->> +NULL MATCH FALSE || total_changes() FILTER (WHERE -NULL) NOT LI
```

---

## Crash 56: `16ae900f1a67890e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021601`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 57: `eff6a6e5dfc659d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022690`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES;
```

---

## Crash 58: `0923a00e8db77e22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023273`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p D
```

---

## Crash 59: `24c4c4475c1e15e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026672`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE >> FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSE
```

---

## Crash 60: `7975c30da0a16792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028117`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 61: `7bf55641f8fc5a0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028126`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 62: `8ed494420d17494b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029224`

```sql
SELECT printf('%.*d', 2147483648, -1.0); SELECT substr('', 1, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT *, *, ~changes() FROM q JOIN s ms_ ON CASE WHEN CAS
```

---

## Crash 63: `42426d18d2a604a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE -FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integ
```

---

## Crash 64: `23314357abca3259` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030361`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE -CAST(FALSE AS FLOAT)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 WITH r (c3)
```

---

## Crash 65: `c468fbc7e347b6f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030610`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT TRUE FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c1); INSERT INTO q VALUES (CURRENT_DAT
```

---

## Crash 66: `53d14a2f84ca98c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT TRUE IS TRUE FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VAL
```

---

## Crash 67: `5fc843c850b3ad97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031567`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT -32919951206631656737725.252430757878628402043987834786063864450303702125005086144427191e1295); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN
```

---

## Crash 68: `f63d9ae63a6d3b37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031648`

```sql
SELECT printf('%.*e', -9223372036854775808, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1));
```

---

## Crash 69: `81d52c12d09a5164` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031838`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1));
```

---

## Crash 70: `bed9c3562ed4ed07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032061`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (CASE FALSE WHEN TRUE THEN TRUE NOT LIKE FALSE MATCH FALSE END); PRAGMA quic
```

---

## Crash 71: `e67790b1e15963ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032202`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (CASE CURRENT_TIME WHEN CURRENT_DATE THEN CURRENT_TIME END); PRAGMA quick_ch
```

---

## Crash 72: `12238d760bd7b070` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032333`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (CASE CURRENT_TIME WHEN CURRENT_TIMESTAMP IS NULL THEN CURRENT_TIME END); PR
```

---

## Crash 73: `e742cacf6498ff03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033003`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 74: `ba4d365f8d3b259b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036924`

```sql
SELECT printf('%lld', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM t3 INDEXED BY c1 INTERSECT SELECT * FROM p NOT INDEXED; CREATE TABLE IF NOT EXI
```

---

## Crash 75: `446145160e0a2b50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037212`

```sql
SELECT round(-1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 76: `c360fb11b15d783f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037364`

```sql
SELECT substr('_9uC  -8  5l', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO t3 VALUES (~FALSE & ~CURRENT_DATE >= TRUE COLLATE NOCASE != CU
```

---

## Crash 77: `7379e32d8d6f5e0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039157`

```sql
SELECT printf('%x', -9223372036854775808, '3-__q0 _XY   '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO q VALUES ((CURRENT_TIMESTAMP) BETWEEN ~NOT NULL IS CURRENT_TIMESTA
```

---

## Crash 78: `cb0a56d8bb98f785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039168`

```sql
SELECT printf('%x', -9223372036854775808, '3-__q0 _XY   '); SELECT printf('%.*s', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p JOIN p a ON N
```

---

## Crash 79: `a882cdd5ad0c1559` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042288`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO p SELECT DISTINCT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 80: `9c79b83da78802c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045892`

```sql
SELECT round(-1.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1));
```

---

## Crash 81: `5d5a28c9129bbc2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046939`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, b BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAU
```

---

## Crash 82: `5ae2280f4786a8e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046981`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (randomblob(TRUE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES
```

---

## Crash 83: `d2f166e295bd8d3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046993`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT
```

---

## Crash 84: `b71b47ec53390dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047026`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1));
```

---

## Crash 85: `b306c5ec00fbccc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049528`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (CAST(CURRENT_TIMESTAMP <> CURRENT_DATE MATCH RAISE(IGNORE) |
```

---

## Crash 86: `c3be8dc417d434f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050673`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) EXCEPT SELECT NULL ORDER BY NULL; SELECT 
```

---

## Crash 87: `304210861d5c971e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050883`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 88: `a52f16ce4eab0c00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052183`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); WITH RECURSIVE t1 AS (SELECT *) INSERT INTO q VALUES (CURRENT_DATE IN (TRUE)); PRAGMA integrity_ch
```

---

## Crash 89: `cade7f2641d22744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054007`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (TRUE BETWEEN FALSE AND NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 90: `0a909c85d625af30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055424`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 91: `5eafcc2df062fcbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055430`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 92: `e8723eb2e5001116` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055436`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 93: `dde1b7d208bd625d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056527`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP ORDER BY -6896718494623665274669071.930 DESC, CURRENT_TIMESTAMP ASC NULLS FIRST); CREATE VIRTUAL 
```

---

## Crash 94: `ee9c1a13f220aa4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056880`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CAST(CURRENT_TIME IS CURRENT_TIME COLLATE NOCASE AS VARCHAR(255)) AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SEL
```

---

## Crash 95: `358771d7399e9b2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057145`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CAST(CURRENT_TIME IS FALSE AS VARCHAR(255)) AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*f', -21
```

---

## Crash 96: `4a050b7ed07e9a90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058043`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT group_concat(TRUE, 'J-__d_zY'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VALUES (-CURRENT_TIME | CAST((FAL
```

---

## Crash 97: `073709714f782139` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063265`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 98: `5f9a863467921004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064588`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c3, 
```

---

## Crash 99: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065867`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 100: `2d44d0cdeec23d32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072512`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BLOB, b VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 101: `c0aefaf42fe85132` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072743`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE CHECK (TRUE)); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g
```

---

## Crash 102: `646bbcf1d68863a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072870`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', 2
```

---

## Crash 103: `38985e57ee408c0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072876`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT prin
```

---

## Crash 104: `45d2631cdff6a26a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073119`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT DEFAULT X'095fdCDdC8D0Ac'); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE 
```

---

## Crash 105: `10a27408387b558d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074486`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 106: `7661174d417f3170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075938`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 107: `5be578b530adc5b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076714`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (EXISTS (SELECT FALSE AS a LIMIT FALSE OFFSET TRUE)); PRAGMA integrity_check
```

---

## Crash 108: `5bbe8de53029cc2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077776`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 109: `d5b49225bb77b1eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077908`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT X'095fdCDdC8D0Ac'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 110: `a8db58f5841bf47a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078183`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT -32919951206631656737725.252430757878628402043987834786063864450303702125005086144427191e1295); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VA
```

---

## Crash 111: `6e5c90a016bb4bd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078216`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * F
```

---

## Crash 112: `de11c51c5b07703e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078549`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT ''); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, c3); SEL
```

---

## Crash 113: `36e49786f3a3d12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079387`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT NOT EXISTS (SELECT * FROM p GROUP BY CURRENT_DATE) FROM p WHERE TRUE) AS sub1; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 114: `10e51fcf3bd8daff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080543`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE -CAST(FALSE AS TEXT)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES
```

---

## Crash 115: `bfe2fa89e96c8a1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080852`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE typeof(FALSE)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); REPLACE INTO t3 VALUES ((SELECT 
```

---

## Crash 116: `46619cdd5de6ab4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081195`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT NOT EXISTS (VALUES (CURRENT_DATE) INTERSECT VALUES (TRUE)) FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 117: `6f56df79e1f18a4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082816`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT X''); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 118: `952c67084ae1fca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084128`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE >> -6896718494623665274669071.930 IS NOT FALSE COLLATE BINARY); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%
```

---

## Crash 119: `3b63280025bee1ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE >> -6896718494623665274669071.930 IS NOT FALSE COLLATE BINARY); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT substr('d
```

---

## Crash 120: `7fcdff06dc5ec35b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084378`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE >> CURRENT_TIMESTAMP IS NOT FALSE COLLATE BINARY); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 121: `f99c9e3dbe175635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (TRUE IS NOT FALSE COLLATE BINARY); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3
```

---

## Crash 122: `0c51b112f95f57c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085216`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (random()); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 123: `e3544bc674a8dc90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085489`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (FALSE); VALUES (randomblob(CURRENT_TIME)); SELECT substr('H', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, b
```

---

## Crash 124: `106794466ea970c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085561`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (FALSE); VALUES (last_insert_rowid()); SELECT substr('H', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, b); IN
```

---

## Crash 125: `64ac6db8c7dacc8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085976`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (TRUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (FALSE); VALUES (CURRENT_
```

---

## Crash 126: `ffe2efbdeb656c92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086175`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP IS NOT randomblob(TRUE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 127: `665aeef604ded7f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086334`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP IS NOT changes()); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INT
```

---

## Crash 128: `c781301b73cb5969` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086503`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (randomblob(TRUE) >> FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALU
```

---

## Crash 129: `acb42aed2113ba2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090542`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 130: `74c4587ddd172bce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091454`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 131: `c635b32da131b9c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091978`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE INDEX IF NOT EXIS
```

---

## Crash 132: `e45ad2e3abb5d38c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092118`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT V
```

---

## Crash 133: `92309b8216327635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092421`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL DEFAULT ' -r-0-r  sg'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 134: `a884fdc6dda4fcf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092668`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT '- 7G _j5', b REAL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); I
```

---

## Crash 135: `7b0953f21d404304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093028`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRE
```

---

## Crash 136: `4950d579a1f34fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093349`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); INS
```

---

## Crash 137: `f2cc201ec4a3dae0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 138: `06a128438f67dc73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094119`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 139: `99e7395c9673c3ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094518`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIME || FALSE)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 140: `c095f719ed2715c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094782`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIME || CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SEL
```

---

## Crash 141: `84583e0082b25b6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095033`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (TRUE || NULL)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT OR REPLAC
```

---

## Crash 142: `05288a9941e11b14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098033`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); VALUES (CAST(CURRENT_TIMESTAMP AS DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 143: `48325f7b00144af1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL = NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); VALUES (RAISE(IGNORE), CURRENT_TIMESTA
```

---

## Crash 144: `3c810393f92f61cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107439`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP ESCAPE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT
```

---

## Crash 145: `a9083cd4520ff9bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108770`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (CURRENT_
```

---

## Crash 146: `9dffcc646f24d8d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108790`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT DEFAULT NULL, rowid INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 
```

---

## Crash 147: `d706285a03c053ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108982`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 DEFAULT VALUES; PRAGMA quick_ch
```

---

## Crash 148: `2c4fec4c7323335c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108988`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY, rowid INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 DE
```

---

## Crash 149: `f6a1ca34b0c8854c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109021`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT DEFAULT -8663015782185191943550033765384095740824414758947349659903653638.0E386547, rowid INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SEL
```

---

## Crash 150: `41b22389a778519c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109742`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c2 NUMERIC UNIQUE, c3 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSE
```

---

## Crash 151: `6d49abd5bf0b95bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109838`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c2 VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO t2 V
```

---

## Crash 152: `9ceca1f4534491de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109974`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SELECT substr('  0tal__', 1
```

---

## Crash 153: `8e58febe09d5972d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111925`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TAB
```

---

## Crash 154: `4e3dcd7437999c4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113047`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE TRUE IS NULL COLLATE RTRIM) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 155: `47eb33fd6cf16705` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113354`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE + CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 156: `f969a47d1d0e3fa0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114249`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT * FROM p WHERE unicode(CURRENT_TIMESTAMP) GRO
```

---

## Crash 157: `e0c2d6f2c57e9a95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114550`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE random()) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 158: `be2deeb326d9baeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114877`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE TRUE < CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 159: `db9bf77814a84fcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115073`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(TRUE < CURRENT_TIMESTAMP AS DATE)) AS sub1; CREATE VIRTUAL 
```

---

## Crash 160: `3adbcc7dab69e330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115392`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE TRUE OR FALSE) AS sub1; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(
```

---

## Crash 161: `0985be61f5968867` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115869`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE GLOB TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 162: `c7a2ced4fd52e62f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116985`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS BLOB)) AS sub1; SELECT printf('%.*g', 2147483647, 
```

---

## Crash 163: `2b2f7c1648b4dec5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117819`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT TRUE << CURRENT_DATE & FALSE FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL
```

---

## Crash 164: `80970ab2e8a8b300` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118152`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT CURRENT_TIME & group_concat(FALSE, 'J-__d_zY') FROM p WHERE NULL) AS sub1; CREA
```

---

## Crash 165: `9b83e4c10ec6b272` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118247`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT CURRENT_TIME & count(*) FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 166: `6191b268eb02ff1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118645`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_DATE AS INT)) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 167: `a6c273bd0a5d7c8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119810`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT *, *, * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 168: `388df2917bfe6686` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121725`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); INSERT INTO p SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () ORDER BY CURRENT_TIME DESC; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUA
```

---

## Crash 169: `3c20a4561e2d3520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121963`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT GENERATED ALWAYS AS (TRUE) STORED, rowid INTEGER NOT NULL); INSERT INTO p SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () ORDER BY CURRENT_TIME DESC; EXPLAIN Q
```

---

## Crash 170: `ad48fb9efe60ceec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128224`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT X'aBfB'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO 
```

---

## Crash 171: `a18ebc962cbb73db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129121`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p SELECT lower(TRUE) ORDER BY CURRENT_TIME DESC; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 172: `697afa692560b440` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129188`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); INSERT INTO p SELECT count(*) ORDER BY CURRENT_TIME DESC; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 173: `b737bb64d3b8a108` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130486`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT CURRENT_TIME NOT LIKE TRUE AS s1__0c1 FROM p WHERE TRUE) AS sub1; SELECT printf
```

---

## Crash 174: `0840708429c72d9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130693`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT CURRENT_TIME LIKE NULL NOT LIKE CURRENT_TIMESTAMP ISNULL AS s1__0c1 FROM p WHER
```

---

## Crash 175: `5b7fedc64b6d09d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130954`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE TRUE NOT NULL) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 176: `731dea24b10d9961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131378`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE IN (CURRENT_DATE)) AS sub1; CREATE VIRTUAL TABLE IF
```

---

## Crash 177: `90bc51aec4de6d59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131606`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE IN (CURRENT_TIME, FALSE)) AS sub1; CREATE VIRTUAL T
```

---

## Crash 178: `38b70522bd013c10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132690`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(NOT NOT NOT NOT NOT NOT NOT NOT NOT CURRENT_TIME AS DATE)) 
```

---

## Crash 179: `48b9d7621882c070` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134006`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE CAST(TRUE OR FALSE AS DATE)) AS sub1; SELECT printf('%.*f', -214
```

---

## Crash 180: `be847dd9480618a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134222`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE BETWEEN FALSE AND NULL OR FALSE) AS sub1; SELECT printf('%
```

---

## Crash 181: `151fd2de86ff8416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135252`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT * FROM p WHERE unicode(CURRENT_TIMESTAMP) GRO
```

---

## Crash 182: `61fed1f7e5953ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135709`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT group_concat(TRUE, '_-_ -q-_hu B -cVPD') OVER
```

---

## Crash 183: `8261efae87abeda5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135819`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT *, * FROM p WHERE CURRENT_DATE GROUP BY NULL 
```

---

## Crash 184: `096917f75da22af9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135827`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT EXISTS (SELECT group_concat(TRUE, '_-_ -q-_hu B -cVPD') OVER
```

---

## Crash 185: `809eab0afadeb655` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135961`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE unicode(NULL)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 186: `7736932c8badce97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136230`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT DEFAULT 880092170139569546992891129491282356693941356264581211214834249842400092065675022937425998954816677815364337888683487995931868052849488536587122619.5e+54)
```

---

## Crash 187: `6b78e99b04c0a9b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137290`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE / -6896718494623665274669071.930) AS sub1; CREATE VIRTUAL 
```

---

## Crash 188: `ac9fcb096ecb5557` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137322`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE / NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 189: `97da34c63f4bfaf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137328`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE FALSE / TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 190: `3051aa1602d9ade7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137434`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT FALSE / CURRENT_TIMESTAMP COLLATE BINARY >= CURRENT_TIMESTAM
```

---

## Crash 191: `7684840be6d1ba11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137529`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); SELECT * FROM (SELECT * FROM p WHERE NOT FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 192: `1eac8f3bd0f8efb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140012`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); SELECT group_concat(TRUE, '_-_ -q-_hu B -cVPD') OVER (), * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 193: `e871caaccd7a5898` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141012`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP ESCAPE CURRENT_DATE > CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 194: `e71ad1daa048c796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141933`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE (SELECT * FROM (SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER ()) AS j43a WHERE TRUE GROUP BY FALSE LIMIT CUR
```

---

## Crash 195: `d01656d3f4c875fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142081`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE (SELECT * FROM (VALUES (TRUE)) AS j43a WHERE TRUE GROUP BY FALSE LIMIT CURRENT_TIME); SELECT printf('%.*g', 2147
```

---

## Crash 196: `ff48fa0bf8765e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142741`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAI
```

---

## Crash 197: `44e551b034d735de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154523`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_DATE > CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPL
```

---

## Crash 198: `309a3e5124da7cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154740`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIMESTAMP >> CAST(CURRENT_DATE IS NULL AS VARCHAR(255)) || FALSE)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); SELECT substr('_8
```

---

## Crash 199: `9cc3b82adfcd02b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154982`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) NOT NULL DEFAULT -26560022096597574165.8664e+08); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF N
```

---

## Crash 200: `8b8f3f96891cacdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156094`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT X'DAa0abBdDE'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 201: `4b0a2de465a09d5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156221`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT X'c2ee', _rowid_ DATE UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 202: `fa9afb20d2c79f7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156832`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER DEFAULT 8.89134917E+2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 203: `6a2845dbf48dc2e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156903`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER DEFAULT 8.89134917E+2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); INSERT INTO p 
```

---

## Crash 204: `74b34484f9bcb763` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159160`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (~-26560022096597574165.8664e+08); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 205: `169f513e37d1ed96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159437`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); INSERT OR REPLA
```

---

## Crash 206: `31c5ffd49c67d2f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159444`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); INSER
```

---

## Crash 207: `8f840563a034fe43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159450`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2
```

---

## Crash 208: `87dce35343f0629b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159469`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 209: `73672ab1fa887fb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160132`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (~CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 210: `597809da8cefd84d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160350`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2)
```

---

## Crash 211: `1e6136877de7fee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164342`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (FALSE); SELECT count(CURRENT_DATE) FILTER (WHERE FALSE) OVER () AS x; SELECT substr('24_D- ', 1); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 212: `d03bb5694e572854` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165610`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (TRUE % -TRUE); VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 213: `d1d83edcf1b22c9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165734`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (TRUE % -CURRENT_TIME); VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 214: `da5ea9ea11b05e35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (TRUE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 DATE, a GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, b INTEGER UN
```

---

## Crash 215: `22c4d0f3a2a11c76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 DATE, a GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, b INTEGER U
```

---

## Crash 216: `7b0bec9ca45dca05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167389`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY NULL, CURRENT_TIMESTAMP LIMIT CUR
```

---

## Crash 217: `93cd7e2edeca11ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167571`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT NULL)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 218: `4f6756b2c979a0af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168175`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CAST(TRUE AS FLOAT) <= FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL 
```

---

## Crash 219: `573afcde8b65e6ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168275`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CAST(TRUE AS VARCHAR(255)) <= FALSE); VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 220: `2da5b26f43542b07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168626`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 221: `67271b7f30f17414` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169063`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (X'cdE9352FEf1b'); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT IN
```

---

## Crash 222: `da4ba0fd82589218` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169372`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 223: `3d66ae7aefda46f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT INTO p VALUES (FALSE NOT BETWEEN NULL AND CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 224: `93aaf7ff634befc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171029`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT 363225248913218990.458756861809040756350262682610061790472054751030698597977239309368896899267005791899288599987294795489374386); INSERT INTO p DEF
```

---

## Crash 225: `bbff0b06b19c27a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171175`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRA
```

---

## Crash 226: `0e6dbeca1badfd60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174743`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE -CURRENT_DATE >> CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIV
```

---

## Crash 227: `cd819109304758da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175073`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT * FROM p WHERE -TRUE OR TRUE) AS sub1; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 228: `d5558168f27e80a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175786`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY NULL ASC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDING AND C
```

---

## Crash 229: `03f04e996ff542d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175940`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT group_concat(TRUE, '_-_ -q-_hu B -cVPD') OVER (ORDER BY CURRENT_TIME ASC, CURRENT_TIME DESC NULLS LAST) FROM (SELECT * FROM p WHERE NULL) AS sub1;
```

---

## Crash 230: `507141ddeb7ebecb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176701`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (FALSE)))) FROM p WHERE CURRENT_TIME) AS sub1; C
```

---

## Crash 231: `dff8096287773f78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176791`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); SELECT * FROM (SELECT CURRENT_TIME NOT IN (CURRENT_TIME NOT IN (NULL)) FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 232: `9a37d0cf1d920876` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177339`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT CURRENT_TIMESTAMP IN (SELECT ALL * FROM p NOT INDEXED) FROM p 
```

---

## Crash 233: `75d6d9804aea5294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177396`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT CURRENT_TIMESTAMP IN (SELECT ALL * FROM p NOT INDEXED) FROM p WHERE CURRENT_TIME) AS sub1; 
```

---

## Crash 234: `9a1b41ed47317500` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180276`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL DEFAULT '-'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 235: `a2963bd39a661e32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180822`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (EXISTS (SELECT FALSE AS a LIMIT FALSE OFFSET EXISTS (SELECT FALSE AS a LIMI
```

---

## Crash 236: `0246c9c6f71ba0d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181065`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (T
```

---

## Crash 237: `05bf39926bc35b54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181496`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE NOT LIKE 88009217013956954699289112949128235669394135626458121
```

---

## Crash 238: `b390974a2c3924ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184019`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT NOT NULL DEFAULT X'8CFE1Bce6b29'); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check
```

---

## Crash 239: `7387eb9b655b547f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185553`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT OR IGNORE INTO q VALUES (TRUE || CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 240: `0f93e28edd97c599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186254`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT X'aBadafFcbCad'); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 241: `2dc322c750545e0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186413`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c2 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 242: `0a27a08c4aacd449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199192`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED LIMIT 2; SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 243: `cb6ac64ebfb978ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199326`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT (CURRENT_TIME
```

---

## Crash 244: `92133a16a40be808` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200563`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid INTEGER PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 245: `5c545529d1f92873` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201327`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO p SELECT ALL * FROM q; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 246: `5298b3622796bcc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201498`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO p SELECT ALL * FROM p; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 247: `acfc66947a83a4d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202080`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO q SELECT DISTINCT * FROM q; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01)
```

---

## Crash 248: `2617d3f827dc230f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210059`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); SELECT group_concat(NULL, 'J-__d_zY'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 249: `79f0f1a8ce9f34b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP LIKE TRUE ESCAPE TRUE FROM p WHERE EXISTS (SELECT TRUE ORDER BY +RAISE(IGNORE) ASC NULLS LAST); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 250: `1a57d8d4d7a3e9af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211440`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP LIKE TRUE ESCAPE TRUE FROM p WHERE EXISTS (SELECT TRUE ORDER BY RAISE(IGNORE) ASC NULLS LAST); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 251: `6ec253dbac82bd83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211967`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT count(*) OVER () COLLATE NOCASE AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 252: `f28a4958cb9bafa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212204`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CAST(lower(TRUE) IS CURRENT_TIME COLLATE NOCASE AS VARCHAR(255)) AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELE
```

---

## Crash 253: `9a91363686701494` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212380`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT CURRENT_TIMESTAMP >> CAST(CURRENT_TIME AS VARCHAR(255)) AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*f', -2147483649,
```

---

## Crash 254: `7d37c1c71367994d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214795`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME NOT IN (TRUE))); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 255: `e37c8c9cdf9a25b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219919`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); WITH RECURSIVE t1 AS (SELECT *) INSERT INTO q VALUES (CURRENT_TIME IN (VALUES (CURRENT_TIMESTAMP))
```

---

## Crash 256: `c7cd5b063c658cf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226508`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC DEFAULT -82); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CAST(CURRENT_TIME AS DATE) >= CURRENT_TIMESTAMP); CREATE VIRTUAL TAB
```

---

## Crash 257: `8a0237e4a3962003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229582`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p (c3) VALUES (CURRENT_TIME) ON CONFLICT(c3) DO UPDATE SET _rowid_ = CURRENT_DATE; 
```

---

## Crash 258: `307a9ae2415db812` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231719`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME BETWEEN FALSE BETWEEN TRUE BETWEEN last_insert_rowid() AND NULL AND NULL AND NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEF
```

---

## Crash 259: `873f7f32284e4feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231976`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (CURRENT_TIME BETWEEN FALSE BETWEEN TRUE BETWEEN randomblob(TRUE) BETWEEN FALSE AND NULL AND NULL AND NULL AND NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT 
```

---

## Crash 260: `a41f8eed74f13715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232110`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (last_insert_rowid() BETWEEN FALSE AND NULL BETWEEN FALSE AND NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE); PRAGMA in
```

---

## Crash 261: `c4482f402a6dc0de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232345`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (json_valid(TRUE))); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 262: `4ac53b91fcab0643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232661`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (randomblob(TRUE))); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 263: `b03affecee5f4f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT count(*) OVER (ORDER BY NULL DESC NULLS LAST ROWS BETWEEN CURRENT_TIME PRECEDING AND FALSE FOLLOWING) AS a FROM p WHERE EXISTS (VALUES (CURRENT_T
```

---

## Crash 264: `40966e44da1202bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234435`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT count(*) OVER (ORDER BY NULL DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS a FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); 
```

---
