# Crash Triage Report

**Total crashes:** 169  
**Unique crash sites:** 169  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 169 | 169 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `465f8b227de2d7d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000199`

```sql
SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT RAISE(IGNORE) IS DISTINCT FROM CURRENT_TIME NOTNULL NOT NULL GLOB total_changes() REGEXP TRUE AND RA
```

---

## Crash 2: `f0196d55f4f1975d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000224`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE t3 AS MATERIALIZED (VALUES (NULL IN (VALUES (NULL) LIMIT FALSE) REGEXP RAISE(IGNORE) IN (RAISE(IGNORE), total_changes()) < (TRU
```

---

## Crash 3: `288a4f7fa7a91e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000320`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, a, b); INSERT INTO p VALUES (TRUE | FALSE LIKE ~CURRENT_DATE IS NOT NOT NULL NOT IN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP) I
```

---

## Crash 4: `42d4bb2fbdb15316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000838`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT ~count(DISTINCT CURRENT_TIME) IS NOT CURRENT_TIMESTAMP LIKE -CURRENT_DATE ESCAPE (NULL) ||
```

---

## Crash 5: `be9054bfd840d355` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000971`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT r.*, CURRENT_DATE + TRUE LIKE lower(CURRENT_TIMESTAMP) = CURRENT_DATE IS FALSE <= NULL COLLATE NOCASE IS
```

---

## Crash 6: `6fd9cf40c4523d83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001084`

```sql
SELECT printf('%.*g', -9223372036854775808, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q AS MATERIALIZED (VALUES (CURRENT_TIME)), q (c3) AS (VALUES (RAISE(IGNORE)) LIMIT CURR
```

---

## Crash 7: `b0730b789e25157c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001127`

```sql
SELECT printf('%.*e', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q AS (SELECT +CURRENT_TIME UNION ALL SELECT DISTINCT * FROM t1 NATURAL LEFT JOIN q WHERE ifn
```

---

## Crash 8: `29ff410a7a41a9ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001169`

```sql
SELECT substr('_____o_P 21_g d_F5', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s VALUES (-TRUE COLLATE NOCASE IS NULL NOT IN (TRUE, NULL || NULL NOT N
```

---

## Crash 9: `641e3fd4e2a84576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001180`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3, a, c2, a, b, c3); INSERT INTO p SELECT TRUE IS NULL | CURRENT_TIME NOT NULL LIKE RAISE(IGNORE) <> CURRENT_TIME COLLATE NOCASE IS NOT DI
```

---

## Crash 10: `3c4d6e33a0e94b93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001544`

```sql
SELECT printf('%s', 4294967295, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; SELECT *; CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (EXISTS (
```

---

## Crash 11: `c6179cccc9fd4336` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001682`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO r VALUES (b); EXPLAIN QUERY PLAN SELECT ALL CURRENT_DATE == CURRENT_TIMESTAMP
```

---

## Crash 12: `7eb5df0bc6ad36ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002147`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY RAISE(IGNORE) HAVING CURRENT_DATE WINDOW w1 AS (), w2 AS (OR
```

---

## Crash 13: `16b6a68060580c6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002177`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (NULL); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 14: `537e72ebed3e04f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002214`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY RAISE(IGNORE) HAVING CURRENT_DATE WINDOW w1 AS (); EXPLAIN Q
```

---

## Crash 15: `3782487cad0c2f63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002221`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY RAISE(IGNORE) HAVING CURRENT_DATE WINDOW w1 AS (), w2 AS (OR
```

---

## Crash 16: `b4d7aac4ec1e9c90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002234`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR
```

---

## Crash 17: `fc1fc047f4a144b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002476`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN SELECT CURRENT_TIMEST
```

---

## Crash 18: `4cf44c6aa3b0b31a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002837`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) EXC
```

---

## Crash 19: `f55ff5968ab1c18c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002850`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 20: `13081bb41a444f97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002856`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL
```

---

## Crash 21: `01fb5326604ad10f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002871`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 22: `aed31bdba77aff52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002883`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INS
```

---

## Crash 23: `5b5b78c1a5666a94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002900`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_TIME - NULL); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 24: `56e6980de3d3908a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004245`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 25: `17f36361fe640a95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004931`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p (c3, c1, _rowid_) VALUES (RAISE(IGNORE), FALSE COLLATE RTRIM NOT BETWEEN +NULL AND (RAISE(IGNORE)) AND 
```

---

## Crash 26: `a9167c784c18fd3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005094`

```sql
SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT DISTINCT * FROM p ORDER BY (count(*) FILTER (WHERE CURRENT_TIME) NOT LIKE CAST(NULL AS BLOB) || CAS
```

---

## Crash 27: `65c7be7447490ccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006511`

```sql
SELECT printf('%lld', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s (b) VALUES (-NULL) ON CONFLICT(a) DO UPDATE SET rowid = CURRENT_TIME; PRAGMA quick_check; 
```

---

## Crash 28: `fc67e27982b46da7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006528`

```sql
SELECT printf('%.*s', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO t2 VALUES (TRUE <> TRUE GLOB TRUE IS NOT NULL NOT LIKE CURRENT_DATE COLLATE NO
```

---

## Crash 29: `93a6bec351b7e847` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006603`

```sql
SELECT printf('%.*g', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO q VALUES (CAST(CASE quote(CAST(+FALSE <> NOT RAISE(IGNORE) IS NOT NULL AS REAL)) 
```

---

## Crash 30: `6f1f99bc62bd1417` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007233`

```sql
SELECT substr('_- t42-Yl_dt_H920_t', -2147483648, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; SELECT p.* FROM t3 WHERE EXISTS (SELECT * LIMIT TRUE, RAISE
```

---

## Crash 31: `568664e2c407b6ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007555`

```sql
SELECT printf('%f', 4294967296, '_-7 -- G-  n934 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 SELECT b AS a LIMIT CASE (upper(CURRENT_TIME) LIKE (FALSE) ESCAPE CURRENT_
```

---

## Crash 32: `36d1563ee253eff2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007755`

```sql
SELECT substr('b0 4Ll12', -1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); SELECT iif((TRUE), NULL, +TRUE) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC
```

---

## Crash 33: `9c2bc2aba21d3062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008102`

```sql
SELECT round(0.01, 1); SELECT printf('%s', 9223372036854775807, 'K -v2_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH t3 (c1) AS NOT MATERIALIZED (VALUES ((TRUE), NULL)) INSERT INTO
```

---

## Crash 34: `dbd0e12e63b9490b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009415`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT RAISE(IGNORE) LIMIT FALSE;
```

---

## Crash 35: `36792225c96cf06f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010706`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CR
```

---

## Crash 36: `02cf9498e7d66555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010743`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex
```

---

## Crash 37: `d64e23e5185c5179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011370`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME LIKE FALSE); PRAG
```

---

## Crash 38: `af76d5af8506b708` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012186`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 39: `50cd17b57aa5ff0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013356`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (random()); PRAGMA integrity_ch
```

---

## Crash 40: `ed0a906b4ab3d817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014462`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 41: `f06c308900fb8a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016017`

```sql
SELECT substr('--K_7-sN1  l', 4294967296, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-1)
```

---

## Crash 42: `766cdfb81aca57ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016277`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 43: `627ec06cf083fc7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016290`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 44: `d170b65ac9777e1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016423`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 45: `f5a55d4d0f37eae3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017444`

```sql
SELECT printf('%.*s', 4294967296); SELECT printf('%.*d', -1, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (RAISE(IGNORE)) UNION ALL SELECT * ORDER BY last_insert_rowid() OVE
```

---

## Crash 46: `caec5716bae4e50c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017633`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT OR FAIL INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK I
```

---

## Crash 47: `b7e87dda6ea1353d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019913`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE p (c2, rowid) AS (SELECT *) SELECT *; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 48: `74e317c5550be6c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021581`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL, a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p (c3) VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 49: `5605705a3d81a43c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022493`

```sql
SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 50: `2390fda5bb87ecc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022568`

```sql
SELECT substr('Y_4McE4 -IS_9 cld', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (FALSE);
```

---

## Crash 51: `3cac12c8f47677aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024344`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-2147
```

---

## Crash 52: `b2cbca01c292c8d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024389`

```sql
SELECT printf('%u', 4294967295, '_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT FALSE NOT BETWEEN +CURRENT_TIME COLLATE BINARY << (CURRENT_DATE) >> RAISE(IGNORE) >> RAISE(IGNORE
```

---

## Crash 53: `0d0da24922901f27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024681`

```sql
SELECT substr(' c___Sb2n', 4294967295, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE 
```

---

## Crash 54: `1f234b6b5620ab23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025211`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (NULL), a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 55: `e39e6e13d61722ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027426`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (-CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 56: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027838`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 57: `6039e1ebbcf00064` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027928`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY, a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUE
```

---

## Crash 58: `d3d7a187df39d095` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028129`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC GENERATED ALWAYS AS (NULL LIKE TRUE ESCAPE NULL) VIRTUAL, rowid BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 59: `9260dde40077148b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030694`

```sql
SELECT printf('%.*s', 2147483647, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 60: `f0317a6a96e70b76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030893`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 61: `07093df815e7adb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032066`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP = FALSE >> CURRENT_DATE); PRAGMA quick_check
```

---

## Crash 62: `d82433e2b8d07477` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032809`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) DEFAULT 258825615485668.842734747963389846655707651979876492907785532327237e2467); INSERT INTO q DEFAULT 
```

---

## Crash 63: `ca5fbc310cdd89ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032826`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 64: `bc35413985e3f20e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032903`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE I
```

---

## Crash 65: `03a968b0b33f0226` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033044`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 66: `e479f0ac7bfd2ebe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033235`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (NULL + CURRENT_TIME & TRUE IS NOT FALSE); PRAGMA quick_check; CREATE V
```

---

## Crash 67: `3f6b66a4baaf2ca1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033479`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE & TRUE IS NOT FALSE); PRAGMA quick_check; CREATE VIRTUAL 
```

---

## Crash 68: `615074d04d8170a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035058`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON ~CURRENT_TIMESTAMP; CREATE VIRTUAL TABL
```

---

## Crash 69: `b725222a2d22242e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035346`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON FALSE; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 70: `1341b335828d3d94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035471`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON ~NULL; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 71: `c7735e5c899b9cdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037796`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 72: `739feb1e5db91011` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038734`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT substr('k_K0', -92
```

---

## Crash 73: `e6c18e0e13f7cbb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039034`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 74: `345b045a22670955` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042094`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_DATE DESC NULL
```

---

## Crash 75: `d3323b9f0bef51dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042402`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP))) ON CONFLICT DO NOTHING; PRAGMA quick_
```

---

## Crash 76: `57db2418b52fc051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_DATE IN (VALUES (TRUE))) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CR
```

---

## Crash 77: `0489fd482e7a664a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043069`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (TRUE IN (VALUES (TRUE))) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 78: `e9510db07ec8800b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043632`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); INSERT OR FAIL INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT RAI
```

---

## Crash 79: `0b2fc7e9693881c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043675`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT * FROM p)); PR
```

---

## Crash 80: `fc81df3576bb5714` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043691`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (random() GLOB random() GLOB ra
```

---

## Crash 81: `c1beec33e8ac764e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043698`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (random() NOT LIKE CURRENT_TIMESTAMP NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); EXPLAIN QU
```

---

## Crash 82: `cfa7cdb416edb796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043742`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL DEFAULT CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 83: `a9f2e4612e32bd82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045303`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); WITH RECURSIVE p AS (VALUES (RAISE(IGNORE))) INSERT INTO q VALUES (+CURRENT_TIMESTAMP * TRUE); PRAGMA 
```

---

## Crash 84: `c3ceaece36e2602a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051073`

```sql
SELECT printf('%x', -2147483648, 'O_g  -__-c'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-
```

---

## Crash 85: `8122ba3ce19cf8e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052793`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 86: `c9368dfa5d656fb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053663`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT ALL NULL FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 87: `055f3b0ac4c81f92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053879`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); INSERT INTO p SELECT CURRENT_TIME AS t; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 88: `0137d271278aeec7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056062`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); WITH RECURSIVE p AS (VALUES (RAISE(IGNORE))) INSERT INTO q VALUES (CURRENT_DATE * CURRENT_DATE * CURRE
```

---

## Crash 89: `cb7d97e7846d5d2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057429`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a IS NULL) UNIQUE, c2 NUMERIC NOT NULL DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NATURAL LEFT JOIN p; 
```

---

## Crash 90: `21f72fea039f5a8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058481`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_DATE))) ON CONFLICT DO NOTHING; PRAGMA quick_
```

---

## Crash 91: `b44dd35e1f41437e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (0))) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELE
```

---

## Crash 92: `7d92f047c08c1ef1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058937`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIME))) ON CONFLICT DO NOTHING; PRAGMA quick_
```

---

## Crash 93: `44e6a1eefe89ee48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059045`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (X'eC0CA9') ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 94: `5045429e47232bb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060243`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT INTO q VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP))) ON CONFLICT DO NOTHING; PRAGMA q
```

---

## Crash 95: `54ea296b6b25e09e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060533`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 REAL NOT NULL); INSERT INTO q VALUES (CURRENT_DATE IN (SELECT * FROM q NOT INDEXED WHERE FALSE)) ON CONFLICT DO NOTHING; 
```

---

## Crash 96: `81fe640e1b080697` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065351`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT OR ROLLBACK INTO p VALUES (X''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1)
```

---

## Crash 97: `db14b3ef9349c993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066258`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (NOT EXISTS (VALUES (FALSE) EXCEPT VALUES (NULL))); PRAGMA integr
```

---

## Crash 98: `37623f028c54d18d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066836`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%
```

---

## Crash 99: `a972a0c44b6ec096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067029`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a * a) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NATURAL LEFT JOIN (VALUES (FALSE)) A
```

---

## Crash 100: `fcb0cf4f29c0b0f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067579`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a = 0) UNIQUE); WITH p AS (VALUES (CURRENT_DATE)) INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 101: `bbdc5cb24f028a1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071231`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON CURRENT_DATE = NULL; CREATE VIRTUAL TAB
```

---

## Crash 102: `d4fd837ec59e64e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071354`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON CURRENT_TIME; CREATE VIRTUAL TABLE IF N
```

---

## Crash 103: `b399ee7812686f2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071980`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON CURRENT_TIME BETWEEN CURRENT_DATE AND C
```

---

## Crash 104: `6c46ce94162075b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072954`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON (VALUES (TRUE)); CREATE VIRTUAL TABLE I
```

---

## Crash 105: `74fe8e88dbffae95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073464`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON FALSE <= CURRENT_TIME; CREATE VIRTUAL T
```

---

## Crash 106: `dd6bf37f468f4765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073742`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT X'd1F3'); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON CURRENT_TIMESTAMP; CREATE
```

---

## Crash 107: `ffcbc7490ad21f3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073775`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT UNIQUE); SELECT * FROM p JOIN p z_md2z_1_q_9_hjf9h04dlv37_j_7v5soq6gz__84w_4_gc4 ON CURRENT_TIMESTAMP; CREATE VI
```

---

## Crash 108: `49ba01947595ef66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075032`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE + CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 109: `658e596d4976d86d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075275`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT LIKE random() + CURRENT_TIME IS NOT FALSE); PRAGMA qu
```

---

## Crash 110: `a7cc062d997f9795` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077266`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT INTO p (rowid) VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 111: `4b880059f3a2f863` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077411`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP >> CURRENT_TIME); PRAGMA quick_check; CREATE
```

---

## Crash 112: `9cbabaf6dc35176b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077612`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL DEFAULT -5012); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 
```

---

## Crash 113: `aeb6937156f58054` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077739`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 
```

---

## Crash 114: `a565b2a9d81f4d75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078010`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE - TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 115: `ef4445161953b1e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078267`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE - TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 116: `e3c164bad660779b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078558`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE - TRUE - TRUE - TRUE); PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 117: `0e5378512f564345` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079170`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ABORT INTO p VALUES (NULL = CAST(CURRENT_TIME AS BOOLEAN)); PRAGMA quick_check; CRE
```

---

## Crash 118: `cdfe213032124470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079337`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED GROUP BY N
```

---

## Crash 119: `6896db41c342f53d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079895`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 120: `0e3b7bbdd4f92aba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079906`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INT UNIQUE); REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER 
```

---

## Crash 121: `d8a92467ab446852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080316`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE, c2 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF N
```

---

## Crash 122: `24276e0e02bd1730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080474`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 123: `a5a2d01d57fb3410` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080622`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIME, b DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREA
```

---

## Crash 124: `0f955f7b64d4b66a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080941`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIME, c3 FLOAT CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE CU
```

---

## Crash 125: `42cf45653068d1c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080965`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 FLOAT CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUA
```

---

## Crash 126: `80783bb4034a124e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080972`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT CURRENT_TIME, c3 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; C
```

---

## Crash 127: `e95395c9043f3cc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081397`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT ''); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 128: `82361401587b6741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081863`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY, a TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT substr('2yj4U', -2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 129: `a2faed5d588afc06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083056`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (count(*) O
```

---

## Crash 130: `b1f615ff9b32987b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083256`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR ABORT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (NULL))); P
```

---

## Crash 131: `69178da5c753de30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084935`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (random() NOT LIKE CURRENT_TIMESTAMP NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KE
```

---

## Crash 132: `572659a21cad20f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085100`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (NULL NOT LIKE TRUE), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf(
```

---

## Crash 133: `b49cc461c28fbb98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085106`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES
```

---

## Crash 134: `d3851ab32394b080` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085112`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CURRENT_TIME NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAU
```

---

## Crash 135: `92a09c727c92c65c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085274`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (random() NOT LIKE CURRENT_TIMESTAMP NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE NOT LIKE CURRENT_TIMESTAMP), rowid FLOAT); CREATE TABLE IF NOT EXI
```

---

## Crash 136: `5e5a92b4f4d1f387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086098`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (random()), rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 137: `84179efbbc91646a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086376`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 138: `bc1cade46ac4dc53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086797`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (TRUE), _rowid_ TEXT NOT NULL DEFAULT TRUE, rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 139: `d6bdca7a78756563` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088067`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT CURRENT_TIMESTAMP IS NOT CURRENT_DATE; CREATE VIRTUAL TA
```

---

## Crash 140: `f11ebcfe5fb0b88f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088187`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 141: `3af2f9f9c2d5d89c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088267`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME LIKE FALSE ESCAPE FALSE; CREATE VIRTUAL TABLE I
```

---

## Crash 142: `85fb6925d6e66631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089126`

```sql
SELECT round(0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); WITH RECURSIVE q (b) AS (SELECT *) SELECT changes() NOT BETWEEN min(FALSE COLLATE BINARY) AN
```

---

## Crash 143: `4044e9a5d24da534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089870`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (CURRENT_TIMESTAMP), c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r GROUP BY TRUE, CURRENT_TIME; INSERT OR 
```

---

## Crash 144: `2c5102b1fb15bb10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100657`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE NOT IN (VALUES (CURRENT_TIME)), FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 145: `8ea610cbd30484c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100823`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT OR FAIL INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT OR ROLLBACK 
```

---

## Crash 146: `b1699ba18f1b8a7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100858`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT OR FAIL INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (random() NOT LIKE CURRENT_TIMESTAM
```

---

## Crash 147: `cc9fd9ce2e9719d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100918`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); INSERT OR FAIL INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b DATE, _rowid_ GENERATED ALWAYS AS (a + -0) UNI
```

---

## Crash 148: `64189120b22e2497` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108499`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC GENERATED ALWAYS AS (NULL LIKE TRUE ESCAPE NULL) VIRTUAL, rowid BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (NULL LIKE FAL
```

---

## Crash 149: `2dca194b4269e9cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109043`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE % TRUE); PRAGMA integrity_check; SELECT printf('%.*f', -21474836
```

---

## Crash 150: `3899ae09efafb4ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED GROUP BY NULL ORDER BY CURRE
```

---

## Crash 151: `c0e5941922a5d458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109869`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 152: `ba88d225b75e9425` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111048`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (random()); PRAGMA integrity_chec
```

---

## Crash 153: `30f04d3cbeaf3e3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111978`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT BETWEEN changes() AN
```

---

## Crash 154: `cf6f9f7827974403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112153`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (NULL NOT LIKE last_insert_rowid()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 155: `a0de96866057168a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113382`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (X''); PRAGMA integrity_check; 
```

---

## Crash 156: `7f5680c30b56d1a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113416`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (X'' NOT LIKE CURRENT_TIMESTAMP
```

---

## Crash 157: `4d400d4fb022d10f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113618`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (-38950453103226233875930947641
```

---

## Crash 158: `e0324152d872f5c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114249`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (total_changes()); PRAGMA integ
```

---

## Crash 159: `03cd55eb3d0bf934` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116994`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME LIKE CAST(CURRENT
```

---

## Crash 160: `65a138aea467eb5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117522`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT 7476902513.60649247902892952664926471912271160024326155002097311747569872688398513920982748396610860106135671820316353443199177649176); CREATE INDEX IF 
```

---

## Crash 161: `bec9f0eb7f3a38e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117703`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_TIMESTAMP AS REAL)); PRAGMA integrity_check; SELECT printf('
```

---

## Crash 162: `0ad3adacf9f66c23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117832`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE << FALSE); PRAGMA
```

---

## Crash 163: `3c388b5de9fe135d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118220`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CAST(NULL AS NUMERIC) IS NULL / CURRENT_TIMESTAMP); PRAGMA integrity_chec
```

---

## Crash 164: `dac9ff55d27700e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT -418771776664017080108684986442223973106431435194878256480867.3707E0260809615968255431412336421
```

---

## Crash 165: `37eb3d2be2fad970` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125113`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNI
```

---

## Crash 166: `c55c8695c1641175` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125134`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NUL
```

---

## Crash 167: `8e8807b4fa0fdf18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125176`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT 
```

---

## Crash 168: `82bb4a6d622ba173` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125228`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483648, 1e-308); CR
```

---

## Crash 169: `8bae6e3df0281de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126688`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL, c1 TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT OR ROLLBACK INTO p VALUES (CAST(FALSE AS BLOB)); PRAGMA i
```

---
