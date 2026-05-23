# sqlite_v4_fast.py — Fast-iteration production grammar for Nautilus SQLite fuzzing
# Version: v4.0b (reduced CTE limits for higher exec/sec, same attack surface as v4.0a)
#
# DESIGN: Removes SQLITE_DEBUG-only functions (fpdecode, parseuri) and boosts
# weight on production-reachable attack surfaces:
#   - High-arity expression patterns (CVE-2025-7458 class: integer overflow in KeyInfo)
#   - Variadic string concatenation functions (CVE-2025-3277 class: concat_ws overflow)
#   - New SQLite 3.44+ functions (unhex, unistr, math, median/percentile)
#   - EXPLAIN wrapper patterns (triggers different code paths in VDBE)
#   - CREATE TABLE AS SELECT with complex subqueries
#   - printf with boundary precision values
#
# Zero PoC contamination. All patterns are structural building blocks.

# ============================================================
# START
# ============================================================
ctx.rule("START", "{Sql-Stmt-List}")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};\n{Sql-Stmt-List}")

# ============================================================
# Sql-Stmt dispatch
# ============================================================
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Stress-Query}", weight=3.0)
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}", weight=2.5)
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Validation-Op}", weight=2.0)
ctx.rule("Sql-Stmt", "SELECT {Boundary-Func-Call}", weight=2.0)

# --- v4.0: New top-level patterns for zero-day hunting ---

# CTAS + DISTINCT + ORDER BY (CVE-2025-7458 class: KeyInfo overflow)
ctx.rule("Sql-Stmt",
    "CREATE TABLE IF NOT EXISTS p AS {Select-Stmt}",
    weight=2.5)

# EXPLAIN wrapper (exercises VDBE display/list code paths)
ctx.rule("Sql-Stmt", "EXPLAIN {Sql-Inner-Stmt}", weight=1.5)

# Variadic function stress (CVE-2025-3277 class)
ctx.rule("Sql-Stmt", "SELECT {Variadic-Func-Call}", weight=2.5)

# Recursive CTE feeding aggregation
ctx.rule("Sql-Stmt",
    "WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < {Cte-Limit}) "
    "{Select-Stmt}",
    weight=2.0)

# Multi-statement stress: schema + populate + complex query
ctx.rule("Sql-Stmt",
    "{Schema-Setup};\n{Insert-Stmt};\n{Insert-Stmt};\n{Stress-Query}",
    weight=1.5)

# Inner statement (for EXPLAIN wrapper — no EXPLAIN-of-EXPLAIN)
ctx.rule("Sql-Inner-Stmt", "{Select-Stmt}")
ctx.rule("Sql-Inner-Stmt", "CREATE TABLE IF NOT EXISTS p AS {Select-Stmt}")
ctx.rule("Sql-Inner-Stmt", "{Insert-Stmt}")
ctx.rule("Sql-Inner-Stmt", "{Update-Stmt}")
ctx.rule("Sql-Inner-Stmt", "{Delete-Stmt}")

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

# v4.0: DISTINCT with high-arity result columns + ORDER BY (CVE-7458 class)
ctx.rule("Select-Core",
    "SELECT DISTINCT {Wide-Result-Col-List} {From-Clause}",
    weight=3.0)
ctx.rule("Select-Core",
    "SELECT DISTINCT {Wide-Result-Col-List} {From-Clause} {Wide-Order-By}",
    weight=3.0)

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

# v4.0: Wide result column lists (many columns — triggers KeyInfo overflow class)
ctx.rule("Wide-Result-Col-List", "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}")
ctx.rule("Wide-Result-Col-List",
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, "
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}")
ctx.rule("Wide-Result-Col-List",
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, "
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, "
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, "
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}")
ctx.rule("Wide-Result-Col-List",
    "{Wide-Result-Col-List}, {Wide-Result-Col-List}",
    weight=1.5)

# v4.0: Wide ORDER BY (many ordering terms)
ctx.rule("Wide-Order-By",
    "ORDER BY {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}")
ctx.rule("Wide-Order-By",
    "ORDER BY {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}")
