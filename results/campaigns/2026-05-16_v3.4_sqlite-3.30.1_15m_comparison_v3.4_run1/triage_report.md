# Crash Triage Report

**Total crashes:** 346  
**Unique crash sites:** 346  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 144 | 144 | 41% |
| Signal | 202 | 202 | 58% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `7a53c8791687cd72` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000152`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WITH RECURSIVE p AS (SELECT p.*) SELECT (CASE WHEN ~(VALUES (NULL) ORDER BY CURRENT_TIMESTAMP + s.b IS (format('', FALSE COLLATE RTRIM) OVER (
```

---

## Crash 2: `5ba5abc76dc82ba0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000480`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, a, c3, c2); INSERT OR ABORT INTO q VALUES (lead(c3) COLLATE RTRIM); SELECT CURRENT_TIME, p.* FROM jsonb_each('{"a":1}') NATURAL JOIN q JOIN json
```

---

## Crash 3: `2591db5e29d30022` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000733`

```sql
SELECT round(1e308, -1); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b, c3, c1); INSERT INTO q WITH p (c3, rowid, c1, c1) AS (SELECT CURRENT_TIME <> CURRENT_TIME AS i_q__7_r_5___i__i2x__q9_ca
```

---

## Crash 4: `2e4ac66a72cefa02` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001017`

```sql
SELECT printf('%lld', 2147483647, '3- __   SO0K3 '); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2); SELECT TRUE ->> CASE WHEN CASE CURRENT_TIMESTAMP WHEN FALSE NOT NULL NOT NULL THEN CU
```

---

## Crash 5: `b9967955079370e1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001068`

```sql
SELECT substr('2lbB5Ze_81 ', -9223372036854775808, 9223372036854775807); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, b); SELECT t1.* UNION SELECT ALL (+RAISE(IGNORE) | -json_type(TRUE, '$
```

---

## Crash 6: `a82be36bd2a8fd10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001525`

```sql
SELECT printf('%.*f', -2147483649, 1e308); SELECT printf('%s', 4294967295, 'E_ bM6nT18'); CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255) GENERATED ALWAYS AS 
```

---

## Crash 7: `1368b470f77eb16e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001658`

```sql
CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed
```

---

## Crash 8: `5beee2780b91bac5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001706`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FRO
```

---

## Crash 9: `a86ab5907929d2d1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001718`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 10: `89a1a3c5c72019a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001727`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c
```

---

## Crash 11: `69ae0008a9826de6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001738`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN se
```

---

## Crash 12: `8fd69fcddecb5119` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001790`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 13: `9bf497c43a93af94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002105`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM q WHERE NULL GROUP BY rank() OVER (ORDER BY RAISE(IGNORE) DESC GROUPS BETWEEN UNB
```

---

## Crash 14: `5fe20cf88c5e1b00` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002111`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM q WHERE NULL GROUP BY RAISE(IGNORE), +count(*) FILTER (WHERE CURRENT_TIMESTAMP) O
```

---

## Crash 15: `9237a0c16eb68fd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002222`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 16: `4e3d22b67dbb417b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002346`

```sql
SELECT hex(zeroblob(-9223372036854775808)); CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) =
```

---

## Crash 17: `9a0877b2014503da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002617`

```sql
SELECT round(1.0, 9223372036854775807); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 18: `f116bf7423073f85` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003102`

```sql
SELECT hex(zeroblob(0)); CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT *, CURRENT_DATE FROM (SELECT CURRENT_TIME FROM p WHERE FALSE) AS sub1; C
```

---

## Crash 19: `5f150f7682a51b03` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003531`

```sql
SELECT printf('%.*s', 2147483647, 1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 20: `a1cb5e7d43a00995` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004120`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM (p) GROUP BY CURRENT_DATE HAVING NULL EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a
```

---

## Crash 21: `2469dec1284209db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004134`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (FALSE) EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed
```

---

## Crash 22: `3267f25a85754a38` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004142`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING NULL EXCEPT SELECT DISTINCT * FROM q; CREATE TA
```

---

## Crash 23: `f156926ab12d86c3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004157`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a
```

---

## Crash 24: `aaf38a11452998ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004212`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a J
```

---

## Crash 25: `93719f02a6652235` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000004857`

```sql
SELECT substr('2', 4294967296, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(
```

---

## Crash 26: `55391ccefb268724` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005009`

```sql
SELECT printf('%.*g', -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead
```

---

## Crash 27: `7130ac087d912f79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005661`

```sql
SELECT printf('%x', 2147483647, ' _2_'); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) 
```

---

## Crash 28: `1e9dbf56ba659c30` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005765`

```sql
SELECT substr(' 9 O_T8', 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVE
```

---

## Crash 29: `4de39837319735cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000005813`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 30: `2547901f81226d3a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010253`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE s
```

---

## Crash 31: `eb1dc22a97d64e35` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010260`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM
```

---

## Crash 32: `ec00a9c76fafebbd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010286`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (jsonb_tree('{"a":{"b":1}}')) WHERE CURRENT_TIME ORDER B
```

---

## Crash 33: `0597a1be58ac646d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010293`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CASE WHEN CURRENT_DATE THEN TRUE END); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 34: `17445ceb40082358` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010299`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (~FALSE > CAST(CURRENT_DATE AS BOOLEAN), NOT NULL); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CRE
```

---

## Crash 35: `4269263ceb1b5044` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010309`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NULL IS NOT NULL < (SELECT DISTINCT * FROM jsonb_tree('{}') LIMIT FALSE OR CURRENT_DATE), ~FALSE > CAST(CURR
```

---

## Crash 36: `d5f4b818ef504e80` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010315`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (count(*), CURRENT_TIMESTAMP); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UN
```

---

## Crash 37: `49344af8bf31c0a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010322`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_TIMESTAMP < TRUE * NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABL
```

---

## Crash 38: `835e10853e717be8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010342`

```sql
SELECT substr('2_t--wTg-_40g3 ', 2147483648, -1); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce
```

---

## Crash 39: `6c08a04753ab1741` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010353`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CAST(CURRENT_DATE AS BOOLEAN))); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE 
```

---

## Crash 40: `bf3449f3030c8574` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010365`

```sql
SELECT printf('%.*d', 0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))
```

---

## Crash 41: `9c9b73db0b3a36d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010372`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES ((SELECT ALL * FROM q INDEXED BY c3 INNER JOIN jsonb_tree('{"a":{"b":1}}') CROSS JOIN json_each('[{"a":1},{"b
```

---

## Crash 42: `7ebd1531f8adb16d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010379`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (NOT EXISTS (SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE RAISE(IGNORE) GROUP BY FALSE LIMIT TRUE OFFS
```

---

## Crash 43: `c97c2bd557f34e0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010388`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p VALUES (TRUE IN (VALUES (TRUE))); PRAGMA integrity_check; CREATE TABLE seed_a(
```

---

## Crash 44: `0a91a0998cf3c2db` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010396`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ BOOLEAN); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY, b FLOAT UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 45: `7da825a1bae3dd0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010402`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC UNIQUE, rowid DATE UNIQUE, c2 DATE PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 46: `f7c17bd3817aadfa` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010411`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (VALUES (CURRENT_TIME)); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a 
```

---

