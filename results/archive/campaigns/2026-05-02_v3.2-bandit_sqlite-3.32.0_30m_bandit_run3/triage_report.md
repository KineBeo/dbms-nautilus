# Crash Triage Report

**Total crashes:** 201  
**Unique crash sites:** 201  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 201 | 201 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `869f09e0a7be6912` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000217`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (c1, _rowid_, _rowid_) VALUES (last_insert_rowid() == +RAISE(IGNORE)) ON CONFLICT(c3) DO UPDATE SET c1 = CURRENT_TIME NOT IN (SEL
```

---

## Crash 2: `6414d4ce092d6475` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000286`

```sql
SELECT printf('%lld', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); WITH RECURSIVE t2 (c2, _rowid_, c3, c3, b, c2) AS NOT MATERIALIZED (SELECT DISTINCT *, p.*
```

---

## Crash 3: `a63037d82b10887b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000437`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b, c3, c3, c3); INSERT OR REPLACE INTO p VALUES (TRUE >> CURRENT_TIME NOT BETWEEN TRUE & RAISE(IGNORE) AND CURRENT_TIMESTAMP COLLATE NOCAS
```

---

## Crash 4: `f1adbeb8ca3c301c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000864`

```sql
SELECT printf('%s', 4294967295, ''); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 5: `4789489dfbb03d76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000991`

```sql
SELECT round(-0.0, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2); INSERT INTO r (c3) VALUES (CURRENT_TIMESTAMP) ON CONFLICT(c1) DO UPDATE SET a = changes() + F
```

---

## Crash 6: `fb4d4f148d26b930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001194`

```sql
SELECT substr('6_', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY, b FLOAT PR
```

---

## Crash 7: `8b8c12c88a63c2d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003951`

```sql
SELECT hex(zeroblob(-1)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 8: `9cd08f3678559a65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004144`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT changes() AS h8__ UNION SELECT ALL NULL AS rp_e771_au__zw3i_p__m3h71_3753_4__net__252k175_5_
```

---

## Crash 9: `724b63917de8db56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004217`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT changes() AS h8__ UNION S
```

---

## Crash 10: `eabae6f151a5be4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004245`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO t3 VALUES (NOT EXISTS (VALUES (+TRUE) LIMIT RAISE(IGNORE), FALSE), NOT +FALSE COLLATE BINA
```

---

## Crash 11: `d0aeae78ee038abf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004360`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 12: `0587bfbc04a317ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004728`

```sql
SELECT substr('K_ucp-HI0', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT quote(CAST(CASE WHEN TRUE THEN CURRENT_DATE REGEXP iif(CURRENT_TIME, NULL, FALSE) FILTER (WHERE
```

---

## Crash 13: `2980f4843fe002d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005804`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (FALSE NOTNULL) RETURNING q.*; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE IS DISTIN
```

---

## Crash 14: `5f552a309b3bb243` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007194`

```sql
SELECT printf('%u', 2147483647, 'Ajz__ _3_0-_R'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c3); SELECT TRUE <= CURRENT_DATE OR FALSE >> CURRENT_TIME COLLATE BINARY AS g6qe, NOT NULL
```

---

## Crash 15: `34366b477bb45d8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007726`

```sql
SELECT printf('%.*g', -2147483648, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO r VALUES (NOT (CASE FALSE WHEN RAISE(IGNORE) IS NULL THEN last_insert_rowid() 
```

---

## Crash 16: `72aa17cedff89eab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007886`

```sql
SELECT round(0.0, 4294967296); SELECT substr('-___Y2Z_ - oDQJ3', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE p AS MATERIALIZED (VALUES (~FALSE == CURRENT_TIM
```

---

## Crash 17: `ddde1a98f33d520a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007936`

```sql
SELECT printf('%.*g', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO t1 VALUES (json_object('mkj-Q M- H5 -', c1) OVER (ORDER BY FALSE ASC, CURRENT_TIME DESC 
```

---