ctx.rule("Wide-Order-By",
    "ORDER BY {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}, "
    "{Ordering-Term}, {Ordering-Term}, {Ordering-Term}, {Ordering-Term}")

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
ctx.rule("Table-Or-Subquery", "json_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_each({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "json_tree({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_tree({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "jsonb_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "jsonb_tree({Json-Literal})")

# ============================================================
# LAYER 1: EXPRESSIONS
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

# v4.0: Wide expression lists (for variadic function arguments)
ctx.rule("Wide-Expr-List",
    "{Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}, {Expr}")
ctx.rule("Wide-Expr-List",
    "{Wide-Expr-List}, {Wide-Expr-List}")
ctx.rule("Wide-Expr-List",
    "{Wide-Expr-List}, {Wide-Expr-List}, {Wide-Expr-List}, {Wide-Expr-List}")

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

# v4.0b: CTE limits — reduced to avoid 500ms timeouts, maximize exec/sec
ctx.rule("Cte-Limit", "50", weight=2.0)
ctx.rule("Cte-Limit", "100", weight=3.0)
ctx.rule("Cte-Limit", "500", weight=2.0)
ctx.rule("Cte-Limit", "1000", weight=1.5)
ctx.rule("Cte-Limit", "5000", weight=1.0)

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
# v4.0: ANY type (for STRICT tables)
ctx.rule("Type-Name", "ANY")

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

ctx.rule("Table-Name", "t1", weight=0.3)
ctx.rule("Table-Name", "t2", weight=0.3)
ctx.rule("Table-Name", "t3", weight=0.3)
ctx.rule("Table-Name", "p", weight=2.0)
ctx.rule("Table-Name", "q", weight=1.5)
ctx.rule("Table-Name", "r", weight=0.5)
ctx.rule("Table-Name", "s", weight=0.3)
ctx.rule("Col-Name", "c1", weight=1.0)
ctx.rule("Col-Name", "c2", weight=1.0)
ctx.rule("Col-Name", "c3", weight=1.0)
ctx.rule("Col-Name", "a", weight=0.8)
ctx.rule("Col-Name", "b", weight=0.8)
ctx.rule("Col-Name", "rowid", weight=0.5)
ctx.rule("Col-Name", "_rowid_", weight=0.3)
# v4.0: additional column name for wider schemas
ctx.rule("Col-Name", "d", weight=0.5)
ctx.rule("Col-Name", "e", weight=0.3)
ctx.rule("Col-Ref", "{Col-Name}", weight=1.0)
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}", weight=1.0)

# ============================================================
# LAYER 1: FUNCTION CALLS
# ============================================================

# --- Core aggregate/scalar functions ---
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
ctx.rule("Func-Call", "replace({Expr}, {Expr}, {Expr})")
ctx.rule("Func-Call", "instr({Expr}, {Expr})")

# --- v4.0: New functions (SQLite 3.44+) ---

# String concatenation (CVE-2025-3277 class attack surface)
ctx.rule("Func-Call", "concat({Expr}, {Expr})", weight=2.0)
ctx.rule("Func-Call", "concat({Expr}, {Expr}, {Expr})", weight=2.0)
ctx.rule("Func-Call", "concat({Expr}, {Expr}, {Expr}, {Expr})", weight=1.5)
ctx.rule("Func-Call", "concat_ws({Expr}, {Expr}, {Expr})", weight=2.5)
ctx.rule("Func-Call", "concat_ws({Expr}, {Expr}, {Expr}, {Expr})", weight=2.0)
ctx.rule("Func-Call", "concat_ws({Expr}, {Expr}, {Expr}, {Expr}, {Expr})", weight=2.0)

# string_agg (SQL standard alias for group_concat)
ctx.rule("Func-Call", "string_agg({Expr}, {Str-Literal})", weight=2.0)

# octet_length (byte length — different from character length for multi-byte)
ctx.rule("Func-Call", "octet_length({Expr})", weight=1.5)

# unhex (hex decode — parsing edge cases)
ctx.rule("Func-Call", "unhex({Expr})", weight=2.0)
ctx.rule("Func-Call", "unhex({Expr}, {Expr})", weight=1.5)

# substring (SQL standard alias)
ctx.rule("Func-Call", "substring({Expr}, {Expr})", weight=1.0)
ctx.rule("Func-Call", "substring({Expr}, {Expr}, {Expr})", weight=1.0)

# unistr (Unicode string processing — escape sequences)
ctx.rule("Func-Call", "unistr({Expr})", weight=2.5)

# subtype introspection
ctx.rule("Func-Call", "subtype({Expr})", weight=1.5)

# NOTE: parseuri() and fpdecode() are SQLITE_DEBUG only — removed for production grammar

# printf with extreme precision (production-reachable path into sqlite3FpDecode)
ctx.rule("Func-Call", "printf({Format-Spec}, {Boundary-Int})", weight=3.0)
ctx.rule("Func-Call", "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Func-Call", "printf({Format-Spec}, {Boundary-Float})", weight=2.5)
ctx.rule("Func-Call", "format({Format-Spec}, {Boundary-Int})", weight=2.5)
ctx.rule("Func-Call", "format({Format-Spec}, {Boundary-Float})", weight=2.5)

# Math functions (new in 3.45+, numerical edge cases)
ctx.rule("Func-Call", "ceil({Expr})", weight=1.5)
ctx.rule("Func-Call", "floor({Expr})", weight=1.5)
ctx.rule("Func-Call", "trunc({Expr})", weight=1.5)
ctx.rule("Func-Call", "ln({Expr})", weight=1.5)
ctx.rule("Func-Call", "log({Expr})", weight=1.5)
ctx.rule("Func-Call", "log10({Expr})", weight=1.5)
ctx.rule("Func-Call", "log2({Expr})", weight=1.5)
ctx.rule("Func-Call", "log({Expr}, {Expr})", weight=1.0)
ctx.rule("Func-Call", "exp({Expr})", weight=1.5)
ctx.rule("Func-Call", "pow({Expr}, {Expr})", weight=1.5)
ctx.rule("Func-Call", "mod({Expr}, {Expr})", weight=1.5)
ctx.rule("Func-Call", "acos({Expr})", weight=1.0)
ctx.rule("Func-Call", "asin({Expr})", weight=1.0)
ctx.rule("Func-Call", "atan({Expr})", weight=1.0)
ctx.rule("Func-Call", "atan2({Expr}, {Expr})", weight=1.0)
ctx.rule("Func-Call", "cos({Expr})", weight=1.0)
ctx.rule("Func-Call", "sin({Expr})", weight=1.0)
ctx.rule("Func-Call", "tan({Expr})", weight=1.0)

# New aggregate functions (median, percentile — new in 3.46+)
ctx.rule("Func-Call", "median({Expr})", weight=2.5)
ctx.rule("Func-Call", "percentile({Expr}, {Expr})", weight=2.0)
ctx.rule("Func-Call", "percentile_cont({Expr}, {Expr})", weight=2.0)
ctx.rule("Func-Call", "percentile_disc({Expr}, {Expr})", weight=2.0)

# soundex
ctx.rule("Func-Call", "soundex({Expr})", weight=1.0)

# total (separate from sum — returns 0.0 for empty sets)
ctx.rule("Func-Call", "total({Expr})", weight=1.5)

# --- v4.0: Variadic function calls with wide argument lists ---
# These drive the concat/concat_ws overflow class
ctx.rule("Variadic-Func-Call",
    "concat({Wide-Expr-List})", weight=3.0)
ctx.rule("Variadic-Func-Call",
    "concat_ws({Expr}, {Wide-Expr-List})", weight=3.0)
ctx.rule("Variadic-Func-Call",
    "printf({Str-Literal}, {Wide-Expr-List})", weight=2.0)
ctx.rule("Variadic-Func-Call",
    "char({Wide-Expr-List})", weight=1.5)
ctx.rule("Variadic-Func-Call",
    "coalesce({Wide-Expr-List})", weight=1.5)
ctx.rule("Variadic-Func-Call",
    "max({Wide-Expr-List})", weight=1.5)
ctx.rule("Variadic-Func-Call",
    "min({Wide-Expr-List})", weight=1.5)

# ============================================================
# JSON/JSONB expansion
# ============================================================

ctx.rule("Json-Key", "a")
ctx.rule("Json-Key", "b")
ctx.rule("Json-Key", "c")
ctx.rule("Json-Key", "key")

ctx.rule("Json-Path", "'$'")
ctx.rule("Json-Path", "'$.{Json-Key}'")
ctx.rule("Json-Path", "'$.{Json-Key}.{Json-Key}'")
ctx.rule("Json-Path", "'$[{Int-Literal}]'")
ctx.rule("Json-Path", "'$[#-1]'")
ctx.rule("Json-Path", "'$.{Json-Key}[{Int-Literal}]'")
ctx.rule("Json-Path", "'$.{Json-Key}[#-1]'")
ctx.rule("Json-Path", "'$[0].{Json-Key}'")

ctx.rule("Json-Literal", "'\\{}'")
ctx.rule("Json-Literal", "'[]'")
ctx.rule("Json-Literal", "'\\{\"a\":1}'")
ctx.rule("Json-Literal", "'[1,2,3]'")
ctx.rule("Json-Literal", "'\\{\"a\":\\{\"b\":1}}'")
ctx.rule("Json-Literal", "'[\\{\"a\":1},\\{\"b\":2}]'")

ctx.rule("Func-Call", "json({Expr})")
ctx.rule("Func-Call", "json_valid({Expr})")
ctx.rule("Func-Call", "json_type({Expr})")
ctx.rule("Func-Call", "json_extract({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_array({Expr-List})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr}, {Str-Literal}, {Expr})")

ctx.rule("Func-Call", "json_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "json_patch({Json-Literal}, {Json-Literal})")
ctx.rule("Func-Call", "json_pretty({Expr})")
ctx.rule("Func-Call", "json_quote({Expr})")

ctx.rule("Func-Call", "jsonb({Expr})")
ctx.rule("Func-Call", "jsonb_array({Expr-List})")
ctx.rule("Func-Call", "jsonb_object({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "jsonb_extract({Expr}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_patch({Json-Literal}, {Json-Literal})")

ctx.rule("Func-Call", "json_type({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_array_length({Expr})")
ctx.rule("Func-Call", "json_array_length({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_error_position({Expr})")

# Window-specific functions
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
ctx.rule("GenCol-Expr", "a", weight=3.0)
ctx.rule("GenCol-Expr", "a + {Int-Literal}", weight=2.0)
ctx.rule("GenCol-Expr", "coalesce(a, b)", weight=2.0)
ctx.rule("GenCol-Expr", "a = {Int-Literal}", weight=2.0)
ctx.rule("GenCol-Expr", "a IS NULL", weight=1.0)
ctx.rule("GenCol-Expr", "a * a", weight=1.0)
ctx.rule("GenCol-Expr", "a || b", weight=1.0)
ctx.rule("GenCol-Expr", "b", weight=2.0)
ctx.rule("GenCol-Expr", "c1", weight=1.5)
ctx.rule("GenCol-Expr", "c2", weight=1.0)

# ============================================================
# LAYER 1: BOUNDARY LITERALS
# ============================================================

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
# v4.0: Additional boundary values for size overflow patterns
ctx.rule("Boundary-Int", "65535", weight=2.0)            # UINT16_MAX
ctx.rule("Boundary-Int", "65536", weight=2.0)            # UINT16_MAX + 1
ctx.rule("Boundary-Int", "32767", weight=1.5)            # INT16_MAX
ctx.rule("Boundary-Int", "32768", weight=1.5)            # INT16_MAX + 1

ctx.rule("Boundary-Float", "0.01", weight=3.0)
ctx.rule("Boundary-Float", "0.0", weight=2.0)
ctx.rule("Boundary-Float", "1.0", weight=2.0)
ctx.rule("Boundary-Float", "-1.0", weight=1.0)
ctx.rule("Boundary-Float", "1e308", weight=2.0)
ctx.rule("Boundary-Float", "-1e308", weight=2.0)
ctx.rule("Boundary-Float", "1e-308", weight=1.0)
ctx.rule("Boundary-Float", "-0.0", weight=1.0)
# v4.0: NaN/Inf-adjacent values for math functions
ctx.rule("Boundary-Float", "9e999", weight=2.0)
ctx.rule("Boundary-Float", "-9e999", weight=2.0)

# ============================================================
# LAYER 2: Schema-Setup
# ============================================================

ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List})",
    weight=1.5)

ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List-GenCol})",
    weight=3.0)

ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE TABLE IF NOT EXISTS q({Col-Def-List})",
    weight=2.5)

ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE VIEW IF NOT EXISTS v1 AS {Select-Stmt}",
    weight=2.0)

