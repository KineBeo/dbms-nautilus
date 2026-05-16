# Crash Triage Report

**Total crashes:** 54  
**Unique crash sites:** 54  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 54 | 54 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `6417398cff595ef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000060`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_, c1, c2); INSERT INTO p VALUES (json_object('', (CURRENT_TIMESTAMP) IS NOT TRUE LIKE CURRENT_DATE ISNULL LIKE CAST(CURRENT_TIMESTAM
```

---

## Crash 2: `d73cdbde14afde38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000171`

```sql
SELECT printf('%lld', -9223372036854775808, 'b8-V_0-_ _ s'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES (+c1 % +CURRENT_TIME COLLATE NOCASE REGEXP CURRENT_TI
```

---

## Crash 3: `c5c74aac8385099b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000197`

```sql
SELECT substr('', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r DEFAULT VALUES; SELECT q.*, q.* FROM t1 JOIN q k1 ON -CASE CURRENT_TIME WHEN NULL COLLATE NOCASE THEN CURRE
```

---

## Crash 4: `3ca458330c40a6ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000631`

```sql
SELECT round(0.01, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); EXPLAIN QUERY PLAN SELECT RAISE(IGNORE) NOT NULL FROM json_tree('{}') NATURAL JOIN json_each('{"a":1}') WH
```

---

## Crash 5: `692a1db277aa1bcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000795`

```sql
SELECT printf('%.*f', -9223372036854775808, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES ((SELECT *) NOT BETWEEN NULL COLLATE NOCASE + TRUE ISNULL & CA
```

---

## Crash 6: `91328c00e5b6ee1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004937`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); EXPLAIN QUERY PLAN SELECT RAISE(IGNORE) NOT NULL FROM json_tree('{}') NATURAL JOIN json_each('{
```

---

## Crash 7: `ef684ca98d3a0e86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007414`

```sql
SELECT printf('%x', 0, 'LIv_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CURRENT_DATE >= CASE WHEN CURRENT_DATE COLLATE BINARY THEN ~CURRENT_TIMESTAMP NOTNULL END
```

---

## Crash 8: `bda0cd18754a4d88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011732`

```sql
SELECT printf('%.*g', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT OR ROLLBACK INTO r VALUES (TRUE NOT IN (VALUES (CURRENT_TIME) LIMIT TRUE)); SELECT *; S
```

---

## Crash 9: `b98fdb6f38b07189` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012276`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 10: `001cad74daefff9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012285`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 11: `2f703e0765e01a28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012291`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 12: `94c2374806bc9656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012401`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 13: `b7d6030ad072a484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012432`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 14: `3a0860e1a58be58b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013713`

```sql
SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT -7 & -RAISE(IGNORE) OR NULL <> FALSE * NOT CURRENT_TIME * NULL <> CURRENT_TIMESTAMP IS
```

---

## Crash 15: `dbea7b4353864f53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT CHECK (random())); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 16: `04ff97c679892e8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016609`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT CHECK (NULL <> FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 17: `2e849d07b4fd5cc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025838`

```sql
SELECT substr('', -2147483648); SELECT substr(' T  7 M_5 j  ', -9223372036854775808, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q SELECT * FROM json_tree((CURRE
```

---

## Crash 18: `48fb8babf09d8e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036778`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM json_each('{}') WHERE FALSE GROUP BY NULL); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 19: `b5ebee20f792619f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037786`

```sql
SELECT printf('%.*s', 2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT OR FAIL INTO q VALUES (CAST(CASE CURRENT_TIMESTAMP IS RAISE(IGNORE) ISNULL WHEN FALSE <> (C
```

---

## Crash 20: `232595817b146794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037811`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT OR FAIL INTO q VALUES (CAST(CASE CURRENT_TIMESTAMP IS RAISE(IGNORE) ISNULL WHEN FALSE <> (CURRENT_TIME) TH
```

---

## Crash 21: `b7d4e97096052a59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044865`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN SELECT ALL FALSE AS g__j1k3__3__u5_ff_77v56__2_6_2l5____g6yqyv_1___g_4hbn0_q16xc0u_7z_7g69_h_7z_4n74z__jevgq2348_j3_w_1__214km_
```

---

## Crash 22: `df58075b24486ccb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049456`

```sql
SELECT substr('_- _I_ 4_Ymnvo  6R_', -1, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (TRUE IS NOT DISTINCT FROM RAISE(IGNORE) - CAST(FALSE | CUR
```

---

## Crash 23: `f9af8e94459ce6b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055700`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c3 REAL, c3 GENERATED ALWAYS AS (a = 0) N
```

---

## Crash 24: `42aee7832075dc96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056514`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (hex(hex(hex(CURRENT_DATE)))); PRAGMA quick_check;
```

---

## Crash 25: `8f94362992a9249e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056521`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(CURRENT_DATE)))))))))); PRAGMA qu
```

---

## Crash 26: `e740987f0de6dbfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056775`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (hex(hex(hex(hex(hex(CURRENT_DATE << CURRENT_DATE)))))); PRAGMA quick_
```

---

## Crash 27: `6bae3e487d47bbff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056782`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT OR ROLLBACK INTO q VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(C
```

---

## Crash 28: `4a905b40670ad7ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058223`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_TIME)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c3
```

---

## Crash 29: `3fca7df8cc8877ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058585`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT DISTINCT TRUE FROM json_each(CURRENT_TIME, '$') NATURAL LEFT JOIN json_tree('[1,2,3]'); CREA
```

---

## Crash 30: `c7b83b36397ef413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058695`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 31: `278e1bbf8dbd87a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069669`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT -CASE WHEN RAISE(IGNORE) - NOT (CURRENT_TIME) IN (RAISE(IGNORE), (CURRENT_TIMESTAMP))
```

---

## Crash 32: `ca02b399136dbbfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072947`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT DISTINCT TRUE FROM (json_each('[]') JOIN p NOT INDEXED NATURAL JOIN 
```

---

## Crash 33: `c373d92f9492e470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072965`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 34: `187fd65e02f3c5e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072973`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT DISTINCT TRUE FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 35: `d5d8151dee916a96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072979`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT DISTINCT TRUE FROM json_each('{"a":1}'); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 36: `dd36c54a8c4f89dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072986`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(b INT); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT DISTINCT TRUE FROM (q) NATURAL LEFT JOIN json_tree('[1,2,3]'); CREAT
```

---

## Crash 37: `3636a13eb9289890` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075240`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); SELECT rowid FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CASE FALSE WHEN TRUE THEN CU
```

---

## Crash 38: `9a991d063cfc82f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090620`

```sql
SELECT substr('-D R_F_64E', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, a, c1, c2); REPLACE INTO q VALUES (+CURRENT_TIMESTAMP, NULL); EXPLAIN QUERY PLAN VALUE
```

---

## Crash 39: `7513bd66c5d96a77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097304`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); REPLACE INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 40: `cd6391e4c1af7437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097759`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); REPLACE INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a NUMERI
```

---

## Crash 41: `3fec9fcebe93cc2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100720`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (c1) VALUES (FALSE LIKE CURRENT_TIMESTAMP IS NOT NULL MATCH ifnull(RAISE(IGNORE) COL
```

---

## Crash 42: `a273193d69238696` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103215`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c3 GENERATED ALWAYS AS (a + 0) NOT NULL UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL
```

---

## Crash 43: `715e9dddabc4ac76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105108`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT
```

---

## Crash 44: `76fc4138c4323e96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105673`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE, _rowid_ BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 45: `eda3e9287ea7942f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105738`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE, _rowid_ BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR 
```

---

## Crash 46: `b4cf2ef9da0174fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111866`

```sql
SELECT substr('3-_Gxc-C', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT DISTINCT p.*, CURRENT_DATE AS g20_w5___8y FROM jsonb_each('{"a":1}') NATURAL JOIN json_each('{"a
```

---

## Crash 47: `d03826320d0c0880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112982`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 48: `2d7f9cd544b6e7d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113487`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE NOT NULL DEFAULT -1633526336306347.6E+294); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*e', 21474
```

---

## Crash 49: `1936c676f0774a25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113907`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (FALSE >= FALSE), c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT r
```

---

## Crash 50: `c21e6315c50a5981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115914`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); IN
```

---

## Crash 51: `de6420b93dd01983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117188`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT CHECK (CURRENT_TIMESTAMP BETWEEN FALSE AND FALSE)); INSERT OR ROLLBACK INTO q VALUES (hex(hex(CURRENT_DATE))); PRA
```

---

## Crash 52: `3cb37c399cdb79aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119284`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 GENERATED ALWAYS AS (a) UNIQUE, c2 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT 
```

---

## Crash 53: `30c4072ad8e603c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119531`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, a); SELECT +-CURRENT_DATE = CURRENT_TIMESTAMP REGEXP TRUE COLLATE RTRIM << (CURRENT_TIMESTAMP) LIKE -FALS
```

---

## Crash 54: `db126aeb544e3928` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121679`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_DATE) EXCEPT SELECT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO q DEFAULT VALUES; PRAGMA inte
```

---
