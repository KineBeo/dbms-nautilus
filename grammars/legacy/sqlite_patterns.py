# sqlite_patterns.py — Pattern-grammar for Nautilus SQLite fuzzing
# Use with: sqlite_harness_patterns_<version> (blank DB, no pre-loaded schema)
#
# DESIGN: Structural-bias grammar — CVE-specific literal PoCs replaced with
# 7 generalizable structural patterns derived from cross-CVE analysis.
# A crash found via a pattern rule is a genuine discovery, not PoC replay.
#
# Pattern taxonomy (from docs/cve-list.md CVE analysis):
#   P1: DDL→DQL          — CREATE TABLE + SELECT w/ JOINs      (4/6 CVEs)
#   P2: GenCol-Op        — generated column + query/PRAGMA      (2/6 CVEs)
#   P4: Compound         — INTERSECT/EXCEPT compound operators  (2/6 CVEs)
#   P6: Schema-Pragma    — DDL + INSERT → PRAGMA integrity      (1/6 CVEs)
#   P7: Boundary-Func    — ANY func(boundary-int arg)           (generalized)
#   P3/P5 inline in Select-Complex via Window-Agg-Expr
#
# BLANK DB: harness opens empty :memory: — all tables created by generated SQL.
# Layer 1 rules referencing t1/t2/t3 silently fail (no table); only pattern
# rules exercise the interesting code paths.
#
# Phase 2 RL interface:
#   ctx.set_weight(rule_id, new_weight)   — RL action
#   ctx.get_weights_for_nt(nt_id)         — RL state observation

# ============================================================
# START
# ============================================================
ctx.rule("START", "{Sql-Stmt-List}")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};\n{Sql-Stmt-List}")

# ============================================================
# LAYER 1 + LAYER 2: Sql-Stmt dispatch with weights
# Layer 1 base statements: weight 0.1–1.0
# Layer 2 stress templates: weight 1.5–3.5
# P1–P7 CVE structural patterns: weight 2.0–3.0
# ============================================================
ctx.rule("Sql-Stmt", "{Select-Stmt}", weight=1.0)
ctx.rule("Sql-Stmt", "{Insert-Stmt}", weight=1.0)
ctx.rule("Sql-Stmt", "{Update-Stmt}", weight=0.5)
ctx.rule("Sql-Stmt", "{Delete-Stmt}", weight=0.5)
ctx.rule("Sql-Stmt", "{Create-Table-Stmt}", weight=0.3)
ctx.rule("Sql-Stmt", "{Create-Index-Stmt}", weight=0.2)
ctx.rule("Sql-Stmt", "{Create-View-Stmt}", weight=0.2)
ctx.rule("Sql-Stmt", "{Create-Trigger-Stmt}", weight=0.2)
ctx.rule("Sql-Stmt", "{Create-Virtual-Table-Stmt}", weight=0.3)
ctx.rule("Sql-Stmt", "{Drop-Stmt}", weight=0.2)
ctx.rule("Sql-Stmt", "{Alter-Table-Stmt}", weight=0.3)
ctx.rule("Sql-Stmt", "{Pragma-Stmt}", weight=0.3)
ctx.rule("Sql-Stmt", "{Analyze-Stmt}", weight=0.2)
ctx.rule("Sql-Stmt", "{Attach-Stmt}", weight=0.2)
# Layer 2 stress templates (elevated weights)
ctx.rule("Sql-Stmt", "{Deep-Nested-Select}", weight=2.5)
ctx.rule("Sql-Stmt", "{Long-Join-Chain}", weight=2.0)
ctx.rule("Sql-Stmt", "{Recursive-CTE-Heavy}", weight=2.5)
ctx.rule("Sql-Stmt", "{Window-Func-Complex}", weight=3.0)
ctx.rule("Sql-Stmt", "{Json-Deep}", weight=1.0)
ctx.rule("Sql-Stmt", "{Aggregate-Complex}", weight=2.0)
ctx.rule("Sql-Stmt", "{Explain-Stress}", weight=1.5)
# P7: Boundary-value function (replaces Printf-Boundary literal PoC rules)
ctx.rule("Sql-Stmt", "{Pattern-Boundary-Func}", weight=3.0)
# P1–P6: CVE structural patterns (multi-statement, self-contained DDL→DQL)
ctx.rule("Sql-Stmt", "{Pattern-DDL-DQL}", weight=2.5)
ctx.rule("Sql-Stmt", "{Pattern-GenCol-Op}", weight=2.5)
ctx.rule("Sql-Stmt", "{Pattern-Compound}", weight=2.0)
ctx.rule("Sql-Stmt", "{Pattern-Schema-Pragma}", weight=2.0)

# ============================================================
# LAYER 1: SELECT
# ============================================================
ctx.rule("Select-Stmt", "{Select-Core}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core}")
ctx.rule("Select-Stmt", "{Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause}")

ctx.rule("Select-Core", "SELECT {Result-Col-List}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Where-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Where-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause} {Where-Clause}")
ctx.rule("Select-Core", "SELECT ALL {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Where-Clause} {Group-By-Clause} {Window-Clause}")
ctx.rule("Select-Core", "VALUES ({Expr-List})")

ctx.rule("Compound-Op", "UNION")
ctx.rule("Compound-Op", "UNION ALL")
ctx.rule("Compound-Op", "INTERSECT")
ctx.rule("Compound-Op", "EXCEPT")

ctx.rule("Result-Col-List", "{Result-Col}")
ctx.rule("Result-Col-List", "{Result-Col}, {Result-Col-List}")
ctx.rule("Result-Col", "*")
ctx.rule("Result-Col", "{Table-Name}.*")
ctx.rule("Result-Col", "{Expr}")
ctx.rule("Result-Col", "{Expr} AS {Col-Alias}")
ctx.regex("Col-Alias", "[a-z][a-z0-9_]*")

ctx.rule("From-Clause", "FROM {Join-Clause}")

ctx.rule("Join-Clause", "{Table-Or-Subquery}")
ctx.rule("Join-Clause", "{Table-Or-Subquery} {Join-Operator} {Table-Or-Subquery}")
ctx.rule("Join-Clause", "{Table-Or-Subquery} {Join-Operator} {Table-Or-Subquery} {Join-Constraint}")
ctx.rule("Join-Clause", "{Table-Or-Subquery} {Join-Operator} {Table-Or-Subquery} {Join-Operator} {Table-Or-Subquery}")

ctx.rule("Join-Operator", "JOIN")
ctx.rule("Join-Operator", "LEFT JOIN")
ctx.rule("Join-Operator", "LEFT OUTER JOIN")
ctx.rule("Join-Operator", "INNER JOIN")
ctx.rule("Join-Operator", "CROSS JOIN")
ctx.rule("Join-Operator", "NATURAL JOIN")
ctx.rule("Join-Operator", "NATURAL LEFT JOIN")
ctx.rule("Join-Operator", ",")

ctx.rule("Join-Constraint", "ON {Expr}")
ctx.rule("Join-Constraint", "USING ({Col-Name})")
ctx.rule("Join-Constraint", "USING ({Col-Name}, {Col-Name})")