ctx.rule("Schema-Setup",
    "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING {Fts-Engine}({Col-Name-List})",
    weight=0.5)

ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE INDEX IF NOT EXISTS idx1 ON p({Col-Name})",
    weight=1.0)

# v4.0: Schema with many columns (enables wide SELECT DISTINCT)
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p(c1 INTEGER, c2 TEXT, c3 REAL, a INTEGER, b TEXT, d BLOB, e NUMERIC)",
    weight=2.0)

# v4.0: STRICT table (exercises different type checking code paths)
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List}) STRICT",
    weight=1.5)

# v4.0: WITHOUT ROWID with many columns
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL, a INTEGER, b TEXT) WITHOUT ROWID",
    weight=1.5)

ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}")
ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}, {Col-Def}")
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, b AS(b) UNIQUE", weight=2.0)
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, c1 AS(c1) UNIQUE", weight=1.5)
ctx.rule("Col-Def-List-GenCol",
    "a {Type-Name}, b AS(b) NOT NULL", weight=1.5)

ctx.rule("Gen-Constraint", "UNIQUE", weight=2.0)
ctx.rule("Gen-Constraint", "NOT NULL", weight=2.0)
ctx.rule("Gen-Constraint", "NOT NULL UNIQUE", weight=1.5)
ctx.rule("Gen-Constraint", "", weight=1.0)

