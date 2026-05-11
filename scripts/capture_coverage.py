"""Parse a Nautilus workdir into an end-of-run coverage.json.

Reads:
  <workdir>/exec.log                  — last 'Execution Count: N' line
  <workdir>/outputs/{queue,signaled,timeout}/  — file counts

Writes:
  <workdir>/coverage.json  (default path; overridable via --output)

Schema note: bits_found_by_* fields are present but always null in v1. A
future spec can populate them after a fuzzer-source change adds a disk dump.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Supports two exec.log formats observed in the wild:
#   (A) Nautilus fuzzer event log: each line is "<exec_count>\t<EVENT>\t<sql>"
#       where EVENT is NEW_COV, SIGNAL(n), TIMEOUT, etc. The max exec_count
#       (the first column of the last line) is the total executions.
#   (B) Legacy summary lines: "Execution Count: N" (kept for back-compat
#       and for the unit tests in tests/triage/test_capture_coverage.py).
_EXEC_RE_PHRASE = re.compile(r"Execution Count:\s*(\d+)")
_EXEC_RE_TAB_LEADING = re.compile(r"^(\d+)\t(?:NEW_COV|SIGNAL|TIMEOUT)", re.MULTILINE)


def parse_exec_count(log_path: Path) -> int | None:
    try:
        text = log_path.read_text(errors="replace")
    except (OSError, FileNotFoundError):
        return None
    # Prefer the tab-leading format (current Nautilus output).
    tab_hits = _EXEC_RE_TAB_LEADING.findall(text)
    if tab_hits:
        return max(int(h) for h in tab_hits)
    # Fall back to the legacy phrase format.
    phrase_hits = _EXEC_RE_PHRASE.findall(text)
    if not phrase_hits:
        return None
    return int(phrase_hits[-1])


def count_outputs(outputs_dir: Path) -> dict[str, int]:
    result = {"queue_final": 0, "signaled_final": 0, "timeout_final": 0}
    if not outputs_dir.is_dir():
        return result
    for sub, key in (("queue", "queue_final"), ("signaled", "signaled_final"), ("timeout", "timeout_final")):
        d = outputs_dir / sub
        if d.is_dir():
            result[key] = sum(1 for p in d.iterdir() if p.is_file())
    return result


def build_coverage(workdir: Path, duration_seconds: int) -> dict:
    exec_count = parse_exec_count(workdir / "exec.log")
    counts = count_outputs(workdir / "outputs")
    if exec_count is not None and duration_seconds > 0:
        eps: float | None = exec_count / duration_seconds
    else:
        eps = None
    return {
        "total_executions": exec_count,
        "duration_seconds": duration_seconds,
        "exec_per_sec": eps,
        "bits_found": None,
        "bits_found_new": None,
        "bits_found_mutation": None,
        "bits_found_deterministic": None,
        **counts,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("workdir", type=Path)
    p.add_argument("--duration", type=int, required=True, help="wall-clock seconds")
    p.add_argument("--output", type=Path, default=None)
    args = p.parse_args(argv)
    report = build_coverage(args.workdir, args.duration)
    out = args.output or (args.workdir / "coverage.json")
    out.write_text(json.dumps(report, indent=2))
    print(f"wrote {out} execs={report['total_executions']} signaled={report['signaled_final']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