ctx.rule("Table-Or-Subquery", "{Table-Name}")
ctx.rule("Table-Or-Subquery", "{Table-Name} AS {Col-Alias}")
ctx.rule("Table-Or-Subquery", "{Table-Name} NOT INDEXED")
ctx.rule("Table-Or-Subquery", "{Table-Name} INDEXED BY {Col-Name}")
ctx.rule("Table-Or-Subquery", "({Select-Stmt}) AS {Col-Alias}")
ctx.rule("Table-Or-Subquery", "({Join-Clause})")

# ============================================================
# LAYER 1: EXPRESSIONS (EBNF _expr, 30+ alternatives)
# Base cases first to ensure nts_to_min_size["Expr"] = 1
# ============================================================

# Terminals
ctx.rule("Expr", "{Literal}")
ctx.rule("Expr", "{Col-Ref}")
ctx.rule("Expr", "NULL")
ctx.rule("Expr", "TRUE")
ctx.rule("Expr", "FALSE")
ctx.rule("Expr", "CURRENT_TIMESTAMP")
ctx.rule("Expr", "CURRENT_DATE")
ctx.rule("Expr", "CURRENT_TIME")

# Unary
ctx.rule("Expr", "~{Expr}")
ctx.rule("Expr", "-{Expr}")
ctx.rule("Expr", "+{Expr}")
ctx.rule("Expr", "NOT {Expr}")

# Binary arithmetic
ctx.rule("Expr", "{Expr} * {Expr}")
ctx.rule("Expr", "{Expr} / {Expr}")
ctx.rule("Expr", "{Expr} % {Expr}")
ctx.rule("Expr", "{Expr} + {Expr}")
ctx.rule("Expr", "{Expr} - {Expr}")

# Bitwise
ctx.rule("Expr", "{Expr} << {Expr}")
ctx.rule("Expr", "{Expr} >> {Expr}")
ctx.rule("Expr", "{Expr} & {Expr}")
ctx.rule("Expr", "{Expr} | {Expr}")

# Comparison
ctx.rule("Expr", "{Expr} < {Expr}")
ctx.rule("Expr", "{Expr} <= {Expr}")
ctx.rule("Expr", "{Expr} > {Expr}")
ctx.rule("Expr", "{Expr} >= {Expr}")
ctx.rule("Expr", "{Expr} = {Expr}")
ctx.rule("Expr", "{Expr} != {Expr}")
ctx.rule("Expr", "{Expr} <> {Expr}")
ctx.rule("Expr", "{Expr} == {Expr}")

# Logical
ctx.rule("Expr", "{Expr} AND {Expr}")
ctx.rule("Expr", "{Expr} OR {Expr}")

# String concat and JSON arrow ops
ctx.rule("Expr", "{Expr} || {Expr}")
ctx.rule("Expr", "{Expr} -> {Expr}")
ctx.rule("Expr", "{Expr} ->> {Expr}")

# IS, ISNULL, NOTNULL
ctx.rule("Expr", "{Expr} ISNULL")
ctx.rule("Expr", "{Expr} NOTNULL")
ctx.rule("Expr", "{Expr} NOT NULL")
ctx.rule("Expr", "{Expr} IS NULL")
ctx.rule("Expr", "{Expr} IS NOT NULL")
ctx.rule("Expr", "{Expr} IS {Expr}")
ctx.rule("Expr", "{Expr} IS NOT {Expr}")
ctx.rule("Expr", "{Expr} IS DISTINCT FROM {Expr}")
ctx.rule("Expr", "{Expr} IS NOT DISTINCT FROM {Expr}")

# LIKE / GLOB / REGEXP / MATCH
ctx.rule("Expr", "{Expr} LIKE {Expr}")
ctx.rule("Expr", "{Expr} NOT LIKE {Expr}")
ctx.rule("Expr", "{Expr} LIKE {Expr} ESCAPE {Expr}")
ctx.rule("Expr", "{Expr} GLOB {Expr}")
ctx.rule("Expr", "{Expr} REGEXP {Expr}")
ctx.rule("Expr", "{Expr} MATCH {Expr}")

# BETWEEN
ctx.rule("Expr", "{Expr} BETWEEN {Expr} AND {Expr}")
ctx.rule("Expr", "{Expr} NOT BETWEEN {Expr} AND {Expr}")

# IN
ctx.rule("Expr", "{Expr} IN ({Select-Stmt})")
ctx.rule("Expr", "{Expr} IN ({Expr-List})")
ctx.rule("Expr", "{Expr} NOT IN ({Select-Stmt})")
ctx.rule("Expr", "{Expr} NOT IN ({Expr-List})")

# Subquery / EXISTS
ctx.rule("Expr", "({Select-Stmt})")
ctx.rule("Expr", "EXISTS ({Select-Stmt})")
ctx.rule("Expr", "NOT EXISTS ({Select-Stmt})")

# Grouping
ctx.rule("Expr", "({Expr})")

# CAST
ctx.rule("Expr", "CAST({Expr} AS {Type-Name})")

# COLLATE
ctx.rule("Expr", "{Expr} COLLATE NOCASE")
ctx.rule("Expr", "{Expr} COLLATE BINARY")
ctx.rule("Expr", "{Expr} COLLATE RTRIM")

# CASE
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} END")
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} ELSE {Expr} END")
ctx.rule("Expr", "CASE {Expr} WHEN {Expr} THEN {Expr} END")
ctx.rule("Expr", "CASE {Expr} WHEN {Expr} THEN {Expr} ELSE {Expr} END")

# RAISE
ctx.rule("Expr", "RAISE(IGNORE)")
ctx.rule("Expr", "RAISE(ABORT, {Str-Literal})")
ctx.rule("Expr", "RAISE(ROLLBACK, {Str-Literal})")
ctx.rule("Expr", "RAISE(FAIL, {Str-Literal})")

# Function call (with optional FILTER and OVER)
ctx.rule("Expr", "{Func-Call}")
ctx.rule("Expr", "{Func-Call} {Filter-Clause}")
ctx.rule("Expr", "{Func-Call} {Over-Clause}")
ctx.rule("Expr", "{Func-Call} {Filter-Clause} {Over-Clause}")

ctx.rule("Expr-List", "{Expr}")
ctx.rule("Expr-List", "{Expr}, {Expr-List}")

# ============================================================
# LAYER 1: WINDOW / FRAME / ORDERING
# ============================================================
ctx.rule("Over-Clause", "OVER ({Window-Defn})")
ctx.rule("Over-Clause", "OVER {Win-Name}")
ctx.regex("Win-Name", "w[0-9]")

ctx.rule("Window-Defn", "")
ctx.rule("Window-Defn", "PARTITION BY {Expr}")
ctx.rule("Window-Defn", "PARTITION BY {Expr}, {Expr}")
ctx.rule("Window-Defn", "ORDER BY {Ordering-Term}")
ctx.rule("Window-Defn", "ORDER BY {Ordering-Term}, {Ordering-Term}")
ctx.rule("Window-Defn", "PARTITION BY {Expr} ORDER BY {Ordering-Term}")
ctx.rule("Window-Defn", "PARTITION BY {Expr} ORDER BY {Ordering-Term} {Frame-Spec}")
ctx.rule("Window-Defn", "ORDER BY {Ordering-Term} {Frame-Spec}")

