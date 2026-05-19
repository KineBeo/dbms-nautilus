#!/usr/bin/env python3
"""
Triage aggregator for RQ1 v35 campaigns.
Reads triage.json and triage_test.json for all 20 v35 workdirs,
produces campaigns_summary.csv and cve_hits.csv under results/rq1_v35/.
"""

import json
import csv
import os
import math
from pathlib import Path
from collections import defaultdict

BASE = Path("/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2")
WORKDIR = BASE / "workdirs"
OUT = BASE / "results" / "rq1_v35"
OUT.mkdir(parents=True, exist_ok=True)

VERSIONS = ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
GRAMMAR = "v35"

# CVE signatures
# CVE-2020-13434: sqlite3_str_vappendf signed-integer-overflow — known hashes from BC003
# CVE-2020-13435: BC006 hash 9411c5875a64a648 — confirmed via smoke test + PoC SQL match
#   PoC: "CREATE TABLE a(c UNIQUE); SELECT a.c FROM a JOIN a b ON 3=a.c NATURAL JOIN a WHERE..."
# CVE-2020-9327: BC010 hash 2b1da72f9048599c — sqlite3Select member access null-ptr
# CVE-2020-13871: BC002 hash 48cb7c287ece21f3 — misaligned-access in sqlite3WindowUnlinkFromSelect
# CVE-2020-15358: no confirmed hash; heap buffer read via INTERSECT subquery (weak signal only)
CVE_SIGS = {
    "CVE-2020-13871": {
        "versions": ["3.32.2"],
        "hash": "48cb7c287ece21f3",
        "function": "sqlite3WindowUnlinkFromSelect",
        "subtype": "misaligned-access",
    },
    "CVE-2020-13434": {
        # BC003 hashes: 767f16fdfbae8ba1, 1ca1c0159b42ae50, b43f365a68048314, 7264a343681aca95
        # Also confirmed in 3.30.1 and 3.32.0 (same code path)
        "versions": ["3.30.1", "3.31.1", "3.32.0"],
        "hash": None,
        "function": "sqlite3_str_vappendf",
        "subtype": "signed-integer-overflow",
    },
    "CVE-2020-9327": {
        # BC010 hash: 2b1da72f9048599c; requires generated col + UNIQUE + VIEW + JOIN
        "versions": ["3.31.1"],
        "hash": "2b1da72f9048599c",
        "function": "sqlite3Select",
        "subtype": "null-pointer",
    },
    "CVE-2020-13435": {
        # BC006 hash 9411c5875a64a648 confirmed by smoke test and exact PoC SQL match
        "versions": ["3.32.0"],
        "hash": "9411c5875a64a648",
        "function": "sqlite3ExprCodeTarget",
        "subtype": "null-pointer",
    },
    "CVE-2020-15358": {
        # No confirmed hash; heap buffer read via INTERSECT subquery
        # signal-6 crashes with INTERSECT SQL are weak evidence only
        "versions": ["3.32.2"],
        "hash": None,
        "function": None,
        "subtype": None,
        "sql_pattern": "INTERSECT",
    },
}

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"  [WARN] JSON parse error in {path}: {e}")
        return None

def match_cve(cve_id, sig, crashes_afl, crashes_test):
    """Try to find evidence of CVE in either crash set. Returns (found, evidence)."""
    all_crashes = list(crashes_test or []) + list(crashes_afl or [])

    for c in all_crashes:
        # Hash match (most specific)
        if sig.get("hash") and c.get("hash", "").startswith(sig["hash"][:8]):
            return True, f"hash={c['hash']}"

        # Full hash match
        if sig.get("hash") and c.get("hash") == sig["hash"]:
            return True, f"hash={c['hash']}"

    # Function + subtype match (test harness is more reliable)
    for c in (crashes_test or []):
        frames = c.get("top_frames", [])
        frame_str = " ".join(frames)
        subtype_match = (not sig.get("subtype")) or (c.get("subtype") == sig.get("subtype"))

        if sig.get("function") and sig["function"] in frame_str and subtype_match:
            snippet = c.get("sql_preview", "")[:60]
            return True, f"func={sig['function']} subtype={c.get('subtype')} sql={snippet!r}"

        # SQL pattern match
        if sig.get("sql_pattern"):
            sql = c.get("sql_preview", "")
            if sig["sql_pattern"].lower() in sql.lower():
                if subtype_match or not sig.get("subtype"):
                    snippet = sql[:80]
                    return True, f"sql_pattern={sig['sql_pattern']} sql={snippet!r}"

    # Also check AFL triage for SQL patterns (debug_assert level)
    if sig.get("sql_pattern"):
        for c in (crashes_afl or []):
            sql = c.get("sql_preview", "")
            if sig["sql_pattern"].lower() in sql.lower():
                return True, f"sql_pattern(afl)={sig['sql_pattern']} sql={sql[:80]!r}"

    return False, ""

