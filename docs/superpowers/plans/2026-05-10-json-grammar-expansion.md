# JSON/JSONB Grammar Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add ~45 JSON/JSONB rules to `grammars/active/sqlite_v3.py` (v3.2 → v3.3) targeting SQLite 3.53.0's json.c module. New nonterminals: Json-Key, Json-Path, Json-Literal. New Func-Call and Table-Or-Subquery rules for all JSON/JSONB functions.

**Architecture:** Layer 1 extension only. No Layer 2 template changes. All rules weight=1.0. JSON composes through existing Schema-Setup × Stress-Query templates.

**Tech Stack:** Python grammar DSL (`ctx.rule()`), Rust fuzzer (`cargo run --bin generator`), bash campaign scripts.

**Key facts:**
- Grammar file: `grammars/active/sqlite_v3.py` (currently 469 rules, ~725 lines)
- Existing JSON rules at lines 513-519 (6 rules in `Func-Call`)
- `Table-Or-Subquery` nonterminal at lines 82-87 — where json_each/json_tree go
- Generator test: `PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo run --bin generator -- -g grammars/active/sqlite_v3.py -t 100`
- Campaign: `DURATION=900 ./scripts/run_eval.sh sqlite-3.53.0 json_smoke`

---

### Task 1: Add Json-Key, Json-Path, Json-Literal nonterminals

**Files:**
- Modify: `grammars/active/sqlite_v3.py` (after line 519, before Window functions section)

- [ ] **Step 1: Add Json-Key nonterminal (4 rules)**

Insert after line 519 (`json_object` rule), before the window functions section:

```python
# ============================================================
# JSON/JSONB expansion (v3.3 — targeting json.c in SQLite 3.45+)
# ============================================================

# Json-Key: short fixed keys for JSON object paths
ctx.rule("Json-Key", "a")
ctx.rule("Json-Key", "b")
ctx.rule("Json-Key", "c")
ctx.rule("Json-Key", "key")
```

- [ ] **Step 2: Add Json-Path nonterminal (8 rules)**

```python
# Json-Path: JSON path expressions for navigation
ctx.rule("Json-Path", "'$'")
ctx.rule("Json-Path", "'$.{Json-Key}'")
ctx.rule("Json-Path", "'$.{Json-Key}.{Json-Key}'")
ctx.rule("Json-Path", "'$[{Int-Literal}]'")
ctx.rule("Json-Path", "'$[#-1]'")
ctx.rule("Json-Path", "'$.{Json-Key}[{Int-Literal}]'")
ctx.rule("Json-Path", "'$.{Json-Key}[#-1]'")
ctx.rule("Json-Path", "'$[0].{Json-Key}'")
```

- [ ] **Step 3: Add Json-Literal nonterminal (6 rules)**

```python
# Json-Literal: well-formed JSON strings as function arguments
ctx.rule("Json-Literal", "'{}'")
ctx.rule("Json-Literal", "'[]'")
ctx.rule("Json-Literal", "'{\"a\":1}'")
ctx.rule("Json-Literal", "'[1,2,3]'")
ctx.rule("Json-Literal", "'{\"a\":{\"b\":1}}'")
ctx.rule("Json-Literal", "'[{\"a\":1},{\"b\":2}]'")
```

- [ ] **Step 4: Verify grammar parses without error**

```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo run --bin generator -- -g grammars/active/sqlite_v3.py -t 10 2>&1 | head -5
```

Expected: 10 SQL statements generated, no `Broken Grammar` panic. Json-Key/Path/Literal may not appear yet since no rules reference them — that's fine, they'll be used in Task 2.

- [ ] **Step 5: Commit**

```bash
git add grammars/active/sqlite_v3.py
git commit -m "feat(grammar): v3.3 — add Json-Key, Json-Path, Json-Literal nonterminals"
```

---

### Task 2: Add JSON text and JSONB Func-Call rules

**Files:**
- Modify: `grammars/active/sqlite_v3.py`

- [ ] **Step 1: Replace existing json_extract with Json-Path version**

Change line 517 from:
```python
ctx.rule("Func-Call", "json_extract({Expr}, {Str-Literal})")
```
to:
```python
ctx.rule("Func-Call", "json_extract({Expr}, {Json-Path})")
```