ctx.rule("Ordering-Term", "{Expr}")
ctx.rule("Ordering-Term", "{Expr} ASC")
ctx.rule("Ordering-Term", "{Expr} DESC")
ctx.rule("Ordering-Term", "{Expr} ASC NULLS FIRST")
ctx.rule("Ordering-Term", "{Expr} ASC NULLS LAST")
ctx.rule("Ordering-Term", "{Expr} DESC NULLS FIRST")
ctx.rule("Ordering-Term", "{Expr} DESC NULLS LAST")

ctx.rule("Asc-Desc", "ASC")
ctx.rule("Asc-Desc", "DESC")

ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW")
ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING")
ctx.rule("Frame-Spec", "ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING")
ctx.rule("Frame-Spec", "ROWS BETWEEN {Expr} PRECEDING AND CURRENT ROW")
ctx.rule("Frame-Spec", "ROWS BETWEEN {Expr} PRECEDING AND {Expr} FOLLOWING")
ctx.rule("Frame-Spec", "ROWS BETWEEN CURRENT ROW AND {Expr} FOLLOWING")
ctx.rule("Frame-Spec", "RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW")
ctx.rule("Frame-Spec", "RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING")
ctx.rule("Frame-Spec", "GROUPS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW")
ctx.rule("Frame-Spec", "GROUPS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING")
ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE CURRENT ROW")
ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE GROUP")
ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE TIES")
ctx.rule("Frame-Spec", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW EXCLUDE NO OTHERS")

ctx.rule("Filter-Clause", "FILTER (WHERE {Expr})")

ctx.rule("Window-Clause", "WINDOW w1 AS ({Window-Defn})")
ctx.rule("Window-Clause", "WINDOW w1 AS ({Window-Defn}), w2 AS ({Window-Defn})")

# ============================================================
# LAYER 1: WITH / CTEs
# ============================================================
ctx.rule("With-Clause", "WITH {Cte-List}")
ctx.rule("With-Clause", "WITH RECURSIVE {Cte-List}")

ctx.rule("Cte-List", "{Cte-Def}")
ctx.rule("Cte-List", "{Cte-Def}, {Cte-List}")

ctx.rule("Cte-Def", "{Table-Name} AS ({Select-Stmt})")
ctx.rule("Cte-Def", "{Table-Name} ({Col-Name-List}) AS ({Select-Stmt})")
ctx.rule("Cte-Def", "{Table-Name} AS MATERIALIZED ({Select-Stmt})")
ctx.rule("Cte-Def", "{Table-Name} AS NOT MATERIALIZED ({Select-Stmt})")
ctx.rule("Cte-Def", "{Table-Name} ({Col-Name-List}) AS NOT MATERIALIZED ({Select-Stmt})")

ctx.rule("Col-Name-List", "{Col-Name}")
ctx.rule("Col-Name-List", "{Col-Name}, {Col-Name-List}")

# ============================================================
# LAYER 1: DML (INSERT / UPDATE / DELETE)
# ============================================================
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} ({Col-Name-List}) VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT OR REPLACE INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT OR IGNORE INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT OR ABORT INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT OR FAIL INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT OR ROLLBACK INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "REPLACE INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} {Select-Stmt}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} DEFAULT VALUES")
ctx.rule("Insert-Stmt", "{With-Clause} INSERT INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}) RETURNING {Result-Col-List}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}) ON CONFLICT DO NOTHING")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} ({Col-Name-List}) VALUES ({Expr-List}) ON CONFLICT({Col-Name}) DO UPDATE SET {Col-Name} = {Expr}")

ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr}, {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR IGNORE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR REPLACE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} RETURNING {Result-Col-List}")
ctx.rule("Update-Stmt", "{With-Clause} UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr}")

ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name} WHERE {Expr}")

# ============================================================
# LAYER 1: DDL
# ============================================================
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TEMP TABLE {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) STRICT")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} AS {Select-Stmt}")

ctx.rule("Col-Def-List", "{Col-Def}")
ctx.rule("Col-Def-List", "{Col-Def}, {Col-Def-List}")

ctx.rule("Col-Def", "{Col-Name} {Type-Name}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} NOT NULL")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} UNIQUE")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} DEFAULT {Literal}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} CHECK ({Expr})")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} NOT NULL DEFAULT {Literal}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} GENERATED ALWAYS AS ({Expr}) STORED")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} GENERATED ALWAYS AS ({Expr}) VIRTUAL")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} GENERATED ALWAYS AS ({Expr}) {Gen-Storage}")

# Storage qualifier for GENERATED columns. Added 2026-04-21 to satisfy
# sqlite_generated.py, which emits {Gen-Storage} (inherited from the
# sibling rl-nautilus whitelist).
ctx.rule("Gen-Storage", "VIRTUAL", weight=2.0)
ctx.rule("Gen-Storage", "STORED", weight=1.5)

ctx.rule("Type-Name", "INTEGER")
ctx.rule("Type-Name", "REAL")
ctx.rule("Type-Name", "TEXT")
ctx.rule("Type-Name", "BLOB")
ctx.rule("Type-Name", "NUMERIC")
ctx.rule("Type-Name", "INT")
ctx.rule("Type-Name", "VARCHAR(255)")
ctx.rule("Type-Name", "FLOAT")
ctx.rule("Type-Name", "BOOLEAN")
ctx.rule("Type-Name", "DATE")

ctx.rule("Create-Index-Stmt", "CREATE INDEX IF NOT EXISTS idx1 ON {Table-Name} ({Col-Name})")
ctx.rule("Create-Index-Stmt", "CREATE UNIQUE INDEX idx1 ON {Table-Name} ({Col-Name})")
ctx.rule("Create-Index-Stmt", "CREATE INDEX idx1 ON {Table-Name} ({Col-Name}, {Col-Name})")
ctx.rule("Create-Index-Stmt", "CREATE INDEX idx1 ON {Table-Name} ({Col-Name}) WHERE {Expr}")

ctx.rule("Create-View-Stmt", "CREATE VIEW v1 AS {Select-Stmt}")
ctx.rule("Create-View-Stmt", "CREATE TEMP VIEW v1 AS {Select-Stmt}")
ctx.rule("Create-View-Stmt", "CREATE VIEW IF NOT EXISTS v1 AS {Select-Stmt}")
ctx.rule("Create-View-Stmt", "CREATE VIEW v1 ({Col-Name-List}) AS {Select-Stmt}")

ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5({Col-Name-List})")
ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3({Col-Name-List})")
ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2)")

ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 BEFORE UPDATE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN {Trigger-Body} END")
ctx.rule("Trigger-Body", "SELECT {Result-Col-List} FROM {Table-Name};")
ctx.rule("Trigger-Body", "INSERT INTO {Table-Name} VALUES({Expr-List});")

ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} RENAME TO {Table-Name}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} RENAME COLUMN {Col-Name} TO {Col-Name}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} ADD COLUMN {Col-Def}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} DROP COLUMN {Col-Name}")

