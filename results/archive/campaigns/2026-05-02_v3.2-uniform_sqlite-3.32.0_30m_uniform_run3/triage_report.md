# Crash Triage Report

**Total crashes:** 287  
**Unique crash sites:** 287  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 287 | 287 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `9817e7f1d84f89fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000420`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT * FROM t3 NOT INDEXED WHERE NULL ORDER BY TRUE ASC NULLS FIRST; CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); IN
```

---

## Crash 2: `12a2d302e3853dfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000426`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP; CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY, c2 BLOB GEN
```

---

## Crash 3: `e20f11c37b3a9992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000479`

```sql
SELECT printf('%f', 9223372036854775807, 'JY-u--d7y '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_, c3, c3, b, b); SELECT CURRENT_DATE UNION SELECT p.*, * FROM r GROUP BY CURRENT_
```

---

## Crash 4: `fcea4c7cbb283a6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000928`

```sql
SELECT printf('%d', 2147483647, 'Tu_cQ o_h0'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE s AS NOT MATERIALIZED (SELECT *) INSERT INTO p VALUES (NOT -CURRENT_DATE NOT NUL
```

---

## Crash 5: `7e89cfd095a418d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001072`

```sql
SELECT substr('-_A3b_O3 k', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, * FROM (SELECT CURRENT_DATE COLLATE RTRIM FROM r WHERE CURRENT_TIME NOT NULL LIKE 
```

---

## Crash 6: `9209be7857448ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001324`

```sql
SELECT printf('%lld', 9223372036854775807, ''); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 7: `d356c7ed533d7c18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001894`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); VALUES (NULL); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 8: `7ad4bc2784e89f34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002067`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHER
```

---

## Crash 9: `93122786daa8d28e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002115`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM
```

---

## Crash 10: `7c42c6bb466b722e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002151`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); VALUES (NULL); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 11: `fb7db6f6a1bdc6e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002331`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 12: `c1034521482ef877` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002498`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT IN
```

---

## Crash 13: `ef48487d81d066cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002513`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL
```

---

## Crash 14: `8c0b40c7a01b6c46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004778`

```sql
SELECT round(-0.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT ~NULL IS RAISE(IGNORE), t3.* FROM (VALUES (CURRENT_TIME) UNION ALL VALUES (NOT FALSE, TRUE)) AS a4i9__7
```

---

## Crash 15: `abd787bb175e7a20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006213`

```sql
SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO t1 VALUES (CURRENT_TIME AND CURRENT_TIMESTAMP >> trim(CURRENT_TIMESTAMP || CURRENT_DA
```

---

## Crash 16: `625d196896aca6a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006442`

```sql
SELECT printf('%lld', -1, 'r'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r (c2, c1, _rowid_) VALUES (NOT EXISTS (SELECT *, *, *, * FROM p LEFT JOIN q USING (c3, a) GROUP B
```

---

## Crash 17: `a0f02c310402092b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007043`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*d', 9223372036854775807, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (CURRENT_TIMESTAMP); CREATE TABLE IF NOT
```

---

## Crash 18: `0fc8c958c688d85c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008025`

```sql
SELECT substr('', 2147483648, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, a, c3); SELECT r.*, p.*, p.*, CURRENT_TIME COLLATE NOCASE / RAISE(IGNORE) IS DISTINCT FROM ~CURRENT_TIMEST
```

---

## Crash 19: `e2f205f740008ab5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008252`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT round(0.01, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (a) VALUES (+CURRENT_TIME NOTNULL & RAISE(IGNORE)); SELECT CU
```

---

## Crash 20: `c5803f38b43fc5be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008301`

```sql
SELECT printf('%.*e', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 VALUES (nullif(CURRENT_DATE * count(*) < CASE WHEN CURRENT_TIME THEN CURRENT_DATE !=
```

---

## Crash 21: `b6ede93aba089156` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008379`

```sql
SELECT substr('v_ e-j_ -_0J_ ', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT DISTINCT EXISTS (WITH RECURSIVE q AS NOT MATERIALIZED (SELECT * ORDER B
```

---

## Crash 22: `af574d774cc4c4bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015805`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p;
```

---

## Crash 23: `e0d9030ade7414f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016017`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; VALUES (TRUE);
```

---