# ---- Step 1: Collect all 20 workdirs ----
expected = []
for ver in VERSIONS:
    for run in range(1, 6):
        expected.append(f"sqlite-{ver}_v35_run{run}")

present = []
missing = []
for name in expected:
    p = WORKDIR / name
    if p.exists():
        present.append(name)
    else:
        missing.append(name)

print("=== Step 1: Workdir Inventory ===")
print(f"Expected: {len(expected)}, Present: {len(present)}, Missing: {len(missing)}")
if missing:
    for m in missing:
        print(f"  MISSING: {m}")
else:
    print("  All 20 workdirs present.")

# ---- Step 2 + 3: Aggregate crash data and CVE matching ----
print("\n=== Step 2+3: Aggregating crash data ===")

summary_rows = []
cve_rows = []

per_version_totals = defaultdict(list)

for name in sorted(present):
    parts = name.split("_")
    # sqlite-3.31.1_v35_run1
    ver = parts[0].replace("sqlite-", "")
    grammar_tag = parts[1]  # v35
    run_num = int(parts[2].replace("run", ""))
    campaign_id = name

    wd = WORKDIR / name
    triage_afl = load_json(wd / "triage.json")
    triage_test = load_json(wd / "triage_test.json")

    # AFL triage summary
    if triage_afl:
        summ = triage_afl.get("summary", {})
        total = triage_afl.get("total_crashes", 0)
        da = summ.get("debug_assert", 0)
        sig = summ.get("signal", 0)
        asan_afl = summ.get("asan", 0)
        ubsan_afl = summ.get("ubsan", 0)
        crashes_afl = triage_afl.get("crashes", [])
    else:
        total = da = sig = asan_afl = ubsan_afl = 0
        crashes_afl = []

    # Test harness triage (UBSan/ASan — primary source)
    if triage_test:
        test_summ = triage_test.get("summary", {})
        ubsan_test = test_summ.get("ubsan", 0)
        asan_test = test_summ.get("asan", 0)
        crashes_test = triage_test.get("crashes", [])
    else:
        ubsan_test = asan_test = 0
        crashes_test = []

    # Prefer test harness counts for ubsan/asan
    ubsan_count = ubsan_test if triage_test else ubsan_afl
    asan_count = asan_test if triage_test else asan_afl

    per_version_totals[ver].append(total)

    summary_rows.append({
        "campaign_id": campaign_id,
        "grammar": grammar_tag,
        "sqlite_version": ver,
        "run": run_num,
        "total_crashes": total,
        "debug_assert_count": da,
        "signal_count": sig,
        "ubsan_count": ubsan_count,
        "asan_count": asan_count,
    })

    # Print interesting ubsan/asan crashes
    interesting = [c for c in crashes_test if c["type"] in ("ubsan", "asan")]
    if interesting:
        print(f"\n  {campaign_id}: {len(interesting)} ubsan/asan unique crashes")
        for c in interesting:
            frames_short = c.get("top_frames", ["?"])[:2]
            print(f"    [{c['type']}:{c.get('subtype','?')}] hash={c['hash']} count={c['count']}")
            print(f"      frames: {frames_short}")
            sql = c.get("sql_preview", "")[:100]
            print(f"      sql: {sql!r}")

    # CVE matching
    for cve_id, sig in CVE_SIGS.items():
        if ver not in sig["versions"]:
            # Mark as N/A (wrong version)
            cve_rows.append({
                "campaign_id": campaign_id,
                "sqlite_version": ver,
                "run": run_num,
                "cve_id": cve_id,
                "found": "N/A",
                "evidence": "wrong_version",
            })
            continue

        found, evidence = match_cve(cve_id, sig, crashes_afl, crashes_test)
        cve_rows.append({
            "campaign_id": campaign_id,
            "sqlite_version": ver,
            "run": run_num,
            "cve_id": cve_id,
            "found": "yes" if found else "no",
            "evidence": evidence,
        })

