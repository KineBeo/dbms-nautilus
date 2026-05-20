# Crash Triage Report

**Total crashes:** 43  
**Unique crash sites:** 43  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 43 | 43 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `f8eed1a184e776b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000445`

```sql
SELECT fpdecode(1e308, 2147483648, 65536); CREATE TABLE IF NOT EXISTS p(a REAL, b AS(b) UNIQUE); INSERT INTO t1 VALUES (CASE changes() FILTER (WHERE (FALSE)) WHEN NOT CASE NOT NULL WHEN CURRENT_DATE T
```

---

## Crash 2: `96b82037e24d9683` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018991`

```sql
SELECT fpdecode(-1e308, 2147483648, -9223372036854775808); SELECT trunc(-9e999);
```

---

## Crash 3: `00a9897468396ae5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023396`

```sql
SELECT fpdecode(1e308, -2147483648, 65536); SELECT trunc(1.0);
```

---

## Crash 4: `14fd39ca51710cb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023412`

```sql
SELECT fpdecode(1e308, 2147483648, 2147483647); SELECT trunc(1.0);
```

---

## Crash 5: `cfc30d8ee7e752ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023426`

```sql
SELECT fpdecode(1.0, 2147483648, 65536); SELECT trunc(1.0);
```

---

## Crash 6: `56f6748ad7901407` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023446`

```sql
SELECT fpdecode(1e308, 2147483648, 9223372036854775807); SELECT trunc(1.0);
```

---

## Crash 7: `63d1d1c4b3f2519f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023508`

```sql
SELECT fpdecode(1e308, 2147483648, 0); SELECT trunc(1.0);
```

---

## Crash 8: `e23cf0671b2fa6c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023543`

```sql
SELECT fpdecode(1e308, 2147483648, -1); SELECT trunc(1.0);
```

---

## Crash 9: `79eddb8c53e64718` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025468`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC GENERATED ALWAYS AS (+RAISE(IGNORE) NOT NULL) STORED, c3 VARCHAR(255)); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL 
```

---

## Crash 10: `335a37e5386b39aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025707`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100000) SELECT string_agg(
```

---

## Crash 11: `1975b9c2aad7f30f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025713`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100000) SELECT string_agg(CAST(
```

---

## Crash 12: `b15bfafd05e6d670` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (CURRENT_TIMESTAMP) UNION SELECT NULL FROM jsonb_tree('[{"a":1},{"b":2}]') GROUP BY NOT CURRENT
```

---

## Crash 13: `6c965363d3457cbc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045650`

```sql
SELECT substr('X--0', -1); SELECT fpdecode(1e308, 2147483648, 4294967296);
```

---

## Crash 14: `c184d6ea82e6bb65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052153`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100000) SELECT DISTINCT * FROM jsonb_each('{}') ORDER BY CURRENT_TIMESTAMP DESC NULLS LAST LIMIT FALSE; SELECT fpdecode(1e30
```

---

## Crash 15: `df73003ba8bc2bcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053076`

```sql
EXPLAIN VALUES (TRUE) EXCEPT VALUES (TRUE); SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 16: `6bd518f97316666f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059306`

```sql
SELECT char(FALSE, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL, CURRENT_DATE, CURRENT_TIME, TRUE); SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 17: `93f878ced3ae7136` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064097`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE INDEX IF NOT EXISTS idx1 ON p(_rowid_); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 18: `1c009def50ca2344` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064219`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 19: `fa7519642b4f8d81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065666`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p n ON NULL IS DISTIN
```

---

## Crash 20: `a9a48b9c8d5411ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088222`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS MATERIALIZED (SELECT *) SELECT NULL AS of, * FROM json_tree('{"a":1}'); SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 21: `a319d71801098f76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090934`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT TRUE IS NOT FALSE AS bo FROM json_each('[1,2,3]') GROUP BY FALSE ORDER BY CURRENT_TIMESTAMP ASC; SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 22: `6beae3e795e8225d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091081`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT * FROM json_each('[1,2,3]') GROUP BY FALSE ORDER BY CURRENT_TIMESTAMP ASC; SELECT fpdecode(1e308, 2147483648, 65536);
```

---

## Crash 23: `c348ccb3e0e39014` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102879`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p n ON CURRENT_TIME C
```

---

## Crash 24: `c971a9848c7596d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103020`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT parseuri(TRUE) FROM p; SELECT fpdec
```

