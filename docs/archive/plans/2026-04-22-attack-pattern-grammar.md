# Attack-Pattern Grammar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce `grammars/sqlite_attack.py` — a CVE-distilled attack-pattern grammar (~365 lines, 8 attack patterns) that follows the Nautilus-mruby shrink philosophy, and demonstrate via a 1-hour pilot on sqlite-3.31.1 that it matches or beats `grammars/sqlite_patterns.py` per CPU-hour.

**Architecture:** One new grammar file (`grammars/sqlite_attack.py`) plus one smoke-test script (`scripts/smoke_attack_grammar.sh`). Existing harness binaries and `scripts/run_eval.sh` are reused unchanged. No fuzzer-source changes. No RL — weights deferred to a separate spec.

**Tech Stack:** Python 3 (grammar), bash (smoke + eval wrapper), Rust Nautilus fuzzer (unchanged), existing AFL-instrumented SQLite harnesses.

**Spec:** `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`

---

## File Structure

Files created or modified by this plan:

| File | Role | Status |
|---|---|---|
| `grammars/sqlite_attack.py` | The attack-pattern grammar (§9 of spec) | **Created** — the deliverable |
| `scripts/smoke_attack_grammar.sh` | Headless smoke: load grammar + generate N samples + check parseability via `sqlite3` CLI | **Created** |
| `docs/attack-grammar-pilot-sqlite-3.31.1.md` | Pilot results report (crashes, TTFC, exec rate, CVE class hits) | **Created** at the end |

Files deliberately **not** touched:
- `fuzzer/**`, `grammartec/**`, `forksrv/**` — no fuzzer-source changes.
- `harness/**` — existing `sqlite_harness_patterns_sqlite-3.31.1` is reused; blank-DB harness is already correct for attack-pattern grammars.
- `scripts/run_eval.sh` — already parameterises grammar via `$GRAMMAR` env var; no edits needed.
- `grammars/sqlite_patterns.py`, `grammars/sqlite_patterns_uniform.py` — untouched comparison baselines.

---

## Conventions used in this plan

- **Every Nautilus grammar file** is a plain Python script evaluated with a `ctx` object exposing `ctx.rule(lhs, rhs)` and `ctx.regex(lhs, pattern)`. `ctx.rule("Foo", "{Bar} xyz {Baz}")` adds production `Foo → {Bar} xyz {Baz}`. Non-terminals are written `{Like-This}` (hyphen-separated, no space). Terminals are written as literal text.
- **`ctx.rule` with weights** is optional; omitting weight uses Nautilus-default uniform selection. Per spec §9, **this grammar ships weight-free** — do not add a `weight=` argument anywhere.
- **Project root** in commands is the repository root:
  `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2`
  All relative paths below are rooted there; `cd` to root before running any command.
- **Env prereqs** (set once per shell):
  ```bash
  export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
  export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
  export PYTHONPATH="$(pwd)"
  ```
- **Grammar regeneration sanity check**: after any edit to `grammars/sqlite_attack.py`, run `cargo run --release --bin generator -- -g grammars/sqlite_attack.py -t 5 -n 200` to confirm the grammar loads and generates samples. This catches syntax errors and broken-grammar panics fast.

---

## Task 1: Scaffold grammar file with Section 1 (START + statement list)

**Files:**
- Create: `grammars/sqlite_attack.py`

**Context:** Spec §9 section 1 — START rule + recursive statement-list. Minimum viable grammar that loads. Everything else in later tasks.

- [ ] **Step 1: Create the file with header and Section 1 only**

Write exactly this content to `grammars/sqlite_attack.py`:

```python
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
```

- [ ] **Step 2: Verify the file parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): scaffold sqlite_attack.py (section 1 START + stmt list)"
```

---

## Task 2: Section 2 — Vocabulary (literals and identifiers)

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 1)

**Context:** Spec §4.1 + §4.2. Every value has provenance in the spec. No values added that aren't in the spec tables.

- [ ] **Step 1: Append Section 2 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
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
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 2 vocabulary (literals + identifiers) to sqlite_attack"
```

---

## Task 3: Section 3 — Types and collations

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 2)

**Context:** Spec §4.3.

- [ ] **Step 1: Append Section 3 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
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
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 3 types and collations to sqlite_attack"
```

---

## Task 4: Section 4 — Canonical SQL forms

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 3)

**Context:** Spec §5 canonical-form cuts. **One** form per construct, optional-sub non-terminals for variadic clauses. No INNER/CROSS/LEFT JOIN, no UNION, no TEMP, no IF NOT EXISTS, no WITHOUT ROWID, no ATTACH/DETACH/ANALYZE/REINDEX/VACUUM.

The Sql-Stmt dispatch table is progressively populated from this section onwards — base statements here, attack patterns in §6.

- [ ] **Step 1: Append Section 4 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
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
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 4 canonical SQL forms to sqlite_attack"
```