## Crash 47: `fa542b0cc62e0c0e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010417`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (TRUE) UNION VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 48: `747b85c2ec4b0c82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010426`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT * FROM jsonb_tree('[1,2,3]') WHERE TRUE GROUP BY CURRENT_TIME WINDOW w1 AS (), w2 AS (); INSERT INTO p DEFAUL
```

---

## Crash 49: `23afd24e29be3fcf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010434`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ABORT INTO p VALUES (NULL / ifnull(NULL, CURRENT_TIMESTAMP NOT NULL)); PRAGMA inte
```

---

## Crash 50: `6eb4330a857d76ea` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010446`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT t1.* FROM json_tree('[{"a":1},{"b":2}]') ORDER BY TRUE ASC NULLS LAST; INSERT INTO p DEFAULT VALUES; PRAGMA i
```

---

## Crash 51: `778e189fb44d35d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010452`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (json_each('{"a":1}') NATURAL LEFT JOIN t2) WHERE TRUE; 
```

---

## Crash 52: `5b4ede50d0c4b356` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010540`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL C
```

---

## Crash 53: `2ac1da5cfa002a5a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010548`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c1 REAL C
```

---

## Crash 54: `cc6790682d42221d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010567`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b NUMERIC
```

---

## Crash 55: `d84356b88d2782a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010580`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b NUMERIC
```

---

## Crash 56: `f7cf675b6731143d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010589`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(b NUMERIC
```

---

## Crash 57: `8eeaa4d3cb0ca1b7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010633`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INT P
```

---

## Crash 58: `780c57362bf84f7a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010844`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_DATE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE);
```

---

## Crash 59: `63b7950456c9c6c9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010901`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (CURRENT_TIMESTAMP * NULL)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_
```

---

