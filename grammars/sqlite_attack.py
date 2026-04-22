# sqlite_attack.py — CVE-distilled attack-pattern grammar for SQLite.
#
# Produced per spec: docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md
# Philosophy: Nautilus-mruby shrink — small vocabulary, one canonical form per
# construct, shared non-terminals so patterns compose, no hand-coded nesting.
#
# Corpus: 6 SQLite CVEs documented in docs/cve-list.md
#   CVE-2020-15358  CVE-2020-13871  CVE-2020-13435
#   CVE-2020-13434  CVE-2020-9327   CVE-2019-19646
#
# 8 attack patterns: one per CVE + P-TRIGGER-GROUPCONCAT (CVE-13434 original PoC
# trigger path) + P-COMPOUND-MIX (derived combination pattern).
#
# No weights — v1 ships Nautilus-default uniform selection. Weights are added
# by a separate spec once the RL design is settled.

# ============================================================
# SECTION 1: START + statement list
# ============================================================

ctx.rule("START", "{Sql-Stmt-List}")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};\n{Sql-Stmt-List}")

# Sql-Stmt alternatives are populated progressively in later sections.
# Each SECTION-N task below adds its own Sql-Stmt alternatives.

# ============================================================
# SECTION 2: Vocabulary — literals and identifiers
# Every value has provenance in spec §4.
# ============================================================

# --- Identifiers (§4.1) ---
ctx.rule("Table-Name", "a")
ctx.rule("Table-Name", "t1")
ctx.rule("Table-Name", "t2")
ctx.rule("Table-Name", "t3")

ctx.rule("Col-Name", "b")
ctx.rule("Col-Name", "c")
ctx.rule("Col-Name", "c1")
ctx.rule("Col-Name", "c2")

ctx.rule("View-Name", "v1")
ctx.rule("View-Name", "v2")

ctx.rule("Alias", "x")
ctx.rule("Alias", "y")

# --- Integer literals (§4.2): corpus + INT32 boundaries ---
ctx.rule("Int-Lit", "0")
ctx.rule("Int-Lit", "1")
ctx.rule("Int-Lit", "2")
ctx.rule("Int-Lit", "3")
ctx.rule("Int-Lit", "9")
ctx.rule("Int-Lit", "123")
ctx.rule("Int-Lit", "2147483647")
ctx.rule("Int-Lit", "-2147483648")
ctx.rule("Int-Lit", "-1")

# Boundary-Int is a named subset used by P-BOUNDARY-FUNC and P-TRIGGER-GROUPCONCAT
ctx.rule("Boundary-Int", "2147483647")
ctx.rule("Boundary-Int", "-2147483648")
ctx.rule("Boundary-Int", "2147483646")
ctx.rule("Boundary-Int", "-2147483647")

# --- Real literals (§4.2) ---
ctx.rule("Real-Lit", "0.01")
ctx.rule("Real-Lit", "3.1")

# --- String literals (§4.2): corpus-exact + LIKE metachar ---
ctx.rule("Str-Lit", "'abc'")
ctx.rule("Str-Lit", "'SM PACK'")
ctx.rule("Str-Lit", "'s%'")
ctx.rule("Str-Lit", "'Y'")
ctx.rule("Str-Lit", "'MED BOX'")
ctx.rule("Str-Lit", "'GERMANY''s%'")
ctx.rule("Str-Lit", "'Brand#23'")

# --- Blob literals (§4.2): boundary values for FTS5/encoding paths ---
ctx.rule("Blob-Lit", "x'00'")
ctx.rule("Blob-Lit", "x'ff'")
ctx.rule("Blob-Lit", "x'4142'")

# --- NULL ---
ctx.rule("Null-Lit", "NULL")

# --- Literal: any of the above ---
ctx.rule("Literal", "{Int-Lit}")
ctx.rule("Literal", "{Real-Lit}")
ctx.rule("Literal", "{Str-Lit}")
ctx.rule("Literal", "{Blob-Lit}")
ctx.rule("Literal", "{Null-Lit}")

# ============================================================
# SECTION 3: Types and collations (§4.3)
# ============================================================

ctx.rule("Type-Name", "INTEGER")
ctx.rule("Type-Name", "DOUBLE")
ctx.rule("Type-Name", "TEXT")
ctx.rule("Type-Name", "BLOB")

ctx.rule("Collation-Name", "BINARY")
ctx.rule("Collation-Name", "NOCASE")
ctx.rule("Collation-Name", "RTRIM")

