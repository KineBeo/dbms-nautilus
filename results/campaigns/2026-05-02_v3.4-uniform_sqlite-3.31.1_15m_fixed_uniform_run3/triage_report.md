# Crash Triage Report

**Total crashes:** 116  
**Unique crash sites:** 116  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 116 | 116 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `c876212f0258706f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000146`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT * FROM p JOIN p psi0_n_0a9l_k25_j_ebklz_cm_9_1___8_k_jrc4q5j_j919ki9_x_3c8y_q_5257n3_2t_76_2_wk_9b_6_4wd9y6_l_4g ON ~CASE WHEN CASE WHE
```

---

## Crash 2: `7f1bdfffdd0e8f8c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000305`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1); SELECT (RAISE(IGNORE) < CURRENT_TIME > NULL NOT NULL) NOTNULL AS e_, ~NOT length(NOT +CURRENT_TIMESTAMP NOT NULL) FILTER (WHERE char(FALSE
```

---

## Crash 3: `47dee5159b1e1087` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000616`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); SELECT CURRENT_TIME NOT NULL IS NULL = CURRENT_TIME MATCH TRUE > CURRENT_DATE > RAISE(IGNORE) COLLATE BINARY IS NULL % NOT EXISTS (SELECT NULL 
```

---

## Crash 4: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000744`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 5: `8bb8fe97982ae1c5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001118`

```sql
SELECT substr('', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT p.*, (CURRENT_TIMESTAMP IS NULL) BETWEEN CURRENT_TIMESTAMP == CURRENT_DATE MATCH CAST(~group_concat(NULL
```

---

## Crash 6: `88cd06e7f2eba48c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001899`

```sql
SELECT hex(zeroblob(-2147483649)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE r (c2, c1, a) AS (SELECT TRUE NOTNULL OR CURRENT_TIMESTAMP & CURRENT_TIMESTAMP <> NULL COLLA
```

---

