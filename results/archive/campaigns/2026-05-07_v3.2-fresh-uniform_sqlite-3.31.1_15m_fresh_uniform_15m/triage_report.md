# Crash Triage Report

**Total crashes:** 105  
**Unique crash sites:** 105  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 105 | 105 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `799bbe0d876dc99c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000110`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, _rowid_); SELECT +FALSE || (SELECT FALSE ISNULL LIKE CURRENT_DATE NOT IN (CURRENT_TIMESTAMP, FALSE, FALSE >> CURRENT_TIMESTAMP, TRUE ISNULL, 
```

---

## Crash 2: `ea6df81ee5836bc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000865`

```sql
SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); WITH RECURSIVE r (b) AS NOT MATERIALIZED (SELECT NOT EXISTS (SELECT * FROM t2 NOT INDEXED GROUP BY (coun
```

---

## Crash 3: `571330b741e248fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000988`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, _rowid_); WITH RECURSIVE s (c1) AS NOT MATERIALIZED (SELECT t3.* FROM p AS g6_apc_7_8i_0wm235_4_a435k37wh__2t0__93_a9__4___ GROUP BY CA
```

---

## Crash 4: `0ee80686becc5b07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001008`

```sql
SELECT printf('%f', -1, '5-a '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); EXPLAIN QUERY PLAN SELECT DISTINCT p.* FROM (s) CROSS JOIN (SELECT (CURRENT_DATE) AS a4_so___7bl__r6_3__
```

---

## Crash 5: `df559462479279ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001171`

```sql
SELECT round(1.0, -1); SELECT substr('--Y_10 F__W_', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_, c2); SELECT s.* FROM t3 WHERE EXISTS (SELECT DISTINCT char(CASE FALS
```

---

## Crash 6: `b85c9965784fccef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001204`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_, _rowid_, c3); WITH RECURSIVE t1 AS MATERIALIZED (SELECT DISTINCT * FROM t1 WHERE CURRENT_TIMESTAMP IS NULL / RAISE(IGNORE) < 
```

---

## Crash 7: `9bbad1c252f10ba1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001270`

```sql
SELECT printf('%.*f', 0); SELECT printf('%.*s', -9223372036854775808, 1e308); SELECT printf('%.*e', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); INSERT INTO q VALUES 
```

---

## Crash 8: `7f852993e73e4d6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001521`

```sql
SELECT printf('%.*g', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO s VALUES (NOT CURRENT_TIMESTAMP NOTNULL IS DISTINCT FROM TRUE <= NULL COLLATE RTRIM IS
```

---

## Crash 9: `50c95fa9facccba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001870`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL); SELECT substr('z  S_Bg 4-z Fp31', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1,
```

---

## Crash 10: `d8e6b8516d6b71be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001914`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT substr('z  S_Bg 4-z Fp31', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1,
```

---

## Crash 11: `9fb8ff105f759c92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001938`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); VALUES (FALSE); SELECT substr('z  S_Bg 4-z Fp31', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, a); INSERT INTO s
```

---

## Crash 12: `23dc52c27f370a24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001944`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT substr('z  S_Bg 4-z Fp31', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 13: `02d491a3ca9689c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002083`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT substr('z  S_Bg 4-z Fp31', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, a); INSERT INTO s (a) VALUES ((VALUES (+FALSE) I
```

---

## Crash 14: `29f0a5d101251893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003350`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, _rowid_ INTEGER NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); WITH t3 (rowid) AS (SELECT DISTINCT FALSE * unicode(EXISTS (WITH RECURSIVE r A
```

---

## Crash 15: `7cd8399cacab2514` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003377`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, _rowid_ INTEGER NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); WITH t3 (rowid) AS (SELECT DISTINCT FALSE * unicode(EXISTS (WITH RECURSIVE 
```

---

## Crash 16: `492b98f7e87e6fab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003398`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT, _rowid_ INTEGER NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 17: `1516388f3ead03ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003681`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q WHERE TRUE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS () UNION SELECT * FROM p WHERE FALSE GROUP BY RAISE
```

---

## Crash 18: `e4b251628f5db018` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q WHERE TRUE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS () UNION SELECT * FROM p WHERE FALSE GROUP BY RAISE
```

---

## Crash 19: `f70dcbec883942bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004096`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a, a) VALUES ((TRUE < TRU
```

---

## Crash 20: `ea2330913e16d5bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006366`

```sql
SELECT round(1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; SELECT CASE WHEN -~RAISE(IGNORE) OR NULL COLLATE RTRIM + NULL IS NULL ->> RAISE(IGNORE) I
```

---

## Crash 21: `098a26afc4a52966` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006762`

```sql
SELECT printf('%.*f', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO t3 VALUES (-CASE WHEN +FALSE THEN NOT EXISTS (SELECT ALL t1.*, * FROM t3 INDEXE
```

---

## Crash 22: `94dd9db63c12a17e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006814`

```sql
SELECT printf('%.*s', 9223372036854775807, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN WITH RECURSIVE r AS (SELECT t2.*) SELECT t3.*, CURRENT_TIMESTAMP <= FALS
```

---

## Crash 23: `543459823b040b34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006979`

```sql
SELECT printf('%lli', -1, ' aU-c_1G_ A_K sL- '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_DATE IS NOT CURRENT_TIMESTAMP COLLATE BINARY AS e_1________, +NULL LIKE CURREN
```

---

## Crash 24: `6a0477ed22deddee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007103`

```sql
SELECT printf('%.*f', -2147483649, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 WITH s AS NOT MATERIALIZED (SELECT DISTINCT CASE WHEN CAST(CURRENT_TIME AS DATE) TH
```

---

## Crash 25: `33115226df5b2c35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007151`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3, c2); INSERT OR ROLLBACK INTO t2 VALUES (NULL IS DISTINCT FROM abs(CURRENT_TIMESTAMP) FILTER (WHERE TRUE NOT
```

---

## Crash 26: `5f38f2763d6b84b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007273`

```sql
SELECT printf('%u', -1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (NULL COLLATE RTRIM IN (VALUES (CURRENT_TIME IS NULL)) LIKE NULL IN (FALSE) ESCAPE _rowid_ 
```

---

## Crash 27: `b2c8c4b7d9dc2783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010851`

```sql
SELECT round(-1.0, 2147483647); CREATE TABLE IF NOT EXISTS p(c2 REAL, _rowid_ FLOAT); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT TRUE, *, * FROM t3 WHERE E
```

---

## Crash 28: `2ffd5772fc44428b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011211`

```sql
SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO s VALUES (FALSE BETWEEN CURRENT_TIMESTAMP IS NOT NULL * CURRENT_DATE COLLATE RTRIM IS NULL / CU
```

---

## Crash 29: `ece83177af2a957e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012743`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) UNION ALL VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT 
```

---

## Crash 30: `54ee8aa22a605972` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019298`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, a, a, a); VALUES (F
```

---

## Crash 31: `9bec08b0c0560bda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019969`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CASE WHEN CURRENT_TIME THEN FALSE ELSE TRUE END); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 32: `46cf7049af58a99c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020165`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t3.* FROM p NATURAL JOIN t1 WHERE -819499179354063981.13964100169501595972114417379498670411571049103086453427
```

---

## Crash 33: `1b08473861ac5a91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023937`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT GENERATED ALWAYS AS (FALSE > NULL) STORED, rowid TEXT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 34: `defea6910d9fe7b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024711`

```sql
SELECT printf('%x', -9223372036854775808, 'v B'); SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c2, _rowid_, c1); INSERT OR FAIL INTO t2 VALUES (CURRENT_TIME != 
```

---

## Crash 35: `3b25cf5c0f0f3f7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026044`

```sql
SELECT substr('', 4294967295, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT INTO q (a, b) VALUES (CAST(RAISE(IGNORE) AS INTEGER) <= NULL <= CURRENT_TIME IS DISTINCT 
```

---

## Crash 36: `d9096f6cbc67f782` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027115`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); WITH RECURSIVE r AS (SELECT *) VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 37: `13f1abe257adb914` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027453`

```sql
SELECT printf('%.*g', -1, 0.01); SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); INSERT INTO s (_rowid_, c1, c1) VALUES (FALSE NOT LIKE TRUE, NULL, NOT 
```

---

## Crash 38: `88f868bce5380ff5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027969`

```sql
SELECT printf('%s', -9223372036854775808, ''); SELECT printf('%lli', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); SELECT RAISE(IGNORE) NOT NULL AS km0_,
```

---

## Crash 39: `4cdebaaefa245e49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028627`

```sql
SELECT printf('%.*d', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT OR REPLACE INTO t3 VALUES (abs(NULL IS NOT NULL OR FALSE LIKE TRUE >> NULL ESCAPE RAISE(I
```

---

## Crash 40: `c03f3b445a8fb17e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031934`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(2147483648));
```

---

## Crash 41: `88fb05ec45a6d219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031984`

```sql
SELECT printf('%.*s', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS (SELECT *, NULL FROM r NOT INDEXED NATURAL LEFT JOIN t3 USING (a, a) WHERE CURREN
```

---

## Crash 42: `384f78051d33a44b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033429`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid TEXT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*g', 214748
```

---

## Crash 43: `0dfffe3f9c3d9c1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034860`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `b23738224ea41bfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035785`

```sql
SELECT printf('%.*g', 2147483647, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 VALUES (~typeof(RAISE(IGNORE) OR FALSE IN (CURRENT_DATE, NULL COLLATE NOCASE, FALSE) 
```

---

## Crash 45: `a7e3b37cd356f5f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038833`

```sql
SELECT substr('', 4294967295, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_); SELECT TRUE, (NULL) <> CURRENT_DATE -> CURRENT_TIME NOTNULL FROM s WHERE EXISTS (SELECT t1.
```

---

## Crash 46: `cab6c20bd79f674d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038840`

```sql
SELECT substr('_s5nN6-67', 0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, _rowid_, c3, c2); INSERT INTO q VALUES (RAISE(IGNORE) BETWEEN FALSE AND RAISE(IGNORE) COLL
```

---

## Crash 47: `292fad742f8b0a8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038907`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); SELECT CURRENT_DATE * FALSE - TRUE COLLATE NOCASE LIKE CASE WHEN TRUE COLLATE BINARY THEN NOT TRUE ELS
```

---

## Crash 48: `d31071cbe9cc5227` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039589`

```sql
SELECT substr('-_ H 3C 7 -_o -  - ', -2147483648, 2147483647); SELECT printf('%.*f', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT t1.*, NOT lag(-RAISE(IGNORE)) FILTER (WHE
```

---

## Crash 49: `04a12f88fd1972be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048223`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid TEXT PRIMARY KEY, c1 INT); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 50: `0af9f56416dd13ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048499`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT 'o3 -_ L_-34Tt 6B'); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 51: `cc67cde4fdc6088d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048653`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `fb2f95bf15c8dddb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048660`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT FALSE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 53: `68a4d07c7cd03836` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050649`

```sql
SELECT printf('%.*g', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, c3); INSERT INTO t1 VALUES (FALSE NOT NULL || CURRENT_TIME MATCH ~CURRENT_DATE NOT BETWEEN FALSE AND TR
```

---

## Crash 54: `4d316a3a8358425e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052045`

```sql
SELECT printf('%.*d', 2147483647, -1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 55: `b8e52fdac9539e43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052310`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_TIME, rowid TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN SELECT NOT EXISTS (SELECT CURRENT_TIME ORDER BY RAISE(IGNORE
```

---

## Crash 56: `dde184057a5fada2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052387`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); EXPLAIN QUERY PLAN SELECT NOT EXISTS (VALUES (CURRENT_DATE)) AS w5; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT DISTI
```

---

## Crash 57: `6a66d494bbb747fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052971`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABL
```

---

## Crash 58: `f33a49fdeda8f2c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057970`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT 05631285282170977785291913392220967035778047537290315657319532179856286852234317730292895472482146798555920929781738719535209906847543819659682.28
```

---

## Crash 59: `9df388e678a13c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058818`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (count() FILTER (WHERE CURRENT_TIME) OVER ()); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 60: `9eba644a404de6c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059431`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT GENERATED ALWAYS AS (FALSE > NULL) STORED, rowid TEXT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP ESCAPE TRUE); CREATE V
```

---

## Crash 61: `f036341e05b944d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059728`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); INSERT INTO p DEFAULT VALUES; VALU
```

---

## Crash 62: `633b2b4c3f6623cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061268`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 63: `830d34360f17180e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061426`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); VALUES (NULL) UNION ALL VALUES (count(*) OVER ()); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 64: `32e767dceb17662c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061724`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); VALUES (NULL) UNION ALL VALUES (count(*) OVER (ORDER BY FALSE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GROUP)); CREATE VIRT
```

---

## Crash 65: `2b9d4291dcb9426e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062445`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); SELECT DISTINCT NULL AS a FROM p UNION ALL VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 WITH r (rowi
```

---

## Crash 66: `c1323bbdf7089547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062793`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 AS(c1) UNIQUE); VALUES (NULL) UNION ALL VALUES (CASE WHEN NULL IN (WITH RECURSIVE r AS (VALUES (CURRENT_TIME)), s AS (VALUES (NULL)), p AS (SELECT *) VALUES (FA
```

---

## Crash 67: `279992782da7b7b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063120`

```sql
SELECT printf('%.*f', -2147483648, 0.0); SELECT substr(' -129 S-_-_-N  L 8', -2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO s VALUES 
```

---

## Crash 68: `6099368f137d5620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066141`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CAST(NULL AS INT)); PRAGMA integrity_check; SELECT substr('P--09  4___8', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 69: `08d5ad26061d1395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069393`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (TRUE = CAST(FALSE AS NUMERIC)); PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 70: `d16db57b0fe745ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069661`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (NULL NOTNULL = CAST(FALSE AS NUMERIC)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 71: `c6d4dd9070a2aff0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069738`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (NULL NOTNULL = TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s VALUES (
```

---

## Crash 72: `3aa722a52a530bf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070488`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CASE WHEN FALSE NOT LIKE TRUE THEN CURRENT_TIMESTAMP COLLATE RTRIM ELSE FALSE END = CURRENT_TIME); PRAGMA integrity_check; SE
```

---

## Crash 73: `3b07aea4e84abcdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071673`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME IS NOT CURRENT_DATE IS TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a)
```

---

## Crash 74: `c3f55543cc7d65ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071699`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME IS NOT FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); SELECT p.*, q
```

---

## Crash 75: `b94319d6e1dc78ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077880`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME || FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE 
```

---

## Crash 76: `a5d1f6b2801362ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078131`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIME || CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3
```

---

## Crash 77: `1634b5ba843e2692` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082317`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS i7_hart4 WHERE FALSE UNION ALL VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 78: `5549b3fa0395c2a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082503`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) INTERSECT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 79: `4ec725108b58a57b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082663`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 80: `a0ee37b7cb96e3c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083962`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3); SELECT CURRENT_TIME <> TRUE >> CURRENT_DATE NOT NULL AS a, *, * INTERSECT SELECT q.* FROM r
```

---

## Crash 81: `f614cf0422fb8f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087538`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) NOT NULL); SELECT DISTINCT NULL AS a FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 82: `4f09105e23d5ef3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087926`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); VALUES (4114131229453208988481430590088423370460335630727170164111852464811664689580094885105425306803231493975072646033686270510654395812820
```

---

## Crash 83: `b13b704052e2b335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088269`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (NULL))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q (c3, a) AS (SELECT *, * FROM r 
```

---

## Crash 84: `4b85e74b2f3b6d7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104418`

```sql
SELECT substr('-klQBk6_c3_A', 4294967295, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t2 VALUES (+CAST(~(-NOT CURRENT_DATE <> RAISE(IGNORE)) AS VARCHAR(255)) NOT
```

---

## Crash 85: `ef442bcb4c9646c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116198`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) UNION VALUES (CAST(FALSE AS REAL)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 86: `1b02fe04be3af8f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116356`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) UNION VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 87: `8cbd4e7fb7a2a843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116363`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) UNION VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 88: `f4f8c5961afb4e0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116667`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); WITH p AS (SELECT *) VALUES (FALSE) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 89: `bcdd64197f4c5f30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119173`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT DISTINCT FALSE AS t7l_46_17 FROM p NOT INDEXED WHERE FALSE UNION VALUES (FALSE) INTERSECT SELECT TRUE AS g ORDER BY FALSE, TRUE ASC NU
```

---

## Crash 90: `8fa0b193e1fe4529` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123500`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t3 VALUES (NOT EXISTS (SELECT ALL FALSE NOT NULL IS NULL + CURRENT_TIME, *, TRUE FROM (SELEC
```

---

## Crash 91: `d6cab77b46a66054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128378`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT TRUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 92: `1fdd7dfd39bc145c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128676`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT INTO p SELECT DISTINCT * FROM p NOT INDEXED WHERE FALSE; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t3.*,
```

---

## Crash 93: `86e58da3361d0d80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130302`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (substr(CURRENT_DATE, FALSE, TRUE) = CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 94: `3aad8b84131d64a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130545`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (substr(CURRENT_DATE, FALSE, TRUE) COLLATE RTRIM = CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 95: `d0666b9a120aed79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130769`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (substr(CURRENT_DATE, FALSE IS NOT NULL, TRUE) COLLATE RTRIM = CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 96: `5c19d401fe0a2b25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130944`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIME AS BOOLEAN)); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 97: `cf86fbbbbc373385` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131528`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (NULL NOTNULL = CAST(FALSE AS REAL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT
```

---

## Crash 98: `929be06c4dde35d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131815`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (TRUE = CAST(FALSE AS FLOAT)); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 99: `17e39e92ad44d6e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132245`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (~FALSE = CAST(FALSE AS NUMERIC)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowi
```

---

## Crash 100: `73b06d28f2a63c0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132368`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 101: `1e6b184f743e5eea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133410`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + 411413122945320898848143059008842337046033563072717016411185246481166468958009488510542530680323149397507
```

---

## Crash 102: `dfe0304766c07d4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133462`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); EXPL
```

---

## Crash 103: `967240db2e7a99a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133708`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + 0.0); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 104: `1dbf32ad645bc6ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144171`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b AS(b) NOT NULL); INSERT OR REPLACE INTO p V
```

---

## Crash 105: `0fdb6a6393fcb930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144553`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT *, * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---
