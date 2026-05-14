# CVE-to-Grammar Pipeline

Converts known CVE-triggering SQL into generalized grammar rules via a
four-stage pipeline: scraping, generalization, validation, and emission.

`cve2grammar/` is a vendored Python subtree with its own `pyproject.toml` and
test suite. Run tests from inside: `cd cve2grammar/ && python3 -m pytest`.

---

## Pipeline Diagram

```mermaid
flowchart TD
    A["CVE bug reports\nManuel Rigger's DBMS bug DB"] -->|scraper/manuelrigger.py| B
    B["Bug records\ncve2grammar/models.py Bug dataclass"] -->|LLM generalization prompt| C
    C["Template payload JSON\ntemplate · feature_tag · weight · notes"] -->|validate_template()| D
    D["Validation\ncve2grammar/generalizer/validate.py\n7 invariant checks"] -->|render_grammar()| E
    E["Generated Python grammar\nctx.rule('Sql-Stmt', template, weight=w)"] -->|scripts/build_grammar.sh| F
    F["Composed grammar\nbase grammar + generated rules\nsingle self-contained .py"] -->|load_python_grammar()| G
    G["Context\ngrammartec/src/context.rs\nweighted rule table"]
```

---

## Stage 1 — Scraping

`cve2grammar/scraper/manuelrigger.py` fetches bug reports from Manuel Rigger's
DBMS bug database. Each bug is parsed into a `Bug` datamodel
(`cve2grammar/models.py`) with fields: `id`, `title`, `sql`, `oracle`,
`status`.

---

## Stage 2 — Generalization

`cve2grammar/generalizer/render.py` exposes `render_grammar(entries)`, which
takes a list of cache payloads (each with `template`, `feature_tag`, `weight`,
`notes`, `status`) and renders them into a complete Python grammar source file.

The generalization step replaces literal SQL values (table names, column names,
literal integers) with non-terminal references from the whitelist. The whitelist
is extracted from the base grammar by
`cve2grammar/generalizer/nonterminals.py:load_whitelist()`, which uses two
regexes:

- `_LHS_RE` — finds `ctx.rule("Name", ...)` or `ctx.regex("Name", ...)` calls.
- `_RHS_RE` — finds `{Name}` references in rule bodies.

The default grammar path resolves to `<repo>/grammars/sqlite_patterns.py`
(via `_DEFAULT_GRAMMAR_PATH` in `nonterminals.py`, lines 28–31).

---

## Stage 3 — Validation

`cve2grammar/generalizer/validate.py:validate_template(payload, whitelist)`
enforces seven invariants before a template can be emitted:

1. Required keys present: `template`, `feature_tag`, `weight`, `notes`.
2. `template` is a `str`.
3. `feature_tag` matches `^[a-z][a-z0-9_]{2,39}$`.
4. `weight` is a real number in `[0.5, 5.0]`.
5. Every `{Name}` reference in `template` appears in the whitelist.
6. No trailing semicolons (the grammar wrapper adds them).
7. `notes` is a non-empty string.

Any invariant failure raises a `ValidationError` with a descriptive message.
Templates that fail validation are not emitted; they remain in the cache with
`status: "invalid"`.

---

## Stage 4 — Emission

`cve2grammar/emitter.py:emit_nautilus(bugs, dbms)` and
`cve2grammar/generalizer/render.py:render_grammar(entries)` convert validated
payloads into `ctx.rule()` calls:

```python
# Example output from render_grammar() / emit_nautilus()
# === overlong_string_printf (2 bugs: sqlite-3.31.1-b1, sqlite-3.31.1-b2) ===
ctx.rule("Sql-Stmt", "SELECT printf('%.*c', {Boundary-Int}, 'x')", weight=2.0)
```

The output file is composed with the base grammar by `scripts/build_grammar.sh`
before being loaded by the fuzzer. The composed grammar must be self-contained:
all non-terminals referenced on the RHS must be defined somewhere in the
combined file.

### Known limitation — generated grammar is not self-contained

`grammars/sqlite_generated.py` defines only `Sql-Stmt` and references 24 base
non-terminals (`Table-Name`, `Col-Def`, `GenCol-Expr`, …) that live in
`grammars/sqlite_patterns.py`. Nautilus loads one grammar per run, so the
generated file panics with `Broken Grammar` if loaded alone.

`scripts/build_grammar.sh` must prepend `sqlite_patterns.py` to the rendered
output to produce a self-contained `.py` file that the fuzzer can load directly.

---

## File Reference

| File | Role |
|------|------|
| `cve2grammar/cve2grammar/emitter.py` | `emit_nautilus()` — Bug → `ctx.rule()` calls |
| `cve2grammar/cve2grammar/generalizer/render.py` | `render_grammar()` — cache entries → grammar source |
| `cve2grammar/cve2grammar/generalizer/validate.py` | `validate_template()` — 7-invariant gate |
| `cve2grammar/cve2grammar/generalizer/nonterminals.py` | `load_whitelist()` — extract NT names from grammar |
| `cve2grammar/scraper/manuelrigger.py` | Scraper — fetch bug reports from Manuel Rigger's DB |
| `cve2grammar/models.py` | `Bug` dataclass — `id`, `title`, `sql`, `oracle`, `status` |
| `scripts/build_grammar.sh` | Compose base + generated grammar into one self-contained `.py` |
| `grammars/sqlite_patterns.py` | Base grammar — provides all shared non-terminal definitions |
| `grammars/sqlite_generated.py` | Generated output — `Sql-Stmt` rules from CVE templates |
