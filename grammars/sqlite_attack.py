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
