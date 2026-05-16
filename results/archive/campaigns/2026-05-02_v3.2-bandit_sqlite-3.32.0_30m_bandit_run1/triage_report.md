# Crash Triage Report

**Total crashes:** 241  
**Unique crash sites:** 241  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 241 | 241 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `f02845f4a5958526` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000126`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT INTO t2 VALUES (RAISE(IGNORE) IS NOT NULL LIKE CURRENT_TIMESTAMP IS NOT NULL == CURRENT_TIME ESCAPE min(TRUE) FILTER (WHERE CURRENT
```

---

## Crash 2: `df2f20f324bdc884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000193`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2, c2, c1); INSERT OR FAIL INTO r VALUES (+TRUE < RAISE(IGNORE) IS NULL GLOB CAST(CURRENT_DATE AS DATE) OR TRUE, CURRENT_TIME BETWEEN
```

---

## Crash 3: `8a755840385094bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000246`

```sql
SELECT round(0.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO p VALUES (FALSE COLLATE BINARY | (SELECT * UNION VALUES (CURRENT_TIMESTAMP))); EXPLAIN QUERY 
```

---

## Crash 4: `ca0d2f56e293f999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000407`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT printf('%.*g', -9223372036854775808, 1e-308);
```

---

## Crash 5: `bae0f28df512673d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000450`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH t3 AS MATERIALIZED (SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE WINDOW w1 AS ()) INSERT INTO 
```

---

## Crash 6: `03acfa6c2b1d592d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000584`

```sql
SELECT substr('b 6 v8  iHDs', 2147483648, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, a, c1, c1, c3, c3); SELECT * FROM p NOT INDEXED WHERE random() GROUP BY FAL
```

---

## Crash 7: `b51443be7c91039c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000850`

```sql
SELECT printf('%.*d', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q AS (VALUES (NULL)) SELECT p.* FROM q; CREATE TABLE IF NOT EXISTS p(rowid INT, c1 INTEGER UNIQU
```

---

## Crash 8: `267109d6980aad55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000906`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO q VALUES (-CURRENT_TIMESTAMP NOTNULL NOT NULL, (SELECT DISTINCT * FROM t1 N
```

---

## Crash 9: `2b5c414406c3bf78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001437`

```sql
SELECT printf('%.*e', 9223372036854775807, -1.0); SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c2); INSERT OR FAIL INTO t1 VALUES (NULL | TRU
```

---

## Crash 10: `b51335de45f13835` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001465`

```sql
SELECT printf('%.*g', 1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); SELECT q.* FROM q WHERE EXISTS (SELECT +-FALSE IS NULL GLOB EXISTS (SELECT FALSE) LIKE CURRENT_TIMESTAMP O
```

---

## Crash 11: `25299d591792b6fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001544`

```sql
SELECT substr('_i_V-3-', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO t2 VALUES ((NULL), NOT EXISTS (WITH RECURSIVE p AS NOT MATERIALIZED (SELECT ALL *,
```

---

## Crash 12: `35a909055f5f4996` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001713`

```sql
SELECT printf('%.*s', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_, a); SELECT * FROM t1 JOIN p a ON TRUE COLLATE BINARY | FALSE COLLATE NOCASE LIKE CURRENT
```

---

## Crash 13: `f4b62775b931a2e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001835`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE, b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 14: `8b3f0aed86f26fb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001882`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 15: `c3bee1d8fc231b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001893`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN VALUES (TRUE);
```

---

## Crash 16: `a216d45bd9948276` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001956`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); E
```

---

## Crash 17: `4e6fae64de607c48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001979`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE));
```

---

## Crash 18: `84180fcc49bd8a0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001992`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 19: `9f3dccf3fd1fb940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002499`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN, c1 INTEGER GENERATED ALWAYS AS (+NULL) VIRTUAL); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT OR FAIL INTO q VALUES (NULL); SELECT CURRENT_TIME FROM p JOIN p lf
```

---

## Crash 20: `ea0af2f3e3b547a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002711`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT OR FAIL INTO q VALUES (NULL); SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_
```

---

## Crash 21: `23df0b254ae876f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004111`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (+RAISE(IGNORE) IS NULL IS NOT NULL BETWEEN FALSE < CURRENT_DATE BET
```

---

## Crash 22: `0ff08f525fa3e0e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004169`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SE
```

---

## Crash 23: `2edc57784620a605` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004186`

```sql
SELECT round(1e308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT NULL FROM p AS t_e_9_215u_888__9sz_vamu_u2vw_ UNION SELECT s.* FROM p NOT INDEXED LEFT OUTER JOIN p INDEXED BY c
```

---

## Crash 24: `5635fd1502007332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005031`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO t3 VALUES (zeroblob(+(SELECT NULL) || FALSE NOT NULL - CURRENT_DATE) FILTER (W
```

---

## Crash 25: `cb540c645a5b4311` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, +CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CU
```

---

## Crash 26: `7d4d195256853059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005213`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CUR
```

---

## Crash 27: `944dbd9c55006dda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005774`

```sql
SELECT printf('%.*f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q (a) VALUES (lower(-RAISE(IGNORE) == FALSE >= TRUE NOTNULL || json_object('', TRUE IS NOT NULL
```

---

## Crash 28: `1f3d6175305cc593` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006691`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 29: `3a6e5e69fc3ddc43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008009`

```sql
SELECT printf('%.*s', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-1));
```

---

## Crash 30: `0948f19d363b534c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008870`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN, c1 INTEGER GENERATED ALWAYS AS (TRUE) VIRTUAL); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 31: `b42a68fffb2de701` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008902`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 32: `d29b62d1a3ee6296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT I
```

---

## Crash 33: `e3e31feee9ac7ac8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010835`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 34: `eb60681436c7919f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; CR
```

---

## Crash 35: `79a6f0f5029834d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016519`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT * FROM q NATU
```

---

## Crash 36: `79e782e20569e6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016612`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 37: `d27c9f04e513d317` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020761`

```sql
SELECT printf('%llu', -1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT TRUE AS q_0__ob, CAST(CURRENT_DATE GLOB CURRENT_DATE AS BLOB) -> FALSE IS DISTINCT FROM TRUE, *, * FROM 
```

---

## Crash 38: `797ca67d8efdaace` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022262`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 39: `b62f1e5df9a24c2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022428`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 40: `0b9640fcde1b9a5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022795`

```sql
SELECT printf('%.*f', -2147483649, 1e308); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 41: `5c4110b445f5d7b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023808`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VI
```

---

## Crash 42: `8395ca753b4cf7fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024310`

```sql
SELECT substr('', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); EXPLAIN QUERY PLAN 
```

---

## Crash 43: `9bdcfc2f3ddee1d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026770`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION ALL VALUES (FALSE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 44: `60b27747acd46ce3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029692`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 45: `ac59491379178328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029938`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 46: `5dd08894f348a406` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031427`

```sql
SELECT substr('  _--', 0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 47: `a98bb2710d2b1f84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033015`

```sql
SELECT round(0.01, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c1, b); INSERT INTO q VALUES (RAISE(ABORT, '28-')); SELECT FALSE COLLATE BINARY AS q1860nlp5 FROM (SELECT 
```

---

## Crash 48: `2dd1f41151b13505` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033339`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN, rowid VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8
```

---

## Crash 49: `89e27c9697e02a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033490`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN, c1 INTEGER GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT OR FAIL INTO q VALUES (NULL); SELECT * FROM p JOIN p lf_____q_63gv
```

---

## Crash 50: `db0429b333daa6bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034077`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1_c__
```

---

## Crash 51: `8f078b2ed621d550` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034256`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 52: `14dc260c371690db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034315`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 53: `b158299c713529d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034968`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_
```

---

## Crash 54: `9a4e0a1810a77043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035203`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_
```

---

## Crash 55: `bebd66b5a205db11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035313`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 56: `2dfeca25252504a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035716`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_
```

---

## Crash 57: `b231e6d10c109af9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036706`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PR
```

---

## Crash 58: `0f22d700cea0a4a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038110`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES (NOT CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 59: `4a7ad536da52954c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038231`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE NOT IN (TRUE)); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 60: `944ba3d1645d83ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039874`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE, b NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 61: `dd8e6e5485ca1e0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041811`

```sql
SELECT printf('%.*s', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME); ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL, rowid 
```

---

## Crash 62: `4bb6960d8ef40057` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042160`

```sql
SELECT printf('%.*f', 4294967295); SELECT round(-0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (RAISE(IGNORE) / TRUE ISNULL); SELECT *, NULL NOTNULL 
```

---

## Crash 63: `6c2627f2d9186099` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042440`

```sql
SELECT substr('_c-h', 4294967296, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, b ->> RAISE(IGNORE) NOT IN (SELECT CURRENT_TIMESTAMP LIMIT TRUE) NOTNULL REGEXP FALSE COLLA
```

---

## Crash 64: `c16e533337ec216c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043345`

```sql
SELECT printf('%s', -2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); EXPLAIN QUERY PLAN SELECT *; SELECT hex(ze
```

---

## Crash 65: `6aaf10265c4d1366` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044097`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT INTO p VALUES (EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_TIME) IS NOT NULL >= CURRENT_TIMESTAMP); PRAGMA integrity_check;
```

---

## Crash 66: `214fbcebeeb59d99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048253`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE << TRUE); PRAGMA integrity_check; SELECT printf('%.*
```

---

## Crash 67: `eadffa276b662356` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055745`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-922337203685477580
```

---

## Crash 68: `606ac42b4a06de3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055757`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-922337203685477580
```

---

## Crash 69: `91bf9482266b478a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056655`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 70: `b48324ec755dd155` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057946`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 71: `19f4c5ff9db2da6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058078`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 72: `925892f60818f7f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058681`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT count(*) OVER (), * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kf
```

---

## Crash 73: `38d09ff8817b0a62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060166`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 74: `de84055a5e1cebde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060221`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (TRUE) ON CONFLIC
```

---

## Crash 75: `d9df5dce08a065ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061233`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CAST(CURRENT_TIME AS INT)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 76: `9a8702862801767b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061825`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIM
```

---

## Crash 77: `cb025d3344dd1f4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062440`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIMESTAMP COLLATE NOCASE); CREATE VIRTUAL TABLE 
```

---

## Crash 78: `08066c6f47338cf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063243`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES 
```

---

## Crash 79: `79dfad597e0b7322` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063440`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 80: `deebdc11a9f25bca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066614`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (~NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 81: `19ea87bf33a3b05b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067863`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 82: `be88bc89e2f70e03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069369`

```sql
SELECT printf('%.*d', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, b, a); WITH RECURSIVE q AS NOT MATERIALIZED (SELECT * EXCEPT SELECT t2.* FROM q NOT INDEXED WHER
```

---

## Crash 83: `8c0c501e6497a9d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073112`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 84: `5c68abad8dea2e71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073190`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 85: `9ccca7e1b0c899ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073310`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 86: `6fd1f3cb0be3fcfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077783`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY TRUE ASC NULLS FIRST ROWS BETWEEN UN
```

---

## Crash 87: `827e3690d8c44a8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079307`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR ABORT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF
```

---

## Crash 88: `aa50684e4a05c04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079504`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR ABORT INTO p VALUES (TRUE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 89: `13244ae6fd935b34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079691`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT 
```

---

## Crash 90: `9a1da7d81ed8c7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080722`

```sql
SELECT round(-1e308, 2147483648); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 91: `c2a9e2f0ba5eadc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081797`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 92: `ee1bc8a817ccb53d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086191`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p w0s___ ON EXISTS (SELECT * FROM p NOT INDEXED GROUP BY FALSE, CU
```

---

## Crash 93: `2a029d26190176d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_TIME); SELECT * FROM p NATURAL JOIN p
```

---

## Crash 94: `285facfcbc055328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089763`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL DEFAULT 1432430849688082814984965784758796197505122760302943924619089099622425771426027043.999969374870712
```

---

## Crash 95: `c381493988e0e3fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090150`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE NULL - CURRENT_DATE; CREATE VIRTUAL TABLE 
```

---

## Crash 96: `227d6238a1e978a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090454`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) DEFAULT 0.0); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABL
```

---

## Crash 97: `458e61ff32960bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090674`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (NULL) VIRTUAL, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p 
```

---

## Crash 98: `16b06596e50a8954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091059`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT * FROM q NATURAL
```

---

## Crash 99: `4cfeb5cffbd5679a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091906`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT * FROM q NATU
```

---

## Crash 100: `d1710eaec33ae685` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092825`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT roun
```

---

## Crash 101: `7458c7cba3295fc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093243`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, c1 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR R
```

---

## Crash 102: `76a19c7a4dedca21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096264`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); VALUES (NULL) UNION ALL SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 103: `16f24f9edab257f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096656`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 104: `361e2b35c7c63891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105087`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON -FALSE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 105: `d902c6577edcb21d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105316`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_DATE IN (VALUES (TRUE)); SELECT round(-0.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 106: `6d0e804f4a7b51a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105483`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON EXISTS (SELECT * FROM p NOT INDEXED GROUP BY -FALSE COLLATE BINARY, CURRENT_DATE IN (VALUES (TRUE)) LIMIT CURRENT_TIME);
```

---

## Crash 107: `58c6940157f7e08d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105697`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_DATE || CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT INTO q VALUES (~(
```

---

## Crash 108: `50ef7d6fdfc0e99b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107509`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p (c1) AS NOT MATERIALIZED (W
```

---

## Crash 109: `a99b27e92637f4aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107612`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CURRENT_TIMESTAMP AND NULL IS NOT CURRENT_TIMESTAMP COLLATE RTRIM; SELECT printf('%.*f', -2147483649, 1e30
```

---

## Crash 110: `b3f854469a2afdfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107893`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE >= FALSE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT +NOT EXISTS (VALUES (NUL
```

---

## Crash 111: `bf57219228daa015` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT OR REPLACE
```

---

## Crash 112: `a386dfcf91370a3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108443`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIMESTAMP LIKE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO p SELECT ALL p.* 
```

---

## Crash 113: `14559aeae2e2f3ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108822`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL GLOB FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT q.* FROM t3 AS rm2__y_z189wom97_w8g_ryu
```

---

## Crash 114: `720a7ca6800638fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108947`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIMESTAMP GLOB FALSE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 115: `5c21c51a722775a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109330`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL NOT BETWEEN NULL IS TRUE COLLATE RTRIM AND CURRENT_TIME IN (FALSE); SELECT substr('', -2147483649); CREATE VIRTUAL 
```

---

## Crash 116: `3a6385d5a170c236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109534`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL IS CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); SELECT -RAISE(IGNORE) LIKE NULL LIKE 
```

---

## Crash 117: `64a4f1bb1537a57b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109837`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL IS TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 118: `03038dd7603c792b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110063`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON TRUE COLLATE RTRIM IN (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO s VALUES (ab
```

---

## Crash 119: `5cc274df5032221f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110510`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT 5901, a REAL NOT NULL DEFAULT 1432430849688082814984965784758796197505122760302943924619089099622425771426027043.9999693748707126080690); SELECT * FROM p
```

---

## Crash 120: `3b4ea490d82eb9a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110723`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN FALSE BETWEEN FALSE BETWEEN FALSE BETWEEN NULL AND CURRENT_DATE AND CURRENT_DATE AND CURRENT_DATE AND CURR
```

---

## Crash 121: `6c9b789182881089` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113436`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES 
```

---

## Crash 122: `6f0dca5e90baaba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114915`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT * FROM q NATURAL JOIN p WHER
```

---

## Crash 123: `ce683a8b10c1f2ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115566`

```sql
SELECT printf('%.*f', 2147483647, -0.0); SELECT substr('pW EC_', 1, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (c3) VALUES (FALSE REGEXP NULL >= FALSE ISNULL); ANALYZE 
```

---

## Crash 124: `9a04420f898bdf61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115946`

```sql
SELECT printf('%.*d', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, _rowid_); WITH q AS NOT MATERIALIZED (SELECT p.* FROM q WHERE NULL GROUP BY RAISE(IGNORE) WINDOW
```

---

## Crash 125: `6f58b971dbaa0fb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117937`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); INSERT INTO p (c1, c1, a, ro
```

---

## Crash 126: `5be3c0f04af53613` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118090`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); INSERT OR FAIL INTO p VALUES (-CURRENT_TIME >> TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, a); SELECT q.* 
```

---

## Crash 127: `506193a75b62972a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118368`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); INSERT OR FAIL INTO p VALUES (CAST(TRUE AS BLOB)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT INTO p VAL
```

---

## Crash 128: `1c8e20c009fc2006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118654`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); INSERT OR FAIL INTO p VALUES (-3828536418566837379070996364018692779491023089638735946633075576.480e+99792789914131); PRAGMA quick_check; CREATE VIRTUAL 
```

---

## Crash 129: `960d163ca4e1c865` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121505`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIMESTAMP LIKE '--K-- -'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VA
```

---

## Crash 130: `d46fdad9ae7f719a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121795`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_TIMESTAMP LIKE X'CaA0D9ddD45c'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 (a, row
```

---

## Crash 131: `162084847055ca3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122348`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CAST(FALSE AS REAL) AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INT
```

---

## Crash 132: `738ed63412cd7838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122483`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CAST(CURRENT_TIMESTAMP AS TEXT) AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 133: `7fb7d591a22f2e44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122687`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CAST(CURRENT_TIMESTAMP AS INTEGER) AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 134: `2a5fc4918273e817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122914`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON FALSE BETWEEN CAST(CURRENT_TIMESTAMP AS REAL) AND CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1,
```

---

## Crash 135: `8c1ef5ce6bcbdf77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123151`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DA
```

---

## Crash 136: `830e3cef1daa63b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123396`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON NULL IS NOT FALSE IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE q (c1) AS NOT MATERIA
```

---

## Crash 137: `2cfd5b27f9756986` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125151`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON -CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 138: `46ca79763d6eb643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125342`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); SELECT * FROM p JOIN p w0s___ ON CURRENT_DATE || CAST(CURRENT_TIMESTAMP AS FLOAT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT I
```

---

## Crash 139: `97617eaa4f1d1925` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134871`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); VALUES (NULL) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 140: `db479417f743d2ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135009`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); VALUES (NULL) INTERSECT VALUES (FALSE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 141: `e4d47d9e61e6a265` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135173`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); VALUES (NULL) UNION ALL SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT TRUE << TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH p
```

---

## Crash 142: `81d818f87873e5bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138041`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABL
```

---

## Crash 143: `b469d0b768629b94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138125`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT prin
```

---

## Crash 144: `c0300424efec22b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138135`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABL
```

---

## Crash 145: `3b98a55afbdcb7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABL
```

---

## Crash 146: `14d87f999477be35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138457`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -16550.67, _rowid_ BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT 
```

---

## Crash 147: `b3bd3e8ddf96f0bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139138`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE); SELECT * FROM q NATU
```

---

## Crash 148: `37d9a4c5164cf859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139385`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, c3 BLOB GENERATED ALWAYS AS (NULL) STORED, rowid TEXT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY, c1 NUMERIC NOT NULL); INSERT OR ROLLBA
```

---

## Crash 149: `4b506d91860c9f4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139466`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY, c1 NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRE
```

---

## Crash 150: `4c997d849773a95b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140116`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, a TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p W
```

---

## Crash 151: `6b42364a1ee23e63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140859`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, c1 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHER
```

---

## Crash 152: `05c9d5d24632fe56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141012`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, c1 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE TRUE; CREATE VIRTU
```

---

## Crash 153: `7991913d8caaefc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141102`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP - FALSE; CREATE VIRTUAL 
```

---

## Crash 154: `d5af4659c0278ca0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142346`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL DEFAULT X''); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DATE OR NULL
```

---

## Crash 155: `52ac7ce8fee46544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142493`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL DEFAULT CURRENT_TIME); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_DAT
```

---

## Crash 156: `208abb67dae45860` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142857`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; SELECT min(TRUE) OVER (PARTITION BY NOT EXISTS (VALUES (NULL)), CURRENT_TIME), * FROM q
```

---

## Crash 157: `2ff84dc5a4970edb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143754`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; SELECT q.* FROM q NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIR
```

---

## Crash 158: `2ca01ad4f4b15448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, CURRENT_TIME); SELECT * FROM q NATURAL JOIN p
```

---

## Crash 159: `3e5483db2dd879e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144007`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE, X'920dB3ACFc0c99'); SELECT * FROM p NATURAL J
```

---

## Crash 160: `00cbd339dc22f839` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145756`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p w0s___ ON EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE HAVI
```

---

## Crash 161: `3aaf725df646474d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150068`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 162: `4fee071c1f60d679` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151142`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY TRUE ASC NULLS FIRST ROWS BETWEEN UN
```

---

## Crash 163: `96ba7fdd72d96f5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151350`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (count(*) OVER ()); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 164: `ea560886d65219df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151616`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT ALL * FROM (VALUES (CURRENT_DATE)) AS x_n5 NATURAL JOIN p NOT INDEX
```

---

## Crash 165: `ba4722f5129018c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL DEFAULT FALSE, rowid NUMERIC NOT NULL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); EXPLAIN QUERY 
```

---

## Crash 166: `096aec9b6db1c421` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158657`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, rowid INTEGER PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); VALUES (TRUE); CREATE VIRTUAL TAB
```

---

## Crash 167: `509e6b824bd28b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158832`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, rowid INTEGER PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); SELECT * FROM q ORDER BY NULL ASC
```

---

## Crash 168: `b8f7ce8723ddb89d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167709`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION ALL VALUES (avg(NULL) FILTER (WHERE FALSE)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 169: `ca5dbe64671a5c04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168798`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION ALL VALUES (TRUE IS NOT TRUE IS NOT TRUE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 170: `a92618159ffb329d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168977`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION ALL VALUES (CURRENT_DATE IS NOT TRUE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 171: `a79342a5a33b2a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169628`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); VALUES (NULL) UNION ALL SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP ORDER BY NULL ASC; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 172: `64cb41c9e1ed31bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174381`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (TRUE * FALSE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 173: `527c923f86c4918c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175018`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT min(TRUE) OVER (PARTITION BY CURRENT_DATE, FALSE) FROM p JOIN p b ON CURRENT_DATE; SEL
```

---

## Crash 174: `893ba533c2b4eb4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 175: `cd7ef01d403d3cb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176263`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c2 GENERATED ALWAYS AS (a * a) UNIQUE, b INT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABL
```

---

## Crash 176: `2b4398c5e2df9899` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177880`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CAST(CURRENT_TIME AS BLOB)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 177: `880beb291915b8f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178108`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) EXCEPT VALUES (CAST(CURRENT_TIME AS REAL)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 178: `874a19a6e1178884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178819`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED EXCEPT VALUES (NULL, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 179: `8a52a5f3ac64f24f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179871`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; SELECT * FROM p AS o7su0201c8_z___w6p_dnl5___9_h_44_3n3evc_le___h7q_u__tf3__77ga__6azl5xp_t_09___c_g_fie_b73
```

---

## Crash 180: `abab68c4bcb43764` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182150`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT count(*) OVER (), count(*) OVER (PARTITION BY NULL, FALSE), * FROM p JOIN 
```

---

## Crash 181: `4364183aabda305a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182335`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT *, count(*) OVER (), * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g
```

---

## Crash 182: `745ff25a932ac04f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182481`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT count(*) OVER (), count(*) OVER (), * FROM p JOIN p lf_____q_63gvqc_tw_o__
```

---

## Crash 183: `f060ec9baf006f84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182583`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT count(*) OVER (), FALSE, * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe395
```

---

## Crash 184: `febc7c8c444fc2c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183009`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 185: `3ec0ac3c9147ba1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183299`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 186: `aaf939d96520efef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184529`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 187: `8abf67031c22206e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185337`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT OR FAIL INTO q VALUES (NULL); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483
```

---

## Crash 188: `c592c66ea38b57ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185900`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c2 REAL UN
```

---

## Crash 189: `b1763d142f826f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186524`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); VALUES (NULL) UNION ALL SELECT min(TRUE) OVER () FROM p NOT INDEXED GROUP BY TRUE ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 190: `70d10dadbd3c7c72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187329`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fk
```

---

## Crash 191: `e6479e3bbbceb745` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 192: `695e0cb1fecf6afe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187934`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 193: `e520649d9ea06d9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196452`

```sql
SELECT substr('_ h_6_t3', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2); SELECT CURRENT_TIMESTAMP AS n39c__km__p21d_b0w_6__r_27_b_f_5i_4_d___2_yx4_
```

---

## Crash 194: `455f98c58e66d1bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196626`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIMESTAMP << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE
```

---

## Crash 195: `e95332b20eb25e5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197235`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT min(TRUE) OVER (PARTITION BY TRUE NOT IN (CURRENT_TIME), 
```

---

## Crash 196: `4278cae4b76db0f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197307`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT FALSE ORDER BY CURRENT_DATE ASC NULLS LAST LIMIT CURRENT_
```

---

## Crash 197: `9de75f8972b411f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197680`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT avg(NULL) OVER () ORDER BY CURRENT_DATE ASC NULLS LAST LI
```

---

## Crash 198: `8867607c743e53d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198736`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT min(NULL) OVER () ORDER BY CURRENT_DATE ASC NULLS LAST LI
```

---

## Crash 199: `a61bfc01b76ce411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198971`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT min(TRUE) OVER () ORDER BY CURRENT_DATE DESC LIMIT CURREN
```

---

## Crash 200: `c941e2fc7b1140dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199088`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT count(*) OVER () ORDER BY CURRENT_TIMESTAMP ASC NULLS FIR
```

---

## Crash 201: `a18b2299b5591500` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200093`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT CURRENT_TIME ORDER BY CURRENT_DATE ASC NULLS LAST LIMIT (
```

---

## Crash 202: `28a5fb625a981e34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200238`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT CURRENT_TIME ORDER BY CURRENT_DATE ASC NULLS LAST LIMIT F
```

---

## Crash 203: `09370574ff3a1d99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201657`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME) UNION SELECT ALL * FROM p LEFT JOIN p USING (c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 204: `535768094c2783e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204005`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); SELECT count(*) OVER (PARTITION BY NULL, FALSE), * FROM (SELECT * FROM p WHERE NULL ISNULL) AS sub1; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 205: `9863cb9bac7315f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204297`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); SELECT * FROM (SELECT _rowid_, * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 206: `a94b9c2669e02a96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204407`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); SELECT * FROM (SELECT NULL, * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 207: `4f4b930ab7b1f90b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204543`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 208: `636c7d370b98ee31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204630`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) ); SELECT * FROM (SELECT * FROM p WHERE trim(CURRENT_TIMESTAMP)) AS sub1; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 209: `014130a14b9d4166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207764`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT INTO p VALUES (EXISTS (SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY CURRENT_TIME)); PRAGMA integrity_check; SELECT prin
```

---

## Crash 210: `4715efc5411deed5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209264`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); VALUES (CURRENT_TIMESTAMP || NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT hex(zeroblob(1))
```

---

## Crash 211: `f006da1cf294d652` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217089`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME) UNION VALUES (FALSE COLLATE NOCASE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*f', 
```

---

## Crash 212: `9a8d401888df94c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217609`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME) UNION SELECT ALL count(*) OVER (PARTITION BY FALSE COLLATE NOCASE ORDER BY CURRENT_DATE 
```

---

## Crash 213: `dced5fb7fc8aa6ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217811`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIME) UNION SELECT ALL count(*) OVER (PARTITION BY NULL ORDER BY CURRENT_DATE ASC NULLS FIRST 
```

---

## Crash 214: `9d236e88e48fa1b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220525`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT * FROM p NOT INDEXED ORDER BY NULL ASC NULLS LAST)); PRAG
```

---

## Crash 215: `bc99dfc6842ca9c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221112`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT avg(FALSE) OVER () ORDER BY CURRENT_DATE ASC NULLS LAST L
```

---

## Crash 216: `c57d6a82fd023151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221579`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT min(TRUE) OVER (ORDER BY FALSE ASC ROWS BETWEEN CURRENT R
```

---

## Crash 217: `bc7dfbc42b518a9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221711`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES ((SELECT min(TRUE) OVER (ORDER BY FALSE ASC RANGE BETWEEN UNBOUNDE
```

---

## Crash 218: `1d6085ea64ba7fe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221747`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE << CURRENT_DATE); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 219: `a4adb2d3fa67f75f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227311`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM p NOT INDEXED ORDER BY TRUE ASC LIMIT -60615; CREA
```

---

## Crash 220: `bba47d4deff969d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228172`

```sql
SELECT printf('%.*f', 2147483648); SELECT printf('%x', 1, 'Q6 1_--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); EXPLAIN QUERY PLAN SELECT p.* FROM p JOIN p , q AS f3_____zlo_7_8y9
```

---

## Crash 221: `3e5d338ad9f6700a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230108`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 222: `19d4b9f3bfefa622` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230697`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 223: `13c00c02bedc10c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232474`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); VALUES (NULL) INTERSECT SELECT NULL AS tn__q0j_74_j3q_7b7pz18nh ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROL
```

---

## Crash 224: `6bfc1bfdc38a3728` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233435`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 225: `cf16fc6a36c7a8bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233492`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 226: `1bdad4c20df55329` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233498`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 227: `5b3a6a13bd498e5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233715`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 228: `726455d7a49ff2d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234042`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 229: `953958485e42c4b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234109`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(b BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM p JOIN p lf_____q_63gvqc_tw_o__612__woe3952d8g_kfm4e___q__3_re1_0_fkoux_2_y1
```

---

## Crash 230: `8ab7f7d1d4d55881` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237938`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; SELECT * FROM p NATURAL LEFT JOIN p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT TRUE; CREATE VIRTUAL TABLE 
```

---

## Crash 231: `4e591c56710aec18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239333`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, _rowid_ GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) UNION ALL VALUES (CAST(CURRENT_TIME AS INT)); SELECT printf('%.*g', 214
```

---

## Crash 232: `bf7c175e0476536a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242666`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), b GENERATED ALWAYS AS (a + -0) NOT NULL UNIQUE, a VARCHAR(255) NOT NULL DEFAULT 143243084968808281498496578475879619750512276030294392461908909962242
```

---

## Crash 233: `3ca8ac079b7a35bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242686`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), b GENERATED ALWAYS AS (a + -0) NOT NULL UNIQUE, a VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 234: `82ad73d41fb2d49b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242788`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), b GENERATED ALWAYS AS (a + -0) NOT NULL UNIQUE, a VARCHAR(255) NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL
```

---

## Crash 235: `c50e93574a600530` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242860`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), b GENERATED ALWAYS AS (a) NOT NULL UNIQUE, a VARCHAR(255) NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CR
```

---

## Crash 236: `274b50232f80c480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259394`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, -CURRENT_DATE || CURRENT_TIMESTAMP * CURRENT_DAT
```

---

## Crash 237: `ee6c7cd49453a57e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259670`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); SELECT DISTINCT * FROM p NOT INDEXED LEF
```

---

## Crash 238: `4ad00b17dd8710bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); SELECT DISTINCT * FROM q NOT INDEXED WHE
```

---

## Crash 239: `1c7396f0e719912f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259729`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); SELECT DISTINCT * FROM p NOT INDEXED LEF
```

---

## Crash 240: `af3734d744aa2591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259735`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); SELECT DISTINCT * FROM p NOT INDEXED LEF
```

---

## Crash 241: `dc2fb1290ed43c94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260733`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE, c2 INT PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_TIMESTAMP, FALSE); VALUES (TRUE); CREATE VIRTUAL TAB
```

---
