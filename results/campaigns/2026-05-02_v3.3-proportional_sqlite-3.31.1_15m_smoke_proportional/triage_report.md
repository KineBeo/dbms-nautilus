# Crash Triage Report

**Total crashes:** 117  
**Unique crash sites:** 117  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 117 | 117 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `b47ebaff967f6844` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000054`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (FALSE <= RAISE(IGNORE) + RA
```

---

## Crash 2: `dd47ec8b711d225f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000198`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b, b); SELECT t1.* FROM (SELECT CURRENT_DATE LIKE FALSE IS NOT NULL LIKE changes() OR FALSE, p.* FROM t1 WHERE (CURRENT_DATE COLLATE BINARY) IS
```

---

## Crash 3: `1b72548ffe859f50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000589`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); SELECT TRUE ISNULL AS c FROM r NOT INDEXED LEFT JOIN q INDEXED BY c1 USING (b, b) INTERSECT SELECT CURRE
```

---

## Crash 4: `c9086a1b9830e4dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001099`

```sql
SELECT substr('', 2147483647, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); EXPLAIN QUERY PLAN SELECT p.* FROM t2 LEFT JOIN t2 AS a USING (c3, c2) WHERE CURRENT_TIMESTAMP <= 
```

---

## Crash 5: `014ad942bfac7d57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002130`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT UNIQUE); VALUES (NULL ISNULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR REPLACE INTO q VALUES (~-CURRENT_TIMESTAMP IS RAISE(IGNORE) NOT IN
```

---

## Crash 6: `ed5093010c032038` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002852`

```sql
SELECT printf('%.*s', 4294967296, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO p VALUES (CASE (NULL) WHEN CURRENT_TIMESTAMP THEN -+-changes() & TRUE = RAISE(
```

---

