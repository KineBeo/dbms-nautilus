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


_DASHBOARD_JS = r"""
<script>
(function () {
  "use strict";
  var payload = window.__PAYLOAD__;
  var bugs = payload.bugs;
  var DBMS = payload.facets.dbms;
  var ORACLES = payload.facets.oracles;

  // Filter state — single source of truth.
  var state = {
    dbms: null,
    oracles: new Set(["crash"]),
    dateRange: null,
    search: "",
    sortBy: "id",
    sortDir: "asc",
    expandedId: null
  };

  // Pre-compute all months present in dataset, sorted.
  var MONTHS = (function () {
    var set = new Set();
    bugs.forEach(function (b) { if (b.month) set.add(b.month); });
    return Array.from(set).sort();
  })();

  // --- Filtering -----------------------------------------------------------

  function matchesExcept(b, skip) {
    if (skip !== "dbms" && state.dbms && b.dbms !== state.dbms) return false;
    if (skip !== "oracle" && state.oracles.size > 0 && !state.oracles.has(b.oracle)) return false;
    if (skip !== "date" && state.dateRange) {
      if (!b.month) return false;
      if (b.month < state.dateRange.start || b.month > state.dateRange.end) return false;
    }
    if (state.search) {
      var q = state.search.toLowerCase();
      if (
        b.id.toLowerCase().indexOf(q) === -1 &&
        b.title.toLowerCase().indexOf(q) === -1 &&
        b.sql.toLowerCase().indexOf(q) === -1
      ) return false;
    }
    return true;
  }

  function visibleBugs() { return bugs.filter(function (b) { return matchesExcept(b, null); }); }
  function forDbmsCounts() { return bugs.filter(function (b) { return matchesExcept(b, "dbms"); }); }
  function forOracleCounts() { return bugs.filter(function (b) { return matchesExcept(b, "oracle"); }); }
  function forDateCounts() { return bugs.filter(function (b) { return matchesExcept(b, "date"); }); }

  // --- Rendering helpers ---------------------------------------------------

  function el(tag, attrs, text) {
    var node = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "onclick") node.onclick = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    if (text != null) node.textContent = text;
    return node;
  }

  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }

  // --- Chart: DBMS ---------------------------------------------------------

  function renderDbmsChart() {
    var container = document.getElementById("chart-dbms");
    clear(container);
    var counted = forDbmsCounts();
    var counts = {};
    DBMS.forEach(function (d) { counts[d] = 0; });
    counted.forEach(function (b) { if (counts[b.dbms] != null) counts[b.dbms]++; });
    var max = Math.max.apply(null, Object.values(counts).concat([1]));
    // Sort descending by count.
    var ordered = DBMS.slice().sort(function (a, b) { return counts[b] - counts[a]; });
    ordered.forEach(function (d) {
      var row = el("div", { class: "bar-row" + (state.dbms === d ? " selected" : "") + (counts[d] === 0 ? " inactive" : "") });
      row.appendChild(el("div", { class: "bar-label" }, d));
      var track = el("div", { class: "bar-track" });
      var fill = el("div", { class: "bar-fill" });
      fill.style.width = (counts[d] / max * 100) + "%";
      track.appendChild(fill);
      row.appendChild(track);
      row.appendChild(el("div", { class: "bar-count" }, String(counts[d])));
      row.onclick = function () { state.dbms = (state.dbms === d ? null : d); renderAll(); };
      container.appendChild(row);
    });
  }

  // --- Chart: Oracle -------------------------------------------------------

  function renderOracleChart() {
    var container = document.getElementById("chart-oracle");
    clear(container);
    var hint = document.getElementById("oracle-hint");
    if (state.oracles.size > 0) hint.textContent = "· " + Array.from(state.oracles).join(", ") + " selected";
    else hint.textContent = "";
    var counted = forOracleCounts();
    var counts = {};
    ORACLES.forEach(function (o) { counts[o] = 0; });
    counted.forEach(function (b) {
      var key = (b.oracle == null ? "" : b.oracle);
      if (counts[key] != null) counts[key]++;
    });
    var max = Math.max.apply(null, Object.values(counts).concat([1]));
    ORACLES.forEach(function (o) {
      var label = o === "" ? "(none)" : o;
      var selected = state.oracles.has(o);
      var row = el("div", { class: "bar-row" + (selected ? " selected" : "") + (counts[o] === 0 ? " inactive" : "") });
      row.appendChild(el("div", { class: "bar-label" }, label));
      var track = el("div", { class: "bar-track" });
      var fill = el("div", { class: "bar-fill" });
      fill.style.width = (counts[o] / max * 100) + "%";
      track.appendChild(fill);
      row.appendChild(track);
      row.appendChild(el("div", { class: "bar-count" }, String(counts[o])));
      row.onclick = function () {
        if (state.oracles.has(o)) state.oracles.delete(o);
        else state.oracles.add(o);
        renderAll();
      };
      container.appendChild(row);
    });
  }

  // --- Chart: Date histogram ----------------------------------------------

  var histDragState = null; // {startIdx, endIdx}

  function renderHistogram() {
    var container = document.getElementById("chart-histogram");
    clear(container);
    var counted = forDateCounts();
    var counts = {};
    MONTHS.forEach(function (m) { counts[m] = 0; });
    counted.forEach(function (b) {
      if (b.month && counts[b.month] != null) counts[b.month]++;
    });
    var max = Math.max.apply(null, Object.values(counts).concat([1]));
    MONTHS.forEach(function (m) {
      var bar = el("div", { class: "hbar" });
      bar.style.height = (counts[m] / max * 100) + "%";
      bar.title = m + ": " + counts[m];
      bar.dataset.month = m;
      if (state.dateRange && m >= state.dateRange.start && m <= state.dateRange.end) {
        bar.classList.add("in-range");
      }
      container.appendChild(bar);
    });
    // Render axis: first year of each year transition.
    var axis = document.getElementById("histogram-axis");
    clear(axis);
    var years = new Set();
    MONTHS.forEach(function (m) { years.add(m.slice(0, 4)); });
    Array.from(years).sort().forEach(function (y) {
      axis.appendChild(el("span", null, y));
    });

    // Drag handlers.
    container.onmousedown = function (e) {
      if (!e.target.classList.contains("hbar")) return;
      histDragState = { startIdx: MONTHS.indexOf(e.target.dataset.month), endIdx: -1 };
      e.preventDefault();
    };
    container.onmousemove = function (e) {
      if (!histDragState || !e.target.classList.contains("hbar")) return;
      histDragState.endIdx = MONTHS.indexOf(e.target.dataset.month);
    };
    container.onmouseup = function (e) {
      if (!histDragState) return;
      var endIdx = histDragState.endIdx;
      var startIdx = histDragState.startIdx;
      if (endIdx === -1 || endIdx === startIdx) {
        // Click without drag → clear filter.
        state.dateRange = null;
      } else {
        var lo = Math.min(startIdx, endIdx);
        var hi = Math.max(startIdx, endIdx);
        state.dateRange = { start: MONTHS[lo], end: MONTHS[hi] };
      }
      histDragState = null;
      renderAll();
    };
    container.onmouseleave = function () { histDragState = null; };
  }

  // --- Active filter pills --------------------------------------------------

  function renderPills() {
    var pills = document.getElementById("pills");
    clear(pills);
    if (state.dbms) {
      var p = el("div", { class: "pill" }, "dbms: " + state.dbms + " ×");
      p.onclick = function () { state.dbms = null; renderAll(); };
      pills.appendChild(p);
    }
    state.oracles.forEach(function (o) {
      var p = el("div", { class: "pill" }, "oracle: " + (o || "(none)") + " ×");
      p.onclick = function () { state.oracles.delete(o); renderAll(); };
      pills.appendChild(p);
    });
    if (state.dateRange) {
      var p2 = el("div", { class: "pill" }, "date: " + state.dateRange.start + "—" + state.dateRange.end + " ×");
      p2.onclick = function () { state.dateRange = null; renderAll(); };
      pills.appendChild(p2);
    }
    if (state.search) {
      var p3 = el("div", { class: "pill" }, 'search: "' + state.search + '" ×');
      p3.onclick = function () { state.search = ""; document.getElementById("search").value = ""; renderAll(); };
      pills.appendChild(p3);
    }
  }

  // --- Table ----------------------------------------------------------------

  var COLUMNS = [
    { key: "id", label: "ID", cls: "col-id" },
    { key: "dbms", label: "DBMS", cls: "" },
    { key: "section", label: "Section", cls: "" },
    { key: "oracle", label: "Oracle", cls: "" },
    { key: "status", label: "Status", cls: "" },
    { key: "date", label: "Date", cls: "" },
    { key: "title", label: "Title", cls: "col-title" }
  ];

  function sortVisible(rows) {
    var k = state.sortBy;
    var dir = state.sortDir === "asc" ? 1 : -1;
    return rows.slice().sort(function (a, b) {
      var av = a[k] == null ? "" : String(a[k]);
      var bv = b[k] == null ? "" : String(b[k]);
      if (av < bv) return -1 * dir;
      if (av > bv) return 1 * dir;
      return 0;
    });
  }

  function renderTable() {
    var container = document.getElementById("table");
    clear(container);
    // Header.
    var head = el("div", { class: "tr head" });
    COLUMNS.forEach(function (c) {
      var cls = "col";
      if (c.key === state.sortBy) cls += " sorted" + (state.sortDir === "desc" ? " desc" : "");
      var th = el("div", { class: cls }, c.label);
      th.onclick = function () {
        if (state.sortBy === c.key) {
          state.sortDir = state.sortDir === "asc" ? "desc" : "asc";
        } else {
          state.sortBy = c.key;
          state.sortDir = "asc";
        }
        renderAll();
      };
      head.appendChild(th);
    });
    container.appendChild(head);

    var rows = sortVisible(visibleBugs());
    if (rows.length === 0) {
      container.appendChild(el("div", { class: "empty" }, "No bugs match these filters."));
      return;
    }

    rows.forEach(function (b) {
      var tr = el("div", { class: "tr" + (state.expandedId === b.id ? " expanded" : "") });
      COLUMNS.forEach(function (c) {
        var val = b[c.key];
        var cls = c.cls;
        if (c.key === "oracle" && b.oracle === "crash") cls += " col-oracle crash";
        var cell = el("div", { class: cls }, val == null ? "" : String(val));
        tr.appendChild(cell);
      });
      tr.onclick = function () {
        state.expandedId = (state.expandedId === b.id ? null : b.id);
        renderAll();
      };
      container.appendChild(tr);

      if (state.expandedId === b.id) {
        var detail = el("div", { class: "detail" });
        var dh = el("div", { class: "detail-head" });
        dh.appendChild(el("div", { class: "detail-label" }, "Test case · " + b.id));
        var copyBtn = el("button", { class: "btn" }, "📋 Copy SQL");
        copyBtn.onclick = function (e) {
          e.stopPropagation();
          navigator.clipboard.writeText(b.sql).then(
            function () { copyBtn.textContent = "✓ Copied"; setTimeout(function () { copyBtn.textContent = "📋 Copy SQL"; }, 1200); },
            function () { copyBtn.textContent = "⚠ Failed"; }
          );
        };
        dh.appendChild(copyBtn);
        detail.appendChild(dh);
        var pre = el("pre");
        pre.textContent = b.sql;
        detail.appendChild(pre);
        var linksDiv = el("div", { class: "links" });
        ["bugtracker", "email", "fix"].forEach(function (k) {
          var url = b.links[k];
          if (!url) return;
          var a = el("a", { href: url, target: "_blank", rel: "noopener" }, k);
          linksDiv.appendChild(a);
        });
        detail.appendChild(linksDiv);
        // stop expanding row click from collapsing when clicking inside detail
        detail.onclick = function (e) { e.stopPropagation(); };
        container.appendChild(detail);
      }
    });
  }

  // --- Top bar --------------------------------------------------------------

  function renderMeta() {
    var meta = document.getElementById("meta");
    var total = bugs.length;
    var visible = visibleBugs().length;
    meta.textContent = total + " bugs · " + DBMS.length + " DBMS · generated " + payload.generated;
    var count = document.getElementById("count");
    clear(count);
    count.appendChild(document.createTextNode("Showing "));
    var strong = el("b", null, String(visible));
    count.appendChild(strong);
    count.appendChild(document.createTextNode(" of " + total + " bugs"));
  }

  // --- Full re-render -------------------------------------------------------

  function renderAll() {
    renderDbmsChart();
    renderOracleChart();
    renderHistogram();
    renderPills();
    renderTable();
    renderMeta();
  }

  // --- Wiring ---------------------------------------------------------------

  var searchInput = document.getElementById("search");
  var searchTimer = null;
  searchInput.oninput = function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      state.search = searchInput.value;
      renderAll();
    }, 100);
  };

  document.getElementById("reset").onclick = function () {
    state.dbms = null;
    state.oracles = new Set();
    state.dateRange = null;
    state.search = "";
    state.sortBy = "id";
    state.sortDir = "asc";
    state.expandedId = null;
    searchInput.value = "";
    renderAll();
  };

  renderAll();
})();
</script>
"""