## Crash 7: `891817b68230eabb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002433`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIR
```

---

## Crash 8: `8dc7754b13a451e7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002472`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(rowid BLOB); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 9: `ab29a8427873c03f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002652`

```sql
CREATE TABLE IF NOT EXISTS p(c2 FLOAT); SELECT CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); REPLACE INTO s VALUES (t1.b <= CASE WHEN CURRENT_TIME ISNULL COLLATE RTRIM TH
```

---

## Crash 10: `6ec1fe0f1e4801fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002685`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT substr('3pxq_', 2147483648, -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 11: `3111786ac99b7ada` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002762`

```sql
SELECT printf('%u', 9223372036854775807, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q (c1) VALUES (length(RAISE(IGNORE) ISNULL REGEXP NULL) OVER (ORDER BY ~FALSE LIKE N
```

---

## Crash 12: `464d6e14deef1403` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003505`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a
```

---

## Crash 13: `fdad39998846f074` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003511`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 U
```

---

## Crash 14: `028b416120884bf8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003517`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 15: `8e49c79917330ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003763`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT OR ROLLBACK INTO q VALUES (CURRENT_TIME); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 16: `a65d8198f4d237f8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003775`

```sql
CREATE TABLE IF NOT EXISTS p(c3 REAL); CREATE TABLE IF NOT EXISTS q(c2 BLOB UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); SELECT 
```

---

## Crash 17: `1f7a88492151dc86` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004671`

```sql
SELECT hex(zeroblob(1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR FAIL INTO s VALUES ((count(*) OVER (PARTITION BY TRUE ORDER BY NULL * TRUE ASC GROUPS BETWEEN UNBOUNDED PRE
```

---

## Crash 18: `663bfe67b65b814d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005503`

```sql
SELECT substr('-3_ 8-U8Yf-A ', 2147483647); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); SELECT ~CURRENT_DATE - TRUE <> CASE WHEN NULL THEN CURRENT_DATE LIKE CURRENT_TIME ESCAPE CURRENT_T
```

---

## Crash 19: `a51659c4583346ec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006054`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 20: `e64c82e16597781c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007303`

```sql
SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 21: `164e7322aac53503` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000007845`

```sql
SELECT printf('%.*f', 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, a, c1); INSERT OR REPLACE INTO q VALUES (json_extract(NULL IS ~TRUE NOTNULL NOT IN (VALUES (CURRENT_TIME) LI
```

---

## Crash 22: `a399b17be55440d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009961`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c1, _rowid_, c2, c2); SELECT TRUE REGEXP TRUE <= CURRENT_TIMESTAMP COLLATE RTRIM IS -FALSE IS NOT NULL, q.* FROM p NATURAL JOIN t1 WHE
```

---

## Crash 23: `0748bc18a2faa1cc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011704`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQ
```

---

## Crash 24: `77d2e07152e49148` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011712`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQ
```

---

## Crash 25: `0a159f0e948ac303` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014325`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT TRUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXI
```

---

## Crash 26: `29bf34e7bcb01b93` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014736`

```sql
SELECT substr('  7 ', 2147483648, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO r VALUES (CURRENT_TIME COLLATE BINARY < FALSE COLLATE NOCASE == CURRENT_DAT
```

---

## Crash 27: `17d2e1383c41c401` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000014784`

```sql
SELECT hex(zeroblob(-1)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT OR FAIL INTO r VALUES (CURRENT_TIME COLLATE BINARY < FALSE COLLATE NOCASE == CURRENT_DATE NOTNULL REGEXP CASE 
```

---

## Crash 28: `850b31304c35da9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015393`

```sql
SELECT substr('_y-Ca', 9223372036854775807, 4294967296); SELECT printf('%.*g', 2147483647, 0.01); CREATE TABLE IF NOT EXISTS p(b TEXT, b GENERATED ALWAYS AS (a IS NULL) UNIQUE, c1 TEXT NOT NULL); INSE
```

---

## Crash 29: `fd5efe0df59809cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021829`

```sql
SELECT round(1e-308, -2147483649); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR FAIL INTO p VALUES ((VALUES (CURRENT_TIMESTAMP) UNION SELECT ALL * FROM p NOT INDEXED ORDER BY CU
```

---

## Crash 30: `25e2e7d4754613de` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000023443`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); WITH RECURSIVE q (row
```

---

## Crash 31: `a7e544ceeaf9b852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024154`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE GENERATED ALWAYS AS (FALSE) STORED, rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VI
```

---

## Crash 32: `b85d5dbef70bf059` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024567`

```sql
SELECT substr('r', 0, 4294967295); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1); INSERT INTO q VALUES (json(-RAISE(IGNORE)) OVER (ORDER BY CASE WHEN CURRENT_DATE IS NULL THEN +FALSE EN
```

---

## Crash 33: `def1e0b9f7a0faa8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025117`

```sql
SELECT printf('%f', 2147483648, ''); SELECT printf('%.*f', 2147483647, -1e308);
```

---

## Crash 34: `ec126cb9ac85bad6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028939`

```sql
SELECT printf('%.*s', 4294967295, -1e308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); WITH RECURSIVE s (c1, b) AS NOT MATERIALIZED (SELECT +CURRENT_TIMESTAMP >> (CURRENT_DATE) IS NOT DI
```

---

## Crash 35: `4bcb4cb05228ab87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028992`

```sql
SELECT printf('%.*g', -1, 1.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2); WITH p AS (VALUES (CURRENT_TIMESTAMP) ORDER BY CURRENT_TIMESTAMP REGEXP NULL << CURRENT_DATE IS DISTINCT F
```

---

## Crash 36: `debe59c75951417c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032226`

```sql
SELECT substr('_1y Bb', 0, 0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 37: `0cb3d8500b9a2fd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035515`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT CURRENT_DATE IS NULL <= CURRENT_TIME IS NOT NULL, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSE
```

---

## Crash 38: `c35046b0d4d60551` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035864`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT FALSE - CURRENT_TIMESTAMP || CURRENT_TIMESTAMP <= CURRENT_TIME IS NOT NULL, * FROM p; SELECT printf('%.*g', 2147483647, 0.
```

---

## Crash 39: `f216ee51f8bf55ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036245`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT TRUE <= FALSE <= CURRENT_TIME, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO q DEFAULT V
```

---

## Crash 40: `5cd24172e324976f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036382`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT +CURRENT_TIME <= FALSE <= NULL, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO
```

---

## Crash 41: `20fd09e21a4f8562` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037003`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT FALSE - CURRENT_TIMESTAMP || FALSE, * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 42: `7c6d160add06f012` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000037813`

```sql
SELECT printf('%.*g', 9223372036854775807, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; SELECT hex(zeroblob(2147483648)
```

---

## Crash 43: `7cbc14590e521073` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038516`

```sql
SELECT printf('%d', -2147483649, ''); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; SELECT hex(zeroblob(2147483648));
```

---

## Crash 44: `68db6ef2af7f5005` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039602`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL, c1 GENERATED ALWAYS AS (a + 0) , a REAL); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); I
```

---

## Crash 45: `cc013b770a3cffe5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040601`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER CHECK (CURRENT_TIMESTAMP), b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c1 REAL UNIQUE); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABL
```

---

## Crash 46: `89b542f38e5932c6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040939`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 47: `d82ffe13187b2dde` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041440`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER CHECK (FALSE NOT NULL), b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VI
```

---

## Crash 48: `d0e68d77a1babd55` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043286`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER CHECK (NULL), b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABL
```

---

## Crash 49: `a4c5f9d37a15e33b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043524`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER CHECK (CURRENT_TIME NOT IN (CURRENT_DATE)), b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integr
```

---

## Crash 50: `673fcde3e7aff846` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000046719`

```sql
SELECT printf('%.*e', 4294967295, 0.01); SELECT hex(zeroblob(-9223372036854775808)); SELECT printf('%.*g', 4294967295, 0.01); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); WITH RECURSIVE q
```

---

## Crash 51: `8668366ded0ea03b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047010`

```sql
SELECT printf('%.*f', -2147483648, 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT INTO p DEFAULT VALUES; SELECT p.*, +NULL * RAISE(IGNORE) LIKE (NULL GLOB CURRENT_TIME = RAISE(
```

---

## Crash 52: `5cc176350b9ec57f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048466`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); VALUES (abs(CASE WHEN RAISE(IGNORE) ->> CURRENT_TIMESTAMP THEN FALSE COLLATE BINARY GLOB TRUE ISN
```

---

## Crash 53: `6d13c0b215b0dd61` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049393`

```sql
SELECT printf('%x', -2147483648, ''); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 54: `01748e35e19fce81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057149`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BLOB NOT NULL DEFAULT X'5EC740bffF87dB', b BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; 
```

---

## Crash 55: `d9731c573072e2dc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057586`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INTEGER CHECK (NULL), b INT CHECK (CURRENT_DATE NOT IN (FALSE)), c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 DATE UNIQUE); INSERT INTO p DEFAULT VALUES;
```

---

## Crash 56: `c6748ba299960dc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057819`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT DEFAULT X'ED9C'); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 2147483647, -1
```

---

## Crash 57: `c40f0b5982f5c57b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057939`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ FLOAT DEFAULT CURRENT_TIME); CREATE TABLE IF NOT EXISTS q(a INT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; SELECT printf('%.*f', 214748364
```

---

## Crash 58: `da10ac07707aff21` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059792`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT X'Ed'); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 59: `fe44013400b8e6fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000059892`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c3); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_row
```

---

## Crash 60: `1261466f6bc4a3e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060896`

```sql
SELECT hex(zeroblob(-9223372036854775808)); SELECT hex(zeroblob(-2147483648)); SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) PRIMARY KEY); CREATE TABLE IF NOT EXISTS 
```

---

## Crash 61: `9459093202688dae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061973`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL, c1 GENERATED ALWAYS AS (a + 0) , a DATE GENERATED ALWAYS AS (FALSE) STORED); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 21
```