---

## Task 5: Section 5 — Shared non-terminals (the composition substrate)

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 4)

**Context:** Spec §7 — these non-terminals are shared across attack patterns so Nautilus's splice mutator can recombine sub-expressions across patterns. **This is the step that enables "CVE A + CVE B → new crash."**

Recursion discipline per spec §7: only `Expr`, `Scalar-Subquery`, `Join-Chain`, and `Boolean-Expr` recurse — all four recurse on themselves directly, no more than one level per rule. Depth comes from Nautilus's Random Recursive Mutation, not from grammar.

- [ ] **Step 1: Append Section 5 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
# ============================================================
# SECTION 5: Shared non-terminals (§7)
# The composition substrate — patterns share these so splice mutation
# recombines sub-expressions across CVEs.
# ============================================================

# --- Expr (core, recursive, shallow — Random Recursive Mutation amplifies) ---
ctx.rule("Expr", "{Literal}")
ctx.rule("Expr", "{Col-Ref}")
ctx.rule("Expr", "({Expr})")
ctx.rule("Expr", "{Expr} {Bin-Op} {Expr}")
ctx.rule("Expr", "({Scalar-Subquery})")
ctx.rule("Expr", "{Case-Expr}")
ctx.rule("Expr", "{Builtin-Func-Call}")
ctx.rule("Expr", "{Agg-Func-Call}")
ctx.rule("Expr", "{Coalesce-Window-Expr}")

ctx.rule("Bin-Op", "+")
ctx.rule("Bin-Op", "-")
ctx.rule("Bin-Op", "*")
ctx.rule("Bin-Op", "/")

ctx.rule("Case-Expr", "CASE WHEN {Boolean-Expr} THEN {Expr} ELSE {Expr} END")

ctx.rule("Expr-List", "{Expr}")
ctx.rule("Expr-List", "{Expr}, {Expr-List}")

# --- Col-Ref (qualified and unqualified) ---
ctx.rule("Col-Ref", "{Col-Name}")
ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}")
ctx.rule("Col-Ref", "{Alias}.{Col-Name}")

# --- Boolean-Expr (recursive, flat logical combinators) ---
ctx.rule("Boolean-Expr", "{Expr} {Compare-Op} {Expr}")
ctx.rule("Boolean-Expr", "{Expr} IN ({Expr-List})")
ctx.rule("Boolean-Expr", "{Expr} IN ({Scalar-Subquery})")
ctx.rule("Boolean-Expr", "{Expr} LIKE {Str-Lit}")
ctx.rule("Boolean-Expr", "{Boolean-Expr} AND {Boolean-Expr}")
ctx.rule("Boolean-Expr", "{Boolean-Expr} OR {Boolean-Expr}")
ctx.rule("Boolean-Expr", "NOT {Boolean-Expr}")
ctx.rule("Boolean-Expr", "({Boolean-Expr})")

ctx.rule("Compare-Op", "=")
ctx.rule("Compare-Op", "<>")
ctx.rule("Compare-Op", "<")
ctx.rule("Compare-Op", ">")
ctx.rule("Compare-Op", "<=")
ctx.rule("Compare-Op", ">=")

# --- Scalar-Subquery (recursive; the shared CVE-13435/13871 substrate) ---
ctx.rule("Scalar-Subquery", "SELECT {Expr}")
ctx.rule("Scalar-Subquery", "SELECT {Expr} FROM {Table-Name}")
ctx.rule("Scalar-Subquery", "SELECT {Expr} FROM {Table-Name} WHERE {Boolean-Expr}")
ctx.rule("Scalar-Subquery", "SELECT ({Scalar-Subquery}) FROM {Table-Name}")
ctx.rule("Scalar-Subquery", "SELECT ({Scalar-Subquery}) FROM {Table-Name} WHERE {Boolean-Expr}")
ctx.rule("Scalar-Subquery", "{Scalar-Subquery} INTERSECT {Scalar-Subquery}")

# --- Join-Chain (recursive; one op per step) ---
ctx.rule("Join-Chain", "{Join-Op} {Table-Name}")
ctx.rule("Join-Chain", "{Join-Op} {Table-Name} {Alias}")
ctx.rule("Join-Chain", "{Join-Op} {Table-Name} ON {Boolean-Expr}")
ctx.rule("Join-Chain", "{Join-Chain} {Join-Op} {Table-Name}")

