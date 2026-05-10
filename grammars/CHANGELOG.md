# Grammar Changelog

## v3.3 — 2026-05-10
- Add 3 new nonterminals: Json-Key (4 rules), Json-Path (8 rules), Json-Literal (6 rules)
- Add 8 JSON text mutation functions: json_insert, json_replace, json_set, json_remove, json_patch, json_pretty, json_quote, multi-key json_object
- Add 9 JSONB binary variants: jsonb, jsonb_array, jsonb_object, jsonb_extract, jsonb_insert, jsonb_replace, jsonb_set, jsonb_remove, jsonb_patch
- Add 4 JSON analysis functions: json_type (2-arg), json_array_length (1 and 2-arg), json_error_position
- Add 6 table-valued functions to Table-Or-Subquery: json_each, json_tree, jsonb_each, jsonb_tree (with path variants)
- Upgrade json_extract to use Json-Path nonterminal instead of Str-Literal
- Motivation: SQLite 3.53.0 json.c grew to 5,682 lines; zero crashes in 5×15min with v3.2 grammar. JSONB (binary JSON) entirely untested.
- All weights=1.0 (lesson from v3.0 FTS dominance)
- 520 rules total (+51 over v3.2)

## v3.2 — 2026-05-05
- Add 15 window function rules (lead, lag, row_number, rank, dense_rank, ntile, first_value, last_value, nth_value, percent_rank, cume_dist)
- Add 3 self-referential GenCol-Expr rules (b, c1, c2) for CVE-9327 class reachability
- Add 3 explicit self-ref Col-Def-List-GenCol templates (b AS(b) UNIQUE, c1 AS(c1) UNIQUE, b AS(b) NOT NULL)
- Add count() zero-arg form for window-compatible aggregate usage
- Add ORDER BY 3-term rule for multi-column ordering patterns
- Motivation: gap analysis showed 4 CVEs (9327, 13435, 13871, 15358) unreachable due to missing structural primitives
- All 6 target CVEs now have all required building blocks in grammar
- 475 rules total (+26 over v3.1)

## v3.1 — 2026-04-28
- Schema-Setup S5 (FTS virtual table) weight reduced from 2.0 to 0.5
- Motivation: V3.0 A/B test showed 92% of crashes were FTS5 — S5 dominated the crash portfolio
- Expected: more diverse crashes across genCol, view, join, and index schemas

## v3.0 — 2026-04-27
- Initial structural primitives design (commit e719c76)
- 4 Sql-Stmt shapes: Schema+Query, Schema+Insert+Query, Schema+Insert+Validation, Boundary-Func
- 6 Schema-Setup alternatives: single table, genCol, two tables, table+view, virtual table, table+index
- 8 Stress-Query alternatives: base SELECT, EXISTS, NATURAL JOIN, recursive CTE, compound, self-JOIN, nested subquery, EXPLAIN
- 4 Validation-Op: PRAGMA integrity_check, quick_check, ANALYZE, EXPLAIN
- 449 rules total
