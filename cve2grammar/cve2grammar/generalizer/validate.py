"""Validate an agent-produced template payload against the hard invariants.

The validator is the ground truth for what ships into the generated grammar
file. The skill's rules make violations rare; this validator makes them
impossible to ship.

Seven checks, each a separate failure mode with a distinct error message
so the slash command can feed the stderr back into a retry prompt.
"""

from __future__ import annotations

import json
import re
import sys
from numbers import Real

from cve2grammar.generalizer.nonterminals import load_whitelist


class ValidationError(Exception):
    """Raised when a template payload fails validation."""


_REQUIRED_KEYS: tuple[str, ...] = ("template", "feature_tag", "weight", "notes")
_FEATURE_TAG_RE = re.compile(r"^[a-z][a-z0-9_]{2,39}$")
_NONTERMINAL_RE = re.compile(r"\{([A-Z][A-Za-z0-9-]*)\}")
_TRAILING_TERMINATOR_RE = re.compile(r";\s*\Z")
_MIN_WEIGHT = 0.5
_MAX_WEIGHT = 5.0


def validate_template(payload: dict, whitelist: set[str]) -> None:
    """Verify that ``payload`` is safe to render into a grammar rule.

    Args:
        payload: The agent's JSON response, parsed to a dict.
        whitelist: The set of allowed non-terminal names.

    Raises:
        ValidationError: If any invariant is violated. The message is
            machine-parseable — the slash command feeds it into a retry
            prompt verbatim.
    """
    for key in _REQUIRED_KEYS:
        if key not in payload:
            raise ValidationError(f"missing required key: {key}")

    template = payload["template"]
    feature_tag = payload["feature_tag"]
    weight = payload["weight"]
    notes = payload["notes"]

    if not isinstance(template, str):
        raise ValidationError("template must be str")
    if not isinstance(feature_tag, str):
        raise ValidationError("feature_tag must be str")
    # bool is a subclass of int — exclude it explicitly so True/False aren't accepted.
    if not isinstance(weight, Real) or isinstance(weight, bool):
        raise ValidationError("weight must be a number")
    if not isinstance(notes, str):
        raise ValidationError("notes must be str")

    if not _FEATURE_TAG_RE.match(feature_tag):
        raise ValidationError(
            f"feature_tag {feature_tag!r} must match ^[a-z][a-z0-9_]{{2,39}}$",
        )

    if not (_MIN_WEIGHT <= weight <= _MAX_WEIGHT):
        raise ValidationError(
            f"weight {weight} out of allowed range [{_MIN_WEIGHT}, {_MAX_WEIGHT}]",
        )

    if not template.strip():
        raise ValidationError("template is empty or whitespace-only")

    if _TRAILING_TERMINATOR_RE.search(template):
        raise ValidationError(
            "template has trailing `;` — the Sql-Stmt-List wrapper adds the terminator",
        )

    # Whitelist check — bail on the first unknown so the retry prompt can focus.
    for match in _NONTERMINAL_RE.finditer(template):
        name = match.group(1)
        if name not in whitelist:
            raise ValidationError(f"unknown non-terminal: {{{name}}}")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Reads JSON from stdin, validates, exits 0 on success.

    Usage:
        python3 -m cve2grammar.generalizer.validate <<< '<payload_json>'

    Exit codes:
        0 — payload is valid, no output
        1 — payload is invalid; one-line reason on stderr
    """
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"malformed json: {e}", file=sys.stderr)
        return 1

    try:
        whitelist = set(load_whitelist())
    except FileNotFoundError as e:
        print(f"grammar file not found: {e.filename}", file=sys.stderr)
        return 1

    try:
        validate_template(payload, whitelist)
    except ValidationError as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