# ---- Step 4: Write CSVs ----
summary_path = OUT / "campaigns_summary.csv"
cve_path = OUT / "cve_hits.csv"

with open(summary_path, "w", newline="") as f:
    cols = ["campaign_id","grammar","sqlite_version","run","total_crashes",
            "debug_assert_count","signal_count","ubsan_count","asan_count"]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(summary_rows)
print(f"\nWrote {summary_path}")

with open(cve_path, "w", newline="") as f:
    cols = ["campaign_id","sqlite_version","run","cve_id","found","evidence"]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(cve_rows)
print(f"Wrote {cve_path}")

# ---- Step 5: Print summary report ----
print("\n" + "="*60)
print("=== Step 5: Summary Report ===")
print(f"Total campaigns: {len(present)}")
print()

def mean_std(vals):
    n = len(vals)
    if n == 0:
        return 0.0, 0.0
    m = sum(vals) / n
    if n == 1:
        return m, 0.0
    var = sum((x - m)**2 for x in vals) / (n - 1)
    return m, math.sqrt(var)

print("Per-version crash counts (total_crashes mean ± std):")
for ver in VERSIONS:
    vals = per_version_totals[ver]
    m, s = mean_std(vals)
    print(f"  sqlite-{ver}: {vals} → mean={m:.1f} ± {s:.1f}")

print()
print("CVE Rediscovery Matrix:")
print(f"{'CVE':<22} {'Version':<12} {'Run1':>5} {'Run2':>5} {'Run3':>5} {'Run4':>5} {'Run5':>5}")
print("-" * 65)

for cve_id, sig in CVE_SIGS.items():
    for ver in sig["versions"]:
        row_hits = []
        evidences = []
        for run in range(1, 6):
            cid = f"sqlite-{ver}_v35_run{run}"
            match = [r for r in cve_rows if r["campaign_id"] == cid and r["cve_id"] == cve_id]
            if match:
                r = match[0]
                row_hits.append("YES" if r["found"] == "yes" else "no")
                if r["found"] == "yes":
                    evidences.append(f"run{run}: {r['evidence'][:60]}")
            else:
                row_hits.append("?")
        line = f"  {cve_id:<20} {ver:<12}"
        for h in row_hits:
            line += f" {h:>5}"
        print(line)
        for ev in evidences:
            print(f"    Evidence: {ev}")

# New/unexpected crash classes
print()
print("Unique UBSan/ASan crash classes across all campaigns:")
seen_classes = {}
for name in sorted(present):
    wd = WORKDIR / name
    triage_test = load_json(wd / "triage_test.json")
    if not triage_test:
        continue
    for c in triage_test.get("crashes", []):
        if c["type"] not in ("ubsan", "asan"):
            continue
        key = (c.get("subtype"), tuple(c.get("top_frames", [])[:2]))
        if key not in seen_classes:
            seen_classes[key] = {"campaigns": [], "count": 0, "hash": c["hash"]}
        seen_classes[key]["campaigns"].append(name)
        seen_classes[key]["count"] += c["count"]

for key, info in sorted(seen_classes.items(), key=lambda x: -x[1]["count"]):
    subtype, frames = key
    print(f"  [{subtype}] hash_sample={info['hash']} total_count={info['count']}")
    print(f"    frames: {list(frames)}")
    print(f"    campaigns: {info['campaigns'][:3]}{'...' if len(info['campaigns'])>3 else ''}")
