#!/usr/bin/env python3
"""
classify.py — Unified crash dedup + classification + report for SQLite fuzzing.

Replaces dedup.py and report.py. Single-pass tool: re-runs each crash once,
deduplicates by stack hash, classifies by exit code (ASan/UBSan/debug_assert),
and produces triage.json + dedup/ + triage_report.md.

Usage:
    python3 triage/classify.py <workdir> --harness <path>
    python3 triage/classify.py <workdir> --harness <path> --enrich campaign.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

DEDUP_FRAMES = 5


@dataclass(frozen=True)
class CrashResult:
    file_name: str
    exit_code: int
    crash_type: str
    subtype: str | None
    frames: tuple[str, ...]
    sql_preview: str
    stack_hash: str


@dataclass
class CrashCluster:
    stack_hash: str
    crash_type: str
    subtype: str | None
    exit_code: int
    count: int
    sample_file: str
    top_frames: list[str]
    sql_preview: str


def classify_crash(exit_code: int, stderr: str) -> tuple[str, str | None]:
    if "runtime error:" in stderr:
        m = re.search(r"runtime error:\s*(.+)", stderr)
        if m:
            kind = m.group(1).strip()
            if "signed integer overflow" in kind or "integer overflow" in kind:
                return ("ubsan", "signed-integer-overflow")
            if "null pointer" in kind:
                return ("ubsan", "null-pointer")
            if "misaligned address" in kind:
                return ("ubsan", "misaligned-access")
            if "outside the range of representable values" in kind:
                return ("ubsan", "float-cast-overflow")
            if "shift exponent" in kind:
                return ("ubsan", "shift-exponent")
            if "member access within null" in kind:
                return ("ubsan", "null-member-access")
            return ("ubsan", "ubsan-other")
        return ("ubsan", "ubsan-other")
    if exit_code == -1:
        return ("timeout", None)
    if exit_code == -5:
        return ("debug_assert", None)
    if exit_code < 0:
        return ("signal", f"signal-{abs(exit_code)}")
    if exit_code == 223:
        if "heap-buffer-overflow" in stderr:
            return ("asan", "heap-buffer-overflow")
        if "stack-buffer-overflow" in stderr:
            return ("asan", "stack-buffer-overflow")
        if "use-after-free" in stderr or "heap-use-after-free" in stderr:
            return ("asan", "use-after-free")
        if "null" in stderr.lower() and "dereference" in stderr.lower():
            return ("asan", "null-dereference")
        return ("asan", "asan-other")
    if exit_code == 1:
        return ("ubsan", "ubsan-other")
    if exit_code == 0:
        return ("debug_assert", None)
    return ("signal", f"exitcode-{exit_code}")


def extract_frames(stderr: str, max_frames: int = DEDUP_FRAMES) -> list[str]:
    frames: list[str] = []
    for line in stderr.splitlines():
        m = re.search(r"#\d+\s+0x[0-9a-f]+\s+in\s+(\S+)", line)
        if m:
            frames.append(m.group(1))
        elif "runtime error:" in line:
            frames.append(line.strip())
        if len(frames) >= max_frames:
            break
    return frames


def _hash_frames(frames: list[str]) -> str:
    key = "\n".join(frames[:DEDUP_FRAMES])
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def run_crash(harness: str, crash_file: str, timeout: int = 5) -> tuple[int, str]:
    env = os.environ.copy()
    env["ASAN_OPTIONS"] = "exitcode=223,abort_on_error=1,detect_leaks=0"
    env["UBSAN_OPTIONS"] = "halt_on_error=1,exitcode=1,print_stacktrace=1"
    try:
        result = subprocess.run(
            [harness, crash_file],
            capture_output=True,
            timeout=timeout,
            env=env,
        )
        return result.returncode, result.stderr.decode(errors="replace")
    except subprocess.TimeoutExpired:
        return -1, ""


def process_crash(harness: str, crash_file: Path, timeout: int = 5) -> CrashResult:
    sql = crash_file.read_text(errors="replace").strip()
    sql_preview = sql[:200].replace("\n", " ")
    exit_code, stderr = run_crash(harness, str(crash_file), timeout)
    crash_type, subtype = classify_crash(exit_code, stderr)
    frames = extract_frames(stderr)
    if not frames:
        content_hash = hashlib.sha256(crash_file.read_bytes()).hexdigest()[:16]
        frames = [f"<no-stack-{content_hash}>"]
    stack_hash = _hash_frames(frames)
    return CrashResult(
        file_name=crash_file.name,
        exit_code=exit_code,
        crash_type=crash_type,
        subtype=subtype,
        frames=tuple(frames),
        sql_preview=sql_preview,
        stack_hash=stack_hash,
    )


def build_clusters(results: list[CrashResult]) -> list[CrashCluster]:
    groups: dict[str, list[CrashResult]] = {}
    for r in results:
        groups.setdefault(r.stack_hash, []).append(r)
    clusters: list[CrashCluster] = []
    for h, members in groups.items():
        first = members[0]
        clusters.append(CrashCluster(
            stack_hash=h,
            crash_type=first.crash_type,
            subtype=first.subtype,
            exit_code=first.exit_code,
            count=len(members),
            sample_file=first.file_name,
            top_frames=list(first.frames[:DEDUP_FRAMES]),
            sql_preview=first.sql_preview,
        ))
    clusters.sort(key=lambda c: -c.count)
    return clusters


def write_triage_json(clusters: list[CrashCluster], total: int, output: Path) -> dict:
    summary: dict[str, int] = {"asan": 0, "ubsan": 0, "debug_assert": 0, "signal": 0, "timeout": 0}
    for c in clusters:
        key = c.crash_type if c.crash_type in summary else "signal"
        summary[key] += 1
    report = {
        "total_crashes": total,
        "unique_crashes": len(clusters),
        "summary": summary,
        "crashes": [
            {
                "hash": c.stack_hash,
                "type": c.crash_type,
                "subtype": c.subtype,
                "exit_code": c.exit_code,
                "count": c.count,
                "sample_file": c.sample_file,
                "top_frames": c.top_frames,
                "sql_preview": c.sql_preview,
            }
            for c in clusters
        ],
    }
    output.write_text(json.dumps(report, indent=2) + "\n")
    return report


def write_dedup_dir(clusters: list[CrashCluster], signaled_dir: Path, dedup_dir: Path) -> None:
    dedup_dir.mkdir(parents=True, exist_ok=True)
    for c in clusters:
        src = signaled_dir / c.sample_file
        if src.exists():
            dest = dedup_dir / f"{c.stack_hash}_{c.sample_file}"
            shutil.copy2(src, dest)


def write_report_md(clusters: list[CrashCluster], total: int, output: Path) -> None:
    lines = [
        "# Crash Triage Report",
        "",
        f"**Total crashes:** {total}  ",
        f"**Unique crash sites:** {len(clusters)}  ",
        "",
        "## Summary",
        "",
        "| Type | Unique | Total | % |",
        "|------|--------|-------|---|",
    ]
    type_totals: dict[str, tuple[int, int]] = {}
    for c in clusters:
        u, t = type_totals.get(c.crash_type, (0, 0))
        type_totals[c.crash_type] = (u + 1, t + c.count)
    type_labels = {"asan": "ASan", "ubsan": "UBSan", "debug_assert": "Debug Assert", "signal": "Signal", "timeout": "Timeout"}
    for key in ["asan", "ubsan", "debug_assert", "signal", "timeout"]:
        u, t = type_totals.get(key, (0, 0))
        pct = f"{t * 100 // total}%" if total > 0 else "0%"
        lines.append(f"| {type_labels.get(key, key)} | {u} | {t} | {pct} |")
    lines += ["", "---", ""]
    for idx, c in enumerate(clusters, 1):
        subtype_str = f" ({c.subtype})" if c.subtype else ""
        lines += [
            f"## Crash {idx}: `{c.stack_hash}` — {c.crash_type}{subtype_str}",
            "",
            f"- **Count:** {c.count} duplicates",
            f"- **Exit code:** {c.exit_code}",
            f"- **Sample file:** `{c.sample_file}`",
            "",
            "```sql",
            c.sql_preview[:2000],
            "```",
            "",
        ]
        if c.top_frames and not c.top_frames[0].startswith("<no-stack"):
            lines += ["### Stack Trace", "", "```"]
            lines += [f"  {f}" for f in c.top_frames[:15]]
            lines += ["```", ""]
        lines += ["---", ""]
    output.write_text("\n".join(lines))


def enrich_campaign_json(clusters: list[CrashCluster], campaign_path: Path) -> None:
    with open(campaign_path) as f:
        data = json.load(f)
    totals: dict[str, int] = {"asan": 0, "ubsan": 0, "debug_assert": 0, "signal": 0, "timeout": 0}
    for c in clusters:
        key = c.crash_type if c.crash_type in totals else "signal"
        totals[key] += c.count
    data.setdefault("results", {})["crash_classification"] = {
        "unique_crash_sites": len(clusters),
        **totals,
    }
    with open(campaign_path, "w") as f:
        json.dump(data, f, indent=2)


def triage(
    workdir: str,
    harness: str,
    output: str,
    dedup_dir: str,
    report: str,
    enrich: str | None = None,
    timeout: int = 5,
) -> dict:
    workdir_path = Path(workdir)
    signaled_dir = workdir_path / "outputs" / "signaled"
    if not signaled_dir.is_dir():
        print(f"[classify] No crashes directory: {signaled_dir}", file=sys.stderr)
        return {"total_crashes": 0, "unique_crashes": 0, "summary": {}, "crashes": []}

    crash_files = sorted(f for f in signaled_dir.iterdir() if f.is_file())
    total = len(crash_files)
    print(f"[classify] Processing {total} crash files...")

    results: list[CrashResult] = []
    for cf in crash_files:
        r = process_crash(harness, cf, timeout)
        results.append(r)

    clusters = build_clusters(results)

    output_path = Path(output)
    report_data = write_triage_json(clusters, total, output_path)
    write_dedup_dir(clusters, signaled_dir, Path(dedup_dir))
    write_report_md(clusters, total, Path(report))

    if enrich:
        enrich_path = Path(enrich)
        if enrich_path.exists():
            enrich_campaign_json(clusters, enrich_path)
            print(f"[classify] Enriched {enrich_path}")

    unique = len(clusters)
    print(f"[classify] {unique} unique crashes out of {total} total.")
    for c in clusters:
        sub = f" ({c.subtype})" if c.subtype else ""
        print(f"  [{c.crash_type}{sub}] {c.stack_hash} — {c.count} crashes")

    return report_data


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify and deduplicate crashes")
    parser.add_argument("workdir", help="Nautilus workdir containing outputs/signaled/")
    parser.add_argument("--harness", required=True, help="Path to harness binary")
    parser.add_argument("--output", default=None, help="triage.json path (default: <workdir>/triage.json)")
    parser.add_argument("--dedup-dir", default=None, help="Dedup directory (default: <workdir>/dedup)")
    parser.add_argument("--report", default=None, help="Markdown report path (default: <workdir>/triage_report.md)")
    parser.add_argument("--enrich", default=None, help="Path to campaign.json to enrich with classification")
    parser.add_argument("--timeout", type=int, default=5, help="Per-crash timeout in seconds (default: 5)")
    args = parser.parse_args()

    workdir = args.workdir
    triage(
        workdir=workdir,
        harness=args.harness,
        output=args.output or f"{workdir}/triage.json",
        dedup_dir=args.dedup_dir or f"{workdir}/dedup",
        report=args.report or f"{workdir}/triage_report.md",
        enrich=args.enrich,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    main()
