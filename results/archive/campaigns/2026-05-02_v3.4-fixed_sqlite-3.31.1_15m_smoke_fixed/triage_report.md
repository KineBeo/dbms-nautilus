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

## Crash 1: `efc10b8151dbb9bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000123`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (RAISE(IGNORE)); EXPLAIN QUERY PLAN SELECT p.* FROM (p AS d42_5f0_iqivz7_7_7_9qc__5ag_) NATURAL JOIN p WHERE _r
```

---

## Crash 2: `85f7727492fad9d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000318`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_); INSERT INTO p (c1, b) VALUES (CURRENT_TIME BETWEEN RAISE(IGNORE) AND FALSE == TRUE COLLATE RTRIM); EXPLAIN QUERY PLAN VALUES (CURRENT_
```

---

## Crash 3: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000723`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 4: `e3445a4f84d17bc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000931`

```sql
SELECT substr('-D_ j _7cZ-  4  ', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p SELECT * FROM q INDEXED BY a CROSS JOIN p WHERE printf('0  --772_-0_', -
```

---

## Crash 5: `a2d4766ebdb7e1f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000979`

```sql
SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(b INTEGER, c3 GENERATED ALWAYS AS (a = 0) NOT NULL); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ~FALSE AS kx_, CAS
```

---

## Crash 6: `0e436ca1894cb348` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001082`

```sql
SELECT printf('%lli', -2147483649, 'G- '); SELECT printf('%.*g', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q WITH t1 (c1) AS NOT MATERIALIZED (VALUES (-FALSE
```

---

## Crash 7: `a2fd70e2e6d9fa2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001448`

```sql
SELECT printf('%.*s', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT q.* FROM q WHERE EXISTS (SELECT CASE WHEN CURRENT_TIMESTAMP THEN TRUE <> CURRENT_DATE -> TRUE ELSE CURRE
```

---

## Crash 8: `0d51a96629f58034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001759`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO p VALUES (+(RAISE(IGNORE)) + CURRENT_DATE IS CASE WHEN -RAISE(IGNORE) THEN +RAISE(IGNORE) NOT
```

---

## Crash 9: `d8c3769ba893178b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001906`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUE
```

---

## Crash 10: `170bbf64c93ded33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001915`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c2 DATE, b GENERATED ALWAYS AS (a) NOT NULL); INSERT INT
```

---

## Crash 11: `332dd84ff4cc1e51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001975`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 12: `9bde13d0d9055685` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002264`

```sql
SELECT round(0.01, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT t2.*, *, * FROM p JOIN p xr_97f__8pnx ON format('_A_  -9-0 _2M  -', -CURRENT_DATE NOT IN (CURRENT_TIME)) FILTER 
```

---

## Crash 13: `4d65d01705502cc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002569`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT q.*, -FALSE IS NULL -> CURRENT_TIMESTAMP COLLATE BINARY NOT BETWEEN -CURRENT_TIME AND CURREN
```

---

## Crash 14: `957144bdfb113e3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002705`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 15: `0d9b7f79a4f8f00f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002782`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_DATE); REPLACE INTO p VALUES (CAST(CURRENT_DATE AS DATE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 16: `d635cfb36d51d4e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002831`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_DATE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSER
```

---

## Crash 17: `8b2e83ae5055e831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002858`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO q VALUES (CURREN
```

---

## Crash 18: `e9bc073b9e7826f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003090`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT substr('3', 0, -9223372036854775808); CREATE VIRTU
```

---

## Crash 19: `9530996663f9274e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004674`

```sql
SELECT round(-1e308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t3 AS MATERIALIZED (SELECT DISTINCT *, FALSE / CURRENT_TIMESTAMP COLLATE BINARY FROM t3 AS o LIMIT p.c
```

---

## Crash 20: `dc7ae43d872a532a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007137`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c2, c3, c2); INSERT INTO t3 VALUES (coalesce(RAISE(IGNORE) COLLATE NOCASE COLLATE BINARY GLOB CURRENT_DATE, CAST(NOT EXISTS (VALUES (T
```

---

## Crash 21: `3e15b49c494be165` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007373`

```sql
SELECT printf('%.*s', 4294967296, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1); WITH RECURSIVE p (a, b, c3) AS NOT MATERIALIZED (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_
```

---

## Crash 22: `f0e7f9543f85fd50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007912`

```sql
SELECT round(1e-308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN DEFAULT -2509
```

---

## Crash 23: `79e3467210f873c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008389`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 24: `a1d66582dc40904b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008450`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 25: `10124b489aabca7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008555`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE, rowid BOOLEAN NOT NULL DEFAULT 7887, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; ANALY
```

---

## Crash 26: `2c83457b31f7115e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008856`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE, rowid BOOLEAN NOT NULL DEFAULT CURRENT_TIME, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO q DEFAULT VALUES; ANALYZE p; SE
```

