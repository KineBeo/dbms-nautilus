# Crash Triage Report

**Total crashes:** 313  
**Unique crash sites:** 313  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 312 | 312 | 99% |
| Signal | 1 | 1 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `ab67af31a2bec9c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000066`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CURRENT_DATE COLLATE BINARY LIKE CAST(CURRENT_TIMESTAMP AS TEXT) == TRUE - CURRENT_DATE IN (SELECT p.*) <= CASE WHEN +TRUE NOT LIKE FALS
```

---

## Crash 2: `f617729ed30388a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000578`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT ALL * FR
```

---

## Crash 3: `8eb4d23e653d115e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000679`

```sql
SELECT substr('', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); EXPLAIN QUERY PLAN WITH q AS MATERIALIZED (SELECT (CASE WHEN NOT EXISTS (SELECT *) < TRUE AND RAISE(IGNORE) IS NULL T
```

---

## Crash 4: `91d1c70e9f94963b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001076`

```sql
SELECT printf('%.*e', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT RAISE(IGNORE) BETWEEN FALSE ->> +RAISE(IGNORE) AND CASE WHEN CURRENT_DATE + CURRENT_TIMESTAMP T
```

---

## Crash 5: `8302a55cb6a604c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001151`

```sql
SELECT printf('%lld', 2147483647, '_-5N '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (c2, b) VALUES (TRUE IS NOT NULL NOT IN (NULL || CURRENT_TIME, +CURRENT_DATE % RAISE(
```

---

## Crash 6: `7762dc1da5dfb162` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001289`

```sql
SELECT substr('k8- l9B5iM', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2); INSERT INTO t3 VALUES (CASE WHEN CURRENT_DATE THEN NULL END + CURRENT_TIMESTAMP REGEXP CASE 
```

---

## Crash 7: `537283458826f3f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001611`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT INTO p (b, b) VALUES (NULL IS NOT NULL, TRUE, NULL) ON CONFLICT(b) DO UPDATE SET rowid = json_val
```

---

## Crash 8: `3caca5a39135bb32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001896`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIME NOT LIKE CURRENT_DATE << CURRENT_DATE); VALUES (FALSE); CREATE VIRTU
```

---

## Crash 9: `153100c7e89d1b90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001929`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 10: `fbb472d1758c3dd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002195`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXIST
```

---

## Crash 11: `c29f888a03bfe699` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002695`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT NOT TRUE & random() F
```

---

## Crash 12: `df86c238b040ed2e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002772`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 13: `f7c50b4ee7d98e82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002793`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); EXPLAI
```

---

