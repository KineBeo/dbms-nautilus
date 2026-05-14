# Spec: Pragmatic EBNF Grammar Expansion

**Date:** 2026-05-14
**Status:** Approved
**Scope:** Expand `grammars/sqlite-ebnf.py` to cover all structurally distinct optional combinations from `docs/tree-sitter-sqlite.ebnf`

---

## Problem

Cross-review (main thread + Opus subagent) found ~155-170 missing rule variants in `sqlite-ebnf.py`. Many EBNF productions with optional parts (`?`, `*`) only have partial combinations expanded. The fuzzer cannot generate SQL shapes for missing combos.

## Decision

Pragmatic baseline: expand only combos that produce structurally different SQL (different SQLite code paths). Skip cosmetic variants (ADD vs ADD COLUMN), schema-qualified names, bind_parameter, CONSTRAINT name prefix. ~65 new rules.

## Expansion List

### 1. select_stmt (+8 rules)
```python
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Limit-Clause}")
ctx.rule("Select-Stmt", "{Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause} {Limit-Clause}")
ctx.rule("Select-Stmt", "{With-Clause} {Select-Core} {Compound-Op} {Select-Core} {Order-By-Clause} {Limit-Clause}")
```

### 2. _select_core (+4 rules)
```python
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List}")
ctx.rule("Select-Core", "SELECT ALL {Result-Col-List}")
ctx.rule("Select-Core", "SELECT DISTINCT {Result-Col-List} {From-Clause} {Where-Clause} {Group-By-Clause}")
ctx.rule("Select-Core", "SELECT {Result-Col-List} {From-Clause} {Group-By-Clause} {Window-Clause}")
```

### 3. update_stmt (+6 rules)
```python
ctx.rule("Update-Stmt", "UPDATE OR ABORT {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR FAIL {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE OR ROLLBACK {Table-Name} SET {Col-Name} = {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} FROM {Join-Clause}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr} ORDER BY {Ordering-Term} LIMIT {Expr}")
ctx.rule("Update-Stmt", "UPDATE {Table-Name} SET {Col-Name} = {Expr} WHERE {Expr} RETURNING {Result-Col-List}")
```

### 4. delete_stmt (+4 rules)
```python
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "DELETE FROM {Table-Name} WHERE {Expr} ORDER BY {Ordering-Term} LIMIT {Expr}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name} WHERE {Expr} RETURNING {Result-Col-List}")
ctx.rule("Delete-Stmt", "{With-Clause} DELETE FROM {Table-Name}")
```

### 5. insert_stmt (+4 rules)
```python
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}), ({Expr-List})")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} ({Col-Name-List}) VALUES ({Expr-List}) RETURNING {Result-Col-List}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} {Select-Stmt} RETURNING {Result-Col-List}")
ctx.rule("Insert-Stmt", "INSERT INTO {Table-Name} VALUES ({Expr-List}), ({Expr-List}), ({Expr-List})")
```

### 6. create_table_stmt (+4 rules)
```python
ctx.rule("Create-Table-Stmt", "CREATE TEMP TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List})")
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List}) WITHOUT ROWID")
ctx.rule("Create-Table-Stmt", "CREATE TABLE IF NOT EXISTS {Table-Name} ({Col-Def-List}) STRICT")
ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID, STRICT")
```

### 7. create_trigger_stmt (+6 rules)
```python
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 BEFORE DELETE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER DELETE ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER UPDATE OF {Col-Name} ON {Table-Name} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} FOR EACH ROW BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} WHEN {Expr} BEGIN {Trigger-Body} END")
ctx.rule("Create-Trigger-Stmt",
    "CREATE TRIGGER trg1 AFTER INSERT ON {Table-Name} FOR EACH ROW WHEN {Expr} BEGIN {Trigger-Body} END")
```

### 8. Trigger-Body (+2 rules)
```python
ctx.rule("Trigger-Body", "UPDATE {Table-Name} SET {Col-Name} = {Expr};")
ctx.rule("Trigger-Body", "DELETE FROM {Table-Name};")
```

### 9. create_view_stmt (+2 rules)
```python
ctx.rule("Create-View-Stmt", "CREATE TEMP VIEW IF NOT EXISTS v1 AS {Select-Stmt}")
ctx.rule("Create-View-Stmt", "CREATE VIEW IF NOT EXISTS v1 ({Col-Name-List}) AS {Select-Stmt}")
```

### 10. column_def (+5 rules)
```python
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY AUTOINCREMENT")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY ASC")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} PRIMARY KEY DESC")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} COLLATE NOCASE")
ctx.rule("Col-Def", "{Col-Name} {Type-Name} DEFAULT ({Expr})")
```

### 11. _expr (+4 rules)
```python
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} WHEN {Expr} THEN {Expr} END")
ctx.rule("Expr", "CASE WHEN {Expr} THEN {Expr} WHEN {Expr} THEN {Expr} ELSE {Expr} END")
ctx.rule("Expr", "({Expr}, {Expr})")
ctx.rule("Expr", "{Expr} NOT GLOB {Expr}")
```

### 12. frame_spec (+4 rules)
```python
ctx.rule("Frame-Spec", "ROWS UNBOUNDED PRECEDING")
ctx.rule("Frame-Spec", "ROWS {Expr} PRECEDING")
ctx.rule("Frame-Spec", "ROWS CURRENT ROW")
ctx.rule("Frame-Spec", "RANGE UNBOUNDED PRECEDING")
```

### 13. join_operator (+3 rules)
```python
ctx.rule("Join-Operator", "NATURAL LEFT OUTER JOIN")
ctx.rule("Join-Operator", "NATURAL INNER JOIN")
ctx.rule("Join-Operator", "NATURAL CROSS JOIN")
```

### 14. rollback_stmt (+2 rules)
```python
ctx.rule("Rollback-Stmt", "ROLLBACK TRANSACTION")
ctx.rule("Rollback-Stmt", "ROLLBACK TO sp1")
```

### 15. begin_stmt (+1 rule)
```python
ctx.rule("Begin-Stmt", "BEGIN TRANSACTION")
```

### 16. drop_stmt (+3 rules)
```python
ctx.rule("Drop-Stmt", "DROP INDEX idx1")
ctx.rule("Drop-Stmt", "DROP VIEW v1")
ctx.rule("Drop-Stmt", "DROP TRIGGER trg1")
```

### 17. ordering_term (+2 rules)
```python
ctx.rule("Ordering-Term", "{Expr} NULLS FIRST")
ctx.rule("Ordering-Term", "{Expr} NULLS LAST")
```

### 18. group_by_clause (+1 rule)
```python
ctx.rule("Group-By-Clause", "GROUP BY {Expr}, {Expr} HAVING {Expr}")
```

### 19. Remove Asc-Desc (-2 rules)
Delete orphan NT (defined but never referenced).

## Out of Scope

- Schema-qualified names (_name2)
- bind_parameter
- CONSTRAINT name prefix on column/table constraints
- Optional keyword synonyms (ADD vs ADD COLUMN, RENAME vs RENAME COLUMN)
- TRANSACTION name parameter in BEGIN/COMMIT/ROLLBACK
- EXPLAIN / EXPLAIN QUERY PLAN prefix
- 3+ items in list NTs beyond what exists

## Verification

After all edits:
1. Grammar loads: `generator -g grammars/sqlite-ebnf.py -t 100 -n 10`
2. No dangling NT references
3. No weight= parameters
4. New productions appear in generated output