ctx.rule("Drop-Stmt", "DROP TABLE IF EXISTS {Table-Name}")
ctx.rule("Drop-Stmt", "DROP TABLE {Table-Name}")
ctx.rule("Drop-Stmt", "DROP INDEX IF EXISTS idx1")
ctx.rule("Drop-Stmt", "DROP VIEW IF EXISTS v1")
ctx.rule("Drop-Stmt", "DROP TRIGGER IF EXISTS trg1")

# ============================================================
# LAYER 1: MISC STATEMENTS
# ============================================================
ctx.rule("Pragma-Stmt", "PRAGMA integrity_check")
ctx.rule("Pragma-Stmt", "PRAGMA quick_check")
ctx.rule("Pragma-Stmt", "PRAGMA journal_mode={Journal-Mode}")
ctx.rule("Pragma-Stmt", "PRAGMA wal_checkpoint({Wal-Mode})")
ctx.rule("Pragma-Stmt", "PRAGMA cache_size={Signed-Number}")
ctx.rule("Pragma-Stmt", "PRAGMA foreign_keys={Pragma-Bool}")
ctx.rule("Pragma-Stmt", "PRAGMA optimize")
ctx.rule("Pragma-Stmt", "PRAGMA analysis_limit={Signed-Number}")
ctx.rule("Pragma-Stmt", "PRAGMA page_size")
ctx.rule("Pragma-Stmt", "PRAGMA synchronous={Sync-Mode}")
ctx.rule("Journal-Mode", "DELETE")
ctx.rule("Journal-Mode", "WAL")
ctx.rule("Journal-Mode", "MEMORY")
ctx.rule("Journal-Mode", "PERSIST")
ctx.rule("Journal-Mode", "TRUNCATE")
ctx.rule("Wal-Mode", "FULL")
ctx.rule("Wal-Mode", "PASSIVE")
ctx.rule("Wal-Mode", "RESTART")
ctx.rule("Pragma-Bool", "ON")
ctx.rule("Pragma-Bool", "OFF")
ctx.rule("Pragma-Bool", "1")
ctx.rule("Pragma-Bool", "0")
ctx.rule("Sync-Mode", "NORMAL")
ctx.rule("Sync-Mode", "FULL")
ctx.rule("Sync-Mode", "OFF")

ctx.rule("Attach-Stmt", "ATTACH ':memory:' AS db2")
ctx.rule("Attach-Stmt", "ATTACH DATABASE ':memory:' AS db2")

ctx.rule("Analyze-Stmt", "ANALYZE")
ctx.rule("Analyze-Stmt", "ANALYZE {Table-Name}")

ctx.rule("Vacuum-Stmt", "VACUUM")
ctx.rule("Vacuum-Stmt", "VACUUM INTO ':memory:'")

ctx.rule("Reindex-Stmt", "REINDEX")
ctx.rule("Reindex-Stmt", "REINDEX {Table-Name}")

ctx.rule("Savepoint-Stmt", "SAVEPOINT sp1")
ctx.rule("Release-Stmt", "RELEASE SAVEPOINT sp1")
ctx.rule("Rollback-Stmt", "ROLLBACK TO SAVEPOINT sp1")
ctx.rule("Rollback-Stmt", "ROLLBACK")

ctx.rule("Where-Clause", "WHERE {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr} HAVING {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr}, {Expr}")
ctx.rule("Order-By-Clause", "ORDER BY {Ordering-Term}")
ctx.rule("Order-By-Clause", "ORDER BY {Ordering-Term}, {Ordering-Term}")
ctx.rule("Limit-Clause", "LIMIT {Expr}")
ctx.rule("Limit-Clause", "LIMIT {Expr} OFFSET {Expr}")
ctx.rule("Limit-Clause", "LIMIT {Expr}, {Expr}")

# ============================================================
# LAYER 1: TERMINALS / LITERALS / IDENTIFIERS
# ============================================================
ctx.rule("Literal", "{Int-Literal}")
ctx.rule("Literal", "{Float-Literal}")
ctx.rule("Literal", "{Str-Literal}")
ctx.rule("Literal", "{Blob-Literal}")
ctx.rule("Literal", "NULL")
ctx.rule("Literal", "TRUE")
ctx.rule("Literal", "FALSE")
ctx.rule("Literal", "CURRENT_TIMESTAMP")
ctx.rule("Literal", "CURRENT_DATE")
ctx.rule("Literal", "CURRENT_TIME")

ctx.regex("Int-Literal", "-?(?:0|[1-9][0-9]{0,6})")
ctx.regex("Float-Literal", "-?[0-9]+\\.[0-9]+(?:[eE][+-]?[0-9]+)?")
ctx.regex("Str-Literal", "'[a-zA-Z0-9 _-]{0,20}'")
ctx.regex("Blob-Literal", "X'[0-9a-fA-F]{0,16}'")

ctx.rule("Signed-Number", "{Int-Literal}")
ctx.rule("Signed-Number", "+{Int-Literal}")
ctx.rule("Signed-Number", "-{Int-Literal}")

# Schema identifiers — t1/t2/t3 kept for Layer 1 rule coverage (blank DB
# means those queries silently fail, which is fine for a fuzzer).
# p/q/r/s added as fresh-names for pattern rules and Layer 1 rule coverage.
ctx.rule("Table-Name", "t1", weight=1.0)
ctx.rule("Table-Name", "t2", weight=1.0)
ctx.rule("Table-Name", "t3", weight=1.0)
ctx.rule("Table-Name", "p", weight=0.4)   # fresh-name: used in pattern rules
ctx.rule("Table-Name", "q", weight=0.4)
ctx.rule("Table-Name", "r", weight=0.3)
ctx.rule("Table-Name", "s", weight=0.2)
ctx.rule("Col-Name", "c1", weight=1.0)
ctx.rule("Col-Name", "c2", weight=1.0)
ctx.rule("Col-Name", "c3", weight=1.0)
ctx.rule("Col-Name", "a", weight=0.8)     # used in pattern DDL rules
ctx.rule("Col-Name", "b", weight=0.8)
ctx.rule("Col-Name", "rowid", weight=0.5)
ctx.rule("Col-Name", "_rowid_", weight=0.3)
ctx.rule("Col-Ref", "{Col-Name}", weight=1.0)
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}", weight=1.0)

