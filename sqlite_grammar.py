# Auto-generated grammar for sqlite — cve2grammar v0.2
# Source: Manuel Rigger DBMS bugs (https://www.manuelrigger.at/dbms-bugs/)
# Generated: 2026-04-10 00:53 UTC
# Bugs: 179

# === MR-SQLITE-0001 (PQS, fixed) ===
# COLLATE nocase index on a WITHOUT ROWID table malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE test (c1 TEXT PRIMARY KEY) WITHOUT ROWID;
CREATE INDEX index_0 ON test(c1 COLLATE NOCASE);
INSERT INTO test(c1) VALUES ('A');
INSERT INTO test(c1) VALUES ('a');
SELECT * FROM test; -- only one row is fetched""", weight=2.0)

# === MR-SQLITE-0002 (error, fixed (in documentation)) ===
# PRAGMA case_sensitive_like can corrupt some databases
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0);
CREATE INDEX index_0 ON test(c0 LIKE '');
PRAGMA case_sensitive_like=false;
VACUUM;
SELECT * from test; -- Error: malformed database schema (index_0) - non-deterministic functions prohibited in index expressions""", weight=2.0)

# === MR-SQLITE-0003 (error, fixed) ===
# Unique index that uses GLOB does not detect duplicate due to REAL conversion
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0, c1 REAL);
CREATE UNIQUE INDEX index_1 ON test(c0 GLOB c1);
INSERT INTO test(c0, c1) VALUES ('1', '1');
INSERT INTO test(c0, c1) VALUES ('0', '1');
REINDEX; -- Error: UNIQUE constraint failed""", weight=2.0)

# === MR-SQLITE-0004 (error, fixed) ===
# Multi-row insert circumvents index check
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0, c1 TEXT);
CREATE UNIQUE INDEX IF NOT EXISTS index_0 ON test(c1 == FALSE);
CREATE INDEX IF NOT EXISTS index_1 ON test(c0 || FALSE) WHERE c1;
INSERT OR IGNORE INTO test(c0, c1) VALUES ('a', TRUE);
INSERT OR IGNORE INTO test(c0, c1) VALUES ('a', FALSE);
PRAGMA legacy_file_format=true;
REINDEX; -- Error: UNIQUE constraint failed: index 'index_0'""", weight=2.0)

# === MR-SQLITE-0005 (PQS, fixed) ===
# COLLATE NOCASE index on REAL column malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0 REAL);
CREATE INDEX index_0 ON test(c0 COLLATE NOCASE);
INSERT INTO test(c0) VALUES ('+/');
SELECT * FROM test WHERE (c0 LIKE '+/'); -- fetches no row""", weight=2.0)

# === MR-SQLITE-0006 (error, fixed (in documentation)) ===
# UPSERT documentation issue
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0 NOT NULL);
INSERT INTO test(c0) VALUES (NULL) ON CONFLICT DO NOTHING; -- results in an error
INSERT OR IGNORE INTO test(c0) VALUES (NULL); -- does not result in an error""", weight=2.0)

# === MR-SQLITE-0007 (error, fixed) ===
# TYPEOF index on REAL column malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0 REAL);
CREATE UNIQUE INDEX index_0 ON test(TYPEOF(c0));
INSERT OR IGNORE INTO test(c0) VALUES (0.1);
INSERT OR IGNORE INTO test(c0) VALUES (FALSE);
REINDEX; -- UNIQUE constraint failed: index 'index_0'""", weight=2.0)

# === MR-SQLITE-0008 (error, fixed) ===
# Problem with REAL values and string functions used in indexes or on expressions
ctx.rule("Sql-Stmt", """CREATE TABLE test (c0 REAL);
CREATE UNIQUE INDEX index_0 ON test(LENGTH(-c0));
INSERT INTO test(c0) VALUES (0.0), ('10:');
REINDEX; -- UNIQUE constraint failed: index 'index_0'""", weight=2.0)

# === MR-SQLITE-0009 (PQS, fixed) ===
# Incorrect result on a table scan of a partial index
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE INDEX index_0 ON t0(c0) WHERE (~c0) NOT NULL;
INSERT INTO t0(c0) VALUES (NULL);
SELECT * FROM t0 WHERE (LIKELY(~c0) OR TRUE); -- no row fetched""", weight=2.0)

# === MR-SQLITE-0010 (error, fixed) ===
# ALTER TABLE fails when renaming an INTEGER PRIMARY KEY column in a WITHOUT ROWID table
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0 INTEGER, PRIMARY KEY (c0)) WITHOUT ROWID;
ALTER TABLE t0 RENAME COLUMN c0 TO c1; -- no such column: c0""", weight=2.0)

# === MR-SQLITE-0011 (PQS, fixed) ===
# INSERT OR FAIL inserts row although it violates a table constraint
ctx.rule("Sql-Stmt", """PRAGMA foreign_keys=true;
CREATE TABLE t0 (c0 UNIQUE, c1 UNIQUE, FOREIGN KEY(c0) REFERENCES t0(c1));
INSERT OR FAIL INTO t0(c0, c1) VALUES (0, 1), (0, 2);
SELECT * FROM t0; -- returns no row""", weight=2.0)

# === MR-SQLITE-0012 (PQS, fixed) ===
# Incorrect result for "<" and "<=" comparison of rowid and non-numeric text value
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0 INTEGER PRIMARY KEY);
PRAGMA reverse_unordered_selects=true;
INSERT INTO t1(c0) VALUES (0);
INSERT INTO t0(c0) VALUES ('a');
SELECT * FROM t1, t0 WHERE t1.c0 < t0.c0; -- no row is fetched""", weight=2.0)

# === MR-SQLITE-0013 (PQS, fixed) ===
# './' LIKE './' does not match
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT UNIQUE COLLATE NOCASE);
INSERT INTO t0(c0) VALUES ('./');
SELECT * FROM t0 WHERE t0.c0 LIKE './'; -- fetches no rows""", weight=2.0)

# === MR-SQLITE-0014 (PQS, fixed) ===
# Row is not fetched with PRAGMA reverse_unordered_selects=true
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INTEGER PRIMARY KEY);
INSERT INTO t0(c0) VALUES (1);
PRAGMA reverse_unordered_selects=true;
SELECT * FROM t0 WHERE ((t0.c0 > 'a') OR (t0.c0 <= 'a')); -- fetches no row
SELECT ((t0.c0 > 'a') OR (t0.c0 <= 'a')) FROM t0; -- returns 1""", weight=2.0)

# === MR-SQLITE-0015 (error, fixed) ===
# Malformed database image when using a REAL PRIMARY KEY
ctx.rule("Sql-Stmt", """CREATE TABLE t1 (c0, c1 REAL PRIMARY KEY);
INSERT INTO t1(c0, c1) VALUES (TRUE, 9223372036854775807), (TRUE, 0);
UPDATE t1 SET c0 = NULL;
UPDATE OR REPLACE t1 SET c1 = 1;
SELECT DISTINCT * FROM t1 WHERE (t1.c0 IS NULL); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0016 (PQS, fixed) ===
# Incorrect handling of Infinity by the ROUND function
ctx.rule("Sql-Stmt", "SELECT 1e500 >= 1,  CAST(1e500 AS INT) >= CAST(1 AS INT), ROUND(1e500) >= ROUND(1); -- 1|1|0", weight=2.0)

# === MR-SQLITE-0017 (PQS, fixed) ===
# Partial NOT NULL index malfunctions with IS NOT/!=
ctx.rule("Sql-Stmt", """CREATE TABLE IF NOT EXISTS t0 (c0);
CREATE INDEX IF NOT EXISTS i0 ON t0(1) WHERE c0 NOT NULL;
INSERT INTO t0(c0) VALUES(NULL);
SELECT * FROM t0 WHERE t0.c0 IS NOT 1; -- returns no row""", weight=2.0)

# === MR-SQLITE-0018 (PQS, fixed) ===
# REINDEX causes rows not to be fetched in a WITHOUT ROWIDs table and PRIMARY KEY DESC
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0 PRIMARY KEY DESC, c1 UNIQUE DEFAULT NULL) WITHOUT ROWID;
INSERT INTO t0(c0) VALUES (1), (2), (3), (4), (5);
REINDEX;
SELECT * FROM t0 WHERE t0.c0 IN (SELECT c0 FROM t0) AND t0.c1 ISNULL; -- fetches only one row instead of all five rows""", weight=2.0)

# === MR-SQLITE-0019 (PQS, fixed) ===
# PRAGMA reverse_unordered_selects=true results in row not being fetched
ctx.rule("Sql-Stmt", """PRAGMA reverse_unordered_selects=true;
CREATE TABLE t1 (c0, c1); CREATE TABLE t2 (c0 INT UNIQUE);
INSERT INTO t1(c0, c1) VALUES (0, 0), (0, NULL);
INSERT INTO t2(c0) VALUES (1);
SELECT 1, NULL INTERSECT SELECT * FROM (SELECT t2.c0, t1.c1 FROM t1, t2 WHERE ((t2.rowid <= 'a')) OR (t1.c0 <= t2.c0) ORDER BY 'a' DESC LIMIT 100); -- no row is fetched""", weight=2.0)

