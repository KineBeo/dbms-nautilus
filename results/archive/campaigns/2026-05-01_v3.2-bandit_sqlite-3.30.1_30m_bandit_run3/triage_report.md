# Crash Triage Report

**Total crashes:** 188  
**Unique crash sites:** 188  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 187 | 187 | 99% |
| Signal | 1 | 1 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `ac97d22375691d11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000103`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q WITH RECURSIVE s AS MATERIALIZED (SELECT *, q.* FROM q NOT INDEXED LEFT JOIN r WHERE CURRENT_TIMESTAMP ISNULL GROUP BY FALSE || 
```

---

## Crash 2: `e4bd63bda6812b11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000312`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 VALUES (NULL, -FALSE NOT BETWEEN NULL - RAISE(IGNORE) AND CURRENT_DATE * TRUE + TRUE COLLATE RTRIM, TRUE COLLATE RTRIM ->> CURRE
```

---

## Crash 3: `0463af497a15b48a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000346`

```sql
SELECT round(1e-308, -2147483649); SELECT round(0.01, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT OR ABORT INTO r VALUES (TRUE AND total_changes(), (CURR
```

---

## Crash 4: `ac57b2ab327372c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000891`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT round(0.01, 2147483648); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (FALSE REGEXP min(FALSE COLLATE NOCASE) FILTER (WHERE CASE WHEN FALSE COLLATE BIN
```

---

## Crash 5: `a4d20c16d50478cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001248`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3, b, a); INSERT OR ROLLBACK INTO q VALUES (RAISE(IGNORE) NOTNULL >> FALSE IS NULL COLLATE BINARY ISNULL IS NULL); EXPLAIN QUERY PLAN
```

---

## Crash 6: `b59abe5212cf1d8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001675`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, c2, c3, c3, c2, b); SELECT CURRENT_TIMESTAMP AS u, rowid, t3.*, NULL -> ~CURRENT_TIMESTAMP <> FALSE ISNULL | FALSE IN (SELECT p.*) = CU
```

---

## Crash 7: `2d9c07aef470f6c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002093`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES ((FALSE OR FALSE) MATCH CURREN
```

---

## Crash 8: `127014fb69aac7b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002418`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT OR IGNORE INTO p VALUES (-0 | RAISE(IGNORE) LIKE TRUE <> CURRENT_TIME ESCAPE NOT RAISE(IGNORE) << CURRENT_
```

---

## Crash 9: `46b6d0706c0ae48d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid REAL PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*e', -1, 1e308); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 10: `c335835c5b383947` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003496`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 11: `24d206f0365d21b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003526`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 12: `4a5d4757577fe454` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004807`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r VALUES (~json_extract(CASE WHEN FALSE % NULL THEN CURRENT_TIMESTAMP 
```

---

## Crash 13: `ee6d717f4184810d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004942`

```sql
SELECT printf('%.*g', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 VALUES (CURRENT_DATE) RETURNING q.*; SELECT json((TRUE) COLLATE RTRIM / TRUE
```

---

## Crash 14: `0a7374f73b77a16b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006086`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CU
```

---

## Crash 15: `f0dcf9bd428275ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006174`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 16: `634fa95f67db69b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006207`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CU
```

---

## Crash 17: `d414912b3314ddcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007412`

```sql
SELECT printf('%.*e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT DISTINCT r.* FROM ((SELECT *, *) AS yxosoy8_9_pst__m78y) LEFT JOIN (VALUES (RAISE(IGNORE))) AS a USING (c1, 
```

---

## Crash 18: `985f93cb8e180532` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008546`

```sql
SELECT printf('%.*e', 0); SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t3 VALUES (CASE WHEN RAISE(IGNORE) THEN RAISE(IGNORE) END ==
```

---

## Crash 19: `d1d2ae14d3fc89bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009206`

```sql
SELECT printf('%f', 9223372036854775807, '7_H_6XRXu-- p'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zero
```

---

## Crash 20: `533f08e608cc47ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009249`

```sql
SELECT printf('%.*d', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(-1));
```

---

## Crash 21: `c475dc03f615258f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009304`

```sql
SELECT substr('', 0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(-1));
```

---

## Crash 22: `2817a8e7a08a18fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013667`

```sql
SELECT substr('', 2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 23: `0de6abf3233cfc31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014113`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO s DEFAUL
```

---

## Crash 24: `3c1553adc3acf842` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014253`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DE
```

---

## Crash 25: `fd9b03ae1b56410c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014266`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAUL
```

---

## Crash 26: `54b43665dd3cd39b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015253`

```sql
SELECT substr('sR_-f', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); INSERT OR FAIL INTO q VALUES (NULL BETWEEN CURRENT_DATE NOTNULL BETWEEN RAISE(IGNORE) ->> NULL
```

---

## Crash 27: `bb8eb62f7db446e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015751`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CR
```

---

## Crash 28: `11575e3318776f2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015758`

```sql
SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 29: `a7bad9ea70609bcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015764`

```sql
SELECT round(1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 30: `02d8cfc2dab1354d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015770`

```sql
SELECT printf('%x', 2147483647, '-tX'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 31: `f2cc09aababfd693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015780`

```sql
SELECT printf('%.*g', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 32: `7755258653d324bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015789`

```sql
SELECT round(0.01, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 33: `ef80aee6e4b01595` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015817`

```sql
SELECT substr('', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 34: `a04326c0b396f29d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015831`

```sql
SELECT round(-1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 35: `ee493cb557f1e2a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015890`

```sql
SELECT substr('B-_3a5', 0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 36: `b8aa2113a67c7a83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015896`

```sql
SELECT round(1e-308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA int
```

---

## Crash 37: `e298d7c55ff23bcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015906`

```sql
SELECT round(1e-308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, 
```

---

## Crash 38: `c9607b0b9a0aebf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016050`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 39: `1c80510d8940c66b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016403`

```sql
SELECT printf('%.*f', -2147483649, -1e308); SELECT hex(zeroblob(1));
```

---

## Crash 40: `1e3fb66b87748436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016450`

```sql
SELECT printf('%.*f', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 41: `5c3f31cc38f5186b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024378`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 42: `25f798c0c5df65f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024726`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); 
```

---

## Crash 43: `a878c5a7e884dacb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024916`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); 
```

---

## Crash 44: `84a2a8e973428730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024927`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); 
```

---

## Crash 45: `32f53057aa729f56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024943`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); 
```

---

## Crash 46: `31741158de91dc28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025115`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME <> CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS
```

---

## Crash 47: `94ec856b86662b04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025710`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (FALSE); SELECT ALL * FROM p AS d0_u_4_i_2ne831pem_8v_gqjs__n_zv_f83rcx75
```

---

## Crash 48: `efa65b79a6858a5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025722`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p AS d0_u_4_i_2ne831pem_8v_gqjs__n_zv_f83rcx75
```

---

## Crash 49: `e32785b751c935fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025732`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (FALSE); SELECT ALL * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 50: `470016893dcbc04d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025738`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (FALSE); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED;
```

---

## Crash 51: `472cb20b718bc583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025751`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE I
```

---

## Crash 52: `53d9f3216854f95c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026575`

```sql
SELECT substr('63N_17', 9223372036854775807, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT hex(zeroblob(214748
```

---

## Crash 53: `8767a718a9659b03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027699`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_TIMESTAMP GLOB FALSE ASC NULLS FIRST; SELECT print
```

---

## Crash 54: `b76cfa0d6170150b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028638`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p AS a LEFT JOIN q ORDER BY NULL DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 55: `2d24ec1b31007715` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032665`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('
```

---

## Crash 56: `a5bc509ff78019ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036700`

```sql
SELECT substr(' -N4', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); REPLACE INTO p VALUES (CASE CASE WHEN ~RAISE(IGNORE) AND json_valid(TRUE == ~NULL COLLATE RTRIM) FILTER (WHERE N
```

---

## Crash 57: `9c82ed7ca0836a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038822`

```sql
SELECT printf('%lli', -2147483649, 'nB__ _-91'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 58: `b18a7d037f184ea7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042686`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid REAL PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE V
```

---

## Crash 59: `936db8b91e80488a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043435`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE) UNION VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 60: `94706c344b86ddf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044700`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH R
```

---

## Crash 61: `c2c1c279782fd9a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044860`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(0)); 
```

---

## Crash 62: `8a1679d08d6f05b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIME < CURRENT_TIME WIN
```

---

## Crash 63: `b1ffa3f6635c8634` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046170`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); EXPLAIN QUERY PLAN SELECT CURRENT_DATE FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW 
```

---

## Crash 64: `4bf70860d1f806f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048081`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1); REPLACE INTO 
```

---

## Crash 65: `3f5d212e99cbc6b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051998`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 66: `cd73973ba575501e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054509`

```sql
SELECT printf('%s', 2147483647, '_p-_   _ _ s  4Ar'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (NULL AND CURRENT_TIMESTAMP IS DISTINCT FROM CURRENT_TIMES
```

---

## Crash 67: `865aa36a7ef478ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054836`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (CURRENT_DATE || NULL & CURRENT_DATE IS NULL COLLATE RTRIM, zeroblob(CURRENT_DATE NOTNULL < NULL)
```

---

## Crash 68: `8c8293bcfbd35e61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054848`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q VALUES (NULL - ((VALUES (CURRENT_TIME, TRUE)) IS NOT DISTI
```

---

## Crash 69: `f1087622293778a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054925`

```sql
SELECT printf('%.*d', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN WITH RECURSIVE p (b) AS NOT MATERIALIZED (SELECT q.*, CASE CURRENT_DATE WHEN FALSE
```

---

## Crash 70: `987f42430ad33e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054949`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, b); SELECT t3.* FROM q WHERE EXISTS (VALUES (+NOT EXISTS (SELECT * FROM s NOT INDEXED WHERE NULL LI
```

---

## Crash 71: `b5dd789a860a69ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055650`

```sql
SELECT printf('%.*g', 4294967295, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (TRUE COLLATE BINARY, +CURRENT_TIMESTAMP COLLATE BINARY); ANALYZE q; CREATE TAB
```

---

## Crash 72: `008e03c0cce02116` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059274`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO p SELECT ALL CURRENT_TIMESTAMP FROM q NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 73: `0efdc8be59563e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059355`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 74: `b5b860294efadb4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059882`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB CHECK (FALSE), _rowid_ NUMERIC CHECK (NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 75: `aa17be053e36128c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060078`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB CHECK (FALSE), c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 76: `b26dfe0f9e6b6540` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060780`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q (b, c2) VALUES (substr(CURRENT_DATE, RAISE(IGNORE) | CURRENT_DATE ->> CURRENT_TIME < CURRENT_TIME
```

---

## Crash 77: `46441c3b41377879` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064419`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); EXPLAIN QUERY PLAN SELECT * FROM (SELECT DISTINCT count(DISTINCT TRUE) AS ng_8c5__6xr__0___y_0q, * FROM q 
```

---

## Crash 78: `960b84c2137667bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065109`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY rowid WINDOW w1 AS (); CREATE V
```

---

## Crash 79: `2d5d78840ae52aa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068217`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE, rowid INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL 
```

---

## Crash 80: `5c6d4cd673e329a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069250`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p NOT INDEXED UNION VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 
```

---

## Crash 81: `bf74cae56b79f607` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071142`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) EXCEPT VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 82: `81e9fadb2b34755a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071706`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) UNION ALL VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 83: `0a29cd93e63673d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072082`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 84: `1990ed109157d56a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072753`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT 0669193598414865971261285108840540469892514683873278558.7648862354630839006293514492222375019844231204563994663748003777E+093155590129234433673745
```

---

## Crash 85: `0b5b52c107e5d89b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073158`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 86: `d8161992639ac3e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073253`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO
```

---

## Crash 87: `85d48d5f9c3f9f31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073502`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 88: `f0d0563bcfda5c2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073712`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT -0494301248061736597904233720722752989271306707826554865090592324171318.041577009177); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEF
```

---

## Crash 89: `50347c282fef4729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073839`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 90: `41cb8a22daf65019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091285`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p LEFT JOIN (SELECT DISTINCT * FROM q NOT INDEXED) AS y_ ORDER BY FALSE ASC; CREA
```

---

## Crash 91: `1f831eb606912635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092184`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (SELECT ALL * FROM q NOT INDEXED) AS y_ ORDER BY FALSE ASC; CREATE VI
```

---

## Crash 92: `7a33084b11c6154f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092385`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (SELECT ALL TRUE FROM q NOT INDEXED) AS y_ ORDER BY FALSE ASC; CREATE
```

---

## Crash 93: `74aded19a9974a32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092683`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (VALUES (CURRENT_TIMESTAMP)) AS y_ ORDER BY FALSE ASC; CREATE VIRTUAL
```

---

## Crash 94: `9d723caeacf4e2f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093293`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT 570429.1292294097379292229941127948076153965539374747831585167634452215571945360773127310798495853714180713426108781052432278805781759765680654287
```

---

## Crash 95: `48534421f9810dfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093453`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT 570429.1292294097379292229941127948076153965539374747831585167634452215571945360773127310798495853714180713426108781052432278805781759765680654287
```

---

## Crash 96: `b5c3dc27327d1e2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093467`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p ORDER BY NULL DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 97: `52b0c26420f75b4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093554`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY min(CURRENT_TIME) FILTER (WHERE FALSE) OVER () ASC NULLS F
```

---

## Crash 98: `2a3f0e3d06983e7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094653`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM ASC NULLS FIRST; CREATE VI
```

---

## Crash 99: `41f068b4fec67e63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094802`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY FALSE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 100: `8a7b07f4337e2054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094823`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT CURRENT_TIME ORDER BY TRUE DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT 
```

---

## Crash 101: `f00c1e29eb396dd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095526`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p LEFT JOIN q NOT INDEXED JOIN p AS h_7f412__4_w ORDER BY CURRENT_TIMESTAMP ASC N
```

---

## Crash 102: `1a8226afdfed2d9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095738`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP)) AS z3 ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CRE
```

---

## Crash 103: `fc9810a02f5fd677` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096351`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER PRIMARY KEY); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_TIMESTAMP GLOB NULL ASC NULLS FIRST; C
```

---

## Crash 104: `82cda809f89c763e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096851`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_TIMESTAMP GLOB CURRENT_TIME <= CURRENT_TIMESTAMP C
```

---

## Crash 105: `4deb41db14f89efd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097405`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT CURRENT_DATE AS ye_q8w FROM q NOT INDEXED ORDER BY CURRENT_TIME DESC NULLS FIRST; CREATE
```

---

## Crash 106: `40b399cd64f7e562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098129`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL DEFAULT -0); SELECT ALL * FROM q NOT INDEXED; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 107: `592656ffa140cd42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098299`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL DEFAULT FALSE); SELECT ALL * FROM q NOT INDEXED; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 108: `6e353693ebaf547a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098931`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME <> (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN SELECT ALL 
```

---

## Crash 109: `e251d62bed76ded3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100765`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (FALSE); VALUES (FALSE / FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 110: `c4a2dee187769de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT N
```

---

## Crash 111: `d54b1350cfa34cc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMA
```

---

## Crash 112: `b52fff50db671014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102571`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); 
```

---

## Crash 113: `f4a1d8c9efd8ccb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102692`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK 
```

---

## Crash 114: `b131c3c425cd95a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102721`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMA
```

---

## Crash 115: `0dc8247c891f5a71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102777`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK 
```

---

## Crash 116: `2509c1a966fa9fd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103490`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 117: `70274da43aff5a28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109314`

```sql
SELECT substr('_c3_C C_', 0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT INTO t2 (c1) VALUES (FALSE, +FALSE / CURRENT_DATE) ON CONFLICT(c2) DO UPDATE SET a = +++CURRENT_TI
```

---

## Crash 118: `84a63e698364b064` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122255`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT 292); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO p VALUES (
```

---

## Crash 119: `204d6bcd361e6824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126737`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM q NOT INDEXED ORDER BY TRUE DESC NULLS FIRST LIMIT NOT CURRENT_DATE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 120: `7c99953bfe5bf1cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128918`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC LIMIT CAST(TRUE AS TEXT); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 121: `9cdd9a05f6a30bd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133753`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY CURRENT_TIME COLLATE BINARY DESC; SEL
```

---

## Crash 122: `5d6f45e1e67c03c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133774`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT FALSE AS c_lqyz41bb FROM r WHERE CURRENT_TIMESTAMP GROUP BY FALSE WINDOW w1 AS (ORDER BY RAISE(IGNORE) DESC NULLS LAS
```

---

## Crash 123: `8c601d962c54855e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133805`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p NOT INDEXED WHERE NOT EXISTS (VALUES (CURRENT_TIME) EXCEPT SELECT * FROM q WHERE CURRENT_TIMESTAMP GROUP BY 
```

---

## Crash 124: `127d6e7a45e6c07a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135573`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); VALUES (CURRENT_DATE NOT LIKE CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 125: `761e589dae8d9203` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135611`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC UNIQUE, c3 FLOAT UNIQUE, b TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE NOT LIKE CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE I
```

---

## Crash 126: `07f325b4132af809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136079`

```sql
SELECT printf('%.*s', -9223372036854775808, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO q VALUES (NOT -FALSE IS NOT NULL >> last_insert_rowid() FILTER (WHERE
```

---

## Crash 127: `fe3403749f9ad658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137017`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); WITH s AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_TIMESTAMP
```

---

## Crash 128: `4d43c2e3c743c425` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138547`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE IN (-RAISE(IGNORE)) WINDOW w1 AS () ORDER BY CURRENT_TIME COLLATE BIN
```

---

## Crash 129: `75db901875131e0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138560`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE EXISTS (WITH RECURSIVE q AS (VALUES (FALSE)) SELECT ALL * FROM q) GROUP BY CURRENT_TIME WINDOW w1 AS (
```

---

## Crash 130: `ae115ec292e22692` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138566`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM (p LEFT JOIN q NOT INDEXED JOIN r NOT INDEXED) WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () O
```

---

## Crash 131: `c97589023d620275` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138577`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CASE WHEN RAISE(IGNORE) THEN (CURRENT_DATE) ELSE CURRENT_TIMESTAMP END << c
```

---

## Crash 132: `a948832b802c17e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138588`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS (ORDER BY RAISE(IGNORE) ROWS BETWEEN CURRENT ROW 
```

---

## Crash 133: `57ceb4b07ee5f782` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138605`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b, c3); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY CURRENT_TIME COLLATE BINARY DESC;
```

---

## Crash 134: `c62a5f852c9c1d68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138620`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (CURRENT_TIME IS NOT TRUE), c2 VARCHAR(255)); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TI
```

---

## Crash 135: `45d09fb9b493547c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138626`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p WHERE NOT EXISTS (SELECT * FROM q WHERE CURRENT_TIME GROUP BY RAISE(IGNORE) HAVING EXISTS (SELECT *) WINDOW 
```

---

## Crash 136: `e27927c8eb21bf64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138632`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM p , (VALUES (CURRENT_TIMESTAMP)) AS z3 ON NULL WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () O
```

---

## Crash 137: `cda065ab2776e01a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138643`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT RAISE(IGNORE) NOT LIKE FALSE BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE NOT BETWEEN CURRENT_TIME AND CURRENT_DATE AS 
```

---

## Crash 138: `57ab1c4402e77b03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138722`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY, rowid BOOLEAN UNIQUE); SELECT * INTERSECT SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY CURRENT_TIME COLLATE 
```

---

## Crash 139: `b172696243b6adcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138732`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT * INTERSECT SELECT * FROM ((SELECT * FROM t1 NOT INDEXED WHERE RAISE(IGNORE) IS NULL ORDER BY +CAST(TRUE AS FLOAT) + CURRENT_TIME >> CUR
```

---

## Crash 140: `99343d6f9448a0be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144697`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM (SELECT ALL * FROM (SELECT ALL * FROM p) AS z3 NATURAL LEFT JOIN (p LEFT JOIN q NOT INDEXED J
```

---

## Crash 141: `9605048be9a22310` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144767`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM (SELECT ALL * FROM (SELECT ALL * FROM p) AS z3 NATURAL LEFT JOIN (p LEFT JOIN q NOT INDEXED J
```

---

## Crash 142: `d5ef4edacc565edd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144878`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM (SELECT ALL * FROM q) AS z3 NATURAL LEFT JOIN q; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 143: `eb71efcdcd1f6a8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144885`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM (SELECT ALL * FROM (VALUES (CURRENT_TIME)) AS z3 NATURAL LEFT JOIN (p LEFT JOIN q NOT INDEXED
```

---

## Crash 144: `da09af4b301c77d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144892`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC NOT NULL); SELECT ALL * FROM (SELECT ALL * FROM (SELECT ALL * FROM p) AS z3 NATURAL LEFT JOIN p) AS z3 NATURAL LEFT JOIN q
```

---

## Crash 145: `3d673809bb5bc48c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147075`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); REPLACE INTO p VALUES (TRUE ||
```

---

## Crash 146: `72253842a45b6c5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147124`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); REPLACE INTO p VALUES (TRUE ||
```

---

## Crash 147: `002dfd57b0aabed2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147878`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (CASE TRUE NOT BETWEEN CURRENT_DATE AND total_changes() WHEN CURRENT_DATE THEN TRUE END), c2 VARC
```

---

## Crash 148: `3f53ed992b7d9b34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148088`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (CASE TRUE NOT BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN TRUE END), c2 VA
```

---

## Crash 149: `f073c61c71c40664` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148419`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (~CASE total_changes() WHEN CURRENT_DATE THEN TRUE END), c2 VARCHAR(255)); INSERT INTO p DEFAULT 
```

---

## Crash 150: `74253399b85e1800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148499`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (~TRUE), c2 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 151: `989041e0b4140eab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148505`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (~CASE CURRENT_TIME WHEN CURRENT_DATE THEN TRUE END), c2 VARCHAR(255)); INSERT INTO p DEFAULT VAL
```

---

## Crash 152: `183ccaab8a9d0037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148542`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (~CASE TRUE NOT BETWEEN CURRENT_DATE AND total_changes() WHEN CURRENT_DATE THEN TRUE END), c2 VAR
```

---

## Crash 153: `f1b19aed88c4090c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148736`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (CURRENT_TIME IS NOT TRUE), c2 VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; C
```

---

## Crash 154: `b9e55898b2864558` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162113`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 INT NOT NU
```

---

## Crash 155: `01deea27291a1e5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162124`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UN
```

---

## Crash 156: `5cac861ddf036de8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163283`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMA
```

---

## Crash 157: `0ad047d4efe21c54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164633`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME <> CAST(FALSE AS BLOB)); VALUES (TRUE); CREATE VIRTUAL TABL
```

---

## Crash 158: `e276da497041411a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165534`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL NULL FROM (p LEFT JOIN q NOT INDEXED NATURAL LEFT JOI
```

---

## Crash 159: `88708dff9e45b008` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165920`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL NULL FROM q NOT INDEXED NATURAL LEFT JOIN (p LEFT JOI
```

---

## Crash 160: `8dbd1421b7369c8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166206`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT ALL NULL FROM q NOT INDEXED NATURAL LEFT JOIN q NOT INDEX
```

---

## Crash 161: `8ea7887d9c1e3736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167633`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (group_concat(CURRENT_TIME, ' _0a7 -87-wx-__ oF-')); CREA
```

---

## Crash 162: `0f2b27935463ded6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167754`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (random()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 163: `29ef3ae328329b34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168970`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB DEFAULT X'CF94BbcC162B'); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TABL
```

---

## Crash 164: `64fa2bfb6ba47ee5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169517`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM (VALUES (FALSE)) AS y_ ORDER BY FALSE ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 165: `821f2b3638ce9011` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169875`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_TIMESTAMP GLOB CURRENT_TIMESTAMP || CURRENT_TIME <
```

---

## Crash 166: `c93d6aabbffc31c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170213`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT count(*) AS ng_8c5__6xr__0___y_0q FROM q NOT INDEXED ORDER BY RAISE(IGNORE) DESC NULLS L
```

---

## Crash 167: `3a045f0dcab2f059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171437`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT CURRENT_TIMESTAMP AS ye_q8w FROM p LEFT JOIN q NOT INDEXED JOIN p AS h_7f412__4_w ORDER 
```

---

## Crash 168: `076a761d149fb0c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171661`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT min(CURRENT_TIME) AS ng_8c5__6xr__0___y_0q, * FROM q NOT INDEXED ORDER BY CURRENT_TIMEST
```

---

## Crash 169: `b7843a0f80152352` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171950`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT count(*) AS ng_8c5__6xr__0___y_0q, * FROM q NOT INDEXED ORDER BY count(*) FILTER (WHERE 
```

---

## Crash 170: `1a603d801e349e3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172022`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT * FROM p NATURAL LEFT JOIN p ORDER BY FALSE DESC NULLS LAST; SELECT
```

---

## Crash 171: `02caa3d5b11901ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172185`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT * FROM p NATURAL LEFT JOIN p ORDER BY FALSE DESC NULLS LAST; SELECT printf('%.*g', 
```

---

## Crash 172: `bd4e1f4b21d4e45b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172194`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT DISTINCT * FROM p NOT INDEXED ORDER BY FALSE DESC NULLS LAST; SELECT printf('%.*g', 21474836
```

---

## Crash 173: `7c66e7a43beeb0c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173014`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM (SELECT DISTINCT * FROM q NOT INDEXED) AS y_ ORDER BY min(CURRENT_TIME) FILTER (W
```

---

## Crash 174: `06bfbba13fb59b4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173195`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); SELECT DISTINCT * FROM q NOT INDEXED ORDER BY min(CURRENT_TIME) FILTER (WHERE FALSE) OVER () ASC
```

---

## Crash 175: `3005eb4c27ab20c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175250`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (SELECT ALL TRUE FROM q NOT INDEXED) AS y_ ORDER BY CASE WHEN TRUE TH
```

---

## Crash 176: `12872a8eac18f557` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175327`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CASE WHEN TRUE THEN TRUE ELSE CURRENT_DATE END ASC; CREATE
```

---

## Crash 177: `6730c1d739973f9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175339`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (SELECT ALL TRUE FROM q NOT INDEXED) AS y_ ORDER BY TRUE DESC NULLS F
```

---

## Crash 178: `ae1df946ceb1edf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175391`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM (VALUES (FALSE)) AS y_ LEFT JOIN (SELECT ALL TRUE FROM q NOT INDEXED) AS y_ ORDER
```

---

## Crash 179: `53331555fd929713` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175912`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN (SELECT ALL * FROM q NOT INDEXED) AS y_ ORDER BY FALSE DESC, EXISTS (
```

---

## Crash 180: `4ca2c0d598601e2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176214`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT * FROM p LEFT JOIN (SELECT DISTINCT count(*) FILTER (WHERE FALSE) OVER () AS e_axu_1_059
```

---

## Crash 181: `89bdcf96d7d5b17a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176407`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT count(DISTINCT TRUE) AS ng_8c5__6xr__0___y_0q, count(*) AS ng_8c5__6xr__0___y_0q, * FROM
```

---

## Crash 182: `4dfcd16fa5fbd5b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176519`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); SELECT DISTINCT avg(TRUE) AS ng_8c5__6xr__0___y_0q, * FROM q NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 183: `ceda622f50e0a2a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185763`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC CHECK (CURRENT_TIMESTAMP NOT IN (NULL) AND NULL), c2 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; SELEC
```

---

## Crash 184: `d492fb233ce3a312` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198725`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT -0494301248061736597904233720722752989271306707826554865090592324171318.041577009177); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p 
```

---

## Crash 185: `7d83807003eec269` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199320`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE);
```

---

## Crash 186: `efc892912d612736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199352`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY
```

---

## Crash 187: `96dbf78b602122b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199380`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY
```

---

## Crash 188: `8bc28dd6c969fd49` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000067844`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); SELECT ALL p.* FROM q NOT INDEXED INNER JOIN (SELECT DISTINCT s.*, s.* FROM p NATURAL LEFT JOIN (r NOT INDEXED) ORDER BY json_type(TRUE) FILTE
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  yy_reduce
  sqlite3Parser
```

---
