# Crash Triage Report

**Total crashes:** 212  
**Unique crash sites:** 212  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 212 | 212 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `72361d808d916d12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000153`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_DATE; SELECT printf('%lli', 0, ''); CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 FLOAT GENERATED ALWAY
```

---

## Crash 2: `3d70f47e2ebe7424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000221`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN, rowid GENERATED ALWAYS AS (a || b) NOT NULL); INSERT OR ROLLBACK INTO q VALUES (CAS
```

---

## Crash 3: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000349`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 4: `52899a2ee4ad91e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000770`

```sql
SELECT substr('d2_-5ex6_  --_', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO t2 VALUES (last_insert_rowid() FILTER (WHERE -RAISE(IGNORE) GLOB RAISE(IG
```

---

## Crash 5: `338186a5cdcfcf67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000959`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT OR ABORT INTO p VALUES (CURRENT_DATE AND CURRENT_DATE * NULL NOTNULL NOT NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS 
```

---

## Crash 6: `3e12eb844b4b8d78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001053`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES (NULL IS NULL LIKE NOT NOT RAISE(IGNORE) IS FALSE ->> CURRENT_DATE NOTNULL E
```

---

## Crash 7: `d145c4744999089b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001258`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, b); INSERT OR ROLLBACK INTO p VALUES (CASE WHEN NOT EXISTS (SELECT p.* FROM q NOT INDEXED WHERE CURRENT_TIME GROUP BY TRUE != NULL
```

---

## Crash 8: `590a7a9324b94b0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001536`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1); SELECT s.* FROM q JOIN p z_xadl_j_u82y_kw3a__8___et__x6_1__u__q19_hg ON -NULL IS NOT RAISE(IGNORE) > TRUE IS 
```

---

## Crash 9: `51bfbce708d55598` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003367`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 10: `27aa7e591165cc85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT q.* FROM q NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INT
```

---

## Crash 11: `72d755806df8a2a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005843`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q (c1, c3) VALUES (CURRENT_TIME, RAISE(IGNORE)) ON CONFLICT(b) DO UPDATE SET _rowid_ = -RAISE(IG
```

---

## Crash 12: `10211552e251a33a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005996`

```sql
SELECT substr('__-', 9223372036854775807); SELECT hex(zeroblob(-2147483648)); SELECT printf('%lld', 2147483648, 'Z-Y-w-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR REPLAC
```

---