# === MR-SQLITE-0020 (PQS, fixed) ===
# REAL rounding seems to depend on FROM clause
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0);
CREATE TABLE t1 (c1 REAL);
INSERT INTO t1(c1) VALUES (8366271098608253588);
INSERT INTO t0(c0) VALUES ('a');
SELECT * FROM t1 WHERE (t1.c1 = CAST(8366271098608253588 AS REAL)); -- fetches row
SELECT * FROM t0, t1 WHERE (t1.c1 = CAST(8366271098608253588 AS REAL)); -- fetches no row
SELECT * FROM t0, t1 WHERE (t1.c1 >= CAST(8366271098608253588 AS REAL) AND t1.c1 <= CAST(8366271098608253588 AS REAL)); -- fetches row""", weight=2.0)

# === MR-SQLITE-0021 (error, fixed (in documentation)) ===
# Malformed image when using no journal mode, zero cache size, and failing when creating an index
ctx.rule("Sql-Stmt", """PRAGMA journal_mode=OFF;
PRAGMA main.cache_size=0;
CREATE TABLE IF NOT EXISTS t0 (c0);
CREATE INDEX i0 ON t0(1);
DROP INDEX "i0";
INSERT OR IGNORE INTO t0(c0) VALUES (1), (2);
CREATE UNIQUE INDEX i0 ON t0(1); -- UNIQUE constraint failed: index 'i0'
CREATE UNIQUE INDEX i0 ON t0(1); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0022 (crash, fixed) ===
# Query results in a SEGFAULT
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1, PRIMARY KEY (c0, c1));
CREATE TABLE t1 (c0);
INSERT INTO t1 VALUES (2);
SELECT * FROM t0, t1 WHERE (t0.c1 >= 1 OR t0.c1 < 1) AND t0.c0 IN (1, t1.c0) ORDER BY 1; -- results in a segfault""", weight=3.0)

# === MR-SQLITE-0023 (PQS, fixed) ===
# Index on non-existing column results in a fabricated value being fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c1, c2);
INSERT INTO t0(c1, c2) VALUES  ('a', 1);
CREATE INDEX i0 ON t0("C3");
ALTER TABLE t0 RENAME COLUMN c1 TO c3;
SELECT DISTINCT * FROM t0; -- fetches C3|1 rather than a|1""", weight=2.0)

# === MR-SQLITE-0024 (PQS, fixed) ===
# Nested boolean formula with IN operator computes an incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES ('val');
SELECT * FROM t0 WHERE (((0 IS NOT FALSE) OR NOT (0 IS FALSE OR (t0.c0 IN (-1)))) IS 0); -- fetches no row""", weight=2.0)

# === MR-SQLITE-0025 (error, fixed) ===
# "Malformed database schema" when creating a failing index within a transaction
ctx.rule("Sql-Stmt", """CREATE TABLE IF NOT EXISTS t0(c0);
INSERT INTO t0(c0) VALUES (-9223372036854775808);
BEGIN TRANSACTION;
CREATE INDEX i0 ON t0(ABS(c0)); -- integer overflow (expected)
COMMIT; -- unexpected: the index is still created
CREATE INDEX i0 ON t0(1); -- malformed database schema (i0) - index i0 already exists""", weight=2.0)

# === MR-SQLITE-0026 (PQS, fixed) ===
# CAST('-' AS NUMERIC) computes 0.0
ctx.rule("Sql-Stmt", "SELECT CAST('-' AS NUMERIC); -- unexpected: computes 0.0 rather than 0", weight=2.0)

# === MR-SQLITE-0027 (PQS, fixed) ===
# Incorrect result when subtracting a large integer number from a TEXT value
ctx.rule("Sql-Stmt", "SELECT '' - 2851427734582196970; -- actual: -2851427734582196736, expected: -2851427734582196970", weight=2.0)

# === MR-SQLITE-0028 (PQS, fixed) ===
# CAST to NUMERIC no longer converts to INTEGER
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0 TEXT);
INSERT INTO t0(c0) VALUES ('1.0');
SELECT CAST(c0 AS NUMERIC) FROM t0; -- expected: 1, actual: 1.0""", weight=2.0)

# === MR-SQLITE-0029 (error, fixed) ===
# TEXT value interpreted as column name in an index with empty list in an IN expression
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE INDEX i0 ON t0('1' IN ());
ALTER TABLE t0 RENAME TO t1; -- error in index i0: no such column: 1""", weight=2.0)

# === MR-SQLITE-0030 (PQS, fixed) ===
# LIKE malfunctions for INT PRIMARY KEY COLLATE NOCASE column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT PRIMARY KEY COLLATE NOCASE);
INSERT INTO t0 VALUES (' 1-');
SELECT * FROM t0 WHERE t0.c0 LIKE ' 1-'; -- expected: ' 1-', actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0031 (error, fixed) ===
# Illegal argument to LIKELIHOOD() does not result in error when combined with "IN ()"
ctx.rule("Sql-Stmt", """CREATE TABLE t1 (c0);
CREATE INDEX i0 ON t1((LIKELIHOOD(c0, 100) IN ())); -- unexpected: no error
ALTER TABLE t1 RENAME COLUMN c0 TO c1; -- error occurs only here: second argument to likelihood() must be a constant between 0.0 and 1.0""", weight=2.0)

# === MR-SQLITE-0032 (PQS, fixed) ===
# CAST('.' AS NUMERIC) computes 0.0 rather than 0
ctx.rule("Sql-Stmt", "SELECT -'.'; -- expected: 0, actual: 0.0", weight=2.0)

# === MR-SQLITE-0033 (PQS, fixed (in documentation)) ===
# COLLATE expression has an affinity
ctx.rule("Sql-Stmt", "SELECT ((CAST(1 as INT)) COLLATE BINARY) == '1'; -- expected: 0, actual: 1", weight=2.0)

# === MR-SQLITE-0034 (error, fixed) ===
# Another case of Illegal argument to LIKELIHOOD() does not result in error when combined with "IN ()"
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE INDEX i0 ON t0(((LIKELIHOOD(1, 2)) AND ((1 IN ())))); -- unexpected: no error
ALTER TABLE t0 RENAME TO t1; -- -- error occurs only here: second argument to likelihood() must be a constant between 0.0 and 1.0""", weight=2.0)

# === MR-SQLITE-0035 (PQS, fixed (in documentation)) ===
# -'1.0' computes -1.0 rather than -1
ctx.rule("Sql-Stmt", "SELECT -'1.0'; -- expected: -1, actual: -1.0", weight=2.0)

# === MR-SQLITE-0036 (PQS, fixed) ===
# COLLATE expression in the right side of an IN operator results in an affinity conversion
ctx.rule("Sql-Stmt", "SELECT (1 IN (CAST('1' as TEXT) COLLATE NOCASE)); -- expected: 0, actual: 1", weight=2.0)

# === MR-SQLITE-0037 (PQS, fixed (in documentation)) ===
# Lossless conversion when casting a large TEXT number to NUMERIC is not performed
ctx.rule("Sql-Stmt", "SELECT CAST('8.2250617031974513E18' AS NUMERIC); -- expected: 8225061703197451300, unexpected: 8.22506170319745e+18", weight=2.0)

# === MR-SQLITE-0038 (PQS, fixed) ===
# LIKELY(), UNLIKELY() and LIKELIHOOD() have affinities
ctx.rule("Sql-Stmt", """SELECT LIKELY(CAST(1 AS INT)) = '1'; -- expected: 0, actual: 1
SELECT UNLIKELY(CAST(1 AS INT)) = '1'; -- expected: 0, actual: 1
SELECT LIKELIHOOD(CAST(1 AS INT), 0.5) = '1'; -- expected: 0, actual: 1""", weight=2.0)

# === MR-SQLITE-0039 (PQS, fixed) ===
# IS TRUE operator malfunctions with COLLATE and REAL value
ctx.rule("Sql-Stmt", """SELECT 0.5 IS TRUE COLLATE NOCASE; -- expected: 1, actual: 0
SELECT 0.5 IS TRUE COLLATE RTRIM; -- expected: 1, actual: 0
SELECT 0.5 IS TRUE COLLATE BINARY; -- expected: 1, actual: 0""", weight=2.0)

# === MR-SQLITE-0040 (PQS, fixed) ===
# CAST('-0.0' AS NUMERIC) computes 0.0 rather than 0
ctx.rule("Sql-Stmt", "SELECT CAST('-0.0' AS NUMERIC); -- expected: 0, unexpected: 0.0", weight=2.0)

# === MR-SQLITE-0041 (PQS, fixed (in documentation)) ===
# CAST takes implicit COLLATE of its operand
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE NOCASE);
INSERT INTO t0(c0) VALUES ('a');
SELECT * FROM t0 WHERE CAST(t0.c0 AS TEXT) = 'A'; -- expected: no row is fetched, actual: a""", weight=2.0)

# === MR-SQLITE-0042 (PQS, fixed) ===
# LIKE malfunctions for UNIQUE COLLATE NOCASE column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT UNIQUE COLLATE NOCASE);
INSERT INTO t0(c0) VALUES ('.1%');
SELECT * FROM t0 WHERE t0.c0 LIKE '.1%'; -- expected: '.1%', actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0043 (PQS, fixed) ===
# Built-in RTRIM collating sequence yields incorrect comparisons
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE RTRIM, c1 BLOB UNIQUE, PRIMARY KEY (c0, c1)) WITHOUT ROWID;
INSERT INTO t0 VALUES (123, 3), (' ', 1), ('	', 2), ('', 4);
SELECT * FROM t0 WHERE c1 = 1; -- expected: ' ', 1, actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0044 (PQS, fixed) ===
# COLLATE in BETWEEN expression is ignored
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c3 TEXT);
INSERT INTO t0(c3) VALUES ('0');
SELECT * FROM t0 WHERE (t0.c3 COLLATE NOCASE) BETWEEN 1 AND '5'; -- expected: no row is fetched, actual: row is fetched""", weight=2.0)

