# Chapter 3 Source-of-Truth Spec

**Date:** 2026-05-17
**Purpose:** Verified markdown spec for rewriting c3_method.tex. Every claim cross-checked against codebase via GitNexus + direct code reading.
**Grammar version:** v3.3 (514 rules) — single stable version presented in thesis.

---

## Remain Work / Pending Checks

- [ ] **State machine (Init → Det → Random):** Verify whether this is original Nautilus or our customization. Do NOT present as Nautilus-standard until confirmed. Check original Nautilus paper/repo for comparison.
- [ ] Cross-check CVE-to-structural-pattern table (Table 3.4) against actual crash triggers in `results/crashes/`
- [ ] Verify figure `fig_3_1_architecture.pdf` matches the 5-subsystem grouping below
- [ ] **Update figure `fig_3_2_grammar_layers.pdf`:** Boundary-Func-Call box shows "3 rules" → should be "7 rules w 1.5-3.0"

---

## Section 3.0 — Chapter Introduction

### MUST CONTAIN
- Problem: byte-level fuzzers produce parser-rejected inputs for structured languages like SQL
- Solution: grammar-based greybox fuzzing (Nautilus engine) + domain-specific SQL grammar targeting vulnerability-triggering code paths
- Contribution framing: the grammar design methodology is the contribution, not the fuzzing engine
- System name: DBMS-Nautilus

### CURRENT ERRORS
- Says "v3.0 through v3.3, growing from 449 to 520 production rules" — wrong numbers and unnecessary version history

### REWRITE NOTES
- Remove version evolution narrative from intro
- State: "The grammar contains 514 production rules organized into a two-layer architecture"
- Keep the chapter roadmap (section overview) as-is

---

## Section 3.1 — System Overview

### MUST CONTAIN

**Architecture:**
- Multi-threaded: `main()` spawns N `fuzzing_thread()` instances
- Each thread owns: FuzzingState { Context, Mutator, Fuzzer (with ForkServer), Config }
- Shared across threads: GlobalSharedState { Queue, coverage bitmaps, stats }, ChunkStoreWrapper (Arc)

**Data flow (per iteration):**
1. Grammar (Python script) → loaded into Context (rules + weights)
2. `generate_random("Sql-Stmt")` → weighted rule selection → derivation tree
3. Tree → unparse to SQL bytes
4. ForkServer: write SQL to temp file → fork child → child executes against instrumented SQLite
5. Child exits → read shared memory bitmap → compare against global bitmap
6. New coverage bits? → add tree to Queue as new item
7. Queue item progresses through mutation stages

**5 functional subsystems (matches Table in thesis):**

| Subsystem | Language | Module | Role |
|-----------|----------|--------|------|
| Grammar Engine | Rust + Python | `grammartec/` | Load grammar via PyO3, weighted rule selection |
| Generation + Mutation | Rust | `grammartec/` + `fuzzer/` | Build trees, 5 mutation operators, minimize |
| Fork Server + Harness | Rust + C | `forksrv/` + `harness/` | AFL fork-server protocol, execute SQL |
| Coverage Feedback | Rust | `fuzzer/` | Track edge bitmap, manage Queue |
| Triage Pipeline | Python | `triage/` | Post-campaign crash dedup, CVE matching |

**Mutation operators (5 operators + minimize):**

| Operator | Function | Description |
|----------|----------|-------------|
| Deterministic substitution | `mut_rules` | Try every alternative rule at each tree node |
| Random subtree | `mut_random` | Pick random node, regenerate subtree from grammar |
| Random recursion | `mut_random_recursion` | Expand or collapse recursive productions |
| Splice | `mut_splice` | Replace random node with ChunkStore subtree of same non-terminal |
| Havoc (random in bulk) | `mut_random` ×100 | 100 iterations of random subtree replacement |

**Minimize (separate from mutation):**
- `minimize` + `minimize_rec`: shrink tree while preserving coverage bits
- Purpose: reduce input to minimal triggering form before entering deterministic stage
- After minimization: tree added to ChunkStore for splice material

**State machine: [PENDING VERIFICATION]**
- Init → Det → Random progression
- NOTE: May be our customization, not original Nautilus. Verify before presenting as standard.

