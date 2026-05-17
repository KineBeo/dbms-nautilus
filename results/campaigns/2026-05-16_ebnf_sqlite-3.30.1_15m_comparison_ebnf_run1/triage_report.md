# Crash Triage Report

**Total crashes:** 128  
**Unique crash sites:** 128  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 126 | 126 | 98% |
| Signal | 2 | 2 | 1% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `20ec08a116254b78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000718`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH t3 AS MATERIALIZED (VALUES (TRUE) UNION SELECT DISTINCT * LIMIT TRUE) DELETE FROM t1 WHERE NULL < NULL RETURNING t2.*; WITH t1 (c3, c3, c
```

---

## Crash 2: `9550e9ed59df5456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000834`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1); CREATE TABLE IF NOT EXISTS t1 (c3 DATE UNIQUE) WITHOUT ROWID; END TRANSACTION;
```

---

## Crash 3: `87a8ca1ec492a7d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002154`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 4: `1e63ad34d174095b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002160`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 5: `be2570d7f560697a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002166`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 6: `0e3c728312edf6c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002175`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 7: `b4e747aa03f46993` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002182`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 8: `4dfb974d1eb71daf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002194`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 9: `f3819e95bfc6d0e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002200`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 10: `1026ab4fdee96852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002207`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 11: `5a7bebe8f0d55e10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002213`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 12: `ead02ea503cc0bff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002219`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN CURRENT_TIME PRECEDING AND CURRENT_TIME FOLLOWING) INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DA
```

---

## Crash 13: `16667c3ef4c613ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002376`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES) INTERSECT SELECT * FROM t2 WHERE CURRENT_DATE GROUP BY CURRENT_TIM
```

---

## Crash 14: `4de280cf0eca5d78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002383`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES) INTERSECT SELECT * FROM t2 WHERE CURRENT_DATE GROUP BY CURRENT_TIM
```

---

## Crash 15: `c659cda9766cfe28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002401`

```sql
SELECT * FROM t3 NOT INDEXED GROUP BY TRUE WINDOW w1 AS (ORDER BY TRUE ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES) INTERSECT SELECT * FROM t2 WHERE CURRENT_DATE GROUP BY CURRENT_TIM
```

---

## Crash 16: `1fc3b021bbf45ed6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002655`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 17: `c0b28d4bf2895185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002662`

```sql
BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2);
```

---

## Crash 18: `3911b8995dc6fb8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003702`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); BEGIN EXCLUSIVE;
```

---

## Crash 19: `7b437cfa60783da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004858`

```sql
BEGIN EXCLUSIVE TRANSACTION; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); WITH t1 AS (SELECT DISTINCT CURRENT_TIME AS myj__7_i_6ql, t1.* EXCEPT SELECT ALL * LIMIT CURREN
```

---

## Crash 20: `b3889090c069481f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005400`

```sql
DROP TABLE IF EXISTS t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t1 AS NOT MATERIALIZED (WITH t3 AS (SELECT * ORDER BY RAISE(IGNORE) ASC) SELECT * ORDER BY NOT FALSE A
```

---

## Crash 21: `4576d21da56013c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006452`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED WHERE changes() FILTER (WHERE CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `d80d26ad23af32af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016405`

```sql
PRAGMA analysis_limit=370581; SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM;
```

---

## Crash 23: `25dac4d61bf606f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016508`

```sql
REINDEX; SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM;
```

---

## Crash 24: `d5381b991a7abaa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016514`

```sql
PRAGMA integrity_check; SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM;
```

---

## Crash 25: `0fdc411bd1f841a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016739`

```sql
PRAGMA cache_size=+4; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 26: `7a99415fe23a2496` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018475`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIEW v1 (c1, _rowid_) AS VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 27: `f6bf67fffb5df547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020217`

