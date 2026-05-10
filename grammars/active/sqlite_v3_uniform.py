# sqlite_v3.py — Structural Primitives grammar for Nautilus SQLite fuzzing
# Version: v3.3 (JSON/JSONB expansion)
# Use with: sqlite_harness_<version> (blank DB)
#
# DESIGN: Variant 3 — decomposes DDL+DQL into separate non-terminals
# (Schema-Setup, Stress-Query, Validation-Op) to maximize Splice mutation
# surface. Zero PoC contamination. All CVEs reachable through composition.
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
# Sql-Stmt dispatch (4 shapes)
# ============================================================
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Stress-Query}")
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}")
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Validation-Op}")
ctx.rule("Sql-Stmt", "SELECT {Boundary-Func-Call}")

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
# JSON table-valued functions (virtual table sources)
ctx.rule("Table-Or-Subquery", "json_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_each({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "json_tree({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_tree({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "jsonb_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "jsonb_tree({Json-Literal})")

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

# Storage qualifier for GENERATED columns.
ctx.rule("Gen-Storage", "VIRTUAL")
ctx.rule("Gen-Storage", "STORED")

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
ctx.rule("Order-By-Clause", "ORDER BY {Ordering-Term}, {Ordering-Term}, {Ordering-Term}")
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

# Schema identifiers — t1/t2/t3 kept at low weight (blank DB, silently fail).
# p/q/r/s are the primary fresh-names used by Schema-Setup rules.
ctx.rule("Table-Name", "t1")
ctx.rule("Table-Name", "t2")
ctx.rule("Table-Name", "t3")
ctx.rule("Table-Name", "p")
ctx.rule("Table-Name", "q")
ctx.rule("Table-Name", "r")
ctx.rule("Table-Name", "s")
ctx.rule("Col-Name", "c1")
ctx.rule("Col-Name", "c2")
ctx.rule("Col-Name", "c3")
ctx.rule("Col-Name", "a")     # used in pattern DDL rules
ctx.rule("Col-Name", "b")
ctx.rule("Col-Name", "rowid")
ctx.rule("Col-Name", "_rowid_")
ctx.rule("Col-Ref", "{Col-Name}")
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}")

# ============================================================
# LAYER 1: FUNCTION CALLS
# ============================================================
ctx.rule("Func-Call", "count(*)")
ctx.rule("Func-Call", "count()")
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
# ============================================================
# JSON/JSONB expansion (v3.3 — targeting json.c in SQLite 3.45+)
# ============================================================

# Json-Key: short fixed keys for JSON object paths
ctx.rule("Json-Key", "a")
ctx.rule("Json-Key", "b")
ctx.rule("Json-Key", "c")
ctx.rule("Json-Key", "key")

# Json-Path: JSON path expressions for navigation
ctx.rule("Json-Path", "'$'")
ctx.rule("Json-Path", "'$.{Json-Key}'")
ctx.rule("Json-Path", "'$.{Json-Key}.{Json-Key}'")
ctx.rule("Json-Path", "'$[{Int-Literal}]'")
ctx.rule("Json-Path", "'$[#-1]'")
ctx.rule("Json-Path", "'$.{Json-Key}[{Int-Literal}]'")
ctx.rule("Json-Path", "'$.{Json-Key}[#-1]'")
ctx.rule("Json-Path", "'$[0].{Json-Key}'")

# Json-Literal: well-formed JSON strings as function arguments
# \\{ and \\} escape literal braces so Nautilus doesn't treat them as nonterminals
ctx.rule("Json-Literal", "'\\{}'")
ctx.rule("Json-Literal", "'[]'")
ctx.rule("Json-Literal", "'\\{\"a\":1}'")
ctx.rule("Json-Literal", "'[1,2,3]'")
ctx.rule("Json-Literal", "'\\{\"a\":\\{\"b\":1}}'")
ctx.rule("Json-Literal", "'[\\{\"a\":1},\\{\"b\":2}]'")

# JSON basic forms (Layer 1)
ctx.rule("Func-Call", "json({Expr})")
ctx.rule("Func-Call", "json_valid({Expr})")
ctx.rule("Func-Call", "json_type({Expr})")
ctx.rule("Func-Call", "json_extract({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_array({Expr-List})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr}, {Str-Literal}, {Expr})")

# JSON text mutation functions
ctx.rule("Func-Call", "json_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "json_patch({Json-Literal}, {Json-Literal})")
ctx.rule("Func-Call", "json_pretty({Expr})")
ctx.rule("Func-Call", "json_quote({Expr})")

# JSONB binary output variants (new in SQLite 3.45+)
ctx.rule("Func-Call", "jsonb({Expr})")
ctx.rule("Func-Call", "jsonb_array({Expr-List})")
ctx.rule("Func-Call", "jsonb_object({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "jsonb_extract({Expr}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_patch({Json-Literal}, {Json-Literal})")

# JSON analysis functions
ctx.rule("Func-Call", "json_type({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_array_length({Expr})")
ctx.rule("Func-Call", "json_array_length({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_error_position({Expr})")

# Window-specific functions (require OVER clause to be meaningful)
ctx.rule("Func-Call", "lead({Expr})")
ctx.rule("Func-Call", "lead({Expr}, {Expr})")
ctx.rule("Func-Call", "lead({Expr}, {Expr}, {Expr})")
ctx.rule("Func-Call", "lag({Expr})")
ctx.rule("Func-Call", "lag({Expr}, {Expr})")
ctx.rule("Func-Call", "lag({Expr}, {Expr}, {Expr})")
ctx.rule("Func-Call", "row_number()")
ctx.rule("Func-Call", "rank()")
ctx.rule("Func-Call", "dense_rank()")
ctx.rule("Func-Call", "ntile({Expr})")
ctx.rule("Func-Call", "first_value({Expr})")
ctx.rule("Func-Call", "last_value({Expr})")
ctx.rule("Func-Call", "nth_value({Expr}, {Expr})")
ctx.rule("Func-Call", "percent_rank()")
ctx.rule("Func-Call", "cume_dist()")

# ============================================================
# GenCol-Expr
# ============================================================
ctx.rule("GenCol-Expr", "a")
ctx.rule("GenCol-Expr", "a + {Int-Literal}")
ctx.rule("GenCol-Expr", "coalesce(a, b)")
ctx.rule("GenCol-Expr", "a = {Int-Literal}")
ctx.rule("GenCol-Expr", "a IS NULL")
ctx.rule("GenCol-Expr", "a * a")
ctx.rule("GenCol-Expr", "a || b")
# Self-referential: column references itself (triggers CVE-2020-9327 class bugs)
ctx.rule("GenCol-Expr", "b")
ctx.rule("GenCol-Expr", "c1")
ctx.rule("GenCol-Expr", "c2")

# ============================================================
# LAYER 1: BOUNDARY LITERALS
# ============================================================

# Boundary-Int: values that trigger integer overflow / UBSan
ctx.rule("Boundary-Int", "2147483647")      # INT32_MAX
ctx.rule("Boundary-Int", "2147483648")      # INT32_MAX + 1
ctx.rule("Boundary-Int", "-2147483648")     # INT32_MIN
ctx.rule("Boundary-Int", "-2147483649")     # INT32_MIN - 1
ctx.rule("Boundary-Int", "4294967295")      # UINT32_MAX
ctx.rule("Boundary-Int", "4294967296")      # UINT32_MAX + 1
ctx.rule("Boundary-Int", "9223372036854775807")   # INT64_MAX
ctx.rule("Boundary-Int", "-9223372036854775808")  # INT64_MIN
ctx.rule("Boundary-Int", "0")
ctx.rule("Boundary-Int", "-1")
ctx.rule("Boundary-Int", "1")

# Boundary-Float: float boundary values
ctx.rule("Boundary-Float", "0.01")     # CVE-2020-13434 PoC value
ctx.rule("Boundary-Float", "0.0")
ctx.rule("Boundary-Float", "1.0")
ctx.rule("Boundary-Float", "-1.0")
ctx.rule("Boundary-Float", "1e308")
ctx.rule("Boundary-Float", "-1e308")
ctx.rule("Boundary-Float", "1e-308")
ctx.rule("Boundary-Float", "-0.0")

# ============================================================
# LAYER 2: Schema-Setup (6 alternatives)
# ============================================================

# S1: Single table, basic columns
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List})")

# S2: Table with generated column + constraints
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List-GenCol})")

# S3: Two tables (enables JOINs between p and q)
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE TABLE IF NOT EXISTS q({Col-Def-List})")

# S4: Table + VIEW
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE VIEW IF NOT EXISTS v1 AS {Select-Stmt}")

# S5: Virtual table (FTS5/FTS3)
ctx.rule("Schema-Setup",
    "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING {Fts-Engine}({Col-Name-List})")

# S6: Table + INDEX
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE INDEX IF NOT EXISTS idx1 ON p({Col-Name})")

# Col-Def-List with guaranteed generated column
ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}")
ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}, {Col-Def}")
# Self-referential generated columns (column expr references own name)
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, b AS(b) UNIQUE")
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, c1 AS(c1) UNIQUE")
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, b AS(b) NOT NULL")

ctx.rule("Gen-Constraint", "UNIQUE")
ctx.rule("Gen-Constraint", "NOT NULL")
ctx.rule("Gen-Constraint", "NOT NULL UNIQUE")
ctx.rule("Gen-Constraint", "")

ctx.rule("Fts-Engine", "fts5")
ctx.rule("Fts-Engine", "fts3")

# ============================================================
# LAYER 2: Stress-Query (8 alternatives)
# ============================================================

# Q1: Base SELECT (full compositional freedom)
ctx.rule("Stress-Query", "{Select-Stmt}")

# Q2: EXISTS subquery
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "WHERE EXISTS ({Select-Stmt})")

