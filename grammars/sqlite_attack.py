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