# ============================================================
# SECTION 4: Canonical SQL forms (§5)
# One form per construct; optional sub-clauses via *-Opt non-terminals.
# ============================================================

# --- Sql-Stmt dispatch (base statements) ---
ctx.rule("Sql-Stmt", "{Select-Stmt}")
ctx.rule("Sql-Stmt", "{Insert-Stmt}")
ctx.rule("Sql-Stmt", "{Update-Stmt}")
ctx.rule("Sql-Stmt", "{Delete-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Table-Stmt}")
ctx.rule("Sql-Stmt", "{Create-View-Stmt}")
ctx.rule("Sql-Stmt", "{Create-Trigger-Stmt}")
ctx.rule("Sql-Stmt", "{Pragma-Stmt}")

# --- SELECT (one canonical form with optional clauses) ---
ctx.rule("Select-Stmt",
    "SELECT {Result-Col-List}{From-Clause-Opt}{Where-Clause-Opt}"
    "{Group-By-Clause-Opt}{Having-Clause-Opt}{Compound-Op-Clause-Opt}"
    "{Order-By-Clause-Opt}")

ctx.rule("Result-Col-List", "*")
ctx.rule("Result-Col-List", "{Expr}")
ctx.rule("Result-Col-List", "{Expr} AS {Col-Name}")
ctx.rule("Result-Col-List", "{Expr}, {Result-Col-List}")

# Optional clauses: each expands to empty or the real clause.
ctx.rule("From-Clause-Opt", "")
ctx.rule("From-Clause-Opt", " FROM {From-Target}")

ctx.rule("From-Target", "{Table-Name}")
ctx.rule("From-Target", "{Table-Name} {Alias}")
ctx.rule("From-Target", "{Table-Name}, {Table-Name}")
ctx.rule("From-Target", "{Table-Name} {Join-Chain}")

ctx.rule("Where-Clause-Opt", "")
ctx.rule("Where-Clause-Opt", " WHERE {Boolean-Expr}")

ctx.rule("Group-By-Clause-Opt", "")
ctx.rule("Group-By-Clause-Opt", " GROUP BY {Expr}")
ctx.rule("Group-By-Clause-Opt", " GROUP BY {Expr}, {Expr}")

ctx.rule("Having-Clause-Opt", "")
ctx.rule("Having-Clause-Opt", " HAVING {Boolean-Expr}")

# Only INTERSECT and EXCEPT (§5).
ctx.rule("Compound-Op-Clause-Opt", "")
ctx.rule("Compound-Op-Clause-Opt", " {Compound-Op} SELECT {Result-Col-List}{From-Clause-Opt}{Where-Clause-Opt}")

ctx.rule("Compound-Op", "INTERSECT")
ctx.rule("Compound-Op", "EXCEPT")

ctx.rule("Order-By-Clause-Opt", "")
ctx.rule("Order-By-Clause-Opt", " {Order-By}")

# --- CREATE TABLE (one canonical form) ---
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name}({Col-Def-List})")

ctx.rule("Col-Def-List", "{Col-Def}")
ctx.rule("Col-Def-List", "{Col-Def}, {Col-Def-List}")

ctx.rule("Col-Def", "{Col-Name}")
ctx.rule("Col-Def", "{Col-Name} {Type-Name}")
ctx.rule("Col-Def", "{Col-Name} UNIQUE")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} UNIQUE")
ctx.rule("Col-Def", "{Col-Name} UNIQUE ON CONFLICT REPLACE")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} CHECK({Boolean-Expr})")
ctx.rule("Col-Def", "{GenCol-Def}")

# --- INSERT (one canonical form; multi-row values covered) ---
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name}({Col-Name}) VALUES ({Expr})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}), ({Expr-List})")

# --- UPDATE (one canonical form) ---
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Boolean-Expr}")

# --- DELETE (one canonical form) ---
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Boolean-Expr}")

# --- PRAGMA (restricted to names with CVE/bug history, §8) ---
ctx.rule("Pragma-Stmt", "PRAGMA {PRAGMA-Name}")

# --- Create View (via shared non-terminal) ---
ctx.rule("Create-View-Stmt", "{View-Def}")

# --- Create Trigger (plain form; used by P-TRIGGER-GROUPCONCAT) ---
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER {Col-Name} INSERT ON {Table-Name} BEGIN {Sql-Stmt}; END")

# ============================================================
# SECTION 5: Shared non-terminals (§7)
# The composition substrate — patterns share these so splice mutation
# recombines sub-expressions across CVEs.
# ============================================================

