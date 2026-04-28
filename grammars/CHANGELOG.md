# Grammar Changelog

## v3.0 — 2026-04-27
- Initial structural primitives design (commit e719c76)
- 4 Sql-Stmt shapes: Schema+Query, Schema+Insert+Query, Schema+Insert+Validation, Boundary-Func
- 6 Schema-Setup alternatives: single table, genCol, two tables, table+view, virtual table, table+index
- 8 Stress-Query alternatives: base SELECT, EXISTS, NATURAL JOIN, recursive CTE, compound, self-JOIN, nested subquery, EXPLAIN
- 4 Validation-Op: PRAGMA integrity_check, quick_check, ANALYZE, EXPLAIN
- 449 rules total
