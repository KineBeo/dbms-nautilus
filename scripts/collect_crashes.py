from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Types only kept in the evidence archive
# ---------------------------------------------------------------------------
_KEEP_TYPES = {"ubsan", "signal", "asan"}

# ---------------------------------------------------------------------------
# Severity and CVE maps keyed by (subtype, key_function)
# ---------------------------------------------------------------------------
_SEVERITY_MAP: dict[tuple[str, str], str] = {
    ("misaligned-access", "sqlite3WindowUnlinkFromSelect"): "HIGH",
    ("null-pointer", "sqlite3Select"): "HIGH",
}
_SEVERITY_BY_SUBTYPE: dict[str, str] = {
    "signed-integer-overflow": "MEDIUM",
    "misaligned-access": "HIGH",
    "null-pointer": "HIGH",
    "float-cast-overflow": "LOW",
    "signal-6": "MEDIUM",
    "signal-11": "HIGH",
}

_CVE_MAP: dict[tuple[str, str], str] = {
    ("signed-integer-overflow", "sqlite3_str_vappendf"): "CVE-2020-13434",
    ("misaligned-access", "sqlite3WindowUnlinkFromSelect"): "CVE-2020-13871",
    ("null-pointer", "sqlite3Select"): "CVE-2020-9327",
}

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class CrashEntry:
    hash: str
    crash_type: str
    subtype: str | None
    exit_code: int
    version: str
    top_frames: list[str]
    error_message: str
    sql_preview: str
    sql_content: str | None
    sql_file: Path | None
    sample_file: str
    campaigns: list[str] = field(default_factory=list)
    total_count: int = 0


@dataclass
class BugClass:
    class_id: str
    name: str
    subtype: str | None
    key_function: str
    error_message: str
    severity: str
    cve: str | None
    hashes: list[str] = field(default_factory=list)
    versions: set[str] = field(default_factory=set)
    total_crashes: int = 0
    top_frames_sample: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def _extract_version(campaign_name: str) -> str:
    """Extract '3.XX.X' from a campaign directory name like sqlite-3.31.1_bandit_run1."""
    m = re.search(r"(\d+\.\d+\.\d+)", campaign_name)
    return m.group(1) if m else "unknown"


def _extract_error_message(frames: list[str]) -> str:
    """Return the first frame line that contains 'runtime error:' (UBSan message)."""
    for frame in frames:
        if "runtime error:" in frame:
            return frame
    return ""


def _find_sql_file(dedup_dir: Path, hash_: str) -> Path | None:
    """Find the file in dedup_dir whose name starts with hash_."""
    if not dedup_dir.is_dir():
        return None
    for f in dedup_dir.iterdir():
        if f.name.startswith(hash_):
            return f
    return None


def _extract_key_function(frames: list[str]) -> str:
    """Return the first frame that is NOT a 'runtime error:' diagnostic line.

    Frames matching ``<no-stack-*>`` are placeholders injected by the triage
    pipeline when GDB cannot capture a stack trace.  They contain a per-crash
    hash, so using them verbatim would create one class per crash.  We
    normalise them to a single ``no_stack`` sentinel so all stack-less crashes
    of the same subtype land in one class.
    """
    for frame in frames:
        stripped = frame.strip()
        if not stripped or "runtime error:" in stripped:
            continue
        if stripped.startswith("<no-stack-"):
            return "no_stack"
        return stripped
    return "unknown"


def _make_class_name(subtype: str | None, key_func: str) -> str:
    """Human-readable class name from subtype + key function."""
    subtype_part = subtype.replace("-", "_") if subtype else "unknown"
    func_part = re.sub(r"[^A-Za-z0-9_]", "_", key_func)[:40]
    return f"{subtype_part}_in_{func_part}"


def _sanitize_dirname(name: str) -> str:
    """Replace characters that are unsafe in directory names."""
    return re.sub(r"[^A-Za-z0-9._\-]", "_", name)


# ---------------------------------------------------------------------------
# Task 1 — Scanner
# ---------------------------------------------------------------------------


