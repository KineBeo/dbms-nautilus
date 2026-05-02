# Crash Triage Report

**Total crashes:** 257  
**Unique crash sites:** 257  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 257 | 257 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `94c0a47d4bf27738` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000263`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; ANALYZE p; CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) PRIMARY KEY); CREATE TABLE 
```

---

## Crash 2: `8ab09e1d39073051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000448`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_TIME ISNULL COLLATE NOCASE % -CURRENT_DATE REGEXP TRUE COLLATE BINARY GLOB CURRENT_TIMESTAMP AS j8_88_c3_u3r_b5q6_8t__q, r.*, CU
```

---

## Crash 3: `b9827dd6348cd01b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000519`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c1, c1); SELECT CURRENT_TIME ISNULL IS DISTINCT FROM CASE WHEN FALSE = RAISE(IGNORE) NOT NULL THEN CURRENT_TIMESTAMP ELSE CURRENT_TIMESTAMP 
```

---

## Crash 4: `6ceacaf7d1dc1e25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001101`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT changes() == CURRENT_TIMESTAMP != CURRENT_TIMESTAMP = count(*) FILTER (WHERE FALSE) OVER ()
```

---

## Crash 5: `4b7d87b9613e7632` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001115`

```sql
SELECT substr('-6v9OU ', 2147483647, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE q (_rowid_, a, b) AS (SELECT *, q.*) SELECT NULL MATCH NOT CASE CURRENT_DATE > FALSE 
```

---

