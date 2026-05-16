# Crash Triage Report

**Total crashes:** 113  
**Unique crash sites:** 113  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 0 | 0 | 0% |
| Signal | 113 | 113 | 100% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `49cec28a33fb5254` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000209`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIMESTAMP AS l___a0__0rv, CURRENT_TIMESTAMP FROM q NOT INDEXED NATURAL JOIN s WHERE
```

---

## Crash 2: `5489f7a09557156f` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000303`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); INSERT INTO q VALUES (CURRENT_TIMESTAMP BETWEEN TRUE IS NOT DISTINCT FROM TRUE | FALSE COLLATE NOCASE NOT NULL == (FALSE NOT NULL) AND
```

---

## Crash 3: `840377f9340fd216` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000750`

```sql
SELECT printf('%.*e', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 (a) VALUES (CAST(CURRENT_TIME IN (VALUES (CURRENT_TIMESTAMP)) NOT NULL ISNULL AS INTEGER)) 
```

---

## Crash 4: `a1056d631531e0e0` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000992`

```sql
SELECT substr('m_7- _ _ ', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); SELECT p.* FROM p JOIN p p5y207_98k12pw_7k__ ON +q.b IS NOT NULL;
```

---

## Crash 5: `ade1bbbccd9d3656` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001129`

```sql
SELECT printf('%.*f', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); INSERT INTO t2 (_rowid_, c2) VALUES (char(RAISE(IGNORE) - NULL % CURRENT_TIME & -NULL IS RAISE(IGN
```

---

## Crash 6: `d70c8ce39e5a248c` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001510`

```sql
SELECT printf('%.*s', 2147483648, 1.0); SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT X'', b INTEGER UNIQUE, c3 INT UNIQUE, a REAL GENERATED ALWAYS
```

---

## Crash 7: `c590cfc9a211232f` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001660`

```sql
SELECT substr('z', 0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT OR IGNORE INTO p VALUES (NOT CASE CASE +NOT TRUE WHEN CURRENT_TIME NOT IN (NULL COLLATE RTRIM I
```

---