def scan_workdirs(workdirs_path: Path) -> dict[str, CrashEntry]:
    """Scan all workdirs, deduplicate crashes by hash, load SQL content."""
    entries: dict[str, CrashEntry] = {}

    for wd in sorted(workdirs_path.iterdir()):
        if not wd.is_dir():
            continue
        triage_file = wd / "triage_test.json"
        if not triage_file.exists():
            continue

        try:
            triage = json.loads(triage_file.read_text())
        except (json.JSONDecodeError, OSError):
            continue

        campaign_name = wd.name
        dedup_dir = wd / "dedup_test"
        version = _extract_version(campaign_name)

        for crash in triage.get("crashes", []):
            if crash.get("type") not in _KEEP_TYPES:
                continue

            # Skip signal-6 crashes with no stack trace — these are SQLite
            # debug asserts (SIGABRT from assert()), not real bugs.
            if crash.get("subtype") == "signal-6":
                frames = crash.get("top_frames", [])
                if all(f.startswith("<no-stack-") for f in frames if f.strip()):
                    continue

            h = crash["hash"]
            count = crash.get("count", 1)

            if h in entries:
                entry = entries[h]
                if campaign_name not in entry.campaigns:
                    entry.campaigns.append(campaign_name)
                entry.total_count += count
                continue

            sql_file = _find_sql_file(dedup_dir, h)
            sql_content: str | None = None
            if sql_file is not None:
                try:
                    sql_content = sql_file.read_text(errors="replace")
                except OSError:
                    sql_content = None

            top_frames = crash.get("top_frames", [])
            entries[h] = CrashEntry(
                hash=h,
                crash_type=crash.get("type", ""),
                subtype=crash.get("subtype"),
                exit_code=crash.get("exit_code", 0),
                version=version,
                top_frames=top_frames,
                error_message=_extract_error_message(top_frames),
                sql_preview=crash.get("sql_preview", ""),
                sql_content=sql_content,
                sql_file=sql_file,
                sample_file=crash.get("sample_file", ""),
                campaigns=[campaign_name],
                total_count=count,
            )

    return entries


# ---------------------------------------------------------------------------
# Task 2 — Root cause grouper
# ---------------------------------------------------------------------------


def group_into_classes(
    entries: dict[str, CrashEntry],
    overrides_path: Path | None = None,
) -> dict[str, BugClass]:
    """Group crash entries into root cause classes by (subtype, key_function)."""
    overrides: dict[str, dict] = {}
    if overrides_path and Path(overrides_path).exists():
        try:
            overrides = json.loads(Path(overrides_path).read_text())
        except (json.JSONDecodeError, OSError):
            pass

    # group_key -> (class_id, BugClass)
    classes: dict[str, BugClass] = {}

    for h, entry in entries.items():
        key_func = _extract_key_function(entry.top_frames)
        group_key = f"{entry.subtype or 'unknown'}::{key_func}"

        # Apply override if present
        if h in overrides:
            override = overrides[h]
            group_key = override.get("group_key", group_key)

        if group_key not in classes:
            subtype = entry.subtype
            severity_key = (subtype or "", key_func)
            severity = _SEVERITY_MAP.get(
                severity_key,
                _SEVERITY_BY_SUBTYPE.get(subtype or "", "LOW"),
            )
            cve = _CVE_MAP.get((subtype or "", key_func))
            class_id = f"BC{len(classes) + 1:03d}"
            name = _make_class_name(subtype, key_func)
            classes[group_key] = BugClass(
                class_id=class_id,
                name=name,
                subtype=subtype,
                key_function=key_func,
                error_message=entry.error_message,
                severity=severity,
                cve=cve,
                hashes=[h],
                versions={entry.version},
                total_crashes=entry.total_count,
                top_frames_sample=entry.top_frames[:5],
            )
        else:
            bug_class = classes[group_key]
            if h not in bug_class.hashes:
                bug_class.hashes.append(h)
            bug_class.versions.add(entry.version)
            bug_class.total_crashes += entry.total_count

    # Re-assign BC IDs sorted by total_crashes desc, key_function asc to match ch4_pipeline
    sorted_classes = sorted(
        classes.values(),
        key=lambda bc: (-bc.total_crashes, bc.key_function),
    )
    result: dict[str, BugClass] = {}
    for i, bc in enumerate(sorted_classes, 1):
        bc.class_id = f"BC{i:03d}"
        bc.name = _make_class_name(bc.subtype, bc.key_function)
        result[bc.class_id] = bc
    return result


# ---------------------------------------------------------------------------
# Task 3 — Archive emitter
# ---------------------------------------------------------------------------