## Crash 60: `8970442997fac29b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010926`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL CHECK (TRUE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE); SELECT 
```

---

## Crash 61: `629138c0987e58e0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000010951`

```sql
CREATE TABLE IF NOT EXISTS p(c1 INTEGER UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (RAISE(IGNORE)); INSERT OR ROLLBACK INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed
```

---

## Crash 62: `4cac1acb7dd25446` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011114`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE seed_a(c UNIQUE); 
```

---

## Crash 63: `c664bbbfcfae5a82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011121`

```sql
SELECT round(-1e308, -2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER()
```

---

## Crash 64: `65f0eebb5b716068` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011137`

```sql
SELECT round(0.0, 2147483647); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 65: `81fa1437bda43f57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011155`

```sql
SELECT substr('', 2147483648); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SU
```

---

## Crash 66: `b4baa469ca4c935d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000011163`

```sql
SELECT printf('%.*f', 2147483647, 1.0); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) O
```

---

## Crash 67: `09477f1a8e8f42b3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017255`

```sql
SELECT substr('2', 4294967296, -9223372036854775808); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coal
```

---

## Crash 68: `366c69f454141525` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017275`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT * FROM p INDEXED BY c3 JOIN p NOT INDEXED ON CURRENT_DATE; VALUES (TRUE); CREATE TAB
```

---

## Crash 69: `f6c45901546e39cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017390`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM (SELECT TRUE COLLATE BINARY IS NOT TRUE FROM p WHERE 622755712578691994062046611578093.611
```

---

## Crash 70: `346141f33a503992` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017396`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM (SELECT TRUE COLLATE BINARY FROM p WHERE 622755712578691994062046611578093.611188307275498
```

---

## Crash 71: `21a1ba0766aeeb5f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017441`

```sql
CREATE TABLE IF NOT EXISTS p(b NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); SELECT * FROM (SELECT TRUE COLLATE BINARY IS NOT TRUE FROM p WHERE CURRENT_DATE) AS sub1; CREATE TABLE s
```

---

## Crash 72: `b1d8b682ae8afd31` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017526`

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

---

## Crash 73: `75de027ff2b90f10` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021502`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE 
```

---

## Crash 74: `6a7e583f701d1c49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021510`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); EXPLAIN QUERY PLAN SELECT CURRENT_TIMESTAMP AS a; CREATE TAB
```

---

## Crash 75: `de1757389ed47e56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021604`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (FALSE)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED WHER
```

---

## Crash 76: `142def4877d3ecd1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021705`

```sql
CREATE TABLE IF NOT EXISTS p(c3 DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM q NOT INDEXED WHERE CU
```

---

## Crash 77: `b61bf2d5937d9c16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021824`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (NULL); SELECT * FROM (SELECT * FROM p WHERE FALSE) AS sub1; CREATE TABLE s
```

---

## Crash 78: `cad992af5bbd75f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021842`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY FALSE DESC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOIN s
```

---

## Crash 79: `ee664ae1baaa07b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021850`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); VALUES (CASE FALSE WHEN FALSE THEN FALSE ELSE CURRENT_TIM
```

---

## Crash 80: `f9a6593b36402a65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021909`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT FALSE ORDER BY RAISE(IGNORE); C
```

---

## Crash 81: `8322480598b4b70a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022078`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ INT PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (TRUE); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{}') WHERE CU
```

---

## Crash 82: `e3988e49b8860662` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022115`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (FALSE | TRUE)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED GROUP
```

---

## Crash 83: `95ac54bf9718fa2a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022125`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p (_rowid_) VALUES (CURRENT_TIMESTAMP); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE)
```

---

## Crash 84: `4b60714ef83c6ee6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022173`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (FALSE | TRUE)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (FALSE); SELECT *, * FROM (SELECT CURRENT_TIME FROM p WHERE C
```

---

## Crash 85: `42c9bbbc127081bc` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022179`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (last_insert_rowid()); PRAGMA integrity_check; CREATE TABLE seed_a(c UNI
```

---

## Crash 86: `6b11a038713dea94` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022765`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CASE WHEN FALSE THEN FALSE | TRUE END)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (~FALSE); EXPLAIN QUERY PLAN SELECT 
```

---

## Crash 87: `8bae8a5df7a5dfe1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000022991`

```sql
CREATE TABLE IF NOT EXISTS p(b INTEGER PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT OR IGNORE INTO p VALUES (~FALSE); EXPLAIN QUERY PLAN SELECT CURRENT_TIME | NULL IS NOT NULL
```

---

## Crash 88: `9bbccdaa8fe2775f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024296`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.
```

---

## Crash 89: `8961dec8cb7fc262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024305`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 REAL DEFAULT -6642199122.579); VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); S
```

---

## Crash 90: `2e91f6fdc87da973` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024323`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (CURRENT_TIMESTAMP) UNION ALL SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT see
```

---

## Crash 91: `5a3414d5bd3feabd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024330`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (-CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed_
```

---

## Crash 92: `f66ae2646dd997b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024380`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c2 TEXT DEFAULT '_- 0i'); VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT * FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT se
```

---

## Crash 93: `9effcff17618be81` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024423`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (CURRENT_TIMESTAMP) EXCEPT SELECT DISTINCT q.* FROM q; CREATE TABLE seed_a(c UNIQUE); SELECT seed
```

---

## Crash 94: `1de18085c359a473` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024495`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (-CURRENT_TIMESTAMP) EXCEPT VALUES (FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM s
```

---

## Crash 95: `db9d89c56dcbf4ae` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024589`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING TRUE COLLATE RTRIM COLLATE RTRIM EXCEPT SELECT 
```

---

## Crash 96: `da8c1b64a43eaac4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024610`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT CURRENT_TIME | NULL IS NOT NULL AS p FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING NULL EXCEPT 
```

---

## Crash 97: `a16dc37455b545b9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024627`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE DEFAULT -0); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING NULL EXCEPT SELECT DISTINCT * FROM q; CREAT
```

---

## Crash 98: `9442584e99cd0e87` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024723`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL DEFAULT X''); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING NULL EXCEPT SELECT DISTINCT * FROM 
```

---

## Crash 99: `69671902948cd10e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024747`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC NOT NULL DEFAULT TRUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING NULL EXCEPT SELECT DISTINCT * FROM
```

---

## Crash 100: `01cb747f602a91d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024780`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); WITH RECURSIVE q AS (SELECT *) VALUES (NULL); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a
```

---

## Crash 101: `4f3886fab54c371e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024900`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_DATE EXCEPT SELECT DISTINCT * FROM q; C
```

---

## Crash 102: `905adee5b678b120` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028091`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (FALSE); VALUES (FALSE > CAST(CURRENT_DATE AS BOOLEAN), FALSE); CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM see
```

---

## Crash 103: `aa1e6c8be35eb272` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034908`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (TRUE), _rowid_ TEXT CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUE
```

---

## Crash 104: `52feeb5bc4ac2c20` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000036955`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIME ASC, CURRENT_TIMESTAMP DESC NULLS LAST; CREATE TABLE IF NOT EXISTS p(c2 NUME
```

---

## Crash 105: `f0f9c727be5cc65a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000040743`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREAT
```

---

## Crash 106: `4205d60d8aaeddb6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041858`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL *, * FROM json_each('{"a":{"b":1}}') ORDER BY FALSE DESC NULLS FIRST; CREATE TABLE seed_a(c UNIQUE); SELECT seed_a.c FROM seed_a JOI
```

---

## Crash 107: `8cb775304410ce1c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041865`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (p NOT INDEXED) WHERE CURRENT_TIME ORDER BY NULL ASC LIMIT NULL; CREAT
```

---

## Crash 108: `3081e40a48c088ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041872`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT NOT NULL DEFAULT FALSE, c1 REAL NOT NULL DEFAULT -9662.0133899084156095045274431412642678787578482013577667968367307241326994853358256071935056E+7876485341938794781
```

---

## Crash 109: `caf2fd75333836ac` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041915`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); C
```

---

## Crash 110: `ec2d53acb13af1f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000041921`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (sum(NULL) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY FALSE ASC ROWS BETWEEN CURRENT ROW AND CURRENT_TIME FOLLOWING))
```

---

## Crash 111: `40b8af93c45dc88a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042007`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL 
```

---

## Crash 112: `56e5d9292f5f4749` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000043931`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (TRUE IS NOT TRUE); PRAGMA integrity_check; CREATE TABLE seed_a(c UNIQUE
```

---

## Crash 113: `9d125feff88dda4d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045018`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE % CURRENT_TIME); SELECT NOT EXISTS (SELECT * FROM json_each('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE L
```

---

## Crash 114: `8f37975f3f755e52` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045061`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC UNIQUE); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE % CURRENT_TIME); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN json_each('{"a":1}') WHERE F
```

---

## Crash 115: `7c0ed9d31f146e79` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000045067`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN json_each('{"a":1}') WHERE TRUE ORDER BY CURRENT_TIME ASC, CURRENT_TIMESTAMP DESC N
```

---

## Crash 116: `02d92e9c7681ded6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047209`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 INT); SELECT * INTERSECT SELECT *, * FROM json_each('[{"a":1},{"b":2}]') INNER JOIN t2 NOT INDEXED NATURAL LEFT JO
```

---

## Crash 117: `07609d7130f0f10f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047284`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT -801404335314690538487437993921.914691871944005252492351964295540880526642231933); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT
```

---

## Crash 118: `0257687c141f6262` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047299`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (FALSE || CURRENT_TIMESTAMP); PRAGMA quick_check; CREATE TABLE IF N
```

---

## Crash 119: `39987aed1d8c3aa3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047317`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TAB
```

---

## Crash 120: `7ed709f1bec990b6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047323`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); C
```

---

## Crash 121: `21339325c72c8424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047332`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); C
```

---

## Crash 122: `b92df03af4b94f1f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047395`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); C
```

---

## Crash 123: `fbdb375aeac88b51` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047473`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL 
```

---

## Crash 124: `ed809d1f32f1f818` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000047479`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT FALSE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL 
```

---

## Crash 125: `5a779dc834760feb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048606`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT -2745224857438598.010825425336274494148526477); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 126: `64fca764fabc967a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052062`

```sql
CREATE TABLE IF NOT EXISTS p(rowid NUMERIC); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT * UNION SELECT * FROM jsonb_each('[{"a":1},{"b":2}]') WHERE CURRENT_DATE GRO
```

---

## Crash 127: `adbd1b161beb5685` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052278`

```sql
CREATE TABLE IF NOT EXISTS p(c1 VARCHAR(255) UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT * FROM q WHERE NULL GROUP BY rank() OVER (ORDER BY RAISE(IGNORE) DESC ROWS BETWEEN CURRE
```

---

## Crash 128: `d3e781084ee40852` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054329`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM p AS a JOIN json_each('[{"a":1},{"b":2}]') NATURAL LEFT JOIN json_tree('{}') ORDER BY CURRENT_TIME ASC NULLS LAST; CREATE TAB
```

---

## Crash 129: `b1b2a4b2efe4e97c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056343`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_each('[1,2,3]') ORDER BY FALSE DESC NULLS FIRST; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(b); INSERT INTO p 
```

---

## Crash 130: `d70e8739cb8a394a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056845`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_tree('[1,2,3]') ORDER BY FALSE DESC NULLS FIRST; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS
```

---

## Crash 131: `19dfdf2d33db4232` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057066`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_tree(NULL, '$[#-1]') ORDER BY FALSE DESC NULLS FIRST; CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT E
```

---

## Crash 132: `337115e862926d92` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000061495`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS VALUES (FALSE); INSERT OR IGNORE INTO p VALUES (CURRENT_TIMESTAMP); SELECT CURRENT_DATE AS a5 LIMIT TRUE, FALSE NOT BET
```

---

## Crash 133: `b6bbe1258717a835` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067282`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM json_tree('{"a":{"b":1}}') WHERE CURRENT_TIMESTAMP GROUP BY FALSE WINDOW w1 AS () ORDER BY NULL ASC LIMIT NULL; CREA
```

---

## Crash 134: `5b7700d7b0faf8be` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000069584`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM p AS a JOIN json_each('[{"a":1},{"b":2}]') NATURAL LEFT JOIN p WHERE TRUE; CREATE
```

---

## Crash 135: `f412dd0db775c7d2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078026`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_DATE EXCEPT SELECT DISTINCT NOT EXISTS 
```

---

## Crash 136: `b503a4a5af70d40f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078049`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING abs((VALUES (CURRENT_TIME)) % TRUE) EXCEPT SELE
```

---

## Crash 137: `07a5ec09bfd71f54` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078072`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_DATE IS NOT CURRENT_TIME EXCEPT SELECT 
```

---

## Crash 138: `ef3709ce53603460` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078216`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CASE WHEN TRUE THEN CURRENT_DATE COLLATE RTRIM 
```

---

## Crash 139: `90fb7eae2e21e7a0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078224`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_TIME != CURRENT_TIMESTAMP LIKE CURRENT_
```

---

## Crash 140: `d5a296562572c220` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078237`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING EXISTS (SELECT DISTINCT * FROM json_tree('{"a":
```

---

## Crash 141: `568bb85f580b904c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078248`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_TIME >= CURRENT_TIMESTAMP COLLATE NOCAS
```

---

## Crash 142: `1257e8fe8e55b1bb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078277`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_TIME COLLATE RTRIM EXCEPT VALUES (sum(N
```

---

## Crash 143: `472f32d7eb38c4f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078288`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY FALSE * FALSE * CURRENT_TIMESTAMP HAVING CURRENT_TIME COLLATE RTRIM
```

---

## Crash 144: `d134af98ef56136d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000078418`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY CURRENT_DATE HAVING CURRENT_DATE LIKE NULL COLLATE RTRIM EXCEPT VAL
```

---

## Crash 145: `71eea10860152c8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001634`

```sql
CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER)
```

---

## Crash 146: `428dc233d5aa4e4a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001752`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_DATE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 147: `6fc9e658a0890da7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001822`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 148: `a951025f96f80608` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001834`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 149: `290ddc587208854c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001850`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 150: `133d89aa20662ffe` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001867`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 151: `5ab4aceaecf16463` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001962`

```sql
CREATE TABLE IF NOT EXISTS p(a INT DEFAULT CURRENT_DATE, c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 152: `de8475ddf5afab41` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000001975`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2
```

---

## Crash 153: `0fd8cbba13251617` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002899`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 154: `2a58fcb9525b2ca1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002909`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12
```

---

## Crash 155: `42099dcc04737f2d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000002986`

```sql
SELECT printf('%.*g', -2147483648, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 156: `83ede5f9e0c7d410` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003037`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 157: `2f643d35c461df3a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003051`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 158: `7030254025e7d887` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003444`

```sql
SELECT printf('%.*f', -9223372036854775808, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55)
```

---

## Crash 159: `a82422d7d8253e37` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003547`

```sql
SELECT printf('%.*s', 4294967296, -1.0); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 160: `3245b36ea080f620` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003627`

```sql
SELECT printf('%f', 0, '  uC_V_q_ '); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE
```

---

## Crash 161: `b1fca720931ab737` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000003717`

```sql
SELECT printf('%.*s', -9223372036854775808); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 162: `7c04a8fa6bcbc9dc` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004193`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p NOT INDEXED GROUP BY TRUE EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 163: `c0f7cb1a5c612ff1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004902`

```sql
SELECT hex(zeroblob(1)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE seed_t
```

---

## Crash 164: `f409d5d0467cbd1e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004928`

```sql
CREATE TABLE seed_b(b INTEGER); INSERT INTO seed_b VALUES (1),(2),(3); SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FR
```

---

## Crash 165: `4b7df402ba3a2381` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000004980`

```sql
SELECT substr('-V--2OB vsz-__', 9223372036854775807, 4294967295); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 V
```

---

## Crash 166: `277254c4e66054db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005045`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM s NATURAL JOIN (SELECT * ORDER BY TRUE DESC NULLS LAST LIMIT RAISE(IGNORE)) AS bs_1b9__et9_
```

---

## Crash 167: `70c84f3e89387c26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000005776`

```sql
SELECT printf('%lld', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(1
```

---

## Crash 168: `cd3af5286e899deb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010967`

```sql
SELECT substr('__', 2147483647, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123);
```

---

## Crash 169: `c7703b7b22ee9ca0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010979`

```sql
SELECT printf('%f', -9223372036854775808, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123
```

---

## Crash 170: `df0c185275d37c4e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000010995`

```sql
SELECT printf('%lld', -1, ''); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE 
```

---

## Crash 171: `76c5666b0e966a47` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011009`

```sql
SELECT printf('%.*s', 1, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 172: `1658fb99d22d3956` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000011043`

```sql
SELECT round(1e308, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABL
```

---

## Crash 173: `44a3a83b046f7980` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012347`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (total_changes()); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 174: `2124730eba15392e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012420`

```sql
SELECT round(-1.0, 2147483648); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CREATE TABLE
```

---

## Crash 175: `31ca2f8716435a62` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000012871`

```sql
SELECT printf('%.*g', 4294967295); CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CASE WHEN FALSE THEN FALSE | TRUE END)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; PR
```

---

## Crash 176: `ffec1a57c9f0b2af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016696`

```sql
SELECT printf('%.*d', 2147483647, 0.01); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CRE
```

---

## Crash 177: `2884491e60d92b8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016789`

```sql
CREATE TABLE IF NOT EXISTS p(c1 REAL NOT NULL); INSERT OR ROLLBACK INTO p VALUES (FALSE); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 178: `8be71e46a99cdb1a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016840`

```sql
SELECT printf('%.*e', 4294967295, 1e-308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 179: `472ad0e9a5ade592` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016885`

```sql
SELECT printf('%.*d', 2147483648, -1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); C
```

---

## Crash 180: `799b0a480c249fec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000016953`

```sql
SELECT substr('N_7jh- g', 2147483648, 2147483647); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),
```

---

## Crash 181: `e6d7cf4fef773efd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017600`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME >> CURRENT_DATE = CURRENT_TIME; CREATE TABLE seed_t1(c1
```

---

## Crash 182: `8d9c900df102834a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017606`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 
```

---

## Crash 183: `0e04bd685365dd00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017612`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_DATE = CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSER
```

---

## Crash 184: `9cda102efe5002ac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017636`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(rowid NUMERIC PRIMARY KEY); SELECT * FROM q NATURAL JOIN q WHERE CURRENT_TIME >> CURRENT_TIME; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 185: `c0e18c856dfe68ca` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017653`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE, rowid FLOAT UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 186: `cffb2cc948aa1da8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017665`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(c1 TEXT NOT NULL); SELECT * FROM q NATURAL JOIN q WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 187: `3f71bd4548fb0841` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017691`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CASE WHEN TRUE THEN CURRENT_DATE COLLATE RTRIM ELSE TRUE END >> CURRENT_DATE = N
```

---

## Crash 188: `e44b7d87a1486177` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000017704`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE); CREATE TABLE IF NOT EXISTS q(b BLOB UNIQUE); SELECT * FROM q NATURAL JOIN q WHERE CASE WHEN TRUE THEN CURRENT_DATE COLLATE RTRIM ELSE TRUE END >> NULL IS NOT NULL
```

---

## Crash 189: `f4d5ca0a4ad77aec` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020744`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); EXPLAIN QUERY PLAN SELECT CURRENT_TIME LIKE CURRENT_DATE ESCAPE CURRENT_TIMESTAMP; CREATE TABLE see
```

---

## Crash 190: `7e01abf910b104db` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000020776`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT NOT NULL); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); VALUES (CAST(CURRENT_DATE AS BOOLEAN), FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t
```

---

## Crash 191: `77cc88185a0ee32e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000021257`

```sql
SELECT printf('%.*d', 2147483647, 1e308); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 INTEGER); INSERT INTO seed_t2 VALUES(44),(55),(123); CR
```

---

## Crash 192: `56e31e4c513997be` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023599`

```sql
CREATE TABLE IF NOT EXISTS p(c3 NUMERIC DEFAULT X'd8bCcadc4ffe', c1 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(c1 BOOLEAN PRIMARY KEY); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TAB
```

---

## Crash 193: `a378aa77327b7cd9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023973`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM q NOT INDEXED WHERE CURRENT_TIME ORDER BY FALSE DES
```

---

## Crash 194: `fdca6c5994b848f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000023989`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) UNION ALL VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 195: `677ad11d732826af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024008`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT -23326483610467304413632220011241156496845746.0E+65946089131025550112005858670); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) E
```

---

## Crash 196: `e0d6006701e52029` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024017`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); EXPLAIN QUERY PLAN SELECT NULL IN (CURRENT_TIMESTAMP, TRUE) AS b81__946_4e937xf75w__wruc_18__8_2_g2__h09
```

---

## Crash 197: `ab7531eef579dd5e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024029`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) UNION VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 198: `9bfb37d2cb5fcd3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024059`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) EXCEPT VALUES (NOT EXISTS (VALUES (NULL))); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO 
```

---

## Crash 199: `d309707836ee0118` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024066`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (+CURRENT_TIMESTAMP IN (NULL)) EXCEPT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 200: `ebe30e75ce270dd4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024076`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) INTERSECT VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VAL
```

---

## Crash 201: `43e7a4e0f5b01b03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024164`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT TRUE <= CURRENT_TIME COLLATE BINARY << CASE WHEN TRUE THEN CURRENT_TIME ELSE FALSE END AS a FROM 
```

---

## Crash 202: `830e5ce2fd6aeea4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024194`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT TRUE <= CURRENT_DATE << CURRENT_DATE AS a FROM json_each('{"a":1}') EXCEPT VALUES (CURRENT_TIME);
```

---

## Crash 203: `251bb5f9f0550285` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024202`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); SELECT CASE WHEN TRUE THEN CURRENT_TIME ELSE FALSE END AS a FROM json_each('{"a":1}') EXCEPT VALUES (CUR
```

---

## Crash 204: `aaa22830745e085b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024248`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) EXCEPT VALUES (NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(12
```

---

## Crash 205: `ba815ae89d27d6ab` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000024255`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (TRUE) EXCEPT VALUES (NOT CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 206: `65358e76c9e1c6d6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000027726`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT row_number() OVER (PARTITION BY CURRENT_DATE ORDER BY NULL DESC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDING AND CURRE
```

---

## Crash 207: `c3c05ac27e85b294` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030710`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CASE WHEN CURRENT_TIME IS NULL THEN CURRENT_TIME END)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); SELECT * FROM (SELECT * FROM p WHERE c2) AS sub1; CR
```

---

## Crash 208: `fce8c4910dc405bb` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030718`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT CURRENT_TIME FROM json_tree('{"a":1}'); CREATE TABLE seed_t
```

---

## Crash 209: `e20af9dbf2c0d09b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000030758`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE EXISTS (SELECT FALSE ORDER BY CASE WHEN CURRENT_DATE THEN TRUE END 
```

---

## Crash 210: `58a50e739f0f2516` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031090`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_TIMESTAMP, * FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER)
```

---

## Crash 211: `15f19bdfca9d5467` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031096`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT NOT EXISTS (SELECT * FROM json_each('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE LIMIT CURRENT_TIM
```

---

## Crash 212: `7210956502e524af` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031102`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE, rowid BLOB PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(
```

---

## Crash 213: `b8ff3b6597632f7f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031112`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE CHECK (TRUE), _rowid_ TEXT CHECK (CURRENT_TIMESTAMP)); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE FALSE) AS sub1; CRE
```

---

## Crash 214: `c3eeb1fa36da2916` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031118`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT NOT EXISTS (SELECT * FROM json_each('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE LIMIT NOT EXISTS (SELECT DI
```

---

## Crash 215: `e819adc39c043068` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031177`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT TRUE MATCH CURRENT_TIME FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 216: `7261d0cf1a2c2eac` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031188`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS WITH q AS (SELECT *) SELECT CURRENT_TIMESTAMP, *; SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE FALSE) AS sub1; 
```

---

## Crash 217: `5efeb475a4deaeda` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031197`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_TIME FROM p WHERE CURRENT_TIMESTAMP < TRUE * NULL) AS sub1; CREATE TABLE s
```

---

## Crash 218: `e20ae1a7c2b4a1c8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031203`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT CURRENT_TIMESTAMP COLLATE BINARY FROM p WHERE FALSE) AS sub1; CREATE TABLE seed_t1
```

---

## Crash 219: `397d17b66201dfb4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031211`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT cume_dist() OVER () FROM json_tree('{"a":1}
```

---

## Crash 220: `1bd6db7c9436cf01` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031266`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT NULL IS NULL IN (NOT CURRENT_DATE IN (SELECT *) COLLATE RTRIM GLOB RAISE(IGNORE) IS NULL = CURRENT_DATE) NO
```

---

## Crash 221: `45c9b38345d4c6f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031275`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT CURRENT_TIMESTAMP + CASE percent_rank() WHEN FALSE THEN FALSE END / -RAISE(IGNORE) >> CURRENT_DATE << FALSE
```

---

## Crash 222: `5a38f163af1aa7f9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031334`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME > TRUE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INS
```

---

## Crash 223: `e373487a29875682` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031726`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR ABORT INTO p VALUES (json_patch('[1,2,3]', '[{"a":1},{"b":2}]')); PRAGMA quick_check; CREATE TABLE seed
```

---

## Crash 224: `15234a2cfd2036f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031739`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ TEXT); CREATE VIEW IF NOT EXISTS v1 AS SELECT row_number() OVER (PARTITION BY CURRENT_DATE ORDER BY NULL DESC NULLS LAST ROWS BETWEEN NULL PRECEDING AND CURRENT RO
```

---

## Crash 225: `f3648d12d6934b64` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031774`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO p DEFAULT VALUES; ANALYZE q; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 226: `5b86976533fae09b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031783`

```sql
CREATE TABLE IF NOT EXISTS p(a INT UNIQUE, c3 VARCHAR(255), c2 VARCHAR(255) DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed
```

---

## Crash 227: `4a083f14afdeb536` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000031838`

```sql
CREATE TABLE IF NOT EXISTS p(a NUMERIC, c3 TEXT NOT NULL DEFAULT -801404335314690538487437993921.914691871944005252492351964295540880526642231933); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO
```

---

## Crash 228: `d2e2c5362fd67d8d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034805`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT avg(CURRENT_DATE) FILTER (WHERE NULL) AS l__x_3exw_yk_1__i_2edr09q_7___d1_1_aa611w_k_dj2_1bb61_g__o1b_9; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 229: `b3e1e89dff75dac3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000034877`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT avg(CURRENT_DATE) FILTER (WHERE TRUE) AS l__x_3exw_yk_1__i_2edr09q_7___d1_1_aa611w_k_dj2_1bb61_g__o1b_9; CREATE TABLE seed_t1(c1 INTEGER
```

---

## Crash 230: `15962f3d66da8569` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039191`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (json_each('{"a":1}') NATURAL LEFT JOIN json_each('{"a":1}')) WHERE TRUE; CREATE TA
```

---

## Crash 231: `0ab5835fad2d167e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039199`

```sql
CREATE TABLE IF NOT EXISTS p(a REAL NOT NULL DEFAULT -23326483610467304413632220011241156496845746.0E+65946089131025550112005858670, c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE); CREATE TABL
```

---

## Crash 232: `7a66b511a0cd4017` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039205`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c3 FLOAT); INSERT INTO p (_rowid_) VALUES (NOT EXISTS (VALUES (CURRENT_TIME))); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(1
```

---

## Crash 233: `fc63ba0dea144f85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039255`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c3 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT ALL NOT EXISTS (SELECT * FROM json_each('{"a":1}') WHERE NULL GROUP BY CURRENT_DATE LIMIT CURRENT_TIMESTAMP) 
```

---

## Crash 234: `1ed77777cd88ebb1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039265`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE ISNULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE se
```

---

## Crash 235: `8f1a9a4676dfd361` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039292`

```sql
CREATE TABLE IF NOT EXISTS p(b INT UNIQUE, c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (count(*), CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234);
```

---

## Crash 236: `c4c47c80a646f7d1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039441`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT OR ABORT INTO p VALUES (NULL / TRUE IS NOT TRUE); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 237: `29a63fe8a8e66a46` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039466`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (~FALSE > CAST(CURRENT_DATE AS BOOLEAN), NOT NULL); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),
```

---

## Crash 238: `a7434960112ea03b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039476`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE + CURRENT_DATE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE 
```

---

## Crash 239: `e64757941baaea95` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039505`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT OR FAIL INTO p VALUES (TRUE <= FALSE NOT IN (CURRENT_TIMESTAMP)); VALUES (TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 240: `343f75614528be3b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039655`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN percent_rank() OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_TIME) THEN NULL END); CREATE TABLE seed_t1(c1 INTEG
```

---

## Crash 241: `d1883b2cd4151c63` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000039716`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CASE WHEN dense_rank() OVER () THEN CURRENT_DATE END); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 242: `07ab2e062168c213` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040214`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN UNIQUE); INSERT OR ABORT INTO q VALUES (FALSE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 243: `10e4ec5e9f7630a4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040245`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN json_each('[]') WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 V
```

---

## Crash 244: `d3c30c5d52124228` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040281`

```sql
CREATE TABLE IF NOT EXISTS p(b INT NOT NULL DEFAULT X''); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 245: `dbcd8777a0f8443c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040287`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES (NULL || FALSE); ANALYZE p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed
```

---

## Crash 246: `94a5956b1dc142b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040370`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; ANALYZE p; CREATE TABLE IF NOT EXISTS p(c2 INT PRIMARY KEY); CREATE INDEX IF N
```

---

## Crash 247: `46becf6b0c24bca3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040667`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE) UNION ALL VALUES (CAST(NULL AS TEXT)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TAB
```

---

## Crash 248: `c101204fd3de1273` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040687`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE) UNION ALL VALUES (CAST(FALSE AS TEXT)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 249: `5a10cd0b1b95536f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040694`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (TRUE <= FALSE NOT IN (CURRENT_TIMESTAMP)); PRAGMA integrity_check; CREATE 
```

---

## Crash 250: `0aff5eb6d92f17b0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040710`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (NULL NOT BETWEEN FALSE || EXISTS (VALUES (NULL)) NOTNULL AND CURRENT_TIMES
```

---

## Crash 251: `3201f630cb09e6ad` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040730`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL CURRENT_DATE FROM json_each('{"a":{"b":1}}') ORDER BY CURRENT_TIME ASC; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 252: `a2ea1f86d1f8cce4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040823`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KE
```

---

## Crash 253: `c52b8722208772df` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040849`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (FALSE & TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT IN
```

---

## Crash 254: `b0ff07d78d4368d5` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040882`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO se
```

---

## Crash 255: `a27ed66b06e924e6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040888`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (FALSE OR CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 256: `89f5d9b867269fd7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040896`

```sql
CREATE TABLE IF NOT EXISTS p(c3 VARCHAR(255), c2 VARCHAR(255) DEFAULT TRUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INT
```

---

## Crash 257: `6b68441a43ff05ce` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040905`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL DEFAULT -6642199122.579); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT 
```

---

## Crash 258: `4ee4aa9d974b6d90` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040924`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BOOLEAN UNIQUE, rowid FLOAT UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); I
```

---

## Crash 259: `7c1b9472f284d176` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040956`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT 0.0); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 260: `7f8a60bf6e27de7d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000040966`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE, c1 NUMERIC NOT NULL DEFAULT X'1AEEDBcD2f942b'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1
```

---

## Crash 261: `2a6a1fee9aec08ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041036`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 262: `1eeeb18dd038dc0d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041061`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT -2745224857438598.010825425336274494148526477); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 263: `5a13db06294d9a3f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041067`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR REPLACE INTO p VALUES (CURRENT_DATE); PRAGMA integrity_check; CREATE TABLE
```

---

## Crash 264: `d3ec67482e355896` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041073`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT * INTERSECT SELECT DISTINCT * FROM p INDEXED BY c3 JOIN p NOT INDEXED USING (c2, c3); INSERT INTO p DEFAULT VALU
```

---

## Crash 265: `76c8f2f24d19a92b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041158`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT ''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 266: `2bd3f3aa19e1b3f2` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041178`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC DEFAULT NULL); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO see
```

---

## Crash 267: `cc78822f3242c415` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041194`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 268: `97839388f7e45e91` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041202`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT CURRENT_TIMESTAMP); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c
```

---

## Crash 269: `42e94483c1a11412` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000041708`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT '_- 0i'); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA quick_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INT
```

---

## Crash 270: `01350c283144837b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000042730`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 BLOB); INSERT OR ABORT INTO p VALUES (CURRENT_TIMESTAMP <> -FALSE <> CURRENT_TIME); PRAGMA quick_check; CREATE TABLE
```

---

## Crash 271: `4f9478d9ef7a06e3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045236`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 BLOB); INSERT OR ABORT INTO p VALUES (CASE WHEN CURRENT_TIME IS NULL THEN CURRENT_TIME END); PRAGMA quick_check; CRE
```

---

## Crash 272: `6ce7f166cef3a064` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000045400`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ VARCHAR(255)); CREATE TABLE IF NOT EXISTS q(c1 BLOB); INSERT OR ABORT INTO p VALUES ((SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL)); PRAGMA quick_check; CREATE
```

---

## Crash 273: `f52746d03235d93d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000047174`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(_rowid_ TEXT UNIQUE); VALUES (NULL) EXCEPT VALUES (FALSE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(1
```

