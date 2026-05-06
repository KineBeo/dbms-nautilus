# Grammar V3 (Structural Primitives) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace PoC-contaminated sqlite_patterns.py with decomposed structural grammar (Schema-Setup × Stress-Query × Validation-Op) that maximizes Splice mutation surface.

**Architecture:** New grammar sqlite_v3.py reuses all Layer 1 rules (expressions, functions, DDL, DML, terminals) from current grammar. Replaces Layer 2 (Pattern-* templates, stress templates) with 4 top-level Sql-Stmt shapes dispatching to Schema-Setup (6 alts), Stress-Query (8 alts), and Validation-Op (4 alts). Old grammars move to grammars/legacy/.

**Tech Stack:** Python grammar DSL (ctx.rule/ctx.regex), Nautilus fuzzer (Rust), run_eval.sh for campaigns, analyze_attribution.py for comparison.

**Spec:** `docs/superpowers/specs/2026-04-27-grammar-v3-structural-primitives-design.md`

---

### Task 1: Move current grammars to legacy/

**Files:**
- Create: `grammars/legacy/` (directory)
- Move: `grammars/sqlite_patterns.py` → `grammars/legacy/sqlite_patterns.py`
- Move: `grammars/sqlite_attack.py` → `grammars/legacy/sqlite_attack.py`
- Move: `grammars/sqlite_patterns_uniform.py` → `grammars/legacy/sqlite_patterns_uniform.py`

- [ ] **Step 1: Create legacy directory and move files**

```bash
mkdir -p grammars/legacy
git mv grammars/sqlite_patterns.py grammars/legacy/sqlite_patterns.py
git mv grammars/sqlite_attack.py grammars/legacy/sqlite_attack.py
git mv grammars/sqlite_patterns_uniform.py grammars/legacy/sqlite_patterns_uniform.py
```

- [ ] **Step 2: Update script references**

In `scripts/deep_test.sh` line 15, change:
```bash
# old
GRAMMAR="$ROOT/grammars/sqlite_patterns.py"
# new
GRAMMAR="$ROOT/grammars/sqlite_v3.py"
```

In `scripts/smoke_test.sh` line 16, change:
```bash
# old
GRAMMAR="$ROOT/grammars/sqlite_patterns.py"
# new
GRAMMAR="$ROOT/grammars/sqlite_v3.py"
```

In `scripts/run_ablation.sh` lines 45-46, change:
```bash
# old
[patterns]="$ROOT/grammars/sqlite_patterns.py"
[uniform]="$ROOT/grammars/sqlite_patterns_uniform.py"
# new
[patterns]="$ROOT/grammars/legacy/sqlite_patterns.py"
[uniform]="$ROOT/grammars/legacy/sqlite_patterns_uniform.py"
```

