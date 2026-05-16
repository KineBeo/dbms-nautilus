# Crash Triage Report

**Total crashes:** 87  
**Unique crash sites:** 87  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 87 | 87 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `bd39eae3e6e3c698` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000447`

```sql
SELECT printf('%.*f', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, a, a); INSERT INTO q DEFAULT VALUES; SELECT (SELECT RAISE(IGNORE) AS b_s__2k_5 ORDER BY CURRENT_TI
```

---

## Crash 2: `a5e12e47bbd3a56e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000505`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, * FROM (SELECT t1.* FROM s WHERE FALSE IN (~unicode(TRUE COLLATE BINARY) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST RANGE BETW
```

---

## Crash 3: `6ba074b95cd60037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000524`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3, _rowid_, c1); INSERT INTO q VALUES (CURRENT_TIMESTAMP COLLATE BINARY + -CURRENT_TIMESTAMP ->> CURRENT_DATE != RAISE(IGNORE) REGEXP
```

---

## Crash 4: `8f28995bf4d57b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001372`

```sql
SELECT printf('%.*s', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CASE WHEN -TRUE THEN ~FALSE ELSE RAISE(IGNORE) END, NOT CURRENT_DATE <= RAISE(IGNORE)) ORDER BY
```

---

## Crash 5: `cc8da4191dadfbe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001416`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) NOT NULL); INSERT OR ABORT
```

---

## Crash 6: `3b2ec9e1a843b68c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001437`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT printf('%.*s', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1, c3, a, c1); WITH RECURSIVE q (c1, rowid) AS NOT 
```

---

## Crash 7: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001722`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 8: `6d76e78808424591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); VALUES (CURRENT_DATE); SELECT printf('%.*g', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r (c2, c1) VALUES (
```

---

## Crash 9: `34c457f8bd838149` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007468`

```sql
SELECT round(0.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT q.*, q.* FROM q JOIN r a ON CASE RAISE(IGNORE) COLLATE RTRIM NOT LIKE RAISE(IGNORE) COLLATE RTRIM A
```

---

## Crash 10: `2c72f5d9e8c729f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007492`

```sql
SELECT printf('%.*g', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); SELECT t2.* FROM p WHERE EXISTS (VALUES (~NULL * CURRENT_DATE + CURRENT_TIMESTAMP NOT IN (SELECT *, *) NOT N
```

---

## Crash 11: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007547`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 12: `c2581e564355041f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007750`

```sql
SELECT printf('%.*e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (c1) VALUES (avg(-CURRENT_DATE ISNULL < TRUE ->> CASE CURRENT_TIMESTAMP == +RAISE(IGNORE) WHEN r
```

---

## Crash 13: `7f45df87825a06bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008814`

```sql
SELECT printf('%x', -2147483648, '_0Z_v'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE p AS MATERIALIZED (SELECT p.* FROM jsonb_tree('[]') ORDER BY (CURRENT_TIMESTAMP
```

---

## Crash 14: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014592`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 15: `1ee9a147e73d6daa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016791`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (TRUE); SELECT *; SELECT hex(zeroblob(4294967296));
```

---

## Crash 16: `57a451ef3f119ff1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017774`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM t1 JOIN jsonb_each('[{"a":1},{"b":2}]') USING (c2, c2) WHERE NULL ORDER BY NOT NUL
```

---

## Crash 17: `96281820bcf48396` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019338`

```sql
SELECT substr('1  Q 6_', -1, 9223372036854775807); SELECT printf('%.*s', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE r (c2) AS NOT MATERIALIZED (SELECT *
```

---

## Crash 18: `65bc1373217a50e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022093`

```sql
SELECT printf('%.*d', 2147483648, 0.0); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 19: `8668103e814b005b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025023`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) NOT NULL); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (c3, c3, CASE WHEN CURRENT_DATE THEN +C
```

---

## Crash 20: `4bc7d074d9d671c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026124`

```sql
SELECT printf('%.*g', -2147483648, 1e308); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 21: `0b981260a0842824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026602`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); SELECT RAISE(IGNORE) ISNULL, r.*, p.*, CURRENT_DATE, (NOT EXISTS (
```

---

## Crash 22: `039cc4f8487b01bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028313`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP BETWEEN NULL AND CURRENT_DATE > CURRENT_TIME AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_5_8v3
```

---

## Crash 23: `fa33c7bf1d07e0a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028519`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_DATE > CURRENT_TIME AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_5_8v32g_y_b_d__hdr0_s8870n_nfxl6_om__, *
```

---

## Crash 24: `447d96a888c4d0ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028754`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP BETWEEN NULL AND CURRENT_DATE << CURRENT_DATE NOT NULL AS i_ib__7___5595c43_i____6_we_w1_tx__x
```

---

## Crash 25: `29f300f68ec25b4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037208`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 DEFAULT VALUES; VALUES 
```

---

## Crash 26: `23251930810a0b1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039155`

```sql
SELECT round(0.01, -2147483649); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 27: `ec262762c66b027e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040288`

```sql
SELECT substr('6 A _jK-QL _', -2147483649, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM jsonb_each('[1,2,3]') JOIN json_each(CASE WHEN NULL THEN FALSE ELSE TRUE END, '$.
```

---

## Crash 28: `02de8d63036425b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040995`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, b AS(b) UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *, * FROM json_each('[{"a":1},{"b":2
```

---

## Crash 29: `e0e8aab0c2d33406` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043797`

```sql
SELECT round(-1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES ((coalesce(FALSE, CURRENT_DATE) FILTER (WHERE TRUE) >> CASE WHEN NOT CASE CAST(CUR
```

---

## Crash 30: `59ef75d604d53cb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043870`

```sql
SELECT printf('%f', 9223372036854775807, '1TL_'); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 31: `6e1eba480e37f671` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044931`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE I
```

---

## Crash 32: `7ceda4a89455b673` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048022`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR REPLACE INTO p VALUES (CAST(-TRUE AS VARCHAR(255)) * CURRENT_TIME); PRAGMA quick_chec
```

---

## Crash 33: `c3867349e805b8a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051386`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (CURRENT_TIMESTAMP BETWEEN NULL AND NULL)); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 34: `95df56c96d34f907` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053764`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 35: `dd398c98ceb22184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054047`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT -41530280.1706705771648993127732652230E69806); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e3
```

---

## Crash 36: `67ce846e84e0fb23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054300`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 37: `0288bed82c536bf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054900`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT 8441230520357028.97); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); 
```

---

## Crash 38: `132c02136b1fdfd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054970`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); INSERT OR REPLA
```

---

## Crash 39: `672df63c360cea18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056432`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; VALUES (rank() OVER ()); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 40: `a06d6317723737ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056593`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 41: `56a64f37fc43d020` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057200`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 42: `565836c2c9fd9abe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060070`

```sql
SELECT printf('%.*s', 2147483647, 1e-308); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 43: `56eb3ffaed76f8b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067266`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b AS(b) NOT NULL); SELECT * FROM json_tree('[]') WHERE CURRENT_TIME GROUP BY CURRENT_TIME; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 44: `7d81ede28ac0ab1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068631`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CAST(CURRENT_DATE AS REAL) << CURRENT_TIME AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_5_8v32g_y_b_d__hdr0_s8870
```

---

## Crash 45: `e1ba560fbc0d2301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069018`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT p.rowid > CURRENT_TIME << FALSE AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_5_8v32g_y_b_d__hdr0_s8870n_nfxl6_om_
```

---

## Crash 46: `69763b2fac872e00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069408`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT X'fC6Bf00E8cEaFd' AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_5_8v32g_y_b_d__hdr0_s8870n_nfxl6_om__, * FROM p; S
```

---

## Crash 47: `2b6c2fe99751c0d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071685`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP BETWEEN NULL AND CURRENT_DATE > CURRENT_TIME COLLATE NOCASE AS i_ib__7___5595c43_i____6_we_w1_
```

---

## Crash 48: `b2bf3cf062f66a11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071764`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); WITH RECURSIVE q AS (SELECT *) SELECT CURRENT_TIMESTAMP BETWEEN NULL AND CURRENT_DATE > CURRENT_TIMESTAMP AS i_ib__7___5595c43_i____6_we_w1_tx__xg7mo_
```

---

## Crash 49: `85805f839e8fca30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072184`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, b GENERATED ALWAYS AS (c2) NOT NULL UNIQUE); WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 50: `87e3aa6477dc206c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076061`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, c3 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 51: `d55819f1350176f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086172`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (FALSE IN (VALUES (TRUE)) IN (VALUES (TRUE))); EXPLAIN QUERY PLAN VALUES (CURR
```

---

## Crash 52: `64b920ba29e83920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091511`

```sql
SELECT substr('lC-y', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3); EXPLAIN QUERY PLAN VALUES (~NOT CAST(-CURRENT_DATE AS INTEGER) GLOB NULL NOT LIKE CASE (CURRENT_DAT
```

---

## Crash 53: `a927f85f97494679` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091683`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 54: `14cde9f96b3de2be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093255`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 55: `35fb66151e3ef275` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094524`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]') GROUP BY CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 56: `0b3d53dbf41fe9e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094888`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INT); SELECT TRUE FROM p NOT INDEXED , json_each('{}') JOIN json_each(CURRENT_DATE, '$') GROUP BY CURRENT_DATE;
```

---

## Crash 57: `c3508538ebcebeef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095971`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE VIRTU
```

---

## Crash 58: `f1f651d4465f9fe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096450`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIME BETWEEN TRUE AND CURRENT_TIME) ON CONFLICT D
```

---

## Crash 59: `b1ea00a6cf5ae122` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096672`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; SELECT * FROM json_each('{"a":1}') GR
```

---

## Crash 60: `1dea0c0d20bc3d1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096758`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_each('{"a":1}') GROUP BY NULL; SELECT printf('%.*g', 
```

---

## Crash 61: `742da33e94e6ea3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097542`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a REAL
```

---

## Crash 62: `2f0f110bb3dc05c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099722`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q LEFT OUTER JOIN json_tree('[1,2,3]') , json_tree(changes() FILTER (WHERE FALSE) OVER (ORDER BY FALSE DESC 
```

---

## Crash 63: `2f819df4ce95a5da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099769`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q LEFT OUTER JOIN json_tree('[1,2,3]') , json_tree(changes() FILTER (WHERE FALSE) OVER (), '$[#-1]') GROUP B
```

---

## Crash 64: `7ac6f2c336626042` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099776`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q LEFT OUTER JOIN json_tree('[1,2,3]') , json_tree(changes() FILTER (WHERE FALSE) OVER (ORDER BY FALSE DESC 
```

---

## Crash 65: `b9e7e8c223549c9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099899`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, b AS(b) NOT NULL); VALUES (-CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q SELECT DISTINCT * FROM q INDEXED BY _rowid_ UNION
```

---

## Crash 66: `632cdee159e1fec0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE, _rowid_ INT UNIQUE, c2 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 67: `182706230af94f2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102745`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 68: `626ebf7ef10b3f53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115301`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO q VALUES (+'' % CURRENT_TIMESTAMP COLLATE BINARY << CURRENT_TIME == CURRENT_DA
```

---

## Crash 69: `ddb3372b8c0ddf9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115337`

```sql
SELECT substr('__WlCPi28__K-1K-', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (min(NULL COLLATE RTRIM > count() & FALSE >= NULL <> CURRENT_TIMESTAMP | RAISE(IGNO
```

---

## Crash 70: `2cee7dba4f76ed7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118593`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(c1 FLOAT DEFAULT CURRENT_TIME); SELECT NULL FROM p NATURAL JOIN p WHERE p.c3; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 71: `72ff54fc83b9a922` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127268`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ABORT INTO p VALUES (CURRENT_TIME OR CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 72: `ca5d2cb0027b8073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129071`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 73: `178f682c1b79c55d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129330`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a REAL
```

---

## Crash 74: `d05d291700a1e502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131345`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP LIKE NOT EXISTS (VALUES (FALSE))) ON CONFLICT DO NOTHING; VALU
```

---

## Crash 75: `1bcf451f258d4e09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132926`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 AS(c1) UNIQUE); SELECT * FROM json_tree('[{"a":1},{"b":2}]') GROUP BY NULL; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 76: `7b534b6a97940b63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133931`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b AS(b) UNIQUE); SELECT CURRENT_TIMESTAMP, * FROM (SELECT ALL * FROM json_tree('{"a":{"b":1}}') ORDER BY NULL DESC) AS t NATURAL JOIN json_tree('[1,2,3]') GROUP
```

---

## Crash 77: `d7c851a5ffd50396` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135406`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) NOT NULL); I
```

---

## Crash 78: `4b6fd932df7a852c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141474`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (TRUE); SELECT DISTINCT * FROM q ORDER BY NULL ASC LIMIT CURRENT_TIME * CURREN
```

---

## Crash 79: `35a54c38cf959e4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141512`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (TRUE); SELECT DISTINCT * FROM q ORDER BY NULL ASC LIMIT CURRENT_TIME * CURREN
```

---

## Crash 80: `7c89484c6e642838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142711`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL 
```

---

## Crash 81: `9f336bb271f23072` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143645`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (CAST(CURRENT_DATE AS BLOB) IN (VALUES (TRUE))); EXPLAIN QUERY PLAN VALUES (CU
```

---

## Crash 82: `43f6ae80b3514e80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144040`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (NULL IS TRUE IN (SELECT FALSE AS kc_b_t336te50__0wu0__83sr_x4_cyx022__72nd_7f
```

---

## Crash 83: `76562ff8aed7255b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144109`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (TRUE IN (SELECT FALSE AS kc_b_t336te50__0wu0__83sr_x4_cyx022__72nd_7f1_c917s_
```

---

## Crash 84: `6c0fc957fdccbd08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144115`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (TRUE IN (VALUES (CURRENT_DATE))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAM
```

---

## Crash 85: `a8490e38f956ee78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144136`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (TRUE IN (VALUES (NULL))); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREA
```

---

## Crash 86: `7207c863071d6867` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144249`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (CURRENT_TIME IN (SELECT * FROM p)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMEST
```

---

## Crash 87: `984dc070ebe38205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144430`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT OR FAIL INTO q VALUES (CURRENT_TIME IN (SELECT * FROM (VALUES (CURRENT_DATE)) AS f_e)); EXPLAIN QUER
```

---
