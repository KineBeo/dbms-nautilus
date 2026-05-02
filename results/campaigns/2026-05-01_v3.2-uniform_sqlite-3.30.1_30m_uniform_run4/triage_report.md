# Crash Triage Report

**Total crashes:** 322  
**Unique crash sites:** 321  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 311 | 311 | 96% |
| Signal | 10 | 11 | 3% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `4a897df9e000b652` — signal (signal-6)

- **Count:** 2 duplicates
- **Exit code:** -6
- **Sample file:** `6_000112865`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE NOCASE))); CREATE V
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  sqlite3ExprDeleteNN
  sqlite3ExprDelete
```

---

## Crash 2: `7a10c3ee30e211e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000068`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CASE WHEN NULL THEN CURRENT_DATE - TRUE ELSE ~CURRENT_TIMESTAMP END == NOT CURRENT_TIME IS NOT DISTINCT FROM RAISE(IGNORE) AS o_, t2.* 
```

---

## Crash 3: `cbe89c5c406abd08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000105`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT t1.*, NULL FROM s NATURAL JOIN q WHERE CURRENT_TIME & TRUE COLLATE NOCASE << CURRENT_DATE AND NULL IN (CURRENT_TIMESTAMP) NOTNULL IS NOT
```

---

## Crash 4: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000144`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 5: `5fa9692bcbac9ca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000487`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a, b, c1, c1); INSERT OR REPLACE INTO p VALUES (p.a NOTNULL NOTNULL LIKE CURRENT_TIMESTAMP <= CURRENT_DATE <> NULL >= (CURRENT_TIME) OR NOT EXI
```

---

## Crash 6: `6124482107bd83d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000844`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT r.*, *, q.*, *, r.*, r.*, t1.* FROM p JOIN t1 d_2_5p351y_9q3chsh43__y___m5_y ON CAST(NOT CU
```

---

## Crash 7: `96c08b0b27c37df5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000883`

```sql
SELECT printf('%.*g', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 BLOB DEFAULT FALSE, c2 NUMERIC, c3
```

---

## Crash 8: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001105`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 9: `74434782c59c48c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001510`

```sql
SELECT substr('', -2147483649); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); EXPLAIN QUERY PLAN WITH q AS (SELECT * FROM q JOIN q INDEXED BY c2 LEFT OUTER J
```

---

## Crash 10: `0cfd50a7dedbd656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001564`

```sql
SELECT printf('%.*g', 2147483647, 0.01); SELECT substr('n', -2147483648); CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT 'u', c2 DATE UNIQUE, c2 INT DEFAULT TRUE, c1 VARCHAR(255) PRIMARY KEY, c
```

---

## Crash 11: `36c8982b6289bfea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002366`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 12: `4371475681b7d195` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002400`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 13: `50f36cf7de82c68a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002463`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 14: `cde9630f0ec34730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002498`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 15: `01b027a18cdf06a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003649`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO r (c3, c3, rowid, _rowid_) VALUES (~CASE WHEN RAISE(
```

---

## Crash 16: `01ff64edad6569a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003986`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; S
```

---

## Crash 17: `a29b59acb560a0fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004004`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO t3 VALUES (CASE WHEN (CURRENT_TIME) THEN CURRENT_TIMESTAMP NOT IN (CURRENT_DATE) - ~CURRENT_TIMESTAMP CO
```

---

## Crash 18: `941c7c9d74ee2507` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004011`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO t3 VALUES (CASE 
```

---

## Crash 19: `9fb45dfffa45f44d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006067`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH REC
```

---

## Crash 20: `9f92254dff40fd8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006282`

```sql
SELECT printf('%.*e', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO q VALUES (FALSE <> TRUE >> random() IS NOT NULL MATCH json(~TRUE AND TRUE
```

---

## Crash 21: `5c8284369ec639a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006825`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 22: `6c3a8cbe6c75456e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007258`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM (SELECT * FROM q WHERE NULL) AS sub1; CREATE TABLE IF NOT EXISTS p(c3 INTEGER, a GENERATED ALWAYS AS (coal
```

---

## Crash 23: `7aebcd9edbfbaa44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007544`

```sql
SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 BLOB, c1 GENERATED ALW
```

---

## Crash 24: `0ccff82c192cd291` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007727`

```sql
SELECT substr('w3xl', 4294967296, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c2) VALUES (RAISE(IGNORE)) ON CONFLICT(b) DO UPDATE SET _rowid_ = ~FALS
```

---

## Crash 25: `8a382349dca1f920` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008028`

```sql
SELECT printf('%.*g', 4294967295, 0.01); SELECT printf('%.*e', -1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO q VALUES (~CAST(+CURRENT_TIMESTAMP COLLATE BI
```

---

## Crash 26: `c0ed8e6c48c07166` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009095`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); S
```

---

## Crash 27: `5b601fe914a90d8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010720`

```sql
SELECT round(0.01, 2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 28: `815579c559a831d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011927`

```sql
SELECT round(1e308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO t3 VALUES ((+NULL COLLATE BINARY % length(+CURRENT_TIMESTAMP LIKE TRUE NOT N
```

---

## Crash 29: `0e0e6b76a0abaaa5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012542`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, 
```

---

## Crash 30: `19820dfbaa45d96f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013452`

```sql
SELECT substr('_VN', 2147483647, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO t2 VALUES (+CAST(CAST(FALSE AS FLOAT) AND CURRENT_TIMESTAMP AS BLOB), q.c3) RE
```

---

## Crash 31: `3ebe3c57fded8ab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018085`

```sql
SELECT printf('%.*g', -2147483648, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2); INSERT INTO p SELECT zeroblob(NULL) FILTER (WHERE changes() OVER (PARTITION BY +CURRENT_TIM
```

---

## Crash 32: `3255cea4a84b5f73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019067`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c2); INSERT INTO r DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 33: `91d0655238367bed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019073`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2); INSERT INT
```

---

## Crash 34: `3b23b40af3f7d432` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019082`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3,
```

---

## Crash 35: `5e273b123b7fd978` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021989`

```sql
SELECT round(-1e308, -9223372036854775808); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 36: `315e931ee3680917` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024861`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (TRUE | TRUE); VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 37: `a2274f33e884e463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025111`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 38: `9943943323fcb29e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025232`

```sql
SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); VALUES (NULL); CREATE TAB
```

---

## Crash 39: `dae0c0a12417aa3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025762`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE || CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 40: `56241611c0b2d2f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027166`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE << CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 41: `b0994bb6654dc9a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027446`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE OR CURRENT_DATE = CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 42: `c721fefd327a4516` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027700`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p SELEC
```

---

## Crash 43: `10a5eca37789eb79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027893`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (VALUES (NULL)) AS a LIMIT FALSE, CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; 
```

---

## Crash 44: `0a9d1bac01fa1918` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027983`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT substr('', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 45: `c1f34ab5f41bb5df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027993`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT FALSE, CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT 
```

---

## Crash 46: `23414594fbafe5dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028182`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE OR CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, 
```

---

## Crash 47: `f5b438de82a1c356` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028376`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIME))) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 48: `eec7275dbc134536` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028519`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p NOT INDEXED LIMIT FALSE)) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f', -21
```

---

## Crash 49: `559a623b53b4d337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028769`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p LIMIT CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 50: `cfbf0831d6b8c115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029086`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p LIMIT CURRENT_DATE, FALSE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 51: `419ef393b26a70b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029252`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME > CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 52: `60e080da24987361` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031160`

```sql
SELECT printf('%x', 4294967296, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); VALUES (NULL); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 53: `709e68a93b1e6ae4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031202`

```sql
SELECT printf('%x', 4294967296, ''); SELECT substr('QP9--lC5 FbINPw', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); INSERT INTO q VALUES (gro
```

---

## Crash 54: `fd0c046ad4cb70b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT OR IGNORE INTO p VALUES (NOT CURRENT_TIMESTAMP); PRAGMA integrity_check; SELECT printf('%.*f', -2147483
```

---

## Crash 55: `c89f829d4df5cf80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033585`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 56: `cb0d7d663772ee03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033883`

```sql
SELECT printf('%f', 2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO q VALUES (CURRENT_DATE); VALUES (NULL);
```

---

## Crash 57: `9293f2faf3767eda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036840`

```sql
SELECT printf('%d', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT CURRENT_TIME AS w2__i8__627lyob_b_2c_8e0_nk_4712_agla_dc0_5tp41013__u___5_2pt0, NULL << T
```

---

## Crash 58: `a55199618115caad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040097`

```sql
SELECT round(0.0, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO t1 VALUES (+CURRENT_DATE IS NOT DISTINCT FROM CURRENT_TIME -> (CURRENT_DATE) IN (SELECT ALL q.* FRO
```

---

## Crash 59: `0e81b073af0b72fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040197`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA quick_check; SELECT substr('EB--p ', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 60: `1c2ee9b6b217e68e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041297`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARC
```

---

## Crash 61: `a531c0acc2361656` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041309`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 VARC
```

---

## Crash 62: `6caf28867b06ee19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041426`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABL
```

---

## Crash 63: `f589b5e2687ac445` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041436`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABL
```

---

## Crash 64: `500a536b2e8db927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041538`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 65: `74bfdc31ea461ed8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041554`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT -98.17347049468); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 66: `6ddda4cd96370e8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041574`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.0
```

---

## Crash 67: `a2bfb7b76c32648b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043567`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL) AS sub1; SELECT print
```

---

## Crash 68: `5a8e1bfbac9a67c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044019`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME GLOB TRUE) AS 
```

---

## Crash 69: `a64ede85a47d023a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044097`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 70: `cbd80595084f19c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044479`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS NOT NU
```

---

## Crash 71: `c75d6a9e646aec66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045239`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT NULL LIKE TRUE IS NOT N
```

---

## Crash 72: `7d951d867314b504` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045789`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE ~CURRENT_TIMESTAMP) AS sub1
```

---

## Crash 73: `4be15ecceac67390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045950`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE VIRTU
```

---

## Crash 74: `fdb08816d590b723` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046123`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE FALSE NOT IN (VALUES (+FALS
```

---

## Crash 75: `fc3ecc7057f00381` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046393`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE VIRT
```

---

## Crash 76: `252c28e9b170f69f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046973`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1;
```

---

## Crash 77: `392ac92eddfe3b85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048707`

```sql
SELECT printf('%.*d', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT *;
```

---

## Crash 78: `64d7dedae072d5e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050871`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN NOT NULL DEFAULT -60260054.3); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TAB
```

---

## Crash 79: `5a9c68dc8d3ffd8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051062`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT NOT NULL DEFAULT X'27F8F0D1', a TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE V
```

---

## Crash 80: `1de1ce3f38fbbcac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051247`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY, a TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TAB
```

---

## Crash 81: `0c010963f316f4dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051253`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INT NOT NULL DEFAULT CURRENT_TIME, a TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREATE 
```

---

## Crash 82: `920efc4c4e311db3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051413`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CAST(X'aA4cEBBd' AS TEXT)) 
```

---

## Crash 83: `200d639c6d9d91c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051648`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT NULL COLLATE BINARY AS sl_e4_pl_3w2 FROM p
```

---

## Crash 84: `0580f69f8e541ea5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051822`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT CURRENT_TIME AS sl_e4_pl_3w2 FROM p WHERE 
```

---

## Crash 85: `9184830bbf7bcd74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051956`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT NULL COLLATE BINARY >= CURRENT_TIMESTAMP A
```

---

## Crash 86: `cc8f91a12458e90a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052092`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE (SELECT * FROM p NOT INDEXE
```

---

## Crash 87: `1771662dd0507e05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052553`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 88: `4c77725310d7500d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052765`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP NOT IN (S
```

---

## Crash 89: `601fedd5ac202368` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053945`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE X'aA4cEBBd' GLOB TRUE) AS s
```

---

## Crash 90: `b9d731684203937d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054339`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS NOT NU
```

---

## Crash 91: `1bcb376ad62cdf95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054623`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NULL GLOB TRUE NOT IN (VALU
```

---

## Crash 92: `7fe744a4fde5d073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054669`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (SELECT
```

---

## Crash 93: `1ad323c8da2fd5cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055305`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 94: `caa3313369113004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055693`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 95: `4c4a3dec09c7d022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056087`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT count(*) FROM p WHERE TRUE) AS sub1; SELEC
```

---

## Crash 96: `672487b5137a226b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058742`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p SELECT DISTINCT * FROM q NOT INDEXED; PRAGMA integrity_check; SELECT printf('
```

---

## Crash 97: `fde4522ca9e96104` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058895`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e3
```

---

## Crash 98: `af9aaf9bfa57aea7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059599`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT -98.17347049468); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (CURRENT_TIME) EXCEPT VALUES (CURRENT_DATE); PRAGMA integrity_ch
```

---

## Crash 99: `e604086fffd3942c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059628`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT X'CeBB6C67F2dA'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 100: `995dfb6c90165043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059641`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 101: `11026b6ddb5f2172` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059910`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES (CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DA
```

---

## Crash 102: `332ce8c5907b2dcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060530`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (random())); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*f', -21474836
```

---

## Crash 103: `a921e22517122187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060969`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (quote(CURRENT_TIME NOT NULL))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRT
```

---

## Crash 104: `af8a4f5149f58d8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066063`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN); SELECT CURRENT_TIME >> EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRE
```

---

## Crash 105: `9a8f5b9ab2d6a37a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068701`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CAST(NULL NOT BETWEEN CURRENT_DATE AND EXISTS (VALUES (TRU
```

---

## Crash 106: `3f60191ddc702cd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071734`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT NOT NULL DEFAULT X'BFeD'); INSERT OR IGNORE INTO p VALUES (NOT CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE V
```

---

## Crash 107: `f2ca2472c224abc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075807`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE NOCASE UNION 
```

---

## Crash 108: `2b3c142a523947a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO r DEFAULT VALUES; PRAGMA quick_check;
```

---

## Crash 109: `e10a7615ac2f1c14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076235`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 110: `222b40b95a086571` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076264`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT -379); CREATE INDEX IF NOT EXISTS idx1 ON p(b); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 111: `06e330a8a03e56e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077535`

```sql
SELECT printf('%s', 1, '1_Ft-22- 2Q'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEFAULT VALUES; SELECT * FROM q JOIN q s50_i_9_k ON CURRENT_DATE COLLATE BINARY; CREATE TA
```

---

## Crash 112: `cfdf71d62aaf4979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077976`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p (rowid) VALUES (CURRENT_DATE); WITH RECURSIVE r AS (SELECT *) SELECT count(*) 
```

---

## Crash 113: `2723aa10c26986de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078200`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE, rowid BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p (rowid) VALUES (CURRENT_DATE); VALUES (TRUE) EXCEPT SELECT * 
```

---

## Crash 114: `330c096cc183c270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079570`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED GROUP BY FALSE)) ON CONFLICT DO NOTHING; PRAGMA integrity_ch
```

---

## Crash 115: `f706d753d6c7d9d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079860`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED NATURAL JOIN p GROUP BY FALSE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE 
```

---

## Crash 116: `75564e3fe3a685f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p JOIN p JOIN p LIMIT CURRENT_TIMESTAMP OFFSET EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT I
```

---

## Crash 117: `81a953debdd7a150` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080975`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (FALSE * FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR R
```

---

## Crash 118: `dab12679edd6812b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p LIMIT CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 119: `6a009c1c487bb537` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083914`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CAST(CURRENT_TIMESTAMP AS INT) = CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 120: `5c1429df85547705` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084097`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NULL = CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSE
```

---

## Crash 121: `814a6c0233d09d3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084191`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME OR CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 122: `5d84a35921cb5df0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (-FALSE) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 123: `4c34ebcc1c0ef634` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084738`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(NULL)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK IN
```

---

## Crash 124: `e4142a907b857fd7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084895`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (random()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO
```

---

## Crash 125: `71896da6b1611a60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084949`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(last_insert_rowid())); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT
```

---

## Crash 126: `6b743ca8fe42ca0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086072`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE ||
```

---

## Crash 127: `fce707212ca17f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086336`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NULL || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VI
```

---

## Crash 128: `c1d9dcf5e5e30dda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086593`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT ALL * FROM (VALUES (NULL)) AS a LIMIT CURRENT_TIMESTAMP OFFSET EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROU
```

---

## Crash 129: `e76532d46b42ab84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087390`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (-CURRENT_TIME); VALUES (NULL); SELECT hex(zeroblob(-2147483648)); 
```

---

## Crash 130: `304a32ef2522b32c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091225`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(CURREN
```

---

## Crash 131: `eb1df5d4f139e265` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093688`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); SELECT CURRENT_DATE LIKE CURRENT_DATE ESCAPE TRUE FROM p WHERE EXISTS (VALUES (FALSE)); CR
```

---

## Crash 132: `9cc2d8eb494bbd9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094197`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CAST(CURRENT_TIME AS BOOLEAN))); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 133: `1275b48f3d8dcb60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094475`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (FALSE || CAST(TRUE AS BOOLEAN))); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (FALSE % CURRENT_TIME >= TRUE); PRAGMA integrity_check
```

---

## Crash 134: `6e3e1343b4023237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094776`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (TRUE >= -98.17347049468); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 135: `77b3499c7dcdee64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095039`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (CURRENT_DATE IS NOT NULL % CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE I
```

---

## Crash 136: `dc8e4976f87232aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095844`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p VALUES (X''); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 137: `03ccb081274a5af2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098750`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN q WHERE FALSE IN (EXISTS (VALUES (TRUE) EXCEPT SEL
```

---

## Crash 138: `58b5ba15964104a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099570`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR ROLLBACK INTO p VALUES (random()); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT I
```

---

## Crash 139: `54eea3b58af78291` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103265`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p SELECT ALL * FROM p LIMIT hex(hex(hex(hex(hex(CURRENT_TIME))))); SELECT *; SELECT hex(zeroblob(0));
```

---

## Crash 140: `251d8c08065572f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103272`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT INTO p SELECT ALL * FROM p LIMIT CURRENT_TIMESTAMP OFFSET EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY
```

---

## Crash 141: `8eb00607f01b8f04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105651`

```sql
SELECT round(1e-308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, c2, c1); SELECT CURRENT_TIMESTAMP IS TRUE GLOB -CURRENT_TIME >= CURRENT_TIME - CURRENT_TIME IS NOT NULL COLLATE BIN
```

---

## Crash 142: `847a36bc1203a209` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112125`

```sql
SELECT printf('%.*d', 2147483647, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (TRUE); VALUES (NULL); SELECT hex(zeroblob(-1));
```

---

## Crash 143: `2661a27f6bda5a01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113092`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR REPLACE INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(CURRENT_TIME))))))))))))); PRA
```

---

## Crash 144: `e58d477fdf66b6e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113642`

```sql
SELECT printf('%f', 9223372036854775807, '___n_xD9Q- -qN_O'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO q VALUES (TRUE); VALUES (NULL); SELECT hex(zeroblob(-1));
```

---

## Crash 145: `98681906e16edf7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114879`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP / TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 146: `879ab45061b8ed9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116582`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM q JOIN p USING (c3, c3) LIMIT CURRENT_TIMEST
```

---

## Crash 147: `01345c4c5d0a19bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 148: `a2bbb15c3f8ec176` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000117173`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 149: `e3f8a9e5bd8c6f75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120222`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(c3 INT UNIQUE, c1 REAL UNIQUE, b BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 150: `23d31e6dc07879d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121489`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT FALSE, c1 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP; SELECT printf('%.*f', -21
```

---

## Crash 151: `686bdc02255fef81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121631`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM p JOIN p a ON CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 152: `c71e3951ecc28373` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122778`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO t2 VALUES (CASE TRUE WHEN NULL THEN CURRENT_TIME ELSE FALSE END); PRAGMA integrity_chec
```

---

## Crash 153: `b8ced97a28bdf28f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123027`

```sql
SELECT printf('%.*d', -1); SELECT printf('%.*g', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a INTEGER 
```

---

## Crash 154: `2a7bab0c744f6735` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127850`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (FALSE)) AS a LEFT JOIN p NOT I
```

---

## Crash 155: `2a7cae5dbf12570f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128448`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED JOIN p NATURAL JOIN p; SE
```

---

## Crash 156: `552dc406f6891bee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIME FROM
```

---

## Crash 157: `534f9841f598b77c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128924`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY, c1 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE 
```

---

## Crash 158: `17bf64a0ba7b2be6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130766`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME) UNION SELECT TRUE AS b_zx_ ORDER BY CURR
```

---

## Crash 159: `6e402d896b2735f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132543`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE NOT NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT I
```

---

## Crash 160: `fe9eaabc6785c8fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137999`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT X'dF5cbf6fCaCC9f'); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE WIND
```

---

## Crash 161: `ef3b54b358084a9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142213`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY); INSERT OR ABORT INTO q VALUES (NULL); SELECT DISTINCT * FROM q ORDER BY CURRENT_TIME ASC NULLS FI
```

---

## Crash 162: `b0fe77719c729e55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146405`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN q WHERE c3 IN (hex(hex(hex(hex(hex(hex(hex(hex(hex
```

---

## Crash 163: `b53905309a7acbf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150082`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_DATE))); PRAGMA quick_check; SELECT hex(zeroblob(-9223
```

---

## Crash 164: `45b02fe11b165abf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150142`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p AS b JOIN p NATURAL LEFT JOIN p NOT
```

---

## Crash 165: `8ac553934b7bb512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150990`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB UNIQUE); SELECT CURRENT_DATE LIKE CURRENT_TIME ESCAPE TRUE FROM p WHERE EXISTS (VALUES (FALSE)); CR
```

---

## Crash 166: `77be5ac2ec148f80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153005`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(hex(CAST(CAST(CURRENT_TIME - 790.8537774203968180297506961
```

---

## Crash 167: `b3103f9fbf298371` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153031`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(json_type(TRUE)))); VALUES (CURRENT_TIME);
```

---

## Crash 168: `fe3b0329b23de9a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153151`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIME COLLATE RTRIM AS b_zx_; INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_TIMESTAMP))); VALUES 
```

---

## Crash 169: `25cf47e69f394061` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153182`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CASE WHEN CURRENT_TIME THEN c3 ELSE RAISE(IGNORE) END); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_T
```

---

## Crash 170: `71d0c9258f0264b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153214`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p NOT INDEXED WHERE RAISE(IGNORE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_TIMESTA
```

---

## Crash 171: `ec9be7db0ae281a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153222`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * FROM q JOIN (SELECT DISTINCT * FROM q NOT INDEXED) AS a USING (c3, c3) LIMIT CURRENT_TIME; INSERT OR R
```

---

## Crash 172: `018ae7e41a3f27d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153229`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE <= TRUE, CURRENT_DATE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_TIMESTAMP))); VALUES
```

---

## Crash 173: `94bbe42712abfeef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153235`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_TIME), count(*) FILTER (
```

---

## Crash 174: `a086ca47ec4f9cbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153247`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY CURRENT_TIMESTAMP, _rowid_ WINDOW w1 AS (); INSERT OR ROLLBACK INTO
```

---

## Crash 175: `2739bd08fbede136` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153254`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (q.c3); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_TIMESTAMP))); VALUES (CURRENT_TIME);
```

---

## Crash 176: `c726f31bcb142991` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153262`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP) UNION SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS (); INSERT OR RO
```

---

## Crash 177: `6eb3e5dda44f89ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153274`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM s NOT INDEXED CROSS JOIN p LEFT OUTER JOIN q AS s9090d9_0v7o4eg076_o; INSERT OR ROLLBACK INTO p VALUE
```

---

## Crash 178: `49b3f3edbcdd6ac4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153289`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (changes() OVER (PARTITION BY CURRENT_DATE ORDER BY EXISTS (SELECT * INTERSECT SELECT * FROM s NOT INDEXED G
```

---

## Crash 179: `ab50a30623729f79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153370`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT p.*; INSERT OR ROLLBACK INTO p VALUES (hex(hex(CURRENT_TIMESTAMP))); VALUES (CURRENT_TIME);
```

---

## Crash 180: `6d0fc5ce1c196779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153407`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ROLLBACK INTO p VALUES (hex(hex(CAST(CURRENT_TIME AS BLOB)))); VALUES (CURRENT_TIME);
```

---

## Crash 181: `1a3cad881ba280b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154515`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT OR ROLLBACK INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(he
```

---

## Crash 182: `f564e9861da91d88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154900`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE WINDOW w1 
```

---

## Crash 183: `2357da663631cecf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154960`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO p SELECT DISTINCT * FROM q ORDER BY CURRENT_TIME ASC NULLS FIRST LIMIT hex(hex(hex(hex(hex(hex
```

---

## Crash 184: `22a11989221e9028` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156971`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP - NOT FALSE || TRUE); EXPLAIN QUERY PLAN VALUES (TRUE)
```

---

## Crash 185: `28f7abf449a57a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158215`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); VALUES (NULL); CREATE TABLE IF NOT EXISTS p(c1 FLOA
```

---

## Crash 186: `fff84ee2c27da9c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158627`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a TEXT PRIMARY KEY); INSERT OR FAIL INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(-397577070.787069e+3)))))))); VALUES (NULL
```

---

## Crash 187: `b89a1631e720e246` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160403`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME || FALSE BETWEEN CURRENT_TIME AND FALSE COLLATE RTRIM || CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_ch
```

---

## Crash 188: `4cc358e5f3e2c4e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161513`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (trim(total_changes()) << CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 189: `849a905dc50744d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161850`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(random())); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBA
```

---

## Crash 190: `ca93e937a2b3ee5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161895`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(CURRENT_TIME))))))))))))))))); PRAGMA integrity_ch
```

---

## Crash 191: `4d4a06709508c80d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162149`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(trim(trim(trim(trim(trim(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(-397577070.787069e+3)))))))))
```

---

## Crash 192: `501889f7748d7a3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162874`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (-CURRENT_DATE NOT IN (VALUES (CURRENT_TIMESTAMP))) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 193: `bed6f13c16443f73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163082`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (-CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR R
```

---

## Crash 194: `bfbff6cc478ede91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163488`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE = CAST(CURRENT_TIMESTAMP AS INT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 195: `dba5663931bfb698` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163997`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); INSERT INTO p VALUES (CAST(TRUE AS TEXT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); IN
```

---

## Crash 196: `375106e90b37eecb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164003`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); INSERT INTO p VALUES (CAST(hex(hex(hex(hex(hex(hex(CURRENT_TIME)))))) AS TEXT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT hex(zeroblob(92
```

---

## Crash 197: `4f60e8a49dba8118` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165625`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE)) ON CONFLICT DO NOT
```

---

## Crash 198: `77ad4ce0862f577d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000165960`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NULL) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE
```

---

## Crash 199: `540a965661f59544` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166281`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p SELECT DISTINCT * FROM (VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIME)) AS g9_v___9zv96z__46u6re2zio520_o9__9_3__lc_v441_c_8ty_m
```

---

## Crash 200: `1fc6c212aa20b4a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166501`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (FALSE * CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 201: `df8d18ee92b07fb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166836`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALU
```

---

## Crash 202: `895af925b5a65687` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168443`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS ())) ON CONF
```

---

## Crash 203: `0f91bdf1c0c34548` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168664`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED NATURAL JOIN p GROUP BY TRUE, FALSE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; C
```

---

## Crash 204: `908c0a44cb69b878` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169084`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME COLLATE RTRIM)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; C
```

---

## Crash 205: `cf47d8c926b3a8cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170925`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FROM p ORDER BY CURRENT_TIME ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 206: `5366a705f3e3355e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171702`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT count(DISTINCT CURRENT_T
```

---

## Crash 207: `81a681489f833f19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173131`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE || CURRENT_DATE) INTERSECT VALUES (CURRENT_TIME); SELECT 
```

---

## Crash 208: `679a5cfd82929fe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173343`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 209: `c11384d020ed781b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177383`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (min(CURRENT_DATE) FILTER (WHERE EXISTS (VALUES (TRUE) EXCEPT SELECT * FRO
```

---

## Crash 210: `99c323d853294e32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180165`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(CURRENT_TIMESTAMP)))))))); EXPLAIN QUERY PLAN SELECT min(RAISE(IGNORE)) AS
```

---

## Crash 211: `672026f7ff8395a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189661`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE, c1 REAL UNIQUE, b BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p (_rowid_) VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(hex(-397577070.
```

---

## Crash 212: `49dde5e6bef33dd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194820`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED
```

---

## Crash 213: `5e728671f6abb760` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195029`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT X'aC7e68BEDffCAf'); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT OR ROLLBACK INTO q VALUES (random()); PRAGMA quick_check; CREAT
```

---

## Crash 214: `2fdd0d491afb96c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196458`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES ((VALUES (CURRENT_TIME) UNION SELECT CURRENT_TIMESTAMP AS b_zx_ ORDER BY CU
```

---

## Crash 215: `a851dae819e11eb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196796`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(
```

---

## Crash 216: `fab1b3e1ed57f885` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197650`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT -98.17347049468); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(CURRENT_TIMESTAMP)))))))) EXCEPT VA
```

---

## Crash 217: `eff981da1c530536` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197761`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT X'AB87d5bb5B'); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 218: `392ea769a5a0ceab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198295`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT *, * FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED
```

---

## Crash 219: `3c73cf1648ccd0cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198492`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEX
```

