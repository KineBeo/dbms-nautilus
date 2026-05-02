# Crash Triage Report

**Total crashes:** 195  
**Unique crash sites:** 195  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 195 | 195 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `519760ca00e87eb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000147`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; SELECT CURRENT_DATE FROM p JOIN p a ON TRUE; SELECT printf('%.*s', 2147483648, -1.0); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 2: `7017f1293da0a4cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000585`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, a, c1, c1, c2); INSERT OR FAIL INTO s VALUES (EXISTS (SELECT * INTERSECT VALUES (CURRENT_TIME)), CASE WHEN FALSE COLLATE NOCASE THEN CURRE
```

---

## Crash 3: `72bf11a5c3e16f4b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001360`

```sql
SELECT substr('ERN-_56V', -9223372036854775808, 4294967296); SELECT substr('_N1_ ', 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t3 (_rowid_, c2, c3, c2) VALUES (CASE NOT 
```

---

## Crash 4: `aada947e6651ce75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001439`

```sql
SELECT printf('%.*e', 1, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR IGNORE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN VALUES (CURRENT_TIME IS NULL COLLATE RTRIM, RAISE(IG
```

---

## Crash 5: `02a24c3b740206a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001501`

```sql
SELECT substr('i- -_8_ _-2_Kd-9T', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT (CURRENT_TIME) FROM t2 NATURAL JOIN r WHERE CASE WHEN FALSE THEN TRUE END LIKE RAISE(IG
```

---

## Crash 6: `17a18147e01b4f1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002795`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO t3 VALUES (NULL); SELECT p.* FROM p WHERE EXISTS (VALUES (+RAISE(IGNORE)));
```

---

## Crash 7: `f592f9cc2244640f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002813`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH t2 AS (VALUES (RAISE(IGNORE))), t3 AS (VALUES (CURRENT_TIMESTAMP)) INSERT INTO p VALUES (CURRENT_TIME);
```

---

## Crash 8: `92562db22a433180` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002826`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSE
```

---

## Crash 9: `b3a60ce32744381c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002973`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 INTEGER NOT NULL); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO s VALUES (NOT EXIST
```

---

## Crash 10: `caa54c0eaf2211d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003465`

```sql
SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN WITH r AS (SELECT ALL p.* FROM t2 INDEXED 
```

---

## Crash 11: `0fb1aba7faef6da4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006247`

```sql
SELECT printf('%u', -2147483649, '--RH9Z'); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT FALSE LIKE CURRENT_TIME IN (SELECT FALSE) IS NULL ESCAPE
```

---

## Crash 12: `4d72109fb6ad0990` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c3 NUMERIC GENERATED ALWAYS AS (NULL) STORED, c2 NUMERIC DEFAULT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 13: `228078a5f45998ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006478`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC GENERATED ALWAYS AS (NULL) STORED, c2 NUMERIC DEFAULT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); 
```

---

## Crash 14: `6dbe86fd40377ccd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006501`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (c3) VALUES (CURRENT_DATE) ON CONFLIC
```

---

## Crash 15: `8243c9b480302fbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006507`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c2 NUMERIC DEFAULT NULL); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (c3) VALUES (CURRENT_DAT
```

---

## Crash 16: `c023c5879e2d9de2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006514`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c2 TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (c3) VALUES (CURRENT_DATE) 
```

---

## Crash 17: `781a53f2833ba49f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006962`

```sql
SELECT round(1e308, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE q (rowid) AS (WITH p AS MATERIALIZED (SELECT p.*), r AS MATERIALIZED (VALUES (FALSE, CURRENT_D
```

---

## Crash 18: `b23bff8d45a149e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007074`

```sql
SELECT substr('', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR ROLLBACK INTO p VALUES ((CURRENT_TIME LIKE RAISE(IGNORE) COLLATE RTRIM IN (FALSE) IN (FALSE < ~NULL) 
```

---

## Crash 19: `68019345c52a3d34` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008195`

```sql
SELECT round(1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VALUES (CURRENT_TIME) INTERSECT SELECT * UNION ALL SELECT DISTINCT CURRENT_TIME ISNULL AS x92o9i9_46__ FROM t1 
```

---

## Crash 20: `f21bd557bad211c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008231`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b, _rowid_, b, c2, c2, c1, b, c2); INSERT INTO p VALUES (NULL NOTNULL << CURRENT_TIMESTAMP, trim(FALSE = -NOT CURRENT_DATE) FILTER (WHERE +RAISE
```

---

## Crash 21: `b0c938df6b319d80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008484`

```sql
SELECT printf('%.*f', 1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t2 (c1) VALUES (NULL COLLATE NOCASE COLLATE BINARY >> CURRENT_TIMESTAMP / CURRENT_TIMESTAMP COLLATE RTRI
```

---

## Crash 22: `55f90e0398ef463d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008512`

```sql
SELECT printf('%.*f', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT * FROM t2 NATURAL JOIN s WHERE RAISE(IGNORE) COLLATE
```

---

## Crash 23: `d4d9165436a848a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011956`

```sql
SELECT substr('', -1, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO r VALUES (CURRENT_DATE REGEXP CURRENT_TIME BETWEEN FALSE ->> +RAISE(IGNORE) << NULL | 
```

---

## Crash 24: `afa55372ac2c4a6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013141`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); REPLACE INTO q VALUES (NULL GLOB TRUE); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE I
```

---

## Crash 25: `9910969d293a0d56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014559`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT * FROM q WHERE EXISTS (SELE
```

---

## Crash 26: `a8291ae7f9cbf6fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014650`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT
```

---

## Crash 27: `b9d4f17b84efce80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014717`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; 
```

---

## Crash 28: `6f274167eb29853c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014779`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 29: `8b362eb4e85288f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014789`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 30: `17afb2b00d650927` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014821`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b DATE PRIMARY KEY); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 31: `7e2b777500fdc8f4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014876`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME IS
```

---

## Crash 32: `2016de5ed8846614` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015051`

```sql
SELECT round(1e-308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT (CURRENT_TIME) * CASE CURRENT_DATE WHEN (CURRENT_TIMESTAMP) THEN +FALSE COLLATE BINARY END IS DISTINCT
```

---

## Crash 33: `cc857c8f97319b5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016796`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME > NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; 
```

---

## Crash 34: `4c02f65634ea4f6a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017173`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME ORDER BY CURRENT_TIME ASC N
```

---

## Crash 35: `e22add6fd9c4d45f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017487`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME > CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VAL
```

---

## Crash 36: `ff65e5d339c1864b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017670`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT q.* FROM q NATURAL JOIN q WHERE NOT 0.
```

---

## Crash 37: `d561af7bf7af7a0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) PRIMARY KEY); SELECT * FROM p JOIN p z_y_4_4ek ON TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; S
```

---

## Crash 38: `3519a595b0acd9ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019556`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON NULL - NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(ze
```

---

## Crash 39: `b1e348852ba69cac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019836`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> NOT CURRENT_TIMESTAMP - NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES
```

---

## Crash 40: `1bbf50292f0c25af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020103`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob
```

---

## Crash 41: `ac3d380ca3abf8c1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020109`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON TRUE - NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(ze
```

---

## Crash 42: `191b483fff62c08c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020225`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> NOT CURRENT_TIMESTAMP - NULL ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); SELECT CURRENT_TI
```

---

## Crash 43: `97f1b148816f9242` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020432`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON NOT FALSE ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_ch
```

---

## Crash 44: `29486ca46241b35d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020565`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 45: `48790e9ad23c1d95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020571`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_DATE ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity
```

---

## Crash 46: `9372a2ef0aa78758` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020614`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELE
```

---

## Crash 47: `3c2a8d811c40921d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020753`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> NOT CURRENT_TIMESTAMP ISNULL NOTNULL + CURRENT_DATE - NULL IS NOT NULL ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS ft
```

---

## Crash 48: `974b9e11ebf46dae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021001`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME IS NOT NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; 
```

---

## Crash 49: `df04bbe196220ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021598`

```sql
SELECT printf('%.*d', 2147483647, 0.01); SELECT substr('', 4294967296, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblo
```

---

## Crash 50: `21364a6f216c39af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022739`

```sql
SELECT printf('%.*d', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT OR REPLACE INTO t3 VALUES (TRUE IN (FALSE) OR total_changes() FILTER (WHERE NULL) COLLATE BINAR
```

---

## Crash 51: `e34b45600fc0dd22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025671`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE)
```

---

## Crash 52: `a390010f24df8840` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025677`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 53: `84de51da5aa2d591` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025687`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _rowid_, _ro
```

---

## Crash 54: `cdbbf4fb28833816` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029010`

```sql
SELECT printf('%d', -9223372036854775808, '4-'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p;
```

---

## Crash 55: `10bac86faceb553f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029519`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 56: `5eb60859a8423e44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029987`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(b DATE CHECK (NULL)); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE VIRTUAL T
```

---

## Crash 57: `eb4c8534ca8361e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032433`

```sql
SELECT printf('%.*d', -9223372036854775808, 1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME);
```

---

## Crash 58: `e653951b7fba64b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034481`

```sql
SELECT printf('%f', -1, 'Yd___ iO'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 59: `29829e737241fa70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034609`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c3 INTEGER PRIMARY KEY, rowid BOOLEAN UNIQUE, a VARCHAR(255) NOT NULL DEFAULT FALSE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_
```

---

## Crash 60: `3234d7611091567d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035406`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSER
```

---

## Crash 61: `ef5d977645743dc1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (CURRENT_TIME)) <> NULL); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b)
```

---

## Crash 62: `2abaf45b8b014be1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039261`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zeroblob(-9223372036854775808));
```

---

## Crash 63: `7ad9a775f51083a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041738`

```sql
SELECT substr('', -9223372036854775808, 2147483648); SELECT printf('%.*e', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c3); SELECT * EXCEPT VALUES (CURRENT_TIME NOTNULL) 
```

---

## Crash 64: `1939971b71d4587f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045625`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 BLOB, c3 INTEGER DEFAULT CURRENT_TIME, _rowid_ DATE); CREATE VIEW IF NOT EXI
```

---

## Crash 65: `6b51d78454d9f3fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045980`

```sql
SELECT printf('%.*s', 1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH q (c2, a) AS (VALUES (c1)) INSERT INTO p VALUES (CASE NULL NOT BETWEEN NULL ISNULL AND FALSE WHEN CURRENT_
```

---

## Crash 66: `9c1e41672744d030` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047627`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 GENERATED ALWAYS AS (a) UNIQUE); WITH RECURSIVE q (c2) AS (VALUES (CURRENT_DAT
```

---

## Crash 67: `f00284f1d053f206` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047638`

```sql
SELECT hex(zeroblob(-2147483649)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 GENERATED ALWAYS AS (a) UNIQUE); WITH RECURSIVE q (c2) AS (VALUES (CURRENT_DAT
```

---

## Crash 68: `65154f4cf3406eaf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048044`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p D
```

---

## Crash 69: `57469bc0d924d668` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063886`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH q AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c2 VA
```

---

## Crash 70: `17bb55a705d250fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064550`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), b GENERATED ALWAYS AS (a = 0) ); WITH t3 AS (VALUES (CURRENT_TIMESTAMP)) INSERT INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 71: `9077fc6ccbcc926d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065680`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (NULL))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p 
```

---

## Crash 72: `b35e135900a65e14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066199`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (FALSE NOT IN (VALUES (CURRENT_TIME))))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 73: `d0748cbdf8466b1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066284`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (FALSE))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR AB
```

---

## Crash 74: `e5446e9ae6e4d239` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068125`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANAL
```

---

## Crash 75: `33eec611be267236` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068631`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP COLLATE RTRIM == CURRENT_DATE); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTER
```

---

## Crash 76: `5d3b8db22b085784` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069213`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW I
```

---

## Crash 77: `833ace96212e6a5e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069677`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL DEFAULT -8091782896707151593130967772605905732563268746312303332031784150932914373157983887678900887663263465
```

---

## Crash 78: `64475f900523fb31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069832`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(c1 BLOB); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 79: `ab65e0069cb8b685` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069839`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 80: `852d6bcbec3d824a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069920`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL DEFAULT X'9c70BF6BAd9d'); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 81: `550bc735d521f102` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074679`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (TRUE IS FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 82: `86f83cef1aa296cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074900`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (NULL); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 83: `f95afb28126c7028` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075020`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (trim(FALSE) * TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 84: `8cd7a085e615bcc3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075200`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE 
```

---

## Crash 85: `5135893e24ae1c6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078369`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY N
```

---

## Crash 86: `4919ec704e90c9e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078422`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY F
```

---

## Crash 87: `f9b00f5ad70bf117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078656`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_TIME); CREATE VIRTUAL 
```

---

## Crash 88: `f06de6b4e7a5f813` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079960`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); SELECT * FROM q WHERE TRUE GROUP BY CURRENT_TIME EXCEPT VALUES (CUR
```

---

## Crash 89: `a0d8db4e041e4930` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080100`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(c2 NUMERIC); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TAB
```

---

## Crash 90: `fc11aa53afa9371a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081694`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(b INTEGER UNIQUE); INSERT INTO q SELECT * FROM p NOT INDEXED; VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 91: `b311a2f94fc5af51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089728`

```sql
SELECT printf('%.*d', -2147483648); SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c3); INSERT INTO p VALUES (CASE NOT NOT CURRENT_TIME COLLATE RTRIM W
```

---

## Crash 92: `897e7b85a47f33be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000090871`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON NOT TRUE << CURRENT_TIME OR TRUE ISNULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALU
```

---

## Crash 93: `cc3a04872dd67868` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091130`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON NOT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELECT hex(zero
```

---

## Crash 94: `59b3ca74b31610d7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091977`

```sql
SELECT printf('%.*d', 0, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, b); INSERT INTO r (c2) VALUES (CURRENT_DATE) ON CONFLICT(_rowid_) DO UPDATE SET c1 = TRUE IS NOT NULL REGEXP 
```

---

## Crash 95: `f666613343326961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091992`

```sql
SELECT printf('%.*d', 0, -1e308); SELECT round(1e308, 4294967295); SELECT printf('%x', 4294967295, '-'); SELECT substr('', -2147483648, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 96: `9ec32a1063dc98a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092888`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> NOT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE p AS (SELECT substr(
```

---

## Crash 97: `9a8ed46175e914ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092953`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIMESTAMP - FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA int
```

---

## Crash 98: `234511ec29ce5843` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093161`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME OR TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SELEC
```

---

## Crash 99: `0d6534a1d5b1a1a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093799`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON NOT X'ceeadaBF9B'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); EXPLAIN QUERY PLAN SELECT NULL AS o FROM p IN
```

---

## Crash 100: `e94ba40c6651a7c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000093933`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE >> NOT X'ceeadaBF9B'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO r VALUES (CURRENT_TIMESTAMP
```

---

## Crash 101: `233890ba5815e4b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094147`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON X'ceeadaBF9B' - NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrit
```

---

## Crash 102: `6039493e16db2d8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094323`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT -7243.39432795572388746142334344569196467038240436002534455461428780891756379804030262076448073350098576561720069909432612604790130e-217363670456179930522
```

---

## Crash 103: `9b43f9e017e864bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094813`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INT
```

---

## Crash 104: `d27be2bd402ce645` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000096663`

```sql
SELECT printf('%.*s', 0, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, b); INSERT INTO p (c3) VALUES (-FALSE | CURRENT_TIMESTAMP COLLATE RTRIM & FALSE IS DISTINCT FROM CURRENT_DAT
```

---

## Crash 105: `a4acf80e1b6ded17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097149`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY NULL HAVING FALSE AND CURRENT_DATE ORDER
```

---

## Crash 106: `5b2e3115314ccbf5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100300`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME > CURRENT_TIMESTAMP COLLATE RTRIM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO 
```

---

## Crash 107: `d406ef10229ac5d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101407`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC DEFAULT ' hv '); SELECT * FROM p JOIN p z_y_4_4ek ON NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE p; SE
```

---

## Crash 108: `15817f121bae40b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102049`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME IN (VALUES (FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALU
```

---

## Crash 109: `20f857d155ad3131` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102279`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT CURRENT_TIME AS x1x8_8k_j__4___p___jg1aw___s87u3xf_x__0o4__94_ra18a_7e
```

---

## Crash 110: `756b63e45d116785` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102563`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY FALSE, CURRENT_TIMESTAMP ORDER BY CURREN
```

---

## Crash 111: `8670f748aa8cf9dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102742`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES
```

---

## Crash 112: `8804420a65edbbef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102902`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) UNION ALL VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 113: `5d90aaf7d97a997a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103990`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE DEFAULT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME LIKE CURRENT_TIMESTAMP ESCAPE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT
```

---

## Crash 114: `bca37ab1c2e47495` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000107926`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT '--_-8-cn_e-___'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (c3) VAL
```

---

## Crash 115: `0f129bdf9e9ac288` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108121`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q (c3) VALUES 
```

---

## Crash 116: `4e4835efceca3800` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108517`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255) UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid TEXT PRIMARY KEY)
```

---

## Crash 117: `36212f7731919a6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109292`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 NUMERIC, c2 REAL UNIQUE, b BOOLEAN GENERATED ALWAYS AS (+CURRENT_TIMESTA
```

---

## Crash 118: `7531d419d19aabd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114071`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); REPLACE INTO q VALUES (NULL); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE FALSE GROUP BY CURREN
```

---

## Crash 119: `843962afe67d9437` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122060`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) , a NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE
```

---

## Crash 120: `b695a72e853960f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000122102`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) , a NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE
```

---

## Crash 121: `432a893c7dfa8941` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123131`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT -03821936.8167749322582661161358770286646802639386011301555714012648696464, c1 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO
```

---

## Crash 122: `ba8e5e84fb7222e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123286`

```sql
CREATE TABLE IF NOT EXISTS p(b BOOLEAN DEFAULT TRUE, c1 BOOLEAN PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(b); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 123: `916d389a6ba6c96a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123509`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a = -768) UNIQUE, b FLOAT NOT NULL DEFAULT -36); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 124: `de907776212f98e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125382`

```sql
SELECT printf('%.*g', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH q AS NOT MATERIALIZED (SELECT q.* LIMIT NULL) INSERT INTO q VALUES (NOT EXISTS (SELECT CURRENT_DATE A
```

---

## Crash 125: `216220f9d7b5a841` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125778`

```sql
SELECT printf('%.*s', 2147483647, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; SELECT p.* FROM p JOIN r j__ ON X'' IS NOT DISTINCT FROM -FALSE LIKE 
```

---

## Crash 126: `58f7486643518bfb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127654`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 GENERATED ALWAYS AS (a IS NULL) UNIQUE, b FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TAB
```

---

## Crash 127: `63dafce292d1721a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128635`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) , a NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 128: `030a58676426f5b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128782`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) , a NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_DATE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || T
```

---

## Crash 129: `13ad92ad7c25ac60` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128865`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) NOT NULL, a NUMERIC NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE
```

---

## Crash 130: `7d39b79fc73bab4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000128949`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a) , a FLOAT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE || TRUE |
```

---

## Crash 131: `8eb2962e2fd74f4a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129005`

```sql
CREATE TABLE IF NOT EXISTS p(a INT, c2 GENERATED ALWAYS AS (a) NOT NULL UNIQUE, b DATE PRIMARY KEY); INSERT OR ROLLBACK INTO p VALUES (~CURRENT_TIMESTAMP || TRUE || TRUE || TRUE || TRUE || TRUE || TRU
```

---

## Crash 132: `80a84f8dd2b6b8a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134573`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED CROSS JOIN q NOT INDEXED NA
```

---

## Crash 133: `606513130fd5e128` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136913`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY); REPLACE INTO q VALUES (NULL GLOB CURRENT_DATE AND NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREAT
```

---

## Crash 134: `052078a8790a4cd2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138410`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON -CURRENT_TIME + CURRENT_DATE;
```

---

## Crash 135: `7d2d0adc3b2f23ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145457`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, rowid TEXT UNIQUE); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME > p.rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VAL
```

---

## Crash 136: `ba2a1270100fd98f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145586`

```sql
CREATE TABLE IF NOT EXISTS p(c1 TEXT NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME > p.rowid; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANAL
```

---

## Crash 137: `2de22861917cbbe3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146927`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY rowid HAVING CURRENT_DATE ORDER BY CURRE
```

---

## Crash 138: `83d760f8d5a91ecb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147364`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIMESTAMP COLLATE RTRIM == FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFA
```

---

## Crash 139: `2d681a96c8294542` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147553`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON FALSE == FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; ANALYZE p; SEL
```

---

## Crash 140: `4a093de93bace5a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147616`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY _rowid_
```

---

## Crash 141: `9fbd1d0801a182bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147754`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON EXISTS (VALUES (CURRENT_TIME) INTERSECT SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIMESTAMP ORDER BY CURRENT
```

---

## Crash 142: `d1003a2d4ec04470` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148216`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE NOT NULL); SELECT * FROM p JOIN p z_y_4_4ek ON CAST(CURRENT_TIMESTAMP AS BLOB); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUE
```

---

## Crash 143: `7e89eb0816bd55e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152257`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_TIME OR TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT I
```

---

## Crash 144: `6e48f4c81dff801e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153190`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT NULL IN (VALUES (CURRENT_TIME) INTERSECT SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER () FROM p NOT INDEXED GROUP BY TRUE ORDER BY CURRENT_TIME ASC NU
```

---

## Crash 145: `f54172f08e8e85e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153506`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_TIME < CURRENT_TIME; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p DEFAULT VALUES; ANALYZE 
```

---

## Crash 146: `c9ebc34fa14bd80a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000153807`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON X'' - NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO q VALUES (+sum(EXISTS (SELECT RAISE(
```

---

## Crash 147: `1a4c1d636179ddf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154758`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT CURRENT_TIMESTAMP AS fk_8_4u__5_76__6__q FROM p JOIN p z_y_4_4ek ON FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT 
```

---

## Crash 148: `9619db6cef3bec14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155975`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT * FROM p JOIN p z_y_4_4ek ON CURRENT_DATE / CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; ANA
```

---

## Crash 149: `84203a82e55d7b07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000157074`

```sql
CREATE TABLE IF NOT EXISTS p(b FLOAT); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (), * FROM p JOIN p z_y_4_4ek ON TRUE << CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 150: `19834adb2f11840c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169076`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p INNER JOIN p NOT INDEXED USING (rowid) GROUP
```

---

## Crash 151: `f3e161a010e677fa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169128`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT EXISTS q(c2 INTEGER UNIQUE); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT * FROM p AS b_ CROSS JOIN (p LEFT JOIN q) GROUP BY FA
```

---

## Crash 152: `fd29d45239e34ddf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174704`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * 
```

---

## Crash 153: `d594c8961eb865f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174937`

```sql
CREATE TABLE IF NOT EXISTS p(b DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREATE
```

---

## Crash 154: `014267f5cf56461f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177178`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY 
```

---

## Crash 155: `4ea3339a26350fbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177645`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * 
```

---

## Crash 156: `56b34d79cffbbe05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177819`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * 
```

---

## Crash 157: `f9fdab22369c5c44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178524`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (last_insert_rowid() * FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 158: `29fab07e012e5528` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178908`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO q SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 159: `09d9b2526b163230` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181608`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CASE WHEN FALSE - CURRENT_TIMESTAMP THEN FALSE END), c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PR
```

---

## Crash 160: `244bd2e6cb720ec9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181937`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CURRENT_TIMESTAMP IS NOT NULL COLLATE BINARY), c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA i
```

---

## Crash 161: `faa37a81567270a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184075`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN CHECK (CASE WHEN FALSE - CURRENT_TIME % TRUE MATCH FALSE NOT IN (CURRENT_TIME) / NULL & CURRENT_TIMESTAMP THEN FALSE END), c3 FLOAT PRIMARY KEY); CREATE TABLE I
```

---

## Crash 162: `13c30088b726a23d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186439`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b NUMERIC DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 163: `3d63f5774f4fccf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186524`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b NUMERIC DEFAULT CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 164: `4c7a37725c37e87a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000186702`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c3 GENERATED ALWAYS AS (coalesce(a, b)) UNIQUE, b NUMERIC DEFAULT -62003.53015203419E+4109956127031113); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE V
```

---

## Crash 165: `437ec02393d14318` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187105`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC GENERATED ALWAYS AS (NULL) VIRTUAL, b FLOAT PRIMARY KEY); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 166: `22a7ef58697beb1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187550`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c1 GENERATED ALWAYS AS (a) UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3); SELECT TRU
```

---

## Crash 167: `7eb977afb8d0fa3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000190481`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (X'ceeadaBF9B' NOT IN (VALUES (FALSE))); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSE
```

---

## Crash 168: `787e00f239f3ffb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192592`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH q AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a TEX
```

---

## Crash 169: `500d8f54b1aa98a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192777`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH q AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a TEX
```

---

## Crash 170: `b5f1f134597fe7f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194676`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC CHECK (NULL), c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 171: `401ff563e9328655` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211240`

```sql
SELECT substr(' 4 98otpPy_ - _ u_', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c3, _rowid_); WITH RECURSIVE t1 AS (SELECT CURRENT_DATE, *) SELECT NULL NOTNULL NOT 
```

---

## Crash 172: `04cbb319f78d90f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218014`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); INSERT INTO p VALUES (NULL) UNION VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p D
```

---

## Crash 173: `ae58b10f03a3f70f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218418`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INTEGER PRIMARY KEY); INSERT INTO p VALUES (CURRENT_DATE); SELECT * FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE 
```

---

## Crash 174: `1aad25d292dece15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218774`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT group_concat(CURRENT_TIMESTAMP) FROM p NATURAL JOIN p WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 175: `6c88394c30886512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000218974`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT count(*) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY FALSE ASC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT RO
```

---

## Crash 176: `05ca065f02b563af` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219119`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL); INSERT INTO p VALUES (CURRENT_DATE); SELECT * 
```

---

## Crash 177: `8bafbc993421b7ce` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000219506`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c1 GENERATED ALWAYS AS (a) NOT NULL UNIQUE); WITH RECURSIVE q (c2) AS (VALUES (CURRENT_DATE)) SELECT FALSE AS h_d___5hz6gft6_x0_7_ows_bov_ex__y0_cg__du_ FROM p;
```

---

## Crash 178: `a7301f40a3234a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000220745`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP, TRUE, CURRENT_TIME)); EXPLAIN QUERY PLAN VALUES (count(DISTINCT NULL)); 
```

---

## Crash 179: `978b3abba52c5a23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247074`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(rowid REAL); CREATE TABLE IF NOT 
```

---

## Crash 180: `99ed07aaa867a499` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247358`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH q AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME); VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c1 VA
```

---

## Crash 181: `a15b3f380f55ca05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248103`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; WITH t3 AS (VALUES (CURRENT_TIMESTAMP)) INSERT INTO p VALUES (CURRENT_TIME); VALUES (CURRENT_TIME) INTERSECT
```

---

## Crash 182: `6e184aa2fd9561d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248264`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME) INTERSECT SELECT DISTINCT * FROM p WHERE TRUE ORDER BY C
```

---

## Crash 183: `6504928b7a8f6818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000248493`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT, c2 FLOAT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN UNIQUE); SELECT * FROM p NOT INDEXED CROSS JOIN q NOT INDEXED NATURAL LEFT JOIN p GROUP BY FALSE; CREATE VIRTUAL
```

---

## Crash 184: `bbddbe4a18b34c25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000249305`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC); INSERT OR REPLACE INTO p VALUES (FALSE NOT IN (VALUES (NULL))); VALUES (CURRENT_DATE); SELECT substr('_ptUm_U f_', 9223372036854775807, 2147483647); CREATE VI
```

---

## Crash 185: `398efebfd6619ec4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000250072`

```sql
SELECT printf('%.*f', 2147483647, 1e308); SELECT printf('%.*g', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c1, c3, c2); SELECT p.*, CASE CURRENT_TIMESTAMP
```

---

## Crash 186: `e6a797385106228d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000251875`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, _rowid_ GENERATED ALWAYS AS (a * a) , a NUMERIC NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 187: `dd8478372e650baa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255190`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL PRIMARY KEY, c2 TEXT UNIQUE); INSERT INTO q SELECT * FROM p NOT INDEXED; PRAGMA integrity_check; CREAT
```

---

## Crash 188: `0ffbfd66ad9c8205` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255639`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN CHECK (FALSE - CURRENT_TIMESTAMP), c3 FLOAT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BLOB UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREA
```

---

## Crash 189: `b82dcf326dac432c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259675`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRE
```

---

## Crash 190: `3dcc027e7cb7fbf7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259864`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (TRUE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGMA integrity_check; CREA
```

---

## Crash 191: `088a686a0f859894` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259870`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME); PRAGM
```

---

## Crash 192: `39bb0f3339f59d84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259879`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRE
```

---

## Crash 193: `10c26b7a5b3d54a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259887`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (TRUE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME 
```

---

## Crash 194: `f193d972993a9387` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259893`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (FALSE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME
```

---

## Crash 195: `4d4962eac138dd52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259899`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INT UNIQUE); INSERT INTO p VALUES (CURRENT_DATE * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURRE
```

---