## Crash 24: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016345`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 25: `b2f5267f64938527` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016427`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL GENERATED ALWAYS AS (NULL) VIRTUAL, c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 26: `45a1e782347caee3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016619`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 27: `7fa7f82e8f9f90c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016841`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 28: `6027af06556b5592` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017030`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE NOT 
```

---

## Crash 29: `a9b7b74d1b5399cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017287`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 30: `c6160c95719dbd4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017771`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 31: `d3690fec47d6e78b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017950`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT -9.6e674260); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 32: `fd23d5df384805fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018620`

```sql
SELECT substr('', 9223372036854775807); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 33: `a3e9097248907cc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018951`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHERE RAISE(IGNORE)) AS sub1; SELECT hex(zeroblob(4294967295));
```

---

## Crash 34: `b79edd00f7997726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019131`

```sql
SELECT substr('7', -2147483649, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHERE RAISE(IGNORE)) AS sub1; SELECT hex(zeroblob(4294967295));
```

---

## Crash 35: `fdc45062e73d5464` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021694`

```sql
SELECT printf('%.*g', 2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHERE TRUE) AS sub1; SELECT hex(zeroblob(1));
```

---

## Crash 36: `90df121e6f22893b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021852`

```sql
SELECT printf('%u', 9223372036854775807, 'JY-u--d7y '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 37: `b24652d8113eeedd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021884`

```sql
SELECT substr('- --p', -9223372036854775808, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 38: `d0978acfc4ebad60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021898`

```sql
SELECT substr('iv-aY_W R- ', 1, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 39: `0223ebc2a0b0348a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021905`

```sql
SELECT printf('%.*g', 0, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 40: `ec70e1f2cbb71fc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021919`

```sql
SELECT round(1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 41: `a1907af5af1bdf20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021948`

```sql
SELECT printf('%s', -2147483648, ' _0iOy _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 42: `54f4331877a103b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021958`

```sql
SELECT printf('%lld', -9223372036854775808, '- __K_4- Q-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 43: `b03d4be9dccb3587` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021964`

```sql
SELECT printf('%f', 9223372036854775807, 'JY-u--d7y '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, a, c3, c2, c2, b, c3, c1); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 44: `639a05bdfb6caa89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022016`

```sql
SELECT printf('%f', 9223372036854775807, 'JY-u--d7y '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a
```

---

## Crash 45: `c3947603982262a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex(zeroblob(-21
```

---

## Crash 46: `0a57835e8297e387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024966`

```sql
SELECT printf('%.*f', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHERE TRUE) AS sub1; SELECT hex(zeroblob(1));
```

---

## Crash 47: `94e81bb052a842a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031606`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT OR FAIL INTO p VALUES (TRUE <> CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 48: `731037825e924eb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032388`

```sql
SELECT substr('_ ', 9223372036854775807, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 49: `540351c2eeff08b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032686`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE NULL BETWEEN TRUE AND TRUE >= NULL) AS sub1; CREATE VIRTUAL 
```

---

## Crash 50: `4fdda0cbfecf4df1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033737`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_DATE FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 51: `d46d9a31d184304e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034933`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 52: `c2ee8e661a4db3a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035119`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TI
```

---

## Crash 53: `b00cde310250caec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036137`

```sql
SELECT printf('%.*d', 2147483647, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES (RAISE(IGNORE)); SELECT hex(zeroblob(4294967295));
```

---

## Crash 54: `92c3987652ed9f15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036206`

```sql
SELECT printf('%.*d', 2147483647, 1.0); SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_, c1); INSERT OR ABORT INTO q VALUES (group_concat(total_chan
```

---

## Crash 55: `73a933b3d90d6166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037640`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION SELECT NULL * CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 56: `34c4a9271154f28f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038670`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM q WHERE TRUE GROUP BY TRUE WINDOW w1 AS () LIMIT FALSE; CREATE VIRTUAL TABLE IF
```

---

## Crash 57: `adf36637e2af2e0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039068`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_TIME > CURRENT_DATE || TRUE; CREATE VIRTUA
```

---

## Crash 58: `d737174cab006550` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039792`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 59: `d6d44eac901f7234` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041910`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 60: `b785f5a810f53033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044941`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE)) NOT NULL) ON CONFLICT D
```

---

## Crash 61: `8c7aea359f13f288` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045820`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE IS NULL))) ON CONFLICT DO
```

---

## Crash 62: `df0d7647a28444f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048570`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM s
```

---

## Crash 63: `a5c20a29722d9090` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049690`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (NULL / FALSE)); CREATE TABLE IF NOT EXISTS q(b 
```

---

## Crash 64: `13d02bbdd23a5ead` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049722`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a BLOB, c1 GENERATED ALWAYS AS (a * a) NOT NULL); INSERT INTO p 
```

---

## Crash 65: `e54e27e250e3c977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049858`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC, c2 GENERATED ALWAYS AS (a + 45795) UNIQUE); INSERT I
```

---

## Crash 66: `89fc919080c08b35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049973`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRE
```

---

## Crash 67: `a877b978d1174e19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049995`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (json_type(TRUE) FILTER (WHERE CU
```

---

## Crash 68: `730ab580e7107aff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050007`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALU
```

---

## Crash 69: `373e27425896e95d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050127`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL IS NOT TRUE BETWEEN CURRENT_TIME AND NULL), 
```

---

## Crash 70: `746f2f0e04fe5f9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050147`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CASE WHEN CURRENT_TIMESTAMP < CASE WHEN TRUE | 
```

---

## Crash 71: `a41db5391afbe6d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050170`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); SELECT printf('%.*e', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 72: `c76e56fcd1c1e03a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053284`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); SELECT printf('%x', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 73: `87a797c09a1ff132` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053419`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 BOOLEAN CHECK (NULL * RAISE(IGNORE) NOT IN (CURRENT_TIMESTAMP, CURRENT_TIME) OR FALSE > TRUE), c3 T
```

---

## Crash 74: `e4346f226b089521` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053497`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NU
```

---

## Crash 75: `07e50df7f15db6a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054317`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURR
```

---

## Crash 76: `92c1b20402653cf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054328`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SEL
```

---

## Crash 77: `887fd010a541132a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054380`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC D
```

---

## Crash 78: `e0a9e56c7859a3b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054688`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c1 GENERATED ALWAYS AS (a IS NULL) UNIQUE, rowid INT PRIMARY KEY); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALU
```

---

## Crash 79: `89ba8aa1d2c2e466` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054699`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL IS NOT TRUE), a NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREAT
```

---

## Crash 80: `4377f66c7a3465a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057502`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_DATE); PRAGMA integrity_check; SELECT print
```

---

## Crash 81: `a2452aab57e8eccb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057765`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; SELECT hex(zeroblob(-922337203685477
```

---

## Crash 82: `a4be28d1393f0d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057870`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.
```

---

## Crash 83: `a083ed8ab25c126f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057907`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL T
```

---

## Crash 84: `35dc086b25e20c23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058319`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 85: `dd6bab34ff2d8f97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058472`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << FALSE); PRAGMA quick_check; SELECT printf('%.*g', 2
```

---

## Crash 86: `64e43f70e500bd08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM q GROUP BY NULL, RAISE(IGNORE) ORDER BY NULL DESC NULLS LAST; INSERT INTO p DEFAULT 
```

---

## Crash 87: `0026a6b2975913cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059842`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT count(DISTINCT CURRENT_DATE
```

---

## Crash 88: `7e800058f0bb2f79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060587`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC PRIMARY KEY); CREATE TABLE 
```

---

## Crash 89: `ce2ec6568b4994a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061080`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE, c1 DATE UNIQUE); CREATE V
```

---

## Crash 90: `4096a4453d7b2bb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062200`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT); VALUES (NULL AND 0.0); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 91: `b4525443957927be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062401`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (NULL AND CURRENT_TIMESTAMP); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 92: `6770a3ede0f64ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062407`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (NULL AND TRUE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 93: `730a1f6a3f65bf7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064279`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN q WHERE TRUE GROUP BY TRUE WINDOW w1 AS () LIMI
```

---

## Crash 94: `3e2e139e7005c752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064934`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (changes() FILTER (WHERE RAISE(ABORT, 'U  5x2 O0_
```

---

## Crash 95: `0852e782ef8fbedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066269`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c3 FLOAT GENERATED ALWAYS AS (CURRENT_TIME <= TRUE) VIRTUAL); CR
```

---

## Crash 96: `873c0469879d2f9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066296`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT IN
```

---

## Crash 97: `c17dff269a88c4c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066486`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b INT, _rowid_ GENERATED ALWAYS AS (coalesce(a, b)) , c2 TEXT GE
```

---

## Crash 98: `000d632040b8b6b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066844`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); EXPLAIN QUERY PLAN SELECT ALL count(*) FILTER
```

---

## Crash 99: `eab79bafdc6f3864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067038`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 REAL)
```

---

## Crash 100: `4a14bea51090c3a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067134`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELEC
```

---

## Crash 101: `fa18263cdc708875` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067342`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p SELECT ALL 
```

---

## Crash 102: `088d353800613332` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067910`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(a INTEGER CHECK (NOT 
```

---

## Crash 103: `c1e2d5d14a521691` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067922`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT CURRENT_TIME, c1 DATE UNIQUE); CREATE
```

---

## Crash 104: `75aeb51214453af8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067941`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 BLOB GENERATED ALWAYS AS (NOT EXISTS (WITH q AS (VALUES (FALS
```

---

## Crash 105: `6f70f6ea08ef3226` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068201`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRE
```

---

## Crash 106: `3516f1e8c9bad0d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068424`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BLOB); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid TEXT); VALUES (NULL A
```

---

## Crash 107: `eec2f0d6e70ddde7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070256`

```sql
SELECT printf('%.*e', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (RAISE(IGNORE)) ON CONFLICT DO NOTHING; WITH RECURSIVE t3 (c3) AS (SELECT TRUE A
```

---

## Crash 108: `2955d047338b4c04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070757`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (VALUES (CURRENT_TIMESTAMP)) AS sf__ LEFT 
```

---

## Crash 109: `d11dd6e099a492bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071068`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT count(*) FILTER (WHERE CURRENT_TIME))) 
```

---

## Crash 110: `ccd5602bd6d64a5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071226`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT TRUE)) ON CONFLICT DO NOTHING; PRAGMA i
```

---

## Crash 111: `04ac9edfc90a8bff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071239`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CAST(TRUE AS BOOLEAN) NOT IN (VALUES (CURRENT_TIMESTAMP))) ON CONFLICT D
```

---

## Crash 112: `9fcdb9f7fc7b0f56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071532`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP))) ON CONFLICT DO NOTHING
```

---

## Crash 113: `9a020f3d7f8b4d0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072358`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL DEFAULT X'8aCE'); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREAT
```

---

## Crash 114: `90b38a7038acc043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073630`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIME
```

---

## Crash 115: `c5a712888cb852c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074204`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE))) ON CONFLICT DO NOTHING; P
```

---

## Crash 116: `1aa1119a91753e5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081204`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 117: `e05f053e4f87a4ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081322`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 118: `1cf28e50b13bf88d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081677`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 119: `4227220c960e6fd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081814`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 120: `deabf94655d543f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081928`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 121: `1c36f50ba8ca8021` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081937`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 122: `07edd5b3ceb25cde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083077`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 123: `07fc688efec6bced` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084688`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 124: `7409f6a144c092af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084945`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP < CURRENT_TIME * _rowid_; CREATE
```

---

## Crash 125: `1e38d1447fff856a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085172`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED LEFT OUTER JOIN q NOT INDEXED ON TRUE WHERE CURRENT_TIME
```

---

## Crash 126: `130b86e244e21feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085546`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM q WHERE TRUE GROUP BY TRUE WINDOW w1 AS () LIMIT CAST(TRUE AS BOOLEAN) < NULL; 
```

---

## Crash 127: `fd9c387d34541c3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086492`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN q LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 128: `e444a9dfbe84e09d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086729`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN p AS u LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 129: `37147d99bdca40c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087632`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (FALSE); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 130: `126167bccb1df900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089522`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (NULL); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 131: `b0292c67b242f01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091694`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 132: `029182f366a91daa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093732`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TI
```

---

## Crash 133: `3259ead8841d0c29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095989`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_TIME * CURRENT_DATE); PRAGMA integrity_check; CREATE 
```

---

## Crash 134: `b19c7ecabacbe93e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096588`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED LEFT OUTER JOIN 
```

---

## Crash 135: `678deefbe6e1c26d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097045`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TI
```

---

## Crash 136: `c66e5c1bc0b82cb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097540`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255) NOT NULL DEFAULT X'fbD9Df35C4F2'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE V
```

---

## Crash 137: `4d530bb363ea4c7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097711`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*f', -2147483649, -1e308
```

---

## Crash 138: `bb6b98a926cdfe84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098205`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_TIME COLLATE BINARY ISNULL AS w50w FROM p WHERE NULL) AS sub1; CREA
```

---

## Crash 139: `12c6826afca79339` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098348`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE, c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_DATE FROM p WHERE NULL) AS sub1; SELECT printf('%
```

---

## Crash 140: `9fe58cae8d156003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098581`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT *, count(*) FILTER (WHERE FALSE) OVER (), * FROM p WHERE FALSE) AS sub1; CR
```

---

## Crash 141: `da8ba6bc4b20cb9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098895`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT -9838499593926328959.857834383705347440951, c3 FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FRO
```

---

## Crash 142: `87224f0d62d4f8d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099343`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE NULL BETWEEN TRUE AND TRUE IS NOT NULL >= TRUE) AS sub1; CRE
```

---

## Crash 143: `e2e8dee6743a21f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100150`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE & CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 144: `a427e5201e7aacde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100465`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME MATCH CURRENT_DATE) AS sub1; CREATE VIRTUAL TAB
```

---

## Crash 145: `3b403524c8150fa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT count(*) FILTER (WHERE TRUE) OVER (ORDER BY FALSE DESC NULLS LAST ROWS BETWEEN UNBOUNDED P
```

---

## Crash 146: `187004c56d74b1a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP NOT IN (VALUES (CURRENT_DATE))) AS sub1; C
```

---

## Crash 147: `02be334a3beee562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101208`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE _rowid_ >= NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 148: `1e365310ffd3c20c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102377`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR FAIL INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 149: `d04189577125df04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103402`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION SELECT TRUE AS p_5 ORDER BY TRUE DESC;
```

---

## Crash 150: `df985522323b7c15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104280`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL DEFAULT -44.957713293072271135455205903842727915199113427550278764077148970461301718440157508352276699085
```

---

## Crash 151: `8e05fa6fe729f98a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113945`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELE
```

---

## Crash 152: `751eaa6669161706` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115242`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q NOT INDEXED WHERE changes() FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TI
```

---

## Crash 153: `b55168d6d48df68c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115573`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (CURRENT_TIME)) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE
```

---

## Crash 154: `4c8a2a0f886c8b64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115993`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (NULL NOT BETWEEN TRUE AND CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 155: `200baaa96ff7b623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116235`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_TIMESTAMP - CURRENT_TIMESTAMP - CURRENT_TIMESTAMP - CURRENT_TIMESTAMP - CURRENT_TIMESTAM
```

---

## Crash 156: `76c967fc3a741794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119419`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT CURRENT_TIME, c1 FLOAT PRIMARY KEY, _rowid_ VARCHAR(255) NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (CURRENT_
```

---

## Crash 157: `04e427da1447bafe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124528`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT -3); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 158: `4e97be7c5783424d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124692`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT -9.6e674260); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 159: `7164aea2562a2e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124821`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT -9.6e674260); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 160: `cdd8fbf3aa7124cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124934`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 161: `f2184fb03f3edb48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125224`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL), a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 162: `c0045dd97a6d1aa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125379`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL), a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 163: `3f08e95431151a37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125406`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL), a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integri
```

---

## Crash 164: `d8525f58ed4aa3ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126568`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'b64C'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 165: `6f4f568c90755ce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126693`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 166: `08c0b8e92473c796` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126851`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 167: `a2457cbafad5a48d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127416`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC DEFAULT X''); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 168: `5a4020ba910fdb33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129890`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); EXPLAIN QUERY PLAN SELECT ALL * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SEL
```

---

## Crash 169: `85ead378cc51fd09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151708`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT -6122); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 170: `22239003fa179ed6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152689`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid DATE NOT N
```

