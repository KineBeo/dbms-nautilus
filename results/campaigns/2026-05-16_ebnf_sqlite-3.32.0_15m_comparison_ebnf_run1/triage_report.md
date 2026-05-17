# Crash Triage Report

**Total crashes:** 17  
**Unique crash sites:** 17  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 17 | 17 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `2632ad3a906b881c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000358`

```sql
BEGIN TRANSACTION; DROP TABLE IF EXISTS t3; WITH RECURSIVE t1 (c3, c2, _rowid_) AS NOT MATERIALIZED (SELECT ALL * ORDER BY -CURRENT_TIME DESC NULLS FIRST LIMIT RAISE(IGNORE)), t1 AS (SELECT ALL * EXCE
```

---

## Crash 2: `ba2224af3b9d3ee9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000777`

```sql
INSERT INTO t2 (rowid, _rowid_) VALUES (json_array(NOT EXISTS (SELECT DISTINCT ~-CURRENT_TIMESTAMP NOT IN (SELECT t1.*) & CASE WHEN FALSE = CURRENT_DATE / +NULL / count(DISTINCT TRUE) - CASE FALSE COL
```

---

## Crash 3: `ad0754187ca87677` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000000928`

```sql
DELETE FROM t2; UPDATE t3 SET _rowid_ = 'Nt_ --_-GJg3R7Pu_' IS NULL | total_changes() -> c3, rowid = total_changes() OVER (PARTITION BY NULL <> CURRENT_TIME ISNULL IS NOT DISTINCT FROM CASE TRUE WHEN 
```

---

## Crash 4: `83045152cb72a078` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000004419`

```sql
VACUUM; CREATE TABLE t2 (c2 TEXT GENERATED ALWAYS AS (CURRENT_TIME >= CURRENT_TIME >> CASE WHEN TRUE THEN NULL END & CURRENT_TIMESTAMP + FALSE < CASE WHEN TRUE THEN FALSE WHEN CURRENT_TIME THEN TRUE E
```

---

## Crash 5: `b029107406a99254` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000004938`

```sql
VACUUM INTO ':memory:'; ANALYZE t1;
```

---

## Crash 6: `9d512fad703104ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000007984`

```sql
CREATE INDEX idx1 ON t2 (_rowid_) WHERE -RAISE(IGNORE) <= CURRENT_TIME & CURRENT_TIME IN (WITH RECURSIVE t2 AS (WITH RECURSIVE t1 AS MATERIALIZED (SELECT DISTINCT * LIMIT CURRENT_TIMESTAMP) VALUES (TR
```

---

## Crash 7: `0037ea98097aa861` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000010531`

```sql
DROP TABLE IF EXISTS t3; ATTACH ':memory:' AS db2; PRAGMA integrity_check; ALTER TABLE t1 RENAME COLUMN rowid TO c2;
```

---

## Crash 8: `2d4fe57a15c9c7b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000027394`

```sql
BEGIN IMMEDIATE TRANSACTION; DROP TABLE t2;
```

---

## Crash 9: `7e2fa5bcec19aed1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000028664`

```sql
ALTER TABLE t2 RENAME COLUMN c1 TO c1; INSERT INTO t3 WITH t3 AS (SELECT DISTINCT * LIMIT CURRENT_TIME OFFSET NOT CURRENT_TIME) SELECT * FROM t3 INDEXED BY rowid ORDER BY (CURRENT_TIME, CURRENT_TIMEST
```

---

## Crash 10: `7f746ead72113ac7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000028818`

```sql
INSERT OR FAIL INTO t3 VALUES (NOT CASE WHEN CURRENT_DATE THEN NOT EXISTS (SELECT DISTINCT CURRENT_DATE ORDER BY FALSE NULLS LAST, changes() ASC NULLS LAST) END ISNULL LIKE last_insert_rowid() FILTER 
```

---

## Crash 11: `d32bfc2511f7c91b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000076720`

```sql
BEGIN IMMEDIATE TRANSACTION; BEGIN IMMEDIATE;
```

---

## Crash 12: `144c963dbb9ac079` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000076864`

```sql
CREATE TRIGGER trg1 AFTER INSERT ON t1 WHEN CASE WHEN RAISE(IGNORE) IS NOT FALSE << FALSE <= +CURRENT_TIMESTAMP LIKE CURRENT_DATE THEN ~FALSE ISNULL OR (RAISE(IGNORE)) WHEN CASE WHEN FALSE THEN RAISE(
```

---

## Crash 13: `8b67dceca2d6933d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000077288`

```sql
DROP TABLE IF EXISTS t3; ATTACH ':memory:' AS db2; CREATE VIEW IF NOT EXISTS v1 AS SELECT ALL t1.* FROM t2 UNION ALL SELECT DISTINCT * ORDER BY NULL ASC NULLS FIRST LIMIT NOT CURRENT_TIMESTAMP, CURREN
```

---

## Crash 14: `1d6b4f98def424f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000087424`

```sql
CREATE TABLE t1 (rowid INT REFERENCES t3 (c3) DEFERRABLE INITIALLY DEFERRED, FOREIGN KEY (rowid) REFERENCES t2 (c1) ON DELETE SET NULL); ATTACH ':memory:' AS db2;
```

---

## Crash 15: `0d86e93d22b084a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000150776`

```sql
ATTACH DATABASE ':memory:' AS db2; BEGIN EXCLUSIVE; CREATE INDEX IF NOT EXISTS idx1 ON t3 (c2);
```

---

## Crash 16: `865bf99a86a45f31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000174961`

```sql
CREATE TABLE t3 (c1 INT); END;
```

---

## Crash 17: `dc534a14d1e127c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** 0
- **Sample file:** `5_000284186`

```sql
PRAGMA optimize; ALTER TABLE t3 RENAME COLUMN _rowid_ TO _rowid_;
```

---