# Q3: NATURAL JOIN
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "NATURAL JOIN {Table-Name} WHERE {Expr}")

# Q4: Recursive CTE
ctx.rule("Stress-Query",
    "WITH RECURSIVE {Cte-Def} "
    "SELECT {Result-Col-List} FROM {Table-Name}")

# Q5: Compound query (INTERSECT/EXCEPT)
ctx.rule("Stress-Query",
    "{Select-Stmt} {Compound-Op} {Select-Stmt}")

# Q6: Self-JOIN + expression
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} {Col-Alias} ON {Expr}")

# Q7: Nested subquery chain
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM "
    "(SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr}) AS sub1")

# Q8: EXPLAIN QUERY PLAN wrapper
ctx.rule("Stress-Query",
    "EXPLAIN QUERY PLAN {Select-Stmt}")

# ============================================================
# LAYER 2: Validation-Op (4 alternatives)
# ============================================================
ctx.rule("Validation-Op", "PRAGMA integrity_check")
ctx.rule("Validation-Op", "PRAGMA quick_check")
ctx.rule("Validation-Op", "ANALYZE {Table-Name}")
ctx.rule("Validation-Op", "EXPLAIN QUERY PLAN {Select-Stmt}")

# ============================================================
# LAYER 2: Boundary-Func-Call
# ============================================================
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})")
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int})")
ctx.rule("Boundary-Func-Call",
    "printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})")
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int})")
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})")
ctx.rule("Boundary-Func-Call",
    "hex(zeroblob({Boundary-Int}))")
ctx.rule("Boundary-Func-Call",
    "round({Boundary-Float}, {Boundary-Int})")

ctx.rule("Format-Spec", "'%.*g'")
ctx.rule("Format-Spec", "'%.*f'")
ctx.rule("Format-Spec", "'%.*e'")
ctx.rule("Format-Spec", "'%.*d'")
ctx.rule("Format-Spec", "'%.*s'")

ctx.rule("Printf-Fmt-Spec", "'%d'")
ctx.rule("Printf-Fmt-Spec", "'%u'")
ctx.rule("Printf-Fmt-Spec", "'%x'")
ctx.rule("Printf-Fmt-Spec", "'%f'")
ctx.rule("Printf-Fmt-Spec", "'%s'")
ctx.rule("Printf-Fmt-Spec", "'%lld'")
ctx.rule("Printf-Fmt-Spec", "'%lli'")
ctx.rule("Printf-Fmt-Spec", "'%llu'")