ctx.rule("Fts-Engine", "fts5", weight=2.0)
ctx.rule("Fts-Engine", "fts3", weight=1.0)

# ============================================================
# LAYER 2: Stress-Query
# ============================================================

ctx.rule("Stress-Query", "{Select-Stmt}", weight=2.0)

ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "WHERE EXISTS ({Select-Stmt})",
    weight=3.0)

ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "NATURAL JOIN {Table-Name} WHERE {Expr}",
    weight=3.0)

ctx.rule("Stress-Query",
    "WITH RECURSIVE {Cte-Def} "
    "SELECT {Result-Col-List} FROM {Table-Name}",
    weight=2.5)

ctx.rule("Stress-Query",
    "{Select-Stmt} {Compound-Op} {Select-Stmt}",
    weight=2.5)

ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} {Col-Alias} ON {Expr}",
    weight=2.0)

ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM "
    "(SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr}) AS sub1",
    weight=1.5)

ctx.rule("Stress-Query",
    "EXPLAIN QUERY PLAN {Select-Stmt}",
    weight=1.5)

# v4.0: New stress patterns targeting recent code paths

# Aggregate with new functions over populated table
ctx.rule("Stress-Query",
    "SELECT {New-Agg-Func} FROM {Table-Name}",
    weight=3.0)

# DISTINCT + wide columns + ORDER BY (CVE-7458 class)
ctx.rule("Stress-Query",
    "SELECT DISTINCT {Wide-Result-Col-List} FROM {Table-Name} {Wide-Order-By}",
    weight=3.0)

