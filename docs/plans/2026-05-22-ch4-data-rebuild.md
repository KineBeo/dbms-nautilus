# Chapter 4 Data Pipeline Rebuild — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the entire Ch4 data extraction, statistics, and figure pipeline from raw workdirs so every number in the thesis is traceable to the correct source. Do NOT modify the thesis .tex structure — only fix data, scripts, and figures.

**Architecture:** Single Python script (`scripts/ch4_pipeline.py`) replaces the current fragmented pipeline (`compute_stats.py`, `consolidate_data.py`, `triage_rq1_v35.py`, `triage_rq2.py`, `generate_figures.py`). One script, one truth, one run. Each RQ reads ONLY from its designated workdirs.

**Tech Stack:** Python 3.13 (scipy, matplotlib, numpy), raw data in `workdirs/`

**Key decisions locked in this plan:**
- RQ1 reads from `workdirs/sqlite-{ver}_v35_run{1..5}/` (grammar v3.5 with boosted seeds)
- RQ2 reads from `workdirs/sqlite-{ver}_v33_run{1..5}/` (grammar v3.3, no seeds)
- RQ3 reads from `workdirs/sqlite-{ver}_comparison_v3.4_run{1..5}/` AND `workdirs/sqlite-{ver}_comparison_ebnf_run{1..5}/` (apples-to-apples comparison)
- EBNF 3.32.0 run1 is MISSING — all RQ3 EBNF 3.32.0 uses n=4, documented in thesis
- Outlier runs (v3.4 3.31.1 run1 queue=123, v3.4 3.32.0 run1 queue=77) are INCLUDED but flagged in output — the thesis discusses them in threats to validity
- Unique root causes = count of files in `dedup_test/` directory (NOT `triage_test.json` UBSan+ASan count)
- TTFC = first `timestamp_sec` where `total_crashes > 0` in `coverage.csv`
- Throughput = `exec_count / timestamp_sec` from last row of `coverage.csv`
- Edge coverage = `total_edges` from last row of `coverage.csv`
- All outputs go to `results/ch4_final/` (clean directory, no legacy data)

### RQ1 Presentation Decision: Only show confirmed successes

**Rationale:** The current Table 4.2 mixes successes, failures, exclusions, and footnoted edge cases. This confuses the reader and invites scrutiny on the weakest points.

**New approach:** RQ1 Table shows ONLY the CVEs that DBMS-Nautilus successfully rediscovered. If the grammar found 4 out of 5 detectable CVEs, the table shows those 4 with their success rates. The 5th (CVE-2020-9327, 0/5) and the excluded one (CVE-2019-19646, oracle limitation) are discussed in the **Limitations** section (4.6.3), not in the results table. This is honest — we state the denominator ("of 5 detectable CVEs, DBMS-Nautilus confirmed 4") and discuss failures where they belong.

**Table 4.2 new design:**
```
CVE              | Bug Type       | Version(s) | DBMS-Nautilus | EBNF-Baseline
CVE-2020-13434   | Int overflow   | 3 ver.     | 14/15         | 0/15
CVE-2020-13435   | Null ptr deref | 3.32.0     | 5/5           | 0/5
CVE-2020-13871   | Use-after-free | 3.32.2     | 4/5           | 4/5*
CVE-2020-15358   | Heap overflow  | 3.32.2     | 5/5           | 0/5
Total            |                |            | 4/4 CVEs      | 1/4 CVEs
```
*EBNF found 13871 on 3.30.1, not 3.32.2 — mention in prose.

CVE-2020-9327 (not found) and CVE-2019-19646 (excluded) go to Section 4.6.3 Limitations.

### Writing Order: Chapter 4 first, then abstract/conclusion

**Rule:** Do NOT update abstract or conclusion during Ch4 work. After Ch4 is finalized and all numbers verified, a SEPARATE pass updates abstract and conclusion to reflect the final results. This prevents the abstract promising numbers that the experiments don't deliver.

---

## Advisor Feedback (2026-05-22)

### Feedback 1: Every RQ must compare DBMS-Nautilus vs EBNF-Baseline

**Current state:** RQ1 and RQ2 only show DBMS-Nautilus results. Only RQ3 has a comparison.

**Required change:** Add EBNF-Baseline columns/data to RQ1 and RQ2 results.

**Data source for EBNF in RQ1/RQ2:** The EBNF comparison workdirs (`workdirs/sqlite-{ver}_comparison_ebnf_run{1..5}/`) ran with the same 4 versions and 5 runs. We extract CVE rediscovery and bug class data from these workdirs alongside the proposed grammar data.

**Impact on tables/figures:**
- Table 4.2 (CVE rediscovery): Add EBNF column showing how many CVEs the baseline found
- Table 4.3 (bug classes): Add column or separate row showing which bug classes EBNF found
- Table 4.4 (per-run classes): Add EBNF row
- Figure 4.1 (time to CVE): Add EBNF data points (if it found any CVEs)
- Figure 4.2 (bug breakdown): Add EBNF comparison or split bars

### Feedback 2: Terminology — only "DBMS-Nautilus" and "EBNF-Baseline"

**Rule:** The defender (thesis committee) should only see two names: "DBMS-Nautilus" and "EBNF-Baseline". No grammar version numbers (v3.3, v3.4, v3.5), no "structural-primitives grammar", no "compositional grammar". These are internal implementation details.

**Impact on .tex:** Replace all variant names:
- "structural-primitives grammar" → "DBMS-Nautilus"
- "compositional grammar" → "DBMS-Nautilus" (explain seed vs no-seed config in one sentence)
- "proposed grammar" → "DBMS-Nautilus"
- "seed-augmented grammar" → "DBMS-Nautilus"
- Consistent hyphenation: "EBNF-Baseline" everywhere (not "EBNF baseline", "EBNF grammar", etc.)

### Feedback 3: Captions and descriptions — shorter, less detail

**Rule (cherry-picked from content-quality-rules.md for Ch4):**
- Rule 6: Use figures/tables for structural info — don't repeat in prose what the table shows
- Rule 7: Avoid long comma-lists — group into categories or use tables
- Rule 8: Keep terminology consistent (see Feedback 2)
- Rule 10: After each paragraph, ask "would the reader know why this matters?"

**Impact on .tex:**
- Table captions: short label only (Ch3 style). Move all explanation to body text after `\ref{}`
- Figure captions: one-line description, no methodology details in caption
- Remove prose that restates what a table already shows (e.g., L160 listing per-version CVE counts already visible in Table 4.2)
- Footnotes on Table 4.2 (†, ‡): move to body text — footnotes in tables are hard to read

---

## Source → Output Map

```
workdirs/sqlite-{ver}_v35_run{N}/
  ├── coverage.csv          → RQ1 TTFC (Fig 4.1)
  ├── triage.json           → RQ1 CVE matching (Table 4.2, DBMS-Nautilus column)
  └── dedup_test/           → RQ1 unique root causes

workdirs/sqlite-{ver}_v33_run{N}/
  ├── triage.json           → RQ2 bug classes (Table 4.3 DBMS-Nautilus, Table 4.4, Fig 4.2)
  └── dedup_test/           → RQ2 unique hashes

workdirs/sqlite-{ver}_comparison_v3.4_run{N}/
  ├── coverage.csv          → RQ3 throughput, edges, TTFC (Table 4.5 DBMS-Nautilus, Figs 4.3-4.5)
  └── dedup_test/           → RQ3 unique root causes (Table 4.5 DBMS-Nautilus)

workdirs/sqlite-{ver}_comparison_ebnf_run{N}/
  ├── coverage.csv          → RQ1 EBNF TTFC, RQ3 throughput/edges/TTFC (Table 4.5 EBNF, Figs 4.3-4.5)
  ├── triage.json           → RQ1 EBNF CVE matching (Table 4.2 EBNF column)
  ├── triage.json           → RQ2 EBNF bug classes (Table 4.3 EBNF column, Table 4.4 EBNF row)
  └── dedup_test/           → RQ2 EBNF unique hashes, RQ3 EBNF unique root causes
```