# === MR-SQLITE-0045 (error, fixed) ===
# Query with ORDER BY results in "database disk image is malformed" error
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0 REAL, c1);
CREATE UNIQUE INDEX i0 ON t0(c1, 0 | c0);
INSERT INTO t0(c0) VALUES (4750228396194493326), (0);
UPDATE OR REPLACE t0 SET c0 = 'a', c1 = '';
SELECT * FROM t0 ORDER BY t0.c1; -- unexpected: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0046 (PQS, fixed) ===
# ANALYZE causes DISTINCT to malfunction in CROSS JOIN
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1, c2, PRIMARY KEY (c0, c1));
CREATE TABLE t1 (c2);
INSERT INTO t0(c2) VALUES (0), (1), (3), (4), (5), (6), (7), (8), (9), (10), (11);
INSERT INTO t0(c1) VALUES ('a');
INSERT INTO t1(c2) VALUES (0);
ANALYZE;
SELECT DISTINCT t0.c0, t1._rowid_, t0.c1 FROM t1 CROSS JOIN t0 ON TRUE ORDER BY t0.c0; -- expected: |1|, |1|a, actual: |1|""", weight=2.0)

# === MR-SQLITE-0047 (PQS, fixed) ===
# Query with DISTINCT does not fetch all distinct rows
ctx.rule("Sql-Stmt", """CREATE TABLE t1 (c1 , c2, c3, c4 , PRIMARY KEY (c4, c3));
INSERT INTO t1(c3) VALUES (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (NULL), (1), (0);
UPDATE t1 SET c2 = 0;
INSERT INTO t1(c1) VALUES (0), (0), (NULL), (0), (0);
ANALYZE t1;
UPDATE t1 SET c3 = 1;
SELECT DISTINCT * FROM t1 WHERE t1.c3 = 1; -- expected: |0|1|, 0||1|, ||1|, actual: |0|1|""", weight=2.0)

# === MR-SQLITE-0048 (PQS, fixed) ===
# MIN() malfunctions for UNIQUE column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE, c1);
INSERT INTO t0(c0, c1) VALUES (NULL, 1);
SELECT MIN(t0.c0), t0.c1 FROM t0; -- expected: NULL | 1, actual: NULL | NULL""", weight=2.0)

# === MR-SQLITE-0049 (PQS, fixed) ===
# MIN() malfunctions for a query with ISNULL condition
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1);
CREATE INDEX i0 ON t0(c1, c1 + 1 DESC);
INSERT INTO t0(c0) VALUES (1);
SELECT MIN(t0.c1), t0.c0 FROM t0 WHERE t0.c1 ISNULL; -- expected: NULL | 1, actual: NULL | NULL""", weight=2.0)

# === MR-SQLITE-0050 (PQS, fixed) ===
# Unexpected affinity conversion in view
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0, c1 TEXT);
CREATE VIEW v0(c0) AS SELECT SUM(t0.c1) FROM t0;
INSERT INTO t0(c0, c1) VALUES ('a', 1);
SELECT * FROM v0, t0 WHERE t0.c1 <= v0.c0; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0051 (PQS, fixed) ===
# Row is not fetched in SELECT from VIEW
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT, c1);
INSERT INTO t0(c0, c1) VALUES (-1, 0);
CREATE VIEW v0(c0, c1) AS SELECT t0.c0, AVG(t0.c1) FROM t0;
SELECT v0.c1 < v0.c0 FROM v0;""", weight=2.0)

# === MR-SQLITE-0052 (PQS, fixed) ===
# Unexpected affinity conversion for view column in IN operator
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT);
CREATE VIEW v0(c0) AS SELECT t0.c0 FROM t0;
INSERT INTO t0(c0) VALUES ('0');
SELECT 0 IN (c0) FROM v0; -- expected: 0, actual: 1""", weight=2.0)

# === MR-SQLITE-0053 (PQS, fixed) ===
# Incorrect result for query that uses MIN() and a CAST on rowid
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE, c1);
INSERT INTO t0(c1) VALUES (0);
INSERT INTO t0(c0) VALUES (0);
CREATE VIEW v0(c0, c1) AS SELECT t0.c1, t0.c0 FROM t0 WHERE CAST(t0.rowid AS INT) = 1;
SELECT v0.c0, MIN(v0.c1) FROM v0; -- expected: 0|, actual: |""", weight=2.0)

# === MR-SQLITE-0054 (PQS, fixed) ===
# Constant expression in partial index results in row not being fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES (0);
CREATE INDEX i0 ON t0(NULL > c0) WHERE (NULL NOT NULL);
SELECT * FROM t0 WHERE ((NULL IS FALSE) IS FALSE); -- expected: row is fetched: actual: row is not fetched""", weight=2.0)

# === MR-SQLITE-0055 (crash, fixed) ===
# Null pointer dereference caused by window functions in result-set of EXISTS(SELECT ...)
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES (0);
SELECT * FROM t0 WHERE EXISTS (SELECT MIN(c0)  OVER (), CUME_DIST() OVER () FROM t0) BETWEEN 1 AND 1;""", weight=3.0)

# === MR-SQLITE-0056 (PQS, fixed) ===
# LEFT JOIN fails to fetch row
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIEW v0(c0) AS SELECT TYPEOF(1) FROM t0;
INSERT INTO t0(c0) VALUES (0), (1);
SELECT * FROM t0 LEFT JOIN v0 ON t0.c0 WHERE NOT(v0.c0 = 'a'); -- unexpected: fetches no row""", weight=2.0)

# === MR-SQLITE-0057 (PQS, fixed) ===
# WHERE clause erroneously influences value of fetched column from view
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIEW v0(c0) AS SELECT LOWER(CAST('1e500' AS TEXT)) FROM t0;
INSERT INTO t0(c0) VALUES (NULL);
SELECT v0.c0 FROM v0, t0 WHERE t0.rowid NOT IN (0, 0, v0.c0); -- expected: '1e500', actual: Inf""", weight=2.0)

# === MR-SQLITE-0058 (PQS, fixed) ===
# INDEXED BY results in row not being fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1);
CREATE INDEX i0 ON t0(CAST(c0 AS NUMERIC));
INSERT INTO t0(c0, c1) VALUES ('a', -1);
SELECT * FROM t0 INDEXED BY i0 WHERE CAST(t0.c0 AS NUMERIC) > LOWER(t0.c1) GROUP BY t0.rowid; -- expected: row is fetched, actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0059 (PQS, fixed) ===
# DISTINCT malfunctions for IS NULL
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1 NOT NULL DEFAULT 1, c2, PRIMARY KEY (c0, c1));
INSERT INTO t0(c2) VALUES (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL), (NULL);
INSERT INTO t0(c2) VALUES ('a');
ANALYZE t0;
SELECT DISTINCT * FROM t0 WHERE NULL IS t0.c0; -- unexpected: |1|a is not part of the result set""", weight=2.0)

# === MR-SQLITE-0060 (PQS, fixed) ===
# Row is not fetched in table with INTEGER PRIMARY KEY
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INTEGER PRIMARY KEY, c1 TEXT);
INSERT INTO t0(c0, c1) VALUES (1, 'a');
SELECT * FROM t0 WHERE '-1' BETWEEN 0 AND t0.c0; -- expected: 1|a, actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0061 (PQS, fixed) ===
# Row with comparison on TEXT UNIQUE column is not fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT UNIQUE, c1);
INSERT INTO t0(c0) VALUES (-1);
SELECT * FROM t0 WHERE - x'ce' >= t0.c0; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0062 (PQS, fixed) ===
# LIKELY() seems to cause unexpected affinity conversion for rowid
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0);
INSERT INTO t0(c0) VALUES ('a');
SELECT * FROM t0 WHERE LIKELY(t0.rowid) <= '0'; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0063 (NoREC, fixed) ===
# Unexpected affinity conversion is performed for the IN operator
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT UNIQUE);
INSERT INTO t0(c0) VALUES (1);
SELECT * FROM t0 WHERE '1' IN (t0.c0); -- unexpected: fetches row""", weight=2.0)

# === MR-SQLITE-0064 (NoREC, fixed) ===
# Partial index causes row to not be fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES (NULL);
CREATE INDEX i0 ON t0(1) WHERE c0 NOT NULL;
SELECT * FROM t0 WHERE (t0.c0 IS FALSE) IS FALSE; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0065 (NoREC, fixed) ===
# Partial index causes row to not be fetched in BETWEEN expression
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c1);
CREATE INDEX i0 ON t0(1) WHERE c1 NOTNULL;
INSERT INTO t0(c1) VALUES (NULL);
SELECT * FROM t0 WHERE t0.c1 IS FALSE BETWEEN FALSE AND TRUE; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0066 (NoREC, fixed) ===
# Partial index and BETWEEN issue
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0);
CREATE INDEX i0 ON t0(1) WHERE c0 NOT NULL;
INSERT INTO t0(c0) VALUES (NULL);
SELECT * FROM t0 WHERE '' BETWEEN t0.c0 AND 1 IN (FALSE); -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0067 (error, fixed) ===
# REINDEX causes "UNIQUE constraint failed" error
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 REAL UNIQUE, c1);
CREATE UNIQUE INDEX i0 ON t0(0 || c1);
INSERT INTO t0(c0, c1) VALUES (1, 2),  (2, 1);
INSERT INTO t0(c0) VALUES (1) ON CONFLICT(c0) DO UPDATE SET c1=excluded.c0;
REINDEX; -- unexpected: UNIQUE constraint failed: index 'i0'""", weight=2.0)

# === MR-SQLITE-0068 (NoREC, fixed) ===
# Expression computed on row yields incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 REAL, c1 TEXT);
CREATE INDEX i0 ON t0(+c0, c0);
INSERT INTO t0(c0) VALUES(0);
SELECT CAST(+ t0.c0 AS BLOB) LIKE 0 FROM t0; -- expected: 0, actual: 1""", weight=2.0)

