# Crash Triage Report

**Total crashes:** 190  
**Unique crash sites:** 190  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 190 | 190 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `e8500e03c0089d36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000262`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CASE CURRENT_TIME / FALSE IS NOT CURRENT_DATE < CURRENT_TIMESTAMP OR CURRENT_DATE WHEN TRUE / NULL COLLATE BINARY COLLATE BINARY THEN C
```

---

## Crash 2: `cd95ecb1d97020d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000321`

```sql
SELECT substr('s_--  G_Q- ljt- -  ', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR ABORT INTO t2 VALUES (CAST(typeof(NULL BETWEEN TRUE AND CURRENT_TIMESTAMP LIKE NULL ES
```

---

## Crash 3: `4a3330e961037ac4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000328`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (+CURRENT_DATE ISNULL, CURRENT_DATE AND TRUE); EXPLAIN QUERY PLAN SELECT CURRENT_DATE FROM p NOT INDEXED , q N
```

---

## Crash 4: `56efb047412b2a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000582`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT FALSE IN (FALSE LIKE RAISE(IGNORE) ESCAPE CURRENT_TIME, CURRENT_DATE) AS u__71_5_7_ndp_4z_y3_g9s5_or48pdy_vtk_40d03o9tn1___7_o1p4_q
```

---

## Crash 5: `30754108879fb841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000603`

```sql
SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c2 INTEGER, c3 GENERATED ALWAYS AS (a IS NULL) UNIQUE); SELECT NOT NOT CURRENT_TIME AS bsb_pf7__8232309mi_6l9z__k4_t_35__n_8_2n00
```

---

## Crash 6: `f2f11f021214507f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001469`

```sql
SELECT substr('Rm_M_ _-_ 5_ _0', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s (c1) VALUES (FALSE ISNULL IS NULL NOT LIKE count(b) FILTER (WHERE -CURRENT_TIMESTA
```

---

## Crash 7: `6604bd64a54f0e2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002026`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, a REAL GENERATED ALWAYS AS (NULL) VIRTUAL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM
```

---

## Crash 8: `3696fe7f97b21fba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002399`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL NOT LIKE NOT EXISTS (VALUES (NULL)) < CURRENT_TIME ISNULL); PRAGMA 
```

---

## Crash 9: `36be5939b7a1e982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002447`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 10: `27062c1d050354ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 11: `6a6c9475f3f722fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002459`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_TIMESTAMP ISNULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 12: `abd00bf2c6dc3b1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002466`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL NOT LIKE FALSE < CURRENT_TIME ISNULL); PRAGMA integrity_check; CREA
```

---

## Crash 13: `f6cc39718218bdd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002486`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL NOT LIKE CURRENT_DATE ISNULL); PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 14: `ba30fc5e84348424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002508`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES ((c1 MATCH +RAISE(IGNORE) COLLATE BINARY IS NOT NULL IN (EXISTS (VALUES (NULL) LIMIT 
```

---

## Crash 15: `42e0063bed6162bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002515`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 16: `3444feb7e85b7f25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003048`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); EXPLAIN QUERY PLAN SELECT ALL * FROM q NOT INDEXED ORDER BY FALSE NOTNULL ASC NULLS FIRST LIMIT FA
```

---

## Crash 17: `c513569225fed44b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003065`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); VALUES (CURRENT_DATE); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 18: `47518c4c8c3ea240` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003218`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 TEXT); VALUES (FALSE); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 19: `b81338b3d748bb45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003251`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 TEXT); VALUES (FALSE); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p
```

---

## Crash 20: `d193511f071a35c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003397`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8
```

---

## Crash 21: `bc88cab5dbbe45a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003473`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE
```

---

## Crash 22: `7066bc9150088e72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003484`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE
```

---

## Crash 23: `58c69e6cda031df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003492`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE
```

---

## Crash 24: `9d795b03344f3f6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003498`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE
```

---

## Crash 25: `d7b58e443e9d70b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005667`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (b) VALUES (CASE WHEN NULL ISNULL THEN ~CURRENT_TIMESTAMP ELSE -RAISE(IGNORE) END, EXISTS (VALUES (~TRU
```

---

## Crash 26: `07f4dc292ae8f918` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005748`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 27: `faae9b3457f367c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006967`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (NOT -TRUE) VIRTUAL, c3 FLOAT NOT NULL DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 28: `a4d2769f0a0286c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006987`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT I
```

---

## Crash 29: `40a358069a16498e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006993`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE, c3 FLOAT NOT NULL DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 30: `249dc5ae87c6bceb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007001`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE, c3 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 31: `2e7309c27736b51c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007015`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE, c2 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 32: `363eeba97b5c133b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007030`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 33: `e10fd54c12b1772d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007448`

```sql
SELECT printf('%.*f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE q (rowid) AS (SELECT FALSE AS amky_ylczm_iy73p_9905v5397h50auow0_a_bch8__p4_r5__xn9_8j_
```

---

## Crash 34: `86210d0e6ebdc4a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007725`

```sql
SELECT printf('%.*d', 9223372036854775807, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT RAISE(IGNORE) UNION SELECT DISTINCT NOT FALSE -> NOT NOT CURRENT_TI
```

---

## Crash 35: `398b19af3e3bdf5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007804`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT EXISTS (SELECT DISTINCT p.* FROM p NOT INDEXED NATURAL LEFT JOIN p INDEXED BY a INTERSECT SELECT ~CU
```

---

## Crash 36: `1bb90e7828fa6b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008219`

```sql
SELECT printf('%.*g', 4294967296, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); SELECT *; CREATE TABLE IF NOT EXISTS p(c2 FLOAT, c3 GENERA
```

---

## Crash 37: `723cdff898e644db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008246`

```sql
SELECT round(-1e308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT p.* FROM p WHERE (+TRUE) AND CASE WHEN FALSE C
```

---

## Crash 38: `b596dec49f7ba1bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008353`

```sql
SELECT round(-1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO p VALUES (TRUE); ANALYZE p; CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIMESTA
```

---

## Crash 39: `18c921c85082c335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008502`

```sql
SELECT printf('%.*e', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES ((CURRENT_TIME)); SELECT printf('%.*f', -2147483649, 1.0); CREATE TABLE IF 
```

---

## Crash 40: `35de97db2713d0b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008509`

```sql
SELECT printf('%.*g', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO r (a, c3) VALUES (json_valid(FALSE COLLATE NOCASE NOT NULL == unicode(~RAISE(IGNORE) C
```

---

## Crash 41: `3e420883cc3116be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008607`

```sql
SELECT printf('%.*e', -1); SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t3.*; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); REPLACE INTO t1 VALUES (C
```

---

## Crash 42: `adfb49b68e175c5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008778`

```sql
SELECT substr('H ___', 2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH q AS (SELECT CURRENT_TIMESTAMP EXCEPT SELECT DISTINCT RAISE(IGNORE), r.* FROM p CROSS JOIN q NOT 
```

---

## Crash 43: `3e2025e77bf807d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008896`

```sql
SELECT round(0.01, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c3) VALUES (CURRENT_DATE, TRUE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENER
```

---

## Crash 44: `7a572d7b78d091b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008992`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); SELECT NOT EXISTS (SELECT * ORDER BY CASE WHEN FALSE IS DISTINCT FROM NULL GLOB CURRENT_DATE THEN CURRENT_TIM
```

---

## Crash 45: `95ee90bf0e100030` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009016`

```sql
SELECT printf('%.*f', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 DEFAULT VALUES; VALUES (CURRENT_TIME, CAST(RAISE(IGNORE) AS TEXT)) UNION SELECT p.*, 
```

---

## Crash 46: `a317c6ca9c98a1d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009988`

```sql
SELECT printf('%.*g', -2147483649, 0.01); SELECT hex(zeroblob(0));
```

---

## Crash 47: `0d5e0bbcc268e891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010842`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (VALUES (TRUE) EXCEPT SELECT * FROM p NOT INDEXED); SELECT printf('%.*g',
```

---

## Crash 48: `69559ab2cdd16323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011808`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 49: `d98216fa6e5765f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012216`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); CREATE
```

---

## Crash 50: `2182d708a37a3f2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012225`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); CREATE
```

---

## Crash 51: `9a48d01ae461ad5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012234`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); CREATE
```

---

## Crash 52: `0818fba3b3d798bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012243`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(1)); CREATE
```

---

## Crash 53: `b5667493fa3b00bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013339`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (-TRUE) VIRTUAL, c3 FLOAT NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_
```

---

## Crash 54: `fb69e6021de06227` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013927`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); CREATE 
```

---

## Crash 55: `2040e724cb125b8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014145`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALU
```

---

## Crash 56: `089f9e758ed6faf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015943`

```sql
SELECT substr('J8C_ _  --__   6s', 0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b); INSERT OR FAIL INTO q VALUES (CASE WHEN TRUE = NULL != (VALUES ((FALSE)) EXCEPT SE
```

---

## Crash 57: `31f422320d40c3b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016510`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 58: `d3b6afec7a2267f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017353`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB NOT NULL, c1 DATE); INSERT OR FAIL INTO q VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (C
```

---

## Crash 59: `63a5fe7eab92739e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017697`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES ((upper(-NULL IS NOT NULL ->> CURRENT_DATE = ~FALSE COLLATE RTRIM NOT LIKE CURRENT_DATE /
```

---

## Crash 60: `b001549cd91bb98b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019671`

```sql
SELECT printf('%.*d', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 61: `d37d9d6230299568` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020837`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c1); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 62: `dad1372a9b53fa3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020844`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 63: `68d251906a3fd75a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020851`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 64: `2b02af34f407a72f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020961`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 65: `8665ee321f765382` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020992`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 66: `ec73c76183eb7d23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023320`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (CURRENT_TIMESTAMP)); WITH RECURSIVE r AS (SELECT *) INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 67: `859eb0ab480e4a6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024787`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT NULL >> count(DISTINCT FALSE) AS l62v FROM q; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 68: `3e5c0943c88a93cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025195`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT substr('sGc', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, b, b); SELECT * FROM p NOT INDEXED UNION ALL SELECT NULL 
```

---

## Crash 69: `05076a33874d96c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025254`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT * FROM q; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 70: `09c5d61781de1b66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025263`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT NULL >> random() AS l62v FROM q; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 71: `4a239c0414a8e895` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025562`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE q (c3) AS (SELECT DISTINCT * FROM p ORDER BY CURRENT_DATE DESC NULLS FIRST) SELECT * FROM q; SELECT 
```

---

## Crash 72: `e54eb7541dc01838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025905`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE q (c3) AS (SELECT DISTINCT * FROM p ORDER BY NOT NULL DESC NULLS LAST) SELECT NULL >> random() AS l6
```

---

## Crash 73: `4b8aeced64811b4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026346`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE q (c3) AS (SELECT DISTINCT * FROM p NATURAL LEFT JOIN p ORDER BY CURRENT_TIMESTAMP ASC) SELECT * FRO
```

---

## Crash 74: `8c1362abdc3a355f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026788`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE q (c3) AS (SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED ORDER BY TRUE DESC NULLS LAST) S
```

---

## Crash 75: `bf8a27e26fb08884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027960`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE RAISE(IGNORE) GROUP BY NULL WINDOW w1 AS (), w2 AS () LIMIT CURRENT_DATE; E
```

---

## Crash 76: `e47c64fb96055e5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030616`

```sql
SELECT substr('M6___6Ou', 4294967296, -9223372036854775808); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 77: `213adbb5e24e7caf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030758`

```sql
SELECT printf('%s', -2147483649, '0 -oi  XA_   '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check;
```

---

## Crash 78: `d7ec93fdfdb615a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030893`

```sql
SELECT printf('%.*s', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 79: `d667a23249f0c1f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031100`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CURRENT_TIME + FALSE)); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUE
```

---

## Crash 80: `673e6d75d8042d77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037289`

```sql
SELECT round(1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (RAISE(IGNORE)) INTERSECT VALUES (RAISE(IGNORE));
```

---

## Crash 81: `e9ca4b895d479cff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037464`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT OR IGNORE INTO p VALUES (CASE WHEN CURRENT_TIME IS NOT FALSE THEN FALSE END); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 82: `7a02e6e4fed4c7fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037671`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT -548408343280186659027602515.796834861435992680378917632813670430487430297333341092728446815e13, a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALU
```

---

## Crash 83: `8f8c0fae711f94e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037999`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_4__xzo3gz3
```

---

## Crash 84: `e6533af4139b371c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038161`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_4__xzo3gz3
```

---

## Crash 85: `6f9c04fb1b51e92d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038668`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 TEXT); VALUES (NULL) INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 86: `6b4fff82c99cd672` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038911`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 TEXT); SELECT * FROM p GROUP BY CURRENT_TIME INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 87: `e2f2540278335061` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040137`

```sql
SELECT round(-1.0, -2147483649); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 88: `d70a04cec8971a0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041845`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL NOT LIKE NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 89: `5af7cc83f3b9f228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042730`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIM
```

---

## Crash 90: `1b977c016570328a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043310`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE < CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 
```

---

## Crash 91: `2435b53762f6f8cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043503`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL < CURRENT_TIME); PRAGMA quick_check; SELECT printf('%.*f', 21474836
```

---

## Crash 92: `5afcfc8272a6cf10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044453`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY
```

---

## Crash 93: `e93b8cfc605cd8aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047434`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, a REAL GENERATED ALWAYS AS (NULL) VIRTUAL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM
```

---

## Crash 94: `bd291e6aa74ab54a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048075`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT CURRENT_TIMESTAMP FROM q WHERE EXISTS (SELECT DISTINCT * FROM p WHERE FALSE ORDER BY NULL DESC NULL
```

---

## Crash 95: `ecbcd55970eece2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049986`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NUL
```

---

## Crash 96: `14802422948ba02c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN CHECK (TRUE)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 97: `433ce52dacba9a06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051251`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED WHERE FALSE ORDER B
```

---

## Crash 98: `605cc13cbddc90dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051461`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT *, count(*) OVER () AS ae0bh1 FROM q WHERE EXISTS (VALUES (CURRENT_TIME)); SELECT printf('%.*g', -21
```

---

## Crash 99: `b607e311c72e8214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051679`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, a REAL GENERATED ALWAYS AS (NULL) STORED); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABL
```

---

## Crash 100: `aa1f123ab93777f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051886`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 101: `6881c2ad9a82d376` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051931`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM p WHERE FALSE ORDER BY NULL DESC NULLS LAST, count(*) OVER () AS
```

---

## Crash 102: `95e79cb2eac5bf2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052332`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 FLOAT PRIMARY KEY, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT DI
```

---

## Crash 103: `82331fa8b588315f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052373`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHER
```

---

## Crash 104: `df8fdb29c7a65543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054392`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL);
```

---

## Crash 105: `b326fe418a8cda0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054423`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); 
```

---

## Crash 106: `46f6cd0c3de0cefd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054518`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*s', -1, 1e-308); CREATE VIRTUAL 
```

---

## Crash 107: `9c04159e6397a89e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INT CH
```

---

## Crash 108: `9c42e0e4675f264e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056251`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE FALSE GROUP BY NULL HAVING
```

---

## Crash 109: `51fe55341a8f4616` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057326`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 N
```

---

## Crash 110: `b02b0b4f9cbd790e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 N
```

---

## Crash 111: `f0197602af06b58e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057361`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 N
```

---

## Crash 112: `31a7a3365cf518ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057972`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT UNIQUE); INSERT OR IGNORE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DA
```

---

## Crash 113: `970a69c25d3ad6c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059136`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); SELECT * FROM p NATURAL LEFT JOIN p NOT INDEXED GROUP BY CURRENT_TIME INTERSECT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 114: `d1031c12b7cafe61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059969`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE, TRUE WINDOW w1 AS () OR
```

---

## Crash 115: `0ea60031944f9bfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060385`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); EXPLAIN QUERY PLAN SELECT ALL * FROM p JOIN q NOT INDEXED ORDER BY CURRENT_TIMESTAMP DESC LIMIT TR
```

---

## Crash 116: `b90e563eae02b0af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061461`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_4__xzo3gz3
```

---

## Crash 117: `0619e14619b27135` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061867`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT count(*), * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_
```

---

## Crash 118: `d2c0397d363de8a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062229`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_4__xzo3gz3
```

---

## Crash 119: `f615fc88e8b3640b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062786`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE NOT NULL); SELECT * FROM q JOIN q b_d01t______9d_gkp_b8tu8u__93oi_7_r7_p_9_oa8_07gf_j6e129ih9_632_o1il_4__xzo3gz3
```

---

## Crash 120: `97f899e18f7dc794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063321`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (CAST(NULL <> CURRENT_TIMESTAMP % CURRENT_TIME AS VARCHAR(255))), c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREAT
```

---

## Crash 121: `941fabf94333feb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063660`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); WITH RECURSIVE r AS (SELECT *) INSERT INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREA
```

---

## Crash 122: `9bbbabdc5a671518` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063763`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 123: `71ec22738408818e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063971`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (CASE WHE
```

---

## Crash 124: `97ade86f5ad267a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063990`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT CHECK (NULL >> NULL >> NULL >> NULL >> NULL >> NULL >> CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 125: `c14d9e7e12d4c841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064367`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE, c3 REAL, c2 NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (RAISE(IGNO
```

---

## Crash 126: `ef5e6e64ae7a9e62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064688`

```sql
SELECT substr('nX-FtBS', 4294967295, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (RAISE(IGNORE)) INTERSECT VALUES (RAISE(IGNORE));
```

---

## Crash 127: `5845fd7ba4fd1361` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065026`

```sql
SELECT printf('%.*f', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b); INSERT OR FAIL INTO q VALUES (RAISE(IGNORE) - CURRENT_DATE GLOB TRUE LIKE CASE -CURRENT_TIME NOT IN (FALSE)
```

---

## Crash 128: `47c93f1552e73237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065151`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c3 TEXT); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT * FROM q JOIN q b_d01t______9d_gkp
```

---

## Crash 129: `da4c76490a7ca0a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068562`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY NULL ORDER BY TRUE DESC NU
```

---

## Crash 130: `8180ae77464e01c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068818`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME LIKE FALSE IN (VALUES (min(NULL)))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 131: `84f581f2942dbecf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069047`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP << CAST(CURRENT_TIMESTAMP BETWEEN CURRENT_TIMESTAMP AND TRUE AS VARCHAR(255))); VALUES (CURRENT_DATE); C
```

---

## Crash 132: `627fc6f66bcbf3d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069207`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP << CAST(CURRENT_TIMESTAMP AS VARCHAR(255))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 133: `1becaeca4940519d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069343`

```sql
SELECT printf('%s', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c1, c1); SELECT ALL * FROM r NOT INDEXED UNION ALL VALUES (NULL) UNION ALL SELECT ALL *
```

---

## Crash 134: `85ba115b21a77ca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069529`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP << CURRENT_TIME COLLATE NOCASE NOTNULL LIKE FALSE IN (VALUES (CURRENT_DATE))); VALUES (CURRENT_DATE); SE
```

---

## Crash 135: `41e5016d595e9e1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071540`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 136: `c918992fcacce5da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073166`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT OR IGNORE INTO p VALUES (CASE WHEN TRUE AND TRUE THEN TRUE END); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 137: `8663d7812f01d2ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073908`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME IS NOT TRUE COLLATE RTRIM); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VAL
```

---

## Crash 138: `365e0f88d5ca0088` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074120`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME IS NOT CAST(CURRENT_TIMESTAMP AS VARCHAR(255)) COLLATE RTRIM); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 139: `a368b2098bf8ae88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074385`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME IS NOT (SELECT DISTINCT * FROM p)); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 140: `1877ea0fa082d47f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074575`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY NULL WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 141: `fc73d2ce4a82a0bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074788`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE, TRUE WINDOW w1 AS (); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 142: `b3bba6a6848da5c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075103`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (); SELECT printf('%.*g', -2147483649, 0.01)
```

---

## Crash 143: `65cdda3e2b81b376` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082039`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE q (c3) AS (SELECT DISTINCT TRUE FROM p ORDER BY TRUE DESC NULLS LAST) SELECT * FROM q; SELECT printf
```

---

## Crash 144: `471e6318dc227644` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084804`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INT); WITH RECURSIVE p AS (VALUES (RAISE(IGNORE))) SELECT count(*) AS l62v FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 145: `973901ffc1615a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085127`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); WITH RECURSIVE q (c3) AS (SELECT DISTINCT * FROM p ORDER BY CURRENT_DATE DESC NULLS FIRST) SELECT * FROM q; CREATE
```

---

## Crash 146: `f1d57b69a6ffe6c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086598`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b GENERATED ALWAYS AS (a) NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 147: `144c4c91955ff2b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086649`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN DEFAULT 077515277034007173306911.7E+9730, rowid NUMERIC NOT NULL); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELE
```