---

## Crash 171: `fcef8fd88b7c39dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153276`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL), a NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b VAR
```

---

## Crash 172: `61f73f8e7fca8c64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153476`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT X'cDCBBCEFcab6f5'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 173: `03b5cfcc9f8ac204` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154007`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT -9.6e674260); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 174: `a98ca92da657362e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154211`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 175: `b7d9527f9c616bd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154856`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 176: `fb2b76152aca74e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154978`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 177: `1caaa11760373c63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161833`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE NOT BETWEEN TRUE AND CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 178: `1fd06f8592805d80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170827`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(c2 INT NOT NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE) UNION SELECT TRUE AS p_5 ORDER BY CURRENT_DA
```

---

## Crash 179: `1f7d5e686dca66cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172377`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 180: `bd83fa4729bbe936` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172583`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE _rowid_ >= TRUE || FALSE) AS sub1; CREATE VIRTUAL TABLE IF N
```

---

## Crash 181: `5d7725358788d14e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172745`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE _rowid_ >= TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 182: `5ffbf781caedcbc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172820`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE, rowid BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE _rowid_ >= NULL) AS sub1; CREA
```

---

## Crash 183: `163ef4767a3a1f66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173566`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP >> TRUE) AS sub1; CREATE VIRTUAL TABLE IF 
```

---

## Crash 184: `26d927b29c8a4418` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174102`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT * FROM p WHERE ~NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 185: `16d8d5ba114e2e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175007`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT NULL AS f_5d_5c_k46_0_7_ FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE 
```

---

## Crash 186: `c27ab9c7848a9cfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175395`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM (SELECT CURRENT_TIME COLLATE BINARY AS w50w FROM p WHERE NULL) AS sub1; SELECT prin
```