ctx.rule("Join-Op", "JOIN")
ctx.rule("Join-Op", "NATURAL JOIN")
ctx.rule("Join-Op", ",")

# --- Generated columns (§5 + spec §7) ---
ctx.rule("GenCol-Def", "{Col-Name} AS ({Expr})")
ctx.rule("GenCol-Def", "{Col-Name} NOT NULL GENERATED ALWAYS AS ({Expr})")
ctx.rule("GenCol-Def", "{Col-Name} AS ({Expr}) UNIQUE")

# --- View-Def (shared by P-INTERSECT-VIEW and P-GENCOL-JOIN-COALESCE) ---
ctx.rule("View-Def", "CREATE VIEW {View-Name} AS {Select-Stmt}")
ctx.rule("View-Def", "CREATE VIEW {View-Name}({Col-Name}) AS {Select-Stmt}")

# --- Window functions (§8 source) ---
ctx.rule("Window-Func-Call", "{Window-Func-Name}({Expr}) OVER ()")
ctx.rule("Window-Func-Call", "{Window-Func-Name}({Expr}) OVER ({Order-By})")
ctx.rule("Window-Func-Call", "COUNT() OVER ({Order-By})")

# --- Aggregate functions (§8 source) ---
ctx.rule("Agg-Func-Call", "{Agg-Func-Name}({Expr})")
ctx.rule("Agg-Func-Call", "{Agg-Func-Name}(DISTINCT {Expr})")
ctx.rule("Agg-Func-Call", "COUNT()")
ctx.rule("Agg-Func-Call", "group_concat({Expr}, {Int-Lit})")

# --- Coalesce-Window-Expr (the cross-CVE shared signal) ---
ctx.rule("Coalesce-Window-Expr", "coalesce({Window-Func-Call}, {Agg-Func-Call})")
ctx.rule("Coalesce-Window-Expr", "coalesce({Col-Ref}, {Window-Func-Call})")

# --- Order-By (used by CVE-13871/15358) ---
ctx.rule("Order-By", "ORDER BY {Expr}")
ctx.rule("Order-By", "ORDER BY {Expr}, {Expr}")
ctx.rule("Order-By", "ORDER BY {Expr}, {Expr}, {Expr}")

# --- Builtin-Func-Call (§8 source) ---
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr})")
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr}, {Expr})")
ctx.rule("Builtin-Func-Call", "{Builtin-Func}({Expr}, {Expr}, {Expr})")
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 5 shared non-terminals to sqlite_attack"
```

---

## Task 6: Section 6 — Attack patterns (the 8 CVE-anchored skeletons)

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 5)

**Context:** Spec §6 catalog. One pattern per row, plus a dispatch rule that exposes each pattern through `Sql-Stmt`. Patterns reference **only** shared non-terminals from Section 5 and literals from Section 2 — no ad-hoc tokens.

- [ ] **Step 1: Append Section 6 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
# ============================================================
# SECTION 6: Attack patterns (§6 catalog — 8 patterns)
# Each pattern = one CVE (or derived). Multi-statement skeletons
# that expand to shared non-terminals from §7.
# ============================================================

# Dispatch: every pattern is reachable through Sql-Stmt
ctx.rule("Sql-Stmt", "{Pattern-P15358}")
ctx.rule("Sql-Stmt", "{Pattern-P13871}")
ctx.rule("Sql-Stmt", "{Pattern-P13435}")
ctx.rule("Sql-Stmt", "{Pattern-P13434-Boundary}")
ctx.rule("Sql-Stmt", "{Pattern-P13434-Trigger}")
ctx.rule("Sql-Stmt", "{Pattern-P9327}")
ctx.rule("Sql-Stmt", "{Pattern-P19646}")
ctx.rule("Sql-Stmt", "{Pattern-Compound-Mix}")

# --- CVE-2020-15358: INTERSECT + VIEW ---
ctx.rule("Pattern-P15358",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "{View-Def};\n"
    "SELECT * FROM {Table-Name}, {Table-Name} "
    "WHERE {Col-Ref} = ({Scalar-Subquery} INTERSECT {Scalar-Subquery}) "
    "AND {Col-Ref} = {Int-Lit}")

# --- CVE-2020-13871: HAVING + window + EXCEPT ---
ctx.rule("Pattern-P13871",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT ({Scalar-Subquery}) FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")

# --- CVE-2020-13435: JOIN + NATURAL JOIN + coalesce window ---
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery}))")

# --- CVE-2020-13434 simplified PoC: SELECT-time boundary-int sink ---
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}('%.*g', {Boundary-Int}, {Real-Lit})")
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}({Boundary-Int})")
ctx.rule("Pattern-P13434-Boundary",
    "SELECT {Builtin-Func}({Str-Lit}, {Boundary-Int}, {Expr})")

# --- CVE-2020-13434 original PoC: INSERT-time sink via trigger ---
ctx.rule("Pattern-P13434-Trigger",
    "CREATE TABLE {Table-Name}({Col-Name} {Type-Name} CHECK("
    "NOT CASE WHEN {Builtin-Func}({Col-Ref}, {Col-Ref}) THEN 0 END) "
    "UNIQUE ON CONFLICT REPLACE);\n"
    "CREATE TRIGGER {Col-Name} INSERT ON {Table-Name} BEGIN "
    "INSERT INTO {Table-Name} SELECT group_concat({Col-Ref}, {Boundary-Int}) "
    "FROM {Table-Name}; END;\n"
    "INSERT INTO {Table-Name} VALUES ({Null-Lit}), ({Int-Lit}), ({Int-Lit});\n"
    "UPDATE {Table-Name} SET {Col-Name} = {Int-Lit}")

# --- CVE-2020-9327: generated col + JOIN + coalesce ---
ctx.rule("Pattern-P9327",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def});\n"
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE, {Col-Name} UNIQUE);\n"
    "{View-Def};\n"
    "SELECT * FROM {View-Name} {Join-Chain} WHERE {Boolean-Expr}")

# --- CVE-2019-19646: generated col + integrity_check ---
ctx.rule("Pattern-P19646",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def});\n"
    "INSERT INTO {Table-Name}({Col-Name}) VALUES ({Int-Lit});\n"
    "PRAGMA integrity_check")

# --- Derived: P-COMPOUND-MIX combines INTERSECT + EXCEPT usage ---
ctx.rule("Pattern-Compound-Mix",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT {Col-Ref} FROM {Table-Name} "
    "INTERSECT SELECT {Col-Ref} FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 6 attack pattern catalog to sqlite_attack"
```

