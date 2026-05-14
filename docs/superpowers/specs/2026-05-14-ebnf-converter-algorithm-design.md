# Spec: EBNF-to-Nautilus Converter Algorithm

**Date:** 2026-05-14
**Status:** Approved

## Problem

Current `scripts/ebnf_to_nautilus.py` is a hardcoded template emitter, not a real algorithm. An advisor would ask "what algorithm did you use?" and the answer would be "copy-paste." Need a proper EBNF parser + CFG flattener that reads the `.ebnf` file and produces the `.py` grammar automatically.

## Algorithm

Standard EBNF-to-CFG flattening (Aho et al., Compilers, 2nd ed., §4.2):

```
A?     → ε | A                    (optional: 2 alternatives)
A*     → ε | A | A A              (Kleene star: capped at depth 2)
A+     → A | A A                  (Kleene plus: capped at depth 2)
(A|B)  → separate rule per alt    (alternation: enumerate)
A B    → cartesian product        (sequence: combine all expansions)
```

## Architecture

3-stage pipeline, clean separation of concerns:

1. **EBNF Parser** — reads `.ebnf`, produces AST per production
2. **CFG Flattener** — walks AST, expands optionals/repeats into flat CFG rules
3. **Nautilus Emitter** — maps CFG rules to `ctx.rule()` using domain config

## Stage 1: EBNF Parser

Parse tree-sitter EBNF format. AST node types:

```python
@dataclass
class Literal:     text: str
class NonTerminal: name: str
class Optional:    inner: Element
class Repeat:      inner: Element      # A* (0+)
class RepeatOne:   inner: Element      # A+ (1+)
class Group:       alternatives: list  # (A | B | C)
class Sequence:    elements: list      # A B C
```

Productions detected by `name ::=` pattern. Keywords (ALL_CAPS names) auto-detected and skipped.

## Stage 2: CFG Flattener

Input: dict of `{name: AST}`. Output: list of `(nt_name, [token_list])`.

Core function `flatten(element) -> list[list[str]]` returns all possible expansions:

- `Literal("X")` → `[["X"]]`
- `NonTerminal("foo")` → `[["{Foo}"]]`
- `Optional(A)` → `flatten(A) + [[]]`
- `Repeat(A)` → `[[]] + flatten(A) + [a+a for a in flatten(A)]` (cap=2)
- `Group([a,b])` → `flatten(a) + flatten(b)`
- `Sequence([a,b])` → cartesian product of `flatten(a) × flatten(b)`

Combinatorial explosion guard: cap total expansions per production at 64.

## Stage 3: Nautilus Emitter

Config file `scripts/sqlite_harness.json`:

```json
{
  "schema": {
    "_name": {"type": "fixed", "values": ["t1", "t2", "t3"]},
    "function_name": {"type": "enum", "values": ["count", "sum", "avg", ...]},
    "collation_name": {"type": "enum", "values": ["NOCASE", "BINARY", "RTRIM"]},
    "identifier": {"type": "regex", "pattern": "[a-z][a-z0-9_]*"}
  },
  "skip": ["_whitespace", "_word", "comment", "_string", "bind_parameter"],
  "nt_rename": {"_expr": "Expr", "_select_core": "Select-Core", ...},
  "repeat_depth": 2,
  "max_expansions": 64
}
```

Name conversion: `snake_case` → `Kebab-Case` (with leading `_` stripped).

## Verification

```bash
python3 scripts/ebnf_to_nautilus.py docs/tree-sitter-sqlite.ebnf -c scripts/sqlite_harness.json -o grammars/sqlite-ebnf-auto.py
python3 scripts/ebnf_to_nautilus.py --diff grammars/sqlite-ebnf-auto.py grammars/sqlite-ebnf.py
```

Grammar must: load in Nautilus, zero dangling refs, zero weights, generate valid SQL.
