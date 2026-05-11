# JSON/JSONB Grammar Expansion — Design Spec

**Date:** 2026-05-10
**Status:** Draft
**Goal:** Expand the SQLite fuzzing grammar with ~35 new JSON/JSONB rules to target the json.c module in SQLite 3.53.0 (5,682 lines, grown from ~3,500 in 3.31.1). Current grammar has 6 JSON rules and zero JSONB, json_each, json_tree, json_set, json_patch, or json_remove coverage.

---

## Motivation

SQLite 3.53.0 campaigns produce zero crashes across 5×15min runs with the current 469-rule grammar. Coverage saturates at ~22,800 edges by 10 minutes. The grammar exhausts its own range before reaching new code in json.c.

json.c grew by ~2,200 lines between 3.31.1 and 3.53.0, adding JSONB (binary JSON) variants of every function, json_parse(), json_pretty(), json_error_position(), and expanded json_each/json_tree virtual table functionality. None of this new code is reachable by the current grammar.

The DBMS fuzzing expert estimates 15-25% crash probability if JSON/JSONB rules are added, based on:
- json.c complexity (5,682 lines with manual memory management)
- JSONB binary format parsing (new, less battle-tested)
- json_each/json_tree virtual table cursor management (historically fragile pattern)

## Approach

Layer 1 extension within existing grammar architecture. No new Sql-Stmt templates (Layer 2). JSON functions compose naturally through existing Schema-Setup × Stress-Query templates. The mutation engine's splice operator will cross-pollinate JSON with window functions, JOINs, and aggregates.

All new rules use default weight=1.0. Lesson from v3.0: boosted FTS weight (2.0) caused 92% crash dominance. Equal weighting preserves compositional diversity.

## File Changed

`grammars/active/sqlite_v3.py` — append new rules after existing JSON section (line ~519).

No other files change. Grammar version bumps to v3.3.

## New Nonterminals

### Json-Key (4 rules)

Short fixed keys for JSON object access. Kept minimal to avoid probability dilution.

```python
ctx.rule("Json-Key", "a")
ctx.rule("Json-Key", "b")
ctx.rule("Json-Key", "c")
ctx.rule("Json-Key", "key")
```

### Json-Path (8 rules)

JSON path expressions for navigating JSON structures. SQLite uses `$` as root, `.key` for object access, `[N]` for array indexing, `[#-1]` for last-element shorthand.

```python
ctx.rule("Json-Path", "'$'")
ctx.rule("Json-Path", "'$.{Json-Key}'")
ctx.rule("Json-Path", "'$.{Json-Key}.{Json-Key}'")
ctx.rule("Json-Path", "'$[{Int-Literal}]'")
ctx.rule("Json-Path", "'$[#-1]'")
ctx.rule("Json-Path", "'$.{Json-Key}[{Int-Literal}]'")
ctx.rule("Json-Path", "'$.{Json-Key}[#-1]'")
ctx.rule("Json-Path", "'$[0].{Json-Key}'")
```

### Json-Literal (6 rules)

Valid JSON text strings for use as function arguments. Provides well-formed JSON so functions reach parsing and traversal code rather than returning early on syntax errors.

```python
ctx.rule("Json-Literal", "'{}'")
ctx.rule("Json-Literal", "'[]'")
ctx.rule("Json-Literal", "'{\"a\":1}'")
ctx.rule("Json-Literal", "'[1,2,3]'")
ctx.rule("Json-Literal", "'{\"a\":{\"b\":1}}'")
ctx.rule("Json-Literal", "'[{\"a\":1},{\"b\":2}]'")
```

## New Func-Call Rules

### JSON Text Output (~8 new rules)

Upgrade existing rules (use Json-Path) and add missing functions:

```python
ctx.rule("Func-Call", "json_extract({Expr}, {Json-Path})")    # replace existing Str-Literal version
ctx.rule("Func-Call", "json_insert({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_replace({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_set({Json-Literal}, {Json-Path}, {Expr})")
ctx.rule("Func-Call", "json_remove({Json-Literal}, {Json-Path})")
ctx.rule("Func-Call", "json_patch({Json-Literal}, {Json-Literal})")
ctx.rule("Func-Call", "json_pretty({Expr})")
ctx.rule("Func-Call", "json_quote({Expr})")
```

### JSONB Binary Output (~9 new rules)

JSONB variants produce binary JSON (internal format). These exercise the JSONB serialization/deserialization code paths — the newest, least-tested part of json.c.

