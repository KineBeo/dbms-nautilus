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


_HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>cve2grammar — Manuel Rigger DBMS bugs</title>
<style>
:root {
  --bg: #0a0a0a;
  --panel: #141414;
  --panel2: #1a1a1a;
  --border: #2a2a2a;
  --fg: #ddd;
  --fg-dim: #888;
  --fg-label: #ccc;
  --accent: #4a9eff;
  --crash: #ff6b4a;
}
* { box-sizing: border-box; }
body { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; background: var(--bg); color: var(--fg); margin: 0; font-size: 12px; }

.topbar { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; border-bottom: 1px solid var(--border); background: #0f0f0f; }
.topbar h1 { margin: 0; font-size: 14px; font-weight: 600; }
.topbar .meta { font-size: 11px; color: var(--fg-dim); margin-top: 2px; }
.topbar-right { display: flex; gap: 8px; align-items: center; }
.search { background: var(--panel); border: 1px solid var(--border); color: var(--fg); padding: 6px 10px; font-family: inherit; font-size: 12px; width: 260px; }
.btn { background: var(--panel); border: 1px solid var(--border); color: var(--fg); padding: 6px 10px; font-family: inherit; font-size: 11px; cursor: pointer; }
.btn:hover { background: var(--panel2); }

.charts { display: grid; grid-template-columns: 1fr 1fr 2fr; gap: 16px; padding: 16px 20px; border-bottom: 1px solid var(--border); background: var(--panel); }
.chart { min-width: 0; }
.chart .label { text-transform: uppercase; font-size: 10px; letter-spacing: 0.5px; color: var(--fg-label); margin-bottom: 8px; }
.chart .label .hint { text-transform: none; color: var(--fg-dim); font-weight: normal; margin-left: 4px; }
.bar-row { display: flex; align-items: center; gap: 8px; font-size: 11px; margin-bottom: 3px; cursor: pointer; }
.bar-row.inactive { color: var(--fg-dim); }
.bar-row .bar-label { width: 80px; text-align: right; color: var(--fg-label); flex-shrink: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.bar-row .bar-track { flex: 1; background: var(--panel2); height: 14px; position: relative; }
.bar-row .bar-fill { background: var(--accent); height: 100%; width: 0%; }
.bar-row.selected .bar-label { color: var(--crash); font-weight: 600; }
.bar-row.selected .bar-fill { background: var(--crash); }
.bar-row .bar-count { width: 36px; text-align: right; color: var(--fg-dim); flex-shrink: 0; }

.histogram { display: flex; align-items: flex-end; gap: 2px; height: 110px; background: var(--panel2); padding: 8px; position: relative; user-select: none; }
.histogram .hbar { flex: 1; background: #3a3a3a; min-width: 4px; }
.histogram .hbar.in-range { background: var(--crash); }
.histogram .hbar.selected { background: var(--accent); }
.histogram-axis { display: flex; justify-content: space-between; font-size: 10px; color: var(--fg-dim); margin-top: 4px; padding: 0 8px; }

.active-filters { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; font-size: 11px; color: var(--fg-dim); border-bottom: 1px solid var(--border); }
.active-filters .count b { color: var(--crash); }
.pills { display: flex; gap: 4px; flex-wrap: wrap; }
.pill { padding: 2px 10px; background: var(--crash); color: #0a0a0a; border-radius: 10px; font-weight: 600; cursor: pointer; }

.table-wrap { padding: 0 20px 20px; }
.table { background: var(--panel); border: 1px solid var(--border); font-size: 11px; }
.tr { display: grid; grid-template-columns: 130px 90px 80px 70px 70px 90px 1fr; gap: 8px; padding: 8px 12px; border-bottom: 1px solid #222; cursor: pointer; align-items: center; }
.tr.head { background: var(--panel2); font-weight: 600; color: var(--fg-label); cursor: pointer; }
.tr.head .col { user-select: none; }
.tr.head .col.sorted::after { content: " ↑"; color: var(--accent); }
.tr.head .col.sorted.desc::after { content: " ↓"; color: var(--accent); }
.tr:hover:not(.head) { background: #181818; }
.tr.expanded { background: #1e1e1e; }
.tr .col-id { color: var(--accent); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.tr .col-oracle.crash { color: var(--crash); }
.tr .col-title { color: #ddd; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.detail { background: var(--panel2); padding: 12px 20px 16px; border-bottom: 1px solid #222; }
.detail-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.detail-label { font-size: 10px; color: var(--fg-dim); text-transform: uppercase; letter-spacing: 0.5px; }
.detail pre { background: #0a0a0a; color: #bdd; padding: 10px; font-size: 11px; margin: 0; border: 1px solid var(--border); white-space: pre-wrap; max-height: 400px; overflow: auto; }
.detail .links { margin-top: 8px; display: flex; gap: 12px; font-size: 11px; }
.detail .links a { color: var(--accent); text-decoration: none; }
.detail .links a:hover { text-decoration: underline; }
.empty { text-align: center; padding: 40px; color: var(--fg-dim); }
</style>
</head>
<body>
<div class="topbar">
  <div>
    <h1>Manuel Rigger DBMS Bugs</h1>
    <div class="meta" id="meta"></div>
  </div>
  <div class="topbar-right">
    <input class="search" id="search" placeholder="search title / id / sql...">
    <button class="btn" id="reset">Reset filters</button>
  </div>
</div>

<div class="charts">
  <div class="chart"><div class="label">DBMS</div><div id="chart-dbms"></div></div>
  <div class="chart"><div class="label">Oracle <span class="hint" id="oracle-hint"></span></div><div id="chart-oracle"></div></div>
  <div class="chart">
    <div class="label">Date found (monthly) <span class="hint">· drag to select range</span></div>
    <div class="histogram" id="chart-histogram"></div>
    <div class="histogram-axis" id="histogram-axis"></div>
  </div>
</div>

<div class="active-filters">
  <div class="count" id="count"></div>
  <div class="pills" id="pills"></div>
</div>

<div class="table-wrap">
  <div class="table" id="table"></div>
</div>

<script id="bugs-data" type="application/json">__BUGS_DATA_JSON__</script>
<script>
(function () {
  "use strict";
  var raw = document.getElementById("bugs-data").textContent;
  window.__PAYLOAD__ = JSON.parse(raw);
  // Real UI logic is attached in a separate script block below.
})();
</script>
__DASHBOARD_JS__
</body>
</html>
"""


def emit_dashboard(bugs: list[Bug]) -> str:
    """Render the given bugs as a self-contained HTML dashboard document.

    Args:
        bugs: Bug records to display. Order is preserved by (section, number)
            during serialization.

    Returns:
        A complete HTML document (``<!doctype html>...``) ready to write to a
        ``.html`` file. No external resources are referenced; the file opens
        correctly from the local filesystem.
    """
    payload = _build_payload(bugs)
    serialized = _serialize_payload(payload)
    html = _HTML_TEMPLATE.replace("__BUGS_DATA_JSON__", serialized)
    html = html.replace("__DASHBOARD_JS__", _DASHBOARD_JS)
    return html


_DASHBOARD_JS = ""  # Populated in Task 6.
