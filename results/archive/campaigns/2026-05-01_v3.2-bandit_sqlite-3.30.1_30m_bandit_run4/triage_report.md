# Crash Triage Report

**Total crashes:** 178  
**Unique crash sites:** 178  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 178 | 178 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `e7251e03095f5549` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000129`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR IGNORE INTO p VALUES (CASE WHEN FALSE COLLATE RTRIM THEN CURRENT_DATE LIKE CURRENT_TIMESTAMP GLOB NULL IS DISTINCT FROM RAISE(IG
```

---

## Crash 2: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000196`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 3: `370f9870911981a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000204`

```sql
SELECT printf('%.*g', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO q VALUES ((CURRENT_TIME), CURRENT_TIME IS CURRENT_TIME); SELECT *, * FROM p NATURA
```

---

## Crash 4: `657689eedf563223` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000255`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c1); INSERT INTO q DEFAULT VALUES; SELECT p.a & CASE WHEN iif(RAISE(IGNORE) >> +FALSE, CURRENT_DATE ->> NULL NOT NULL, CAST(CURRENT_TIME AS 
```

---

## Crash 5: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000534`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 6: `56453d77e334cc27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001139`

```sql
SELECT substr('', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c2, c1); INSERT OR REPLACE INTO q VALUES (CAST(NOT EXISTS (SELECT CURRENT_TIME AS tfqp24x_411
```

---

## Crash 7: `06907ba681be9756` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001455`

```sql
SELECT printf('%.*s', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT (+TRUE < NULL COLLATE NOCASE IS TRUE IN (VALUES (RAISE(IGNORE))) % RAISE(IGNORE)) COLLATE RTRIM
```

---

## Crash 8: `2d8ee67c2e25b420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001732`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_DATE AS s_f8p_, FALSE COLLATE BINARY != CURRENT_TIMESTAMP AS a05qq_658y__ps6sw25h6_
```

---

## Crash 9: `db16fa035f07a3bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002062`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_DATE AS s_f8p_, FALSE COLLATE BINARY != CURRENT_TIMESTAMP AS a05qq_658y__ps6sw25h6_0ot_9v1w__c_6_3_m9_
```

---

## Crash 10: `7b249d22e4f32e92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002175`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (FALSE / TRUE <= NULL COLLATE RTRIM NOT IN (CURRENT_TIMESTAMP != FALSE IS NULL, (CURRE
```

---

## Crash 11: `ee159415f888561b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002565`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_TIMESTAMP)); INSERT OR FAIL INTO p VALUES (TRUE NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECU
```

---

## Crash 12: `730447c7d23a11e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002591`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t3 AS MATERIALIZED (
```

---

## Crash 13: `78f26ecfa0fd1c23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002603`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT OR FAIL INTO p VALUES (TRUE NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS
```

---

## Crash 14: `54bbed765fc36bd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002609`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); INSERT OR FAIL INTO p VALUES (TRUE NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 
```

---

## Crash 15: `0add4d1b8ce39312` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002615`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS MATE
```

---

## Crash 16: `3c92ca55e8d6db5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002630`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS MATERIALIZED (SELEC
```

---

## Crash 17: `c5ee61c0de4708ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002687`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE t3 AS MATERIALIZED (SELEC
```

---

## Crash 18: `d75e4b0a0dd78878` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004629`

```sql
SELECT round(-1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q (b) AS (VALUES (CURRENT_DATE)) INSERT INTO q VALUES (CURRENT_TIME NOT BETWEEN CUR
```

---

## Crash 19: `322c3042e242d35a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005279`

```sql
SELECT round(0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO s SELECT ~TRUE BETWEEN FALSE AND ~CURRENT_TIMESTAMP COLLATE BINARY FROM r NATURAL LE
```

---

## Crash 20: `17471bb988047eee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005360`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 21: `cdbce7d512cac7f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005808`

```sql
SELECT substr(' yp_-g9S _8', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT q.* FROM (SELECT p.*, CASE WHEN CASE CURRENT_DATE WHEN RAISE(IGNORE) THEN CURRENT_TI
```

---

