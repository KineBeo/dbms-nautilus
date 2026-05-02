# Crash Triage Report

**Total crashes:** 233  
**Unique crash sites:** 233  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 233 | 233 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `89318794710b1f24` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000262`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c2); INSERT OR IGNORE INTO t1 VALUES (CURRENT_TIMESTAMP % CURRENT_TIMESTAMP <> FALSE COLLATE BINARY NOT NULL & t3.c2 != EXISTS (SELECT NULL <
```

---

## Crash 2: `b4303ea51a19dbb2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000554`

```sql
SELECT printf('%lli', 4294967296, '_ '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); INSERT OR ABORT INTO t3 VALUES ((WITH RECURSIVE p (c3) AS NOT MATERIALIZED (VALUES (CASE CURRENT_D
```

---

## Crash 3: `012046da832a49c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000632`

```sql
SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 4: `44b3575b95f95982` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000831`

```sql
SELECT substr('', 2147483648, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); INSERT OR ROLLBACK INTO p VALUES (NOT RAISE(IGNORE) IS NOT NULL <> 505712779.497662337
```

---

## Crash 5: `9aa96f858997f934` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001009`

```sql
SELECT printf('%llu', -9223372036854775808, '- _N T-pNM  _--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP) UNI
```

---

## Crash 6: `6c369845be7a48ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001094`

```sql
SELECT substr('', 9223372036854775807); SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN GENERATED ALWAYS AS (+trim(RAISE(IGNORE) IS NOT NULL & CURRENT_TIME COLLATE 
```

---

## Crash 7: `9774aeef73744d8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001299`

```sql
SELECT printf('%.*f', 9223372036854775807, 1e308); SELECT printf('%.*g', -2147483649, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1, a); INSERT INTO p (c3, b) VALUES (char((VALUE
```

---