---

## Crash 187: `f6c86db614ae90a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175624`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 188: `12c452819348d041` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175778`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 BLOB NOT NULL, c3 DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF 
```

---

## Crash 189: `8a2d0e3af0b546b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175942`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 190: `ae5daca84639eafc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176639`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TI
```

---

## Crash 191: `38dc56fd53d64c20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176786`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED LEFT OUTER JOIN 
```

---

## Crash 192: `ff5e4a2acec0b682` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177075`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_TIME * CURRENT_DATE * CURRENT_DATE * CURRENT_DATE); P
```

---

## Crash 193: `50c7091669f43390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177270`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_DATE * CURRENT_DATE * CURRENT_DATE); PRAGMA integrity
```

---

## Crash 194: `b8c694a37b634328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177291`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 195: `99190f971de8ad37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177298`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_TIME * CURRENT_DATE * CURRENT_DATE); PRAGMA integrity
```

---

## Crash 196: `a64659086c9d8b89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177346`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_TIMESTAMP * CURRENT_DATE * CURRENT_DATE * CURRENT_DAT
```

---

## Crash 197: `407e7b60a26f80c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178373`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q (_rowid_) VALUES (CURRENT_TIMESTAMP * CURRENT_DATE * CURRENT_DATE * CURRENT_DAT
```

---

## Crash 198: `8d1c84f6b12b18e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178936`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED LEFT OUTER J
```