---

## Crash 274: `d9015557ed713321` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048207`

```sql
CREATE TABLE IF NOT EXISTS p(_rowid_ DATE PRIMARY KEY); INSERT OR REPLACE INTO p VALUES (TRUE >> CURRENT_TIME GLOB CURRENT_TIMESTAMP); VALUES (CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 275: `03d2aa2267c12bb7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048223`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT X'a33a45Bd0aEbCc'); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(
```

---

## Crash 276: `446fcfd967773cd8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048271`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT 396736665649267184.5945345311278791645170785826016); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_chec
```

---

## Crash 277: `65f9e2abcba4a170` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048334`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT X''); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NUL
```

---

## Crash 278: `ab58572afeecbb52` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048579`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE NOT NULL DEFAULT -2745224857438598.010825425336274494148526477); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 279: `c126494181b8648e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048598`

```sql
CREATE TABLE IF NOT EXISTS p(c2 REAL NOT NULL DEFAULT -2745224857438598.010825425336274494148526477); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR FAIL INTO p VALUES (FALSE || FALSE); PRAGMA in
```

---

## Crash 280: `a5786f2a6f20b67d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048615`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT -2745224857438598.010825425336274494148526477); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CR
```

---

## Crash 281: `c169a57f922522ee` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048636`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM json_each('[{"a":1},{"b":2}]') ORDER BY FALSE DESC NULLS FIRST; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 282: `728f9069bed10b80` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048771`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (TRUE IS NOT NULL)); CREATE TABLE IF NOT EXISTS q(c2 BOOLEAN UNIQUE); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); 
```

