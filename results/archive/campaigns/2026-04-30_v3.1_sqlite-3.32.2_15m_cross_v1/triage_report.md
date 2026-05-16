# Crash Triage Report

**Total crashes:** 127  
**Unique crash sites:** 127  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 127 | 127 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `49935375b3333cc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000113`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT OR ABORT INTO q VALUES (RAISE(IGNORE) COLLATE NOCASE * CASE CURRENT_TIME WHEN FALSE THEN NULL ELSE CURRENT_TIME END IS NOT s.a IS N
```

---

## Crash 2: `9053476b658fb742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000527`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO q (c1) VALUES (-CURRENT_DATE == CURRENT_TIME); SELECT TRUE AS x_, +total_changes() FROM p NATURAL JOIN p WHERE TRUE ->> NULL RE
```

---

## Crash 3: `e5ba9dab5a44df2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000987`

```sql
SELECT substr('Oz N9__ R3 ', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT q.*, CURRENT_TIMESTAMP OR RAISE(IGNORE) & CAST(last_insert_rowid() AS BLOB)
```

---

## Crash 4: `92dd9c0ef6f377f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001162`

```sql
SELECT round(1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 DEFAULT VALUES; SELECT CURRENT_TIMESTAMP NOT IN (SELECT q.*) AS dxe_, p.*, RAISE(IGNORE) NOTNULL < FALSE 
```

---

## Crash 5: `bd1cf78c6ce8135f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001278`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p SELECT ALL CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP) FROM q; EXPLAIN QUERY PLAN S
```

---

## Crash 6: `ab0017b33908b4ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001774`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM p WHERE EXISTS (SELECT q.* ORDER BY NULL DESC NULLS LAST); CREATE TABLE IF NOT EXISTS p(b NUMERIC
```

---

## Crash 7: `5cc34629124cfcf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001848`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT ALL q.* FROM p NOT INDEXED , r INDEXED BY c3 CROSS JOIN (SELECT DISTINCT * FROM q ORDE
```

---

## Crash 8: `e78e1df1dd9d38a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001856`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT 
```

---

## Crash 9: `10508d5238f1e62f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001871`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT ALL q.* FROM p NOT INDEXED , r INDEXED BY c3 CROSS JOIN (SELECT DISTINCT * FROM q ORDER BY chan
```

---

## Crash 10: `438702d9dc621c15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001899`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO q VALUES (CURRENT_TIMESTA
```

---

## Crash 11: `83a3e1aeee24095b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002180`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (CASE NULL WHEN NULL THEN CURRENT_TIME END); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 12: `a15d3d1fa6c7f068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002195`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (json(NULL NOTNULL IS NOT NULL OR CURRENT_DATE NOT NULL), CURRENT_TIME, (RAISE(IGNORE) <= (SELEC
```

---

## Crash 13: `9a91647694d49f9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002868`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSER
```

---

## Crash 14: `1c20d285c52f7019` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003405`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, b); WITH q (c3, _rowid_) AS NOT MATERIALIZED (SELECT NULL COLLATE RTRIM FROM t1 JOIN s ON CURRE
```

---

## Crash 15: `39e0e1a54e6076c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004327`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_chec
```

---

## Crash 16: `94f6c9906254f21d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004372`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_
```

---

## Crash 17: `2f8550508e015971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006767`

```sql
SELECT printf('%.*e', 1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO r VALUES (NOT q.b); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP >> CURRENT_DATE AS ng96
```

---

## Crash 18: `8de164ec690254d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007136`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALUES (+CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PL
```

---

## Crash 19: `cb38fa822f2a2bd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007339`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE p (c1, a, a, a) AS NOT MATERIALIZED (VALUES (RAISE(IGNORE), CURRENT_TIME) ORDE
```

---

## Crash 20: `6fd77a5af827c4cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007527`

```sql
SELECT substr('_ _r__ _A-_', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r (c2) VALUES (CURRENT_TIME NOT IN (TRUE) % RAISE(IGNORE) % RAISE(IGNORE) <= CURRENT_DATE
```

---

## Crash 21: `334276b7aca83bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010788`

```sql
SELECT printf('%.*e', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); INSERT INTO q SELECT p.*; WITH RECURSIVE q AS NOT MATERIALIZED (SELECT t1.* ORDER BY NULL || FALSE
```

---

## Crash 22: `b3dc8800ceffd7c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015677`

```sql
SELECT substr('_-lPaS ', 9223372036854775807, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c2); INSERT INTO s DEFAULT VALUES; SELECT *, * FROM q NOT INDEXED WHERE TRUE IS 
```

---

## Crash 23: `aeb928e78d02ef69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT FALSE AS 
```

---

## Crash 24: `becd91aca1ea0a8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018156`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid) VALUES (CURRENT_TIMESTAMP) ON CONFLICT(c3) DO UPDATE SET c3 = RAISE(IGNORE); PR
```

---

## Crash 25: `f14b8008cc803f2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021381`

```sql
SELECT printf('%x', -2147483649, '  _   __-3Y03-L_eQ'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (c1) VALUES (NULL) ON CONFLICT(c3) DO UPDATE SET c3 = CURRENT_DATE;
```

---

## Crash 26: `4e4ef9b6684f8d8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 27: `4fa08d4ae2e26171` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023823`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () LIMIT CURRENT_TIME NOT IN (VALUES (TRUE)); CREATE V
```

---

## Crash 28: `f5b19f504f9b02f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025473`

```sql
SELECT printf('%.*f', -9223372036854775808, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT t2.*; SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c2 BLO
```

---

## Crash 29: `f1f03d84b1f75b60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025642`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 30: `a7c0766a9316bea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028205`

```sql
SELECT substr('47U__34ms', 2147483647, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO r VALUES (-(SELECT ALL NULL NOT NULL AS a FROM (SELECT NULL ORDER B
```

---

## Crash 31: `fdcb91069a27142e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028408`

```sql
SELECT printf('%.*d', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid) VALUES (NULL) ON CONFLICT(c3) DO UPDATE SET c3 = CURRENT_TIME; PRAGMA quic
```

---

## Crash 32: `12831c6933d69b7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029730`

```sql
SELECT round(1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); SELECT ALL t1.*, * FROM p NOT INDEXED LIMIT RAISE(IGNORE) - TRUE NOT IN (VALUES (NULL IS NOT NU
```

---

## Crash 33: `73f2687288dd8371` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029921`

```sql
SELECT printf('%.*s', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c2); SELECT t3.* FROM (q NOT INDEXED CROSS JOIN p) GROUP BY CURRENT_TIME -> (CURRENT_TIMESTAMP) HAVING c
```

---

## Crash 34: `d505cff3f4b8d73c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031541`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); WITH RECURSIVE t2 AS (VALUES (FALSE)) SELECT *, CURRENT_TIMESTAMP FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (
```

---

## Crash 35: `3652689bdaf36388` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031813`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); WITH RECURSIVE t2 AS (VALUES (FALSE)) SELECT NULL FROM p; SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 36: `5a0754239de80a25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032761`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_TIME, c3 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 37: `69c383c50b7496ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid) VALUE
```

---

## Crash 38: `1d309eb376a40d9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033960`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE -CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid, c1) 
```

---

## Crash 39: `29f0f64bd39dd1c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034867`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid, c1) VALUES (N
```

---

## Crash 40: `b2b83ce9a5d800d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035135`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY TRUE COLLATE BINARY HAVING FALSE LIMIT FALSE); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 41: `3e1a7e5554e901db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035363`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_DATE LIMIT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 42: `1c33072564db6628` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035846`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY FALSE LIMIT ~FALSE ISNULL, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 43: `bfeacc39339d61dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035888`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, c3, a, _rowid_, c1, a); EXPLAIN QUERY PLAN SELECT q.*, CURRENT_TIMESTAMP NOT IN (RAISE(IGNORE)) >> CURRENT_TIME MATCH RAISE(IGNORE) || C
```

---

## Crash 44: `044ac50d86ce8f83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038482`

```sql
SELECT round(0.0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT ~RAISE(IGNORE) <= CURRENT_TIME >= --FALSE = TRUE FROM (SELECT -TRUE NOT NULL * EXISTS (VALUES (+CURRENT_DATE)) > 
```

---

## Crash 45: `310beab0831f2245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040299`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT 3636.220320795247e+056); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 46: `15eb3cd771c81e19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040306`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NATURAL JOIN p USING (c3, c3) WHERE CURRENT_TIME GROUP BY RAISE(IGNORE) WINDOW w1 AS (); EXPLAIN QUERY 
```

---

## Crash 47: `6106bf02596b0395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040313`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP NOT IN (FALSE))); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 48: `3b0116a15b745894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040319`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY FALSE DESC NULLS FIRST)); PRAGMA quick_check; CREATE VI
```

---

## Crash 49: `7764a438b9fac021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040356`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 50: `a1f6a3572b2e1560` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040370`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT, c3 GENERATED ALWAYS AS (a * a) UNIQUE, a FLOAT DEFAULT -520679); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_
```

---

## Crash 51: `4312a7ea35edeec8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040376`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (FALSE), rowid INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 52: `de3bb8ef07f42c3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042347`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REP
```

---

## Crash 53: `58d2a28e2dcbb261` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042427`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN GENERATED ALWAYS AS (-NULL) VIRTUAL, c2 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CRE
```

---

## Crash 54: `84427f6c28ae37ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043023`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 55: `dcd36b0fa2ed4f69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043706`

```sql
SELECT substr('X5 -GV-9P  TYDU_9_', -2147483648, 4294967295); SELECT substr('', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2, _rowid_, c1); INSERT INTO t2 V
```

---

## Crash 56: `e80bd2c450c2cd8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044393`

```sql
SELECT round(-0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c2); INSERT INTO p SELECT q.*, * ORDER BY NULL << NULL - NULL DESC NULLS FIRST, NULL LIKE FALSE ESCAPE TRUE
```

---

## Crash 57: `5eb598765291c360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044860`

```sql
SELECT substr('_x4 L2  __leB2 ', 0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (c1) VALUES (NULL) ON CONFLICT(c3) DO UPDATE SET c3 = CURRENT_DA
```

---

## Crash 58: `24fc2a536f53a6c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044958`

```sql
SELECT printf('%.*s', -1); SELECT round(0.01, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r (a) VALUES (CAST(trim(CAST((+CASE WHEN c2 | RAISE(IGNORE) <>
```

---

## Crash 59: `71568832735ece1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045423`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p fr1u ON CURRENT_TIME IN (changes(), CURRENT_TIMES
```

---

## Crash 60: `ef35faddd01d37db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045653`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p fr1u ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 61: `9697892c98c2c8d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045659`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p fr1u ON CURRENT_TIME IN (FALSE); CREATE VIRTUAL T
```

---

## Crash 62: `ec3a7f3985af61b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045665`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p fr1u ON CURRENT_TIME IN (TRUE, CURRENT_TIMESTAMP)
```

---

## Crash 63: `be01dd4859278e33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045850`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p fr1u ON CURRENT_TIME IN (~upper(NULL), CURRENT_TI
```

---

## Crash 64: `7c2d89f298119c8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046902`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE, a FLOAT PRIMARY KEY); INSERT INTO p (a) VALUES (NOT CURRENT_TIME); SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 65: `d6106055ceac762f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046988`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 66: `4f72097cb492781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047123`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 67: `79b2bcd545a31f6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047137`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(-92233
```

---

## Crash 68: `dd540970c313af55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049815`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES ((SELECT * FROM p GROUP BY CURRENT_TIME)); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TA
```

---

## Crash 69: `1d47b64d3fa4e746` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049825`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES ((SELECT * FROM p GROUP BY CURRENT_TIME)); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF N
```

---

## Crash 70: `27d5f069a5cadedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049835`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES ((SELECT * FROM p GROUP BY CURRENT_TIME)); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF N
```

---

## Crash 71: `25e37f9297d962d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049853`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES ((SELECT * FROM p GROUP BY CURRENT_TIME)); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF N
```

---

## Crash 72: `afab639dbe9fc980` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049919`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 73: `21d40340cceb6039` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050233`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); 
```

---

## Crash 74: `0d2419146abfc2b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050499`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSER
```

---

## Crash 75: `44b023e8c4488f6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050512`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); INSER
```

---

## Crash 76: `884b11e35aa6641f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050938`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (random()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (
```

---

## Crash 77: `f08dafd99196c78a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051217`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (NULL
```

---

## Crash 78: `9e95a791753b3943` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051907`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 79: `224d4cf6eb3ab599` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053409`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a + 0) UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (CURREN
```

---

## Crash 80: `5c89d5b32480aeb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053979`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE; 
```

---

## Crash 81: `ddc42b91f3971f71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054170`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (TRUE LIKE TRUE ESCAPE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p NATURAL JOIN p
```

---

## Crash 82: `57c1d03f9709a8f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055267`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (TRUE LIKE TRUE ESCAPE TRUE IS FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (c
```

---

## Crash 83: `741da11b564b7bfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055454`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); INSERT INTO p VALUES (CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CASE NULL WHEN CA
```

---

## Crash 84: `7fd1708a106500f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055799`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); VALUES (CURRENT_TIMESTAMP BETWEEN TRUE AND CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 85: `10dda64af2d73b56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057732`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_DATE LIMIT CURRENT_DAT
```

---

## Crash 86: `c31c6a556082066c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058329`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY TRUE HAVING TRUE LIMIT CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 87: `8898e8f72f5ef725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058811`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT CURRENT_DATE IS TRUE AS w FROM p WHERE EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLAC
```

---

## Crash 88: `006b240425772855` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059001`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT CURRENT_DATE IS group_concat(FALSE, '  h9 76_nl4o_--Az') AS w FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 89: `b4d8dd1e821a9ba6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059431`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIMESTAMP BETWEEN TRUE AND CURRENT_TIMESTA
```

---

## Crash 90: `bdeb53ad1206e235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059692`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY FALSE, NULL LIMIT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 91: `a56ac344331ae659` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059943`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY p.b LIMIT CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 92: `9d0bf1dee81730e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060311`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP AS f FROM p NOT INDEXED WHERE TRUE GROUP BY FALSE LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 93: `e58036e853198454` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061559`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE)) UNION ALL VALUES (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); IN
```

---

## Crash 94: `200f4224c9e0811a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061935`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_DATE DESC NULLS LAST, NULL ASC NULLS LAST); CREATE VI
```

---

## Crash 95: `6915945d00bc82e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062131`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY RAISE(IGNORE) ASC NULLS FIRST); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 96: `5733f925afd96908` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064954`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT NULL, rowid REAL NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INT
```

---

## Crash 97: `c284f369ed2c70cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065098`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; AN
```

---

## Crash 98: `41cbafea8cd57402` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065302`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (rowid,
```

---

## Crash 99: `5a490de41382da71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066599`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA
```

---

## Crash 100: `bd91cd8abae367b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066837`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME GLOB FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (r
```

---

## Crash 101: `b3c667e836626f0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067021`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, c3 FLOAT UNIQUE, c1 TEXT UNIQUE, a REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATU
```

---

## Crash 102: `0d61b17b937d3b4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (RAISE(IGNORE)) STORED, c3 FLOAT UNIQUE, rowid BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NATURAL JOIN 
```

---

## Crash 103: `e0b463c45058afd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068344`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT 773514869173620591667847.288092356060141441369933605448782900407894930804057321461762313494656646438641676784437507557646123743559662305373937573
```

---

## Crash 104: `1410d5e56c4d53ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068572`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT FALSE, * FROM p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 105: `337674a74cd277c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069395`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY, c1 FLOAT DEFAULT TRUE); WITH RECURSIVE t2 AS (VALUES (FALSE)) SELECT NULL FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO
```

---

## Crash 106: `d6eda1d1ad8b9bd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069990`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); WITH RECURSIVE t2 AS (VALUES (FALSE)) SELECT NULL OR FALSE AND NULL FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p
```

---

## Crash 107: `612ac92a1c746518` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071660`

```sql
SELECT printf('%.*s', 2147483648); SELECT round(-1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b); INSERT INTO t1 VALUES (CAST(NULL == TRUE COLLATE RTRIM | FALSE IS N
```

---

## Crash 108: `48b066a592717c19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074496`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); INSERT INTO p VALUES (TRUE); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p
```

---

## Crash 109: `c45bba2df31ee594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077013`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ISNULL ORDER BY CURRENT_DATE ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 110: `83d365541e1b30ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080059`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT *, * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () LIMIT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 111: `be979756596671a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080380`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () LIMIT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 112: `612812dca64be151` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080942`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () LIMIT CURRENT_TIME NOT IN (SELECT * FROM p WHERE CU
```

---

## Crash 113: `729e4f6adca8b321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082336`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT X'68F4Beec6a'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 114: `50a12fb142153fdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082573`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT 'E-_bTeX-_'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 115: `83202d4a389620c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowi
```

---

## Crash 116: `253b5720fa7a2d6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082831`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT CURRENT_DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; S
```

---

## Crash 117: `115b11b6e520e135` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083126`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY TR
```

---

## Crash 118: `58f712bdc40cc5a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084153`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY TR
```

---

## Crash 119: `1b557a4bb0d361cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084511`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT * FROM p NOT INDEXED WHERE NUL
```

---

## Crash 120: `417eff8b82370574` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089502`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c3 GENERATED ALWAYS AS (coalesce(a, b)) UNIQUE, b REAL GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 121: `233dee5811e3e5bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093684`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); SELECT ALL * FROM p LEFT JOIN q NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); I
```

---

## Crash 122: `9674f9f8806f0611` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X'39D5DfA0D7BE1E'); CREATE VIEW IF
```

---

## Crash 123: `39349320c75facbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094007`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b FLOAT, a GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UN
```

---

## Crash 124: `b7e218ccab067fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094193`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); SELECT printf('%f', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 125: `ddbae27846597771` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094292`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (NULL IS CURRENT_TIMESTAMP IS NOT FALSE)); CRE
```

---

## Crash 126: `90c8375b86c5fa1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094323`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB, c1 GENERATED ALWAYS AS (coalesce(a, b)) UNIQU
```

---

## Crash 127: `a628ad15eae98268` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094577`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); VALUES (TRUE); SELECT printf('%.*e', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---
