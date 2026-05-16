# Crash Triage Report

**Total crashes:** 204  
**Unique crash sites:** 204  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 204 | 204 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d627b4c90317ea29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (length(~CURRENT_TIME <> CURRENT_TIMESTAMP LIKE ~CURRENT_TIMESTAMP IS NULL ESCAPE -NULL || ~CURRENT_DATE * CURREN
```

---

## Crash 2: `caa893b0d544e512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000074`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, b); SELECT CASE FALSE >= CURRENT_DATE NOT NULL WHEN +NULL THEN NOT FALSE << CURRENT_DATE OR ~FALSE COLLATE RTRIM || hex(NULL IS NULL) COLLAT
```

---

## Crash 3: `65034a723931a040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001115`

```sql
SELECT printf('%.*f', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r VALUES (CURRENT_TIME) RETURNING q.*; SELECT CASE WHEN RAISE(IGNORE) NOTNULL
```

---

## Crash 4: `e002ad6cd45f6904` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001201`

```sql
SELECT substr('L6_', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, b); REPLACE INTO q VALUES (FALSE ISNULL != CURRENT_TIME NOT IN (count(*)) < CURRENT_DATE | CURRENT_TIME 
```

---

## Crash 5: `ff172f49f169aa90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001230`

```sql
SELECT printf('%.*f', 2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT CURRENT_TIME | TRUE OR X'dDCce4CcBAEd53' AND FALSE NOT BETWEEN NULL AND RAISE(IGNORE) FROM (
```

---

## Crash 6: `bf8abdfe9e2f3593` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001718`

```sql
SELECT substr('6', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO q VALUES (CURRENT_TIMESTAMP BETWEEN CURRENT_DATE + RAISE(IGNORE) COLLATE RTRIM AND ty
```

---

## Crash 7: `4e140c24fb62accc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001998`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (c2, c3) VALUES (NULL = FALSE > NOT +~count(DISTINCT TRUE IN (CURRENT_TIME)) FILTER (WHERE RAISE(IGNORE
```

---

## Crash 8: `689a6af8e9f361ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002215`

```sql
SELECT round(1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZE t3;
```

---

## Crash 9: `5c325fc9069f3ad1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002281`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (a, c1, a) VALUES (+CURRENT_DATE != count(*) =
```

---

## Crash 10: `33e76841fd91884a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002306`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PL
```

---

## Crash 11: `58ccb616ff4b48e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002468`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, rowid GENERATED ALWAYS AS (a) , b VARCHAR(255) NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 12: `991bbc5876546020` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002481`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (-054066442877939073543047253860.779022507434911369596878852634942361029598990
```

---

## Crash 13: `61ff92c6837f8be3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002578`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, t2.*, *, * FROM (SELE
```

---

## Crash 14: `fb9aaa933af393bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003703`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURS
```

---

## Crash 15: `ffba69582ebfc271` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004217`

```sql
SELECT printf('%.*g', 9223372036854775807, 0.01); SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO r VALUES (CASE CASE CASE WHEN NULL THEN RAI
```

---

## Crash 16: `a7308f38c0f0698e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006454`

```sql
SELECT printf('%.*s', 0, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO q VALUES (CAST(CURRENT_DATE IS NOT NULL + CASE RAISE(IGNORE) WHEN NULL + RAISE(IGNORE) TH
```

---

## Crash 17: `31f08574da36cd81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006928`

```sql
SELECT substr(' 1arT-16O_r Tq24-5', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO q VALUES (CASE CURRENT_TIMESTAMP NOT NULL WHEN -NULL = CURRENT_DATE NOT
```

---

## Crash 18: `cacae8817fe08340` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007165`

```sql
SELECT substr('C-NUf- r4 __ X_', 4294967296, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_DATE - CURRENT_DATE, r.* FROM t2 WHERE EXISTS (SELECT ALL ifnull(FAL
```

---

## Crash 19: `975829d157fc752e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008308`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO p VALUES (CASE WHEN (SELECT *, *) >> CURRENT_DATE - CASE WHEN FALSE THEN CURRENT_DATE ELSE CURRENT_DATE 
```

---

## Crash 20: `7bb9e1048da3b4a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008577`

```sql
SELECT round(-1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); INSERT INTO t3 (b) VALUES ((VALUES (TRUE)) IS CURRENT_TIME, max(NOT RAISE(IGNORE)) FILTER (WHERE CURRENT_
```

---

## Crash 21: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008608`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 22: `22e71c7ee890f44d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008700`

```sql
SELECT printf('%.*d', -2147483649, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); SELECT NULL NOTNULL IS TRUE AND NULL <= CURRENT_TIMESTAMP / CURRENT_DATE AND TRUE - FALSE == RAISE(
```

---

## Crash 23: `4a4a292f2e407102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008921`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CASE WHEN count(FALSE IS last_insert_rowid() IN (SELECT *)) ISNULL THEN CUR
```

---

## Crash 24: `3e9e3a371470b004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011470`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, c2); S
```

---

## Crash 25: `fe6d2a5a5bec8426` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011545`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 26: `ecd0da300e9bc721` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011561`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 27: `ab017a00fd9e05ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011575`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 28: `5be2abd92f3e3a52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011593`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 29: `83a95cdde87802b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011602`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 30: `065862c9b887a569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011613`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a TEXT); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 31: `88638796be507e00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012046`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, 
```

---

## Crash 32: `43b71ba9fe87985f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012181`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); SELECT * FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUES (TRUE <> CURRENT_TIMES
```

---

## Crash 33: `51c0b39354f1bc1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012823`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); E
```

---

## Crash 34: `6804a8c9b4b77c46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013923`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c3 INT DEFAULT FALSE); SELECT DISTINCT q.* FROM q INDEXED BY c3 OR
```

---

## Crash 35: `3c3a70341107c6ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018135`

```sql
SELECT round(1.0, 2147483648); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 36: `bf26e17707a46bfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE LIKE CURRENT_DATE, TRUE, TRUE); EXPLAIN QUER
```

---

## Crash 37: `0ece3124116bdf93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019986`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, TRUE, TRUE); EXPLAIN QUERY PLAN VALUES (CUR
```

---

## Crash 38: `3108050a4f930f44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020094`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME, TRUE, TRUE); EXPLAIN QUERY PLAN VA
```

---

## Crash 39: `241826bd9cb3d729` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021377`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b INT CHECK (NULL)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (json(FALSE), TRUE, CURRENT_TIME); EXPLAIN QUERY 
```

---

## Crash 40: `fa00e0487edfa780` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021642`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (json(FALSE), TRUE, CURRENT_TIME); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 41: `fd3e43e60bf23b6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (random(), TRUE, CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 42: `3e67aed8e883c1b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021975`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME >= CURRENT_TIME COLLATE RTRIM, TRU
```

---

## Crash 43: `cfc5c81bbd37c150` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022622`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, NULL); VALUES (CURRENT_DATE); SEL
```

---

## Crash 44: `d68d08709c0cf5c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022911`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, FALSE); VALUES (CURRENT_DATE); SE
```

---

## Crash 45: `cc646b87f612d792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027022`

```sql
SELECT round(-1e308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 46: `cfa6bd84106eaafe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027403`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (FALSE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 47: `aff790b4f234e8d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031886`

```sql
SELECT printf('%f', 4294967296, '-E'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (last_insert_rowid(), TRUE, CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CU
```

---

## Crash 48: `ac96f49445853615` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034653`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO q VALUES (CASE WHEN changes() THEN NULL ELSE abs(NULL) FILTER (WHERE CURRENT_TIME
```

---

## Crash 49: `ca4e868dbc1b923c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038556`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (last_insert_rowid(), TRUE, CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_D
```

---

## Crash 50: `c3048057e2307fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042264`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 51: `466f1ea875418cdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042303`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT 8.1157e836927); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *;
```

---

## Crash 52: `0c6e9d8cc532951f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044968`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, rowid GENERATED ALWAYS AS (a) , b VARCHAR(255) NOT NULL); WITH RECURSIVE p (a) AS (VALUES (CURRENT_TIME)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 53: `e849247691732910` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050992`

```sql
SELECT printf('%llu', -2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 VALUES (p.b <= CURRENT_TIMESTAMP || CASE WHEN CURRENT_DATE - CURRENT_TIME THEN ifnull(T
```

---

## Crash 54: `bff1e2a4bf2adde4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051068`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2); INSERT OR REPLACE INTO p VALUES (+EXISTS (SELECT q.* FROM p WHERE +'V-z _ G t_-w125__-' GROUP BY NU
```

---

## Crash 55: `fb61df33590deafd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052608`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); EXPLAIN QUERY PLAN WITH q AS (VALUES (RAISE(IGNORE))) VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); VALUES (CURRENT_TIME);
```

---

## Crash 56: `e6355a14edefe762` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052648`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT TRUE, a VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); EXPLAIN QUERY PLAN WITH q AS (VALUES (RAISE(IGNORE))) VALUES (NULL); CRE
```

---

## Crash 57: `eeef54fedcf19fb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054600`

```sql
SELECT substr('-t04Ls_- ', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, TRUE, CURRENT_TIME); EXPLAIN Q
```

---

## Crash 58: `e9105837492d2e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054670`

```sql
SELECT substr('-t04Ls_- ', 9223372036854775807, 2147483648); SELECT substr('-_S_7-', 4294967295, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT INTO p VALUES (CASE WHEN CURR
```

---

## Crash 59: `cc2c343ef5f6c413` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056862`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE OR NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPL
```

---

## Crash 60: `e50db139af053f2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057024`

```sql
SELECT printf('%.*g', 1, 1e-308); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 61: `e248c0aead8259d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057687`

```sql
SELECT printf('%.*d', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (hex(p.c1 + (FALSE) IS c2 | (CURRENT_DATE) + CURRENT_DATE GLOB CURRENT_TIMESTAMP & CURRENT_DATE NOTNU
```

---

## Crash 62: `5eb648f36656f38a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061661`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, rowid GENERATED ALWAYS AS (a) , b VARCHAR(255) NOT NULL); WITH RECURSIVE p (b) AS (VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('
```

---

## Crash 63: `2fc12b188aef8f2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061869`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p (b) AS (VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 64: `111655f713f01fd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073486`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS WITH t1 AS (VALUES (CURRENT_TIME)), p (c3) AS (VALUES (TRUE)) VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA q
```

---

## Crash 65: `9f05704c9fe904c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073518`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 66: `0affe07ba0e42aa1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073548`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT 9.6, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 67: `113e9099d1640b51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073705`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 68: `eced509804bdacb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084481`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); SELECT * FROM (SELECT * FROM p WHERE FALSE | TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VALUES (NULL CO
```

---

## Crash 69: `132307f8fd005007` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084516`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VALUES (NULL COLLATE NO
```

---

## Crash 70: `819506e8ea498da6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084983`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT ' 4 30v61_-G11'); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 71: `de234b04d342f8c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085117`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 72: `83e629f9a5475dcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085124`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT TRUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 73: `a9fd03eed5ce762a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087558`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p SELECT FALSE AS y; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (last_insert_rowid(
```

---

## Crash 74: `dc19460ace050666` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088039`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (last_i
```

---

## Crash 75: `acc1bf675c2cf906` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089301`

```sql
SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY, a INTEGER DEFAULT
```

---

## Crash 76: `f92fbbd799d4302e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089549`

```sql
SELECT printf('%.*s', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p (c2, _rowid_, c2) AS NOT MATERIALIZED (SELECT DISTINCT CURRENT_DATE AS y5 FROM q WHERE -N
```

---

## Crash 77: `dc47eceb5662ed3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095207`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 78: `55f4c0e69e260658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095842`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT V
```

---

## Crash 79: `e4fd46711c2ee6bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095853`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT V
```

---

## Crash 80: `30af6510b8749e16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096100`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WH
```

---

## Crash 81: `411dbe0b86b7b36d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096690`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE >= CURRENT_TIME COLLATE RTRIM, TRU
```

---

## Crash 82: `50e9cf7c3aa29db9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096878`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE COLLATE RTRIM, TRUE, CURRENT_TIME)
```

---

## Crash 83: `f8641cb591eac224` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097929`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c3 GENERATED ALWAYS AS (a) UNIQUE); SELECT ~NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 84: `ad9744a8cb87d38f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098404`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE, c2 TEXT PRIMARY KEY, c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, CURRENT_TIME); E
```

---

## Crash 85: `45f189639427812a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 86: `5efebf5c6930ce1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 87: `6682288e2df9ef81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098687`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 88: `bfeeea7b3a4c6f22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099500`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, c3 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (TRUE || CURRENT_TIMESTAMP, TRUE, TRUE);
```

---

## Crash 89: `f4d9c3280cce0ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100195`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (X'aBde' AND CURRENT_DATE, TRUE, TRUE); EXPLAIN QUERY
```

---

## Crash 90: `2990819c7430b585` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100466`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL AND CURRENT_DATE, TRUE, TRUE); EXPLAIN QUERY PL
```

---

## Crash 91: `dc1323998a9be760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101145`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE LIKE CURRENT_DATE, TRUE, TRUE); EXPLAIN QUER
```

---

## Crash 92: `fab1ed0df9b35cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101184`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, TRUE, TRUE); EXPLAIN QUERY PLAN VALUES (CUR
```

---

## Crash 93: `82f5b55acbb063f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101819`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (FALSE, TRUE, TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DA
```

---

## Crash 94: `4bbfcf92d7ebb03a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102814`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, EXISTS (VALUES (RAISE(IGNORE)
```

---

## Crash 95: `be9f8686ab2d1c77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103081`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*f', 2147483
```

---

## Crash 96: `3e15d2be0617f38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107019`

```sql
SELECT printf('%x', -2147483649, '_ 8O ---b- s-_-q_'); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 97: `79583bcff2bc437d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115359`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT BETWEEN CURRENT_TIMESTAMP AND TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 98: `cecba0432e5b1cc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116138`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE & CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 99: `83b4b6cd32360d66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP); PRAGMA integrity_check; SELEC
```

---

## Crash 100: `6d04e65d2386b723` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117257`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURR
```

---

## Crash 101: `42aac81ed65c3ce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118044`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME * -CURRENT_DATE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 102: `f7b6c5f28df01d84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118522`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE * NULL NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE); PRAGMA quick_check; SELEC
```

---

## Crash 103: `d6353824cf826e9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119167`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME * json(FALSE)); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 104: `e8dad51f622926d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119336`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME * last_insert_rowid()); PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 105: `98840715446251ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119401`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT '-9'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 106: `4a5184d4ac97ba2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119522`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 107: `495f526005c421d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129763`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * CURRENT_TIMEST
```

---

## Crash 108: `e3e9dcdb1920eb35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129937`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE * -CURRENT_DATE * CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 109: `15e18429a565847d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129945`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * CURRENT_TIMESTAMP); PRA
```

---

## Crash 110: `5225b80c31c61809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129952`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-CURRENT_DATE * -CURRENT_DATE * FALSE * -CURRENT_DATE * -CURRENT_DATE * CURRENT_TIMESTAMP); PR
```

---

## Crash 111: `55487345f5497a22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130006`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (-CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE * -CURRENT_DATE)
```

---

## Crash 112: `ce431878ef030d4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141196`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, TRUE, CURRENT_TIMESTAMP); S
```

---

## Crash 113: `654b52370cd36b4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141258`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, TRUE, CURRENT_TIMESTAMP); S
```

---

## Crash 114: `9416f0901e8b1026` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141884`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE, TRUE, lower(TRUE)); EXPLAIN QUERY PLAN VALU
```

---

## Crash 115: `dcef2dc59fc70794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141955`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 116: `8b21a21f0ffb4924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142763`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME AND X'aBde', TRUE, TRUE); EXPLAIN QUERY
```

---

## Crash 117: `0979ec2162088e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143885`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c3 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p (rowid, rowid) VALUES (NULL, FALSE) ON CONFLICT(c3) DO UPDATE SET c1 =
```

---

## Crash 118: `d4055201b06f1067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144831`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 119: `3aaac666ddb46352` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149902`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; SELECT group_concat(CURRENT_TIME) OVER (PARTITION BY CURRENT
```

---

## Crash 120: `dc956bca8b59e8b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151891`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE RTRIM LIKE CURRENT_TIME IS NOT NULL 
```

---

## Crash 121: `737315cf352c0091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, TRUE, FALSE); SELECT DISTINCT * FROM p
```

---

## Crash 122: `c0af0231ccd09ddf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE RTRIM LIKE NULL, TRUE, FALSE); SELEC
```

---

## Crash 123: `580033b3a5ee9916` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152109`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME COLLATE RTRIM LIKE FALSE >= FALSE, TRUE, FAL
```

---

## Crash 124: `3c6e07bc34366aea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152767`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); VALUES (CURRENT_DATE) UNION ALL SELECT -5.42470038687435735639644471562875090872557553394660337029020396490664442646392393776067148e173 IN (NULL, TRUE, NULL) AS 
```

---

## Crash 125: `cc845d4c1f5349da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152821`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); VALUES (CURRENT_DATE) UNION ALL SELECT CURRENT_DATE IN (NULL, TRUE, NULL) AS y; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT s.*, co
```

---

## Crash 126: `1b3c92e7d09835ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152827`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); VALUES (CURRENT_DATE) UNION ALL SELECT TRUE IN (NULL, TRUE, NULL) AS y; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT s.*, count(NOT 
```

---

## Crash 127: `0f7716f0d0c1df09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152833`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); VALUES (CURRENT_DATE) UNION ALL SELECT -5.42470038687435735639644471562875090872557553394660337029020396490664442646392393776067148e173 IN (CURRENT_TIME) AS y; C
```

---

## Crash 128: `98896f718f0b8f86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152839`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); VALUES (CURRENT_DATE) UNION ALL SELECT -5.42470038687435735639644471562875090872557553394660337029020396490664442646392393776067148e173 IN (NULL, CURRENT_DATE) A
```

---

## Crash 129: `3e0de89ae1c84672` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159464`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p SELECT DISTINCT * FROM p; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 130: `a893d9e805ff1451` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160402`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (CURRENT_TIME) UNION SELECT CURRENT_TIMESTAMP COLLATE NOCASE AS y ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST; PRAGMA integrity_check; CREATE
```

---

## Crash 131: `2fc8663deff82700` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160892`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (CURRENT_TIME) UNION SELECT TRUE AS y ORDER BY CURRENT_TIME DESC NULLS FIRST; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 132: `26c32587143e01c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162527`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 133: `7aa1b989f1d60e56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163628`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); SELECT * FROM (SELECT * FROM p WHERE FALSE IN (SELECT * FROM p GROUP BY TRUE INTERSECT VALUES (NULL))) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 134: `bf4b8aa6579dc419` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165143`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME > CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE
```

---

## Crash 135: `bc748a91f3f404e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165318`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (NULL
```

---

## Crash 136: `4f0332f7115ac590` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192170`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); SELECT count(*) FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY FALSE ORDER BY RAISE(IGNORE) ASC NULLS LAST LIMIT CURRENT_DATE); CREAT
```

---

## Crash 137: `9927b1f9004327f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192373`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); SELECT count(DISTINCT NULL) FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p 
```

---

## Crash 138: `2d6bd99abea08b2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193399`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT count(*) OVER () AS cezf7bv2 ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST LIMIT CURRENT_DATE); CREATE VIRTUAL
```

---

## Crash 139: `00628505fd6aa999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194879`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, rowid GENERATED ALWAYS AS (a) , b VARCHAR(255) NOT NULL); WITH RECURSIVE p (b) AS (VALUES (TRUE) EXCEPT VALUES (CURRENT_DATE)) SELECT * FROM p; CREATE VIRTUAL TAB
```

---

## Crash 140: `4b7579dfc2f452d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205488`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308)
```

---

## Crash 141: `8cf45ef3f5f8b88f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205731`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, _rowid_ FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 142: `94abfd57bae7af16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207562`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME NOT IN (NULL, TRUE))); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); VALUES (CURREN
```

---

## Crash 143: `bc91068e91f500d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207599`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) CHECK (CURRENT_TIME LIKE NULL ESCAPE FALSE OR NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 144: `70e38510c59efa6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207607`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT CURREN
```

---

## Crash 145: `45a6f7489d611646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207633`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, c2 BLOB NOT NULL); EXPLAIN QUERY PLAN WITH q AS (VALUES (RAISE(IGNORE))) VALUES (NULL); CREATE VIRTUAL TABLE IF N
```

---

## Crash 146: `c456854385bc2085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208516`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 147: `ca3a0e8da247403b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211684`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) CHECK (quote(FALSE) IN (FALSE IN (NULL, TRUE, NULL), FALSE))); INSERT INTO q DEFAULT VALUES; VALUES (CURR
```

---

## Crash 148: `6ecab77fa898ff88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211774`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) CHECK (quote(CURRENT_TIMESTAMP) IN (FALSE IN (NULL, TRUE, NULL), FALSE))); INSERT INTO q DEFAULT VALUES; 
```

---

## Crash 149: `61c7f0027ca2c606` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212218`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT, c1 REAL GENERATED ALWAYS AS (~RAISE(IGNORE)) STORED); EXPLAIN QUERY PLAN WITH q AS (VALUES (RAISE(IGNORE))) VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 150: `d636b9514464c1ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212237`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t3 LEFT JOIN p INDEXED BY b NATURAL LEFT JOIN p NOT INDEXED UNION SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 151: `de9f59e625de21fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224762`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, a GENERATED ALWAYS AS (a) UNIQUE); WITH RECURSIVE p (c2, a) AS (VALUES (CURRENT_TIME, X'aBde')) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 152: `5c532585754b831f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228645`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); SELECT min(_rowid_) FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO
```

---

## Crash 153: `ae534f4f932c4cac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228754`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); SELECT min(CURRENT_TIMESTAMP) FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR RE
```

---

## Crash 154: `57a26bcf6cda8025` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231229`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (min(+CAST(CURRENT_DATE AS BLOB))); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 155: `bda6c162f1ba0c85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231416`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (min(+TRUE)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 156: `e82d274239de9958` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231668`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (min(NULL)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 157: `a69080cb51cebe97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231861`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (total_changes()); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 158: `cc4aa1e6b934b4d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231878`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (NOT X'Cc9547'); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 159: `2e7648ea131468d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232057`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (NOT CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 160: `ab2b0c90d957b9e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232166`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (char(CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE TABLE IF N
```

---

## Crash 161: `90de2cdc06354b06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232271`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS
```

---

## Crash 162: `2e4d7e6818aaaf7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232764`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (count(DISTINCT NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a, c1, b, a, b, c1) VALUES (avg(FALSE <> 
```

---

## Crash 163: `e21af664a67bf4b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232838`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY); VALUES (count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (a, c1, b, a, b, c1) VALUES (avg(FALSE <> FALSE % RAIS
```

---

## Crash 164: `20f48676d9ae5ec7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252060`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (''); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NOT b; SELECT pr
```

---

## Crash 165: `9515ed80b881756f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252223`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NOT b; SELECT 
```

---

## Crash 166: `8aa42b771070a0c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252729`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); VALUES (FALSE <= +TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS MATERIALIZED (VALUES ((CURRENT_DATE))) INSERT 
```

---

## Crash 167: `7b86924be1bebc5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257318`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME NOT IN (NULL, 42422827902859375271151070311359067906818539.886696825006127199918097392730, FALSE))); INSERT INTO p DEFAULT VALUES; VALUES (FALSE
```

---

## Crash 168: `49aec791ec7acf0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257454`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME NOT IN (NULL, CURRENT_DATE, FALSE))); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 169: `ad7d4bfd71a66a94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257815`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (CURRENT_TIME NOT IN (NULL, X'', FALSE))); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR RE
```

---

## Crash 170: `bbfd819979237126` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257927`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (last_insert_r
```

---

## Crash 171: `4085a9e5dc792ac3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258398`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; SELECT * FROM p AS a NATURAL LEFT JOIN p NOT INDEXED GROUP BY TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 172: `669c0f861296005c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259110`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT X'ACb7d0Ac'); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP > c1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 173: `545ce1ecd1d6a4c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259684`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); SELECT * FROM (SELECT * FROM p WHERE FALSE IN (SELECT * FROM p AS a NATURAL LEFT JOIN p NOT INDEXED GROUP BY TRUE INTERSECT VALUES (NULL))) AS sub1; CREATE VIR
```

---

## Crash 174: `174dc04643007aaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259760`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); SELECT * FROM (SELECT * FROM p WHERE FALSE IN (VALUES (CURRENT_DATE))) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 (c2) V
```

---

## Crash 175: `a9472b3d8020bd86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260560`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (json(TRUE)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT substr
```

---

## Crash 176: `baaa4298e8a77b10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261776`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) CHECK (CURRENT_TIME LIKE NULL ESCAPE NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 177: `c09a141972c6ffc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262708`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (CURRENT_TIME) UNION SELECT * FROM p GROUP BY TRUE ORDER BY CURRENT_TIME COLLATE NOCASE ASC NULLS FIRST; PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 178: `0fb73e95e7aeef8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262914`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (CURRENT_TIME) UNION SELECT TRUE AS y ORDER BY TRUE COLLATE NOCASE COLLATE NOCASE ASC NULLS FIRST; PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 179: `4b9de77de99ac971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263623`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p VALUES (CURRENT_TIME) UNION SELECT CURRENT_TIMESTAMP AS y ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST; PRAGMA integrity_check; CREATE TABLE IF NOT E
```

---

## Crash 180: `be656c9fd27ed49f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p SELECT ALL FALSE FROM p; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 181: `fc310c6f20c81473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264221`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p SELECT ALL * FROM p; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 182: `8b84d7baf536f5a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264447`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); INSERT INTO p SELECT DISTINCT * FROM p NATURAL JOIN p NATURAL LEFT JOIN p; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 183: `123b186999768eda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000273702`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, rowid INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP, TRUE, FALSE); SELECT DISTINCT *, *, *,
```

---

## Crash 184: `ad234f24896b3ffb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274906`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_TI
```

---

## Crash 185: `a51075998811d191` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275385`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a REAL N
```

---

## Crash 186: `32efa80000fce03a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000276511`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, FALSE); SELECT group_concat(CURRE
```

---

## Crash 187: `bb16609b84465716` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277035`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) GENERATED ALWAYS AS (NULL) STORED, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURR
```

---

## Crash 188: `b65840f3a35c4cef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277157`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 189: `4bfe5436aa53e644` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277476`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 INTEGER DEFAULT ' '); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 190: `92706a5b7234fbbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000277986`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, NULL, FALSE); VALUES (CURRENT_DATE); CR
```

---

## Crash 191: `8603ddee7172ee86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000278513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, CURRENT_TIME * CURRENT_TIME *
```

---

## Crash 192: `30a735eb19648746` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279366`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE, c2 NUMERIC, a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (NULL, TRUE, FALSE); VALUES (CURRENT_DATE)
```

---

## Crash 193: `090756833477770e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279843`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (FALSE IS TRUE COLLATE RTRIM, TRUE, CURRENT_TIME
```

---

## Crash 194: `4570f0cfa17e7863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279999`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE >= CURRENT_TIME || CURRENT_TIME CO
```

---

## Crash 195: `d5af6af547a00209` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000281393`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b INT CHECK (CURRENT_TIMESTAMP != CURRENT_TIME)); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (FALSE, TRUE, CURREN
```

---

## Crash 196: `45d8488bd566aa45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000282350`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 197: `7a9a656b2a0f1da7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000282447`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, _rowid_ INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE
```

---

## Crash 198: `e608ac7293db8289` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000285782`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c3 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY NUL
```

---

## Crash 199: `d1448875dab9d056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286269`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, b FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME AND 0, TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DA
```

---

## Crash 200: `95ed5122af7c711d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286705`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 201: `b771e08b0259e960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000286773`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 202: `99738f50a20c734a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000287389`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE, c2 NUMERIC, a INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (FALSE, TRUE, TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_D
```

---

## Crash 203: `d77e0a85d915148d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000288203`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (total_changes(), TRUE, CURRENT_TIMESTAMP); SELECT * FROM (SEL
```

---

## Crash 204: `fcf51be7057f8568` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000288386`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE, c2 NUMERIC, b INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT OR REPLACE INTO p VALUES (total_changes(), TRUE, CURRENT_TIMESTAMP); SELECT * FROM (SEL
```

---
