#!/usr/bin/env python3
"""
RQ2 crash triage aggregation script.
Aggregates triage.json and triage_test.json across all 20 RQ2 v33 campaigns.
Produces campaigns_summary.csv, bug_classes.csv, and registry.json.
"""

import json
import csv
import os
import sys
from pathlib import Path
from collections import defaultdict
import statistics

# ─── Known bug classes from RQ1 ───────────────────────────────────────────────
KNOWN_CLASSES = {
    ("null-pointer", "sqlite3Fts5GetTokenizer"):          "BC001",
    ("misaligned-access", "sqlite3WindowUnlinkFromSelect"): "BC002",
    ("signed-integer-overflow", "sqlite3_str_vappendf"):  "BC003",
    ("float-cast-overflow", "alsoAnInt"):                 "BC004",
    ("signal-6", "sqlite3WindowListDelete"):              "BC005",
    ("null-pointer", "sqlite3ExprCodeTarget"):            "BC006",
    ("null-pointer", "sqlite3AtoF"):                      "BC007",
    ("null-pointer", "sqlite3Atoi64"):                    "BC008",
    ("float-cast-overflow", "sqlite3VdbeMemNumerify"):    "BC009",
    ("null-pointer", "sqlite3Select"):                    "BC010",
}

# CVE mapping from known class IDs
CVE_MAP = {
    "BC002": "CVE-2020-13871",
    "BC003": "CVE-2020-13434",
    "BC010": "CVE-2020-9327",
}

SEVERITY_MAP = {
    "null-pointer":            "HIGH",
    "misaligned-access":       "HIGH",
    "signed-integer-overflow": "MEDIUM",
    "float-cast-overflow":     "LOW",
    "signal-6":                "MEDIUM",
    "signal-11":               "HIGH",
    "heap-buffer-overflow":    "CRITICAL",
    "stack-buffer-overflow":   "CRITICAL",
    "use-after-free":          "CRITICAL",
    "global-buffer-overflow":  "HIGH",
    "double-free":             "CRITICAL",
}

def get_key_function(crash):
    """Extract the most informative function name from top_frames."""
    frames = crash.get("top_frames", [])
    for frame in frames:
        # Skip error message lines (contain 'runtime error:')
        if "runtime error:" in frame:
            continue
        # Skip no-stack placeholders
        if frame.startswith("<no-stack"):
            continue
        # Skip file:line paths
        if frame.startswith("../") or frame.startswith("/"):
            continue
        # Return first real function name
        return frame.strip()
    return None


def classify_crash(crash):
    """Return (subtype, key_function) for a crash entry."""
    subtype = crash.get("subtype") or ""
    # For signal types, use subtype like 'signal-6'
    if crash.get("type") == "signal":
        subtype = f"signal-{abs(crash.get('exit_code', 0))}" if not subtype else subtype
    key_fn = get_key_function(crash)
    return subtype, key_fn


def map_to_class(subtype, key_fn):
    """Map (subtype, key_function) to known class ID or None."""
    if not subtype or not key_fn:
        return None
    return KNOWN_CLASSES.get((subtype, key_fn))


