# Grammar Engine

Grammar loading, tree generation, and static weighted sampling via the PyO3 bridge.

> Last updated: 2026-05-14. Function names refer to code in the repository at the time of writing.

---

## 1. Grammar Loading (Step 1)

At startup, `main()` in `fuzzer/src/main.rs` calls
`python_grammar_loader::load_python_grammar(&grammar_path)`. This function:

1. Acquires the Python GIL via `pyo3::prepare_freethreaded_python()`.
2. Executes the grammar `.py` file inside a local namespace containing a
   `PyContext` object.
3. Returns a populated `Context` (from `grammartec/src/context.rs`).

The `PyContext` exposes three methods to the Python grammar:

| Method | Rust call | Rule variant produced |
|--------|-----------|----------------------|
| `ctx.rule(nt, format, weight=1.0)` | `Context::add_rule_weighted()` | `Rule::Plain` |
| `ctx.script(nt, nts, script, weight=1.0)` | `Context::add_script_weighted()` | `Rule::Script` |
| `ctx.regex(nt, regex, weight=1.0)` | `Context::add_regex_weighted()` | `Rule::RegExp` |

Each call appends a `Rule` variant to `Context.rules` and registers it in
`Context.nts_to_rules`, indexed by non-terminal name.

---

## 2. Thread Initialization (Step 2)

`main()` clones the `Context` for each fuzzing thread and spawns `N` threads
(`config.number_of_threads`) calling `fuzzing_thread()`. A `GlobalSharedState`
and `ChunkStoreWrapper` are shared across all threads via `Arc<Mutex<>>`.

Each thread owns its own `Context` clone. Weights are set at grammar load time
and remain static for the duration of the campaign.

---

## 3. Input Generation (Step 3)

When the queue is empty, each thread calls `state.generate_random("START")`,
which calls `Context::generate_tree_from_nt()` starting from the `"START"`
non-terminal.

Tree generation is recursive: for each non-terminal slot in a rule,
`Context::get_random_rule_for_nt()` performs weighted random selection (see
Section 5) and calls `Rule::generate()` to expand the subtree.

The result is a `Tree` — a flat array of `RuleIDOrCustom` values with parallel
`sizes` and `paren` arrays. The tree is serialized to bytes by
`tree.unparse_to_vec(ctx)` before being passed to the fork server.

---

## 4. Grammar Weight System

### Rule weight storage

Each `Rule` variant (`Plain`, `Script`, `RegExp`) carries a `weight: f32`
field defined in `grammartec/src/rule.rs`. The default weight is `1.0`.
`Context::add_rule_weighted()` sets this field before pushing the rule into
`Context.rules`.

### Weighted random selection

`Context::get_random_rule_for_nt()` delegates to
`dumb_get_random_rule_for_nt()`. For a given non-terminal and maximum tree
depth, this:

1. Collects applicable rules (those whose `rules_to_min_size` fits within the
   remaining depth budget).
2. Computes `total_weight` as the sum of all applicable rules' weights.
3. Samples a threshold uniformly in `[0, total_weight)`.
4. Walks the rules list subtracting each weight until the threshold goes
   non-positive.

This is a linear-scan weighted sampling algorithm — O(k) where k is the number
of applicable rules for the non-terminal.

### PyO3 bridge

`fuzzer/src/python_grammar_loader.rs` defines `PyContext`, a `#[pyclass]`
wrapper around `Context`. The `rule()` `#[pymethod]` accepts an optional
`weight: Option<f32>` argument and calls `ctx.add_rule_weighted()`. This is
the sole interface between Python grammar files and the Rust engine.

Grammar files set initial weights at definition time:

```python
# grammars/active/sqlite_v3.py
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Stress-Query}", weight=3.0)
ctx.rule("Sql-Stmt", "{Schema-Setup};\n{Insert-Stmt};\n{Stress-Query}", weight=2.5)
```

These weights are static — set once at load time and fixed for the campaign.

---

## 5. Grammar Files

The active grammar is `grammars/active/sqlite_v3.py`. Legacy grammars are
preserved under `grammars/legacy/` for reference.

| File | Purpose |
|------|---------|
| `grammars/active/sqlite_v3.py` | Current production grammar: `START`, `Sql-Stmt`, `Schema-Setup`, weighted attack patterns |
| `grammars/legacy/sqlite_patterns.py` | Base non-terminals used by the cve2grammar pipeline |
| `grammars/legacy/sqlite_attack.py` | Earlier attack-focused grammar (superseded by v3) |

The composed grammar loaded by the fuzzer must be self-contained: every
non-terminal referenced on a rule RHS must be defined in the same file.
`scripts/build_grammar.sh` handles composition when using the cve2grammar
pipeline output.

---

## 6. CVE-to-Grammar Pipeline

`cve2grammar/` converts known CVE-triggering SQL into generalized grammar rules
via four stages: scraping (manuelrigger.py), generalization (render.py),
validation (validate.py — 7-invariant gate), and emission (emitter.py →
`ctx.rule()` calls). The output is composed with the base grammar by
`scripts/build_grammar.sh`. See `docs/architecture.md §7` for the full
pipeline diagram.