## Crash 22: `25b39d31d7c11a6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006382`

```sql
SELECT substr('', 4294967296, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_); SELECT CASE WHEN CURRENT_DATE -> TRUE THEN NULL END BETWEEN RAISE(IGNORE) IS NOT NULL -> CASE RAISE(
```

---

## Crash 23: `15bf8f3d8a471d01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006718`

```sql
SELECT round(-1.0, 2147483647); SELECT printf('%.*d', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH q AS NOT MATERIALIZED (WITH RECURSIVE q (c2) AS NOT MATERIALIZED (SELECT q.*) VA
```

---

## Crash 24: `1838e582e3b230c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007242`

```sql
SELECT substr('___ 9l', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT OR ROLLBACK INTO p VALUES (-FALSE, substr(CURRENT_DATE, CURRENT_TIME IS NULL, CURRENT_TIME) OV
```

---

## Crash 25: `7ce3a51153f9f233` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012442`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 26: `a50897555f9cc67b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012455`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(2147
```

---

## Crash 27: `16ea2f4caf11ac59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012566`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 28: `aa6e9d392ee14d50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012597`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 29: `4f82bcfbbf70c235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016767`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT -8346834338298850180513103060665619000738645337008675386616541081053035652284226940484347668427411375710322014586704709442704196599988896959835341
```

---

## Crash 30: `9e854ea609a90aad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023803`

```sql
SELECT printf('%lld', -2147483648, 'q-j_l 0Ck_-g1_jg- _'); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 31: `4d6745365ecc15fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024816`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT last_insert_rowid() NOT NULL == RAISE(IGNORE) IS NOT DISTINCT FROM json_array(TRUE) AS z2 FROM t2 NATURAL J
```

---

## Crash 32: `c4fc31ebfb558330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024902`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p (b) VALUES ((WITH RECURSIVE p AS (SELECT *), q AS (SELECT *) VALUES (TRUE))); EXPLAIN QUERY PLA
```

---

## Crash 33: `0d4da0396dc3d338` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024943`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) CHECK (RAISE(IGNORE) LIKE CURRENT_TIMESTAMP ESCAPE CURRENT_DATE), c1 NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VAL
```

---

## Crash 34: `1bfe3917beeb34de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024974`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP, * FROM q ORDER BY TRUE LIM
```

---

## Crash 35: `f00692c164fdeb2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024987`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 36: `f64c5078a758405d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025113`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN DEFAULT ''); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 37: `efe12d95011b3493` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025125`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 38: `83abf92f87c5cafe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025416`

```sql
SELECT substr('', -9223372036854775808, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2); INSERT INTO t3 VALUES (NULL LIKE CURRENT_DATE LIKE (VALUES (NULL)) OR NULL GL
```

---

## Crash 39: `40b465b7adb21247` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026240`

```sql
SELECT printf('%.*s', -1, 1e-308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `87063d16cf347576` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032760`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH 
```

---

## Crash 41: `4ce0deaac1992a08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032835`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRA
```

---

## Crash 42: `e9fd4407f52873d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036321`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT
```

---

## Crash 43: `d8b0e0dcafb3e3a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036424`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(1));
```

---

## Crash 44: `dbb356f31f870be1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037384`

```sql
SELECT printf('%.*g', 2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 45: `1aa2ee8cb900b8d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038286`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT json(changes() FILTER (WHERE NULL) OVER (PARTITION BY CURRENT_TIME NOT IN (CURRENT_TIMESTAMP IS NOT N
```

---