# ============================================================
# LAYER 1: FUNCTION CALLS
# ============================================================
ctx.rule("Func-Call", "count(*)")
ctx.rule("Func-Call", "count({Expr})")
ctx.rule("Func-Call", "count(DISTINCT {Expr})")
ctx.rule("Func-Call", "sum({Expr})")
ctx.rule("Func-Call", "avg({Expr})")
ctx.rule("Func-Call", "min({Expr})")
ctx.rule("Func-Call", "max({Expr})")
ctx.rule("Func-Call", "abs({Expr})")
ctx.rule("Func-Call", "length({Expr})")
ctx.rule("Func-Call", "typeof({Expr})")
ctx.rule("Func-Call", "substr({Expr}, {Expr})")
ctx.rule("Func-Call", "substr({Expr}, {Expr}, {Expr})")
ctx.rule("Func-Call", "coalesce({Expr}, {Expr})")
ctx.rule("Func-Call", "nullif({Expr}, {Expr})")
ctx.rule("Func-Call", "ifnull({Expr}, {Expr})")
ctx.rule("Func-Call", "iif({Expr}, {Expr}, {Expr})")
ctx.rule("Func-Call", "upper({Expr})")
ctx.rule("Func-Call", "lower({Expr})")
ctx.rule("Func-Call", "trim({Expr})")
ctx.rule("Func-Call", "hex({Expr})")
ctx.rule("Func-Call", "quote({Expr})")
ctx.rule("Func-Call", "last_insert_rowid()")
ctx.rule("Func-Call", "changes()")
ctx.rule("Func-Call", "total_changes()")
ctx.rule("Func-Call", "random()")
ctx.rule("Func-Call", "randomblob({Expr})")
ctx.rule("Func-Call", "zeroblob({Expr})")
ctx.rule("Func-Call", "char({Expr})")
ctx.rule("Func-Call", "unicode({Expr})")
ctx.rule("Func-Call", "format({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "printf({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "group_concat({Expr})")
ctx.rule("Func-Call", "group_concat({Expr}, {Str-Literal})")
# JSON basic forms (Layer 1)
ctx.rule("Func-Call", "json({Expr})")
ctx.rule("Func-Call", "json_valid({Expr})")
ctx.rule("Func-Call", "json_type({Expr})")
ctx.rule("Func-Call", "json_extract({Expr}, {Str-Literal})")
ctx.rule("Func-Call", "json_array({Expr-List})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr})")

# ============================================================
# LAYER 2: EXECUTION STRESS TEMPLATES
# ============================================================

# --- Deep-Expr: forced-depth expression subtrees ---
ctx.rule("Deep-Expr", "{Expr} {Bin-Op} {Deep-Expr-L2}", weight=3.0)
ctx.rule("Deep-Expr", "({Deep-Expr-L2})", weight=2.0)
ctx.rule("Deep-Expr", "CAST({Deep-Expr-L2} AS {Type-Name})", weight=1.0)
ctx.rule("Deep-Expr", "CASE WHEN {Deep-Expr-L2} THEN {Deep-Expr-L2} ELSE {Expr} END", weight=2.0)
ctx.rule("Deep-Expr", "{Func-Call}", weight=1.0)

ctx.rule("Deep-Expr-L2", "{Expr} {Bin-Op} {Expr}", weight=4.0)
ctx.rule("Deep-Expr-L2", "({Expr} {Bin-Op} {Expr})", weight=2.0)
ctx.rule("Deep-Expr-L2", "{Func-Call}", weight=2.0)
ctx.rule("Deep-Expr-L2", "{Col-Ref}", weight=1.0)

ctx.rule("Bin-Op", "+")
ctx.rule("Bin-Op", "-")
ctx.rule("Bin-Op", "*")
ctx.rule("Bin-Op", "/")
ctx.rule("Bin-Op", "%")
ctx.rule("Bin-Op", "&")
ctx.rule("Bin-Op", "|")
ctx.rule("Bin-Op", "<<")
ctx.rule("Bin-Op", ">>")
ctx.rule("Bin-Op", "||")

# --- Deep-Nested-Select: subquery chains ---
ctx.rule("Deep-Nested-Select",
    "SELECT {Result-Col-List} FROM (SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr}) AS sub1",
    weight=3.0)
ctx.rule("Deep-Nested-Select",
    "SELECT {Result-Col-List} FROM (SELECT {Result-Col-List} FROM "
    "(SELECT {Result-Col-List} FROM {Table-Name}) AS sub1) AS sub2",
    weight=2.0)
ctx.rule("Deep-Nested-Select",
    "SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr} IN "
    "(SELECT {Col-Name} FROM (SELECT {Col-Name} FROM {Table-Name}))",
    weight=2.0)
ctx.rule("Deep-Nested-Select",
    "SELECT {Result-Col-List} FROM {Table-Name} WHERE EXISTS "
    "(SELECT 1 FROM {Table-Name} WHERE EXISTS "
    "(SELECT 1 FROM {Table-Name} WHERE {Expr}))",
    weight=1.0)

# --- Long-Join-Chain: multi-table joins ---
ctx.rule("Long-Join-Chain",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} ON {Col-Ref} = {Col-Ref}",
    weight=3.0)
ctx.rule("Long-Join-Chain",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} ON {Col-Ref} = {Col-Ref} "
    "JOIN {Table-Name} ON {Col-Ref} = {Col-Ref}",
    weight=2.0)
ctx.rule("Long-Join-Chain",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "LEFT JOIN {Table-Name} ON {Col-Ref} = {Col-Ref} "
    "LEFT JOIN {Table-Name} ON {Expr}",
    weight=2.0)
ctx.rule("Long-Join-Chain",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "CROSS JOIN {Table-Name} "
    "NATURAL JOIN {Table-Name}",
    weight=1.0)
ctx.rule("Long-Join-Chain",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} USING ({Col-Name}) "
    "JOIN {Table-Name} USING ({Col-Name}) "
    "JOIN {Table-Name} ON {Expr}",
    weight=1.0)

# --- Recursive-CTE-Heavy: non-trivial recursive CTEs ---
ctx.rule("Recursive-CTE-Heavy",
    "WITH RECURSIVE cnt(x) AS "
    "(SELECT {Int-Literal} UNION ALL SELECT x + 1 FROM cnt WHERE x < {Int-Literal}) "
    "SELECT x FROM cnt",
    weight=3.0)
ctx.rule("Recursive-CTE-Heavy",
    "WITH RECURSIVE cte({Col-Name}) AS "
    "(SELECT {Expr} FROM {Table-Name} "
    "UNION ALL "
    "SELECT {Expr} FROM {Table-Name} JOIN cte ON {Col-Ref} = {Col-Ref}) "
    "SELECT {Result-Col-List} FROM cte",
    weight=2.0)
ctx.rule("Recursive-CTE-Heavy",
    "WITH RECURSIVE "
    "a(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM a WHERE x < 5), "
    "b(y) AS (SELECT {Expr} FROM a) "
    "SELECT {Result-Col-List} FROM b",
    weight=2.0)
ctx.rule("Recursive-CTE-Heavy",
    "WITH {Table-Name}({Col-Name}) AS "
    "({Select-Stmt} UNION ALL {Select-Stmt}) "
    "SELECT {Result-Col-List} FROM {Table-Name}",
    weight=2.0)

# --- Window-Func-Complex: window functions with complex partitions/frames ---
ctx.rule("Window-Func-Complex",
    "SELECT {Win-Func-Expr} OVER ({Win-Partition} {Win-Order} {Win-Frame}) "
    "FROM {Table-Name}",
    weight=3.0)
ctx.rule("Window-Func-Complex",
    "SELECT {Win-Func-Expr} OVER w1, {Win-Func-Expr} OVER w1 "
    "FROM {Table-Name} "
    "WINDOW w1 AS ({Win-Partition} {Win-Order})",
    weight=2.0)