**Weighted sampling (CORRECT description):**
- Each production rule carries a numeric weight (set in grammar Python script)
- At selection time: sum applicable rule weights → generate random threshold → linear scan until threshold ≤ 0
- Implementation: `context.rs:314-336` — proportional weighted random, O(n) where n = rules for that non-terminal
- NOT O(1) loaded_dice. `LoadedDiceSampler` exists only in `recursion_info.rs` for recursion depth bias (separate mechanism)
- API: `ctx.rule("NT", "pattern", weight=W)` from Python → `add_rule_weighted(nt, format, weight)` in Rust

**Fork Server + Harness:**
- AFL fork-server protocol: `__AFL_INIT()` only (no `__AFL_LOOP` — one execution per fork)
- Harness opens empty in-memory SQLite database before `__AFL_INIT()`
- Each child: reads SQL from temp file → `sqlite3_exec()` → exits
- Exit code interpretation:
  - 223 = ASan crash (memory safety violation)
  - 1 = UBSan (undefined behavior)
  - Signal = crash (SIGTRAP from debug asserts, SIGSEGV, etc.)
  - Normal (any other code) = check bitmap for new coverage
- Shared memory bitmap (65536 bytes default) for edge coverage tracking

**Self-contained test cases:**
- Every generated SQL starts from empty database
- Structure: Schema-Setup → Data-Insert → Stress-Query/Validation-Op
- Contrast with SQLsmith (needs pre-populated DB) and Squirrel (internal schema model)

### CURRENT ERRORS IN THESIS
1. Line 23: "weighted sampling via the loaded dice algorithm" → WRONG. Linear scan, not loaded_dice.
2. Line 26 (fig caption): "four mutation operators" → WRONG. 5 operators.
3. Line 26: "replacing a subtree, expanding or collapsing recursive productions, or splicing subtrees between two trees" → INCOMPLETE. Missing mut_rules (deterministic) and havoc (bulk random).

### REWRITE NOTES
- Weighted sampling: say "weighted random selection proportional to rule weights" — do not name an algorithm
- Mutation: list all 5 explicitly with a table
- Minimize: describe as a separate tree-reduction step, not a mutation operator

---

## Section 3.1.1 — Positioning Among DBMS Fuzzers

### MUST CONTAIN
- Comparison table: SQLsmith vs Squirrel vs DBMS-Nautilus
- Dimensions: generation method, schema handling, mutation, coverage, targeting, isolation
- Key distinction: DBMS-Nautilus embeds targeting bias in grammar weights

### CURRENT STATUS
- Largely correct — comparative claims don't depend on internal code details
- No code-verified errors found

### REWRITE NOTES
- Minor: ensure "weighted production rules" phrasing doesn't imply O(1) algorithm
- Keep table as-is

---

## Section 3.2 — Grammar Design

### MUST CONTAIN
- Zero PoC contamination principle: no rule contains a complete CVE proof-of-concept
- Three design constraints: (a) no fixed PoC strings, (b) composable non-terminals for each CVE's structural prereqs, (c) sufficient combinatorial freedom for novel discoveries
- Circularity defense: CVEs = ground truth for evaluation, zero-PoC ensures non-trivial rediscovery
- Grammar stats: v3.3, 514 production rules

### CURRENT ERRORS
- Says "520 production rules" → actually 514
- Says "approximately 350 in Layer 1 and 170 in Layer 2" → WRONG. Actual: **465 Layer 1 + 49 Layer 2 = 514**

### REWRITE NOTES
- Update to 514 rules
- Layer split: ~465 rules define SQL atoms (Layer 1: expressions, clauses, functions, terminals) + ~49 rules define composed shapes (Layer 2: Schema-Setup + helpers, Stress-Query, Validation-Op, Boundary-Func-Call)
- Present as "the grammar contains 514 production rules: Layer 1 defines over 460 SQL atomic constructs, while Layer 2 composes these into approximately 50 vulnerability-targeting shapes"

---

## Section 3.2.1 — Two-Layer Architecture

