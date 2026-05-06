# Grammar V3: Structural Primitives Design

**Date:** 2026-04-27
**Status:** Draft
**Target:** Replace PoC-contaminated sqlite_patterns.py with decomposed structural grammar

---

## Problem

The current grammar (sqlite_patterns.py, 1010 lines, 26 Sql-Stmt alternatives) has three problems:

1. **PoC contamination** — Pattern-DDL-DQL templates contain near-literal CVE PoC strings (exact variable names, exact query shapes from CVE-2020-9327, CVE-2020-13871, CVE-2020-13435). These replay known bugs, not discover them.
2. **34.5% wasted weight** — 10 rules (Select-Stmt, Insert-Stmt, Update-Stmt, Delete-Stmt, Create-Index, Create-Trigger, Alter-Table, Deep-Nested-Select, Long-Join-Chain, Window-Func-Complex) consuming 11.0/31.9 total weight produce zero crashes.
3. **Monolithic templates block mutation** — Pattern-DDL-DQL fuses DDL+DQL into single tree nodes with only 2 mutable sub-expressions. Splice cannot recombine DDL from one corpus entry with DQL from another.

## Constraints

1. Grammar MUST be able to reproduce all 6 target CVEs through composition (provably reachable).
2. Grammar MUST NOT hardcode PoC strings, CVE-specific variable names, or exact CVE query structures.
3. Grammar follows the structural-pattern mindset: CVE = evidence of a vulnerable production rule pattern, not an input to replay.

## Decision: Variant 3 (Structural Primitives)

Selected over two alternatives after expert panel debate:

- **Variant 1 (Seed Templates)** — Rejected. Shallow tree depth (2 mutable points per template). Splice surface too small. RL action space too coarse (8 fused templates).
- **Variant 2 (Pure Compositional)** — Rejected. No DDL-before-DQL guarantee on blank DB. ~50% of multi-statement inputs semantically invalid. Wastes execution cycles.
- **Variant 3 (Structural Primitives)** — Selected. Decomposes DDL+DQL into separate non-terminals (Schema-Setup, Stress-Query, Validation-Op). Each boundary is a Splice point. 10+ mutable positions per input vs 2 in current grammar.

## Architecture

### Top-Level Structure

```
START → Sql-Stmt-List
Sql-Stmt-List → Sql-Stmt ;
Sql-Stmt-List → Sql-Stmt ; Sql-Stmt-List
```

### Sql-Stmt Dispatch (4 shapes)

| # | Shape | Weight | Purpose |
|---|-------|--------|---------|
| 1 | `{Schema-Setup}; {Stress-Query}` | 3.0 | DDL → complex DQL |
| 2 | `{Schema-Setup}; {Insert-Stmt}; {Stress-Query}` | 2.5 | DDL → data → complex DQL |
| 3 | `{Schema-Setup}; {Validation-Op}` | 2.0 | DDL → PRAGMA/ANALYZE |
| 4 | `SELECT {Boundary-Func-Call}` | 2.0 | Standalone boundary functions |

### Schema-Setup (6 alternatives)

| # | Alternative | Weight | CVE coverage |
|---|------------|--------|-------------|
| 1 | Single table, basic columns: `CREATE TABLE IF NOT EXISTS p({Col-Def-List})` | 1.5 | Base DDL |
| 2 | Table with generated column: `CREATE TABLE IF NOT EXISTS p({Col-Def-List-GenCol})` | 3.0 | CVE-2020-9327, CVE-2019-19646 |
| 3 | Two tables: `CREATE TABLE IF NOT EXISTS p({Col-Def-List}); CREATE TABLE IF NOT EXISTS q({Col-Def-List})` | 2.5 | CVE-2020-15358 |
| 4 | Table + VIEW: `CREATE TABLE IF NOT EXISTS p({Col-Def-List}); CREATE VIEW IF NOT EXISTS v1 AS {Select-Stmt}` | 2.0 | CVE-2020-15358, CVE-2020-9327 |
| 5 | Virtual table (FTS): `CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING {Fts-Engine}({Col-Name-List})` | 2.0 | FTS crash surface |
| 6 | Table + INDEX: `CREATE TABLE IF NOT EXISTS p({Col-Def-List}); CREATE INDEX IF NOT EXISTS idx1 ON p({Col-Name})` | 1.0 | Index optimization path |

