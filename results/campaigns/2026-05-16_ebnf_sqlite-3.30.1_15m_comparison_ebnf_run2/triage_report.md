# Crash Triage Report

**Total crashes:** 108  
**Unique crash sites:** 108  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 108 | 108 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `2ff1b6068888c231` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000030`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); VACUUM;
```

---

## Crash 2: `24c1799e0aaad1c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000335`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_); SELECT ALL CASE WHEN CURRENT_TIMESTAMP THEN FALSE END AS e_n0_w3_o3nsz_o2r0y__3w18w0u_95x_z_4__m_2k_1_1tsr_mw3
```

---

## Crash 3: `4e3fceae585faa08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000721`

```sql
PRAGMA cache_size=+0; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t3 SET c2 = t3.c1 * CASE WHEN CURRENT_
```

---

## Crash 4: `8323e06c36c9ea71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002665`

```sql
PRAGMA page_size; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t3 SET c2 = t3.c1 * CASE WHEN CURRENT_TIME
```

---

## Crash 5: `5b76e0dc3a7507d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002673`

```sql
PRAGMA page_size; BEGIN IMMEDIATE; COMMIT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t3 SET c2 = t3.c1 * CASE WHEN CURRENT_TIME THEN FALSE WHEN NULL COLLATE NOCASE THEN CURRENT_
```

---

## Crash 6: `d3f7d5538446a4d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002679`

```sql
PRAGMA page_size; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t3 SET c2 = t3.c1 * CASE 
```

---

## Crash 7: `d2213bcc5bad382b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002743`

```sql
PRAGMA page_size; BEGIN IMMEDIATE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); UPDATE t3 SET c2 = t3.c1 * CASE WHEN CURRENT_TIME THEN FALSE WHEN NULL COLLATE NOCASE THEN CURRENT
```

---

## Crash 8: `546fb36e064b6044` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004721`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); VACUUM;
```

---

## Crash 9: `b35678ec7dcad3f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004872`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TEMP VIEW v1 AS SELECT * FROM t1 NOT INDEXED WHERE CURRENT_TIME UNION VALUES (FALSE NOT IN (EXISTS (SELECT
```

---

## Crash 10: `1c588cde49a70a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005205`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 FLOAT COLLATE NOCASE); DROP TABLE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ATTACH DATABASE ':memory:' AS db2;
```

---

## Crash 11: `e26fe452e9153701` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009080`

```sql
PRAGMA analysis_limit=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 12: `588e2dac07098337` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009165`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 13: `2cf282b984d9916e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009396`

```sql
ATTACH ':memory:' AS db2; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 14: `a8c9e70eb76afd9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010810`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ REAL NOT NULL DEFAULT 0.0, rowid BOOLEAN NOT NULL REFERENCES t2 (c1) ON UPDATE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 15: `9cc1a005c5c45ad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014450`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_);
```

---

## Crash 16: `d2f01fb6938ba726` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014480`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_);
```

---

## Crash 17: `539ded89ce3d17ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014821`

```sql
BEGIN EXCLUSIVE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 18: `cbc48a86363c61bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015561`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 19: `d587c121687c7dac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015660`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 20: `6161c96a3c45af02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015718`

```sql
PRAGMA cache_size=-0; BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1);
```

---

## Crash 21: `fe11129236278a69` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016375`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 22: `cc2003b039e9cd5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017696`

```sql
PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 23: `8a342c00dcdf3758` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017799`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 24: `3183bba47c01ad7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017871`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_); VACUUM INTO ':memory:';
```

---

## Crash 25: `749edd3f3b77294f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019514`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 VARCHAR(255) DEFAULT X''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 26: `53f0cedd71d1e38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021964`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 27: `1da8dc5aa0ea45f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022219`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL * ORDER BY NULL NOT IN (SELECT ALL *) ASC, RAISE(IGNORE) DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 28: `c327a2adc7cbbce6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024202`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); ANALYZE; ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 29: `e6072bfb735e6ed7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025416`

```sql
ANALYZE; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3);
```

---

## Crash 30: `8a2599e54ce8b627` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028834`

