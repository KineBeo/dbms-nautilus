# SQLite EBNF Baseline Grammar for Nautilus
# Pure spec-complete grammar derived from tree-sitter-sqlite.ebnf.
# All productions map 1:1 to EBNF structural rules. No attack patterns,
# no stress templates, no weighted bias. Uniform weight (default 1.0).
#
# Purpose: baseline for comparison campaigns against pattern/attack grammars.
#
# Fixed schema (harness pre-loads):
#   CREATE TABLE t1(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL)
#   CREATE TABLE t2(c1 INTEGER, c2 TEXT, c3 REAL)
#   CREATE TABLE t3(c1 INTEGER, c2 TEXT NOT NULL, c3 REAL DEFAULT 0.0)
#   CREATE VIRTUAL TABLE fts_t1 USING fts5(c1, c2)
#   CREATE VIRTUAL TABLE fts_t2 USING fts3(c1, c2)

# ============================================================
# START
# ============================================================
ctx.rule("START", "{Sql-Stmt-List}")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};\n{Sql-Stmt-List}")

# ============================================================
# Sql-Stmt dispatch (EBNF sql_stmt production)
# ============================================================
ctx.rule("Sql-Stmt", "{Select-Stmt}")
ctx.rule("Sql-Stmt", "{Insert-Stmt}")
ctx.rule("Sql-Stmt", "{Update-Stmt}")
ctx.rule("Sql-Stmt", "{Delete-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Table-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Index-Stmt}")
ctx.rule("Sql-Stmt", "{Create-View-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Trigger-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Virtual-Table-Stmt}")
ctx.rule("Sql-Stmt", "{Drop-Stmt}")
ctx.rule("Sql-Stmt", "{Alter-Table-Stmt}")
ctx.rule("Sql-Stmt", "{Pragma-Stmt}")
ctx.rule("Sql-Stmt", "{Analyze-Stmt}")
ctx.rule("Sql-Stmt", "{Vacuum-Stmt}")
ctx.rule("Sql-Stmt", "{Attach-Stmt}")
ctx.rule("Sql-Stmt", "{Reindex-Stmt}")
ctx.rule("Sql-Stmt", "{Savepoint-Stmt}")
ctx.rule("Sql-Stmt", "{Rollback-Stmt}")
ctx.rule("Sql-Stmt", "{Release-Stmt}")
ctx.rule("Sql-Stmt", "{Begin-Stmt}")
ctx.rule("Sql-Stmt", "{Commit-Stmt}")
ctx.rule("Sql-Stmt", "{Detach-Stmt}")

# ============================================================
# SELECT (EBNF select_stmt, _select_core)
# ============================================================
ctx.rule("Select-Stmt", "{Select-Core}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core}")
ctx.rule("Select-Stmt", "{Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause} {Limit-Clause}")

ctx.rule("Select-Core", "SELECT {Result-Col-List}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Where-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Where-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause} {Where-Clause}")
ctx.rule("Select-Core", "SELECT ALL {Result-Col-List} {From-Clause}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List}")
ctx.rule("Select-Core", "SELECT ALL {Result-Col-List}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause} {Where-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Group-By-Clause} {Window-Clause}")
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
ctx.rule("Join-Operator", "NATURAL LEFT OUTER JOIN")
ctx.rule("Join-Operator", "NATURAL INNER JOIN")
ctx.rule("Join-Operator", "NATURAL CROSS JOIN")
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
# EXPRESSIONS (EBNF _expr)
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
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} WHEN {Expr} THEN {Expr} END")
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} WHEN {Expr} THEN {Expr} ELSE {Expr} END")
ctx.rule("Expr", "({Expr}, {Expr})")
ctx.rule("Expr", "{Expr} NOT GLOB {Expr}")

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
# WINDOW / FRAME / ORDERING (EBNF window_defn, frame_spec, ordering_term)
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
ctx.rule("Ordering-Term", "{Expr} NULLS FIRST")
ctx.rule("Ordering-Term", "{Expr} NULLS LAST")

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
ctx.rule("Frame-Spec", "ROWS UNBOUNDED PRECEDING")
ctx.rule("Frame-Spec", "ROWS {Expr} PRECEDING")
ctx.rule("Frame-Spec", "ROWS CURRENT ROW")
ctx.rule("Frame-Spec", "RANGE UNBOUNDED PRECEDING")