---

## Task 7: Section 7 — Target-specific symbols

**Files:**
- Modify: `grammars/sqlite_attack.py` (append after Section 6)

**Context:** Spec §8 — terminals drawn from SQLite documentation for modules with CVE history. Enumerated lists only; no regex fallbacks.

- [ ] **Step 1: Append Section 7 to the grammar file**

Append to `grammars/sqlite_attack.py`:

```python
# ============================================================
# SECTION 7: Target-specific symbols (§8)
# ============================================================

ctx.rule("Builtin-Func", "printf")
ctx.rule("Builtin-Func", "format")
ctx.rule("Builtin-Func", "zeroblob")
ctx.rule("Builtin-Func", "hex")
ctx.rule("Builtin-Func", "substr")
ctx.rule("Builtin-Func", "quote")
ctx.rule("Builtin-Func", "typeof")
ctx.rule("Builtin-Func", "likelihood")
ctx.rule("Builtin-Func", "ifnull")
ctx.rule("Builtin-Func", "coalesce")
ctx.rule("Builtin-Func", "iif")
ctx.rule("Builtin-Func", "random")
ctx.rule("Builtin-Func", "randomblob")

ctx.rule("Agg-Func-Name", "sum")
ctx.rule("Agg-Func-Name", "count")
ctx.rule("Agg-Func-Name", "avg")
ctx.rule("Agg-Func-Name", "group_concat")
ctx.rule("Agg-Func-Name", "max")
ctx.rule("Agg-Func-Name", "min")
ctx.rule("Agg-Func-Name", "total")

ctx.rule("Window-Func-Name", "lead")
ctx.rule("Window-Func-Name", "lag")
ctx.rule("Window-Func-Name", "row_number")
ctx.rule("Window-Func-Name", "rank")
ctx.rule("Window-Func-Name", "dense_rank")
ctx.rule("Window-Func-Name", "first_value")
ctx.rule("Window-Func-Name", "last_value")
ctx.rule("Window-Func-Name", "nth_value")

ctx.rule("PRAGMA-Name", "integrity_check")
ctx.rule("PRAGMA-Name", "foreign_key_check")
ctx.rule("PRAGMA-Name", "writable_schema")
ctx.rule("PRAGMA-Name", "encoding")
ctx.rule("PRAGMA-Name", "journal_mode")
ctx.rule("PRAGMA-Name", "schema_version")
ctx.rule("PRAGMA-Name", "cache_size")
ctx.rule("PRAGMA-Name", "page_size")

ctx.rule("Module-Name", "fts5")
ctx.rule("Module-Name", "fts4")
ctx.rule("Module-Name", "rtree")
ctx.rule("Module-Name", "geopoly")
ctx.rule("Module-Name", "zipfile")
```

