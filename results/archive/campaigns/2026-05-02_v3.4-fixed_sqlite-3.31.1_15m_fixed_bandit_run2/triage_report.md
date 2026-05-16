# Crash Triage Report

**Total crashes:** 139  
**Unique crash sites:** 139  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 139 | 139 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d620c8ee0794d883` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000111`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT t1.*, p.* FROM q AS a WHERE CAST(NOT CURRENT_TIME OR NULL NOTNULL AS INT) GROUP BY CASE RAISE(IGNORE) ->> TRUE IS NO
```

---

## Crash 2: `b7dd5cda1d861a9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000204`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT RAISE(IGNORE) NOT NULL, NULL FROM p NOT INDEXED NATURAL LEFT JOIN t2 NOT INDEXED , q NOT I
```

---

## Crash 3: `f6466cccc41cf266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000554`

```sql
SELECT substr('A_G6 _ -j__2Rb ', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT DISTINCT CASE WHEN RAISE(IGNORE) IS NOT CURRENT_TIME THEN RAISE(IGNORE) COLLAT
```

---

## Crash 4: `1b2a7f3c43092ad7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000560`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; VALUES (changes()); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (NULL % ~~-CURRE
```

---

## Crash 5: `f85b99135ab04446` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000893`

```sql
SELECT substr('T__', 9223372036854775807, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q VALUES (NOT CURRENT_TIME LIKE RAISE(IGNORE) ESCAPE NULL COLLATE NOCA
```

---

