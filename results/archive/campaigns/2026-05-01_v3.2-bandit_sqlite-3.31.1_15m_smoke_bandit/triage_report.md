# Crash Triage Report

**Total crashes:** 174  
**Unique crash sites:** 174  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 174 | 174 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `2acb175e427689c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000278`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (CASE CASE ~~CURRENT_TIMESTAMP WHEN CURRENT_TIME IS NOT NULL THEN CURRENT_TIME IS NULL ELSE NULL IS RAISE(IGNOR
```

---

## Crash 2: `e3c3566adbd3ddba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000337`

```sql
SELECT printf('%.*g', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT TRUE COLLATE BINARY % RAISE(IGNORE) <= NULL AS a FROM q NATURAL JOIN p WHERE (+FALSE << RAISE(IGNORE
```

---

## Crash 3: `709364d70c75bde7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000443`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, a, c2); INSERT INTO p VALUES (upper(CASE WHEN RAISE(IGNORE) THEN RAISE(IGNORE) + TRUE = TRUE GLOB FALSE MATCH RAISE(IGNORE) ELSE rowid IS N
```

---

## Crash 4: `10fe567e94017be0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000460`

```sql
SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p (c1) VALUES (TRUE, CURRENT_DATE NOT NULL) ON CONFLICT(c3) DO UPDATE SET c2 = NOT TRUE != RAI
```

---

## Crash 5: `ae6ac590558bdfb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000474`

```sql
SELECT printf('%.*g', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); SELECT q.* FROM q NATURAL JOIN p WHERE NOT EXISTS (WITH q (rowid) AS (SELECT RAISE(IGNORE) & CURRENT_DA
```

---

## Crash 6: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000544`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 7: `0d8914b7a8cac878` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000608`

```sql
SELECT printf('%lld', -2147483648, '_--_6'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT OR ROLLBACK INTO t2 VALUES (+CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME, -C
```

---

## Crash 8: `533adaa9acdba862` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000857`

```sql
SELECT round(0.01, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (CASE NOT CAST(+RAISE(IGNORE) AS BOOLEAN) > CAST(CASE WHEN RAISE(IGNORE) THEN NULL ELSE TRUE END 
```

---

## Crash 9: `910ed16ad2f0a10b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001096`

```sql
SELECT printf('%u', 2147483648, ' -- 2  -42'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT s.* INTERSECT SELECT * ORDER BY -CURRENT_DATE || t3.c3, FALSE COLLATE RTRIM << CURRENT_D
```

---

## Crash 10: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001477`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 11: `e2768d9930eed6f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002957`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP AND NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE 
```

---

## Crash 12: `3aa3489223f90a40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002972`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CAST(TRUE AS TEXT) AS n7__w_u_543v__495_9yp_109_6_o02__5_7a_56mx6_p5tqr_7y50______7n2n3162446___37_9
```

---

## Crash 13: `3dec0464eccc1722` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002979`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 14: `0e8a94bab0978f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 15: `f8a877ad8c560a0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004152`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INT
```

---

## Crash 16: `faadd6bbbd1d5375` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004862`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES ((CURRENT_TIME)) UNION VALUES (NULL, CURRENT_TIMESTAMP COLLATE RTRIM) UNION SELECT DISTINCT * FROM p ORDER BY ~
```

---

## Crash 17: `ae7ff69aa4c741ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004909`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES ((CURRENT_TIME)) UNION VALUES (NULL, CURRENT_TIMESTAMP COLLATE RTRIM) UNION SELECT DISTINCT 
```

---

## Crash 18: `f3e2d83d5017e56f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005028`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); WITH t2 AS (SELECT *) INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES ((CURRENT_TIME
```

---

## Crash 19: `094e3361c5ec6ade` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005316`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; VALUES (C
```

---

## Crash 20: `e23ff3187ad0177e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006546`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT r.*; CREATE TABLE IF NOT EXISTS p(rowid BLOB CHECK (trim(TRUE) FILTER (WHERE RAISE(IGNORE))),
```

---

## Crash 21: `baa24cd0aad8f82b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006582`

```sql
SELECT substr('jW_b', 2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO q VALUES (NOT EXISTS (SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP 
```

---

## Crash 22: `4dd12ed102ec7e20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007108`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 DEFAULT VALUES; SELECT DISTINCT 
```

---

## Crash 23: `4bfc76341e1b7a80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007886`

```sql
SELECT printf('%.*d', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q AS MATERIALIZED (VALUES (FALSE ISNULL, FALSE)) SELECT NOT CURRENT_TIME, * FROM p; SELECT he
```

---

## Crash 24: `9f1ce2ba107b4be7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008035`

```sql
SELECT substr('_ 5P6N-', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, c2, c1, c2, c3); SELECT (CURRENT_TIME) ->> CURRENT_TIMESTAMP IS NOT
```

---

## Crash 25: `4dfe45f4b37476aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008279`

```sql
SELECT substr('VKL _r7m_ yE-T_7', -9223372036854775808, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO q VALUES (+NOT ~hex(FALSE COLLATE NOCASE) MATCH CURRENT_
```

---

## Crash 26: `25d4f9740a98b1b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008374`

```sql
SELECT substr('YI-JH', -1, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, a); INSERT OR ROLLBACK INTO p VALUES (NULL / (CURRENT_TIMESTAMP) ->> CURRENT_DATE, json_extrac
```

---

## Crash 27: `bfb79af3bcb923a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008395`

```sql
SELECT printf('%.*s', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p (c1) VALUES ((RAISE(IGNORE)) IS NOT DISTINCT FROM CURRENT_TIMESTAMP, lower(zeroblob(3667
```

---

## Crash 28: `21ad60ed5b35584a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008702`

```sql
SELECT printf('%.*f', 9223372036854775807, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT substr(TRUE, TRUE || FALSE) FILTER (WHERE RAISE(IGNORE) COLLATE RTRIM IS NULL) FROM r J
```

---

## Crash 29: `37040bd1b67937ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010300`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 30: `f80c920ec995ea98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011165`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, c3 BLOB NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT count(DISTINCT NULL) <> NULL FROM p NATURAL 
```

---

## Crash 31: `f0fc9dc57d8b16a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012317`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, c1 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 32: `81bf1f5bb113c0e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013786`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, c1 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 33: `d7beda4f7b35af7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014087`

```sql
SELECT printf('%.*f', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(9223372036854775807)); CREATE TABLE IF NOT EXI
```

---

## Crash 34: `6663b80d0054330a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015526`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (CURRENT_TIME NOT BETWEEN TRUE AND TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT
```

---

## Crash 35: `1fa828401afb91c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019826`

```sql
SELECT substr('7_p_ b -9_L W3', 1, 9223372036854775807); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 36: `30d52e45d0912b15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020016`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (NULL), c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 37: `87795de9d1368707` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020654`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (EXISTS (SELECT TRUE ORDER BY CURRENT_DATE DESC NULLS LAST, RAISE(IGNORE)) < CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check
```

---

## Crash 38: `f49addc693e00a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020689`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (EXISTS (SELECT TRUE ORDER BY CURRENT_DATE DESC NULLS LAST, RAISE(IGNORE)) < CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check
```

---

## Crash 39: `1170885a64e2d21b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021220`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE NULL IS NOT NULL >= CURRENT_DATE WHEN NULL AND CURRENT_DATE THEN C
```

---

## Crash 40: `0a6069e974cd8374` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021773`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE CURRENT_TIME >= CURRENT_DATE WHEN NULL AND CURRENT_DATE THEN CAST(
```

---

## Crash 41: `0aae8cb0cf74060a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021779`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE NULL IS NOT NULL >= CURRENT_DATE WHEN CURRENT_TIMESTAMP THEN CAST(
```

---

## Crash 42: `6e67704cfc9c0608` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021915`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE FALSE IS NOT NULL >= FALSE WHEN CURRENT_DATE THEN CAST(CURRENT_DAT
```

---

## Crash 43: `d73c4a4e5927bd41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022030`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE CURRENT_DATE WHEN CURRENT_DATE THEN CAST(CURRENT_DATE AS BLOB) ELS
```

---

## Crash 44: `5c21fae35710a0fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022036`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CASE CURRENT_DATE WHEN CURRENT_DATE THEN FALSE ELSE CURRENT_DATE END) O
```

---

## Crash 45: `6e6e4a2e2cd9f070` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025238`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (TRUE OR CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 46: `8124d8ba85b56078` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025320`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c
```

---

## Crash 47: `6fdb625f2733298c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025771`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (CURRENT_DATE AND FALSE OR CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 48: `4fe301bc717334d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025852`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 49: `76e739d076952d8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025858`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (CURRENT_DATE AND NULL)); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 50: `1257c80c02875a5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026548`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT * FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); 
```

---

## Crash 51: `70328b34faf7bf45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026922`

```sql
SELECT printf('%.*e', 4294967296, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r (c3) VALUES (+-t2.c1 < CAST(RAISE(IGNORE) IS NULL IN (TRUE, RAISE(IGNORE), TRUE) AS VAR
```

---

## Crash 52: `a94d7f03c444c4af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027176`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT -73.322821331360728382142989769121299841327625655527789705728765717210058503330882
```

---

## Crash 53: `5f0ff68c061ce083` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027263`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE >> FALSE, NULL); CREATE VIRTUA
```

---

## Crash 54: `8d0ebafe194a6985` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027717`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); SELECT (SELECT * LIMIT TRUE) IN (CURRENT_DATE NOT BETWEEN CURRENT_TIME AND RAISE(IGNORE) NOT NULL, CURRENT
```

---

## Crash 55: `292465f8b29e237c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027842`

```sql
SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 VALUES (NULL IS NOT DISTINCT FROM CURRENT_DATE COLLATE BINARY LIKE total_cha
```

---

## Crash 56: `aae17ec83fc6fb22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027974`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); INSERT OR IGNORE INTO q VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 57: `4b5683ae82252c06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032576`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (TRUE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); INSERT INTO t1 VALUES (json(NOT RAISE(IGNO
```

---

## Crash 58: `ef488acb742cb838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038908`

```sql
SELECT round(-1e308, 2147483647); CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (SELECT *) SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABL
```

---

## Crash 59: `4910b6b6906c690a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039432`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP;
```

---

## Crash 60: `73a61bef23bb614c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042796`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 61: `6c541fa35503dedf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042836`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 62: `791febc8de2b227c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043533`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (CURRENT_TIME / CURRENT_TIMESTAMP IS NOT TRUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIR
```

---

## Crash 63: `4f8908c2dee39dc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043624`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (TRUE IS NOT TRUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 64: `dc041b9a0ba9460e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045546`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); I
```

---

## Crash 65: `0dd329b3907520ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045619`

```sql
SELECT printf('%.*e', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE t3 (a, _rowid_) AS (SELECT p.* FROM p NOT INDEXED LEFT OUTER JOIN p ORDER BY randomblob(CURRENT
```

---

## Crash 66: `10e42cdac4808642` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045684`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CASE WHEN CURRENT_TIMESTAMP IS NOT NULL THEN CURRENT_DATE ELSE F
```

---

## Crash 67: `1e6bb801da174edf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045965`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NOT NULL; SELECT printf('%.*g', 2147483647,
```

---

## Crash 68: `32bfe94016311c1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046213`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); 
```

---

## Crash 69: `24f344ef49d562d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046975`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL || NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); SELECT *, (SE
```

---

## Crash 70: `9aa3d559d14d5afb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047369`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL IS NOT CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 71: `555ac7e4f9f59f7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048263`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBAC
```

---

## Crash 72: `e9cfac9775bd63ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049092`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL || FALSE IS NOT NULL); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 73: `f71e808e87dbbe0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049351`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NOT NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c1, c1, c2); INSERT OR
```

---

## Crash 74: `8a250416959b30af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049562`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NOT FALSE LIKE FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, b); WITH 
```

---

## Crash 75: `bd6579e546080efb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049745`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE || FALSE LIKE CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); 
```

---

## Crash 76: `7171c85ced5d118f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049828`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM q GROUP BY TRUE, RAISE(IGNORE) ORDER BY coalesce(CURRENT_TIMESTAMP, NULL) D
```

---

## Crash 77: `7f059d6dd23e55c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049838`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE || CURRENT_DATE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF N
```

---

## Crash 78: `7b79408b3413ce98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049950`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP != CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 79: `7ead91576a4e77c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050117`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE || TRUE IS NOT NULL != CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 80: `96b499cbd7e9a359` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051604`

```sql
SELECT printf('%.*d', -2147483649, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); INSERT OR ROLLBACK INTO q VALUES (-~CASE WHEN RAISE(IGNORE) LIKE TRUE ESCAPE RAISE(IGNORE) || 
```

---

## Crash 81: `c8476b16bc708e4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052118`

```sql
SELECT printf('%.*s', 4294967295, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO q VALUES (count(CURRENT_DATE NOT NULL > CURRENT_TIME) FILTER (WHERE CURRENT_TI
```

---

## Crash 82: `cb28d8cd8fbfe2ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052764`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP, * FROM p WHERE FALSE) AS sub1; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 83: `914aab8ae08e9be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054799`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT -0); WITH RECURSIVE q AS (SELECT *) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO p VALUES (TRUE =
```

---

## Crash 84: `80d433ad4ea6e2de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055293`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE != NOT CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT O
```

---

## Crash 85: `a05d0a6f79d05b8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057241`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE IN (TRUE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); WITH RECURSIVE
```

---

## Crash 86: `bd6e481135c41315` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057429`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE << CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b);
```

---

## Crash 87: `0b7c429c2e030bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057485`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE << CURRENT_TIME); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 88: `58bcd3b37fcd0b76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058334`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT X'aFDcf2'); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 89: `6c57a7e8423c304f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058416`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR
```

---

## Crash 90: `cd68cfa44aa12de9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058422`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT X'aFDcf2'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INT
```

---

## Crash 91: `11e24b20dd25676a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058547`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL IS NOT TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FA
```

---

## Crash 92: `c0beda0b7a3cd285` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062931`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); SELECT max(CURRENT_DATE) OVER (ORDER BY NULL ASC, FALSE ASC) FROM p NATU
```

---

## Crash 93: `0261701fb58247d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063360`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE NULL IS NOT NULL >
```

---

## Crash 94: `dced1c9705857b68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063572`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE >= CU
```

---

## Crash 95: `56b3d8ef39e517ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT changes() FROM p NATURAL JOIN p WHERE CURRENT_DA
```

---

## Crash 96: `c37b93c7ebd7107a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064555`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 97: `f62928db98d67745` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (31385198.8232232342950500418255326312922251878097506841107369609381498663776788151
```

---

## Crash 98: `401817705c0f9e53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065568`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); SELECT CURRENT_TIMESTAMP % FALSE AS b6_n__m_bd9___f_tu9
```

---

## Crash 99: `c8312866ebb221ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066879`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (X'') ON CONFLICT DO NOTHING; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 100: `de2b50eb76479623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068685`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 101: `72c4bbd996d8887f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068920`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); SELECT * FROM p ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM ASC NULLS FIRST, TRUE ASC; SELECT printf('%.*g', 2
```

---

## Crash 102: `0b9408b60d88033a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070941`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (NULL)); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT substr('O8G__-8_- 5i _-e ', 2147483647, 0); CREATE VIRTUAL TABLE IF 
```

---

## Crash 103: `9a66c9f4d55a2f07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070994`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER NOT NULL); REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT substr('O8G__-8_- 5i _-e ', 2147483647, 0); CREATE VIRTUAL TABLE IF N
```

---

## Crash 104: `13d8c916f1316431` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT X'aed80a90'); INSERT OR ABORT INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 105: `17107de545eaf22f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082028`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); WITH RECURSIVE t1 AS (SELECT *) INSERT INTO p VALUES ((VALUES (FALSE) UNION VALUES (FALSE))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 106: `1be0e18a5c7bbc4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086322`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c2 GENERATED ALWAYS AS (a IS NULL) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); IN
```

---

## Crash 107: `e3e2b78e140f2c1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086810`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p WHERE CURRENT_DATE GROUP BY 
```

---

## Crash 108: `f1463033bbaf9e44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087057`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT ' 0-'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL T
```

---

## Crash 109: `bae4d43b6ff26127` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087245`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VI
```

---

## Crash 110: `4264f5f5718028d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087384`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT 'd27  9k 1'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIR
```

---

## Crash 111: `d48233ce2f916bc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087467`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL T
```

---

## Crash 112: `f864a4406fdc9704` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087683`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a + 2) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT -0336318626924151223148694511227026918.3152022409841028E+1); INSERT INTO p DEFAULT
```

---

## Crash 113: `0d933b8fe03068f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089022`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, _rowid_ GENERATED ALWAYS AS (a = 0) NOT NULL UNIQUE, a INTEGER NOT NULL DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL T
```

---

## Crash 114: `8680c6b34cc307af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (count(*), FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT IN
```

---

## Crash 115: `8a97b9968a2fae64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090945`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (FALSE <= last_insert_rowid())); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 116: `086a10e5006b70ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092815`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL CHECK (CURRENT_DATE AND TRUE)); CREATE TABLE IF NOT EXISTS q(c1 INT); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 117: `9921c7ebaac667be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095745`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) EXCEPT SELECT * FROM p GROUP BY TRUE, RAISE(IGNORE); INSERT INTO p DEFAULT VALUES; PRAGMA qu
```

---

## Crash 118: `4c6f4f42478f4a8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098005`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CURRENT_DATE IS NOT NULL AS l, total_changes() FILTER (WHERE NULL) OVER () IS NOT ++NULL GLOB 
```

---

## Crash 119: `37b7427dcbc3ff54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100208`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (-26.1593422683496694910330691123E+8544042982625410059471827140920111776
```

---

## Crash 120: `b9620ab7f747328c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100497`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CAST(CURRENT_DATE AS TEXT)) ON CONFLICT DO NOTHING; PRAGMA quick_check;
```

---

## Crash 121: `1f898a650ee36e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100705`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 122: `f021d18637dc5cc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100864`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUA
```

---

## Crash 123: `f38c0ea33845f5e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100887`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CAST(CURRENT_DATE AS INT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; 
```

---

## Crash 124: `f4a04d77856e2206` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101331`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b BLOB PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP COLLATE RTRIM) ON CONFLICT DO NO
```

---

## Crash 125: `22a1ec57f1b83c23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103308`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (TRUE OR CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 126: `487443af10216adf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103660`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (-26.1593422683496694910330691123E+8544042982625410059471827140920111776 < CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; 
```

---

## Crash 127: `3d1b9789bf742303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103942`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (EXISTS (SELECT TRUE ORDER BY EXISTS (SELECT TRUE ORDER BY NULL ASC NULLS LAST) DESC NULLS LAST, RAISE(IGNORE))) ON CONFLICT DO NOTHI
```

---

## Crash 128: `4cf295db5f072975` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104037`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p VALUES (CURRENT_DATE COLLATE NOCASE < CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 129: `e64c0d45ea8b94b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104708`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB CHECK (NOT CURRENT_DATE IN (CURRENT_TIME)), c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE 
```

---

## Crash 130: `b7fb12a3c23038c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105020`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 131: `55cd34ed1a59a3b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105669`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL DEFAULT X'DdeDeb34', c2 FLOAT); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 
```

---

## Crash 132: `8fd2511fdd2d2cf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106124`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL DEFAULT 0); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 133: `d78f46ee55f4aac8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108217`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 134: `8fa675ffd9e3ce2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108351`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 VARCHAR(255)); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 135: `e198f5ec09990acf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109339`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (NULL IS NOT CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR A
```

---

## Crash 136: `b7b7ba6f9cf600dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109491`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p 
```

---

## Crash 137: `2589ec5b4d5baf23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109539`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (NULL IS NOT TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO p 
```

---

## Crash 138: `7a329268f6dfd2a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109652`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (NULL IS NOT TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('_5Ipr ', 0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 139: `921386116c71dd12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110720`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) DEFAULT -343999422903615399674847910248424197190741493.3717017507718379613416986349869358197373133760464058725747870652443145500630408470731266007537186
```

---

## Crash 140: `d7ddba98972f0ab0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111056`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER GENERATED ALWAYS AS (FALSE) STORED, c2 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 141: `1f67f476e51ccd49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111379`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (FALSE NOT NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 142: `b286752f30b5af8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (total_changes() NOT BETWEEN TRUE AND TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WIT
```

---

## Crash 143: `6ecfd40e39c957ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112576`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (hex(CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p (rowid) VALU
```

---

## Crash 144: `ef39b50de52319f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113507`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE, c1 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(b VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 145: `626b370effdccc40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115901`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, c1 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 146: `4a2a9b0835b07cf2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117071`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT count(DISTINCT NULL) <> NULL LIKE TRUE FROM p NATURAL JOIN p WHERE FALSE - NULL; CREATE VIRTUAL T
```

---

## Crash 147: `b136bb1676f8d0ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117364`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT count(DISTINCT NULL) <> (VALUES (NULL)) FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF
```

---

## Crash 148: `310166843d0cf067` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117650`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT NULL LIKE NULL FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 149: `a75f7ba9d7d819a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117772`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT count(*) OVER () FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 150: `0244d86bfa0dd63e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117956`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT max(CURRENT_DATE) OVER (ORDER BY NULL ASC, FALSE ASC) IS CURRENT_DATE FROM p NATURAL JOIN p WHERE
```

---

## Crash 151: `16f7278e67fa7172` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120945`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT total_changes() LIKE count(*) FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 152: `27ddd453efaf313a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121125`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT NULL + CURRENT_TIMESTAMP <> NULL FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*g', 214
```

---

## Crash 153: `d4bb6db0ac0804c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122814`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME OR CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 154: `2ebb53921504b7a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123632`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 155: `647b29c39e2b064b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124253`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT json_extract(c3, '') FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 156: `96dcf0f4e1c88bd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124662`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL DEFAULT 0.0); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 157: `0d8cf76b6e1e779f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125304`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE +TRUE; SELECT printf('%x', 9223372036854775807, ''); CREATE V
```

---

## Crash 158: `cc0b0ba89f4a3c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125903`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); SELECT * FROM p NATURAL JOIN p WHERE NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 159: `a09c49bd625bdeb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126170`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, b FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 160: `5f787f23cdbe96c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126963`

```sql
SELECT round(1e-308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c1); EXPLAIN QUERY PLAN SELECT NOT EXISTS (SELECT * LIMIT EXISTS (WITH RECURSIVE r AS MATERIALIZED (SELEC
```

---

## Crash 161: `da7b370e4e266edb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127849`

```sql
SELECT round(1e308, 9223372036854775807); SELECT printf('%.*f', -2147483649, -1e308); SELECT substr('--', 9223372036854775807);
```

---

## Crash 162: `8acd2c760674fee0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131217`

```sql
SELECT printf('%.*e', -1); SELECT printf('%.*e', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, a); SELECT TRUE NOT BETWEEN quote(CURRENT_DATE * CURRENT_TIME << CURRE
```

---

## Crash 163: `23bc6e6057034bcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131515`

```sql
SELECT printf('%.*d', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (rowid) VALUES (group_concat(FALSE >= RAISE(IGNORE) COLLATE BINARY, '_- cGy_ 9-- 0_-  U7') FIL
```

---

## Crash 164: `407dc7ecf8eda28c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136985`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT count(DISTINCT NULL) <> count(DISTINCT NULL) FROM p NATURAL JOIN p WHERE NULL; CREATE VI
```

---

## Crash 165: `22e61fff17175ef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137050`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT random() <> count(DISTINCT NULL) FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE 
```

---

## Crash 166: `e8ffcd116198b77c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137445`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT EXISTS (SELECT TRUE ORDER BY count(FALSE) OVER (ORDER BY FALSE DESC, CURRENT_TIME DESC) DESC N
```

---

## Crash 167: `04daceefa9c9d4e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137710`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT EXISTS (SELECT TRUE ORDER BY TRUE DESC NULLS FIRST) FROM p NATURAL JOIN p WHERE NULL; SELECT p
```

---

## Crash 168: `a1658d580ac75815` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137717`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT EXISTS (SELECT TRUE ORDER BY count(FALSE) OVER () DESC NULLS FIRST) FROM p NATURAL JOIN p WHER
```

---

## Crash 169: `16113cf897656e21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138189`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER DEFAULT X'eb49e6cf'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 170: `0979a35ce6515ac3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138285`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 171: `a73a03cf80b7b794` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140101`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE, c1 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, a INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 172: `908487c8d8a9b6de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140850`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT max(TRUE COLLATE RTRIM) AS a0; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 173: `225fe783513502f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142077`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER NOT NULL DEFAULT '-'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 174: `80438e3cc0b67f95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144484`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT CHECK (CURRENT_TIMESTAMP >= CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---