```sql
VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 31: `6060c591351d5c6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029914`

```sql
CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL * UNION SELECT NULL AS k_03___0_8_j1w9__e5_506qldj_1b6t1_2_d_q_o__42__2___mkk___39___g3511_u0ne_857_07_h__4_cn6___5ucu_219_518h7us3_09t0_5671fp_54_u51_90z_m7
```

---

## Crash 32: `26e3ac89e9f7d938` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030990`

```sql
CREATE VIEW v1 AS SELECT DISTINCT * UNION SELECT DISTINCT total_changes() FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY TRUE ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING
```

---

## Crash 33: `3a674558b4d6d41a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033232`

```sql
ATTACH ':memory:' AS db2; PRAGMA journal_mode=WAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 34: `2c6d6edea4e9f511` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033279`

```sql
ATTACH ':memory:' AS db2; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 35: `28ec58d5fc5496d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046953`

```sql
CREATE TABLE t3 (c3 INT UNIQUE, PRIMARY KEY (c3) ON CONFLICT IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 36: `b1791ce9f42aa6c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047310`

```sql
CREATE TABLE t3 (c3 INTEGER PRIMARY KEY AUTOINCREMENT, CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VACUUM INTO ':memory:';
```

---

## Crash 37: `dc7c95c6ccfb78e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052512`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 NUMERIC UNIQUE, c2 REAL PRIMARY KEY DESC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 38: `7c56050ad4ceb009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054055`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid TEXT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 39: `bb43c7e7a4426a4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054374`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 INTEGER NOT NULL DEFAULT -0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 40: `b28c1fc749277b6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054508`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 NUMERIC UNIQUE, c2 REAL PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 41: `5ba777ceb209b4fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056453`

```sql
BEGIN IMMEDIATE; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 42: `89d201d543ab7066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056672`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 43: `56882745255e42e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056713`

```sql
BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 44: `90356501a7b302b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059353`

```sql
SELECT * UNION SELECT * FROM t1 NATURAL LEFT JOIN t1 NOT INDEXED ON NULL WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURR
```

---

## Crash 45: `bf731c3c0c5d605f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059968`

```sql
PRAGMA cache_size=-0; ANALYZE; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE TRIGGER trg1 BEFORE DELETE ON t1 BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE
```

---

## Crash 46: `1be346b858a08572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066944`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT * FROM t1 NOT INDEXED WHERE FALSE GROUP BY CURRENT_DATE, FALSE HAVING RAISE(IGNORE) ORDER BY TRUE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 47: `2e66dfbe13efaa16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067081`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST ROWS BETWEEN RAISE(IGNORE) PRECEDING AND RAISE(IGNORE) FOLLOWING) FROM t1 NOT INDEXED WHERE FALSE GROU
```

---

## Crash 48: `1bf9a259fe0f2cf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067186`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM t1 NOT INDEXED WHERE FALSE GROUP BY TRUE ORDER
```

---

## Crash 49: `604d94b067b5e748` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067249`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 50: `785a51216ee8fd59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067378`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL *; BEGIN EXCLUSIVE TRANSACTION; ROLLBACK TRANSACTION; ANALYZE; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); COMMIT TRAN
```

---

## Crash 51: `2de6d1bb7d34d33b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067396`

```sql
CREATE TEMP VIEW v1 AS SELECT ALL *; BEGIN EXCLUSIVE TRANSACTION; ROLLBACK TRANSACTION; ANALYZE; BEGIN IMMEDIATE TRANSACTION; DROP VIEW IF EXISTS v1; COMMIT TRANSACTION; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 52: `ade3bc6c473b23e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067606`

```sql
BEGIN EXCLUSIVE TRANSACTION; ATTACH ':memory:' AS db2; ROLLBACK TRANSACTION; PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 53: `1fe2664b73692233` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067744`

```sql
ANALYZE; BEGIN EXCLUSIVE TRANSACTION; ANALYZE; ROLLBACK TRANSACTION; CREATE TEMP VIEW v1 AS SELECT DISTINCT *; SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS (
```

---

## Crash 54: `d32b634ca86d93fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068309`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); 
```

---

## Crash 55: `d66a57897f4fbd55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069629`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 56: `fdba25d5d0d68109` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070100`

```sql
DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 57: `b78efb396023a4cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084016`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); CREATE TRIGGER trg1 AFTER INSERT ON t2 BEGIN DELETE FROM t1; END;
```

---

## Crash 58: `1602b98f208c0301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084324`

```sql
SELECT DISTINCT t2.* FROM t3 AS i___p428km__9n__ap8____zx_7_w04g_39ai_______r25w_ INTERSECT SELECT iif(NULL NOT LIKE CURRENT_DATE, FALSE, FALSE << CURRENT_TIMESTAMP) OVER (ORDER BY CASE WHEN NULL THEN
```

---

## Crash 59: `08d1b98628153069` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092549`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, _rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ATTACH DATABASE ':memory:' AS db2; BEGIN EXCLUSIVE TRANSACTION;
```

---

## Crash 60: `6510ce3e96c1c64e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102569`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_, c3, rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 61: `4257b23d8deb78d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105445`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 BLOB PRIMARY KEY ASC, c1 INTEGER UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 62: `503982510ca2a1c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105824`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 REAL PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); ALTER TABLE t3 ADD COLUMN c3 REAL COLLATE NOCASE; VACUUM INTO ':memory:'; C
```

---

## Crash 63: `1a60e8dfbd994696` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106001`

```sql
CREATE VIEW IF NOT EXISTS v1 (c2) AS VALUES (RAISE(IGNORE)); BEGIN EXCLUSIVE TRANSACTION; ROLLBACK TRANSACTION; ANALYZE; BEGIN IMMEDIATE TRANSACTION; DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 64: `31713b6e61a711c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107986`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (rowid INT COLLATE NOCASE); CREATE TEMP TABLE IF NOT EXISTS t2 (c2 INT NOT NULL REFERENCES t3 (c2) DEFERRABLE INITIALLY DEFERRED, c3 BLOB PRIMARY KEY DESC); CREATE V
```

---

## Crash 65: `5b57e592c53221e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108033`

```sql
REINDEX; CREATE TEMP TABLE IF NOT EXISTS t2 (c2 INT NOT NULL REFERENCES t3 (c2) DEFERRABLE INITIALLY DEFERRED, c3 BLOB PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 66: `363c13ab00eda485` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108041`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (rowid INT COLLATE NOCASE); CREATE TABLE t3 AS VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 67: `89cc7d3df2c739f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109046`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (rowid INT COLLATE NOCASE); CREATE TEMP TABLE IF NOT EXISTS t2 (c3 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 68: `86aa1b620fa1f7b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115826`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT NOT TRUE ISNULL; ANALYZE;
```

---

## Crash 69: `04215c8a5ffdb3ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115832`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, -5363684724024285633636465705758045340724360625156201516681812605473
```

---

## Crash 70: `4aec52fb1763700c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115840`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_TIME COLLATE NOCASE <= CURRENT_DATE; 
```

---

## Crash 71: `4df37fc5ec3a6283` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115846`

```sql
SELECT DISTINCT TRUE BETWEEN NOT +CURRENT_TIMESTAMP == NULL / FALSE IS NOT NULL NOT LIKE CURRENT_DATE ISNULL IS NOT CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP AS g UNION SELECT * FROM t3 WHERE RAISE(IGNO
```

---

## Crash 72: `85b039dc6a4b3fe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115859`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT X'E9eEfccA'; ANALYZE;
```

---

## Crash 73: `242338bcf3a4b65a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115865`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS (), w2 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_DATE; ANALYZE;
```

---

## Crash 74: `931f5f9e37e026e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115872`

```sql
SELECT * FROM (VALUES (-95.08979925047675973694713206579738e-252782745091245475491513017144419901288706134876010199322044250865536668916083435477429972191956892)) AS e UNION SELECT * FROM t3 WHERE RAI
```

---

## Crash 75: `2b63771a26434852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115881`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY changes() FILTER (WHERE CURRENT_TIME) OVER (ORDER BY NULL DESC NULLS LAST, FALSE DESC), CURRENT_TIMESTAMP HAVING FALSE WINDOW w1 AS () ORDE
```

---

## Crash 76: `fb53b62182c2f187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115889`

```sql
SELECT * UNION SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST ROWS BETWEEN RAISE(IGNORE) PRECEDING AND (VALUES (TRUE) INTERSECT SELECT ALL * LIMIT RAISE(IGNORE)) FOLLOWING), * FROM t3 WH
```

---

## Crash 77: `b9bc66ae6576e8f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115895`

```sql
SELECT count(DISTINCT CURRENT_DATE) FILTER (WHERE CURRENT_TIME), CURRENT_TIMESTAMP UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS 
```

---

## Crash 78: `c92b29b895398753` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115906`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY (SELECT DISTINCT *) COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_DATE; ANALYZE;
```

---

## Crash 79: `caaef0d535e222e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115912`

```sql
SELECT * UNION SELECT * FROM (SELECT * FROM (VALUES (CURRENT_TIME)) AS e , t3 ON RAISE(IGNORE)) AS e , t3 ON RAISE(IGNORE) WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLL
```

---

## Crash 80: `55ac96dfed59869e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115928`

```sql
SELECT * UNION SELECT count(*) OVER (ORDER BY CURRENT_TIME DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW) FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WIN
```

---

## Crash 81: `86748870d418e8b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115938`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY FALSE LIKE NULL ESCAPE CURRENT_TIMESTAMP WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_DATE; ANAL
```

---

## Crash 82: `de4b097b90305f39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115944`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_DATE OFFSET last_insert_rowid() FILTE
```

---

## Crash 83: `7b188319a4bd7b17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115966`

```sql
SELECT * UNION SELECT * FROM (VALUES (random() == NULL ISNULL)) AS e WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURRENT_
```

---

## Crash 84: `13fc4838e0f6fc9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115985`

```sql
SELECT * UNION SELECT * FROM t3 WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, --CURRENT_TIMESTAMP REGEXP CURRENT_TIMESTAMP LIKE NULL ->> NULL ISNU
```

---

## Crash 85: `9d8213e167131b3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115997`

```sql
SELECT * UNION SELECT * FROM t2 AS a__ NATURAL LEFT OUTER JOIN t3 AS f0x4e1_yu8__lh09_8_z__9_wc_qe_4w2_0qr_zem8_g_w_vt__7x__4_w____03_a4_1_yx6g__w__ka_06__a___h_sr0_7___t__a9i_2c6_45_0_89sxgh__4g22t6g
```

---

## Crash 86: `c582d4cf5ef2e420` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116075`

```sql
SELECT * UNION SELECT * FROM (t2 NOT INDEXED LEFT OUTER JOIN t1 AS c_) WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) WINDOW w1 AS () ORDER BY TRUE COLLATE BINARY NULLS LAST, CURRENT_DATE ASC LIMIT CURREN
```

---

## Crash 87: `782cb6835a36d00f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119655`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c3, _rowid_);
```

---

## Crash 88: `72f458eda026c3dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121564`

```sql
PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 89: `7975ba230532b76a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121945`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 BOOLEAN REFERENCES t3 (c1) ON DELETE RESTRICT); ALTER TABLE t1 RENAME COLUMN c1 TO c3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 90: `96f78899ec8e0315` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123510`

```sql
CREATE TABLE IF NOT EXISTS t1 (c1 TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 91: `98821e5bd69aca67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126511`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 NUMERIC UNIQUE, c2 REAL PRIMARY KEY DESC) WITHOUT ROWID; ALTER TABLE t2 RENAME TO t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 92: `a08a46bb37095c74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132477`