ctx.rule("Filter-Clause", "FILTER (WHERE {Expr})")

ctx.rule("Window-Clause", "WINDOW w1 AS ({Window-Defn})")
ctx.rule("Window-Clause", "WINDOW w1 AS ({Window-Defn}), w2 AS ({Window-Defn})")

# ============================================================
# WITH / CTEs (EBNF with_clause, common_table_expression)
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
# DML (EBNF insert_stmt, update_stmt, delete_stmt)
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
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}), ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} ({Col-Name-List}) VALUES ({Expr-List}) RETURNING {Result-Col-List}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} {Select-Stmt} RETURNING {Result-Col-List}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}), ({Expr-List}), ({Expr-List})")

ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr}, {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR IGNORE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR REPLACE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} RETURNING {Result-Col-List}")
ctx.rule("Update-Stmt", "{With-Clause} UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR ABORT {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR FAIL {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR ROLLBACK {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} FROM {Join-Clause}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr} ORDER BY {Ordering-Term} LIMIT {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr} RETURNING {Result-Col-List}")

ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name} WHERE {Expr}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr} ORDER BY {Ordering-Term} LIMIT {Expr}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name} WHERE {Expr} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name}")

# ============================================================
# DDL (EBNF create_*_stmt, alter_table_stmt, drop_*_stmt)
# ============================================================
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TEMP TABLE {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) STRICT")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} AS {Select-Stmt}")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}, {Table-Constraint})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}, {Table-Constraint}, {Table-Constraint})")
ctx.rule("Create-Table-Stmt", "CREATE TEMP TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List}) WITHOUT ROWID")
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List}) STRICT")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID, STRICT")

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
ctx.rule("Col-Def", "{Col-Name} {Type-Name} {Foreign-Key-Clause}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} NOT NULL {Foreign-Key-Clause}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY AUTOINCREMENT")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY ASC")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY DESC")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} COLLATE NOCASE")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} DEFAULT ({Expr})")

ctx.rule("Table-Constraint", "PRIMARY KEY ({Col-Name})")
ctx.rule("Table-Constraint", "PRIMARY KEY ({Col-Name}, {Col-Name})")
ctx.rule("Table-Constraint", "UNIQUE ({Col-Name})")
ctx.rule("Table-Constraint", "UNIQUE ({Col-Name}, {Col-Name})")
ctx.rule("Table-Constraint", "CHECK ({Expr})")
ctx.rule("Table-Constraint", "FOREIGN KEY ({Col-Name}) {Foreign-Key-Clause}")
ctx.rule("Table-Constraint", "FOREIGN KEY ({Col-Name}, {Col-Name}) {Foreign-Key-Clause}")
ctx.rule("Table-Constraint", "PRIMARY KEY ({Col-Name}) ON CONFLICT {Conflict-Action}")
ctx.rule("Table-Constraint", "UNIQUE ({Col-Name}) ON CONFLICT {Conflict-Action}")

ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name})")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}, {Col-Name})")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE CASCADE")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE SET NULL")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE SET DEFAULT")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE RESTRICT")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE NO ACTION")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON UPDATE CASCADE")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON UPDATE SET NULL")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON UPDATE RESTRICT")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) ON DELETE CASCADE ON UPDATE CASCADE")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) DEFERRABLE INITIALLY DEFERRED")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) NOT DEFERRABLE INITIALLY IMMEDIATE")
ctx.rule("Foreign-Key-Clause", "REFERENCES {Table-Name} ({Col-Name}) MATCH {Col-Name}")