ctx.rule("Win-Func-Expr", "row_number()", weight=2.0)
ctx.rule("Win-Func-Expr", "rank()", weight=2.0)
ctx.rule("Win-Func-Expr", "dense_rank()", weight=2.0)
ctx.rule("Win-Func-Expr", "lag({Expr}, {Int-Literal}, {Expr})", weight=2.0)
ctx.rule("Win-Func-Expr", "lead({Expr}, {Int-Literal}, {Expr})", weight=2.0)
ctx.rule("Win-Func-Expr", "nth_value({Expr}, {Int-Literal})", weight=1.0)
ctx.rule("Win-Func-Expr", "first_value({Deep-Expr})", weight=1.0)
ctx.rule("Win-Func-Expr", "last_value({Deep-Expr})", weight=1.0)
ctx.rule("Win-Func-Expr", "sum({Deep-Expr})", weight=1.0)
ctx.rule("Win-Func-Expr", "count({Expr})", weight=1.0)

ctx.rule("Win-Partition", "", weight=1.0)
ctx.rule("Win-Partition", "PARTITION BY {Expr}", weight=2.0)
ctx.rule("Win-Partition", "PARTITION BY {Expr}, {Expr}", weight=1.0)
ctx.rule("Win-Order", "", weight=1.0)
ctx.rule("Win-Order", "ORDER BY {Expr}", weight=2.0)
ctx.rule("Win-Order", "ORDER BY {Expr} {Asc-Desc}, {Expr}", weight=1.0)
ctx.rule("Win-Frame", "", weight=2.0)
ctx.rule("Win-Frame", "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW", weight=2.0)
ctx.rule("Win-Frame", "ROWS BETWEEN {Int-Literal} PRECEDING AND CURRENT ROW", weight=1.0)
ctx.rule("Win-Frame", "ROWS BETWEEN CURRENT ROW AND {Int-Literal} FOLLOWING", weight=1.0)
ctx.rule("Win-Frame", "ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING", weight=1.0)
ctx.rule("Win-Frame", "RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW", weight=1.0)

# --- Pattern-Boundary-Func (P7): generalized boundary-value function calls ---
# Replaces Printf-Boundary literal PoC rules.
# Root cause of CVE-2020-13434: integer overflow in sqlite3_str_vappendf when
# precision arg is INT32_MAX. Generalized to ANY function taking a boundary int.
# A crash found here means the fuzzer generated a *class* of boundary SQL.

ctx.rule("Pattern-Boundary-Func",
    "SELECT {Boundary-Func-Call}",
    weight=3.0)
ctx.rule("Pattern-Boundary-Func",
    "SELECT {Boundary-Func-Call}, {Boundary-Func-Call}",
    weight=1.5)
# group_concat variant requires a table — create one inline
ctx.rule("Pattern-Boundary-Func",
    "CREATE TABLE IF NOT EXISTS p(x TEXT);\n"
    "INSERT INTO p VALUES({Str-Literal}),({Str-Literal}),({Str-Literal});\n"
    "SELECT group_concat(x, {Boundary-Int}) FROM p",
    weight=2.0)

ctx.rule("Boundary-Func-Call", "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Boundary-Func-Call", "printf({Format-Spec}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call", "printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})", weight=1.5)
ctx.rule("Boundary-Func-Call", "substr({Str-Literal}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call", "substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})", weight=1.5)
ctx.rule("Boundary-Func-Call", "hex(zeroblob({Boundary-Int}))", weight=2.0)
ctx.rule("Boundary-Func-Call", "round({Boundary-Float}, {Boundary-Int})", weight=1.5)

# Format-Spec: precision format specifiers (CVE-2020-13434 root cause class)
ctx.rule("Format-Spec", "'%.*g'", weight=3.0)  # CVE-2020-13434 root specifier
ctx.rule("Format-Spec", "'%.*f'", weight=2.0)
ctx.rule("Format-Spec", "'%.*e'", weight=2.0)
ctx.rule("Format-Spec", "'%.*d'", weight=1.0)
ctx.rule("Format-Spec", "'%.*s'", weight=1.0)

ctx.rule("Printf-Fmt-Spec", "'%d'", weight=2.0)
ctx.rule("Printf-Fmt-Spec", "'%u'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%x'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%f'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%s'", weight=2.0)

# --- Json-Deep: deeply nested JSON construction + extraction ---
ctx.rule("Json-Deep",
    "SELECT json_extract(json({Json-Obj}), {Json-Path})",
    weight=3.0)
ctx.rule("Json-Deep",
    "SELECT json_insert(json({Json-Obj}), {Json-Path}, {Expr})",
    weight=2.0)
ctx.rule("Json-Deep",
    "SELECT json_replace(json({Json-Obj}), {Json-Path}, {Expr})",
    weight=2.0)
ctx.rule("Json-Deep",
    "SELECT json_remove(json({Json-Obj}), {Json-Path})",
    weight=2.0)
ctx.rule("Json-Deep",
    "SELECT json_type(json({Json-Obj}), {Json-Path})",
    weight=2.0)
ctx.rule("Json-Deep",
    "SELECT json_valid(json({Json-Obj}))",
    weight=1.0)
ctx.rule("Json-Deep",
    "SELECT json_array_length(json({Json-Obj}))",
    weight=1.0)
ctx.rule("Json-Deep",
    "SELECT json_each.key, json_each.value FROM json_each(json({Json-Obj}))",
    weight=1.0)
ctx.rule("Json-Deep",
    "SELECT json_tree.path FROM json_tree(json({Json-Obj}))",
    weight=1.0)

ctx.rule("Json-Obj", "json_object('a', {Expr})", weight=2.0)
ctx.rule("Json-Obj", "json_object('a', json_object('b', {Expr}))", weight=2.0)
ctx.rule("Json-Obj", "json_object('a', json_object('b', json_object('c', {Expr})))", weight=1.0)
ctx.rule("Json-Obj", "json_object('a', json_array({Expr-List}))", weight=2.0)
ctx.rule("Json-Obj", "json_array(json_object('a', {Expr}), {Expr})", weight=1.0)
ctx.rule("Json-Obj", "json_array({Expr}, {Expr}, {Expr})", weight=1.0)

ctx.rule("Json-Path", "'$'", weight=2.0)
ctx.rule("Json-Path", "'$.a'", weight=2.0)
ctx.rule("Json-Path", "'$[0]'", weight=1.0)
ctx.rule("Json-Path", "'$.a.b'", weight=1.0)
ctx.rule("Json-Path", "'$.a[0]'", weight=1.0)
ctx.rule("Json-Path", "'$[0][0][0]'", weight=0.5)

# --- Aggregate-Complex: aggregates with FILTER clause ---
ctx.rule("Aggregate-Complex",
    "SELECT count({Expr}) FILTER (WHERE {Expr}), "
    "sum({Expr}) FILTER (WHERE {Expr}) FROM {Table-Name}",
    weight=3.0)
ctx.rule("Aggregate-Complex",
    "SELECT count({Expr}) FILTER (WHERE {Expr}) FROM {Table-Name} GROUP BY {Expr}",
    weight=3.0)
ctx.rule("Aggregate-Complex",
    "SELECT {Agg-Func} FROM {Table-Name} GROUP BY {Expr}, {Expr} HAVING count(*) > {Int-Literal}",
    weight=2.0)