**Outputs:**
```
results/ch4_final/
  ├── rq1_cve_hits.csv              → Table 4.2 (both DBMS-Nautilus AND EBNF columns)
  ├── rq1_ttfc_per_cve.csv          → Figure 4.1
  ├── rq2_bug_classes.csv           → Table 4.3 (DBMS-Nautilus classes)
  ├── rq2_ebnf_bug_classes.csv      → Table 4.3 (EBNF classes for comparison)
  ├── rq2_per_run_classes.csv       → Table 4.4 (both grammars)
  ├── rq3_per_campaign.csv          → Tables 4.5, 4.6
  ├── rq3_statistical_tests.csv     → Table 4.5 (p-values, Cliff's d)
  ├── rq3_summary.csv               → Table 4.6
  ├── manifest.json                 → Full provenance (git hash, workdir→output mapping)
  └── AUDIT.md                      → Human-readable verification report

docs/thesis/v2/figures/
  ├── fig_4_1_time_to_first_cve.pdf
  ├── fig_4_2_bug_class_breakdown.pdf
  ├── fig_4_3_coverage_growth.pdf
  ├── fig_4_4_throughput.pdf
  └── fig_4_5_time_to_first_crash.pdf
```

---

## Task 1: Create the pipeline script skeleton

**Files:**
- Create: `scripts/ch4_pipeline.py`

- [ ] **Step 1: Create the script with constants and CLI**

```python
#!/usr/bin/env python3
"""
Chapter 4 unified data pipeline.

Reads ONLY from raw workdirs. Produces all CSVs, figures, and an audit report.
Each RQ uses its own designated workdir set — no cross-contamination.

Usage:
    python3 scripts/ch4_pipeline.py                  # full run
    python3 scripts/ch4_pipeline.py --rq1            # RQ1 only
    python3 scripts/ch4_pipeline.py --rq2            # RQ2 only
    python3 scripts/ch4_pipeline.py --rq3            # RQ3 only
    python3 scripts/ch4_pipeline.py --figures-only   # regenerate figures from CSVs
    python3 scripts/ch4_pipeline.py --audit-only     # just print the audit report
"""
import argparse
import csv
import json
import os
import subprocess
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.stats import mannwhitneyu

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
WORKDIRS = ROOT / "workdirs"
OUT_DIR = ROOT / "results" / "ch4_final"
FIG_DIR = ROOT / "docs" / "thesis" / "v2" / "figures"

VERSIONS = ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
RUNS = [1, 2, 3, 4, 5]

# ── Workdir patterns (the ONLY source of truth) ─────────────────────────────
# RQ1: v3.5 grammar with boosted CVE seeds
RQ1_PATTERN = "sqlite-{ver}_v35_run{run}"
# RQ2: v3.3 grammar without seeds
RQ2_PATTERN = "sqlite-{ver}_v33_run{run}"
# RQ3: v3.4 (proposed) vs EBNF (baseline) — same-campaign comparison
RQ3_PROPOSED_PATTERN = "sqlite-{ver}_comparison_v3.4_run{run}"
RQ3_BASELINE_PATTERN = "sqlite-{ver}_comparison_ebnf_run{run}"

# ── Plot style ───────────────────────────────────────────────────────────────
COLOR_PROPOSED = "#2196F3"
COLOR_BASELINE = "#9E9E9E"
plt.rcParams.update({
    "font.family": "serif",
    "axes.spines.top": False,
    "axes.spines.right": False,
})
```

- [ ] **Step 2: Add metric extraction helpers**

These read one workdir and return one number. No aggregation — that happens at the RQ level.

```python
# ── Metric extraction (one workdir → one value) ─────────────────────────────

def get_throughput(wdir: Path) -> float | None:
    """exec_count / timestamp_sec from last row of coverage.csv."""
    cov = wdir / "coverage.csv"
    if not cov.exists():
        return None
    last = None
    with open(cov) as f:
        for row in csv.DictReader(f):
            last = row
    if last is None:
        return None
    t = int(last["timestamp_sec"])
    e = int(last["exec_count"])
    return e / t if t > 0 else None


def get_edges(wdir: Path) -> int | None:
    """total_edges from last row of coverage.csv."""
    cov = wdir / "coverage.csv"
    if not cov.exists():
        return None
    last = None
    with open(cov) as f:
        for row in csv.DictReader(f):
            last = row
    if last is None:
        return None
    return int(last["total_edges"])


def get_unique_rcs(wdir: Path) -> int | None:
    """Count of files in dedup_test/ directory."""
    dt = wdir / "dedup_test"
    if not dt.exists():
        return None
    return len(list(dt.iterdir()))


def get_ttfc(wdir: Path) -> int | None:
    """First timestamp_sec where total_crashes > 0 in coverage.csv."""
    cov = wdir / "coverage.csv"
    if not cov.exists():
        return None
    with open(cov) as f:
        for row in csv.DictReader(f):
            if int(row["total_crashes"]) > 0:
                return int(row["timestamp_sec"])
    return None


def get_queue_size(wdir: Path) -> int | None:
    """Count of files in outputs/ directory (fuzzer queue size)."""
    outputs = wdir / "outputs"
    if not outputs.exists():
        return None
    return len(list(outputs.iterdir()))


def get_coverage_timeseries(wdir: Path) -> list[tuple[int, int]] | None:
    """Return [(timestamp_sec, total_edges), ...] from coverage.csv."""
    cov = wdir / "coverage.csv"
    if not cov.exists():
        return None
    series = []
    with open(cov) as f:
        for row in csv.DictReader(f):
            series.append((int(row["timestamp_sec"]), int(row["total_edges"])))
    return series


def get_git_hash() -> str:
    """Current git commit hash."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"
```

- [ ] **Step 3: Add statistical test helpers**

```python
# ── Statistics ───────────────────────────────────────────────────────────────

def cliffs_delta(a: list[float], b: list[float]) -> float:
    n1, n2 = len(a), len(b)
    if n1 == 0 or n2 == 0:
        return float("nan")
    greater = sum(1 for x in a for y in b if x > y)
    less = sum(1 for x in a for y in b if x < y)
    return (greater - less) / (n1 * n2)


def effect_label(d: float) -> str:
    ad = abs(d)
    if ad >= 0.474:
        return "large"
    if ad >= 0.330:
        return "medium"
    if ad >= 0.147:
        return "small"
    return "negligible"


def mann_whitney(a: list[float], b: list[float]) -> tuple[float, float, float, str]:
    """Returns (U, p_value, cliffs_d, effect_label)."""
    if len(a) < 2 or len(b) < 2:
        return float("nan"), float("nan"), float("nan"), "N/A"
    u, p = mannwhitneyu(a, b, alternative="two-sided")
    d = cliffs_delta(a, b)
    return u, p, d, effect_label(d)
```

- [ ] **Step 4: Commit skeleton**

```bash
git add scripts/ch4_pipeline.py
git commit -m "feat: add ch4_pipeline.py skeleton with metric helpers"
```

---

## Task 2: Implement RQ1 data extraction

**Files:**
- Modify: `scripts/ch4_pipeline.py`

- [ ] **Step 1: Add RQ1 CVE signature matching**