---

## Crash 27: `bc8ca0be7db06cd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008862`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE, rowid BOOLEAN NOT NULL DEFAULT CURRENT_TIME, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO q DEFAULT VALUES; PRAGMA quick_
```

---

## Crash 28: `ba887ff7d2d8775c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011002`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c3, c2, c3, c3, _rowid_, c3); SELECT *, * FROM p NOT INDEXED JOIN s NOT INDEXED USING (c2) WHERE ~(SELECT ALL * FROM t1 EXCEPT SELECT CURREN
```

---

## Crash 29: `26acfa340b4c49e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013913`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT OR IGNORE INTO p VALUES (CASE WHEN (VALUES (TRUE)) THEN CURRENT_TIMESTAMP END); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 30: `867126dfdb027ee1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015166`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, _rowid_ BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 31: `17ef3d8aeadccbfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016147`

```sql
SELECT printf('%.*f', -2147483649); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 32: `432e8058949e42d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018061`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 33: `e49f791a4f8720cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018712`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT NULL) AS su
```

---

## Crash 34: `ec80c54e602fa0a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018952`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE) AS sub1; 
```

---

## Crash 35: `191e3bf43d181b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019568`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE IS NOT TRU
```

---

## Crash 36: `22a1a3e4d44daf7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020646`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 
```

---

## Crash 37: `524312e9f0c5d7b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021500`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p SE
```

---

## Crash 38: `e67fa3ed2e3b9467` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025515`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 39: `802c3926c527f327` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026219`

```sql
SELECT substr('2__ _-_-2_1WKE4_ S', -2147483649, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (a) VALUES (CURRENT_DATE); VALUES (CURRENT_DATE);
```

---

## Crash 40: `da494bc572321123` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026531`