def _emit_crash_dir(
    entry: CrashEntry,
    bug_class: BugClass,
    hash_dir: Path,
    harness_dir: Path,
    replay: bool,
) -> None:
    """Create all files for a single crash inside hash_dir."""
    hash_dir.mkdir(parents=True, exist_ok=True)

    # trigger.sql
    sql = entry.sql_content or entry.sql_preview or ""
    (hash_dir / "trigger.sql").write_text(sql)

    # stack_trace.txt
    stack_text = "\n".join(entry.top_frames)
    (hash_dir / "stack_trace.txt").write_text(stack_text)

    # stderr.log  (populated by replay if requested)
    stderr_log = hash_dir / "stderr.log"
    if replay and harness_dir.exists():
        harness_bins = list(harness_dir.glob(f"*{entry.version}*"))
        if harness_bins:
            harness_bin = harness_bins[0]
            try:
                sql_path = hash_dir / "trigger.sql"
                result = subprocess.run(
                    [str(harness_bin), str(sql_path)],
                    capture_output=True,
                    timeout=5,
                )
                stderr_log.write_bytes(result.stderr)
            except (subprocess.TimeoutExpired, OSError, FileNotFoundError):
                stderr_log.write_text("")
        else:
            stderr_log.write_text("")
    else:
        stderr_log.write_text(entry.error_message)

    # metadata.json
    metadata = {
        "hash": entry.hash,
        "crash_type": entry.crash_type,
        "subtype": entry.subtype,
        "exit_code": entry.exit_code,
        "version": entry.version,
        "error_message": entry.error_message,
        "sql_preview": entry.sql_preview,
        "campaigns": entry.campaigns,
        "total_count": entry.total_count,
        "sample_file": entry.sample_file,
        "bug_class": bug_class.class_id,
        "cve": bug_class.cve,
        "severity": bug_class.severity,
    }
    (hash_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))

    # reproduce.sh
    harness_path = harness_dir / f"sqlite_harness_sqlite-{entry.version}_test"
    reproduce_sh = (
        "#!/usr/bin/env bash\n"
        "# Reproduce crash: run trigger SQL through the test harness\n"
        f"HARNESS={harness_path}\n"
        f'if [ ! -f "$HARNESS" ]; then\n'
        f'  echo "Harness not found: $HARNESS" >&2\n'
        f'  exit 1\n'
        f'fi\n'
        f'"$HARNESS" trigger.sql\n'
    )
    repro_file = hash_dir / "reproduce.sh"
    repro_file.write_text(reproduce_sh)
    current_mode = repro_file.stat().st_mode
    repro_file.chmod(current_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def _emit_class_readme(bug_class: BugClass, class_dir: Path) -> None:
    """Write a README.md for a bug class directory."""
    cve_str = f" ({bug_class.cve})" if bug_class.cve else ""
    lines = [
        f"# {bug_class.class_id}: {bug_class.name}{cve_str}",
        "",
        f"**Severity:** {bug_class.severity}",
        f"**Subtype:** {bug_class.subtype or 'n/a'}",
        f"**Key function:** `{bug_class.key_function}`",
        f"**CVE:** {bug_class.cve or 'none'}",
        f"**Versions affected:** {', '.join(sorted(bug_class.versions))}",
        f"**Total crash count:** {bug_class.total_crashes}",
        f"**Unique hashes:** {len(bug_class.hashes)}",
        "",
        "## Error message",
        "",
        f"```",
        bug_class.error_message or "(none)",
        "```",
        "",
        "## Top frames (sample)",
        "",
        "```",
    ]
    lines += bug_class.top_frames_sample
    lines += [
        "```",
        "",
        "## Crash hashes",
        "",
    ]
    for h in bug_class.hashes:
        lines.append(f"- `{h}`")
    (class_dir / "README.md").write_text("\n".join(lines) + "\n")


def _emit_registry_json(
    classes: dict[str, BugClass],
    entries: dict[str, CrashEntry],
    output_dir: Path,
    campaigns_scanned: int,
) -> None:
    """Write master registry.json index."""
    classes_list = []
    for bc in sorted(classes.values(), key=lambda c: c.class_id):
        classes_list.append(
            {
                "class_id": bc.class_id,
                "name": bc.name,
                "subtype": bc.subtype,
                "key_function": bc.key_function,
                "severity": bc.severity,
                "cve": bc.cve,
                "versions": sorted(bc.versions),
                "total_crashes": bc.total_crashes,
                "unique_hashes": len(bc.hashes),
                "hashes": bc.hashes,
            }
        )

    registry = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_unique_crashes": len(entries),
        "total_bug_classes": len(classes),
        "campaigns_scanned": campaigns_scanned,
        "classes": classes_list,
    }
    (output_dir / "registry.json").write_text(json.dumps(registry, indent=2))