### MUST CONTAIN
- Layer 1 (SQL Atoms): expressions (30+ alternatives), clauses, window functions, CTEs, DML, DDL, function calls, terminals/literals
- Layer 2 (Composed Shapes): Schema-Setup (6 alts), Stress-Query (8 alts), Validation-Op (4 alts), Boundary-Func-Call (7 alts)
- Start symbol: `Sql-Stmt` composes Layer 2 shapes via 4 top-level alternatives:
  - `{Schema-Setup};\n{Stress-Query}` (w=3.0)
  - `{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}` (w=2.5)
  - `{Schema-Setup};\n{Insert-Stmt};\n{Validation-Op}` (w=2.0)
  - `SELECT {Boundary-Func-Call}` (w=2.0)

### CURRENT ERRORS
- Thesis figure caption says Layer 2 has "required" and "optional" shapes — verify against actual Sql-Stmt rules above (Schema-Setup appears in 3/4; Boundary-Func-Call only in 1/4)

### REWRITE NOTES
- Describe the 4 Sql-Stmt alternatives explicitly — this shows exactly how layers compose
- Boundary-Func-Call has 7 alternatives (thesis shows only 3)

---

## Section 3.2.2 — Structural Pattern Categories

### Schema Topology Patterns (S1–S6) ✅ CORRECT IN THESIS

| ID | Pattern | Weight | Target |
|----|---------|--------|--------|
| S1 | Single table, basic columns | 1.5 | Base schema |
| S2 | Table with generated column + constraints | 3.0 | Generated column processor |
| S3 | Two tables (enables JOINs) | 2.5 | Join optimizer |
| S4 | Table + VIEW | 2.0 | View materializer |
| S5 | Virtual table (FTS5/FTS3) | 0.5 | FTS subsystem |
| S6 | Table + INDEX | 1.0 | Index maintenance |

Code-verified: exact match with `grammars/v3.3/sqlite_v3.py:649-680`

### Query Stress Patterns (Q1–Q8) — NEEDS CORRECTION

| ID | Pattern | Weight | Thesis says | Code says |
|----|---------|--------|-------------|-----------|
| Q1 | Base SELECT | 2.0 | ✅ | `{Select-Stmt}` |
| Q2 | EXISTS subquery | 3.0 | ✅ | `SELECT ... WHERE EXISTS (...)` |
| Q3 | NATURAL JOIN | 3.0 | ✅ | `SELECT ... NATURAL JOIN ... WHERE ...` |
| Q4 | **Recursive CTE** | 2.5 | ❌ "correlated subqueries" | `WITH RECURSIVE {Cte-Def} SELECT ...` |
| Q5 | Compound query | 2.5 | ✅ | `{Select-Stmt} {Compound-Op} {Select-Stmt}` |
| Q6 | Self-JOIN | 2.0 | ✅ | `SELECT ... JOIN ... ON ...` |
| Q7 | **Nested subquery chain** | 1.5 | ❌ "window functions with OVER" | `SELECT ... FROM (SELECT ... ) AS sub1` |
| Q8 | **EXPLAIN QUERY PLAN** | 1.5 | ❌ "aggregate GROUP BY HAVING" | `EXPLAIN QUERY PLAN {Select-Stmt}` |

Code-verified: `grammars/v3.3/sqlite_v3.py:703-748`

### Validation Operations — NEEDS CORRECTION

| Alternative | Weight | Thesis says | Code says |
|-------------|--------|-------------|-----------|
| PRAGMA integrity_check | 3.0 | ✅ | ✅ |
| PRAGMA quick_check | 2.0 | ✅ | ✅ |
| **ANALYZE {Table-Name}** | 1.5 | ❌ "foreign_key_check" | ANALYZE |
| **EXPLAIN QUERY PLAN {Select-Stmt}** | 1.5 | ❌ "REINDEX" | EXPLAIN QUERY PLAN |

Code-verified: `grammars/v3.3/sqlite_v3.py:750-755`

### Boundary Value Patterns — NEEDS EXPANSION

Thesis shows 3 alternatives. Code has **7**:

| Alternative | Weight | In thesis? |
|-------------|--------|-----------|
| `printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})` | 3.0 | ✅ |
| `printf({Format-Spec}, {Boundary-Int})` | 2.0 | ❌ |
| `printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})` | 1.5 | ❌ |
| `substr({Str-Literal}, {Boundary-Int})` | 2.0 | ✅ (partial) |
| `substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})` | 1.5 | ❌ |
| `hex(zeroblob({Boundary-Int}))` | 2.0 | ✅ |
| `round({Boundary-Float}, {Boundary-Int})` | 1.5 | ❌ |

