---
name: generalize-sql
description: |
  Rules for rewriting a bug-triggering SQL test case into a feature-scoped
  Nautilus grammar template using whitelisted non-terminals. Invoked by the
  sql-generalizer agent during the /generalize slash command.
---

# Generalize SQL Bug → Nautilus Grammar Template

## Goal

Transform a **specific bug's SQL test case** into a **family of SQL** that
exercises the same DBMS feature. The fuzzer will then mutate this family
to explore the neighborhood of the bug, rather than just replaying the
original POC.

Two bugs hitting the same feature should converge to the same template
(shared `feature_tag`). Unique bugs get unique templates.

## Rules

### 1. Feature-scoped, not bug-specific

- **DO** preserve the feature that triggered the bug:
  FTS4 snippet, COLLATE NOCASE on WITHOUT ROWID, printf precision,
  window function with frame spec, recursive CTE, etc.
- **DON'T** copy all literals verbatim.
- **DON'T** abstract so hard the feature vanishes
  (e.g. collapsing to `SELECT {Expr}` loses the bug signal).

### 2. Use only whitelisted non-terminals

Any `{Name}` token in your output must be in the whitelist provided in
the prompt. If no non-terminal fits, use a literal keyword.

Do NOT invent non-terminals like `{Special-Bug-Thing}`. The validator
will reject them and your output will be retried.

### 3. Literal keywords are fine — and often necessary

SQL keywords that name the feature stay literal:

- `WITHOUT ROWID` → stays literal (removing it changes the feature)
- `PRIMARY KEY` → stays literal
- `COLLATE NOCASE` → stays literal IF NOCASE is the bug's feature
- `COLLATE {Collation}` → use non-terminal if the bug is about any collation

**Rule of thumb:** when in doubt, keep the keyword literal. Too-specific
is recoverable (the fuzzer still produces interesting variants on the
`{Non-Terminal}` slots); too-abstract is not.

### 4. Abstract identifiers and scalar values

| Bug content | Replace with |
|---|---|
| Table names (`test`, `t0`, `v1`) | `{Table-Name}` |
| Column names (`c0`, `x`) | `{Col-Name}` |
| Index names (`idx`, `index_0`) | `{Index-Name}` |
| Scalar values (`'hello'`, `42`) | `{Literal-Value}`, `{Boundary-Int}`, `{Boundary-Str}`, `{Boundary-Float}` |
| Expressions (`a + b`, `NULL`) | `{Expr}` |
| Comparisons (`=`, `<`) | `{Compare-Op}` |
| Binary operators (`+`, `*`) | `{Bin-Op}` |
| Column-definition lists (`(c0, c1, c2)`) | `({Col-Def-List})` |
| Result column lists (`*`, `a, b`) | `{Result-Col-List}` |

Consult the whitelist in the prompt for the full set.

### 5. Preserve statement order and count

If the bug has 4 statements (CREATE, CREATE INDEX, INSERT, SELECT), emit
4 statements. Order matters — do not shuffle DDL / DML / DQL.

Strip SQL comments (`-- explanation`). They are not part of the grammar.

### 6. Multi-statement formatting

- Between statements: `;\n` — a semicolon then a newline.
- After the FINAL statement: NO trailing `;`, NO trailing newline.

The rl-nautilus `Sql-Stmt-List` wrapper adds the outer terminator after
your template. If you add one, the validator will reject your output.

Example correct multi-statement template:

```
CREATE TABLE {Table-Name} ({Col-Def-List}) WITHOUT ROWID;\nCREATE INDEX {Index-Name} ON {Table-Name}({Col-Name} COLLATE NOCASE);\nSELECT * FROM {Table-Name}
```

(In JSON the `\n` appears as the two-character sequence `\\n`.)

### 7. `feature_tag`

Short, stable, `^[a-z][a-z0-9_]{2,39}$` — 3 to 40 chars, lowercase + digits
+ underscore, leading letter. Examples:

- `collate_nocase_without_rowid`
- `printf_precision_overflow`
- `fts4_snippet`
- `window_func_partition_by`
- `recursive_cte_heavy`

Bugs with the same tag collapse to one `ctx.rule` in the generated file.

### 8. `weight`

Default 3.0 for crash bugs (matches `sqlite_patterns_v2.py`'s pattern
weights). Lower to 2.5 ONLY if the template is so generic it would
overwhelm the base grammar; in that case put the rationale in `notes`.

Range: [0.5, 5.0] (validator-enforced).

## Output

Return EXACTLY one JSON object. No prose, no markdown fences:

```json
{
  "template": "<the rewritten SQL>",
  "feature_tag": "<short_snake_case>",
  "weight": 3.0,
  "notes": "<one-line rationale>"
}
```

## Allowed non-terminals — reference snapshot

The prompt provides the live whitelist (extracted at runtime from
`../rl-nautilus/grammars/sqlite_patterns_v2.py`). This list is a snapshot
for context. Always trust the prompt's list over this snapshot.

Representative non-terminals you will commonly use:

- **Names**: Table-Name, Col-Name, Index-Name, Col-Alias, View-Name, Trigger-Name
- **Col definitions**: Col-Def, Col-Def-List, Type-Name, Collation
- **Statements**: Create-Table-Stmt, Create-Index-Stmt, Insert-Stmt, Select-Stmt, Select-Core
- **Result / clauses**: Result-Col-List, From-Clause, Where-Clause, Group-By-Clause, Having-Clause, Order-By-Clause, Limit-Clause, Window-Clause
- **Joins**: Join-Clause, Join-Operator, Join-Constraint, Table-Or-Subquery
- **Compounds**: Compound-Op (`UNION`, `INTERSECT`, `EXCEPT`)
- **Expressions**: Expr, Expr-List, Deep-Expr, Bin-Op, Compare-Op, Boundary-Int, Boundary-Float, Boundary-Str, Literal-Value
- **Functions**: Func-Call, Agg-Func, Filter-Clause, Frame-Spec
- **Specialized**: Fts-Query, Fts-Highlight, Cte-Def, Cte-List

Do not rely on this snapshot — the prompt's whitelist is authoritative.

## Examples

See `examples.md` in this directory for 8 worked rewrites with
explanations of both good and bad options.
