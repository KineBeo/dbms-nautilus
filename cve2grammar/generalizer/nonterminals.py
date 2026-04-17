"""Extract the non-terminal whitelist from the rl-nautilus grammar file.

A non-terminal is any symbol of the form ``{Capitalized-Name}`` that the
Nautilus grammar parser recognizes. We collect them from two places:

1. LHS of rule definitions — ``ctx.rule("Name", ...)`` or ``ctx.regex("Name", ...)``.
2. RHS references — any ``{Name}`` substring whose first character is uppercase.

The union is the whitelist. We include RHS-only names because they may be
defined in a sibling grammar file that this one imports or expects to be
loaded alongside.

The extractor is a two-regex text-level parse, deliberately NOT an AST
parse — robust to minor syntax drift and stdlib-only.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

_LHS_RE = re.compile(r"""ctx\.(?:rule|regex)\(\s*["']([A-Z][A-Za-z0-9-]*)["']""")
_RHS_RE = re.compile(r"\{([A-Z][A-Za-z0-9-]*)\}")

_DEFAULT_GRAMMAR_PATH = (
    Path(__file__).resolve().parent.parent.parent.parent
    / "rl-nautilus" / "grammars" / "sqlite_patterns_v2.py"
)


def _resolve_path(path: Path | None) -> Path:
    """Pick the grammar path to read: explicit arg > env var > hardcoded default."""
    if path is not None:
        return path
    env = os.environ.get("RL_NAUTILUS_GRAMMAR")
    if env:
        return Path(env)
    return _DEFAULT_GRAMMAR_PATH


def load_whitelist(path: Path | None = None) -> list[str]:
    """Return the sorted list of non-terminals found in the grammar file.

    Args:
        path: Explicit grammar file to parse. If ``None``, uses the
            ``RL_NAUTILUS_GRAMMAR`` env var or the hardcoded default at
            ``<repo>/../rl-nautilus/grammars/sqlite_patterns_v2.py``.

    Raises:
        FileNotFoundError: The resolved path does not exist.

    Returns:
        A sorted list of distinct non-terminal names. Empty list if the
        grammar file has no rules.
    """
    grammar_path = _resolve_path(path)
    source = grammar_path.read_text(encoding="utf-8")
    names = set(_LHS_RE.findall(source)) | set(_RHS_RE.findall(source))
    return sorted(names)