## Crash 6: `0021663e36880d4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001362`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, c2, c2, a, c3); REPLACE INTO t1 VALUES (+CAST(TRUE AS BOOLEAN) & CASE WHEN CURRENT_DATE < CURRENT_DATE THEN TRUE IS DISTINCT FROM FALSE ELSE
```

---

## Crash 7: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001424`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 8: `c50b073466d90ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001951`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (TRUE == NOT CURRENT_DATE == NULL << FALSE COLLATE RTRIM >> 
```

---

## Crash 9: `09b1ccf89b637db9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001974`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT FALSE FROM p NATURAL JOIN q WHERE CASE +RAISE(IGNORE) WHEN CURRENT_TIMESTAMP COLLATE B
```

---

## Crash 10: `9066a7223939a06d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002100`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL
```

---

## Crash 11: `475d83d195425068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003325`

```sql
SELECT printf('%.*g', 2147483647, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.*, CURRENT_TIME NOT LIKE CURRENT_TIME AS a FROM p WHERE EXISTS (SELECT total_changes() EXCEPT
```

---

## Crash 12: `f2f43edb13004ca2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003332`

```sql
SELECT printf('%.*g', 2147483647, 1.0); CREATE TABLE IF NOT EXISTS p(a NUMERIC NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 13: `8ba4c6fdc811c766` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003490`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 VALUES (NULL OR FALSE COLLATE RTRIM OR NOT NULL MATCH TRUE + CASE FALSE WHEN RAISE(IGNORE) ->> CU
```

---

## Crash 14: `70b737ccfc169402` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 15: `751d7e9c04cb9264` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003695`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM (SELECT *) AS s_ WHERE NULL UNION ALL SELECT * FROM q GROUP BY FALSE, CURRENT_DATE; EXPLAIN QU
```

---

## Crash 16: `3fe23a854ce1da57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003725`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM s NOT INDEXED WHERE NULL UNION ALL SELECT * FROM q GROUP BY FALSE, CURRENT_DATE; EXPLAIN QUERY
```

---

## Crash 17: `7477acd15f24e01d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004103`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(_rowid_ INTEGER); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELECT +CASE 
```

---

## Crash 18: `fbd69518588eb3f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004934`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q (c1) AS (SELECT *) SELECT CURRENT_TIME AS uz_7aq_8_q, CASE NULL WHEN CURRENT_DATE THEN NOT FALSE END F
```

---

## Crash 19: `0e1fda94a151989e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005021`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q (c1) AS (SELECT *) SELECT *, CASE NULL WHEN CURRENT_DATE THEN NOT FALSE END FROM p; CREATE VIRTUAL TAB
```

---

## Crash 20: `76e90818083c7c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005029`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE q (c1) AS (SELECT *) SELECT *, TRUE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INS
```

---

## Crash 21: `61a947cf1d95699d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005925`

```sql
SELECT substr('Ne U r', -9223372036854775808, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q VALUES ((RAISE(IGNORE)) AND CURRENT_TIME <= FALSE < CURRENT_TIMESTAMP NOTNULL 
```

---

## Crash 22: `fc7ac28814ca48d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005961`

```sql
SELECT substr('-_--L- e', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT p.* FROM (SELECT TRUE << CURRENT_DATE / FALSE COLLATE NOCASE BETWEEN CURRENT_DATE AND (CURRENT_DA
```

---

## Crash 23: `9b2923f6f8c3df9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007423`

```sql
SELECT substr('_XU_ut__-BF  -_---', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q (c2) AS NOT MATERIALIZED (SELECT p.* ORDER BY FALSE IS NULL LIKE TRUE IS NOT
```

---

## Crash 24: `6eff19bb23395e96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010850`

```sql
SELECT printf('%.*f', -2147483648, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p SELECT * EXCEPT VALUES (TRUE) ORDER BY ~NULL % TRUE AND CURRENT_DATE AND FALSE -> ~R
```

---

## Crash 25: `60994a7943797197` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016270`

```sql
SELECT printf('%x', -1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT *, s.* FROM t1 NATURAL JOIN p WHERE (WITH RECURSIVE p AS (SELECT * UNION ALL VALUES (RAISE(IGNORE))) SELECT
```

---

## Crash 26: `9ade9e35a3ce7c61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018638`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY FALSE HAVING FALSE); SELECT 
```

---

## Crash 27: `87d99d0209478131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019781`

```sql
SELECT substr('Ne U r', -9223372036854775808, 0); SELECT printf('%.*g', 4294967295, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_); INSERT INTO p VALUES (zeroblob((SELECT DI
```

---

## Crash 28: `b0744d0719f364df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020182`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 29: `cbd145f65da72807` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020191`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF 
```

---

## Crash 30: `63abe553dcd7ebc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020266`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255), rowid
```

---

## Crash 31: `ac078957b7c305fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020502`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 32: `602187a78c455250` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021034`

```sql
SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; PRAGMA quic
```

---

## Crash 33: `10bd81dfcd613763` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022897`

```sql
SELECT printf('%.*g', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 34: `241633267120cfb3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023462`

```sql
SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 35: `e1cb6ec74f6e3b72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023922`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, 
```

---

## Crash 36: `067dd05a16c8eb88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023945`

```sql
SELECT printf('%lli', -2147483649, ''); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 37: `3ccef4ce1a9ddfc7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025493`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CU
```

---

## Crash 38: `aa3c56ea08a1ea67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026331`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE t3 AS (VALUES (CURRENT_DATE)) SELECT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 39: `003d5c732e2f6eb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027208`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); 
```

---

## Crash 40: `dae89a85733e1282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027466`

```sql
SELECT round(-1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; SELECT hex(zeroblob(2147483647));
```

---

## Crash 41: `49268607bb4b335b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028217`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 42: `d90997c853491d71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028444`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLL
```

---

## Crash 43: `7d0281d64f7d151a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028751`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 44: `d98315a925439a1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028930`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE
```

---

## Crash 45: `9d1bd7720e95b65e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028999`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_TIMESTAMP), c2 BOOLEAN PRIMARY KEY, rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA
```

---

## Crash 46: `7e9339473d469a0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031958`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check;
```

---

## Crash 47: `7f36ec78f878e61b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035208`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (FALSE) INTERSECT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 48: `5ed4fd5b05a1570e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (FALSE) INTERSECT VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY FALSE ORDER BY CURRENT_DAT
```

---

## Crash 49: `2821401c84b9e0a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037437`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM (SELECT last_insert_rowid() OVER (ORDER BY CURRENT_TIME ASC ROWS BETWEEN CURRENT_TIME PRECEDIN
```

---

## Crash 50: `c4b48b059e485b76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037456`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)) UNION ALL SELECT * FROM q GROUP BY FALSE, CURRENT_DATE; EXPLAIN QUERY PLAN VALUES (CURRENT_TIM
```

---

## Crash 51: `a3110dcb562bff21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037471`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM (SELECT last_insert_rowid() OVER () NOT IN (NULL) AS b6so) AS s_ WHERE NULL UNION ALL SELECT *
```

---

## Crash 52: `8c12eeb05ea328af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037478`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM (SELECT last_insert_rowid() OVER (ORDER BY CURRENT_TIME ASC ROWS BETWEEN CURRENT ROW AND UNBOU
```

---

## Crash 53: `ec7a3025b0ff22d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038112`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p (c1) AS (VALUES (CURRENT_TIMESTAMP)) SELECT NOT last_insert_row
```

---

## Crash 54: `092b97e386762872` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038338`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p (c1) AS (VALUES (CURRENT_TIMESTAMP)) SELECT NOT CURRENT_DATE IS
```

---

## Crash 55: `06538b9abf886ea9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039131`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 56: `b2d4a415fb88e006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042251`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN VALUES (TRUE) INTERSECT SELECT DISTINCT * FROM q; SELECT printf('%.*f', -2147483649, 1e30
```

---

## Crash 57: `e9db1a980b1778d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044614`

```sql
SELECT printf('%s', 4294967295, ' 8 _---KZ1'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c1); INSERT INTO p (_rowid_) VALUES (c1 IS min(CASE CURRENT_DATE NOT BETWEEN CURRENT_TIME AN
```

---

## Crash 58: `d8089d133c68cdae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048524`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE TRUE WHEN CURRENT_TIME THEN CURRENT_TIME END; SELECT substr('I_0 1N
```

---

## Crash 59: `e13b808ce3a287fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048885`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE TRUE WHEN CURRENT_TIMESTAMP COLLATE BINARY THEN CURRENT_TIME END; S
```

---

## Crash 60: `422c3c10e541ed77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050070`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT TRUE, c2 BLOB UNIQUE, c3 NUMERIC DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 61: `b662720279521dd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050211`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, c2 BLOB UNIQUE, c3 NUMERIC DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 62: `f6462fd5c4405e5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050229`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL, a FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 63: `7fba3353bb8fbe2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051337`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483648)); CREATE VIR
```

---

## Crash 64: `e906df5a4c400c28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051789`

```sql
SELECT printf('%.*d', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT p.*, group_concat(CASE WHEN TRUE THEN CURRENT_TIME END, 'v-') FILTER (WHERE FALSE COLLATE RTRIM) OV
```

---

## Crash 65: `afc35d78ae68d497` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051883`

```sql
SELECT substr('_h', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1); INSERT INTO p (c1, c1) VALUES ((FALSE)); SELECT CURRENT_DATE ->> CURRENT_DATE IS NULL AS a, 
```

---

## Crash 66: `94351a6a19fbcb1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052762`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE TRUE + NULL % CURRENT_DATE IS 
```

---

## Crash 67: `88de8b69526455da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052950`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE TRUE; SELECT printf('%.*g', -2
```

---

## Crash 68: `8b74c3a090beee43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052956`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT INTO q DEFAULT VALUES; SELECT * FROM q NATURAL JOIN q WHERE TRUE + TRUE; SELECT printf('%.
```

---

## Crash 69: `8d83f29fa39906c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053643`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT, _rowid_ TEXT UNIQUE); SELECT CURRENT_DATE FROM q JOIN q a ON CURRENT_TIME; SELECT printf('%.*f', -2147483649, 1e
```

---

## Crash 70: `6a9bff55be932556` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053744`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT, _rowid_ TEXT UNIQUE); SELECT * FROM q JOIN q a ON CURRENT_TIME; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 71: `0633e04191b78793` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055349`

```sql
SELECT substr('Q9___ ', 2147483647, 4294967296); SELECT printf('%.*f', -2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR REPLACE INTO t2 VALUES (NOT EXISTS (VA
```

---

## Crash 72: `f5fdd3d9fe9c323e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055912`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT TRUE, c2 BLOB UNIQUE, c3 NUMERIC DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE); SELECT printf('%.*g', 4294967295); CREATE VIRT
```

---

## Crash 73: `4c82146b6158afc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056390`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE X'' WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME END; CREATE VIRTUAL TA
```

---

## Crash 74: `135746849b0af27d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056561`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE CURRENT_DATE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME END; CREATE V
```

---

## Crash 75: `006de3b537c0fccb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057399`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE / CURRENT_DATE == CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 76: `ecb09ae5e885b95a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058244`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 DATE DEFAULT 8556844156906104057720089949265274.2601642142704E-00349304914869); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_D
```

---

## Crash 77: `c6f466ad3c6db408` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058352`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN NOT NULL DEFAULT X'd5A9cb', rowid DATE NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; SELECT 
```

---

## Crash 78: `c51131b78b8678b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058562`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ BOOLEAN NOT NULL DEFAULT TRUE, rowid DATE NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; SELECT print
```

---

## Crash 79: `35b547bccc968534` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058988`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE NULL IS NOT NULL <= NULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 80: `dac3742180b7d6b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059134`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME <= NULL; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 81: `213e89dc2b82462a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060842`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIME, TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || 
```

---

## Crash 82: `73705684d6ddda70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060852`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIME, TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 83: `94a87d7851b5893c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060897`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIME, TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || 
```

---

## Crash 84: `3fa76b5f0232f9db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060906`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIME, TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || 
```

---

## Crash 85: `09b12a6666618ebd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074581`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER BY sum(NOT EXISTS 
```

---

## Crash 86: `9a9f9a96e87f01c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075409`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY NOT EXISTS (VALUES (FA
```

---

## Crash 87: `659992945773cd41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075854`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_DATE ASC, +FAL
```

---

## Crash 88: `752bef06e04b70b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075895`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY CURRENT_TIME DESC NULL
```

---

## Crash 89: `8c4b7fbebc3c84dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079543`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE); SELECT DISTINCT FALSE FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 90: `674ebd0099bc1fbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079561`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (FALSE); SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT 
```

---

## Crash 91: `1d963edd08915fcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080606`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (TRUE || FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 92: `ba07ba8c1cecb9b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080821`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a + 0) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 93: `c5fd06b0fe1b410f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081302`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (FALSE)) AS a LEFT OUTER JOIN p NO
```

---

## Crash 94: `2bc7b2ecc39cbc23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081782`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a = 0) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 95: `d7b052bafe00fd95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082545`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (CURRENT_TIME)) SELECT * FROM q; SELECT hex(zeroblob
```

---

## Crash 96: `d753222a7983fd75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082895`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p AS (SELECT *) SELECT count(DISTINCT TRUE) AS u FROM q; CREATE V
```

---

## Crash 97: `fc4b0c87caab0c8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083695`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE t3 AS (VALUES (TRUE)) SELECT trim(_rowid_) AS u FROM q; SELECT pr
```

---

## Crash 98: `efe4962b0f5d328e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083815`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE t3 AS (VALUES (TRUE)) SELECT changes() AS u FROM q; SELECT printf
```

---

## Crash 99: `a668fb53cbafbf8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084126`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBAC
```

---

## Crash 100: `389be1f7c8b751c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084202`

```sql
SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO r VALUES (CASE WHEN FALSE NOT NULL COLLATE BINARY IS NOT CURRENT_TIME | CUR
```

---

## Crash 101: `c051f50089321737` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089560`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); SELECT DISTINCT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (CURRENT_TIME); SELECT printf('%
```

---

## Crash 102: `dfc7066762d7aff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092398`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT OR FAIL INTO q VALUES (~TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 103: `86e505c42f345255` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097022`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (), NULL); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 104: `4d8c943f005811cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097579`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO 
```

---

## Crash 105: `1d4a28edfb5313fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097592`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO 
```

---

## Crash 106: `e8d5e477782850bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097638`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (NULL); SELECT * FROM p GROUP BY CURRENT_TIME; SELECT hex(zeroblob
```

---

## Crash 107: `1f30a16ed6ef207e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097764`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (FALSE < NULL IS NOT TRUE)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p 
```

---

## Crash 108: `72e6ac8cffc9b3e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097892`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (NULL)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME
```

---

## Crash 109: `c368f692312e47d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097930`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (X'' IS NOT TRUE)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO 
```

---

## Crash 110: `4742a24cccd20e50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098307`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE IS NOT TRUE IS NOT TRUE)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 111: `69d3ee6f316f6b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100255`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE ||
```

---

## Crash 112: `7b9e89f67e0273c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(NULL AS DATE))); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT length(TRUE) NOT IN (SELECT NULL ORDER BY -TRUE DESC NULLS FIRST) AS a; SELECT
```

---

## Crash 113: `4a60f5108c16b6bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100873`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT NULL ORDER BY TRUE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 114: `d060ba9ba0cfc3af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, rowid NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 115: `65907ee3822e1b9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN PRIMARY KEY, rowid NUMERIC UNIQUE); SELECT TRUE FROM p NATURAL JOIN q WHERE CURRENT_TIME; SELECT printf('%.*g', -214748364
```

---

## Crash 116: `a77cfa48f1c1e74e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105947`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE, a INTEGER UNIQUE); SELECT NULL FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 117: `917510e2e63bc331` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106152`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 118: `d9ef630b9be603cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106492`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER UNIQUE); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255)); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 119: `fd7fc4e27a1613f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107232`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c1 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b VARCHAR(25
```

---

## Crash 120: `35200caf7890be64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107791`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, _rowid_ TEXT NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 121: `6874545e77e2e21c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107969`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT '--Y-', c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 122: `2237dd612f28aa20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108130`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT FALSE, c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 123: `14856773b0a35a57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108150`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT CURRENT_TIME, c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 124: `11684e55a24e0d7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108162`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, _rowid_ TEXT NOT NULL DEFAULT X'5602'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f',
```

---

## Crash 125: `16237a029645f4b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108313`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, b GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a INTEGER DEFAULT 1522215.221993027290948378221581834872833516988945415102853291029536E23509581484150800015612508668
```

---

## Crash 126: `5196a8ac14f6b5e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108495`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, b GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a INTEGER DEFAULT CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 127: `d74d259cd813955a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109710`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED LEFT JOIN p NOT INDEXED USING (rowi
```

---

## Crash 128: `523d8ae40945f597` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109903`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (NULL)); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 129: `6cf45bb5f9744438` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110876`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM (p NOT INDEXED INNER JOIN p AS i1a700__9__5b3d6_b17_ys0___5q___
```

---

## Crash 130: `7e5a81b53a014bbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112527`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255), c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p GROUP BY FALSE); CREATE VIRT
```

---

## Crash 131: `b014504cce644b8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113001`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE, a TEXT GENERATED ALWAYS AS (-NULL) STORED); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP
```

---

## Crash 132: `438ad44ad7e331a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114020`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING TRUE NOT I
```

---

## Crash 133: `7ddd566cef290f13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114145`

```sql
SELECT round(1e-308, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q VALUES (CURRENT_DATE); SELECT TRUE - CURRENT_TIME FROM p JOIN s l__k04__96_u_a7k1_359
```

---

## Crash 134: `36443662a8bf2761` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115430`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (TRUE) INTERSECT VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL
```

---

## Crash 135: `81df286190cbdfea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115518`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY FALSE NOT IN (VALUES (CURRENT_
```

---

## Crash 136: `1fc724eea4e0157c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115866`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT -0); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY TRUE); SELECT printf('%.*g', -
```

---

## Crash 137: `4f50204520866930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116250`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT DISTINCT * FROM (SELECT CURRENT_TIME COLLATE BINARY AS j_4) 
```

---

## Crash 138: `c643e9a6e51814fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116852`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (count(*) OVER (), NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 139: `e032aa887f477cc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116983`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (WITH p (c2) AS (VALUES (NULL)) SELECT DISTINCT * FROM (VALUES (CURRENT_TIM
```

---

## Crash 140: `d131ad9cb6b96348` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118057`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 DATE NOT NULL, rowid BLOB GENERATED ALWAYS AS (TRUE) VIRTUAL); SELECT * FROM q WHERE EXISTS (VALUES (RAISE(IGNORE))); CREATE V
```

---

## Crash 141: `b2af0fdce7069382` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118383`

```sql
SELECT printf('%.*d', -2147483649, 1e308); SELECT printf('%.*d', 2147483647, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT NULL IS NULL, CURRENT_TIME COLLATE NOCASE = TRUE I
```

---

## Crash 142: `6f8d67d093ce09f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118766`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_DATE AS q__9u_4g_ FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP
```

---

## Crash 143: `22960fdfd3300ffa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119168`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING FALSE AND TRUE); CREA
```

---

## Crash 144: `56e664b240c9d424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119431`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING FALSE ISNULL); CREATE
```

---

## Crash 145: `b01267af0e330080` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119572`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY NULL HAVING EXISTS (VALUES (NULL))); CREA
```

---

## Crash 146: `501c0cd6625dc2e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119760`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF 
```

---

## Crash 147: `761f9a368c654410` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000143605`

```sql
SELECT printf('%.*s', 0); SELECT printf('%d', 4294967295, '4fv4'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c2); WITH RECURSIVE p (a, b) AS (VALUES (FALSE) EXCEPT SELECT *) SELECT *
```

---

## Crash 148: `81e8bb1a62cf64e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144005`

```sql
SELECT printf('%d', -9223372036854775808, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c2, c3); INSERT OR FAIL INTO t1 VALUES (CURRENT_DATE IS CAST(NULL COLLATE NOCASE || TRUE NOT NULL
```

---

## Crash 149: `ec8cd139559934a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147104`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL); SELECT DISTINCT count(*) AS q__9u_4g_ FROM p NOT INDEXED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 150: `faf16a16fd4c5517` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162880`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE DEFAULT FALSE, rowid FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY F
```

---

## Crash 151: `ec1326052b14543e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163320`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING NULL BETWE
```

---

## Crash 152: `af8fdbb8738cc1bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164108`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING CASE WHEN 
```

---

## Crash 153: `3b5e49a938ddcf4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164182`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME HAVING CASE WHEN 
```

---

## Crash 154: `33492dc8214499e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164265`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT count(*) AS q__9u_4g_, * FROM p NOT INDEXED GROUP BY CURRENT
```

---

## Crash 155: `5b03ef7c4afb7ba0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (count(*) OVER (), NOT EXISTS (VALUES (CURRENT_TIMESTAMP) IN
```

---

## Crash 156: `7e907497d4ebaadf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000166840`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (count(*) OVER (), CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE
```

---

## Crash 157: `7b1ef47bbcc8f384` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168572`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); SELECT * FROM q WHERE EXISTS (SELECT c1 AS e_ FROM p NOT INDEXED LEFT JOIN p NOT INDEXED USIN
```

---

## Crash 158: `db4fbe3b0123f5a1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169863`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL, c3 DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 159: `ee376b9687befcce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170080`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, b GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a INTEGER DEFAULT ' - '); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 0
```

---

## Crash 160: `5ec368d6562599a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170520`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT, b GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE, a INTEGER DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 161: `76aeedf05c481ec3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170839`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT FALSE, c1 BLOB UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 162: `9a7fe9ca340a6b86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170926`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, _rowid_ TEXT NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TA
```

---

## Crash 163: `423efb31f97f2f81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173424`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); SELECT max(CURRENT_DATE) FILTER (WHERE TRUE) OVER (PARTITION BY TRUE ORDER BY FALSE ROWS BETWEEN FALSE PRECEDING A
```

---

## Crash 164: `1b1793cca2d0e154` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173559`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); SELECT max(CURRENT_DATE) FILTER (WHERE TRUE) OVER (PARTITION BY TRUE ORDER BY FALSE ROWS BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 165: `9dccce1ea038f88b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173774`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL); SELECT max(CURRENT_DATE) FILTER (WHERE TRUE) OVER () NOT LIKE count(*) FILTER (WHERE TRUE) OVER () FROM p NATURAL 
```

---

## Crash 166: `328e12e7f605ea6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177397`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || CAST(CURRENT_DATE AS DATE) || FALSE || FALSE
```

---

## Crash 167: `5c5d706e088b7cbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177440`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE IN (rowid) || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE 
```

---

## Crash 168: `0a5594c1212c03b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177446`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || CAST(CAST(TRUE IS NOT TRUE AS DATE) AS VARCHAR(255)) || FALSE || FALSE || FALSE 
```

---

## Crash 169: `bb22a35e1883a15f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177458`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || trim(trim(trim(trim(_rowid_)))) || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || 
```

---

## Crash 170: `fbbea215ce4994a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177483`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || 00158474957125067237289217472586464082468.9608e4 || FALSE || FALSE || FALSE || FALSE || FALSE || F
```

---

## Crash 171: `4a452cf798c58c81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177522`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || (0) || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || F
```

---

## Crash 172: `05bb9b2ff3d8be31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177593`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || TRUE || 
```

---

## Crash 173: `8c9abf119741b687` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179856`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE NOT IN (CURRENT_TIMESTAMP) IS NOT TRUE IS NOT TRUE)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 174: `bc57964cabde86b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179884`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIMESTAMP IS NOT TRUE IS NOT TRUE)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3)
```

---

## Crash 175: `a2f4e7302ae21e0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179890`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (TRUE NOT IN (CURRENT_TIMESTAMP) IS NOT CURRENT_TIME)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 176: `7d521c4ddbe0ea8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180533`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (NULL IS NOT FALSE)); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO q VALUES 
```

---

## Crash 177: `a42f509f80d2c3fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180831`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(FALSE || 00158474957125067237289217472586464082468.9608e4 AS DATE) IS NULL)); INSERT OR REPLACE INTO p VALUES (NULL); VALUES (TRUE); SELECT hex(zeroblo
```

---

## Crash 178: `df61336bb269ce94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181177`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CURRENT_TIME IN (TRUE, TRUE, CURRENT_TIME))); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT 
```

---

## Crash 179: `62e6f256cd4e0344` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181857`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES ((VALUES (TRUE))); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 180: `6e0000ff1d1bc8e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183988`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p VALUES (TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 181: `b89f3953ae385158` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184438`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); INSERT INTO p VALUES (TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE); VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 182: `bfb18b52a15003d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186041`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) DEFAULT 848.3213e+48); CREATE TABLE IF NOT EXISTS q(b BOOLEAN NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 183: `342afa09e24ac9b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186689`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); INSERT OR FAIL INTO q VALUES (CAST(FALSE || 00158474957125067237289217472586464082468.9608e4 AS DATE))
```

---

## Crash 184: `b2f88b20744a0f4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186803`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(b BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER PRIMARY KEY); INSERT OR FAIL INTO q VALUE
```

---

## Crash 185: `5199f3814fe33a01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186869`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN CHECK (CURRENT_TIMESTAMP), c2 INT CHECK (CURRENT_TIMESTAMP), rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALU
```

---

## Crash 186: `6bd65691c2493693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189491`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT X'9De65b1DAb6F5d'; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 187: `e0dc0b1a92e1ff72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189614`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(rowid); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE); SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 188: `bdd60ad9f125521d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL) UNION SELECT * FROM p GROUP BY CURRENT_TIME ORD
```

---

## Crash 189: `d4cb3093142f3e55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190124`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (count(DISTINCT CURRENT_DATE) FILTER (WHERE CURRENT_DA
```

---

## Crash 190: `ce00dcccacc81013` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192591`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (count(*) FILTER (WHERE CURRENT_DATE) OVER (PARTITION BY NULL ORDER BY CURRENT_DATE ASC NULLS FIR
```

---

## Crash 191: `a226225f198185f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192805`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (CURRENT_DATE) INTERSECT VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY FALSE ORDER BY CURR
```

---

## Crash 192: `ca8c664cd4a0a0ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193210`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT DISTINCT * FROM p NATURAL JOIN p UNION ALL VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY F
```

---

## Crash 193: `b5d5843749566bb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193402`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (NULL) UNION ALL VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY FALSE ORDER BY CURRENT_DATE
```

---

## Crash 194: `0d89e5ede6da8531` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193408`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY FALSE ORDER BY CURR
```

---

## Crash 195: `2edad9919eef84b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193414`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT DISTINCT * FROM p NOT INDEXED UNION ALL VALUES (CURRENT_DATE) UNION SELECT * FROM p GROUP BY FALS
```

---

## Crash 196: `8ac8fded719e5afc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193617`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); VALUES (FALSE) INTERSECT VALUES (NULL COLLATE RTRIM) UNION SELECT * FROM p GROUP BY FALSE ORDER BY NULL 
```

---

## Crash 197: `b21aee0e01cc2d98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195224`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT quote(CURRENT_DATE) AS u FROM q; CREATE VI
```

---

## Crash 198: `16546e4b6af9924b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195388`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p (c1) AS (VALUES (CURRENT_TIMESTAMP)) SELECT quote(TRUE) AS u FR
```

---

## Crash 199: `ba6fa788e8535ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196096`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE t3 AS (VALUES (TRUE)) SELECT trim(trim(trim(trim(trim(trim(trim(t
```

---

## Crash 200: `a40d498a806d5052` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196664`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p AS (SELECT *) SELECT NOT count(*) AS u FROM q; CREATE VIRTUAL T
```

---

## Crash 201: `9113cc33aa58a465` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197557`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE p AS (SELECT *) SELECT max(NULL) FILTER (WHERE TRUE) OVER () FROM
```

---

## Crash 202: `9b79e2b53aae27cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198552`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE c3 == CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 203: `63ac43becf797314` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198742`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP == CURRENT_DATE; SELECT printf('%.*g', -2147483649, 0.
```

---

## Crash 204: `b4c785d7612e91c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198933`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); 
```

---

## Crash 205: `a4a896acaa238512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199287`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 206: `093a83ed8ca794b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199747`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(FALSE || 00158474957125067237289217472586464082468.9608e4 AS DATE))); INSERT INTO p SELECT TRUE; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT hex(z
```

---

## Crash 207: `e3d244e87b2a559c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200377`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (max(FALSE COLLATE BINARY)); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 208: `c153e1e5fa79a495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200689`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p GROUP BY FALSE, NULL; SELECT printf('%.*f', -2147483649, 1e308);
```

---

## Crash 209: `4fc8255dbad489f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202874`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p VALUES (X''); SELECT * FROM p NATURAL JOIN p WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE VIRTU
```

---

## Crash 210: `ab54ddbc7c643995` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204863`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY count(*) OVER (ORDER B
```

---

## Crash 211: `155b717fbe0cf82a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205220`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT ALL * FROM (SELECT ALL * FROM p ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST LIMIT N
```

---

## Crash 212: `21052722df13816b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE GROUP BY TRUE WINDOW w1 AS () ORDER BY FALS
```

---

## Crash 213: `39a74ac77e2a08cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207174`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE FALSE LIKE CURRENT_TIMESTAMP COLLATE RTRIM GROUP BY CURRENT_DATE WI
```

---

## Crash 214: `de042838815ccc84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208514`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM p) AS a LEFT OUTER JOIN p WHERE TRUE GROUP BY CURRENT_TI
```

---

## Crash 215: `d3157369480366eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209742`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM p LEFT JOIN q NOT INDEXED ON CURRENT_TIME) AS a NATURAL 
```

---

## Crash 216: `892b7b45f387a6e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210016`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (NULL)) AS a NATURAL JOIN p WHERE CURRENT_TIMESTAMP GROUP BY CURREN
```

---

## Crash 217: `fa86ab80d5935390` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212503`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(FALSE || 00158474957125067237289217472586464082468.9608e4 AS DATE))); INSERT INTO p VALUES (TRUE) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 218: `526f4213304d0cdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226484`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CASE WHEN CURRENT_DATE THEN CURRENT_DATE ELSE CURRENT_TIMESTAMP END LIMIT CURRENT_TIME, TRUE || FALSE || FALSE || FALSE || FALSE |
```

---

## Crash 219: `14f5c60ae68e5197` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226497`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_TIME AS q__d LIMIT CAST(nullif(NULL, NULL) NOT IN (CURRENT_TIME, FALSE, CURRENT_TIMESTAMP) AS INT), TRUE || FALSE || FALSE
```

---

## Crash 220: `c396df04ee637291` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226587`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b, c3, c2); SELECT CURRENT_TIME AS q__d LIMIT CURRENT_TIME, TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE |
```

---

## Crash 221: `02fd677232367d4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229840`

```sql
CREATE TABLE IF NOT EXISTS p(b INT DEFAULT X'a8Bae0bCcCfFca'); CREATE TABLE IF NOT EXISTS q(c2 REAL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 222: `ce7cf5e685f933bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BLOB DEFAULT 8556844156906104057720089949265274.2601642142704E-00349304914869); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_D
```

---

## Crash 223: `e5964c10fa144e99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230342`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME IN (TRUE, TRUE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 224: `4388668d3a1e3b96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230522`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME IN (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 225: `3a4295ec6003f824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230528`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME IN (TRUE, CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 226: `a2413030b0994b42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP IS TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 227: `8efc9789dd65af3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231118`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE / TRUE || FALSE == CURRENT_TIME; SELECT printf('%.*g', -2147483649
```

---

## Crash 228: `53c248c8abbc0e8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231494`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME IS FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 229: `868da70dcb410245` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232696`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME == q.rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 230: `c7ba4864fa2c5a7d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232927`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT NOT NULL DEFAULT '- - _E9_Q- Xu16d'); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; SELECT printf('%.*f',
```

---

## Crash 231: `1e106b285ccb9c10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233106`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE == c3 == c3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 232: `4d308a2142033547` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233273`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP OR FALSE || FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 233: `14b8428ccd71592c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233707`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE TRUE WHEN CURRENT_DATE || FALSE || FALSE || FALSE || FALSE || FALSE
```

---

## Crash 234: `bb5ba8886ba34009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233970`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE X'488FDB329fbfCE'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 235: `dac20274b7f74492` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234114`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE X'B82A1B4d'; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 236: `c2fa2e307b43c36c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234608`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP LIKE CAST(FALSE || 00158474957125067237289217472586464
```

---

## Crash 237: `e7b4a82c71e9bf6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234667`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP ESCAPE FALSE; CREATE VIRTUAL TA
```

---

## Crash 238: `6cb63d50b2089ea8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235045`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT DEFAULT TRUE, c1 INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (-FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p
```

---

## Crash 239: `198708c38aa683af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237101`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1); INS
```

---

## Crash 240: `ed0b290da118ea90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237186`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(b); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN p; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 241: `571b8298e755fec8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238963`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL DEFAULT CURRENT_DATE, rowid NUMERIC DEFAULT CURRENT_TIMESTAMP); INSERT INTO q DEFAULT VALUES; SELECT * FROM
```

---

## Crash 242: `966aacd9f23cd168` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239070`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL DEFAULT CURRENT_DATE, rowid NUMERIC DEFAULT 03502367161324930905079849651948421708054798637687085.62); INSE
```

---

## Crash 243: `355066ba3446f0ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239393`

```sql
SELECT printf('%.*s', 1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT RAISE(IGNORE) AS r5gw6am, q.* FROM p NATURAL JOIN q WHERE rowid;
```

---

## Crash 244: `b52569df978d09e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242100`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT CHECK (CAST(FALSE || 00158474957125067237289217472586464082468.9608e4 AS DATE))); INSERT INTO p VALUES (CAST(CURRENT_DATE AS DATE) NOT IN (VALUES (CURRENT_DATE) UN
```

---

## Crash 245: `4b4219393e42e6c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243131`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CASE TRUE WHEN CURRENT_TIMESTAMP OR FALSE || FALSE THEN CURRENT_TIME END
```

---

## Crash 246: `f794f0140f288e15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243294`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE NULL >= TRUE OR FALSE || FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 247: `e23ebfbab7987804` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243753`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP COLLATE RTRIM == c3; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 248: `ec270f1104f57a13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244346`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME == q.rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 249: `69c10b92a6d0b85b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244852`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE -FALSE == c3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); 
```

---

## Crash 250: `d04c0c4edb15db5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245615`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE / TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FA
```

---

## Crash 251: `72a9e2a0a1edfd4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245812`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE / FALSE || FALSE || FALSE || FALSE || FALSE || FALSE; SELECT print
```

---

## Crash 252: `a11f3b1f96599e9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247269`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); CREATE TABLE IF NOT EXISTS q(rowid INTEGER PRIMARY KEY, c1 INT NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE FALSE; SELECT printf('%.*g', -2147483649, 0.01)
```

---

## Crash 253: `584df311e4f3b4f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249038`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); SELECT CURRENT_DATE << ~CURRENT_TIMESTAMP || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE LIMIT CURRENT_
```

---

## Crash 254: `282fedf2231812f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267038`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM q LEFT OUTER JOIN p) AS a NATURAL JOIN p WHERE CURRENT_T
```

---

## Crash 255: `4406ccc1566ba61c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267367`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM (SELECT ALL * FROM p LEFT JOIN q NOT INDEXED ON CURRENT_TIME) AS a NATURAL 
```

---

## Crash 256: `ce1cbed65c0ab5b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267402`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q NATURAL JOIN q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_TIME 
```

---

## Crash 257: `e2013d331e759a22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000268894`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM q LEFT OUTER JOIN p WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS () ORDER 
```

---