# === MR-SQLITE-0069 (NoREC, fixed) ===
# Different rounding when converting TEXT to REAL
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 REAL UNIQUE);
INSERT INTO t0(c0) VALUES(2.07093491255203046E18);
SELECT * FROM t0 WHERE c0 IN ('2070934912552030444') UNION ALL SELECT c0 IN ('2070934912552030444') FROM t0; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0070 (NoREC, fixed) ===
# IS NULL unexpectedly evaluates to TRUE
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT, c1 REAL, c2, PRIMARY KEY(c2, c0, c1));
CREATE INDEX i0 ON t0(c1 IN (c0));
INSERT INTO t0(c0, c2) VALUES (0, NULL) ON CONFLICT(c2, c1, c0) DO NOTHING;
UPDATE t0 SET c2 = x'';
SELECT * FROM t0 WHERE t0.c2 IS NULL; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0071 (NoREC, fixed) ===
# COLLATE NOCASE string comparison yields incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE NOCASE, c1);
CREATE INDEX i0 ON t0(0) WHERE c0 >= c1;
REPLACE INTO t0 VALUES('a', 'B');
SELECT * FROM t0 WHERE t0.c1 <= t0.c0; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0072 (NoREC, fixed) ===
# BETWEEN issue in view
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES('');
CREATE VIEW v2(c0, c1) AS SELECT 'B' COLLATE NOCASE, 'a' FROM t0 ORDER BY t0.c0;
SELECT v2.c1 BETWEEN v2.c0 AND v2.c1 as count FROM v2; -- expected: 1, actual: 0""", weight=2.0)

# === MR-SQLITE-0073 (NoREC, fixed) ===
# COLLATE issue in view
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE NOCASE);
INSERT INTO t0(c0) VALUES ('B');
CREATE VIEW v0(c0, c1) AS SELECT DISTINCT t0.c0, 'a' FROM t0;
SELECT * FROM v0 WHERE v0.c1 >= v0.c0; -- unexpected: no row is fetched""", weight=2.0)

# === MR-SQLITE-0074 (NoREC, fixed) ===
# GLOB unexpectedly does not match
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE);
INSERT INTO t0 VALUES (-1);
SELECT * FROM t0 WHERE t0.c0 GLOB '-*'; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0075 (NoREC, fixed) ===
# Row is not fetched when using WHERE clause with INSTR()
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 PRIMARY KEY, c1);
INSERT INTO t0(c0) VALUES (x'bb'), (0);
SELECT COUNT(*) FROM t0 WHERE INSTR(x'aabb', t0.c0) ORDER BY t0.c0, t0.c1; -- 1
SELECT * FROM t0 WHERE INSTR(x'aabb', t0.c0) ORDER BY t0.c0, t0.c1; -- no row is fetched""", weight=2.0)

# === MR-SQLITE-0076 (NoREC, fixed) ===
# Comparison on view malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0(c0) VALUES (0);
CREATE VIEW v0(c0) AS SELECT t0.rowid FROM t0 ORDER BY 1;
SELECT COUNT(*) FROM v0 WHERE ABS('1') = v0.c0; -- expected: 1, actual: 0""", weight=2.0)

# === MR-SQLITE-0077 (error, fixed) ===
# FTS integrity-check malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
BEGIN TRANSACTION;
INSERT INTO vt0(c0) VALUES (NULL);
ALTER TABLE t0 ADD COLUMN c5 REAL;
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- unexpected: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0078 (error, fixed) ===
# FTS pgsz option results in "database disk image is malformed" error
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(a);
PRAGMA reverse_unordered_selects = true;
INSERT INTO vt0 VALUES('365062398'), (0), (0);
INSERT INTO vt0(vt0, rank) VALUES('pgsz', '38');
UPDATE vt0 SET a = 399905135; -- unexpected: database disk image is malformed
INSERT INTO vt0(vt0) VALUES('integrity-check');""", weight=2.0)

# === MR-SQLITE-0079 (error, fixed) ===
# FTS rebuild in transaction causes integrity-check to fail
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0(c0) VALUES (NULL);
BEGIN TRANSACTION;
INSERT INTO vt0(vt0) VALUES('rebuild');
INSERT INTO vt0(vt0) VALUES('rebuild');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0080 (error, fixed) ===
# FTS integrity-check indicates that the database disk image is malformed
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0, c1);
INSERT INTO vt0(vt0, rank) VALUES('pgsz', '70000');
INSERT INTO vt0(c0) VALUES (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0);
UPDATE vt0 SET c1 = 'T,D&p^y/7#3*v<b<4j7|f';
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0081 (error, fixed) ===
# FTS rebuild in combination with crisismerge results in error "database or disk is full"
ctx.rule("Sql-Stmt", """PRAGMA reverse_unordered_selects = true;
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0(vt0, rank) VALUES('crisismerge', 2000);
INSERT INTO vt0(vt0, rank) VALUES('automerge', 0);
INSERT INTO vt0(c0) VALUES (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0),(0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0), (0);
INSERT INTO vt0(vt0) VALUES('rebuild'); -- database or disk is full""", weight=2.0)

# === MR-SQLITE-0082 (NoREC, fixed) ===
# LEFT JOIN in view malfunctions
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c1);
CREATE TABLE t1(c0);
CREATE VIEW v0 AS SELECT c1 FROM t1 LEFT JOIN t0;
INSERT INTO t1 VALUES (1);
SELECT * FROM v0 WHERE NOT(v0.c1 IS FALSE); -- expected: row is fetched, actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0083 (NoREC, fixed) ===
# LEFT JOIN in view malfunctions with NOTNULL
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c1);
INSERT INTO t0(c0) VALUES(0);
CREATE VIEW v0(c0) AS SELECT t1.c1 FROM t0 LEFT JOIN t1;
SELECT * FROM v0 WHERE v0.c0 NOTNULL NOTNULL; -- expected: row is fetched, actual: no row is fetched""", weight=2.0)

# === MR-SQLITE-0084 (error, fixed) ===
# FTS order=DESC results into integrity-check failing
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts4(c0, order=DESC);
INSERT INTO vt0(c0) VALUES (0), (0);
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0085 (error, fixed) ===
# FTS integrity-check malfunctions for transaction and the prefix option
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts4(c0, prefix=1);
BEGIN;
INSERT INTO vt0 VALUES (0);
INSERT INTO vt0(vt0) VALUES('optimize');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0086 (error, fixed) ===
# FTS integrity_check fails when inserting x'00'
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts4(c0);
INSERT INTO vt0 VALUES (x'00');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0087 (error, fixed) ===
# Trigger inserts duplicate value in UNIQUE column
ctx.rule("Sql-Stmt", """PRAGMA recursive_triggers = true;
CREATE TABLE t0(c0 UNIQUE);
CREATE TRIGGER tr0 AFTER DELETE ON t0 BEGIN INSERT INTO t0 VALUES(0); END;
INSERT OR REPLACE INTO t0(c0) VALUES(0), (0);
REINDEX; -- UNIQUE constraint failed: t0.c0""", weight=2.0)

# === MR-SQLITE-0088 (hang, fixed) ===
# FTS merge does not terminate
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts4(c0, order=DESC);
INSERT INTO vt0(c0) VALUES (0);
INSERT INTO vt0(c0) VALUES (0);
UPDATE vt0 SET c0 = NULL;
INSERT INTO vt0(vt0) VALUES('merge=1,4'); -- unexpected: does not terminate""", weight=2.5)

# === MR-SQLITE-0089 (NoREC, fixed) ===
# Comparison of row values results in incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE NOCASE, c1);
INSERT INTO t0 VALUES('a', 'A');
SELECT * FROM t0 WHERE (+ t0.c1, 1) >= (t0.c0, 1); -- expected: row is not fetched, actual: row is fetched""", weight=2.0)

