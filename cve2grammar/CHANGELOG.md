# Changelog

All notable changes to this project are documented here. Dates are ISO-8601
and follow the commit dates on `main` / `feat/grammar-generalizer`.

## [Unreleased] — `feat/grammar-generalizer`

### Added
- **Grammar generalizer subsystem** (`cve2grammar/generalizer/`) — LLM-driven
  rewriter that converts crash-oracle POC SQL into feature-scoped Nautilus
  grammar templates using non-terminals from the live rl-nautilus grammar.
  - `nonterminals.py` — whitelist extractor (two-regex parse of
    `ctx.rule/regex` LHS plus `{Name}` RHS references) with CLI entry point
  - `validate.py` — 7-rule invariant check (required keys, types,
    `feature_tag` regex, weight range `[0.5, 5.0]`, non-empty, no trailing
    `;`, whitelist membership) exposed as a stdin CLI with
    `ValidationError` surfaced as machine-parseable stderr
  - `cache.py` — content-addressed disk cache keyed by `sha256(sql)[:16]`,
    atomic writes via `<key>.tmp` sidecars + `os.replace`, `PROMPT_VERSION`
    constant for invalidation without file deletion
  - `render.py` — deterministic grammar file rendering (OK entries sorted
    alphabetically by feature tag, bugs sorted by id within groups,
    fallback block emitted last)
- **CLI subcommand** `generalize-candidates` — emits crash-oracle (or
  other) bugs as JSON on stdout for the slash command to consume
- **Claude Code integration**
  - `.claude/agents/sql-generalizer.md` — subagent persona with `tools: []`
  - `.claude/skills/generalize-sql/SKILL.md` — 8 numbered rules for rewriting
    (feature-scoped, whitelist-only, literal keywords allowed, abstract
    identifiers, preserve order, multi-statement `;\n` separator with no
    trailing terminator, `feature_tag` regex, weight range)
  - `.claude/skills/generalize-sql/examples.md` — 8 worked rewrites
  - `.claude/commands/generalize.md` — `/generalize` slash command
    orchestrating fetch → whitelist → filter → per-bug (cache get →
    dispatch → validate → retry → cache put) → render → report
- **`scripts/refresh-skill-whitelist.py`** — auto-generates the
  WHITELIST-SNAPSHOT block in SKILL.md from the live
  `rl-nautilus/grammars/sqlite_patterns_v2.py` and warns non-fatally on
  stale names in `examples.md` `"template"` JSON fields
- **`README.md`** and **`CHANGELOG.md`** — project documentation
- **`AGENTS.md`** — GitNexus-generated agent usage guide

### Fixed
- Skill whitelist drift — replaced 10 non-terminals that did not exist in
  the live rl-nautilus grammar (`Literal-Value`, `Compare-Op`, `Index-Name`,
  `View-Name`, `Trigger-Name`, `Collation`, `Having-Clause`, `Boundary-Str`,
  `Fts-Query`, `Fts-Highlight`) with real equivalents (`Literal`,
  `Str-Literal`) or literal tokens. Smoke-test run on bugs MR-SQLITE-0022,
  -0055, -0093 now produces valid templates on the first try (no fallbacks).

### Changed
- `.gitignore` narrowed: `.claude/settings.local.json` only (skills,
  agents, slash commands remain tracked); added `generated/`,
  `cache/generalizer/*.tmp`, and `.claude/skills/gitnexus/` (installed
  per-user by the GitNexus CLI)

### Repository stats at time of merge
- 196 tests passing
- 21 commits on `feat/grammar-generalizer` ahead of `main`
- 3 cache entries committed from the smoke test

## [0.1.0] — 2026-04-15

### Added
- **Bug triage dashboard** (`cve2grammar/dashboard.py`) — `dashboard`
  subcommand emits a single self-contained HTML file across all DBMS with
  facet filters and per-bug table rows. `__DASHBOARD_JS__` slot pattern
  keeps JS separate from the Python source string
- `_bug_to_dict` payload builder and `_build_payload` with facets
- `_serialize_payload` with `</script>` escape for safe HTML embedding
- Oracle facets now derived from data (handles TLP variants correctly)

## [0.0.1] — 2026-04-14

### Added
- Initial scrape-and-emit pipeline
  - `scraper/manuelrigger.py` — DOM-position-stateful scraper walking
    `h2`/`h3`/`li` tags in document order; state tracked via
    `current_section` and `current_dbms`
  - `emitter.py` — `emit_nautilus(bugs, dbms)` returning a Python source
    string with no imports and no function wrapper (runs as flat module
    body against injected `ctx`)
  - `models.py::Bug` — frozen dataclass DTO with `id`, `dbms`, `section`,
    `number`, `title`, `sql`, `oracle`, `status`, `date_found`,
    `bugtracker_url`, `email_url`, `fix_url`
  - `config.py` — `ORACLE_WEIGHTS` (`crash=3.0`, `hang=2.5`, logic
    oracles=`2.0`, unknown=`1.5`), `SUPPORTED_DBMS`, `SUPPORTED_SECTIONS`
  - `cli.py::main` — argparse dispatch, `fetch` subcommand with
    `--dbms`, `--section`, `--output`, `--html`
- Test suite under `tests/` with hand-curated `fixtures/sample_page.html`
  (7 bugs across 3 DBMS, 2 sections) — no network, offline-reproducible
- `pyproject.toml` — Python 3.10+, `requests`, `beautifulsoup4`; dev:
  `pytest`, `pytest-cov`, `ruff`