---

## Crash 283: `723fcabf8d07668b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000048785`

```sql
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN); INSERT INTO p DEFAULT VALUES; VALUES (count() FILTER (WHERE CURRENT_DATE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(12
```

---

## Crash 284: `0e10f6504299952a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049115`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR REPLACE INTO p VALUES (TRUE); PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CR
```

---

## Crash 285: `d0d48d0a04ed5931` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049129`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX
```

---

## Crash 286: `bcfb47d87dd1ce44` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049160`

```sql
CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE IF NOT EXISTS p(c2 DATE UNIQUE); CREATE INDEX
```

---

## Crash 287: `e2a092a8574d498f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049292`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT -58953); INSERT INTO p DEFAULT VALUES; PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); C
```

---

## Crash 288: `2356edc1e7726066` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049307`

```sql
CREATE TABLE IF NOT EXISTS p(c1 NUMERIC NOT NULL DEFAULT X'1AEEDBcD2f942b'); INSERT INTO p VALUES (TRUE IN (SELECT * FROM p NOT INDEXED GROUP BY CURRENT_TIME)); PRAGMA integrity_check; CREATE TABLE se
```

---

## Crash 289: `2e7aa189f05cc6b3` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049436`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES (TRUE IS NOT TRUE); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGE
```

---

## Crash 290: `39caf7108fdf78d9` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049442`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES ((SELECT DISTINCT * FROM p NOT INDEXED WHERE NULL)); PRAGMA integrity_chec
```

---

## Crash 291: `3b9d87a7ca321495` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049458`