```python
# ── RQ1: CVE Rediscovery ─────────────────────────────────────────────────────

# CVE predicates: each returns True if a crash matches the CVE signature
def is_cve_13434(crash: dict) -> bool:
    """Integer overflow in sqlite3_str_vappendf."""
    return (crash.get("subtype") == "signed-integer-overflow"
            and any("vappendf" in f for f in crash.get("top_frames", [])))

def is_cve_13435(crash: dict) -> bool:
    """Null pointer — known hash on 3.32.0."""
    return crash.get("hash") == "9411c5875a64a648"

def is_cve_13871(crash: dict) -> bool:
    """Use-after-free — WindowUnlinkFromSelect or resetAccumulator."""
    frames = crash.get("top_frames", [])
    return any("WindowUnlinkFromSelect" in f or "resetAccumulator" in f for f in frames)

def is_cve_15358(crash: dict) -> bool:
    """Heap overflow — INTERSECT pattern signal-6."""
    return (crash.get("type") in ("signal",)
            and "INTERSECT" in crash.get("sql_preview", ""))

def is_cve_9327(crash: dict) -> bool:
    """Null pointer in sqlite3Select."""
    frames = crash.get("top_frames", [])
    return (crash.get("subtype") == "null-pointer"
            and any("sqlite3Select" in f for f in frames))

# Which CVEs are applicable to which versions
CVE_VERSION_MAP = {
    "CVE-2020-13434": ["3.30.1", "3.31.1", "3.32.0"],
    "CVE-2020-13435": ["3.32.0"],
    "CVE-2020-13871": ["3.30.1", "3.32.2"],
    "CVE-2020-15358": ["3.32.2"],
    "CVE-2020-9327":  ["3.31.1"],
}

CVE_PREDICATES = {
    "CVE-2020-13434": is_cve_13434,
    "CVE-2020-13435": is_cve_13435,
    "CVE-2020-13871": is_cve_13871,
    "CVE-2020-15358": is_cve_15358,
    "CVE-2020-9327":  is_cve_9327,
}


def run_rq1():
    """Extract CVE rediscovery data from v3.5 AND EBNF workdirs (advisor: all RQs compare both)."""
    print("=== RQ1: CVE Rediscovery (DBMS-Nautilus v3.5 + EBNF-Baseline) ===")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    cve_rows = []
    ttfc_rows = []

    # Process BOTH grammars
    for grammar, pattern, label in [
        ("DBMS-Nautilus", RQ1_PATTERN, "proposed"),
        ("EBNF-Baseline", RQ3_BASELINE_PATTERN, "baseline"),
    ]:
        for ver in VERSIONS:
            for run in RUNS:
                wdir = WORKDIRS / pattern.format(ver=ver, run=run)
                if not wdir.exists():
                    continue

                triage_file = wdir / "triage_test.json"
                if not triage_file.exists():
                    triage_file = wdir / "triage.json"
                with open(triage_file) as f:
                    triage = json.load(f)
                crashes = triage.get("crashes", [])

                for cve_id, predicate in CVE_PREDICATES.items():
                    applicable_versions = CVE_VERSION_MAP[cve_id]
                    if ver not in applicable_versions:
                        cve_rows.append({
                            "grammar": grammar, "version": ver, "run": run,
                            "cve": cve_id, "found": "N/A", "evidence": "wrong_version",
                        })
                        continue

                    matching = [c for c in crashes if predicate(c)]
                    found = len(matching) > 0
                    evidence = ""
                    if found and matching:
                        evidence = f"hash={matching[0].get('hash','')}"

                    cve_rows.append({
                        "grammar": grammar, "version": ver, "run": run,
                        "cve": cve_id, "found": "yes" if found else "no",
                        "evidence": evidence,
                    })

                    if found:
                        ttfc = get_ttfc(wdir)
                        if ttfc is not None:
                            ttfc_rows.append({
                                "grammar": grammar, "cve": cve_id,
                                "version": ver, "run": run, "ttfc_sec": ttfc,
                            })

    # Write CVE hits CSV (includes BOTH grammars)
    cve_path = OUT_DIR / "rq1_cve_hits.csv"
    with open(cve_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["grammar", "version", "run", "cve", "found", "evidence"])
        w.writeheader()
        w.writerows(cve_rows)
    print(f"  Wrote {cve_path} ({len(cve_rows)} rows)")

    ttfc_path = OUT_DIR / "rq1_ttfc_per_cve.csv"
    with open(ttfc_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["grammar", "cve", "version", "run", "ttfc_sec"])
        w.writeheader()
        w.writerows(ttfc_rows)
    print(f"  Wrote {ttfc_path} ({len(ttfc_rows)} rows)")

    # Print summary for BOTH grammars
    for grammar in ["DBMS-Nautilus", "EBNF-Baseline"]:
        print(f"\n  {grammar}:")
        for cve_id in CVE_PREDICATES:
            hits = [r for r in cve_rows if r["grammar"] == grammar
                    and r["cve"] == cve_id and r["found"] == "yes"]
            applicable = [r for r in cve_rows if r["grammar"] == grammar
                          and r["cve"] == cve_id and r["found"] != "N/A"]
            print(f"    {cve_id}: {len(hits)}/{len(applicable)} runs")
```

- [ ] **Step 2: Verify RQ1 by running it**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
python3 scripts/ch4_pipeline.py --rq1
```

Expected output should show:
- CVE-2020-13434: 14/15
- CVE-2020-13435: 5/5
- CVE-2020-13871: check actual count (was 4/5 in old data, may differ with triage_test.json)
- CVE-2020-15358: 5/5
- CVE-2020-9327: 0/5

- [ ] **Step 3: Commit**

```bash
git add scripts/ch4_pipeline.py results/ch4_final/
git commit -m "feat: ch4_pipeline RQ1 extraction from v3.5 workdirs"
```

---

## Task 3: Implement RQ2 data extraction

**Files:**
- Modify: `scripts/ch4_pipeline.py`

- [ ] **Step 1: Add RQ2 bug class extraction**

```python
# ── RQ2: Bug Detection (v3.3 workdirs) ──────────────────────────────────────

# Known CVE function signatures for classification
CVE_FUNCTION_MAP = {
    "sqlite3_str_vappendf": "CVE-2020-13434",
    "sqlite3WindowUnlinkFromSelect": "CVE-2020-13871",
    "sqlite3Select": "CVE-2020-9327",
}


