# Crash Triage Report

**Total crashes:** 55  
**Unique crash sites:** 55  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 55 | 55 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `7c382516507d9aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000127`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r VALUES (+count(CURRENT_TIME IS NOT DISTINCT FROM CURRENT_TIMESTAMP + FALSE MATCH CURRENT_TIME COLLATE NOCASE << FALSE OR CURRENT
```

---

## Crash 2: `bc5cf07b8ef2fb60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000319`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); INSERT OR FAIL INTO t2 VALUES (FALSE ISNULL & (SELECT *) | (TRUE) LIKE CURRENT_TIMESTAMP OR (FALSE) = CURRENT_TIMESTAMP REGEXP TRUE CO
```

---

## Crash 3: `b988187cec456c4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000533`

```sql
SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s (_rowid_, c3, _rowid_) VALUES (CURRENT_TIMESTAMP >> TRUE ISNULL IS NULL IS CURRENT_TIME IS NU
```

---

## Crash 4: `942a23efdfbe8e81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000777`

```sql
SELECT printf('%f', 9223372036854775807, '7-f_35_---g8U-Q '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t3 VALUES (CURRENT_TIMESTAMP LIKE (CURRENT_DATE <> row_number() * CUR
```

---

## Crash 5: `cce7425ae6a8029a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001241`

```sql
SELECT printf('%.*e', 4294967296); SELECT substr(' m_j-', -2147483649, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_, c2); SELECT FALSE FROM t1 INTERSECT SELECT FALSE NOT NULL GL
```

---

## Crash 6: `bc5e38a2b10c01c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001326`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, _rowid_); INSERT INTO s VALUES (TRUE) UNION ALL SELECT percent_rank() FILTER (WHERE TRUE) COLLATE BINARY ISNULL AS a; ANALYZE t3; CREA
```

---

## Crash 7: `d566836b3b054355` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001447`

```sql
SELECT printf('%x', -2147483648, '-Nv _7-j_E_  _'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c1); INSERT OR ROLLBACK INTO t2 VALUES (NULL NOT LIKE random(), CURRENT_DATE COLLATE BINA
```

---

## Crash 8: `ca7fa94ae9ef7ef8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001584`

```sql
SELECT substr('j_3_-- -  i 3 ft0_8', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT *, CAST(+CURRENT_DATE NOTNULL NOT NULL >> RAISE(IGNORE) LIKE CURRENT_DATE ->>
```

---

## Crash 9: `cdd961f5f3d929db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001711`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE t3 AS NOT MATERIALIZED (WITH r (a, b, c3) AS (SELECT TRUE ISNULL IN (FALSE) AS h3_6n0_o0rfg9__9nm5__w23
```

---

## Crash 10: `74b898a1afbf431e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001854`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1);
```

---

## Crash 11: `0f5c2eb7dccf5fb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001861`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NOT CURRENT_TIMESTAMP); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 12: `aca2f0a4b6ccb2f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001868`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NOT CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME END); ANALYZE p; CREATE VIRTU
```

---

## Crash 13: `0f9afea93a367fa9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001898`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (TRUE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); 
```

---

## Crash 14: `07450c42ca226d5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001905`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NOT TRUE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c
```

---

## Crash 15: `e3cb5e74e2db3777` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001911`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NOT CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME END); PRAGMA integrity_check;
```

---

## Crash 16: `bece9c582f263040` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001944`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); SELECT min(upper(CURRENT_DATE) <= NULL <= TRUE IS CURRENT_TIMESTAMP) FILTER (WHERE CASE WHEN CU
```

---

## Crash 17: `8e83956f0c9b2034` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001951`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 18: `afa3fdbd054ef756` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001958`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 19: `b0edec0b5d136707` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002011`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NOT TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 20: `7bd8e848c50b8127` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002030`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 21: `60b9b67a7550fc11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002974`

```sql
SELECT hex(zeroblob(0)); SELECT round(1e-308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME || FALSE NOTNULL NOT IN (TRUE) REGEXP CURRENT_TIME * TRUE IS N
```

---

## Crash 22: `578cd1aaa2ba33f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004872`

```sql
SELECT substr('', 2147483648); CREATE TABLE IF NOT EXISTS p(rowid TEXT, c1 GENERATED ALWAYS AS (a = -6) UNIQUE, a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL T
```

---

## Crash 23: `2865d5d3a4775cdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004890`

```sql
SELECT substr('', 2147483648); CREATE TABLE IF NOT EXISTS p(rowid TEXT, c1 GENERATED ALWAYS AS (a = -6) UNIQUE, a NUMERIC UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL); CREAT
```

---

## Crash 24: `3c1dbde33dfbf5d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006431`

```sql
SELECT round(1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO p SELECT NULL AS o_2j_5_l40_3__h_24h____2d_2n_k5__12d8__me__r1iq_x8_j6a7_l__w2y4s__2_0ck8i88n
```

---

## Crash 25: `36c12220d79ffaa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006488`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE r AS NOT MATERIALIZED (SELECT DISTINCT s.* FROM ((q NOT INDEXED LEFT OUTER JOIN ((VALUES (TR
```

---

## Crash 26: `5db37b05bd21fc04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006517`

```sql
SELECT printf('%.*d', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c1); WITH RECURSIVE r AS NOT MATERIALIZED (SELECT s.* INTERSECT SELECT DISTINCT CASE CURRENT_TIMESTAMP ->
```

---

## Crash 27: `433c637efcd89e8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006922`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO t3 VALUES (NULL NOTNULL LIKE (SELECT ALL * FROM p NOT INDEXED LIMIT CAST(CURRENT_TIME AS
```

---

## Crash 28: `97ef3c0c7b5d8f41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007097`

```sql
SELECT printf('%s', 4294967295, '_J--F h93Zcr '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE p (c3, rowid, _rowid_, c3, c2, c2) AS NOT 
```

---

## Crash 29: `0fdb9547ab2ae582` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007132`

```sql
SELECT printf('%.*e', 4294967296, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2); INSERT INTO s DEFAULT VALUES; SELECT CASE WHEN +NOT (TRUE REGEXP CURRENT_TIMESTAMP) IS NOT NU
```

---

## Crash 30: `9e275189291823d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010829`

```sql
SELECT round(0.0, 4294967296); SELECT printf('%.*f', 2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, b, c3); VALUES (RAISE(IGNORE));
```

---

## Crash 31: `97e4dacb40d8b328` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010897`

```sql
SELECT round(0.0, 4294967296); SELECT printf('%.*f', 2147483647, 1e308); CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (FALSE == substr(CURRENT_TIME > CURRENT_TIME, CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP
```

---

## Crash 32: `209e5d2bded5ef82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016068`

```sql
SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO t2 VALUES (+RAISE(IGNORE) NOT NULL IS +RAISE(IGNORE) COLLATE RTRIM ->> randomblob(CURRENT_DATE 
```

---

## Crash 33: `d368980a37f365c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016199`

```sql
SELECT substr('', 9223372036854775807); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 34: `5e40547e300f69de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016730`

```sql
SELECT printf('%f', -9223372036854775808, '-__bD36- _ q91w'); SELECT substr('s  80S e9p-Sj', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CURRENT_DATE) INTERSECT SELECT * ORDER
```

---

## Crash 35: `ecb00ee3113e5f83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025481`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT ALL CASE NUL
```

---

## Crash 36: `2f703c95c18b59cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025549`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 37: `04bd69f6963ba350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025977`

```sql
SELECT printf('%.*g', 0, 1e308); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 38: `045d7f735a143bdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026963`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, b AS(b) NOT NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT INTO t3 (c2) VALUES (RAISE(IGNORE) IN (SELECT * ORDER BY TRU
```

---

## Crash 39: `203a8f7f8a950af2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027470`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 40: `dfe784d04d1c0948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027885`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE, b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 214
```

---

## Crash 41: `211a44134a3cd0dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032465`

```sql
SELECT printf('%.*d', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT ~FALSE COLLATE NOCASE AS a, FALSE, NULL AS a FROM r NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS NO
```

---

## Crash 42: `b094a9ab9ce59dfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039126`

```sql
SELECT printf('%.*f', -9223372036854775808, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, c1, c3); SELECT CAST(NULL & NULL / RAISE(IGNORE) IS NOT DISTINCT FROM TRUE AS REAL) 
```

---

## Crash 43: `0eb7d0b123c74d58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039147`

```sql
SELECT substr('', 1, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); INSERT OR FAIL INTO s VALUES (group_concat(RAISE(IGNORE) IS NULL IS RAISE(IGNORE) || NULL) FILTER (W
```

---

## Crash 44: `8ee7edde51f702b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039217`

```sql
SELECT substr('', 4294967296); SELECT printf('%.*d', -9223372036854775808, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3, _rowid_, c2); INSERT INTO r VALUES (NOT CURRENT_TIM
```

---

## Crash 45: `c2f8dc3840e1d107` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039301`

```sql
SELECT substr('', -2147483648, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, b, c3); SELECT DISTINCT *, FALSE FROM s NOT INDEXED NATURAL LEFT JOIN s NOT INDEXED UNION SELEC
```

---

## Crash 46: `58a7132ce700d5f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039743`

```sql
SELECT printf('%.*f', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, a, c2); INSERT INTO r (b) VALUES (CURRENT_TIMESTAMP ISNULL, TRUE); WITH RECURSIVE t1 AS MATERIALIZED (SELECT * ORD
```

---

## Crash 47: `7ef125bd346b7a53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046351`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, b AS(b) UNIQUE); VALUES (-CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM s WHER
```

---

## Crash 48: `f2915fbcdef121a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046676`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP IN (SELECT -1060.98E00006551781570016079817719726768398412761
```

---

## Crash 49: `f7c70de0d1c8d783` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047255`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_DATE))); PRAGMA quick_check; SELECT print
```

---

## Crash 50: `de782093f1e96a5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047449`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIMESTAMP COLLATE BINARY))); PRAGMA quick
```

---

## Crash 51: `5d3bc098cc397be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047498`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIME))); PRAGMA quick_check; CREATE VIRTU
```

---

## Crash 52: `3b536ca1ddb9d4af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047504`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIMESTAMP IN (VALUES (FALSE))); PRAGMA quick_check; CREATE VIRTUAL TABL
```

---

## Crash 53: `66cc3e07a1c8c3eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048723`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB NOT NULL DEFAULT 03815.6E12, _rowid_ VARCHAR(255) DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA quick_chec
```

---

## Crash 54: `7e2d94dcad47839a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049543`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT NOT NULL DEFAULT X'F5ABc68Aad1a1F'); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 2
```

---

## Crash 55: `0fa1a22f074490f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049715`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT NOT NULL DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL); REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*f', 214748
```

---