## Crash 13: `e8cb48e3566b93a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006411`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t3 VALUES (~CASE ~CURRENT_TIMESTAM
```

---

## Crash 14: `cd89e4c196170b26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007949`

```sql
SELECT printf('%x', 1, ' S 7u '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; SELECT FALSE; SELECT substr('-0NO_0D4lMKYRo0 F_', 2147483647, -2147483648);
```

---

## Crash 15: `d9f19c3b01b8388e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015749`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-21474836
```

---

## Crash 16: `728cf644c2939d37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019176`

```sql
SELECT printf('%.*e', -2147483649, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (TRUE IS NOT NULL AND +CURRENT_TIME != TRUE - NULL || typeof(NULL) == TR
```

---

## Crash 17: `04a2f41a79198ba5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019374`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (CURRENT_DATE >= CURRENT_TIME BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP), b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); EXPLAIN 
```

---

## Crash 18: `fae05e363a4d1af5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019386`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAUL
```

---

## Crash 19: `688c3181bafca730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019393`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (NULL IS NOT NULL < TRUE)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAULT VAL
```

---

## Crash 20: `73406ecce8998d1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019408`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT X'C2C0'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 21: `49bc32fe63d8e112` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019444`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, 
```

---

## Crash 22: `78e5efed29ee92c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019475`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT
```

---

## Crash 23: `4293afbcea2598f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019542`

```sql
SELECT printf('%.*d', -2147483649, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME);
```

---

## Crash 24: `999dda3cff9796a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021092`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 25: `73a1434181923c25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021453`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT DEFAULT 0, c1 INTEGER UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALUES (+CAST(TR
```

---

## Crash 26: `5b3a105469604820` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021588`

```sql
SELECT printf('%.*s', -9223372036854775808, 1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 27: `4749717f531fa50b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021729`

```sql
SELECT printf('%.*d', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN WITH RECURSIVE r AS NOT MATERIALIZED (WITH p (c2) AS (SELECT DISTINCT p.* FROM p
```

---

## Crash 28: `290e921cdbac0dec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021844`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 29: `b6652b73b3d00eab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023097`

```sql
SELECT round(0.01, 4294967296); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 30: `104a8ff3382a4bfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023144`

```sql
SELECT round(0.01, 4294967296); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 31: `9153e79e1da28331` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024254`

```sql
SELECT substr('', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT count(CURRENT_DATE > (TRUE) - TRUE) FROM (SELECT p.*, TRUE FROM t2 WHERE json_object('-W9_CbN_ _6--M  '
```

---

## Crash 32: `08328be844157664` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024948`

```sql
SELECT printf('%.*g', 0, -1.0); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 33: `f422922d082a2fb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027345`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND FALSE % CURRENT_DATE - CURRENT_TIMESTAMP LIKE TRUE IS NULL | TRUE 
```

---

## Crash 34: `e419326c7c184ae4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027793`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (NULL - CURRENT_DATE NOT IN (CURRENT_DATE)); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 35: `c60936b8389d36d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027898`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (NULL - CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 36: `27cef239c3477632` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028085`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND TRUE - NULL); PRAGMA integrity_check; SELECT printf('%.*g', 214748
```

---

## Crash 37: `e7da604464e4401a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029406`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT VALUES; VALUES (RAISE(IGNORE) COLLATE RTRIM) LIMIT total_changes() FILTER (
```

---

## Crash 38: `3aec548cb11cdf01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031847`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT 
```

---

## Crash 39: `e30069599d10a2b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032208`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 40: `092c2919b8f54055` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032593`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE (VALUES (TRUE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 41: `7e3245e9bc6ec547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033053`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE (SELECT * FROM q NOT INDEXED LIMIT CURRENT_TIME, FALSE IN (VALUES (CURRENT_
```

---

## Crash 42: `0f0d7e22cd527d1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034630`

```sql
SELECT printf('%d', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r SELECT *, q.* FROM p WHERE max(NULL COLLATE NOCASE) FILTER (WHERE RAISE(IGNORE) COLLATE RT
```

---

## Crash 43: `f2eff099e83ff33d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034756`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELEC
```

---

## Crash 44: `acec66386027d116` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036034`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO p VALUES (7); SELECT FALSE - -TRUE, RAISE(IGNORE) FROM t1 JOIN p k23lry6w2_l2gu ON CURRENT_TIMESTA
```

---

## Crash 45: `75fb7d1095e7bb87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036553`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE s AS (VALUES (-CURRENT_DATE) ORDER BY CURRENT_TIME LIMIT CURRENT_DATE OFFSET CURRENT_DATE) S
```

---

## Crash 46: `366c207109b0215b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037018`

```sql
SELECT round(0.0, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 47: `fa89c7344099fbd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043361`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE >> CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 48: `e1dfb74a963db416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044162`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE nullif(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE 
```

---

## Crash 49: `a43ff71976dc2c47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044257`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE total_changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 50: `70071826c3c28712` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045995`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE nullif(CURRENT_TIMESTAMP, NULL); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 51: `cccbc525d1deeae0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048139`

```sql
SELECT printf('%.*s', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO p VALUES (FALSE IS NOT NULL); SELECT * FROM r NATURAL JOIN q WHERE CURRENT_TIMESTAMP COLLATE NO
```

---

## Crash 52: `f0801ab9523426be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048261`

```sql
SELECT round(1e-308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH q AS MATERIALIZED (SELECT t2.*, q.* FROM s LEFT OUTER JOIN q AS o_9y ON count(*) <> NOT TRUE | NULL IN (CURRENT_T
```

---

## Crash 53: `2ce7e95d0c3b7014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048437`

```sql
SELECT substr('y2- Vv6e Q-8 utM_', 9223372036854775807, -2147483649); SELECT printf('%.*d', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR IGNORE INTO s VALUES (-0640.864
```

---

## Crash 54: `78a4c850d6a8e8bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048969`

```sql
SELECT substr(' _G Pf 1n_', 2147483647, 9223372036854775807); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 55: `3471f3983b79e2a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049067`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_TIME, CURRENT_DATE) ON CONFLICT DO NOT
```

---

## Crash 56: `490134da73ecefbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050341`

```sql
SELECT round(-1e308, -1); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 57: `ef009efe999070c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051799`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE ~NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH 
```

---

## Crash 58: `8e8acf4ddf581c70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054699`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE length(CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 59: `8e7b832dc14ae88c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055185`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF N
```

---

## Crash 60: `66c465e311121709` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057297`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE nullif(FALSE, CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647,
```

---

## Crash 61: `f9329fb6a3a8d997` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057413`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 62: `681481749a6553d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057470`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP LIKE FALSE; SELECT printf('%.*f', 2147483647, -1e
```

---

## Crash 63: `67132bf37104a36f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059217`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT NULL AS t03c FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 64: `3f24cbbee1dc7f64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060296`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL COLLATE BINARY IN (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 65: `3db9b0b9b9ce586d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060529`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE < TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 66: `912e6f8aa5f42ee0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060856`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE ' _T v_M6n' >> CURRENT_DATE; SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 67: `5b833111c5429129` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061236`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 68: `111eed99f52049a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066010`

```sql
SELECT substr('', 9223372036854775807); SELECT round(-1.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (CURRENT_TIME BETWEEN +NULL IS 
```

---

## Crash 69: `851d981a76da74ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067746`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT CURRENT_TIME ORDER BY CURRENT_TIME DESC NULLS FIRST LIMIT TRUE; PRAGMA quick_check; SELECT p
```

---

## Crash 70: `2ce56d56680bd148` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068663`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME AS rce_gx_ilrnd47vy5l8__5_ FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 71: `cd6af98fa372e24b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069114`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN DEFAULT 1163068667629.6e+36559827856367043635182455653); INSERT INTO p (_rowid_) VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 72: `5f89fbcad044c9d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071812`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a + -0) ); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c1, a)
```

---

## Crash 73: `bbd7bcdddac8bbe4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075123`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE FALSE IN (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY N
```

---

## Crash 74: `6d95420e4b16abd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076139`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT group_concat(CURRENT_TIME, '') OR CURRENT_TIMESTAMP FROM q NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TAB
```

---

## Crash 75: `7ed2e42bd960b739` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076198`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT count(*) OR CURRENT_TIMESTAMP FROM q NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 76: `efa6e17ca9c323c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076529`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE FALSE IN (SELECT * FROM q NOT INDEXED LIMIT CURRENT_TIME, FALSE IN (SELECT 
```

---

## Crash 77: `40a66124eadb097e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076951`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE, b BLOB NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 78: `b565c52f3974893b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077642`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE (SELECT DISTINCT * FROM p); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 79: `7e1fd8a123566ab0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077804`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NOT INDEXED GROUP BY CURRENT_DATE ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL TA
```

---

## Crash 80: `d5cbde2464adc197` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078313`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 DATE CHECK (CURRENT_TIME MATCH TRUE NOT NULL < TRUE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 81: `b16d4e795075e027` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q JOIN p d__rq ON CURRENT_TIMESTAMP LIKE CURRENT_TIME ESCAPE FALSE; SELECT printf('%.*f', 21474836
```

---

## Crash 82: `376c895ab66e4926` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082858`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND CURRENT_DATE; CREATE VIRTUAL TAB
```

---

## Crash 83: `105c89066ef64153` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083127`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE, b REAL DEFAULT -2875353187.3E-2); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT substr('', 2147483647)
```

---

## Crash 84: `cf7a6f95823f13f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083209`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT substr('', 2147483647); CREATE VIRT
```

---

## Crash 85: `5765c5bf61d2550b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083217`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ DATE, b REAL DEFAULT CURRENT_DATE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT substr('', 2147483647); CR
```

---

## Crash 86: `01ec59221775cc06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086060`

```sql
SELECT printf('%.*e', -2147483648, 0.01); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 87: `40b0244f3f25780e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086508`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (), CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 88: `d1e2983105f242d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086758`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 89: `38f7950e7dda8b82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087266`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_DATE, rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREA
```

---

## Crash 90: `662aef71730da790` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (FALSE IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 91: `7998dfe335b572c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087966`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIMESTAMP OR TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WIT
```

---

## Crash 92: `47825d88ee0315aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088241`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 93: `5891dd463821c071` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088645`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (
```

---

## Crash 94: `40da4976d0ca5a85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088657`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (
```

---

## Crash 95: `bd9552069420c702` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089194`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN DEFAULT 80084.649959363682137370); INSERT INTO p (_rowid_) VALUES (TRUE | TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 96: `e7675b61ece79dc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089586`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE - FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSE
```

---

## Crash 97: `c675a48bd3e77f80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090557`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIME - X''); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 98: `b2cfa94908592994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091029`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIMESTAMP - CURRENT_TIMESTAMP LIKE FALSE NOT IN ((VALUES (TRUE)), CAST(FALSE AS DATE) IS CURRENT_DATE
```

---

## Crash 99: `a6b32fd566af1e8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091773`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CAST(FALSE AS INTEGER)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 100: `9950ea9cab9766c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092038`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_TIMESTAMP LIKE CURRENT_DATE); PRAGMA quick_check; SELECT round(-1.0, 2147483647); SELECT substr('', 1
```

---

## Crash 101: `2d1223b9d0607e38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097003`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN UNIQUE, c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid_) VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 102: `2f9f3ddedebc30db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097743`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p
```

---

## Crash 103: `8c624175e5b4529a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098133`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 104: `5c1d7acf478bd92e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098406`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE, c1 INTEGER UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO 
```

---

## Crash 105: `25dc145eb6482c7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098891`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 106: `f8eed3833b5a2dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099027`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 107: `ba45ec14a84d01ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101839`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL DEFAULT TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT INTO p DEFAULT VALUE
```

---

## Crash 108: `f9a951ec1148d4a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101845`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, c3 GENERATED ALWAYS AS (a) UNIQUE, a BLOB GENERATED ALWAYS AS (RAISE(IGNORE) IS a) STORED); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 109: `6c0e00c2c8e9310e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101858`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); INSERT OR ROLLBACK INTO q VALUES (FALSE / FALSE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 110: `6780549c2bafd3ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101865`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), a GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2)
```

---

## Crash 111: `c6a9e4e690c245e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101894`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE, c3 DATE NOT NULL, c1 FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 112: `b7d3b6cd1fd94a36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT X'7Fe3dA20Da8F'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAUL
```

---

## Crash 113: `44d4d09429dccb33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104098`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (CURRENT_TIMESTAMP BETWEEN CURRENT_DATE AND CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 114: `fd20f149c02c2b43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105625`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC GENERATED ALWAYS AS (TRUE) VIRTUAL, _rowid_ BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 115: `3e5ddddc02c339d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106893`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*s', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CASE 
```

---

## Crash 116: `1ebf276540699ee4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110542`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; SELECT
```

---

## Crash 117: `42d41c16d32a4d18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111907`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); WITH p AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p
```

---

## Crash 118: `7aff1b675bf7fe24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112225`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (NULL), c2 DATE CHECK (TRUE), c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 119: `09e38260e75a73b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112390`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE, c2 DATE CHECK (TRUE), c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); IN
```

---

## Crash 120: `ffbcc9a6b28cd06c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112397`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (NULL), c2 NUMERIC PRIMARY KEY, c1 INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 121: `564a3dd0e3f8596f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113926`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 122: `ca86b3ca480b9e83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114538`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); EXPLAIN QUERY PLAN VALUES (TRUE) EXCEPT VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 123: `f94486696eb93a60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127377`

```sql
SELECT substr('   _', 2147483648, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO q VALUES (CASE RAISE(IGNORE) WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME ELSE
```

---

## Crash 124: `4c6392c8db4151b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127800`

```sql
SELECT substr('', 0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT FALSE, * FROM q CROSS JOIN r WHERE CASE TRUE WHEN CURRENT_TIMESTAMP THEN (CURRENT_DATE) ELSE CURRENT_
```

---

## Crash 125: `544ecf4b57a1ef6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128059`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); INSERT OR ROLLBACK INTO p VALUES (CAST(CURRENT_TIMESTAMP % CURRENT_DATE >= CURRENT_TIMES
```

---

## Crash 126: `51ece047384259c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128096`

```sql
SELECT printf('%f', 9223372036854775807, '- __-s_ l x'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1); INSERT INTO p VALUES (CURRENT_TIME NOT IN (TRUE IS NOT NULL) << FALSE >= CURR
```

---

## Crash 127: `53dae3050f8bd4a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131312`

```sql
SELECT printf('%.*d', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, _rowid_); INSERT OR REPLACE INTO p VALUES (-+CURRENT_TIMESTAMP NOT IN (WITH RECURSIVE t2 AS NOT MATERIALIZED (
```

---

## Crash 128: `c3f59d7b06e2f26c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132829`

```sql
SELECT round(-1.0, 1); CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); WITH RECURSIVE t3 AS (SELECT *) SELECT -~FALSE LIKE FALSE AS w_ FROM p; CREATE VIRTUAL TA
```

---

## Crash 129: `1b0da739314ef42d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135589`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT ' E__-t  -s_O35 2', c2 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 130: `b6768b356a02cc5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143734`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); IN
```

---

## Crash 131: `770a0201cbb0d396` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144570`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; SELECT * FR
```

---

## Crash 132: `bb6de987fb57e744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145256`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT UNIQUE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT V
```

---

## Crash 133: `98bc512f6af8e492` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148640`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY NULL; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CR
```

---

## Crash 134: `e333e02b5980b950` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148654`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CASE TRUE WHEN CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_TIME THEN NULL END), c2 RE
```

---

## Crash 135: `e3ac1506ba0f0cfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153600`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TA
```

---

## Crash 136: `f368b9a569bd377e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153663`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT INTO p
```

---

## Crash 137: `880bcb09639bf37c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153695`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE INDEX IF NOT EX
```

---

## Crash 138: `106899f4f6619021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153727`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 139: `9a1c3e3f328c590c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154457`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB, b NUMERIC GENERATED ALWAYS AS (hex(FALSE)) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid_) VALUES (FALSE); PRAGMA integrity_check; SELE
```

---

## Crash 140: `ff3e5a039a53ea72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154623`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT CURRENT_DATE, c2 BLOB, b NUMERIC GENERATED ALWAYS AS (hex(a)) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid_) VALUES 
```

---

## Crash 141: `ebc08a1112060ca5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154773`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT CURRENT_DATE, c2 BLOB, b NUMERIC GENERATED ALWAYS AS (hex(hex(hex(a)))) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid
```

---

## Crash 142: `88dfd04492f93041` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154787`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT CURRENT_DATE, c2 BLOB, b NUMERIC GENERATED ALWAYS AS (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(a)))))))))))))))))) ST
```

---

## Crash 143: `f66016b2f3eefd11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155028`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT CURRENT_DATE, c2 BLOB, _rowid_ VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (_rowid_) VALUES (FALSE); PRAGMA in
```

