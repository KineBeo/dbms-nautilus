# Crash Triage Report

**Total crashes:** 100  
**Unique crash sites:** 100  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 100 | 100 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `0ecd71dc40b41524` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040878`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (FALSE IS NOT TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT parseuri('_133 I0 
```

---

## Crash 2: `8c6689fb73155f75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041298`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT parseuri('_133 I0  4- t_U__', 21474
```

---

## Crash 3: `efdefce5e6c554d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043428`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL, a INTEGER, b TEXT) WITHOUT ROWID; EXPLAIN QUERY PLAN VALUES (FALSE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 4: `8fa80af773ca271e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047465`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER) STRICT; INSERT OR FAIL INTO p VALUES (NULL > NULL -> NOT NULL IN (VALUES (TRUE))); PRAGMA integrity_check; SELECT fpdecode(-1e308, 2147483648, 32768);
```

---

## Crash 5: `a6386c996a362b2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053422`

```sql
SELECT printf('%.*f', -9223372036854775808, 9e999); SELECT fpdecode(-1e308, 2147483648, 65536);
```

---

## Crash 6: `273cc0ee1965d979` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057372`

```sql
CREATE TABLE IF NOT EXISTS p(rowid FLOAT UNIQUE, c1 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM json_tree('[]') CROSS JOIN jsonb_each('{}') ON RAISE(IGNORE) WHERE R
```

---

## Crash 7: `880db40b983551ba` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062360`

```sql
SELECT fpdecode(-1.0, 2147483648, -1);
```

---

## Crash 8: `9bd3630d617b82a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063720`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB NOT NULL); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p AS (SELECT *) VALUES (NULL)); SELECT fpdecode(1.0, -214
```

---

## Crash 9: `db0a03199e4b3c82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063894`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL, a INTEGER, b TEXT) WITHOUT ROWID; SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p AS (SELECT *) VALUES (NULL)); SELECT fpdecode(1.
```

---

## Crash 10: `20883005d3b6c525` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063900`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL, a INTEGER, b TEXT) WITHOUT ROWID; WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 50) SELECT string_a
```

---

## Crash 11: `09bae4b2129cd7c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068252`

```sql
SELECT substr('', 4294967295, 2147483647); SELECT fpdecode(1e308, -2147483648, 2147483647);
```

---

## Crash 12: `bc93a2fac7f9a37b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076255`

```sql
SELECT unistr(' 0-_n9_T-84_ _L -G-'); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 13: `04a789b60d30c7bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077042`

```sql
SELECT max(FALSE, CURRENT_TIME, CURRENT_TIME, CURRENT_TIMESTAMP, FALSE, NULL, FALSE COLLATE NOCASE, CURRENT_TIMESTAMP); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 14: `64f59a5160ba850b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077170`

```sql
SELECT max(FALSE, CURRENT_TIME, CURRENT_TIME, CURRENT_TIMESTAMP, FALSE, NULL, NULL, CURRENT_TIMESTAMP); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 15: `aa3a745280bc681c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079249`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHER
```

---

## Crash 16: `00aebc225ef0fc3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083771`

```sql
SELECT printf('%.*d', 2147483647, 1.0); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 17: `e3d852ab0bfcd6b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109811`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT FALSE, CURRENT_TIME, TRUE
```

---

## Crash 18: `66929aa344c03aca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109984`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); SELECT unistr(TRUE) FROM p; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 19: `713b0c39b2b15311` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109991`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p AS (SELECT *) VALUES (CURRENT_TIMESTAMP)); SELECT fpdec
```

---

## Crash 20: `8041251eb56336d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109997`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); SELECT * FROM p WHERE EXISTS (WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT FALSE, CURRENT_TIME, TRUE
```

---

## Crash 21: `20b948831e05ac12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127767`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA integrity_check; SELECT fpdecode(1e308, -2147483648, 1);
```

---

## Crash 22: `b2921dffaae8f6e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135053`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (-CURRENT_DATE); ANALYZE p; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 23: `05a424f2d8d6e8da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141670`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (FALSE OR TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; INSERT INTO p DEFAULT VALUES; SELECT parseuri('_133 I0  4- 
```

---

## Crash 24: `da6442f7430548c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142584`

```sql
SELECT fpdecode(1.0, -2147483648, 0);
```

---

## Crash 25: `b884585f6e9584f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142625`

```sql
SELECT fpdecode(1.0, -2147483648, 9223372036854775807);
```

---

## Crash 26: `0a885a178ab7595a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148631`

```sql
SELECT concat(CURRENT_DATE, FALSE, TRUE, CURRENT_TIMESTAMP, NULL, FALSE, CURRENT_DATE, ~CURRENT_TIME OR NULL); SELECT fpdecode(1e308, 2147483648, 4294967296);
```