- [ ] **Step 2: Verify the file still parses as Python**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`
Expected: `ok`

- [ ] **Step 3: Count lines and confirm within budget**

Run: `wc -l grammars/sqlite_attack.py`
Expected: Line count between 300 and 440 (spec budget ~365 lines, tolerance 20%).

- [ ] **Step 4: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add section 7 target-specific symbols, complete sqlite_attack.py"
```

---

## Task 8: Nautilus generator smoke test

**Files:**
- Create: `scripts/smoke_attack_grammar.sh`

**Context:** The grammar must (a) load without `Broken Grammar` panic, (b) generate valid-looking SQL samples, (c) pass through SQLite's parser at least some non-trivial fraction of the time. This script is the pre-pilot gate — if it fails, Task 9's pilot will waste CPU-hours.

- [ ] **Step 1: Create the smoke script**

Write exactly this content to `scripts/smoke_attack_grammar.sh`:

```bash
#!/usr/bin/env bash
# smoke_attack_grammar.sh — Pre-pilot gate for grammars/sqlite_attack.py.
#
# Checks:
#   1. Grammar loads via Nautilus generator (no Broken Grammar panic).
#   2. Generates N samples without panic.
#   3. At least 30% of samples parse cleanly as SQL by sqlite3 CLI
#      (semantic errors are fine; we only check syntactic acceptability).
#   4. Every attack pattern is observed at least once in the sample set.
#
# Usage:
#   ./scripts/smoke_attack_grammar.sh
#   SAMPLES=500 ./scripts/smoke_attack_grammar.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

GRAMMAR="grammars/sqlite_attack.py"
SAMPLES="${SAMPLES:-200}"
OUT_DIR="$(mktemp -d)"
trap 'rm -rf "$OUT_DIR"' EXIT

echo "== Step 1: Build generator =="
cargo build --release --bin generator 2>&1 | tail -5

echo "== Step 2: Generate $SAMPLES samples =="
# Note: do NOT pass -s. With -s, the Nautilus generator writes one file
# per tree to ./corpus/ and emits nothing to stdout, so the redirect
# below would capture an empty file. Omitting -s makes it unparse each
# tree to stdout, which is what we want to pipe into sqlite3.
./target/release/generator -g "$GRAMMAR" -t 100 -n "$SAMPLES" \
    > "$OUT_DIR/samples.txt"

sample_count=$(grep -c . "$OUT_DIR/samples.txt" || true)
echo "Generated $sample_count non-empty lines"
if [[ "$sample_count" -lt 50 ]]; then
    echo "FAIL: generator produced <50 samples"
    exit 1
fi

echo "== Step 3: Syntactic acceptability check via sqlite3 CLI =="
pass=0
fail=0
while IFS= read -r stmt; do
    [[ -z "$stmt" ]] && continue
    # Use :memory: DB, wrap in sqlite3's EXPLAIN to check parse without execute.
    # Exit 1 = parse error; we tolerate semantic errors (no such table, etc.).
    if output=$(sqlite3 ':memory:' "EXPLAIN $stmt" 2>&1); then
        ((pass+=1)) || true
    else
        if echo "$output" | grep -qiE 'syntax error|malformed|near "'; then
            ((fail+=1)) || true
        else
            # Semantic error is OK for syntactic smoke
            ((pass+=1)) || true
        fi
    fi
done < <(head -100 "$OUT_DIR/samples.txt")

total=$((pass + fail))
if [[ "$total" -eq 0 ]]; then total=1; fi
pct=$((pass * 100 / total))
echo "Syntactic pass rate: $pass / $total ($pct%)"
if [[ "$pct" -lt 30 ]]; then
    echo "FAIL: syntactic pass rate below 30% threshold"
    exit 1
fi

echo "== Step 4: Attack pattern presence check =="
for token in \
    "INTERSECT" \
    "EXCEPT" \
    "GENERATED ALWAYS AS" \
    "integrity_check" \
    "NATURAL JOIN" \
    "printf" \
    "group_concat" \
    "CREATE TRIGGER" \
; do
    if grep -q -- "$token" "$OUT_DIR/samples.txt"; then
        echo "  OK: '$token' observed"
    else
        echo "  FAIL: '$token' never generated in $SAMPLES samples"
        exit 1
    fi
done

echo ""
echo "SMOKE TEST PASSED"
```

- [ ] **Step 2: Make the script executable**

Run: `chmod +x scripts/smoke_attack_grammar.sh`

- [ ] **Step 3: Run the smoke test**

Run: `./scripts/smoke_attack_grammar.sh`
Expected final line: `SMOKE TEST PASSED`