def run_rq2():
    """Extract bug class data from v3.3 AND EBNF workdirs (advisor: all RQs compare both)."""
    print("\n=== RQ2: Bug Detection (DBMS-Nautilus v3.3 + EBNF-Baseline) ===")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all crashes across all runs, for BOTH grammars
    all_bugs = []  # list of dicts per (grammar, version, run, hash)

    for grammar, pattern, label in [
        ("DBMS-Nautilus", RQ2_PATTERN, "proposed"),
        ("EBNF-Baseline", RQ3_BASELINE_PATTERN, "baseline"),
    ]:
        for ver in VERSIONS:
            for run in RUNS:
                wdir = WORKDIRS / pattern.format(ver=ver, run=run)
                if not wdir.exists():
                    continue

                triage_file = wdir / "triage_test.json"
                if not triage_file.exists():
                    triage_file = wdir / "triage.json"
                with open(triage_file) as f:
                    triage = json.load(f)

                for crash in triage.get("crashes", []):
                    ctype = crash.get("type", "unknown")
                    if ctype == "debug_assert":
                        continue
                    all_bugs.append({
                        "grammar": grammar,
                        "version": ver,
                        "run": run,
                        "hash": crash.get("hash", ""),
                        "type": ctype,
                        "subtype": crash.get("subtype", ""),
                        "key_function": crash.get("top_frames", ["unknown"])[0]
                            if crash.get("top_frames") else "unknown",
                        "count": crash.get("count", 1),
                    })

    # Build bug classes SEPARATELY for each grammar, using a unified class registry
    # First pass: identify all (function, subtype) keys from BOTH grammars
    all_keys = set()
    for bug in all_bugs:
        all_keys.add((bug["key_function"], bug["subtype"]))

    # Sort by total crash count (DBMS-Nautilus) for stable ordering
    proposed_bugs = [b for b in all_bugs if b["grammar"] == "DBMS-Nautilus"]
    key_counts = defaultdict(int)
    for b in proposed_bugs:
        key_counts[(b["key_function"], b["subtype"])] += b["count"]
    sorted_keys = sorted(all_keys, key=lambda k: key_counts.get(k, 0), reverse=True)

    class_id_map = {}
    for i, key in enumerate(sorted_keys, start=1):
        class_id_map[key] = f"BC{i:03d}"

    def get_cve(func: str) -> str:
        for pattern, cve in CVE_FUNCTION_MAP.items():
            if pattern in func:
                return cve
        return ""

    def get_severity(subtype: str) -> str:
        if subtype in ("null-pointer", "misaligned-access") or "heap" in subtype:
            return "HIGH"
        elif "integer-overflow" in subtype:
            return "MEDIUM"
        return "LOW"

    # Write bug class summary for EACH grammar
    for grammar, filename in [
        ("DBMS-Nautilus", "rq2_bug_classes.csv"),
        ("EBNF-Baseline", "rq2_ebnf_bug_classes.csv"),
    ]:
        grammar_bugs = [b for b in all_bugs if b["grammar"] == grammar]
        grammar_keys = defaultdict(list)
        for b in grammar_bugs:
            grammar_keys[(b["key_function"], b["subtype"])].append(b)

        rows = []
        for key in sorted_keys:
            if key not in grammar_keys:
                continue
            func, subtype = key
            bugs = grammar_keys[key]
            rows.append({
                "class_id": class_id_map[key],
                "key_function": func,
                "subtype": subtype,
                "severity": get_severity(subtype),
                "versions": ", ".join(sorted(set(b["version"] for b in bugs))),
                "cve": get_cve(func),
                "unique_hashes": len(set(b["hash"] for b in bugs)),
                "total_crashes": sum(b["count"] for b in bugs),
            })

        path = OUT_DIR / filename
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=[
                "class_id", "key_function", "subtype", "severity",
                "versions", "cve", "unique_hashes", "total_crashes",
            ])
            w.writeheader()
            w.writerows(rows)
        total_h = sum(r["unique_hashes"] for r in rows)
        print(f"  {grammar}: {len(rows)} classes, {total_h} unique hashes -> {path.name}")

    # Per-run class counts for Table 4.4 — BOTH grammars
    per_run_rows = []
    for grammar, pattern in [
        ("DBMS-Nautilus", RQ2_PATTERN),
        ("EBNF-Baseline", RQ3_BASELINE_PATTERN),
    ]:
        grammar_bugs = [b for b in all_bugs if b["grammar"] == grammar]
        for ver in VERSIONS:
            for run in RUNS:
                run_bugs = [b for b in grammar_bugs
                            if b["version"] == ver and b["run"] == run]
                run_classes = set()
                for b in run_bugs:
                    key = (b["key_function"], b["subtype"])
                    if key in class_id_map:
                        run_classes.add(class_id_map[key])
                per_run_rows.append({
                    "grammar": grammar, "version": ver, "run": run,
                    "num_classes": len(run_classes),
                })

    pr_path = OUT_DIR / "rq2_per_run_classes.csv"
    with open(pr_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["grammar", "version", "run", "num_classes"])
        w.writeheader()
        w.writerows(per_run_rows)
    print(f"  Wrote {pr_path}")

    # Print Table 4.4 summary for BOTH grammars
    for grammar in ["DBMS-Nautilus", "EBNF-Baseline"]:
        print(f"\n  {grammar} (Table 4.4):")
        for ver in VERSIONS:
            counts = [r["num_classes"] for r in per_run_rows
                      if r["grammar"] == grammar and r["version"] == ver]
            if counts:
                m = statistics.mean(counts)
                s = statistics.stdev(counts) if len(counts) > 1 else 0
                print(f"    {ver}: {m:.1f} +/- {s:.1f} classes/run (n={len(counts)})")
```

- [ ] **Step 2: Verify RQ2**

```bash
python3 scripts/ch4_pipeline.py --rq2
```

Expected: 11 bug classes (matching thesis), sequential BC001-BC011, total 45 hashes. If the count differs because triage_test.json filters differently than triage.json, investigate and document.

- [ ] **Step 3: Commit**

```bash
git add scripts/ch4_pipeline.py results/ch4_final/
git commit -m "feat: ch4_pipeline RQ2 extraction from v3.3 workdirs"
```

---

## Task 4: Implement RQ3 data extraction (the critical fix)

**Files:**
- Modify: `scripts/ch4_pipeline.py`

This is the task that fixes the main review finding: RQ3 now reads BOTH proposed and baseline from comparison workdirs.

- [ ] **Step 1: Add RQ3 per-campaign extraction**

```python
# ── RQ3: Performance Trade-off (comparison workdirs) ────────────────────────

def run_rq3():
    """Extract performance metrics from v3.4 and EBNF comparison workdirs."""
    print("\n=== RQ3: Performance (v3.4 vs EBNF comparison workdirs) ===")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    campaign_rows = []
    anomalies = []

    for grammar, pattern, label in [
        ("proposed", RQ3_PROPOSED_PATTERN, "v3.4"),
        ("baseline", RQ3_BASELINE_PATTERN, "EBNF"),
    ]:
        for ver in VERSIONS:
            for run in RUNS:
                wdir = WORKDIRS / pattern.format(ver=ver, run=run)
                if not wdir.exists():
                    print(f"  INFO: missing {wdir.name}", file=sys.stderr)
                    continue

                tp = get_throughput(wdir)
                edges = get_edges(wdir)
                rcs = get_unique_rcs(wdir)
                ttfc = get_ttfc(wdir)
                queue = get_queue_size(wdir)

                row = {
                    "grammar": grammar,
                    "grammar_label": label,
                    "version": ver,
                    "run": run,
                    "throughput": round(tp, 1) if tp else None,
                    "edges": edges,
                    "unique_rcs": rcs,
                    "ttfc": ttfc,
                    "queue_size": queue,
                    "workdir": wdir.name,
                }
                campaign_rows.append(row)

                # Flag anomalies (queue_size < 200 for proposed grammar)
                if grammar == "proposed" and queue is not None and queue < 200:
                    anomalies.append(
                        f"ANOMALY: {wdir.name} queue_size={queue} "
                        f"(expected ~1200+). RCs={rcs}, tp={tp:.1f}"
                    )

    # Write per-campaign CSV
    pc_path = OUT_DIR / "rq3_per_campaign.csv"
    fields = ["grammar", "grammar_label", "version", "run",
              "throughput", "edges", "unique_rcs", "ttfc", "queue_size", "workdir"]
    with open(pc_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(campaign_rows)
    print(f"  Wrote {pc_path} ({len(campaign_rows)} campaigns)")

    # Print anomalies
    if anomalies:
        print(f"\n  ANOMALIES DETECTED ({len(anomalies)}):")
        for a in anomalies:
            print(f"    {a}")

    # ── Statistical tests ────────────────────────────────────────────────
    stats_rows = []
    for metric_name, metric_key in [
        ("unique_rcs", "unique_rcs"),
        ("edges", "edges"),
        ("throughput", "throughput"),
        ("ttfc", "ttfc"),
    ]:
        for ver in VERSIONS:
            proposed = [r[metric_key] for r in campaign_rows
                        if r["grammar"] == "proposed" and r["version"] == ver
                        and r[metric_key] is not None]
            baseline = [r[metric_key] for r in campaign_rows
                        if r["grammar"] == "baseline" and r["version"] == ver
                        and r[metric_key] is not None]

            u, p, d, eff = mann_whitney(
                [float(x) for x in proposed],
                [float(x) for x in baseline],
            )

            p_mean = statistics.mean(proposed) if proposed else 0
            p_std = statistics.stdev(proposed) if len(proposed) > 1 else 0
            b_mean = statistics.mean(baseline) if baseline else 0
            b_std = statistics.stdev(baseline) if len(baseline) > 1 else 0

            stats_rows.append({
                "metric": metric_name,
                "version": ver,
                "proposed_n": len(proposed),
                "proposed_mean": round(p_mean, 4),
                "proposed_std": round(p_std, 4),
                "baseline_n": len(baseline),
                "baseline_mean": round(b_mean, 4),
                "baseline_std": round(b_std, 4),
                "U_statistic": round(u, 4) if not np.isnan(u) else "",
                "p_value": round(p, 6) if not np.isnan(p) else "",
                "cliffs_d": round(d, 2) if not np.isnan(d) else "",
                "effect_size": eff,
            })

    st_path = OUT_DIR / "rq3_statistical_tests.csv"
    with open(st_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "metric", "version", "proposed_n", "proposed_mean", "proposed_std",
            "baseline_n", "baseline_mean", "baseline_std",
            "U_statistic", "p_value", "cliffs_d", "effect_size",
        ])
        w.writeheader()
        w.writerows(stats_rows)
    print(f"  Wrote {st_path}")

    # ── Summary table (Table 4.6) ────────────────────────────────────────
    summary_rows = []
    for metric_name, metric_key in [
        ("unique_rcs", "unique_rcs"),
        ("edges", "edges"),
        ("throughput", "throughput"),
        ("ttfc", "ttfc"),
    ]:
        all_proposed = [float(r[metric_key]) for r in campaign_rows
                        if r["grammar"] == "proposed" and r[metric_key] is not None]
        all_baseline = [float(r[metric_key]) for r in campaign_rows
                        if r["grammar"] == "baseline" and r[metric_key] is not None]
        summary_rows.append({
            "metric": metric_name,
            "proposed_n": len(all_proposed),
            "proposed_mean": round(statistics.mean(all_proposed), 1) if all_proposed else 0,
            "proposed_std": round(statistics.stdev(all_proposed), 1) if len(all_proposed) > 1 else 0,
            "baseline_n": len(all_baseline),
            "baseline_mean": round(statistics.mean(all_baseline), 1) if all_baseline else 0,
            "baseline_std": round(statistics.stdev(all_baseline), 1) if len(all_baseline) > 1 else 0,
        })

    sm_path = OUT_DIR / "rq3_summary.csv"
    with open(sm_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "metric", "proposed_n", "proposed_mean", "proposed_std",
            "baseline_n", "baseline_mean", "baseline_std",
        ])
        w.writeheader()
        w.writerows(summary_rows)
    print(f"  Wrote {sm_path}")

    # Print Table 4.5 for visual inspection
    print("\n  Table 4.5 (from v3.4 comparison workdirs):")
    for row in stats_rows:
        print(f"    {row['metric']:<12} {row['version']:<8} "
              f"proposed={row['proposed_mean']:>8}+/-{row['proposed_std']:<8} "
              f"baseline={row['baseline_mean']:>8}+/-{row['baseline_std']:<8} "
              f"p={row['p_value']:<10} d={row['cliffs_d']:<6} {row['effect_size']}")

    # Print Table 4.6 summary
    print("\n  Table 4.6 (grand means):")
    for row in summary_rows:
        print(f"    {row['metric']:<12} proposed={row['proposed_mean']}+/-{row['proposed_std']} "
              f"(n={row['proposed_n']})  baseline={row['baseline_mean']}+/-{row['baseline_std']} "
              f"(n={row['baseline_n']})")

    return campaign_rows  # needed for figures