# Recursive CTE feeding concat_ws (CVE-3277 class)
ctx.rule("Stress-Query",
    "WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < {Cte-Limit}) "
    "SELECT concat_ws({Str-Literal}, group_concat(x)) FROM cnt",
    weight=3.0)

# Recursive CTE feeding string_agg
ctx.rule("Stress-Query",
    "WITH RECURSIVE cnt(x) AS (VALUES(1) UNION ALL SELECT x+1 FROM cnt WHERE x < {Cte-Limit}) "
    "SELECT string_agg(CAST(x AS TEXT), {Str-Literal}) FROM cnt",
    weight=2.5)

# Window function with new aggregates
ctx.rule("Stress-Query",
    "SELECT {Func-Call} {Over-Clause} FROM {Table-Name}",
    weight=2.5)

# unistr stress (escape sequence edge cases — production reachable)
ctx.rule("Stress-Query",
    "SELECT unistr({Expr}) FROM {Table-Name}",
    weight=3.0)

# printf with boundary precision (production path into FpDecode)
ctx.rule("Stress-Query",
    "SELECT printf({Format-Spec}, {Boundary-Int}, {Boundary-Float}) FROM {Table-Name}",
    weight=3.0)

# Math function chains (numerical edge cases: NaN, Inf, overflow)
ctx.rule("Stress-Query",
    "SELECT {Math-Func-Chain} FROM {Table-Name}",
    weight=2.0)