```sql
CREATE TABLE t1 (c3 DATE PRIMARY KEY DESC, c2 NUMERIC COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 28: `122f897d71e5484c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020320`

```sql
CREATE TABLE t1 (c3 BOOLEAN NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 29: `c94d2504134d8666` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021500`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 30: `d8fc203acf69d439` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021640`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 31: `4e7743e7bc5a1a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021658`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, _rowid_);
```

---

## Crash 32: `26ad29600a82281d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023836`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2);
```

---

## Crash 33: `c89a9dc9118f00dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023970`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); BEGIN DEFERRED; COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 34: `08e0a88cdbbf6113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028610`

```sql
VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 35: `554093d311270f0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029146`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t3 NOT INDEXED NATURAL JOIN t2 NOT INDEXED JOIN t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE R
```

---

## Crash 36: `9ae47372abe5edfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029153`

```sql
SELECT DISTINCT 291.197201198539507633944736964513743816166073374942789E+068258, * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TI
```

---

## Crash 37: `adcd2e278c9a640b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029159`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE random() FILTER (WHERE FALSE % CURRENT_DATE) OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_DATE NOTNULL) GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER 
```

---

## Crash 38: `280aec7bab112f0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029165`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY TRUE | TRUE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 39: `6279ffca5f6d9954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029171`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_DATE / TRUE > CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION
```

---

## Crash 40: `b449efcef0a4872a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029178`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE FALSE < CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 41: `20fac6e567a0fc76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029187`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY NULL == CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 42: `d8fb13e5e928ccc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029193`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY NULL NOT GLOB changes() NOT GLOB TRUE NOT GLOB NULL NOT GLOB FALSE NOT GLOB CURRENT_DATE 
```

---

## Crash 43: `eccb5b9ee21f3788` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029203`

```sql
SELECT DISTINCT * INTERSECT SELECT NULL AS a, * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 44: `a2fbcef6bbb5fb7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029218`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY NOT EXISTS (SELECT ALL * FROM t2 INDEXED BY c1 ORDER BY CURRENT_TIMESTAMP DESC NULLS FIRS
```

---

## Crash 45: `ab222d840a0d7fe0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029226`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY NULL HAVING TRUE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 46: `87ee8cb224e4a5fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029233`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t1 NATURAL LEFT OUTER JOIN (t1) WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRAN
```

---

## Crash 47: `a2ffd5e9622c0b55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029239`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 NOT INDEXED CROSS JOIN t1 NOT INDEXED NATURAL INNER JOIN t1 NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CUR
```

---

## Crash 48: `bc3ed00906bdc81d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029245`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY FALSE, FALSE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 49: `9a48360e676eb4a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029254`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY total_changes() OVER (PARTITION BY CURRENT_DATE ORDER BY NULL ASC RANGE UNBOUNDED PRECEDING) WINDOW w1 AS () ORDER BY CURRENT_T
```

---

## Crash 50: `ec6a42053501c218` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029262`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS (), w2 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 51: `07ddbb8341315d5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029270`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY -NULL ISNULL NOT BETWEEN (FALSE, CURRENT_DATE ISNULL || CURRENT_DATE) AND FALSE LIKE CASE
```

---

## Crash 52: `62f3ed0928eb5ee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029276`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t3 AS l5v__2l98_d__5e30a866339_i_ WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TR
```

---

## Crash 53: `2f87c0ddbebd1dd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029283`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS (ORDER BY FALSE ASC ROWS EXISTS (VALUES (RAISE(IGNORE))) PRECEDING) ORDER BY CURRENT_TIME, CURRENT_TI
```

---

## Crash 54: `2eae0a17b645181f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029289`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE NOT EXISTS (SELECT * FROM t2 NOT INDEXED WHERE CURRENT_TIME EXCEPT SELECT ALL * ORDER BY CURRENT_TIME ASC NULLS LAST) GROUP BY CURRENT_DATE WINDOW w1
```

---