```

- [ ] **Step 2: Verify RQ3**

```bash
python3 scripts/ch4_pipeline.py --rq3
```

Check that:
1. Proposed throughput mean for 3.30.1 is ~90.6 (NOT 76.7 from v3.5)
2. All EBNF 3.32.0 metrics show n=4 (not 5)
3. Anomalies are flagged for v3.4 3.31.1 run1 (queue=123) and v3.4 3.32.0 run1 (queue=77)
4. Unique RCs match the old values (205.6 for grand mean) since they already came from v3.4

- [ ] **Step 3: Commit**

```bash
git add scripts/ch4_pipeline.py results/ch4_final/
git commit -m "feat: ch4_pipeline RQ3 extraction from v3.4+EBNF comparison workdirs"
```

---

## Task 5: Implement figure generation

**Files:**
- Modify: `scripts/ch4_pipeline.py`

- [ ] **Step 1: Add Figure 4.1 (Time to first CVE crash)**

```python
# ── Figures ──────────────────────────────────────────────────────────────────

def plot_fig_4_1():
    """Time to first CVE-matching crash (RQ1, v3.5 workdirs)."""
    # Use TTFC from coverage.csv for each v3.5 run that found each CVE
    cve_times = defaultdict(list)

    for ver in VERSIONS:
        for run in RUNS:
            wdir = WORKDIRS / RQ1_PATTERN.format(ver=ver, run=run)
            if not wdir.exists():
                continue
            triage_file = wdir / "triage_test.json"
            if not triage_file.exists():
                triage_file = wdir / "triage.json"
            with open(triage_file) as f:
                triage = json.load(f)
            crashes = triage.get("crashes", [])

            cov = wdir / "coverage.csv"
            if not cov.exists():
                continue
            cov_rows = []
            with open(cov) as f:
                cov_rows = list(csv.DictReader(f))

            for cve_id, pred in CVE_PREDICATES.items():
                if ver not in CVE_VERSION_MAP[cve_id]:
                    continue
                matching = [c for c in crashes if pred(c)]
                if not matching:
                    continue
                # Find earliest crash exec index
                min_idx = float("inf")
                for c in matching:
                    try:
                        idx = int(c["sample_file"].split("_")[1])
                        min_idx = min(min_idx, idx)
                    except (KeyError, IndexError, ValueError):
                        pass
                # Map to time via coverage.csv exec_count
                if min_idx < float("inf"):
                    for row in cov_rows:
                        ec = int(row.get("exec_count", 0))
                        if ec >= min_idx:
                            cve_times[cve_id].append(int(row["timestamp_sec"]))
                            break

    # Only plot CVEs that were found
    found = {k: v for k, v in cve_times.items() if v}
    if not found:
        print("  Fig 4.1: no CVE timing data — skipping")
        return

    labels = sorted(found.keys())
    data = [found[k] for k in labels]

    fig, ax = plt.subplots(figsize=(8, 5))
    positions = range(1, len(labels) + 1)
    ax.boxplot(data, positions=list(positions), widths=0.45, patch_artist=True,
               medianprops=dict(color="white", linewidth=2),
               boxprops=dict(facecolor=COLOR_PROPOSED, alpha=0.85),
               whiskerprops=dict(color=COLOR_PROPOSED),
               capprops=dict(color=COLOR_PROPOSED))

    # Overlay individual points
    rng = np.random.default_rng(42)
    for i, (pos, times) in enumerate(zip(positions, data)):
        jitter = rng.uniform(-0.12, 0.12, len(times))
        ax.scatter([pos + j for j in jitter], times, color=COLOR_PROPOSED,
                   s=30, zorder=3, alpha=0.75, edgecolors="white", linewidths=0.5)

    short_labels = [l.replace("CVE-2020-", "CVE-\n") for l in labels]
    ax.set_xticks(list(positions))
    ax.set_xticklabels(short_labels, fontsize=10)
    ax.set_ylabel("Time to first crash (seconds)", fontsize=12)
    ax.set_xlabel("CVE", fontsize=12)
    ax.tick_params(labelsize=10)
    fig.tight_layout()

    out = FIG_DIR / "fig_4_1_time_to_first_cve.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  Fig 4.1 saved -> {out}")