# --- Expr (core, recursive, shallow — Random Recursive Mutation amplifies) ---
ctx.rule("Expr", "{Literal}")
ctx.rule("Expr", "{Col-Ref}")
ctx.rule("Expr", "({Expr})")
ctx.rule("Expr", "{Expr} {Bin-Op} {Expr}")
ctx.rule("Expr", "({Scalar-Subquery})")
ctx.rule("Expr", "{Case-Expr}")
ctx.rule("Expr", "{Builtin-Func-Call}")
ctx.rule("Expr", "{Agg-Func-Call}")
ctx.rule("Expr", "{Coalesce-Window-Expr}")

ctx.rule("Bin-Op", "+")
ctx.rule("Bin-Op", "-")
ctx.rule("Bin-Op", "*")
ctx.rule("Bin-Op", "/")

ctx.rule("Case-Expr", "CASE WHEN {Boolean-Expr} THEN {Expr} ELSE {Expr} END")

ctx.rule("Expr-List", "{Expr}")
ctx.rule("Expr-List", "{Expr}, {Expr-List}")

# --- Col-Ref (qualified and unqualified) ---
ctx.rule("Col-Ref", "{Col-Name}")
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}")
ctx.rule("Col-Ref", "{Alias}.{Col-Name}")

# --- Boolean-Expr (recursive, flat logical combinators) ---
ctx.rule("Boolean-Expr", "{Expr} {Compare-Op} {Expr}")
ctx.rule("Boolean-Expr", "{Expr} IN ({Expr-List})")
ctx.rule("Boolean-Expr", "{Expr} IN ({Scalar-Subquery})")
ctx.rule("Boolean-Expr", "{Expr} LIKE {Str-Lit}")
ctx.rule("Boolean-Expr", "{Boolean-Expr} AND {Boolean-Expr}")
ctx.rule("Boolean-Expr", "{Boolean-Expr} OR {Boolean-Expr}")
ctx.rule("Boolean-Expr", "NOT {Boolean-Expr}")
ctx.rule("Boolean-Expr", "({Boolean-Expr})")

ctx.rule("Compare-Op", "=")
ctx.rule("Compare-Op", "<>")
ctx.rule("Compare-Op", "<")
ctx.rule("Compare-Op", ">")
ctx.rule("Compare-Op", "<=")
ctx.rule("Compare-Op", ">=")

# --- Scalar-Subquery (recursive; the shared CVE-13435/13871 substrate) ---
ctx.rule("Scalar-Subquery", "SELECT {Expr}")
ctx.rule("Scalar-Subquery", "SELECT {Expr} FROM {Table-Name}")
ctx.rule("Scalar-Subquery", "SELECT {Expr} FROM {Table-Name} WHERE {Boolean-Expr}")
ctx.rule("Scalar-Subquery", "SELECT ({Scalar-Subquery}) FROM {Table-Name}")
ctx.rule("Scalar-Subquery", "SELECT ({Scalar-Subquery}) FROM {Table-Name} WHERE {Boolean-Expr}")
ctx.rule("Scalar-Subquery", "{Scalar-Subquery} INTERSECT {Scalar-Subquery}")

# --- Join-Chain (recursive; one op per step) ---
ctx.rule("Join-Chain", "{Join-Op} {Table-Name}")
ctx.rule("Join-Chain", "{Join-Op} {Table-Name} {Alias}")
ctx.rule("Join-Chain", "{Join-Op} {Table-Name} ON {Boolean-Expr}")
ctx.rule("Join-Chain", "{Join-Chain} {Join-Op} {Table-Name}")

ctx.rule("Join-Op", "JOIN")
ctx.rule("Join-Op", "NATURAL JOIN")
ctx.rule("Join-Op", ",")

# --- Generated columns (§5 + spec §7) ---
ctx.rule("GenCol-Def", "{Col-Name} AS ({Expr})")
ctx.rule("GenCol-Def", "{Col-Name} NOT NULL GENERATED ALWAYS AS ({Expr})")
ctx.rule("GenCol-Def", "{Col-Name} AS ({Expr}) UNIQUE")

# --- View-Def (shared by P-INTERSECT-VIEW and P-GENCOL-JOIN-COALESCE) ---
ctx.rule("View-Def", "CREATE VIEW {View-Name} AS {Select-Stmt}")
ctx.rule("View-Def", "CREATE VIEW {View-Name}({Col-Name}) AS {Select-Stmt}")

