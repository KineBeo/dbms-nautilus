# Crash Triage Report

**Total crashes:** 126  
**Unique crash sites:** 126  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 126 | 126 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `028e0eb85a702d61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000131`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); CREATE TABLE t1 AS WITH t2 AS MATERIALIZED (WITH t2 AS (VALUES (CURRENT_DATE ISNULL) UNION ALL VALUES (CURRENT_TIMESTAMP <> CURRENT_TIME) 
```

---

## Crash 2: `8ea24aace176b23a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000523`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_, c3, c3, c3, c2);
```

---

## Crash 3: `be1816113fc3277a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000739`

```sql
ATTACH DATABASE ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 4: `3763396650c8d8d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001299`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c2, _rowid_, c3, _rowid_, _rowid_, c3);
```

---

## Crash 5: `9ab944f55e5a7c9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005717`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, c2); ANALYZE t3;
```

---

## Crash 6: `eedf40904b47d50f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006022`

```sql
VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3); UPDATE OR FAIL t2 SET _rowid_ = NULL <= CURRENT_DATE NOT IN (CURRENT_TIME COLLATE NOCASE NOT NULL OR ~CAST(RAISE(IGNORE) AS VA
```

---

## Crash 7: `de2d2b8c65365c3c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009035`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 8: `9a1bf17371fe6ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009600`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2,
```

---

## Crash 9: `02520e1e55cfaff5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010166`

```sql
PRAGMA foreign_keys=ON; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, _rowid_);
```

---

## Crash 10: `0fe0e56f8bd9f5df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010210`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, _rowid_);
```

---

## Crash 11: `9e16f321cc73fbc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012490`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 12: `8c471091c427d9a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014650`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 13: `481a5864fc6b0269` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014709`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 14: `06867ea3a8c25d52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014715`

```sql
PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 15: `c5ee960d313a2dc2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018320`

```sql
DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); DROP TABLE IF EXISTS t2;
```

---

## Crash 16: `edfee291707aaa7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020650`

```sql
PRAGMA synchronous=FULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 17: `c158cc761a149640` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023121`

```sql
DROP VIEW IF EXISTS v1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 18: `064195803bc98ec1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023562`

```sql
CREATE TABLE t1 (c3 TEXT UNIQUE, UNIQUE (c3)); CREATE TRIGGER trg1 BEFORE DELETE ON t1 BEGIN DELETE FROM t1; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_);
```

---

## Crash 19: `f2ddc94d70f73d9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024869`

```sql
CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c3, c3);
```

---

## Crash 20: `01d979f44f9cbbd4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025632`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (c2 TEXT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); PRAGMA wal_checkpoint(FULL);
```

---

## Crash 21: `29ec334bb1b314b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025801`

```sql
VACUUM; BEGIN IMMEDIATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 22: `73bd38b28930ff79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026736`

```sql
DROP INDEX IF EXISTS idx1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ROLLBACK;
```

---

## Crash 23: `eaf117ffa4b3718d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030647`

```sql
PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2);
```

---

## Crash 24: `4022467c3d2e6f23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000031294`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 25: `722132c47a63380c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033665`

```sql
PRAGMA cache_size=6513; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); UPDATE OR IGNORE t2 SET rowid = ~+CASE changes() FILTER (WHERE CURRENT_TIME) OVER (PARTITION BY FALSE) WHEN CASE C
```

---

## Crash 26: `03bc08d428d5be40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034164`

```sql
VACUUM; BEGIN EXCLUSIVE; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 27: `98ca28773ce26ccc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034226`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 DATE NOT NULL REFERENCES t2 (c2) ON DELETE RESTRICT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); VACUUM;
```

---

## Crash 28: `952a81f79eb59442` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036377`

```sql
PRAGMA journal_mode=PERSIST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 29: `3fbf651286a1e50a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036654`

```sql
CREATE TEMP VIEW v1 AS SELECT * FROM t3 NOT INDEXED GROUP BY CURRENT_TIME, FALSE WINDOW w1 AS () ORDER BY CURRENT_DATE DESC NULLS LAST LIMIT RAISE(IGNORE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 30: `0a5604a8a0d6d5b4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036730`

```sql
CREATE TEMP VIEW v1 AS SELECT DISTINCT *; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1);
```

---

## Crash 31: `2c2d49f31913e73c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037811`

```sql
CREATE TABLE t1 (c3 TEXT GENERATED ALWAYS AS (RAISE(IGNORE)) VIRTUAL, c1 REAL NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_); SELECT DISTINCT CURRENT_DATE COLLATE RTR
```

---

## Crash 32: `d6f22080f7283755` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038220`

```sql
CREATE TEMP TABLE t1 (_rowid_ FLOAT NOT NULL); BEGIN EXCLUSIVE; ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_); ROLLBACK TO sp1;
```

---

## Crash 33: `5e8ac59548cc61a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038231`

```sql
CREATE TEMP TABLE t1 (_rowid_ FLOAT NOT NULL); BEGIN EXCLUSIVE; ANALYZE t1; ANALYZE t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 34: `023a76baadfc6f77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039215`

```sql
SAVEPOINT sp1; PRAGMA wal_checkpoint(PASSIVE); ROLLBACK; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 35: `22ac10cbba67d7a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039225`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DROP TABLE IF EXISTS t3; DROP TABLE t1; CREATE VIEW IF NOT EXISTS v1 AS WITH t2 (c3) AS NOT MATERIALIZED (SELECT
```

---

## Crash 36: `aa969f7a439ccd0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039242`

```sql
SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 37: `90e891714bced675` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040937`

```sql
VALUES (TRUE NOT IN (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c2);
```

---

## Crash 38: `10c61da67f97ac9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041529`

```sql
VALUES (CURRENT_TIME | NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 39: `bb9953f6295f1b5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041616`

```sql
PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 40: `710420d7c81ab8b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041625`

```sql
VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 41: `a73b6c04b1511fc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042472`

```sql
VALUES (~''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 42: `18acd59bfe3990a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043904`

```sql
CREATE TABLE t2 (c1 VARCHAR(255) DEFAULT (FALSE), c3 NUMERIC UNIQUE, UNIQUE (c1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 43: `66d66f8b912b71e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045763`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_DATE LIKE FALSE ESCAPE FALSE), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1);
```

---

## Crash 44: `05899923c8c777f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048027`

```sql
CREATE TABLE t2 (c2 DATE UNIQUE, _rowid_ FLOAT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_);
```

---

## Crash 45: `8b20308e87998d85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048061`

```sql
CREATE TABLE t2 (c2 DATE UNIQUE, _rowid_ FLOAT PRIMARY KEY) WITHOUT ROWID; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3); DELETE FROM t3 WHERE CAST(TRUE AS TEXT)
```

---

## Crash 46: `8970ead9182e2eca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050071`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_DATE), UNIQUE (rowid)); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 47: `53c824ee310555fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050899`

```sql
CREATE TABLE t1 (c3 TEXT UNIQUE, PRIMARY KEY (c3) ON CONFLICT FAIL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 48: `52be7338ff26d526` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055173`

```sql
WITH RECURSIVE t2 AS (VALUES (NULL)) SELECT * FROM t2 NOT INDEXED GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c2, c1); PRAGMA journal_mode=MEMOR
```

---

## Crash 49: `49e55d1e05296c13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057867`

```sql
BEGIN; END; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); END TRANSACTION; CREATE TEMP VIEW IF NOT EXIS
```

---

## Crash 50: `9e95a6eb6f3dd11f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058878`

```sql
BEGIN; END; CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT DISTINCT *; VACUUM; BEGIN; END; BEGIN EXCLUSIVE; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 51: `f5218bf48240be8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059522`

```sql
CREATE TABLE t2 (c3 BOOLEAN REFERENCES t2 (c2) DEFERRABLE INITIALLY DEFERRED, c2 BOOLEAN COLLATE NOCASE, UNIQUE (c2, c3), PRIMARY KEY (c2)); BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 52: `0243493f8ea76185` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065985`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 NUMERIC PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c3, c2, c2, c2); ATTACH ':memory:' AS db2; REINDEX t1; END; 
```

---

## Crash 53: `f9768b165e61df02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067942`

```sql
ATTACH ':memory:' AS db2; PRAGMA journal_mode=WAL; BEGIN; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 54: `fbb8cdcb0f7b5004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079073`

```sql
CREATE TABLE t2 AS SELECT -CURRENT_DATE AS z_8s_xovc_w; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 55: `16e158e712bf2fcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080246`

```sql
CREATE TABLE t2 AS SELECT TRUE >> CURRENT_TIME + FALSE AS r; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 56: `8f83b373d7729d43` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080449`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME + CURRENT_DATE LIKE FALSE ESCAPE FALSE AS r; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 57: `fd8fe268e9ed7f68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080514`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME + NULL AS r; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 58: `9e29be49dbbcd7f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080803`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || CURRENT_TIME == CASE WHEN FALSE THEN CURRENT_TIMESTAMP ELSE CURRENT_TIME END; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 59: `fa4014acd61b70f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081021`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || NULL GLOB CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT DISTINCT *; ATTACH DATABASE ':memory:' AS db2; SELECT ALL (T
```

---

## Crash 60: `8df51394e7619812` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081066`

```sql
CREATE TABLE t3 (c2 BLOB PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT DISTINCT *; ATTACH DATABASE ':memory:' AS db2; SELECT ALL (TRUE COLLA
```

---

## Crash 61: `94056072ff000c48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081076`

```sql
CREATE TABLE t2 AS SELECT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_); SELECT DISTINCT *; ATTACH DATABASE ':memory:' AS db2; SELECT ALL (TRUE COLLATE BINARY REGEXP CASE WHE
```

---

## Crash 62: `26f10f277f7815f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081153`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || random() GLOB CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 63: `fdb6f86ca6f593f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082060`

```sql
CREATE TABLE t2 AS SELECT typeof(FALSE) == NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 64: `4f48e8bd8622700d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082511`

```sql
CREATE TABLE t1 (c3 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 65: `3b04e30a065c0c35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082876`

```sql
CREATE TABLE t2 AS SELECT changes(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 66: `3ebbc7b021a6eced` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083542`

```sql
CREATE TABLE t2 AS SELECT FALSE == FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3);
```

---

## Crash 67: `476b7e3ab650e84e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083683`

```sql
CREATE TEMP TABLE t3 (c3 FLOAT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 68: `d28281d0ca77a50f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088755`

```sql
CREATE TABLE t2 AS SELECT 0.0 == FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 69: `d3dc75f0ee83124d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088896`

```sql
CREATE TABLE t2 AS SELECT typeof(FALSE) == CURRENT_DATE COLLATE RTRIM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 70: `647b03ae72a79f9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088949`

```sql
CREATE TABLE t2 AS SELECT total_changes() == CURRENT_DATE COLLATE RTRIM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 71: `8d66435834f56577` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090005`

```sql
CREATE TABLE t2 AS SELECT last_insert_rowid(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); ANALYZE t2;
```

---

## Crash 72: `76d7e26fff7b31e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091104`

```sql
CREATE TABLE t2 AS SELECT sum(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 73: `1701b5a844cb8c04` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092700`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || random() GLOB CURRENT_DATE NOT NULL == CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2, c1, c2, _rowid_); UPDATE t1 SET _rowid_
```

---

## Crash 74: `05a32ee2238e2222` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093334`

```sql
CREATE TABLE t2 AS SELECT CURRENT_TIME || NULL; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t1 AS MATERIALIZED (SELECT ALL t1.* LIMIT CURRENT_TIMESTAMP), t2 (
```

---

## Crash 75: `7eb09ce08e9b8d38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093390`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t1 AS MATERIALIZED (SELECT ALL t1.* LIM
```

---

## Crash 76: `75ce0cca4652d631` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094457`

```sql
CREATE TABLE t2 AS SELECT FALSE + FALSE AS r; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 77: `b4cf38c5fcdbcf68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094954`

```sql
CREATE TABLE t2 AS SELECT TRUE AS r; UPDATE t2 SET rowid = FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); COMMIT TRANSACTION;
```

---

## Crash 78: `47fee546f815d19e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095071`

```sql
CREATE TABLE t2 AS VALUES (CURRENT_TIME); ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); COMMIT TRANSACTION;
```

---

## Crash 79: `e86843188e3b2c02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102073`

```sql
VALUES (NULL) EXCEPT SELECT DISTINCT FALSE AS a; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_); CREATE VIEW v1 AS SELECT CURRENT_TIMESTAMP NOT IN (SELECT DISTINCT * LIMIT CURRENT_D
```

---

## Crash 80: `0e205bed2ff3bce4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000104011`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid, _rowid_, c1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 81: `7a48340cff647f5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107928`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 NUMERIC PRIMARY KEY ASC) WITHOUT ROWID; CREATE TABLE IF NOT EXISTS t2 (c2 NUMERIC PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 82: `ec04a68c2eea16e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109244`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ INT DEFAULT -0, c1 NUMERIC PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 83: `19179230e9df87a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109685`

```sql
CREATE TABLE IF NOT EXISTS t2 (c1 BOOLEAN PRIMARY KEY DESC, rowid TEXT NOT NULL DEFAULT X'4fAFEb', c3 BOOLEAN COLLATE NOCASE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 84: `e21d206188fd41da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115974`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 85: `e7f5b0ffede6e893` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000116777`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, _rowid_, c1, c3, c3); REINDEX t2; WITH RECURSIVE t2 (c2) AS NOT MATERIALIZED
```

---

## Crash 86: `a9c874465734aa3e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000118331`

```sql
BEGIN; END; ATTACH ':memory:' AS db2; DETACH DATABASE db2; ANALYZE; BEGIN; END; PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 87: `75d4dfffe410b004` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000119771`

```sql
PRAGMA cache_size=+1; CREATE TABLE t3 (_rowid_ INTEGER PRIMARY KEY DESC); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 88: `28c031312a2fd89c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123085`

```sql
WITH RECURSIVE t2 AS (VALUES (NULL)) SELECT TRUE FROM t2 NOT INDEXED GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 89: `0dfae55ebe92f535` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123740`

```sql
WITH RECURSIVE t2 AS (VALUES (CAST(CURRENT_DATE AS TEXT))) SELECT * FROM t2 NOT INDEXED GROUP BY CURRENT_TIME WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 90: `3ce9a250705881f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124541`

```sql
SELECT CURRENT_TIME AS z_8s_xovc_w ORDER BY FALSE ASC NULLS FIRST LIMIT FALSE, TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); CREATE TABLE t2 (c3 INTEGER);
```

---

## Crash 91: `060b5603ce9732ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133512`

```sql
CREATE TABLE t3 (c3 BOOLEAN NOT NULL DEFAULT CURRENT_TIME, rowid DATE NOT NULL DEFAULT FALSE, PRIMARY KEY (c3, rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 92: `c84b5834323eb559` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133705`

```sql
CREATE TABLE IF NOT EXISTS t2 (c3 VARCHAR(255) PRIMARY KEY DESC) WITHOUT ROWID; PRAGMA journal_mode=WAL; ANALYZE t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1); CREATE VIRTUAL TABLE IF N
```

---

## Crash 93: `989c23d216bc20e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134042`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid FLOAT PRIMARY KEY) WITHOUT ROWID; CREATE INDEX IF NOT EXISTS idx1 ON t1 (rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DROP TABLE IF EXISTS t1;
```

---

## Crash 94: `6074f0fcd2470f1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134562`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_TIMESTAMP GLOB RAISE(IGNORE)), UNIQUE (rowid)); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 95: `79c3da3d60ec7ded` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138106`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (RAISE(IGNORE) NOT BETWEEN CURRENT_TIME AND CURRENT_DATE || FALSE IS NOT FALSE), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2);
```

---

## Crash 96: `44cbfe6abdcc5bcb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138829`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (TRUE), UNIQUE (rowid)); DELETE FROM t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 97: `b6c4c5d6caa1da65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139644`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (_rowid_), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 98: `878d87c8fb7d44ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140210`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_TIMESTAMP), UNIQUE (rowid)); ALTER TABLE t1 ADD COLUMN _rowid_ INTEGER NOT NULL DEFAULT '5 - __'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowi
```

---

## Crash 99: `55114561b45d1eb0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140255`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_TIMESTAMP), UNIQUE (rowid)); PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 100: `aa3faddcded6e142` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140263`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (CURRENT_TIMESTAMP), UNIQUE (rowid)); ALTER TABLE t1 ADD COLUMN _rowid_ INTEGER NOT NULL DEFAULT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 101: `71c39380a68bab19` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147483`

```sql
VALUES (CURRENT_DATE NOT LIKE NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 102: `f932c2e41368e965` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147536`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 103: `58c6c838f106f792` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149294`

```sql
VALUES (CASE WHEN TRUE NOT IN (FALSE) THEN CURRENT_TIME WHEN FALSE THEN CURRENT_DATE ELSE CURRENT_TIME END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 104: `c038f94ac92e6e08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149500`

```sql
VALUES (CASE WHEN CURRENT_DATE THEN CURRENT_TIME WHEN FALSE THEN CURRENT_DATE ELSE NULL END); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); PRAGMA cache_size=98379;
```

---

## Crash 105: `bca818c816c8165d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149658`

```sql
VALUES (CASE WHEN -27744864523269777437.63861341293074196590740955027888639603058040382216477430987594656564421E89 THEN CURRENT_TIME WHEN FALSE THEN CURRENT_DATE ELSE TRUE END); CREATE VIRTUAL TABLE I
```

---

## Crash 106: `5c7c847734524445` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150195`

```sql
VALUES (TRUE NOT IN (FALSE * CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 107: `1b479bf4a1b489d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154737`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_);
```

---

## Crash 108: `702e9d008aebfe30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154776`

```sql
SAVEPOINT sp1; DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_);
```

---

## Crash 109: `de5e936618290dec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154782`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_);
```

---

## Crash 110: `73da0c8b5f6b1c11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154980`

```sql
SAVEPOINT sp1; ROLLBACK TO sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 111: `44e85549a3468bda` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000156714`

```sql
CREATE TEMP TABLE t1 (_rowid_ FLOAT NOT NULL); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 112: `251491cbc53d62c7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158783`

```sql
CREATE TABLE IF NOT EXISTS t2 (_rowid_ DATE REFERENCES t3 (c2) MATCH rowid, c1 INT PRIMARY KEY DESC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2);
```

---

## Crash 113: `ef5a16935e655316` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169473`

```sql
CREATE TABLE t2 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); INSERT INTO t2 DEFAULT VALUES; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); BEGIN IMMEDIATE;
```

---

## Crash 114: `8b18dad3c78fe0a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170825`

```sql
VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT FALSE ORDER BY FALSE NULLS FIRST LIMIT NOT 'bDC -q-5n w Y_yR6'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1); WITH RECURSIVE t3 (c1) AS 
```

---

## Crash 115: `8bf21915696f1dc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170897`

```sql
VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT FALSE ORDER BY FALSE NULLS FIRST LIMIT NOT CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1); WITH RECURSIVE t3 (c1) AS NOT MAT
```

---

## Crash 116: `5f231ad1edd19942` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000170903`

```sql
VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT FALSE ORDER BY FALSE NULLS FIRST LIMIT NOT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, c1); WITH RECURSIVE t3 (c1) AS NOT MATERIALIZE
```

---

## Crash 117: `456699912411b868` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000171414`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT FALSE ORDER BY FALSE ASC NULLS FIRST LIMIT -CURRENT_DATE, -CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DELETE FROM t1 WHERE
```

---

## Crash 118: `d94caab86f76d3bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172051`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT FALSE ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE
```

---

## Crash 119: `c4e69072ffe6a285` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172070`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT FALSE ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || 
```

---

## Crash 120: `f60de1b9bc1b6e02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172168`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT FALSE ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE
```

---

## Crash 121: `0d553b6c0d656009` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000172175`

```sql
VALUES (CURRENT_TIMESTAMP) INTERSECT SELECT FALSE ORDER BY CURRENT_TIMESTAMP DESC LIMIT TRUE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE || FALSE
```

---

## Crash 122: `245b24b0a4e90029` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173758`

```sql
VALUES (TRUE || FALSE * CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3, _rowid_, _rowid_); CREATE INDEX idx1 ON t3 (c1, _rowid_); ROLLBACK TO sp1;
```

---

## Crash 123: `1acbdf096d1b6f9e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176814`

```sql
CREATE TABLE t2 (c2 BOOLEAN COLLATE NOCASE, CHECK (CURRENT_TIMESTAMP MATCH RAISE(IGNORE)), PRIMARY KEY (c2)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c1, _rowid_, c1, c1, _ro
```

---

## Crash 124: `299cb6df4297c027` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181603`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (FALSE >= NULL), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); DROP TABLE IF EXISTS t1;
```

---

## Crash 125: `b79c29f515c4745c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183754`

```sql
CREATE TABLE t1 (rowid REAL, CHECK (TRUE IS NULL), UNIQUE (rowid)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); DROP TABLE t3; VACUUM; CREATE TABLE t3 (_rowid_ BLOB PRIMARY KEY DESC) WIT
```

---

## Crash 126: `19b04e15cf700813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184771`

```sql
CREATE TEMP TABLE IF NOT EXISTS t2 (_rowid_ FLOAT DEFAULT '- ---u_-n_', rowid BOOLEAN); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1);
```

---