## Crash 18: `22d670ba06cb642d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007983`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q VALUES ((VALUES (RAISE(IGNORE) COLLATE NOCASE) ORDER BY FALSE NOT LIKE TRUE NOT NULL DESC NUL
```

---

## Crash 19: `6b047cd16f2a191c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015446`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 20: `8167d6b3028b706b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017762`

```sql
SELECT round(1e-308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, c2, c3, c2, c2); INSERT INTO q (c2, c3) VALUES (24882) ON CONFLICT(b) DO UPDATE SET c3 = (SELECT *, * 
```

---

## Crash 21: `797ff2a793032d39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017847`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, a, c2, c3, c2, c2); INSERT INTO q (c2, c3) VALUES (24882) ON CONFLICT(b) DO UPDATE SET c3 = (SELECT *, * FROM p AS
```

---

## Crash 22: `07241dd9d6b5c043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017917`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 23: `8cfd118cc366c62d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018341`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c3); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 24: `bf219113792321ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018355`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c3); INSERT INTO q DEFAULT VALUES; PRAGMA quick_ch
```

---

## Crash 25: `6227f7ad3dbd662d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018366`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, _rowid_); INSERT INTO q DE
```

---

## Crash 26: `c9defcd136ff0fb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018982`

```sql
SELECT printf('%lli', -2147483648, '2 __6_-'); SELECT printf('%.*f', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 DEFAULT VALUES; PRAGMA quick_c
```

---

## Crash 27: `28739e7e65f4c675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020755`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 28: `15d5bf6a27bbb920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020806`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE I
```

---

## Crash 29: `7772e5a261813e7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020986`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (TRUE OR CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (FALS
```

---

## Crash 30: `df3a92e66049b221` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021273`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (CURRENT_DATE OR CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALU
```

---

## Crash 31: `303bb436f4cbf987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021445`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_DATE)) OR CURRENT_DATE) ON CONFLICT DO NOTHING; E
```

---

## Crash 32: `540dc6cd772dddf9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021544`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_DATE)) OR CURRENT_DATE) ON CONFLICT DO NOTHING; E
```

---

## Crash 33: `4ef9a03180502b9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022089`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 34: `c03f3b445a8fb17e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022928`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT hex(zeroblob(2147483648));
```

---

## Crash 35: `83ef643f70648c54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023162`

```sql
SELECT substr('-1_v_v', 1, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT t3.* FROM r WHERE total_changes() != -0 COLLATE NOCASE) AS sub1; CREATE TABLE IF NOT EXIST
```

---

## Crash 36: `b158494bbcea1379` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024513`

```sql
SELECT printf('%.*e', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CASE WHEN TRUE THEN 0.0 END > CASE 
```

---

## Crash 37: `7473f48655667830` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025040`

```sql
SELECT printf('%lld', 1, ''); SELECT substr('l5Vx', -2147483648, -1); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 38: `0f8ab3a749d21d8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027593`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE, a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 39: `d86f288fec3f6afa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027910`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT X'03fcB4DcFCDc'); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 40: `7752d97a1b2fc711` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040222`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (CURRENT_DATE COLLATE BINARY); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 41: `b2c072694a9e4b30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040301`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL T
```

---

## Crash 42: `66a278d1fcbd550a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040326`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF 
```

---

## Crash 43: `566d145d333f555c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040786`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 44: `54a9568a7d1a3d34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040963`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 45: `237d0e7c4205bd3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040976`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT 
```

---

## Crash 46: `d1b05515161f3217` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040987`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT 
```

---

## Crash 47: `cd20dc9b8042266c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041685`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 48: `3865cb1b26cfd4e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042143`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE UNIQUE, b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 49: `cca87160d446c588` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042601`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 50: `e7037fb0c28c85a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042652`

```sql
SELECT round(-1.0, -9223372036854775808); SELECT printf('%x', 9223372036854775807, ''); SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT OR IGNOR
```

---

## Crash 51: `331532ccf2e4243d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043861`

```sql
SELECT printf('%.*s', 2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO r VALUES ((SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_DATE NOT NULL COLLATE N
```

---

## Crash 52: `d25c1c7072c0adc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044107`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TA
```

---

## Crash 53: `9cff5691e7ef350a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044230`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE != CURRENT_TIMESTAMP; CREATE VIRTUAL
```

---

## Crash 54: `db2ac51bc0c53b9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044475`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE != CURRENT_TIMESTAMP << TRUE COLLATE
```

---

## Crash 55: `00373d6e0fc680e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045910`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE NULL << CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 56: `7c67d19737851509` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046149`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE != TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 57: `b4eb8e2e98022289` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046697`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE << FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 58: `f0f5133165144186` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046729`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 59: `098e811ddb89969c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047457`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE OR RAISE(IGNORE); SELECT printf('%.*f', -2147483649, -
```

---

## Crash 60: `87366f70758cf5d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047809`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE << CURRENT_DATE; SELECT printf('%.*f', -214748
```

---

## Crash 61: `9480230e501387af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050984`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT GENERATED ALWAYS AS
```

---

## Crash 62: `b72c7ba09649ee26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051433`

```sql
SELECT round(1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, b); INSERT INTO p VALUES (random()) ORDER BY NULL NOT IN (FALSE ->> (FALSE COLLATE NOCASE) IN (WITH RECURSI
```

---

## Crash 63: `1ccee184b8d3393c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051672`

```sql
SELECT printf('%f', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT hex(zeroblob(9223372036854775807));
```

---

## Crash 64: `502453639bfb3eff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052562`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE p AS (VALUES (NULL) UNION VALUES (NULL)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 65: `6844065d3f300461` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052736`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE p AS (VALUES (NULL IS NULL) UNION VALUES (NULL NOT LIKE CURRENT_DATE)) SELECT * FROM p; SELECT
```

---

## Crash 66: `68836dbebca64564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052951`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE t2 AS (VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 67: `8e6894aa70231846` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052957`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE p AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 68: `331f76f472f15b57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054737`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 69: `30ebaf593bc59c86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056772`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) DEFAULT X'DeF9bBeBEF71E5'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF 
```

---

## Crash 70: `c33f3d1cd705d59c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057436`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) NOT NULL DEFAULT CURRENT_TIME, a INTEGER CHECK (TRUE), c1 DATE NOT NULL, c3 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FR
```

---

## Crash 71: `5c1dd8199d7f41f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057491`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY, a INTEGER CHECK (TRUE), c1 DATE NOT NULL, c3 INTEGER); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE C
```

---

## Crash 72: `ce7172fecd1c3d10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057497`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) NOT NULL DEFAULT CURRENT_TIME, c2 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE
```

---

## Crash 73: `bc25d07315e125b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057798`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE NULL IS TRUE NOTNULL; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 74: `a8c80c740cb6169f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057863`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE NULL IS CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 75: `122b87409ec413ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058135`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE | FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 76: `80e20ab3d8eb2543` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059742`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE IS CURRENT_TIMESTAMP COLLATE NOCASE; SELECT pr
```

---

## Crash 77: `1f0a0ccbe840aee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060803`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP || CURRENT_DATE; CREATE VIRTUAL
```

---

## Crash 78: `800e5dd10c73dcb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060930`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE FALSE % CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 79: `4895eb3ca55d7cb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061673`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP); CRE
```

---

## Crash 80: `26df8097b9363812` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061705`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 81: `4fe99d348b6a0f4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062116`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRE
```

---

## Crash 82: `901cf08a8d9f45b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062477`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP < CURRENT_TIMESTAMP; CREATE VIR
```

---

## Crash 83: `86d5061199fefa99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062810`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME GLOB NULL; CREATE VIRTUAL TABLE IF N
```

---

## Crash 84: `f0df5cb6df062a9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065316`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED NATURAL LEFT JOIN p AS a ORD
```

---

## Crash 85: `f62315ceb2a6f481` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065424`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 86: `53f91883675688ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069092`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 87: `eb89605e749481a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069417`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 88: `62c68eef311fccc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076967`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a * a) ); INSERT INTO p VALUES (CURRENT_DATE OR CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE
```

---

## Crash 89: `ab5a2b503800caaa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077253`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT X'06a3Fd'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 90: `35f2c6f0d4776ee0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077390`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_r
```

---

## Crash 91: `5cee85ae23c71945` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078133`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE FALSE IS NOT NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 92: `13eca598b5a79a0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084093`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIMESTAMP NOT LIKE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 93: `6ec6f96bad0d77d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087343`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE NULL ORDER BY CURRENT_TIME DESC NULLS FIRST; CREAT
```

---

## Crash 94: `c4f3ab3144b1345d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089649`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST, FALSE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF
```

---

## Crash 95: `30cb3ee80c76b20e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091467`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE, a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE TRUE; SELECT round(1.0,
```

---

## Crash 96: `1a0c61c6d62d02c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096293`

```sql
SELECT round(-1e308, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 (a) VALUES (NOT TRUE IN (VALUES (FALSE COLLATE RTRIM) ORDER BY CURRENT_TIME IS DISTINCT FROM 
```

---

## Crash 97: `866058fa76b8634c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097770`

```sql
SELECT printf('%.*s', 1, 1e-308); SELECT printf('%llu', 2147483647, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2); INSERT OR ROLLBACK INTO s VALUES (CURRENT_TIME + ~NOT RAISE(IGNOR
```

---

## Crash 98: `ceee1bc2d8880c0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100668`

```sql
SELECT substr('W-', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE LIKE RAISE(IGNORE) NOT NULL ESCAPE RAISE(IGNORE) AS 
```

---

## Crash 99: `3ed80c0c411e53d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101339`

```sql
SELECT printf('%.*f', 9223372036854775807, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c1, c1); WITH RECURSIVE s (c1, _rowid_) AS NOT MATERIALIZED (VALUES (TRUE)) SELECT * FRO
```

---

## Crash 100: `e9a040f346562f18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102255`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL) INTERSECT SELECT * FROM p; SELECT pr
```

---

## Crash 101: `9e7180bd54ba8890` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102452`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED; CREATE VIRTU
```

---

## Crash 102: `79ab4b3bdbec478c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102505`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN 
```

---

## Crash 103: `7f796b592f8fcee2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102992`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (FALSE); CREA
```

---

## Crash 104: `894d48d65430edbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104284`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (TRUE OR CURRENT_TIME) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (FALS
```

---

## Crash 105: `bf2f733f007eb034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105238`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE, c1
```

---

## Crash 106: `7e2320b23d484e60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108994`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT X'aaAA'); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 107: `62b29f55fe8639a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109098`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 108: `695ee8b2e01426cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109655`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (random() OR NULL)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*g', 
```

---

## Crash 109: `bd08a56adb281d85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113423`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT -733.72385446236313664456850808422425357E3836595088); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EX
```

---

## Crash 110: `f7699b2ea33d9313` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113576`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (count(*), CURRENT_DATE)); SELECT printf('%.*f', -214748
```

---

## Crash 111: `d0b569e03a13d85b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114523`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING 
```

---

## Crash 112: `ba68585cb6aae6c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115204`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (count(DISTINCT CURRENT_TIME), CURRENT_TIME)); CREATE VI
```

---

## Crash 113: `246a8b5b5079fbdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132440`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT SELECT ALL * FROM (VALUES (NULL))
```

---

## Crash 114: `f4521b96a54b93e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132889`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT SELECT ALL * FROM (SELECT * FROM 
```

---

## Crash 115: `19e34257ad294757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133015`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 116: `77f98f58b9aa4205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133021`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (FALSE); CREATE VIRTUAL TA
```

---

## Crash 117: `93f93162c93b72a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133030`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT SELECT ALL * FROM (VALUES (TRUE))
```

---

## Crash 118: `d90e30aa3a7a784f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133037`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT SELECT ALL * FROM (SELECT * FROM 
```

---

## Crash 119: `47ec6981ad81a628` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135053`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g
```

---

## Crash 120: `532c21c77af0b4b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141098`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (typeof(CURRENT_TIMESTAMP)
```

---

## Crash 121: `5eee0da4c2cff29b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141214`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (last_insert_rowid()); CRE
```

---

## Crash 122: `863909e47957dabd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141893`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (CURRENT_DATE NOT IN (SELE
```

---

## Crash 123: `d12344e5f7cf2b5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142047`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (avg(CURRENT_DATE) FILTER 
```

---

## Crash 124: `c501cdbd09b3e0fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143028`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) INTERSECT VALUES (-809036706253720525276
```

---

## Crash 125: `43877e85e781239d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143189`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (7.6e4529); CREATE VIRTUAL
```

---

## Crash 126: `3a89beb9278f8b46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143407`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (FALSE) EXCEPT VALUES (-809036706253720525276744
```

---

## Crash 127: `102646160b19e4ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153100`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT FALSE, c3 BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 128: `7347218b7a34102d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154800`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (count(DISTINCT NULL), CURRENT_TIME)); CREATE VIRTUAL TA
```

---

## Crash 129: `0cb697bd64f0e572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155739`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT avg(CURRENT_DATE) OVER (), * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE VIRTUAL TABL
```

---

## Crash 130: `4515e821ce7b2b17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156943`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE IF NOT EXISTS p(c2 BLOB, a GENERA
```

---

## Crash 131: `3e7777b969081ae8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156997`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL);
```

---

## Crash 132: `c67e90a95554d385` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157016`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (FALSE)); CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KE
```

---

## Crash 133: `247055d304b50362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157927`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (count(*), _rowid_, NULL)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 134: `dcf2b621f81650ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159227`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT ALL * FROM p ORDER BY count(*) OVER () ASC, CURRENT_DATE
```

---

## Crash 135: `9ec48bf2b28f8ee8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160862`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED NATURAL LEFT JOIN p NOT IN
```

---

## Crash 136: `c4a4dcef06ecc4ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160995`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED NATURAL LEFT JOIN p NOT IN
```

---

## Crash 137: `467e41d2c14b2bfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161001`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED NATURAL LEFT JOIN p NOT IN
```

---

## Crash 138: `c2b4373c34788cb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161525`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM p LEFT JOIN (VALUES (TRUE)) AS a ON TRUE
```

---

## Crash 139: `93f901bc8b72a7b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161676`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT count(*) OVER (PARTITION BY CURRENT_TIME, FALSE
```

---

## Crash 140: `b0611894f6ba820d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161875`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT count(*) OVER () FROM p WHERE CURRENT_TIMESTAMP
```

---

## Crash 141: `d6f95cb0280c18aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162344`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT count(*) OVER (PARTITION BY FALSE ORDER BY TRUE
```

---

## Crash 142: `5c62e8eff569bed1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162555`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED NATURAL LEFT JOIN p WHERE 
```

---

## Crash 143: `6d299e296fcfa63f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163391`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (NULL), b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT); INSERT INTO p (a) VALUES (NULL) ON CONFLICT(b) DO UPDATE SET b = CURRENT_TIME; 
```

---

## Crash 144: `46770e25039aa8a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164242`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF
```

---

## Crash 145: `054a2c7ea1f647e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164353`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 146: `6046adcea2203e60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165500`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (random() OR NULL)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); SELECT printf('%.*f', 
```

---

## Crash 147: `5bb92df32f3a51c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165830`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 INTEGER); INSERT OR IGNORE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTU
```

---

## Crash 148: `4989512344935dcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168681`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KE
```

---

## Crash 149: `a57a1f06b80100ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168951`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; VALUES (NULL) UNION SELECT ALL * FROM p; CREA
```

---

## Crash 150: `a2fcc0b8c2938993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169573`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (FALSE || FALSE IN (CURRENT_TIME)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN 
```

---

## Crash 151: `bfed3c68e36d248d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170039`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (-CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (FALSE)
```

---

## Crash 152: `e5ec96c5fccc6e8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170460`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p VALUES (FALSE OR CURRENT_DATE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 153: `780bfc5f0838543e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179305`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT X'03fcB4DcFCDc'); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(row
```

---

## Crash 154: `16c012f5b4e8294a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179392`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER NOT NULL DEFAULT CURRENT_DATE); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(rowid 
```

---

## Crash 155: `63cfa638f434fdab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180125`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL NOT NULL); SELECT TRUE LIKE CURRENT_TIME ESCAPE FALSE AS y1 INTERSECT VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 156: `70a8673a7c539eb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183574`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT DISTINCT * FROM (VALUES (TRUE)) AS a JOIN p NOT INDEXED ORDER BY CURRENT_TIME ASC NULLS FIRST LIMIT FALSE
```

---

## Crash 157: `204dc4e89a230174` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183655`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT DISTINCT * FROM p NOT INDEXED ORDER BY CURRENT_TIME ASC NULLS FIRST LIMIT FALSE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 158: `998d990191a53196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183887`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME ORDER BY CURRENT_DATE DESC NULLS FIRST LIMIT FALSE; CREATE VIRTUA
```

---

## Crash 159: `d587f99e941c446f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186862`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); SELECT * FROM (SELECT * FROM q WHERE CURRENT_TIME COLLATE RTRIM = CURRENT_TIMESTAMP) AS sub1; SELECT print
```

---

## Crash 160: `c073073ad0040431` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196684`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVE
```

---

## Crash 161: `0598a2446761ee62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196805`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT count(*)
```

---

## Crash 162: `a20012f272beec43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197583`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a + -71) ); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 163: `1b4adbb21dce3f8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197712`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 GENERATED ALWAYS AS (a * a) ); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 164: `49e712585e7c4e36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209079`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a + -71) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 165: `ea1ab925271a1210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209106`

```sql
SELECT printf('%d', -9223372036854775808, '0 v _-Z S'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); INSERT INTO q VALUES (CAST(CASE CURRENT_TIMESTAMP == TRUE NOT NULL WHEN FALSE 
```

---

## Crash 166: `7399333d0cacd218` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209156`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a + -71) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QU
```

---

## Crash 167: `30ed51fab1fa0a77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212851`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL DEFAULT X'2fceC8Ae'); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 168: `0eb0f0f47efe2519` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213915`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT count(*) OVER (PARTITION BY FALSE ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW E
```

---

## Crash 169: `9991c906fb07d349` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214023`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT '', c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 170: `d3fd49a0d1266f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214160`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT TRUE, c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 171: `0444ac02c6d913d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214747`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) INTERSECT VALUES (count(*) OVER (PARTI
```

---

## Crash 172: `27c438d792ba4cb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217884`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT ALL * FROM q ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST
```

---

## Crash 173: `551e2f72970322d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218245`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION SELECT ALL * FROM q ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CR
```

---

## Crash 174: `44471fdbba4cba7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219607`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE TABLE IF NOT EXISTS p(c2 NUM
```

---

## Crash 175: `6961ce3de59db960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220794`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT count(*) OVER (PARTITION BY FALSE ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN CU
```

---

## Crash 176: `319c16add992cd15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRE
```

---

## Crash 177: `e2d0192655643abc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221194`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL, b BLOB NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE 
```

---

## Crash 178: `49a1ae7458c14cd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221479`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT group_concat(CURRENT_DATE) AS mr4q__44 FROM p NATURAL JOIN p WHERE FALSE; CREAT
```

---

## Crash 179: `ec7426113af42507` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221929`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE COLLATE RTRIM IN (CURRENT_TIMESTAMP)
```

---

## Crash 180: `93aea87c91b12778` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222103`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME = CURRENT_TIMESTAMP; CREATE VIRTUAL 
```

---

## Crash 181: `3c3cfdd86f3021a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223878`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 182: `87092ba9ef52b638` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228701`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIMESTAMP)); SELECT p
```

---

## Crash 183: `7c366d4b93c1b6e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231799`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB GENERATED ALWAYS AS (TRUE) STORED, c1 BLOB); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE INDEX IF NOT EXISTS idx1 ON 
```

---

## Crash 184: `d0207dfc7ec8cd19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234520`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); WITH RECURSIVE p AS (VALUES (NULL) UNION SELECT * FROM (VALUES (NULL)) AS a_r8e7_8_w244iu_pa_tum1_60_w5__um) 
```

---

## Crash 185: `f681d4663a79f6d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236095`

```sql
SELECT printf('%.*s', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); INSERT INTO t3 VALUES (p.b * (-RAISE(IGNORE) | CURRENT_TIMESTAMP NOT BETWEEN FALSE & NULL AND TRUE REGEXP
```

---

## Crash 186: `b5dacec2d203386e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237220`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE ISNULL); VALUES (~NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT NU
```

---

## Crash 187: `e62c728d346ef77b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241612`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT -CAST(CURRENT_DATE AS REAL) AS rz_q1l_al FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 188: `803cf39d7c7cb981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241729`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p (c2) AS (VALUES (TRUE)) SELECT -CURRENT_TIME AS rz_q1l_al FROM p; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 189: `5b70d19425b1abe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE c2 NOT IN (SELECT * FROM p WHERE CURRENT_TIME); CREATE VIRTU
```

---

## Crash 190: `a88525a800940557` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE c2 NOT IN (VALUES (FALSE)); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 191: `5e1b2d895a12271f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248409`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE NOT FALSE NOT IN (CURRENT_TIME) OR NULL; CREATE V
```

---

## Crash 192: `4fef54cd208f27f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248482`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME NOT IN (CURRENT_TIME) OR NULL; CREAT
```

---

## Crash 193: `5a703e530f0c8c44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250310`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME < CURRENT_TIME COLLATE NOCASE; CREAT
```

---

## Crash 194: `7f9b3128cdfb7c4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251654`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT ALL * FROM (VALUES (CURRENT_TIME) UNION VALUES (CURREN
```

---

## Crash 195: `6790c512014bd5fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251903`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST
```

---

## Crash 196: `58b191e4f2f2e1fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251909`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT ALL * FROM (VALUES (CURRENT_DATE)) AS a ORDER BY CURRE
```

---

## Crash 197: `71a7809b7f2f8013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253138`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); VALUES (FALSE) EXCEPT VALUES (TRUE) EXCEPT SELECT ALL * FROM q ORDER BY FALSE ASC NULLS LAST; CREA
```

---

## Crash 198: `3d1c2a995520db45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254647`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) INTERSECT SELECT * FROM p WHERE CURREN
```

---

## Crash 199: `b45799d944653859` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259977`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a * a) UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE * CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 200: `81690dfbc506c3a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261367`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a + -6396) NOT NULL UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 201: `3aec64573e1fb395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261541`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---