```sql
CREATE TABLE IF NOT EXISTS p(b BLOB); CREATE TABLE IF NOT EXISTS q(c3 NUMERIC PRIMARY KEY); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_tree('{"a":1}'); CREATE TABLE seed_t1(c1 INTEGER);
```

---

## Crash 292: `8304de331a0f66bd` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049595`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INTEGER PRIMARY KEY); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT OR ABORT INTO p VALUES (NULL); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 293: `d2df20867b72e054` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000049992`

```sql
CREATE TABLE IF NOT EXISTS p(a DATE NOT NULL); CREATE TABLE IF NOT EXISTS q(rowid BOOLEAN UNIQUE); INSERT OR ABORT INTO q VALUES (CURRENT_TIMESTAMP NOT IN (FALSE) == NULL IS CURRENT_TIME); PRAGMA inte
```

---

## Crash 294: `df16acf3fc939417` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050018`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT * FROM p NOT INDEXED WHERE CURRENT_TIMESTAMP GROUP BY CURRENT_DATE HAVING FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT I
```

---

## Crash 295: `b8cc5efded10a2c6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050055`

```sql
CREATE TABLE IF NOT EXISTS p(a BLOB UNIQUE); CREATE TABLE IF NOT EXISTS q(b INTEGER); SELECT row_number() OVER (); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE
```

---

## Crash 296: `bdd463fb1ce8eb43` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050086`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT avg(CURRENT_DATE) FILTER (WHERE CURRENT_TIME >= CURRENT_TIMESTAMP COLLATE NOCASE) AS l__x_3exw_yk_1__i_2edr09q_7___d1_1_aa611w_k_dj2_1bb
```

---

## Crash 297: `86e65388c7438d8a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050563`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (PARTITION BY CURRENT_TIMESTAMP ORDER BY CURRENT_TIMESTAMP ASC NULLS LAST ROWS BETWEEN UNBOUNDED PRECEDI
```

