#!/usr/bin/env python3
"""
RQ2 Single Source of Truth
==========================
Run every BC trigger + every CVE PoC against all 19 SQLite versions (test + nosanit),
compare crash signatures, classify bugs, and produce one authoritative markdown report.

Output: results/ch4_final/rq2_source_of_truth.md

Usage: python3 scripts/rq2_source_of_truth.py
"""

import csv
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINIMIZE_DIR = ROOT / "results" / "minimize_v33"
HARNESS_TEST = ROOT / "harness" / "test"
HARNESS_NOSANIT = ROOT / "harness" / "nosanit"
CH4_DIR = ROOT / "results" / "ch4_final"
OUTPUT_PATH = CH4_DIR / "rq2_source_of_truth.md"

VERSIONS = [
    "3.26.0", "3.27.0", "3.27.1", "3.27.2",
    "3.28.0", "3.29.0", "3.30.0", "3.30.1",
    "3.31.1", "3.32.0", "3.32.1", "3.32.2",
    "3.32.3", "3.33.0", "3.34.0", "3.36.0",
    "3.39.1", "3.40.0", "3.53.0",
]

TIMEOUT_SEC = 10
MAX_LOG_LINES = 20


@dataclass
class CrashResult:
    version: str
    harness_type: str  # "test" or "nosanit"
    exit_code: int
    status: str  # OK, UBSan, ASan, SEGV, SIGABRT, HANG
    crash_line: str  # e.g. "101292" or ""
    crash_function: str  # e.g. "sqlite3ExprCodeTarget" or ""
    error_type: str  # e.g. "null pointer", "signed integer overflow"
    full_log: str  # full stderr, trimmed to MAX_LOG_LINES


@dataclass
class BugClass:
    bc_id: str
    label: str
    sql_file: str
    results: list = field(default_factory=list)
    ebnf_found: bool = False
    ebnf_versions: str = ""
    ebnf_hashes: int = 0
    dbms_hashes: int = 0
    dbms_total_crashes: int = 0
    cve_matches: dict = field(default_factory=dict)


@dataclass
class CVEPoC:
    cve_id: str
    sql_file: str
    results: list = field(default_factory=list)


def run_harness(harness_path: Path, sql_path: Path) -> CrashResult:
    """Run harness, return structured result with full log."""
    if not harness_path.exists():
        return CrashResult(
            version="", harness_type="", exit_code=-1,
            status="NO_HARNESS", crash_line="", crash_function="",
            error_type="", full_log="harness not found"
        )

    try:
        result = subprocess.run(
            ["timeout", str(TIMEOUT_SEC), str(harness_path), str(sql_path)],
            capture_output=True, timeout=TIMEOUT_SEC + 5,
        )
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        ec = result.returncode
        timed_out = ec == 124
    except subprocess.TimeoutExpired:
        return CrashResult(
            version="", harness_type="", exit_code=124,
            status="HANG", crash_line="", crash_function="",
            error_type="", full_log="TIMEOUT"
        )
    except Exception as e:
        return CrashResult(
            version="", harness_type="", exit_code=-1,
            status="ERROR", crash_line="", crash_function="",
            error_type="", full_log=str(e)
        )

    # Trim log
    lines = stderr.split("\n")
    if len(lines) > MAX_LOG_LINES:
        trimmed = "\n".join(lines[:MAX_LOG_LINES]) + f"\n... ({len(lines) - MAX_LOG_LINES} more lines)"
    else:
        trimmed = stderr

    # Classify status
    if timed_out:
        status = "HANG"
    elif ec == 0 and not stderr:
        status = "OK"
    elif ec == 0 and stderr:
        status = "OK_WITH_OUTPUT"
    elif ec == 1:
        status = "UBSan"
    elif ec in (134, -6):
        status = "SIGABRT"
    elif ec in (139, -11):
        status = "SEGV"
    elif ec == 223:
        status = "ASan"
    else:
        status = f"EXIT_{ec}"

    # Extract crash details
    crash_line = ""
    crash_function = ""
    error_type = ""

    # UBSan: sqlite3.c:LINE:COL: runtime error: MESSAGE
    m = re.search(r'sqlite3\.c:(\d+):\d+: runtime error: (.+)', stderr)
    if m:
        crash_line = m.group(1)
        error_type = m.group(2).strip()
        if status == "OK_WITH_OUTPUT":
            status = "UBSan"

    # ASan: ERROR: AddressSanitizer: TYPE ...
    m_asan = re.search(r'ERROR: AddressSanitizer: (\S+)', stderr)
    if m_asan:
        error_type = m_asan.group(1)
        status = "ASan"

    # Function from ASan stack: #0 ... in FUNC
    m_func = re.search(r'#0 .* in (\w+)', stderr)
    if m_func:
        crash_function = m_func.group(1)

    # Also try to get line from ASan stack
    if not crash_line:
        m_line = re.search(r'sqlite3\.c:(\d+)', stderr)
        if m_line:
            crash_line = m_line.group(1)

    # For SEGV without ASan details
    if status == "SEGV" and not error_type:
        error_type = "SEGV"
    if status == "SIGABRT" and not error_type:
        error_type = "SIGABRT"

    return CrashResult(
        version="", harness_type="",
        exit_code=ec, status=status,
        crash_line=crash_line, crash_function=crash_function,
        error_type=error_type, full_log=trimmed,
    )