---

## Crash 220: `874a863eb4e3790b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198927`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 221: `3f128c15d4f2aeaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199923`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (TRUE << TRUE OR CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTU
```

---

## Crash 222: `4d20e1382997bc0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199973`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 223: `7a1ceba0be3b415e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199979`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (TRUE << NULL)); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 224: `7e033f3ff11dcc39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203240`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 225: `215f9f0d6a59cb1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203369`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 226: `a3d1aa2ae5a606b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203458`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 227: `c140bb94e810cc0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203624`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 228: `96658c5aa7b102ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203883`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 229: `b1f1b698833e6e5b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204056`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 230: `b5000264f35e54b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204062`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 231: `796da25c4d590115` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204304`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 232: `0c2b0867afe7d189` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204670`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (SELECT
```

---

## Crash 233: `010ee2969edae1f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205412`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN
```

---

## Crash 234: `eaad77f1520252e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206362`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE X'aA4cEBBd' GLOB X'aA4cEBBd
```

---

## Crash 235: `f330c38b597df968` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206510`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE X'aA4cEBBd' GLOB NULL) AS s
```

---

## Crash 236: `e1ad331f4836f364` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207999`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP IS NOT b)
```

---

## Crash 237: `883cb5d93695e398` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209455`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT min(CURRENT_TIME IN (SELECT * FROM p NOT INDEXED WHERE CU
```

---

## Crash 238: `b97250f221daccb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209464`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 239: `a6a1ff5ea8117ee1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209472`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 240: `e58881e5bbbf8edf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209482`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 241: `d5088641c9389c35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209509`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT NOT CURRENT_TIMESTAMP <> CURRENT_T
```

---

## Crash 242: `e1f1570b77659f9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209523`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a REAL NOT NULL DEFAULT '--_8O_', c1 BLOB); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURREN
```

---

## Crash 243: `7d530508f992fe79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209537`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT NULL, * ORDER BY CURRENT_DATE DESC
```

---

## Crash 244: `4b537ddda862167c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209545`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 245: `1d329255b10598ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209554`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 246: `74b93e90063e20cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209561`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 247: `6002e2e74a90697d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209595`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 248: `80a5315ce4e60173` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209615`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 249: `ed60c932389ca3d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209646`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT (SELECT * ORDER BY CURRENT_DATE DESC NULLS
```

---

## Crash 250: `10a5e8e821b9d158` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210199`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT CURRENT_DATE NOT IN (SE
```

---

## Crash 251: `9824153e5895c58c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210896`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE (SELECT * FROM p NOT INDEXE
```

---

## Crash 252: `f879cbff9051cca3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211119`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT NULL COLLATE BINARY >= CURRENT_TIMESTAMP A
```

---

## Crash 253: `f5e54d1605929220` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212421`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN NOT NULL DEFAULT CURRENT_TIME); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE CURRENT_
```

---

## Crash 254: `81a11a193506763a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212737`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT TRUE, a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(a) DO UPDATE SET c3
```

---

## Crash 255: `202eca7717b0cdab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213280`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(rowid NUMERIC U
```

---

## Crash 256: `8b5317edc60a3beb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213652`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET c3 = CURRENT_TIME; VAL
```

---

## Crash 257: `b69e3b1a2e8681b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213778`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO p (_rowid_) VALUES (TRUE) ON CONFLICT(c3) DO UPDATE SET _rowid_ = CURRENT_TIME; V
```

---

## Crash 258: `bb4d2e795d750d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216838`

```sql
SELECT round(-1.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, c3); SELECT NULL IS -CURRENT_DATE MATCH CURRENT_TIMESTAMP BETWEEN ~FALSE AND ~FALSE COLLATE NOCASE
```

---

## Crash 259: `3813bb2d50632548` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217106`

```sql
SELECT substr('', 9223372036854775807, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO t1 VALUES (last_insert_rowid() COLLATE RTRIM, CURRENT_DATE C
```

---

## Crash 260: `e0bc0aaf54221546` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217299`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NOT TRUE <> CURRENT_TIME >= NOT TRUE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*
```

---

## Crash 261: `861e7e8756db9e1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218273`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER CHECK (CAST(CURRENT_TIME AS BOOLEAN))); CREATE TABLE IF NOT EXISTS q(rowid INTEGER); REPLACE INTO p VALUES (json(hex(hex(hex(random()))))); PRAGMA quick_check;
```

---

## Crash 262: `6cb752b9663fa806` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218313`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); REPLACE INTO p VALUES (json(hex(hex(hex(random()))))); PRAGMA quick_check;
```

---

## Crash 263: `75a48df1bded18e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222711`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE NOT CURRENT_DATE NOT IN 
```

---

## Crash 264: `73d7f040b67b641a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223063`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE TRUE / 0.0) AS sub1; SELECT
```

---

## Crash 265: `30b20301b5315f51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223206`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE TRUE / CURRENT_TIME) AS sub
```

---

## Crash 266: `ddeedbe809ee03a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000223854`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP NOT IN (S
```

---

## Crash 267: `f5300d4abb5adeee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225968`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CAST(CAST(hex(hex(hex(hex(h
```

---

## Crash 268: `41e51079413a73e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226777`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 269: `cf17afbb96cccb03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226910`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 270: `6147884d8a6b1dc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227570`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL PRIMARY KEY); INSERT INTO q DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE CURRENT_DATE NOT IN (VALUES
```

---

## Crash 271: `481ab90bf9663ad3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231290`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 272: `4d588bd2a40621d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232084`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL DEFAULT -98.17347049468); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_r
```

---

## Crash 273: `44a2f83736a42229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232653`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p VALUES ((VALUES (CURRENT_TIME) UNION SELECT * FROM p NOT INDEXED WHERE NULL GROUP 
```

---

## Crash 274: `2a64d8c358940810` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233263`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT -510586149.5496384e924974796201950818697); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_
```

---

## Crash 275: `7e7342813b38bc37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235602`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (CURRENT_DATE IS NOT FALSE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); CREATE VIRTUAL
```

---

## Crash 276: `c5d5ccdef76eff44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235827`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE CHECK (FALSE IN (FALSE, FALSE, FALSE))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT pr
```

---

## Crash 277: `1d546107e9cfee33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237374`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY hex(hex(hex(CAST(hex(hex(CURRENT_TIME)) AS
```

---

## Crash 278: `c7776302a9622b13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252237`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIMESTAMP DES
```

---

## Crash 279: `29335f0ed5202360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252420`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (), count(*) FILTER (WHERE CURR
```

---

## Crash 280: `3d6a11cde9001734` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT); CREATE TABLE IF NOT EXISTS q(rowid TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY CURRENT_TIMESTAMP DES
```

---

## Crash 281: `6f1065e8f3a4f75e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000254668`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_TIME, CURRENT_DATE) EXCEPT VALUES (FALSE, CURRENT_DATE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 282: `287ed4b2f9ffbcfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255004`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(hex(hex(hex(hex(hex(CURRENT_TIMESTAMP))))))) UNION VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 283: `077d8366d93871a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255177`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(total_changes())) UNION VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 284: `f35404ea8c098f17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255184`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(hex(last_insert_rowid()))) UNION VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 285: `434b7f1f75434d4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255193`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(hex(hex(hex(count(*)))))) UNION VALUES (NULL); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 286: `875e6e90eaf9027e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255933`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (json_extract(CASE FALSE WHEN CURRENT_TIMESTAMP THEN FALSE END, '_-_3c _3
```

---

## Crash 287: `41d0978a90bba2cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255989`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE INDEX IF NOT EXISTS idx1 ON p(b); REPLACE INTO p VALUES (json(FALSE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); IN
```

---

## Crash 288: `bec58a1b17241791` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256421`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(hex(hex(hex(hex(hex(hex(CURRENT_DATE)))))))) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 289: `eba3b0b0d7de9f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256554`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (hex(changes())) INTERSECT VALUES (CURRENT_TIME); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 290: `48d5f20c59e83383` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257590`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT count(DISTINCT CURRENT_T
```