# === MR-SQLITE-0090 (NoREC, fixed) ===
# Comparison of row values results in incorrect result (incomplete fix)
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 COLLATE NOCASE, c1);
INSERT INTO t0 VALUES('a', 'A');
SELECT * FROM t0 WHERE (+ t0.c1, 1) >= (t0.c0, 1); -- expected: row is not fetched, actual: row is fetched""", weight=2.0)

# === MR-SQLITE-0091 (NoREC, fixed) ===
# Row value comparison yields incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT PRIMARY KEY);
INSERT INTO t0(c0) VALUES ('');
SELECT * FROM t0 WHERE (t0.c0, TRUE) > (CAST('' AS REAL), FALSE); -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0092 (NoREC, fixed) ===
# Comparison of row values with COLLATE NOCASE yields incorrect result
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE);
INSERT INTO t0(c0) VALUES('a');
SELECT * FROM t0 WHERE (t0.c0, 0) < ('B' COLLATE NOCASE, 0); -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0093 (crash, fixed) ===
# Crash on REPLACE INTO of a table with an AFTER DELETE trigger
ctx.rule("Sql-Stmt", """PRAGMA recursive_triggers = true;
CREATE TABLE t0(c0, c1, c2 UNIQUE);
CREATE UNIQUE INDEX i0 ON t0(c1) WHERE c0;
CREATE TRIGGER tr0 AFTER DELETE ON t0 BEGIN DELETE FROM t0; END;
INSERT INTO t0(c2) VALUES(-1572226132);
INSERT INTO t0(c0) VALUES(1), (1);
REPLACE INTO t0(c0, c1, c2) VALUES(2, 0, 0xffffffffa249bbac); -- unexpected: SEGFAULT""", weight=3.0)

# === MR-SQLITE-0094 (error, fixed) ===
# FTS integrity-check malfunctions nondeterministically with tokenize="ascii"
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0, tokenize = "ascii", prefix = 1);
INSERT INTO vt0(c0) VALUES (x'd1');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- unexpected error: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0095 (NoREC, fixed) ===
# Trigger causes query to compute incorrect result
ctx.rule("Sql-Stmt", """PRAGMA temp.recursive_triggers = true;
CREATE TABLE t0(c0, c1 UNIQUE);
CREATE TRIGGER c DELETE ON t0
	BEGIN INSERT INTO t0(c1) VALUES(1);
END;
INSERT INTO t0(c1) VALUES(0);
REPLACE INTO t0(c1) VALUES (0);
SELECT t0.c1 BETWEEN 0 AND (CASE WHEN 1 THEN 1 ELSE t0.c0 END NOT NULL) FROM t0; -- expected: 1 and 1, actual: 1""", weight=2.0)

# === MR-SQLITE-0096 (error, fixed) ===
# REINDEX causes "UNIQUE constraint failed" error for generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0, c1 TEXT GENERATED ALWAYS AS (1) UNIQUE);
INSERT INTO t0(c0) VALUES (1);
REINDEX;
INSERT INTO t0(c0) VALUES (0);
REINDEX; -- unexpected: UNIQUE constraint failed""", weight=2.0)

# === MR-SQLITE-0097 (crash, fixed) ===
# Segfault in table with generated columns
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INTEGER PRIMARY KEY GENERATED ALWAYS AS(1), c1 UNIQUE GENERATED ALWAYS AS(1), c2 UNIQUE);
INSERT INTO t0 VALUES(NULL); -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0098 (crash, fixed) ===
# Segfault when updating table with generated columns
ctx.rule("Sql-Stmt", """PRAGMA temp_store = MEMORY;
CREATE TEMP TABLE t0(c0, c1 AS(1) CHECK(NULL) UNIQUE NOT NULL, c2 CHECK(1.0) PRIMARY KEY) WITHOUT ROWID;
CREATE UNIQUE INDEX e ON t0(CAST(0.0 AS INT)) WHERE 0;
REINDEX;
INSERT INTO t0(c2) VALUES (0), (1);
REPLACE INTO t0(c2, c0) VALUES (0, 0), (x'9b', NULL);
UPDATE t0 SET c2 = 0; -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0099 (error, fixed) ===
# VACUUM issue on table with generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS(1));
CREATE INDEX i0 ON t0(0 DESC);
PRAGMA legacy_file_format = true;
VACUUM; -- table vacuum_db.t0 has 0 columns but 1 values were supplied""", weight=2.0)

# === MR-SQLITE-0100 (error, fixed) ===
# VACUUM on table with generated column results in an error
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS(1), c1);
PRAGMA legacy_file_format = true;
CREATE INDEX i0 ON t0(0 DESC);
VACUUM; -- table vacuum_db.t0 has 1 columns but 2 values were supplied""", weight=2.0)

# === MR-SQLITE-0101 (error, fixed) ===
# VACUUM on table with generated column that uses TYPEOF results in an error
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS(TYPEOF(c1)), c1);
INSERT INTO t0(c1) VALUES(0);
VACUUM; -- table vacuum_db.t0 has 1 columns but 2 values were supplied""", weight=2.0)

# === MR-SQLITE-0102 (crash, fixed) ===
# Segfault in table with generated column and foreign key
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0, c1, c2 AS(1), PRIMARY KEY(c0) FOREIGN KEY(c2) REFERENCES t0);
CREATE VIRTUAL TABLE vt0 USING fts4;
CREATE INDEX i0 ON t0(c2, 0 BETWEEN '' AND c1 COLLATE BINARY, CASE '' WHEN c3 THEN 0 WHEN 0 THEN 0 WHEN '' THEN 0 WHEN 0 THEN c0 ELSE c1 END);
INSERT INTO t0 VALUES (0, 0), ('', 0);
PRAGMA foreign_keys = true;
ANALYZE;
UPDATE t0 SET c1 = c0; -- unexpected: Segmentation fault""", weight=3.0)

# === MR-SQLITE-0103 (crash, fixed) ===
# REPLACE causes segfault in table with generated column and foreign key
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1 a UNIQUE AS (1), c2, c3, FOREIGN KEY(c3) REFERENCES t0(c1));
CREATE VIRTUAL TABLE vt0 USING fts4(c0);
PRAGMA foreign_keys = true;
INSERT INTO vt0 VALUES (0);
REPLACE INTO t0(c3, c2, c0) VALUES (0, 0, 0), (0, 0, 0); -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0104 (NoREC, fixed) ===
# Incorrect result for GLOB operator
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE INDEX i0 ON t0(0) WHERE c0 GLOB c0;
INSERT INTO t0 VALUES (0);
CREATE UNIQUE INDEX i1 ON t0(0);
CREATE UNIQUE INDEX i2 ON t0(0);
REPLACE INTO t0 VALUES(0);
SELECT COUNT(*) FROM t0 WHERE t0.c0 GLOB t0.c0; -- expected: 1, actual: 2""", weight=2.0)

# === MR-SQLITE-0105 (NoREC, fixed) ===
# LEFT JOIN in view malfunctions with partial index on table
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0);
INSERT INTO t1(c0) VALUES (0);
CREATE INDEX i0 ON t0(0) WHERE NULL IN (c0);
CREATE VIEW v0(c0) AS SELECT t0.c0 FROM t1 LEFT JOIN t0;
SELECT COUNT(*) FROM v0 WHERE NULL IN (v0.c0); -- expected: 0, actual: 1""", weight=2.0)

# === MR-SQLITE-0106 (error, fixed) ===
# PRAGMA integrity_check fails due to CHECK constraint even without records
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 CHECK(ABS(-9223372036854775808)));
PRAGMA integrity_check; -- unexpected: integer overflow""", weight=2.0)

# === MR-SQLITE-0107 (NoREC, fixed) ===
# Row value comparison malfunctions on view with left join
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0);
CREATE VIEW v0(c0) AS SELECT t0.c0 FROM t1 LEFT JOIN t0;
INSERT INTO t1(c0) VALUES (0);
SELECT * FROM v0 WHERE (v0.c0, x'') != (NULL, 0); -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0108 (crash, fixed) ===
# REPLACE on table with generated NOT NULL column results in segfault
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 NOT NULL AS(c1), c1);
REPLACE INTO t0(c1) VALUES(NULL); -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0109 (NoREC, fixed) ===
# NULL WHERE condition unexpectedly results in row being fetched
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0 GENERATED ALWAYS AS (1), c1 UNIQUE, c2 UNIQUE);
INSERT INTO t0(c1) VALUES (1);
SELECT * FROM t0 WHERE 0 = t0.c2 OR t0.c1 BETWEEN t0.c2 AND 1; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0110 (crash, fixed) ===
# Segfault when inserting into table with generated columns
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS ((c4, 9, c4) < ('a', c1, 1)), c1 AS (1) NOT NULL, c2, c3 CHECK  ((x'56', 0) = (c1, 0)), c4 NOT NULL);
PRAGMA integrity_check;
INSERT INTO t0 VALUES (0, 0, 0), (0, 0, 0); -- unexpected: Segmentation fault""", weight=3.0)

# === MR-SQLITE-0111 (crash, fixed) ===
# UPDATE on table with two generated columns and CHECK clause results in segfault
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0, c1 AS(c0 + c2), c2 AS(c1) CHECK(c2));
UPDATE t0 SET c0 = NULL; -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0112 (error, fixed) ===
# VACUUM results in "database disk image is malformed" for PRIMARY KEY with duplicate column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0, c1 UNIQUE COLLATE NOCASE, PRIMARY KEY(c1, c1)) WITHOUT ROWID;
INSERT INTO t0(c1) VALUES(0);
VACUUM; -- unexpected: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0113 (NoREC, fixed) ===
# DISTINCT malfunctions for VIEW with virtual table
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO t0(c0) VALUES (1), (0);
INSERT INTO vt0(c0) VALUES (0), (0);
CREATE VIEW v0 AS SELECT DISTINCT t0.c0 FROM vt0, t0 ORDER BY vt0.rowid;
SELECT * FROM v0; -- unexpected: 4 rows are fetched""", weight=2.0)