---

## Crash 62: `e9b60e5e3e874fe8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062374`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'ccFDBbA0'); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 63: `38384f7658178c4f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000064780`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT CURRENT_TIME NOT IN (VALUES (CURRENT_DATE) UNION ALL VALUES (FALSE)) FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 64: `7f3fd9f60c9fc80c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065273`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP), * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); INSERT OR RE
```

---

## Crash 65: `83cd5eb51cc6528f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066673`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT FALSE || FALSE - CURRENT_TIMESTAMP || CURRENT_TIMESTAMP <= CURRENT_TIMESTAMP, * FROM p; SELECT printf('%.*f', 2147483647, 
```

---

## Crash 66: `f599ca616b090210` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067570`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT count(*) AS n__5_c87504 FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3, b); SELECT CURRENT_TIME GLOB 
```

---

## Crash 67: `ba4e2ad84f368ce4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067689`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT NULL <= CURRENT_DATE IS NULL <= FALSE, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLA
```

---

## Crash 68: `663cdf6160b24ec7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067891`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); WITH RECURSIVE t3 AS (SELECT *) SELECT FALSE <= FALSE, * FROM p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT OR REPLACE INTO p VALUES (FALSE
```

---

## Crash 69: `04db69a53b22e698` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070688`

```sql
CREATE TABLE IF NOT EXISTS p(rowid REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE VIRT
```