def load_ebnf_data() -> dict:
    """Load EBNF bug class data from CSV."""
    path = CH4_DIR / "rq2_ebnf_bug_classes.csv"
    data = {}
    if path.exists():
        with open(path) as f:
            for row in csv.DictReader(f):
                data[row["class_id"]] = {
                    "versions": row.get("versions", ""),
                    "hashes": int(row.get("unique_hashes", 0)),
                }
    return data


def load_dbms_data() -> dict:
    """Load DBMS-Nautilus bug class data from CSV."""
    path = CH4_DIR / "rq2_bug_classes.csv"
    data = {}
    if path.exists():
        with open(path) as f:
            for row in csv.DictReader(f):
                data[row["class_id"]] = {
                    "hashes": int(row.get("unique_hashes", 0)),
                    "total_crashes": int(row.get("total_crashes", 0)),
                }
    return data


def discover_bc_files() -> list[BugClass]:
    """Find all BC trigger SQL files in minimize_v33."""
    bcs = []
    for f in sorted(MINIMIZE_DIR.glob("BC*.sql")):
        bc_id = f.name.split("_")[0]
        label = f.stem.replace(f"{bc_id}_", "").replace("_", " ")
        bcs.append(BugClass(bc_id=bc_id, label=label, sql_file=str(f)))
    return bcs


def discover_cve_files() -> list[CVEPoC]:
    """Find all CVE PoC SQL files in minimize_v33."""
    cves = []
    for f in sorted(MINIMIZE_DIR.glob("CVE-*.sql")):
        cve_id = f.stem.replace("_poc", "")
        cves.append(CVEPoC(cve_id=cve_id, sql_file=str(f)))
    return cves


def run_all(items: list, item_type: str) -> None:
    """Run all items against all versions and harness types."""
    total = len(items) * len(VERSIONS) * (2 if item_type == "bc" else 1)
    done = 0

    for item in items:
        harness_types = ["test", "nosanit"] if item_type == "bc" else ["test"]
        for ver in VERSIONS:
            for ht in harness_types:
                done += 1
                pct = done * 100 // total
                name = item.bc_id if item_type == "bc" else item.cve_id
                print(f"\r  [{pct:3d}%] {name:16s} | {ver:8s} | {ht:7s}", end="", flush=True)

                if ht == "test":
                    harness = HARNESS_TEST / f"sqlite_harness_sqlite-{ver}_test"
                else:
                    harness = HARNESS_NOSANIT / f"sqlite_harness_sqlite-{ver}_nosanit"

                r = run_harness(harness, Path(item.sql_file))
                r.version = ver
                r.harness_type = ht
                item.results.append(r)

    print()


