# Crash Triage Report

**Total crashes:** 230  
**Unique crash sites:** 230  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 230 | 230 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `34e76ed0dacbdf57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000224`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT t2.* FROM p NATURAL JOIN t3 WHERE +random() > CASE WHEN RAISE(IGNORE) ISNULL THEN c3 END << (RAISE(IGNORE)) == CURRENT_DATE COLLATE NOC
```

---

## Crash 2: `3a43c723985d792c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000248`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_, c1); EXPLAIN QUERY PLAN SELECT DISTINCT RAISE(IGNORE) < RAISE(IGNORE) * FALSE AS q_j_o0n__f_mch_37f5____4_c2766c8pwa__06__4j6492cp
```

---

## Crash 3: `02a2fd28659f5aff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000441`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; ANALYZE t1; CREATE TABLE IF NOT EXISTS p(c2 TEXT GENERATED ALWAYS AS (+CURRENT_DATE GLOB '' == (SELECT * ORDER BY
```

---

## Crash 4: `500efce66a3fc7c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000599`

```sql
SELECT printf('%.*e', -2147483649, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME & NOT EXISTS (SELECT * LIMIT (CURRENT_TIME), TRUE) IN
```

---

## Crash 5: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001253`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 6: `cfad8de5eecfe01d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001444`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, a); INSERT INTO r VALUES (FALSE + CURRENT_DATE / CURRENT_DATE NOT NULL COLLATE BINARY / NULL BETWEEN TRU
```

---

## Crash 7: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001713`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 8: `16dcd296f87127fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001740`

```sql
SELECT printf('%.*d', -2147483649, -1e308); SELECT printf('%.*e', 0, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE p (c2) AS (SELECT CURRENT_TIMESTAMP == CURRENT_TIME A
```

---

## Crash 9: `c12c7bf8e8fc88c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002345`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM q NATURAL JOIN p WHERE CASE CASE WHEN CASE CURRENT_TIME WHEN NOT NULL THEN TRUE < +FALSE LIKE
```

---

## Crash 10: `cbb4f3af23c14a24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003002`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 11: `cc0246e7dbfa819b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003819`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (TRUE)); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 12: `3d4d272c5e6a0f5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003854`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (a) VALUES (NOT CURR
```

---

## Crash 13: `21a1c5e7417bb5a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003942`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q (a) VALUES (NOT CURRENT
```

---

## Crash 14: `07032328031f8415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005619`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL, a FLOAT); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); SELECT * FROM r NATURAL
```

---

## Crash 15: `3011b34d975a47ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006759`

```sql
SELECT substr('O_p35', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); SELECT *, * FROM p NATURAL JOIN t2 WHERE last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 16: `5012ca228c9c0bb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006865`

```sql
SELECT printf('%d', 4294967295, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT *, * LIMIT CASE WHEN FALSE BETWEEN NULL AND CURRENT_DATE THEN FALSE != NOT TRUE END COLLATE BINARY
```

---

## Crash 17: `ace813d1c1de4b6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006883`

```sql
SELECT round(-1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); WITH RECURSIVE p (b, c2) AS NOT MATERIALIZED (SELECT total_changes()) SELECT * FROM r; CREATE TABLE IF NO
```

---

## Crash 18: `1e38a3ac4b3f9b75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006894`

```sql
SELECT substr(' _', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q VALUES (CURRENT_TIME); SELECT NOT FALSE AS s FROM s NATURAL JOIN t2 WHERE CASE random
```

---

## Crash 19: `5bd3e54f1d5bdce7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007087`

```sql
SELECT substr('_p -H_-P -8-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT_TIMESTAMP, CURRENT_DATE, * FROM q NATURAL JOIN s WHERE CASE CASE WHEN 
```

---

## Crash 20: `2356e212d94e79a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014591`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c1, c1, c1, c1, c1, c1, c1, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 21: `dfc958ae03af6db9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014677`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 22: `78dc349e80e75bcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015059`

```sql
SELECT round(-0.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (CURRENT_TIME | a, typeof(NULL) FILTER (WHERE TRUE) OVER () AND CURRENT_TIME -> CURRENT_T
```

---

## Crash 23: `4719d97411a0c9b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017901`

```sql
SELECT printf('%.*s', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (CURRENT_DATE);
```

---

## Crash 24: `4619f71152dd2662` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018262`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY, c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME) UNION ALL SELECT DISTINCT * FROM r NOT INDEXED NATURAL LEFT JOIN q ON FALSE WHE
```

---

## Crash 25: `aa70a65bbcb197e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018455`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 26: `1cd72e48ecf94527` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018555`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); CREATE TABL
```

---

## Crash 27: `dea578fe397893f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018974`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM q NATURAL JOIN p WHERE EXISTS (SELECT * FROM p NOT INDEXED JOIN (q NOT INDEXED) JOIN q NOT IN
```

---

## Crash 28: `ea051aa636f98572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019227`

```sql
SELECT substr('_', 2147483647, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 29: `4f984b30fbd3dc1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020565`

```sql
SELECT printf('%.*g', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 30: `10417e839a506e6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021908`

```sql
SELECT printf('%.*d', -9223372036854775808, -1e308); SELECT substr('-1h-_u_3_s- -', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3); INSERT OR FAIL INTO p VALUES (substr(CURRENT_D
```

---

## Crash 31: `6eb96b33c8f2aa70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022544`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; PRAGMA 
```

---

## Crash 32: `49d4a30f5ecffe13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022824`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zerob
```

---

## Crash 33: `85be8589e0bd32e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023302`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(b FLO
```

---

## Crash 34: `b64ea2736014e60e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023363`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO 
```

---

## Crash 35: `e051c8c0e86de8e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023572`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO 
```

---

## Crash 36: `06385773570e2bbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023778`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUE
```

---

## Crash 37: `21f4d8db13bc54b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023992`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (NULL)); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p 
```

---

## Crash 38: `e159d933dc55c708` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024207`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VA
```

---

## Crash 39: `fd0a71499fd2ffc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024408`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR ABORT INTO p VALUES (-CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p V
```

---

## Crash 40: `25519d4c6a217b4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024650`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; P
```

---

## Crash 41: `3366d4859445179f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024958`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-NULL); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 42: `0ab35fa0f2bc9314` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025642`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUES (CURRE
```

---

## Crash 43: `7178598fd88ef479` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025836`

```sql
SELECT printf('%.*e', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(2
```

---

## Crash 44: `7f702629a4c19dab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026358`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 45: `1abcb34a6496cb5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026537`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR 
```

---

## Crash 46: `89f4154dbbc844c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026642`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%x', 4294967296, 'ocI2 _kL__1--bP_b'); CREATE VIRTUA
```

---

## Crash 47: `c5b2f94730bc2aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027436`

```sql
SELECT substr('_', 4294967296, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(2147483648));
```

---

## Crash 48: `d0c4fbbf287207d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027930`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b GENERATED ALWAYS AS (a || b) NOT NULL); SELECT * FROM (SELECT CURRENT_TIME % CURRENT_DATE != CURRENT_TIMESTAMP COLLATE NOCASE AS zl12__95zayra99a_iy4l_ FROM p
```

---

## Crash 49: `1b471d1c01532ca7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031020`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 50: `f5883c394de49a49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031922`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURR
```

---

## Crash 51: `9ede1f77cc7f8003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032519`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME ASC NU
```

---

## Crash 52: `247b672f65043fe7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035763`

```sql
SELECT printf('%f', -9223372036854775808, 'Y 2'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(21
```

---

## Crash 53: `5654854e167f7db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036923`

```sql
SELECT round(0.01, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 54: `cc89588aee652416` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037082`

```sql
SELECT printf('%.*s', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob
```

---

## Crash 55: `a25f89c944f670ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043619`

```sql
SELECT substr('-Wt J_Z-c_g_2b_q', 2147483647, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CURRENT_TIME, CURRENT_TIMESTAMP, NULL) RETURNING NULL NOTNULL 
```

---

## Crash 56: `fd7e47702e51e27d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045283`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (TRUE BETWEEN FALSE AND TRUE) STORED, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE 
```

---

## Crash 57: `26df63c0704d5efa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045504`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (TRUE BETWEEN FALSE AND TRUE) STORED, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELE
```

---

## Crash 58: `2691c92f427dadc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045514`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (TRUE BETWEEN FALSE AND TRUE) STORED, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELE
```

---

## Crash 59: `035f4bb1ba583647` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045524`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (TRUE BETWEEN FALSE AND TRUE) STORED, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELE
```

---

## Crash 60: `5cf7612fe3d73ef4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045564`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIE
```

---

## Crash 61: `4818090a4e00aedf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047589`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO 
```

---

## Crash 62: `9027353fa387cf92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051067`

```sql
SELECT printf('%.*g', 9223372036854775807, 1e-308); SELECT substr(' AM- k _S_ ', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT DISTINCT FALSE IN (CURRENT_TIME), +CURREN
```

---

## Crash 63: `c1c8a3267a2ee6b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067729`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT DEFAULT X'2Fe2fd5F'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 64: `5a97cc30a18d4fb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067891`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE CURRENT_DATE) AS cjh__4
```

---

## Crash 65: `722e337fc104ade6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068319`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON FALS
```

---

## Crash 66: `ce42ad7e78fd0c7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069666`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURR
```

---

## Crash 67: `2971f475a50f5ab0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070726`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (CURRENT_TIMESTAMP)) AS a , p N
```

---

## Crash 68: `f63611550c8df1b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071251`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE, c2 FLOAT GENERATED ALWAYS AS (TRUE) STORED, b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN
```

---

## Crash 69: `7297ae5fe13a3449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071422`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME FROM p ORDER BY CURRENT_
```

---

## Crash 70: `0db4963c920e13d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071889`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME ASC NU
```

---

## Crash 71: `d926f36cab151e7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072882`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NOT NULL NOT IN (VA
```

---

## Crash 72: `36289fbab4b7902a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077760`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC GENERATED ALWAYS AS (NULL IS NOT TRUE) VIRTUAL, c2 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (NULL); SELECT p
```

---

## Crash 73: `a1fa2959e187a5c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078005`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); SELECT * FROM (SELECT TRUE <> TRUE % CURRENT_DATE AS zl12__95zayra99a_
```

---

## Crash 74: `446ea7f6f2e9c0a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078316`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b GENERATED ALWAYS AS (a || b) NOT NULL); SELECT count(*) FILTER (WHERE CURRENT_TIME) OVER () AS ik3 FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL T
```

---

## Crash 75: `9c8bff6e9968eb37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079087`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b GENERATED ALWAYS AS (a || b) NOT NULL); SELECT * FROM (SELECT FALSE COLLATE BINARY AS zl12__95zayra99a_iy4l_ FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE 
```

---

## Crash 76: `5e93c22716c8eea0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079711`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a) UNIQUE, c3 NUMERIC); SELECT * FROM (SELECT CURRENT_DATE AS zl12__95zayra99a_iy4l_ FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUA
```

---

## Crash 77: `59f2ed1387ccb975` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080921`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (count(*) FILTER (WHERE FALSE) OVER ()))); PRAGMA quick_
```

---

## Crash 78: `7e01eb8d462f76f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081168`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIME))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 79: `7eaaacb60e3d4f18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081391`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIME GLOB CURRENT_DATE OR CURRENT_TIMESTAMP); PRAGMA quick_ch
```

---

## Crash 80: `5f5a494f856961a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081596`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT -179802); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 81: `ad11053fe2b83f77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081773`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB, a TEXT NOT NULL DEFAULT X'5Dac1A8ABe2aCa'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 82: `2b4cf5e5f2889689` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081956`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 83: `dfa2715bdd9572b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082138`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 84: `780381967a5df4bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082289`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 85: `9c2be14d5ddefcaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082336`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 86: `5dd25db1b1370ea6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082355`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 87: `6b0d8b1d16f48e96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082583`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 88: `e453bcb79c251d26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082805`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT X'AbeC'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 89: `f9053b9e8cf19d2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083288`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (CURRENT_DATE OR CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR
```

---

## Crash 90: `c4847e2b7ccdc7a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083514`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT GENERATED ALWAYS AS (-TRUE) STORED, rowid VARCHAR(255) NOT NULL); INSERT OR ABORT INTO p VALUES (-FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 91: `d85f1d36403daa35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084168`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL DEFAULT 'U07m__6D6-_  '); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT IN
```

---

## Crash 92: `a7f7503fdf5c3ba0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084449`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL DEFAULT X'', c1 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p
```

---

## Crash 93: `990a34dde2b7363d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085622`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE);
```

---

## Crash 94: `39b19dc432960817` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085849`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL NO
```

---

## Crash 95: `e4bb0dd4a2b216bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086059`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0)); SELECT hex(zeroblob
```

---

## Crash 96: `5cc689d4da909a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086069`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; SELECT hex(zeroblob(0)); SELECT hex(zeroblob
```

---

## Crash 97: `bfae02d9cef0dbe4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (CURRENT_TIME % NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFA
```

---

## Crash 98: `f6a45cb98c9d28ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087095`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (CURRENT_TIME GLOB CURRENT_DATE OR CURRENT_TIMESTAMP)); INSERT OR ABORT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 99: `7838cdf246de8227` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087818`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL CHECK (rowid)); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUE
```

---

## Crash 100: `b895870792546485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088048`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 101: `e380e5858ac2b18f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088384`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE GLOB CURRENT_TIME IN (EXISTS (VALUES (FALSE)))); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 102: `ceedea9203d85477` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088916`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-NULL NOT IN (SELECT * FROM p NOT INDEXED GROUP BY FALSE) GLOB FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 103: `a7890b5cf5906df9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089158`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (X'd1dbEcfcB4a853'); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT 
```

---

## Crash 104: `8d9d558487e25abb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089314`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-X'd1dbEcfcB4a853'); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT
```

---

## Crash 105: `04a6c1b2230119b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089483`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO
```

---

## Crash 106: `325b992a02e42c1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089508`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE || NULL GLOB FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR
```

---

## Crash 107: `c0707dd09a6a3c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089718`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-5565358874242.3050889e-10); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT O
```

---

## Crash 108: `3d9e2fe5a5a5f31c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090053`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INS
```

---

## Crash 109: `0ea4c2ba955dcccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090084`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT FALSE, c1 NUMERIC NOT NULL); CREAT
```

---

## Crash 110: `7504042cccc30ffe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090172`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INT, c1 GENERATED ALWAYS AS (a = -2) NOT NULL UNIQUE); INSERT O
```

---

## Crash 111: `186cbdd127a3964e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090441`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); 
```

---

## Crash 112: `51070d3de04234c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090582`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE GLOB CURRENT_DATE GLOB FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 113: `42d73a587288bf54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090907`

```sql
SELECT printf('%.*d', -9223372036854775808, -1e308); SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (FALSE); PRAG
```

---

## Crash 114: `03baa3cf972680e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL CURRENT_TIMESTAMP AS a6_r_w FROM p ORDER BY CURRENT_TIMESTAMP ASC NULL
```

---

## Crash 115: `b0b32a6d438e3fa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092791`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b GENERATED ALWAYS AS (a) NOT NULL UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST LIMIT NULL; SELECT printf('%.*f', 214
```

---

## Crash 116: `8878d48804ca3551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092948`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST LIMIT 0; CREATE VIR
```

---

## Crash 117: `5230910a1775e414` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093175`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p NOT INDEXED LEFT OUTER JOIN q ON CURRENT_DATE ORDER BY CURREN
```

---

## Crash 118: `899b4c48999501bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST LIMIT TRUE BETWEEN 
```

---

## Crash 119: `f6b1d7c220075723` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094350`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a TEXT); SELECT * FROM q NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 120: `dba0dfdc649bee82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095124`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE); ANALYZE p; SELECT round(0.01, -9223372036854775808); CREATE VIRTUAL TA
```

---

## Crash 121: `32d1ee7c94a141ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104405`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 122: `74e285de4dc4adb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104424`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); SELECT * FROM p WHERE EXISTS (SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_DATE WINDOW w1 AS () LIMIT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 123: `a42cb9ff39224f3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107663`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL DEFAULT 700621.3e+2637); SELECT * FROM q GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 124: `238dd7e4f10740f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107805`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL DEFAULT NULL); SELECT * FROM q GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 125: `29f34d3f989c61c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107850`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO
```

---

## Crash 126: `87ad58e49131d81c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108519`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (FALSE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 127: `3e41e9fcdba5eec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108752`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 FLOAT GENERATED ALWAYS AS (-TRUE) STORED, rowid VARCHAR(255) NOT NULL); SELECT * FROM q GROUP BY CURRENT_TIME; CRE
```

---

## Crash 128: `98be20986bb85d45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108921`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM q GROUP BY NULL HAVING NULL COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 129: `00f5fbe2d81c00bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109062`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM q GROUP BY NULL HAVING CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 130: `00c1703b1a2048c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109077`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM q GROUP BY CURRENT_DATE COLLATE NOCASE HAVING NULL COLLATE NOCASE; CREATE VIRTUAL TABLE I
```

---

## Crash 131: `4f0397255f0c4bb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109923`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON NULL IS NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 132: `17a013504687c9f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110387`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON NULL IS NOT CURRENT_DATE; SELECT printf('%.*g', 214748
```

---

## Crash 133: `04e392a2e2aaa113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111831`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT CURRENT_TIME ORDER BY FALSE DESC NULLS LAST LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 134: `8fb135fd4521356d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112026`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT *, * FROM q GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR AB
```

---

## Crash 135: `4bfefff28e869f09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114775`

```sql
SELECT printf('%.*f', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO r VALUES (FALSE ISNULL); ANALYZE p; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 136: `fc09415f4f0483fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115138`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c1 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT I
```

---

## Crash 137: `0fd0499fcc333856` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115270`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 138: `a77ed30756595d54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118453`

```sql
SELECT substr('p-V  5T-- ', -2147483648, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CURRENT_TIMESTAMP GLOB CURRENT_DATE, FALSE, (CURRENT_DATE
```

---

## Crash 139: `e0b178e8774e21b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119859`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (TRUE | TRUE); EXPLAIN QUERY PLAN VALUES (CURREN
```

---

## Crash 140: `58fdd2d93741e0ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120007`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (TRUE | TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CRE
```

---

## Crash 141: `5f5d219f2b119282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120013`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (TRUE | TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREA
```

---

## Crash 142: `1b8369e7a35cd705` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126283`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON NULL IS NOT FALSE; SELECT printf('%.*f', 2147483647, -
```

---

## Crash 143: `46a48576e05809fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127032`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid FLOAT); SELECT * FROM p NOT INDEXED WHERE NULL NOT IN (SELECT ALL * FROM p ORDER BY TRUE ASC NULLS LAST) GROUP 
```

---

## Crash 144: `fc8ac9525c2b6783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140249`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST LIMIT 55553; CREATE
```

---

## Crash 145: `db6fe77d8ea66ef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141025`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a FLOAT UNIQUE); EXPLAIN QUERY PLAN SELECT ALL * FROM (VALUES (CURRENT_TIMESTAMP)) AS a , p NATURAL JOIN p ORDER BY C
```

---

## Crash 146: `2163924d7b465ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142889`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CAST(TRUE AS TEXT)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT
```

---

## Crash 147: `f6b50ecefcc64752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143403`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNIO
```

---

## Crash 148: `5adaaed55defc3d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143480`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT INTO p 
```

---

## Crash 149: `08a7afea1e334de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143908`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INTEGER GENERATED ALWAYS AS (FALSE LIKE TRUE ESCAPE RAISE(IGNOR
```

---

## Crash 150: `8cb5a27d958ca6a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143955`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) CHECK (CURRENT_DATE)); INSERT INTO p DEFAULT VALUE
```

---

## Crash 151: `6b97ec1ffa4ba685` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143962`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER); INSE
```

---

## Crash 152: `d792073347c04a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144099`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT 700621.3e+2637); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR A
```

---

## Crash 153: `21a05e60efae364f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144271`

```sql
SELECT printf('%.*g', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO t3 VALUES (CAST(CURRENT_TIME IS NULL + CURRENT_TIME NOTNULL COLLATE BINARY AS VARCHAR(255)) >
```

---

## Crash 154: `4fc03c0c4ffc0251` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144400`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE || FALSE || TRUE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 155: `9ad105d06de69cae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144538`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE || FALSE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE
```

---

## Crash 156: `c989f129c6bd61d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144745`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 157: `cfac946f8278ed82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144999`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-'- 4-A- - ji_08dr-'); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 158: `0079076fe961274b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145557`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (EXISTS (VALUES (FALSE))); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INT
```

---

## Crash 159: `c23b0036a0b22ead` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149833`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 160: `f390b82ca29c98b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149959`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 161: `51e152695d67940b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149973`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), c1 GENERATED ALWAYS AS (a + -715) NOT NULL); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 162: `f9319f802400eae1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150376`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE >> CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT 
```

---

## Crash 163: `7cbc03609514eb9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150720`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CAST(TRUE AS VARCHAR(255))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT IN
```

---

## Crash 164: `2c4f79c65afda17d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151229`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (~CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES 
```

---

## Crash 165: `1112806229f671ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153211`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT X'AbeC'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQU
```

---

## Crash 166: `80ed9505d4252bd5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153687`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY, b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 167: `947307a03dbbd8d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155025`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_DATE IN (SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME ASC NULLS LAST LIMIT TRUE)); 
```

---

## Crash 168: `65afe6674f1b3726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155134`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT DISTINCT count(*) AS wa49_2j_9_1y_o263___s3_i1p8_a__0995
```

---

## Crash 169: `5a6af979cb6ff650` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155276`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE VIRTUAL 
```

---

## Crash 170: `0d464aecb64f2c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155283`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (SELECT DISTINCT TRUE AS wa49_2j_9_1y_o263___s3_i1p8_a__09958i1_
```

---

## Crash 171: `2f2145b82d143998` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155313`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 172: `156e7f2a6de9993a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155531`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIMESTAMP NOT IN (VALUES (count(*) FILTER (WHERE FALSE) OVER (ORDER BY TRUE DESC 
```

---

## Crash 173: `26c103788de583ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157174`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a) UNIQUE, c3 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABOR
```

---

## Crash 174: `1310eabd1bd89e84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157288`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c2 GENERATED ALWAYS AS (a) UNIQUE, c3 NUMERIC); SELECT *, * FROM (SELECT CURRENT_DATE AS zl12__95zayra99a_iy4l_ FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIR
```

---

## Crash 175: `e4c56200dbcb67a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158141`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b GENERATED ALWAYS AS (a || b) NOT NULL UNIQUE); SELECT * FROM (SELECT NOT EXISTS (SELECT DISTINCT * FROM p ORDER BY CURRENT_TIME ASC NULLS LAST LIMIT CURRENT_D
```

---

## Crash 176: `005a542924ad83bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158498`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, b GENERATED ALWAYS AS (a || b) UNIQUE); SELECT * FROM (SELECT count(*) AS zl12__95zayra99a_iy4l_ FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 177: `33cabeead1618491` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159150`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL DEFAULT X'a4FEbEC39647'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 178: `6f2d7d65716da6f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159855`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN DEFAULT ' _-Q---_3 - 0bau'); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY TRUE DESC NULLS LAST, CURRENT_TIME DESC NULLS FIRST; INSERT INTO p DEFAULT VALUES;
```

---

## Crash 179: `4e7790563ca616b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160448`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL, c1 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, 
```

---

## Crash 180: `b31726887cf1de6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160587`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL, c1 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 181: `bfefa78590e54292` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160640`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL, c1 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM (SELECT *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, *, 
```

---

## Crash 182: `556cce838ae72e39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162349`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT FALSE IS NULL + TRUE IS NOT NULL + TRUE * FALSE AS o FROM (SELECT * FROM p WHERE NULL) AS sub1; C
```

---

## Crash 183: `ffcc75a4f794a5c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT FALSE + FALSE <= FALSE * CURRENT_TIMESTAMP COLLATE NOCASE AS o FROM (SELECT * FROM p WHERE NULL) 
```

---

## Crash 184: `ae4f89aaffd9303f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162768`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT TRUE + FALSE <= NULL AS o FROM (SELECT count(*) OVER () AS a6_r_w, * FROM p WHERE NULL) AS sub1; 
```

---

## Crash 185: `38408f3dedb5078a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166194`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP 
```

---

## Crash 186: `3a3f6305d616ecd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166829`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (TRUE = CURRENT_TIMESTAMP IS NO
```

---

## Crash 187: `ab14211174aeeed3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169342`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL LIKE (SELECT * FROM q NOT INDEXED WHERE 
```

---

## Crash 188: `7dee56e93b32bafa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169525`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL LIKE NULL ESCAPE count(*) OVER ()); CREA
```

---

## Crash 189: `33dfe13a6a4a0175` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169954`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY c1 W
```

---

## Crash 190: `d0ae51d27388458c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171601`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE total_changes() GRO
```

---

## Crash 191: `7950aba2acd5b0e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171804`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE upper(NULL) GROUP B
```

---

## Crash 192: `dece8b6e07f07627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171947`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT count(*) FILTER (WHERE CURRENT_DATE) AS cjh__4
```

---

## Crash 193: `972d4f826ce1bb1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176602`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); WITH RECURSIVE p AS (VALUES (CURRENT_DATE)) SELECT * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 194: `ec24121a675c152e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201472`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (NULL IS NOT FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO s VALUES (
```

---

## Crash 195: `064ed4a4b8d083ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201802`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (FALSE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 196: `3d7c608a89dc2a28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202057`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (TRUE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 197: `5fed175de5995ce3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202295`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA q
```

---

## Crash 198: `62c9083b391ee228` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202430`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREA
```

---

## Crash 199: `cb4099aece3d2987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202670`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (NULL != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p 
```

---

## Crash 200: `a6399df3d4a4603d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202840`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_TIME != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 201: `e3536760fa4d6c36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205833`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT * FROM p NOT INDEXED WHER
```

---

## Crash 202: `4f642f03ce0cce70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205992`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p NOT INDEXED WHERE FA
```

---

## Crash 203: `bfa4eaa61c070473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206636`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b NUMERIC PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM p NOT INDEXED WHER
```

---

## Crash 204: `b1a912440755391b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207615`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (TRUE) STORED, c1 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE 
```

---

## Crash 205: `d59105e48c2c78ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207864`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 206: `8ea7124773622537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208683`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB GENERATED ALWAYS AS (NULL BETWEEN FALSE AND TRUE) STORED, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 207: `f8a5be91b62d5c48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210208`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE VIE
```

---

## Crash 208: `4e2b657c1e61bb6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211437`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (CU
```

---

## Crash 209: `f252159efb6b9f0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211603`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT UNIQUE); WITH r (c1, b) AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p AS i_ GROUP BY NULL EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 210: `180607cd68a3db92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212051`

```sql
SELECT substr('hq-H', 4294967295, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); INSERT OR FAIL INTO t1 VALUES (+-CURRENT_DATE IS DISTINCT FROM FALSE * +RAISE(IGNORE) N
```

---

## Crash 211: `addf5b0fae4e9924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219568`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (TRUE != CAST(TRUE AS TEXT) != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE != CURRENT_DATE)); INSERT INTO p DEFAULT VA
```

---

## Crash 212: `187a1c7a1924a9f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219771`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CAST(CURRENT_TIME AS INT) != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 213: `4ff2f187d5b1bbf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219942`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_TIME COLLATE RTRIM != CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 214: `85e6d42fd40ca7ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247984`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON FALS
```

---

## Crash 215: `92017a329f60fe46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248115`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON FALS
```

---

## Crash 216: `49dfa24c95d3a5af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY _row
```

---

## Crash 217: `e6930c39ef3a1932` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250282`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM p ORDER BY CURRENT_T
```

---

## Crash 218: `2f518e3cfc21daad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250401`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (TRUE)) AS ns__13y6_ GROUP BY N
```

---

## Crash 219: `0841aad2f574f2d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252432`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT '-'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 220: `eeca1d02d565aa49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252611`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 221: `e0637326e78dc334` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252655`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM (VALUES (TRUE, CURRENT_TIMESTAMP, TRUE,
```

---

## Crash 222: `ef1d539a381437e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253952`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL NOT IN (SELECT
```

---

## Crash 223: `7fb2dfd2b3ce0f1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT _rowid_ AS a6_r_w FROM (SELECT min(CURRENT_DATE) AS a6_r_w, * FROM p WHERE NULL) AS sub1; CREATE 
```

---

## Crash 224: `6341212d83fc6903` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262364`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CR
```

---

## Crash 225: `01617a0a25e8aae9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262603`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF
```

---

## Crash 226: `330d45c80e886bff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262615`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF
```

---

## Crash 227: `afebf052673b078c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262670`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF
```

---

## Crash 228: `788e01f6ebf3bdf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262888`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CR
```

---

## Crash 229: `84fb831e56334ad8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262894`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CR
```

---

## Crash 230: `5143108506ef6623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263839`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE); PRAGMA
```

---