---

## Crash 199: `b99298dce6488460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179139`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED LEFT OUTER J
```

---

## Crash 200: `93ad113a95b40e5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179860`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT NOT EXISTS (SELECT ALL * FROM (VALUES
```

---

## Crash 201: `5561407ca1d8cee7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180744`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p JOIN (q CROSS JOIN p AS 
```

---

## Crash 202: `15d9ebc318f2996a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183504`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p WHERE EXISTS (SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f
```

---

## Crash 203: `026185c7473090a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184777`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (FALSE) UNION SELECT random() * CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 204: `0be58f401b55bc2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184957`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (FALSE) UNION SELECT TRUE LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 205: `c420ce744fb5f658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186886`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION SELECT upper(EXISTS (VALUES (CURRENT_TIMESTAMP))) * CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*f', 21474
```

---

## Crash 206: `78b26473570ee12a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187162`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION SELECT CAST(CURRENT_TIMESTAMP AS BLOB) LIMIT TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 207: `8d4695178c5f2a68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187287`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION SELECT last_insert_rowid() LIMIT TRUE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 208: `0edff1ee546abf40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188218`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION SELECT CURRENT_TIMESTAMP LIMIT TRUE OFFSET CURRENT_TIMESTAMP - CURRENT_TIMESTAMP; SELECT printf('%.*f', -2147
```

