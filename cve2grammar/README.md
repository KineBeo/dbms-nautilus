# cve2grammar

Scrape Manuel Rigger's [DBMS bugs page](https://www.manuelrigger.at/dbms-bugs/)
and emit a **Nautilus-compatible Python grammar file** that biases the fuzzer
toward high-value test cases. Optionally rewrite each bug's POC SQL into a
feature-scoped grammar template via an LLM-driven pipeline.

Downstream consumer: the sibling `rl-nautilus` project, whose grammar loader
calls `ctx.rule("Sql-Stmt", <sql>, weight=<w>)` once per bug.

## What it does

Three subcommands, all scrape the same curated bug list:

| Subcommand | Output | Use |
|---|---|---|
| `fetch` | `<name>.py` grammar file | Drop into `rl-nautilus/grammars/` |
| `dashboard` | `<name>.html` self-contained triage UI | Human review of bug corpus |
| `generalize-candidates` | JSON to stdout | Feeds the `/generalize` pipeline |

Plus a Claude Code `/generalize` slash command that turns crash-oracle POC
SQL into feature-scoped grammar templates using non-terminals from the live
rl-nautilus grammar. See [Grammar generalizer](#grammar-generalizer) below.

## Install

```bash
pip install -e '.[dev]'
```

Python 3.10+. Runtime deps: `requests`, `beautifulsoup4`. Dev deps: `pytest`,
`pytest-cov`, `ruff`.

## Usage

```bash
# Scrape + emit SQLite grammar
cve2grammar fetch --dbms sqlite -o sqlite_grammar.py

# Use a pre-downloaded HTML file (offline / reproducible)
cve2grammar fetch --dbms sqlite --html page.html -o sqlite_grammar.py

# Different section (default is "fixed")
cve2grammar fetch --dbms postgresql --section all -o pg_grammar.py

# HTML dashboard for bug triage (all DBMS)
cve2grammar dashboard -o dashboard.html

# JSON candidates for the generalizer pipeline
python3 -m cve2grammar generalize-candidates --oracle crash
```

Supported DBMS: `sqlite`, `postgresql`, `mysql`, `mariadb`, `cockroachdb`,
`tidb`, `duckdb`, `tdengine`, `h2`. Supported sections: `fixed` (default),
`confirmed`, `open`, `closed`, `all`.

## Pipeline flow

Strict linear dataflow; each module has one concern.

```
CLI (cli.py)
  ↓ argparse → dispatch subcommand
scraper/manuelrigger.py :: fetch(html|URL) → list[Bug]
  ↓ filter by --dbms + --section
emitter.py :: emit_nautilus(bugs, dbms) → Python source string
  ↓ write to --output
```

### Key design rules

- **`Bug` (models.py) is the only DTO** — frozen dataclass. The scraper
  constructs it; the emitter consumes it. Adding a field means touching
  both ends plus tests.
- **The scraper is DOM-position-stateful.** It walks `h2`/`h3`/`li` tags in
  document order and tracks `current_section` + `current_dbms` as state.
  Unknown headings are silently skipped, so adding a new DBMS requires
  updating `DBMS_HEADINGS` *and* `SUPPORTED_DBMS` in `config.py`.
- **Oracle weights drive sampling.** `ORACLE_WEIGHTS` in `config.py` maps
  oracle labels (`crash=3.0`, `hang=2.5`, logic oracles=`2.0`, unknown
  defaults to `1.5`) — calibrated to slot alongside rl-nautilus's existing
  CVE stress templates (weights 2.0–3.5) without overwhelming them.
- **Output grammar has no imports and no function wrapper** — it runs as a
  flat module body against an injected `ctx` object.
- **Don't rename `"Sql-Stmt"`** — it must match the base SQLite grammar in
  `rl-nautilus/grammars/sqlite.py`.
- **Tests never hit the network.** `tests/fixtures/sample_page.html` is a
  hand-curated subset (7 bugs across 3 DBMS, 2 sections); integration tests
  use `fetch(html=...)`.

## Grammar generalizer

Rewrites each crash-oracle bug's POC SQL into a *feature-scoped grammar
template* so the fuzzer mutates a family of SQL rather than replaying the
original POC verbatim.

Subsystem lives in `cve2grammar/generalizer/`:

| Module | Role |
|---|---|
| `nonterminals.py` | Extract the live non-terminal whitelist from `rl-nautilus/grammars/sqlite_patterns_v2.py` |
| `validate.py` | 7-rule invariant check on each LLM-produced template (required keys, types, feature-tag regex, weight range, whitelist membership, non-empty, no trailing `;`) |
| `cache.py` | Content-addressed disk cache keyed by `sha256(sql)[:16]` with atomic writes |
| `render.py` | Deterministic grammar file rendering (sorted by feature tag; fallbacks last) |

Orchestrated by the `/generalize` Claude Code slash command
(`.claude/commands/generalize.md`), which dispatches the `sql-generalizer`
subagent per bug, validates via stdin, retries once on failure, falls back
to literal SQL on second failure, and renders via the `render` CLI.

Cache entries live in `cache/generalizer/<sha16>.json` and are committed to
the repo for cross-run reproducibility.

### Keeping the skill whitelist in sync

The skill file at `.claude/skills/generalize-sql/SKILL.md` contains a
reference snapshot of non-terminals between BEGIN/END markers.
`scripts/refresh-skill-whitelist.py` regenerates the snapshot from the live
rl-nautilus grammar and warns (non-fatally) if `examples.md` references
non-terminals that no longer exist in `"template"` JSON fields.

## Testing

```bash
pytest                                              # full suite
pytest tests/test_emitter.py                        # single file
pytest tests/test_emitter.py::TestWeights           # single class
pytest -k "escape"                                  # by keyword
pytest --cov=cve2grammar --cov-report=term-missing  # with coverage
```

196 tests at time of writing. Tests use `pytest.fixture`, `tmp_path`, and
`monkeypatch` — no network, no subprocess except CLI smoke tests.

## Lint

```bash
ruff check .
```

Line length 100, targets py310.

## Repository layout

```
cve2grammar/
├── cli.py              — argparse dispatch: fetch / dashboard / generalize-candidates
├── config.py           — ORACLE_WEIGHTS, SUPPORTED_DBMS, SUPPORTED_SECTIONS
├── models.py           — Bug dataclass (the only DTO)
├── scraper/
│   └── manuelrigger.py — DOM-position-stateful scraper
├── emitter.py          — bugs → Nautilus grammar source
├── dashboard.py        — bugs → self-contained HTML
└── generalizer/        — LLM-driven bug-SQL → template pipeline
tests/
├── fixtures/sample_page.html  — offline fixture
└── test_*.py                  — 8 test modules
scripts/
└── refresh-skill-whitelist.py — auto-generator for the skill snapshot
.claude/
├── agents/sql-generalizer.md  — subagent persona
├── commands/generalize.md     — /generalize slash command
└── skills/generalize-sql/     — rules + worked examples
cache/generalizer/             — committed cache entries for reproducibility
```

## License

Unspecified (see repository root).