# v4.0: New aggregate function calls
ctx.rule("New-Agg-Func", "median({Expr})", weight=3.0)
ctx.rule("New-Agg-Func", "percentile({Expr}, {Boundary-Float})", weight=2.5)
ctx.rule("New-Agg-Func", "percentile_cont({Expr}, {Boundary-Float})", weight=2.0)
ctx.rule("New-Agg-Func", "percentile_disc({Expr}, {Boundary-Float})", weight=2.0)
ctx.rule("New-Agg-Func", "string_agg({Expr}, {Str-Literal})", weight=2.0)
ctx.rule("New-Agg-Func", "total({Expr})", weight=1.5)

# v4.0: Math function chains (compose boundary values through multiple math ops)
ctx.rule("Math-Func-Chain", "ceil(ln({Expr}))", weight=2.0)
ctx.rule("Math-Func-Chain", "floor(exp({Boundary-Float}))", weight=2.0)
ctx.rule("Math-Func-Chain", "trunc(pow({Expr}, {Boundary-Int}))", weight=2.0)
ctx.rule("Math-Func-Chain", "log(abs({Expr}) + 1)", weight=1.5)
ctx.rule("Math-Func-Chain", "asin(cos({Expr}))", weight=1.5)
ctx.rule("Math-Func-Chain", "atan2({Boundary-Float}, {Boundary-Float})", weight=1.5)
ctx.rule("Math-Func-Chain", "mod({Boundary-Int}, {Expr})", weight=2.0)
ctx.rule("Math-Func-Chain", "pow({Expr}, {Expr})", weight=1.5)

# v4.0b: Feature interaction patterns (historically bug-prone combinations)

# Generated column + JOIN + aggregate (CVE-2020-9327 class interaction)
ctx.rule("Stress-Query",
    "SELECT {New-Agg-Func} FROM {Table-Name} "
    "JOIN {Table-Name} {Col-Alias} ON {Expr}",
    weight=3.0)

# New aggregate as window function + EXCEPT
ctx.rule("Stress-Query",
    "SELECT {New-Agg-Func} {Over-Clause} FROM {Table-Name} "
    "EXCEPT SELECT {Func-Call} FROM {Table-Name}",
    weight=2.5)

# RETURNING clause with new functions
ctx.rule("Stress-Query",
    "INSERT INTO {Table-Name} VALUES({Expr-List}) "
    "RETURNING {Func-Call}",
    weight=2.0)

# UPDATE with RETURNING + window function
ctx.rule("Stress-Query",
    "UPDATE {Table-Name} SET {Col-Name} = {Expr} "
    "RETURNING {Func-Call} {Over-Clause}",
    weight=2.0)

# Subquery in FROM with new aggregate + NATURAL JOIN
ctx.rule("Stress-Query",
    "SELECT * FROM (SELECT {New-Agg-Func} FROM {Table-Name}) AS sub1 "
    "NATURAL JOIN {Table-Name}",
    weight=2.5)