---

## Crash 70: `23636ee1ddb67b75` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070784`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a INT
```

---

## Crash 71: `9c7dbca4406b5545` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070846`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(rowid
```

---

## Crash 72: `5ad42cff89cc5a0b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000070918`

```sql
CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (FALSE); PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c1 BO
```

---

## Crash 73: `b867f39a6f9bb4bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000071148`

```sql
SELECT hex(zeroblob(-2147483648)); CREATE TABLE IF NOT EXISTS p(c2 VARCHAR(255) UNIQUE); CREATE TABLE IF NOT EXISTS q(a FLOAT PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; SELECT hex
```

---

## Crash 74: `ebbf4619748a053c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072697`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT count(*) AS n__5_c87504 FROM p NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 75: `1fb493f2e5538b2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT count(*) AS n__5_c87504 FROM p NATURAL JOIN q WHERE NULL; SELECT printf('%.*f', -2147483649); CREATE
```

---

## Crash 76: `9c22bfa8a2a97529` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072942`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT json_valid(NULL) AS n__5_c87504 FROM p NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS
```

---

## Crash 77: `c45283e9d8558f38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073174`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 INT NOT NULL); SELECT json_valid(changes()) AS n__5_c87504 FROM p NATURAL JOIN q WHERE NULL; CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 78: `f701d367af15db5c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073812`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(a); WITH RECURSIVE p (a) AS (VALUES (TRUE) EXCEPT VALUES (CURRENT_TIMESTAMP)) SELECT * FROM p; SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 79: `ea2e6193643c5819` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074566`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 DATE PRIMARY KEY); SELECT * FROM p NATURAL JOIN q WHERE TRUE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 80: `ee50ddea66784ccf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000074970`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BLOB UNIQUE); SELECT * FROM p NATURAL JOIN q WHERE FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INS
```

---

## Crash 81: `aa5f263e35cba04e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075394`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CAST(TRUE AS BLOB); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 82: `6279c9b61a2253d3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000075577`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE I
```

---

## Crash 83: `a20a4478b0cbc6d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076078`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP IN (NULL IN (NULL)); CREATE VIRTUAL TABLE IF N
```

---

## Crash 84: `50a94e154b7f06d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076165`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP IN (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT
```

---

## Crash 85: `aac93e9c125dfda5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076442`

```sql
CREATE TABLE IF NOT EXISTS p(b INT CHECK (CURRENT_TIME), c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(b INTEGER NOT NULL); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; SELECT print
```

---

## Crash 86: `013a35b05866cb8e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000076850`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT NOT NULL); CREATE TABLE IF NOT EXISTS q(c3 BOOLEAN NOT NULL DEFAULT FALSE, a INT); SELECT * FROM p NATURAL JOIN q WHERE CURRENT_TIMESTAMP; CREATE VIRTUAL TABLE IF
```

---

## Crash 87: `21c5926df05dfae8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088179`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 NUMERIC PRIMARY KEY)
```

---

## Crash 88: `aa777a7a227be176` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088278`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); INSERT O
```

---

## Crash 89: `52a39d87d5bff46d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088493`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts3(c1); INSERT 
```

---

## Crash 90: `51131b79aacf01ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089024`

```sql
CREATE TABLE IF NOT EXISTS p(c3 BLOB NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIMESTAMP); INSERT INTO p (c3) VALUES (CURRENT_DATE) ON CONFLICT(_rowid_) DO UPDATE SET rowid = CURRENT_
```

---

## Crash 91: `13a0338b8bc79498` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000091869`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(b BOOLEAN); INSERT OR FAIL INTO p VALUES (FALSE); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 92: `c8600c75afc3db6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092015`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC); INSERT INTO p (c1) VALUES (CURRENT_TIME); PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USIN
```

---

## Crash 93: `4e448226ad470fac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092314`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL DEFAULT -8827.71); CREATE TABLE IF NOT EXISTS q(c3 TEXT PRIMARY KEY); INSERT INTO q DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF N
```

---

## Crash 94: `4d433da346fde595` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092431`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 VARCHAR(255) DEFAULT -7277499085503986919856635032046241653149650135528669990973739257652598341805369548515496890124374671
```

---

## Crash 95: `f89c85d7cf47510d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000092964`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); VALUES (last_insert_rowid()); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 96: `3fe1f304354d234e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000094599`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES (TRUE); VALUES (CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_
```