If this fails with "Broken Grammar" from Nautilus's Rust loader, the grammar
has an undefined non-terminal. Run
`./target/release/generator -g grammars/sqlite_attack.py -t 100 -n 10 -s`
directly to see which non-terminal panics.

If it fails with low syntactic pass rate, print the first 10 samples and
inspect for obvious malformed SQL — the likely culprit is a shared
non-terminal expanding to garbage. Fix in place, re-run the smoke.

- [ ] **Step 4: Commit**

```bash
git add scripts/smoke_attack_grammar.sh
git commit -m "feat(scripts): add smoke_attack_grammar.sh pre-pilot gate"
```

---

## Task 9: 1-hour pilot on sqlite-3.31.1 — `sqlite_attack.py` vs `sqlite_patterns.py`

**Files:**
- No new files; runs existing `scripts/run_eval.sh` twice.

**Context:** Spec §10.4 — 1-hour pilot, one grammar × one target × one seed is enough to decide whether `sqlite_attack.py` is pilot-acceptance-grade. Acceptance from spec §10.6: attack grammar must hit ≥3 of 6 CVE classes in 1 hour.

We pick **sqlite-3.31.1** because the existing `docs/crash-report-patterns-pilot.md` used it (direct comparability) and it's vulnerable to 2 CVEs in the corpus (CVE-2020-13434, CVE-2020-9327) — plus CVE-2020-13435 and CVE-2020-15358 are often triggered via the SIGTRAP assertion path on this version, so 4 classes are realistically reachable.

- [ ] **Step 1: Verify preconditions**

```bash
ls -l harness/sqlite_harness_patterns_sqlite-3.31.1
wc -l grammars/sqlite_attack.py grammars/sqlite_patterns.py
```
Expected: harness binary exists; both grammar files exist with reasonable line counts.

- [ ] **Step 2: Run pilot for attack grammar (1 hour)**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
DURATION=3600 \
GRAMMAR="$(pwd)/grammars/sqlite_attack.py" \
HARNESS_SUFFIX=patterns_ \
./scripts/run_eval.sh sqlite-3.31.1 attack_pilot_1h
```

Expected: workdir at `/tmp/nautilus_eval/sqlite-3.31.1_attack_pilot_1h/` with `outputs/signaled/` containing crashes and `fuzzer.log` ending cleanly after ~3600 seconds.

- [ ] **Step 3: Run pilot for patterns baseline grammar (1 hour, fresh workdir)**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
DURATION=3600 \
GRAMMAR="$(pwd)/grammars/sqlite_patterns.py" \
HARNESS_SUFFIX=patterns_ \
./scripts/run_eval.sh sqlite-3.31.1 patterns_pilot_1h
```

Expected: workdir at `/tmp/nautilus_eval/sqlite-3.31.1_patterns_pilot_1h/`.

- [ ] **Step 4: Collect baseline metrics from both workdirs**

```bash
for run in attack_pilot_1h patterns_pilot_1h; do
    wd="/tmp/nautilus_eval/sqlite-3.31.1_${run}"
    echo "=== $run ==="
    echo -n "  crashes (signaled/): "
    ls "$wd/outputs/signaled/" 2>/dev/null | wc -l
    echo -n "  queue size:          "
    ls "$wd/outputs/queue/" 2>/dev/null | wc -l
    echo -n "  timeouts:            "
    ls "$wd/outputs/timeout/" 2>/dev/null | wc -l
    echo -n "  total exec count:    "
    grep -oP 'Execution Count: \K\d+' "$wd/fuzzer.log" 2>/dev/null | tail -1 || echo "n/a"
done
```

Record the output — needed in Task 10.

- [ ] **Step 5: Commit whatever scripts/artifacts (none expected here — just log)**

No files to commit in this task. If `scripts/run_eval.sh` produced any new
files in the repo tree (unlikely — it writes to `/tmp/`), commit them with:
```bash
git status
```
and commit only repo-tree changes.

---

## Task 10: Analyze and dedup crashes, classify CVE hits

**Files:**
- No new files. Uses existing `triage/dedup.py`.

**Context:** Spec §10.3 requires unique crash hashes and unique CVE classes hit. Existing `triage/dedup.py` clusters crashes by input signature.

- [ ] **Step 1: Run dedup on both workdirs**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
for run in attack_pilot_1h patterns_pilot_1h; do
    wd="/tmp/nautilus_eval/sqlite-3.31.1_${run}"
    echo "=== $run ==="
    python3 triage/dedup.py "$wd" || echo "dedup.py exited non-zero"
