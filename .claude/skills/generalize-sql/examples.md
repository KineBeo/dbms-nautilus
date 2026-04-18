# Worked Examples — SQL → Template

Each example shows the **original SQL**, a **bad rewrite** (too abstract
or too specific) with why it's bad, and the **good rewrite** that should
be emitted.

---

## 1. COLLATE NOCASE on WITHOUT ROWID

**Original SQL:**

```sql
CREATE TABLE test (c1 TEXT PRIMARY KEY) WITHOUT ROWID;
CREATE INDEX index_0 ON test(c1 COLLATE NOCASE);
INSERT INTO test(c1) VALUES ('A');
INSERT INTO test(c1) VALUES ('a');
SELECT * FROM test;
```

**Feature:** case-insensitive index on a WITHOUT ROWID table.

**Bad rewrite — too abstract:**
```
SELECT {Result-Col-List} FROM {Table-Name}
```
Loses the whole feature. Indistinguishable from any SELECT.

**Bad rewrite — too specific:**
```
CREATE TABLE test (c1 TEXT PRIMARY KEY) WITHOUT ROWID;\nCREATE INDEX index_0 ON test(c1 COLLATE NOCASE);\nSELECT * FROM test
```
Names are baked in. The fuzzer won't try other shapes.

**Good rewrite:**
```json
{
  "template": "CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID;\nCREATE INDEX idx ON {Table-Name}({Col-Name} COLLATE NOCASE);\nINSERT INTO {Table-Name} VALUES ({Literal});\nSELECT * FROM {Table-Name}",
  "feature_tag": "collate_nocase_without_rowid",
  "weight": 3.0,
  "notes": "NOCASE index on WITHOUT ROWID — keep both literal keywords"
}
```

Literal `WITHOUT ROWID` and `COLLATE NOCASE` because those *are* the
feature. Table and column names abstracted; index name stays literal
(`idx` — no `{Index-Name}` non-terminal exists). One INSERT preserved as
the DML step (the fuzzer mutates `{Literal}`).

---

## 2. printf precision overflow

**Original SQL:**

```sql
SELECT printf('%.*g', 2147483647, 0.01);
```

**Feature:** integer-overflow vulnerability in printf's precision
argument.

**Bad rewrite:**
```
SELECT {Expr}
```
Missing `printf`. No fuzzer run from this template hits the vulnerable
code path.

**Good rewrite:**
```json
{
  "template": "SELECT printf('%.*g', {Boundary-Int}, {Expr})",
  "feature_tag": "printf_precision_overflow",
  "weight": 3.0,
  "notes": "int32 boundary in precision arg; any expr for the value"
}
```

`printf` and the format string stay literal (the feature is the format
specifier `%.*g` with a giant precision). `{Boundary-Int}` mutates the
attack value; `{Expr}` varies the final argument.

---

## 3. FTS4 snippet function

**Original SQL:**

```sql
CREATE VIRTUAL TABLE t USING fts4(content);
INSERT INTO t VALUES('hello world');
SELECT snippet(t, '<b>', '</b>', '...', -1, -1) FROM t WHERE content MATCH 'hello';
```

**Feature:** the `snippet()` function on a virtual FTS4 table.

**Good rewrite:**
```json
{
  "template": "CREATE VIRTUAL TABLE {Table-Name} USING fts4({Col-Def-List});\nINSERT INTO {Table-Name} VALUES ({Str-Literal});\nSELECT snippet({Table-Name}, '<b>', '</b>', '...', -1, -1) FROM {Table-Name} WHERE {Col-Name} MATCH {Str-Literal}",
  "feature_tag": "fts4_snippet",
  "weight": 3.0,
  "notes": "FTS4 virtual table + literal snippet() call; MATCH clause with string literal"
}
```

`USING fts4`, `snippet(...)`, and `MATCH` all stay literal — no `Fts-*`
non-terminals exist in the live grammar. Column names and string values
abstracted via `{Col-Name}` and `{Str-Literal}`.

---

## 4. Window function with PARTITION BY

**Original SQL:**

```sql
SELECT a, row_number() OVER (PARTITION BY b ORDER BY c) FROM t;
```

**Feature:** window function with `PARTITION BY`.

**Good rewrite:**
```json
{
  "template": "SELECT {Result-Col-List}, {Agg-Func}() OVER (PARTITION BY {Col-Name} ORDER BY {Col-Name}) FROM {Table-Name}",
  "feature_tag": "window_func_partition_by",
  "weight": 3.0,
  "notes": "Any agg-func, any partition/order column"
}
```

`OVER`, `PARTITION BY`, `ORDER BY` kept literal — they name the feature.
`{Agg-Func}` and `{Col-Name}` diversify the function choice and sort columns.

---

## 5. Deeply nested CASE expression

**Original SQL:**