---

## Crash 209: `e1e61abaa314cd7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188885`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT NULL * CURRENT_TIMESTAMP LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 210: `d22931234cc77644` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192140`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE FALSE) OVER (PARTITION BY CURRENT_DATE ORDER BY CURRENT_TIMESTA
```

---

## Crash 211: `f605971163f72c0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192455`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN (p AS a JOIN p USING (c1)) LIMIT FALSE; CREATE VIRT
```

---

## Crash 212: `163d4c08670d9058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193049`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN q WHERE TRUE GROUP BY NULL, NULL WINDOW w1 AS () LI
```

---

## Crash 213: `9af059d8c7210e77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED LEFT OUTER JOIN q NOT INDEXED ON TRUE WHERE CASE WHEN TR
```

---

## Crash 214: `fdb210ba9a5015d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193710`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE CASE WHEN TRUE THEN FALSE ELSE CURRENT_DATE END; CREATE VIRTUA
```

---

## Crash 215: `a515a2978b9d859c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193803`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED LEFT OUTER JOIN q NOT INDEXED ON TRUE WHERE CURRENT_TIME
```

---

## Crash 216: `1447340a06ffa724` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194224`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED LEFT OUTER JOIN q NOT INDEXED ON CURRENT_TIME NOT LIKE T
```

---

## Crash 217: `77daf728b1bf5cde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194571`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (CURRENT_TIME)) AS nve__3_ WHERE CURRENT_TIMESTAMP < CURRENT_T
```

---

