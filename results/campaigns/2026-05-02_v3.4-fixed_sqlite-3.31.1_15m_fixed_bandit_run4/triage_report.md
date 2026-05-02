# Crash Triage Report

**Total crashes:** 192  
**Unique crash sites:** 192  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 192 | 192 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `48a1c2f9bde4fb4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000018`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO t3 VALUES (~NULL | CURRENT_TIMESTAMP <> (CURRENT_TIMESTAMP) LIKE CAST(CURRENT_TIME > FALSE NOT IN (VALUES (CURRENT_DATE)) << FALSE 
```

---

## Crash 2: `7be402c7fa0f3d6b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000326`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); INSERT INTO r VALUES (quote(CASE TRUE IS NOT NULL WHEN NULL THEN json_type(TRUE) FILTER (WHERE TRUE BETWEEN CURRENT_TIMESTAMP COLLATE RTRIM
```

---

## Crash 3: `ed7904a7ce62959f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002000`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSE
```

---

## Crash 4: `f8df2019b363f303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002125`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO p VALUES (NOT 'Lq' 
```

---

## Crash 5: `7a4ef817438a0807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002238`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE r (rowid) AS NOT MATERIALIZED (VALUES (FALSE) EXCEPT SELECT DISTINCT * FROM p NOT I
```

---

## Crash 6: `b9c63bc67808113e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002442`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s (c2) VALUES (CURRENT_TIMESTAMP) ON CONFLICT(c3) DO UPDATE SET rowid = CURRENT_TIMESTAMP; ANALYZE q; CRE
```

---

## Crash 7: `911f553eda5a174f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002519`

```sql
SELECT substr('-F ', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (a) VALUES (+typeof(TRUE) FILTER (WHERE json_array(+TRUE < RAISE(IGNORE) LIKE CURRE
```

---

## Crash 8: `e53b42c1269432fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002565`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (a) VALUES (+typeof(TRUE) FILTER (WHERE json_array(+TRUE < RAISE(IGNORE) LIKE CURRENT_TIME) FI
```

---

## Crash 9: `b6abddd1d7b0cef3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003135`

```sql
SELECT round(1e-308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIME LIKE RAISE(IGNORE) >> TRUE COLLATE NOCASE IS NULL & RAISE(IGNOR
```

---

## Crash 10: `3e150ebea68b9f5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004837`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO
```

---

## Crash 11: `9562a632709a71bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004887`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO p VALUES (RAISE(IGNORE)); SELECT +TRUE IS NOT CURRENT_TIMESTAMP >= EXISTS (SELECT CURRENT_TIMES
```

---

## Crash 12: `61cc610db8e8dd15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006478`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO q VALUES (FALSE COLLATE RTRIM - CURRENT_DATE AND CURRENT_DATE, -CURRENT_TIME <= NULL < RAISE(IGN
```

---

## Crash 13: `2792d0d44f1fbf9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006860`

```sql
SELECT printf('%lld', -2147483648, '-_6 --1__o_52H6 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (CURRENT_TIME NOTNULL IN (CURRENT_TIME != RAISE(IGNORE) <
```

---

## Crash 14: `bf9b551031e7b5c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007211`

```sql
SELECT printf('%.*e', -2147483648, -0.0); SELECT round(0.01, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT p.* FROM p JOIN t1 h_5sgjt ON (coalesce(CURRENT_TIMESTAMP, NU
```

---

## Crash 15: `41b8fb50b44251f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007538`

```sql
SELECT substr('', -2147483649, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT CASE NULL WHEN -CURRENT_TIME GLOB CURRENT_TIMESTAMP IN (NULL) T
```

---

## Crash 16: `4b795e419a19f358` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007893`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, _rowid_, a, b, c2); INSERT INTO t1 VALUES (typeof(FALSE IS NOT NULL >> (CURRENT_TIMESTAMP >> TRUE) == +CURRENT_TIME > NOT TRUE > FALSE MATCH
```

---

## Crash 17: `afbdaf3ddd1afea5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008617`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL DEFAULT X''); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAUL
```

---

## Crash 18: `a4f87bc25f72171e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009242`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO 
```

---

## Crash 19: `9f88a182326fb33e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012141`

```sql
SELECT printf('%.*f', -2147483649, -1e308); SELECT hex(zeroblob(4294967295));
```

---

## Crash 20: `ec4864737842b71b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012471`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PR
```

---

## Crash 21: `ca0061b461ae1d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012497`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 22: `40edea00609db480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012596`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT PRIMARY KEY, b TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 23: `372dc349a1be6443` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT PRIMARY KEY, b TEXT); INSERT INTO q (rowid) VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 24: `e4643e091baf2263` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013511`

```sql
SELECT substr('2', -1, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO p VALUES (FALSE IS NOT CURRENT_TIME IS NOT CASE CURRENT_TIME WHEN NULL THEN CURRENT_DATE END 
```

---

## Crash 25: `064d3d5f576490c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014235`

```sql
SELECT printf('%s', 1, '6_VC41_-_CT   '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES ((SELECT ALL * FROM t3 NOT INDEXED ORDER BY CURRENT_TIME NOTNULL NOT LIKE NULL 
```

---

## Crash 26: `8b08f423cd937d07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014384`

```sql
SELECT round(1e308, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO t2 VALUES (CASE CURRENT_DATE NOT IN (SELECT *) WHEN CURRENT_TIME COLLATE RTRIM THEN NOT NULL = EX
```

---

## Crash 27: `1f2105a78a25ff49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014691`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 
```

---

## Crash 28: `00b9938ccfa13477` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014698`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, c2); INSERT INTO r DEFAULT VALUES; SELECT *;
```

---

## Crash 29: `d3bbed1036018d0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015232`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 30: `fa5f9d348d71ca9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(2
```

---

## Crash 31: `af505e40a4a087d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015269`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(2
```

---

## Crash 32: `1aa2461b7db81e32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015279`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(2
```

---

## Crash 33: `2f9acc3ec63d4964` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015316`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE I
```

---

## Crash 34: `ab2065d7b0ce4a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015517`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 35: `74ad5d914bb0fad7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015611`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-9223372036854775808)
```

---

## Crash 36: `1dfd8f4edd93f743` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015990`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP ELSE CURREN
```

---

## Crash 37: `dc3304ee1ccc1825` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016213`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME <= CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMES
```

---

## Crash 38: `7ab5cfa87b0efb0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016283`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE - CURRENT_TIMESTAMP + TRUE NOT LIKE CURRENT_TIMESTAMP <= 
```

---

## Crash 39: `03624f59b76fce54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017151`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP <= CURRENT_TIME); PRAGMA integrity_che
```

---

## Crash 40: `6e447b1bc29fbdea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018245`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 41: `e04681b1d43c3d9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018430`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE IF NO
```

---

## Crash 42: `46af3aec45de0bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018719`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE + NULL); PRAGMA integrity_check; SELECT hex(zeroblob(-1))
```

---

## Crash 43: `cf99df291c35651c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018750`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 44: `e2d406336383a897` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018780`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 45: `cbfa268ea26b9c66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018812`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE + CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRT
```

---

## Crash 46: `5de70e35040bea91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019220`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL + CURRENT_DATE NOT LIKE CURRENT_TIMESTAMP); PRAGMA integr
```

---

## Crash 47: `c073c4e0e4b34262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019490`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*e', 92233720
```

---

## Crash 48: `807103a10ae610a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL <= NULL)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 49: `01a12206c14b03ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019991`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 50: `4185e3c00b52900c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020032`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 51: `844a887794acd362` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024912`

```sql
SELECT round(1e308, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `37d4244fd52de6bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026222`

```sql
SELECT substr('I3- - _I- 8f3lr_N', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP);
```

---

## Crash 53: `f81913d1a7bdcdb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026498`

```sql
SELECT printf('%.*d', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648));
```

---

## Crash 54: `20cee25e063a4d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026623`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (NULL) UNION ALL SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRST; CREAT
```

---

## Crash 55: `e39cedf52d615dde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026629`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (NULL) UNION ALL SELECT CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC; CREATE VIRTUAL TA
```

---

## Crash 56: `b78924e62e6f7169` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029143`

```sql
SELECT round(0.01, 2147483647); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 57: `3d343521ebaf9445` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031059`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 58: `8436ab7ef078e02d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031113`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 59: `027c40ef33522a3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032829`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT FALSE NOT BETWEEN NULL AND TRUE FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 60: `0ad5d4ef0c968e23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033578`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIME == CURRENT_TIME COLLATE RTRIM AND TRUE FROM p WHERE EXISTS (VALUES (TRUE)); CREA
```

---

## Crash 61: `6d3de6c6d6924f90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034531`

```sql
SELECT printf('%llu', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, b); INSERT OR FAIL INTO p VALUES (group_concat(~CURRENT_DATE IS DISTINCT FROM RAISE(IGNORE)) OVER (PA
```

---

## Crash 62: `0ae86dfb34573aa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036570`

```sql
SELECT printf('%.*s', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT r.* FROM p CROSS JOIN t3 NOT INDEXED JOIN p INDEXED BY c1 ORDER BY NOT NOT FALSE / NULL < CURR
```

---

## Crash 63: `beab413468aebc8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON CURRENT_TIMESTAMP < CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF N
```

---

## Crash 64: `c232aafc76411e32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037524`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT p.* FROM p JOIN q g ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 65: `68711057d4a40cad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037978`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 66: `33011828cbe7c566` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038121`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 67: `6e0464b9437e14bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038847`

```sql
SELECT printf('%.*e', -2147483649, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 68: `5df1efc37fbaf832` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038891`

```sql
SELECT printf('%.*f', 2147483647, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT t2.*, CASE WHEN TRUE <= CURRENT_TIMESTAMP THEN CURRENT_TIME ISNULL + NULL ELSE FALSE COLLATE BI
```

---

## Crash 69: `5c6555e4465f6d56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041121`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 70: `eee5d5187daf3a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043070`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE, CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY, a INT GENERATED ALWAYS AS (RAISE(IGNORE)) STORED
```

---

## Crash 71: `23863fc6d906e210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043634`

```sql
SELECT substr('', -2147483648, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a); SELECT ~CURRENT_DATE COLLATE RTRIM IS NOT CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP ESCAPE -TRUE 
```

---

## Crash 72: `d40f56ca817ba4c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044308`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CAST(CURRENT_DATE AS BOOLEAN)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 73: `43b1c0af1775b0b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044517`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_DATE AND CURRENT_DATE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 74: `94e9b529469431c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045063`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CURRENT_DATE AND CAST(NULL AS BOOLEAN)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 75: `ae78a854abd817c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045624`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 76: `5c9ed41fe26b28e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045841`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE, c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 77: `5df5794ec494047e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049592`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); VALUES (NULL); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 78: `2720f6704301274d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049886`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM p NOT INDEXED CROSS JOIN p USING (c3, a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VI
```

---

## Crash 79: `11de5296cbbb01d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049930`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM p NOT INDEXED CROSS JOIN p ON TRUE; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 80: `b47346b176ec93f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049991`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p JOIN q ON CURRENT_DATE WHERE RAISE(IGNORE) GROUP BY CURRENT_TIMESTAMP; INSERT INTO p DEFAULT VALUES
```

---

## Crash 81: `38a75d48f2e134d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050402`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 82: `94929e606d9c9994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051327`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p VALUES (CAST(CURRENT_DATE AS BLOB)); PRAGMA quick_check; SELECT printf('%.*f', -2147483649, -1e30
```

---

## Crash 83: `2125d27fb842fc25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051862`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE, min(NULL)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 84: `8b7b0f94583c4657` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051999`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE, random()); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 85: `99240eef4a0df79e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052298`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE); EXPLAIN QUERY PLAN VALUES (count(DISTINCT TRUE) FILTER (WHERE CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); SELECT ALL (CURRE
```

---

## Crash 86: `bb0689a5f68cbdbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053813`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (TRUE IN (-57564461652492770112862792873963929502903623037696402237561676562818669319752525191049054819050.0682396e-7)) UNION ALL VA
```

---

## Crash 87: `0a3c5a5a305a720e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054113`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 88: `9a1471c5125f23f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054121`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (TRUE IN (CURRENT_DATE)) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 89: `6ec7bc3cbc6a0ec6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054919`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) UNION ALL VALUES (random()); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 90: `0c88759740c6cd87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055626`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 91: `b3d7d5b88c6b31e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058700`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB DEFAULT -96); SELECT * FROM p JOIN q g ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 92: `9e19df5036153dca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058791`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 BLOB DEFAULT NULL); SELECT * FROM p JOIN q g ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 93: `e6cd31158db1c278` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059800`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON NULL; CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); INSERT I
```

---

## Crash 94: `d8d40c779d31bb15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON TRUE GLOB CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 95: `3d8ec46fa5ca4d92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060358`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON CURRENT_TIME == NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 96: `26d1ffc7d5a878f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060586`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY); SELECT * FROM p JOIN q g ON CURRENT_TIME BETWEEN NULL AND CURRENT_TIME; CREATE VIRTUAL TABLE
```

---

## Crash 97: `67a6080758f07236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061292`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); EXPLAIN QUERY PLAN SELECT X'fdfFD1A9B2e57f'; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 98: `86dfaf66bb495896` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064368`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT CURRENT_TIMESTAMP NOT BETWEEN CURRENT_TIMESTAMP COLLATE RTRIM AND TRUE FROM p WHERE EXISTS (VALUES (count(*) OVER (PARTITIO
```

---

## Crash 99: `892c1b35432dbe94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065039`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE, c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); SELECT TRUE FROM p WHERE EXISTS (VALUES (TRUE)); SELECT printf('%.*g', 2147483647, 0.01
```

---

## Crash 100: `bd25ac3067124749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065182`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE, c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (TRUE)); SELECT hex(zeroblob(0)); CREATE VIRTUAL T
```

---

## Crash 101: `7c931ce3d2fa27d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065449`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST ROWS BETWEEN CURRENT ROW AND TRU
```

---

## Crash 102: `e881523c4b7388e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065730`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER () FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 103: `11b0ad912e5fded2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065737`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 104: `c47ddebdf2528485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067307`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT min(NULL) FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE 
```

---

## Crash 105: `b1643a75a0230d71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067472`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) FROM p WHERE EXISTS (VALUES (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE I
```

---

## Crash 106: `7f43b21577f23fa6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067593`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) OVER (ORDER BY CURRENT_TIMESTAMP ASC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT 
```

---

## Crash 107: `f93f8ac9d2213622` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067765`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, a GENERATED ALWAYS AS (a) ); SELECT count(*) OVER () FROM p WHERE EXISTS (VALUES (TRUE)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 108: `6759b1011b4cf036` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070548`

```sql
SELECT round(-1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q SELECT CURRENT_DATE AS lu_b8; EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(0));
```

---

## Crash 109: `4f48ba4f9efd36ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075108`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL DEFAULT -9352349363680673627233145416646188411708387791703108238775354643740751622406876420193353986776320808679030953870522787526450314586775694626650420
```

---

## Crash 110: `2bac3e55caad70e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075319`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT -485512032048114916.1e26); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', -2
```

---

## Crash 111: `245ed70490110058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075923`

```sql
SELECT substr('-', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (lower(CURRENT_TIME)) LIMIT NULL OFFSE
```

---

## Crash 112: `92710b7d2a9346b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076815`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (FALSE) EXCEPT VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 113: `28e564a3a276a022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077786`

```sql
SELECT printf('%.*g', 4294967295); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 114: `92a6fee23405a8dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078245`

```sql
SELECT substr('', -9223372036854775808, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN SELECT CAST(+FALSE | CURRENT_DATE IS NOT NULL OR CURRENT_TIME AS DATE) 
```

---

## Crash 115: `c6ebe156a0536d17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081389`

```sql
SELECT printf('%.*e', 2147483647); SELECT printf('%.*g', 2147483647, -1e308); SELECT printf('%.*g', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES;
```

---

## Crash 116: `2389ad44946299ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083208`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (FALSE) UNION VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 117: `5067260a7abcfa11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083593`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (FALSE) UNION VALUES (count(*) OVER (ORDER BY TRUE ASC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)); SELECT printf('
```

---

## Crash 118: `450860d5cdf73804` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085301`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN UNIQUE); EXPLAIN QUERY PLAN SELECT ALL CURRENT_TIMESTAMP, * FROM p NOT INDEXED ORDER BY FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 119: `b32f1f21ab6b81b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088532`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (TRUE IS NOT NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 120: `4a1ab6f0475850a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088648`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 121: `07e5c2ed3494bc67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088820`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (TRUE IS NOT CURRENT_TIME)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 122: `034534499e06846f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090041`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 123: `95a04a3a92d8fea6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090346`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('-_', 9223372036854775807, 
```

---

## Crash 124: `7b0c27079209367e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090363`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, 
```

---

## Crash 125: `8422a9671c42650a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090375`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ FLOA
```

---

## Crash 126: `3d591e5f2e10c851` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090604`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL <= TRUE IN (CURRENT_TIME))); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 127: `f82a59dc98ea62bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091054`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (CURRENT_DATE != CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE V
```

---

## Crash 128: `a13a5c6012ee8ba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091130`

```sql
CREATE TABLE IF NOT EXISTS p(rowid DATE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER NOT NULL DEFAULT ' s_15m'); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 129: `30ce101b8ed223fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091336`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL <= p.c3)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f', -2
```

---

## Crash 130: `567be4d36a1aa5ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091726`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (NULL <= rowid)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f', -
```

---

## Crash 131: `651ad6ae71431ad8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091747`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIME AS REAL) + FALSE); PRAGMA integrity_check; C
```

---

## Crash 132: `efa01439f51cef0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091934`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP + FALSE); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 133: `ba9aaa6040ddf6b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092074`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL NOT NULL DEFAULT X'cfcA4De0F2Ff'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 134: `18e0c163dc689431` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092867`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 135: `9da3d0755d6eb8f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092923`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 136: `514a52700e5253db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092999`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT substr('-_AL8_v_-4G4_ -
```

---

## Crash 137: `8d8033b84def35e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093093`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 138: `289e6219c8bec586` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093251`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE + NULL); PRAGMA integrity_check; SELECT printf('%.*f', -2
```

---

## Crash 139: `f82b0dad01265ed9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093302`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2
```

---

## Crash 140: `1bc587c9ff9106d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093619`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL CHECK (CURRENT_TIMESTAMP), b REAL CHECK (FALSE), c3 TEXT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP)
```

---

## Crash 141: `d3c5c4dd8e8f9d3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093693`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC NOT NULL, b REAL CHECK (FALSE), c3 TEXT); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA inte
```

---

## Crash 142: `6629aa4052725ffd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094185`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL GENERATED ALWAYS AS (FALSE) STORED, c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 143: `e7a862a59f7438e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094917`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME ISNULL NOT LIKE CURRENT_TIMESTAMP <= CURRENT_TIME); PRAGMA integr
```

---

## Crash 144: `af80a0f217ce4585` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095522`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL CHECK (CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME NOT LIKE CURRENT_
```

---

## Crash 145: `9d5556f4f16fead3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096583`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT INTO q SELECT FALSE AS lu_b8; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 146: `dbf0f86ed6e0d1bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097827`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE / CURRENT_TIMESTAMP); PRAGMA integrity_check; CRE
```

---

## Crash 147: `400cfdd623e584f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098814`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL DEFAULT -485512032048114916.1e26); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA quick_check; CREAT
```

---

## Crash 148: `b9f992bb137435aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099777`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 149: `2c23cd081e5a9b4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100247`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 150: `825dfaf0a49351ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101887`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (NULL LIKE NULL ESCAPE NULL); PRAGMA integrity_check; SELECT su
```

---

## Crash 151: `7d86c4cdfdd520ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104903`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3
```

---

## Crash 152: `98ac645875f8cbfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105123`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL DEFAULT 0.0); INSERT INTO q (rowid) VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 153: `e916e351d244e5b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106318`

```sql
SELECT printf('%.*d', -2147483649, 1e308); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 154: `235a40593c9911c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106579`

```sql
SELECT printf('%.*d', -2147483649, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 BL
```

---

## Crash 155: `68b008bf8819515f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108668`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q; SELECT substr('_xG_', 2147483647); CREAT
```

---

## Crash 156: `c97783f7fa4c3181` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110779`

```sql
SELECT printf('%.*s', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *, NULL IS DISTINCT FROM RAISE(IGNORE) NOT BETWEEN TRUE COLLATE RTRIM AND random() % RAISE(IGNORE) ->
```

---

## Crash 157: `8a2d7d1cd56e7bb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE FALSE; SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 158: `89c49ab0af63a272` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112765`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY TRUE, NULL NOT BETWEEN TRUE AND CURRENT_TIMESTAMP || NULL; C
```

---

## Crash 159: `6f1403e03a2ef8c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY TRUE, TRUE IS NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 160: `65c8e30dcd01d73d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113822`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY TRUE, FALSE <> (VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 161: `cd4815a31c25a288` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114234`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) DEFAULT FALSE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 162: `f121b0d1c42f6772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p AS k2_7 LEFT JOIN p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 163: `0dab3e673bfe078e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114569`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT NULL IS NOT CURRENT_TIME NOTNULL FROM q; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 164: `5042e83ad60b96cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114719`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT CASE CURRENT_TIMESTAMP WHEN FALSE THEN +TRUE END FROM q LEFT JOIN p NOT INDEXE
```

---

## Crash 165: `30e2970601b2d4e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115238`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY TRUE >> CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 166: `e9a24eaa25b3cf57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q GROUP BY CURRENT_TIMESTAMP; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 167: `5c73bf56944a40ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116362`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) UNIQUE, c3 BOOLEAN UNIQUE, c1 INT UNIQUE, b REAL NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY CU
```

---

## Crash 168: `bfa0efddc0e6f661` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118113`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT ALL CURRENT_TIME BETWEEN NULL AND CURRENT_TIME AS e_ FROM p NOT INDEXED; SELEC
```

---

## Crash 169: `7a46d0f5dd599628` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118589`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_DATE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); WITH 
```

---

## Crash 170: `52e9ce17b8dca0d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119977`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC GENERATED ALWAYS AS (NULL COLLATE NOCASE) VIRTUAL, _rowid_ REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); SELECT * FROM p JOIN p a ON FALSE; SELECT printf
```

---

## Crash 171: `de514ee5b87de05d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121668`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (total_changes() LIKE EXISTS (VALUES (NULL)) ESCAPE TRUE, NULL); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 172: `22d4797abcb6c776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124068`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM q GROUP BY TRUE >> TRUE >> NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 173: `5d58bb242a3c2364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124202`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT CURRENT_DATE FROM q LEFT JOIN (p INNER JOIN q NATURAL LEFT JOIN p NOT INDEXED)
```

---

## Crash 174: `fb58a13f70035389` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125729`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL LEFT JOIN p , q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 175: `4d41099afd7d29cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126150`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p AS py7_9_oq_ozp NATURAL LEFT JOIN p NOT INDEXED GROUP BY FALSE; CREAT
```

---

## Crash 176: `4547941a1dae6be7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128188`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT); CREATE TABLE IF NOT EXISTS q(b FLOAT UNIQUE); INSERT OR REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN p
```

---

## Crash 177: `18e83d653db89f03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130627`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT DEFAULT CURRENT_DATE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 178: `0a6412b6c31dc261` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL DEFAULT '- - _ -D--x 0'); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 179: `fdf3390ca64d1137` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132270`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT INTO q (rowid) VALUES (TRUE - CURRENT_DATE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT
```

---

## Crash 180: `b34dbb3f43259451` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133533`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (json_valid(CURRENT_TIMESTAMP)); PRAGMA integrity_check; SELECT
```

---

## Crash 181: `e3334d608a19765e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (changes()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 182: `8ecdb9330f9a10ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135198`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 183: `84574ac613ac30de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135218`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXI
```

---

## Crash 184: `6268e316cbf09347` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135506`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME <= CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMES
```

---

## Crash 185: `a1ae71a38458b03c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135647`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES ((VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM q NOT INDE
```

---

## Crash 186: `edb404f282d9a8d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136616`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(FALSE AS VARCHAR(255))); PRAGMA quick_check; CREATE VIRTUAL TAB
```

---

## Crash 187: `b8e53e4e70bc5651` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136744`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIMESTAMP AS INT) IN (VALUES (CURRENT_TIMESTAMP))
```

---

## Crash 188: `6a5b0be84b880a29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136977`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE IN (VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CR
```

---

## Crash 189: `3d4f3151e4ced275` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137887`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (-5756446165249277011286279287396392950290362303769640223756167
```

---

## Crash 190: `ff94c5717d8f95b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138139`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 191: `b1b10fc3dc679114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138155`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 192: `1323c48af35cf9f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138703`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE < 7.5E+49877662865496298295554486388920902657799380884349
```

---