# === MR-SQLITE-0114 (NoREC, fixed) ===
# LEFT JOIN malfunctions with partial ISNULL index
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0);
CREATE INDEX i0 ON t0(1) WHERE c0 ISNULL;
INSERT INTO t0(c0) VALUES (1);
INSERT INTO t1(c0) VALUES (1);
SELECT * FROM t1 LEFT JOIN t0 WHERE t0.c0 ISNULL; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0115 (NoREC, fixed) ===
# Incorrect result for TEXT comparison on rtree table
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
INSERT INTO rt0(c2) VALUES(NULL);
SELECT * FROM rt0 WHERE rt0.c2 >= 'a'; -- unexpected: fetches row""", weight=2.0)

# === MR-SQLITE-0116 (NoREC, fixed) ===
# column = NULL predicate evaluates to TRUE for rtree table
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
INSERT INTO rt0(c0) VALUES(0);
SELECT * FROM rt0 WHERE rt0.c0 = NULL; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0117 (NoREC, fixed) ===
# Join on two rtree tables malfunctions
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, a, b);
CREATE VIRTUAL TABLE rt1 USING rtree(c0, a, b);
INSERT INTO rt1(c0) VALUES (x'00');
INSERT INTO rt0(c0) VALUES ('a');
SELECT rt0.c0 = CAST(rt1.c0 AS TEXT) FROM rt1, rt0;""", weight=2.0)

# === MR-SQLITE-0118 (NoREC, fixed) ===
# Row value comparison malfunctions with rtree table
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
INSERT INTO rt0(c2) VALUES(NULL);
INSERT INTO t0 VALUES(0);
SELECT * FROM rt0, t0 WHERE (t0.c0, 0) > (rt0.c2, 0); -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0119 (NoREC, fixed) ===
# Comparison on INT column in rtree table malfunctions
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2 INT);
INSERT INTO rt0(c2) VALUES(0);
SELECT * FROM rt0 WHERE '0' = rt0.c2; -- unexpected: row is not fetched""", weight=2.0)

# === MR-SQLITE-0120 (NoREC, fixed) ===
# Incorrect result for predicate on rtree table
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
INSERT INTO rt0(c1) VALUES(0);
SELECT 1 FROM rt0 WHERE rt0.c1 > '-1' UNION ALL SELECT rt0.c1 > '-1' FROM rt0;""", weight=2.0)

# === MR-SQLITE-0121 (NoREC, fixed (in documentation)) ===
# NOT NULL auxiliary column in rtree table malfunctions
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2, +c3 NOT NULL);
INSERT INTO rt0(c3) VALUES(NULL); -- unexpected: inserting NULL succeeds
SELECT 0 in (rt0.c3) ISNULL FROM rt0; -- expected: 1, actual: 0""", weight=2.0)

# === MR-SQLITE-0122 (crash, fixed) ===
# CREATE VIRTUAL TABLE causes segfault
ctx.rule("Sql-Stmt", "CREATE VIRTUAL TABLE vt0 USING rtree;", weight=3.0)

# === MR-SQLITE-0123 (crash, fixed) ===
# Generated column and foreign key causes a segfault
ctx.rule("Sql-Stmt", """PRAGMA cache_size = 100000;
PRAGMA foreign_keys = true;
CREATE TEMP TABLE t0(c0, c1 INTEGER PRIMARY KEY AUTOINCREMENT CHECK (c0), c2 BLOB NOT NULL CHECK (LTRIM(1)) UNIQUE DEFAULT '0000000000000'
COLLATE BINARY, c3 BLOB UNIQUE NOT NULL ON CONFLICT ABORT CHECK ((''IN (c0, NULL, c1))) GENERATED ALWAYS AS (1), FOREIGN KEY(c1) REFERENCES t0(c2) ON DELETE CASCADE);
CREATE UNIQUE INDEX i0 ON t0(0, 0, 0);
CREATE UNIQUE INDEX i1 ON t0(0, 0, 0);
CREATE UNIQUE INDEX i2 ON t0(0, 0, c1);
CREATE UNIQUE INDEX i3 ON t0(0, 0, c1);
CREATE UNIQUE INDEX i4 ON t0(c0, 0, c2);
CREATE INDEX i5 ON t0(0, CASE WHEN 1 THEN 1 WHEN c2 THEN c1 END, 0);
VACUUM;
INSERT OR REPLACE INTO t0(c0, c1) VALUES (2, 1), (1, 0); -- segfault""", weight=3.0)

# === MR-SQLITE-0124 (error, fixed) ===
# Query on table without rows and generated column results in "out of memory" error
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS (1), c1);
CREATE TABLE t1(c0);
SELECT * FROM t0, t1 WHERE t0.c0 == 0; -- out of memory""", weight=2.0)

# === MR-SQLITE-0125 (hang, fixed) ===
# PRAGMA integrity_check does not terminate on table with generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0 (c0, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0));
INSERT INTO t0(c0) VALUES (0);
PRAGMA integrity_check; -- hangs""", weight=2.5)

# === MR-SQLITE-0126 (crash, fixed) ===
# LEFT JOIN segfault on rtree table
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE VIRTUAL TABLE vt0 USING rtree(c0, c1, c2);
INSERT INTO t0(c0) VALUES(0);
SELECT * FROM t0 LEFT JOIN vt0 ON c2 IN (0) WHERE c1 IN (NULL);""", weight=3.0)

# === MR-SQLITE-0127 (error, fixed) ===
# REINDEX results in "UNIQUE constraint failed" for generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS (0 = UNLIKELY(c1)) UNIQUE, c1 TEXT);
INSERT INTO t0(c1) VALUES (1), (0);
REINDEX; -- UNIQUE constraint failed: t0.c0""", weight=2.0)

# === MR-SQLITE-0128 (error, fixed) ===
# FTS database disk image is malformed for UTF-16 encoding after update
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF-16';
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0 VALUES (x'46f0');
UPDATE vt0 SET c0=NULL;
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0129 (crash, fixed) ===
# REINDEX segfaults on table with generated columns
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 AS(1 >= 1), c1 UNIQUE AS(TYPEOF(c0)), c2);
CREATE VIRTUAL TABLE t1 USING fts4;
INSERT INTO t0 VALUES(0);
REINDEX; -- segfault""", weight=3.0)

# === MR-SQLITE-0130 (NoREC, fixed) ===
# LEFT JOIN malfunctions with generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0, c1 AS(1));
INSERT INTO t0 VALUES(0);
SELECT t1.c1 IS TRUE FROM t0 LEFT JOIN t1; -- expected: 0, actual: 1""", weight=2.0)

# === MR-SQLITE-0131 (error, fixed) ===
# UPDATE causes "database table is locked" for rtree table
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE t0 USING rtree(c0, c1, c2);
INSERT INTO t0(c1) VALUES(0), (0);
UPDATE t0 SET c0 = (SELECT 1 FROM t0); -- unexpected: database table is locked""", weight=2.0)

# === MR-SQLITE-0132 (crash, fixed) ===
# FILTER clause in window function causes a segfault
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0, c1 UNIQUE);
INSERT INTO t0(c0) VALUES(NULL);
SELECT COUNT(*) FROM t0, t1 WHERE (SELECT AVG(0) FILTER(WHERE t1.c1)); -- segmentation fault""", weight=3.0)

# === MR-SQLITE-0133 (NoREC, fixed) ===
# Incorrect result for BETWEEN and generated column
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 REAL AS(1) UNIQUE, c1 INT);
INSERT INTO t0 VALUES('');
SELECT * FROM t0 WHERE (1 BETWEEN CAST(t0.c0 AS TEXT) AND t0.c0); -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0134 (error, fixed) ===
# FTS database disk image is malformed for UTF-16 encoding
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF-16';
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0 VALUES (x'3078');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0135 (error, fixed) ===
# FTS database disk image is malformed for update on languageid
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts4(c0, languageid="lid");
INSERT INTO vt0 VALUES (0), (1);
BEGIN;
UPDATE vt0 SET lid = 1;
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- unexpected: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0136 (crash, fixed) ===
# Debug assertion sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Str)==0 || (pMem->n==pX->n && pMem->z==pX->z)' failed
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF16';
CREATE TABLE t0(c0 REAL, c1);
INSERT INTO t0(c0) VALUES (''), (0);
CREATE INDEX i0 ON t0(c1) WHERE c0 GLOB 3;
UPDATE t0 SET c1=0; -- sqlite3.c:75871: sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Str)==0 || (pMem->n==pX->n && pMem->z==pX->z)' failed.""", weight=3.0)

# === MR-SQLITE-0137 (crash, fixed) ===
# Debug assertion fts5StructureRead: Assertion `p->iStructVersion!=0' failed
ctx.rule("Sql-Stmt", """PRAGMA locking_mode = EXCLUSIVE;
PRAGMA journal_mode = PERSIST;
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0(vt0) VALUES('integrity-check');
INSERT INTO vt0(vt0, rank) VALUES('usermerge', 2); -- sqlite3.c:213961: fts5StructureRead: Assertion `p->iStructVersion!=0' failed.""", weight=3.0)

