# Crash Triage Report

**Total crashes:** 286  
**Unique crash sites:** 286  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 286 | 286 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `f8b140451c5e2b36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000106`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c1, c2, c3, c3, a); SELECT EXISTS (SELECT RAISE(IGNORE)), q.* FROM p NATURAL JOIN p WHERE hex(NOT CASE WHEN NOT EXISTS (WITH RECUR
```

---

## Crash 2: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000347`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 3: `7bbc49ac0b53182d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000971`

```sql
SELECT printf('%.*f', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (+NULL NOTNULL <> CURRENT_DATE AND ~TRUE - -count(*) IN (TRUE, FALSE COLLATE RTRIM) | (avg(EXI
```

---

## Crash 4: `f08d3b7d86cf6281` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001069`

```sql
SELECT printf('%.*f', 2147483647, -1e308); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURSIVE q AS (SELECT ALL *, * FROM p NOT INDEXED LEFT OUT
```

---

## Crash 5: `6ac12a94241c3c8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001425`

```sql
SELECT printf('%.*f', -9223372036854775808, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); WITH RECURSIVE q (b, c3) AS (SELECT TRUE NOT IN (SELECT CURRENT_DATE FROM r NOT INDEXED) 
```

---

## Crash 6: `87a01a68e309fa26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001514`

```sql
SELECT substr('MM__ 8c1Os', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q (a, a) VALUES (CURRENT_DATE & CURRENT_TIMESTAMP | CURRENT_TIMESTAMP ISNULL, +TRUE
```

---

## Crash 7: `d923df055d215d28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001786`

```sql
SELECT printf('%.*e', -2147483649, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (NULL ISNULL NOT IN (VALUES (CURRENT_DATE)) NOT NULL, ~NULL IS FALSE = CURRENT
```

---

## Crash 8: `afe8f41359c90250` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (RAISE(IGNORE) IS 
```

---

## Crash 9: `449e804704404488` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003226`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT ~CURRENT_TIME AS m__7u_t0_v____r1fgl_1_3 FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CRE
```

---

## Crash 10: `5d766a4617e392f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003232`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT ~CURRENT_TIME AS m__7u_t0_v____r1fgl_1_3 FROM p NATURAL JOIN q WHERE (CURRENT_TIMESTAMP); C
```

---

## Crash 11: `a700be8f838ca051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003238`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT ~CURRENT_TIME AS m__7u_t0_v____r1fgl_1_3 FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (C
```

---

## Crash 12: `0b15777e05da1752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003244`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT ~CURRENT_TIME AS m__7u_t0_v____r1fgl_1_3 FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (C
```

---

## Crash 13: `bd9acfe55d319773` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003303`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 14: `53aad95f3a3418c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003311`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p
```

---

## Crash 15: `bc13d24885de396d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003318`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p
```

---

## Crash 16: `cf6b176433493381` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003324`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p
```

---

## Crash 17: `6c3e186989d32d16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003354`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (RAISE(IGNORE) IS NULL, RAISE(IGNORE)) LIMIT group_concat(RAISE(IGNORE) GLOB CURRENT_DATE COLLATE RTRIM, '') FI
```

---

## Crash 18: `1762fd4a7ab0aac6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003361`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 19: `36d982d4cd342a88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003368`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 20: `34208e13d2015826` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003375`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION VALUES (CURRENT
```

---

## Crash 21: `2758adbb97f43f56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003389`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (RAISE(IGNORE) IS NULL, RAISE(IGNORE)) LIMIT group_concat(RAISE(IGNORE) GLOB CURRENT_DATE COLLATE RTRIM, '') F
```

---

## Crash 22: `8384e70eda7e6bd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003431`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p
```

---

## Crash 23: `3685f04af070606a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003560`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT CURRENT_
```

---

## Crash 24: `2bb5e7079e776006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004160`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t2 CROSS JOIN p NOT INDEXED ON CURRENT_TIMESTAMP UNION ALL SELECT * FROM t3 WHERE TRUE GROUP BY NU
```

---

## Crash 25: `6e4049e7dde16f49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004195`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q VALU
```

---

## Crash 26: `bd863f8990f75bf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004255`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT * FROM t3 WHERE TRUE GROUP BY CURRENT_DATE WINDOW w1 AS (ORDER BY RAISE(IGNORE) ASC ROWS BETWEE
```

---

## Crash 27: `7b269e4cc3fb2af8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004273`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT * UNION ALL SELECT * FROM t3 WHERE TRUE GROUP BY CURRENT_DATE WINDOW w1 AS (); VALUES (CURRENT_DATE); CREATE VIRTU
```

---

## Crash 28: `7ae5fcdfc606a4ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004352`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT printf('%x', 0, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO q VALUES (avg(CURRENT_TIME) IN (CASE TRUE COLLATE NOCASE WHE
```

---

## Crash 29: `ede3e34f79782049` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005296`

```sql
SELECT round(1.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NULL % ~TRUE NOTNULL < FALSE FROM t2 NOT INDEXED GROUP BY RAISE(IGNORE) HAVING (SELECT * FROM r ORDER BY 
```

---

## Crash 30: `382deb04610ad30b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005837`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE 
```

---

## Crash 31: `a42f21fde6029b9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006259`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 SELECT ALL q.* FROM p NATURAL JOIN q INDEXED BY _rowid_ UNION SELECT +CURRENT_TIMESTAMP AS o
```

---

## Crash 32: `7f90c1c416f79c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006315`

```sql
SELECT printf('%lld', -2147483648, '_3--8N0'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (TRUE <= CASE TRUE WHEN NULL THEN RAISE(IGNORE) ELSE NULL END); ANALYZE p; 
```

---

## Crash 33: `e5bec9626731205e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007003`

```sql
SELECT substr('', 4294967296, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NULL UNIQ
```

---

## Crash 34: `a85fe72d75984838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007019`

```sql
SELECT substr('', 4294967296, 2147483648); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT CURRENT_DATE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR
```

---

## Crash 35: `a1083e6aecb8360c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007094`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE IS NOT FALSE COLLATE RTRIM)
```

---

## Crash 36: `8e408bf0f6015658` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007227`

```sql
SELECT substr('', 4294967296, 2147483648); CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO 
```

---

## Crash 37: `cecaf8695ca5ac60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008404`

```sql
SELECT round(-1e308, -2147483649); SELECT printf('%.*s', 4294967296); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, b); SELECT r.*, ~NULL || 
```

---

## Crash 38: `41244622e601a59e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011622`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); EXPLAIN QUERY PLAN VALUES (-CURRENT_DATE 
```

---

## Crash 39: `a4e2aa8b676424ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012834`

```sql
SELECT substr('-2F', 4294967295, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t3 DEFAULT VALUES; SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 40: `824b5fb84bd9f9a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013496`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *
```

---

## Crash 41: `d31ea02bd393b52c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014484`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL DEFAULT X'c5'); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (CURRENT_T
```

---

## Crash 42: `f1c43b258f8044c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 43: `bb5dc080837b45fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016322`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT TRUE - CURRENT_DATE ISNULL AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 44: `863b99beb2f7613f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016983`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT NULL - NULL AS xm__a_99g_kf2_r0 FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 45: `e5183a3a44aab77f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017333`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT NULL COLLATE RTRIM AS xm__a_99g_kf2_r0 FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 46: `b097c4054dd89c69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018423`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p VALUES (CURRENT_DATE); 
```

---

## Crash 47: `6e452966da6e8aa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018666`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CURRENT_DATE NOT IN (NULL), * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 48: `c3af48c5d59a1900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020509`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 49: `019c610cfbfcff7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021109`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 50: `46ad2d4e471276b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022059`

```sql
SELECT printf('%.*g', 0, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c1, c2, c3, c3, a); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 51: `f09c9ef701044c14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022866`

```sql
SELECT substr('--_y-mgv  N-  ahQ -', 0, -1); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `39625497652db0fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023512`

```sql
SELECT printf('%.*g', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid FLOAT, rowid GENERA
```

---

## Crash 53: `8ea54ae4a99a7b79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025171`

```sql
SELECT substr('s_-mnq - --a', 2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p SELECT _rowid_ FROM t3 , t3 USING (c1) WHERE CURRENT_DATE IN (VALUES (CUR
```

---

## Crash 54: `fb1ba62a9f32c4b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026651`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 55: `448ec6a3190b45b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029118`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (TRUE >> CURRENT_TIMESTAMP >= CURRENT_DATE NOTNULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 56: `8cacc9228499757e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_TIME >= CURRENT_DATE NOTNULL); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 57: `cb1341f92eeaff62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030189`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE CURRENT_DATE LIMIT CURRENT_TIMESTAMP, FAL
```

---

## Crash 58: `ec3904e2e8998532` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030512`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q WHERE CURRENT_DATE LIMIT TRUE; SELECT printf('%
```

---

## Crash 59: `3368cb9a5150c96b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031143`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); IN
```

---

## Crash 60: `ac2de340d58fc3d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032494`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 61: `936453652c37579b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033566`

```sql
SELECT round(-1.0, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM t3 WHERE EXISTS (VALUES (TRUE, CURRENT_TIME) ORDER BY FALSE DESC NULLS LAST); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 62: `4188df207931af3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033867`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (CURRENT_DATE NOT IN (VALUES (TRUE)), TRUE IS NOT NULL COLLATE 
```

---

## Crash 63: `fb521309d9adff30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034053`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (TRUE NOT IN (VALUES (TRUE)), TRUE) ON CONFLICT DO NOTHING; PRA
```

---

## Crash 64: `a73bd665893c682f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034620`

```sql
SELECT round(-1.0, 0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 65: `9e2b3160321199b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037263`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_DATE == CURRENT_TIME COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, a);
```

---

## Crash 66: `1160efd992bbc232` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037317`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, a); SELECT q.*, CURRENT_DATE != FALSE || R
```

---

## Crash 67: `490ea4777e11baa2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037323`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_DATE == TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, a); SELECT q.*, CURRENT_DA
```

---

## Crash 68: `db6a74dfa3a82cef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037610`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_DATE == CURRENT_TIMESTAMP; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 69: `bf9f97604da398cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037937`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE COLLATE NOCASE IN (VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT RA
```

---

## Crash 70: `d8799b56e7ae8ba9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041647`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT *, p.*, * FROM p NOT INDEXED LIMIT FALSE; SELECT
```

---

## Crash 71: `9c0418eae3925248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042257`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT TRUE < TRUE; SELECT printf('%.*f'
```

---

## Crash 72: `231007cc925d76a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042676`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT -9338992037517287064530680820169.
```

---

## Crash 73: `de332ad9da5f3e17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043808`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE == CASE NULL WHEN CURRENT_TIME THEN CURRENT_DATE LI
```

---

## Crash 74: `244693b2e1d06850` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046187`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 75: `cff29d775444b423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048219`

```sql
SELECT printf('%.*s', 2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (NULL - NULL >> CURRENT_TIMESTAMP GLOB TRUE COLLATE BINARY IS NULL AND CURRENT
```

---

## Crash 76: `0c6ec577da967178` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048777`

```sql
SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, * FROM (SELECT * FROM q WHERE TRUE -> RAISE(IGNORE)) AS sub1; SELECT printf('%.*g', -922
```

---

## Crash 77: `ca76494dea33ec68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053671`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY CURRENT_DATE DESC NULLS LAST L
```

---

## Crash 78: `6abc8915e9ea5520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054869`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT -0 NOT IN (VALUES (CURRENT_TIME))
```

---

## Crash 79: `406d08814f99d55f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055202`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT 'z3' NOT IN (VALUES (CURRENT_TIME
```

---

## Crash 80: `fd6868aa76b47395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055473`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT -0; SELECT printf('%.*g', 2147483
```

---

## Crash 81: `bebb9fc936beb2c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056850`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY, c2 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT 
```

---

## Crash 82: `b7ed60c64f7bc2e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056986`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT CURRENT_DATE; CREATE VIRTUAL
```

---

## Crash 83: `82ea129649095d94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058306`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW E
```

---

## Crash 84: `c04ffce068cbe38d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059268`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT NULL IN (
```

---

## Crash 85: `0c9c4a4d92187d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059787`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT CURRENT_T
```

---

## Crash 86: `8e69433e6abc6d38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060249`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p 
```

---

## Crash 87: `aee10b6ff27588b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061008`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE TRUE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 88: `8eb1bdf373267cd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061245`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT '-jrS oq_ _Yw4- '); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 89: `a4c3d8fe10bcd72e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061762`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE TRUE LIKE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 90: `c40a3d3fd4b2fee2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062081`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER NOT NULL, c1 INT NOT NULL DEFAULT CURRENT_TIMESTAMP); SELECT * FROM p NATURAL JOIN q WHERE NULL; SELECT print
```

---

## Crash 91: `0e8b4171887dbb31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064017`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE IN (VALUES (count(*) OVER ())); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2); INS
```

---

## Crash 92: `f6eb7e592a89ac4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064185`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE IN (VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME DESC GROUPS BETWEEN UNBOUN
```

---

## Crash 93: `3a68685dc92ac0eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064962`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIME); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 94: `f5fd697ae084a0b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065049`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON NULL IS NULL | FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT q.* FROM q CROSS JOIN
```

---

## Crash 95: `2067fba4cd9258df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066296`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_DATE == CURRENT_DATE COLLATE NOCASE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSER
```

---

## Crash 96: `c95a81e64fe1924f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066861`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE < CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); INSERT OR ABORT INTO q 
```

---

## Crash 97: `08b04f196500eefd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067195`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT count(*) OVER (), * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CURRENT_TIME); CRE
```

---

## Crash 98: `74f192d358efb589` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069064`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t2 CROSS JOIN p NOT INDEXED ON CURRENT_TIMESTAMP UNION ALL SELECT * FROM t3 WHERE TRUE GROUP BY RA
```

---

## Crash 99: `894d234d90dd5988` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069105`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (NULL); SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 100: `67c54aa90b29e618` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069111`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (CURRENT_TIME); SELECT printf('%.*g', 9223372036854775807); CREATE VIRTUAL TABLE IF
```

---

## Crash 101: `36ca912474625555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074765`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 102: `139a3ec17aac2b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075409`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_DATE FROM q WHERE CURRENT_DATE LIMIT NULL; CREAT
```

---

## Crash 103: `d513524a52f993fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075800`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIM
```

---

## Crash 104: `899b9dfbf7d6cf6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076641`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q AS r3_1 LEFT JOIN p NOT INDEXED , q WHERE CURRE
```

---

## Crash 105: `2ce3e1505ab02dbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078492`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE >> CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (FA
```

---

## Crash 106: `f9dd797a0c8507a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078678`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO p VALUES (TRUE >> CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRT
```

---

## Crash 107: `c6d23b9c49e292a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (random()); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPL
```

---

## Crash 108: `1380bab0356c6da4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079416`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (last_insert_rowid()); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 109: `9360c6aa6fa5a300` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079937`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(~NULL, FALSE, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 110: `c219f13047a3e1de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080047`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (total_changes()); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 111: `58fb9e1abed24575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080053`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(CURRENT_TIMESTAMP, FALSE, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147483647,
```

---

## Crash 112: `98d0487c7f47d948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080230`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(~NULL, FALSE, NULL)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 113: `e013e5f784a16c4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080268`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (changes()); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_); SEL
```

---

## Crash 114: `c8165e137de12940` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081664`

```sql
SELECT printf('%.*d', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT CURRENT_DATE; SELECT 
```

---

## Crash 115: `25b31d01476822fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081975`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 116: `25222be08be34929` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084836`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c3, c1); WITH q (b) AS NO
```

---

## Crash 117: `e6e1cdf0ca574e54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085407`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a) UNIQUE, c3 FLOAT UNIQUE); SELECT DISTINCT * FROM p LIMIT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p 
```

---

## Crash 118: `045686808fa6b456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087001`

```sql
SELECT substr(' v7-i-6_7o', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAIN QUERY PLAN SELECT ALL ~NULL == ~RAISE(IGNORE) - RAISE(IGNORE) IS DISTINCT FROM CURRENT_TIMEST
```

---

## Crash 119: `e53ee13d04d83589` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087852`

```sql
SELECT printf('%.*s', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON 
```

---

## Crash 120: `033aeec0515904a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088983`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE), NULL)); C
```

---

## Crash 121: `bbce7cd6d24b29d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089248`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO p VALUES (NULL); SELECT * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE V
```

---

## Crash 122: `dbb011ad50913682` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092272`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT, rowid GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a BLOB NOT NULL); INSERT INTO p VALUES (CURRENT_DATE, TRUE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE I
```

---

## Crash 123: `1d6a6bdca853b985` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093343`

```sql
SELECT printf('%.*e', 2147483648, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES (EXISTS (SELECT * EXCEPT SELECT * ORDER BY CURRENT_TIMESTAMP << RAISE(IGNORE) LI
```

---

## Crash 124: `9f535b0dcd9ec93c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094727`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (TRUE <= -9338992037517287064530680820169.78e436971906763146116237125313119
```

---

## Crash 125: `a28bfada517784e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098158`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 126: `9513813b36ba4f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099251`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT X'85a3'); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CURRENT_TIME); C
```

---

## Crash 127: `5a456ef251b215a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100612`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS), * FROM p WHERE 
```

---

## Crash 128: `e8eb2b9161aff18e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100974`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE FALSE ISNULL) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 129: `db03d8746558132c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101306`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP), * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL
```

---

## Crash 130: `857b6738fbe0dd12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104196`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT 'E614  1_'); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT (NOT CURRENT_D
```

---

## Crash 131: `77d13faf64d9ea6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104264`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL DEFAULT NULL); SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT (NOT CURRENT_DATE) A
```

---

## Crash 132: `ae2782809cb1e3e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104649`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE 
```

---

## Crash 133: `4273fa6d0a1de0b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105028`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT CURRENT_DATE NOT IN (TRUE) FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 134: `34aef92db6124a7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105956`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, c3 VARCHAR(255) NOT NULL DEFAULT FALSE); SELECT * FROM (SELECT FALSE AS xm__a_99g_kf2_r0 FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 135: `81020c6cdfa98a4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106722`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, b GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE); SELECT * FROM (SELECT CURRENT_TIME AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 136: `ea058a19cb0829cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107099`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE CAST(FALSE AS REAL)) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT CURRENT_TI
```

---

## Crash 137: `526520f3f1f60b28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107416`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CURRENT_TIME + TRUE - CURRENT_TIME AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 138: `f43b49cc95d6e79b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107675`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT NULL NOT LIKE count(*) FILTER (WHERE FALSE) + TRUE AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF N
```

---

## Crash 139: `c2ada9289d4d2240` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107710`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT NULL NOT LIKE NULL + TRUE AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 140: `8c9bd3bf41957a98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108525`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT TRUE - TRUE - TRUE - TRUE - CURRENT_TIMESTAMP AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; SELECT printf('%.*g', 21474836
```

---

## Crash 141: `b4fd3b3315df2629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); VALUES (count(DISTINCT CURRENT_TIMESTAMP) FILTER (WHERE CURRENT_TIMESTAMP) - NULL IS NULL COLLATE NOCASE, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 142: `2fa31ff9cac12574` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111990`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH p AS (VALUES (FALSE)) VALUES (NULL); INSERT INTO 
```

---

## Crash 143: `d0b2c36824b9dfa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112001`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREATE 
```

---

## Crash 144: `b6e2ad62f817929a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112041`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p SELECT DISTINCT * FR
```

---

## Crash 145: `2a68266614faa857` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112086`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(b NUMERIC GENERATED ALWAYS AS ((c2)) VIRTUAL, c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSE
```

---

## Crash 146: `d7060e73690df453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112162`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * FROM (SELECT CURRENT_TIMESTAMP, * FROM p WHERE NU
```

---

## Crash 147: `729e8cf37ba4f971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112197`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT NOT NULL DEFAULT 2.73536388864846552001717228e+20073859017138970468889648140620834987298173931015435374599449715491282412812866439193855748890872277819702114026623
```

---

## Crash 148: `f1ef910b1aa2833c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112436`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR FAIL INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 149: `6a78176fcc302b25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116955`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT 
```

---

## Crash 150: `60cd82cf8fb6ac42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117901`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT -673); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 151: `4b43bd9a8fd68261` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119522`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CAST(CURRENT_DATE AS REAL), CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 152: `a8fe916214a68a8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119730`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CURRENT_DATE == CAST(CURRENT_TIME AS REAL), CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 153: `251ed666d0297493` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119947`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON NOT EXISTS (VALUES 
```

---

## Crash 154: `0cdf8132a64feb95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120048`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES ((VALUES (FALSE)), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT
```

---

## Crash 155: `c35a9e995c26bea8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120440`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT -183295.50); CREATE INDEX IF NOT EXISTS 
```

---

## Crash 156: `045a93260dd4a873` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120469`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC N
```

---

## Crash 157: `033467dcb13beb66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121962`

```sql
SELECT printf('%.*d', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT INTO q SELECT t1.* UNION ALL SELECT * FROM r NOT INDEXED GROUP BY CURRENT_DATE; SEL
```

---

## Crash 158: `3fba74e45b962cda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123953`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (CURRENT_TIME / TRUE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 159: `f1166f170ca4ebae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125111`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE IN
```

---

## Crash 160: `b6a0076d6efbef2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128221`

```sql
SELECT printf('%f', -9223372036854775808, ''); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 161: `46cc2cf575b72711` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138625`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT X'c5'); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 162: `cbd34cc7bd0c6977` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138650`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME OR CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 163: `b0f183d426dbf951` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139829`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT X'EbA35e'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 164: `10a566f933fc13bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141936`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL); VA
```

---

## Crash 165: `6b2c2ba77d90b9c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142318`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL); VA
```

---

## Crash 166: `d569e41f18af4f74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142325`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL); VA
```

---

## Crash 167: `6fc147ca47b532c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142332`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (NULL); VA
```

---

## Crash 168: `f4a75b8a817f25a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142998`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); SELECT DISTINCT * FROM p LIMIT X'85a3' NOT IN (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INT
```

---

## Crash 169: `dd1332cd6c1637e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143149`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); SELECT DISTINCT * FROM p LIMIT CURRENT_TIME NOT IN (VALUES (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLAC
```

---

## Crash 170: `9a5a6bb85f77e055` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144326`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH q (a) AS (VALUES (TRUE)) SELECT *; INSERT INTO p D
```

---

## Crash 171: `4010dd19d928d773` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144705`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); VALUES (min(FALSE)); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 172: `67f968e12e293a6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (CURRENT_DATE) INTERS
```

---

## Crash 173: `f7511aa47fc92880` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146677`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (avg(TRUE) FILTER (WHERE CURRENT_TIMESTAMP), TRUE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 174: `96623037b01ed8d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146928`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); VALUES (group_concat(FALSE, '-dv_1-7-3 Z uvS-j') FILTER (WHERE CURRENT_TIMESTAMP) - NULL IS TRUE, TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 175: `1e4b38d07eb7853c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147632`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); VALUES (count(DISTINCT CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME) FILTER (WHERE CURRENT_TIMESTAMP)
```

---

## Crash 176: `f52daf809eda4ab5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148220`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT -2.3261); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 177: `d930bdac8d2d75b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148706`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CAST(CURRENT_TIME AS REAL) - TRUE - CURRENT_TIME AS xm__a_99g_kf2_r0 FROM p WHERE FALSE) AS sub1; SELECT printf('%.*f', -2147
```

---

## Crash 178: `5bf45edd0c91f96f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148922`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CASE CURRENT_TIMESTAMP << FALSE IS NOT NULL WHEN TRUE THEN CASE WHEN NOT FALSE THEN NULL ELSE TRUE END OR TRUE END & TRUE AS 
```

---

## Crash 179: `fce473024745b7fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148951`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CASE CURRENT_TIMESTAMP << CURRENT_TIMESTAMP WHEN TRUE THEN CASE WHEN NOT FALSE THEN NULL ELSE TRUE END OR TRUE END & TRUE AS 
```

---

## Crash 180: `0ccc026d79dee2ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149018`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT FALSE LIKE CURRENT_DATE ESCAPE NULL AS d5__zff2_14__2qfj___u23_j2yyu_7____1xbflw06dxi__895_hj4niy___6i FROM p WHERE FALSE) AS
```

---

## Crash 181: `c360975869587dce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150012`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME DESC ROWS BETWEEN CURRENT ROW AND CURRENT_TIME FOLLOWING) - CU
```

---

## Crash 182: `83959970f661a5e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150094`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
```

---

## Crash 183: `9a4ada7d6f23c4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150844`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT min(FALSE) FROM (SELECT * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES
```

---

## Crash 184: `2393e1457e668aef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151177`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT NULL COLLATE RTRIM AS xm__a_99g_kf2_r0 FROM p WHERE CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHEN CASE TRUE WHE
```

---

## Crash 185: `36bf4f94c3303fef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154005`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CURRENT_DATE NOT IN (8158689194399302995191849197550369.59E0), * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABL
```

---

## Crash 186: `7ee57af9d01d7003` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154048`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT TRUE, * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (c2)
```

---

## Crash 187: `c9409ed968d72c70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154056`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT CURRENT_DATE NOT IN (CURRENT_TIMESTAMP), * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 188: `f4509baa37d4109a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154471`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT count(*) OVER (), avg(CURRENT_DATE) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST, TRUE) AS h4___u___c9mu_e0s98_98__x41_9pj__7kz9dqv02qla__r0
```

---

## Crash 189: `8f5ae4625a1092f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154641`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT *, avg(CURRENT_DATE) OVER (ORDER BY CURRENT_DATE DESC NULLS FIRST, TRUE) AS h4___u___c9mu_e0s98_98__x41_9pj__7kz9dqv02qla__r0x_d16a0b_e0o_l0
```

---

## Crash 190: `4783fc2c767e528c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154652`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT count(*) OVER (), avg(CURRENT_DATE) OVER () AS h4___u___c9mu_e0s98_98__x41_9pj__7kz9dqv02qla__r0x_d16a0b_e0o_l0_1__r558bsp31pi0__998__16___y
```

---

## Crash 191: `4e95c9258d958294` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156551`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN CURRENT_DATE PRECEDING AND NULL FOLLOWING), * FROM p WHERE CURRENT_DATE
```

---

## Crash 192: `b315b58473f81a58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159005`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN PRIMARY KEY); SELECT * FROM (SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () AS o FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 193: `7ec7ddf7e33b4e70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160398`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIME AS REAL)); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 194: `bc061039821cce8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160465`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (CAST(CURRENT_TIME AS INTEGER)); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 195: `9e7205cde32b6d46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161028`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT OR IGNORE INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 196: `2662b823f8dc8b85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163449`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (-9338992037517287064530680820169.78e43697190676314611623712531311950861809
```

---

## Crash 197: `5c6a8757d2c54856` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163473`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL); INSERT INTO p VALUES (FALSE NOT IN (VALUES (NULL))); PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 198: `41b5f3e6de72a352` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164748`

```sql
SELECT printf('%.*f', 4294967296, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO t3 VALUES (+-CURRENT_TIMESTAMP OR total_changes() OVER () - (VALUES (NOT CURRE
```

---

## Crash 199: `f8c1946bd2175d32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169348`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT avg(CURRENT_DATE) OVER () FROM p WHERE EXISTS (VALUES (
```

---

## Crash 200: `dde21bf5545d515b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173180`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a) UNIQUE, c3 FLOAT UNIQUE); SELECT ALL avg(CURRENT_DATE) AS i4_9f FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 201: `33b4f3ea2e71358e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173411`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a) UNIQUE, c3 FLOAT UNIQUE); SELECT ALL CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURR
```

---

## Crash 202: `d88846931ec004b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173937`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a) UNIQUE, c3 FLOAT UNIQUE); SELECT ALL nullif(FALSE, FALSE) AS i4_9f FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 203: `fc93e9401adba21e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174162`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE, c1 GENERATED ALWAYS AS (a) UNIQUE, c3 FLOAT UNIQUE); SELECT ALL nullif(NULL, FALSE) AS i4_9f FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 204: `f0b43475b6418fb1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175955`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); SELECT DISTINCT * FROM p CROSS JOIN (VALUES (FALSE)) AS c443y_ttkb4i3_ NATURAL JOIN p WHERE CURRENT_D
```

---

## Crash 205: `2ba683bd5d457754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181512`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (random()); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c1 BLOB, a GENERATED ALWAYS AS (a) NOT NUL
```

---

## Crash 206: `7b9009cc3804efd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183795`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LEFT JOIN p AS h_3ikn_9_12zk5d4q_09t7__k_0y0_c_
```

---

## Crash 207: `5d51b4f74d6a4286` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185028`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY, rowid BLOB); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q AS r3_1 LEFT JOIN p NOT INDEXED , q 
```

---

## Crash 208: `8521940faaaae54d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186232`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED INNER JOIN q NOT INDEXED NATURAL JO
```

---

## Crash 209: `52164fce6529e55f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186290`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED INNER JOIN (VALUES (FALSE)) AS c443
```

---

## Crash 210: `a4723c597a7a6e2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186540`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN (VALUES (FALSE)) 
```

---

## Crash 211: `1660c85d0d6e7b91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189243`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 212: `732a7efb8613238c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189274`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 213: `f83a3472112c7ee8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189427`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXIST
```

---

## Crash 214: `21aed8b260a37519` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189453`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 215: `57dcec1ce1f5ec84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190309`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); IN
```

---

## Crash 216: `d8710bdb7e9a6205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191094`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB GENERATED ALWAYS AS (NULL) VIRTUAL, a REAL UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 217: `8705cf1005705ef0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192118`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); INSERT OR REPLACE INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN p)); PRAGMA integr
```

---

## Crash 218: `8f614d914b1e1b04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192841`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); INSERT OR ROLLBACK INTO p VALUES (TRUE | CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT t1.*, 
```

---

## Crash 219: `9f967b05050b1586` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194435`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (TRUE NOT IN (VALUES (group_concat(CURRENT_DATE, '_ --_H-C_ _4'
```

---

## Crash 220: `9ca313086071d285` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (TRUE NOT IN (VALUES (CAST(FALSE AS REAL))), TRUE) ON CONFLICT 
```

---

## Crash 221: `b11a77e6ad0d114b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194780`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (NOT EXISTS (VALUES (max(CURRENT_TIMESTAMP)) INTERSECT VALUES (
```

---

## Crash 222: `59a6e58abd62a919` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194975`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (NOT EXISTS (VALUES (total_changes()) INTERSECT VALUES (FALSE))
```

---

## Crash 223: `06c2cd1687db1864` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195231`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (TRUE NOT IN (VALUES (CAST(CURRENT_DATE AS REAL))), TRUE) ON CO
```

---

## Crash 224: `ab31e766a3b1497c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198470`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a + 0) NOT NULL UNIQUE); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 225: `a9c6f56da0a13129` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198763`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT count(*) OVER (), count(*) OVER (ORDER BY CURRENT_DATE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS), * FROM p JOIN p k_910_300__
```

---

## Crash 226: `6fc884359157f9c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199204`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY, rowid BLOB); SELECT count(*) OVER (), * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3,
```

---

## Crash 227: `f3dcc4e1f058a179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201106`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON json_extract(NULL || TRUE, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT TRUE == NU
```

---

## Crash 228: `9a7e96d72d47a3e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201166`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT TRUE == NULL AS n9_ F
```

---

## Crash 229: `9e427f72d7b9b38c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202302`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_TIMESTAMP IS NULL OR NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 230: `e2e687de88ec0321` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202462`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE OR NULL; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 231: `e53737a93e4f5beb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202545`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE NOT IN (VALUES (TRUE)) OR CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 232: `3adcf04a51928767` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202654`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON NULL OR CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 233: `1874550f1d67e674` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203261`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT 2.73536388864846552001717228e+20073859017138970468889648140620834987298173931015435374599449715491282412812866439193855748890872277819702114026623
```

---

## Crash 234: `1d84ab999baf933d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203867`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_TIME OR TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT 
```

---

## Crash 235: `0083e51fd399c5f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205321`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE > CURRENT_TIME; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 236: `f865391fc54f9d7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205489`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE NOT BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 237: `136e3341a7908db9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206019`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_TIMESTAMP IS NOT TRUE IS NOT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 238: `a994f2f87e8ac112` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206533`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON NOT EXISTS (VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT DISTINCT * FROM (VALUES (CURRENT_TIMESTAMP) INTERSE
```

---

## Crash 239: `9f986762ccced749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207074`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT -605324953342720233379975760066442489714561896708818597699514056638355825571033177361811239630111765097515551587570784281.2733e76); CREATE TABLE I
```

---

## Crash 240: `e400597ef96f319c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207795`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP BETWEEN CURRENT_DATE AND CURRENT_DATE; C
```

---

## Crash 241: `ce6eca4dce216274` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208904`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME IS NOT c1; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 242: `1fea1051b046b65e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210514`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT 
```

---

## Crash 243: `1d34b7f880a764c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212479`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT count(*) OVER (ORDER BY -940743408592835703971490864663049554965050775818821802696042249199
```

---

## Crash 244: `dda2015a6bb1f46f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212874`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT count(*) OVER (), EXISTS (VALUES (RAISE(IGNORE))) AS a FROM p NATURAL JOIN q WHERE CURRENT_
```

---

## Crash 245: `f990e5d9fab495aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215129`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT *, *, count(*) OVER () AS xm__a_99g_kf2_r0 FROM 
```

---

## Crash 246: `e9faec29aeaf1b08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219609`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIMESTAMP FROM p LEFT OUTER JOIN p NOT I
```

---

## Crash 247: `5551f687e2599a83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220738`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN PRIMARY KEY, a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY CURRENT_DATE DE
```

---

## Crash 248: `6f8c0cb30978d8f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221082`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY NULL ORDER BY C
```

---

## Crash 249: `384d8922fd457b75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221363`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY NULL ORDER BY C
```

---

## Crash 250: `45d6ccd3d160c147` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221516`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY NULL ORDER BY N
```

---

## Crash 251: `5b1a5a3bba80b316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227367`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT, c3 GENERATED ALWAYS AS (a = 79945) NOT NULL UNIQUE, a BLOB UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 252: `8fca19be70eb6fb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232139`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB, c2 GENERATED ALWAYS AS (a) NOT NULL, a BLOB NOT NULL DEFAULT CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 253: `f3d677a9529c839b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232483`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (CURRENT_TIME AND CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME *
```

---

## Crash 254: `16972d60a6ed39c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232555`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (CURRENT_TIME AND CURRENT_TIME / FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE 
```

---

## Crash 255: `9ad8a81674085e66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232733`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (NULL - NULL >> CURRENT_TIMESTAMP GLOB TRUE IS NULL AND CURRENT_DATE / FALSE); PRA
```

---

## Crash 256: `c38d690c77c6da2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237869`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURRENT_TIMESTA
```

---

## Crash 257: `2ee5bbf3614533d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239220`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p LIMIT 'z3' NOT IN (VALUES ('z3' NOT IN 
```

---

## Crash 258: `f69ecf0d532e92eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242262`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT NULL NOT LIKE count(*) FILTER (WHERE FALSE) AS x
```

---

## Crash 259: `7cc291813c1b9e69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244792`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE % TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 260: `bf604b26132f0524` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247356`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p N
```

---

## Crash 261: `59baed4272bf4a67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247631`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p 
```

---

## Crash 262: `435769a056cfa400` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247657`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p 
```

---

## Crash 263: `149f5413931f2c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249407`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); SELECT char(FALSE) NOT LIKE CURRENT_TIME AS a, * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP;
```

---

## Crash 264: `9c48ff674a06f263` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249537`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) UNIQUE); SELECT TRUE NOT LIKE CURRENT_TIME AS a, * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; SELECT
```

---

## Crash 265: `6bb9127947731aab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251888`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE IN (VALUES (count(*) OVER (PARTITION BY (SELECT DISTINCT * FROM p ORDER BY CURRENT_DATE DESC NULLS LA
```

---

## Crash 266: `8223c2155cfb083b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252267`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_TIME OR CURRENT_TIME OR CURRENT_TIME OR RAISE(IGNORE) OR CURRENT_TIME OR TRUE OR CURRENT_TIMESTAMP 
```

---

## Crash 267: `29efa1f77768b4c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252360`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON FALSE OR NULL OR FALSE OR CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 268: `a1ace4a17f24dccf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253399`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON NULL IS NULL | FALSE OR CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 269: `588bdc9574a1a61f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253521`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON CURRENT_DATE == CURRENT_TIME OR CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, 
```

---

## Crash 270: `912d9131e85d5ffc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256732`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT CASE WHEN CURRENT_TIME NOT BETWEEN CURRENT_DATE AND FALSE THEN FALSE END - TRUE AS l FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE; CREATE VIRTUAL TAB
```

---

## Crash 271: `31f3fb2e42f58e6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257035`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); SELECT max(NULL) OVER (), NULL IN (SELECT * FROM p), * FROM p JOIN p k_910_300__ixx64_0yer_od__05 ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 272: `b2cb025491b3d48a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257959`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE) UNION VALUES (CAST(CURRENT_DATE == CURRENT_TIMESTAMP AS REAL)); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 273: `8bc10e0cc23b8ddc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259068`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p UNION VALUES (group_concat(CURRENT_TIMESTAMP, '-dv_1-7-3 Z uvS-j') FILTER (WHERE FALSE
```

---

## Crash 274: `403774010481db38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261101`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL, c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (CAST(CURRENT_TIME AS BLOB) NOT IN (VALUES (TRUE)), TRUE) ON CO
```

---

## Crash 275: `edc17a8a0fa96b3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262662`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (rowid)); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647,
```

---

## Crash 276: `3c44861c7782a0dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262758`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT CHECK (CURRENT_TIMESTAMP)); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g',
```

---

## Crash 277: `d582f350a19f8ecc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266962`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIM
```

---

## Crash 278: `f7df661309bc447c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267268`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid INTEGER NOT NULL, c3 DATE, a BOOLEAN, _rowid_ VARCHAR(255)); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED WH
```

---

## Crash 279: `40217ea4b4ea810d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000269829`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED CROSS JOIN (VALUES (CURRENT_TIMESTA
```

---

## Crash 280: `078c7da5a49eb44c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000273950`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (json_array(TRUE, CURRENT_TIME)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 281: `1e93341b7456de42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274859`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(CURRENT_TIME, substr(~CURRENT_DATE, FALSE, CURRENT_DATE), CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); S
```

---

## Crash 282: `145aad7c298276f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274899`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(CURRENT_TIME, CURRENT_TIMESTAMP, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); SELECT printf('%.*g', 2147
```

---

## Crash 283: `14b4f95ca9b87e6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000274918`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (zeroblob(NULL)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (
```

---

## Crash 284: `61c04a6fb4a5a15a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275171`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(zeroblob(NULL), FALSE, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 285: `580ae43ea23d03ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275364`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(TRUE, FALSE, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 286: `939fb50b7ed51966` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000275370`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (substr(last_insert_rowid(), FALSE, CURRENT_DATE)); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXI
```

---