---

## Crash 291: `796705e52271c9d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258825`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE, TRUE WINDOW w1 AS () ORDER BY CURRENT_TIMESTAMP ASC 
```

---

## Crash 292: `d2049ae865b4bd9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258973`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_TIMESTAMP ASC NULLS 
```

---

## Crash 293: `11f47fe57ebb2c7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259003`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY NULL DESC NULLS LAST; SELECT
```

---

## Crash 294: `c4633aa2bb2940a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259857`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM (VALUES (CURRENT_TIME)) AS a NATURAL LEFT JOIN p GROUP BY FALSE)) ON CONFLICT DO NOTHING; PRAGMA inte
```

---

## Crash 295: `557806b2410a06fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260061`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NATURAL LEFT JOIN p GROUP BY FALSE)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 296: `acb79bd507bcdc5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260822`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL TRUE FROM p AS b JOIN p JOIN (p JOIN p AS r) LIMIT CURRENT_TIMESTAMP OFFSET EXISTS (VALUES (TRUE) EXCEPT
```

---

## Crash 297: `f09acb16799980b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261522`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (hex(CURRENT_TIMESTAMP) * CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VI
```

---

## Crash 298: `c275abcf2ec8ec57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261589`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM p LIMIT CURRENT_TIME)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 299: `a6090e5a41c4a066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000261757`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_TIME) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALU
```

---

## Crash 300: `81542334e0f1341e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263254`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (SELECT ALL * FROM p AS b JOIN p LEFT OUTER JOIN p AS on5jf_t_h_) AS a LIMIT CURRENT_DATE IS NOT 
```