- [ ] **Step 2: Add JSON text mutation functions (8 rules)**

Insert after the existing `json_object` rule (line 519):

```python
# JSON text mutation functions
ctx.rule("Func-Call", "json_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "json_patch({Json-Literal}, {Json-Literal})")
ctx.rule("Func-Call", "json_pretty({Expr})")
ctx.rule("Func-Call", "json_quote({Expr})")
ctx.rule("Func-Call", "json_object({Str-Literal}, {Expr}, {Str-Literal}, {Expr})")
```

- [ ] **Step 3: Add JSONB binary functions (9 rules)**

```python
# JSONB binary output variants (new in SQLite 3.45+)
ctx.rule("Func-Call", "jsonb({Expr})")
ctx.rule("Func-Call", "jsonb_array({Expr-List})")
ctx.rule("Func-Call", "jsonb_object({Str-Literal}, {Expr})")
ctx.rule("Func-Call", "jsonb_extract({Expr}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "jsonb_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "jsonb_patch({Json-Literal}, {Json-Literal})")
```

- [ ] **Step 4: Add JSON analysis functions (4 rules)**

```python
# JSON analysis functions
ctx.rule("Func-Call", "json_type({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_array_length({Expr})")
ctx.rule("Func-Call", "json_array_length({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_error_position({Expr})")
```

- [ ] **Step 5: Generate and verify JSON functions appear in output**

```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo run --bin generator -- -g grammars/active/sqlite_v3.py -t 200 2>&1 | grep -i 'json\|jsonb' | head -20
```

Expected: Multiple lines containing `json_set`, `jsonb_extract`, `json_patch`, etc.

- [ ] **Step 6: Commit**

```bash
git add grammars/active/sqlite_v3.py
git commit -m "feat(grammar): v3.3 — add JSON text, JSONB, and analysis Func-Call rules"
```

---

### Task 3: Add json_each/json_tree as Table-Or-Subquery alternatives

**Files:**
- Modify: `grammars/active/sqlite_v3.py` (Table-Or-Subquery section, ~line 82-87)

- [ ] **Step 1: Add table-valued function rules (6 rules)**

Insert after line 87 (`({Join-Clause})` rule):

```python
# JSON table-valued functions (virtual table sources)
ctx.rule("Table-Or-Subquery", "json_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_each({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "json_tree({Json-Literal})")
ctx.rule("Table-Or-Subquery", "json_tree({Expr}, {Json-Path})")
ctx.rule("Table-Or-Subquery", "jsonb_each({Json-Literal})")
ctx.rule("Table-Or-Subquery", "jsonb_tree({Json-Literal})")
```

- [ ] **Step 2: Generate and verify json_each/json_tree appear in FROM clauses**

```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo run --bin generator -- -g grammars/active/sqlite_v3.py -t 500 2>&1 | grep -i 'json_each\|json_tree\|jsonb_each\|jsonb_tree' | head -10
```

Expected: Lines like `SELECT ... FROM json_each(...)` or `... FROM json_tree(...) JOIN ...`

- [ ] **Step 3: Commit**

```bash
git add grammars/active/sqlite_v3.py
git commit -m "feat(grammar): v3.3 — add json_each/json_tree table-valued functions"
```

---

### Task 4: Update grammar version metadata and uniform grammar

**Files:**
- Modify: `grammars/active/sqlite_v3.py` (version comment at top)
- Modify: `grammars/active/sqlite_v3_uniform.py` (sync new rules with weight=1.0)

- [ ] **Step 1: Update version comment**

Change line 1-2 of `grammars/active/sqlite_v3.py`:
```python
# sqlite_v3.py — Structural Primitives grammar for Nautilus SQLite fuzzing
# Version: v3.3 (JSON/JSONB expansion)
```

- [ ] **Step 2: Count total rules to verify**

```bash
grep -c 'ctx.rule\|ctx.add_rule\|ctx.regex' grammars/active/sqlite_v3.py
```

Expected: ~514 (was 469, added ~45)

- [ ] **Step 3: Sync uniform grammar**