def _emit_registry_md(
    classes: dict[str, BugClass],
    output_dir: Path,
    entries: dict[str, CrashEntry],
) -> None:
    """Write human-readable registry.md summary table."""
    lines = [
        "# Crash Evidence Registry",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"Total unique crashes: {len(entries)}",
        f"Total bug classes: {len(classes)}",
        "",
        "## Bug Classes",
        "",
        "| Class | Name | Severity | CVE | Versions | Crashes | Hashes |",
        "|-------|------|----------|-----|----------|---------|--------|",
    ]
    for bc in sorted(classes.values(), key=lambda c: c.class_id):
        cve = bc.cve or ""
        versions = ", ".join(sorted(bc.versions))
        lines.append(
            f"| {bc.class_id} | {bc.name} | {bc.severity} | {cve} "
            f"| {versions} | {bc.total_crashes} | {len(bc.hashes)} |"
        )
    (output_dir / "registry.md").write_text("\n".join(lines) + "\n")


def emit_archive(
    entries: dict[str, CrashEntry],
    classes: dict[str, BugClass],
    output_dir: Path,
    replay: bool = False,
    incremental: bool = False,
) -> None:
    """Create the full crash evidence archive directory structure."""
    output_dir.mkdir(parents=True, exist_ok=True)

    harness_dir = ROOT / "harness" / "test"

    # Build reverse map: hash -> BugClass
    hash_to_class: dict[str, BugClass] = {}
    for bc in classes.values():
        for h in bc.hashes:
            hash_to_class[h] = bc

    for entry in entries.values():
        bug_class = hash_to_class.get(entry.hash)
        if bug_class is None:
            continue

        class_dirname = _sanitize_dirname(f"{bug_class.class_id}_{bug_class.name}")
        class_dir = output_dir / class_dirname
        class_dir.mkdir(parents=True, exist_ok=True)

        hash_dir = class_dir / entry.hash
        if incremental and hash_dir.exists():
            continue

        _emit_crash_dir(entry, bug_class, hash_dir, harness_dir, replay)

    # Write class-level READMEs
    for bc in classes.values():
        class_dirname = _sanitize_dirname(f"{bc.class_id}_{bc.name}")
        class_dir = output_dir / class_dirname
        class_dir.mkdir(parents=True, exist_ok=True)
        _emit_class_readme(bc, class_dir)

    # Count campaigns scanned
    campaigns_scanned = len({c for e in entries.values() for c in e.campaigns})

    _emit_registry_json(classes, entries, output_dir, campaigns_scanned)
    _emit_registry_md(classes, output_dir, entries)


# ---------------------------------------------------------------------------
# Task 4 — CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="collect_crashes.py",
        description="Scan fuzzing workdirs, deduplicate crashes, and emit a structured evidence archive.",
    )
    parser.add_argument(
        "--workdirs",
        type=Path,
        default=ROOT / "workdirs",
        metavar="DIR",
        help="Path to workdirs directory (default: workdirs/)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "results" / "crashes",
        metavar="DIR",
        help="Output directory for evidence archive (default: results/crashes/)",
    )
    parser.add_argument(
        "--scan-only",
        action="store_true",
        help="Only scan and group; skip replay and archive emission",
    )
    parser.add_argument(
        "--incremental",
        action="store_true",
        help="Skip crash hashes that already have a directory in the output",
    )
    parser.add_argument(
        "--overrides",
        type=Path,
        default=None,
        metavar="FILE",
        help="Path to class_overrides.json for manual grouping overrides",
    )

    args = parser.parse_args()

    print(f"[collect_crashes] Scanning workdirs at: {args.workdirs}")
    entries = scan_workdirs(args.workdirs)
    print(f"[collect_crashes] Found {len(entries)} unique crash hashes")

    print("[collect_crashes] Grouping into root cause classes...")
    classes = group_into_classes(entries, overrides_path=args.overrides)
    print(f"[collect_crashes] Identified {len(classes)} bug classes")

    if args.scan_only:
        print("[collect_crashes] --scan-only: skipping archive emission")
        for bc in sorted(classes.values(), key=lambda c: c.class_id):
            cve = f" ({bc.cve})" if bc.cve else ""
            print(f"  {bc.class_id} {bc.name}{cve}  severity={bc.severity}  hashes={len(bc.hashes)}")
        return

    print(f"[collect_crashes] Emitting archive to: {args.output}")
    emit_archive(
        entries,
        classes,
        args.output,
        replay=not args.scan_only,
        incremental=args.incremental,
    )
    print("[collect_crashes] Done.")
    print(f"  Registry: {args.output / 'registry.json'}")
    print(f"  Summary:  {args.output / 'registry.md'}")


if __name__ == "__main__":
    main()
