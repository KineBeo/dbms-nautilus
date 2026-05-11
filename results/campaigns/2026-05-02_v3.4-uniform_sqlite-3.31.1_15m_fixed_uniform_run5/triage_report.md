# Crash Triage Report

**Total crashes:** 159  
**Unique crash sites:** 159  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 159 | 159 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `4e847f5368928dc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000042`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE t2 (rowid, c2, c1, c1, b, _rowid_, c3) AS NOT MATERIALIZED (SELECT r.* FROM r NOT INDEXED NATURAL JOIN p NOT INDEXED INTERSECT 
```

---

## Crash 2: `7351a5678dfc6e7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000174`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2, c3, c3); INSERT OR FAIL INTO q VALUES (FALSE != RAISE(IGNORE) != CURRENT_TIMESTAMP <= NULL IS NOT NULL ISNULL <> TRUE ->> TRUE || TRUE,
```

---

## Crash 3: `7eb6312cc66bb637` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000296`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC CHECK (EXISTS (SELECT *) | 9.46133E31863818821 /
```

---

## Crash 4: `bb96ed4974274ce1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000554`

```sql
SELECT round(0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO q VALUES (CURRENT_TIME || NULL); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); CREAT
```

---

## Crash 5: `54c05afd4b50436c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000586`

```sql
SELECT substr('-5-1-8- 86', -9223372036854775808); SELECT printf('%d', 4294967295, '6V- u_I-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT (WITH p AS NOT MATERIALIZED (VALUES (CU
```

---

## Crash 6: `a418edcf6cc13e20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000658`

```sql
SELECT printf('%.*f', 2147483647, -1e308); SELECT substr('-_NV-_9-3-', -2147483649, 9223372036854775807);
```

---

## Crash 7: `5ad919f37a235ba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001907`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIME ORDER BY TRUE LIKE TRUE ISNULL DESC; CREATE TABLE IF NOT EXIS
```

---

## Crash 8: `2a584316738d9c72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001975`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (SELECT *) SELECT * FROM q NOT IN
```

---

## Crash 9: `ce2364882d87f4ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002012`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CURRENT_TIME ORDER BY CURRENT_T
```

---

## Crash 10: `f65f22420a46f04c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002056`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p AS (SELECT *) SELECT * FROM q NOT IN
```

---

## Crash 11: `922050131a53c8a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003462`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1))
```

---

## Crash 12: `41f37f31d4c61308` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004446`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL DEFAULT 'D '); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 13: `c5b65853bdd18e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004458`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 14: `7f8196c294efc0f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004465`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 15: `309dd7ca282596b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004567`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALU
```

---

## Crash 16: `437afed3a73d29e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006009`

```sql
SELECT substr('-CbGmNp  _ -K 0-7_', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM q NATURAL JOIN t1 WHERE NULL IS NULL;
```

---

## Crash 17: `824e15205357b0e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007354`

```sql
SELECT substr('____D_', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 SELECT ALL NOT EXISTS (SELECT *) FROM (SELECT * UNION ALL SELECT *) AS hi__k__61 I
```

---

## Crash 18: `5e4d5475bcef7963` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007778`

```sql
SELECT printf('%.*g', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT t3.* FROM p WHERE EXISTS (SELECT q.* FROM t3 NATURAL LEFT JOIN q , q GROUP BY TRUE HAVING CURRE
```

---

## Crash 19: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008537`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 20: `7399e668ab61ddc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015457`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (TRUE AN
```

---

## Crash 21: `67dd9b54d29cf181` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015592`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP LIKE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO
```

---

## Crash 22: `ebc1df306ae9a834` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015857`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT I
```

---

## Crash 23: `26f1a40850a3ea4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016203`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE)); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_TIME)); VAL
```

---

## Crash 24: `1223e45a59b2700e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016345`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE)); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); VALUES (CURRENT_T
```

---

## Crash 25: `7ed88543a7ed8fa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018147`

```sql
SELECT round(-1e308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 26: `e63617e7ad38ec35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018273`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (c3, c1) AS (SELECT *) SELECT FALSE AS b__sm_9__3___8__y_72j____q5n_5_
```

---

## Crash 27: `164bf462c31082f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020238`

```sql
SELECT substr('e _   5_uv--', 4294967296, 9223372036854775807); SELECT substr(' kcSEt ', 0); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 28: `285c6c32f2f2e9be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020552`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT count(*) IS NOT NULL FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 29: `426ec5ca5d7b706c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020796`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT coalesce(TRUE == FALSE, NULL) FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE 
```

---

## Crash 30: `3df024b44d49cae8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020972`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 31: `f1f5c23324aada71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021123`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT NULL != CURRENT_TIMESTAMP FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF N
```

---

## Crash 32: `85fa027625d3a8c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021823`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (+++t1.c1 REGEXP TRUE * NULL IS NULL IS NOT DISTINCT FROM TR
```

---

## Crash 33: `1450cc77d2fbccc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022059`

```sql
SELECT printf('%.*s', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); SELECT EXISTS (SELECT *, s.*, RAISE(IGNORE), * FROM t3 INDEXED BY c2 WHERE -CURRENT_DATE UNION S
```

---

## Crash 34: `e0a75e3c80441104` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023965`

```sql
SELECT printf('%.*f', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 35: `ffb0c2729f3fcb68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024271`

```sql
SELECT printf('%.*d', -2147483648); SELECT substr('Yo ', 2147483648); SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT NULL); INSERT OR FAIL INTO p VALUES
```

---

## Crash 36: `bcf21da457b261f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026496`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL COLLATE RTRIM > CURRENT_DATE NOT BETWEEN TRUE AND NULL); VALUES 
```

---

## Crash 37: `de75b74479cd8564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026545`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 38: `59db3377cd62209a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026551`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 39: `39aa3d48b5e1d495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026558`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP NOT BETWEEN TRUE AND NULL); VALUES (CURRENT_TIME); 
```

---

## Crash 40: `cd1d62e6b8309530` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027977`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a);
```

---

## Crash 41: `f85a564da4a5cf0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028305`

```sql
SELECT round(-1.0, -2147483649); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 42: `b2ba9cccc309b022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029124`

```sql
SELECT printf('%f', -9223372036854775808, 'j__3-Ao -M'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(2147483
```

---

## Crash 43: `8a3f7a323f1fd997` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030422`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 44: `9e1281cac9695bd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031456`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL DEFAULT CURRENT_TIME); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 45: `3b33450e457a2586` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032306`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 46: `8cd81ed7a79284dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032357`

```sql
SELECT printf('%.*s', -9223372036854775808, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 47: `a50865cc8f5669c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032649`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (NULL NOT IN (WITH RECURSIVE p AS (VALUES (FALSE)) VALUES (CURRENT
```

---

## Crash 48: `e2ac8847e308ccea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (NULL NOT IN (VALUES (FALSE))); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 49: `a7b53927170dfa1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036680`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); SELECT *, * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR FAIL INTO t1 VAL
```

---

## Crash 50: `80cd739363019888` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039557`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY);
```

---

## Crash 51: `371b1765ae690fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY);
```

---

## Crash 52: `e71b1fa59e95581b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039597`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY);
```

---

## Crash 53: `ad240238228adea4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040270`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE AND TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 54: `d825685c72add436` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040785`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 55: `9c160c823499468a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043686`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME IN (VALUES (NULL) UNION VALUES (CURRENT_DATE))); EX
```

---

## Crash 56: `70bfced0abed54fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044053`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME IN (VALUES (NULL) UNION VALUES (FALSE))); EXPLAIN Q
```

---

## Crash 57: `883a90f72ea531fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049271`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), b GENERATED ALWAYS AS (a IS NULL) UNIQUE, a BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 58: `2e8288f6f520a576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051853`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT, a GENERATED ALWAYS AS (a) NOT NULL, b VARCHAR(255) CHECK (CURRENT_TIMESTAMP)); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a)
```

---

## Crash 59: `85101c38e0ed10d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051991`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT UNIQUE, b NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 60: `da3a7ecc443e4bf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052046`

```sql
SELECT printf('%.*s', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483647));
```

---

## Crash 61: `3f1203b6211cd5da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052266`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_TIME ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 62: `2792139107df4b46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054080`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO p VALUES (FALSE ISNULL) RETURNING CURRENT_DATE IS NULL REGEXP NULL >> FALSE; ANALYZE t2; CREATE T
```

---

## Crash 63: `46f86bcc2cb5a6ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054112`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO s VALUES ((SELECT *, * FROM p WHERE ~RAISE(IGNORE) <= RAISE(IGNORE) COLLA
```

---

## Crash 64: `43b3db592be6defd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054701`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (TRUE, changes()) ON CONFLICT DO NOTHING; SELECT RAISE(IGNORE) FROM p NATURAL JOIN t2 
```

---

## Crash 65: `f830e5915a5f6bec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055080`

```sql
SELECT round(-1.0, 9223372036854775807); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 66: `4d965262c9ada245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056680`

```sql
SELECT printf('%.*d', -2147483649); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 67: `9ff274bda780114d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058250`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT CURRENT_TIME COLLATE BINARY ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CREATE VIRTUAL TABLE 
```

---

## Crash 68: `f83d70264620da8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059165`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT); INSERT INTO p VALUES (CAST(CURRENT_DATE AS NUMERIC)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; C
```

---

## Crash 69: `82ef4d4bdcd172ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066262`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (TRUE NOT IN (TRUE)), c3 INTEGER GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT OR IGNORE INTO q VAL
```

---

## Crash 70: `6c57450713274ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066451`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT OR IGNORE INTO q VALUES (NULL); VALUES (CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 71: `369cb6f03fb9c8e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066457`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(a NUMERIC UNIQUE, c3 INTEGER GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT OR IGNORE INTO q VALUES (NULL); VALUES (CURR
```

---

## Crash 72: `ccb6b5b02935e5a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066463`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC CHECK (NULL), c3 INTEGER GENERATED ALWAYS AS (FALSE) VIRTUAL); INSERT OR IGNORE INTO q VALUES (NULL); VA
```

---

## Crash 73: `687c82fd503ce7b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069391`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO q VALUES (' __ o5 _x-j ' IN (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN V
```

---

## Crash 74: `b5c273ddf85666ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069604`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN VAL
```

---

## Crash 75: `372fb280e22c061a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071595`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE EXISTS (SELECT * FROM q NOT INDEXED WHERE NULL GROUP BY FALSE WI
```

---

## Crash 76: `ded59e152b1d79b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072780`

```sql
SELECT printf('%llu', -2147483649, 'v m-_ 2_90_Oo __'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c3, c3); INSERT INTO p (c2, c1) VALUES (+~count(*) IS NULL NOT NULL * -NULL CO
```

---

## Crash 77: `eafc2c16cf28b635` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073177`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREAT
```

---

## Crash 78: `154a83af08e7a98e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073367`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 79: `1ffdea8ec371287d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073521`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP - CURRENT_DATE - CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 80: `5f524cde9578e7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073808`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL) UNION VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 81: `319c80f0fb16b5c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074055`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE V
```

---

## Crash 82: `90815bd465588c2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074215`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 83: `28ef31641827d98e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074406`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 84: `e167000db744e765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075385`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY);
```

---

## Crash 85: `d82307cde7b93b41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075656`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 86: `1be781d27e506577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075810`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a * a) NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 87: `0dc63135529e7f47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076120`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT
```

---

## Crash 88: `033dc7412779386a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078651`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); SELECT count(*) FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES 
```

---

## Crash 89: `913028ba2de1981a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078993`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN DEFAULT FALSE); SELECT * FROM (SELECT * FROM p WHERE FALSE < FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NUL
```

---

## Crash 90: `8d46ef926164fb54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079118`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (NULL) UNION VALUES 
```

---

## Crash 91: `daa64fc0a4281130` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079944`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS NOT NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INT
```

---

## Crash 92: `549128d5b7276619` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080275`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); SELECT coalesce(CURRENT_TIME, NULL) FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 93: `741bf04e610f77a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080464`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME ISNULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO
```

---

## Crash 94: `a21d1c137ff09d83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081582`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE '- ab GQ HO-_5_r_') AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT
```