ctx.rule("Conflict-Action", "ROLLBACK")
ctx.rule("Conflict-Action", "ABORT")
ctx.rule("Conflict-Action", "FAIL")
ctx.rule("Conflict-Action", "IGNORE")
ctx.rule("Conflict-Action", "REPLACE")

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
ctx.rule("Create-View-Stmt", "CREATE TEMP VIEW IF NOT EXISTS v1 AS {Select-Stmt}")
ctx.rule("Create-View-Stmt", "CREATE VIEW IF NOT EXISTS v1 ({Col-Name-List}) AS {Select-Stmt}")

ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5({Col-Name-List})")
ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3({Col-Name-List})")
ctx.rule("Create-Virtual-Table-Stmt", "CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2)")

ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 BEFORE UPDATE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 INSTEAD OF DELETE ON v1 BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 BEFORE DELETE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER DELETE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER UPDATE OF {Col-Name} ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} FOR EACH ROW BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} WHEN {Expr} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} FOR EACH ROW WHEN {Expr} BEGIN {Trigger-Body} END")
ctx.rule("Trigger-Body", "SELECT {Result-Col-List} FROM {Table-Name};")
ctx.rule("Trigger-Body", "INSERT INTO {Table-Name} VALUES({Expr-List});")
ctx.rule("Trigger-Body", "UPDATE {Table-Name} SET {Col-Name} = {Expr};")
ctx.rule("Trigger-Body", "DELETE FROM {Table-Name};")

ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} RENAME TO {Table-Name}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} RENAME COLUMN {Col-Name} TO {Col-Name}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} ADD COLUMN {Col-Def}")
ctx.rule("Alter-Table-Stmt", "ALTER TABLE {Table-Name} DROP COLUMN {Col-Name}")

ctx.rule("Drop-Stmt", "DROP TABLE IF EXISTS {Table-Name}")
ctx.rule("Drop-Stmt", "DROP TABLE {Table-Name}")
ctx.rule("Drop-Stmt", "DROP INDEX IF EXISTS idx1")
ctx.rule("Drop-Stmt", "DROP VIEW IF EXISTS v1")
ctx.rule("Drop-Stmt", "DROP TRIGGER IF EXISTS trg1")
ctx.rule("Drop-Stmt", "DROP INDEX idx1")
ctx.rule("Drop-Stmt", "DROP VIEW v1")
ctx.rule("Drop-Stmt", "DROP TRIGGER trg1")

# ============================================================
# MISC STATEMENTS (EBNF pragma_stmt, attach_stmt, analyze_stmt, etc.)
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
ctx.rule("Rollback-Stmt", "ROLLBACK TRANSACTION")
ctx.rule("Rollback-Stmt", "ROLLBACK TO sp1")

ctx.rule("Begin-Stmt", "BEGIN")
ctx.rule("Begin-Stmt", "BEGIN DEFERRED")
ctx.rule("Begin-Stmt", "BEGIN IMMEDIATE")
ctx.rule("Begin-Stmt", "BEGIN EXCLUSIVE")
ctx.rule("Begin-Stmt", "BEGIN DEFERRED TRANSACTION")
ctx.rule("Begin-Stmt", "BEGIN IMMEDIATE TRANSACTION")
ctx.rule("Begin-Stmt", "BEGIN EXCLUSIVE TRANSACTION")
ctx.rule("Begin-Stmt", "BEGIN TRANSACTION")

ctx.rule("Commit-Stmt", "COMMIT")
ctx.rule("Commit-Stmt", "END")
ctx.rule("Commit-Stmt", "COMMIT TRANSACTION")
ctx.rule("Commit-Stmt", "END TRANSACTION")

ctx.rule("Detach-Stmt", "DETACH db2")
ctx.rule("Detach-Stmt", "DETACH DATABASE db2")

ctx.rule("Where-Clause", "WHERE {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr} HAVING {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr}, {Expr}")
ctx.rule("Group-By-Clause", "GROUP BY {Expr}, {Expr} HAVING {Expr}")
ctx.rule("Order-By-Clause", "ORDER BY {Ordering-Term}")
ctx.rule("Order-By-Clause", "ORDER BY {Ordering-Term}, {Ordering-Term}")
ctx.rule("Limit-Clause", "LIMIT {Expr}")
ctx.rule("Limit-Clause", "LIMIT {Expr} OFFSET {Expr}")
ctx.rule("Limit-Clause", "LIMIT {Expr}, {Expr}")

# ============================================================
# TERMINALS / LITERALS (EBNF _literal_value, numeric_literal, string_literal, etc.)
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

# Fixed schema identifiers
ctx.rule("Table-Name", "t1")
ctx.rule("Table-Name", "t2")
ctx.rule("Table-Name", "t3")
ctx.rule("Col-Name", "c1")
ctx.rule("Col-Name", "c2")
ctx.rule("Col-Name", "c3")
ctx.rule("Col-Name", "rowid")
ctx.rule("Col-Name", "_rowid_")
ctx.rule("Col-Ref", "{Col-Name}")
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}")

# ============================================================
# FUNCTION CALLS (EBNF function_name '(' args ')')
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
