"""Stack-level root-cause dedup for Nautilus crash workdirs.

Method:
  1. For each crash in outputs/signaled/, run the harness under gdb with the
     crash file as stdin, capturing the top 5 frames.
  2. Filter to SQLite-internal frames (drop libc, libasan, the harness wrapper).
  3. Hash the joined filtered frames; crashes with identical hash are the same
     root cause.
  4. Emit dedup.json per spec 2026-04-22-measurement-and-fidelity-design.md 2.1.

SIGTRAP from SQLITE_DEBUG asserts still produces a source-line signature in
sqlite3.c, so this works even without ASan frames.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

_SKIP_PATTERNS = (
    "libc",
    "ld-linux",
    "libasan",
    "libubsan",
    "libpthread",
    "__asan",
    "__ubsan",
    "__libc",
    "__interceptor",
    "sqlite_harness",
    "afl_init",
    "__AFL",
)

_BT_LINE = re.compile(
    r"^#\d+\s+(?:0x[0-9a-f]+\s+in\s+)?([\w:.<>~]+)\s+.*?at\s+([\w./-]+):(\d+)"
)


def filter_frames(raw_lines: Iterable[str]) -> list[str]:
    """Drop libc/asan/harness wrapper frames. Keep SQLite-internal frames."""
    kept: list[str] = []
    for line in raw_lines:
        if any(pat in line for pat in _SKIP_PATTERNS):
            continue
        kept.append(line)
    return kept


def hash_frames(frames: Iterable[str]) -> str:
    """sha256 of joined frames — the root-cause identifier."""
    h = hashlib.sha256()
    h.update("\n".join(frames).encode("utf-8"))
    return h.hexdigest()


def parse_gdb_bt(output: str) -> list[str]:
    """Extract 'function:file:line' tokens from gdb 'bt' output."""
    frames: list[str] = []
    for line in output.splitlines():
        m = _BT_LINE.match(line.strip())
        if not m:
            continue
        func, src, lineno = m.group(1), m.group(2), m.group(3)
        frames.append(f"{func}:{src}:{lineno}")
    return frames


def build_clusters(crashes: list[dict]) -> list[dict]:
    """Group crash records by hash_frames(record['frames'])."""
    groups: dict[str, list[dict]] = {}
    for rec in crashes:
        h = hash_frames(rec["frames"])
        groups.setdefault(h, []).append(rec)
    clusters: list[dict] = []
    for h, members in groups.items():
        first = members[0]
        clusters.append({
            "hash": h,
            "count": len(members),
            "representative": first["file"],
            "top_frame": first["frames"][0] if first["frames"] else "<no-frame>",
            "example_sql": first["sql"][:200],
        })
    clusters.sort(key=lambda c: -c["count"])
    return clusters


def run_gdb_on_crash(harness: Path, crash_file: Path, timeout_sec: int = 20) -> list[str]:
    """Spawn gdb --batch on the harness with the crash file as argv[1]; return top 5 filtered frames.

    The SQLite harnesses in this repo take the input path as argv[1] (per
    `usage: ... <input_file>` message). They do NOT read from stdin. They
    also refuse to run under ptrace with LeakSanitizer's default settings,
    so we disable leak detection via ASAN_OPTIONS for the gdb subprocess.
    """
    cmd = [
        "gdb",
        "--batch",
        "--nx",
        "--ex", "set pagination off",
        "--ex", f"run {crash_file}",
        "--ex", "bt 5",
        "--ex", "quit",
        str(harness),
    ]
    env = os.environ.copy()
    # LeakSanitizer aborts under ptrace by default; disable it for the replay.
    env["ASAN_OPTIONS"] = env.get("ASAN_OPTIONS", "") + ":detect_leaks=0:abort_on_error=1"
    env["UBSAN_OPTIONS"] = env.get("UBSAN_OPTIONS", "") + ":abort_on_error=1"
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
            env=env,
        )
    except subprocess.TimeoutExpired:
        return []
    bt_frames = parse_gdb_bt(proc.stdout + "\n" + proc.stderr)
    return filter_frames(bt_frames)


def dedup_workdir(workdir: Path, harness: Path, output_path: Path) -> dict:
    signaled_dir = workdir / "outputs" / "signaled"
    if not signaled_dir.is_dir():
        raise FileNotFoundError(f"no signaled/ dir: {signaled_dir}")
    crashes: list[dict] = []
    for crash_file in sorted(signaled_dir.iterdir()):
        if not crash_file.is_file():
            continue
        try:
            sql = crash_file.read_bytes().decode("utf-8", errors="replace")
        except OSError:
            continue
        frames = run_gdb_on_crash(harness, crash_file)
        crashes.append({"file": crash_file.name, "sql": sql, "frames": frames})
    clusters = build_clusters(crashes)
    report = {
        "total_crashes": len(crashes),
        "unique_root_causes": len(clusters),
        "clusters": clusters,
    }
    output_path.write_text(json.dumps(report, indent=2))
    return report


def _main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("workdir", type=Path, help="fuzzing workdir containing outputs/signaled/")
    p.add_argument("--harness", type=Path, required=True, help="harness binary")
    p.add_argument("--output", type=Path, default=None, help="dedup.json path (default: <workdir>/dedup.json)")
    args = p.parse_args(argv)
    out = args.output or (args.workdir / "dedup.json")
    report = dedup_workdir(args.workdir, args.harness, out)
    print(f"total_crashes={report['total_crashes']} unique_root_causes={report['unique_root_causes']}")
    return 0


if __name__ == "__main__":
    sys.exit(_main())