```sql
SELECT printf('%.*e', 4294967296); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 41: `77ce289621f24c50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026908`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, a GENERATED ALWAYS AS (a IS NULL) UNIQUE); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) UNION VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 42: `b3d17ba552011c6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030285`

```sql
SELECT printf('%.*g', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO r VALUES (NULL NOTNULL); EXPLAIN QUERY PLAN SELECT *; CREATE TABLE IF NOT EXISTS p(b REAL CHECK
```

---

## Crash 43: `cf91d92e517073de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030948`

```sql
SELECT printf('%lld', -9223372036854775808, 'reD'); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 44: `a7b028dce8c7f951` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037199`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 45: `4b896aa7e6f9f0e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037820`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT X'376e'); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT IN
```

---

## Crash 46: `d95acea8e7eec1e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037836`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT X'376e'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT 
```

---

## Crash 47: `225c0a32dafd13fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038116`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 48: `64ff3ee697ca46f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038295`

```sql
SELECT printf('%.*d', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (CASE WHEN CASE CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN CURRENT_TIME % -TRUE 
```

---

## Crash 49: `011c8cc38781e59d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039291`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (CUR
```

---

## Crash 50: `1db8c59011e2fce4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040246`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(1));
```

---

## Crash 51: `986c58be2b4dabe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044600`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE IS NOT CUR
```

---

## Crash 52: `eed2de7f9529adb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044609`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 53: `16afd5ee73f34cbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044674`

```sql
SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s DEFAULT VALUES; VALUES (CURRENT_DATE);
```

---

## Crash 54: `7d46123134934356` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045538`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIR
```

---

## Crash 55: `5392299597502c34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046092`

```sql
SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT ~TRUE, q.*, CASE CURRENT_TIME > -NULL WHEN TRUE = CURRENT_TIMESTAMP < CURRENT_TIME THEN FALSE END COLLATE
```

---

## Crash 56: `2101467b9d2ff0ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046539`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; SELECT NOT c2 MATCH CURRENT_TIMESTAMP <> NOT TRUE AND CURRENT_TIME IS DISTINCT FROM CURRE
```

---

## Crash 57: `157d2b8da2a15a5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049781`

```sql
SELECT printf('%f', -9223372036854775808, '_cf--'); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 58: `5bf16970d341ecb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049957`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM p WHERE EXISTS (VALUES (~NULL, CURRENT_TIME, FALSE ISNULL) INTERSECT SELECT DISTINCT
```

---

## Crash 59: `97fadcfb9266b87c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051894`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CAST(CURRENT_TIME AS DATE)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 60: `b2d9eebbf54e795b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052099`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CAST(CURRENT_TIME AS DATE)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 61: `bb80a15e1ba55d9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057115`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT ALL NULL FROM p; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 62: `5b22bd6815bdf9cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059397`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CAST(CURRENT_DATE AS BLOB)); VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 63: `cfee5d188345e1ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059785`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 INT); REPLACE INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIME); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXI
```

---

## Crash 64: `a1ac3145ab2994a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060124`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT ALL *
```

---

## Crash 65: `d48de482284af571` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060478`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT UNIQUE); REPLACE INTO p VALUES (CAST(CURRENT_DATE AS REAL)); VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 66: `6515deb962d5adce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060644`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); REPLACE INTO p VALUES (CAST(CAST(CURRENT_DATE AS DATE) AS DATE)); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); RE
```

---

## Crash 67: `e9ca416441d1e044` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061117`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); INSERT INTO p DEFAULT VALUES; SELECT max(FALSE) OVER () AS q4_g FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TA
```

---

## Crash 68: `c215282e62fa247b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061137`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 69: `ed1fe546eb2b0564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061602`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES (CAST(CURREN
```

---

## Crash 70: `ebd50a82366e7e57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061613`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INT); REPLACE INTO p VALUES (CAST(CURRENT_DATE AS DATE)); VA
```

---

## Crash 71: `be0e31260d0518ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062170`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT X'376e'); INSERT OR ROLLBACK INTO p VALUES (FALSE NOT LIKE FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 72: `1c40cd8e19ed7d95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062378`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 73: `2b0e24accc8ce1df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062786`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); INSERT OR FAIL INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (FALSE)
```

---

## Crash 74: `4e07036eb255a750` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063450`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC)
```

---

## Crash 75: `8fd8d91b35ad0730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064215`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); V
```

---

## Crash 76: `08db5a6d788d4972` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065589`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; VALUES (~X'3BdE'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); R
```

---

## Crash 77: `47d113c7e4f6b4d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066536`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CAST(TRUE AS TEXT)); PRAGMA quick_check; SELECT printf('%.*
```

---

## Crash 78: `2b1027c192c1caf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066569`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA quick_check; SELECT printf('%.*f', 214748364
```

---

## Crash 79: `c78f83ecf925957a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066783`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); SELECT count(*) AS lcw_56wz_594 FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 80: `236ae8bd38df753b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067077`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', -214748
```

---

## Crash 81: `dcb0758f2433104b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079470`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) UNION ALL VALUES (FALSE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 82: `493feb1cdad8a7b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079615`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 83: `48ad58e6287986f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080028`

```sql
SELECT substr('  4l-uI2', 4294967296); SELECT printf('%.*d', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO p VALUES ((NULL)); SELECT RAISE
```

---

## Crash 84: `137755181ea02d20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080172`

```sql
SELECT round(1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CURRENT_TIME); ANALYZE p; SELECT hex(zeroblob(2147483647));
```

---

## Crash 85: `3e9cea90bd5a4efb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081319`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p 
```

---

## Crash 86: `fbe24bf6f8e9afed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086895`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p JOIN p h_y ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, a); INSERT O
```

---

## Crash 87: `75f055181038e865` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086965`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_DATE ORDER BY CURRENT_DATE DESC NULLS LAST, TRUE LIKE TRUE ESCAPE NULL ASC; EXPLAIN QUERY PLAN VALUES 
```

---

## Crash 88: `36789667f9bf864a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089001`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE IS NULL) A
```

---

## Crash 89: `8a683271b04c930d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089571`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE IS NOT FAL
```

---

## Crash 90: `10784c64162385e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090116`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT *, * FROM q WHERE CURRENT_DATE) AS sub
```

---

## Crash 91: `46bdd1ef75eec4e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090426`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT ' Q-'); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 92: `b96f46f0f1605827` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090730`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIME <= CURRENT
```

---

## Crash 93: `10048c41d9717666` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091327`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT TRUE IS NOT
```

---

## Crash 94: `77db28d69f77c7eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091455`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT CURRENT_TIM
```

---

## Crash 95: `94c3f5f2a28cf2fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091558`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT TRUE IS NOT
```

---

## Crash 96: `bd9c18017985d7ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091889`

```sql
SELECT substr('', 4294967296, 2147483648); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 97: `d2e8573341663fa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094762`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 98: `0d2017ed083aedac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095807`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, _rowid_ BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 99: `990fe2c62db4e088` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096786`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT OR IGNORE INTO p VALUES (NOT EXISTS (SELECT DISTINCT * FROM p LEFT JOIN p AS l USING (a))); VALUES (TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 100: `e6a05a9773727742` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097456`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT OR IGNORE INTO p VALUES (~NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CURRENT_TIME); ANALYZE p
```

---

## Crash 101: `cd8246192ab7d1f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098265`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT OR IGNORE INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (VALUES (NULL)) AS n)); VALUES (TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 102: `806a38fe141f445f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113919`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT 7029377.0092512313354291358267909030869058944108323735680212920294846363541601922562185233648790524
```

---

## Crash 103: `f593f0483fa0b765` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114418`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b TEXT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 104: `49a0ae9b33a74bcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114655`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT X'5d'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 105: `db7a75d191d16197` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114712`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b NUMERIC DEFAULT X'5d'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 9223372036854775807, 1e-308); C
```

---

## Crash 106: `efd4e44a2e57dbd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114865`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL DEFAULT 1553274294090455013528078597.13e37); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE
```

---

## Crash 107: `901db21eb17572c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114929`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT TRUE, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; C
```

---

## Crash 108: `33422c732a8d1741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115237`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (NULL), a INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 109: `605a572993b51d28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115261`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC PRIMARY KEY, a INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 110: `fa013e6343b614db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115818`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT 666.2214003320739346841609188575964789124444810600197136935026534793872132962115792640588197403462560302E-714105, c2 VARCHAR(255) UNIQUE); C
```

---

## Crash 111: `5093b5129fd68114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115943`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g
```

---

## Crash 112: `b7fb8f47ef620a07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115970`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); WITH q AS (SELECT *) INSERT INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 113: `6c2a1aa9b44b4120` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 114: `a387d48f40d4565a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116476`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT X'FF', c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 115: `4dfdd2ce59f066ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117132`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT FALSE, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 116: `2c862b2d3159472b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117430`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT X'd43DF9Ecdc', c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 117: `12caa71cc74ed795` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117492`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL DEFAULT -0); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', -2147483
```

---

## Crash 118: `729e1b32dccdf0f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117847`

```sql
SELECT printf('%llu', 4294967296, '__l5 H-k-_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r (c3, c2) VALUES (CASE WHEN CURRENT_TIMESTAMP ISNULL THEN NULL END <= TRUE ISNULL
```

---

## Crash 119: `acd431a3c0f6fdf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117865`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 DATE CHECK (NOT CURRENT_DATE IS NULL)); VALUES (-CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 120: `a44c7f342d8f07a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120379`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (total_changes() >= FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE FALSE), a INT); INSERT INTO q DEFAULT VALUES; PRAGMA 
```

---

## Crash 121: `3aab8d134612f125` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (TRUE >= FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE FALSE), a INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 122: `b33c2dc834ed4060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120479`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (total_changes() >= FALSE NOT LIKE CURRENT_TIMESTAMP), a INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; C
```

---

## Crash 123: `ae9c552143c8e033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120485`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (total_changes() >= FALSE NOT LIKE FALSE NOT LIKE NULL), a INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 124: `0575f62c86160633` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120559`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (total_changes() >= FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE NULL), a INT); INSERT I
```

---

## Crash 125: `7f7715e7ac6b28d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121037`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL CHECK (total_changes() >= FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE FALSE NOT LIKE CURRENT_TIME), a INT); INSERT INTO q D
```

---

## Crash 126: `b04e62f4d707fbe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (TRUE); SELECT printf('%.*g', -2147483
```

---

## Crash 127: `68516b0201e59f6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134670`

```sql
SELECT printf('%.*f', 4294967296, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FAIL INTO p VALUES ((SELECT DISTINCT t1.*, q.*, ~CURRENT_DATE OR TRUE NOTNULL AS r8_a50o1_
```

---

## Crash 128: `e4e06f67b55e9f97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136053`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); INSERT OR IGNORE INTO p VALUES (NOT EXISTS (SELECT DISTINCT * FROM p LEFT JOIN p AS l ON NULL)); VALUES (TRUE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 129: `61bd15eb7ad6caf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136781`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, _rowid_ BOOLEAN NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF 
```

---

## Crash 130: `dc16bc7a00f7c452` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137283`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT TRUE AS f FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 131: `1724213a28bc4851` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137585`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p , (VALUES (TRUE)) AS o__ju_u7__6_4_bznt_naw
```

---

## Crash 132: `3c80aeaa53f178b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139967`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE IS NOT CURRENT_TIM
```

---

## Crash 133: `b2e5c6bffa71ac6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141210`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE TRUE NOT IN (TRUE, NULL
```

---

## Crash 134: `f34272fa9a6f0fdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142298`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_DATE IS NOT CUR
```

---

## Crash 135: `bbdbf562554df790` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142470`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP GLOB 
```

---

## Crash 136: `4051363f141de35f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142660`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT CURRENT_DATE != TRUE COLLATE NOCASE AS
```

---

## Crash 137: `b6c613bd3a21f983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143244`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL DEFAULT TRUE, c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT 
```

---

## Crash 138: `9a36623174277fea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144133`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT 656605); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); SELEC
```

---

## Crash 139: `393d985fcd7769a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146433`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p JOIN p h_y ON random(); SELECT printf('%.*f', -2147483649, -1e308);
```

---