```python
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

### Analysis Functions (~4 new rules)

Functions that inspect JSON structure without modifying:

```python
ctx.rule("Func-Call", "json_type({Expr}, {Json-Path})")           # two-arg form (one-arg exists)
ctx.rule("Func-Call", "json_array_length({Expr})")
ctx.rule("Func-Call", "json_array_length({Expr}, {Json-Path})")
ctx.rule("Func-Call", "json_error_position({Expr})")
```

### From-Clause Table-Valued Functions (~6 new rules)

json_each() and json_tree() are virtual table functions that produce rows. Added as alternatives in the From-Clause nonterminal.

```python
ctx.rule("From-Clause", "json_each({Json-Literal})")
ctx.rule("From-Clause", "json_each({Expr}, {Json-Path})")
ctx.rule("From-Clause", "json_tree({Json-Literal})")
ctx.rule("From-Clause", "json_tree({Expr}, {Json-Path})")
ctx.rule("From-Clause", "jsonb_each({Json-Literal})")
ctx.rule("From-Clause", "jsonb_tree({Json-Literal})")
```

## Rule Inventory

| Category | New Rules | Nonterminal |
|----------|-----------|-------------|
| Json-Key | 4 | Json-Key (new) |
| Json-Path | 8 | Json-Path (new) |
| Json-Literal | 6 | Json-Literal (new) |
| JSON text functions | 8 | Func-Call |
| JSONB binary functions | 9 | Func-Call |
| Analysis functions | 4 | Func-Call |
| Table-valued functions | 6 | From-Clause |
| **Total** | **45** | |

**Old rule to remove:** `ctx.rule("Func-Call", "json_extract({Expr}, {Str-Literal})")` — replaced by Json-Path version.

**Grammar version:** v3.2 (469 rules) → v3.3 (513 rules)

## Composition Examples

The fuzzer's mutation engine will discover combinations like:

```sql
-- JSON + window function
SELECT json_extract(c1, '$.a') OVER (ORDER BY c2) FROM p;

-- json_each JOIN with real table
SELECT p.c1, j.value FROM p, json_each(p.c1) AS j WHERE j.key = 'a';

-- JSONB round-trip (serialize then parse)
SELECT json(jsonb_set('{"a":1}', '$.b', 42));

-- json_tree in subquery
SELECT * FROM p WHERE c1 IN (SELECT value FROM json_tree('{"a":{"b":[1,2,3]}}'));

-- Nested JSON functions
SELECT json_patch(json_set('{}', '$.a', 1), '{"b":2}');
```

None of these are encoded as templates — they emerge from compositional combination of Layer 1 primitives through the mutation engine.

## Integration with Existing Grammar

No Layer 2 changes. JSON enters through:

```
Sql-Stmt → Schema-Setup; Stress-Query
                              ↓
                         Select-Stmt → SELECT {Expr} FROM {From-Clause}
                                         ↓                  ↓
                                    Func-Call             json_each(...)
                                      ↓                  json_tree(...)
                                json_extract(...)
                                jsonb_set(...)
```

## Testing

After adding rules:
1. `cargo run --bin generator -- -g grammars/active/sqlite_v3.py -t 100` — verify 100 valid SQL generated without `Broken Grammar` panic
2. Grep generated output for `json`, `jsonb`, `json_each` — confirm new rules appear
3. Run 15-min smoke campaign on 3.53.0: `DURATION=900 ./scripts/run_eval.sh sqlite-3.53.0 json_smoke`
4. Check coverage delta: expect >22,800 edges (previous max) if json.c code reached
5. Run full 1-hour campaign: `DURATION=3600 ./scripts/run_eval.sh sqlite-3.53.0 json_1h`

## Constraints

- All rules weight=1.0 (no boosting)
- No PoC contamination — no hardcoded JSON strings that trigger specific bugs
- No changes outside `grammars/active/sqlite_v3.py`
- Must not break existing grammar (all old nonterminals still resolvable)
- Json-Literal uses single quotes as SQL string delimiters, with escaped inner double quotes for JSON keys

## Out of Scope

- FULL OUTER JOIN rules (separate expansion)
- RETURNING clause rules (separate expansion)
- API_ARMOR harness flag (separate harness rebuild)
- Adversarial PRAGMA configurations (separate schema change)
- Grammar composition with sqlite_generated.py (blocked on separate spec)