---

## Crash 301: `144226f331732e54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000263736`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT EXISTS (SELECT ALL * FROM (VALUES (NOT EXISTS (SELECT ALL min(CURRENT_TIME) AS b_zx_, * FROM (VALUES (CURRENT_DATE)) AS a L
```

---

## Crash 302: `3ef0bd2b4aad4fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264055`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE = CAST(CURRENT_TIMESTAMP AS TEXT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 303: `442a3a1d410c729d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264375`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (hex(hex(CURRENT_DATE)) = CAST(FALSE IN (FALSE, FALSE, FALSE) AS INT)) ON CONFLICT DO NOTHING; PRAGMA quick_check; SELECT hex(ze
```

---

## Crash 304: `ffd199bd1426f458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000265285`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (trim(hex(hex(hex(hex(hex(hex(hex(hex(random())))))))))); PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 305: `40534f9f2da0a825` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266071`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (random()); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VAL
```

---

## Crash 306: `b8b833638ed05b5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266170`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (random());
```

---

## Crash 307: `2d519fdc050745c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266176`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p
```

---

## Crash 308: `de912468f046d7d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266182`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES 
```

---

## Crash 309: `0d640eacbba9596c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000266988`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM (SELECT * FROM p WHERE hex(hex(hex(CURRENT_TIME))) NOT IN (SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY FALSE
```

---

## Crash 310: `f71b172b9fcde4c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268222`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (NOT 0.0) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 311: `7d39d8265df3381d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268382`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE || hex(hex(hex(hex(hex(hex(hex(hex(hex(CURRENT_TIMESTAMP)))))))))) ON CONFLICT DO NOTHING; PRAGMA integrity_check;
```