done
```

Record stdout — want unique-cluster counts per run.

- [ ] **Step 2: Classify CVE hits manually (5 min)**

For each workdir, pick 5 random crash files from `outputs/signaled/`:
```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
for run in attack_pilot_1h patterns_pilot_1h; do
    wd="/tmp/nautilus_eval/sqlite-3.31.1_${run}"
    echo "=== $run ==="
    ls "$wd/outputs/signaled/" | shuf -n 5 | while read f; do
        echo "--- $f ---"
        cat "$wd/outputs/signaled/$f"
        echo
    done
done
```

Visually classify each crash against the 6 CVE classes in `docs/cve-list.md`
using these signatures:
- `printf('%.*g', 2147483647, …)` or `group_concat(_, 2147483647)` → CVE-2020-13434
- `GENERATED ALWAYS AS` + JOIN + coalesce → CVE-2020-9327
- `JOIN … NATURAL JOIN` + coalesce+window → CVE-2020-13435
- `INTERSECT` inside WHERE + VIEW ORDER BY → CVE-2020-15358
- HAVING + window + EXCEPT → CVE-2020-13871
- `GENERATED ALWAYS AS` + `PRAGMA integrity_check` → CVE-2019-19646

Record the set of unique CVE classes hit per run.

---

## Task 11: Write pilot results report

**Files:**
- Create: `docs/attack-grammar-pilot-sqlite-3.31.1.md`

**Context:** Spec §10 evaluation plan — record metrics in a form that's comparable to `docs/crash-report-patterns-pilot.md` (the existing pilot report for `sqlite_patterns.py`).

- [ ] **Step 1: Write the report using actual numbers from Tasks 9–10**

Write to `docs/attack-grammar-pilot-sqlite-3.31.1.md`:

```markdown
# Pilot Results — sqlite_attack.py vs sqlite_patterns.py on sqlite-3.31.1

**Date:** <YYYY-MM-DD from run>
**Duration per run:** 3600 s (1 hour)
**Target:** sqlite-3.31.1 (ASan + UBSan harness, blank-DB patterns mode)
**Harness:** `harness/sqlite_harness_patterns_sqlite-3.31.1`
**Spec:** `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`

## Headline Numbers

| Metric | sqlite_attack.py | sqlite_patterns.py |
|---|---|---|
| Grammar lines | <fill from wc -l> | <fill from wc -l> |
| Total executions | <from fuzzer.log> | <from fuzzer.log> |
| Exec/sec | <total / 3600> | <total / 3600> |
| Signaled crashes (raw) | <from ls signaled/> | <from ls signaled/> |
| Unique crash clusters (dedup) | <from dedup.py> | <from dedup.py> |
| CVE classes hit | <count from Task 10 classification> | <count from Task 10 classification> |
| Crashes per million execs | <raw * 1e6 / total> | <raw * 1e6 / total> |

## CVE Class Hits

| CVE | sqlite_attack.py | sqlite_patterns.py | Notes |
|---|---|---|---|
| CVE-2020-13434 (printf / group_concat boundary) | <Y/N> | <Y/N> | |
| CVE-2020-9327 (gen-col + JOIN + coalesce) | <Y/N> | <Y/N> | |
| CVE-2020-13435 (JOIN + NATURAL JOIN + coalesce-window) | <Y/N> | <Y/N> | |
| CVE-2020-15358 (INTERSECT + VIEW) | <Y/N> | <Y/N> | |
| CVE-2020-13871 (HAVING + window + EXCEPT) | <Y/N> | <Y/N> | |
| CVE-2019-19646 (gen-col + integrity_check) | <Y/N> | <Y/N> | wrong version — 3.31.1 has it patched |

## Pilot Acceptance (Spec §10.6)

- attack grammar hits at least 3 of 6 CVE classes in 1 hour: <PASS/FAIL>
- attack grammar does NOT miss any CVE class that patterns grammar found: <PASS/FAIL>
- attack grammar crashes-per-million-execs at least 50% of patterns grammar rate: <PASS/FAIL>

## Interpretation

<1-3 short paragraphs on what the numbers mean. Hooks for the thesis:>
- Does the smaller grammar find bugs per CPU-hour at a competitive rate?
- Are there CVE classes only one grammar found? Why? (Grammar coverage gap or mutation luck?)
- Any SIGTRAP clusters that aren't in the 6-CVE corpus? (Possible new bug signal.)

## Next Steps

- If acceptance PASSED: proceed to spec-10.5 24-hour full campaign on all 4 versions.
- If acceptance FAILED: identify which vocabulary or canonical-form cut over-shrunk;
  file a follow-up spec, do NOT patch the grammar blindly.

## Raw Workdir Locations