## Crash 8: `afb3c2bb75e81428` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001528`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, _rowid_, c1, c1, a); INSERT INTO p (c1, c1) VALUES (CURRENT_DATE, TRUE) ON CONFLICT(c2) DO UPDATE SET a = FALSE != (SELECT CASE CURRENT_DATE WHE
```

---

## Crash 9: `3d78b6196c0a3bc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001544`

```sql
SELECT printf('%d', -2147483648, 'wk_---1  7K-_'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p VALUES (~+CURRENT_DATE LIKE NOT EXISTS (VALUES (RAISE(IGNORE))) LIKE ~+CURREN
```

---

## Crash 10: `ffbb64f4b608b6c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001714`

```sql
SELECT printf('%.*f', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); INSERT INTO q DEFAULT VALUES; WITH RECURSIVE q AS NOT MATERIALIZED (SELECT CURRENT_TIME NOT BETWEEN CUR
```

---

## Crash 11: `26be99e063f89b93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001879`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT p.* FROM q WHERE EXISTS (SELECT * UNION SELECT DISTINCT RAISE(IGNORE) NOT IN (VALUES (CURRENT_TIME)) AS x3__68
```

---

## Crash 12: `0cd0bc23842ecb0a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001941`

```sql
SELECT hex(zeroblob(0)); SELECT printf('%.*g', 2147483647, 0.01); SELECT printf('%.*f', -2147483649, 1.0); CREATE TABLE IF NOT EXISTS p(c2 TEXT, c2 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT
```

---

## Crash 13: `759adc993a9536e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001948`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE, a GENERATED ALWAYS AS (a) NOT NULL); VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01); SELECT printf('%.*f', -2147483649, 1.0); CREATE TABLE IF
```

---

## Crash 14: `79d0fecf7cdd03aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002155`

```sql
SELECT printf('%.*f', 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (CASE NULL WHEN CURRENT_TIME THEN NULL END > +TRUE BETWEEN (TRUE) AND ~RAIS
```

---

## Crash 15: `6f8089e875bba9ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002338`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO p VALUES (CASE NULL WHEN CURRENT_TIME THEN NULL END > +TRUE BETWEEN NULL AND FALSE); SELECT (W
```

---

## Crash 16: `6c49c6e5b87d2b14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002440`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 17: `59c4a1ae250bc6c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002470`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT OR FAIL INTO t1 VALUES (NOT
```

---

## Crash 18: `f9c2bb6dc414b900` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002479`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c2 NUMERIC, c2 GENERATED ALWAYS AS (coalesce(a, b)) UNIQUE, a BOOLEAN PRIMARY KEY); INSERT INTO p DEFA
```

---

## Crash 19: `ebe74652a7b43db0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(b NUMERIC, c1 GENERATED ALWAYS AS (a) NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 20: `2ee2f757d342bcef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002535`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); EXPLAIN QUERY PLAN VALUES (NULL); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT OR FAIL INTO t1 VALUES (N
```

---

## Crash 21: `7fc2d15b5b389f77` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003113`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME | TRUE < CURRENT_DA
```

---

## Crash 22: `278d78ae6a295edb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003598`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (FALSE); SELECT hex(zeroblob(0));
```

---

## Crash 23: `22a2ebb097e34564` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003604`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME); SELECT hex(zerobl
```

---

## Crash 24: `aa1adf55905a592b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003610`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (NULL); SELECT hex(zeroblob(0)); 
```

---

## Crash 25: `d31f713a86853f99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003616`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME | CURRENT_TIME); SE
```

---

## Crash 26: `38e84e2c428a9663` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003623`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_TIME | TRUE < CURRENT_DA
```

---

## Crash 27: `cc28c03b40bfb59f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003814`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM / FALSE * NULL, NULL DESC; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 28: `6ad6e2ea4f9f2f16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003864`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE ASC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO r WITH t
```

---

## Crash 29: `5439cc7d7164a694` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003893`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, CURRENT_TIMESTAMP DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 30: `7cbb4be956bb1b0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004441`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES ((CURRENT_DATE IN (CURRENT_TIMESTAMP IS NOT NULL, TRUE))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 31: `a6b089348754fac1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004579`

```sql
SELECT printf('%.*g', 4294967296); SELECT hex(zeroblob(-2147483648)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); VALUES (CASE max(~RAISE(IGNORE) LIKE CURRENT_DATE < RAISE(IGNORE)) FILTER
```

---

## Crash 32: `e80f69f194247a5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005039`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c3 INT NOT NULL DEFAULT FALSE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 33: `5e804004e18e492c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005057`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 34: `5ebfddc996195f5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005063`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b FLOAT, c1
```

---

## Crash 35: `732b4fd1fb1a9a17` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005077`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b FLOAT, c1 GENERATED ALW
```

---

## Crash 36: `e16d0ddc27363811` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007402`

```sql
SELECT substr('f_ ', -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ABORT INTO q VALUES ((VALUES (FALSE) UNION ALL SELECT ALL *, * FROM q ORDER BY (CURRENT_TIMESTAMP 
```

---

## Crash 37: `2741e517d4610379` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011474`

```sql
SELECT printf('%.*s', -1); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 38: `7187b73df2f5a646` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011624`

```sql
SELECT printf('%.*d', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, a); VALUES (CURRENT_TIME);
```

---

## Crash 39: `5e6718767b0800c4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011849`

```sql
SELECT round(0.0, -2147483648); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `68d1dad2e94440ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012357`

```sql
SELECT substr('g', -2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ROLLBACK INTO q VALUES (CASE (changes()) WHEN TRUE MATCH RAISE(IGNORE) THEN CURRENT_TI
```

---

## Crash 41: `6d907274ee91ad84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012991`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 42: `1d77a46bc2b0432d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000013063`

```sql
SELECT substr('', 2147483647, 2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO q VALUES (X'f4Fa' REGEXP CASE RAISE(IGNORE) IS NULL WHEN RAISE(IGNORE) COLLA
```

---

## Crash 43: `c9c6310c09acb714` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014463`

```sql
SELECT printf('%.*e', -9223372036854775808); SELECT substr('g-g1p', -9223372036854775808, 2147483648); SELECT printf('%.*f', -2147483649, -1e308);
```

---

## Crash 44: `392ff13b68a8324d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014817`

```sql
SELECT substr('-i-w7U_ 0_', 9223372036854775807, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REPLACE INTO p VALUES (FALSE IS NULL, CURRENT_TIME NOTNULL NOT NULL LIKE ~CURRE
```

---

## Crash 45: `2471dcd124485a87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018515`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 46: `8c0a596aa9c89f3b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000019193`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE changes() FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND 
```

---

## Crash 47: `cd12ec2ea39f23cd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000020333`

```sql
SELECT hex(zeroblob(0)); SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA in
```

---

## Crash 48: `0a69054cbff8dbc9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023081`

```sql
SELECT printf('%lli', -9223372036854775808, '9- _o_ __-2m0'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); VALUES (CURRENT_TIME) ORDER BY random() DESC NULLS FIRST LIMIT CURRENT_DATE % CUR
```

---

## Crash 49: `dda55e5e1db89055` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024036`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_DATE) UNION ALL VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 50: `7c44628928f56eb5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024358`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(a INT); VALUES (CURRENT_DATE) UNION ALL SELECT ALL * FROM q NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 51: `1cf54e70812d0f0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025088`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE, CURRENT_TIME)); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 52: `9ed7fc643c257ecc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029613`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM, NULL DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USI
```

---

## Crash 53: `2eac374aaab263e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034326`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIME) INTERSECT VALUES (CURRENT_DATE != CURRENT_DATE); C
```

---

## Crash 54: `9187c7af5b9dd037` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034582`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (last_insert_ro
```

---

## Crash 55: `4c55804cfb563f6e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035164`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (changes()); CR
```

---

## Crash 56: `8f678a54b0977740` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035306`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 57: `c689d62e9339933c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035880`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (count(*)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 58: `2d5924b1a8c2a77d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036137`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (CURRENT_DATE) EXCEPT VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 59: `9a2cdba68254822b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036576`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE NULL INTERSECT VALUES (total_changes()); SELECT pr
```

---

## Crash 60: `515005109f92cc9c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036724`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (NULL) INTERSECT VALUES (CURRENT_DATE); SELECT printf('%.*g', 214
```

---

## Crash 61: `38271669d685f296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036966`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE NULL INTERSECT VALUES (CURRENT_DATE | TRUE); CREAT
```

---

## Crash 62: `c30f1d7ca98a7132` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037865`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c3 DATE, a GENERATED ALWAYS AS (a) NOT NULL); SELECT * FROM p WHERE EXISTS (SELECT CURRENT_TIMESTAMP L
```

---

## Crash 63: `b86b9ac62fc32dad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037872`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(rowid INT CHECK (CAST(FALSE AS BLOB))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT INTO p 
```

---

## Crash 64: `07354c3ccf6128ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037943`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT UNIQUE); VALUES (CURRENT_DATE); SELECT round(0.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); INSERT INTO t3 DEFAULT VALUES; EXPLAIN
```

---

## Crash 65: `499d916a99573ab7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040762`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM t3 NOT INDEXED JOIN p ON CURRENT_DATE WHERE NULL GROUP BY CURRENT_DATE; VALUES (TRUE); CREATE VIRTUAL T
```

---

## Crash 66: `a2e08af1dcb0f869` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043859`

```sql
SELECT printf('%.*e', 9223372036854775807, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3); REPLACE INTO q VALUES (CURRENT_TIME IS NULL LIKE NOT CURRENT_DATE = RAISE(IGNORE) | FALSE
```

---

## Crash 67: `206a5ebb1c4c5c22` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044151`

```sql
SELECT substr('--3w_- _-x8x', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH s AS NOT MATERIALIZED (SELECT FALSE FROM r NOT INDEXED WHERE NULL != RAISE(IGNORE) GR
```

---

## Crash 68: `e6c2a1e1d324e456` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044287`

```sql
SELECT printf('%.*e', -9223372036854775808, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); EXPLAIN QUERY PLAN SELECT DISTINCT q.* FROM (VALUES (NULL COLLATE NOCASE) LIMIT CURRENT_T
```

---

## Crash 69: `5bce3019b1191043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046178`

```sql
SELECT round(-1.0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN NOT NULL, c2 INT UNI
```

---

## Crash 70: `7ef3e2d766505c1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051163`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL, b DATE UNIQUE); SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAMP) AS sub1; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 71: `f690b2384ce5c0a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000051922`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (min(CURRENT_DATE)) EXCEPT SELECT * FROM p WHERE NULL INTERSECT VALUES (CURRENT_TIMESTAMP); CR
```

---

## Crash 72: `9663c5f57a2c1a6f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052569`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT TRUE AS h3__6074 ORDER BY TRUE DESC NULLS FIRST; SELECT printf('%.*f', 21
```

---

## Crash 73: `36bdf061043f15aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054655`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p AS a NATURAL LEFT JOIN p AS vw4_e_7_n1_8_21_p___m__mi2r_
```

---

## Crash 74: `361ddcfaecc20820` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054908`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT TRUE GLOB FALSE AS a FROM p WHERE CURRENT_TIMESTAMP INTERSECT VAL
```

---

## Crash 75: `ed74196ff68c378e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063054`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_DATE ASC NULLS LAST; SELECT printf('%.*g', 2147483647,
```

---

## Crash 76: `34c76a1226968dd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063372`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_TIME ASC NULLS LAST, NULL DESC; CREATE VIRTUAL TABLE I
```

---

## Crash 77: `8da93d3b673c94f2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063412`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_DATE ASC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 78: `bb1a2dc87a92dd51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069789`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_DATE)); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 79: `4ea683184b0961ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069901`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (CURRENT_TIMESTAMP, NULL)); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 80: `33fe191afe77988c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070302`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 81: `1d36b7e92b2bc498` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070408`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE, CURRENT_DATE, CURRENT_TIMESTAMP)); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 82: `2c96d937f242dcf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070606`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (CURRENT_DATE, CURRENT_DATE, CURRENT_TIME)); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 83: `cffd33dc173d1ecd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071035`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (CURRENT_TIME))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO
```

---

## Crash 84: `67f3c8daf1d2698f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072626`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(a INT); VALUES (CURRENT_DATE) INTERSECT SELECT ALL * FROM q NOT INDEXED LIMIT TRUE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 85: `1230a94768523b75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074980`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (hex(hex(hex(hex(hex(hex(hex(hex(hex(TRUE)))))))))); SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 86: `4ec6c32d13d1c9fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075001`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (hex(hex(CURRENT_TIME))); SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 87: `957329ed00ba2e13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080712`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (random() >> TRUE), c1 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 88: `04a7ed66176f97a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081122`

```sql
SELECT hex(zeroblob(1)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(1)); CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE), rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(a 
```

---

## Crash 89: `321a8ce1f03e190a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081164`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE), rowid NUMERIC UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT E
```

---

## Crash 90: `85f011c85e5d17c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081618`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (FALSE NOT BETWEEN TRUE AND CURRENT_TIMESTAMP), c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 91: `0c5e74b2ae669f3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081999`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p (c2) VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b
```

---

## Crash 92: `076c29e60365bb5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083936`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE DEFAULT ''); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a)
```

---

## Crash 93: `6567451a2e6f7707` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086149`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (NULL NOT LIKE TRUE), rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 94: `3b2e42a0cf33bb20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086284`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (NULL ISNULL), rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 95: `039b447ec63ab877` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086387`

```sql
CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE, rowid INT UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 96: `d63f6fe7ba97d4bd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087602`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (EXISTS (VALUES (NULL))); CREATE VIRTUAL TABLE IF NOT EXISTS f
```

---

## Crash 97: `1ed5b1748e7c9271` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088023`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL DEFAULT X'CEB5A27B'); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 98: `1f1ea8a1d525efcd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088090`

```sql
CREATE TABLE IF NOT EXISTS p(rowid TEXT); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN NOT NULL DEFAULT CURRENT_TIMESTAMP); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); SELECT printf('%.*g', 2147483647, 0
```

---

## Crash 99: `0669e8bfc39438ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088113`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(_rowid_ INT DEFAULT CURREN
```

---

## Crash 100: `4a9279aa4ce323de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088127`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255), _rowid
```

---

## Crash 101: `713a3cd30442d8fc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088136`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c3 REAL UNIQUE); CREATE VI
```

---

## Crash 102: `a3894596afbbdb05` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098921`

```sql
SELECT printf('%f', 2147483647, ''); SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); SELECT *, * FROM p NATURAL JOIN p WHERE CURRENT_TIMESTAMP IS CURRENT_DATE * NOT
```

---

## Crash 103: `bb86e744c4ba8073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100906`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q DEFAULT VALUES; ANALYZE q; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 104: `e913fd74cee31d86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101039`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 105: `0c68c104aa5206bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101117`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 REAL); WITH RECURSIVE q AS (SELECT *) INSERT INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 106: `9dddb6ff81fced9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105104`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 107: `ef7bde99667ba21f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106137`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT OR FAIL INTO p VALUES (TRUE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 108: `1eb8d574cd6c361f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106485`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT, c1 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (hex(hex(CURRENT_TIME))); EXPLAIN QUERY PLAN SELECT *; SELECT hex(zeroblob(922337
```

---

## Crash 109: `24529e665a3eabec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110956`

```sql
SELECT substr('zz  l--S bp--_ IN', 2147483647); SELECT printf('%.*d', -2147483649, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c1); INSERT INTO q VALUES (NOT EXISTS (SELECT * F
```

---

## Crash 110: `ddc89e05b641ebef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114549`

```sql
SELECT substr('_w8', -9223372036854775808, 4294967296); SELECT hex(zeroblob(-2147483648)); SELECT printf('%.*f', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); IN
```

---

## Crash 111: `659cba6813d19282` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115669`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE, c1 VARCHAR(255) UNIQUE); WITH RECURSIVE t3 (c1, rowid) AS (SELECT DISTINCT * FROM p) SELECT * FROM t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 112: `dff88b76d0281b61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115956`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 DATE); WITH RECURSIVE t3 (rowid) AS (VALUES (zeroblob(CURRENT_TIMESTAMP))) SELECT * FROM t3; SELECT printf('%.*f', 21474836
```

---

## Crash 113: `24991d7d06865dc6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127681`

```sql
SELECT round(-1e308, 2147483648); SELECT round(0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, b); WITH p AS MATERIALIZED (SELECT CURRENT_TIMESTAMP AS a FROM q NOT 
```

---

## Crash 114: `1279e5457d02897d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132515`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE VI
```

---

## Crash 115: `74b05254d8c6e815` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132590`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(a TEXT GENERATED ALWAYS AS
```

---

## Crash 116: `2aa3ba4cb481e04f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132600`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c1 INTEGER, a GENERATED AL
```

---

## Crash 117: `66682a2b7bdd6270` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133215`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE changes() FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC ROWS BETWEEN UNBOUNDED PRECEDING AND 
```

---

## Crash 118: `ee5e769aec8a2c15` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134250`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT CURRENT_TIMESTAMP AS h3__6074
```

---

## Crash 119: `f96523ad7a9092a6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134442`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c1 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (NULL) UNION ALL VALUES (CURRENT_TIME)
```

---

## Crash 120: `0452c23e6458f047` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135456`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TA
```

---

## Crash 121: `dae2d97cf7470a1a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135542`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BLOB, b GENERATED ALWA
```

---

## Crash 122: `b20c47e3e38e0761` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135636`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 DATE); SELECT * FROM p
```

---

## Crash 123: `9cfea252131dcc83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135698`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE 
```

---

## Crash 124: `9a3859afbe1635fd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136417`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB DEFAULT X'6A69ce'); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 125: `5b30a0d59d88b960` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137094`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE LIKE TRUE ESCAPE FALSE >= NULL), c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 126: `9f40394f4cc96870` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000137287`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE >= NULL), c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2
```

---

## Crash 127: `49ce629a42baea5d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138270`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (CURRENT_DATE), b REAL PRIMARY KEY, c3 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE 
```

---

## Crash 128: `3cc8e95862f203a4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138689`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE DEFAULT X'fE', c1 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 129: `7567eff17958342c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139261`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (random() >> TRUE BETWEEN CURRENT_DATE AND TRUE << CURRENT_DATE NOT LIKE TRUE), c1 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VA
```

---

## Crash 130: `91032b6b32c85b55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139695`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (random() >> TRUE >> TRUE >> TRUE), c1 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL
```

---

## Crash 131: `04ef3e3677f9b686` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139842`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (TRUE), c1 REAL); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 132: `8c2ad54eab7ace5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145793`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (hex(TRUE)); SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (total_changes()); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 133: `c36f9e498db266c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145912`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (FALSE); SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (total_changes()); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 134: `b0bb1fcf03f5197e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145918`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (total_changes()); CREATE VIRTUAL TABLE I
```

---

## Crash 135: `e9e9f8d26444640d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145924`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (random()); SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (total_changes()); CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 136: `5d8667ede50e932c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145950`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC CHECK (random() >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE >> TRUE)); INSERT OR REPLACE INTO p VALUES (hex(hex(CURRENT_TIME))); SELECT *; SELECT hex(zeroblo
```

---

## Crash 137: `9e89f0d19e2e9d47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000145998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (hex(hex(random() >> TRUE - TRUE))); SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 138: `269fbf4490dee9a3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000146343`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_TIMESTAMP); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL); INSERT OR REPLACE INTO p VALUES (F
```

---

## Crash 139: `c69ddc163e447ed5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (FALSE) UNION ALL VALUES (0.0) INTERSECT VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 140: `b55bcdfe533c9116` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000147180`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); VALUES (FALSE) UNION ALL VALUES (CURRENT_TIMESTAMP) UNION ALL VALUES (TRUE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 141: `aa172861bb314e26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148235`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN q a ON NULL OR NULL IN (CURRENT_DATE); CREATE VIRTUAL TAB
```

---

## Crash 142: `6629d6d632a978b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000148767`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(a INT); VALUES (CURRENT_DATE) INTERSECT SELECT * FROM q NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_D
```

---

## Crash 143: `67851662c830a76d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149521`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE TABLE IF NOT EXISTS q(a INT); VALUES (CURRENT_DATE) UNION ALL SELECT DISTINCT CURRENT_TIMESTAMP AS h3__6074 FROM p NOT INDEXED WHERE CURRENT_DATE LIMIT TR
```

---

## Crash 144: `1f3f11d5c15aa225` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150509`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (+TRUE))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM p WH
```

---

## Crash 145: `b6f7d05857ed798f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150707`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (NULL))); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM p WHE
```

---

## Crash 146: `30724311b597886e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151084`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN ('c9__SI2 -_ ')); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAU
```

---

## Crash 147: `21602b1969e4f12e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151577`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CAST(CURRENT_DATE AS INTEGER) IN (CURRENT_DATE, CURRENT_DATE, CURRENT_TIMESTAMP)); PRAGMA quick_check; SELECT printf('%.*g', 214748
```

---

## Crash 148: `67579375678b3a8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151721`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CAST(CURRENT_DATE AS INTEGER) IN (CURRENT_DATE, TRUE)); PRAGMA quick_check; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 149: `ea9a86fe0731c901` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151987`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE U
```

---

## Crash 150: `a78e6fc271ef083b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152126`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5
```

---

## Crash 151: `d3875720708d2b20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152149`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p NOT INDEXED 
```

---

## Crash 152: `dd0bbf03baadd27c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158460`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, count(*) FILTER (WHERE TRUE) OVER (ORDER BY TRUE DESC ROWS BETWEEN 
```

---

## Crash 153: `089513755c043bb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158712`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, count(*) FILTER (WHERE TRUE) OVER (ORDER BY CURRENT_TIME DESC NULLS LAST GROUPS BE
```

---

## Crash 154: `90205885ebd2bfa4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158906`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, count(*) FILTER (WHERE TRUE) OVER () DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT 
```

---

## Crash 155: `5dd0e1a9970a265a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159563`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE, CURRENT_TIMESTAMP) INTERSECT VALUES (CURRENT_DATE, CURRENT_TIMESTAMP); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 156: `d8d2192e2213763c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000159780`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE, FALSE ORDER BY CURRENT_TIME ASC NULLS LAST, NULL DESC; CREATE VIRTUAL TABLE I
```

---

## Crash 157: `a67b4f5b1dcc006c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160242`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p AS a LEFT JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_DATE ASC NULLS LAST; CREA
```

---

## Crash 158: `ac63d0e77c8a9c4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160681`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY c2 ASC NULLS LAST; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 159: `2839e9589f4292d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160820`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY CURRENT_TIMESTAMP DESC; SELECT printf('%.*f', 2147483647, 1e30
```

---

## Crash 160: `4242ea55e805a3c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000160867`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY c2 MATCH TRUE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 161: `930dcc501e5e69ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161212`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL LEFT JOIN p AS vw4_e_7_n1_8_21_p___m__mi2r_0i34txah_k40kty5_048gjpt__0_ccx8j__3f0t2gy5_q_7__5224te2s__lg_03va
```

---

## Crash 162: `297fac311dabc623` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161522`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p AS a LEFT JOIN p NOT INDEXED WHERE CURRENT_DATE ORDER BY NULL DESC; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 163: `a73e8cc78fe70f86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173447`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (min(FALSE)); S
```

---

## Crash 164: `8102af1eb9150458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000173588`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_DATE) INTERSECT VALUES (random()); SELECT printf('%.*f',
```

---

## Crash 165: `daa42ebd72df2033` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174429`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT 0); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (CURRENT_DATE
```

---

## Crash 166: `b97dd3f227770360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000174550`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALU
```

---

## Crash 167: `0b62686185a8b309` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000176506`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, CURRENT_DATE ASC NULL
```

---

## Crash 168: `4b3ab9b51811c2e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178446`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL, b DATE UNIQUE); SELECT * FROM (SELECT TRUE COLLATE BINARY AS h3__6074 FROM p WHERE CURRENT_TIMESTAMP) AS su
```

---

## Crash 169: `b4cbfc6395ad5836` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178608`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL, b DATE UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP AS h3__6074 FROM p WHERE CURRENT_TIMESTAMP) AS sub1
```

---

## Crash 170: `7b9492dee01e62ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178643`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL, b DATE UNIQUE); SELECT * FROM (SELECT CURRENT_TIMESTAMP FROM p WHERE CURRENT_TIMESTAMP) AS sub1; SELECT pri
```

---

## Crash 171: `88072db771a11a9b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178818`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, rowid GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL, b DATE UNIQUE); SELECT NULL IN (VALUES (CURRENT_DATE)) AS a, * FROM (SELECT * FROM p WHERE CURRENT_TIMESTAM
```

---

## Crash 172: `77ea081cb3fc8879` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184075`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIMESTAMP; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL T
```

---

## Crash 173: `3a9730df9b49f434` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184403`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 TEXT UNIQUE); INSERT INTO p SELECT * FROM p WHERE CURRENT_TIMESTAMP; EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIR
```

---

## Crash 174: `2e4649cc7bf42f06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184563`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 175: `0d07f8f2f0b6caeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000185325`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); VALUES (count(*) FILTER (WHERE TRUE) OVER ()); SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 176: `5397a4be19fac043` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191583`

```sql
SELECT printf('%f', -9223372036854775808, 'U __jpD--'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM p WHERE EXISTS (SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY FALSE, 
```

---

## Crash 177: `f8e052279ced3045` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000192161`

```sql
SELECT printf('%.*g', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INTO t2 VALUES (CURRENT_TIMESTAMP * CURRENT_TIME <= FALSE, CASE NULL WHEN CURRENT
```

---

## Crash 178: `6a1aa124bdd52345` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193009`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY CURRENT_TIME ORDER BY CURREN
```

---

## Crash 179: `d4227dabadd2a9f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193136`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE RAISE(IGNORE) GROUP BY CURRENT_TIMESTAMP WINDOW w1 AS (PARTITION BY CURRENT_TIME ORDER BY CURREN
```

---

## Crash 180: `21da0eec09141a35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199257`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); ANALYZE p; SELECT printf('%.*f', 2147483647, 1e308);
```

---

## Crash 181: `8aa5e23c814989b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000207740`

```sql
CREATE TABLE IF NOT EXISTS p(c1 DATE, a GENERATED ALWAYS AS (a) ); SELECT count(*) FILTER (WHERE TRUE) OVER (PARTITION BY CURRENT_TIME ORDER BY CURRENT_TIME ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UN
```

---

## Crash 182: `d2d917f6897e347f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000209304`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); SELECT avg(CURRENT_DATE) FROM p NOT INDEXED EXCEPT VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 183: `d9eb3e985cca1183` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000211624`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (NULL COLLATE NOCASE); CREAT
```

---

## Crash 184: `0366ed2dc3655c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212231`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM (SELECT CURRENT_TIMESTAMP OR CURRENT_TIME COLLATE BINARY F
```

---

## Crash 185: `8e37079d78107c41` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212420`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM (VALUES (NULL)) AS h0f15_3_7_91_85v_0_g_a_4_990_ WHERE CUR
```

---

## Crash 186: `3f71e85e094ac77d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212428`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM (SELECT TRUE FROM p) AS h0f15_3_7_91_85v_0_g_a_4_990_ WHER
```

---

## Crash 187: `b09a6005aa7c0a51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212506`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM (SELECT avg(CURRENT_DATE) FILTER (WHERE TRUE) OVER () FROM
```

---

## Crash 188: `368fe3b783ffbe14` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213216`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c3); VALUES (CURRENT_DATE) INTERSECT SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY CURRENT_DATE DESC; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 189: `6e0891863c07cf12` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213827`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT SELECT * FROM p WHERE CURRENT_TIMESTAMP INTERSECT VALUES (count(DISTINCT
```

---

## Crash 190: `4db55b7a35e5af10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213919`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (zeroblob(CURRENT_TIMESTAMP)) INTERSECT VALUES (NULL) EXCEPT VALUES (CURRENT_DATE); CREATE VIR
```

---

## Crash 191: `4bbf9d96ff0b6117` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214749`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (json_valid(NULL)) INTERSECT VALUES (NULL); CREATE VIRTUAL TABLE 
```

---

## Crash 192: `80e699cdf1f7df83` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215021`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (json_valid(json_array(NULL))) INTERSECT VALUES (NULL); SELECT pr
```

---

## Crash 193: `3c23323794d2b505` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215119`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (json_valid(last_insert_rowid())) INTERSECT VALUES (NULL); SELECT
```

---

## Crash 194: `2b30051ce83a0354` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215376`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (json_valid(json_array(FALSE))) INTERSECT VALUES (CURRENT_TIME); 
```

---

## Crash 195: `d2fd691f3fae0fe8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215566`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid FLOAT NOT NULL); VALUES (CURRENT_DATE) EXCEPT VALUES (json_valid(count(*))) INTERSECT VALUES (CURRENT_TIME); CREATE VI
```

---

## Crash 196: `8ab472448d383e62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000225856`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL LEFT JOIN (SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP) AS a NATURAL JOIN p NOT INDEXED WHERE CURRENT
```

---

## Crash 197: `31c8bd1322614275` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226135`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE ORDER BY rowid MATCH TRUE ASC NULLS LAST; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 198: `147944175b8b863c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226308`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL JOIN p NOT INDEXED NATURAL JOIN p NOT INDEXED WHERE CURRENT_TIMESTAMP ORDER BY c2 ASC NULLS LAST; CREATE VIRT
```

---

## Crash 199: `a0f6ffb9d2382c31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000226529`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT * FROM p WHERE CURRENT_TIMESTAMP GROUP BY (SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, count(*) FILTER (WHERE TRUE) OVE
```

---

## Crash 200: `cc854344e2a81a30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000227763`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL); EXPLAIN QUERY PLAN SELECT FALSE AS gi9ap4_6cs6xi1_10h ORDER BY FALSE, count(*) FILTER (WHERE TRUE) OVER (ORDER BY CURRENT_TIMESTAMP COLLATE RTRIM GROUPS
```

---

## Crash 201: `e0c48e4824a213e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235661`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(a); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE CURRENT_DATE U
```

---

## Crash 202: `90f354ca86c81c44` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236145`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (FALSE)) OR CURRENT_DATE IN (CURRENT_DATE, CURRENT_DATE, CURRENT_TIMESTAMP)); PRAGMA quick_check; SELECT pr
```

---

## Crash 203: `6345a46fe4240ab2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236338`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (VALUES (FALSE)) OR CURRENT_DATE IN (CURRENT_TIMESTAMP)); PRAGMA quick_check; SELECT printf('%.*f', 2147483647, 1e3
```

---

## Crash 204: `453b8c19a568bb25` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (zeroblob(CURRENT_TIMESTAMP), zeroblob(CURRENT_TIMESTAMP), FALSE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 205: `f0dcb71efb9c8620` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236815`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (last_insert_rowid(), zeroblob(CURRENT_TIMESTAMP), FALSE)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 206: `9758fa67abb187c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237063`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (CURRENT_DATE IN (-83412)); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT * FROM p WHERE EXIS
```

---

## Crash 207: `2fae9f047439affa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000237593`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT); INSERT OR FAIL INTO p VALUES (-1406242881963099447559362294225337673069700193868394384265424316265180553660637973069390455948604316644866878089988972346713964102
```

---

## Crash 208: `f37d89828be5f898` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240818`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT count(*) FILTER (WHERE TRUE) OVER () AS a, * FROM p JOIN q a ON NULL IN
```

---

## Crash 209: `d7b982bf9352e371` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241008`

```sql
CREATE TABLE IF NOT EXISTS p(b INT); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) NOT NULL); INSERT INTO p DEFAULT VALUES; SELECT * FROM p JOIN q a ON NULL IN (CURRENT_DATE, CURRENT_TIME); CREATE VIRTU
```

---

## Crash 210: `5470138826cdbfca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241427`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(_rowid_); VALUES (CURRENT_DATE) UNION ALL VALUES (X'b2EBBFDB'); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 211: `80d47a8af5d7d58a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242820`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC NOT NULL); INSERT OR REPLACE INTO p VALUES (hex(hex(FALSE || FALSE || zeroblob(CURRENT_TIMESTAMP)))); SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 212: `83596edca9389c78` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000242846`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (hex(hex(CURRENT_TIME))); SELECT *; SELECT hex(zeroblob(-2147483649));
```

---

## Crash 213: `0a88e058637bb7da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000247870`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT DEFAULT -48.011474307224029347126077151413273242907525709653992119594190629642371441767832069786680324544556357744844963882365933e+93277660798923630063731151030619
```

---

## Crash 214: `68144cd2ca09494f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000252976`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c3 BOOLEAN); CREATE TABLE
```

---

## Crash 215: `85d84d61295b964e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253244`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c
```

---

## Crash 216: `aa10e91f1a8fb95e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253351`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 INTEGER, a GENERATED A
```

---

## Crash 217: `058d7228fbfb94fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000253728`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b
```

---

## Crash 218: `e1c60795f6049a31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255098`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c
```

---

## Crash 219: `b877aed14c846d6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255898`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b FLOAT, c1 GENERATED ALW
```

---

## Crash 220: `b172940030b5187f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256059`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a BOOLEAN); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT IN
```

---

## Crash 221: `d38331c450ced7cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257214`

```sql
CREATE TABLE IF NOT EXISTS p(b VARCHAR(255)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p WHERE changes() FILTER (WHERE CURRENT_TIME) OVER (ORDER BY TRUE DESC ROWS BETWEEN CURRENT_TIME PRECEDING A
```

---

## Crash 222: `0d5ff3a806734b42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258296`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c3 DATE, a GENERATED ALWAY
```

---

## Crash 223: `051ec4a81625b431` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258321`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE); CREATE TABLE IF NOT EXISTS p(c3 DATE); SELECT * FROM p 
```

---

## Crash 224: `20a8b7588b2cdd0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260614`

```sql
SELECT printf('%.*s', 0, -0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR REPLACE INTO q VALUES (-NULL ISNULL NOT IN (typeof(RAISE(IGNORE) = FALSE IS NULL IS NOT CURRENT_DATE 
```

---

## Crash 225: `174b89b5828d07cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000273715`

```sql
SELECT printf('%.*s', 2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO t1 VALUES (trim(RAISE(IGNORE) COLLATE NOCASE) NOT IN (SELECT * LIMIT NOT NULL -> FALSE 
```

---

## Crash 226: `5643c24eb5e98962` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000278599`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE, c1 VARCHAR(255) UNIQUE); WITH RECURSIVE t3 (c1, rowid) AS (SELECT DISTINCT * FROM p NATURAL JOIN p AS vw4_e_7_n1_8_21_p___m__mi2r_0i34txah_k40kty5_048gjpt_
```

---

## Crash 227: `a35a21db6d8ac015` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279635`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid REAL NOT NULL DEFAULT CURRENT_TIME); INSERT INTO q VALUES (CURRENT_TIME) UNION VALUES (FALSE); PRAGMA quick_check;
```

---

## Crash 228: `49d2e58abaa559f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000279835`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q SELECT ALL * FROM q NOT INDEXED LIMIT FALSE; PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 229: `0f6c038a105c3ec4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280157`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIME) UNION SELECT * FROM p; PRAGMA quick_check; CREATE VIRTUAL TABLE
```

---

## Crash 230: `2b41ac03d942484f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280303`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 INT PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIME) UNION VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE 
```

---

## Crash 231: `b06163796071e181` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280725`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NATURAL LEFT JOIN p
```

---

## Crash 232: `62043a227636a818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000280860`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c1 GENERATED ALWAYS AS (a * a) NOT NULL UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_TIME); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p WHERE CURRENT_DATE;
```

---

## Crash 233: `f01b610ae5bd6b84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000284411`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB NOT NULL DEFAULT X'Cd8dae'); CREATE VIEW IF NOT EXISTS v1 AS SELECT TRUE % TRUE - CURRENT_TIMESTAMP IS NULL || CURRENT_DATE AS a_l_w_77_257_ea5__3h_8p_73ve0_t_01280
```

---