## Crash 8: `af7fd9cbc733af05` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001817`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (count(*) FILTER (WHERE NULL BETWEEN CURRENT_DATE AND RAISE(IGNORE)) OVER ());
```

---

## Crash 9: `e2ef62152e52d79e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002619`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB DEFAULT X'e9dFFF53A4'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 10: `ee5dbde3f907b610` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002632`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO t3 VALUES (abs(CURRENT_DATE) <> CURRENT_DATE NOT LIKE FALSE NOT NULL << TRUE 
```

---

## Crash 11: `bdbbcc587e7d5395` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002639`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 12: `768d3aa70536579d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002645`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 13: `31395495beb5cee7` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002666`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 14: `60f95b42df3e8665` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002692`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); WITH RECURSIVE t2 AS (SELECT *) SELECT *, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VAL
```

---

## Crash 15: `5adbb0c0956a4d4f` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002708`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (substr((-CASE
```

---

## Crash 16: `39b5cfc5ff8afcb9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002893`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c3 INTEGER, c1 GENERATED ALWAYS AS (a + 0) NOT NULL UNIQUE, a DAT
```

---

## Crash 17: `167b203c6de01d03` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002902`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c1 DATE); VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 18: `e68618586562818e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003848`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO q VALUES (s.c1); SELECT CURRENT_TIME / RAISE(IGNORE) IS (VALUES (RAISE(IGNOR
```

---

## Crash 19: `93745ed4e3062807` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004745`

```sql
SELECT printf('%f', -1, ' UY '); SELECT printf('%.*d', 4294967296); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (p.c2); S
```

---

## Crash 20: `daae7f70ab2956c3` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005301`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t1 LEFT OUTER JOIN q LEFT OUTER JOIN q INDEXED BY c1; INSERT INTO p DEFAULT VALUES; ANALYZE p; CRE
```

---

## Crash 21: `6c83290a24396950` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005315`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p
```

---

## Crash 22: `466d2c9f73ea067b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005322`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM s NOT INDEXED; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 23: `138f2318cef2d954` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005330`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t1 LEFT OUTER JOIN q LEFT OUTER JOIN q INDEXED BY c1; INSERT INTO p DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 24: `6c4eee2824f941d2` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005580`

```sql
SELECT printf('%.*e', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP COLLATE NOCASE NOT NULL - RAISE(IGNORE) IS NOT NULL >
```

---

## Crash 25: `6e9e75757bfca797` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005901`

```sql
SELECT printf('%.*f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; SELECT p.*, p.*, CURRENT_DATE >= NULL AS a, total_changes() = NULL ISNUL
```

---

## Crash 26: `e577bc64b0515d54` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006667`

```sql
SELECT substr('--', -1, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO t1 VALUES (((SELECT p.*, p.* FROM t3 NATURAL LEFT JOIN r)) > CASE WHEN CURRENT_TIM
```

---

## Crash 27: `133d0b105a37d87e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007820`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE p AS (SELECT *, NULL LIMIT EXISTS (SELECT CURRENT_TIME AS l5)) SELECT EXISTS (SELECT t1.*) AS ke8b FROM 
```

---

## Crash 28: `ce6aa420a049d1c0` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007897`

```sql
SELECT round(1e-308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT --NULL IS NOT NULL & CURRENT_TIMESTAMP COLLATE NOCASE <= c3 BETWEEN CURRENT_TIMESTAMP NOT IN (SELECT 
```

---

## Crash 29: `aa5cd90b0ef3396b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009426`

```sql
SELECT substr('-7', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 30: `fed0c47a5db14ee7` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010886`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 31: `77f22f90a2728cc6` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010895`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 32: `2912f199b4c9f7b6` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011218`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 33: `1fd94afaf9370db6` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011369`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 34: `b59c55151a0446e8` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012273`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 35: `7782155e3859206b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016854`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (EXISTS (SELECT * FROM s INDEXED BY c3 GROUP BY TRUE ORDER BY TRUE ASC NULLS LAST)) VIRTUAL); 
```

---

## Crash 36: `2346e25342626a9b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017184`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, _rowid_); INSERT INTO t2 DEFAULT VALUES; SELECT 
```

---

## Crash 37: `e2553e778cfb2634` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017211`

```sql
SELECT substr('-7  Q  9_5Ba ', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *;
```

---

## Crash 38: `9feaeed76b0ad096` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019532`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a = -712104) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY 
```

---

## Crash 39: `bef74a355c2a832f` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020456`

```sql
SELECT printf('%.*e', 9223372036854775807, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELE
```

---

## Crash 40: `f073c3cd107d1f56` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020560`

```sql
SELECT printf('%.*d', 2147483647, -1e308); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 41: `ca3d67a46773c03c` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021346`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 (c2) VALUES (EXISTS (SELECT ALL * FROM p NOT INDEXED INTERSECT SELECT DISTINCT *, * FROM r NOT IN
```

---

## Crash 42: `ea00f8f8364b6711` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021487`

```sql
SELECT substr('z --E8--__MkT  G-p_', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, _rowid_); INSERT OR REPLACE INTO t2 VALUES (RAISE(IGNORE) ISNULL, FALSE > CURRENT_TIMESTAM
```

---

## Crash 43: `59c9b7e70cb1ed78` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023287`

```sql
SELECT printf('%.*g', 9223372036854775807, -1e308); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 44: `36427e25f10e26f0` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026163`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01)
```

---

## Crash 45: `f7de6f02df5a6609` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026181`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 46: `cbe539ef998d6291` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026693`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO s VALUES (randomblob(b) NOT LIKE CASE CURRENT_TIME COLLATE RTRIM NOT IN (CU
```

---

## Crash 47: `71304ee56f3ff7f0` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028968`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *; SELECT hex(zeroblob(0));
```

---

## Crash 48: `c72f327e4d98106b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033524`

```sql
SELECT printf('%x', 4294967296, '- WQW  -_ 8_2_lkM5_'); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 49: `8faff12b9b621ea9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033805`

```sql
SELECT printf('%.*g', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELEC
```

---

## Crash 50: `4b909583e6715428` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035728`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT DEFAULT CURRENT_TIMESTAMP, c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT 
```

---

## Crash 51: `4490378cea42b090` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036969`

```sql
SELECT substr(' G3C_L8--_Fr', -9223372036854775808, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALU
```

---

## Crash 52: `310beca8980c6dc2` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037502`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); WITH RECURSIVE t2 AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO 
```

---

## Crash 53: `0b533e11f9ca5413` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038120`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (FALSE); SELECT printf('%.*f', -2147483649, -1
```

---

## Crash 54: `348bc1db50b5b482` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038522`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTU
```

---

## Crash 55: `960d129a92cbcb79` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038700`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT -0); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT printf(
```

---

## Crash 56: `1930a4ae03e6aa46` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038805`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 57: `cd935be39982e2d2` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039294`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXI
```

---

## Crash 58: `f9d3f20afbc39c43` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039737`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE < FALSE) ON CONFLICT DO NOTHING; VALUES (CURRENT
```

---

## Crash 59: `0f8c8ff4ba9c91f1` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040139`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_DATE >= CURRENT_TIMESTAMP) ON CONFLICT DO NOTH
```

---

## Crash 60: `ab96c9f53ddb1a73` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040772`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_TIME >= CURRENT_TIMESTAMP) ON CONFLICT DO NOTH
```

---

## Crash 61: `9fbd9ae73ba69a66` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041147`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE >= TRUE OR NULL) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIME); CREATE VIRTU
```

---

## Crash 62: `ea175828394deff9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041292`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 63: `39f5d67f6a0e526e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042541`

```sql
SELECT printf('%.*d', -2147483649, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p SELECT p.* UNION ALL SELECT CURRENT_DATE ->> RAISE(IGNORE) > ~CURRENT_TIMESTAMP | TR
```

---

## Crash 64: `955ed6f1de051115` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043332`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT round(1.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (RAISE(IGNORE) - NULL IN ((NOT NULL
```

---

## Crash 65: `91c40e174f6cbb0a` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044425`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR 
```

---

## Crash 66: `e36e2db1b080bf58` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046758`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); REPLACE INTO q VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; C
```

---

## Crash 67: `de46c6e10e94cdae` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047558`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (changes()); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 68: `a06fc44d05f1ec1d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048785`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT ALL * FRO
```

---

## Crash 69: `293f264ad5b6d104` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049727`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (NULL % FALSE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 70: `ea80e9253e38552a` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049969`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE >= CAST(FALSE AS FLOAT)) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIME); CREATE VI
```

---

## Crash 71: `121469657d441008` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050473`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT FALSE)) ON CONFLICT DO NOTHING; 
```

---

## Crash 72: `445e2c42bc581bb9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051016`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(rowid B
```

---

## Crash 73: `cbe249d78e9bdc5e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051285`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (FALSE < CURRENT_DATE LIKE TRUE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIME); CREATE VIRTUAL TABL
```

---

## Crash 74: `d4db6780e33ee97d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051546`

```sql
SELECT printf('%s', -2147483649, ''); SELECT printf('%.*g', -2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); SELECT p.* FROM p WHERE EXISTS (SELECT ALL +TRUE NOT LIKE R
```

---

## Crash 75: `476c73914ccc2cc4` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051718`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2); I
```

---

## Crash 76: `e4b886d59ebfabf3` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051877`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (min(TRUE)); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 77: `7d8c21f4409d625c` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052687`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT min(FALSE) AS a; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 78: `24c418fa2a00e805` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052842`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN SELECT min(CURRENT_TIME COLLATE 
```

---

## Crash 79: `b845aac45ab9f094` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE r AS (VALUES (CURRENT_TIMESTAMP)) SELECT DISTINCT * FROM p NO
```

---

## Crash 80: `e103d20e50281184` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059771`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (FALSE)) AS b2 LIMIT CURRENT_DATE OFFSET X'c4DefdB7'; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 81: `975def9b85381666` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060404`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); SELECT DISTINCT * FROM p LIMIT FALSE, FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 82: `9da1cc5aa5b450a6` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060652`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); SELECT DISTINCT * FROM p LIMIT FALSE, CURRENT_DATE << CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 83: `38f89c4f91f528d9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060889`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); VALUES (FALSE) UNION SELECT ALL * FROM q LEFT JOIN q NOT INDEXED USING (rowid) ORDER BY FALSE DES
```

---

## Crash 84: `891f61ddd1a4b224` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062085`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); SELECT * FROM p WHERE CURRENT_TIMESTAMP IS TRUE GROUP BY TRUE WINDOW w1 AS (); CREATE VIRTUAL TAB
```

---

## Crash 85: `092b08ada8f074a6` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062780`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid INTEGER UNIQUE); SELECT DISTINCT * FROM q LEFT JOIN q NOT INDEXED USING (rowid); SELECT printf('%.*g', -2147483649
```

---

## Crash 86: `ace1ecff94082516` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071827`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); PR
```

---

## Crash 87: `af2a51d388913624` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072458`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 88: `b38582328dff29aa` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085017`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t1 LEFT OUTER JOIN q LEFT OUTER JOIN q INDEXED BY c1; INSERT INTO p DEFAULT VALUES; ANALYZE p; CRE
```

---

## Crash 89: `a7f08633ac54943f` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085061`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 90: `f4ec2ae5d745c78d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085282`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT 69.0081824504129490473487916106757, _rowid_ REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quic
```

---

## Crash 91: `152cf2c4db940ba4` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087177`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a = -712104) UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 92: `a51672e3015bf59e` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087405`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 93: `e0261c80c429c67c` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087772`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a = -712104) UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 94: `b0cb6160676db946` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087906`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT OR FAIL INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 95: `61c0d56fdc616b39` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087978`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (a = -712104) UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 96: `5ade85e43d7d357d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091329`

```sql
SELECT printf('%f', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex
```

---

## Crash 97: `0c1968831991120c` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106575`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (TRUE NOT LIKE CURRENT_DATE); PRAGMA quick_check; SELECT subs
```

---

## Crash 98: `307e329de7760b2b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107525`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME | NULL); PRAGMA quick_check; SELECT printf('%.*
```

---

## Crash 99: `a4e74d3d48306abf` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107926`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (NULL IS TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 100: `69c95ea3b6369ddf` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108501`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE << ~FALSE); PRAGMA integrity_check; SELECT prin
```

---

## Crash 101: `e77c034d3c2c1c31` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108607`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*f', -214748
```

---

## Crash 102: `d359a523979894d0` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108700`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE << ~CURRENT_DATE << CURRENT_TIME != CURRENT_TIM
```

---

## Crash 103: `96e214649bf6b8ab` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109533`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 104: `8f80aa8cbb4607c1` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110156`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (TRUE >> CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE V
```

---

## Crash 105: `23f22bfb998a4579` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110321`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN CHECK (TRUE)); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 106: `a63a55747ba57ca1` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110468`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN CHECK (TRUE)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 107: `2027502956766e7d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110689`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT E
```

---

## Crash 108: `fbcef98c9ba51d6b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110841`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (2900.90872851394049484977122525363E228973235259120605324312
```

---

## Crash 109: `1fac9cd73a45865d` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111071`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (NULL NOT IN (FALSE)); PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 110: `5fd630a32f2891dd` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 111: `6c672c469b425f6b` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112538`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME != TRUE & CURRENT_DATE); PRAGMA integrity_check
```

---

## Crash 112: `d5c77963fb2ae8e9` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113718`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (c2)); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 113: `b2f03f37a66b2f37` — signal (signal-5)

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115221`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---