```

- [ ] **Step 2: Add Figure 4.2 (Bug class breakdown)**

```python
def plot_fig_4_2():
    """Bug class breakdown bar chart (RQ2, from rq2_bug_classes.csv)."""
    bc_path = OUT_DIR / "rq2_bug_classes.csv"
    with open(bc_path) as f:
        classes = list(csv.DictReader(f))

    labels = [c["class_id"] for c in classes]
    hashes = [int(c["unique_hashes"]) for c in classes]
    severities = [c["severity"] for c in classes]
    has_cve = [bool(c["cve"]) for c in classes]

    sev_colors = {"HIGH": "#F44336", "MEDIUM": "#FF9800", "LOW": "#4CAF50"}
    colors = [sev_colors[s] for s in severities]

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(labels))
    bars = ax.bar(x, hashes, color=colors, width=0.6, alpha=0.85,
                  edgecolor="white", linewidth=0.5)

    for bar, is_cve in zip(bars, has_cve):
        if is_cve:
            bar.set_hatch("///")
            bar.set_edgecolor("#333")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=9)
    ax.set_ylabel("Unique crash hashes", fontsize=12)
    ax.set_xlabel("Bug class", fontsize=12)
    ax.tick_params(labelsize=10)

    legend_handles = [
        mpatches.Patch(facecolor=sev_colors["HIGH"], label="HIGH"),
        mpatches.Patch(facecolor=sev_colors["MEDIUM"], label="MEDIUM"),
        mpatches.Patch(facecolor=sev_colors["LOW"], label="LOW"),
        mpatches.Patch(facecolor="#aaa", hatch="///", edgecolor="#333", label="CVE match"),
    ]
    ax.legend(handles=legend_handles, fontsize=9, loc="upper right")

    for bar, val in zip(bars, hashes):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
                str(val), ha="center", va="bottom", fontsize=8)

    fig.tight_layout()
    out = FIG_DIR / "fig_4_2_bug_class_breakdown.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  Fig 4.2 saved -> {out}")
```

- [ ] **Step 3: Add Figures 4.3, 4.4, 4.5 (RQ3 comparison figures)**

```python
def plot_fig_4_3():
    """Coverage growth over time (RQ3, v3.4 vs EBNF comparison workdirs)."""
    T = 900

    def gather_series(pattern: str) -> np.ndarray:
        all_series = []
        for wdir in sorted(WORKDIRS.iterdir()):
            if pattern not in wdir.name:
                continue
            cov = wdir / "coverage.csv"
            if not cov.exists():
                continue
            series = np.zeros(T + 1)
            with open(cov) as f:
                for row in csv.DictReader(f):
                    t = int(row["timestamp_sec"])
                    if t <= T:
                        series[t] = int(row["total_edges"])
            for t in range(1, T + 1):
                if series[t] == 0:
                    series[t] = series[t - 1]
            all_series.append(series)
        if not all_series:
            return np.zeros((1, T + 1))
        return np.stack(all_series)

    proposed = gather_series("_comparison_v3.4_run")
    baseline = gather_series("_comparison_ebnf_run")
    t_axis = np.arange(T + 1)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t_axis, proposed.mean(axis=0), color=COLOR_PROPOSED, linewidth=2, label="DBMS-Nautilus")
    ax.fill_between(t_axis, proposed.mean(axis=0) - proposed.std(axis=0),
                    proposed.mean(axis=0) + proposed.std(axis=0), color=COLOR_PROPOSED, alpha=0.15)
    ax.plot(t_axis, baseline.mean(axis=0), color=COLOR_BASELINE, linewidth=2, label="EBNF-Baseline")
    ax.fill_between(t_axis, baseline.mean(axis=0) - baseline.std(axis=0),
                    baseline.mean(axis=0) + baseline.std(axis=0), color=COLOR_BASELINE, alpha=0.15)

    ax.set_xlabel("Time (seconds)", fontsize=12)
    ax.set_ylabel("Cumulative edge coverage", fontsize=12)
    ax.set_xlim(0, 900)
    ax.legend(fontsize=11)
    ax.tick_params(labelsize=10)
    fig.tight_layout()

    out = FIG_DIR / "fig_4_3_coverage_growth.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  Fig 4.3 saved -> {out}")


def plot_fig_4_4():
    """Throughput comparison bar chart (RQ3, from rq3_per_campaign.csv)."""
    pc_path = OUT_DIR / "rq3_per_campaign.csv"
    with open(pc_path) as f:
        rows = list(csv.DictReader(f))

    proposed_tp = {v: [] for v in VERSIONS}
    baseline_tp = {v: [] for v in VERSIONS}
    for r in rows:
        if r["throughput"]:
            tp = float(r["throughput"])
            if r["grammar"] == "proposed":
                proposed_tp[r["version"]].append(tp)
            else:
                baseline_tp[r["version"]].append(tp)

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(VERSIONS))
    width = 0.35

    p_means = [statistics.mean(proposed_tp[v]) for v in VERSIONS]
    p_stds = [statistics.stdev(proposed_tp[v]) if len(proposed_tp[v]) > 1 else 0 for v in VERSIONS]
    b_means = [statistics.mean(baseline_tp[v]) for v in VERSIONS]
    b_stds = [statistics.stdev(baseline_tp[v]) if len(baseline_tp[v]) > 1 else 0 for v in VERSIONS]

    ax.bar(x - width/2, p_means, width, yerr=p_stds, color=COLOR_PROPOSED,
           alpha=0.85, label="DBMS-Nautilus", capsize=4)
    ax.bar(x + width/2, b_means, width, yerr=b_stds, color=COLOR_BASELINE,
           alpha=0.85, label="EBNF-Baseline", capsize=4)

    ax.set_xticks(x)
    ax.set_xticklabels([f"SQLite {v}" for v in VERSIONS], fontsize=10)
    ax.set_ylabel("Throughput (execs/sec)", fontsize=12)
    ax.legend(fontsize=10)
    ax.tick_params(labelsize=10)
    fig.tight_layout()

    out = FIG_DIR / "fig_4_4_throughput.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  Fig 4.4 saved -> {out}")


def plot_fig_4_5():
    """Time to first crash comparison (RQ3, from rq3_per_campaign.csv)."""
    pc_path = OUT_DIR / "rq3_per_campaign.csv"
    with open(pc_path) as f:
        rows = list(csv.DictReader(f))

    fig, axes = plt.subplots(1, 4, figsize=(14, 4), sharey=True)

    for i, ver in enumerate(VERSIONS):
        proposed = [int(r["ttfc"]) for r in rows
                    if r["grammar"] == "proposed" and r["version"] == ver and r["ttfc"]]
        baseline = [int(r["ttfc"]) for r in rows
                    if r["grammar"] == "baseline" and r["version"] == ver and r["ttfc"]]

        ax = axes[i]
        data = [proposed, baseline]
        bp = ax.boxplot(data, positions=[1, 2], widths=0.5, patch_artist=True,
                        medianprops=dict(color="white", linewidth=2))
        bp["boxes"][0].set_facecolor(COLOR_PROPOSED)
        bp["boxes"][1].set_facecolor(COLOR_BASELINE)

        ax.set_xticks([1, 2])
        ax.set_xticklabels(["Proposed", "EBNF"], fontsize=9)
        ax.set_title(f"SQLite {ver}", fontsize=10)
        if i == 0:
            ax.set_ylabel("TTFC (seconds)", fontsize=11)

    fig.tight_layout()
    out = FIG_DIR / "fig_4_5_time_to_first_crash.pdf"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"  Fig 4.5 saved -> {out}")
```

- [ ] **Step 4: Verify all figures**

```bash
python3 scripts/ch4_pipeline.py --figures-only
ls -la docs/thesis/v2/figures/fig_4_*.pdf
```

All 5 PDFs should exist and have recent timestamps.

- [ ] **Step 5: Commit**

```bash
git add scripts/ch4_pipeline.py docs/thesis/v2/figures/fig_4_*.pdf
git commit -m "feat: ch4_pipeline figure generation from correct workdirs"
```

---

## Task 6: Add audit report and manifest

**Files:**
- Modify: `scripts/ch4_pipeline.py`

- [ ] **Step 1: Add manifest and audit generation**

```python
# ── Audit ────────────────────────────────────────────────────────────────────