## Crash 46: `65a2df9a08f2f185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038703`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) SELECT ALL * FROM p NOT INDEXED; VALUES (TRUE); CREATE VIRTUAL TA
```

---

## Crash 47: `2a88992c0dcd00df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038959`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) VALUES (FALSE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 48: `8be449377beb7269` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040727`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 49: `40d92be623c91a95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044492`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) EXCEPT VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 50: `0f29c2cba05c74b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045026`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH q AS (SELECT *) INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTU
```

---

## Crash 51: `f6035552124ed80f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045065`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) CHECK (CURRENT_DATE < NULL)); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 52: `a16cffdf6661fcdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045076`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY RAISE(IGNORE), RAISE(IGNORE) DESC NULLS FIRST; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 53: `00e245d607a164c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045097`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 DATE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 54: `66b1cd1dc6ac792a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045175`

```sql
SELECT substr(' -h8Wl_ -', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 55: `1a5c560b0a35b912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045790`

```sql
SELECT printf('%.*d', 2147483648, -1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 56: `9e06f343bb98d0c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045992`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(1));
```

---

## Crash 57: `5aca11a51fb378cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046455`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, c2, _rowid_); SELECT (VALUES (TRUE) LIMIT CURRE
```

---

## Crash 58: `02c867973d0b9fd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047247`

```sql
SELECT printf('%u', -2147483648, 'Cso--4--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT INTO q DEFAULT VALUES; ANALYZE t1;
```

---

## Crash 59: `e19bf91595b58c59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047371`

```sql
SELECT printf('%x', 1, 'i P'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT +~NULL NOT LIKE CURRENT_DATE != NULL IS NULL NOT NULL LIKE CURRENT_TIME AS ez81o1___26g_, upper(FALSE + C
```

---

## Crash 60: `160c825a8eed3a02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049571`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT NULL ORDER BY FALSE ASC NULLS FIRST LIMIT CURRENT_DATE)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT
```

---

## Crash 61: `4525a2af9c731303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054205`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 62: `8947034a0aa0d422` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054733`

```sql
SELECT printf('%.*g', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT INTO q (b) VALUES (RAISE(IGNORE)) ON CONFLICT(c3) DO UPDATE SET b = (CASE RAISE(IGNORE) WHEN CURRENT_TIM
```

---

## Crash 63: `04510662032212e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054768`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER DEFAULT 589439849579011781704407523195090113630010379218885827084574291844946773712782750438945049045774366254110668157972008432542042761081284936610356773
```

---

## Crash 64: `8187f744ceacb5a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055117`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL / NULL)); INSERT OR FAIL INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_TIME); SELECT substr('aE R  y Q1-__c', 4294967295); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 65: `6d553810443ae0fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055395`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p GROUP BY CURRENT_DATE, CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, b, c1, 
```

---

## Crash 66: `6638b208c8cefeb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) SELECT ALL * FROM p NOT INDEXED; VALUES (TRUE); CREATE VIRTUAL
```

---

## Crash 67: `e35163f5377bb5e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059992`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) SELECT * FROM q JOIN q NOT INDEXED USING (c3) WHERE CURRENT_TIME;
```

---

## Crash 68: `2f6e0944e492d5c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062895`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_TIMESTAMP BETWEEN TRUE AND CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 69: `2e668f0f5a6b8d52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064739`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(b VARCHAR(255), a TEXT); INSERT INTO p DEFAU
```

---

## Crash 70: `a3b76b6ea4883e0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064882`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT X'9B3bbcEbAe'); CREATE INDEX
```

---

## Crash 71: `a5ce7869562295da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064889`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUE
```

---

## Crash 72: `0cfb973b587e5efd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064910`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF 
```

---

## Crash 73: `496aa2e69190d9dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064956`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT '--_ll--19i'); C
```

---

## Crash 74: `4dfd0d09cb8e56cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065410`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VI
```

---

## Crash 75: `7ef87ad55003dea6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT TRUE AS x53_ LIMIT CURRENT_DATE, CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 76: `5bed30e3cbf56642` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065880`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR REPLACE INTO p VALUES (abs(CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT IN
```

---

## Crash 77: `4250b844af1c0308` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065902`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT -23.3); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 78: `b239473e43a619c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065917`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 79: `b281ce605bbb515b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067674`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 80: `aeb288c5396cdefc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068728`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q AS (VALUES (NULL) UNION ALL VALUES (CURRENT_TIMESTAMP OR TRUE)) SELECT * FROM q; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 81: `0f07c11016aa9f8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069075`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); WITH RECURSIVE q AS (VALUES (count(*) FILTER (WHERE CURRENT_TIME))) SELECT * FROM q; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 82: `a1bfe409af8de5f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069855`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME | CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAUL
```

---

## Crash 83: `288b41b565523cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070932`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s (b, c2) V
```

---

## Crash 84: `301b73e0dd92a1ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071158`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIR
```

---

## Crash 85: `f4f53cdb1e7e8096` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071168`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TAB
```

---

## Crash 86: `629ae5f28081cdca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075631`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER UNIQUE, b INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY TRUE ASC NUL
```

---

## Crash 87: `466c733244232c9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076293`

```sql
SELECT printf('%f', 9223372036854775807, '0-_ V _p'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (FALSE NOT LIKE CURRENT_TIME >> CURRENT_TIMESTAMP ->> RAISE(IGNORE) 
```

---

## Crash 88: `2d5c5ea5e702738c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090622`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL, rowid TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (X'd6Bdcf2E', FALSE); PRAGMA quick_check; CREATE VIRT
```

---

## Crash 89: `e9f4522f7ae02ef2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT 75141); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT X''); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 90: `b100b4b2ae65152d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090688`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, c1 DATE NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 91: `49d7b7742d6e1f80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096886`

