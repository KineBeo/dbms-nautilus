# Crash Triage Report

**Total crashes:** 253  
**Unique crash sites:** 253  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 253 | 253 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `676963c30b61fdd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000250`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO q VALUES (FALSE >= FALSE OR NOT EXISTS (SELECT c3 << NULL COLLATE NOCASE AS q, CAST(CURRENT_TIMESTAMP AS INTEGER) IS NU
```

---

## Crash 2: `f2d0eda423b3187c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000368`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (t2.b == ifnull(CASE CASE WHEN json_valid(TRUE) THEN CAST(FALSE AS REAL) END WHEN +total_changes() IS RAISE(IGNORE) NOTNUL
```

---

## Crash 3: `0b89f760514d0205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000681`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); SELECT CURRENT_DATE IS NOT DISTINCT FROM CURRENT_TIME AS z5 FROM q WHERE EXISTS (SELECT * FROM q WHERE NULL ISNULL GROUP BY ~CURRENT_
```

---

## Crash 4: `245836cd23e651cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000796`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, a, _rowid_); WITH q AS (VALUES (CURRENT_DATE)), q AS MATERIALIZED (SELECT CURRENT_TIMESTAMP | FALSE GLOB -FALSE FROM p INDEXED BY a GROUP B
```

---

## Crash 5: `2fe3a7a8498df7cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001166`

```sql
SELECT substr('', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * UNION ALL SELECT *; CREATE TABLE IF NOT EXISTS p(b BOOLEAN, c2 GENERATED ALWAYS AS (a || b) NOT NULL, b VARCHAR
```

---

## Crash 6: `4918827c73232de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001465`

```sql
SELECT round(1.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c1, c2, c2); INSERT OR ABORT INTO q VALUES (NOT typeof(FALSE) FILTER (WHERE +CURRENT_TIMESTAMP | ~CURRENT_TIME
```

---

## Crash 7: `a83385e9c5d2101c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001822`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 8: `4053f411b291a93a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001838`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (c3 COLLATE NOCASE MATCH upper(CURRENT_TIMESTAMP & NULL BETWEEN CURRE
```

---

## Crash 9: `5e9256d2b58708e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002243`

```sql
SELECT printf('%.*s', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (_rowid_) VALUES (TRUE IS NULL <= FALSE = RAISE(IGNORE) * RAISE(IGNORE) = NULL ISNULL NOT LI
```

---

## Crash 10: `d8c71f29329249f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002291`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; SELECT q.* ORDER BY CURRENT_TIME ASC, FALSE NOTNULL - CURRENT_TIMESTAMP ASC NULLS FIRS
```

---

## Crash 11: `0a046914b1441987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003012`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO q VALUES (CASE WHEN RAISE(IGNORE) GLO
```

---

## Crash 12: `2ce0121c7270660b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003562`

```sql
SELECT hex(zeroblob(-1)); SELECT substr(' _CtxUl- _2A0-l_C', 4294967296, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT ALL nullif(sum(TRUE), -NULL) FILTER (WHERE CASE W
```

---

## Crash 13: `37c1d0593332ba6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005238`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME LIKE CURRENT_TIMESTAMP); SELECT hex
```

---

## Crash 14: `218822d472bd35ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005259`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483648)); CREAT
```

---

## Crash 15: `f6e7e2e121c0e82e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005266`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); SELECT hex(zeroblob(-2147483648)); CREAT
```

---

## Crash 16: `3f2dac7e27e67c4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005662`

```sql
SELECT printf('%.*d', 9223372036854775807, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO p VALUES (NULL IS NULL -> NULL ISNULL NOT IN (TRUE NOTNULL >= ~CUR
```

---

## Crash 17: `01b69570cf0bb575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006249`

```sql
SELECT substr('___Q-_B-', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE s AS MATERIALIZED (VALUES (TRUE IS NULL IS NULL) ORDER BY CASE json_extract(NULL, '') WH
```

---

## Crash 18: `66c9ccbab251cf4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006416`

```sql
SELECT printf('%.*f', 2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (CASE RAISE(IGNORE) WHEN NOT CURRENT_DATE IS CURRENT_DATE THEN CASE FALSE WHEN NUL
```

---

## Crash 19: `8c266e31466c7056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006813`

```sql
SELECT substr('', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CASE WHEN FALSE THEN NULL < -NULL IS NOT DISTINCT FROM CURRENT_DATE REGEXP (NULL) ELSE FALSE OR RAISE(IG
```

---

## Crash 20: `1a48724d9deb3c9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007124`

```sql
SELECT substr('- _s-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS MATERIALIZED (SELECT *, FALSE AS b3f8c_9h5__ec__0g2___l_h_9_c513s287_o2n_4505
```

---

## Crash 21: `99d467d9f52d975d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008207`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CR
```

---

## Crash 22: `d5b23a24fdc42f35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010857`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(-92233720368
```

---

## Crash 23: `32cba85e97c9692f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010971`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN UNIQUE, rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE V
```

---

## Crash 24: `aeafd5401bcb2aec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 25: `0542b842dc21f50a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017626`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c3 INTEGER GENERATED ALWAYS AS (NOT NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIME - CURRENT_TIMESTAMP GROUP BY FALSE
```

---

## Crash 26: `00b1bb175dbde7ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020298`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_
```

---

## Crash 27: `54c7c32224ca3b95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020611`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); I
```

---

## Crash 28: `e71a889d69045683` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020766`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 29: `dc6603db9897ccae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021085`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME LIKE CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 30: `8d9dbb1bcac20ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023072`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 31: `090d011dab83150c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023143`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 32: `218f870a3ec61c76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023167`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY)
```

---

## Crash 33: `84eb4e18ce4878e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023283`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT CURRENT_TIME, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, NULL); PRAGMA quick_check; CREA
```

---

## Crash 34: `b2873c6495e9d1ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023540`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT -0, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 35: `de5c854110445fc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023804`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSE
```

---

## Crash 36: `6dcf4602e1ee39f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023841`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT CURRENT_TIME, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 37: `7f6e0bac0f34688b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025332`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 
```

---

## Crash 38: `7e0ccb2f97e148bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025341`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(2147483648));
```

---

## Crash 39: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027876`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 40: `746986fbd10329eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027927`

```sql
SELECT printf('%.*g', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT p.* INTERSECT VALUES ((TRUE), TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTA
```

---

## Crash 41: `021ed8c6cc8870bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029102`

```sql
SELECT substr('', 9223372036854775807); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 42: `55effd540662a434` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030562`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(1));
```

---

## Crash 43: `30afebceafd5d878` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031041`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); C
```

---

## Crash 44: `9d804ed2df68f3ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031240`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 45: `8df68e888ae4a79b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031382`

```sql
SELECT hex(zeroblob(1)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 46: `32ebc0bb64a61474` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031468`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); INSERT INTO p DEFAULT VAL
```

---

## Crash 47: `5e6b6a56f30aed28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031749`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 48: `1a4038d9256f7704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031940`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q LIMIT -NOT FALSE IS TRUE OFFSET FALSE COLLATE BINARY; PRAGMA integrity_check; CR
```

---

## Crash 49: `c79d39ef95b2808e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037181`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY, c2 REAL); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 50: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039287`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 51: `b25f5f9fc03c7e5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040248`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT *, NULL > CURRENT_DATE IS CURRENT_DATE AS u6_ FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 52: `d87c2de2ac4e8b3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045106`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1
```

---

## Crash 53: `236e31fade0f9353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045593`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE
```

---

## Crash 54: `a7f2ac2021904b33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046283`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); SELECT * FROM q JOIN q c_88__7y_8s_g78q5__z7696pne7u56_na3oc__m6_9_fo_pl5wdae_6_m_1_1wik__qd_6d_g9nw
```

---

## Crash 55: `a9ab73b67f37eb9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047075`

```sql
SELECT substr('v  _-X-_  53', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB GENERATED ALWAYS AS (
```

---

## Crash 56: `1e29041284128c75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047469`

```sql
SELECT substr('', -2147483648, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (~+CURRENT_TIME COLLATE BINARY MATCH CURRENT_DATE & NULL LIKE ~CURRENT_TIME CO
```

---

## Crash 57: `bcd37dc5924103d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049992`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT X'10b8dF'); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT p.* FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFA
```

---

## Crash 58: `93c6b1a76ee09154` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050138`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB DEFAULT TRUE); WITH RECURSIVE r AS (VALUES (CURRENT_TIME)) SELECT p.* FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT V
```

---

## Crash 59: `f1dcd1f9094d636e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050408`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 60: `e05bcface91031ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050640`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP COLLATE NOCASE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 61: `71e2c2214540163e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052464`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME ISNULL) 
```

---

## Crash 62: `b0ff3717ad4330e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052627`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE
```

---

## Crash 63: `370763f3680cb0d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052681`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_DATE AS l_sj_2f1r7_9__xr__ih
```

---

## Crash 64: `625890251a0d4487` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058944`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT 033915372015050674264370449284951077581079231959726627385709068815010618984003902638178016526716286881818319346874961404835.77174941489811832221
```

---

## Crash 65: `1084c61c4e1647de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); SELECT *
```

---

## Crash 66: `959d2e63b941613b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060296`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_TIMESTAMP AS u6_ FROM p; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 67: `fa0b76113edd4d27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061514`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT NULL > TRUE BETWEEN CURRENT_TIMESTAMP AND NULL AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 68: `511d128eb1ea186f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062517`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_TIME COLLATE NOCASE > CURRENT_TIME > FALSE AS u6_ FROM p; CREATE VIRTUAL TABLE IF 
```

---

## Crash 69: `eff27c5f3d807c34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063782`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT count(DISTINCT CURRENT_TIME) > CURRENT_DATE AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 70: `239ce250bd67e8ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064072`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT count(*) > CURRENT_DATE AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 71: `9eae0fe1abc93357` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064571`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT *, count(DISTINCT CURRENT_TIME) AS u6_ FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 72: `8b2656a51ca66307` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064744`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT *, last_insert_rowid() AS u6_ FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 73: `3990f5737f412614` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066887`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT CHECK (TRUE), c3 BLOB CHECK (CURRENT_TIME), rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 74: `959a466c81b96560` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067066`

```sql
SELECT round(-1.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT hex(zeroblob(92233720368
```

---

## Crash 75: `094d3a55ac803740` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068253`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p N
```

---

## Crash 76: `4503579c478e6e58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072275`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q WHERE NOT EXISTS (SELECT * FROM q WHERE TRUE); PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 77: `fcfaabc3e5f66fc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073659`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT X'a0d3Df077d10eb'); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 214748
```

---

## Crash 78: `bce8b0c17a54b470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073747`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308)
```

---

## Crash 79: `2d271a1121747829` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073765`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q LIMIT CURRENT_DATE IS FALSE OFFSET FALSE; PRAGMA quick_check; CREATE VIRTUAL TAB
```

---

## Crash 80: `e505003413996280` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075367`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 81: `81b1b9faff6e46a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075522`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (random()); PRAGMA integrity_check; SELECT printf('%.*s', 9223372036854775807, -0.0); CRE
```

---

## Crash 82: `dc2035a1d1a5c0c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075676`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 83: `021bb1272fd9db01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076103`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (TRUE) UNION VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 84: `1d2d9e5c5f1ea577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076302`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM (VALUES (TRUE) UNION VALUES (CURRENT_TIME)) AS bv LIMIT TRUE; PRAGMA integrity_che
```

---

## Crash 85: `2ba22e339e2d256c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076505`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q NOT INDEXED LIMIT TRUE; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647
```

---

## Crash 86: `0e75cd097bccb3d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076511`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM p LIMIT TRUE; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 87: `692a8c55872d916e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076874`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, a); WITH RECURSIVE q (b, c3, rowid, c1, c3, c3, _rowid_, c3) AS NOT MATERIALIZED (SELECT p.*, 
```

---

## Crash 88: `824d2d049a1911be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077700`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT CURRENT_DATE AS l_sj_2f1r7_9__xr__ih_aj70a0_d_c2c3yeju__d__w2slt_7e3__19_114v_z02_d5___5o886_6x4__11_61_mm8203n335k
```

---

## Crash 89: `95d873fbfec52e3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086730`

```sql
SELECT round(1e308, 1); SELECT substr('', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT *, s.*, * FROM t3 WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED JO
```

---

## Crash 90: `24ce4d755fae8989` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088393`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (CURRENT_DATE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 91: `b05ccb83deac43da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088676`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT X'aD93FCCE', c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 92: `288e16da72891397` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088933`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 REAL); INS
```

---

## Crash 93: `075d3c826072cb41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089326`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT 008412.823616628831921226E-0, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 94: `50c342ba607068ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089388`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT X'f2eF'); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 95: `cffb04c3306a27ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089662`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT 65896); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 96: `57870fe9c5ee24f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089719`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT '71 ', c2 BLOB); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0
```

---

## Crash 97: `1482882bcdac0c81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090209`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 98: `6c6135f35ddae2ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090375`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT X'7B591F0ddFA8', c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -214
```

---

## Crash 99: `9a73142f9b2431a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090493`

```sql
SELECT printf('%.*d', 4294967296, 0.01); SELECT printf('%f', 2147483648, '_6vd8n_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, _rowid_, c1); WITH RECURSIVE p AS NOT MATERIALIZED (SE
```

---

## Crash 100: `f80d790792a09b98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090964`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT CURRENT_TIME, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSE
```

---

## Crash 101: `bd71f1ab18acd017` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091099`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, X'cE4e'); PRAGMA integrity_check; CREATE VIRTUA
```

---

## Crash 102: `909cf6e5e71f9743` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091442`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY)
```

---

## Crash 103: `3b5c689e6a7f1ed3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091600`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 104: `05b807bd8239b894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091610`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PR
```

---

## Crash 105: `563deafaf73d7d43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091724`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p
```

---

## Crash 106: `6b810108c4d1400f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091984`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT substr('-_jg6___3-_', 9223372036854775807
```

---

## Crash 107: `7f23ca35fbc2dd0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096366`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (NOT FALSE IS FALSE COLLATE RTRIM); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 108: `2620e274cd01a5f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096769`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED GROUP BY NULL ORDER BY CURREN
```

---

## Crash 109: `c50e5f1d8778011b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098929`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME LIKE CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 110: `5599547814f1aefa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099417`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT SELECT * FROM q LIMIT -NOT FALSE OFFSET FALSE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 111: `e45372ffbf9b2d2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099607`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT SELECT * FROM q LIMIT -CURRENT_TIMESTAMP OFFSET FALSE; CREATE VIRTUAL TABLE I
```

---

## Crash 112: `042a00a95e9ac743` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099875`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) INTERSECT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); I
```

---

## Crash 113: `0aab9cac83906037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100384`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 114: `0ca8cc328b29c1e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101283`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS (); CREATE VIRTUAL TAB
```

---

## Crash 115: `062ceec502a31fc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105638`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (NULL) EXCEPT VALUES (TRUE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 116: `67b1815a7229ebdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106997`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (CURRENT_TIME), a BOOLEAN DEFAULT ' -'); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); 
```

---

## Crash 117: `f42cc14acc519e7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107551`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (CURRENT_TIMESTAMP / TRUE), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES
```

---

## Crash 118: `6347c0a1e2a2c8e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107777`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (NULL <= CURRENT_TIME)); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE V
```

---

## Crash 119: `3af3ed3fbba4c526` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108098`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (CASE +CURRENT_TIME WHEN CURRENT_TIME THEN TRUE + CURRENT_DATE END), rowid NUMERIC UNIQUE); INSERT INTO q 
```

---

## Crash 120: `0146be4d0ba2cae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109136`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () LIMIT FALSE NOT LIKE CURRENT_TIMESTAMP; PRAGMA quick_check; CREATE VIRT
```

---

## Crash 121: `feb96ee8b85da7f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112315`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (NULL), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIR
```

---

## Crash 122: `cb1b0849b7d64d05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112500`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) DEFAULT X'', rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SEL
```

---

## Crash 123: `649a797cef88a2df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112750`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (TRUE >= TRUE), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CR
```

---

## Crash 124: `40f97e38726e9605` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113229`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BOOLEAN
```

---

## Crash 125: `a3e2553be83d255c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113371`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT round(1e-308, 4294967295); CREA
```

---

## Crash 126: `d2f3d0d41b2ffd3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114277`

```sql
SELECT printf('%.*g', 0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 127: `a9b3d448f3f107aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116737`

```sql
SELECT substr(' 6A-y80_Ju-785', -9223372036854775808, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, c2); INSERT INTO q VALUES (CURRENT_DATE IS DISTINCT FROM CURRENT_TIMESTAM
```

---

## Crash 128: `39252bec8a9fcd32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116809`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (CURRENT_TIME >> FALSE IS FALSE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PL
```

---

## Crash 129: `b7ab88d99a6846f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119605`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a, c2, b) VALUES ((SELECT * LIMIT CURRENT_DATE < CURRENT_TIMESTAMP OFFSET FALSE | RAISE(IGNORE) 
```

---

## Crash 130: `5f7bcccd1702d778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125128`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS N
```

---

## Crash 131: `d80247860c8490b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125510`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS NOT NULL IS N
```

---

## Crash 132: `e3fb962a2a69d141` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125710`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () LIMIT X'c866dafAE483fd' NOT LIKE CURRENT_TIMESTAMP; PRAGMA quick_check;
```

---

## Crash 133: `6305c81ce73b50e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126050`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () LIMIT -0; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 134: `6f8d488eebe2947e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126469`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (CURRENT_TIME), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NO
```

---

## Crash 135: `8e29d0f3b289ed74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126561`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (CURRENT_TIME), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p OR
```

---

## Crash 136: `957255a63743a656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126761`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (TRUE + ~CURRENT_TIMESTAMP), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 137: `83c4f4e2a3765db3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126972`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB CHECK (TRUE + NULL), rowid NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CRE
```

---

## Crash 138: `87756288bd177eb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127065`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (TRUE NOT IN (~NULL))); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VI
```

---

## Crash 139: `ac17834d0d8510e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127221`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (TRUE OR RAISE(IGNORE))); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE 
```

---

## Crash 140: `805b79c52f9b5091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127438`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) CHECK (TRUE NOT IN (~FALSE - CURRENT_TIME))); INSERT INTO q DEFAULT VALUES; VALUES (NULL) UNION SELECT *
```

---

## Crash 141: `db1e81e2dbd7ffc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133142`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (TRUE) UNION VALUES (CURRENT_TIME)); SELECT printf('%.*g', -2
```

---

## Crash 142: `662c4ef4cb901eb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134431`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM (VALUES (TRUE) UNION SELECT * 
```

---

## Crash 143: `9e068a4e8741ae5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134542`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) A
```

---

## Crash 144: `1f1b5acc4baf2f88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135814`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (TRUE) EXCEPT VALUES (CAST(TRUE AS REAL)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 145: `fa029d6695709855` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136403`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (X'') UNION ALL VALUES (CURRENT_DATE) EXCEPT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 146: `7239457b751cf510` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (FALSE) EXCEPT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_)
```

---

## Crash 147: `b86e678ba00c0b57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136530`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (count(*) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_DATE D
```

---

## Crash 148: `624e39c425aecec0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137011`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (count(*) OVER (ORDER BY CURRENT_DATE ASC NULLS LAST ROWS BETWEEN UNBO
```

---

## Crash 149: `2e12640b58e9b66f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (count(*) OVER (PARTITION BY NULL, CURRENT_TIME)); CREATE VIRTUAL TABL
```

---

## Crash 150: `ef8cb07118f9f652` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137442`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (TRUE) EXCEPT VALUES (sum(TRUE) OVER ()); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 151: `4ce145a756e9b8d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137599`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (TRUE) EXCEPT VALUES (count(*) OVER ()); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 152: `a612632177451eff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137619`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES ((VALUES (TRUE)) LIKE count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 153: `3d87ba4e340973dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137861`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (TRUE LIKE count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 154: `60887213d5ac5fcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138182`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (TRUE) EXCEPT VALUES (count(*) OVER () LIKE count(*) OVER ()); SELECT printf('%.*f', 214748
```

---

## Crash 155: `82384184da81f785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138663`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP <= count(*)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 156: `24a6ab8c45269c0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140438`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIMESTAMP, FALSE) EXCEPT SELECT ALL * FROM p NOT INDEXED JOIN q; SELECT prin
```

---

## Crash 157: `8965e95a8d324cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140887`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIMESTAMP / TRUE) EXCEPT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 158: `954a97170f4d08a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142019`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE, a VARCHAR(255) NOT NULL DEFAULT -894554.9); CREATE TABLE IF NOT EXISTS q(c2 DATE PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE, NULL); PRAGMA integrit
```

---

## Crash 159: `7ade169189a1eaca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142522`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY)
```

---

## Crash 160: `a1b16fb07435b411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142676`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY)
```

---

## Crash 161: `5a506bcfb400dc23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144276`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 162: `3661516f9be2a4c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158714`

```sql
SELECT printf('%.*e', -2147483648); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 163: `8ef8798e1548c460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160242`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY EXISTS (SELECT * ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT count(*) OVER (O
```

---

## Crash 164: `697dd4f50a499423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160249`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p CROSS JOIN (SELECT DISTINCT * FROM p NOT INDEXED ORDER BY RAISE(IGNORE) DESC LIMIT NULL OFFSET CURRENT_DAT
```

---

## Crash 165: `6bc0c6aec7405f19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160258`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_TIME HAVING FALSE WINDOW w1 AS () ORDER BY FALSE COLLATE NOCASE ASC, N
```

---

## Crash 166: `c3caa862ced05621` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160266`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE COLLATE NOCASE ASC, CASE WHEN RAISE(IGNORE
```

---

## Crash 167: `068f2d79031d0911` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160279`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (count(DISTINCT CURRENT_TIMESTAMP NOT IN (WITH RECURSIVE t1 AS (VALUES (NULL)) SELECT * FROM q NOT INDEXED))) UNION SELECT * FROM p WHE
```

---

## Crash 168: `24f7e19527746d6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160291`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES ((SELECT *) & RAISE(IGNORE) NOT LIKE RAISE(IGNORE) NOT IN (CURRENT_TIMESTAMP) & CASE CURRENT_DATE << NULL WHEN CURRENT_DATE THEN CURREN
```

---

## Crash 169: `5e97847c129c3198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160303`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS (), w2 AS (ORDER BY EXISTS (VALUES (RAISE(IGNORE)) UNION ALL
```

---

## Crash 170: `b65df4d7c61bc594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160313`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS (PARTITION BY NULL ORDER BY NULL DESC ROWS BETWEEN CURRENT R
```

---

## Crash 171: `ee4cf1e0f97c9484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160324`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY (FALSE) COLLATE NOCASE ASC, NULL DESC; SELECT he
```

---

## Crash 172: `7de1b88f03e7f677` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160337`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY CURRENT_DATE NOT IN (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIME GROUP BY C
```

---

## Crash 173: `53fe62d3d5b69498` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160350`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p NOT INDEXED LEFT JOIN p NATURAL JOIN (p CROSS JOIN (p NOT INDEXED NATURAL JOIN p NOT INDEXED CROSS JOIN p)
```

---

## Crash 174: `266f07da3f42a022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160371`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED ON TRUE WHERE FALSE UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WIN
```

---

## Crash 175: `5dd4acc169ef26a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160379`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE FALSE >> FALSE BETWEEN FALSE || CURRENT_TIMESTAMP AND FALSE GROUP BY NULL WINDOW w1 AS () ORDER BY F
```

---

## Crash 176: `f8ef0051a7c78a77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160399`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CAST(FALSE & +FALSE / TRUE & TRUE NOT BETWEEN NULL AND CURRENT_DATE NOTNULL - CASE RAISE(IGNORE) WHEN CURRENT_TIMESTAMP THEN RAISE(IGN
```

---

## Crash 177: `b5e10db0dfe93f9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160412`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid, c2, a, c1, b, _rowid_); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE COLLATE NOCASE A
```

---

## Crash 178: `72d57b7a2617bcb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160456`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM (p LEFT JOIN t3 AS a USING (rowid, c1)) WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () ORDER BY FALSE COLL
```

---

## Crash 179: `b98916f142a9a608` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160464`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT NOT FALSE NOTNULL || CASE WHEN CURRENT_TIME COLLATE NOCASE THEN CASE WHEN CURRENT_TIME THEN TRUE ELSE ~FALSE END COLLATE BINARY ELSE RA
```

---

## Crash 180: `ce82f522c809b2d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162414`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (~TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 181: `9513f76d82b5c33b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162431`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 182: `a3da35e94deb5290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162647`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM (VALUES (TRUE) UNION SELECT * FROM (VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP)
```

---

## Crash 183: `68c41eee598e5a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163051`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT TRUE); INSERT INTO p VALUES (TRUE) UNION VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1)
```

---

## Crash 184: `608766f11b99d6fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163883`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY
```

---

## Crash 185: `3390549d3caf005f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164092`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2)
```

---

## Crash 186: `9bb82f9752b00492` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165345`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (group_concat(CURRENT_TIME, '') FILTER (WHERE FALSE) OVER (PARTITION BY CURRENT_TIMESTAMP
```

---

## Crash 187: `11d16aa84b631f89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165495`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (count(*) FILTER (WHERE FALSE) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIME
```

---

## Crash 188: `15d05a91b187f27a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165668`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 189: `a9303ec8e91aee1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167582`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT CHECK (CURRENT_TIMESTAMP == NOT CURRENT_DATE MATCH CURRENT_TIMESTAMP NOT NULL), b INTEGER NOT NULL); INSERT INTO 
```

---

## Crash 190: `dfa29b326dd8a63a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167719`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT CHECK (CURRENT_TIMESTAMP == NOT CURRENT_TIMESTAMP), b INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA qui
```

---

## Crash 191: `64fe2fb17d819df1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167725`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT CHECK (CURRENT_TIMESTAMP == NOT CURRENT_DATE MATCH NULL), b INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAG
```

---

## Crash 192: `f93e809053bff5ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170670`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT DISTINCT q.*, (VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT q.* FROM r WHERE FALSE GROUP BY C
```

---

## Crash 193: `885609250f4aebdc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173811`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () UNION VALUES (CURRENT_TIME); PR
```

---

## Crash 194: `80534a6dc7eb3333` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174182`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIME LIMIT TRUE; PRAGMA integrity_check; CREATE VIR
```

---

## Crash 195: `ca797d32ce897ede` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174682`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT OR FAIL INTO p VALUES (-CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 196: `d09c112a827526b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174887`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT DISTINCT NULL AS i786 FROM q NOT INDEXED WHERE CURRENT_DATE LIMIT TRUE; PRAGMA integrity_
```

---

## Crash 197: `eeced4303926cb34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177032`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNIQUE); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () LIMIT FALSE
```

---

## Crash 198: `788f612711ff2345` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180031`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT upper(NULL) AS u6_ FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 199: `06b0bc7cdde6b129` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180206`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT count(*) AS u6_ FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 200: `8bbe243514e6ae13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT count(*) AS u6_ FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 201: `6254d179159b3185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180624`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT group_concat(CURRENT_TIME, '') AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 202: `db84defeafc9e64d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181104`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE s AS (VALUES (RAISE(IGNORE))) SELECT count(DISTINCT CURRENT_TIME) > count(*) AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 203: `83ae44275c780675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182603`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q AS (VALUES (NULL)) SELECT coalesce(TRUE, CURRENT_TIMESTAMP) > CURRENT_TIME AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 204: `08a7e310eca5c4f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183116`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT X'fefCda64C1' IS TRUE AS u6_ FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 205: `1a8bdb53b28a10e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184668`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (min(CURRENT_DATE) OVER ())) SELECT * FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 206: `f346fd63f41a3fe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185572`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT CASE WHEN FALSE THEN TRUE ELSE CURRENT_TIMESTAMP END AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 207: `15c9aaf6a0ecc0bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188302`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT CURRENT_DATE AS l_sj_2f1r7_9__xr__ih_aj70a0_d_c2c3yeju__d__w2slt_7e3__19_114v_z02_d5___5o886_6x4__
```

---

## Crash 208: `04fba203e3aed30f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188476`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELE
```

---

## Crash 209: `822c17c75745fdec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189712`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT ''); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIME DESC NULLS LAST, random() FILTER (WHERE CUR
```

---

## Crash 210: `f082ad26a4bbb91b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190503`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT 033915372015050674264370449284951077581079231959726627385709068815010618984003902638178016526716286881818319346874961404835.771749414898118
```

---

## Crash 211: `d5e8d852c4a933d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198344`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (p.rowid)); CREATE TABLE IF NOT EXISTS q(c3 FLOAT PRIMARY KEY); INSERT OR FAIL INTO p VALUES (TRUE); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIME G
```

---

## Crash 212: `097066c53f46ea5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204305`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT min(CURRENT_DATE) FILTER (WHERE FALSE) AS a FROM (S
```

---

## Crash 213: `c3c3b3f8beaf650d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205980`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT count(*) AS u6_ FROM p WHERE CURRENT
```

---

## Crash 214: `8756c3dbf728e1c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206836`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (trim(FALSE)); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 215: `1db9b7d517314ca7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206922`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (last_insert_rowid()); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 216: `350b35699c23eec1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207202`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t1 NOT INDEXED WHERE CURRENT_DATE GROUP BY TRUE WINDOW w1 AS (PARTITION BY NULL ORDER BY NULL DESC ROWS BETWEEN CUR
```

---

## Crash 217: `2e92fad5f5d7c4e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213338`

```sql
SELECT printf('%.*e', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT VALUES; SELECT *; CREATE TABLE IF NOT EXISTS p(b TEXT, a GENERATED ALWAYS A
```

---

## Crash 218: `f6e8691206e565a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217250`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (SELECT * FROM p WHERE TRUE GROUP BY _rowid_ HAVING FALSE WINDOW w1 AS ())); PRAGMA quick_check; CREATE
```

---

## Crash 219: `0cab241accd2723f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (SELECT * FROM p WHERE TRUE GROUP BY FALSE HAVING FALSE WINDOW w1 AS ())); PRAGMA quick_check; CREATE V
```

---

## Crash 220: `550ab4e89935d2ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217649`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP COLLATE NOCASE) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 221: `0367d66b7235606e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219025`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(CURRENT_DATE))
```

---

## Crash 222: `25cf3ad5b666b9b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220621`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1
```

---

## Crash 223: `9cb35c2787f3fdfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT -12006375.94e3); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 224: `03be9201104f8066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233314`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_DATE)) SELECT CASE WHEN FALSE IS NOT TRUE THEN TRUE ELSE CURRENT_TIMESTAMP END AS u6_ FROM p; CREATE VIRTUAL 
```

---

## Crash 225: `5ae7182dfc8db74c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235706`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT group_concat(X'', 's-') FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS u6_ FROM p; SELECT print
```

---

## Crash 226: `9fafdd839a03e18c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236843`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (count(*) OVER (PARTITION BY NULL ORDER BY NULL ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GROUP
```

---

## Crash 227: `16242f09154e9479` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238685`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE HAVING CURRENT_TIME ORDER B
```

---

## Crash 228: `90706d10a294247c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239039`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p NOT INDEXED ORDER BY CURRENT_TIMESTAMP DESC) SELECT * FROM p; SELECT printf(
```

---

## Crash 229: `cad33e908b439f88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240308`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, c2 FLOAT); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT count(*) AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 230: `e8e4cc71ea62ad1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240920`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q AS (SELECT *) SELECT upper(TRUE) AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VA
```

---

## Crash 231: `930f00dc2e1104fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241432`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT min(CURRENT_DATE) AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 232: `9ad23d81c569e460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241646`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL); WITH RECURSIVE q (b) AS (VALUES (RAISE(IGNORE))) SELECT sum(TRUE) AS u6_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 233: `ccafa986eaad270e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242471`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT X'dEBA'); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 234: `a5472e28bc8739fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249860`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL HAVING NOT EXISTS (SELECT * FROM q NOT INDE
```

---

## Crash 235: `5d1d4f805924e4b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252902`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM q LIMIT CURRENT_TIME % CURRENT_TIME OFFSET TRUE; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 236: `11986f9bdcf6666f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255186`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT OR FAIL INTO p VALUES (hex(random())); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 237: `06e58878dd63b725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255228`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*e', -2147483648, 0.01); CREATE VIRTUAL
```

---

## Crash 238: `5bc2a713fbee5efe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255263`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL); CREATE V
```

---

## Crash 239: `1c7915892eb35798` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255353`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 9223372036854775807, 1e308); CREAT
```

---

## Crash 240: `fe9be4fab9532783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255423`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT X'c866dafAE
```

---

## Crash 241: `4c3eb98579938cc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256296`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (TRUE) UNION VALUES (substr(CURRENT_DATE, NULL)); PRAGMA integrity_check; SELECT printf('
```

---

## Crash 242: `53e97ec42162ed59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256474`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (TRUE) UNION VALUES (total_changes()); PRAGMA integrity_check; SELECT printf('%.*g', -214
```

---

## Crash 243: `2e75ccba92b823bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256541`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p VALUES (TRUE) UNION VALUES (substr(CURRENT_DATE, CURRENT_TIME)); PRAGMA integrity_check; SELECT 
```

---

## Crash 244: `4d520b5af1c4c1f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256584`

```sql
SELECT printf('%llu', -9223372036854775808, 'q'); SELECT printf('%.*f', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE p (c2) AS (SELECT -FALSE IS
```

---

## Crash 245: `9a213b718f8c1e1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256712`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO p SELECT * FROM (VALUES (TRUE) UNION ALL SELECT * FROM p NOT INDEXED) AS bv LIMIT TRUE; PRAGMA int
```

---

## Crash 246: `3689948534a319ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256971`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (~TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL); INSERT INTO 
```

---

## Crash 247: `0d14d879db376ba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257365`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT NULL AS a; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 248: `ce7ae89968911008` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258884`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION SELECT * FROM p WHERE CURRENT_TIMESTAMP NOT IN (VALUES (count(*) OVER (PARTITION BY p.c3 ORDER BY NULL ASC ROWS BETWEEN UN
```

---

## Crash 249: `8b2df5281dc7ccf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259604`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) UNION SELECT NULL AS f4u_4bit ORDER BY NULL DESC NULLS FIRST; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 250: `3629024248383050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260090`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB CHECK (FALSE IN (WITH r AS (VALUES (CURRENT_TIME)) SELECT 
```

---

## Crash 251: `40e11e9994f99912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260952`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE IN (SELECT CURRENT_TIME AS y8w FROM p NOT INDEXED)); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 252: `647d481cdc5fbd9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261000`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE IN (SELECT * FROM p NOT INDEXED)); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3
```

---

## Crash 253: `604b21ff4df2dcd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---