---

## Crash 148: `87982235b1e0150d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087043`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT min(CURRENT_TIME) AS l62v FROM q; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 149: `64c15930e4ec57ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087131`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT count(*) AS l62v FROM q; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 150: `cb0ffce04033e5f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087653`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT NULL >> NULL >> NULL >> NULL >> NULL >> NULL >> NULL >> NULL >> NULL >> CURRENT_DATE AS l62v F
```

---

## Crash 151: `3a79bc3dba77cce2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087871`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q (c3) AS (VALUES (NULL)) SELECT FALSE >> CURRENT_DATE AS l62v FROM q; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 152: `eabab0ba029ae3af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090233`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 153: `301b4a6b09ad52f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090802`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL DEFAULT CURRENT_DATE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 154: `ddd1d1d7fc76ed70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090974`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY
```

---

## Crash 155: `bc3f461d3f276170` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE 
```

---

## Crash 156: `18b79a533bca940f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091060`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 157: `ce06ebc177d16bf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091069`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN, rowid GENE
```

---

## Crash 158: `e6f34275717ceacd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094019`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT NOT NULL); INSERT INTO q VALUES (FALSE OR CURRENT_DATE) ON CONFLICT DO NOTHING; VALUES (TRUE); CREATE VIRTUAL TAB
```

---

## Crash 159: `225928eb4cb5b473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094481`

```sql
SELECT printf('%f', -9223372036854775808, 'n-x-q'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (count(*) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST, CURRENT_DATE ASC NULLS L
```

---

## Crash 160: `90963062c4c46448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095987`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT INTO p SELECT * FROM p NOT INDEXED; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (CURRENT_TIMESTAMP); 
```

---

## Crash 161: `544bac34cecdc6cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096611`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT INTO p SELECT DISTINCT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () AS ae0bh1 FROM p; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 162: `a57c74d0382eaa06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096921`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT INTO p SELECT DISTINCT rowid FROM p; VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 163: `4e9dbefd9c21eabe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099886`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT OR FAIL INTO q VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT prin
```

---

## Crash 164: `975cd464dc2e0052` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100326`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB NOT NULL, c1 REAL UNIQUE); INSERT OR FAIL INTO q VALUES (CURRENT_TIME, CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VA
```

---

## Crash 165: `19a74607ef18420a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p GROUP BY FALSE; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 166: `278ff4a77e6556e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106415`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT FALSE COLLATE NOCASE AS a FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 167: `aae2408071d3e44e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106591`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT *, * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); IN
```

---

## Crash 168: `c5c6482f473bb018` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107231`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE TRUE MATCH CURRENT_TIME) AS sub1; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 169: `32964c515f600eb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107527`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT GENERATED ALWAYS AS (NULL > FALSE) VIRTUAL, a REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TA
```

---

## Crash 170: `a829af29290374f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107755`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT CURRENT_DATE / FALSE, * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 171: `4717335caeefcd81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107991`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME NOT LIKE CURRENT_DATE NOT IN (TRUE, CURRENT_DATE)) AS sub1; CREA
```

