#!/usr/bin/env python3
"""
Bug Verification Matrix: run every bug class trigger against every SQLite
version harness (test + nosanit) and produce a complete verification matrix.

Output:
  - results/ch4_final/bug_verification_matrix.csv
  - results/ch4_final/bug_verification_report.md
  - stdout summary
"""

import csv
import json
import os
import subprocess
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
CRASHES_DIR = ROOT / "results" / "crashes_v33_fresh"
HARNESS_TEST = ROOT / "harness" / "test"
HARNESS_NOSANIT = ROOT / "harness" / "nosanit"
OUTPUT_DIR = ROOT / "results" / "ch4_final"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VERSIONS = [
    "3.26.0", "3.27.0", "3.27.1", "3.27.2",
    "3.28.0", "3.29.0", "3.30.0", "3.30.1",
    "3.31.1", "3.32.0", "3.32.1", "3.32.2",
    "3.32.3", "3.33.0", "3.34.0", "3.36.0",
    "3.39.1", "3.40.0", "3.53.0",
]

TIMEOUT_SEC = 10


def classify_exit(exit_code, timed_out):
    """Classify harness result from exit code.

    Python subprocess returns negative values for signal deaths:
      -11 = SIGSEGV, -6 = SIGABRT
    The timeout command returns 128+signal:
      139 = SIGSEGV, 134 = SIGABRT
    Handle both conventions.
    """
    if timed_out:
        return "HANG"
    if exit_code == 0:
        return "OK"
    if exit_code == 1:
        return "UBSan"
    if exit_code in (134, -6):
        return "SIGABRT"
    if exit_code in (139, -11):
        return "SEGV"
    if exit_code == 223:
        return "ASan"
    return f"CRASH({exit_code})"


def is_crash(status):
    """Return True if the status indicates any kind of crash/error."""
    return status not in ("OK",)


def run_harness(harness_path, trigger_path):
    """Run a harness binary with the trigger file, return (exit_code, stderr_preview, timed_out)."""
    if not harness_path.exists():
        return (-1, "HARNESS_NOT_FOUND", False)

    try:
        result = subprocess.run(
            ["timeout", str(TIMEOUT_SEC), str(harness_path), str(trigger_path)],
            capture_output=True,
            timeout=TIMEOUT_SEC + 5,  # extra buffer beyond the `timeout` command
        )
        stderr_text = result.stderr.decode("utf-8", errors="replace").strip()
        stderr_lines = stderr_text.split("\n")[:3]
        stderr_preview = " | ".join(line.strip() for line in stderr_lines if line.strip())

        # timeout command returns 124 when it kills the child
        timed_out = result.returncode == 124
        return (result.returncode, stderr_preview, timed_out)
    except subprocess.TimeoutExpired:
        return (124, "TIMEOUT", True)
    except Exception as e:
        return (-1, f"ERROR: {e}", False)


def load_registry():
    """Load the crash registry JSON."""
    registry_path = CRASHES_DIR / "registry.json"
    with open(registry_path) as f:
        return json.load(f)


def get_trigger_for_bug_class(bc_dir):
    """Get the first trigger.sql (first hash subdir alphabetically)."""
    subdirs = sorted([
        d for d in bc_dir.iterdir()
        if d.is_dir() and (d / "trigger.sql").exists()
    ], key=lambda d: d.name)
    if not subdirs:
        return None
    return subdirs[0] / "trigger.sql"