```sql
SELECT printf('%.*f', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO t2 VALUES (avg(CASE WHEN NOT ~TRUE & CURRENT_DATE >> FALSE + FALSE NOTNULL COLLATE NOCASE IS CU
```

---

## Crash 92: `e93340da6c95b3b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097580`

```sql
SELECT substr('', 4294967295, 9223372036854775807); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 93: `6899a175ba664c05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098159`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT -8346834338298850180513103060665619000738645337008675386616541081053035652284226940484347668427411375710322014586704709442704196599988896959835341
```

---

## Crash 94: `e9618e0850758e04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098198`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE UNIQUE, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 95: `9008b14d2cf87846` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099147`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR ABORT INTO p VALUES (FALSE, NULL); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 96: `d9e7f5e55dc5dc9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099806`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT DEFAULT -6084042359853412432.9); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 97: `14ed3406e63b4600` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099927`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT DEFAULT CURRENT_DATE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 98: `a10fd82b437fb3b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099937`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT X'1c15', c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 99: `0dd534e2349d8d75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101017`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT X'9B3bbcEbAe'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY CURRENT_TIME HAVING F
```

---

## Crash 100: `7dc3f1bce794064c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101898`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count(DISTINCT CURRENT_DATE) FILTER (WHERE CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 101: `5b759efa3281271e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102192`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (FALSE, NULL)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 102: `665fb0531733e54d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102549`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY TRUE HAVING TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 103: `6453cc6fb176d330` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT '9 G qM-_N B', rowid NUMERIC); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p
```

---