---

## Crash 172: `41df4e03393d092a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108864`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (CAST(NULL <> CURRENT_TIMESTAMP % CURRENT_TIME AS VARCHAR(255))), c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT
```

---

## Crash 173: `fd562e8cbae59eb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110096`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT -8.99114505359815764490263553877344197470670608800E1396655394602284627947); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUE
```

---

## Crash 174: `00dd563922275988` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110403`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT -548408343280186659027602515.796834861435992680378917632813670430487430297333341092728446815e13, a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELE
```

---

## Crash 175: `5bf87fefd369f230` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110591`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT 077515277034007173306911.7E+9730); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf(
```

---

## Crash 176: `cb55dc530ebc17e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112347`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 REAL CHECK (NULL LIKE NULL ESCAPE NULL)); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.0
```

---

## Crash 177: `d0edadec96c2be5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112898`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(a INT UNIQUE, c2 NUMERIC UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 178: `101cfc87b2ee2cf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113039`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO q
```

---

## Crash 179: `73f1ebbe48b1f7fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114537`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (SELECT DISTINCT CURRENT_DATE AS ae0bh1 FROM p); CREATE VIRTUAL TABLE IF 
```

---

## Crash 180: `1fda8858ae3afd5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (TRUE NOT LIKE CURRENT_TIMESTAMP), a INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 181: `4825525c61d493cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115894`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); SELECT * FROM q JOIN p q_ ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 182: `fd032b6f99599b20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115956`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (VALUES (TRUE) UNION SELECT * FROM p NOT INDEXED); CREATE VIRTUAL TABLE I
```

---

## Crash 183: `5d3f686ef41a6569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116178`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (VALUES (TRUE) INTERSECT SELECT * FROM p NOT INDEXED); CREATE VIRTUAL TAB
```

---

## Crash 184: `0e04d8f9e2b90350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116393`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (SELECT * FROM (VALUES (FALSE)) AS v253ls_5j0f_e__tk9ow77_____h____6_q_lm
```

---

## Crash 185: `e5690a1ef84e951b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116792`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON FALSE % FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 186: `b4d7e09aac551162` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117121`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); V
```

---

## Crash 187: `55b9eca313f82b14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117650`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (VALUES (TRUE) UNION VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF
```

---

## Crash 188: `0c9e933270ff5059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117975`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL DEFAULT -548408343280186659027602515.796834861435992680378917632813670430487430297333341092728446815e13, a BOOLEAN); CREATE TABLE IF NOT EXISTS q(
```

---

## Crash 189: `46d6880a9fbf8f2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118449`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT); SELECT * FROM q JOIN p q_ ON (VALUES (TRUE) EXCEPT VALUES (CAST(NULL AS TEXT))); SELECT printf('%.*f',
```

---

## Crash 190: `e5d6540a0514db1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121869`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL UNIQUE); INSERT INTO q DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', 2147483647, 1e308);
```

---