Format-Spec non-terminal: `%.*g` (w=3.0), `%.*f` (w=2.0), `%.*e` (w=2.0), `%.*d` (w=1.0), `%.*s` (w=1.0)
Printf-Fmt-Spec: `%d`, `%u`, `%x`, `%f`, `%s`, `%lld` (w=3.0), `%lli` (w=2.0)

Code-verified: `grammars/v3.3/sqlite_v3.py:758-787`

### REWRITE NOTES
- Fix Q4, Q7, Q8 descriptions completely
- Fix Validation-Op alternatives (ANALYZE, EXPLAIN QUERY PLAN)
- Expand Boundary-Func-Call to show all 7 (or select representative subset with note "7 alternatives total")
- Update the paragraph explaining WHY each pattern category targets specific subsystems — ensure Q4 (Recursive CTE) and Q7 (nested subquery) rationale is correct for the ACTUAL patterns

---

## Section 3.2.3 — Cross-Pollination

### MUST CONTAIN
- Independence of Layer 2 selections → Cartesian product of compositions
- CVE-to-structural-pattern mapping table
- Key property: no pattern unique to single CVE, every CVE needs 2-5 patterns
- Consequence: improving one pattern benefits multiple CVEs

### CURRENT STATUS
- Conceptually correct
- Table values need verification against actual crash evidence in `results/crashes/`

### PENDING CHECK
- [ ] Verify CVE-2020-9327 structural requirements (thesis says: gen col + coalesce + JOIN + CREATE VIEW)
- [ ] Verify CVE-2020-13435 requirements (thesis says: NATURAL JOIN + coalesce + window OVER + UNIQUE + IN subquery) — but Q7 is NOT window functions! Does 13435 actually need window funcs from elsewhere in grammar?
- [ ] Verify CVE-2020-13871 requirements (thesis says: EXCEPT + multi-col ORDER BY + scalar subquery)
- [ ] Verify CVE-2020-15358 requirements (thesis says: VIEW + ORDER BY + INTERSECT + implicit JOIN)

---

## Section 3.2.4 — Grammar Analysis and Limitations

### MUST CONTAIN
- Contribution = methodological (grammar design approach), not algorithmic (engine is Nautilus)
- Cross-pollination as multiplicative benefit
- Modularity: new Layer 1 atom → available to all Layer 2 shapes; new Layer 2 shape → composes with all Layer 1 atoms
- Comparison with automated grammar inference (Skyfire, IFuzzer) — manual trades scalability for targeting precision

**Limitations (3):**
1. Requires manual domain expertise (CVE root-cause analysis → SQL structural patterns)
2. Weight sensitivity (bad weights → shallow exploration; needs empirical tuning)
3. Reachability ceiling (grammar defines hard boundary; coverage feedback navigates within it, cannot expand)

### CURRENT STATUS
- Content largely correct
- Any mention of "loaded dice" algorithm must be removed

### REWRITE NOTES
- Remove or correct any reference to loaded_dice / O(1) sampling
- Keep limitations section as-is (well-written, honest)

---

## Summary of ALL Errors to Fix

| Location | Error | Fix |
|----------|-------|-----|
| Intro | "449 to 520 rules" | "514 production rules" (v3.3 only) |
| 3.1 §Grammar Engine | "loaded dice algorithm" | "weighted random selection proportional to rule weights" |
| 3.1 §Gen+Mutation | "four mutation operators" | 5 operators + minimize separate |
| 3.1 fig caption | "four mutation operators" | 5 operators |
| 3.2.2 Q4 | "correlated subqueries" | "Recursive CTE" |
| 3.2.2 Q7 | "window functions with OVER" | "Nested subquery chain" |
| 3.2.2 Q8 | "aggregate GROUP BY HAVING" | "EXPLAIN QUERY PLAN" |
| 3.2.2 Validation-Op | "foreign_key_check, REINDEX" | "ANALYZE, EXPLAIN QUERY PLAN" |
| 3.2.2 Boundary-Func-Call | Shows 3 alternatives | Actually 7 alternatives |
| 3.2 | "520 production rules" | 514 |
| 3.2 | "approximately 350 Layer 1, 170 Layer 2" | Actually 465 Layer 1 + 49 Layer 2 |