# === MR-SQLITE-0138 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `memIsValid(pRec)' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE);
INSERT INTO t0 VALUES(0);
SELECT * FROM t0 WHERE (0, t0.c0) IN(SELECT DENSE_RANK() OVER(), LAG(0) OVER() FROM t0); -- sqlite3.c:87244: sqlite3VdbeExec: Assertion `memIsValid(pRec)' failed.""", weight=3.0)

# === MR-SQLITE-0139 (crash, fixed) ===
# SELECT on window function causes a segfault
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE);
SELECT * FROM t0 WHERE(c0, 0) IN(SELECT FIRST_VALUE(0) OVER(), 0); -- Segmentation fault""", weight=3.0)

# === MR-SQLITE-0140 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `flags3==pIn3->flags' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 CHECK(c1 IN(c1)), c1 INT);
INSERT INTO t0(c1) VALUES('0'); -- sqlite3.c:86300: sqlite3VdbeExec: Assertion `flags3==pIn3->flags' failed.""", weight=3.0)

# === MR-SQLITE-0141 (crash, fixed) ===
# Debug assertion sqlite3ExprSkipCollateAndLikely: Assertion `pExpr->op==TK_COLLATE' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE INDEX i0 ON t0((c0 NOTNULL) COLLATE BINARY);
SELECT * FROM t0 WHERE(c0 NOTNULL) COLLATE BINARY BETWEEN 0 AND c0; -- sqlite3.c:98025: sqlite3ExprSkipCollateAndLikely: Assertion `pExpr->op==TK_COLLATE' failed.""", weight=3.0)

# === MR-SQLITE-0142 (crash, fixed) ===
# Debug assertion constructAutomaticIndex: Assertion `!ExprHasProperty(pExpr, EP_FromJoin) || pExpr->iRightJoinTable!=pSrc->iCursor || pLoop->prereq!=0' failed
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0);
CREATE TABLE t0(c0);
CREATE VIEW v0(c0) AS SELECT 0 GROUP BY 1;
SELECT * FROM v0, t0 LEFT JOIN vt0 ON vt0.c0 MATCH 1 WHERE v0.c0 == 0; -- sqlite3.c:143296: constructAutomaticIndex: Assertion `!ExprHasProperty(pExpr, EP_FromJoin) || pExpr->iRightJoinTable!=pSrc->iCursor || pLoop->prereq!=0' failed.""", weight=3.0)

# === MR-SQLITE-0143 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `pIn1!=pIn3' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT, CHECK(c0 IN (c0)));
INSERT INTO t0 VALUES(0);
UPDATE t0 SET c0 = 0; -- sqlite3.c:86323: sqlite3VdbeExec: Assertion `pIn1!=pIn3' failed.""", weight=3.0)

# === MR-SQLITE-0144 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `flags3==pIn3->flags' failed (2)
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT, CHECK(CASE c0 WHEN c0 THEN 0 END));
INSERT INTO t0 VALUES('0'); -- sqlite3.c:86300: sqlite3VdbeExec: Assertion `flags3==pIn3->flags' failed.""", weight=3.0)

# === MR-SQLITE-0145 (crash, fixed) ===
# Debug assertion sqlite3MemCompare: Assertion `pMem1->enc==pMem2->enc || pMem1->db->mallocFailed' failed
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF16';
CREATE VIRTUAL TABLE t0 USING fts5(c0);
INSERT INTO t0(c0) VALUES (x'00');
SELECT * FROM t0 WHERE CAST(SUBSTR(c0, 0) AS TEXT) > 0; -- sqlite3.c:81076: sqlite3MemCompare: Assertion `pMem1->enc==pMem2->enc || pMem1->db->mallocFailed' failed.""", weight=3.0)

# === MR-SQLITE-0146 (crash, fixed) ===
# Debug assertion sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Str)==0 || (pMem->n==pX->n && pMem->z==pX->z)' failed (2)
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF16';
CREATE TABLE t0(c0 TEXT);
CREATE INDEX i0 ON t0(0 LIKE COALESCE(c0, 0));
INSERT INTO t0(c0) VALUES (0), (0); -- sqlite3.c:75871: sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Str)==0 || (pMem->n==pX->n && pMem->z==pX->z)' failed.""", weight=3.0)

# === MR-SQLITE-0147 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `pC!=0' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE);
SELECT * FROM t0 WHERE (t0.c0, 1) IN(SELECT NTILE(1) OVER(), 0 FROM t0); -- sqlite3.c:90197: sqlite3VdbeExec: Assertion `pC!=0' failed.""", weight=3.0)

# === MR-SQLITE-0148 (crash, fixed) ===
# Debug assertion impliesNotNullRow: Assertion `pWalker->eCode==0' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
CREATE TABLE t1(c0);
SELECT * FROM t0 LEFT JOIN t1 WHERE (t1.c0 BETWEEN 0 AND 0) > ('' AND t0.c0); -- sqlite3.c:103271: impliesNotNullRow: Assertion `pWalker->eCode==0' failed.""", weight=3.0)

# === MR-SQLITE-0149 (crash, fixed) ===
# Debug assertion rtreeRelease: Assertion `pRtree->nNodeRef==0 || pRtree->bCorrupt' failed
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
CREATE TABLE t0(c0);
INSERT INTO t0 VALUES (0), (1);
INSERT INTO rt0(c0) VALUES (0), (1);
CREATE VIEW v0 AS SELECT 0 LIMIT 0;
SELECT * FROM t0 LEFT JOIN rt0 INNER JOIN v0; -- sqlite3.c:185720: rtreeRelease: Assertion `pRtree->nNodeRef==0 || pRtree->bCorrupt' failed.""", weight=3.0)

# === MR-SQLITE-0150 (error, fixed) ===
# FTS database disk image is malformed for special characters in table
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt1 USING fts5(c1, c2, prefix = 1, tokenize = "porter ascii");
INSERT INTO vt1 VALUES (x'e4', '+ä¬+');
INSERT INTO vt1(vt1) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0151 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `pIn1!=pIn3' failed (2)
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 TEXT, CHECK(c0 BETWEEN 0 AND +c0));
INSERT INTO t0 VALUES (0);
UPDATE t0 SET c0 = 0; -- sqlite3.c:86402: sqlite3VdbeExec: Assertion `pIn1!=pIn3' failed.""", weight=3.0)

# === MR-SQLITE-0152 (error, fixed (in documentation)) ===
# UPDATE with complex WHERE condition on rtree results in "database table is locked" error
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE rt0 USING rtree(c0, c1, c2);
INSERT INTO rt0(c0) VALUES (0), (1), (2);
UPDATE rt0 SET c0 = 0 WHERE(SELECT ROW_NUMBER() OVER() FROM rt0); -- database table is locked""", weight=2.0)

# === MR-SQLITE-0153 (crash, fixed) ===
# Debug assertion sqlite3Fts5HashScanNext: Assertion `!sqlite3Fts5HashScanEof(p)' failed
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0, prefix = 71, tokenize = "porter ascii", prefix = 9);
BEGIN;
INSERT INTO vt0(c0) VALUES (x'e9');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- sqlite3.c:213028: sqlite3Fts5HashScanNext: Assertion `!sqlite3Fts5HashScanEof(p)' failed""", weight=3.0)

# === MR-SQLITE-0154 (error, fixed) ===
# FTS database disk image is malformed for UTF-16 encoding and integrity check
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF-16';
CREATE VIRTUAL TABLE vt0 USING fts5(c0, c1);
INSERT INTO vt0(vt0, rank) VALUES('pgsz', '37');
INSERT INTO vt0(c0, c1) VALUES (0.66077, 1957391816);
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- unexpected: database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0155 (crash, fixed) ===
# Debug assertion fts5CheckTransactionState: Assertion `iSavepoint<=p->ts.iSavepoint' failed
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0);
CREATE VIRTUAL TABLE vt1 USING fts4(c0);
INSERT INTO vt1(c0) VALUES(0);
BEGIN;
UPDATE vt1 SET c0 = 0;
INSERT INTO vt1(c0) VALUES (0), (0);
UPDATE vt0 SET c0 = 0;
INSERT INTO vt1(c0) VALUES (0);
UPDATE vt1 SET c0 = 0;
INSERT INTO vt1(vt1) VALUES('automerge=1');
UPDATE vt1 SET c0 = 0;
DROP TABLE vt1; -- sqlite3.c:219981: fts5CheckTransactionState: Assertion `iSavepoint<=p->ts.iSavepoint' failed""", weight=3.0)

# === MR-SQLITE-0156 (crash, fixed) ===
# Debug assertion sqlite3TableColumnAffinity: Assertion `iCol<pTab->nCol' failed.
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE t0 USING rtree(c0, c1, c2);
SELECT * FROM t0 WHERE ((0, 0) IN (SELECT COUNT(*), LAG(5) OVER(PARTITION BY 0) FROM t0), 0) <= (t0.c1, 0); -- sqlite3.c:98053: sqlite3TableColumnAffinity: Assertion `iCol<pTab->nCol' failed.""", weight=3.0)

# === MR-SQLITE-0157 (crash, fixed) ===
# Debug assertion sqlite3BtreeInsert: Assertion `pCur->curFlags & BTCF_ValidNKey' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 UNIQUE AS(0), c1, c2);
INSERT INTO t0(c1) VALUES(0);
UPDATE t0 SET c1 = 0, c2 = 0 WHERE(c0) >= 0; -- sqlite3.c:72305: sqlite3BtreeInsert: Assertion `pCur->curFlags & BTCF_ValidNKey' failed.""", weight=3.0)

# === MR-SQLITE-0158 (crash, fixed) ===
# Debug assertion sqlite3FinishCoding: Assertion `!pParse->isMultiWrite || sqlite3VdbeAssertMayAbort(v, pParse->mayAbort)' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 PRIMARY KEY, c1, c2 UNIQUE) WITHOUT ROWID;
INSERT OR FAIL INTO t0(c2) VALUES (0), (NULL) ON CONFLICT(c2) DO UPDATE SET c1 = c0; -- sqlite3.c:108474: sqlite3FinishCoding: Assertion `!pParse->isMultiWrite || sqlite3VdbeAssertMayAbort(v, pParse->mayAbort)' failed.""", weight=3.0)

# === MR-SQLITE-0159 (crash, fixed) ===
# Debug assertion assert_pager_state: Assertion `pPager->changeCountDone==0 || pPager->eLock>=RESERVED_LOCK' failed
ctx.rule("Sql-Stmt", """PRAGMA locking_mode = EXCLUSIVE;
PRAGMA journal_mode = WAL;
PRAGMA locking_mode = NORMAL;
PRAGMA integrity_check;
PRAGMA journal_mode = MEMORY; -- sqlite3.c:51926: assert_pager_state: Assertion `pPager->changeCountDone==0 || pPager->eLock>=RESERVED_LOCK' failed.""", weight=3.0)