---

## Crash 27: `c78d37d6e15b9d41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158407`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM json_tree('{}') ORDER BY NULL || NULL; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 28: `5f4d4e58e429c114` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161244`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT * FROM jsonb_tree('{"a":1}') GROUP BY FALSE ORDER BY CURRENT_TIME DESC NULLS FIRST; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 29: `6a706ca0b84d03b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184817`

```sql
SELECT round(-1.0, -1); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 30: `f4f9381e6e69a925` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184915`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 31: `a1447186fe99f3c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187508`

```sql
SELECT concat(FALSE IN (WITH t2 (c3) AS (SELECT *) VALUES (FALSE)), FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, row_number() OVER (), CURRENT_DATE, TRUE, TRUE); SELECT fpdecode(1e308, 2147483648, 214
```

---

## Crash 32: `4c38600cf1ecbd33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206308`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (NOT EXISTS (SELECT EXISTS (VALUES (RAISE(IGNORE)) INTERSECT SELECT CURRENT_TIMESTAMP IS NOT NULL) AS s_e86c44_9__7_1cj4dcn_j_99 FROM jsonb_each('{}'))); SELECT 
```

---

## Crash 33: `be808a082ab8b393` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000206462`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (NOT EXISTS (VALUES (CURRENT_DATE))); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 34: `cfff57f719f77e3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000232313`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIMESTAMP FROM jsonb_tree('{"a":1}') GROUP BY NULL ORDER BY CURRENT_DATE ASC NULLS FIRST; SELECT fpdecode(1.
```

---

## Crash 35: `f817c6350f803fa7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248873`

```sql
SELECT parseuri('', -1); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 36: `17392064a4e6b04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251295`

```sql
CREATE TABLE IF NOT EXISTS p(e INTEGER PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (NULL AND 185268.942514E-402); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 37: `e5f0b8eb564d3bc8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251398`

```sql
CREATE TABLE IF NOT EXISTS p(e INTEGER PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (NULL); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 38: `9d1eb67d26767ff1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251404`

```sql
CREATE TABLE IF NOT EXISTS p(e INTEGER PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (NULL AND NULL); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 39: `ce801e1ed8c0b661` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260690`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER) STRICT; INSERT OR FAIL INTO p VALUES (-jsonb_set('[]', '$', FALSE)); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 40: `961c47fc0856a111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000299387`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (group_concat(FALSE, '') FILTER (WHERE NULL) OVER ()); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 41: `9c3b629feddfd472` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000308193`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(NULL) OVER () FROM p EXCEPT SELECT substring(NULL, NULL) FR
```

---

## Crash 42: `7d79de4ecdded030` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000318024`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(d IS NULL << CURRENT_DATE) FROM p; SELECT fpdecode(1e308, 2
```

---

## Crash 43: `60940c27a042adae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000318083`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(FALSE) FROM p; SELECT fpdecode(1e308, 2147483648, 429496729
```

---

## Crash 44: `d3fc5ee3095c8eae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000318089`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(CURRENT_DATE << CURRENT_DATE) FROM p; SELECT fpdecode(1e308
```

---

## Crash 45: `38162e8ae0f338bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000318095`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(TRUE IS NULL << CURRENT_DATE) FROM p; SELECT fpdecode(1e308
```

---

## Crash 46: `9ba28df84900aca4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000318238`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC); INSERT INTO p DEFAULT VALUES; SELECT total(FALSE IS NOT CAST(CURRENT_TIMESTAMP << CURRENT_DATE AS REAL
```

---

## Crash 47: `43189ddf88823161` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000322713`

```sql
CREATE TABLE IF NOT EXISTS p(e VARCHAR(255), c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT total(rowid) FROM p; SELECT fpdecode(1.0,
```

---

## Crash 48: `a2c6eb12a2a8cb04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000322835`

```sql
CREATE TABLE IF NOT EXISTS p(e VARCHAR(255), c2 TEXT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; SELECT total(CURRENT_DATE) FROM p; SELECT fpdeco
```

---

## Crash 49: `a980a270d8e39411` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000329714`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; SELECT total(NULL) OVER () FROM p EXCEPT SELECT count(DISTINCT TRUE) FROM p; SE
```

---

## Crash 50: `3cee063629b857ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000336761`

```sql
SELECT char(FALSE, TRUE, CURRENT_TIMESTAMP, NULL, -TRUE, NULL, FALSE, FALSE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 51: `4b245d2e8a988b39` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000359482`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (parseuri('0_63p m 1Z_13n_r', -2147483649)) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2
```

---

## Crash 52: `fb17b2dd92d0b720` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000359594`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (FALSE) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 53: `8cd15120a9bd4f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000359600`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); INSERT INTO p VALUES (changes()) ON CONFLICT DO NOTHING; PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 54: `9d6e7d77d69b2837` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000383362`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT fpdecode(-1e308, -214
```

---

## Crash 55: `66bea512a17a8c3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000383423`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY) STRICT; INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB,
```

---

## Crash 56: `9e9aea1f05830bbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000388624`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; INSERT OR FAIL INTO p VALUES (NULL IN (SELECT * FROM p)); WITH RECURSIVE 
```

---

## Crash 57: `f8509ab66c5e06c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000388774`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); WITH RECURSIVE cnt(x) A
```

---

## Crash 58: `aee81b1f93149c73` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000388781`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; INSERT OR FAIL INTO p VALUES (NULL IN (VALUES (CURRENT_DATE))); WITH RECU
```

---

## Crash 59: `aaaca0c7141880b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000400270`

```sql
SELECT concat(CURRENT_DATE, FALSE, TRUE, CURRENT_TIMESTAMP, NULL, FALSE, CURRENT_DATE, json_object('Q 23--F _-', json_object('Q 23--F _-', count()))); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 60: `967097b2c666d4d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000400433`

```sql
SELECT concat(CURRENT_DATE, FALSE, TRUE, CURRENT_TIMESTAMP, NULL, FALSE, CURRENT_DATE, json_object('Q 23--F _-', NULL)); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 61: `ac8fe51ec4da5911` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000401056`

```sql
SELECT concat(CURRENT_DATE, FALSE, TRUE, CURRENT_TIMESTAMP, NULL, FALSE, CURRENT_DATE, max(NULL)); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 62: `0f60645b8692a47d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000407536`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM jsonb_tree('[{"a":1},{"b":2}]') ORDER BY random() || random() || random() << FALSE; SELECT fpdecode(1
```

---

## Crash 63: `96381df5049e73d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000417024`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT jsonb_remove('{"a":1}', '$') AS r30_ FROM json_tree('{"a":{"b":1}}'); SELECT fpdecode(1.0, -2147483648, 2147483648);
```

---

## Crash 64: `2c34816817b2dad4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000417117`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}'); SELECT fpdecode(1.0, -2147483648, 2147483648);
```

---

## Crash 65: `5c3d73df5ea93de7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000417124`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT CURRENT_TIMESTAMP AS r30_ FROM json_tree('{"a":{"b":1}}'); SELECT fpdecode(1.0, -2147483648, 2147483648);
```

---

## Crash 66: `0c652915f4be4db5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000417130`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS (SELECT *) SELECT DISTINCT count(*) AS r30_ FROM json_tree('{"a":{"b":1}}'); SELECT fpdecode(1.0, -2147483648, 2147483648);
```

---

## Crash 67: `8cb339bebf2ee24b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000427315`

```sql
SELECT unhex('d0_47_'); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 68: `77c14f6311418f1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000429103`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS NOT MATERIALIZED (VALUES (CURRENT_DATE) INTERSECT SELECT CURRENT_TIME AS r4jf1g__6o3ny1___p5v_1_2_7_004f___62eq7_m0ipx__1g_4_e_1_0_xl___04___8s9__na___m FROM 
```

---

## Crash 69: `0b5b74c6d0e5acf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000431458`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS MATERIALIZED (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM json_each(CURRENT_TIMESTAMP - CURRENT_TIMESTAMP - CURRENT_DATE, '$'); SELECT fpdecode(-1
```

---

## Crash 70: `04859b30cc653853` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434676`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE 
```

---

## Crash 71: `10f41e0f685a242d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434875`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIME ASC; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 72: `fde2b226b61c3762` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434881`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY FALSE ASC NULLS LAST; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 73: `ca9f249e36299fd9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434888`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_DATE << TRUE; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 74: `66a5cde82be3660c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434896`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY TRUE << TRUE << TRUE << TRUE << TRUE; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 75: `ef11e2e6423409ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000434910`

```sql
CREATE TABLE IF NOT EXISTS p AS SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_TIMESTAMP << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << 
```

---

## Crash 76: `edf721266323c6f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000463474`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS MATERIALIZED (SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY CURRENT_DATE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRUE << TRU
```

---

## Crash 77: `3a4a55310c6f938e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000463610`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS MATERIALIZED (SELECT ALL * FROM jsonb_each('[{"a":1},{"b":2}]') ORDER BY FALSE DESC NULLS FIRST) SELECT DISTINCT * FROM p; SELECT fpdecode(1.0, -214
```

---

## Crash 78: `2ef711a3e6ab5da5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000468235`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS MATERIALIZED (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM json_each(jsonb_patch('[1,2,3]', '[1,2,3]'), '$[#-1]'); SELECT fpdecode(1.0, -2147483648
```

---

## Crash 79: `0e941625f0cdbfef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000468362`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH RECURSIVE p AS MATERIALIZED (VALUES (CURRENT_TIME)) SELECT DISTINCT * FROM json_each(TRUE, '$[#-1]'); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 80: `c25a74ea1f1205d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000473654`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS NOT MATERIALIZED (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') NATURAL JOIN (json_tree('{}') NATURAL LEFT JOIN jsonb_tree('[]')) L
```

---

## Crash 81: `74b15630163a9f3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000473728`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS NOT MATERIALIZED (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') NATURAL JOIN jsonb_each('{"a":{"b":1}}') LEFT OUTER JOIN (VALUES (C
```

---

## Crash 82: `3f863b6b155406f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000473734`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS NOT MATERIALIZED (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') NATURAL JOIN (json_tree('[{"a":1},{"b":2}]')) LEFT OUTER JOIN (VALU
```

---

## Crash 83: `4d270bf881aaf111` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000473740`

```sql
CREATE TABLE IF NOT EXISTS p AS WITH p AS NOT MATERIALIZED (VALUES (CURRENT_DATE)) SELECT DISTINCT * FROM json_each('{"a":{"b":1}}') NATURAL JOIN (json_tree('{}') NATURAL LEFT JOIN jsonb_tree('[]')) L
```

---

## Crash 84: `4391819db4779dac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000480622`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (percent_rank() OVER () % CURRENT_TIME); SELECT fpdecode(1e308, 2147483648, 4294967295);
```

---

## Crash 85: `24bd495daf7e70a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000480726`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (TRUE % CURRENT_TIME); SELECT fpdecode(1e308, 2147483648, 4294967295);
```

---

## Crash 86: `a98c99d2c9d1901d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000488103`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM json_tree('{"a":1}') LEFT OUTER JOIN json_each(CAST(TRUE AS BLOB), '$[#-1]') ORDER BY FALSE DESC NULL
```

---

## Crash 87: `3a358d80c564fad5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000488216`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM json_tree('[]') ORDER BY FALSE DESC NULLS LAST; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 88: `7a5e1e8ae33e34b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000488224`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM json_tree('{"a":1}') LEFT OUTER JOIN json_each(FALSE, '$[#-1]') ORDER BY FALSE DESC NULLS LAST; SELEC
```

---

## Crash 89: `e0e150af2aee1214` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000488234`

```sql
SELECT hex(zeroblob(65536)); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 90: `cd3491684cbac14d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000488244`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 100) SELECT ALL * FROM json_tree('{"a":1}') LEFT OUTER JOIN json_each('[{"a":1},{"b":2}]') ORDER BY FALSE DESC NULLS LAST; S
```

---

## Crash 91: `f60abf77b313ff5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000499119`

```sql
SELECT concat(CURRENT_DATE, FALSE, TRUE, CURRENT_TIMESTAMP, NULL, FALSE, CURRENT_DATE, CURRENT_TIME GLOB FALSE); SELECT fpdecode(1e308, 2147483648, 4294967296);
```

---

## Crash 92: `d901a2f9d890a238` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000523052`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER) STRICT; INSERT OR FAIL INTO p VALUES (TRUE -> X'0a45'); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 93: `52396fefbfdd22f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000523216`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER) STRICT; INSERT OR FAIL INTO p VALUES (TRUE -> TRUE); PRAGMA integrity_check; SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 94: `181816737e90bc62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000542822`

```sql
WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < 50) SELECT DISTINCT * FROM jsonb_each('[]') LIMIT TRUE OFFSET CURRENT_DATE IS NULL; SELECT fpdecode(-1e308, -2147483648, 1);
```

---

## Crash 95: `f026c01600afe9c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000545412`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (count() OVER () NOT LIKE count() OVER ()) INTERSECT VALUES (TRUE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 96: `23b71b06e764c2c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000545551`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (NULL) INTERSECT VALUES (TRUE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 97: `792d8846a5ed1a94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000545558`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (NULL NOT LIKE count() OVER ()) INTERSECT VALUES (TRUE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 98: `70196afc879db403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000545564`

```sql
CREATE TABLE IF NOT EXISTS p AS VALUES (count() OVER () NOT LIKE NULL) INTERSECT VALUES (TRUE); SELECT fpdecode(1.0, -2147483648, -2147483648);
```

---

## Crash 99: `5cf63761f9f29de8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000547542`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL, a INTEGER, b TEXT) WITHOUT ROWID; SELECT * FROM p WHERE EXISTS (SELECT * FROM p ORDER BY RAISE(IGNORE) ASC); SELECT fpdecode(1e30
```

---

## Crash 100: `a70d62aa3ddb4b15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000548929`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB PRIMARY KEY, c3 ANY); SELECT fpdecode(-1.0, 2147483648, 32768); EXPLAIN DELETE FROM q WHERE FALSE RETURN
```

---