---

## Crash 144: `d89bef779c3cd14d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158637`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CAST(NULL AS INTEGER)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 145: `5c26bf53459ea53b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158723`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (NULL - CURRENT_TIME IS NOT TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 146: `208399742176a617` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160283`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_TIME - X''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 147: `6fa62716bf934852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160522`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE * CURRENT_DATE * TRUE - X''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 148: `efc3c3aef74d5469` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160700`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE - X''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 149: `883f29e6cd47df43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160885`

```sql
SELECT substr('M  _-- H_ 5G', -9223372036854775808, 2147483647); SELECT substr('', 2147483648, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT *, CURRENT_TIME IS NOT
```

---

## Crash 150: `8369b96c5c543be4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161740`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURRENT_DATE - CURR
```

---

## Crash 151: `d6acb4c33dc87f75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162641`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT FALSE); INSERT INTO p (_rowid_) VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (TRUE) UNION 
```

---

## Crash 152: `355de984ca63e7a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162832`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT 08182081456048253083723650282139044364786734963212710631059257755202880753038294926787502153730985779863998771204396912998454746959235656250.1392
```

---

## Crash 153: `05dd94520c2363a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (CURRENT_DATE * CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SE
```

---

## Crash 154: `e8c7adaaa5358944` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166108`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY, c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 155: `4e9162d6d88200ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166438`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN, rowid INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDE
```

---

## Crash 156: `51168fe09e7e325d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170736`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 DATE CHECK (CURRENT_TIME MATCH TRUE NOT NULL << RAISE(IGNORE))); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 157: `619c9c504f2b9e4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174932`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIMESTAMP > FALSE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 158: `418268ed53db1626` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175727`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 159: `395df553dba32dc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175821`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT DEFAULT X'aEbf7b'); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 160: `b862a61e6748ab1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176887`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS a LEFT OUTER JOIN p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 161: `d98f7431bb7a13c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176996`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT DISTINCT * FROM q NOT INDEXED LEFT OUTER JOIN p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 162: `be6c5a16dd35991b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177961`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT); SELECT * FROM q NATURAL JOIN q WHERE FALSE IN (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY -
```

---

## Crash 163: `fe6f9e500d1ac699` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180045`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p AS (SELECT changes()) SELECT * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 164: `5d891fb3823e677d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180213`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p AS (SELECT FALSE) SELECT * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 165: `3e63defcb41c2e3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180534`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p AS (VALUES (NULL) UNION ALL VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 166: `a4401135ac6c3fb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180610`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); WITH RECURSIVE p AS (VALUES (CURRENT_TIME)) SELECT count(*) FROM p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 167: `7c7f447df3a4d35f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183431`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 168: `e0429bbb28421e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184595`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN CHECK (CURRENT_TIMESTAMP OR TRUE), c3 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 169: `936811eccac24ae2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185910`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EX
```

---

## Crash 170: `e46c303739e210ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186102`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME AS rce_gx_ilrnd47vy5l8__5_ FROM p NATURAL LEF
```

---

## Crash 171: `9722629546baaf08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186109`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); INSERT INTO p DEFAU
```

---

## Crash 172: `83a92b27a9cd8d44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186386`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c3 GENERATED ALWAYS AS (a)
```

---

## Crash 173: `9d77cb83def4dfc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187275`

```sql
SELECT substr('_7j-vEN-7 ', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO r VALUES (CASE CASE -FALSE -> -CURRENT_TIMESTAMP WHEN CURRE
```

---

## Crash 174: `b084de56a75d3b6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187634`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT 1163068667629.6e+36559827856367043635182455653); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 175: `5435e2076a6539f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188033`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 176: `99e1f48b40fd9f87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189994`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT CURRENT_TIME ORDER BY count(*) OVER () DESC NULLS FIRST LIMIT TRUE; PRAGMA quick_check; SELE
```

---

## Crash 177: `614e91c3986ba40f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190106`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT CURRENT_TIME ORDER BY RAISE(IGNORE) DESC NULLS LAST LIMIT TRUE; PRAGMA quick_check; SELECT p
```

---

## Crash 178: `1a6045953411305d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190112`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT CURRENT_TIME ORDER BY TRUE ASC LIMIT TRUE; PRAGMA quick_check; SELECT printf('%.*g', 2147483
```

---

## Crash 179: `899fbfd179514568` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190155`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT X'5677d04ffB71'); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 180: `d0e614e1ea1a451e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199785`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE IS NOT NULL > CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 181: `857f47f225cc4126` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200068`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE -61773086970856153902812996070728.60e881089818359565802304225422317
```

