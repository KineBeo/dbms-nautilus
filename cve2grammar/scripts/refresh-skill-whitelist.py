#!/usr/bin/env python3
"""Regenerate the WHITELIST-SNAPSHOT block in .claude/skills/generalize-sql/SKILL.md.

Reads the live non-terminal whitelist from rl-nautilus/grammars/sqlite_patterns_v2.py
(via cve2grammar.generalizer.nonterminals.load_whitelist) and rewrites the block
between the markers:

    <!-- WHITELIST-SNAPSHOT:BEGIN ... -->
    ...
    <!-- WHITELIST-SNAPSHOT:END -->

Also scans examples.md for references to names not in the live whitelist and
prints warnings to stderr. Exit code 1 if the marker block is missing; 0
otherwise (stale-name warnings are non-fatal so the script can be run from a
pre-commit hook without blocking).

Usage:
    python3 scripts/refresh-skill-whitelist.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = REPO_ROOT / ".claude" / "skills" / "generalize-sql" / "SKILL.md"
EXAMPLES_PATH = REPO_ROOT / ".claude" / "skills" / "generalize-sql" / "examples.md"

BEGIN_MARKER = "<!-- WHITELIST-SNAPSHOT:BEGIN"
END_MARKER = "<!-- WHITELIST-SNAPSHOT:END -->"

_BUCKETS: list[tuple[str, tuple[str, ...]]] = [
    ("Names", ("Table-Name", "Col-Name", "Col-Alias", "Col-Ref")),
    ("Col definitions", ("Col-Def", "Col-Def-List", "Col-Name-List", "Type-Name")),
    (
        "Statements",
        (
            "Create-Table-Stmt", "Create-Index-Stmt", "Create-Trigger-Stmt",
            "Create-View-Stmt", "Create-Virtual-Table-Stmt", "Insert-Stmt",
            "Update-Stmt", "Delete-Stmt", "Select-Stmt", "Select-Core",
            "Sql-Stmt", "Sql-Stmt-List",
        ),
    ),
    (
        "Result / clauses",
        (
            "Result-Col", "Result-Col-List", "From-Clause", "Where-Clause",
            "Group-By-Clause", "Order-By-Clause", "Ordering-Term", "Asc-Desc",
            "Limit-Clause", "Window-Clause", "With-Clause",
        ),
    ),
    (
        "Joins",
        ("Join-Clause", "Join-Operator", "Join-Constraint", "Table-Or-Subquery", "Long-Join-Chain"),
    ),
    ("Compounds", ("Compound-Op", "Compound-Op-Set")),
    (
        "Expressions",
        (
            "Expr", "Expr-List", "Deep-Expr", "Deep-Expr-L2", "Bin-Op",
            "Literal", "Int-Literal", "Float-Literal", "Str-Literal",
            "Blob-Literal", "Signed-Number", "Boundary-Int", "Boundary-Float",
            "Boundary-Func-Call",
        ),
    ),
    ("Functions", ("Func-Call", "Agg-Func", "Filter-Clause")),
    (
        "Window",
        (
            "Frame-Spec", "Over-Clause", "Win-Frame", "Win-Func-Expr",
            "Win-Name", "Win-Order", "Win-Partition", "Window-Agg-Expr",
            "Window-Defn", "Window-Func-Complex",
        ),
    ),
    (
        "CTE / nested",
        ("Cte-Def", "Cte-List", "Recursive-CTE-Heavy", "Deep-Nested-Select"),
    ),
    (
        "Trigger / JSON / pragma",
        (
            "Trigger-Body", "Json-Deep", "Json-Obj", "Json-Path", "Pragma-Stmt",
            "Pragma-Bool", "Format-Spec", "Printf-Fmt-Spec", "Journal-Mode",
            "Sync-Mode", "Wal-Mode", "Gen-Storage", "GenCol-Expr",
        ),
    ),
]

_NAME_RE = re.compile(r"\{([A-Z][A-Za-z0-9-]*)\}")
_TEMPLATE_FIELD_RE = re.compile(r'"template"\s*:\s*"((?:[^"\\]|\\.)*)"')


def _load_whitelist() -> list[str]:
    sys.path.insert(0, str(REPO_ROOT))
    from cve2grammar.generalizer.nonterminals import load_whitelist
    return load_whitelist()


def _render_snapshot(whitelist: set[str]) -> str:
    lines = ["Representative non-terminals you will commonly use:", ""]
    for heading, names in _BUCKETS:
        present = [n for n in names if n in whitelist]
        if not present:
            continue
        if heading == "Compounds":
            entry = "- **Compounds**: Compound-Op (`UNION`, `INTERSECT`, `EXCEPT`)"
            if "Compound-Op-Set" in present:
                entry += ", Compound-Op-Set"
            lines.append(entry)
        else:
            lines.append(f"- **{heading}**: " + ", ".join(present))
    lines.append("")
    lines.append(
        "**Names with no non-terminal** (use a literal identifier): "
        "Index-Name, View-Name, Trigger-Name, Savepoint names."
    )
    lines.append(
        "**Operators with no non-terminal** (use literal): "
        "comparison operators (`=`, `<`, `>`, etc.), "
        "collation names (`NOCASE`, `BINARY`, `RTRIM`)."
    )
    lines.append(
        "**FTS features**: no dedicated `Fts-*` non-terminals — "
        "keep `MATCH`, `snippet(...)`, `highlight(...)`, and "
        "`USING fts4(...)` literal."
    )
    lines.append("")
    lines.append("Do not rely on this snapshot — the prompt's whitelist is authoritative.")
    return "\n".join(lines)


def _rewrite_skill(skill_text: str, snapshot: str) -> str:
    begin = skill_text.find(BEGIN_MARKER)
    end = skill_text.find(END_MARKER)
    if begin == -1 or end == -1 or end < begin:
        raise SystemExit(
            f"marker block not found in {SKILL_PATH}; "
            f"expected {BEGIN_MARKER}...{END_MARKER}"
        )
    begin_line_end = skill_text.find("\n", begin)
    head = skill_text[: begin_line_end + 1]
    tail = skill_text[end:]
    return head + snapshot + "\n" + tail


def _check_examples(whitelist: set[str]) -> list[str]:
    """Return stale non-terminals that appear inside JSON "template" fields.

    Prose mentions like "no `{Foo}` non-terminal exists" are ignored — only
    names the agent would paste into a rewrite are flagged.
    """
    if not EXAMPLES_PATH.exists():
        return []
    text = EXAMPLES_PATH.read_text(encoding="utf-8")
    names: set[str] = set()
    for template_body in _TEMPLATE_FIELD_RE.findall(text):
        names.update(_NAME_RE.findall(template_body))
    return sorted(n for n in names if n not in whitelist)


def main() -> int:
    whitelist_list = _load_whitelist()
    whitelist = set(whitelist_list)
    print(f"loaded {len(whitelist)} non-terminals from live grammar", file=sys.stderr)

    snapshot = _render_snapshot(whitelist)
    skill_text = SKILL_PATH.read_text(encoding="utf-8")
    new_text = _rewrite_skill(skill_text, snapshot)
    if new_text != skill_text:
        SKILL_PATH.write_text(new_text, encoding="utf-8")
        print(f"updated {SKILL_PATH.relative_to(REPO_ROOT)}", file=sys.stderr)
    else:
        print(f"{SKILL_PATH.relative_to(REPO_ROOT)} already up to date", file=sys.stderr)

    stale = _check_examples(whitelist)
    if stale:
        print(
            f"WARNING: {EXAMPLES_PATH.relative_to(REPO_ROOT)} references "
            f"{len(stale)} non-terminal(s) not in the live whitelist: "
            + ", ".join(stale),
            file=sys.stderr,
        )
        print(
            "  examples.md requires manual rewrite — auto-generation would lose "
            "the worked semantics.",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