---

## Crash 95: `bd310cdae2f828fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082439`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) UNIQUE); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); SELECT p.rowid FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 96: `7dedd1cb0861b8db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083685`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (NULL NOT IN (SELECT count(*) AS n ORDER BY CURRENT_DATE DESC)); P
```

---

## Crash 97: `0459672171f04a39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084324`

```sql
SELECT printf('%x', -1, 'Mi3P--Z-5_8J-c'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CURRENT_TIME AND -TRUE LIKE CURRENT_TIME COLLATE BINARY ESCAPE (CASE WHEN RAISE(IGNORE) THEN 
```

---

## Crash 98: `75c6bc278f7dab4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084431`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (NULL NOT IN (SELECT * FROM p NOT INDEXED WHERE NULL)); PRAGMA int
```

---

## Crash 99: `93bde8c783166894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT IN (VALUES (FALSE)) NOT IN (VALUES (FALSE))); PR
```

---

## Crash 100: `39d8f650550454d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086455`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT X'0Dcd'); CREATE TABLE IF NOT EXISTS q(rowid INT); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 101: `cd81f154ec93bef2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096637`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT count(DISTINCT CURRENT_DATE) FILTER (WHERE FALSE) FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); C
```

---

## Crash 102: `5f654df3e4ea0524` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096976`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT min(CURRENT_TIMESTAMP) FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); SELECT printf('%.*f', 214748
```

---

## Crash 103: `6d86350973e59b46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098001`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT coalesce(CAST(FALSE COLLATE NOCASE AS VARCHAR(255)) == FALSE, NULL) FROM p WHERE EXISTS (VALUES (
```

---

## Crash 104: `cde5df746da0a939` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098976`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT randomblob(CURRENT_TIMESTAMP >> NULL) FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUA
```

---

## Crash 105: `c068a4a3949138a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099655`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, a GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT NULL FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 106: `8a56e9c13d0ec7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102070`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE, c1 INTEGER, _rowid_ FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (FALSE - CURRENT_DATE, NULL, TRUE); SE
```

---

## Crash 107: `0af96e42fe4a879d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110120`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (X''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; PRAG
```

---

## Crash 108: `1a3322058217e458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110255`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (0.0); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLA
```

---

## Crash 109: `5bd1a48081ad0a9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110637`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE)); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXIST
```

---

## Crash 110: `23daab296e686157` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111033`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT -3725); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT 
```

---

## Crash 111: `17042acac291af12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111198`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY
```

---

## Crash 112: `6705b9c449b7fc78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111366`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE))))
```

---

## Crash 113: `4d2f99908fc76e2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111419`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_DATE IN (CURRENT_TIME))))); PRAGMA quick_check; CREATE VIRT
```

---

## Crash 114: `6c10ecfc14e8404e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111605`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP IS NOT NULL NOT IN (TRUE) LIKE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 115: `801b6e69ad0c515b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112590`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (total_changes() LIKE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q
```

---

## Crash 116: `a61c2032a467d3eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113132`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME LIKE CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 117: `8f05af8e8a72a358` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113291`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME LIKE CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INS
```

---

## Crash 118: `60635ea2abda327d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113298`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME LIKE CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INS
```

---

## Crash 119: `f024421ef26b6710` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113354`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p VA
```

---

## Crash 120: `f377343361a62863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113364`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p VA
```

---

## Crash 121: `584b3d63d2819d64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114282`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELEC
```

---

## Crash 122: `ebd640e2a821695e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114309`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELEC
```

---

## Crash 123: `f013e24304e668c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114782`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE > CAST(FALSE COLLATE NOCASE AS VARCHAR(255))); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 124: `493ceb29b84e5adb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114857`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE > CAST(NULL AS VARCHAR(255))); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 125: `d8fce337ee7c9b54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117495`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT); INSERT INTO p VALUES (FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE
```

---

## Crash 126: `31a72bdbebc8ac6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117691`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_TIME NOT NULL || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 127: `5d20d573ddae4ea2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123909`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE HAVING CURRENT_TIMESTAMP MATCH TRUE LIMIT TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 128: `75c4af56e2e54d23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124321`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT 0); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VAL
```

---

## Crash 129: `816abb89ddd848b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124698`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIME FROM p NOT INDEXED GROUP BY CURRENT_TIME LIMIT TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 130: `962fff5f0da0d687` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128024`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT ALL * FROM p NOT INDEXED; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 131: `e8621434099f6af4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128424`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p VALUES (NULL) INTERSECT VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 132: `dfe5914b26c20a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128527`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT * FROM q NOT INDEXED WHERE NULL GROUP BY FALSE WINDOW w1 AS () ORDER BY CURRENT_DATE ASC; P
```

---

## Crash 133: `f81718f61727f96d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129436`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT DISTINCT CURRENT_TIME FROM q; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308)
```

---

## Crash 134: `800076406fcd8545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129601`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT DISTINCT CURRENT_TIME FROM (VALUES (CURRENT_TIMESTAMP)) AS a; PRAGMA quick_check; CREATE VI
```

---

## Crash 135: `d99996a4d302859b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130848`

```sql
SELECT printf('%.*e', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES ((SELECT CURRENT_DATE IS NULL, RAISE(IGNORE) ORDER BY CURRENT_TIME IS NOT RAISE(IGNORE
```

---

## Crash 136: `9c1eeb48c3deb212` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131376`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-7091.370040442647e4562083153800615214976272378814166783457602287065593766); PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 137: `9abaf47974213747` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132570`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT DISTINCT CURRENT_TIME FROM p NOT INDEXED JOIN q NOT INDEXED LEFT OUTER JOIN p; PRAGMA quick
```

---

## Crash 138: `4552bc6f598ff75d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132734`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT * FROM p NOT INDEXED GROUP BY FALSE; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 
```

---

## Crash 139: `39f003aee123a449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133209`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT * FROM q NOT INDEXED; PRAGMA quick_check; SELECT printf('
```

---

## Crash 140: `98c15c679c190828` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133363`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT * FROM q NOT INDEXED; PRAGMA quick_check; SELECT printf('%.*g', 214748364
```

---

## Crash 141: `1cc325e389e000f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133369`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p SELECT * FROM q NOT INDEXED; PRAGMA quick_check; SELECT printf('%.*g', 2147483647,
```

---

## Crash 142: `c590fd1dd62b04d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134634`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO p VALUES (NULL) UNION ALL SELECT CURRENT_TIMESTAMP AS o1__m75__o__81ti1__v___t17_0j ORDER BY NULL DE
```

---

## Crash 143: `b161b1cb7fec0db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137848`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE HAVING min(CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIME) LIMIT TRUE); SELECT printf('%.*g
```

---

## Crash 144: `a9d6b2b95370f543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138218`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p (b) AS (VALUES (CURRENT_DATE)) SELECT ALL * FROM p NOT INDEXED INNER JOIN p AS l1_5d0_____7f__8_2a7_i57xqa2_9zyo___
```

---

## Crash 145: `e652b3c17198ec13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138456`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p (b) AS (VALUES (CURRENT_DATE)) SELECT ALL * FROM (VALUES (CURRENT_TIME)) AS v61ydsy_ NATURAL LEFT JOIN (VALUES (CUR
```

---

## Crash 146: `b0c41ebe208cccd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139164`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (VALUES (NULL) UNION SELECT count(*) AS n); SELECT printf('%.*e', 2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 147: `f7f45236902fe904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139486`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE LIMIT json_type(CAST(TRUE AS REAL))); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 148: `a368e725c59eba30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139654`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE LIMIT json_type(NULL)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 149: `7182210d2831eda0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140048`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE LIMIT json_type(NULL > CURRENT_DATE NOTNULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 150: `5ca7e82fa1ac1330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143407`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p (c2) AS NOT MATERIALIZED (SELECT NULL IS NOT NULL AS l, q.*, p.* FROM q INTERSECT SELECT DISTINCT t2.*
```

---

## Crash 151: `e526c32d647b868f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147231`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL DEFAULT X'DcD2'); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3);
```

---

## Crash 152: `058565a2fea4ed68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148362`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p VALUES (FALSE 
```

---

## Crash 153: `fffb014cbcbf557b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148899`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid, _rowid_); INSE
```

---

## Crash 154: `ec81638afdcc1bf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148921`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE VIEW IF NOT EXISTS v1 AS WITH s AS (SELECT *) VALUES (CURRENT_DATE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VI
```

---

## Crash 155: `16ff93d005f28ef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148936`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1
```

---

## Crash 156: `dfe58ad4ecbb6f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149100`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p 
```

---

## Crash 157: `58e14ae23c076aa0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150009`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP AS o1__m75__o__81ti1__v___t17_0j, count(*) FILTER (WHERE CURRENT_TIME) OVER () FROM p NOT INDEXED GROUP BY 
```

---

## Crash 158: `0f0d190aa5c99abe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152742`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); SELECT * FROM p WHERE EXISTS (SELECT count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_DATE) FROM p NOT INDEXED GROUP BY FALSE LIMIT TRUE); SELECT p
```

---

## Crash 159: `1e1723ac8ef01049` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152972`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE LIKE CURRENT_DATE ESCAPE NULL); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---