---

## Crash 182: `393ef01dcf408de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200247`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE X'a7A9E0babA'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 183: `d22ac12d4a794100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201204`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), c2 GENERATED ALWAYS AS (a) UNIQUE, a NUMERIC CHECK (CURRENT_TIME)); SELECT * FROM p NATURAL JOIN p WHERE (VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 184: `052eb74d24d10742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202342`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IN (CURRENT_TIME, NULL, CURRENT_TIME); CREA
```

---

## Crash 185: `2c82553887d22185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203820`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT X'Ac'); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 186: `9500fb52f62bff60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203965`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 187: `34d3147704bb2fa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204656`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IN (CURRENT_DATE) OR TRUE IS NOT NULL; CREATE VIRTUAL TABLE IF
```

---

## Crash 188: `2024efbe7b1f1a44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204788`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE p.a IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 189: `420298f50dcc3620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205425`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE OR TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 190: `1b9b939fe450c183` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205578`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL OR TRUE OR TRUE OR TRUE OR TRUE OR TRUE OR TRUE OR TRUE OR TRU
```

---

## Crash 191: `1b2c466ba620e103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207912`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE 6854036.91151954541983574462544391975652949218161522018414903417E-7
```

---

## Crash 192: `5c69701b8969e1c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208098`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IN (NULL, CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 193: `3e5c2dcac3787de1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208289`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE (SELECT * FROM q NOT INDEXED GROUP BY CURRENT_DATE) IN (CURRENT_TIM
```

---

## Crash 194: `b665bfe738f4d940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209005`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE length(FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 195: `bf72c30af903a4be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209294`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT CURRENT_TIME NOT LIKE CURRENT_DATE FROM p NATURAL JOIN p WHERE length(CURRENT_TIMESTAMP); CREATE 
```

