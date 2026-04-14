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

from cve2grammar.models import Bug


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
