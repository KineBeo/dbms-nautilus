# Crash Triage Report

**Total crashes:** 85  
**Unique crash sites:** 85  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 85 | 85 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9bcf4b52214ae083` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000153`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t2 VALUES (CURRENT_TIMESTAMP COLLATE NOCASE COLLATE NOCASE); SELECT q.* UNION ALL WITH q AS NOT MATERIALIZED (SELECT *), t3 AS (SEL
```

---

## Crash 2: `4eb20ec39b9dd35c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000314`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3, c1); EXPLAIN QUERY PLAN SELECT sum(CASE CURRENT_TIME > CURRENT_DATE IS DISTINCT FROM (VALUES (CURRENT_DATE COLLATE BINARY)) NOT BETWEEN
```

---

## Crash 3: `4dd77b13188e420b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000493`

```sql
SELECT substr('b_s___-i_ P _', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NOT EXISTS (WITH RECURSIVE t2 AS NOT MATERIALIZED (SELECT * UNION ALL SELECT
```

---

## Crash 4: `9f46b52bafc356a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000580`

```sql
SELECT substr('--_5-_ S G-_s   0', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO t2 (c3) VALUES (+FALSE - CASE FALSE WHEN CURRENT_TIMESTAMP THEN FALSE ELSE NUL
```

---

## Crash 5: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000884`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 6: `09da6cafd8bab223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001111`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO t1 VALUES (NOT NOT CURRENT_DATE IN (CURRENT_DATE) MATCH -changes() AND CURRENT_TIME LIKE RAISE(I
```

---

## Crash 7: `1c75cce87593e6fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001756`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN SELECT * FROM p AS j_j___4o__0_6m_6___9szj06_8_6r__r_l6_9_r053kqe__qp_v7q__4u_b2__4i_qh___5g_j105vm_
```

---

## Crash 8: `da1cf094b9d5595a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001769`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_DATE IN (SEL
```

---

## Crash 9: `f467b26be73ad4d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002304`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 10: `a79f4f58aae91643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002350`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE IN
```

---

## Crash 11: `af2f484feabfb6f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002519`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE, c3 NUMERIC UNIQUE, c1 VARCHAR(255) DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CRE
```

---

## Crash 12: `d8f20a29bdad03ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002546`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE, c3 NUMERIC UNIQUE, c1 VARCHAR(255) DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SEL
```

---

## Crash 13: `7accc420af2e4ae9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002593`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE, c1 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-1)); SE
```

---

## Crash 14: `b7be716537b097bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003199`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN SELECT CURRENT_TIME BETWEEN (CURRENT_TIMESTAMP) AND
```

---

## Crash 15: `f226540b6e48ba5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003762`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT round(-1e308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 R
```

---

## Crash 16: `c3d5da135876b04a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005322`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (FALSE REGEXP RAISE(IGNORE) GLOB CAST(TRUE AS INT) IS CURRENT_TIME ISNULL NOTNULL NOT NULL); SEL
```

---

## Crash 17: `a8805ca8f98c1f3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005585`

```sql
SELECT substr('', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s VALUES (CAST(CURRENT_TIMESTAMP COLLATE NOCASE AS NUMERIC)); ANALYZE q; CREATE TABLE IF NOT EXISTS
```

---

## Crash 18: `d166035ead82b9f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005606`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s VALUES (CAST(CURRENT_TIMESTAMP COLLATE NOCASE AS NUMERIC)); ANALYZE q; CREATE TABLE I
```

---

## Crash 19: `5eb8c9aa0db082b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005879`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURS
```

---

## Crash 20: `6092ab7a1e08e5d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006675`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 VALUES ((SELECT ALL CURRENT_TIMESTAMP NOTNULL, p.* FROM p NOT INDEXED JOIN q AS nj)) ON CONFLICT 
```

---

## Crash 21: `6f8e689f210e8213` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007061`

```sql
SELECT substr('', 4294967295, 0); SELECT printf('%d', 4294967295, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT CURRENT_TIME REGEXP CURRENT_TIME COLLATE RTRIM, (N
```

---

## Crash 22: `924154ab297a9179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007155`

```sql
SELECT printf('%.*e', -2147483649); SELECT substr(' ---x--__K_  U', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT RAISE(IGNORE) AS dl_, r.* FROM p NATURAL JOIN
```

---

## Crash 23: `6d5bf0b8d092833d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007685`

```sql
SELECT substr('', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (NULL, json_extract(TRUE != ~+CURRENT_TIMESTAMP ->> CURRENT_DATE, 'S6Ge96 p') OVER (PARTITI
```

---

## Crash 24: `a94aabe8c5f41171` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007763`

```sql
SELECT printf('%s', 9223372036854775807, ' F e9__v_4-_px0'); SELECT printf('%u', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO q (c2, c1, a, c1, c1, c2) VALUES (RAIS
```

---

## Crash 25: `9beb59487cf55b5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013949`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, _rowid_ GENERATED ALWAYS AS (a IS NULL) NOT NULL, c1 VARCHAR(255) GENERATED ALWAYS AS (FALSE) STORED); INSERT OR IGNORE INTO p VALUES (NULL); PRAGMA integrity_che
```

---

## Crash 26: `29aed32521cdc388` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014017`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, _rowid_ GENERATED ALWAYS AS (a IS NULL) NOT NULL, c1 VARCHAR(255) GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 27: `a4e8a07698ed4322` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014672`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-1
```

---

## Crash 28: `8fcecd270f4c2e73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014715`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-1
```

---

## Crash 29: `f8ae96883c2d6783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014733`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-1
```

---

## Crash 30: `4af33dceae0f20f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016221`

```sql
SELECT printf('%.*s', 2147483647); SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO r VALUES (CURRENT_DATE != TRUE, (FALSE))
```

---

## Crash 31: `f677b86d8d3576b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016393`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, a); VALUES (TRUE);
```

---

## Crash 32: `2ee262cd5474c129` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016399`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 33: `fb704d3d77be38d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016406`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 34: `812e094d36be3818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016544`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 35: `7ef877a53172c095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017663`

```sql
SELECT printf('%lli', -2147483648, ' '); SELECT printf('%.*f', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES (RAISE(IGNORE) || CURRENT_TIME != ~CURRENT_DATE
```

---

## Crash 36: `ea2fb1a4940be140` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018845`

```sql
SELECT round(1.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c3, _rowid_); EXPLAIN QUERY PLAN WITH RECURSIVE t1 AS (VALUES (CURRENT_TIME, RAISE(IGNORE)) INTERSE
```

---

## Crash 37: `d1b7cb36a48e557b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019054`

```sql
SELECT substr('', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (abs(+-FALSE COLLATE NOCASE NOT IN (CURRENT_TIME < CURRENT_TIME, N
```

---

## Crash 38: `643f469bd078662a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023041`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME <> CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_row
```

---

## Crash 39: `9154fecdd400c65c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023462`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME << FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT
```

---

## Crash 40: `39f8814ab4aca0e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023683`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); INSERT OR IGNORE INTO p VALUES (~NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 DEFAULT
```

---

## Crash 41: `5a1052fbf68dc979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024048`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP IS NULL COLLATE BINARY); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 42: `1f481e6a3a1c750d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024866`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER CHECK (FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 43: `d7a3917920545f55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024951`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(rowid REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `497a2bdab8f1b72c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025220`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 45: `d0a5ac54fdb6ee35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025552`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER CHECK (TRUE NOT BETWEEN TRUE AND TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 46: `d5ac3f9e657e1735` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025766`

```sql
SELECT printf('%.*e', 1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, a); WITH RECURSIVE s AS NOT MATERIALIZED (VALUES (CASE RAISE(IGNORE) WHEN CURRENT_DATE NOT NULL THEN CURRENT
```

---

## Crash 47: `6ae4f6fe31656573` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026370`

```sql
SELECT printf('%.*s', -1, -1.0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 48: `d4c767e3f3d5472a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027077`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid
```

---

## Crash 49: `1096a1f7486fc8fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027636`

```sql
SELECT printf('%.*d', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO p VALUES (NULL IN (SELECT r.* FROM q) GLOB unicode(NULL) FILTER (WH
```

---

## Crash 50: `a5d371176769df80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027748`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 51: `4a7857f45d898f3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028272`

```sql
SELECT printf('%.*s', -9223372036854775808); SELECT round(1.0, -2147483649); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 52: `b8761d88a70bdfee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029102`

```sql
SELECT printf('%x', 0, ' 361-_4x--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); SELECT hex(zeroblob(2147483648));
```

---

## Crash 53: `a4b328b9592f9dbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029228`

```sql
SELECT substr('_P_  _g7-', -2147483648, 2147483647); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 54: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029979`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 55: `af963773d3cb572f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030076`

```sql
SELECT round(-1.0, 0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 56: `825c95c177e2eb30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030266`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 57: `c94652a99bb371d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030437`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 58: `92b69c0d02a6304e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033774`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 59: `e57305adf5726f1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034132`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE, c3 NUMERIC UNIQUE, c1 VARCHAR(255) DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME
```

---

## Crash 60: `628e71df4e1bc84e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034867`

```sql
SELECT printf('%.*f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT q.* FROM t2 NOT INDEXED CROSS JOIN r NOT INDEXED NATURAL LEFT JOIN p AS a WHERE CASE WHEN RAISE(IGNOR
```

---

## Crash 61: `9a2593cb4ffc1fc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035486`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 62: `ec32e2a916c078ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035629`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 63: `2479ea1e2d489c25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035667`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a
```

---

## Crash 64: `071f63fce00fed84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035692`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a
```

---

## Crash 65: `a8729445066bfbd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037323`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 66: `da752f21adacfb32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039822`

```sql
SELECT printf('%.*s', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIME); SELECT hex(zeroblob(2147483648));
```

---

## Crash 67: `08bee82b6efc6dca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040920`

```sql
SELECT printf('%.*d', 0, -1e308); SELECT round(1e-308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (a) VALUES (CURRENT_DATE IS CURRENT_TIME ISNULL) ON CONFLICT(
```

---

## Crash 68: `8076fbf34403cd92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041141`

```sql
SELECT printf('%f', 4294967296, 't-__ R   2F _y1-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT TRUE MATCH CURRENT_TIMESTAMP IS DISTINCT FROM NULL - RAISE(IGNORE) AS tpd_5x__ FROM
```

---

## Crash 69: `1f6d59f393e86fde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041655`

```sql
SELECT printf('%.*g', -2147483649, -0.0); SELECT printf('%.*f', 1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY (VALUES (CURRENT_TI
```

---

## Crash 70: `bd2c55dba7272ba0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042546`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); WITH p AS (SELECT *) INSERT INTO q VALUES (TRUE < CURRENT_TIME - CURRENT_TIMESTAMP); PRAGMA quick_check;
```

---

## Crash 71: `92fbcdfbf3b0a49e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044525`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE); VALUES (NULL) EXCEPT VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO p VA
```

---

## Crash 72: `bf8c8a96ac21d034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048369`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN DEFAULT 'Bbdb_Op--__  FI'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (NULL); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 73: `9ceee69c94c6ea01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050658`

```sql
SELECT printf('%.*d', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE r AS NOT MATERIALIZED (SELECT * FROM q NOT INDEXED INTERSECT VALUES (group_con
```

---

## Crash 74: `42cac1c673cc31e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053329`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - CURRENT_DATE = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIME
```

---

## Crash 75: `25b4cf8281ad77bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053367`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> CURRENT_DATE), c1 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE V
```

---

## Crash 76: `7184ad5b396ca196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053373`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> FALSE - CURRENT_DATE = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_T
```

---

## Crash 77: `e92fffba99504755` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053379`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - TRUE), c1 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRT
```

---

## Crash 78: `9f2eee11cf22e292` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053385`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - CURRENT_DATE = CURRENT_TIMESTAMP), c1 DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 79: `6259957c1dc90b27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053391`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP), c1 DATE NOT NULL); INSERT I
```

---

## Crash 80: `c28613bfb0d5b7d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053397`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP), c1 DATE
```

---

## Crash 81: `412ca4026fa28156` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053403`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - NULL = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP), 
```

---

## Crash 82: `67f3094491e8e022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053409`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INT CHECK (NULL <> c1 - FALSE = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP = CURRENT_TIMESTAMP =
```

---

## Crash 83: `702c4e771feb0fbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053597`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); REPLACE INTO p VALUES (CAST(TRUE AS REAL)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 84: `ff1c6287ebf70cfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053792`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 85: `fe099afc045c07f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053909`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE, c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---