ctx.rule("Aggregate-Complex",
    "SELECT {Agg-Func} FROM ({Select-Stmt}) AS sub GROUP BY {Expr}",
    weight=2.0)
ctx.rule("Aggregate-Complex",
    "SELECT count(DISTINCT {Expr}) FROM {Table-Name}",
    weight=2.0)
ctx.rule("Aggregate-Complex",
    "SELECT group_concat({Expr}, {Str-Literal}) FROM {Table-Name} GROUP BY {Expr}",
    weight=2.0)
ctx.rule("Aggregate-Complex",
    "SELECT sum({Deep-Expr}) FILTER (WHERE {Expr} > 0) FROM {Table-Name} GROUP BY {Expr}",
    weight=2.0)

ctx.rule("Agg-Func", "count({Expr})", weight=2.0)
ctx.rule("Agg-Func", "sum({Expr})", weight=2.0)
ctx.rule("Agg-Func", "avg({Expr})", weight=1.0)
ctx.rule("Agg-Func", "min({Expr})", weight=1.0)
ctx.rule("Agg-Func", "max({Expr})", weight=1.0)
ctx.rule("Agg-Func", "group_concat({Expr})", weight=1.0)
ctx.rule("Agg-Func", "count(*)", weight=2.0)

# --- Explain-Stress: EXPLAIN QUERY PLAN prefix ---
ctx.rule("Explain-Stress", "EXPLAIN QUERY PLAN {Select-Stmt}")
ctx.rule("Explain-Stress", "EXPLAIN QUERY PLAN {Deep-Nested-Select}")
ctx.rule("Explain-Stress", "EXPLAIN QUERY PLAN {Long-Join-Chain}")
ctx.rule("Explain-Stress", "EXPLAIN {Select-Stmt}")

# ============================================================
# LAYER 2: BOUNDARY LITERAL INJECTION
# (Not in generic Expr path — only reachable via stress templates)
# ============================================================

# Boundary-Int: values that trigger integer overflow / UBSan
ctx.rule("Boundary-Int", "2147483647", weight=3.0)      # INT32_MAX
ctx.rule("Boundary-Int", "2147483648", weight=3.0)      # INT32_MAX + 1
ctx.rule("Boundary-Int", "-2147483648", weight=3.0)     # INT32_MIN
ctx.rule("Boundary-Int", "-2147483649", weight=2.0)     # INT32_MIN - 1
ctx.rule("Boundary-Int", "4294967295", weight=2.0)      # UINT32_MAX
ctx.rule("Boundary-Int", "4294967296", weight=2.0)      # UINT32_MAX + 1
ctx.rule("Boundary-Int", "9223372036854775807", weight=3.0)   # INT64_MAX
ctx.rule("Boundary-Int", "-9223372036854775808", weight=3.0)  # INT64_MIN
ctx.rule("Boundary-Int", "0", weight=2.0)
ctx.rule("Boundary-Int", "-1", weight=2.0)
ctx.rule("Boundary-Int", "1", weight=1.0)

# Boundary-Float: float boundary values
ctx.rule("Boundary-Float", "0.01", weight=3.0)     # CVE-2020-13434 PoC value
ctx.rule("Boundary-Float", "0.0", weight=2.0)
ctx.rule("Boundary-Float", "1.0", weight=2.0)
ctx.rule("Boundary-Float", "-1.0", weight=1.0)
ctx.rule("Boundary-Float", "1e308", weight=2.0)
ctx.rule("Boundary-Float", "-1e308", weight=2.0)
ctx.rule("Boundary-Float", "1e-308", weight=1.0)
ctx.rule("Boundary-Float", "-0.0", weight=1.0)

# ============================================================
# LAYER 2: CVE STRUCTURAL PATTERNS (P1–P6)
# Each pattern is self-contained: DDL creates tables, DML populates them,
# DQL exercises the interesting code path.
# ============================================================

# --- Pattern-DDL-DQL (P1): DDL → complex SELECT ---
# Covers CVE-2020-13435 (JOIN+window), CVE-2020-13871 (GROUP BY+window),
# CVE-2020-15358 (INTERSECT+JOIN+VIEW), CVE-2020-9327 (genCol+JOIN)

ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER, b TEXT, c REAL);\n"
    "SELECT {Result-Col-List} FROM p",
    weight=1.5)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER, b TEXT);\n"
    "CREATE TABLE IF NOT EXISTS q(x INTEGER, y TEXT);\n"
    "SELECT {Result-Col-List} FROM p {Join-Operator} q ON p.a = q.x",
    weight=2.0)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER UNIQUE, b TEXT);\n"
    "INSERT INTO p VALUES({Int-Literal}, {Str-Literal});\n"
    "SELECT {Result-Col-List} FROM p WHERE {Expr}",
    weight=2.0)
# P1+P3: DDL + self-JOIN + window (covers CVE-2020-13435 structure)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(a UNIQUE);\n"
    "SELECT p.a FROM p JOIN p q ON 3 = p.a NATURAL JOIN p "
    "WHERE p.a IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(a))) FROM p d WHERE p.a))",
    weight=2.0)
# P1+P4: DDL + VIEW + JOIN + INTERSECT (covers CVE-2020-15358 structure)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER);\n"
    "CREATE TABLE IF NOT EXISTS q(b INTEGER);\n"
    "CREATE VIEW IF NOT EXISTS vp AS SELECT a FROM p ORDER BY a;\n"
    "SELECT {Result-Col-List} FROM p, q "
    "WHERE p.a = (SELECT {Int-Literal} INTERSECT SELECT b FROM vp) AND p.a = {Int-Literal}",
    weight=2.0)
# P1+P3: DDL + GROUP BY + HAVING + two window exprs (covers CVE-2020-13871 structure)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS p(b);\n"
    "SELECT(SELECT b FROM p GROUP BY b HAVING(NULL AND b IN(\n"
    "  (SELECT COUNT() OVER(ORDER BY b) = lead(b) OVER(\n"
    "    ORDER BY SUM(DISTINCT CASE WHEN b > 0 THEN b*b ELSE 0 END) / {Int-Literal}\n"
    "  ))\n"
    "))) FROM p EXCEPT SELECT b FROM p ORDER BY b",
    weight=1.5)
# P1+P5: DDL + three-table DDL + JOIN + complex WHERE (covers CVE-2020-9327 structure)
ctx.rule("Pattern-DDL-DQL",
    "CREATE TABLE IF NOT EXISTS v0(v3, v1 GENERATED ALWAYS AS (v3) UNIQUE);\n"
    "CREATE TABLE IF NOT EXISTS v5(v6 UNIQUE, v7 UNIQUE);\n"
    "CREATE VIEW IF NOT EXISTS v8 AS SELECT coalesce(v3, v1) AS v9 FROM v0 "
    "WHERE v1 IN({Str-Literal});\n"
    "SELECT * FROM v8 JOIN v5 WHERE 0 > v7 AND v9 OR v6 = {Str-Literal}",
    weight=1.5)

# --- Pattern-GenCol-Op (P2): generated column → operation ---
# Covers CVE-2020-9327 (generated col + UNIQUE + JOIN),
# CVE-2019-19646 (generated col + PRAGMA integrity_check)