## Crash 218: `7ffef777e9aaba0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194936`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL LEFT JOIN q WHERE TRUE GROUP BY TRUE WINDOW w1 AS () LIM
```

---

## Crash 219: `5893b429285fe390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL JOIN (SELECT ALL * FROM q NOT INDEXED LEFT OUTER JOIN p NOT 
```

---

## Crash 220: `68936062e7a1f3c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198216`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT count(*) FILTER (WHERE FALSE) OVER (ORDER BY TRUE DESC NULLS LAST ROWS BETWEEN CURRENT ROW AND UNBOUNDED 
```

---

## Crash 221: `aaa76e29092f60e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198226`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * FROM p WHERE FALSE GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_DATE LIMIT TR
```

---

## Crash 222: `482ddc5515d0f51d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198232`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT count(*) FILTER (WHERE FALSE) OVER (PARTITION BY TRUE ORDER BY CURRENT_DATE ASC R
```

---

## Crash 223: `e0ee2c113f0096c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198253`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 224: `0155dc8a7152e5f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198259`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT TRUE, * FROM p NOT INDEXED WHERE FALSE; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r
```

---

## Crash 225: `0aed5d52a535a0ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198268`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT json_type(CURRENT_TIMESTAMP) AS jmc_; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y7599199
```

---

## Crash 226: `2ec057e5b528d2b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198297`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT count(*) OVER () LIMIT TRUE; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__
```

---

## Crash 227: `20053d167ed77e20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198319`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_TIMESTAMP < FALSE > TRUE)); CREATE TABLE IF NOT EXISTS q(b INT); INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423
```

---

## Crash 228: `c7e25669a26a3656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198327`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 229: `b9282b885745380b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198355`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB GENERATED ALWAYS AS (NULL) STORED, c1 BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f
```

---

## Crash 230: `056520aa136e6440` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198439`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.*; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti
```

---

## Crash 231: `af87283602778def` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198882`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 232: `dee759f6516b4371` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199779`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT TRUE AS u7gwqv_9__3v_b_bgv_3__5_6_r67_y75991991f7f_o8__q_423__9t8g__3b1_x57nwti__
```

---

## Crash 233: `4a998d598079ff7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202350`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (CURRENT_DATE) UNION SELECT TRUE AS p_5 ORDER BY TRUE DESC; SELECT min(NULL) FILT
```

---

## Crash 234: `c4c1f0918b29516e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211364`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP + CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA quick_c
```

---

## Crash 235: `e5cd256173d03704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212096`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE))
```

---

## Crash 236: `2163208a45de248a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212487`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (NOT CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE
```

---

## Crash 237: `090b503038369ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213012`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT UNIQUE); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; PRAGMA integrity_check; SELECT printf('%.*g', 21474
```

---

## Crash 238: `387588ad0cd19560` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213178`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT NOT NULL); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 239: `33332151dd17f0ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213362`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE
```

---

## Crash 240: `d72291bede6f7648` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214273`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CAST(TRUE AS BLOB) NOT IN (VALUES (FALSE))) ON CONFLICT DO NOTHING; PRAG
```

---

## Crash 241: `1a848b7e144c1da0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214487`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CAST(TRUE AS BLOB))) NOT IN (VALUES (FALSE)
```

---