## Crash 14: `ad4449fe752e4a08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002806`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CAST(CA
```

---

## Crash 15: `ca7368bd052827ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002812`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (CURRENT_TIMESTAMP))); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 16: `e38a93f900656d1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002818`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (FALSE))); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 17: `98b3d252cac936a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005915`

```sql
SELECT round(0.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE p AS NOT MATERIALIZED (SELECT ALL NOT EXISTS (SELECT t1.* ORDER BY +CURRENT_DATE DESC NULLS LAST) FROM t
```

---

## Crash 18: `1723173ad0b94442` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006436`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3, c3, c2); REPLACE INTO q VALUES (iif(TRUE COLLATE NOCASE, TRUE, RAISE(IGNORE)) OVER (PARTITION BY CURRENT_TIME, NULL)); EXPLAIN QUERY PL
```

---

## Crash 19: `a142eceaa33f30d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006448`

```sql
SELECT printf('%s', 4294967296, ' --_ l-Y92_-5gQ_kE'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, b, c1); REPLACE INTO q VALUES (NOT CURRENT_TIME NOTNULL >= CURRENT_DATE NOT LIKE NOT 
```

---

## Crash 20: `9bcf862e44a0dbfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007105`

```sql
SELECT printf('%.*f', 1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q (c2) AS (SELECT CURRENT_TIME MATCH RAISE(IGNORE) >= RAISE(IGNORE) IS NULL FROM r NOT INDEXED W
```

---

## Crash 21: `2e9c3f1c1e7f97ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007807`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 22: `fc8d9b656c66d98a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007843`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex(zeroblob(-922337203685477
```

---

## Crash 23: `cc87334c9c5b9262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011646`

```sql
SELECT printf('%.*s', 4294967296, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO p VALUES ((sum(CAST(CURRENT_TIMESTAMP IS NULL AS INT) ISNULL) FILTER (WHERE CUR
```

---

## Crash 24: `40405ed4fb1603cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012877`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO p
```

---

## Crash 25: `69fd72f5564c2cab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013086`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob
```

---

## Crash 26: `cc0895b369320646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013689`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 27: `fc86c6e4b660276b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014742`

```sql
SELECT printf('%.*g', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 28: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015161`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 29: `d63990463ace69a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015317`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC DEFAULT X'1CaeBbffCaAb'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 30: `a4492265a78eeffd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015504`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ BLOB); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b);
```

---

## Crash 31: `bb2fb20a44289cf9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015510`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC DEFAULT CURRENT_TIMESTAMP); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 32: `fe4589080264618c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015535`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 33: `88dff457496cd179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015928`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 34: `d52f2cec0aa126a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016237`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME | TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 35: `9220e4592885ce28` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016868`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 36: `1808333d6ac9bf4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016948`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 37: `90f162d130965d06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017156`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (FALSE + CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF 
```

---

## Crash 38: `b955181ca3ba4942` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017382`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 39: `68683a10487835f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017546`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE + CURRENT_DATE); PRAGMA integrity_check; SELECT printf('%.
```

---

## Crash 40: `0df2b696e72986da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018185`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN); INSERT OR REPLACE INTO q VALUES (CURRENT_DATE LIKE CURRENT_DATE ESCAPE TRUE); PRAGMA integrity_check; CREATE VIR
```

---

## Crash 41: `c581e524684685e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018206`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b, c3, a, c1, _rowid_, b, b, c2, b); SELECT CASE json_array(-FALSE << CURRENT_DATE, RAISE(IGNORE) COLLATE BINARY <> FALSE COLLATE BINARY MATCH 
```

---

## Crash 42: `a0d935cf3168b123` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018696`

```sql
SELECT printf('%.*g', -1, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 43: `079f69334a9fedda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021588`

```sql
SELECT printf('%.*g', 0, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); SELECT hex(zeroblob(-2147483648));
```

---

## Crash 44: `4079d2b7036ed0c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022780`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_TIMESTAMP OR FALSE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * ORDER BY FALSE ASC, CURRENT_TIMESTAMP DESC NULLS FIRST; INSERT INTO p DEFAULT
```

---

## Crash 45: `8cfe5863d5cf28bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023040`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_TIMESTAMP OR NOT FALSE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM p ORDER BY FALSE ASC, CURRENT_TIMESTAMP DESC NULLS FIRST; I
```

---

## Crash 46: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023117`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 47: `9bbb3ff947b0e27e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023196`

```sql
SELECT substr('gH0CHJu p4--0y', 4294967295, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 48: `024b3c2aa228be57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023428`

```sql
SELECT substr('', -2147483648, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 49: `407320f728ac1d97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023539`

```sql
SELECT round(-1.0, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * ORDER BY q.rowid ASC NULLS LAST LIMIT (WITH s (rowid) AS (VALUES (RAISE(IGNORE))), p AS NOT MATERIALI
```

---

## Crash 50: `9818c3ed961b7583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023761`

```sql
SELECT printf('%.*g', -2147483648, -0.0); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 51: `175260597b3a8369` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027494`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b INT DEFAULT -524580571531861908026739899326486249700615307675666809504671057673881365640548455551995123246382628520832721311700
```

---

## Crash 52: `b7874b6ea20c41ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028651`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT CURRENT_TIME NOT IN (VALUES (FALSE)) FROM (SELECT * FROM p WHERE TRUE) AS sub1; CREATE V
```

---

## Crash 53: `25ea48ea96c42af5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032828`

```sql
SELECT printf('%.*d', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 54: `11233403d2d49254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033510`

```sql
SELECT substr(' A8---1B -7 lF-0_9', 0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c1, b); SELECT NOT CURRENT_DATE MATCH CURRENT_DATE AS d_ FROM (SELECT t2.*, (T
```

---

## Crash 55: `f4f2a9fd7cc32827` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034952`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 56: `a780bf6aba342058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036248`

```sql
SELECT round(-1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES (NULL); ANALYZE p; SELECT hex(zeroblob(1));
```

---

## Crash 57: `5ba0b4118639c7cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036745`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (150578706154331542409909073958897883579041284302803858546934.7460640470986728284120348501184929671153647741825404622170825769574355014476007820702419480362975
```

---

## Crash 58: `e8de24aa112c0682` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036964`

```sql
SELECT printf('%x', -2147483648, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c
```

---

## Crash 59: `6f78c5403997ddf3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037484`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT INTO p VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIMESTAMP); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 60: `7969ce70cff23555` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038634`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (150578706154331542409909073958897883579041284302803858546934.746064047098672828412034850118492967115364774182540462217082
```

---

## Crash 61: `44f5d15c3ba44a19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038871`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); SELECT CURRENT_TIME >= CURRENT_DATE AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____
```

---

## Crash 62: `f8845b911c6b94e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039065`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT CURRENT_TIME != CURRENT_TIMESTAMP AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_
```

---

## Crash 63: `66cfe5ccbae0f572` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042021`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO 
```

---

## Crash 64: `291bcb5fa5dd4ade` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042697`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT (SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE) HAVING CURRENT_TIME WINDOW w1 AS () O
```

---

## Crash 65: `223f16b75d705b3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043123`

```sql
SELECT printf('%.*e', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, b); SELECT +X'1eC1' % (VALUES (TRUE) INTERSECT SELECT * ORDER BY CURRENT_TIME ASC NULLS LAST) = CURREN
```

---

## Crash 66: `2e95811865281772` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044036`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIME NOT LIKE TRUE); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF 
```

---

## Crash 67: `fa4fee6480846238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045788`

```sql
SELECT printf('%.*d', 2147483647, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 68: `14e6629a6145fda4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045870`

```sql
SELECT round(-1.0, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 69: `39e8b1f792b183f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046789`

```sql
SELECT printf('%.*g', 4294967296, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO q VALUES (CASE NOT CURRENT_DATE WHEN CURRENT_DATE THEN CURRENT_TIMESTAMP END -> NOT RA
```

---

## Crash 70: `beef785056fcc0c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046799`

```sql
SELECT substr(' o-mb--5--', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3, c2); INSERT OR FAIL INTO q VALUES (+NOT CURRENT_TIME >= NOT CURRENT_TIME NOTNULL GLOB (SELECT DISTI
```

---

## Crash 71: `86d74215c0368238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046846`

```sql
SELECT printf('%lld', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t1 DEFAULT VALUES; ANALYZE t2; CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); CREATE TABLE 
```

---

## Crash 72: `e871cd2e26580633` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048954`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME NOT IN (changes())); EXPLAIN QUERY PLAN VALUES (TRUE); CREAT
```

---

## Crash 73: `e7be2efad0a1e6e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049654`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT p.* FROM p NATURAL JOIN q WHERE NULL || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 74: `68fd1d55d4b4b346` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049807`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT p.* FROM p NATURAL JOIN q WHERE NULL || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 75: `4f2903ab7983ff80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049815`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE NULL || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 76: `65f98a1c5087d175` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049821`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT TRUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLAC
```

---

## Crash 77: `c736f471bc32e5a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049834`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE NULL || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 78: `0687eccc9eedb5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049980`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE FALSE || CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3,
```

---

## Crash 79: `4802cb8edd26b035` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050218`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE TRUE || TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR FA
```

---

## Crash 80: `ca82d812ab047c41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, b DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF 
```

---

## Crash 81: `5c188b606f2a4450` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053989`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE NULL GROUP BY TRUE, CURRENT_DATE; SELEC
```

---

## Crash 82: `1d9d71a0e459129c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058133`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT max(TRUE) OVER (ORDER BY NULL ASC NULLS LAST ROWS BETWEEN TRUE PRECEDING AND CURRENT ROW) AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_
```

---

## Crash 83: `e03bc41c391e9743` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058237`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT TRUE AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_; SELECT hex(zeroblob(0)); CR
```

---

## Crash 84: `884c79e312963e60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058249`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT TRUE AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_; SELECT hex(zeroblob(0)); CR
```

---

## Crash 85: `4ecc8e7d97dd5789` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058896`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT CURRENT_DATE NOT IN (CURRENT_TIMESTAMP) AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v
```

---

## Crash 86: `81c89c6ddd345b00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059506`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); SELECT min(NULL) OVER () AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_1
```

---

## Crash 87: `c3ec5040bbdcfdc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059919`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); SELECT count(CURRENT_DATE) OVER () AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_; SEL
```

---

## Crash 88: `db205f17f946eab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060113`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_TIMESTAMP, CURRENT_DATE); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 89: `9a88b3b27aea9103` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060809`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT count(*) AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL 
```

---

## Crash 90: `4eb3f7d37391ad2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061023`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT CURRENT_TIME AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRT
```

---

## Crash 91: `e93c9a9e4337f6e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061094`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT X'' AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE
```

---

## Crash 92: `d62b36b59cdbd000` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061526`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT count(*) % X'' AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VI
```

---

## Crash 93: `86d9babf94eeeb1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062366`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (ifnull(CURRENT_TIME, NULL) % TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 94: `55fd9b75bff3e960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062448`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (NULL % TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT 
```

---

## Crash 95: `fef3d986a823df49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062454`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (random() % TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INS
```

---

## Crash 96: `9e13e8b580b54bc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062892`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (min(FALSE) FILTER (WHERE TRUE) OVER (ORDER BY NULL ASC NULLS LAST ROWS BETWEEN 
```

---

## Crash 97: `c70be792fdc364ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065508`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL); SELECT count(*) OVER (PARTITION BY CURRENT_DATE), * FROM p WHERE EXISTS (VALUES (RAISE(IGNORE))); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 98: `2e741e75b8c418ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065964`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q (rowid) VALUES (FALSE); WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT count(*) AS z04eq6p____m
```

---

## Crash 99: `d0fa5d36e5ec1d32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066078`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q (rowid) VALUES (FALSE); WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT CAST(CURRENT_TIME AS NUM
```

---

## Crash 100: `d98f381091e7b961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066611`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT CAST(CURRENT_TIME AS NUMERIC) AS z04eq6p___
```

---

## Crash 101: `b58da4d62b90042c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066793`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT json_type(TRUE) AS z04eq6p____m_lhg FROM p;
```

---

## Crash 102: `e743d28b05effcfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT last_insert_rowid() AS z04eq6p____m_lhg FRO
```

---

## Crash 103: `33fc63ef2ddb3d70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070318`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC CHECK (CURRENT_TIME AND TRUE)); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483
```

---

## Crash 104: `c818edab10d10b8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071755`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT NOT NULL DEFAULT -35047197520865757540619978625754207545191012348937862258.17E-932884876739558193840445); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT IN
```

---

## Crash 105: `3f9ac41da497e7f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071885`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 106: `7f7e75a71d30203d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072706`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p (_rowid_) VALUES (TRUE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 107: `8009510a03f63f1d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078788`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p SELECT * FROM (VALUES (TRUE)) AS u6x7_1__79_01a_7__i_kp8_0_pr3136vym1_t948f6___c_73t_1w225__7jo6z_0hi_49g00575y0___8c6_f459x__88z____
```

---

## Crash 108: `0c37b7b2daa54bf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079379`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY FALSE ASC, CURRENT_TIMESTAMP DESC NULLS FIRST; CREATE VIRTUAL TAB
```

---

## Crash 109: `e6a393fa10923026` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079618`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p ORDER BY CURRENT_TIMESTAMP ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 110: `f94b012d1107af90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080637`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT *, * FROM (SELECT TRUE NOT IN (TRUE) FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIR
```

---

## Crash 111: `dad801de8e64bd9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080874`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT *, * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 112: `c4ae2e602e4aa26e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081548`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY
```

---

## Crash 113: `c6b2afc60540ec2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081681`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE NULL BETWEEN CURRENT_DATE AND FALSE) AS sub1; CREATE VIRTU
```

---

## Crash 114: `e75fd1d7c5793a5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082932`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT count(*) FILTER (WHERE TRUE) FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL T
```

---

## Crash 115: `ace7b5339ad3388d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084505`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); INSERT INTO p VALUES (-CURRENT_DATE); VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRE
```

---

## Crash 116: `cdced47e9a70acdf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086446`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (NULL) UNION ALL VALUES (NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (TRU
```

---

## Crash 117: `8ec49c81ac72c147` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086488`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIME ASC
```

---

## Crash 118: `c2bc8d37ed452e9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089514`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 TEXT); INSERT INTO q VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 119: `98e589cc37c03df4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089875`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p JOIN t1 USING (b, c3) WHERE RAISE(IGNORE) LIMIT NULL; SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * F
```

---

## Crash 120: `30cc068ecd9fb403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091028`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_TIMESTAMP OR FALSE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (min(FALSE) FILTER (
```

---

## Crash 121: `4983cade1191400a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091185`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE, count(*) FILTER (WHERE TRUE) OVER ()
```

---

## Crash 122: `866bd09029c8a0b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091236`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_DATE NOT IN (FALSE))); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CRE
```

---

## Crash 123: `2ff95e1c461bef7c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091436`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NO
```

---

## Crash 124: `4bbe23ddf28a10ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091491`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) CHECK (CURRENT_TIME != CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT
```

---

## Crash 125: `235cb414a9178dc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092702`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); SELECT FALSE EXCEPT VALUES (CURRENT_DATE < CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 126: `3123b4f506e41cee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092853`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT FALSE EXCEPT VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 127: `d23dbcc097583ff5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092859`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT FALSE EXCEPT VALUES (NULL); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 128: `427a0b411ec6e94f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097922`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p SELECT * EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY FALSE WINDOW w1 AS () ORDER B
```

---

## Crash 129: `40918e7fde044ff2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103886`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN); INSERT OR REPLACE INTO q VALUES (~NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 130: `58d6026840fab060` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104577`

```sql
SELECT printf('%.*s', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a); SELECT *, *, FALSE IS NULL FROM r JOIN p a ON count(CAST(CURRENT_DATE <> NOT ~(CURRENT_TIMESTAMP) >
```

---

## Crash 131: `6b405d50c5a11660` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105256`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (FALSE + ~CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 132: `72a0c4f69c64b616` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106306`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL DEFAULT '-L 2W3- i2Zst iuD6e'); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (TRUE); PRAGMA integrity_check; CREATE V
```

---

## Crash 133: `456f2b8d081f9d4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106679`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (150578706154331542409909073958897883579041284302803858546934.7460640470986728284120348501184929671153647741825404622170825769574355014476007820702419480362975
```

---

## Crash 134: `5465b4caf14916ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106837`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR REPLACE INTO q VALUES (TRUE LIKE CURRENT_DATE ESCAPE TRUE + NOT FALSE IS NULL); PRAGMA integrity_check; S
```

---

## Crash 135: `d6074b6a7663edc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107440`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR REPLACE INTO q VALUES (-FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 136: `ae6320a4a2622849` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107783`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME AND TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 137: `8d46fc30a04812b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107913`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); INSERT OR REPLACE INTO q VALUES (CURRENT_TIME > NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 138: `7a661d78aa2b7146` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109266`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL DEFAULT X'FC3F783d'); CREATE TABLE IF NOT EXISTS q(c1 REAL NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 139: `47db15d1d8471bef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109401`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC DEFAULT -524580571531861908026739899326486249700615307675666809504671057673881365640548455551995123246382628520832
```

---

## Crash 140: `b1db0cc027df78de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109471`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 141: `26a60b20276f3441` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109664`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 142: `440fcea92748ba48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109834`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL DEFAULT 0.0); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 143: `ea5524e7e3a2abd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109969`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC DEFAULT 66894338505376.528448609161); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', 
```

---

## Crash 144: `143be89a007e43fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111751`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (NULL); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p VALUES (TRUE) UNION ALL VALUES (NULL); V
```

---

## Crash 145: `42e835b255f933d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112219`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (+TRUE NOT IN (CURRENT_TIME)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO 
```

---

## Crash 146: `62ecd18646be6910` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112686`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); REPLACE INTO p VALUES (FALSE LIKE NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_TIM
```

---

## Crash 147: `39dec7f7dfa57329` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112893`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); IN
```

---

## Crash 148: `26598ba22cf8eec8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112909`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); INSERT INTO p DEFAULT VALUES; PRAGMA qui
```

---

## Crash 149: `0e2de92a45e90da6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112944`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*e', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 150: `598b6e4a0214be0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113553`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); IN
```

---

## Crash 151: `e50b91d907827179` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113579`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NA
```

---

## Crash 152: `3c0f00f5dc9181fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113601`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (CURRENT_DATE < CURRENT_TIME), b INT); INSERT INT
```

---

## Crash 153: `13d0146483914705` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113760`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(b DATE, rowid BLOB PRIMARY KEY)
```

---

## Crash 154: `4ae3ecb30386c312` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113815`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INTEGER CHECK (FALSE MATCH CURRENT_TIME)); CREATE TABLE IF NOT EXIS
```

---

## Crash 155: `032bd5477d8e295e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113831`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(a); REPLACE INTO
```

---

## Crash 156: `31aec197a1122d34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114151`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS WITH RECURS
```

---

## Crash 157: `34d95e39fe668cfd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114292`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 158: `adad4fa15274d361` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114724`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (json_type(NULL))); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF 
```

---

## Crash 159: `72f676b409000068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122369`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB UNIQUE, c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT count(CURRENT_TIME IS NO
```

---

## Crash 160: `9d00689f5dd23894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123343`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); REPLACE INTO q VALUES (upper(FALSE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 161: `19606a4889fb9969` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124551`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB); INSERT OR FAIL INTO p VALUES (last_insert_rowid()); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 162: `0ada9861c3c0a62a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129082`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO p VALUES (TRUE) UNION ALL SELECT * FROM q WHERE NULL GROUP BY FALSE; SELECT * UNION ALL SE
```

---

## Crash 163: `c7feca81d9ccda97` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129237`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); INSERT INTO p VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); SELECT * UNION ALL SELECT * EXCEPT SELECT
```

---

## Crash 164: `1eb481e399aa4ff9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129486`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 INTEGER CHECK (upper(CURRENT_TIMESTAMP))); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL 
```

---

## Crash 165: `52c58378ede41650` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130234`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CRE
```

---

## Crash 166: `d469f9f9f1eaa981` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130295`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY K
```

---

## Crash 167: `1d86d899376a2cc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130426`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CU
```

---

## Crash 168: `5e0e835654f95218` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130622`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL UNIQUE); 
```

---

## Crash 169: `bdbf99b22820170e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132028`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT ''); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES (CURRENT_T
```

---

## Crash 170: `d6c4205bf041d6d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132138`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT CURRENT_TIME); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE INTO p VALUES 
```

---

## Crash 171: `7e15008ec124af60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133686`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE CHECK (CURRENT_TIME)); REPLACE INTO p VALUES (NULL LIKE CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT IN
```

---

## Crash 172: `f0d50390994afb24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137048`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CASE WHEN FALSE THEN changes() IS TRUE END)); INSERT INTO q DEFAULT VALUES; PRAGMA i
```

---

## Crash 173: `04023ea1ac539b2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137169`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CURRENT_TIMESTAMP)); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VI
```

---

## Crash 174: `f8aabc5e669956b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137213`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CASE WHEN FALSE THEN changes() IS TRUE END * CURRENT_TIME)); INSERT INTO q DEFAULT V
```

---

## Crash 175: `e7af1b7e157e427e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137690`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CASE WHEN FALSE THEN changes() IS TRUE END * CURRENT_TIME * CURRENT_TIME * CURRENT_T
```

---

## Crash 176: `c740d4c798db90ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137908`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CASE WHEN FALSE THEN changes() IS TRUE END * CURRENT_TIME * CURRENT_TIME * CURRENT_T
```

---

## Crash 177: `db97db6992a2cb2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138179`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP * CASE WHEN FALSE THEN changes() IS TRUE END * CURRENT_TIME * CURRENT_TIME * CURRENT_T
```

---

## Crash 178: `70567c14c9aa213c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138616`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (TRUE + TRUE || TRUE); PRAGMA integrity_check; SELECT printf('%.*g', -21
```

---

## Crash 179: `ddfa8869279e9a93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138812`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE ||
```

---

## Crash 180: `93402895c786e606` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138887`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(a DATE PRIMARY KEY); INSERT OR REPLACE INTO q VALUES (TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE ||
```

---

## Crash 181: `b5481e047007d1b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139566`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN); INSERT OR REPLACE INTO q VALUES (TRUE % ~FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 182: `201b01009d7c2f99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146629`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB PRIMARY KEY); SELECT (VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS LAST, CURREN
```

---

## Crash 183: `74a589c19877e8fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147428`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (NULL) UNION ALL VALUES (CURRENT_TIME); SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 184: `e495ebc0cf932ba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149139`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 INTEGER); SELECT * EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY FALSE WINDOW w1 AS () ORDER BY NULL DESC NULLS
```

---

## Crash 185: `392deb8baa3b6b27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149534`

```sql
SELECT round(-1e308, -9223372036854775808); SELECT printf('%.*s', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, _rowid_, a, c2); INSERT INTO p VALUES (CASE WHEN ~TRUE IS NOT CUR
```

---

## Crash 186: `286add47df255a14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149772`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB DEFAULT CURRENT_TIME, c1 REAL); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL W
```

---

## Crash 187: `68bc6add676537d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154458`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c3 FLOAT); WITH q AS (VALUES (CURRENT_TIME)) INSERT INTO q VALUES (FALSE & TRUE); EXPLAIN QUERY PLAN SELECT * EXCEPT SELECT * FROM p 
```

---

## Crash 188: `dc124151e8ca94bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156530`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT * FROM p NOT INDEXED)); VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL
```

---

## Crash 189: `5fb9c8ef5fb89cbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158602`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT (SELECT DISTINCT * FROM q NOT INDEXED ORDER BY CURRENT_DATE ASC NULLS LAST) FROM (SELECT
```

---

## Crash 190: `858add990fcd1f5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158740`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT (VALUES (FALSE)) FROM (SELECT * FROM p WHERE NULL) AS sub1; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 191: `e742205af8e54b9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160439`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT CURRENT_TIME NOT IN (VALUES (_rowid_) UNION ALL VALUES (NULL)) FROM (SELECT * FROM p WHE
```

---

## Crash 192: `e4ef90ac64a97087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160640`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT CURRENT_TIME NOT IN (VALUES (FALSE) UNION ALL VALUES (NULL)) FROM (SELECT * FROM p WHERE
```

---

## Crash 193: `e4e703733051c3e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161089`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE EXISTS (VALUES (count(*) FILTER (WHERE TRUE) OVER (PARTITI
```

---

## Crash 194: `e8a58f405b21d989` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161274`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT * FROM (SELECT * FROM p WHERE EXISTS (VALUES (count(*) FILTER (WHERE TRUE) OVER (), TRUE
```

---

## Crash 195: `df6bf696b5d6a657` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161368`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT *, * FROM (SELECT TRUE NOT IN (0) FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT printf
```

---

## Crash 196: `a3225054dea76d1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161512`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 REAL PRIMARY KEY); SELECT *, * FROM (SELECT TRUE NOT IN (NULL) FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT pri
```

---

## Crash 197: `bbfb9f73884c72dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163098`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT min(b) AS a FROM p NOT INDEXED; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 198: `66cc5320de9bab15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164611`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p SELECT TRUE & CURRENT_DATE FROM (VALUES (TRUE)) AS u6x7_1__79_01a_7__i_kp8_0_pr3136vym1_t948f6___c_73t_1w225__7jo6z_0hi_49g00575y0___
```

---

## Crash 199: `59a1a41c6bdf1de9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164815`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p SELECT TRUE & CURRENT_DATE FROM p GROUP BY NULL; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 200: `9403a3a2c25cffed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164891`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); INSERT INTO p SELECT * FROM p GROUP BY CURRENT_TIMESTAMP COLLATE RTRIM HAVING CURRENT_TIMESTAMP; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE V
```

---

## Crash 201: `359ea65c20a3e259` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172599`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT CHECK (NULL * NULL == TRUE), a VARCHAR(255)); INSERT INTO p DEFAULT VALUES; SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE
```

---

## Crash 202: `6d6c2ab09dd0dc94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p JOIN p s18j3u2___03__9 ON TRUE / FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_DATE <> CURRENT_DATE - N
```

---

## Crash 203: `7566654655b5176f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173678`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL); SELECT * FROM p JOIN p s18j3u2___03__9 ON TRUE / CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO p VALUES (TRUE); PR
```

---

## Crash 204: `dcd20a7c9c6c1433` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000175428`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p AS (VALUES (count(*) FILTER (WHERE CURRENT_TIME) OVER ())) SELECT * FROM p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 205: `5817a9d267d87b20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); WITH RECURSIVE p (a) AS (VALUES (CURRENT_TIMESTAMP IS NOT FALSE) UNION ALL VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; SELECT printf('%.*g', 
```

---

## Crash 206: `ab4ce5b61da99754` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177667`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT SELECT DISTINCT * FROM q NATURAL LEFT JOIN (SELECT CURRENT_TIMESTAMP, * FROM p GRO
```

---

## Crash 207: `09f215369daad343` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178657`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT VALUES (NULL) INTERSECT SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY _rowid_ WINDO
```

---

## Crash 208: `26b66fe3ef8a4842` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178663`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT SELECT DISTINCT * FROM q INTERSECT SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY _r
```

---

## Crash 209: `6e006d5641b6619e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178674`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT SELECT DISTINCT * FROM q NATURAL LEFT JOIN (SELECT *, * FROM p GROUP BY CURRENT_TI
```

---

## Crash 210: `bf08555bd4ada891` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT VALUES (NULL) INTERSECT SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY RAISE(IGNORE)
```

---

## Crash 211: `00e02cbf8ff7494b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178735`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT VALUES (TRUE) INTERSECT SELECT * FROM q WHERE NULL GROUP BY NULL ORDER BY NULL COL
```

---

## Crash 212: `983347e195ef7c03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178913`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) EXCEPT VALUES (FALSE) INTERSECT SELECT * FROM q WHERE NULL GROUP BY NULL ORDER BY NULL AS
```

---

## Crash 213: `828344a2b006c962` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180475`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT CAST(CURRENT_TIME AS REAL) NOT BETWEEN CURR
```

---

## Crash 214: `e73f828970f001e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180603`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT NULL NOT BETWEEN CURRENT_TIMESTAMP AND TRUE
```

---

## Crash 215: `87d483d093f1aa72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180722`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE r AS (SELECT *) SELECT CAST(CURRENT_TIME AS VARCHAR(255)) NOT BETW
```

---

## Crash 216: `6d0a3b5fcfc944c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181130`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT json_type(FALSE) AS z04eq6p____m_lhg FROM p
```

---

## Crash 217: `a4073b20ec966e5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181953`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q (rowid) VALUES (FALSE); WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT EXISTS (VALUES (count(*)
```

---

## Crash 218: `04f9cd961a548b46` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182209`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT count(DISTINCT TRUE) FILTER (WHE
```

---

## Crash 219: `e9a7cee6ce0f5395` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182851`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q (rowid) VALUES (FALSE); WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT CAST(CURRENT_TIME AS NUM
```

---

## Crash 220: `ae7805e5ec08ebae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182993`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT FALSE NOT BETWEEN CURRENT_TIMEST
```

---

## Crash 221: `89a4794854a87056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184235`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); VALUES (min(FALSE) FILTER (WHERE TRUE) OVER (ORDER BY NULL ASC NULLS LAST ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING), count(*) FILTER (WHERE CURRENT
```

---

## Crash 222: `e64e101b2b97fe7b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185056`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (VALUES (TRUE)) AS u6x7_1__79_01a_7__i_kp
```

---

## Crash 223: `b08f9dac9fcf07cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185381`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN UNIQUE, c1 VARCHAR(255) 
```

---

## Crash 224: `fb056f51d723dc9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185642`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT INTO p SELECT ALL * FROM p NOT INDEXED; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLA
```

---

## Crash 225: `7f74658f44f55091` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187697`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); SELECT * FROM p JOIN p a ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 226: `c9849c3b6fb514c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000188835`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT count(*) AS a FROM (VALUES (FALSE)) AS a)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE 
```

---

## Crash 227: `12d42e1f2e873a6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189043`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (VALUES (NULL) INTERSECT SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY _rowid_ WINDOW w1 AS () ORDER B
```

---

## Crash 228: `4b4967d29f90ecd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000189483`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT count(*) % count(*) AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREA
```

---

## Crash 229: `9d27e055db846514` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190106`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT ' k7WP_' AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL 
```

---

## Crash 230: `3efad0174e81fb91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190786`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT min(b) AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT printf('%.
```

---

## Crash 231: `8938761e2aa57b87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191134`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (150578706154331542409909073958897883579041284302803858546934.746064047098672828412034850118492967115364774182540462217082
```

---

## Crash 232: `1b435d421d0b6c93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191192`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (X'FC3F783d' NOT IN (VALUES (CURRENT_TIME))); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 233: `48b40c4579c72971` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194361`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(CURRENT_DATE) OVER (ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLU
```

---

## Crash 234: `6f695051afb58f68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194704`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(*) OVER (ORDER BY TRUE DESC NULLS LAST, CURRENT_TIME DESC NULLS LAST) AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1
```

---

## Crash 235: `6d152eaaa6d26c99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194860`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(*) OVER () AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_; SELECT printf('
```

---

## Crash 236: `48d45ac3467db9a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195419`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE, c1 VARCHAR(255) PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q NO
```

---

## Crash 237: `dbbdb5e380b95ece` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195434`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, a); SELECT * UNION ALL VALUES (CURRENT_TIME
```

---

## Crash 238: `8b42491bb0f66d55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195447`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM 
```

---

## Crash 239: `baa51ae4978ef1bf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195455`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM 
```

---

## Crash 240: `bfe65fe90bc67c37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195465`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, *, *, max(TRUE) OVER (PARTITION BY CURRENT_DATE ORDE
```

---

## Crash 241: `e5b4fe7feeb40cbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195471`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (NULL); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 242: `25174e712c1b6f7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195477`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); REPLACE INTO q VALUES (CURRENT_DATE << CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL 
```

---

## Crash 243: `904bf542d2caf0f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195508`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL SELECT DISTINCT * FROM q LEFT OUTER JOIN p 
```

---

## Crash 244: `974b59fa196df229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195518`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL SELECT * FROM (VALUES (TRUE)) AS u6x7_1__79
```

---

## Crash 245: `3c7011cc76b1bd16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195526`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3, c2); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * 
```

---

## Crash 246: `24865810f4b1c17b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195539`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM 
```

---

## Crash 247: `c304ebf33eb8ea89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195547`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (count(*) FILTER (WHERE TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEP
```

---

## Crash 248: `c9738dac3bd33da2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195600`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * UNION ALL VALUES (CURRENT_TIME) EXCEPT SELECT * FROM 
```

---

## Crash 249: `ba6400f9c8b11a60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199908`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP), c2 DATE CHECK (~X'Fdf504fcdE')); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_
```

---

## Crash 250: `2f488010fbe1e64b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202858`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p , p NOT INDEXED USING (c1); CREATE VIRTUAL TABLE 
```

---

## Crash 251: `bf7457589608bf37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203409`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (FALSE); VALUES ((SELECT DISTINCT * FROM p WHERE TRUE LIMIT TRUE)); CREATE VIRTUAL
```

---

## Crash 252: `d13eef473d3f93c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204126`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT * FROM q GROUP BY CURRENT_TIME LIMIT ~TRUE; CREATE VIRTUAL TABLE IF
```

---

## Crash 253: `966aab5b5dabab66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204379`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); VALUES
```

---

## Crash 254: `a4da5ba25f5334eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204570`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * C
```

---

## Crash 255: `775a3d4d264366ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204830`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURREN
```

---

## Crash 256: `dad150e2a643fae6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204958`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * C
```

---

## Crash 257: `4632bef4b866a1b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207922`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CAST(TRUE AS TEXT)); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 258: `1d7cd8a8b675b752` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208122`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CAST(TRUE AS DATE)); VALUES (NULL) EXCEPT VALUES (NULL) INTERSECT SE
```

---

## Crash 259: `bcde4d3417a214c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208320`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CAST(FALSE || TRUE AS BLOB)); VALUES (NULL); SELECT printf('%.*g', -
```

---

## Crash 260: `65ac54b7e605a14c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209161`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, b DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (c2) VALUES (FALSE) ON CONFLICT(c2) DO UPDATE SET rowid = CURRENT_DATE; VALUES (NU
```

---

## Crash 261: `fc3a0ecec7f5e2f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209947`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE TRUE || 150578706154331542409909073958897883579041284302803858546934.74606404709867
```

---

## Crash 262: `ad18f6bae5379fef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210457`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 263: `66e7e71e6c80bb4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210661`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE FALSE || CURRENT_DATE << CURRENT_DATE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 264: `2fe2ceb402b06430` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211156`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE FALSE || ~CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid
```

---

## Crash 265: `202444d631b3575b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211509`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT DEFAULT X'1eD21e5DA7'); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 266: `e0ca3a50515226f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211691`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME || CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 267: `656407b0cc694480` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211806`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT count(*) OVER (PARTITION BY CURRENT_DATE) FROM p NATURAL JOIN q WHERE FALSE; SELECT printf('%.*f', 2147
```

---

## Crash 268: `a034cc08a508e5ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212429`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); 
```

---

## Crash 269: `eb7c88fa1a934640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212502`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); SELECT * FROM p NATURAL JOIN q WHERE NULL == TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); I
```

---

## Crash 270: `3b59a07e6bb6e227` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212802`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 TEXT); SELECT * FROM p NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO
```

---

## Crash 271: `6b94d3bdfd81819c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213802`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (CAST(FALSE AS BLOB) NOT IN (CURRENT_TIME)); EXPLAIN QUERY PLAN VALUES (TR
```

---

## Crash 272: `12b46ddda810d6f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214061`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT OR ROLLBACK INTO q VALUES (740753.6); EXPLAIN QUERY PLAN VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 273: `ec17522c30c50241` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215371`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (CURRENT_TIME) EXCEPT SELECT * FROM p NOT INDEXED WHERE NULL GROUP BY NULL WINDOW w1 AS () ORDER BY CURRENT_TIME ASC NULLS LAST, CURREN
```

---

## Crash 274: `d970b027fe54de8d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000216210`

```sql
SELECT printf('%.*d', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT OR REPLACE INTO t1 VALUES (CASE RAISE(IGNORE) AND CURRENT_TIMESTAMP NOT IN (SELECT *, 
```

---

## Crash 275: `1df069795c465b21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218613`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT NOT NULL); SELECT * FROM p JOIN p c_ ON CURRENT_TIMESTAMP IN (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH q (c3
```

---

## Crash 276: `77a23a88f9dd1603` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219291`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE, c2 REAL UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 277: `8964bee8df9e8c3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219819`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT NULL, c1 BLOB, b TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); REPLACE
```

---

## Crash 278: `26c5514228a65ff8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220356`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER PRIMARY KEY, b DATE); SELECT * FROM p NATURAL JOIN q WHERE FALSE || ~CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 279: `900e0c2b14f65347` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221117`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, b DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL LE
```

---

## Crash 280: `da3bff8db06eb248` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221685`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, _rowid_ FLOAT CHECK (CURRENT_DATE)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (c2) VALUES (FALSE) ON CONFLICT(c2) DO UPDATE SET rowi
```

---

## Crash 281: `427298847206b689` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000221884`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY, rowid DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p (c2) VALUES (FALSE) ON CONFLICT(c2) DO UPDATE SET rowid = CURRENT_DATE;
```

---

## Crash 282: `d89ab9c85027ab34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CAST(CAST(TRUE AS BLOB) AS BLOB)); VALUES (NULL); SELECT printf('%.*
```

---

## Crash 283: `869b5c57f0351ef5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224744`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * ~
```

---

## Crash 284: `46e2c428ed4f186e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226047`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INTEGER PRIMARY KEY); REPLACE INTO q VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 285: `cc6325d8c9cf6af6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226910`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE, c1 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p NATURAL LEFT JOIN q 
```

---

## Crash 286: `1da7ac75464f6433` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227100`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM p NATURAL LEFT JOIN (SELECT ALL * FROM p NOT INDEXE
```

---

## Crash 287: `27353c3c457a76fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227272`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 288: `c96b865a0b7760b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227890`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q , p NOT INDEXED USING (c1); CREATE VIRTUAL TABLE I
```

---

## Crash 289: `2ff40248acd38449` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227982`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 FLOAT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q , p NOT INDEXED USING (c1); CREATE VIRTUAL TABLE 
```

---

## Crash 290: `72560de9d681684c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228454`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q , (SELECT CURRENT_TIM
```

---

## Crash 291: `727999c33a9d166f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; SELECT DISTINCT * FROM q; CREATE VIRTUAL TABLE
```

---

## Crash 292: `d51a3d162a7701d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229767`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE TRUE GROUP BY CASE WHEN FALSE THEN FALS
```

---

## Crash 293: `4afca6c71eea62aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000229876`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 FLOAT UNIQUE); REPLACE INTO q VALUES (CURRENT_TIMESTAMP); SELECT * FROM q WHERE TRUE GROUP BY FALSE, CURRENT_DATE; SELE
```

---

## Crash 294: `850ed892559a7aa0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231134`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP), c2 DATE CHECK (CURRENT_DATE NOT IN (CURRENT_TIME, CURRENT_TIME, CURRENT_TIME)));
```

---

## Crash 295: `a3db150c4737027f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231227`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ FLOAT CHECK (CURRENT_TIMESTAMP), c2 DATE CHECK (CURRENT_DATE NOT IN (CURRENT_TIME, CURRENT_TIME))); INSERT INTO q
```

---

## Crash 296: `d2b2b2e6130cb85b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000231271`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE CHECK (~'0 _ j1d_eW')); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*g', -2147483649, 
```

---

## Crash 297: `1881752a75be795d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234058`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT max(FALSE COLLATE BINARY) OVER (ORDER BY NULL ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES) AS etl8qi0wc
```

---

## Crash 298: `cf8fd83288de5e37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234230`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT max(FALSE COLLATE BINARY) OVER () AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_
```

---

## Crash 299: `8e68d1177d50656c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234252`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT max(CURRENT_TIME) OVER () AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l_33_jw_s36xq_rj1h1____4r_5p_b_7_11q11g8_558__6dfz0r__v_7w86_; SELECT
```

---

## Crash 300: `45356e3f774e51cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234441`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT count(*) OVER (ORDER BY 0 DESC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS etl8qi0wc_2g_3_y_5_u_9_n___39_0_hj_i__l
```

---

## Crash 301: `de140f182318f7ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000234698`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT max(TRUE) OVER (ORDER BY EXISTS (VALUES (min(TRUE) OVER ())) ASC NULLS LAST GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS etl8q
```

---

## Crash 302: `48ede8c40c57cb6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239510`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_TIME NOT IN (SELECT count(*) FILTER (WHERE CURRENT_DATE) AS a FROM p NOT INDEXED)); EXPLAIN QUERY PLAN VALUES (CU
```

---

## Crash 303: `c9380f1bd2310942` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241753`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT INTO p SELECT ALL *, * FROM (VALUES (TRUE) EXCEPT SELECT TRUE AS r1_h_n_1___01e6s28l_7nk_e_25n_u___iz1, CURRENT_TIME AS s_djz_z, TRUE, * FROM (SE
```

---

## Crash 304: `580e45de17a65c33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241989`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b INT NOT NULL); CREATE TABLE IF NO
```

---

## Crash 305: `dd895b7da83db3da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242041`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER UNIQUE); INSERT OR ABORT INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT NOT NULL); CREATE TAB
```

---

## Crash 306: `851cbc52a7d9c9fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245243`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT CAST(CURRENT_TIME AS NUMERIC) NO
```

---

## Crash 307: `74927b2a1015aa6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245898`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE t3 (c1) AS (VALUES (NULL)) SELECT count(*
```

---

## Crash 308: `a889e3cacd29b323` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246073`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC PRIMARY KEY, c1 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE q AS (VALUES (NULL)) SELECT NULL AS z04eq
```

---

## Crash 309: `e2ad0015d3a7dd89` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000246406`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT typeof(NULL) AS z04eq6p____m_lhg FROM p; CR
```

---

## Crash 310: `30152cfa31b0131b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247103`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(rowid REAL); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE s AS (SELECT *) SELECT max(CURRENT_TIMESTAMP) AS z04eq6p____m_lhg 
```

---

## Crash 311: `dbae97a18e9158d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249801`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) UNION ALL VALUES (FALSE) INTERSECT SELECT * FROM q WHERE NULL GROUP BY NULL ORDER BY NULL
```

---

## Crash 312: `fde51be4c99687a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249905`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL); VALUES (NULL) UNION VALUES (FALSE) INTERSECT SELECT * FROM q WHERE NULL GROUP BY NULL ORDER BY NULL ASC
```

---

## Crash 313: `24cb8086d4e4ccd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000134322`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC CHECK (CURRENT_TIME IN (SELECT * LIMIT CURRENT_DATE IN (SELECT * LIMIT TRUE IN (SELECT * LIMIT TRUE IN (SELECT * LIMIT CURRENT_DATE IN (SELECT * LIMIT NULL IN (
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