```sql
SELECT CASE WHEN a>0 THEN CASE WHEN b>0 THEN CASE WHEN c>0 THEN 1 ELSE 2 END ELSE 3 END ELSE 4 END FROM t;
```

**Feature:** parser/planner stress from deeply nested CASE WHEN.

**Good rewrite:**
```json
{
  "template": "SELECT {Deep-Expr} FROM {Table-Name}",
  "feature_tag": "deep_nested_case_expr",
  "weight": 3.0,
  "notes": "{Deep-Expr} is the rl-nautilus nonterminal for nested CASE/expression stress"
}
```

Here abstraction wins — the whole point IS the depth, which is what
`{Deep-Expr}` is designed to produce.

---

## 6. Trigger with recursive CTE

**Original SQL:**

```sql
CREATE TABLE t(x INTEGER);
CREATE TRIGGER tr AFTER INSERT ON t BEGIN
  WITH RECURSIVE r(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM r WHERE n<10)
  INSERT INTO t SELECT n FROM r;
END;
INSERT INTO t VALUES(1);
```

**Feature:** trigger body containing a recursive CTE.

**Good rewrite:**
```json
{
  "template": "CREATE TABLE {Table-Name}({Col-Def-List});\nCREATE TRIGGER tr AFTER INSERT ON {Table-Name} BEGIN {Cte-Def} INSERT INTO {Table-Name} SELECT {Col-Name} FROM {Table-Name}; END;\nINSERT INTO {Table-Name} VALUES ({Literal})",
  "feature_tag": "trigger_with_recursive_cte",
  "weight": 3.0,
  "notes": "Trigger body using {Cte-Def} (rl-nautilus handles RECURSIVE expansion)"
}
```

`CREATE TRIGGER`, `AFTER INSERT ON`, `BEGIN`/`END` stay literal — they
name the feature. Trigger name stays literal (`tr` — no `{Trigger-Name}`
non-terminal). The CTE gets expressed via `{Cte-Def}`.

---

## 7. INSERT INTO ... ON CONFLICT

**Original SQL:**

```sql
CREATE TABLE t(a INTEGER PRIMARY KEY, b);
INSERT INTO t VALUES(1, 'x');
INSERT INTO t VALUES(1, 'y') ON CONFLICT(a) DO UPDATE SET b=excluded.b;
```

**Feature:** UPSERT via ON CONFLICT.

**Good rewrite:**
```json
{
  "template": "CREATE TABLE {Table-Name}({Col-Def-List});\nINSERT INTO {Table-Name} VALUES ({Literal});\nINSERT INTO {Table-Name} VALUES ({Literal}) ON CONFLICT({Col-Name}) DO UPDATE SET {Col-Name}=excluded.{Col-Name}",
  "feature_tag": "insert_on_conflict_do_update",
  "weight": 3.0,
  "notes": "ON CONFLICT DO UPDATE — UPSERT path"
}
```

`ON CONFLICT`, `DO UPDATE`, and `excluded.` stay literal because they're
the syntactic hooks for the feature.

---

## 8. UNIQUE index with generated column

**Original SQL:**

```sql
CREATE TABLE v0(v3, v1 GENERATED ALWAYS AS (v3) UNIQUE);
INSERT INTO v0(v3) VALUES(1);
SELECT * FROM v0;
```

**Feature:** generated column with UNIQUE constraint.

**Good rewrite:**
```json
{
  "template": "CREATE TABLE {Table-Name}({Col-Name}, {Col-Name} GENERATED ALWAYS AS ({Expr}) UNIQUE);\nINSERT INTO {Table-Name}({Col-Name}) VALUES ({Literal});\nSELECT {Result-Col-List} FROM {Table-Name}",
  "feature_tag": "generated_column_unique",
  "weight": 3.0,
  "notes": "GENERATED ALWAYS AS (...) UNIQUE is the feature"
}
```

`GENERATED ALWAYS AS`, `UNIQUE` kept literal. Column names and the
generated expression abstracted to diversify the downstream fuzzing.

---

## Patterns across examples

- Keep **feature-naming keywords** literal (`WITHOUT ROWID`, `COLLATE NOCASE`,
  `OVER`, `PARTITION BY`, `ON CONFLICT`, `GENERATED ALWAYS AS`).
- Abstract **identifiers** always (names, aliases).
- Abstract **scalar values** always (use `{Boundary-*}` variants to
  emphasize overflow/boundary attacks where the bug's flavor calls for it).
- When the bug is about structural depth, prefer a single `{Deep-Expr}`
  or `{Deep-Nested-Select}` over trying to replicate the tree.
- Trust the non-terminals that exist. If a specific non-terminal for your
  feature is in the whitelist (`{Cte-Def}`, `{Frame-Spec}`, `{Deep-Expr}`,
  etc.), use it. If one doesn't exist (e.g., no `{Fts-Highlight}` or
  `{Index-Name}`), keep the relevant tokens literal.