def generate_audit():
    """Generate manifest.json and AUDIT.md for full provenance."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = {
        "generated": __import__("datetime").datetime.now().isoformat(),
        "git_hash": get_git_hash(),
        "script": "scripts/ch4_pipeline.py",
        "workdir_mapping": {
            "RQ1": {"pattern": RQ1_PATTERN, "grammar": "v3.5", "count": 0},
            "RQ2": {"pattern": RQ2_PATTERN, "grammar": "v3.3", "count": 0},
            "RQ3_proposed": {"pattern": RQ3_PROPOSED_PATTERN, "grammar": "v3.4", "count": 0},
            "RQ3_baseline": {"pattern": RQ3_BASELINE_PATTERN, "grammar": "EBNF", "count": 0},
        },
        "missing_workdirs": [],
    }

    # Count actual workdirs
    for rq, pattern in [
        ("RQ1", RQ1_PATTERN),
        ("RQ2", RQ2_PATTERN),
        ("RQ3_proposed", RQ3_PROPOSED_PATTERN),
        ("RQ3_baseline", RQ3_BASELINE_PATTERN),
    ]:
        for ver in VERSIONS:
            for run in RUNS:
                wdir = WORKDIRS / pattern.format(ver=ver, run=run)
                if wdir.exists():
                    manifest["workdir_mapping"][rq]["count"] += 1
                else:
                    manifest["missing_workdirs"].append(wdir.name)

    with open(OUT_DIR / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)

    # Generate AUDIT.md
    audit_lines = [
        "# Chapter 4 Data Audit Report",
        f"",
        f"**Generated:** {manifest['generated']}",
        f"**Git hash:** `{manifest['git_hash']}`",
        f"**Script:** `scripts/ch4_pipeline.py`",
        f"",
        "## Workdir Inventory",
        f"",
        f"| RQ | Grammar | Expected | Found | Missing |",
        f"|---|---|---|---|---|",
    ]

    for rq, info in manifest["workdir_mapping"].items():
        expected = 20
        found = info["count"]
        missing = expected - found
        audit_lines.append(f"| {rq} | {info['grammar']} | {expected} | {found} | {missing} |")

    if manifest["missing_workdirs"]:
        audit_lines.extend([
            f"",
            "## Missing Workdirs",
            f"",
        ])
        for w in manifest["missing_workdirs"]:
            audit_lines.append(f"- `{w}`")

    # Add output file checksums
    audit_lines.extend([
        f"",
        "## Output Files",
        f"",
        f"| File | Exists | Rows |",
        f"|---|---|---|",
    ])
    for csv_name in [
        "rq1_cve_hits.csv", "rq1_ttfc_per_cve.csv",
        "rq2_bug_classes.csv", "rq2_per_run_classes.csv",
        "rq3_per_campaign.csv", "rq3_statistical_tests.csv", "rq3_summary.csv",
    ]:
        p = OUT_DIR / csv_name
        if p.exists():
            with open(p) as f:
                row_count = sum(1 for _ in f) - 1  # minus header
            audit_lines.append(f"| `{csv_name}` | YES | {row_count} |")
        else:
            audit_lines.append(f"| `{csv_name}` | **NO** | — |")

    with open(OUT_DIR / "AUDIT.md", "w") as f:
        f.write("\n".join(audit_lines) + "\n")

    print(f"\n  Wrote {OUT_DIR / 'manifest.json'}")
    print(f"  Wrote {OUT_DIR / 'AUDIT.md'}")
```

- [ ] **Step 2: Add main() with CLI**

```python
# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Chapter 4 data pipeline")
    parser.add_argument("--rq1", action="store_true", help="Run RQ1 only")
    parser.add_argument("--rq2", action="store_true", help="Run RQ2 only")
    parser.add_argument("--rq3", action="store_true", help="Run RQ3 only")
    parser.add_argument("--figures-only", action="store_true", help="Regenerate figures from CSVs")
    parser.add_argument("--audit-only", action="store_true", help="Just generate audit report")
    args = parser.parse_args()

    run_all = not (args.rq1 or args.rq2 or args.rq3 or args.figures_only or args.audit_only)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    if run_all or args.rq1:
        run_rq1()
    if run_all or args.rq2:
        run_rq2()
    if run_all or args.rq3:
        run_rq3()

    if run_all or args.figures_only:
        print("\n=== Generating Figures ===")
        plot_fig_4_1()
        plot_fig_4_2()
        plot_fig_4_3()
        plot_fig_4_4()
        plot_fig_4_5()

    if run_all or args.audit_only:
        generate_audit()

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Full pipeline run and verify**

```bash
python3 scripts/ch4_pipeline.py
cat results/ch4_final/AUDIT.md
```

Check AUDIT.md shows:
- RQ1: 20/20 workdirs
- RQ2: 20/20 workdirs
- RQ3_proposed: 20/20 workdirs
- RQ3_baseline: 19/20 workdirs (3.32.0 run1 missing)
- All 7 CSV files exist with correct row counts

- [ ] **Step 4: Commit**

```bash
git add scripts/ch4_pipeline.py results/ch4_final/
git commit -m "feat: ch4_pipeline audit report and full pipeline"
```

---

## Task 7: Cross-check pipeline output against thesis and update .tex

**Files:**
- Read: `results/ch4_final/*.csv` (pipeline output)
- Modify: `docs/thesis/v2/chapters/c4_experiments.tex`

This task uses the pipeline CSV output to update every number in the thesis that changed.

- [ ] **Step 1: Compare new RQ3 numbers against thesis**

```bash
python3 -c "
import csv

print('=== New Table 4.5 proposed values (from v3.4) ===')
with open('results/ch4_final/rq3_statistical_tests.csv') as f:
    for row in csv.DictReader(f):
        print(f'{row[\"metric\"]:<12} {row[\"version\"]:<8} proposed={row[\"proposed_mean\"]}+/-{row[\"proposed_std\"]} baseline={row[\"baseline_mean\"]}+/-{row[\"baseline_std\"]} p={row[\"p_value\"]} d={row[\"cliffs_d\"]}')

print()
print('=== New Table 4.6 (from v3.4) ===')
with open('results/ch4_final/rq3_summary.csv') as f:
    for row in csv.DictReader(f):
        print(f'{row[\"metric\"]:<12} proposed={row[\"proposed_mean\"]}+/-{row[\"proposed_std\"]} (n={row[\"proposed_n\"]}) baseline={row[\"baseline_mean\"]}+/-{row[\"baseline_std\"]} (n={row[\"baseline_n\"]})')
"
```

Write down all numbers that differ from the current thesis. These are the values to update in c4_experiments.tex.

- [ ] **Step 2: Update Table 4.5 in .tex with new values**

Replace every throughput and edge coverage cell for "DBMS-Nautilus" with the new v3.4 values from `rq3_statistical_tests.csv`. Update p-values and Cliff's d if they changed.

- [ ] **Step 3: Update Table 4.6 in .tex with new summary values**

Replace throughput and edge coverage means/stds with values from `rq3_summary.csv`.

- [ ] **Step 4: Update all prose ratio claims**

Recompute from the new numbers:
- "X.Xx-Y.Yx higher throughput" — use new per-version ratios
- "XX.X% lower throughput" — (baseline_mean - proposed_mean) / baseline_mean
- "XX.X% lower edge coverage" — same formula
- "X.Xx slower" — baseline_tp / proposed_tp
- All instances in L289, L358, L374, L394

- [ ] **Step 5: Terminology cleanup (Advisor Feedback 2)**

Global find-and-replace in `c4_experiments.tex`:
- "the proposed grammar" → "DBMS-Nautilus" (everywhere except where grammatically awkward)
- "structural-primitives grammar" → "DBMS-Nautilus"
- "compositional grammar" → "DBMS-Nautilus"
- "seed-augmented grammar" → "DBMS-Nautilus"
- "EBNF baseline" → "EBNF-Baseline" (hyphenated everywhere, matching table headers)
- "the EBNF grammar" → "the EBNF-Baseline"
- "generic baseline grammar" → "EBNF-Baseline"
- Remove any mention of v3.3/v3.4/v3.5 grammar versions

In Section 4.3 (Baselines), replace the current seed/no-seed explanation with ONE sentence:
"For the RQ1 evaluation, six low-weight seed rules are added to DBMS-Nautilus; for RQ2, the grammar is used without seed rules; RQ3 uses the full grammar."

- [ ] **Step 6: Add EBNF comparison to RQ1 results (Advisor Feedback 1)**

Table 4.2: Add an "EBNF-Baseline" column showing how many runs found each CVE.
This data comes from `results/ch4_final/rq1_cve_hits.csv` (now includes both grammars).

Add 1-2 sentences in RQ1 prose comparing: "The EBNF-Baseline found CVE-2020-13871 on version 3.30.1 in X/5 runs but did not trigger any other CVEs, confirming that ..."

- [ ] **Step 7: Add EBNF comparison to RQ2 results (Advisor Feedback 1)**

Table 4.4: Add EBNF-Baseline row with per-version bug class counts from `rq2_per_run_classes.csv`.

Add 1-2 sentences comparing: "The EBNF-Baseline found X distinct bug classes vs Y for DBMS-Nautilus, with the difference concentrated in ..."

- [ ] **Step 8: Shorten captions (Advisor Feedback 3)**

Apply Ch3-style short captions:
- Table 4.2: "CVE rediscovery results." (move all detail to body text)
- Table 4.3: "Bug classes discovered across 20 campaigns." (remove severity/methodology from caption)
- Table 4.4: "Bug class discovery per campaign." (remove "mean ± std" from caption)
- Table 4.5: "Statistical comparison: DBMS-Nautilus vs EBNF-Baseline." (remove n/thresholds from caption)
- Table 4.6: "Overall comparison." (remove "mean across all versions" from caption)
- Figure captions: one line each, no methodology details

Move table footnotes (†, ‡) from Table 4.2 into body text paragraphs.

- [ ] **Step 9: Remove prose that restates table data (Advisor Feedback 3, Rule 6)**

Remove or shorten:
- L160: paragraph listing per-version CVE counts already in Table 4.2
- Any prose repeating numbers already visible in a table — reader has the table, just interpret

- [ ] **Step 10: Fix section order sentence (L4)**

Change the intro sentence to match actual order: Metrics → Baselines → Setup.

- [ ] **Step 11: Fix "80 campaigns" to "79" (L102)**

Update total and add note about missing EBNF 3.32.0 run1.

- [ ] **Step 12: Renumber BC IDs sequentially (Table 4.3)**

Pipeline already generates sequential BC001-BCnnn. Update all BC references in prose.

- [ ] **Step 13: Fix "WindowListDelete" → "clearSelect" (L360)**

Replace `sqlite3WindowListDelete` with `clearSelect`.

- [ ] **Step 14: Soften overreach claims**

- "vulnerability-relevant" → "crash-producing"
- "concentrated in non-vulnerable code paths" → "does not translate into proportional crash discovery"
- "This demonstrates" → "This suggests" (for n=2 CVE-9327)
- "confirming that" → "supporting the hypothesis that"

- [ ] **Step 15: Add "previously unreported" evidence (near L205)**

Add: "We searched the National Vulnerability Database and SQLite changelog for versions 3.30.1 and 3.31.1 and found no matching reports as of May 2026."

- [ ] **Step 16: Build PDF and verify**

```bash
cd docs/thesis/v2
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
```

Verify: 0 errors, all figures render, page count reasonable.

- [ ] **Step 14: Commit**

```bash
git add docs/thesis/v2/chapters/c4_experiments.tex docs/thesis/v2/figures/fig_4_*.pdf results/ch4_final/
git commit -m "fix: rebuild ch4 data pipeline from correct workdirs, fix all review issues"
```

---

## Task 8: Final verification — re-run the review rules

**Files:**
- Read: All outputs from Tasks 1-7

- [ ] **Step 1: Run the full pipeline one more time**

```bash
python3 scripts/ch4_pipeline.py
```

- [ ] **Step 2: Spot-check 5 random numbers from thesis against CSV**

Pick 5 numbers from the updated .tex (one from each table) and manually verify they match the pipeline CSV output.

- [ ] **Step 3: Verify all figures use correct workdir patterns**

```bash
grep -n "v35_run\|v33_run\|comparison_v3.4\|comparison_ebnf" scripts/ch4_pipeline.py
```

Confirm: Fig 4.1 uses v35_run (RQ1), Fig 4.2 uses rq2_bug_classes.csv (from v33), Figs 4.3-4.5 use comparison_v3.4 and comparison_ebnf (RQ3).

- [ ] **Step 4: Update data_governance.md with resolution status**

Mark all 25 issues as resolved or document remaining items.

- [ ] **Step 5: Commit final state**

```bash
git add -A
git commit -m "docs: mark ch4 review issues resolved after data pipeline rebuild"
```

---

## Dependencies

```
Task 1 (skeleton)
  → Task 2 (RQ1) ─────────────────────────┐
  → Task 3 (RQ2) ──────────────────────────┤
  → Task 4 (RQ3) ──────────────────────────┤
                                            ├→ Task 5 (figures)
                                            │    → Task 6 (audit)
                                            │       → Task 7 (update .tex)
                                            │          → Task 8 (verify)
```

Tasks 2, 3, 4 are independent and can run in parallel once Task 1 is done.
Tasks 5-8 are sequential.

**Estimated total time:** 4-5 hours (script writing + verification + .tex updates + terminology cleanup + PDF rebuild).

---

## Advisor Feedback Checklist (verify at the end)

- [ ] Every RQ section has DBMS-Nautilus vs EBNF-Baseline comparison
- [ ] Only two grammar names appear in .tex: "DBMS-Nautilus" and "EBNF-Baseline"
- [ ] No version numbers (v3.3, v3.4, v3.5) appear in .tex
- [ ] All table captions are short (one line, Ch3 style)
- [ ] All figure captions are short (one line)
- [ ] No prose restating what a table already shows
- [ ] Table 4.2 footnotes moved to body text
- [ ] BC IDs sequential (no gaps)
- [ ] All data comes from correct workdirs (v3.5 for RQ1, v3.3 for RQ2, v3.4+EBNF for RQ3)
- [ ] Table 4.2 shows ONLY confirmed CVE successes (failures/exclusions in Limitations)
- [ ] Abstract and conclusion NOT touched during Ch4 work

---

## Task 9: Update abstract and conclusion (AFTER Ch4 finalized)

**Prerequisite:** Tasks 1-8 ALL complete. Ch4 numbers are final and verified.

**Files:**
- Modify: `docs/thesis/v2/chapters/abstract_en.tex`
- Modify: `docs/thesis/v2/chapters/conclusion.tex`
- Modify: `docs/thesis/v2/chapters/c1_introduction.tex` (if it previews Ch4 results)

- [ ] **Step 1: Extract final numbers from Ch4**

Read the finalized `c4_experiments.tex` and collect:
- How many CVEs rediscovered (N out of M)
- How many bug classes found (total, CVE-matching, new)
- Key comparison ratios (Xx more RCs, X% lower throughput, etc.)

- [ ] **Step 2: Update abstract**

Replace all Ch4-related claims with the final numbers. Keep it concise — one sentence per RQ.

- [ ] **Step 3: Update conclusion**

Align conclusion's "principal findings" paragraph with the actual Ch4 summary (Section 4.6.5).

- [ ] **Step 4: Check Ch1 introduction**

If Ch1 previews results ("as shown in Chapter 4..."), update those previews.

- [ ] **Step 5: Build PDF and verify consistency**

```bash
cd docs/thesis/v2
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
```

Grep for any remaining numbers that don't match: `grep -n "79.*more\|61.5\|14.5\|2.6.*slower\|4 out of 5\|5 out of 6" docs/thesis/v2/chapters/*.tex`

- [ ] **Step 6: Commit**

```bash
git add docs/thesis/v2/chapters/abstract_en.tex docs/thesis/v2/chapters/conclusion.tex docs/thesis/v2/chapters/c1_introduction.tex
git commit -m "docs: update abstract and conclusion to reflect finalized Ch4 results"
```
