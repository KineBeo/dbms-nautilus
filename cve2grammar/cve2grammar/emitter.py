"""Emit a Nautilus-compatible Python grammar file from a list of Bug records.

The output file is a sequence of `ctx.rule("Sql-Stmt", <sql>, weight=<w>)` calls
that the rl-nautilus python_grammar_loader can ingest.
"""

from __future__ import annotations

from datetime import datetime, timezone

from cve2grammar.config import DEFAULT_WEIGHT, ORACLE_WEIGHTS
from cve2grammar.models import Bug


def emit_nautilus(bugs: list[Bug], dbms: str) -> str:
    """Render the given bugs as a Nautilus grammar Python source file.

    Args:
        bugs: Bug records to emit. Order is preserved by (section, number).
        dbms: DBMS slug for the header (e.g. "sqlite").

    Returns:
        A complete .py file body, ending in a newline.
    """
    sorted_bugs = sorted(bugs, key=lambda b: (b.section, b.number))

    lines: list[str] = [_header(dbms, len(sorted_bugs))]
    if not sorted_bugs:
        lines.append("# No bugs to emit.")
        return "\n".join(lines) + "\n"

    for bug in sorted_bugs:
        lines.append("")
        lines.extend(_emit_bug(bug))

    return "\n".join(lines) + "\n"


def _header(dbms: str, count: int) -> str:
    """Top-of-file comment block."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return (
        f"# Auto-generated grammar for {dbms} — cve2grammar v0.2\n"
        f"# Source: Manuel Rigger DBMS bugs (https://www.manuelrigger.at/dbms-bugs/)\n"
        f"# Generated: {now}\n"
        f"# Bugs: {count}"
    )


def _emit_bug(bug: Bug) -> list[str]:
    """Emit one bug as a comment header followed by a single ctx.rule() call."""
    weight = ORACLE_WEIGHTS.get(bug.oracle, DEFAULT_WEIGHT)
    label = bug.oracle or "unspecified"
    status = bug.status or "unknown"
    return [
        f"# === {bug.id} ({label}, {status}) ===",
        f"# {bug.title}",
        _emit_rule(bug.sql, weight),
    ]


def _emit_rule(sql: str, weight: float) -> str:
    """Format the SQL as a ctx.rule(...) Python call.

    Multi-line SQL uses a triple-quoted string. Single-line SQL uses a regular
    double-quoted string. Backslashes and triple quotes inside the SQL are
    escaped.
    """
    if "\n" in sql:
        # Triple-quoted: only need to escape \\ and any literal triple-quote.
        escaped = sql.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
        return f'ctx.rule("Sql-Stmt", """{escaped}""", weight={weight})'

    escaped = sql.replace("\\", "\\\\").replace('"', '\\"')
    return f'ctx.rule("Sql-Stmt", "{escaped}", weight={weight})'
