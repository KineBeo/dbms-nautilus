# Grammar Changelog

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