def main():
    registry = load_registry()
    classes = registry["classes"]

    # Build lookup from class_id
    class_info = {}
    for c in classes:
        class_info[c["class_id"]] = c

    # Discover bug classes on disk
    bc_dirs = sorted([
        d for d in CRASHES_DIR.iterdir()
        if d.is_dir() and d.name.startswith("BC")
    ], key=lambda d: d.name)

    # Prepare CSV rows
    csv_rows = []
    # summary data: bc_id -> { "test": {ver: status}, "nosanit": {ver: status} }
    summary = OrderedDict()

    total_runs = len(bc_dirs) * len(VERSIONS) * 2
    completed = 0

    for bc_dir in bc_dirs:
        bc_name = bc_dir.name
        bc_id = bc_name.split("_")[0]  # e.g. "BC001"
        info = class_info.get(bc_id, {})
        key_function = info.get("key_function", "unknown")
        subtype = info.get("subtype", "unknown")
        cve = info.get("cve", None)

        trigger = get_trigger_for_bug_class(bc_dir)
        if trigger is None:
            print(f"WARNING: No trigger.sql found for {bc_name}", file=sys.stderr)
            continue

        summary[bc_id] = {
            "name": bc_name,
            "key_function": key_function,
            "subtype": subtype,
            "cve": cve,
            "test": OrderedDict(),
            "nosanit": OrderedDict(),
        }

        for version in VERSIONS:
            for harness_type in ["test", "nosanit"]:
                completed += 1
                if harness_type == "test":
                    harness_path = HARNESS_TEST / f"sqlite_harness_sqlite-{version}_test"
                else:
                    harness_path = HARNESS_NOSANIT / f"sqlite_harness_sqlite-{version}_nosanit"

                exit_code, stderr_preview, timed_out = run_harness(harness_path, trigger)
                status = classify_exit(exit_code, timed_out)

                # Progress
                pct = completed * 100 // total_runs
                print(f"\r  [{pct:3d}%] {bc_id} | {version} | {harness_type:7s} | {status}",
                      end="", flush=True)

                summary[bc_id][harness_type][version] = status

                csv_rows.append({
                    "bug_class": bc_id,
                    "key_function": key_function,
                    "subtype": subtype,
                    "version": version,
                    "harness_type": harness_type,
                    "exit_code": exit_code,
                    "status": status,
                    "stderr_preview": stderr_preview[:200],
                })

    print()  # newline after progress

    # ── Write CSV ──────────────────────────────────────────────────────────
    csv_path = OUTPUT_DIR / "bug_verification_matrix.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "bug_class", "key_function", "subtype", "version",
            "harness_type", "exit_code", "status", "stderr_preview",
        ])
        writer.writeheader()
        writer.writerows(csv_rows)
    print(f"\nCSV written: {csv_path}")

    # ── Stdout Summary ─────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("BUG VERIFICATION MATRIX SUMMARY")
    print("=" * 80)

    classification_results = {}

    for bc_id, data in summary.items():
        cve_str = f" [CVE: {data['cve']}]" if data["cve"] else ""
        print(f"\n{bc_id} ({data['key_function']} / {data['subtype']}){cve_str}")

        test_crashes = [v for v in VERSIONS if is_crash(data["test"].get(v, "OK"))]
        nosanit_crashes = [v for v in VERSIONS if is_crash(data["nosanit"].get(v, "OK"))]

        # Detailed crash types for test
        test_details = []
        for v in VERSIONS:
            s = data["test"].get(v, "OK")
            if is_crash(s):
                test_details.append(f"{v}({s})")

        nosanit_details = []
        for v in VERSIONS:
            s = data["nosanit"].get(v, "OK")
            if is_crash(s):
                nosanit_details.append(f"{v}({s})")

        print(f"  Test crashes:    {' '.join(test_details) if test_details else 'NONE'}")
        print(f"  Nosanit crashes: {' '.join(nosanit_details) if nosanit_details else 'NONE'}")

        # Find fix version: first version where BOTH test and nosanit are OK
        fix_version = None
        # We look for the first version after any crash where both are clean
        found_any_crash = False
        for v in VERSIONS:
            t = data["test"].get(v, "OK")
            n = data["nosanit"].get(v, "OK")
            if is_crash(t) or is_crash(n):
                found_any_crash = True
            elif found_any_crash:
                fix_version = v
                break

        if fix_version:
            print(f"  Fix version:     {fix_version} (first version with no crash on both)")
        elif found_any_crash:
            # Check if it's still crashing on latest
            last_t = data["test"].get(VERSIONS[-1], "OK")
            last_n = data["nosanit"].get(VERSIONS[-1], "OK")
            if is_crash(last_t) or is_crash(last_n):
                print(f"  Fix version:     NOT FIXED (still crashes on {VERSIONS[-1]})")
            else:
                # Crashes only on non-contiguous versions? Find the actual fix
                print(f"  Fix version:     COMPLEX (non-contiguous crash pattern)")
        else:
            print(f"  Fix version:     N/A (no crashes found)")

        # ── Classification ─────────────────────────────────────────────────
        has_cve = data["cve"] is not None
        has_nosanit_crash = len(nosanit_crashes) > 0
        has_test_crash = len(test_crashes) > 0
        test_only = has_test_crash and not has_nosanit_crash

        # Check nosanit crash types
        nosanit_segv = any(data["nosanit"].get(v) == "SEGV" for v in VERSIONS)
        nosanit_sigabrt = any(data["nosanit"].get(v) == "SIGABRT" for v in VERSIONS)

        if has_cve:
            classification = "Known CVE"
        elif test_only:
            # Only sanitizer catches it
            classification = "Sanitizer-only"
        elif has_nosanit_crash and fix_version:
            classification = "Silently fixed"
        elif has_nosanit_crash:
            classification = "Real crash (unfixed)"
        elif not has_test_crash:
            classification = "No crash (false positive?)"
        else:
            classification = "Sanitizer-only"

        # Exploitability note
        if nosanit_segv:
            exploit_note = "SEGV on nosanit = potentially exploitable"
        elif nosanit_sigabrt:
            exploit_note = "SIGABRT on nosanit = denial of service"
        elif test_only:
            exploit_note = "sanitizer-only detection, no production impact"
        else:
            exploit_note = ""

        classification_results[bc_id] = {
            "classification": classification,
            "exploit_note": exploit_note,
            "fix_version": fix_version,
            "test_crashes": test_crashes,
            "nosanit_crashes": nosanit_crashes,
        }

        print(f"  Classification:  {classification}")
        if exploit_note:
            print(f"  Exploitability:  {exploit_note}")

    # ── Classification Summary ─────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("CLASSIFICATION SUMMARY")
    print("=" * 80)

    categories = {}
    for bc_id, cr in classification_results.items():
        cat = cr["classification"]
        categories.setdefault(cat, []).append(bc_id)

    for cat, bugs in sorted(categories.items()):
        print(f"\n  {cat}:")
        for bc_id in bugs:
            info = summary[bc_id]
            print(f"    {bc_id} - {info['key_function']} ({info['subtype']})")

    # ── Write Report ───────────────────────────────────────────────────────
    report_path = OUTPUT_DIR / "bug_verification_report.md"
    with open(report_path, "w") as f:
        f.write("# Bug Verification Matrix Report\n\n")
        f.write(f"Generated: {subprocess.check_output(['date', '-Iseconds']).decode().strip()}\n\n")
        f.write(f"- **Bug classes tested:** {len(summary)}\n")
        f.write(f"- **SQLite versions:** {len(VERSIONS)} ({VERSIONS[0]} -- {VERSIONS[-1]})\n")
        f.write(f"- **Total test runs:** {len(csv_rows)}\n\n")

        # Overview table
        f.write("## Classification Summary\n\n")
        f.write("| Category | Count | Bug Classes |\n")
        f.write("|----------|-------|-------------|\n")
        for cat, bugs in sorted(categories.items()):
            bug_list = ", ".join(bugs)
            f.write(f"| {cat} | {len(bugs)} | {bug_list} |\n")
        f.write("\n")

        # Per-bug detail
        f.write("## Per-Bug Detail\n\n")
        for bc_id, data in summary.items():
            cr = classification_results[bc_id]
            cve_str = f" \\[{data['cve']}\\]" if data["cve"] else ""
            f.write(f"### {bc_id}: {data['key_function']} ({data['subtype']}){cve_str}\n\n")
            f.write(f"- **Classification:** {cr['classification']}\n")
            if cr["exploit_note"]:
                f.write(f"- **Exploitability:** {cr['exploit_note']}\n")
            if cr["fix_version"]:
                f.write(f"- **Fix version:** {cr['fix_version']}\n")
            f.write("\n")

            # Version matrix table
            f.write("| Version | Test | Nosanit |\n")
            f.write("|---------|------|---------|\n")
            for v in VERSIONS:
                t = data["test"].get(v, "N/A")
                n = data["nosanit"].get(v, "N/A")
                # Bold crashes
                t_fmt = f"**{t}**" if is_crash(t) else t
                n_fmt = f"**{n}**" if is_crash(n) else n
                f.write(f"| {v} | {t_fmt} | {n_fmt} |\n")
            f.write("\n")

        # Full heat map
        f.write("## Full Matrix (Compact)\n\n")
        f.write("Legend: `.` = OK, `U` = UBSan, `S` = SEGV, `A` = SIGABRT, `X` = ASan, `H` = HANG, `?` = other\n\n")

        status_char = {
            "OK": ".",
            "UBSan": "U",
            "SEGV": "S",
            "SIGABRT": "A",
            "ASan": "X",
            "HANG": "H",
        }

        # Header
        f.write(f"| Bug Class | {'| '.join(VERSIONS)} |\n")
        f.write(f"|-----------|{'|'.join(['---' for _ in VERSIONS])}|\n")

        for bc_id, data in summary.items():
            # Test row
            cells = []
            for v in VERSIONS:
                s = data["test"].get(v, "OK")
                cells.append(status_char.get(s, "?"))
            f.write(f"| {bc_id} test | {'| '.join(cells)} |\n")

            # Nosanit row
            cells = []
            for v in VERSIONS:
                s = data["nosanit"].get(v, "OK")
                cells.append(status_char.get(s, "?"))
            f.write(f"| {bc_id} nosanit | {'| '.join(cells)} |\n")

        f.write("\n---\n\n")
        f.write("*Report generated by `scripts/verify_bug_matrix.py`*\n")

    print(f"\nReport written: {report_path}")
    print(f"CSV written:    {csv_path}")
    print(f"\nDone. {len(csv_rows)} total test runs across {len(summary)} bug classes x {len(VERSIONS)} versions x 2 harness types.")


if __name__ == "__main__":
    main()