New sub-non-terminal `Col-Def-List-GenCol` guarantees at least one generated column:

```
Col-Def-List-GenCol:
  → {Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}
  → {Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}, {Col-Def}

Gen-Constraint:
  → UNIQUE
  → NOT NULL
  → NOT NULL UNIQUE
  → (empty)
```

### Stress-Query (8 alternatives)

| # | Alternative | Weight | Attribution evidence |
|---|------------|--------|---------------------|
| 1 | Base: `{Select-Stmt}` | 2.0 | Full compositional freedom |
| 2 | EXISTS: `SELECT {Result-Col-List} FROM {Table-Name} WHERE EXISTS ({Select-Stmt})` | 3.0 | 77-100% of top crash rules |
| 3 | NATURAL JOIN: `SELECT {Result-Col-List} FROM {Table-Name} NATURAL JOIN {Table-Name} WHERE {Expr}` | 3.0 | 48-81% of top crash rules |
| 4 | Recursive CTE: `WITH RECURSIVE {Cte-Def} SELECT {Result-Col-List} FROM {Table-Name}` | 2.5 | R19: 275 crashes |
| 5 | Compound: `{Select-Stmt} {Compound-Op} {Select-Stmt}` | 2.5 | R27: CVE-2020-13871, CVE-2020-15358 |
| 6 | Self-JOIN: `SELECT {Result-Col-List} FROM {Table-Name} JOIN {Table-Name} {Col-Alias} ON {Expr}` | 2.0 | 80% of R25 crashes |
| 7 | Nested subquery: `SELECT {Result-Col-List} FROM (SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr}) AS sub1` | 1.5 | Subquery chains |
| 8 | EXPLAIN: `EXPLAIN QUERY PLAN {Select-Stmt}` | 1.5 | R23: 221 crashes |

### Validation-Op (4 alternatives)

| # | Alternative | Weight |
|---|------------|--------|
| 1 | `PRAGMA integrity_check` | 3.0 |
| 2 | `PRAGMA quick_check` | 2.0 |
| 3 | `ANALYZE {Table-Name}` | 1.5 |
| 4 | `EXPLAIN QUERY PLAN {Select-Stmt}` | 1.5 |

### Boundary-Func-Call

Unchanged from current grammar. Printf + zeroblob + round + substr with Boundary-Int (INT32_MAX, INT64_MAX, etc.) and Boundary-Float.

### Layer 1 (Unchanged)

The entire Layer 1 grammar carries over without modification:
- Select-Stmt, Select-Core (10 alternatives)
- Expr (60+ alternatives including all operators, CASE, CAST, IN, EXISTS, LIKE, etc.)
- Func-Call (40+ SQLite functions including json_*)
- Join-Clause, Join-Operator (8 join types), Join-Constraint
- With-Clause, Cte-Def (5 CTE forms)
- Window-Defn, Frame-Spec, Over-Clause, Filter-Clause
- Col-Def, Col-Def-List, Type-Name (10 types)
- Insert-Stmt (14 forms), Update-Stmt (7 forms), Delete-Stmt (4 forms)
- All DDL: Create-Table-Stmt, Create-View-Stmt, Create-Virtual-Table-Stmt, etc.
- All terminals: Table-Name, Col-Name, Col-Ref, Literal, Int-Literal, Str-Literal, etc.
- GenCol-Expr, Gen-Storage, Compound-Op
- Pragma-Stmt alternatives, Analyze-Stmt, Attach-Stmt
- Boundary-Int (11 values), Boundary-Float (8 values), Format-Spec

## What's Deleted

