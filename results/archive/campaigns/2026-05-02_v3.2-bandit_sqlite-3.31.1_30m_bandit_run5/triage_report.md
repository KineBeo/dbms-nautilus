# Crash Triage Report

**Total crashes:** 210  
**Unique crash sites:** 210  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 210 | 210 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `d97906b4988ca0ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000012`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE t1 AS MATERIALIZED (SELECT * ORDER BY CURRENT_DATE DESC) INSERT INTO t2 VALUES (upper(TRUE) / (RAISE(IGNORE)) NOT BETWEEN NULL 
```

---

## Crash 2: `f8307e0601253eed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000210`

```sql
SELECT printf('%.*s', 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO t2 DEFAULT VALUES; SELECT DISTINCT CURRENT_TIME COLLATE BINARY AS a FROM (p AS h_) CROS
```

---

## Crash 3: `828780cda8d9cc50` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000406`

```sql
SELECT substr('F -910_--3L S  ', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t3 VALUES (CURRENT_TIMESTAMP); VALUES (FALSE) UNION ALL SELECT * ORDER BY TRUE ->> 
```

---

## Crash 4: `e590cc20ad5e1e8f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000968`

```sql
SELECT round(1e308, 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p VALUES (zeroblob(CURRENT_DATE) >= NULL >> CURRENT_DATE ISNULL % CURRENT_TIMESTAMP / CURRENT_TIME
```

---

## Crash 5: `acc80a0778db5fdd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000974`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, b); SELECT q.*, p.*, CURRENT_TIME REGEXP RAISE(IGNORE) LIKE NULL ESCAPE CURRENT_TIMESTAMP + CASE CASE WHEN NULL + FALSE THEN ~CURRENT_TIME =
```

---

## Crash 6: `0331f002d58d1c52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001535`

```sql
SELECT substr('b-62 N-9', 4294967296); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR IGNORE INTO p VALUES (CURRENT_DATE COLLATE BINARY, CURRENT_TIME GLOB RAISE(IGNORE) - CURRENT_T
```

---

## Crash 7: `c09118b7444d6451` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001679`

```sql
SELECT printf('%.*g', -1, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(rowid DATE, c3 DATE GENE
```

---

## Crash 8: `2fafe21a907304df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001861`

```sql
SELECT hex(zeroblob(0)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); SELECT hex(zeroblob(2147483647));
```

---

## Crash 9: `778f5c3c8c07caae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002553`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); REPLACE INTO p VALUES (FALSE); VALUES (TRUE); CREATE TABLE IF NOT EXISTS p(a DATE GENERATED ALWAYS
```

---

## Crash 10: `ebdf4f59bdd073f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002562`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (FALSE); VALUES (TRUE); CREATE VIRTUAL TAB
```

---

## Crash 11: `257768b666cc051e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002634`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE VIRTUAL TABL
```

---

## Crash 12: `0ad7ce8bddad751e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002964`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT * FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; PRAGMA integri
```

---

## Crash 13: `8383cd9f875a1d94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002977`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check;
```

---

## Crash 14: `6ecea2905fc6ac1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006717`

```sql
SELECT printf('%d', -2147483648, '-q_-- By0 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE) ORDER BY NOT TRUE MATCH CURRENT
```

---

## Crash 15: `b1fe2dd27acb3fc4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006730`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT INTO q DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (FALSE) ORDER BY NOT TRUE MATCH CURRENT_TIME BETWEEN -CURRENT_
```

---

## Crash 16: `d9deca0fc729b3ab` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007374`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT (CASE CURRENT_TIMESTAMP COLLATE NOCASE & FALSE NOT NULL COLLATE BINARY WHEN (RAISE(IGN
```

---

## Crash 17: `a65bacd2cc804b1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007523`

```sql
SELECT printf('%f', 2147483648, '_ 5 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); INSERT INTO q DEFAULT VALUES; VALUES (FALSE) LIMIT FALSE ISNULL; CREATE TABLE IF NOT EXISTS p(ro
```

---

## Crash 18: `d21e3219bec45c01` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007741`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2, c1, _rowid_); SELECT * FROM (SELECT CURRENT_DATE FROM r WHERE CURRENT_TIME NOT IN (VALUES (FALSE IS NOT NULL)) NOT IN (SELECT ALL CURRENT_T
```

---

## Crash 19: `2ca8a867c91b4c5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007893`

```sql
SELECT printf('%.*f', -9223372036854775808, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b); INSERT OR ABORT INTO p VALUES (b -> RAISE(IGNORE) ISNULL, NULL); SELECT ~total_changes()
```

---

## Crash 20: `7bf215a0c0bc7a99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008032`

```sql
SELECT substr('', 1, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT RAISE(IGNORE) >= RAISE(IGNORE) >> NOT CURRENT_DATE ->> ~RAISE(IGNORE) -> TRUE > CURRENT_DATE FROM p W
```

---

## Crash 21: `ed7027e137da9639` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008148`

```sql
SELECT substr('J---Q ', 9223372036854775807, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO r VALUES (CASE CURRENT_TIMESTAMP NOT NULL WHEN +TRUE THEN CURRE
```

---

## Crash 22: `aa1aa9a6a232a335` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008220`

```sql
SELECT printf('%.*s', -9223372036854775808, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2); SELECT NOT EXISTS (SELECT *) OR CURRENT_TIMESTAMP AS s__218_68_b2t__f____3, NULL AS a, RA
```

---

## Crash 23: `8d0c527878df54ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008251`

```sql
SELECT printf('%.*f', -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c3); SELECT * FROM t2 INDEXED BY b GROUP BY CURRENT_TIME & FALSE COLLATE NOCASE REGEXP NOT RAISE(IGNORE) REG
```

---

## Crash 24: `b020447b1d8bc1ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015459`

```sql
SELECT round(0.01, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c2, b); INSERT INTO q VALUES (CURRENT_TIMESTAMP COLLATE RTRIM) RETURNING *, *; EXPLAIN QUERY PLAN WITH p (c1) AS
```

---

## Crash 25: `56f6ee81ada32acd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015531`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 26: `1dcc85cfb180ab7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015841`

```sql
SELECT hex(zeroblob(-1)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT V
```

---

## Crash 27: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016483`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 28: `5bc48592066a15d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016680`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, b); VALUES (CURRENT_TIME);
```

---

## Crash 29: `ba5e06392fd53600` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016694`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, b); VALUES (CURRENT_TIME);
```

---

## Crash 30: `e52a28bf759b26ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016704`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, _rowid_); VALUES (CURRENT_TIME);
```

---

## Crash 31: `db5dcb68ccc3c6e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017420`

```sql
SELECT printf('%.*d', -1, 0.01); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 32: `66a17f78f97afc4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017572`

```sql
SELECT printf('%llu', -2147483648, 'FS1OL'); SELECT printf('%.*e', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c1); SELECT * FROM t2 JOIN q ob___e66_04_k7k___a_4_mcv
```

---

## Crash 33: `a01a46747a0de9e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018400`

```sql
SELECT printf('%.*f', 2147483647, -1e308); SELECT hex(zeroblob(-2147483649));
```

---

## Crash 34: `99b65876c787a017` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018480`

```sql
SELECT printf('%.*f', 4294967296, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); SELECT p.*, -random() FILTER (WHERE (CURRENT_DATE)) OVER () AND CURRENT_TIME AS a FROM q NATURA
```

---

## Crash 35: `c8441ea0c24ad5cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000018784`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (VALUES (CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 36: `ebe87a4a2f449fa6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025578`

```sql
SELECT round(-1.0, -2147483648); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES (count(DISTINCT (EXISTS (SELECT * LIMIT CURRENT_TIME IS NOT CURRENT_TIMESTAMP)) 
```

---

## Crash 37: `53dae09806735242` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026068`

```sql
SELECT round(-1e308, 0); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 38: `150e90f750088769` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026556`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME; SELECT printf
```

---

## Crash 39: `d56f80dd1070ea45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000027343`

```sql
SELECT printf('%.*s', 1, -1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 40: `9fb02634e1bd20cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029045`

```sql
SELECT round(-0.0, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a, c1, _rowid_, c3, c1, b); REPLACE INTO p VALUES (CURRENT_TIMESTAMP + FALSE || CURRENT_TIME ISNULL IS NO
```

---

## Crash 41: `0dfffe3f9c3d9c1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030004`

```sql
SELECT printf('%.*d', 2147483647, 1e308); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 42: `f7a1fb9e1088bf08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032942`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INSERT INTO r DEFAULT VALUES; 
```

---

## Crash 43: `86c8c749e2677d85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034033`

```sql
SELECT printf('%.*d', -2147483648, -1e308); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 44: `a4e54f45e140f8a2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039219`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT CURRENT_DATE IS NOT NULL OFFSET FALSE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 45: `c346402314b438e5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040113`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (FALSE); SELECT * FROM p LIMIT +FALSE OFFSET CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 46: `6eac310338b5557a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044134`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB, c2 GENERATED ALWAYS AS (a) ); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); WITH RECURSIVE t
```

---

## Crash 47: `b7c81e10c7d05d84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045586`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, b GENERATED ALWAYS AS (a || b) NOT NULL, c3 DATE UNIQUE); VALUES (TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); SELECT group_concat(CURRENT_TIME 
```

---

## Crash 48: `4e1cf05b11e10b11` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046248`

```sql
SELECT substr('', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ABORT INTO p VALUES (avg(iif(TRUE, count(*), CURRENT_TIME) OVER (ORDER BY RAISE(IGNORE) COLLATE NOCASE DESC N
```

---

## Crash 49: `6bcf48392d3278cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048535`

```sql
SELECT round(-1.0, 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR ROLLBACK INTO p VALUES (EXISTS (SELECT *, * UNION SELECT CURRENT_DATE IS NOT DISTINCT FROM RAISE(IGN
```

---

## Crash 50: `6534fff005a0dff6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049176`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, c2 GENERATED ALWAYS AS (a * a) NOT NULL, a VARCHAR(255) DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 51: `b1a3db07a6791ed4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049583`

```sql
CREATE TABLE IF NOT EXISTS p(c2 TEXT NOT NULL); INSERT OR ROLLBACK INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, b, c1); INSERT OR FAIL INTO t3
```

---

## Crash 52: `b0f3bf26d1b536e3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049915`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 53: `cb5266c8712e82e8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000050112`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 54: `b311d5423799002b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058957`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT json_array(CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR ABORT INTO p VALUES (typeof(CURRENT_TIMESTAMP / 
```

---

## Crash 55: `83f238fe1c16378d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059173`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT json_array(NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; E
```

---

## Crash 56: `c0e11fa9b9bb82d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059373`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT random(); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO p VALUES (CURRENT_TIMESTAMP) ON CONFLICT DO NOTHING; EXPLAIN Q
```

---

## Crash 57: `ae3cbff566db80aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060120`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (min(TRUE)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 58: `d4e9a9db6598c539` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060355`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (count(*)); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 59: `34b869e4a62fdd45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060456`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p AS dkn_jbbk NATURAL JOIN p NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE IF 
```

---

## Crash 60: `57598cc0a4a23b70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060919`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT FALSE ORDER BY FALSE DESC NULLS LAST LIMIT FALSE; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 61: `d61042bab434292f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061632`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); SELECT * FROM p LIMIT CURRENT_DATE + TRUE OFFSET FALSE; CREATE VIRT
```

---

## Crash 62: `bd993d5ad721308c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061860`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT CURRENT_DATE + zeroblob(CURRENT_TIMESTAMP) OFFSET FALSE; CREATE VIRTU
```

---

## Crash 63: `75400ea77a419c92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061959`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT CURRENT_DATE + changes() OFFSET FALSE; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 64: `ab3d9e0493893feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062054`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT CURRENT_DATE + -CURRENT_TIME OFFSET FALSE; CREATE VIRTUAL TABLE IF NO
```

---

## Crash 65: `096be5c92016c13c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063073`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (json_type(FALSE)) VIRTUAL, a DATE UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 66: `74efcc8c6b1a2895` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063298`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, a DATE UNIQUE); SELECT * FROM p JOIN p a ON CURRENT_DATE; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 67: `44a01c19ef853ae5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063455`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> CURRENT_DATE ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3, a);
```

---

## Crash 68: `053399abf8d71203` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063516`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT TRUE FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c3, a); SELECT t3.* FROM t3 WHERE EXIS
```

---

## Crash 69: `3b88385e2b0515eb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063699`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> CURRENT_TIME ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_); SELEC
```

---

## Crash 70: `8b84733adeda9058` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000063942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> 'w-0_  g-J - 2' ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3); INS
```

---

## Crash 71: `09c01d63690bf853` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065312`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (FALSE >= FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 72: `7e16d784183d483f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065501`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (FALSE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 73: `f1465b4e57e3a01d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065507`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 74: `194e3dba3dd2c74e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067238`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b BLOB GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE V
```

---

## Crash 75: `47bd547549df1b92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072040`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP NOT BETWEEN CAST(TRUE AS DATE) AND NULL; CREA
```

---

## Crash 76: `116f29da8859c04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072356`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB TRUE COLLATE BINARY; CREATE VIRTUAL TABLE IF 
```

---

## Crash 77: `a927c42118ecb7bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072612`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE COLLATE BINARY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 78: `84f47d0d5d55120e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073266`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (TRUE) VIRTUAL, a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL
```

---

## Crash 79: `4d358637573290c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074077`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 80: `94460a245c5135b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074581`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON CURRENT_TIMESTAMP LIKE FALSE ESC
```

---

## Crash 81: `1100f3fc36d0a6dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074853`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT CURRENT_TIMESTAMP LIKE FALSE ESCAPE NULL AS vom8_26_1_5n6_8hk019d____ca FROM q NATURAL JOIN p
```

---

## Crash 82: `ca4d04a9d0b1eafe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083582`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM p JOIN q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME; CREATE
```

---

## Crash 83: `8eddc951cfbb660b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000083979`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (FALSE)) AS a GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 84: `836cb6c3558d6113` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084590`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED NATURAL JOIN p NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT 
```

---

## Crash 85: `a188057f08983f64` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000084899`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB NOT NULL, c2 TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT * FROM q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT C
```

---

## Crash 86: `9b6625658e8af2f5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085201`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT *, * FROM q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME; CREATE VIR
```

---

## Crash 87: `43f8439831a31a1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085321`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 88: `3f525c04b4ebbc16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000103424`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); SELECT * FROM q WHERE EXISTS (SELECT FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT 
```

---

## Crash 89: `1f72527246ab9ff0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106973`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a * a) UNIQUE); SELECT CASE WHEN CURRENT_TIME IN (NULL) THEN NULL END AS a, * FROM p JOIN p x9_ ON CURRENT_DATE; SELECT printf('%.*g'
```

---

## Crash 90: `6488866720fa9d0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108268`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT
```

---

## Crash 91: `511d1563f552b462` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108568`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE q; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 92: `d66ce95cfc02abfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000108888`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 93: `173b430e46235fe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112211`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE) EXCEPT SELECT FALSE ORDER BY FALSE DESC NULLS LAST LIMIT FAL
```

---

## Crash 94: `c7f818234e75222a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113137`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (FALSE); SELECT printf('%.*f', 214
```

---

## Crash 95: `fffb254653b75d42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000123217`

```sql
SELECT printf('%.*f', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO q VALUES (~length(CAST(FALSE <= RAISE(IGNORE) AS FLOAT) < ~NULL > RAISE(IGNORE) GLOB
```

---

## Crash 96: `67a87c5fd7e64ea4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000133978`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP) EXCEPT VALUES (FALSE) UNION ALL SELECT * FROM q 
```

---

## Crash 97: `efc63013452242ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134149`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-1)); CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUE
```

---

## Crash 98: `830253a3fc5feb0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134992`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE) INTERSECT SELECT FALSE ORDER BY FALSE DESC NULLS LAST LIMIT 
```

---

## Crash 99: `90f725a5b7771474` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135555`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE) UNION ALL SELECT FALSE ORDER BY FALSE DESC NULLS LAST LIMIT 
```

---

## Crash 100: `d59e7cd5dec706ff` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135766`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; VALUES (FALSE) EXCEPT SELECT FALSE ORDER BY FALSE DESC NULLS LAST LIMIT TRU
```

---

## Crash 101: `838fac52614a85a9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136201`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM r LEFT JOIN q USING (rowid, _rowid_) WHERE NULL; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 102: `9120557f9a76a1fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138490`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL NOT NULL DEFAULT 444021); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 103: `2644e8879a6a6f18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138635`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ REAL NOT NULL DEFAULT TRUE); INSERT INTO q DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 104: `0be6d2935ccdda42` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138787`

```sql
SELECT printf('%.*d', -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p (c2) VALUES (RAISE(IGNORE) NOTNULL * RAISE(IGNORE) GLOB FALSE) ON CONFLICT(b) DO UPDATE SET c1 = ~CASE
```

---

## Crash 105: `d57b0e76cfabd427` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139000`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q VALUES (CURRENT_TIMESTAMP) UNION VALUES (NULL); ANALYZE q; CREATE VIRT
```

---

## Crash 106: `efbbb995d51275d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000139104`

```sql
CREATE TABLE IF NOT EXISTS p(rowid VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; SELECT hex(zeroblob(1)); SELEC
```

---

## Crash 107: `0e4002379ec0387d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140002`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a + 72) UNIQUE); SELECT * FROM p JOIN p x9_ ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q 
```

---

## Crash 108: `4e8ea38224061074` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140130`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a * a) UNIQUE); SELECT * FROM p JOIN p x9_ ON CURRENT_TIME > FALSE COLLATE BINARY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 109: `4c9e9adddcac6915` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140255`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a * a) UNIQUE); SELECT * FROM p JOIN p x9_ ON CURRENT_TIME > CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 110: `d2a539e5ea3a9cad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000140299`

```sql
CREATE TABLE IF NOT EXISTS p(a BOOLEAN, rowid GENERATED ALWAYS AS (a * a) UNIQUE); SELECT sum(CURRENT_TIMESTAMP) FILTER (WHERE NULL) AS z2_6d_c50_76j, * FROM p JOIN p x9_ ON CURRENT_DATE; SELECT print
```

---

## Crash 111: `de6c8523b0ca71c8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000142762`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT PRIMARY KEY, a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC UNIQUE); EXPLAIN QUERY PLAN VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 112: `8fe464dfbcd24ada` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000167408`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY CURRENT_DATE WINDOW w1 AS () ORD
```

---

## Crash 113: `519ee223c5904396` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168135`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM (SELECT * FROM (SELECT * FROM p ORDER BY NULL ASC NULLS FIRST) AS v_dx_h2e
```

---

## Crash 114: `21afc15a5f14da1b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168268`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM (SELECT * FROM (VALUES (FALSE)) AS v_dx_h2e_l_29_7t8n9_5_76bv409_6_7__57_s
```

---

## Crash 115: `579d396ce9b9cff0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000168630`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM q WHERE NOT EXISTS (SELECT * FROM q WHERE FALSE GROUP BY TRUE HAVING CURRE
```

---

## Crash 116: `5ba5ad3acad6654f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169426`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM p LEFT JOIN q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME; C
```

---

## Crash 117: `547e19933b672961` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169580`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM p NATURAL JOIN q NOT INDEXED GROUP BY CURRENT_TIMESTAMP LIMIT CURRENT_TIME
```

---

## Crash 118: `1e55a27d37ebf3a8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000177151`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM r NOT INDEXED GROUP BY RAISE(IGNORE) HAVING CURRENT_DATE LIMIT CURRENT_TIMESTAMP; VALUES (CURRENT_TIM
```

---

## Crash 119: `713114e83c5d3e67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000178434`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER); CREATE TABLE IF NOT EXISTS q(c1 TEXT UNIQUE); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); 
```

---

## Crash 120: `4be6cb51a05ef0e2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179614`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON CURRENT_TIMESTAMP LIKE FALSE ESC
```

---

## Crash 121: `34023938fee253f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000179749`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM q ORDER BY RAISE(IGNORE) ASC LIMIT CURRENT_TIME) AS vom8_26_1_5n6_8
```

---

## Crash 122: `4e2e033e9740cc37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180037`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON CURRENT_DATE NOTNULL ORDER BY FA
```

---

## Crash 123: `86d0bf2162ac5463` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180380`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON CURRENT_DATE NOTNULL OR NULL ORD
```

---

## Crash 124: `fcb54d8b52544153` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000180570`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT CURRENT_TIME OR NULL OR NULL AS vom8_26_1_5n6_8hk019d____ca FROM q NATURAL JOIN p WHERE TRUE;
```

---

## Crash 125: `952cebd6b02acda9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181210`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 REAL CHECK (CURRENT_TIMESTAMP), _rowid_ TEXT); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABL
```

---

## Crash 126: `8da9fc73f000ce2b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181315`

```sql
SELECT printf('%x', 0, 'e_cX'); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t1 (c2, a, c2) VALUES ((VALUES (CURRENT_TIMESTAMP NOT LIKE NOT (VALUES (CURRENT_TIMESTAMP ISNULL))
```

---

## Crash 127: `c30882364f411d06` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181352`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 BLOB NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 128: `4340fdcd4ead5e98` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000181469`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE FALSE COLLATE RTRIM > CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 129: `2f33a232354c6f9f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000182692`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a)
```

---

## Crash 130: `46bbf45cec210085` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183436`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB zeroblob(CURRENT_TIMESTAMP); CREATE VIRTUAL T
```

---

## Crash 131: `e74724ddddaff100` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183520`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB random(); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 132: `c928b6bf6f95e6ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000183590`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT sum(CURRENT_TIMESTAMP) FILTER (WHERE NULL) AS z2_6d_c50_76j, * FROM q NATURAL JOIN p WHERE NU
```

---

## Crash 133: `46a16a306883f75e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184120`

```sql
CREATE TABLE IF NOT EXISTS p(b TEXT GENERATED ALWAYS AS (FALSE) VIRTUAL, a DATE UNIQUE); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME; SELECT prin
```

---

## Crash 134: `8819492a1ab6dd40` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184289`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CAST(CURRENT_TIMESTAMP AS DATE); SELECT printf('%.*f', 21474836
```

---

## Crash 135: `5c98d0989c638bf6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184481`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CAST(TRUE AS INTEGER); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 136: `0f224ab949f3ec66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000184679`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIMESTAMP NOT BETWEEN FALSE AND CURRENT_TIMESTAMP NOT B
```

---

## Crash 137: `a10e7501bb4f5415` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187351`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b BLOB GENERATED ALWAYS AS (+TRUE) STORED); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE V
```

---

## Crash 138: `bbb7377fb2b4311c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000187540`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL, c3 GENERATED ALWAYS AS (coalesce(a, b)) NOT NULL UNIQUE, b BLOB GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE 
```

---

## Crash 139: `4e9246b3415dcfe9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191103`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (CURRENT_TIMESTAMP) UNION VALUES (NULL) EXCEPT VALUES (NULL); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 140: `30016149fffc8cbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191454`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (0.0); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 141: `d6335f3accd74138` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000191706`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (TRUE) EXCEPT VALUES (0.0 >= FALSE); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 142: `6b767647b8513244` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193262`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); WITH t2 AS (SELECT *) INSERT INTO p VALUES (CURRENT_TIME != FALSE >= CURRENT_DATE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 143: `7db80be0166195f7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000193725`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> '- M1-CE-K  5j- - -i' ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); I
```

---

## Crash 144: `bde7b0cafe47802b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> -4060688.60 ISNULL FROM p JOIN p a ON CURRENT_DATE; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 145: `26201763c204b651` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194302`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT TRUE - FALSE ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO p VALUES (TRU
```

---

## Crash 146: `3e077ff94d0becd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000194737`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT ~NULL >> CURRENT_DATE FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q DEFAULT VA
```

---

## Crash 147: `29143f380b251347` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000195588`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c2); VALUES (NULL) UNION ALL VALUES (CASE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP END); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 148: `fa88ed2a8dc9551c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000196948`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIMESTAMP ORDE
```

---

## Crash 149: `800fd64c9c8f47d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197078`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (PARTITION BY CURRENT_TIMESTAMP, FAL
```

---

## Crash 150: `b519237dc95cd9df` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197504`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), count(*) FILTER (WHERE CURRENT_T
```

---

## Crash 151: `272cf63b88090680` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000197956`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT TRUE + -CURRENT_TIME OFFSET FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 152: `b39e5f2fd2fc7bd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198409`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (CURRENT_DATE << CURRENT_TIME); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP)
```

---

## Crash 153: `1b3a8684fca0523b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000198642`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (NULL); EXPLAIN QUERY PLAN VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE I
```

---

## Crash 154: `b075436bae2b030e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199214`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT X'FAAdAF6aaC7Bce'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 155: `9f0536a3b3e96a0c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000199897`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255), rowid GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p AS dkn_jbbk NATURAL JOIN p NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABL
```

---

## Crash 156: `52c0ccc103a8aa71` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200371`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (min(CURRENT_DATE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSER
```

---

## Crash 157: `ebab460e3a2bfa29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000200675`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (FALSE); SELECT * FROM p LIMIT '103'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 158: `805d27cf35437b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201220`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM p NOT INDEXED LEFT OUTER JOIN q ON NULL; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT +FALSE OFFSET CURRENT_DA
```

---

## Crash 159: `c099d32efbc80b2f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000201539`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED NATURAL LEFT JOIN p NOT INDEXED LIMIT TRUE; CREATE VIR
```

---

## Crash 160: `0e1222f85d13ea4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202086`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT json_array(CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c2 FLOAT, rowid GENERATED ALWAYS AS (a) NOT NULL UNIQUE); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 161: `589e20b89f1a69f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000202711`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT json_array(count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT INTO q 
```

---

## Crash 162: `5cb5fbaa05eef877` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203821`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT CURRENT_TIME LIKE FALSE ESCAPE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); REPLACE INTO t3 VALUES (CASE WHEN min(RAISE(IGN
```

---

## Crash 163: `88e040aa290875b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000203987`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT randomblob(CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 164: `c37539f2ec524b57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000204784`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC DEFAULT ' 52g'); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (FALSE); SELECT * FROM p LIMIT 0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1
```

---

## Crash 165: `c3ff5b9d31bd30cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205204`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL); REPLACE INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a REAL UNIQUE); CREATE VI
```

---

## Crash 166: `3adbcf00f8b48f84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000205736`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED WHERE FALSE; CREATE VIRTUAL TA
```

---

## Crash 167: `688aa82ffe4a5159` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000212547`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a) NOT NULL); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 168: `e8b85a966ed78af6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000213837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC
```

---

## Crash 169: `e783116aae18ca08` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214042`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (random()); PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 170: `cc7fd977f27288f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214222`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CR
```

---

## Crash 171: `a5ee769685fa556b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000214251`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CR
```

---

## Crash 172: `818c6c4d7d19268d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000215831`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, c2 GENERATED ALWAYS AS (a * a) NOT NULL, a VARCHAR(255) DEFAULT 672179182237537746024884390676597928987514574489908984550125634043110280090780866153838540806277852
```

---

## Crash 173: `f1d1408bbc88e258` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224341`

```sql
CREATE TABLE IF NOT EXISTS p(b REAL, c2 GENERATED ALWAYS AS (a + 72) NOT NULL, a REAL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; VALUES (FALSE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 174: `089dc7a42193ecf1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224705`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) GENERAT
```

---

## Crash 175: `fb9df474aab352fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224733`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAU
```

---

## Crash 176: `c329ffa7cad69693` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000224855`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c1); REPLACE INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE, c1 GENERATED A
```

---

## Crash 177: `ca7cc9393971c92d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000233051`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER PRIMARY KEY); REPLACE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM p NOT INDEXED WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 178: `5d77dd28e2d9f502` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235133`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB PRIMARY KEY); SELECT json_array(TRUE, CURRENT_DATE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_TIME, CURRENT_TIME, CURREN
```

---

## Crash 179: `cfa34892edffc079` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235515`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT json_array(FALSE, TRUE, CURRENT_DATE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, NULL, CURRENT_TIMESTAMP, CURRENT_DATE, CURRENT_TIME, CURRENT
```

---

## Crash 180: `201e16d8f23a6c7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000235651`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); SELECT json_array(FALSE, TRUE, CURRENT_DATE, CURRENT_TIMESTAMP, CURRENT_DATE); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 181: `5a4bc5585123c987` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236322`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(b); SELECT json_array(-1688045444447581720152074671577628765985164021741825562144162432256.4); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 182: `4966f502e5edfebf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000236517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 DATE); INSERT INTO p SELECT ALL * FROM p LIMIT TRUE; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 183: `c29bfbb09447bda4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238748`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; SELECT * FROM p LIMIT 444021; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INS
```

---

## Crash 184: `71d29604679a6928` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000238922`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (min(NULL COLLATE NOCASE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 185: `8140fc877bff6c13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239377`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, _rowid_ BOOLEAN NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p NOT INDEXED LIMIT TRUE; CR
```

---

## Crash 186: `cbf07c8c32f52266` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000239496`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY, _rowid_ BOOLEAN NOT NULL DEFAULT TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p NOT INDEXED LIMIT TRUE; CREATE VIRTUAL TABLE I
```

---

## Crash 187: `89ca6f157aa168aa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240300`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (randomblob(CURRENT_DATE)); VALUES (CURRENT_TIME); CREATE VIR
```

---

## Crash 188: `442f859ff5bc2d87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240509`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (randomblob(CURRENT_DATE)); VALUES (CURRENT_TIME); CREATE TAB
```

---

## Crash 189: `015356cd1d06c22f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240620`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT C
```

---

## Crash 190: `fd310654fdc76dfe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240780`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VI
```

---

## Crash 191: `0ae2faf225b5af29` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000240835`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(c1 FLOAT UNIQUE); CREATE VI
```

---

## Crash 192: `52b68e6e65d3294f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241076`

```sql
CREATE TABLE IF NOT EXISTS p(a INT PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); SELECT hex(zeroblob(1)); SELECT hex(zeroblob(0)); CREATE
```

---

## Crash 193: `9483830f3e34b809` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000241379`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT NOT NULL DEFAULT X'FAAdAF6aaC7Bce'); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; REPLACE INTO p VALUES (randomblob(CURRENT_TIME * CURRENT_TIME * CURRENT_TIME * CURR
```

---

## Crash 194: `83d9dc0ea780d995` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243527`

```sql
CREATE TABLE IF NOT EXISTS p(a INT); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; VALUES (count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (ORDER BY TRUE DESC ROWS BETWEEN UNB
```

---

## Crash 195: `d0b9fd7eb0f4d551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000243888`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC); CREATE TABLE IF NOT EXISTS q(b REAL UNIQUE); VALUES (NULL) UNION ALL SELECT * FROM p WHERE CURRENT_DATE GROUP BY TRUE LIMIT -1025; CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 196: `86142ee326c49ad4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245538`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT count(*) FILTER (WHERE CURRENT_TIMESTAMP) OVER (), * FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 197: `3176df2772cbf6bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245759`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> X'' ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAUL
```

---

## Crash 198: `69926e65415944d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000245864`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) NOT NULL); SELECT CURRENT_TIME >> NULL ISNULL FROM p JOIN p a ON CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO q DEFAU
```

---

## Crash 199: `eb184096e4a1248c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255207`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT sum(CURRENT_TIMESTAMP) FILTER (WHERE NULL) AS z2_6d_c50_76j, sum(CURRENT_TIMESTAMP) FILTER (W
```

---

## Crash 200: `4dfea90a7d631bbe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255634`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB X'EC19a92D'; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 201: `aa1ec3ae6a082f70` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000255760`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE CURRENT_TIME GLOB NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 202: `6cd4ed8cbc2f606c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000256859`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (TRUE) VIRTUAL, a BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a VARCHAR(255) PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE NULL; SELEC
```

---

## Crash 203: `aa09fc6fd7c25296` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257058`

```sql
CREATE TABLE IF NOT EXISTS p(a INTEGER, c2 GENERATED ALWAYS AS (a IS NULL) NOT NULL UNIQUE, b TEXT NOT NULL); SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 204: `9ebc042c6964f053` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257265`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL GENERATED ALWAYS AS (TRUE) VIRTUAL, b INT NOT NULL, c1 REAL NOT NULL, rowid BOOLEAN NOT NULL); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM p NAT
```

---

## Crash 205: `705e3ed2be49e509` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000257998`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE c2 > CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 206: `5c3459c689588821` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000258169`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT * FROM q NATURAL JOIN p WHERE q.rowid > CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 207: `fc53acef7d81942a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000259837`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT NOT EXISTS (SELECT * FROM p NOT INDEXED LEFT OUTER JOIN (VALUES (TRUE)) AS a ON NULL ORDER BY
```

---

## Crash 208: `0c5c80d7eca359dd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000260835`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); SELECT CURRENT_TIMESTAMP LIKE FALSE ESCAPE count(*) AS vom8_26_1_5n6_8hk019d____ca FROM q NATURAL JO
```

---

## Crash 209: `b26b04e65e4eaa37` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000271162`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM (VALUES (FALSE) INTERSECT SELECT * FROM q NOT INDEXED) AS v_dx_h2e_l_29_7t
```

---

## Crash 210: `477927c6cd2bdb4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000271433`

```sql
CREATE TABLE IF NOT EXISTS p(a VARCHAR(255) NOT NULL); CREATE TABLE IF NOT EXISTS q(a BLOB); EXPLAIN QUERY PLAN SELECT * FROM (SELECT * FROM p NOT INDEXED NATURAL JOIN p NOT INDEXED) AS v_dx_h2e_l_29_
```

---