## Crash 55: `45289b1d0ecaff66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029296`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY +NULL WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 56: `4f24390c878fb242` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029322`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY ~char(c2 NOT NULL) DESC NULLS LAST, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION
```

---

## Crash 57: `7985574bd242fdfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029329`

```sql
SELECT DISTINCT t1.* INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, CURRENT_TIMESTAMP COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 58: `7b77bcd2eaa13f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029354`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM t2 WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_TIME, RAISE(ROLLBACK, '') COLLATE RTRIM; ROLLBACK TRANSACTION;
```

---

## Crash 59: `cb4601a47c907484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029402`

```sql
SELECT DISTINCT * INTERSECT SELECT * FROM ((t3 NOT INDEXED NATURAL JOIN t3 NOT INDEXED) NATURAL JOIN t3 NATURAL LEFT JOIN t1) WHERE CURRENT_TIME GROUP BY CURRENT_DATE WINDOW w1 AS () ORDER BY CURRENT_
```

---

## Crash 60: `e100e720a51552b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031774`

```sql
PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c3);
```

---

## Crash 61: `cb50d226744f2779` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034382`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, rowid, c2, _rowid_); CREATE TRIGGER trg1 AFTER I
```

---

## Crash 62: `30a5be332f28cdbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034426`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, rowid, c2, _rowid_); CREATE TRIGGER trg1 AFTER INSERT ON t2 FOR
```

---

## Crash 63: `cc147341edc8c981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035482`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 64: `09e6708c46771b22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036850`

```sql
PRAGMA foreign_keys=1; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); CREATE UNIQUE INDEX idx1 ON t3 (c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, 
```

---

## Crash 65: `681ee5ab7bd1c85b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036902`

```sql
VACUUM; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); CREATE UNIQUE INDEX idx1 ON t3 (c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 66: `c40dc6cb4483ee28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037998`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_);
```

---

## Crash 67: `70a4985accd3fc35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038819`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); ALTER TABLE t2 RENAME TO t1;
```

---

## Crash 68: `ca148ef025f189d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039322`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (c1 INTEGER NOT NULL); ALTER TABLE t3 RENAME TO t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 69: `6654bf7421e3ea0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039533`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 NUMERIC UNIQUE, _rowid_ TEXT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 70: `5b7ec439eca50cc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040807`

```sql
DROP INDEX IF EXISTS idx1; BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 71: `c5b3516b8dccb266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044460`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIMESTAMP, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 72: `98d2b557e3d19db7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045857`

```sql
CREATE TABLE t1 (_rowid_ NUMERIC COLLATE NOCASE, c1 INT COLLATE NOCASE, PRIMARY KEY (_rowid_) ON CONFLICT REPLACE, UNIQUE (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, 
```

---

## Crash 73: `ba619142104e7b3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045926`

```sql
CREATE TABLE t1 (_rowid_ NUMERIC COLLATE NOCASE, c1 INT COLLATE NOCASE, PRIMARY KEY (_rowid_), UNIQUE (_rowid_)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c1);
```

---

## Crash 74: `97ce79c396b801c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046140`

```sql
PRAGMA wal_checkpoint(FULL); ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c2);
```

---

## Crash 75: `d3f5b380f601a61a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046157`