Copy `sqlite_v3.py` to `sqlite_v3_uniform.py` and strip all weights:

```bash
cp grammars/active/sqlite_v3.py grammars/active/sqlite_v3_uniform.py
sed -i 's/, weight=[0-9.]*)/)/g' grammars/active/sqlite_v3_uniform.py
```

Verify uniform grammar also parses:
```bash
PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 cargo run --bin generator -- -g grammars/active/sqlite_v3_uniform.py -t 10 2>&1 | head -3
```

- [ ] **Step 4: Update grammars/v3.3/meta.json**

```bash
mkdir -p grammars/v3.3
cp grammars/active/sqlite_v3.py grammars/v3.3/sqlite_v3.py
```

Create `grammars/v3.3/meta.json`:
```json
{
  "version": "3.3",
  "date": "2026-05-10",
  "rules": 514,
  "change": "+45 JSON/JSONB rules: json_set, json_patch, jsonb_*, json_each, json_tree, Json-Path, Json-Literal nonterminals",
  "target": "json.c expansion in SQLite 3.45+"
}
```

- [ ] **Step 5: Commit**

```bash
git add grammars/active/ grammars/v3.3/
git commit -m "feat(grammar): v3.3 — finalize JSON/JSONB expansion (469 → 514 rules)"
```

---

### Task 5: Smoke test on SQLite 3.53.0

**Files:**
- No code changes — execution and verification only

- [ ] **Step 1: Run 15-min smoke campaign**

```bash
DURATION=900 ./scripts/run_eval.sh sqlite-3.53.0 json_smoke
```

Expected: completes without error. Check coverage delta vs previous runs.

- [ ] **Step 2: Check coverage improvement**

```bash
tail -1 workdirs/sqlite-3.53.0_json_smoke/coverage.csv
```

Expected: edges > 22,789 (previous max). If json.c code is now reached, should see 1,000-3,000 new edges.

- [ ] **Step 3: Check for crashes**

```bash
ls workdirs/sqlite-3.53.0_json_smoke/outputs/signaled/ 2>/dev/null | wc -l
```

Any crashes are a win. Run triage if crashes found:
```bash
python3.13 triage/classify.py workdirs/sqlite-3.53.0_json_smoke --harness harness/test/sqlite_harness_sqlite-3.53.0_test
```

- [ ] **Step 4: Check JSON function frequency in generated inputs**

```bash
grep -r -l 'json_each\|jsonb_set\|json_tree\|json_patch' workdirs/sqlite-3.53.0_json_smoke/outputs/queue/ 2>/dev/null | wc -l
```

Expected: >0 — confirms JSON rules are being used.

- [ ] **Step 5: Report results and commit campaign data**

```bash
# Archive campaign
GRAMMAR_VERSION=v3.3 ./scripts/run_eval.sh sqlite-3.53.0 json_smoke_archive 2>/dev/null || true
git add workdirs/sqlite-3.53.0_json_smoke/ 2>/dev/null || true
```

---

### Task 6: Run 1-hour campaign

**Files:**
- No code changes — long campaign execution

- [ ] **Step 1: Run 1-hour campaign**

```bash
DURATION=3600 ./scripts/run_eval.sh sqlite-3.53.0 json_1h
```

This takes 60 minutes. Monitor with:
```bash
tail -f workdirs/sqlite-3.53.0_json_1h/coverage.csv
```

- [ ] **Step 2: Triage results**

After completion:
```bash
python3.13 triage/classify.py workdirs/sqlite-3.53.0_json_1h \
  --harness harness/test/sqlite_harness_sqlite-3.53.0_test

python3.13 triage/classify.py workdirs/sqlite-3.53.0_json_1h \
  --harness harness/nosanit/sqlite_harness_sqlite-3.53.0_nosanit \
  --output workdirs/sqlite-3.53.0_json_1h/triage_nosanit.json
```

- [ ] **Step 3: Update crash evidence archive if crashes found**

```bash
python3.13 scripts/collect_crashes.py --incremental
```

- [ ] **Step 4: Report coverage and crash metrics**

Compare:
- Previous 3.53.0 max coverage: 22,789 edges
- New coverage with JSON grammar
- Any new crash classes?
