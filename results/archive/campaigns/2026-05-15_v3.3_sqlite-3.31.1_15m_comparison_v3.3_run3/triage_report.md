# Crash Triage Report

**Total crashes:** 86  
**Unique crash sites:** 86  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 86 | 86 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `8ac7c74b4615fa2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000193`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, b, a); INSERT INTO t1 VALUES (json_array_length(NULL IS NOT CURRENT_DATE == CURRENT_TIMESTAMP) IS CURRENT_TIMESTAMP NOTNULL NOT BETWEEN
```

---

## Crash 2: `157282124a8b2480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000199`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT q.*, p.* FROM p WHERE EXISTS (SELECT DISTINCT NULL AND CURRENT_TIME OR NULL IS NOT DISTINCT FROM TRUE
```

---

## Crash 3: `0d70d4113cc44577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000974`

```sql
SELECT substr('NAe-h-t-3Y-m  3 ', 9223372036854775807, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c2); SELECT *, * FROM json_each(CASE WHEN ~CASE WHEN TRUE = ~CURRENT_TIME IS NOT
```

---

## Crash 4: `03b8aee51b555560` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001302`

```sql
SELECT substr(' K', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIME ISNULL, FALSE); SELECT q.* FROM q JOIN p t___29z___z8r_a__sk_744t_
```

---

## Crash 5: `ee7bb88ac3bdab82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005544`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, a, c3); REPLACE
```

---

## Crash 6: `ef06ee78e9803645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005559`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, a, c3); REPLACE INTO p VALUES (RAISE(IGNORE) IN (FALSE)); WITH RECURSIVE p AS MATERIALIZED (SELE
```

---

## Crash 7: `7c4615ae818290c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005576`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME NOT NULL) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 8: `27d7e78233424199` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005594`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, a, c3); REPLACE INTO p VALUE
```

---

## Crash 9: `43bbf3802e26f673` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005600`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 10: `71cce4fb7b86937a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007190`

```sql
SELECT printf('%.*f', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q SELECT q.* INTERSECT VALUES (c1 IS NOT NULL); ANALYZE t2; CREATE TABLE IF NOT EXISTS p(a INT, b 
```

---

## Crash 11: `27ec9e33838725bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007286`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT NULL >> RAISE(IGNORE), NOT FALSE OR NULL -> NOT CURRENT_TIME AS mrgwzh FROM r JOIN t2 l_b5__93
```

---

## Crash 12: `1d005d00ac29c555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007341`

```sql
SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (+NULL IS NULL & TRUE LIKE TRUE GLOB ~FALSE != CURRENT_DATE), a INT UNIQUE, b TEXT CHECK (+lead(total_changes() IS FA
```

---

## Crash 13: `d7c1f55209a0e19c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007380`

```sql
SELECT printf('%.*e', -1, -1.0); SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELEC
```

---

## Crash 14: `261b0745adea69ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007676`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL DEFAULT 0.0, a NUMERIC NOT NULL DEFAULT 5.64991746072055038582056223116036741240501288E1); WITH RECURSIVE t2 AS (SELECT RAISE(IGNORE) FROM jsonb_tree('{"a":1}') LE
```

---

## Crash 15: `32e0612159866684` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007981`

```sql
SELECT printf('%.*f', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); SELECT p.* FROM t1 NATURAL JOIN t3 WHERE NULL IN (CURRENT_DATE) LIKE TRUE NOTNULL == CASE FALSE << RAISE(IGNORE) 
```

---

## Crash 16: `4ba629cf37f0c095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009950`

```sql
SELECT printf('%.*f', 2147483647, -1e308); SELECT substr('N- ', 9223372036854775807); CREATE TABLE IF NOT EXISTS p(b NUMERIC CHECK ((FALSE <= NULL)), b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(_ro
```

---

## Crash 17: `7dcddc344718a776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010598`

```sql
SELECT printf('%.*s', 4294967296, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t2 AS (SELECT q.*, * FROM json_tree(RAISE(IGNORE), '$.c[#-1]') INNER JOIN json_tree('[{
```

---

## Crash 18: `d599f1681789e56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018640`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_TIMESTAMP NOT IN (FALSE))); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL
```

---

## Crash 19: `a33b827df90d5ad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019505`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_TIME)); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 20: `61348e1a0734f994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022022`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 21: `0c68c6abc2079baf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024614`

```sql
SELECT substr('3-C _b-', -9223372036854775808, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; ANALYZE q;
```

---

## Crash 22: `e8b024036ea3cf37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027735`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT CURRENT_TIME); SELECT * FROM (SELECT *, * FROM q WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*g', 2147483647
```

---

## Crash 23: `8ee2ef13a3bd3ec7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027755`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INT PRIMARY KEY); SELECT * FROM (SELECT *, * FROM q WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 24: `d09c7cef628e98ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027762`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 25: `ea57a5ddb045b991` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028365`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); SELECT * FROM (SELECT NULL AND CURRENT_DATE << CURRENT_TIME, * FROM q WHERE TRUE) AS sub1; CREATE VIRTUAL
```

---

## Crash 26: `44c6b24b686960ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034777`

```sql
SELECT printf('%.*g', -2147483649); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 27: `ab051df3673b78bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035589`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 28: `b160023b43be6f66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039656`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 29: `6752258a0e9ec88e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040302`

```sql
SELECT round(-1e308, -9223372036854775808); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 30: `acc16e3bf36407f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043719`

```sql
SELECT printf('%.*s', -2147483649, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE -> TRUE LIKE NULL & ~CURRENT_DATE IN (SELECT * LIMI
```

---

## Crash 31: `a65e0d6189abe0e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043735`

```sql
SELECT substr(' q-_2f- G___cp', 4294967295, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CURRENT_TIME IS FALSE == CURRENT_TIMESTAMP ->> CURRENT_DATE NO
```

---

## Crash 32: `5238dec3085973ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048419`

```sql
SELECT printf('%.*d', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); SELECT RAISE(IGNORE) OR CURRENT_DATE AS j161____81l_2r FROM p JOIN t3 w ON ~count(DISTINCT FALSE
```

---

## Crash 33: `919cb70e3e178350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049010`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); WITH RECURSIVE t2 AS (SELECT RAISE(IGNORE) FROM jsonb_tree('{"a":1}') LEFT JOIN p INDEXED BY c3 INTERSECT SELECT DISTINCT NULL COLLATE NOCASE
```

---

## Crash 34: `5dabaf7aaf0dcb89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052516`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE
```

---

## Crash 35: `6e8cf8c99e016174` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052660`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE
```

---

## Crash 36: `9aef915dc4cc1b2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052668`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 AS(c1) UNIQUE
```

---

## Crash 37: `2c28a930ceb5ecf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052893`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT 7.360E172); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 214748364
```

---

## Crash 38: `b8ab622f598bc104` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053104`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 39: `ce9aee8a0374edc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053111`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT CURRENT_TIME); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 214748
```

---

## Crash 40: `c1d93b048e78bce8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056553`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); WITH RECURSIVE r (a) AS (VALUES (NULL)) SELECT * FROM r; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 41: `daff1acbfa2e7426` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063515`

```sql
SELECT printf('%.*e', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO q VALUES ((TRUE COLLATE BINARY) & RAISE(IGNORE) ISNULL - RAISE(IGNORE) MATCH TRUE
```

---

## Crash 42: `5e4a35672d9e787b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064795`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1,
```

---

## Crash 43: `1fd6a09fffacb537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069943`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) UNIQUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 44: `ffb777dc2ce75deb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072767`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 AS(c1) UNIQUE); VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CASE CURRENT_TIMESTAMP CO
```

---

## Crash 45: `5a99a16fe15c11be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074578`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT *; SE
```

---

## Crash 46: `2a277e0d7afa9ffc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074689`

```sql
SELECT printf('%.*f', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 47: `be2f7151e489f91c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080801`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%s', -9223372036854775808, '48QQ-_-MYL__e--_---'); SELECT round(1e-308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBAC
```

---

## Crash 48: `d49af4bc611e5398` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085774`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); SELECT * FROM (SELECT CURRENT_DATE << CURRENT_TIMESTAMP BETWEEN NULL AND FALSE, * FROM q WHERE TRUE) AS s
```

---

## Crash 49: `5e62b050dcb12792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085973`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); SELECT * FROM (SELECT FALSE, * FROM q WHERE TRUE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 50: `ca3f0ddb652c409e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086309`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255)); SELECT * FROM (SELECT NULL AND CURRENT_TIMESTAMP COLLATE BINARY, * FROM q WHERE TRUE) AS sub1; CREATE VIR
```

---

## Crash 51: `ac2517e484c1948c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087703`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT -4147993041417556326258372398439597338529530462402462571007910914993911815556463411435347272692200337889986.79
```

---

## Crash 52: `d5ab6183fc2f54f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087788`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT -4147993041417556326258372398439597338529530462402462571007910914993911815556463411435347272692200337889986.79
```

---

## Crash 53: `1048d64764fc8018` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087838`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308)
```

---

## Crash 54: `67d2d5c2303d06a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089945`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) UNIQUE); SELECT *, * FROM (SELECT CURRENT_TIME NOT IN (CURRENT_TIMESTAMP), * FROM q WHERE FALSE) AS sub1;
```

---

## Crash 55: `5ce7c5c95e010856` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100308`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 56: `ccf205ff6e4250c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100556`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT X''); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 57: `88d39f8483f568ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100855`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY, c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483
```

---

## Crash 58: `8ddd81597952eb4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT FALSE AS x44___2 FROM json_each('[]') GROUP BY CURRENT_TIM
```

---

## Crash 59: `ccfe6a1eecac3a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107924`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (random())); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 60: `360a725eb74f9dfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109720`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_TIMESTAMP NOT IN (CAST(FALSE AS FLOAT)))); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME);
```

---

## Crash 61: `768530a80aca93d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109918`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 62: `127afd9c1df86c8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109929`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_TIMESTAMP NOT IN (CURRENT_TIME))); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); SELECT 
```

---

## Crash 63: `dfda1eb1494e47da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (TRUE)); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VI
```

---

## Crash 64: `bdffd8d1a8565681` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111115`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') NATURAL JOIN json
```

---

## Crash 65: `087ded3f0856bc35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111346`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (NULL BETWEEN CURRENT_DATE AND FALSE NOT IN (TRUE))); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN V
```

---

## Crash 66: `28445cc60350c83b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113461`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_each('{}') JOIN (q
```

---

## Crash 67: `ade631e65562c5e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113782`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q; CREATE VIRTUAL TABLE
```

---

## Crash 68: `628f1523031220f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118436`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('[1,2,3]') GROUP BY CURRENT
```

---

## Crash 69: `039c9234d86190ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122010`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM json_tree('{}') WHERE TRUE GROUP BY NULL,
```

---

## Crash 70: `6de3734c398e8058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483
```

---

## Crash 71: `a71aa6c07a90ae5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125742`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT CAST(FALSE AS REAL) >> CURRENT_DATE AS a; SELECT printf('%.*f', 21474
```

---

## Crash 72: `91867cbc160d1b9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127527`

```sql
SELECT printf('%.*e', -9223372036854775808, 1e-308); SELECT substr('-  - 6-E_-_', 1, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO q VALUES (NOT FALSE I
```

---

## Crash 73: `481e4f68ce851fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130072`

```sql
SELECT substr('4uWIH _- 5e-ix _', 2147483648, 9223372036854775807); SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); INSERT INTO p DEFAULT VALUES; E
```

---

## Crash 74: `4ba98f60bbd0002e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134726`

```sql
SELECT printf('%lld', -2147483648, '4'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO t2 VALUES (NOT -trim(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP) OVER (
```

---

## Crash 75: `10f9c520ac473404` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135554`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE r AS (SELECT *), p AS (VALUES (NULL)) SELECT *; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 76: `395a0af3f1b5b337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136032`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, b AS(b) UNIQUE); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE IS NOT NULL COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT 
```

---

## Crash 77: `1fc9204f212be987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141666`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT CAST(FALSE AS VARCHAR(255)) >> CURRENT_DATE AS a; CREATE VIRTUAL TABL
```

---

## Crash 78: `3b00a92e07322d02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142227`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT NULL NOT IN (VALUES (count())) FROM p GROUP BY CURRENT_TIMESTAMP; SEL
```

---

## Crash 79: `712523aaeaad8779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142427`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT NULL NOT IN (VALUES (CURRENT_DATE)) FROM p GROUP BY CURRENT_TIMESTAMP
```

---

## Crash 80: `7b8317269ccf53ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT NULL NOT IN (VALUES (TRUE)) FROM p GROUP BY CURRENT_TIMESTAMP; SELECT
```

---

## Crash 81: `aa1fe801844d378f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (SELECT DISTINCT * FROM (
```

---

## Crash 82: `70d71b2b92d581be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147074`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{}') WHERE TR
```

---

## Crash 83: `9d62786aa146f91b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT CHECK (CURRENT_DATE NOT IN (TRUE, CURRENT_TIMESTAMP * CURRENT_TIMESTAMP * CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
```

---

## Crash 84: `87cd696abff62763` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149800`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED; CREATE
```

---

## Crash 85: `91d085fcd4580483` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150004`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT q.* FROM (json_each('{}') JOIN
```

---

## Crash 86: `c5d45522d8fc9f92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150854`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME FROM q; SELECT pr
```

---