def _normalize_error_category(error_type: str, status: str) -> str:
    """Normalize error type to a category for comparison."""
    e = error_type.lower()
    if "null pointer" in e or "zero offset to null" in e:
        return "null-pointer"
    if "integer overflow" in e:
        return "integer-overflow"
    if "misaligned" in e:
        return "misaligned-access"
    if "float" in e or "outside the range" in e:
        return "float-cast-overflow"
    if "heap-use-after-free" in e:
        return "heap-uaf"
    if status == "SEGV":
        return "segv"
    if status == "SIGABRT":
        return "assertion"
    if status == "ASan":
        return "asan"
    return "other"


def match_cve(bc: BugClass, cve: CVEPoC) -> dict:
    """Compare BC and CVE crash signatures. Return match info.

    Requires: same crash line AND same specific error category on the same version.
    Assertion/SIGABRT matches are excluded — SQLITE_DEBUG assertions are too broad
    (many different bugs trip the same assertion on old versions).
    Line-only matches (different error type) are flagged as LINE_ONLY.
    """
    bc_test = {r.version: r for r in bc.results if r.harness_type == "test" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS")}
    cve_test = {r.version: r for r in cve.results if r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS")}

    full_matches = []
    line_only_matches = []

    for ver in VERSIONS:
        bc_r = bc_test.get(ver)
        cve_r = cve_test.get(ver)
        if bc_r and cve_r and bc_r.crash_line and cve_r.crash_line:
            line_diff = abs(int(bc_r.crash_line) - int(cve_r.crash_line))
            if line_diff <= 1:
                bc_cat = _normalize_error_category(bc_r.error_type, bc_r.status)
                cve_cat = _normalize_error_category(cve_r.error_type, cve_r.status)
                # Skip assertion matches — too broad
                if bc_cat == "assertion" or cve_cat == "assertion":
                    line_only_matches.append(ver)
                elif bc_cat == cve_cat:
                    full_matches.append(ver)
                else:
                    line_only_matches.append(ver)

    if not full_matches and not line_only_matches:
        return {"verdict": "NO_MATCH", "full_matches": [], "line_only_matches": [], "note": ""}

    # Check version range consistency
    bc_versions = set(bc_test.keys())
    cve_versions = set(cve_test.keys())
    bc_range = f"{min(bc_versions)}--{max(bc_versions)} ({len(bc_versions)} ver.)" if bc_versions else "none"
    cve_range = f"{min(cve_versions)}--{max(cve_versions)} ({len(cve_versions)} ver.)" if cve_versions else "none"

    range_consistent = len(bc_versions) <= len(cve_versions) * 2 and len(cve_versions) <= len(bc_versions) * 2

    if full_matches and range_consistent:
        verdict = "MATCH"
    elif full_matches:
        verdict = "PARTIAL_MATCH"
    elif line_only_matches:
        verdict = "LINE_ONLY"
    else:
        verdict = "NO_MATCH"

    note = f"BC range: {bc_range}, CVE range: {cve_range}"
    if line_only_matches and not full_matches:
        note += f" | LINE_ONLY: same line but different error type on {', '.join(line_only_matches[:3])}"

    return {
        "verdict": verdict,
        "full_matches": full_matches,
        "line_only_matches": line_only_matches,
        "note": note,
    }


def generate_report(bcs: list[BugClass], cves: list[CVEPoC]) -> str:
    """Generate the full markdown report."""
    lines = []
    w = lines.append

    w("# RQ2 Single Source of Truth")
    w("")
    w(f"Generated: {datetime.now().isoformat()}")
    w(f"Script: `scripts/rq2_source_of_truth.py`")
    w(f"Versions tested: {len(VERSIONS)} ({VERSIONS[0]} -- {VERSIONS[-1]})")
    w(f"Bug classes: {len(bcs)}")
    w(f"CVE PoCs: {len(cves)}")
    w("")

    # ── Section 1: Summary Table ──────────────────────────────────
    w("## 1. Bug Class Summary")
    w("")
    w("| BC | Bug Type | DBMS Versions | EBNF Versions | CVE Match | Prod SEGV? | Hashes (DBMS/EBNF) | Fix |")
    w("|-----|----------|---------------|---------------|-----------|------------|---------------------|-----|")

    for bc in bcs:
        test_crashes = [r.version for r in bc.results if r.harness_type == "test" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS")]
        nosanit_crashes = [r.version for r in bc.results if r.harness_type == "nosanit" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS")]

        # Unique crash versions
        test_vers = sorted(set(test_crashes))
        nosanit_vers = sorted(set(nosanit_crashes))

        # Find fix version
        fix = "---"
        found_crash = False
        for v in VERSIONS:
            t = any(r.version == v and r.harness_type == "test" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS") for r in bc.results)
            n = any(r.version == v and r.harness_type == "nosanit" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS") for r in bc.results)
            if t or n:
                found_crash = True
            elif found_crash:
                fix = v
                break

        # Best CVE match
        best_cve = "---"
        for cve_id, m in bc.cve_matches.items():
            if m["verdict"] == "MATCH":
                best_cve = f"**{cve_id}**"
                break
            elif m["verdict"] == "PARTIAL_MATCH" and best_cve == "---":
                best_cve = f"{cve_id}?"

        prod = "YES" if nosanit_vers else "no"
        ebnf_vers_str = bc.ebnf_versions if bc.ebnf_found else "---"
        hashes_str = f"{bc.dbms_hashes}/{bc.ebnf_hashes}" if bc.ebnf_found else f"{bc.dbms_hashes}/---"

        dbms_vers_str = ", ".join(test_vers[:6])
        if len(test_vers) > 6:
            dbms_vers_str += f" +{len(test_vers)-6}"

        w(f"| {bc.bc_id} | {bc.label[:35]} | {dbms_vers_str} | {ebnf_vers_str} | {best_cve} | {prod} | {hashes_str} | {fix} |")

    w("")

    # ── Section 2: CVE Match Matrix ──────────────────────────────
    w("## 2. CVE Match Matrix")
    w("")
    w("Match = same crash line on same version. PARTIAL = line matches but version range inconsistent.")
    w("")

    header = "| BC |"
    sep = "|-----|"
    for cve in cves:
        header += f" {cve.cve_id} |"
        sep += "---|"
    w(header)
    w(sep)

    for bc in bcs:
        row = f"| {bc.bc_id} |"
        for cve in cves:
            m = bc.cve_matches.get(cve.cve_id, {"verdict": "NO_MATCH"})
            if m["verdict"] == "MATCH":
                row += f" **MATCH** ({','.join(m['full_matches'][:2])}) |"
            elif m["verdict"] == "PARTIAL_MATCH":
                row += f" PARTIAL ({','.join(m['full_matches'][:2])}) |"
            elif m["verdict"] == "LINE_ONLY":
                row += f" LINE_ONLY ({','.join(m['line_only_matches'][:2])}) |"
            else:
                row += " --- |"
        w(row)

    w("")

    # ── Section 3: Production Impact Matrix ──────────────────────
    w("## 3. Production Impact (nosanit)")
    w("")
    w("Legend: `.` = OK, `S` = SEGV, `A` = SIGABRT, `-` = no harness")
    w("")

    header = "| BC |"
    sep = "|-----|"
    for v in VERSIONS:
        header += f" {v} |"
        sep += "---|"
    w(header)
    w(sep)

    status_char = {"OK": ".", "SEGV": "S", "SIGABRT": "A", "NO_HARNESS": "-",
                   "OK_WITH_OUTPUT": ".", "HANG": "H"}

    for bc in bcs:
        row = f"| {bc.bc_id} |"
        for v in VERSIONS:
            r = next((r for r in bc.results if r.version == v and r.harness_type == "nosanit"), None)
            if r:
                ch = status_char.get(r.status, "?")
                row += f" {ch} |"
            else:
                row += " - |"
        w(row)

    w("")

    # ── Section 4: Sanitizer Crash Matrix ────────────────────────
    w("## 4. Sanitizer Crash (test harness)")
    w("")
    w("Legend: `.` = OK, `U` = UBSan, `X` = ASan, `S` = SEGV, `A` = SIGABRT, `-` = no harness")
    w("")

    header = "| BC |"
    sep = "|-----|"
    for v in VERSIONS:
        header += f" {v} |"
        sep += "---|"
    w(header)
    w(sep)

    status_char2 = {"OK": ".", "UBSan": "U", "ASan": "X", "SEGV": "S",
                    "SIGABRT": "A", "NO_HARNESS": "-", "OK_WITH_OUTPUT": ".", "HANG": "H"}

    for bc in bcs:
        row = f"| {bc.bc_id} |"
        for v in VERSIONS:
            r = next((r for r in bc.results if r.version == v and r.harness_type == "test"), None)
            if r:
                ch = status_char2.get(r.status, "?")
                row += f" {ch} |"
            else:
                row += " - |"
        w(row)

    w("")

    # ── Section 5: CVE PoC Crash Signatures ──────────────────────
    w("## 5. CVE PoC Crash Signatures")
    w("")

    for cve in cves:
        w(f"### {cve.cve_id}")
        w("")
        for r in cve.results:
            if r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS"):
                w(f"**{r.version}** ({r.status}): L{r.crash_line} `{r.crash_function}` — {r.error_type[:80]}")
                if r.full_log:
                    w("```")
                    w(r.full_log)
                    w("```")
                    w("")
        w("")

    # ── Section 6: Per-BC Detail with Full Logs ──────────────────
    w("## 6. Per-Bug-Class Detail")
    w("")

    for bc in bcs:
        w(f"### {bc.bc_id}: {bc.label}")
        w("")

        # Best CVE match
        for cve_id, m in bc.cve_matches.items():
            if m["verdict"] != "NO_MATCH":
                matches_str = ', '.join(m['full_matches'][:3]) if m['full_matches'] else ', '.join(m['line_only_matches'][:3])
                w(f"- **CVE match:** {cve_id} → {m['verdict']} (versions: {matches_str})")
                w(f"  - {m['note']}")

        # EBNF
        if bc.ebnf_found:
            w(f"- **EBNF-Baseline:** YES (versions: {bc.ebnf_versions}, hashes: {bc.ebnf_hashes})")
        else:
            w(f"- **EBNF-Baseline:** not found")

        w(f"- **DBMS-Nautilus:** {bc.dbms_hashes} hashes, {bc.dbms_total_crashes} total crashes")
        w("")

        # Test harness crashes
        w("#### Sanitizer (test) crashes")
        w("")
        for r in bc.results:
            if r.harness_type == "test" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS"):
                w(f"**{r.version}** — {r.status} L{r.crash_line} `{r.crash_function}`")
                w(f"  Error: {r.error_type[:100]}")
                if r.full_log:
                    w("```")
                    w(r.full_log)
                    w("```")
                w("")

        # Nosanit crashes
        nosanit_crashes = [r for r in bc.results if r.harness_type == "nosanit" and r.status not in ("OK", "OK_WITH_OUTPUT", "NO_HARNESS")]
        if nosanit_crashes:
            w("#### Production (nosanit) crashes")
            w("")
            for r in nosanit_crashes:
                w(f"**{r.version}** — {r.status}")
                if r.full_log:
                    w("```")
                    w(r.full_log)
                    w("```")
                w("")
        else:
            w("#### Production (nosanit): no crashes on any version")
            w("")

        w("---")
        w("")

    # ── Section 7: Flags for Human Review ────────────────────────
    w("## 7. Flags for Human Review")
    w("")

    flags = []
    for bc in bcs:
        for cve_id, m in bc.cve_matches.items():
            if m["verdict"] == "MATCH":
                flags.append(f"- **{bc.bc_id} ↔ {cve_id}**: MATCH confirmed — {m['note']}")
            elif m["verdict"] == "PARTIAL_MATCH":
                flags.append(f"- **{bc.bc_id} ↔ {cve_id}**: PARTIAL_MATCH — {m['note']}")
            elif m["verdict"] == "LINE_ONLY":
                flags.append(f"- **{bc.bc_id} ↔ {cve_id}**: LINE_ONLY (same line, different error type) — {m['note']}")

    # Check for BCs that match multiple CVEs
    for bc in bcs:
        matches = [cid for cid, m in bc.cve_matches.items() if m["verdict"] in ("MATCH", "PARTIAL_MATCH")]
        if len(matches) > 1:
            flags.append(f"- **{bc.bc_id}**: matches MULTIPLE CVEs: {', '.join(matches)} — needs manual review")

    # Check for CVEs matched by multiple BCs
    for cve in cves:
        matching_bcs = [bc.bc_id for bc in bcs if bc.cve_matches.get(cve.cve_id, {}).get("verdict") in ("MATCH", "PARTIAL_MATCH")]
        if len(matching_bcs) > 1:
            flags.append(f"- **{cve.cve_id}**: matched by MULTIPLE BCs: {', '.join(matching_bcs)} — needs manual review")

    if flags:
        for f in flags:
            w(f)
    else:
        w("No flags.")

    w("")
    w("---")
    w(f"*Generated by `scripts/rq2_source_of_truth.py` at {datetime.now().isoformat()}*")

    return "\n".join(lines)


def main():
    print("=" * 60)
    print("  RQ2 Single Source of Truth")
    print(f"  {datetime.now().isoformat()}")
    print("=" * 60)

    # Discover files
    bcs = discover_bc_files()
    cves = discover_cve_files()
    print(f"\nFound {len(bcs)} BC triggers, {len(cves)} CVE PoCs")

    # Load existing data
    ebnf_data = load_ebnf_data()
    dbms_data = load_dbms_data()
    for bc in bcs:
        if bc.bc_id in ebnf_data:
            bc.ebnf_found = True
            bc.ebnf_versions = ebnf_data[bc.bc_id]["versions"]
            bc.ebnf_hashes = ebnf_data[bc.bc_id]["hashes"]
        if bc.bc_id in dbms_data:
            bc.dbms_hashes = dbms_data[bc.bc_id]["hashes"]
            bc.dbms_total_crashes = dbms_data[bc.bc_id]["total_crashes"]

    # Run all BCs
    print(f"\nRunning {len(bcs)} BCs × {len(VERSIONS)} versions × 2 harness types...")
    run_all(bcs, "bc")

    # Run all CVEs
    print(f"\nRunning {len(cves)} CVEs × {len(VERSIONS)} versions × 1 harness type...")
    run_all(cves, "cve")

    # CVE matching
    print("\nMatching BCs to CVEs...")
    for bc in bcs:
        for cve in cves:
            bc.cve_matches[cve.cve_id] = match_cve(bc, cve)

    # Generate report
    print("\nGenerating report...")
    report = generate_report(bcs, cves)

    CH4_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(report)

    print(f"\nOutput: {OUTPUT_PATH}")
    print(f"Size: {len(report)} chars, {report.count(chr(10))} lines")
    print("\nDone.")


if __name__ == "__main__":
    main()