## Crash 6: `12c69451456e26ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001084`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(b INTEGER, c2 GENERATED ALWAYS AS (a * a) NOT NULL, rowid DATE); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_TIME AS s452_ FROM 
```

---

## Crash 7: `0c61b3a2efabfef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001409`

```sql
SELECT substr('C', 4294967295, -2147483648); SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT 0.0, rowid DATE GENERATED ALWAYS AS (CURRENT_DATE NOTNULL NOTNULL C
```

---

## Crash 8: `e56c2e69db6fe1aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001553`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2); SELECT ALL ~FALSE NOTNULL ->> NOT RAISE(IGNORE) > NOT FALSE << TRUE IS NOT NULL || last_insert_rowid() FILTER (WHERE (RAISE(
```

---

## Crash 9: `8c89f06c88b8cc76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001655`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VALUES ((VALUES (RAISE(IGNORE)) EXCEPT SELECT * ORDER BY RAISE(IGNORE)), upper(CURR
```

---

## Crash 10: `23c653a675977247` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001672`

```sql
SELECT printf('%.*f', 0, 0.0); SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; SELECT p.*; SELECT hex(zeroblob(-2147483648)); 
```

---

## Crash 11: `ff050d90ba6fbb72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001851`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM s WHERE TRUE GROUP BY CURRENT_TIME, RAISE(IGNORE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABL
```

---

## Crash 12: `6b073d078cfeb2dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001877`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DE
```

---

## Crash 13: `ddc5f682b436b97c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); VALUES (TRUE NOT LIKE CURRENT_TIMESTAMP); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREAT
```

---

## Crash 14: `6108834536906018` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002170`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES (FALSE, CURRENT_TIMESTAMP, CURRENT_DATE); ANALYZE t1; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 15: `40531a0dd53f9864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002237`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CAST(FALSE AS BOOLEAN) == CASE -NULL WHEN CURRENT_TIMESTAMP COLLATE BINARY NOT IN (changes(
```

---

## Crash 16: `c2f87591fa16960d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004363`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_
```

---

## Crash 17: `ba8f624d0cc83ad5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004805`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT *, TRUE NOT BETWEEN count
```

---

## Crash 18: `42525e5176fcd8b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005189`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (c3) AS (SELECT *) SELECT q.* FROM q; CREATE VIRTUAL TABL
```

---

## Crash 19: `64574b5eb030ef76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005770`

```sql
SELECT substr('k_9_1_--0v22_', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM q WHERE EXISTS (SELECT p.*, p.* FROM q AS s__v_3 LEFT JOIN q WHERE CASE WHEN FALSE -
```

---

## Crash 20: `b3ab85221e4f18bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006655`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*e', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH r (c2) AS (VALUES (CURRENT_DATE COLLATE NOCA
```

---

## Crash 21: `f5a09b79b74d46f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006747`

```sql
SELECT printf('%.*e', 4294967296, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 VALUES (CURRENT_DATE); SELECT q.* FROM p LEFT OUTER JOIN p NOT INDEXED USING (c3) WHER
```

---

## Crash 22: `9524b6e170b1f4a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007789`

```sql
SELECT substr('-m__--64__ 8_ - -K', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO s VALUES (CAST((CASE WHEN FALSE THEN TRUE COLLATE NOCASE ELSE +RAISE(IGNORE) END AND NOT 
```

---

## Crash 23: `a3357f1fe03b6a04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007833`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*s', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 24: `44f2854b1becdc83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008220`

```sql
SELECT printf('%.*g', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 VALUES (CURRENT_DATE COLLATE RTRIM) ORDER BY RAISE(IGNORE) AND NULL / CURRENT_TIME COLLATE RTRIM >= 
```

---

## Crash 25: `944d381a8059a8ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008483`

```sql
SELECT round(-1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, a, b, c3); INSERT INTO t2 (c2) VALUES ((CASE count(DISTINCT CURRENT_DATE == TRUE) WHEN CURRENT_TIME >> CUR
```

---

## Crash 26: `b52d671ada9b004f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008682`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; SELECT * FROM p NATURAL JOIN t2 WHERE FALSE; SELECT printf('%lli', 
```

---

## Crash 27: `2591f4135c7c376f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008712`

```sql
SELECT printf('%.*g', -2147483649, 0.01); CREATE TABLE IF NOT EXISTS p(a BOOLEAN GENERATED ALWAYS AS (RAISE(IGNORE) - TRUE & -NULL GLOB TRUE COLLATE BINARY <= NOT FALSE ISNULL LIKE -CURRENT_TIMESTAMP 
```

---

## Crash 28: `97239552b5e21a52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008885`

```sql
SELECT printf('%lli', -2147483649, '--__De - D l'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c2); SELECT CURRENT_TIME FROM (SELECT EXISTS (SELECT q.* LIMIT last_insert_rowid(), FALS
```

---

## Crash 29: `d0e186b897a6e647` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011233`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; SELE
```

---

## Crash 30: `5a30fcce7999bad9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012870`

```sql
SELECT substr('', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 31: `b3eb6897c8b9f0e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014575`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c2, a, _rowid_, b, c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME);
```

---

## Crash 32: `8a6f8595c9ce448a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014584`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 33: `03c8dfb1d89b26c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014594`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 34: `87004ac58e6d763b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014773`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 35: `21e37e17153227ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015189`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME BETWEEN CURRENT_DATE AND TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 36: `48b30c9d0dd7e42d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015224`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *, TRUE FROM p INDEXED BY a WHERE CURRENT_TIME GROUP BY FALSE GLOB TRUE + RAISE(IGNORE); VALUES (CURRENT_DATE); CREATE VIR
```

---

## Crash 37: `403c86f355bd4c3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015289`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 38: `d36cec64f9a821c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015323`

```sql
SELECT printf('%.*g', 2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 39: `e8c7c3a5b8d1b5a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015607`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 40: `86d4f04018688499` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019288`

```sql
SELECT round(1e-308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 41: `8afb1acba423583b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021173`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); WITH RECURSIVE p AS (VALUES (TRUE)) SELECT * FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 42: `c8e5c1c3a893fef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024319`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT CURRENT_TIMESTAMP FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY
```

---

## Crash 43: `535bf33550ac6b5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029219`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH p (b) AS NOT MATERIALIZED (SELECT NULL) INSERT
```

---

## Crash 44: `b010fe4f741deb58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029472`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CASE
```

---

## Crash 45: `b25af60bc41fc655` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029902`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT count(*), * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, b); SELECT NULL IN (FALSE
```

---

## Crash 46: `f4da8c890f504a79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030613`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); SELECT *, count(*), * FROM p
```

---

## Crash 47: `d0ad86de64325332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032561`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO q VALUES (printf('v53--iH_M -4W', NOT EXISTS (VALUES (changes() OVER (), RAISE(IGNORE)) LIMIT 
```

---

## Crash 48: `0de8fdf31036e270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033038`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), a GENERATED ALWAYS AS (a) UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, 
```

---

## Crash 49: `9d87b6cfe2bed885` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033363`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), a GENERATED ALWAYS AS (a) UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT I
```

---

## Crash 50: `3af4c61e024f6198` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033674`

```sql
SELECT printf('%.*g', -2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO q VALUES (~CURRENT_DATE & NULL <= CURRENT_DATE COLLATE NOCASE IS NULL, TRUE <
```

---

## Crash 51: `2a2b2eae1de2c828` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034152`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex
```

---

## Crash 52: `65947b1a3e4e6d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034166`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)); SELECT hex
```

---

## Crash 53: `477080e890dfb228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034547`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 54: `4f27ffc8f8a62725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034555`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT
```

---

## Crash 55: `f2cc9e5567ab55a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034929`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 56: `a4788fa3f6835d71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037265`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 57: `194ce63fee5ee9f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037645`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (FALSE || CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 58: `eadb21bc605a01a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038869`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (CURRENT_TIMESTAMP - TRUE < CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 59: `80a79f3a7bb0483b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039098`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); WITH RECURSIVE t2 AS (VALUES (RAISE(IGNORE))) SELECT FALSE GLOB FALSE AS d___7gw_cy_8h__6_689i_f58z395k_7y5n_s_y0_7n5_2__6n2o6_y4vzr__cb1_wfea75
```

---

## Crash 60: `73c980f64287d275` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039422`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); WITH RECURSIVE t2 AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_TIME - FALSE GLOB FALSE AS d___7gw_cy_8h__6_689i_f58z395k_7y5n_s_y0_7n5_2__6n2o6_y4
```

---

## Crash 61: `1269c36d2a0b7e04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042628`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELECT hex(zeroblob(-214748
```

---

## Crash 62: `43c3de73d5629c50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048316`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647,
```

---

## Crash 63: `99e9803629a9a284` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048810`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 64: `cb9bc6e521bda7ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051115`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, _rowid_, c3); INSERT INTO p VALUES (+FALSE IS DISTINCT FROM TRUE LIKE RAISE(IGNORE) OR TRUE ESCAP
```

---

## Crash 65: `bc270e7cbc9ce3e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051591`

```sql
SELECT printf('%.*d', -2147483649); SELECT printf('%s', 2147483648, '-_H9_ 6uk4B25u_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q WITH RECURSIVE r AS (SELECT p.* FROM s U
```

---

## Crash 66: `fc8b967b7b8d9c34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055254`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 67: `953ba2b4f0194393` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055463`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); VALUES (TRUE NOT LIKE CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE I
```

---

## Crash 68: `ec729b9abb273781` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055983`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC GENERATED ALWAYS AS (FALSE) STORED, b FLOAT PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 69: `7477826db8ba34f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056721`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF 
```

---

## Crash 70: `4d57d874db426063` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056760`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT 
```

---

## Crash 71: `903cc02c6b63b0e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061413`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT X'CBB92B2A0eBC'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 72: `db27f922d83cbc8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061528`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 73: `629c563154aeef7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061872`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION SELECT ALL count(*) FILTER (WHERE CURRENT_TIMES
```

---

## Crash 74: `63cefeaa6bab75af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062160`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) UNION SELECT ALL * FROM p NOT INDEXED NATURAL LE
```

---

## Crash 75: `0444573359eaaf0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063620`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN SELECT *, * FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () UNION SELECT
```

---

## Crash 76: `77bd75d11f772e52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063889`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT ALL X'deCB' FROM p; CREATE VIRTUAL TABLE
```

---

## Crash 77: `07b369794cbdc650` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064339`

```sql
SELECT round(0.01, 1); SELECT substr('56Y3--i H-i-9-_', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO t1 VALUES (TRUE BETWEEN FALSE AND CURRENT
```

---

## Crash 78: `91bb006b40fac98f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066908`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); WITH RECURSIVE t2 AS (VALUES (RAISE(IGNORE))) SELECT CURRENT_TIME GLOB FALSE AS d___7gw_cy_8h__6_689i_f58z395k_7y5n_s_y0_7n5_2__6n2o6_y4vzr__cb1
```

---

## Crash 79: `66eaeb66fab91615` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068882`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL DEFAULT 744.4e-214787044728756400116201744115257215332817947172223215281272801920888416795269878680049080475114583); CREATE VIEW IF NOT EXISTS v1 AS VALUES
```

---

## Crash 80: `948f51de715bf631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069713`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 81: `146e8ab4d1958c04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069836`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIMESTAMP AS REAL)); PRAGMA integrity_check; 
```

---

## Crash 82: `b4f15ae8f4e086f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072879`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FRO
```

---

## Crash 83: `c5ee77655ab5613e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073918`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INT); INSERT INTO p DEF
```

---

## Crash 84: `097304d1f9012388` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073938`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INT); INSERT INTO p DEF
```

---

## Crash 85: `35573f2cf4112ca7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073949`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE, c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 86: `2efdbb0328d774f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074582`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VI
```

---

## Crash 87: `b2fbccd059319833` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074740`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VI
```

---

## Crash 88: `1174d6dec96c812b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074860`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 89: `cd7906bcd71038ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076247`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255), a GENERATED ALWAYS AS (a) UNIQUE); VALUES (TRUE) EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VA
```

---

## Crash 90: `da1259cd77a7dcd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076938`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 91: `78f6ae74646292f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078073`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); WITH q AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (quote(NULL)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 92: `9d4157d1cad84f73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078284`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); WITH q AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (changes()); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 93: `1253cd1829da714e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078339`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CAST('A' AS DATE)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 94: `1a818be6d928e160` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078495`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CAST(FALSE AS DATE)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 95: `6bc9455f3ba5b197` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080851`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE);
```

---

## Crash 96: `bdadda05b6cff05d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080862`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE);
```

---

## Crash 97: `835d4ab159dd671b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080889`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE);
```

---

## Crash 98: `e63b87cad9d39c7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081623`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL, c1 DATE, b VARCHAR(255) DEFAULT NULL, c2 TEXT PRIMARY KEY); SELECT count(*), * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF N
```

---

## Crash 99: `f4139ab070d0f01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081898`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL, c3 BLOB NOT NULL); SELECT count(*), * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT I
```

---

## Crash 100: `b6d4d7810186cc54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081908`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL, c1 DATE, b VARCHAR(255) DEFAULT NULL, c2 TEXT PRIMARY KEY); SELECT *, * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 101: `297692794a83d6e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082918`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE IN (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA inte
```

---

## Crash 102: `2732d2ac0927b602` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083169`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE IN (NULL, CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t2 VALUES (
```

---

## Crash 103: `4db1e010b4e99746` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083371`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE, b INTEGER PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%f', -1, 't-_ X_-_6_'); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 104: `b1161e97c6f8a6fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083577`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT count(*), count(*), * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 DEF
```

---

## Crash 105: `a15b0f58b82ddb3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084012`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT NULL AS f_a1_49ru_b_9q2k5__iz1_4r_t_14, * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); S
```

---

## Crash 106: `9e107aef3a4e376b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084330`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE 'I_- _ 46_u9_  '; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; PRAGMA in
```

---

## Crash 107: `814c004f6752126b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085322`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT CURRENT_TIME LIKE CURRENT_TIMESTAMP ESCAPE TRUE AS j_3___7__ FROM (SELECT * FRO
```

---

## Crash 108: `23c05151aba5a794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085451`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE 
```

---

## Crash 109: `8e57c0ead5b1bdc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085624`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT count(*) FILTER (WHERE CURRENT_DATE) FROM (SELECT * FROM q WHERE CURRENT_TIMEST
```

---

## Crash 110: `3983bcf6fd894694` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086504`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM (SELECT * FROM q WHERE EXISTS (VALUES (TRUE) UNION VALUES (CURRENT_TIMES
```

---

## Crash 111: `fb56c7291352ed2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087241`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (c3) AS (SELECT *) SELECT count(*) FROM q; SELECT printf(
```

---

## Crash 112: `1a547966df6702e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087714`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; VALUES (count(DISTINCT TRUE)); CREATE VIR
```

---

## Crash 113: `308592db2099189f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088290`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a NUMERIC PRIMARY KEY); SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 114: `e156df945eca9794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089963`

```sql
SELECT round(1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(2147483648));
```

---

## Crash 115: `c415b223cc290b22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092021`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p e_ ON random() IS NULL; SELECT printf('%.*f', 42
```

---

## Crash 116: `4121b42ec7e9ea14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092247`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q JOIN p e_ ON CURRENT_TIMESTAMP OR CURRENT_TIMESTAMP; CR
```

---

## Crash 117: `fff622e289b7e4f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094646`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT * FROM p EXCEPT SELECT DISTINCT * FROM (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIM
```

---

## Crash 118: `52b92c16fbfb26d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095228`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY count(*) OVER (
```

---

## Crash 119: `2f82367a18d6070f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095661`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT TRUE FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY TRUE ASC NUL
```

---

## Crash 120: `8aed19349839187f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096029`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); SELECT ~c1 FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY TRUE ASC NULL
```

---

## Crash 121: `00bfb5b5714ac260` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108395`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE || TRUE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT
```

---

## Crash 122: `2ac4d1bb2306baf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 123: `65c8558cdd3b30fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108572`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 124: `3f612ed9e3cee1b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 125: `a8c0f0691bbcf172` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108659`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TR
```

---

## Crash 126: `7b57072aa91f05fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108920`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 127: `11b69fff0cc8f7af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109079`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY FALSE WINDOW w1 AS ())
```

---

## Crash 128: `76b852e7262109a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109845`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT 4.907445312924278943345193546883905575653256366276443662145689038821391125265383939444699258901427293082724452457778546173829215810198519898911
```

---

## Crash 129: `20022a1be816120d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111291`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 130: `8070c02f11788b7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111638`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL, a TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a
```

---

## Crash 131: `1d9577a0fb1e9a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111794`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 132: `80bb4c9a390db1a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112139`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a BLOB DEFAULT 4795568977104358429018164148981956.49093220642846410558551364212373397288796272210754529E+2); EXPL
```

---

## Crash 133: `ef45f2b76d87bb8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112153`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT count(*) FILTER (WHERE CURRENT_DATE), * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUA
```

---

## Crash 134: `3bcb9922b93b40e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112363`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CASE CURRENT_DATE WHEN CURRENT_TIME THEN CURRENT_DATE ELSE
```

---

## Crash 135: `43810e8b1844a0ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113258`

```sql
CREATE TABLE IF NOT EXISTS p(b INT, rowid GENERATED ALWAYS AS (a + 0) NOT NULL UNIQUE, a TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 136: `4a3b603f2b94a5fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113382`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 137: `c418722cf2452992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121014`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP COLLATE BINARY < FALSE GROUP BY FALSE WINDOW w1 AS ()); CREATE VIRT
```

---

## Crash 138: `f7d4a52fc9325410` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122510`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT NULL NOT 
```

---

## Crash 139: `e4eb351fc787721e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126522`

```sql
SELECT printf('%.*s', 4294967296, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT r.* FROM p AS s4s_us6cd__9_8__ NATURAL JOIN p AS l265k5526__ef_3p INNER JOIN (SELEC
```

---
