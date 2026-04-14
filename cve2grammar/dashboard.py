"""Emit a single-file HTML dashboard for browsing Manuel Rigger DBMS bugs.

The output is a self-contained HTML document with all bug data embedded as
JSON inside a <script type="application/json"> tag. Vanilla JS + CSS in the
same file implements three filter-charts (DBMS / oracle / monthly date
histogram) over a filterable table. Opens directly from the filesystem —
no server, no CDN, no network at view time.

JSON-in-script-tag safety: the serialized payload has `</` replaced with
`<\\/` before embedding, so literal `</script>` substrings inside bug data
cannot terminate the script tag. Client-side rendering uses `textContent`
only, never `innerHTML`. These two rules together keep the output safe
against arbitrary bug content.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

from cve2grammar.config import SUPPORTED_DBMS
from cve2grammar.models import Bug

_SOURCE_URL = "https://www.manuelrigger.at/dbms-bugs/"

# Ordered for UI display: crash first (memory-safety priority), then hang,
# error, logic oracles, empty-oracle bucket last. Pinned independently of
# config.ORACLE_WEIGHTS because the dashboard is about display order, not
# grammar-sampling weights.
_ORACLE_ORDER: tuple[str, ...] = (
    "crash", "hang", "error", "PQS", "NoREC", "TLP", "",
)

_SECTION_ORDER: tuple[str, ...] = ("fixed", "confirmed", "open", "closed")


def _bug_to_dict(bug: Bug) -> dict:
    """Transform a Bug into the JSON-serializable dict used by the dashboard JS."""
    return {
        "id": bug.id,
        "dbms": bug.dbms,
        "section": bug.section,
        "number": bug.number,
        "title": bug.title,
        "oracle": bug.oracle,
        "status": bug.status,
        "date": bug.date_found,
        "month": bug.date_found[:7] if bug.date_found else "",
        "sql": bug.sql,
        "links": {
            "bugtracker": bug.bugtracker_url,
            "email": bug.email_url,
            "fix": bug.fix_url,
        },
    }


def _build_payload(bugs: list[Bug]) -> dict:
    """Build the full JSON-serializable payload embedded in the HTML."""
    sorted_bugs = sorted(bugs, key=lambda b: (b.section, b.number))
    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": _SOURCE_URL,
        "facets": {
            "dbms": list(SUPPORTED_DBMS),
            "oracles": list(_ORACLE_ORDER),
            "sections": list(_SECTION_ORDER),
        },
        "bugs": [_bug_to_dict(b) for b in sorted_bugs],
    }


def _serialize_payload(payload: dict) -> str:
    """Serialize payload to JSON safe to embed inside <script type="application/json">.

    Two rules, both non-negotiable:

    1. ``ensure_ascii=True`` — every non-ASCII character is \\uXXXX-escaped,
       neutralizing Unicode attack surface and keeping the output portable
       across any viewer encoding.
    2. ``</`` → ``<\\/`` — prevents literal ``</script>`` substrings in bug
       data from terminating the embedding tag. This is the standard
       mitigation for JSON-in-script-tag injection.
    """
    raw = json.dumps(payload, ensure_ascii=True, separators=(",", ":"))
    return raw.replace("</", "<\\/")