# === MR-SQLITE-0160 (error, fixed (in documentation)) ===
# FTS4 integrity-check results in "database disk image is malformed" for UTF-16 encoding
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF-16';
CREATE VIRTUAL TABLE vt0 USING fts4(c0);
INSERT INTO vt0 VALUES ('ï»¿');
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0161 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `memIsValid(&aMem[pOp->p1])' failed.
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 NOT NULL DEFAULT '', c1 AS(c0) NOT NULL);
REPLACE INTO t0(c0) VALUES(NULL); -- sqlite3.c:85112: sqlite3VdbeExec: Assertion `memIsValid(&aMem[pOp->p1])' failed.""", weight=3.0)

# === MR-SQLITE-0162 (crash, fixed) ===
# Debug assertion exprSrcCount: Assertion `0' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
SELECT (0, 0) IN(SELECT MIN(c0), NTILE(0) OVER()) FROM t0; -- sqlite3.c:103486: exprSrcCount: Assertion `0' failed.""", weight=3.0)

# === MR-SQLITE-0163 (crash, fixed) ===
# Debug assertion sqlite3VdbeExec: Assertion `memIsValid(pRec)' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 NOT NULL DEFAULT 1, c1 AS(c0) UNIQUE);
REPLACE INTO t0 VALUES(NULL); -- sqlite3.c:87334: sqlite3VdbeExec: Assertion `memIsValid(pRec)' failed.""", weight=3.0)

# === MR-SQLITE-0164 (crash, fixed) ===
# Debug assertion sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Real)==0 || pMem->u.r==pX->u.r' failed
ctx.rule("Sql-Stmt", """PRAGMA foreign_keys = true;
CREATE TABLE t0(c0 INT AS(2) UNIQUE, c1 TEXT UNIQUE, FOREIGN KEY(c0) REFERENCES t0(c1));
INSERT INTO t0(c1) VALUES(0.16334143182538696), (0); -- sqlite3.c:75926: sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Real)==0 || pMem->u.r==pX->u.r' failed.""", weight=3.0)

# === MR-SQLITE-0165 (error, fixed) ===
# Trigger on normal table causes the database disk image to become malformed
ctx.rule("Sql-Stmt", """PRAGMA recursive_triggers = true;
CREATE TABLE t0(c0 UNIQUE ON CONFLICT REPLACE, c1, c2);
CREATE INDEX i0 ON t0(c2);
INSERT INTO t0(c0) VALUES (0);
CREATE TRIGGER tr0 DELETE ON t0 BEGIN
UPDATE t0 SET c2 = c0;
END;
INSERT INTO t0(c0, c2) VALUES(4, 0), (9, 0);
UPDATE t0 SET c0 = 0;
SELECT * FROM t0 WHERE x'' > t0.c2 GROUP BY c1; -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0166 (error, fixed) ===
# NATURAL JOIN on virtual table results in "parse error in rank function"
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE vt0 USING fts5(c0, c1);
CREATE VIRTUAL TABLE vt1 USING fts5(c0);
INSERT INTO vt1(c0) VALUES ('');
SELECT * FROM vt1 NATURAL JOIN vt0 WHERE vt0.c1 MATCH 'a'; -- parse error in rank function:""", weight=2.0)

# === MR-SQLITE-0167 (crash, fixed) ===
# Debug assertion codeVectorCompare: Assertion `0' failed
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 CHECK(((0, 0) > (0, c0))));
INSERT INTO t0(c0) VALUES(0) ON CONFLICT(c0) DO UPDATE SET c0 = 3; -- sqlite3.c:98717: codeVectorCompare: Assertion `0' failed.""", weight=3.0)

# === MR-SQLITE-0168 (crash, fixed) ===
# Debug assertion sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Real)==0 || pMem->u.r==pX->u.r' failed (2)
ctx.rule("Sql-Stmt", """PRAGMA foreign_keys = true;
CREATE TABLE t0(c0 TEXT PRIMARY KEY, c1 INT UNIQUE REFERENCES t0 CHECK(CAST(c1 AS INT) BETWEEN 0 AND CASE WHEN 1 THEN c0 END));
REPLACE INTO t0(c0, c1) VALUES(0.7675826647230917, 0), (0, x''); -- sqlite3.c:75952: sqlite3VdbeMemAboutToChange: Assertion `(mFlags&MEM_Real)==0 || pMem->u.r==pX->u.r' failed.""", weight=3.0)

# === MR-SQLITE-0169 (error, fixed) ===
# FTS5 integrity-check results in "database disk image is malformed" for UTF-16 encoding and SUBSTR
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF16';
CREATE VIRTUAL TABLE vt0 USING fts5(c0);
INSERT INTO vt0 VALUES (SUBSTR(x'37', ''));
INSERT INTO vt0(vt0) VALUES('integrity-check'); -- database disk image is malformed""", weight=2.0)

# === MR-SQLITE-0170 (NoREC, fixed) ===
# DBSTAT query computes incorrect result for aggregate column
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE stat USING dbstat;
SELECT * FROM stat WHERE stat.aggregate == NULL; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0171 (NoREC, fixed) ===
# DBSTAT query computes incorrect result for name column
ctx.rule("Sql-Stmt", """CREATE VIRTUAL TABLE stat USING dbstat;
SELECT * FROM stat WHERE stat.name = NULL; -- unexpected: row is fetched""", weight=2.0)

# === MR-SQLITE-0172 (NoREC, fixed) ===
# Incorrect result for query with 0 >= t0.c0 AND t0.c0 = v0.c0 condition
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0);
INSERT INTO t0 VALUES('0');
CREATE VIEW v0(c0) AS SELECT CAST(0 AS INT) FROM t0;
SELECT * FROM t0, v0 WHERE 0 >= t0.c0 AND t0.c0 = v0.c0; -- unexpected: fetches row""", weight=2.0)

# === MR-SQLITE-0173 (NoREC, fixed) ===
# Incorrect result for COUNT(), UTF16be encoding and SUBSTR
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF16be';
CREATE TABLE t0(c0, c1);
INSERT INTO t0(c0) VALUES (x'00');
CREATE INDEX i0 ON t0(c0 COLLATE BINARY);
INSERT INTO t0(c0) VALUES (1);
SELECT COUNT(*) FROM t0 WHERE SUBSTR(t0.c0, ','); -- expected: 1, actual: 2""", weight=2.0)

# === MR-SQLITE-0174 (TLP (aggregate), fixed) ===
# GROUP BY causes unexpected conversion
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 REAL, c1 REAL GENERATED ALWAYS AS (c0));
INSERT INTO t0(c0) VALUES (1);
SELECT * FROM t0 GROUP BY c0; -- expected: 1.0|1.0, actual: 1.0|1
SELECT * FROM t0; -- 1.0|1.0""", weight=1.5)

# === MR-SQLITE-0175 (TLP (aggregate), fixed) ===
# MAX yields unexpected result for UTF-16
ctx.rule("Sql-Stmt", """PRAGMA encoding = 'UTF-16';
CREATE TABLE t0(c0 TEXT);
INSERT INTO t0(c0) VALUES ('ì'), (1);
SELECT MAX(CASE 1 WHEN 1 THEN t0.c0 END) FROM t0; -- ì
SELECT MAX(t0.c0) FROM t0; -- 1""", weight=1.5)

# === MR-SQLITE-0176 (TLP (aggregate), fixed (in documentation)) ===
# Unexpected result for MIN on string that contains a null character
ctx.rule("Sql-Stmt", """SELECT HEX(MIN(a)) FROM (SELECT CHAR(0, 1) COLLATE NOCASE as a UNION SELECT CHAR(0, 0) as a); -- 0000
SELECT HEX(MIN(a)) FROM (SELECT CHAR(0, 0) COLLATE NOCASE as a UNION SELECT CHAR(0, 1) as a); -- 0001""", weight=1.5)

# === MR-SQLITE-0177 (TLP (DISTINCT), fixed) ===
# UNION operator malfunctions in LEFT JOIN on view
ctx.rule("Sql-Stmt", """CREATE TABLE t0(c0 INT);
CREATE VIEW v0(c0) AS SELECT CAST(t0.c0 AS INTEGER) FROM t0;
INSERT INTO t0(c0) VALUES (0);
SELECT * FROM t0 LEFT JOIN v0 ON v0.c0 >= '0' WHERE TRUE UNION SELECT 0,0 WHERE 0; -- expected: {0|0}, actual:{0|NULL}""", weight=1.5)

# === MR-SQLITE-0178 (PQS, fixed) ===
# Incorrect result for IN expression with right-hand IS TRUE sub-expression
ctx.rule("Sql-Stmt", "SELECT (1 IN (2 IS TRUE)); -- expected: {1}, actual: {0}", weight=2.0)

# === MR-SQLITE-0179 (PQS, fixed (in documentation)) ===
# Unexpected result for % and '1E1'
ctx.rule("Sql-Stmt", "SELECT 1 % '1E1'; -- expected: {1.0}, actual: {0.0}", weight=2.0)