- [ ] **Step 3: Verify old grammars still load from legacy/**

```bash
cargo run --bin generator -- -g grammars/legacy/sqlite_patterns.py -t 5
```

Expected: 5 SQL outputs printed, no errors.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: move sqlite grammars to grammars/legacy/"
```

---

### Task 2: Create sqlite_v3.py — Layer 1 (reused base grammar)

**Files:**
- Create: `grammars/sqlite_v3.py`

This task creates the file with the START rules and all Layer 1 content copied from the current grammar. Layer 1 includes: Select-Stmt, Expr (60+ alts), Func-Call (40+ functions), Join-Clause, With-Clause, Window-Defn, Col-Def, Insert-Stmt, Update-Stmt, Delete-Stmt, DDL statements, all terminals, literals, identifiers.

- [ ] **Step 1: Create sqlite_v3.py with header and START rules**

Write the file header and the 4 top-level Sql-Stmt shapes:

```python
# sqlite_v3.py — Structural Primitives grammar for Nautilus SQLite fuzzing
# Use with: sqlite_harness_patterns_<version> (blank DB)
#
# DESIGN: Variant 3 — decomposes DDL+DQL into separate non-terminals
# (Schema-Setup, Stress-Query, Validation-Op) to maximize Splice mutation
# surface. Zero PoC contamination. All CVEs reachable through composition.
#
# Phase 2 RL interface:
#   ctx.set_weight(rule_id, new_weight)   — RL action
#   ctx.get_weights_for_nt(nt_id)         — RL state observation

# ============================================================
# START
# ============================================================
ctx.rule("START", "{Sql-Stmt-List}")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};")
ctx.rule("Sql-Stmt-List", "{Sql-Stmt};\n{Sql-Stmt-List}")

# ============================================================
# SQL-STMT DISPATCH (4 top-level shapes)
# ============================================================
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Stress-Query}", weight=3.0)
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}", weight=2.5)
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Validation-Op}", weight=2.0)
ctx.rule("Sql-Stmt", "SELECT {Boundary-Func-Call}", weight=2.0)
```

- [ ] **Step 2: Copy all Layer 1 rules from legacy/sqlite_patterns.py**

Copy these sections verbatim from `grammars/legacy/sqlite_patterns.py`:
- Lines 70-87: Select-Stmt, Select-Core (keep all 10 alternatives)
- Lines 89-92: Compound-Op
- Lines 94-127: Result-Col, From-Clause, Join-Clause, Join-Operator, Join-Constraint, Table-Or-Subquery
- Lines 130-243: Expr (all 60+ alternatives)
- Lines 245-246: Expr-List
- Lines 249-293: Over-Clause, Window-Defn, Ordering-Term, Asc-Desc, Frame-Spec, Filter-Clause, Window-Clause
- Lines 296-308: With-Clause, Cte-List, Cte-Def
- Lines 310-311: Col-Name-List
- Lines 316-342: Insert-Stmt, Update-Stmt, Delete-Stmt
- Lines 347-417: Create-Table-Stmt, Col-Def-List, Col-Def, Type-Name, Gen-Storage, Create-Index-Stmt, Create-View-Stmt, Create-Virtual-Table-Stmt, Create-Trigger-Stmt, Alter-Table-Stmt, Drop-Stmt
- Lines 422-463: Pragma-Stmt, Journal-Mode, Wal-Mode, Pragma-Bool, Sync-Mode, Attach-Stmt, Analyze-Stmt, Vacuum-Stmt, Reindex-Stmt, Savepoint-Stmt
- Lines 465-473: Where-Clause, Group-By-Clause, Order-By-Clause, Limit-Clause
- Lines 478-516: Literal, Int-Literal, Float-Literal, Str-Literal, Blob-Literal, Signed-Number, Table-Name, Col-Name, Col-Ref
- Lines 521-560: Func-Call (all 40+ functions)
- Lines 820-841: Boundary-Int, Boundary-Float
- Lines 929-935: GenCol-Expr

Do NOT copy:
- Lines 37-65: Old Sql-Stmt dispatch (replaced by our 4 shapes)
- Lines 567-632: Deep-Expr, Deep-Nested-Select, Long-Join-Chain (deleted)
- Lines 660-692: Window-Func-Complex, Win-Func-Expr, Win-Partition, etc. (deleted)
- Lines 694-775: Pattern-Boundary-Func, Json-Deep, Json-Obj, Json-Path (restructured in Task 3)
- Lines 778-813: Aggregate-Complex, Explain-Stress (deleted)
- Lines 844-1009: All Pattern-* templates (deleted)

- [ ] **Step 3: Adjust Table-Name weights**

Change Table-Name weights to favor p/q (used in Schema-Setup) over t1/t2/t3 (blank DB):

```python
ctx.rule("Table-Name", "t1", weight=0.3)
ctx.rule("Table-Name", "t2", weight=0.3)
ctx.rule("Table-Name", "t3", weight=0.3)
ctx.rule("Table-Name", "p", weight=2.0)
ctx.rule("Table-Name", "q", weight=1.5)
ctx.rule("Table-Name", "r", weight=0.5)
ctx.rule("Table-Name", "s", weight=0.3)
```

- [ ] **Step 4: Verify Layer 1 loads without errors**

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 5
```

Expected: will fail because Schema-Setup, Stress-Query, Validation-Op, Boundary-Func-Call are not yet defined. The error should be about undefined non-terminals, NOT about syntax errors in Layer 1.

- [ ] **Step 5: Commit**

```bash
git add grammars/sqlite_v3.py
git commit -m "feat(grammar): sqlite_v3.py Layer 1 base — reused from patterns"
```

---

### Task 3: Add Schema-Setup non-terminal (6 alternatives)

**Files:**
- Modify: `grammars/sqlite_v3.py`

- [ ] **Step 1: Add Schema-Setup rules**

Append to sqlite_v3.py after the Sql-Stmt dispatch section:

```python
# ============================================================
# SCHEMA-SETUP: DDL that establishes table structure
# Splice can swap entire Schema-Setup subtrees between corpus entries.
# ============================================================

# S1: Single table, basic columns
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List})",
    weight=1.5)

# S2: Table with generated column + constraints
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List-GenCol})",
    weight=3.0)

# S3: Two tables (enables JOINs between p and q)
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE TABLE IF NOT EXISTS q({Col-Def-List})",
    weight=2.5)

# S4: Table + VIEW
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE VIEW IF NOT EXISTS v1 AS {Select-Stmt}",
    weight=2.0)

# S5: Virtual table (FTS5/FTS3)
ctx.rule("Schema-Setup",
    "CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING {Fts-Engine}({Col-Name-List})",
    weight=2.0)

# S6: Table + INDEX
ctx.rule("Schema-Setup",
    "CREATE TABLE IF NOT EXISTS p({Col-Def-List});\n"
    "CREATE INDEX IF NOT EXISTS idx1 ON p({Col-Name})",
    weight=1.0)
```

- [ ] **Step 2: Add Col-Def-List-GenCol and Gen-Constraint**

```python
# Col-Def-List with guaranteed generated column
ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}")
ctx.rule("Col-Def-List-GenCol",
    "{Col-Name} {Type-Name}, {Col-Name} GENERATED ALWAYS AS ({GenCol-Expr}) {Gen-Constraint}, {Col-Def}")

ctx.rule("Gen-Constraint", "UNIQUE", weight=2.0)
ctx.rule("Gen-Constraint", "NOT NULL", weight=2.0)
ctx.rule("Gen-Constraint", "NOT NULL UNIQUE", weight=1.5)
ctx.rule("Gen-Constraint", "", weight=1.0)
```

- [ ] **Step 3: Add Fts-Engine**

```python
ctx.rule("Fts-Engine", "fts5", weight=2.0)
ctx.rule("Fts-Engine", "fts3", weight=1.0)
```

- [ ] **Step 4: Commit**

```bash
git add grammars/sqlite_v3.py
git commit -m "feat(grammar): add Schema-Setup non-terminal (6 alternatives)"
```

---

### Task 4: Add Stress-Query non-terminal (8 alternatives)

**Files:**
- Modify: `grammars/sqlite_v3.py`

- [ ] **Step 1: Add Stress-Query rules**

Append to sqlite_v3.py:

```python
# ============================================================
# STRESS-QUERY: Optimizer-stressing DQL patterns
# Each alternative creates a distinct tree shape that Splice can
# recombine with any Schema-Setup.
# ============================================================

# Q1: Base SELECT (full compositional freedom)
ctx.rule("Stress-Query", "{Select-Stmt}", weight=2.0)

# Q2: EXISTS subquery (77-100% of top crash rules in attribution)
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "WHERE EXISTS ({Select-Stmt})",
    weight=3.0)

# Q3: NATURAL JOIN (48-81% of top crash rules)
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "NATURAL JOIN {Table-Name} WHERE {Expr}",
    weight=3.0)

# Q4: Recursive CTE
ctx.rule("Stress-Query",
    "WITH RECURSIVE {Cte-Def} "
    "SELECT {Result-Col-List} FROM {Table-Name}",
    weight=2.5)

# Q5: Compound query (INTERSECT/EXCEPT)
ctx.rule("Stress-Query",
    "{Select-Stmt} {Compound-Op} {Select-Stmt}",
    weight=2.5)

# Q6: Self-JOIN + expression (80% of R25 crashes)
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM {Table-Name} "
    "JOIN {Table-Name} {Col-Alias} ON {Expr}",
    weight=2.0)

# Q7: Nested subquery chain
ctx.rule("Stress-Query",
    "SELECT {Result-Col-List} FROM "
    "(SELECT {Result-Col-List} FROM {Table-Name} WHERE {Expr}) AS sub1",
    weight=1.5)

# Q8: EXPLAIN QUERY PLAN wrapper
ctx.rule("Stress-Query",
    "EXPLAIN QUERY PLAN {Select-Stmt}",
    weight=1.5)
```

- [ ] **Step 2: Commit**

```bash
git add grammars/sqlite_v3.py
git commit -m "feat(grammar): add Stress-Query non-terminal (8 alternatives)"
```

---

### Task 5: Add Validation-Op and Boundary-Func-Call

**Files:**
- Modify: `grammars/sqlite_v3.py`

- [ ] **Step 1: Add Validation-Op rules**

```python
# ============================================================
# VALIDATION-OP: Post-schema checks (PRAGMA, ANALYZE, EXPLAIN)
# ============================================================

ctx.rule("Validation-Op", "PRAGMA integrity_check", weight=3.0)
ctx.rule("Validation-Op", "PRAGMA quick_check", weight=2.0)
ctx.rule("Validation-Op", "ANALYZE {Table-Name}", weight=1.5)
ctx.rule("Validation-Op", "EXPLAIN QUERY PLAN {Select-Stmt}", weight=1.5)
```

- [ ] **Step 2: Add Boundary-Func-Call rules**

Copy from legacy grammar (lines 694-841), keeping only the Boundary-Func-Call, Format-Spec, Printf-Fmt-Spec non-terminals. Boundary-Int and Boundary-Float are already in Layer 1.

```python
# ============================================================
# BOUNDARY-FUNC-CALL: Standalone boundary-value function calls
# Targets CVE-2020-13434 class (integer overflow in printf precision)
# ============================================================

ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int}, {Boundary-Float})", weight=3.0)
ctx.rule("Boundary-Func-Call",
    "printf({Format-Spec}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "printf({Printf-Fmt-Spec}, {Boundary-Int}, {Str-Literal})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int})", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "substr({Str-Literal}, {Boundary-Int}, {Boundary-Int})", weight=1.5)
ctx.rule("Boundary-Func-Call",
    "hex(zeroblob({Boundary-Int}))", weight=2.0)
ctx.rule("Boundary-Func-Call",
    "round({Boundary-Float}, {Boundary-Int})", weight=1.5)

ctx.rule("Format-Spec", "'%.*g'", weight=3.0)
ctx.rule("Format-Spec", "'%.*f'", weight=2.0)
ctx.rule("Format-Spec", "'%.*e'", weight=2.0)
ctx.rule("Format-Spec", "'%.*d'", weight=1.0)
ctx.rule("Format-Spec", "'%.*s'", weight=1.0)

ctx.rule("Printf-Fmt-Spec", "'%d'", weight=2.0)
ctx.rule("Printf-Fmt-Spec", "'%u'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%x'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%f'", weight=1.0)
ctx.rule("Printf-Fmt-Spec", "'%s'", weight=2.0)
```

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_v3.py
git commit -m "feat(grammar): add Validation-Op and Boundary-Func-Call"
```

---

### Task 6: Smoke test the new grammar

**Files:**
- None created/modified (testing only)

- [ ] **Step 1: Generate test inputs**

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 50
```

Expected: 50 SQL outputs. Each should start with one of:
- `CREATE TABLE ...` (shapes 1, 2, 3)
- `SELECT printf(...)` or `SELECT substr(...)` (shape 4)

No panics, no "Broken Grammar" errors.

- [ ] **Step 2: Verify variety — all 4 shapes present**

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 200 2>/dev/null | \
  grep -c "^CREATE TABLE\|^CREATE VIRTUAL"
```

Expected: roughly 150-170 of 200 should start with CREATE (shapes 1-3). The rest should be SELECT boundary funcs (shape 4).

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 200 2>/dev/null | \
  grep -c "PRAGMA\|ANALYZE"
```

Expected: some lines contain PRAGMA or ANALYZE (shape 3).

- [ ] **Step 3: Verify Schema-Setup variety**

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 200 2>/dev/null | \
  grep -c "GENERATED ALWAYS"
```

Expected: some outputs contain generated columns (Schema-Setup S2).

```bash
cargo run --bin generator -- -g grammars/sqlite_v3.py -t 200 2>/dev/null | \
  grep -c "CREATE VIRTUAL TABLE"
```

Expected: some outputs contain virtual tables (Schema-Setup S5).

- [ ] **Step 4: Quick 10-second fuzzing campaign**

```bash
DURATION=10 HARNESS_SUFFIX=patterns_ GRAMMAR=$(pwd)/grammars/sqlite_v3.py \
  timeout 25 ./scripts/run_eval.sh sqlite-3.31.1 v3_smoke 2>&1 | tail -10
```

Expected: campaign runs without crashes in the fuzzer itself. Some queue entries and possibly some crash files in outputs/signaled/.

- [ ] **Step 5: Verify exec.log has attribution data**

```bash
head -10 /tmp/nautilus_eval/sqlite-3.31.1_v3_smoke/exec.log
```

Expected: 4-column format `exec_count\tstrategy:event\tR{id}\tSQL`. Rule IDs should show variety (not all R0).

---

### Task 7: Run 15-minute A/B comparison

**Files:**
- None created/modified (evaluation only)

- [ ] **Step 1: Run 15-min campaign with new grammar**

```bash
DURATION=900 HARNESS_SUFFIX=patterns_ \
  GRAMMAR=$(pwd)/grammars/sqlite_v3.py \
  timeout 930 ./scripts/run_eval.sh sqlite-3.31.1 v3_baseline_15m
```

- [ ] **Step 2: Run attribution analysis**

```bash
python3 scripts/analyze_attribution.py \
  /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
  --grammar grammars/sqlite_v3.py
```

- [ ] **Step 3: Compare against current grammar baseline**

The baseline (from docs/attribution_baseline_15m.txt):
- 5,374 log entries
- 329 saved crash files
- 1,423 queue entries
- 83,092 total executions

Compare:
- Total unique crashes (success: >= 80% of 329 = 263)
- Coverage paths found
- Per-rule distribution (no Sql-Stmt alternative with zero activity)
- Crash diversity (unique root causes via triage/dedup.py)

- [ ] **Step 4: Save comparison report**

```bash
cp /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m/attribution_report.txt \
   docs/attribution_v3_15m.txt
```

- [ ] **Step 5: Commit evaluation results**

```bash
git add -f docs/attribution_v3_15m.txt
git commit -m "docs(eval): grammar V3 15-min attribution baseline"
```

Note: if docs/ is gitignored, save to a non-ignored location or use `git add -f`.