```sql
SELECT * FROM (VALUES (CURRENT_TIME)) AS e ORDER BY NULL ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 93: `7843c513d32d0517` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134583`

```sql
CREATE TABLE t1 (c3 INTEGER PRIMARY KEY ASC); CREATE INDEX IF NOT EXISTS idx1 ON t1 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); ROLLBACK; CREATE TEMP VIEW IF NOT EXISTS v1 AS 
```

---

## Crash 94: `e961f4598cfa00d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134739`

```sql
CREATE TABLE t1 (c3 INTEGER PRIMARY KEY ASC); CREATE INDEX IF NOT EXISTS idx1 ON t1 (c3); CREATE INDEX IF NOT EXISTS idx1 ON t1 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 95: `777d0b82cc4488a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134818`

```sql
CREATE TABLE t1 (c3 INTEGER PRIMARY KEY ASC); VACUUM; CREATE INDEX IF NOT EXISTS idx1 ON t1 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 96: `387affd11bdd7304` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134825`

```sql
CREATE TABLE t1 (c3 INTEGER PRIMARY KEY ASC); CREATE INDEX IF NOT EXISTS idx1 ON t1 (c3); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 97: `66b0656c94ebfdcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135222`

```sql
CREATE TABLE t3 (c3 INTEGER PRIMARY KEY AUTOINCREMENT, CHECK (FALSE NOT IN (CURRENT_TIME))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 98: `ec7c3254cbff5ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135454`

```sql
CREATE TABLE t3 (c2 BOOLEAN CHECK (NULL), CHECK (TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 99: `244a738b2e6a4d0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136099`

```sql
PRAGMA synchronous=NORMAL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE VIEW v1 AS SELECT t2.* FROM t2 NOT INDEXED GROUP BY TRUE LIKE CURRENT_TIMESTAMP ORDER BY NULL <> CURRENT_TIM
```

---

## Crash 100: `a4231e5e596c3cb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138284`

```sql
CREATE TABLE t2 (_rowid_ VARCHAR(255) PRIMARY KEY ASC) WITHOUT ROWID; PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 101: `3bd81887b84038b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157567`

```sql
VALUES (CAST(CURRENT_TIME AS BOOLEAN)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 102: `bca111387d60f7ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157652`

```sql
VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 103: `8be2b2e1d3ba3838` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166091`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 VARCHAR(255) CHECK (CURRENT_TIME IS TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3);
```

---

## Crash 104: `bcdc62729b3926f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167454`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); UPDATE OR ABORT t2 SET _rowid_ = -c3; DELETE FROM t3; R
```

---

## Crash 105: `5c8561b925eb4301` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168836`

```sql
PRAGMA foreign_keys=ON; CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ TEXT REFERENCES t3 (_rowid_) ON DELETE CASCADE, c3 INTEGER PRIMARY KEY AUTOINCREMENT, c1 REAL REFERENCES t2 (c1) ON UPDATE SET NULL)
```

---

## Crash 106: `bd126ab87e531a3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169028`

```sql
PRAGMA foreign_keys=ON; CREATE TEMP TABLE IF NOT EXISTS t3 (_rowid_ TEXT REFERENCES t3 (rowid) ON DELETE CASCADE, rowid TEXT PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_ro
```

---

## Crash 107: `afbd73841ce4a8c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177870`

```sql
VALUES (FALSE) EXCEPT SELECT ALL NULL LIMIT CURRENT_TIME IS TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); CREATE INDEX IF NOT EXISTS idx1 ON t2 (c2); ANALYZE t2;
```

---

## Crash 108: `08aea9358aeeb764` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187629`

```sql
CREATE TEMP VIEW v1 AS WITH RECURSIVE t1 (c2) AS (SELECT ALL CURRENT_DATE) SELECT DISTINCT TRUE == CURRENT_TIME, RAISE(IGNORE) OR CURRENT_DATE FROM (t1) WHERE CURRENT_DATE NOT LIKE NULL GROUP BY NOT N
```

---