# --- Window functions (§8 source) ---
ctx.rule("Window-Func-Call", "{Window-Func-Name}({Expr}) OVER ()")
ctx.rule("Window-Func-Call", "{Window-Func-Name}({Expr}) OVER ({Order-By})")
ctx.rule("Window-Func-Call", "COUNT() OVER ({Order-By})")

# --- Aggregate functions (§8 source) ---
ctx.rule("Agg-Func-Call", "{Agg-Func-Name}({Expr})")
ctx.rule("Agg-Func-Call", "{Agg-Func-Name}(DISTINCT {Expr})")
ctx.rule("Agg-Func-Call", "COUNT()")
ctx.rule("Agg-Func-Call", "group_concat({Expr}, {Int-Lit})")

# --- Coalesce-Window-Expr (the cross-CVE shared signal) ---
ctx.rule("Coalesce-Window-Expr", "coalesce({Window-Func-Call}, {Agg-Func-Call})")
ctx.rule("Coalesce-Window-Expr", "coalesce({Col-Ref}, {Window-Func-Call})")

# --- Order-By (used by CVE-13871/15358) ---
ctx.rule("Order-By", "ORDER BY {Expr}")
ctx.rule("Order-By", "ORDER BY {Expr}, {Expr}")
ctx.rule("Order-By", "ORDER BY {Expr}, {Expr}, {Expr}")

# --- Builtin-Func-Call (§8 source) ---
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr})")
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr}, {Expr})")
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr}, {Expr}, {Expr})")

# ============================================================
# SECTION 5b: Tight non-terminals for B2 fidelity (measurement-and-fidelity §3.2)
# One production each. Pattern rules in Section 6 reference these by name.
# Composition still happens INSIDE each tight rule via shared vocabulary NTs.
# ============================================================

ctx.rule("Scalar-Subquery-CoalesceWindow",
    "SELECT (SELECT coalesce({Window-Func-Call}, {Agg-Func-Call})) "
    "FROM {Table-Name} {Alias} WHERE {Col-Ref}")

ctx.rule("Join-Chain-NaturalPair",
    "JOIN {Table-Name} {Alias} ON {Expr} NATURAL JOIN {Table-Name}")

ctx.rule("Join-Chain-CommaJoin-Pair",
    ", {Table-Name}")

ctx.rule("GenCol-Def-SelfRef",
    "{Col-Name} AS ({Col-Name}) UNIQUE")

ctx.rule("GenCol-Def-NotNull",
    "{Col-Name} NOT NULL GENERATED ALWAYS AS ({Boolean-Expr})")

ctx.rule("View-Def-OrderedSelect",
    "CREATE VIEW {View-Name} AS SELECT {Col-Name} FROM {Table-Name} ORDER BY {Col-Name}")

ctx.rule("Scalar-Subquery-HavingWindow",
    "SELECT {Col-Ref} FROM {Table-Name} GROUP BY {Col-Ref} HAVING ({Coalesce-Window-Expr})")


# ============================================================
# SECTION 6: Attack patterns (§6 catalog — 8 patterns)
# Each pattern = one CVE (or derived). Multi-statement skeletons
# that expand to shared non-terminals from §7.
# ============================================================

# Dispatch: every pattern is reachable through Sql-Stmt
ctx.rule("Sql-Stmt", "{Pattern-P15358}")
ctx.rule("Sql-Stmt", "{Pattern-P13871}")
ctx.rule("Sql-Stmt", "{Pattern-P13435}")
ctx.rule("Sql-Stmt", "{Pattern-P13434-Boundary}")
ctx.rule("Sql-Stmt", "{Pattern-P13434-Trigger}")
ctx.rule("Sql-Stmt", "{Pattern-P9327}")
ctx.rule("Sql-Stmt", "{Pattern-P19646}")
ctx.rule("Sql-Stmt", "{Pattern-Compound-Mix}")

# --- CVE-2020-15358: INTERSECT + VIEW ---
ctx.rule("Pattern-P15358",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "{View-Def-OrderedSelect};\n"
    "SELECT * FROM {Table-Name}, {Table-Name} "
    "WHERE {Col-Ref} = ({Scalar-Subquery} INTERSECT {Scalar-Subquery}) "
    "AND {Col-Ref} = {Int-Lit}")

# --- CVE-2020-13871: HAVING + window + EXCEPT ---
ctx.rule("Pattern-P13871",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT ({Scalar-Subquery-HavingWindow}) FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")

# --- CVE-2020-13435: JOIN + NATURAL JOIN + coalesce window ---
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain-NaturalPair} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery-CoalesceWindow}))")