---

## Crash 196: `736cf8630b85c3d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216316`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME NOT LIKE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 197: `a1323d86afa0a674` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218235`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN UNIQUE, c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_TIME, CURRENT_DATE) ON CONFLI
```

---

## Crash 198: `a73e7b0af6dad831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218672`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * FALSE, CURRENT_DATE) ON CONFLICT DO NOTHING; P
```

---

## Crash 199: `b75ebccfaedb3a2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218824`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * C
```

---

## Crash 200: `2cf130a034f1fca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219338`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * C
```

---

## Crash 201: `b756c8a83a2be01d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220653`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE * C
```

---

## Crash 202: `fb840164bb4e3a13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220810`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * TRUE, CURRENT_DATE) ON CONFLICT DO NOTHING; PR
```

---

## Crash 203: `4510c2c683f8e5f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220816`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL UNIQUE, c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_TIMESTAMP, CURRENT_DATE
```

---

## Crash 204: `5d52f6a5c58ac725` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222809`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT
```

---

## Crash 205: `53cd5afbbac777a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223227`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT X'Bcb73Dc5'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 206: `96110a04084053f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229546`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL IN (CURRENT_TIMESTAMP) MATCH NULL; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 207: `548d933b0a2009d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229948`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE IN (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN (SELECT * F
```

---

## Crash 208: `46f4151b9c79b69a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231583`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE OR FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 209: `27aa79910deed009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231796`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME NOT NULL OR TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 210: `a20433fa207db8b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232208`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE a IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT INTO p VALUES (~FALSE) ON CONFLICT DO N
```

---

## Crash 211: `a778cd2abb4b0458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232278`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE p.a IS NULL COLLATE BINARY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 212: `d9122e11d968e11d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234918`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IN (NULL, FALSE, CURRENT_DATE); CREATE VIRT
```

---