---

## Crash 312: `dd60f7e36833d861` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268388`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (TRUE NOT IN (VALUES (count(*) FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_TIMESTAMP DESC ROWS BETWEEN UNBOUNDED PRECEDING AND C
```

---

## Crash 313: `da832f0bdb971009` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000175218`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT CURRENT_TIME COLLATE RTRIM IS NOT NULL) LIKE CURRENT_DATE LIKE
```

---

## Crash 314: `24cb8086d4e4ccd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000201848`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER CHECK (EXISTS (VALUES (TRUE) EXCEPT SELECT * FROM s NOT INDEXED WHERE NULL GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY RAISE(IGNORE) COLLATE NOCASE) IS CURRE
```

### Stack Trace

```
  sqlite3WindowListDelete
  clearSelect
  sqlite3SelectDelete
  sqlite3ExprDeleteNN
  sqlite3ExprDeleteNN
```

---

## Crash 315: `b8bfad3c653990dd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000239734`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p VALUES (NOT EXISTS (SELECT * FROM p NATURAL JOIN p GROUP BY FALSE)) ON CONFLICT DO NOTHING; EXPLAI
```

---

## Crash 316: `7916a93c4ac12f15` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000253840`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT CURRENT_TIME COLLATE RTRIM) LIKE CURRENT_DATE LIKE min(hex(hex
```

---

## Crash 317: `0d37103568f7518e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000253861`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b, c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT CURRENT_TIME COLLATE RTRIM) LIKE CURRENT_DATE LIKE count(*)
```

---

## Crash 318: `d95005768d5f7106` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000253871`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT count(DISTINCT CURRENT_TIME COLLATE RTRIM) LIKE CURRENT_DATE LIKE count(*) FI
```

---

## Crash 319: `613a225648522000` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000253930`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (max(trim(trim(trim(trim(trim(trim(trim(trim(last_insert_rowid())))))))))) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DIS
```

---

## Crash 320: `52e9f6d03bd805f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000253940`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT CURRENT_DATE NOT IN (VALUES (count(*) OVER (PARTITION BY FALSE
```

---

## Crash 321: `862fe368e171d910` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000254039`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT count(DISTINCT CURRENT_TIME COLLATE RTRIM) LIKE count(DISTINCT CURRENT_TIME C
```

---