# --- CVE-2020-13434 simplified PoC: SELECT-time boundary-int sink ---
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}('%.*g', {Boundary-Int}, {Real-Lit})")
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}({Boundary-Int})")
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}({Str-Lit}, {Boundary-Int}, {Expr})")

# --- CVE-2020-13434 original PoC: INSERT-time sink via trigger ---
ctx.rule("Pattern-P13434-Trigger",
    "CREATE TABLE {Table-Name}({Col-Name} {Type-Name} CHECK("
    "NOT CASE WHEN {Builtin-Func}({Col-Ref}, {Col-Ref}) THEN 0 END) "
    "UNIQUE ON CONFLICT REPLACE);\n"
    "CREATE TRIGGER {Col-Name} INSERT ON {Table-Name} BEGIN "
    "INSERT INTO {Table-Name} SELECT group_concat({Col-Ref}, {Boundary-Int}) "
    "FROM {Table-Name}; END;\n"
    "INSERT INTO {Table-Name} VALUES ({Null-Lit}), ({Int-Lit}), ({Int-Lit});\n"
    "UPDATE {Table-Name} SET {Col-Name} = {Int-Lit}")

# --- CVE-2020-9327: generated col + JOIN + coalesce ---
ctx.rule("Pattern-P9327",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def-SelfRef});\n"
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE, {Col-Name} UNIQUE);\n"
    "{View-Def};\n"
    "SELECT * FROM {View-Name}{Join-Chain-CommaJoin-Pair} WHERE {Boolean-Expr}")

# --- CVE-2019-19646: generated col + integrity_check ---
ctx.rule("Pattern-P19646",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def-NotNull});\n"
    "INSERT INTO {Table-Name}({Col-Name}) VALUES ({Int-Lit});\n"
    "PRAGMA integrity_check")

# --- Derived: P-COMPOUND-MIX combines INTERSECT + EXCEPT usage ---
ctx.rule("Pattern-Compound-Mix",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT {Col-Ref} FROM {Table-Name} "
    "INTERSECT SELECT {Col-Ref} FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")

# ============================================================
# SECTION 7: Target-specific symbols (§8)
# ============================================================

ctx.rule("Builtin-Func", "printf")
ctx.rule("Builtin-Func", "format")
ctx.rule("Builtin-Func", "zeroblob")
ctx.rule("Builtin-Func", "hex")
ctx.rule("Builtin-Func", "substr")
ctx.rule("Builtin-Func", "quote")
ctx.rule("Builtin-Func", "typeof")
ctx.rule("Builtin-Func", "likelihood")
ctx.rule("Builtin-Func", "ifnull")
ctx.rule("Builtin-Func", "coalesce")
ctx.rule("Builtin-Func", "iif")
ctx.rule("Builtin-Func", "random")
ctx.rule("Builtin-Func", "randomblob")

ctx.rule("Agg-Func-Name", "sum")
ctx.rule("Agg-Func-Name", "count")
ctx.rule("Agg-Func-Name", "avg")
ctx.rule("Agg-Func-Name", "group_concat")
ctx.rule("Agg-Func-Name", "max")
ctx.rule("Agg-Func-Name", "min")
ctx.rule("Agg-Func-Name", "total")

ctx.rule("Window-Func-Name", "lead")
ctx.rule("Window-Func-Name", "lag")
ctx.rule("Window-Func-Name", "row_number")
ctx.rule("Window-Func-Name", "rank")
ctx.rule("Window-Func-Name", "dense_rank")
ctx.rule("Window-Func-Name", "first_value")
ctx.rule("Window-Func-Name", "last_value")
ctx.rule("Window-Func-Name", "nth_value")

ctx.rule("PRAGMA-Name", "integrity_check")
ctx.rule("PRAGMA-Name", "foreign_key_check")
ctx.rule("PRAGMA-Name", "writable_schema")
ctx.rule("PRAGMA-Name", "encoding")
ctx.rule("PRAGMA-Name", "journal_mode")
ctx.rule("PRAGMA-Name", "schema_version")
ctx.rule("PRAGMA-Name", "cache_size")
ctx.rule("PRAGMA-Name", "page_size")

ctx.rule("Module-Name", "fts5")
ctx.rule("Module-Name", "fts4")
ctx.rule("Module-Name", "rtree")
ctx.rule("Module-Name", "geopoly")
ctx.rule("Module-Name", "zipfile")
