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