---

## Crash 298: `128d915767fde4ed` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050598`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT * FROM json_tree('{}') WHERE TRUE GROUP BY CURRENT_DATE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(
```

---

## Crash 299: `6352b50d3e322d9a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050608`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (min(FALSE) OVER ()); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c
```

---

## Crash 300: `6d5422c0988c3f09` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050618`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (PARTITION BY CURRENT_TIME ORDER BY TRUE DESC NULLS FIRST ROWS BETWEEN t1.c2 PRECEDING AND FALSE FOLLOWI
```

---

## Crash 301: `be49f820dd2905b4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050647`

```sql
CREATE TABLE IF NOT EXISTS p(c2 INT CHECK (CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN CASE WHEN FALSE | TRUE THEN NULL END THEN CURRENT_DATE END THEN CURRENT_DATE END THEN TRUE END TH
```

---

## Crash 302: `7113c1ec596fed00` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050653`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_DATE NOT LIKE TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE s
```

---

## Crash 303: `13cd1aaf0a443134` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050780`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (ORDER BY CURRENT_TIME <> FALSE GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)); CREATE TABLE seed_
```

---

## Crash 304: `4a05562070df920a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050793`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (ORDER BY CURRENT_TIME <> -CURRENT_TIME NOT IN (CURRENT_TIME) GROUPS BETWEEN UNBOUNDED PRECEDING AND CUR
```

---

## Crash 305: `560889262a2cd73e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050805`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (ORDER BY CURRENT_TIME <> -CURRENT_TIME NOT IN (FALSE, CURRENT_DATE) GROUPS BETWEEN UNBOUNDED PRECEDING 
```

---

## Crash 306: `9e06a92a3e255ab0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000050842`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (ORDER BY -CURRENT_TIME GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)); CREATE TABLE seed_t1(c1 IN
```

---

## Crash 307: `e09ee1347a398bc8` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051017`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (dense_rank() OVER (PARTITION BY CURRENT_TIME ORDER BY TRUE DESC NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED
```

---

## Crash 308: `cf45eb18abecb95e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051077`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (rank() OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 309: `20ba44b6a6ef7984` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051098`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (percent_rank() OVER (ORDER BY EXISTS (VALUES (CURRENT_TIMESTAMP)) ASC NULLS LAST)); CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 310: `fad9d6fb41fc970c` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051131`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (TRUE - FALSE, CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TA
```

---

## Crash 311: `c14dfad59bfed85d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051141`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (sum(NULL) OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_TIME)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALU
```

---

## Crash 312: `e109e95ed3dac5f4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051151`

```sql
CREATE TABLE IF NOT EXISTS p(c2 BLOB NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS idx1 ON p(c2); INSERT INTO p DEFAULT VALUES; VALUES (percent_rank() OVER (PARTITION BY CURRENT_TIMESTAMP, CURRENT_T
```

---

## Crash 313: `0e6a904f9c7feb85` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051160`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT OR FAIL INTO p VALUES (CURRENT_TIMESTAMP LIKE CURRENT_TIME NOT LIKE CURRENT_TIMESTAMP ESCAPE NULL); VALUES (percent_rank() OVER (PARTITION BY CURRENT_TIM
```

---

## Crash 314: `d63dc624d84b7d9a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051391`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; VALUES (CURRENT_TIMESTAMP < TRUE); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE see
```

---

## Crash 315: `f897532c336ec85e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051567`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM p NOT INDEXED WHERE TRUE ORDER BY TRUE ASC LIMIT FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_
```

---

## Crash 316: `43e14d9d769db6f7` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051632`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT ALL * FROM json_tree('[1,2,3]') ORDER BY TRUE ASC LIMIT FALSE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES
```

---

## Crash 317: `234114591ffa1e16` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000051638`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT); INSERT INTO p DEFAULT VALUES; SELECT DISTINCT * FROM json_each('[]') LEFT JOIN p NOT INDEXED NATURAL JOIN json_tree('{"a":1}') ORDER BY TRUE ASC LIMIT FALSE; CR
```

---

## Crash 318: `04a272d3fb5fbc03` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000060938`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); VALUES (FALSE = -count() FILTER (WHERE NULL) OVER (ORDER BY CURRENT_TIMESTAMP, CURRENT_TIME) != CURRENT_TIME AND CURRENT_TIMESTAMP); CREATE TAB
```

---

## Crash 319: `cb056b7cc21a8378` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062147`

```sql
CREATE TABLE IF NOT EXISTS p(rowid INT, _rowid_ TEXT CHECK (NULL != FALSE)); CREATE VIEW IF NOT EXISTS v1 AS VALUES (CURRENT_TIME); INSERT INTO p DEFAULT VALUES; EXPLAIN QUERY PLAN VALUES (TRUE); CREA
```

---

## Crash 320: `3958cb8840d42d8f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062190`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT ALL * FROM p AS a JOIN json_each('[{"a":1},{"b":2}]') NATURAL LEFT JOIN p; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(
```

---

## Crash 321: `177c16d0a4209438` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062205`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT avg(CASE WHEN CASE NULL WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME END THEN CURRENT_TIMESTAMP < TRUE * NULL ELSE CURRENT_TIME END = FALSE)
```

---

## Crash 322: `7b523609bb7ff561` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062213`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT * FROM json_each('{"a":1}') WHERE NOT EXISTS (SELECT * FROM json_each('{"a":1}') WHERE CURRENT_TIME GROUP BY CURRENT_DATE LIMIT CURRENT_
```

---

## Crash 323: `e35420d65c293f26` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062220`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT avg(FALSE NOT BETWEEN NULL AND CURRENT_TIMESTAMP) FILTER (WHERE TRUE) AS l__x_3exw_yk_1__i_2edr09q_7___d1_1_aa611w_k_dj2_1bb61_g__o1b_9;
```

---

## Crash 324: `67baa5c72798f47f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000062253`

```sql
CREATE TABLE IF NOT EXISTS p(c2 NUMERIC NOT NULL); CREATE TABLE IF NOT EXISTS q(c1 VARCHAR(255)); INSERT OR ABORT INTO p VALUES (FALSE / CURRENT_TIME); PRAGMA integrity_check; CREATE TABLE seed_t1(c1 
```

---

## Crash 325: `4a377999084d490a` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000065931`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (CURRENT_DATE IS NOT CURRENT_TIME); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE T
```

---

## Crash 326: `2c8bf7c3daff896b` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066112`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (VALUES (NULL)) AS a WHERE CURRENT_TIME ORDER BY count(*) OVER (), CUR
```

---

## Crash 327: `5ef2c27d2330fd75` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000066347`

```sql
CREATE TABLE IF NOT EXISTS p(a FLOAT PRIMARY KEY); EXPLAIN QUERY PLAN SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (SELECT DISTINCT * FROM json_tree('{"a":{"b":1}}') LEFT JOIN (SELECT D
```

---

## Crash 328: `c2a8045a134a1e77` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068246`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT -801404335314690538487437993921.914691871944005252492351964295540880526642231933); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT INTO p VALUES (
```

---

## Crash 329: `c3fb0ba52a798c70` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068268`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); VALUES (min(FALSE), CURRENT_TIMESTAMP); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VALUES(12),(123),(1234); CREATE TABLE seed_t2(c2 
```

---

## Crash 330: `8982b77c09a1d92f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068309`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT DISTINCT * FROM p AS a JOIN json_each('[{"a":1},{"b":2}]') NATURAL LEFT JOIN p WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 331: `413d440b8b371356` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068318`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT -801404335314690538487437993921.914691871944005252492351964295540880526642231933); CREATE TABLE IF NOT EXISTS q(a DATE CHECK (TRUE), _rowid_ TEXT 
```

---

## Crash 332: `3848bbf74c39a427` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068327`

```sql
CREATE TABLE IF NOT EXISTS p(c3 TEXT NOT NULL DEFAULT -801404335314690538487437993921.914691871944005252492351964295540880526642231933); CREATE TABLE IF NOT EXISTS q(a NUMERIC); INSERT OR FAIL INTO p 
```

---

## Crash 333: `a3033a69a8f93289` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068620`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT DISTINCT * FROM (VALUES (NULL)) AS a LEFT JOIN json_each('{"a":1}') WHERE TRUE ORDER BY FALSE DES
```

---

## Crash 334: `b33b5147a348682d` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068633`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE TRUE ISNULL) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO
```

---

## Crash 335: `8508f31d86698ff4` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068653`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT avg(CURRENT_DATE) FILTER (WHERE FALSE AND RAISE(IGNORE)) AS l__x_3exw_yk_1__i_2edr09q_7___d1_1_aa
```

---

## Crash 336: `1b93a9da98749c22` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068676`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_each('[]') LEFT JOIN json_tree(CURRENT_TIMESTA
```

---

## Crash 337: `e78124b798daea71` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068730`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT +RAISE(IGNORE) IS FALSE / TRUE IS NOT NULL << -RAISE(IGNORE) COLLATE RTRIM + FALSE BETWEEN CURRENT_TIMESTAM
```

---

## Crash 338: `c478e2e9c5145bd6` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068792`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT_TIME > CURRENT
```

---

## Crash 339: `830fa0f9e62cdca1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000068871`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM (SELECT * FROM p WHERE FALSE * CURRENT_DATE) AS sub1; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---

## Crash 340: `d636535d6a65ffff` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069021`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT DISTINCT * FROM json_tree(CURRENT_DATE, '$[#-1]') LEFT JOIN json_each('{"a":1}') WHERE CASE WHEN RAISE(IGNO
```

---

## Crash 341: `0c22a600cab0443f` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069059`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; VALUES (count(*), count() FILTER (WHERE NULL)); CREATE TABLE seed_t1(c1 INTEGER); INSERT INTO seed_t1 VA
```

---

## Crash 342: `3e72085a514109c0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069839`

```sql
CREATE TABLE IF NOT EXISTS p(a TEXT NOT NULL); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; INSERT INTO p VALUES (TRUE IN (SELECT FALSE AS a FROM json_each('{"a":1}'))); PRAGMA integrity_check; CREATE TA
```

---

## Crash 343: `ae15c05d47155f2e` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000069991`

```sql
CREATE TABLE IF NOT EXISTS p(c3 INTEGER PRIMARY KEY); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT * FROM p WHERE EXISTS (SELECT DISTINCT * FROM json_tree(CURRENT_DATE, '$[#-1]') LEFT JOIN json_ea
```

---

## Crash 344: `a3fffcfb3f69d4a0` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000074397`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); SELECT DISTINCT *, *, *, *, * FROM json_tree('{"a":{"b":1}}') LEFT JOIN json_each('{"a":1}') WHERE TRUE; CREATE TABLE seed_t1(c1 INTEGER); INSE
```

---

## Crash 345: `725319616c1847f1` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000074554`

```sql
CREATE TABLE IF NOT EXISTS p(rowid BOOLEAN PRIMARY KEY); EXPLAIN QUERY PLAN VALUES (min(CURRENT_DATE) FILTER (WHERE CURRENT_DATE) OVER (ORDER BY FALSE ASC ROWS BETWEEN CURRENT ROW AND CURRENT_TIME FOL
```

---

## Crash 346: `79d8f49cb193d053` — signal (signal-6)

- **Count:** 1 duplicates
- **Exit code:** -6
- **Sample file:** `6_000075285`

```sql
CREATE TABLE IF NOT EXISTS p(c3 FLOAT UNIQUE); CREATE VIEW IF NOT EXISTS v1 AS SELECT *; SELECT CURRENT_DATE LIKE FALSE ESCAPE FALSE FROM p NATURAL JOIN p WHERE 0; CREATE TABLE seed_t1(c1 INTEGER); IN
```

---
