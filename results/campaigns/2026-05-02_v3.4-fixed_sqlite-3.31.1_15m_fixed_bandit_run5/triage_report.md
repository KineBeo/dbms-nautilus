# Crash Triage Report

**Total crashes:** 124  
**Unique crash sites:** 124  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 124 | 124 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `a322635c0e059437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000215`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT s.*; CREATE TABLE IF NOT EXISTS p(c3 TEXT GENERATED ALWAYS AS (NOT EXISTS (SELECT * FROM t2 WHERE FALSE) IS CURRENT_
```

---

## Crash 2: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000532`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 3: `946df816c2aaac57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000542`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a); WITH RECURSIVE q (c2, rowid, c1) AS NOT MATERIALIZED (VALUES (RAISE(IGNORE) IS NULL COLLATE NOCASE ISNULL % random() NOT NULL IS NOT CURREN
```

---

## Crash 4: `412644a1d81e0d30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000919`

```sql
SELECT printf('%lli', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t1 SELECT DISTINCT total_changes() FILTER (WHERE NULL BETWEEN FALSE NOT IN (VALUES (CU
```

---

## Crash 5: `aaae4501fa1d4521` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001165`

```sql
SELECT substr('_-6-_sG M5G_-8E', -2147483648, -9223372036854775808); SELECT substr('', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO r VALUES (zeroblob(CASE NUL
```

---

## Crash 6: `11e94ee85d12fb93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001243`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, c1, c1, c1, b, c1); INSERT INTO p SELECT CURRENT_DATE COLLATE NOCASE, * FROM q NATURAL JOIN q USING (rowid) WHERE (SELECT *) ->> lower(CURREN
```

---

## Crash 7: `f58481264838ce9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001591`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO q VALUES (upper(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME != RAISE(IGNORE)) > CURRENT_
```

---

## Crash 8: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001623`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 9: `8987ce70a3422796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002268`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NULL COLLATE BINARY); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE
```

---

## Crash 10: `78791fffec059bd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002655`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_DATE); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 11: `0fd50d75a409e223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002703`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 12: `14bba9c3822d5f8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002966`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 13: `fe618cf80a08becc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003079`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); SELECT round(1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (CURRENT_TIME) ORDER BY CURRENT_TIME & TRUE ASC EXCEPT SELE
```

---

## Crash 14: `870ac89727b056fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003505`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY CURRENT_DATE DESC; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT
```

---

## Crash 15: `75c8558162585540` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003549`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT CURRENT_DATE LIMIT CURRENT
```

---

## Crash 16: `08aaa6d933c3a8ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003577`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 17: `5c88fb3a03e35569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004488`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p JOIN p h_6__hu_37a_4m__06__9z4_2v__44_hu_u_5_5__z025 ON FALSE; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 18: `5f05a7e4c98ef9eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004557`

```sql
SELECT printf('%.*s', -9223372036854775808, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT * FROM p NATURAL JOIN p WHERE EXISTS (SELECT DISTINCT TRUE COLLATE BINARY >= RAI
```

---

## Crash 19: `88e801a5d66c8e62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007685`

```sql
SELECT substr('Er', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT FALSE, r.* FROM (SELECT NOT (SELECT *, * ORDER BY FALSE DESC) LIKE iif(+TRUE COLLATE BIN
```

---

## Crash 20: `f43fa4f4263e03a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009507`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON TRUE = CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 21: `e658b57b4e47e7cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012230`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c1 INTEGER UNIQUE); WITH RECURSIVE r AS (VALUES (CURRENT_DATE)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 22: `56db1fdc24967fe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012493`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT TRUE); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); IN
```

---

## Crash 23: `05c354378d1f30f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012711`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT X'17A0dC83Ef3b6A'); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 24: `59518121043019db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012858`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT CURRENT_TIME); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; SELECT hex(zeroblob(-9223372036854775808)); CREATE V
```

---

## Crash 25: `b46336e94d5e2912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012896`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 BOOLEAN); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS
```

---

## Crash 26: `f739f45f5b955f07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012934`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT CURRENT_TIME); VALUES (FALSE); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 27: `3aecc91c118bd818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012983`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 REAL PRIMARY KEY); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 28: `96e3238470c86348` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013309`

```sql
SELECT round(-1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); VALUES (FALSE) ORDER BY NULL COLLATE RTRIM << FALSE = NULL << NOT RAISE(IGNORE) NOT NULL DESC NULLS FIRS
```

---

## Crash 29: `36a514d171f77839` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016669`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 30: `4f605c6f809fe76c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018667`

```sql
SELECT substr('-_u0 b_-', -1, 2147483648); SELECT printf('%lld', -2147483648, 'n rR_ _ _  _v--1-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q VALUES (NULL NOT IN (SE
```

---

## Crash 31: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020059`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 32: `64271cdf6b57c187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020981`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRAGMA in
```

---

## Crash 33: `f0b6d14d44a19d12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021978`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE EXISTS (SELECT DISTINCT * FROM p LIMIT NULL IS NOT CURRENT_TIMESTAMP IS NOT NULL, TRUE COLLATE NOCASE); CREATE VIRTUA
```

---

## Crash 34: `ae01138347cab052` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023208`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 35: `f8d9a25e0b595368` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023540`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p JOIN p h_6__hu_37a_4m__06__9z4_2v__44_hu_u_5_5__z025 ON ~CURRENT_DATE < CURRENT_DATE; CREATE VIR
```

---

## Crash 36: `4d89c39e029c8a5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023934`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p JOIN p h_6__hu_37a_4m__06__9z4_2v__44_hu_u_5_5__z025 ON FALSE >> CURRENT_TIME; CREATE VIRTUAL TA
```

---

## Crash 37: `ddf7b6eb499f0db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024139`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p JOIN p h_6__hu_37a_4m__06__9z4_2v__44_hu_u_5_5__z025 ON CURRENT_DATE NOT NULL; CREATE VIRTUAL TA
```

---

## Crash 38: `e0f42cb3231f8f19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024684`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 39: `74f40d450b6e9e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025322`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r NOT INDEXED LEFT JOIN t3 AS jv USING (rowid, a) WHERE CURRENT_TIMESTAMP LIMIT CURRENT_DATE; INSERT INTO
```

---

## Crash 40: `85d02e7f707b4a0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030746`

```sql
SELECT printf('%f', 9223372036854775807, ' Q'); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 41: `3bcb1d6a89a95f06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031716`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 42: `e1a4dfa0ec82b9bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035962`

```sql
SELECT printf('%.*g', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(4294967295));
```

---

## Crash 43: `c44a30d75f325b72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037060`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid
```

---

## Crash 44: `6cdbb70b7c82358f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038452`

```sql
SELECT printf('%.*d', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(4294967295));
```

---

## Crash 45: `96bf86b9527bf033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039319`

```sql
SELECT hex(zeroblob(1)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 46: `25e697b2070b9501` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039421`

```sql
SELECT hex(zeroblob(1)); SELECT substr('yy cKLC-', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r DEFAULT VALUES; ANALYZE r; SELECT printf('%.*e', 2147483647, -1e
```

---

## Crash 47: `6a05718bf13a620e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042777`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (-817148.9477489902736153375336634685704468); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 48: `2b70c2c21e91a97c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042804`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (_rowid_)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRA
```

---

## Crash 49: `c87742ab7092a107` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT CURRENT_DATE, c2 BOOLEAN GENERATED ALWAYS AS (c1) VIRTUAL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 50: `bd071b6e4717ac39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042873`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, c3 GENERATED ALWAYS AS (a IS NULL) , a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 51: `d35398f36f78de64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043496`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL COLLATE BINARY); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 52: `bd5d29d71bbf0631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047554`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2, c2); INSERT INTO q VALUES (NULL <= FALSE GLOB FALSE, TRUE, +CASE RAISE(IGNORE) WHEN CURRENT_DATE COL
```

---

## Crash 53: `8773f8872bf3d680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047612`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(rowid DATE UNIQUE, c2 NUMERIC NOT NULL DEFAULT '_A O_-_ 5-_ '); EXPLAIN QUERY PLAN SELECT TRUE; CREATE VIRTUAL 
```

---

## Crash 54: `56848baacba2eb88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048150`

```sql
SELECT substr('', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO q VALUES (randomblob(TRUE > CURRENT_DATE ->> TRUE) FILTER (WHERE (NOT CURREN
```

---

## Crash 55: `adfcd93e8b0a8b50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050211`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) DEFAULT X'EEC8EeDfaBfF7B'); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 56: `03730936cea68bdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050310`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 57: `ea355fe23b310da0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051335`

```sql
SELECT printf('%.*d', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(4294967295));
```

---

## Crash 58: `14e02b38824b018a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058106`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); WITH t3 AS (SELECT *) SELECT * FROM (SELECT * FROM p WHERE FALSE GROUP BY NULL) AS n_f_96k35a4_5om_
```

---

## Crash 59: `bba177249de6321d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059182`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); INSERT INTO p 
```

---

## Crash 60: `54a335a447b4c185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059320`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); INSERT INTO p 
```

---

## Crash 61: `6612460c9ab99e7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059856`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VI
```

---

## Crash 62: `2aebcc19c1b6632c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059902`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT, a GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (-817148.9477489902736153375336634685704468); 
```

---

## Crash 63: `a70215d31b19acab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE VIEW IF NOT EXISTS v1 AS WITH t2 (b) AS (VALUES (CURRENT_DATE)), t1 AS (VALUES (RAISE(IGNORE))) SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) EX
```

---

## Crash 64: `d131b538637a8b3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059946`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT CHECK (NULL > CASE WHEN CURRENT_TIMESTAMP - CURRENT_TIMESTAMP > RAISE(IGNORE) IN (NULL) THEN FALSE <= CURRENT_TIMESTAMP + CURRENT_DATE ELSE -NULL BETWEEN CURRENT_
```

---

## Crash 65: `f85f697919ec7491` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061855`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME * CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 66: `8c1b5edefb6471ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064947`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_DATE) UNION ALL VALUES (count(*) OVER ()); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 67: `f55e7a2b014f6e47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067354`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 68: `1db1faa26145cf64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067365`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) U
```

---

## Crash 69: `97808c08653154ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067497`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT
```

---

## Crash 70: `7ff620a72969cde9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067616`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT X'cff2F9F34A'); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 71: `6017b794323ae5d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067665`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 72: `6ba6ff2fe00c6203` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068061`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION SELECT DISTINCT * FROM 
```

---

## Crash 73: `8ac2e54bc94efe03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068212`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INT
```

---

## Crash 74: `886ef226462b67f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068364`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT 
```

---

## Crash 75: `b2f9278faacf93db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068880`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO p SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_DATE; PRAGMA quick_check; CREATE VI
```

---

## Crash 76: `9268e47ee434285f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075318`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN SELECT DISTINCT count(*) OVER (OR
```

---

## Crash 77: `9913dca4b88a7264` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087175`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (NULL IS NOT CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 78: `4a7bcc47a2214dd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090316`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p JOIN p h_6__hu_37a_4m__06__9z4_2v__44_hu_u_5_5__z025 ON TRUE; CREATE TABLE IF NOT EXISTS p(c2 NU
```

---

## Crash 79: `79fe216b449ee036` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090797`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT NULL % CURRENT_TIME MATCH changes() AS y_y7j8____2b_miz1mtngkojyb1_77_9sg_j_24dy1l205tw5___7_z_9a__180_5_
```

---

## Crash 80: `c71a3f575910dee3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091520`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE IN (CURRENT_DATE, FALSE, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p 
```

---

## Crash 81: `4b7dca9524b0600a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091980`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (TRUE)) BETWEEN CURRENT_TIME AND CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 82: `0191f4fd95efc6d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092181`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE BETWEEN CURRENT_TIME AND CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 83: `6c33de41776078eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095110`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE EXISTS (SELECT DISTINCT * FROM p LIMIT NULL IS NOT CURRENT_TIMESTAMP IS NOT NULL, EXISTS (SELECT DISTINCT * FROM p LI
```

---

## Crash 84: `14cc7a13a715eee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095985`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE (VALUES (CURRENT_TIMESTAMP)) < FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT
```

---

## Crash 85: `b5c9acd5b8dc317b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096419`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT FALSE, c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.*f', -21
```

---

## Crash 86: `a709f4663c6bbe16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096582`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.*f', -2147483649, -1e308
```

---

## Crash 87: `e0ff2cc3e4cbbedf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097516`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_TIME IS NOT FALSE IS NOT NULL; SELECT printf('%.*g', -2147483649, 0.01)
```

---

## Crash 88: `32af28d01a584736` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097964`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT FALSE IS NOT NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 89: `b759b7205c8864ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098359`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 90: `1f4a068315ecc712` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098471`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT NULL IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VAL
```

---

## Crash 91: `924bdbd419fce5aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098502`

```sql
SELECT printf('%.*f', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NULL NOT IN (avg(CURRENT_TIMESTAMP) FILTER (WHERE +CURRENT_TIME COLLA
```

---

## Crash 92: `1d5260411a673fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098580`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES 
```

---

## Crash 93: `0169ae332ae6e8bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100338`

```sql
SELECT round(1e-308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, b, c2, c3, c3, a, c1); SELECT ALL CURRENT_TIME ISNULL LIKE TRUE NOTNULL ESCAPE last_insert_rowid() || CUR
```

---

## Crash 94: `db2f3641656fdb4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101002`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (TRUE)); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 95: `b8ca48ccdfec04fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101140`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 96: `a745933739ba0956` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101547`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT OR IGNORE INTO p VALUES (EXISTS (SELECT DISTINCT * FROM p LIMIT CURRENT_DATE)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 97: `9b7685db1d8d6c94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105895`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE, b VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 DEFAULT VALUES;
```

---

## Crash 98: `539bf11ee40bf56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106240`

```sql
SELECT substr('', 0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 (rowid) VALUES (EXISTS (VALUES (NOT EXISTS (SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIMEST
```

---

## Crash 99: `f09dcf6b4805ce9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106452`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER); SELECT NULL AS t_a4re_7mo_1_840_b8__q_f2, * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INT
```

---

## Crash 100: `92d95165b36012e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115514`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT TRUE); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); INS
```

---

## Crash 101: `7831bb70ec4b37a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115887`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) , c2 DATE DEFAULT X''); WITH RECURSIVE r AS (SELECT *) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 102: `fb7ae00ccb4ef3ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116254`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); WITH RECURSIVE p AS (VALUES (CURRENT_DATE)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 103: `d1f5ac448ede6174` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122040`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP || TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 104: `2bc4e19eccc96760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122256`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP || CURRENT_TIMESTAMP NOT LIKE TRUE; CREATE VIRTUAL TABLE I
```

---

## Crash 105: `ec1145c1227317d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122608`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON TRUE = NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 106: `fd2acc7be7629dec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122677`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON TRUE = FALSE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 107: `8203efe8e861fcef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124867`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TAB
```

---

## Crash 108: `e252c88d2d00b6b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125439`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT NULL, c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CRE
```

---

## Crash 109: `8b55afe5516fc9cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125660`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT -54, c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREA
```

---

## Crash 110: `dbcac991dffe5f02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125738`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE TRUE > CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 111: `301321146122152b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126282`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL, c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT CURRENT_DATE COLLATE RTRIM AS oklts_ FROM p WHERE CURRENT_
```

---

## Crash 112: `ccb192871a12014f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126432`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT FALSE AS oklts_ FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUA
```

---

## Crash 113: `7cc0740b01d4c1de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126463`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CAST(CURRENT_TIME AS TEXT)) AS sub1; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 114: `122e1062164f758a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126997`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT '___ 8SV-_-RW_-D_ _Y'); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRT
```

---

## Crash 115: `8371665786061c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127775`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT p.* FROM q JOIN p a ON CURRENT_DATE IS NOT NOT FALSE / RAISE(IGNORE) NOT BETWEEN NULL AND -FALSE
```

---

## Crash 116: `676df5729b0c824d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128184`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT * FROM p GROUP BY CURRENT_TIMESTAMP, CURRENT_TIMESTAMP LIMIT TRUE + TRUE OFFSET CU
```

---

## Crash 117: `b516a44d275c4394` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129168`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME LIKE _rowid_) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 118: `b2c6d1020f72f9e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129349`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE NULL COLLATE NOCASE) AS sub1; CREATE VIRTUAL T
```

---

## Crash 119: `d911f35dd7e56de5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129430`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE LIKE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF
```

---

## Crash 120: `80f6bb0cb95191a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129986`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT group_concat(CURRENT_DATE, '---2--wX8n_') FILTER (WHERE CURRENT_TIMESTAMP) OVER
```

---

## Crash 121: `d151916aad6468d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131090`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN p a ON TRUE = -0.9; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSER
```

---

## Crash 122: `8c03a77b4ac31995` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143652`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER); SELECT count(*) FILTER (WHERE EXISTS (SELECT DISTINCT * FROM p LIMIT NULL)) AS f_ FROM p NATURAL JOIN p WHERE TRUE; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 123: `7d835c9688a8943a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143770`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER); SELECT *, avg(NULL) FILTER (WHERE CURRENT_TIMESTAMP) AS f_ FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); IN
```

---

## Crash 124: `b369e96040c05703` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144536`

```sql
SELECT printf('%.*d', -9223372036854775808); SELECT printf('%.*e', 9223372036854775807, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (EXISTS (VALUES (C
```

---