# CTAS with compound query + new functions
ctx.rule("Stress-Query",
    "CREATE TABLE IF NOT EXISTS r AS "
    "SELECT {Func-Call} FROM {Table-Name} "
    "{Compound-Op} SELECT {Func-Call} FROM {Table-Name}",
    weight=2.0)

# ============================================================
# LAYER 2: Validation-Op
# ============================================================
ctx.rule("Validation-Op", "PRAGMA integrity_check", weight=3.0)
ctx.rule("Validation-Op", "PRAGMA quick_check", weight=2.0)
ctx.rule("Validation-Op", "ANALYZE {Table-Name}", weight=1.5)
ctx.rule("Validation-Op", "EXPLAIN QUERY PLAN {Select-Stmt}", weight=1.5)

# ============================================================
# LAYER 2: Boundary-Func-Call
# ============================================================
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "hex(zeroblob({Boundary-Int}))", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "round({Boundary-Float}, {Boundary-Int})", weight=1.5)

# v4.0: New boundary function calls targeting recent code
ctx.rule("Boundary-Func-Call",
    "concat_ws({Str-Literal}, {Boundary-Int}, {Boundary-Int}, {Boundary-Int})", weight=2.5)
ctx.rule("Boundary-Func-Call",
    "concat({Boundary-Int}, {Boundary-Float}, {Str-Literal})", weight=2.0)
# NOTE: parseuri() and fpdecode() removed — SQLITE_DEBUG only
ctx.rule("Boundary-Func-Call",
    "unistr({Str-Literal})", weight=2.5)
ctx.rule("Boundary-Func-Call",
    "unhex({Str-Literal})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "octet_length({Str-Literal})", weight=1.5)
# printf boundary (production path)
ctx.rule("Boundary-Func-Call",
    "printf('%.*f', {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Boundary-Func-Call",
    "printf('%.*g', {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Boundary-Func-Call",
    "format('%.*e', {Boundary-Int}, {Boundary-Float})", weight=2.5)
ctx.rule("Boundary-Func-Call",
    "ceil({Boundary-Float})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "floor({Boundary-Float})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "trunc({Boundary-Float})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "exp({Boundary-Float})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "pow({Boundary-Float}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "log({Boundary-Float})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "mod({Boundary-Int}, {Boundary-Int})", weight=2.0)

ctx.rule("Format-Spec", "'%.*g'", weight=3.0)
ctx.rule("Format-Spec", "'%.*f'", weight=2.0)
ctx.rule("Format-Spec", "'%.*e'", weight=2.0)
ctx.rule("Format-Spec", "'%.*d'", weight=1.0)
ctx.rule("Format-Spec", "'%.*s'", weight=1.0)

ctx.rule("Printf-Fmt-Spec", "'%d'", weight=2.0)
ctx.rule("Printf-Fmt-Spec", "'%u'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%x'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%f'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%s'", weight=2.0)
ctx.rule("Printf-Fmt-Spec", "'%lld'", weight=3.0)
ctx.rule("Printf-Fmt-Spec", "'%lli'", weight=2.0)
ctx.rule("Printf-Fmt-Spec", "'%llu'", weight=2.0)

# ============================================================
# v4.0a: Unicode escape literals for unistr() testing
# ============================================================
ctx.rule("Unicode-Literal", "'\\u0041'", weight=2.0)
ctx.rule("Unicode-Literal", "'\\u0000'", weight=2.5)
ctx.rule("Unicode-Literal", "'\\uFFFF'", weight=2.0)
ctx.rule("Unicode-Literal", "'\\U0001F600'", weight=1.5)
ctx.rule("Unicode-Literal", "'hello\\u0000world'", weight=2.0)

# v4.0a: Large repeat strings for concat overflow testing
ctx.rule("Long-Str-Literal", "zeroblob(1000000)", weight=2.5)
ctx.rule("Long-Str-Literal", "randomblob(100000)", weight=2.0)
ctx.rule("Long-Str-Literal", "hex(zeroblob(100000))", weight=2.0)
