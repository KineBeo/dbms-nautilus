# Crash Triage Report

**Total crashes:** 259  
**Unique crash sites:** 259  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 259 | 259 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `26c29713fb328fe2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000060`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c2) VALUES ((NULL ISNULL COLLATE NOCASE) NOT NULL IS CURRENT_TIMESTAMP IN (SELECT *), json_object('Ysll-K_', q.a ISNULL << ~EXIS
```

---

## Crash 2: `957f4432bcb711ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000163`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); INSERT OR ROLLBACK INTO t3 VALUES (CASE WHEN CAST(NULL AS FLOAT) COLLATE BINARY + NULL IS NOT NULL THEN random() NOTNULL * TRUE LIKE 
```

---

## Crash 3: `238fc351b2a9dd35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000354`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q (b) VALUES (~NULL GLOB group_concat(CURRENT_TIME IS NOT NULL, 'hk-2-G-_N-') OVER (PARTITION B
```

---

## Crash 4: `3f36877403b7e3ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000941`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c3, c2, c3, b, c1); INSERT OR IGNORE INTO p VALUES (-CURRENT_TIMESTAMP ISNULL BETWEEN json(changes() OVER ()) << RAISE(IGNORE) COLLATE RTRIM
```

---

## Crash 5: `ea47bc0499bc1646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001057`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT p.* FROM p WHERE EXISTS (SELECT CASE WHEN CURRENT_TIMESTAMP THEN NULL END IS NOT NULL / FALSE ISNULL >> FALSE 
```

---

## Crash 6: `cd604229a4ceb835` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001152`

```sql
SELECT substr('', -2147483649, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); WITH RECURSIVE t3 (a) AS (SELECT r.*, q.* FROM (SELECT CAST(CURRENT_TIMESTAMP AS TEXT) / TRUE IS NOT NULL |
```

---

## Crash 7: `b8b5c524af93fba1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001217`

```sql
SELECT printf('%.*f', 0, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ABORT INTO q VALUES (TRUE NOTNULL IS NULL, TRUE <= -NULL COLLATE NOCASE, coalesce(CURRENT_TIMESTAM
```

---

## Crash 8: `09804fc2fd271c91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001227`

```sql
SELECT substr('', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO s VALUES (CURRENT_DATE COLLATE BINARY - NULL ->> total_changes() FILTER (WHERE FALSE IS NUL
```

---

## Crash 9: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001429`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 10: `7ec501c48d3ab888` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001654`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO q VALUES (NULL, CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); SELECT prin
```

---

## Crash 11: `08cba649d60dea60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001964`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO p VALUES (NULL, CURRENT_TIME); ANALYZE t3; CREATE TABLE IF NOT EXISTS p(c1 BOO
```

---

## Crash 12: `d9b8ec947294d75c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002590`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT round(-1e308, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT CURRENT_TIME AS d
```

---

## Crash 13: `48964db060992f51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003339`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t1 AS MATERIALIZED (SELECT q.*, NOT CURRENT_DAT
```

---

## Crash 14: `711701d872ce9f8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003474`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); SELECT CURRENT_DATE IS NULL, * FROM (SELECT *, * FROM p WHERE NOT FALSE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO
```

---

## Crash 15: `580fa0a93929fdbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003510`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 16: `12d3f8da6e73723e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003568`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO q VALUES (-CASE WHEN TRUE THEN CURRENT_
```

---

## Crash 17: `b4ee7aa7620ddcca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003576`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER UNIQUE); SELECT * FROM (SELECT *, * FROM p WHERE CURRENT_DATE) AS sub1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO q VALUES (-CASE WH
```

---

## Crash 18: `3d570223fd61dba4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007200`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2); INSERT INTO t2 VALUES (TRUE); VALUES (+CURRENT_TIME); SELECT printf('%.*e', -2147483648, -1e308);
```

---

## Crash 19: `af748a222bdc5473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007247`

```sql
SELECT printf('%.*e', -2147483648, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r (c3) VALUES (c2 - NOT CURRENT_DATE NOT BETWEEN -FALSE IS NOT NULL >= CURRENT_DATE BETW
```

---

## Crash 20: `735657433c0c2f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007439`

```sql
SELECT printf('%lld', -2147483648, ' 8-hi 2__ -OI'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (NULL); ANALYZE t2; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE 
```

---

## Crash 21: `aaf4c205609d9c8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007641`

```sql
SELECT printf('%llu', 2147483647, 'I-7h_'); SELECT round(0.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO r DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT *, *;
```

---

## Crash 22: `f6f5e014f5d9f2ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007843`

```sql
SELECT round(0.01, 2147483648); SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); WITH RECURSIVE q (c1) AS NOT MATERIALIZED (WITH q AS MATERIALIZED 
```

---

## Crash 23: `fa14b7da98ca1bd0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008091`

```sql
SELECT substr('12G- -_N', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); INSERT OR ABORT INTO q VALUES (json_valid(CURRENT_TIME LIKE CURRENT_DATE ESCAPE ~T
```

---

## Crash 24: `408762f2f8b1d3a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008203`

```sql
SELECT printf('%.*e', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO q (a) VALUES ((FALSE) LIKE NULL ESCAPE total_changes(), CURRENT_DATE COLLATE BINAR
```

---

## Crash 25: `03877fca6fdfb448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008344`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 26: `e037b14374d050be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008498`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TAB
```

---

## Crash 27: `68a83cd9181f21bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008507`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TAB
```

---

## Crash 28: `6588741804a9b06f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009117`

```sql
SELECT substr(' 0 9 -gP_f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SELECT hex(zeroblob(1));
```

---

## Crash 29: `d222cb974f0ba792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010351`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (changes()); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, a); INSERT INTO p SELECT ALL * FRO
```

---

## Crash 30: `ab9b1434be6ad77d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011652`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (random()); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SELECT hex(zeroblob(1
```

---

## Crash 31: `de1c3e44cb527aa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011977`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(abs(CURRENT_DATE) AS BOOLEAN)); VALUES (FALSE); SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE I
```

---

## Crash 32: `b53bd22edae70b88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015007`

```sql
SELECT printf('%.*f', 1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p (c3) VALUES (CASE WHEN CURRENT_DATE THEN TRUE ELSE TRUE END + random(), CASE CURRENT_TIME IS NOT
```

---

## Crash 33: `c8e3a7f4733d6eb8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017726`

```sql
SELECT printf('%f', -2147483648, ''); SELECT printf('%.*e', 9223372036854775807, 1e-308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 34: `bca01f2f7d3d61b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018254`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 35: `b0fc0c0bf446e26c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018328`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT 0); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 36: `59a5ce5cb6181229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018344`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(a REAL UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 37: `409f4e1396e57062` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018351`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(b BLOB NOT NULL DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 38: `917b5ff4e3bc216f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018821`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NATURAL LEFT JOIN q NOT INDEXED USING (_rowid_, b) ORDER BY TRUE DESC LIMIT TRUE; EXPLAIN QUERY PLAN VALUES
```

---

## Crash 39: `106cc61f8c266424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018835`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT s.*, CAS
```

---

## Crash 40: `ea1001fbba9e2093` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022227`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts
```

---

## Crash 41: `e36c96e18138fb85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025498`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); WITH q AS (VALUES (TRUE)) INSERT INTO q VALUES (NULL NOTNULL <> avg(NULL LIKE CASE CURRENT_TIM
```

---

## Crash 42: `a482440c97f7f9a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025612`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) UNION ALL VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAUL
```

---

## Crash 43: `fdd92d89b24a5f36` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031567`

```sql
SELECT round(-1e308, 2147483647); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 44: `0dfffe3f9c3d9c1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032453`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 45: `e15f5a307a19b2ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032479`

```sql
SELECT printf('%.*f', 2147483647, 1e308); SELECT hex(zeroblob(2147483648));
```

---

## Crash 46: `038a43df1307ef2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039344`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, _rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 47: `df3de6b464e5f6b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039730`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP)); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SELECT hex(zeroblob(1));
```

---

## Crash 48: `d4863d6a3ed29cc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039739`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT '', c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 49: `d9da6abc24f9e6cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039752`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT 0, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 50: `0ec540abaed5ab14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041932`

```sql
SELECT printf('%.*g', 4294967296, 0.01); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 51: `6e4d04691e3f048f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044614`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT INTO q VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT DISTINCT * FROM q NOT INDEXED; PRA
```

---

## Crash 52: `27c265adbe3abb21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044621`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zerob
```

---

## Crash 53: `88c0d7beaec80698` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044670`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE = TRUE << CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (
```

---

## Crash 54: `86fde5589c7feab6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044687`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (FALSE * NOT CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INS
```

---

## Crash 55: `4051d036445aacef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045480`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT * FROM p GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIME COLLATE BINARY; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 56: `323f13469c08ed80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048137`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAULT VALUES; PRAGMA integrity_c
```

---

## Crash 57: `92698d4b6eb8304b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048465`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(-2147483649
```

---

## Crash 58: `cb1f7adc9879ec8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048529`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 59: `ca2b4879b8139beb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048654`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT last_insert_rowid(), 
```

---

## Crash 60: `66f678ad9642fcf0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049903`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO t3 VALUES (p.c2 COLLATE 
```

---

## Crash 61: `640941c67e268a58` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050233`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA integrity_check; SELECT printf('%.*d', -2147483649, -1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 62: `02f26b7d3c674138` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050823`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON NULL BETWEEN CURRENT_TIME AND CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 63: `dd49aba271c4d688` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053038`

```sql
SELECT substr('0-2SM-', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE q AS MATERIALIZED (SELECT +NULL << CURRENT_TIME || TRUE || NULL IS DISTINCT FROM NULL ORDE
```

---

## Crash 64: `7d944d62b0884b32` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053393`

```sql
SELECT printf('%.*s', -2147483648, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 (_rowid_) VALUES (FALSE NOT NULL / CURRENT_TIME) ON CONFLICT(c3) DO UPDATE SET rowid 
```

---

## Crash 65: `c0d1dbaa0a7106ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053579`

```sql
SELECT round(1e308, 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a); INSERT OR FAIL INTO p VALUES (CASE 0 NOT NULL WHEN CASE WHEN quote(RAISE(IGNORE)) FILTER (WHERE CURRENT_TIMESTAMP CO
```

---

## Crash 66: `13477c76ba93fb49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053626`

```sql
SELECT substr('oNz-1y1', 4294967295, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE s; SELECT printf('%lld', -2147483648, 'vL88_3N--8_8');
```

---

## Crash 67: `0644ed917f53ee8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056597`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON NULL IS TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEF
```

---

## Crash 68: `58bb9663d7a5363c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056775`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON json_object('QI_g 1 -_m  -_N_-', NULL); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 69: `3311b607513ef5d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056910`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON random(); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 70: `12f07910a597bf63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON NULL = CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSER
```

---

## Crash 71: `6898944fee89689c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057475`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VA
```

---

## Crash 72: `6db56efc27d509b5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057764`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE 
```

---

## Crash 73: `fae3b16a7ffa14e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058753`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR AB
```

---

## Crash 74: `c65839ee5b6d6f03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058783`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL * CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT
```

---

## Crash 75: `87cf213cb0f68250` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058982`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRE
```

---

## Crash 76: `6d05f08e1cb0adbb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059174`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TI
```

---

## Crash 77: `568464c61c2517e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 78: `bb6130d1a3c1dd06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059659`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRE
```

---

## Crash 79: `207726c62964e45f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059908`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 80: `396c98fa77c4833e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060173`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 VALUES (group_concat(~
```

---

## Crash 81: `da592e433b8930a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060257`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT '', c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 82: `4201ae367bcc4c94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060401`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT FALSE, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(1))
```

---

## Crash 83: `47f083654000a476` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060421`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT CURRENT_DATE, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL T
```

---

## Crash 84: `81635be95e56dcd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060475`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIMESTAMP AND TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SE
```

---

## Crash 85: `bfb4291488aaf8b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061025`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT X'5Ee87C0c004bE4'); CREATE TABLE IF NOT EXISTS q(b TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 86: `209255891398a26f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061127`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *;
```

---

## Crash 87: `f88e647759dfb657` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061526`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL IS last_insert_rowid() NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 88: `6e7a567071338aea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062571`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CR
```

---

## Crash 89: `d7e8a121a4f512eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062748`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT * FROM p NATURAL JO
```

---

## Crash 90: `d80d9a41f00392ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062772`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL > TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABORT INTO p VALUES (
```

---

## Crash 91: `c894e2a213e41eeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063114`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (FALSE IS TRUE NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p D
```

---

## Crash 92: `a7431cf8abd81b4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063358`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL = CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFA
```

---

## Crash 93: `33468758009388af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065311`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1); SELECT p.*, p.*, p.* FROM q JOIN q rh_zs51_12_v5y__7y____6vo2_ffg_7l____6_l61ex4n ON a IS NOT NULL COL
```

---

## Crash 94: `65299e60b848cc90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066218`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT * FROM p GROUP BY CURRENT_TIMESTAMP HAVING CURRENT_TIMESTAMP ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 95: `9da784081d4dd59e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066391`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAULT VALUES; PRA
```

---

## Crash 96: `4d3e0118522d120e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066397`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT * FROM p GROUP BY CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEF
```

---

## Crash 97: `4fe636fd8741a0f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066891`

```sql
SELECT printf('%.*g', 1, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c2, c1); INSERT INTO p VALUES (s.rowid -> CASE WHEN CURRENT_DATE ISNULL COLLATE RTRIM > TRUE THEN CU
```

---

## Crash 98: `5ca7066473869c22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073603`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w2 AS (
```

---

## Crash 99: `db37c217651090d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073723`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w
```

---

## Crash 100: `eb99887a9c908066` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074877`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1
```

---

## Crash 101: `205360b5db286e68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076285`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT X'bDbeA00D'); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 102: `ac2061e4086eb2e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077343`

```sql
CREATE TABLE IF NOT EXISTS p(a INT CHECK (RAISE(IGNORE)), c2 BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT * FROM p GROUP BY NULL; CREATE VIRTUAL 
```

---

## Crash 103: `1530f0471ea81399` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081260`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL NOT NULL DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT X''; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p
```

---

## Crash 104: `c78e91d465febd81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081555`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT substr('ylq', 0, -9223372036854775808); SELECT printf('%.*s', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO q VAL
```

---

## Crash 105: `8c85fc6310f35915` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081755`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); WITH RECURSIVE q (c3) AS (VALUES (FALSE) UNION SELECT
```

---

## Crash 106: `a02a4191eca4fedc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081967`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL) UNION SELECT * FR
```

---

## Crash 107: `98905719bbce5a2d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082140`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN VALUES (NULL) UNION SELECT * FRO
```

---

## Crash 108: `ae6fccd381b46e90` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082200`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT ' UZ8c', c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEX
```

---

## Crash 109: `d162f65a34c7c4d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090323`

```sql
SELECT printf('%llu', -1, ' B_7_--_J 0_'); SELECT substr('9sS O_U P7T-_C', 9223372036854775807, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); REPLACE INTO p VALUES (sum(+
```

---

## Crash 110: `8244b1c47dea7365` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091522`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CURRENT_TIME AS ds FROM p NOT INDEXED WHERE FALSE UNION ALL VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF N
```

---

## Crash 111: `8cc5725800bae24d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092144`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT
```

---

## Crash 112: `ed5a111d312a6687` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092429`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (TRUE); PRAGMA integrity_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 113: `b237b772c8cfa32f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092437`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; SEL
```

---

## Crash 114: `cea428e6e497bf5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092443`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integ
```

---

## Crash 115: `8c4d4f94259313d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092449`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT
```

---

## Crash 116: `12ee2299a0d39aae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093854`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (NULL * CURRENT_TIME)); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (FALSE); PRAGMA integrity_check; SELECT round(-1.0, 429496
```

---

## Crash 117: `5b854686fa8da48b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093946`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * C
```

---

## Crash 118: `6c416d2af766bfad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095213`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE IN (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY TRUE)); PRAG
```

---

## Crash 119: `3778db0bdde0092b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095923`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL DEFAULT FALSE, c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 120: `f800d05ae820b38b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096179`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT -231902044684773910305519550079760321910544938026811969567199086662554881259951303169375369836803220425020730879222074637960564670755582550024315811897299
```

---

## Crash 121: `1a841046e2d1c6e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096308`

```sql
SELECT printf('%.*s', -1, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); INSERT INTO t2 VALUES (--avg(NOT CASE NULL == CURRENT_TIMESTAMP WHEN CURRENT_DATE THEN CURRENT_TIMESTAMP 
```

---

## Crash 122: `74a73175d0c91f47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111163`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b FLOAT NOT NULL); INSERT INTO q VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT CURRENT_TIME COLLATE BINARY I
```

---

## Crash 123: `75e9554c0e1e3579` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113874`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_DATE AS TEXT)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT NULL << C
```

---

## Crash 124: `e88123140ba547e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114014`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_DATE AS BLOB)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *;
```

---

## Crash 125: `7f761dbb3c6b1e68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (abs(CURRENT_DATE)); VALUES (97.1E7875959); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAU
```

---

## Crash 126: `c9f2cea33c601c8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114332`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(TRUE AS INTEGER)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s DEFAULT 
```

---

## Crash 127: `fafac463b0aee730` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114878`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(changes() AS BLOB)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT CURRENT_TIME 
```

---

## Crash 128: `ed2f2ba7dd072bb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115004`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CAST(CURRENT_TIME AS REAL)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO p DEF
```

---

## Crash 129: `5669d4668f08d4fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115249`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (abs(CURRENT_DATE)); VALUES (FALSE); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 130: `ebb65711fa88b3e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115852`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); INSERT OR REPLACE INTO p VALUES (random()); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALY
```

---

## Crash 131: `d901a57b44a41659` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116081`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (random()); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT O
```

---

## Crash 132: `c2f0220bd76d4803` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119249`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); VALUES (avg(FALSE) FILTER (WHERE CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 133: `e40ee7c3c872f546` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119678`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (json_object('', CURRENT_TIMESTAMP)); VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 134: `1964d3774be3a1b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120116`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (CURRENT_TIMESTAMP NOT IN (CURRENT_TIME), CURRENT_DATE); SELECT printf('%.*f', 2147483647, 1
```

---

## Crash 135: `e4acebf99e2c1955` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000121550`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (length(CURRENT_TIMESTAMP)); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT
```

---

## Crash 136: `704297b89615da19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123142`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE IS NOT NULL >> NULL); EXPLAIN QUERY PLAN VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP
```

---

## Crash 137: `a467dea7e81d7e27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123609`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (json_valid(NULL)); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 138: `d794b2592a41b4f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124058`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (NULL) EXCEPT SELECT DISTINCT * FROM q NO
```

---

## Crash 139: `91ab026bbc0e37ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124236`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (CURRENT_TIMESTAMP)); SELECT printf('%.*f
```

---

## Crash 140: `9a3827ef04817ad3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE FALSE GLOB TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 141: `eef743b5ff3ebd3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126158`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB CHECK (CURRENT_DATE)); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT
```

---

## Crash 142: `97719ea08ac98229` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126257`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT UNIQUE, b INT); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 143: `be9a22690ce94ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126706`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT p.* FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 144: `9770677a01f65ba8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127328`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); 
```

---

## Crash 145: `62e51089e8bc52a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127488`

```sql
SELECT substr('', 1, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, a, b); INSERT OR FAIL INTO r VALUES (CURRENT_TIME MATCH CURRENT_TIMESTAMP >= FALSE IS NOT DISTINCT FROM NOT RAISE(IGN
```

---

## Crash 146: `5079b8799a0006e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127508`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT, rowid INTEGER NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT CASE WHEN NULL THEN -+NULL < TRUE || TRUE COLLATE RTRIM ELSE CURRENT_TIME END FROM q WHERE total_
```

---

## Crash 147: `cd9443e998094b2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128454`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY, b TEXT UNIQUE, c2 NUMERIC NOT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p (c2) VALUES (TRUE) ON CONFLICT(a) DO UPDATE SET a =
```

---

## Crash 148: `56df5a2b5b3527c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128813`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BLOB PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 149: `a25f48a4106920cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128880`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(_rowid_ NUMERIC PRIMARY KEY, c2 FLOAT UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE TRUE; SELECT printf('%.*f', 21474
```

---

## Crash 150: `48f84715329a3e24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129085`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT p.rowid FROM p NATURAL JOIN q WHERE TRUE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 151: `d61eaaacd8b15b08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130239`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT CHECK (CURRENT_TIMESTAMP), c1 BLOB); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 152: `6ce4a57d8ba29f43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131109`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (count(*) OVER (PARTITION BY CURRENT_DATE
```

---

## Crash 153: `0ad5023ac159b4aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131261`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (VALUES (count(*) OVER ())); CREATE VIRTUAL TABLE
```

---

## Crash 154: `0c22698b56804e24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131367`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE IN (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 155: `876f37f9c1a4f092` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132086`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NOT EXISTS (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DAT
```

---

## Crash 156: `4c84ea157c3cbc74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132578`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (json_valid(json_valid(json_valid(json_valid(CURRENT_TIMESTAMP))))); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION S
```

---

## Crash 157: `6607c4fd99fb59e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (json_valid(total_changes())); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRE
```

---

## Crash 158: `e7aa39e30179fe6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133698`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 159: `9a49417d59da2b2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137029`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMES
```

---

## Crash 160: `c05a5614bd5e945f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138722`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (TRUE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INT
```

---

## Crash 161: `44870c8f2bd34cf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139358`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 162: `40b6c5318aaf6373` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139885`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p V
```

---

## Crash 163: `21e82025181fb776` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140244`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (quote(CURRENT_DATE)); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VA
```

---

## Crash 164: `746ba2da98158b4e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140751`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); SELECT * FROM p INNER JOIN (VALUES (CURRENT_DATE)) AS a GROUP BY CURRENT_TIME; SELECT printf('%.*g'
```

---

## Crash 165: `bd02f4a6f9f928af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141033`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (random()); SELECT * FROM p GROUP BY json_object('QI_g 1 -_m  -_N_-', json_object('QI_g 1 -_m  -_N_-', json_object('QI_g
```

---

## Crash 166: `ba0ab7d90bb570a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161033`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH r AS (VALUES (NULL)) SELECT * FROM p INNER JOIN (WITH r AS (VALUES (NULL)) SELECT * FROM p INNER JOIN (WITH 
```

---

## Crash 167: `0c72f2931fc8fad0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161308`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) DEFAULT -23190204468477391030551955007976032191054493802681196956719908666255488125995130316937536983680322042502073087922207463796056467075558255002431581
```

---

## Crash 168: `a348eb14a35851c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162358`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE IN (SELECT * FROM p NOT INDEXED INNER JOIN p USING (c3, c3) WHER
```

---

## Crash 169: `479b9776656df0ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162443`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE IN (SELECT * FROM q NOT INDEXED WHERE TRUE GROUP BY TRUE)); PRAG
```

---

## Crash 170: `1a04809e99f53f94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162914`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE IN (VALUES (FALSE) UNION VALUES (TRUE))); PRAGMA integrity_check
```

---

## Crash 171: `eb7ba862ef5c9be3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163765`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB CHECK (CURRENT_TIMESTAMP <> TRUE)); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 172: `20c5611de6c54c80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176483`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT NULL, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE FALSE; CREATE VI
```

---

## Crash 173: `d311938697190cc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178237`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM (SELECT DISTINCT * FROM p LIMIT NULL) AS f77; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 174: `95eb96906d118f9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180110`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME GROUP BY NULL WINDOW w1 AS () LIMIT CURRENT_TIME OFFSET CURREN
```

---

## Crash 175: `c219eea3bf6963eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182457`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT NULL AS a FROM p GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 176: `8b7f168aeff7d4f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182666`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER DEFAULT X'FC54'); EXPLAIN QUERY PLAN SELECT * FROM p GROUP BY NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR IGNORE INTO q VALUES (FAL
```

---

## Crash 177: `9a7350bbcc8b7764` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185335`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT '--q _-59_3-Gt Ev', c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL
```

---

## Crash 178: `387b1671da6f48df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185491`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); CREATE TABLE IF NOT EXISTS q(a DATE UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT IN
```

---

## Crash 179: `e37beb8a2cbdb430` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185992`

```sql
SELECT printf('%x', -1, 'uv-_--h-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SELECT hex(zeroblob(1));
```

---

## Crash 180: `dd4e73d0099f6ab8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186011`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE << -CURRENT_DATE + CURRENT_TIME); EXPLAIN QUERY PLA
```

---

## Crash 181: `1e9dad17a856122a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186063`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL IS TRUE NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *; SELECT hex(zero
```

---

## Crash 182: `868190006a31f04d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186921`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY); VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF N
```

---

## Crash 183: `6c3f8270070c83d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187476`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PART
```

---

## Crash 184: `6d3abe033c1f959b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187496`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PART
```

---

## Crash 185: `88f7e2f3591aec61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187506`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIME > (CURRENT_TIMESTAMP COLLATE RTRIM > NULL), CURRENT_TIME > (CURRENT_TIMESTAMP > NULL), CURR
```

---

## Crash 186: `4e7bd542a5539d9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187516`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (RAISE(IGNORE) >= last_insert_rowid() FILTER (WHERE CURRENT_DATE)) UNION SELECT * FROM r NOT INDEXED WHER
```

---

## Crash 187: `a3124db100a2957e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187522`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT last_insert_rowid() FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY RAISE(IGNORE)
```

---

## Crash 188: `e61ccd883514b774` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187535`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM p WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS () OR
```

---

## Crash 189: `99c565cfc2e08002` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187542`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT NOT EXISTS (WITH RECURSIVE p (c2) AS (VALUES (RAISE(IGNORE))), q AS (VALUES (TRUE)) S
```

---

## Crash 190: `307d45861faea448` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187572`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (), w
```

---

## Crash 191: `3faf9ddba10bc402` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187585`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM p NOT INDEXED CROSS JOIN q NATURAL LEFT JOIN (WITH r AS (VALUES (NULL)) SELECT
```

---

## Crash 192: `18df21387de0a7e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187591`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY NULL HAVING ~CURRENT_DATE WINDOW w1 
```

---

## Crash 193: `16acb4f2e485b7fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187609`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM t3 INDEXED BY c1 WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS ()
```

---

## Crash 194: `17f1362e9e3af483` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187622`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_, c1); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW w1
```

---

## Crash 195: `eaf45cd462b6aa63` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187628`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT NOT group_concat(CURRENT_TIME != NULL, '7-5I-U-2v6Xa7d_ ') FILTER (WHERE NULL <> -113
```

---

## Crash 196: `778fa197faa28de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187639`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM (q NOT INDEXED) LEFT OUTER JOIN r NOT INDEXED JOIN t2 NOT INDEXED WHERE CURREN
```

---

## Crash 197: `1e836ad87d740f59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187650`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); SELECT * FROM q WHERE EXISTS (VALUES (NULL) UNION SELECT * FROM (t1 INDEXED BY c1 CROSS JOIN p NOT INDEXED USING (rowid, c2)) INNER JOIN (SELE
```

---

## Crash 198: `bf8498d32b5036d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194541`

```sql
SELECT printf('%d', -2147483648, '  '); SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 VALUES (CASE WHEN CURRENT_DATE THEN CURRENT_TIMESTA
```

---

## Crash 199: `38d756ae81fa3689` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194687`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT count(DISTINCT TRUE) AS a FROM p GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 200: `8d933fa3ce34718f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195107`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT NOT NULL); EXPLAIN QUERY PLAN VALUES (FALSE) UNION SELECT FALSE IS c1 AS a FROM p GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 201: `f221de85cb4b2594` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197063`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT *, * FROM p ORDER BY CURRENT_DATE ASC NULLS LAST, FALSE DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 202: `b2fc1dbb28590424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197359`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP AS ds FROM p INNER JOIN p ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 203: `9e77ee0105040707` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197911`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE ORDER BY count(*) OVER (ORDER BY NULL ASC GROUPS BETWEEN UNBOUNDED PRECEDING AND 
```

---

## Crash 204: `0f25c4ccb87255b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197985`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE ORDER BY CURRENT_DATE DESC, FALSE DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 205: `d0912df07263e18a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198300`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY NULL ORDER BY NULL ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); 
```

---

## Crash 206: `6e4ce5a85f42d1d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199414`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); 
```

---

## Crash 207: `085228fb1417ec03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199705`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIME OR CURRENT_DATE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR ABOR
```

---

## Crash 208: `4b920338fba83e79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200510`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (b)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 209: `f96e7cf9e1c55be9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201328`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT X'Be714d', rowid INTEGER); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 210: `aa7e86d6b63b13c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201347`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (CURRENT_TIME NOT IN (FALSE, NULL, FALSE))); INSERT INTO p
```

---

## Crash 211: `2015a79ff00cb37c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201374`

```sql
CREATE TABLE IF NOT EXISTS p(b INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); INSERT OR REPLACE INTO p VALUES (quote(CASE WHEN FALS
```

---

## Crash 212: `ed1beda0638f0252` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203355`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE FALSE NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE NOT LIKE CURRENT_DATE NOT LIKE CURRENT_TIME NOT LIKE NULL)); INSERT
```

---

## Crash 213: `8cf8bb7553ac4dea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203492`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE FALSE NOT LIKE NULL NOT LIKE FALSE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 214: `7aa1da9ddeb38de3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203498`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE FALSE NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; C
```

---

## Crash 215: `605504d423a77187` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203505`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE FALSE NOT LIKE NULL NOT LIKE CURRENT_TIMESTAMP NOT LIKE TRUE NOT LIKE CURRENT_DATE NOT LIKE FALSE)); INSERT INTO p DEFAULT VALUE
```

---

## Crash 216: `b31c43dbf08d46b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203850`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (last_insert_rowid() NOT LIKE CURRENT_TIMESTAMP NOT LIKE CURRENT_TIMESTAMP NOT LIKE NULL NOT LIKE last_insert_rowid() NOT LIKE CURRENT_TIME NOT LIKE TRUE NOT 
```

---

## Crash 217: `f83a13f4e4427fbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204398`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255) NOT NULL DEFAULT 545288906592162581656691642007.623E+7); CREATE TABLE IF NOT EXISTS q(b TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE 
```

---

## Crash 218: `b24eb76c16652d31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204651`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIME IS NOT CURRENT_TIMESTAMP)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSER
```

---

## Crash 219: `224e4813ea4146ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205911`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL * X''); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT *, CAST(NULL B
```

---

## Crash 220: `34dac25e188400d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205946`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NULL * NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT *, CAST(NULL 
```

---

## Crash 221: `9de84bf2e80d288c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206267`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (TRUE * ~TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAU
```

---

## Crash 222: `a7276fa7f41a2290` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207357`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_che
```

---

## Crash 223: `c2b3ea8c5009a12f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207585`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 224: `a49f7903441e529d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207591`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 225: `18cfb2ecfc718506` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208329`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); INS
```

---

## Crash 226: `36416d8cfbc99327` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000208797`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TI
```

---

## Crash 227: `660ce4afd8725d1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (-NOT CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO s 
```

---

## Crash 228: `6bcbb265f48519ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210333`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON NULL NOT IN (VALUES (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2
```

---

## Crash 229: `f0d85db5a2b7812d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210867`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON FALSE % CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INT
```

---

## Crash 230: `e56104b6ad21f08d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000210950`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON CURRENT_DATE IN (SELECT * FROM p NOT INDEXED WHERE TRUE GROUP BY TRUE); SELECT printf('%.
```

---

## Crash 231: `2feed31c6ce5b57f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211604`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 TEXT); SELECT * FROM p JOIN p xym6l_2 ON FALSE IS NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT *;
```

---

## Crash 232: `fa88f810d3632a53` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217077`

```sql
SELECT printf('%lli', -9223372036854775808, 'A5-4'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT p.* FROM (SELECT NOT CASE CASE CURRENT_DATE NOT NULL OR +CURRENT_TIMESTAMP WHEN NUL
```

---

## Crash 233: `ce8bc2da6e954ee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000217298`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN VALUES ((
```

---

## Crash 234: `30f945e8733dc503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218328`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS f77 LIMIT TRUE * CURRENT_TIME; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 235: `1ab2413c235502f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218454`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS f77 LIMIT 0; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 236: `fd6c7f1bca5b9578` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218611`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT DISTINCT * FROM (VALUES (CURRENT_DATE)) AS f77 LIMIT TRUE; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 237: `e13d322d4a57d159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219560`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT 8.679e-9653966282041441398202); CREATE INDEX IF NOT EXISTS idx1 ON p(rowid); INSERT OR REPLACE INTO p VALUES (random()); PRAGMA integrity_check
```

---

## Crash 238: `5fa3548018b39b72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000222452`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (NOT json_object('QI_g 1 -_m  -_N_-', CURRENT_TIMESTAMP)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 239: `aa1c787fa7b23acb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225054`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT OR ABORT INTO p VALUES (FALSE * ~TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN
```

---

## Crash 240: `df75c77b8dc3381a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225701`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN NO
```

---

## Crash 241: `383874f010171983` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226540`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (_rowid_)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR IGNORE INTO q VALUES (CU
```

---

## Crash 242: `5ee067dacf1392ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228699`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (NULL IS last_insert_rowid() NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSE
```

---

## Crash 243: `6c78a7234885fa59` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000228810`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE CHECK (CURRENT_TIME NOT LIKE TRUE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSERT OR ABORT INT
```

---

## Crash 244: `6aee0523a92fcf73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000230642`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT DEFAULT X'Caef'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANA
```

---

## Crash 245: `7753669876f6d6d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE, TRUE ORDER BY count(DISTINCT CURRENT_DATE) FILTER (WHERE CURRENT_TIMESTAMP) ASC 
```

---

## Crash 246: `7f7e67a02d8ce453` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232706`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE, TRUE ORDER BY CURRENT_DATE ASC, FALSE DESC; SELECT printf('%.*f', 2147483647, 1e
```

---

## Crash 247: `859718f676dfe461` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232854`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT TRUE AS a FROM p ORDER BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VAL
```

---

## Crash 248: `cdc4f670cf56c8b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT max(NULL) FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC NULLS LAST, CURRENT_DATE DESC NULLS LAST) AS a FROM 
```

---

## Crash 249: `6bf5dc923cc44db6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237218`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL CHECK (p.a)); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL) UNION SELECT * FROM r NOT INDEXED WHERE CURRENT_TIME GROUP BY CURRENT_TIMESTAMP WINDOW 
```

---

## Crash 250: `512a0301d86e63ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000244682`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 REAL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 TEXT PRIMARY KEY); CREAT
```

---

## Crash 251: `b287e9f843d4fdaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250710`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE CHECK (TRUE)); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL LEFT JOIN p NOT INDEXED WH
```

---

## Crash 252: `ecd9a17b0d7efb8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250858`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL LEFT JOIN p NOT INDEXED W
```

---

## Crash 253: `36ac726c4859ed7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250895`

```sql
CREATE TABLE IF NOT EXISTS p(a INT NOT NULL DEFAULT NULL, c3 FLOAT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p WHERE FALSE; S
```

---

## Crash 254: `0377d0e319d07840` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262312`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB DEFAULT X'Be714d', rowid INTEGER); INSERT INTO p DEFAULT VALUES; VALUES (CAST(CURRENT_TIMESTAMP AS BOOLEAN)) UNION ALL VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE 
```

---

## Crash 255: `9e4b3ec8d63062b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000262465`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 256: `05d6f15cc74579dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264154`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (json_type(TRUE)); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 257: `6befed4e4cc26569` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000264997`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 FLOAT PRIMARY KEY
```

---

## Crash 258: `c8ecc6af4d3276c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000267100`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE IN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIME OR CURRENT_TI
```

---

## Crash 259: `103f656a5db285fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000271913`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(b FLOAT PRIMARY KEY); SELECT * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED NATURAL JOIN q; CREATE VIRTUAL TABLE IF NO
```

---
