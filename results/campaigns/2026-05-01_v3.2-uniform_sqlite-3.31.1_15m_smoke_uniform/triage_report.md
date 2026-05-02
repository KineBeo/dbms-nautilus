# Crash Triage Report

**Total crashes:** 112  
**Unique crash sites:** 112  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 112 | 112 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `8f01946abbcac8c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000138`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(c2 BLOB, c3 GENERATED ALWAYS AS (a = -372) UNIQUE, c1 VARCHAR(255) NOT NULL DEFAULT X'B8f'); INSERT INTO p (a, c1) VALUES (TRUE 
```

---

## Crash 2: `374604095a19677f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000166`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c1, a); INSERT OR FAIL INTO p VALUES (CASE WHEN CURRENT_DATE GLOB NULL || FALSE NOTNULL THEN hex(+NULL REGEXP FALSE NOT BETWEEN CURRENT_DATE
```

---

## Crash 3: `0a82f5345e91ca3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000172`

```sql
SELECT substr('x', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM q NATURAL JOIN t2 WHERE NULL NOT NULL; CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT CUR
```

---

## Crash 4: `f90e7bbd732fa359` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000359`

```sql
SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2); REPLACE INTO s VALUES (+NULL NOT LIKE FALSE & CURRENT_TIMESTAMP * CURRENT_DATE GLOB CURRENT_TIME * RAISE
```

---

## Crash 5: `70393dfa24eb2823` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000657`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q (rowid, rowid) AS (SELECT CURRENT_TIMESTAMP) INSERT INTO s VALUES (NULL ISNULL == NULL IS NULL ISNULL
```

---

## Crash 6: `25f4f11b196f4cda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000786`

```sql
SELECT round(1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO p VALUES ((RAISE(IGNORE))); SELECT *, *, * FROM (SELECT CURRENT_TIMESTAMP FROM q WHERE 
```

---

## Crash 7: `4a5fd82e7e7bcbb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001353`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c1, c3); REPLACE INTO r VALUES (TRUE >> CURRENT_TIME AND ~NULL NOTNULL | CURRENT_DATE MATCH NULL MA
```

---

## Crash 8: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001513`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 9: `f5f6300bce6d5d04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002215`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a) ); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO q VALUES (abs(
```

---

## Crash 10: `04ebe6e2cfc12cca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002713`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick
```

---

## Crash 11: `250d23f8b55d0c6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002916`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT hex(CURRENT_DATE) FILTER (WHERE +CASE (CUR
```

---

## Crash 12: `1a71cd385f953a9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002966`

```sql
SELECT substr('__ --YVi775__8', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT p.*, -CURRENT_TIME % NULL AS y6 FROM p WHERE EXISTS (SELECT *, * FROM p NATURAL JOIN q WHER
```

---

## Crash 13: `ff11e423757fc32a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004155`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT I
```

---

## Crash 14: `1c029d7b921f7d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 15: `9db72ad56d78d897` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004208`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES ((VALUES (CURRENT_TIMESTAMP))); VALUES (~RAISE(IGNORE), CASE CURRENT_TIME WHEN NULL T
```

---

## Crash 16: `0b09d372d3f66099` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005578`

```sql
SELECT printf('%s', -1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT +EXISTS (SELECT t2.* ORDER BY NULL IS NULL NOTNULL ASC NULLS FIRST, CURRENT_TIME ASC NULLS FIRST) ->> RAIS
```

---

## Crash 17: `621717ee0778c600` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005605`

```sql
SELECT printf('%.*g', -2147483648, 1e308); SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT TRUE * +CURRENT_TIME IS NULL <> CURRENT_DATE MAT
```

---

## Crash 18: `5b9a4adbf40ca5e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006353`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT NULL AS nhl_6654__n3uf90 FROM p NATURAL JOIN p WHERE ifnull(CAST((CURRENT_DATE LIKE last_insert_rowid()) LIKE R
```

---

## Crash 19: `bfda0d0a4524d4ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007022`

```sql
SELECT printf('%d', -2147483649, '_1K--I__Buse-2-   _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO t2 VALUES (NULL NOT NULL, CURRENT_DATE); ANALYZE q; CREATE VI
```

---

## Crash 20: `a47517522bf714b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007283`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, a, c1, _rowid_, c2); WITH RECURSIVE t3 (c1, c2) AS (SELECT NOT TRUE == CURRENT_TIME IN (SELECT *) IS NOT NULL AS rs4v4_25_k1__78q___b_i
```

---

## Crash 21: `eaa77372b6813b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007422`

```sql
SELECT printf('%.*g', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIMESTAMP IS NULL != total_changes() > RAISE(IGNORE) NOT NULL); 
```

---

## Crash 22: `c7e30975c8b03544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017251`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 
```

---

## Crash 23: `2be63cee029f116e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017773`

```sql
SELECT round(-1e308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT -CASE WHEN NULL THEN FALSE ELSE CURRENT_TIME << CURRENT_TIME END / a > NOT TRUE IS NOT NULL 
```

---

## Crash 24: `113c19f2ea1218ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018134`

```sql
SELECT substr('7A0SK_79QnIC_ k_- -', 2147483648, 9223372036854775807); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO r VALUES
```

---

## Crash 25: `2cb20498ff2b08d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018195`

```sql
SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_DATE & RAISE(IGNORE) AS bl0_lz06_js_ FROM (
```

---

## Crash 26: `5ae53e0f163019e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018242`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB NOT NULL); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 27: `fe9bf77bc95f1f81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019674`

```sql
SELECT printf('%.*g', -2147483648, 1e308); SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO q VALUES (CASE WHEN FALSE AND +CURRENT_DATE <> FALSE
```

---

## Crash 28: `40fd444f65dc395c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020971`

```sql
SELECT substr('- 38 ', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 29: `43a6f7f3bda83908` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021586`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT); INSERT OR ABORT INTO p VALUES (TRUE); VALUES (NULL); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 30: `2a502f550c3889c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022223`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 31: `1f2b76f078c70d2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022346`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE I
```

---

## Crash 32: `a4ab6a92d0de5073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022406`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE VIEW 
```

---

## Crash 33: `d2b58e031004eeda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024471`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 34: `d43754fab9b1f5bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024598`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%.*g', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); SELECT q.* FROM (SELECT RAISE(IGNORE) & FALSE COLLATE BINARY + CURRENT_TIMESTAMP L
```

---

## Crash 35: `d2102dcfa6a90fbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026040`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT NULL IS CURRENT_DATE FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 36: `28e66232995ac3cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029983`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NO
```

---

## Crash 37: `0f87997787982576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030429`

```sql
SELECT round(-1.0, 4294967295); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 38: `01afa656111b1592` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031550`

```sql
SELECT printf('%.*s', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT +CASE ~TRUE IS NULL IS NOT DISTINCT FROM -RAISE(IGNORE) != RAISE(IGNORE) LIKE CURRENT_DATE -> FALSE 
```

---

## Crash 39: `af84237326658e07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031706`

```sql
SELECT printf('%.*f', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); INSERT INTO s DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 40: `81e03fcc63729900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032288`

```sql
SELECT printf('%.*d', 2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, b, c3); EXPLAIN QUERY PLAN SELECT -CASE WHEN CURRENT_TIMESTAMP ISNULL * FALSE >= CURRENT_TIMESTAMP
```

---

## Crash 41: `8b21f1860ab283f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032595`

```sql
SELECT substr('d_ Ec_hP-S', -1, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT round(1.0, 1); CREATE TABLE IF
```

---

## Crash 42: `d3d4e956521ba238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033943`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 43: `2ed5be91c2bfc78b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036641`

```sql
SELECT printf('%.*s', 9223372036854775807, -1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 44: `d6216ebeb4f7e69d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037356`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 45: `34c5f16e1d5ba053` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038511`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT TRUE <> FALSE LIKE NULL ESCAPE FALSE AS j_ds_44_f_1d_3_7_39v_4__ek_ FROM q WHERE EXISTS (VAL
```

---

## Crash 46: `41788f207d9ec8dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041708`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIMESTAMP | NULL <> TRUE; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 47: `d2e1df2fdd7085e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041996`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NOT CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 48: `318ec4685bc8d834` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042141`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 49: `b145f1823cfec299` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042563`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NOT FALSE ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN SELECT *; SELECT hex
```

---

## Crash 50: `3a2fc1008e4a7cce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042816`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NOT FALSE GLOB CURRENT_TIMESTAMP ISNULL | NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s 
```

---

## Crash 51: `b08ec4493cbebb46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042899`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON FALSE GLOB CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN SELECT *
```

---

## Crash 52: `31481a01f0a45abe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043066`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(21
```

---

## Crash 53: `444c981f8b67ed9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043634`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (a) VALUES (min(RAISE(IGNORE)) FIL
```

---

## Crash 54: `439f8d7079cf8aa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044084`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NULL || NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT CAST(-NULL << RAISE(IGNORE) + T
```

---

## Crash 55: `ee3f412b11251b89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048887`

```sql
SELECT round(0.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, b); INSERT OR IGNORE INTO r VALUES (CURRENT_TIMESTAMP); ANALYZE q; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 56: `75d3ed328a7b1577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048996`

```sql
SELECT printf('%llu', 4294967295, ' 6w--z-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT INTO p VALUES (FALSE, CURRENT_DATE COLLATE NOCASE) RETURNING -CURRENT_TIMESTAMP AS xyv
```

---

## Crash 57: `45547d76ca4cc4be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049406`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 NUMERIC UNIQUE, c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 58: `dc0eb050fa556976` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049481`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE, c3 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a BLOB); INSERT INTO q VALUES (CURRENT_TIMESTAMP > CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF 
```

---

## Crash 59: `259b13ecd5041a6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB); INSERT INTO q VALUES (CURRENT_TIMESTAMP > CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 60: `e411fa7507b3807f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051508`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); INSERT OR FAIL INTO p VALUES (~(SELECT DISTINCT * FROM p NOT INDEXED)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); IN
```

---

## Crash 61: `b6b3655843161217` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055412`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT INTO q VALUES (CURRENT_DATE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 62: `7a95fb404b4c594c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056872`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL DEFAULT X'dBA42FA3dF', b NUMERIC); SELECT * FROM p JOIN p e ON NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 63: `a0918f4c7f025eb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057225`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIME OR NULL GLOB NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 64: `f7c029e903c291eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057924`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE (SELECT * FROM q WHERE CURRENT_TIMES
```

---

## Crash 65: `9eb2cadc693a528e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058040`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE (VALUES (CURRENT_DATE))) AS sub1; CR
```

---

## Crash 66: `9d4cc29437697a6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058066`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE) AS sub1; CREATE TABLE 
```

---

## Crash 67: `3f044eb8c4f27f08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058272`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON FALSE IS TRUE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 68: `65b551c79335114f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058598`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIMESTAMP LIKE NULL ESCAPE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT
```

---

## Crash 69: `8e3baabce079581b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058935`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON NOT CAST(FALSE AS TEXT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN WITH RECURSIVE q 
```

---

## Crash 70: `b0a2abd85b006baf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059877`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT * FROM p JOIN p e ON CURRENT_TIMESTAMP = CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN
```

---

## Crash 71: `50f68c0c907da06c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060081`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); SELECT DISTINCT * FROM p NATURAL JOIN p ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAU
```

---

## Crash 72: `c2f23e9f2456dc24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063600`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE HAVING CURRENT_TIME WINDOW
```

---

## Crash 73: `1896b0a65cbfe2fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063693`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 74: `7ec32673c3eeab46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063699`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS ()); S
```

---

## Crash 75: `0f8cc22c48a99754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064406`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL JOIN p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 76: `c09246959ab920b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064572`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (count(DISTINCT TRUE) FILTER (WHERE CURRENT_DATE))); CREATE VI
```

---

## Crash 77: `94f33c0a661519fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064733`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 78: `e60caf1f9057f2a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064993`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP GROUP BY CURRE
```

---

## Crash 79: `ec77a568dd7e03cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066176`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME IN (VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE))) AS sub1; SELECT printf('%.*f', 2147483647, -1e30
```

---

## Crash 80: `37c7b049063f2be3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067516`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p SELECT * FROM p NOT INDEXED; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 81: `569d76a0e5e50c17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067781`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE IND
```

---

## Crash 82: `bde0739a8640e140` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068495`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 83: `eccb9f7ebf6d5016` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070019`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); REPLACE INTO q VALUES (CAST(CURRENT_TIME AS INT)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 84: `38815da417980478` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070247`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 85: `824b9a5ed82a9426` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070272`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', 21474
```

---

## Crash 86: `d4ddec3d77f7be21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070504`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); REPLACE INTO q VALUES (TRUE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 87: `25ac2b349c2b0e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071755`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAU
```

---

## Crash 88: `7b43d080bfe2262e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072735`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); VALUES (CAST(FALSE AS BOOLEAN)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (NULL);
```

---

## Crash 89: `60d613d0c49c5e5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077596`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); SELECT DISTINCT * FROM p NATURAL JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c
```

---

## Crash 90: `dcfdb221028f2816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082129`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT CURRENT_TIME IS NOT TRUE FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 91: `0c64f68efbe74f4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083520`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE NULL) OVER (), NULL)) SELECT CURRENT_DATE IS NOT ifnull(CURRENT_DATE, NULL COLLATE NOCASE)
```

---

## Crash 92: `448f32548cb67b4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084883`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (FALSE)) SELECT count(DISTINCT CURRENT_TIME) FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 93: `547c648a4f55b2e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086117`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, a GENERATED ALWAYS AS (a) UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(21
```

---

## Crash 94: `bb634ef6fcac541b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086124`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 95: `542d7631b32b4050` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086186`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN CHECK (RAISE(IGNORE) OR FALSE), b TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 96: `bc986f132b16a754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089422`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 97: `21b240dcd46c7505` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089607`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT -44126012522274771568299478660399980323364314713793596319828013507180255519909920583960230765123807201832333441178434508596758605671220259106136748
```

---

## Crash 98: `6c766c952c1da209` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090158`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT X'fE95A4'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 99: `e075c4a7f3a21210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090230`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT 'L7- V 59_-'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 100: `7628b61c454d7a00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090534`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT X'cCCCCFaf8DeFA8'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 101: `8f3258bc45127da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090637`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 102: `b0b943ede319336e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090644`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 103: `1292825c7b4d1629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091627`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 FLOAT); INSERT OR ABORT INTO p VALUES (TRUE); VALUES (count(*) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 104: `45aa20c5e2be5329` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096001`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT count(*) FROM (SELECT * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 105: `1dc2fa62b5e07824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096641`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT NULL COLLATE BINARY FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 106: `c5230857ccc93c92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096928`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT *, * FROM p WHERE NULL) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 107: `68ad729ac9a6347d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097422`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN CURRENT_TIME NOT BETWEEN CURRENT_TIME NOT BETWEEN TRUE AND NULL AND NULL AND NULL) AS sub1
```

---

## Crash 108: `cc36d2739a04a722` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097612`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN CURRENT_DATE AND NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 109: `5ad92f8e3682db15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097803`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN CURRENT_TIME NOT BETWEEN CURRENT_TIME NOT BETWEEN TRUE AND NULL AND NULL AND NULL NOTNULL)
```

---

## Crash 110: `9c46e05e10a888dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097837`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT BETWEEN CURRENT_DATE AND NULL NOTNULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 111: `923de0288b836870` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097916`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP LIKE CURRENT_DATE FROM p WHERE CURRENT_TIME) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 112: `568d26f100b455f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098331`

```sql
SELECT substr('-_gX     _--8', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(2147483647));
```

---