## Crash 7: `3bddfcc30b316237` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003597`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CRE
```

---

## Crash 8: `841c97d95d302372` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003642`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); INSERT OR REPLACE INTO q VALUES (CASE WHEN CURRENT_DATE IS NOT DISTINCT FROM FALSE MATCH 
```

---

## Crash 9: `02d8d990f2973cc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003897`

```sql
SELECT round(1e308, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO t3 VALUES ((VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE NOT LIKE TRUE) ORDER BY F
```

---

## Crash 10: `28781379fbca35bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003939`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER NOT NULL); CREATE TABLE IF NOT EXISTS q(b DATE); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (FALSE IS NOT NULL
```

---

## Crash 11: `7a19b747f9f857c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007096`

```sql
SELECT printf('%.*g', 4294967296, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL DEFAULT TRUE); C
```

---

## Crash 12: `78e6ac858c3e27cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007116`

```sql
SELECT hex(zeroblob(-1)); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t1 VALUES (FALSE <= RAISE(IGNORE) + RAISE(IGNORE) >> F
```

---

## Crash 13: `725331afff34cf83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007469`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, c3, c1, c2, _rowid_); INSERT INTO t3 (c1, a) VALUES (-p.b IS TRUE IS RAISE(IGNORE) COLLATE NOCASE GLOB max(EXISTS (SELECT * ORDER BY TR
```

---

## Crash 14: `b9b65d4365ae4a76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007626`

```sql
SELECT printf('%.*f', 4294967295, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c2); INSERT INTO t2 DEFAULT VALUES; ANALYZE q; CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN NOT NULL); C
```

---

## Crash 15: `08c6dd1549ba6b0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007909`

```sql
SELECT substr('--FKs_bZXCK7 n39', -2147483649, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1); SELECT CASE json_type(-RAISE(IGNORE) IS NULL) FILTER (WHERE -FALSE MATCH TRUE N
```

---

## Crash 16: `2ed7ecdd633debdb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008000`

```sql
SELECT printf('%f', 2147483647, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a); WITH RECURSIVE q AS NOT MATERIALIZED (SELECT DISTINCT *, p.* FROM p NOT INDEXED NATURAL JOIN t3 AS g6_
```

---

## Crash 17: `857b440a1f79a367` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008123`

```sql
SELECT round(-1e308, 1); SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (CASE ~CASE WHEN CURRENT_TIMESTAMP NOT IN (CURRENT_TIMESTAMP) THEN NULL 
```

---

## Crash 18: `fdb895aad514482d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008341`

```sql
SELECT printf('%.*s', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); EXPLAIN QUERY PLAN SELECT t3.* FROM q WHERE TRUE <> CURRENT_TIME GROUP BY CURRENT_TIME LIKE FALSE ESCAPE FAL
```

---

## Crash 19: `6e6a634e56f883bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009650`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*e', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 20: `ec0080b2a13afda0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009658`

```sql
SELECT printf('%.*f', -2147483648, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 21: `3dc77339402d637e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009671`

```sql
SELECT printf('%.*f', 4294967295, -1.0); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 22: `32539e8ca97629bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009677`

```sql
SELECT printf('%.*e', 4294967295, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 23: `06a0a1e7fae91f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009687`

```sql
SELECT printf('%.*s', 4294967295, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 24: `90790446f290787b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009712`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT substr('__3__kk  hI_e', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 25: `6ba63e795ab7d954` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009721`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 26: `32c51e0dab5cf5ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009734`

```sql
SELECT printf('%.*f', 4294967295, 1e308); CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE -TRUE GROUP BY CURRENT_DATE HAVING 
```

---

## Crash 27: `5b66c0f15e2c0719` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009756`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT substr('-4zbF-KH', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 28: `d7d985707df6e353` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009773`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*d', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 29: `aa5a1807799d5672` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009797`

```sql
SELECT printf('%.*f', 2147483647, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 30: `8cbaa23c7522666e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009806`

```sql
SELECT printf('%.*d', 4294967295, 1e308); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 31: `636a4b6ba819558e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009832`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT round(0.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 32: `519f0eaaf01a3dec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009840`

```sql
SELECT printf('%.*f', 4294967295, 1e308); SELECT printf('%.*d', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO t2 DEFAULT VALUES; SELECT *;
```

---

## Crash 33: `398e0e043c450199` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010103`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT I
```

---

## Crash 34: `fedcc9789d2c9201` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010843`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT CURRENT_DATE, b DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT
```

---

## Crash 35: `3740ed64f5d1a279` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011183`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 36: `2bdbd2d4c89a749c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011833`

```sql
SELECT printf('%.*g', 2147483647, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE t3 (c3, b) AS NOT MATERIALIZED (SELECT *) INSERT INTO q VALUES (FALSE); PRAGMA integ
```

---

## Crash 37: `af933bcec4c72f93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012085`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT * LIMIT CURRENT_TIMESTAMP OFFSET last_insert_rowid() FILTER (WHERE FALSE) OVER (ORDER BY CURRENT_TIME DESC ROWS BETWEEN NUL
```

---

## Crash 38: `71fbc45c9e9ab0d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012992`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2); EXPLAIN QU
```

---

## Crash 39: `d20f7273d0a92140` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013004`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 40: `56df54b73e58c49f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013112`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 41: `07c041e276321570` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013143`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 42: `fdf45fb64087f888` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014080`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 9223372036854775807, 0
```

---

## Crash 43: `c96bd753acad5e54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014288`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (CURRENT_TIME), c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 92233720
```

---

## Crash 44: `24e83d2fc3f58478` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014537`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ REAL PRIMARY KEY, c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 92233720368
```

---

## Crash 45: `a7873057d34b2950` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016312`

```sql
SELECT printf('%x', 1, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q SELECT DISTINCT * FROM r NOT INDEXED LEFT JOIN p CROSS JOIN q NOT INDEXED WHERE CURRENT_DATE ORDER BY
```

---

## Crash 46: `4fc29dc12cbb11e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020312`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY TRUE HAVING FALSE; SELECT printf('%.*g', 92233720368547
```

---

## Crash 47: `bd132755acfbde5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020520`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (FALSE); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 48: `9f063eb3304aed7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020526`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY NULL; SELECT printf('%.*g', 9223372036854775807, 0.01);
```

---

## Crash 49: `cfb49ee00e524307` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020878`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY TRUE HAVING NULL; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 50: `15812fcf0c58840d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020940`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VALUES (max(C
```

---

## Crash 51: `6c7a771474bcb57d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021130`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY TRUE HAVING CURRENT_TIME % TRUE; CREATE VIRTUAL TABLE I
```

---

## Crash 52: `1bae57b8a4853442` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021705`

```sql
SELECT substr('_--X-JY- -_e', 2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, a, a); REPLACE INTO q VALUES (~EXISTS (SELECT q.* UNION ALL SELECT * FROM q NOT INDEXED 
```

---

## Crash 53: `284d2c42b6319ac4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030572`

```sql
SELECT substr('e _-', 4294967296, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO s VALUES (FALSE < FALSE COLLATE BINARY REGEXP ~CURRENT_TIMESTAMP || CURR
```

---

## Crash 54: `2087765c9e0fbafb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030826`

```sql
SELECT printf('%.*d', 2147483647, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO s (a) VALUES (TRUE -> CURRENT_TIMESTAMP + CURRENT_TIME BETWEEN CURRENT_TIME = -CURRENT_TI
```

---

## Crash 55: `e3dc986baa97df87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037618`

```sql
SELECT printf('%.*s', 4294967296, 0.01); SELECT substr(' 0_- k-', 0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP COLLATE RTRI
```

---

## Crash 56: `fd3c0aa03b3c5828` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046285`

```sql
SELECT round(-1.0, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); EXPLAIN QUERY PLAN SELECT *;
```

---

## Crash 57: `3b990ce2f0c5fbd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047978`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME / FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 58: `af613b6d00146669` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048034`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 59: `ef41b58ac3367c98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050289`

```sql
SELECT printf('%.*g', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, c2); INSERT INTO p VALUES (unicode(p.a & (-CURRENT_DATE) LIKE CURRENT_DATE - CURRENT_TIME = count(*) IS C
```

---

## Crash 60: `f66c3a58fdf89bd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055535`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), rowid GENERATED ALWAYS AS (a) NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELEC
```

---

## Crash 61: `e9edf4643289d7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059377`

```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 62: `1234c12e5e835a8b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062594`

```sql
SELECT substr('4 l7nn6---0_-XQ89', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT CURRENT_TIME * NULL || sum(CURRENT_TIME) = CASE WHEN RAISE(IGNORE) THEN NULL REGEXP CU
```

---

## Crash 63: `0824c0fef8fd118f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064296`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED , (VALUES (FALSE)) AS lh6; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT +total_cha
```

---

## Crash 64: `69203c89ca835ef8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065451`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT TRUE - FALSE FROM p NATURAL JOIN p WHERE CURREN
```

---

## Crash 65: `beaa7b44fcb842b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065606`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT CURRENT_TIMESTAMP FROM p NATURAL JOIN p WHERE C
```

---

## Crash 66: `43c09f0103057ac8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066057`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT * FROM p NATURAL JOIN p W
```

---

## Crash 67: `1bb8d3694b9f7b1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066207`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE I
```

---

## Crash 68: `41c5c0ea8691e774` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066273`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p VALUES (CURRENT_DATE) ON CONFLICT DO NOTHING; SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE TABL
```

---

## Crash 69: `01562b5e62abb8eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074808`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 70: `1fcdfe1332f4661d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074876`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (random()); PRAGMA integrity_check; SELECT printf('%.*g', 92233720368547758
```

---

## Crash 71: `2444f46e181ee54c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075442`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a REAL
```

---

## Crash 72: `f2f08794587b1484` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075740`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR ROLLBACK INTO p VALUES (FALSE); PRAGMA integrity_check; SELECT printf('%.*g', 9223372036854775807,
```

---

## Crash 73: `c41562fca50bd999` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086426`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE >> CURRENT_TIMESTAMP GROUP BY TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 74: `b48f4b625dc9d9f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087525`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT 6505.4126542298748462291485038015237476548250705318330657943452039979133115121995143913107364294773492170); CREATE VIEW IF NOT EXISTS v1 AS SELECT
```

---

## Crash 75: `b358322049e6930b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087693`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 76: `b148f61593d9b215` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087700`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL DEFAULT FALSE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 77: `7d8f7f10827a80f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090871`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING NULL IS NULL; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 78: `d0ff7f582e75b520` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091157`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING NOT NULL IS NULL & TRUE; SELECT printf('%.*
```

---

## Crash 79: `b8bb36827626d289` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091339`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING NOT NULL; SELECT printf('%.*g', -2147483649
```

---

## Crash 80: `70e74d615f07dba3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091533`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE NULL GROUP BY CURRENT_DATE HAVING CURRENT_DATE < CAST(CURRENT_DATE AS TEXT); 
```

---

## Crash 81: `bd62b761f2286cf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091851`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE NULL GROUP BY CURRENT_DATE HAVING CURRENT_DATE < CAST(NULL IS NULL AS TEXT); 
```

---

## Crash 82: `60552ae9916dadcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092335`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE HAVING CURRENT_TIMESTAMP COLLATE BINA
```

---

## Crash 83: `3b42cfaa13b88e3f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092458`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE HAVING CURRENT_DATE BETWEEN NULL AND 
```

---

## Crash 84: `c9a7f7d318d8b8e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093266`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * FROM (VALUES (NULL)) AS a WHERE -TRUE GROUP BY NULL; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 85: `7f0b10ba5d3d8c35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093398`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); SELECT * FROM (VALUES (NULL)) AS a WHERE CURRENT_DATE GROUP BY NULL; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 86: `52dbecc69fa34ba7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094027`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING (VALUES (TRUE * TRUE IS NULL)) <= FALSE; SE
```

---

## Crash 87: `84792e5a8633bfc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094487`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (count(*) FILTER (WHERE NULL)); SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIR
```

---

## Crash 88: `e13fa6c719edd728` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094859`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING count(*) FILTER (WHERE TRUE) IS NOT NULL <=
```

---

## Crash 89: `632ff12749f7cde0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095108`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING CURRENT_TIMESTAMP <= FALSE; CREATE VIRTUAL 
```

---

## Crash 90: `864e5528c6097423` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095114`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE TRUE GROUP BY CURRENT_DATE HAVING FALSE IS NOT NULL <= FALSE; CREATE VIRTUAL 
```

---

## Crash 91: `245dda4cc0cef575` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095128`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE CURRENT_DATE IS FALSE GROUP BY CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 92: `984805cbbb3dc07c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095381`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE -FALSE GROUP BY FALSE; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 93: `b31424fbb127d4f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095547`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE -CURRENT_DATE IS FALSE IS NULL GROUP BY CURRENT_DATE HAVING CURRENT_TIMESTAMP
```

---

## Crash 94: `9a84c102f68c3583` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095738`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE FALSE GROUP BY CURRENT_DATE HAVING CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF
```

---

## Crash 95: `53301207996cef14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095745`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE -NULL GROUP BY CURRENT_DATE HAVING CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF
```

---

## Crash 96: `f402bfbb18b53a4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098135`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL, c2 INTEGER GENERATED ALWAYS AS (RAISE(IGNORE)) STORED); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); SELECT TRUE AS g_ FROM p CROSS JOIN p NOT INDEXED WHERE 
```

---

## Crash 97: `4a794b079ad2453c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098367`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p ORDER BY FALSE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 98: `da8eb47c89499d6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099596`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_TIME FROM p NOT INDEXED WHERE TRUE GROUP BY CURRENT_TIME; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 99: `d160edcacb902a27` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000099616`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 100: `8093caa70b8315a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100193`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p NATURAL JOIN p NOT INDEXED WHERE TRUE GROUP BY CURRENT_TIME; SELECT printf('%.*g', 
```

---

## Crash 101: `4ef31986f53ea625` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103182`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (TRUE AND NULL), c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*f', 2147483
```

---

## Crash 102: `12ad1706875679f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104281`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (FALSE || NULL), c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 103: `7ae3065cc4d51b21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104712`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (TRUE <> last_insert_rowid()), c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL 
```

---

## Crash 104: `d1357d7a1d6fea49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105056`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT CHECK (last_insert_rowid() BETWEEN NULL AND CURRENT_TIME), c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA quick_
```

---

## Crash 105: `bea7846271fdb9c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106762`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT FALSE LIKE CURRENT_TIMESTAMP NOT LIKE RAISE(IGNORE) ESCAPE TRUE FROM r NOT INDEXED WHERE FALSE; INSERT INTO p DEFA
```

---

## Crash 106: `31071e7671345e96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107246`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO
```

---

## Crash 107: `0a1b717225d7d112` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107279`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT UNIQUE, c3 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * EXCEPT SELECT * FROM t2 WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE WINDOW w1 AS (), w2 AS ()
```

---

## Crash 108: `10a42555c6560e24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107476`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB, c1 GENERATED ALWAYS AS (a + 31) UNIQUE, a DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 109: `99780af597edb184` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107726`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC NOT NULL DEFAULT -251384.829791244105623422693656070687791527593198750397319229104432418853825678434799657496200949683100489114791241718869270797634539472441
```

---

## Crash 110: `4fe0539bf659469b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107762`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER NOT NULL DEFAULT '_ k6_Ud4_0__ _3'); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', -2147483649, 0.01);
```

---

## Crash 111: `1e36980bfcfb319b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108243`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT CURRENT_TIME FROM p INNER JOIN p NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 112: `ce4fc1bfa0039655` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000111539`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL DEFAULT -79847, b DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTU
```

---

## Crash 113: `31cf09c082a94c45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112390`

```sql
SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); SELECT he
```

---

## Crash 114: `3075433b5c8b870e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113346`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT PRIMARY KEY); INSERT OR IGNORE INTO q VALUES ((SELECT DISTINCT * FROM p)); PRAGMA quick_check; CREATE VIRTUAL TABLE I
```

---

## Crash 115: `e55a32ebf5750e98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113491`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 TEXT PRIMARY KEY); INSERT OR IGNORE INTO q VALUES ((VALUES (CURRENT_TIMESTAMP))); PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 116: `d223e6829f0bdf07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119307`

```sql
SELECT round(1e-308, -2147483649); SELECT round(1e-308, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, c1); WITH RECURSIVE q AS NOT MATERIALIZED (VALUES (CURRENT_TIM
```

---

## Crash 117: `0f65cf6e1ff5e665` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120319`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); SELECT * FROM p JOIN p a ON TRUE | CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---