---

## Crash 97: `bb5522dd8e279fa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095448`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT OR FAIL INTO p VALUES ((VALUES (CURRENT_TIMESTAMP) UNION SELECT ALL * FROM p NOT INDEXED ORDER BY CURRENT_TIMEST
```

---

## Crash 98: `3c01a5f084af7b80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097538`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NOT INDEXED WHERE CURRENT_DATE GROUP BY CURRENT_TIME WINDOW w1 AS ()
```

---

## Crash 99: `2e9e5c3fe336f0e4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098156`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN NOT NULL IS NULL THEN CURRENT_TIME END); CREATE VIRTUAL TABLE IF N
```

---

## Crash 100: `e89255ee62f8511e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098365`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN CURRENT_TIME THEN CURRENT_TIME END); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 101: `447f5928b28c0bf4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000098371`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN TRUE IS NULL THEN CURRENT_TIME END); CREATE VIRTUAL TABLE IF NOT E
```

---

## Crash 102: `9676eb781a2652f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105593`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT 12.42892378581511915732452268223E+9903628909948626245335546396438887010328359292039800752834444884789433248734628611103387809361659053345944114); C
```

---

## Crash 103: `7a114a290dc9b9b2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000105618`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE, b BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF
```

---

## Crash 104: `f18a9617845732d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106024`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR FAIL INTO q VALUES (CURRENT_TIME BETWEEN CURRENT_TIME AND CURRENT_DATE); EXPLAIN QUERY PLAN VALUES
```

---

## Crash 105: `6fc3a2b26104ab76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106428`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR FAIL INTO q VALUES (FALSE != CURRENT_TIME GLOB FALSE BETWEEN CURRENT_DATE AND CURRENT_DATE); EXPLA
```

---

## Crash 106: `8980d2bceaa94350` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106586`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN); CREATE TABLE IF NOT EXISTS q(rowid INT NOT NULL); INSERT OR FAIL INTO q VALUES (CURRENT_TIMESTAMP BETWEEN CURRENT_DATE AND CURRENT_DATE); EXPLAIN QUERY PLAN V
```

---

## Crash 107: `e1d882aa4da1fb03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000106993`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INT NOT NULL DEFAULT ''); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_DATE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE VIRTUAL TABLE IF NOT EXIST
```

---

## Crash 108: `48d55619bdd8f512` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110642`

```sql
SELECT printf('%.*g', 4294967296); SELECT printf('%.*e', -2147483648, 0.01); SELECT printf('%.*d', -2147483648, 1e-308); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a); INSERT OR ROLLBACK INT
```

---

## Crash 109: `9189ebd412919c48` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113910`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (count(*) OVER (), CURRENT_TIMESTAMP); SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 110: `694e75e0ee7cb9a7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125972`

```sql
SELECT round(0.01, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT INTO t2 SELECT q.* ORDER BY -TRUE DESC NULLS LAST, NULL DESC NULLS LAST LIMIT FALSE OFFSET CURRENT_DATE LIKE c3
```

---

## Crash 111: `724d51d24001bf6d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000134071`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIME, CURRENT_TIMESTAMP) UNION SELECT ALL * FROM p NOT INDEXED ORDER BY CURREN
```

---

## Crash 112: `c115a61ca3d12d7e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135335`

```sql
SELECT printf('%.*d', -2147483648, -1e308); SELECT printf('%.*f', -2147483649, -1e308); CREATE TABLE IF NOT EXISTS p(c2 INT, c3 GENERATED ALWAYS AS (a = -0) NOT NULL UNIQUE, a DATE); SELECT t2.*, avg(
```

---

## Crash 113: `8531e69dfac09cd8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136402`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; SELECT * FROM p NATURAL JOIN p WHERE NULL; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts
```

---

## Crash 114: `699e07bc9e39187c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000136495`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c2 GENERATED ALWAYS AS (a) UNIQUE); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (CURRENT_DATE); CREATE TABLE IF NOT EXISTS p(c1 REAL UNIQUE); CREATE
```

---

## Crash 115: `d0af36bd645c9a3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000152849`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (trim(CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3
```

---

## Crash 116: `b0000b4dbfb2b82b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000154285`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BLOB); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE); INSERT INTO p DEFAULT VALUES; VALUES (TRUE) EXCEPT VALUES (-700711532058354461938795049978998728.04E+4577903461435
```

---