ctx.rule("Pattern-GenCol-Op",
    "CREATE TABLE IF NOT EXISTS p(a, b GENERATED ALWAYS AS (a) VIRTUAL);\n"
    "SELECT {Result-Col-List} FROM p",
    weight=2.0)
ctx.rule("Pattern-GenCol-Op",
    "CREATE TABLE IF NOT EXISTS p(a, b GENERATED ALWAYS AS ({GenCol-Expr}) UNIQUE);\n"
    "CREATE TABLE IF NOT EXISTS q(x UNIQUE, y UNIQUE);\n"
    "SELECT {Result-Col-List} FROM p JOIN q ON p.a = q.x",
    weight=2.0)
# Covers CVE-2019-19646 exactly: NOT NULL generated col + INSERT + PRAGMA
ctx.rule("Pattern-GenCol-Op",
    "CREATE TABLE IF NOT EXISTS p(a, b NOT NULL GENERATED ALWAYS AS ({GenCol-Expr}));\n"
    "INSERT INTO p(a) VALUES({Int-Literal});\n"
    "PRAGMA integrity_check",
    weight=2.5)
ctx.rule("Pattern-GenCol-Op",
    "CREATE TABLE IF NOT EXISTS p(a, b NOT NULL GENERATED ALWAYS AS ({GenCol-Expr}));\n"
    "INSERT INTO p(a) VALUES({Int-Literal});\n"
    "PRAGMA quick_check",
    weight=1.5)
ctx.rule("Pattern-GenCol-Op",
    "CREATE TABLE IF NOT EXISTS p(a {Type-Name}, b GENERATED ALWAYS AS ({GenCol-Expr}) STORED);\n"
    "INSERT INTO p(a) VALUES({Literal}),({Literal});\n"
    "SELECT {Result-Col-List} FROM p WHERE {Expr}",
    weight=1.5)

ctx.rule("GenCol-Expr", "a", weight=3.0)
ctx.rule("GenCol-Expr", "a + {Int-Literal}", weight=2.0)
ctx.rule("GenCol-Expr", "coalesce(a, b)", weight=2.0)
ctx.rule("GenCol-Expr", "a = {Int-Literal}", weight=2.0)
ctx.rule("GenCol-Expr", "a IS NULL", weight=1.0)
ctx.rule("GenCol-Expr", "a * a", weight=1.0)
ctx.rule("GenCol-Expr", "a || b", weight=1.0)

# --- Pattern-Compound (P4): INTERSECT/EXCEPT compound operators ---
# Covers CVE-2020-13871 (EXCEPT), CVE-2020-15358 (INTERSECT)

ctx.rule("Pattern-Compound",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER, b TEXT);\n"
    "INSERT INTO p VALUES({Int-Literal}, {Str-Literal}),({Int-Literal}, {Str-Literal});\n"
    "SELECT a FROM p {Compound-Op-Set} SELECT a FROM p",
    weight=2.5)
ctx.rule("Pattern-Compound",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER);\n"
    "CREATE TABLE IF NOT EXISTS q(b INTEGER);\n"
    "INSERT INTO p VALUES({Int-Literal}),({Int-Literal});\n"
    "INSERT INTO q VALUES({Int-Literal}),({Int-Literal});\n"
    "SELECT a FROM p {Compound-Op-Set} SELECT b FROM q",
    weight=2.0)
# Window with compound op in PARTITION BY (covers CVE-2020-15358 window variant)
ctx.rule("Pattern-Compound",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER);\n"
    "INSERT INTO p VALUES({Int-Literal}),({Int-Literal}),({Int-Literal});\n"
    "SELECT {Win-Func-Expr} OVER "
    "(PARTITION BY (SELECT {Int-Literal} {Compound-Op-Set} SELECT a FROM p) {Win-Order}) "
    "FROM p",
    weight=1.5)
# Compound op in subquery within WHERE
ctx.rule("Pattern-Compound",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER, b TEXT);\n"
    "CREATE TABLE IF NOT EXISTS q(c INTEGER);\n"
    "INSERT INTO p VALUES({Int-Literal}, {Str-Literal});\n"
    "INSERT INTO q VALUES({Int-Literal}),({Int-Literal});\n"
    "SELECT {Result-Col-List} FROM p WHERE a IN "
    "(SELECT a FROM p {Compound-Op-Set} SELECT c FROM q)",
    weight=2.0)

ctx.rule("Compound-Op-Set", "INTERSECT", weight=2.0)
ctx.rule("Compound-Op-Set", "EXCEPT", weight=2.0)
ctx.rule("Compound-Op-Set", "UNION ALL", weight=1.0)

# --- Pattern-Schema-Pragma (P6): DDL → DML → PRAGMA integrity_check ---
# Covers CVE-2019-19646: generated col with NOT NULL + PRAGMA = infinite loop

ctx.rule("Pattern-Schema-Pragma",
    "CREATE TABLE IF NOT EXISTS p(a, b NOT NULL GENERATED ALWAYS AS ({GenCol-Expr}));\n"
    "INSERT INTO p(a) VALUES({Int-Literal});\n"
    "PRAGMA integrity_check",
    weight=2.5)
ctx.rule("Pattern-Schema-Pragma",
    "CREATE TABLE IF NOT EXISTS p(a {Type-Name}, b {Type-Name});\n"
    "INSERT INTO p VALUES({Literal}, {Literal}),({Literal}, {Literal});\n"
    "PRAGMA quick_check",
    weight=2.0)
ctx.rule("Pattern-Schema-Pragma",
    "CREATE TABLE IF NOT EXISTS p(a INTEGER);\n"
    "PRAGMA integrity_check",
    weight=1.0)
ctx.rule("Pattern-Schema-Pragma",
    "CREATE TABLE IF NOT EXISTS p(a, b GENERATED ALWAYS AS ({GenCol-Expr}) UNIQUE);\n"
    "INSERT INTO p(a) VALUES({Int-Literal}),({Int-Literal});\n"
    "PRAGMA integrity_check(1)",
    weight=1.5)

# --- Window-Agg-Expr (P3+P5 inline): window + aggregate in same expression ---
# Used inside HAVING, IN subqueries, complex WHERE expressions.
# Covers CVE-2020-13435 (lead + SUM), CVE-2020-13871 (COUNT OVER + lead OVER)
ctx.rule("Window-Agg-Expr", "count() OVER ({Win-Partition} {Win-Order})", weight=2.0)
ctx.rule("Window-Agg-Expr", "sum({Col-Ref}) OVER ({Win-Order})", weight=2.0)
ctx.rule("Window-Agg-Expr", "lead({Col-Ref}) OVER ({Win-Order})", weight=2.0)
ctx.rule("Window-Agg-Expr", "lag({Col-Ref}) OVER ({Win-Order})", weight=2.0)
ctx.rule("Window-Agg-Expr",
    "SUM(DISTINCT CASE WHEN {Expr} THEN {Expr} ELSE 0 END)",
    weight=1.5)
ctx.rule("Window-Agg-Expr",
    "{Agg-Func} OVER ({Win-Partition} {Win-Order})",
    weight=1.5)