| Component | Lines | Reason |
|-----------|-------|--------|
| Pattern-DDL-DQL (7 templates) | 853-897 | PoC contaminated, blocks Splice |
| Pattern-GenCol-Op (5 templates) | 903-927 | Replaced by Schema-Setup #2 |
| Pattern-Compound (4 templates) | 940-968 | Replaced by Stress-Query #5 |
| Pattern-Schema-Pragma (4 templates) | 977-995 | Replaced by Validation-Op |
| Window-Func-Complex (2 templates) | 660-668 | Zero crashes, standalone |
| Deep-Nested-Select (4 templates) | 590-605 | Zero crashes, standalone |
| Long-Join-Chain (5 templates) | 608-632 | Zero crashes, standalone |
| Win-Func-Expr, Win-Partition, Win-Order, Win-Frame | 670-692 | Layer 2 duplicates |
| Deep-Expr, Deep-Expr-L2, Bin-Op | 567-588 | Unused forced-depth |
| Window-Agg-Expr | 1000-1009 | Only used by deleted patterns |
| Aggregate-Complex (7 templates) | 778-807 | Over-weighted (2.0), 0.2x efficiency |
| Explain-Stress (4 templates) | 810-813 | Replaced by Stress-Query #8 + Validation-Op #4 |
| Agg-Func | 801-807 | Only used by deleted Aggregate-Complex |

## What Moves to Legacy

```
grammars/sqlite_patterns.py    → grammars/legacy/sqlite_patterns.py
grammars/sqlite_attack.py      → grammars/legacy/sqlite_attack.py
grammars/sqlite_patterns_uniform.py → grammars/legacy/sqlite_patterns_uniform.py
```

## New File

`grammars/sqlite_v3.py` — estimated ~500 lines (Layer 1 ~450 + new Layer 2 ~50).

## CVE Reachability Proof

| CVE | Path through grammar |
|-----|---------------------|
| CVE-2020-9327 | Sql-Stmt shape 1 → Schema-Setup #2 (genCol + UNIQUE) + Schema-Setup #3 (second table) → Stress-Query #3 (NATURAL JOIN) or #6 (self-JOIN) with coalesce in Expr |
| CVE-2020-13434 | Sql-Stmt shape 4 → Boundary-Func-Call → printf('%.*f', 2147483647, 0.01) |
| CVE-2020-13435 | Sql-Stmt shape 1 → Schema-Setup #1 (table with UNIQUE) → Stress-Query #6 (self-JOIN) with window functions in Expr (lead, SUM via Func-Call + Over-Clause) |
| CVE-2020-13871 | Sql-Stmt shape 1 → Schema-Setup #1 → Stress-Query #5 (Compound: EXCEPT) with GROUP BY + HAVING + window in Select-Stmt |
| CVE-2020-15358 | Sql-Stmt shape 1 → Schema-Setup #4 (table + VIEW) + Schema-Setup #3 (two tables) → Stress-Query #5 (INTERSECT) or #3 (NATURAL JOIN) |
| CVE-2019-19646 | Sql-Stmt shape 3 → Schema-Setup #2 (genCol + NOT NULL) → INSERT → Validation-Op #1 (PRAGMA integrity_check) |

## Mutation Surface Comparison

| Metric | Current (sqlite_patterns.py) | New (sqlite_v3.py) |
|--------|-------|-----|
| Splice points per Pattern input | 2 | 10+ |
| Sql-Stmt alternatives | 26 (fused) | 4 (decomposed) |
| Schema × Query combinations from Gen | 7 fixed | 6 × 8 = 48 |
| Schema × Query combinations via Splice | ~7 | hundreds (combinatorial) |
| RL action space | 26 correlated weights | Schema (6) + Query (8) independent |
| Estimated line count | 1,010 | ~500 |

## Validation Plan

1. Build: `cargo build --release` (grammar is Python, no Rust changes needed)
2. Smoke test: `cargo run --bin generator -- -g grammars/sqlite_v3.py -t 50` — verify all 4 shapes produce valid SQL
3. Attribution run: 15-min campaign with `analyze_attribution.py` — compare against baseline
4. A/B metrics: total crashes, unique crashes, TTFC, per-rule crash efficiency, coverage growth curve

## Success Criteria

- All 6 CVEs remain reachable (verify via manual grammar walk or targeted generation)
- Total unique crashes >= 80% of baseline (329 in 15 min) — some regression expected since PoC replay is removed
- Per-rule crash diversity > baseline (more unique root causes, fewer re-triggers of same path)
- No Sql-Stmt alternative with zero crashes after 15 min