## Crash 104: `6f09790271e1ce6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT CURRENT_TIMESTAMP, rowid NUMERIC); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT IN
```

---

## Crash 105: `8292885cc47ba79a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103675`

```sql
SELECT printf('%.*e', -2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); INSERT OR REPLACE INTO t2 VALUES (CASE WHEN ~TRUE IS NOT NULL IS DISTINCT FROM CASE ~RAISE(IGNORE
```

---

## Crash 106: `d62ca02584aba04b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106145`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE, rowid BOOLEAN UNIQUE, a FLOAT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 107: `8c8bf4af0c18cf31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106286`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 108: `7ad766ddfe9d247f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106485`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-9223372036854775808)); CREATE
```

---

## Crash 109: `f73b5c6443ac5bf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106579`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT 502569353.552999353575); CREATE TABLE IF NOT EXISTS q(b DATE NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 110: `eb0e1175376480cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115920`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP END); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 111: `80fbb58a8455a50b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118826`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (FALSE) UNION VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 112: `b502041909124797` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121225`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL DEFAULT 6.603130152351391703450697334643716504259016E0723); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e3
```

---

## Crash 113: `aa0505ae4f944b4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121849`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT NULL, a INT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, b); SELECT t1.*, *, * FROM q
```

---

## Crash 114: `afdf7ebdd1d51e3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122037`

```sql
SELECT substr('__82 __X pf-1  ', -1, -1); SELECT round(0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2); INSERT INTO t3 SELECT * FROM p AS i__a548_n__4jn_bn
```

---

## Crash 115: `d0c2922695923bdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123200`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT DEFAULT X'4aebfDEFeBaaE3'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALU
```

---

## Crash 116: `a62f16581f5cd322` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138860`

```sql
SELECT printf('%.*e', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN WITH RECURSIVE s AS MATERIALIZED (SELECT CURRENT_TIMESTAMP AS b66o02_9_y_e045 ORDER
```

---

## Crash 117: `282a5604a43f42bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138989`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE)) UNION ALL VALUES (TRUE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 118: `b84bb8d334dff056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139612`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count(*) FILTER (WHERE TRUE) OVER (ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN CURRENT_DATE PRECEDING AND CURR
```

---

## Crash 119: `a76ea1314b9d7e2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140351`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); SELECT * FROM p WHERE EXISTS (VALUES (count(*) FILTER (WHERE FALSE) OVER ())); SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 120: `786cfdfc07457c4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148243`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN DEFAULT 40219); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 121: `2795312b56261e58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148414`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN DEFAULT ''); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('h  -O f_-Sb_XRj ', 1);
```

---

## Crash 122: `c0d645dfbfa225cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173385`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF N
```

---

## Crash 123: `819a84de8434f98d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173397`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABL
```

---

## Crash 124: `af02b7d969230d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173975`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY, b INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 FLOA
```

---

## Crash 125: `90ed9c6cdbebf7c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174198`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE, a FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 126: `1047719d3187485a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178103`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, *, * FROM p NOT INDEXED WHERE NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 127: `70ae599c1b227252` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178811`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT max(CURRENT_DATE) FILTER (WHERE CURRENT_TIME) IN (VALUES (NULL)) FROM p NOT INDEXED WHERE NULL; CREATE VI
```

---

## Crash 128: `78fe549791dc9971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179012`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT TRUE FROM p NOT INDEXED WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 129: `dd181a61223194c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179018`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT FALSE IN (VALUES (NULL)) FROM p NOT INDEXED WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 130: `94d9b0abb6fa42fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181734`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT 40219); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 131: `a5d55fdbb1163297` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181954`

```sql
SELECT hex(zeroblob(1)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELEC
```

---

## Crash 132: `2795f8899ac3367b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183941`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL), c2 NUMERIC NOT NULL)
```

---

## Crash 133: `5dd27a6ed6a4ae51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a TEXT CHECK (RAISE(IGNORE) > FALSE)); CREAT
```

---

## Crash 134: `8e0c8258efcaf13d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c2
```

---

## Crash 135: `d2fca9382a99895d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189005`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) VALUES (FALSE); VALUES (upper(CURRENT_TIMESTAMP)); SELECT printf(
```

---

## Crash 136: `0aac5ef835843b7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189900`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH p (a) AS (VALUES (CURRENT_TIMESTAMP)) SELECT ALL * FROM p NOT INDEXED; VALUES (TR
```

---

## Crash 137: `5d8eb1ac45d0f791` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192626`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_DATE ORDER BY FALSE ASC NULLS FIRST LIMIT -029.72260108
```

---

## Crash 138: `58b9e6ab93ade4db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194669`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (NULL) INTERSECT VALUES (count(*) OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIME ASC ROWS BETWEEN UNBOUNDE
```

---

## Crash 139: `14864ba692325542` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194869`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 140: `0640938f3b806625` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194875`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (NULL) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 141: `804b73128760b14c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194883`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (NULL) INTERSECT VALUES (count(*) OVER ()); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 142: `d11399ee76892258` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195471`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (count(DISTINCT NULL)) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 143: `e2c226dcb91f2823` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195596`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (random()) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 144: `390ef8559a49f249` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196622`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (total_changes()) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 145: `2e3dfcc0a54ced91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198719`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT DEFAULT 589439849579011781704407523195090113630010379218885827084574291844946773712782750438945049045774366254110668157972008432542042761081284936610356773547
```

---

## Crash 146: `9ef7d10ed7c4447c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199232`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT *, * FROM p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO 
```

---

## Crash 147: `975ddcbd03922ecc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200219`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT CURRENT_DATE, c1 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 148: `c35a080daff76580` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200487`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p
```

---

## Crash 149: `5d95b0175c6173ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200675`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 150: `650cef554571f4f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203893`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE COLLATE RTRIM IS NOT CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 151: `a126d5f3a99044c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205789`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT CURRENT_TIME ORDER BY FALSE ASC NULLS FIRST LIMIT FALSE)) ON CONFLICT DO NOTHING; VALUES (-count(*) FILTER (WHERE FALSE) 
```

---

## Crash 152: `0659a54d554c0bcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205953`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, -1e30
```

---

## Crash 153: `2671a5a11c08546a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206716`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY TRUE)) ON CONFLICT DO NOTHING; EXP
```

---

## Crash 154: `649115697c857470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206846`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT NULL ORDER BY FALSE ASC NULLS FIRST LIMIT TRUE)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL
```

---

## Crash 155: `483333fbfdd7eeb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210485`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); SELECT TRUE AS a FROM p INDEXED BY c1 NATURAL JOIN p , p NOT INDEXED WHERE +CURRENT_TIMESTAMP NOT BETWEE
```

---

## Crash 156: `2fc32494191d432c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211065`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL, rowid REAL, b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP >> CURRENT_T
```

---

## Crash 157: `e8e0bca331beaf0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213254`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT * FROM (VALUES (CURRENT_DATE)) AS gr_p76nbp_s_c6 GROUP BY FALSE ORDER BY TRUE)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLA
```

---

## Crash 158: `7be8548cdadcb600` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214119`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p VALUES ((SELECT CURRENT_TIME ORDER BY FALSE ASC NULLS FIRST LIMIT FALSE)) ON CONFLICT DO NOTHING; VALUES (group_concat(FALSE, '') FILTER 
```

---

## Crash 159: `ec0cdf45ae7b26d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219817`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME ORDER BY CURRENT_TIME DESC, CURREN
```

---

## Crash 160: `9b6e17e3ec9b51b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220307`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 161: `3591b2aaf9b43d5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222710`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (abs(CURRENT_DATE)) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 162: `63fb32cf156c1ac1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222836`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (count(*)) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 163: `e2a7cb22058ac8c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223586`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (abs(X'da3d')) EXCEPT VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 164: `a5e95ac4e5c26534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223716`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (total_changes()) EXCEPT VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 165: `908d18a2d1acb847` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223722`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (abs(TRUE)) EXCEPT VALUES (NULL) UNION VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 166: `48196db5617f0cc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223729`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (abs(X'da3d')) EXCEPT VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 167: `266e43634ef04b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224456`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (abs(CURRENT_DATE)) EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 168: `eb095aaf209c50b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227931`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIME); SELECT * FROM q LEFT JOIN q NOT INDEXED USING (c3) WHERE CURREN
```

---

## Crash 169: `f5cd49dfa3e723c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231778`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (upper(NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 170: `2c6fb7e2f2432159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231903`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q WITH s AS (SELECT *) VALUES (FALSE); VALUES (upper(upper(CURRENT_TIMESTAMP))); CREATE 
```

---

## Crash 171: `9c3e6aaf4cd6ff8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232041`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP); VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 172: `c874b02b77a19653` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232048`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP); VALUES (upper(total_changes())); CREATE VIRTUAL TABLE IF N
```

---

## Crash 173: `fc05d6cc2cf025d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (c2), c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 174: `c4494946afc30386` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233139`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (TRUE), c3 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 175: `dcf8afa418b6d093` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238199`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL IN (SELECT * FROM p NOT INDEXED ORDER BY TRUE ASC NULLS FIRST)); EXPLAIN QUERY PLAN VALUES (TRUE); SELECT round(0.0,
```

---

## Crash 176: `b12fda157ee3bd62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238684`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CAST(NULL AS FLOAT) IN (CURRENT_TIME, CURRENT_TIME, FALSE))); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLA
```

---

## Crash 177: `d3d77c491baab4dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241390`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED WHERE p.rowid IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); 
```

---

## Crash 178: `5cae50d1dcb4d8bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241484`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_TIME IS NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, 
```

---