```sql
PRAGMA wal_checkpoint(FULL); ATTACH ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 76: `7c726165018ae9b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051139`

```sql
CREATE TABLE t1 (c1 INTEGER PRIMARY KEY ASC, CHECK (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ROLLBACK TO SAVEPOINT sp1;
```

---

## Crash 77: `103ca0c0e72ec7d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051167`

```sql
CREATE TABLE t1 (c1 INTEGER PRIMARY KEY ASC, CHECK (FALSE)); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); COMMIT TRANSACTION;
```

---

## Crash 78: `77a3133a0e43d420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053984`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t2 NATURAL JOIN t2 NOT INDEXED USING (c1, c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 79: `1fe75fb4cc501edc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055440`

```sql
ANALYZE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 80: `b30e01a26926ab33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058995`

```sql
CREATE TABLE t1 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT, c2 INTEGER COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 81: `5960c78e6816d578` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061395`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BLOB COLLATE NOCASE, c1 INTEGER PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 82: `92f816f7daf58f0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064337`

```sql
PRAGMA journal_mode=DELETE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 83: `501ea0e24e891948` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066112`

```sql
CREATE TABLE t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC, c3 INTEGER REFERENCES t2 (c1) ON DELETE CASCADE ON UPDATE CASCADE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 84: `6e817dfccb5262a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089197`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM t3 NOT INDEXED WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); UPDATE t1 SET _r
```

---

## Crash 85: `bfa942826e833bb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090976`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, rowid, c3, c2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, _rowid_);
```

---

## Crash 86: `253b5dd8bc6149ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112953`

```sql
VALUES (FALSE) INTERSECT SELECT TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || 
```

---

## Crash 87: `3d390fafed619373` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113040`

```sql
VALUES (FALSE) INTERSECT SELECT TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || 
```

---

## Crash 88: `b2757e2418c44529` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113135`

```sql
VALUES (FALSE) INTERSECT SELECT TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || FALSE IS CAST(FA
```

---

## Crash 89: `0419cc1117bbf726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121515`

```sql
CREATE TABLE t2 (c3 INTEGER UNIQUE, c1 VARCHAR(255) PRIMARY KEY); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 90: `1d288f6141b140c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125353`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid BLOB NOT NULL REFERENCES t3 (c2) ON DELETE CASCADE ON UPDATE CASCADE, _rowid_ TEXT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 91: `8bb3db3757382b8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125811`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 REAL PRIMARY KEY DESC, c3 REAL UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 92: `9b6fd42ff0c95926` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126387`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 DATE DEFAULT CURRENT_TIMESTAMP, c1 FLOAT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 93: `0a7bafee74f0782a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126826`

```sql
CREATE TABLE t1 AS VALUES (NULL); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2); ROLLBACK TO sp1; DETACH DATABASE db2;
```

---

## Crash 94: `e420b361d3ca50af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129913`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 BLOB PRIMARY KEY) WITHOUT ROWID; WITH RECURSIVE t2 AS (SELECT *) SELECT * FROM t1 ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 95: `3ddb63900143d87a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132317`

```sql
CREATE TABLE t1 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT, c2 INTEGER COLLATE NOCASE); INSERT OR FAIL INTO t1 VALUES (NULL, NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT
```

---

## Crash 96: `2dbe99e479b49973` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134023`

```sql
CREATE TABLE t1 (_rowid_ INTEGER PRIMARY KEY AUTOINCREMENT, c2 INTEGER COLLATE NOCASE); INSERT INTO t1 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 97: `84fd23e83bb09068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138907`

```sql
ATTACH DATABASE ':memory:' AS db2; PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR FAIL INTO t3 VALUES (~CASE CASE WHEN (WITH RECURSIVE t1 AS (SELECT DISTINCT
```

---

## Crash 98: `5b4ac61bcf25a04a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144249`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; CREATE TABLE t2 (c2 BOOLEAN PRIMARY KEY, c1 INTEGER NOT NULL) WITHOUT ROWID; ANALYZE; ANALYZE; CREATE VIRTUAL TABLE 
```

---

## Crash 99: `a62772c73ac8c01e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146350`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 NUMERIC NOT NULL DEFAULT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 100: `7700735381915d1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147144`

```sql
CREATE TABLE t1 AS SELECT ALL 0.0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 101: `f2cc6958ae215f6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147193`

```sql
CREATE TABLE t1 AS SELECT ALL CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 102: `a89a018c47f5751c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148185`

```sql
CREATE TABLE t2 (_rowid_ DATE PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 103: `8b40243111bff089` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154488`

```sql
CREATE TABLE t1 (_rowid_ NUMERIC COLLATE NOCASE, c1 INT COLLATE NOCASE, CHECK (RAISE(IGNORE)), FOREIGN KEY (_rowid_, _rowid_) REFERENCES t1 (c2, c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 104: `53016c7cfd8f2eda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157312`

```sql
VALUES (count(*) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 105: `6fd74cb036245d19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157407`

```sql
VALUES (count(*) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); END; REINDEX t2; CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT RAISE(IGNORE) MATCH last_insert
```

---

## Crash 106: `b6f66ae4f6980201` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157891`

```sql
VALUES (count(*) OVER (PARTITION BY NULL IS NOT NULL ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 107: `9d6ba9f9c6cbeb76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158112`

```sql
VALUES (count(*) OVER (), count(*) OVER (), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 108: `a1fdf241ff7f577a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159119`

```sql
VALUES (count(*) OVER (ORDER BY CURRENT_TIME, NULL), CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c1); VACUUM INTO ':memory:'; INSERT INTO t1 VALUES (CASE WHEN CURRENT_D
```

---

## Crash 109: `5540a35848aeda6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160952`

```sql
VALUES (TRUE) UNION ALL SELECT DISTINCT NULL AS a ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ATTACH ':memory:' AS db2; CREATE TRIGGER trg1 BEFORE DE
```

---

## Crash 110: `616f683896cd3bad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163722`

```sql
CREATE TEMP TABLE IF NOT EXISTS t1 (c3 VARCHAR(255) UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK TO SAVEPOINT sp1;
```

---

## Crash 111: `e588ef5b0c111aa0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168758`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 NUMERIC UNIQUE, _rowid_ INTEGER PRIMARY KEY ASC) WITHOUT ROWID; ALTER TABLE t3 RENAME TO t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c3);
```

---

## Crash 112: `98445951a1bcb147` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172097`

```sql
BEGIN IMMEDIATE; PRAGMA foreign_keys=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 113: `f07aa4a53869bca9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172185`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 114: `66dc48f327239d92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177703`

```sql
PRAGMA foreign_keys=1; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 115: `213348eb8d970dab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178539`

```sql
CREATE TABLE t1 (_rowid_ INT UNIQUE, PRIMARY KEY (_rowid_) ON CONFLICT REPLACE, CHECK (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 116: `a2713b60685062fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178693`

```sql
CREATE TABLE t1 (_rowid_ INTEGER COLLATE NOCASE, c1 INT COLLATE NOCASE, PRIMARY KEY (_rowid_) ON CONFLICT REPLACE, CHECK (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 117: `78d6c7dfc3f02abd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179632`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 118: `e98a8144bb11fdfc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179944`

```sql
CREATE TABLE t2 (c3 BLOB PRIMARY KEY DESC); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ATTACH ':memory:' AS db2; DETACH DATABASE db2;
```

---

## Crash 119: `b17a95a1cf4ca4c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180402`

```sql
WITH RECURSIVE t2 AS (SELECT *) SELECT DISTINCT sum(CURRENT_TIME NOTNULL) AS d__u_ ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);
```

---

## Crash 120: `82ef79319b5eef3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180411`

```sql
BEGIN IMMEDIATE; VALUES (X'AABA050AfE') INTERSECT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 121: `362a824c206a9924` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180421`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 122: `3b4e4b522beb5ddc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180429`

```sql
BEGIN IMMEDIATE; CREATE TABLE t1 AS SELECT ALL 0.0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 123: `2993160e3f10fdd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180498`

```sql
PRAGMA foreign_keys=OFF; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 124: `d1eac73e5bc85b7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180509`

```sql
BEGIN IMMEDIATE; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 125: `eeb3fe2300661e21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180520`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 126: `deede2f9909455e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183098`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ TEXT PRIMARY KEY ASC) WITHOUT ROWID; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 127: `a28bb2548322c04e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000120672`

```sql
CREATE TABLE t2 (c3 TEXT COLLATE NOCASE); INSERT INTO t2 VALUES (CURRENT_TIME), (CURRENT_TIME), (count(*) OVER (PARTITION BY RAISE(IGNORE) ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN CURREN
```

---

## Crash 128: `be6652a077714dc1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000121073`

```sql
CREATE TABLE t2 (c3 TEXT COLLATE NOCASE); INSERT INTO t2 VALUES (CURRENT_TIME), (CURRENT_TIME), (count(*) OVER ()); ANALYZE;
```

---