---

## Crash 25: `92de108f22aa3177` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103027`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN p n ON CURRENT_DATE I
```

---

## Crash 26: `1d4cd05ecca00824` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107069`

```sql
SELECT round(-1.0, -1); SELECT fpdecode(1e308, -2147483648, 65536);
```

---

## Crash 27: `15a0b1d4115b85d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114589`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(e INT NOT NULL); INSERT INTO p VALUES (FALSE) RETURNING NOT EXISTS (VALUES (TRUE)), RAISE(IGNORE); PRAGMA integr
```

---

## Crash 28: `e23dfce1c5a3164b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114895`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(e INT NOT NULL); INSERT INTO p VALUES (FALSE) RETURNING NOT EXISTS (VALUES (cume_dist() OVER () IN (CURRENT_TIME
```

---

## Crash 29: `02ef8516b7b8533c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115237`

```sql
SELECT hex(zeroblob(32768)); SELECT fpdecode(1e308, 2147483648, 2147483647);
```

---

## Crash 30: `d67520cbe398dc56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000120119`

```sql
EXPLAIN SELECT * FROM json_each('{}') NATURAL LEFT JOIN json_each('{"a":1}') WHERE FALSE IN (CURRENT_DATE); SELECT fpdecode(1e308, -2147483648, 65536);
```

---

## Crash 31: `507493a175748266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136688`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'f38A01'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT fpdecode(1e308, 2147483648, 4294967296);
```

---

## Crash 32: `0b0775ae3686792a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137130`

```sql
SELECT concat(4294967295, -1e308, '--g_-5Fc '); SELECT fpdecode(1e308, 2147483648, -2147483648);
```

---

## Crash 33: `858c1a93e8293968` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140856`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(CURRENT_DATE << -CURRENT_TIME COLLATE NOCASE) || CURRENT_TIMESTAMP) UNION VALUES (FALSE); 
```

---

## Crash 34: `1f94393f34b902bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141005`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (TRUE) UNION VALUES (FALSE); SELECT fpdecode(1e308, -2147483648, 65536);
```

---

## Crash 35: `ff8655969b6fca08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141015`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(FALSE) || CURRENT_TIMESTAMP) UNION VALUES (FALSE); SELECT fpdecode(1e308, -2147483648, 655
```

---

## Crash 36: `e3804ebbf3019eba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141021`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(CURRENT_TIME COLLATE NOCASE) || CURRENT_TIMESTAMP) UNION VALUES (FALSE); SELECT fpdecode(1
```

---

## Crash 37: `3e466921138a5fcc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141027`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(CURRENT_DATE << NULL COLLATE NOCASE) || CURRENT_TIMESTAMP) UNION VALUES (FALSE); SELECT fp
```

---

## Crash 38: `30da976c8d306a4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141033`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(CURRENT_DATE << -CURRENT_TIME COLLATE NOCASE) || NULL) UNION VALUES (FALSE); SELECT fpdeco
```

---

## Crash 39: `425e2fbfeda70b01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141050`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT concat_ws('', 
```

---

## Crash 40: `6bbaa0e6bc2bed5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141064`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); VALUES (max(CURRENT_DATE << NULL COLLATE NOCASE) || NULL) UNION VALUES (FALSE); SELECT fpdecode(1e308,
```

---

## Crash 41: `cee01fd314181c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150469`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE NULL LIMIT CURRENT_TIMESTAMP, FALSE; SELECT fpdecode(1e308, -21
```

---

## Crash 42: `5ebc2140dae38174` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150612`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') WHERE NULL LIMIT TRUE; SELECT fpdecode(1e308, -2147483648, 65536);
```

---

## Crash 43: `3f2fb8db6a3bdd43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152845`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY) STRICT; INSERT INTO p (rowid) VALUES (NULL); WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT string_agg(CAS
```

---