## Crash 242: `bfed8b5ba89ac7a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214637`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (FALSE NOT IN (VALUES (FALSE))) ON CONFLICT DO NOTHING; PRAGMA integrity_
```

---

## Crash 243: `30541f0774604196` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214643`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_DATE)) NOT IN (VALUES (FALSE))) ON 
```

---

## Crash 244: `720a7c6e91d4913d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)) NOT IN (VALUES (FALSE))) ON 
```

---

## Crash 245: `89c1420e9e6ba274` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215337`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CAST(TRUE AS VARCHAR(255))) ON CONFLICT DO NOTHING; PRAGMA integrity_che
```

---

## Crash 246: `a738567fd36a0d91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (CURRENT_DATE NOT IN (SELECT -723.01E-97198213442262110317742781172224475
```

---

## Crash 247: `620492eb4c468de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216593`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN NOT NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (SELECT ALL * FROM (SELECT ALL * FROM (SEL
```

---

## Crash 248: `211f54badde605b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223028`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQU
```

---

## Crash 249: `8df300ded1e1a8a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b BLOB GENERATED ALWAYS AS (NULL << FALSE COLLATE RTRIM
```

---

## Crash 250: `e7882fbc36e7bd2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226575`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid VARCHAR(255), c2 TEXT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN q WHERE TRUE GROUP BY TRUE
```

---

## Crash 251: `3f007bdd0f8f1ca5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226770`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INT DEFAULT CURRENT_DATE, c3 DATE); EXPLAIN QUERY PLAN SELECT * FROM p CROSS JOIN q NATURAL JOIN q WHERE TRUE GROUP BY T
```

---

## Crash 252: `2444972ecd17fe25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231003`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT E
```

---

## Crash 253: `14b4e7422c7f1437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231708`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN CHECK (RAISE(IGNORE) NOT IN (CURRENT_TIMESTAMP, CURRENT_TIME)), c3 TEXT UNIQUE); VALUES (FALSE, CURRENT_TIME) EXCEP
```

---

## Crash 254: `c8dc0a8c00340a05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231919`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INT PRIMARY KEY, c3 TEXT UNIQUE); VALUES (FALSE, CURRENT_TIME) EXCEPT SELECT * FROM q WHERE FALSE ORDER BY CURRENT_TIME DES
```

---

## Crash 255: `d6f9e29fe683a948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232244`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY, c2 REAL UNIQUE); VALUES (NULL); SELECT printf('%.*g', 2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 256: `03ac744af66c0a97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232370`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) GENERATED ALWAYS AS (NULL > (SELECT *)) VIRTUAL, c3 FLO
```

---

## Crash 257: `783a5c783ff35365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236922`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << typeof(NULL)); PRAGMA quick_check; SELECT printf('%
```

---

## Crash 258: `fb0e5f6548a45d2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236986`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << FALSE - CURRENT_DATE); PRAGMA quick_check; CREATE V
```

---

## Crash 259: `465043aed862c62f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237358`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA quick_check; CREATE VIRTU
```

---

## Crash 260: `cfe8c06abec3b4d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237623`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL CHECK (NULL)); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 261: `c4980f1f75d2b603` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237779`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (FALSE / CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 262: `026281a460926e2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237981`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (NOT EXISTS (SELECT ALL * FROM q NOT INDEXED) / FALSE); PRAGMA quick
```

---

## Crash 263: `6cf99653bb297294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238144`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (TRUE | NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 264: `375b5bb8124f7323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238664`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 265: `16b928d5aecbcc52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239111`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 266: `0c32d670e03ee744` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239308`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 BOOL
```

---

## Crash 267: `1dcb0bc9e882551a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239352`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 TEXT
```

---

## Crash 268: `d8dcecac9277fef7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240441`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (min(NULL)); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 269: `047e5a0de0376bde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241798`

```sql
SELECT printf('%.*d', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); EXPLAIN QUERY PLAN SELECT rowid / CURRENT_TIMESTAMP % NULL COLLATE BINARY IS NOT NULL IS NULL A
```

---

## Crash 270: `b47533285bb763ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242318`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES ((VALUES (CURRENT_DATE)) IN (FALSE)); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 271: `07bd8c8655e6aeed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243712`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p
```

---

## Crash 272: `5604d5b7edd17e62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244747`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES ('-ESd-u_ YY--j-5'); PRAGMA quick_check; SELECT printf('%.*f', -2147
```

---

## Crash 273: `9e2808b27f7ab9f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 274: `d017a6b997230b49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245339`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 275: `619f060b9f16f78f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245570`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ VARCHAR(255) NOT NULL); REPLACE INTO p VALUES (NOT ''); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 276: `9a5afdb9638f630d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246919`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 DATE NOT NULL); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * FROM (SELECT * FROM q WHE
```

---

## Crash 277: `36260077f2165278` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249331`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b NUMERIC PRIMARY 
```

---

## Crash 278: `7cc9218d10d7475c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249918`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(_rowid_ INT); INSERT INTO p SELECT * FROM p NOT INDEXED GROUP
```

---

## Crash 279: `39302ed9dc848f48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250118`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN CHECK (TRUE), c3 TEXT UNIQUE); VALUES (FALSE, CURRENT_TIME) EXCEPT SELECT * FROM q WHERE TRUE ORDER BY CURRENT_TIME
```

---

## Crash 280: `4bd19b45d24886c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250269`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) NOT NULL, c3 TEXT UNIQUE); VALUES (FALSE, CURRENT_TIME) INTERSECT SELECT * FROM q WHERE FALSE ORDER BY CURRENT
```

---

## Crash 281: `643a172505fd1eeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255623`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); INSERT INTO p DEFAULT VALUES; ANALYZ
```

---

## Crash 282: `36b1d046f89fa708` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255643`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); INSERT INTO p DEFAULT VALUES; ANALYZ
```

---

## Crash 283: `403c081e2318329a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256706`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 FLOAT); INSERT INTO p SELECT ALL * FROM q NOT INDEXED; EXPLAIN 
```

---

## Crash 284: `34126e49cc4338fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258162`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRE
```

---

## Crash 285: `d3d071446620e1ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258230`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT GENERATED ALWAYS AS (count(*)) VIRTUAL); CREATE VIE
```

---

## Crash 286: `2196fbec592e88c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259125`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BLOB NOT N
```

---

## Crash 287: `8e4cb648e0033c70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259304`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid BLOB UNIQUE); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT 
```

---