WORKDIR_ROOT = Path("/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/workdirs")
OUTPUT_DIR = Path("/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/results/rq2_fresh")
VERSIONS = ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
RUNS = [1, 2, 3, 4, 5]

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    campaigns = []   # list of dicts for campaigns_summary.csv
    bug_rows = []    # list of dicts for bug_classes.csv

    # Aggregate bug class info across all campaigns
    # Key: (subtype, key_function) → {class_id, versions set, hashes set, total_crashes}
    class_agg = defaultdict(lambda: {
        "class_id": None,
        "name": None,
        "subtype": None,
        "key_function": None,
        "severity": None,
        "cve": None,
        "versions": set(),
        "hashes": set(),
        "total_crashes": 0,
    })

    # Track new classes counter
    next_new_id = 11  # BC011, BC012, ...

    print("=== Step 1: Inventorying all 20 workdirs ===")
    missing = []
    for v in VERSIONS:
        for r in RUNS:
            wd = WORKDIR_ROOT / f"sqlite-{v}_v33_run{r}"
            tf = wd / "triage.json"
            tft = wd / "triage_test.json"
            ok = True
            if not tf.exists():
                print(f"  MISSING triage.json: {v}_run{r}")
                missing.append(str(tf))
                ok = False
            if not tft.exists():
                print(f"  MISSING triage_test.json: {v}_run{r}")
                missing.append(str(tft))
                ok = False
            if ok:
                print(f"  OK: sqlite-{v}_v33_run{r}")

    if missing:
        print(f"\nWARNING: {len(missing)} missing files")
    else:
        print("  All 20 workdirs present with both triage files.\n")

    print("=== Step 2 & 3: Aggregating crash data and identifying bug classes ===\n")

    for v in VERSIONS:
        for r in RUNS:
            campaign_id = f"sqlite-{v}_v33_run{r}"
            wd = WORKDIR_ROOT / f"sqlite-{v}_v33_run{r}"

            # ── Parse triage.json (AFL harness, debug_assert/signal) ──
            triage_path = wd / "triage.json"
            with open(triage_path) as f:
                triage = json.load(f)

            summary = triage.get("summary", {})
            total_crashes_afl = triage.get("total_crashes", 0)
            debug_assert_count = summary.get("debug_assert", 0)
            signal_count_afl = summary.get("signal", 0)
            asan_afl = summary.get("asan", 0)
            ubsan_afl = summary.get("ubsan", 0)

            # ── Parse triage_test.json (test harness, UBSan/ASan) ──
            triage_test_path = wd / "triage_test.json"
            with open(triage_test_path) as f:
                triage_test = json.load(f)

            summary_test = triage_test.get("summary", {})
            total_crashes_test = triage_test.get("total_crashes", 0)
            ubsan_count = summary_test.get("ubsan", 0)
            asan_count = summary_test.get("asan", 0)
            signal_count_test = summary_test.get("signal", 0)

            # Use triage.json for aggregate counts (AFL harness total)
            # Use triage_test.json for bug classification
            campaigns.append({
                "campaign_id": campaign_id,
                "grammar": "v3.3",
                "sqlite_version": v,
                "run": r,
                "total_crashes": total_crashes_afl,
                "debug_assert_count": debug_assert_count,
                "signal_count": signal_count_afl,
                "ubsan_count": ubsan_count,
                "asan_count": asan_count,
            })

            # ── Process triage_test.json crashes for bug classification ──
            crashes_test = triage_test.get("crashes", [])
            for crash in crashes_test:
                crash_type = crash.get("type", "")
                if crash_type not in ("ubsan", "asan"):
                    continue  # Only real sanitizer bugs

                subtype, key_fn = classify_crash(crash)
                if not subtype or not key_fn:
                    continue

                h = crash.get("hash", "")
                count = crash.get("count", 1)

                class_key = (subtype, key_fn)
                known_id = map_to_class(subtype, key_fn)

                entry = class_agg[class_key]
                if entry["class_id"] is None:
                    if known_id:
                        entry["class_id"] = known_id
                    else:
                        entry["class_id"] = f"BC0{next_new_id:02d}"
                        next_new_id += 1
                    entry["subtype"] = subtype
                    entry["key_function"] = key_fn
                    entry["name"] = f"{subtype.replace('-', '_')}_in_{key_fn}"
                    entry["severity"] = SEVERITY_MAP.get(subtype, "MEDIUM")
                    entry["cve"] = CVE_MAP.get(entry["class_id"])

                entry["versions"].add(v)
                if h:
                    entry["hashes"].add(h)
                entry["total_crashes"] += count

                bug_rows.append({
                    "campaign_id": campaign_id,
                    "sqlite_version": v,
                    "run": r,
                    "hash": h,
                    "type": crash_type,
                    "subtype": subtype,
                    "key_function": key_fn,
                    "class_id": entry["class_id"],
                    "count": count,
                })

    # ── Write campaigns_summary.csv ──
    csv_campaigns_path = OUTPUT_DIR / "campaigns_summary.csv"
    with open(csv_campaigns_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "campaign_id", "grammar", "sqlite_version", "run",
            "total_crashes", "debug_assert_count", "signal_count",
            "ubsan_count", "asan_count"
        ])
        writer.writeheader()
        writer.writerows(campaigns)
    print(f"Written: {csv_campaigns_path}")

    # ── Write bug_classes.csv ──
    csv_bugs_path = OUTPUT_DIR / "bug_classes.csv"
    with open(csv_bugs_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "campaign_id", "sqlite_version", "run", "hash",
            "type", "subtype", "key_function", "class_id", "count"
        ])
        writer.writeheader()
        writer.writerows(bug_rows)
    print(f"Written: {csv_bugs_path}")

    # ── Build registry.json ──
    registry_classes = []
    for (subtype, key_fn), entry in sorted(class_agg.items(), key=lambda x: x[1]["class_id"]):
        registry_classes.append({
            "class_id": entry["class_id"],
            "name": entry["name"],
            "subtype": entry["subtype"],
            "key_function": entry["key_function"],
            "severity": entry["severity"],
            "cve": entry["cve"],
            "versions": sorted(entry["versions"]),
            "total_crashes": entry["total_crashes"],
            "unique_hashes": len(entry["hashes"]),
            "hashes": sorted(entry["hashes"]),
        })

    registry = {
        "generated_at": "2026-05-19",
        "grammar": "v3.3",
        "experiment": "RQ2",
        "total_bug_classes": len(registry_classes),
        "campaigns_scanned": 20,
        "classes": registry_classes,
    }

    registry_path = OUTPUT_DIR / "registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"Written: {registry_path}")

    # ── Step 5: Report Summary ──
    print("\n" + "="*70)
    print("=== STEP 5: SUMMARY REPORT ===")
    print("="*70)

    print(f"\nTotal campaigns: {len(campaigns)}")

    # Per-version crash counts
    print("\nPer-version crash counts (AFL harness total):")
    for v in VERSIONS:
        vcamps = [c for c in campaigns if c["sqlite_version"] == v]
        totals = [c["total_crashes"] for c in vcamps]
        mean = statistics.mean(totals)
        std = statistics.stdev(totals) if len(totals) > 1 else 0.0
        print(f"  sqlite-{v}: mean={mean:.1f}, std={std:.1f}, runs={totals}")

    print("\nPer-version UBSan/ASan crash counts (test harness):")
    for v in VERSIONS:
        vcamps = [c for c in campaigns if c["sqlite_version"] == v]
        ubsans = [c["ubsan_count"] for c in vcamps]
        asans = [c["asan_count"] for c in vcamps]
        total_san = [u + a for u, a in zip(ubsans, asans)]
        mean = statistics.mean(total_san)
        std = statistics.stdev(total_san) if len(total_san) > 1 else 0.0
        print(f"  sqlite-{v}: ubsan+asan total mean={mean:.1f}, std={std:.1f}, per-run={total_san}")

    # Bug class table
    print("\n" + "-"*70)
    print(f"Bug class table ({len(registry_classes)} unique classes found in RQ2):")
    print("-"*70)
    known_ids = set(KNOWN_CLASSES.values())
    cve_matches = 0
    novel = 0
    for cls in registry_classes:
        is_known = cls["class_id"] in known_ids
        has_cve = cls["cve"] is not None
        status = "CVE" if has_cve else ("RQ1-known" if is_known else "NEW")
        if has_cve:
            cve_matches += 1
        elif not is_known:
            novel += 1
        versions_str = ", ".join(cls["versions"])
        print(f"  {cls['class_id']:8s} | {cls['name'][:45]:45s} | {cls['subtype']:30s} | "
              f"v={versions_str:25s} | hashes={cls['unique_hashes']:3d} | crashes={cls['total_crashes']:6d} | {status}")

    print(f"\nCVE matches: {cve_matches}")
    print(f"RQ1-known (non-CVE): {len(registry_classes) - cve_matches - novel}")
    print(f"NEW bug classes (not in RQ1): {novel}")

    if novel > 0:
        print("\n  NEW classes details:")
        for cls in registry_classes:
            if cls["class_id"] not in known_ids and cls["cve"] is None:
                print(f"    {cls['class_id']}: {cls['name']}")
                print(f"      subtype={cls['subtype']}, key_fn={cls['key_function']}")
                print(f"      versions={cls['versions']}, crashes={cls['total_crashes']}, hashes={cls['unique_hashes']}")

    print("\n" + "="*70)
    print("STATUS: DONE")
    print("="*70)


if __name__ == "__main__":
    main()