- sqlite_attack pilot: `/tmp/nautilus_eval/sqlite-3.31.1_attack_pilot_1h/`
- sqlite_patterns pilot: `/tmp/nautilus_eval/sqlite-3.31.1_patterns_pilot_1h/`

These are ephemeral (`/tmp`) — if they need to persist, copy to
`docs/pilot-artifacts/<date>/` and commit separately.
```

Fill every `<...>` placeholder with the actual number from Tasks 9 and 10
before committing. Do not commit a report with unfilled placeholders.

- [ ] **Step 2: Verify no placeholders remain**

Run: `grep -n '<' docs/attack-grammar-pilot-sqlite-3.31.1.md || echo "no placeholders"`
Expected: `no placeholders`

- [ ] **Step 3: Commit the report**

```bash
git add docs/attack-grammar-pilot-sqlite-3.31.1.md
git commit -m "docs: add 1-hour pilot report for sqlite_attack.py vs sqlite_patterns.py"
```

---

## Task 12: Verify final deliverable state

**Files:** None modified.

**Context:** Final sanity pass before declaring the plan complete.

- [ ] **Step 1: Confirm all deliverables are in place**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
echo "-- Grammar --"
wc -l grammars/sqlite_attack.py
echo "-- Smoke script --"
ls -l scripts/smoke_attack_grammar.sh
echo "-- Pilot report --"
ls -l docs/attack-grammar-pilot-sqlite-3.31.1.md
echo "-- Spec reference --"
ls -l docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md
echo "-- Git log (last 10) --"
git log --oneline -10
```

Expected: all three deliverables exist; line count for grammar is in the
300-440 range; the last ~10 git commits include each section's feat commit.

- [ ] **Step 2: Run the smoke test one more time as regression check**

Run: `./scripts/smoke_attack_grammar.sh`
Expected: `SMOKE TEST PASSED`

- [ ] **Step 3: Declare complete**

No commit needed. Surface the pilot-report headline numbers to the user
and point at `docs/attack-grammar-pilot-sqlite-3.31.1.md` for detail.

---

## Out of Scope (explicit exclusions)

- **RL weight tuning.** Spec §9 defers weights to a separate spec. Do NOT add
  `weight=` anywhere in `sqlite_attack.py` during this plan.
- **24-hour full campaign** on all 4 SQLite versions (spec §10.5). That is a
  separate plan once the 1-hour pilot passes acceptance.
- **`sqlite_generated.py` (cve2grammar) integration.** Spec §11 open question.
- **Cross-DBMS porting** to DuckDB/MySQL. Spec §11 open question.
- **Fuzzer-source changes** (mutation scheduler, fork server, RL hooks). This
  plan touches Python grammar files only.

---

## Plan Self-Review (performed at plan-write time)

**Spec coverage check:**

| Spec section | Implementing task |
|---|---|
| §1 Motivation | Covered in plan header + Task 1 file header |
| §2 Corpus | Task 6 attack-pattern rules are one-per-CVE |
| §3 Six-step procedure | Tasks 1-7 execute the procedure in order |
| §4.1 Identifiers | Task 2 |
| §4.2 Literals | Task 2 |
| §4.3 Types/collations | Task 3 |
| §5 Canonical-form cuts | Task 4 |
| §6 Attack-pattern catalog | Task 6 |
| §7 Shared non-terminals | Task 5 |
| §8 Target-specific symbols | Task 7 |
| §9 Grammar file structure | Tasks 1-7 follow the structure |
| §10.3 Metrics | Tasks 9-10 collect metrics |
| §10.4 Pilot | Task 9 |
| §10.6 Acceptance criteria | Task 11 report records pass/fail |
| §11 Open questions | Out-of-scope list above |

**Placeholder scan:** No TBDs. Every code step has full code. Every command
has explicit env-var setup and expected output. Report template in Task 11
contains `<...>` placeholders that are explicitly called out as fill-ins
from prior-task outputs, with a grep step to block committing an unfilled
report.

**Type consistency:** non-terminal names are checked for hyphenation
consistency across tasks. `Pattern-P13434-Boundary`, `Pattern-P13434-Trigger`
(Task 6) match the spec §6 naming. `Coalesce-Window-Expr`, `Scalar-Subquery`,
`Join-Chain`, `GenCol-Def`, `View-Def` (Task 5) are referenced consistently
by Task 6 patterns.

**Ambiguity noted:** Spec §6 row for `P-COMPOUND-MIX` left `{DDL-sequence}`
and `{Col-List}` undefined. Plan Task 6 resolves this by using explicit
`CREATE TABLE ... CREATE TABLE ...` DDL and a concrete `SELECT ... ORDER BY`
that references shared `{Order-By}` rule — no ambiguous non-terminals
leaked into the grammar.
