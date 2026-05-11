# Measurement + Pattern Fidelity Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver (α-full) stack-level dedup + end-of-run coverage + per-pattern fidelity scorer, (β / B2) split 7 attack patterns into tight/loose non-terminals, and (E2) run a 4-variant × 3-seed × 1-hour ablation on sqlite-3.31.1 that produces a thesis-defensible verdict on whether tightening fidelity improves unique-root-cause bug count.

**Architecture:** Three measurement tools live under `triage/`; grammar edits stay in `grammars/sqlite_attack.py`; evaluation wrapper extends `scripts/run_eval.sh`; no fuzzer-source changes in scope. Deliverables pair cleanly with the existing per-task commit style established in the grammar-implementation plan.

**Tech Stack:** Python 3 (tools), bash (scripts), Rust Nautilus fuzzer (read-only except one small append to `run_eval.sh`), AFL-instrumented SQLite harnesses, gdb for backtrace extraction, regex-based structural parsing (tree-sitter is a deferred upgrade path).

**Spec:** `docs/superpowers/specs/2026-04-22-measurement-and-fidelity-design.md`

---

## File Structure

Files created or modified by this plan:

| File | Role | Status |
|---|---|---|
| `triage/stack_dedup.py` | A1: gdb-backtrace root-cause dedup; emits `dedup.json` per workdir | **Created** |
| `triage/fidelity_score.py` | A3: per-pattern structural fidelity scorer; emits `fidelity-report.json` | **Created** |
| `triage/cve_signatures.py` | Library of per-CVE required-node signatures used by A3 | **Created** |
| `tests/triage/test_stack_dedup.py` | TDD for A1 | **Created** |
| `tests/triage/test_capture_coverage.py` | TDD for A2 helper | **Created** |
| `tests/triage/test_cve_signatures.py` | TDD for CVE signatures | **Created** |
| `tests/triage/test_fidelity_score.py` | TDD for A3 | **Created** |
| `scripts/run_eval.sh` | A2: end-of-run coverage capture + `coverage.json` emission | **Modified** (append ~10 lines) |
| `scripts/capture_coverage.py` | A2 helper: parses workdir outputs into `coverage.json` | **Created** |
| `scripts/run_ablation.sh` | E2: orchestrates the 12-run matrix | **Created** |
| `grammars/sqlite_attack.py` | B2: 7 tight NT definitions + 7 pattern-body edits | **Modified** |
| `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md` | Non-behavioral amendment: §9 line budget raised ~365 → ~460 | **Modified** |
| `docs/task-0-findings.md` | Task 0 investigation record | **Created** |
| `docs/fidelity-baseline-attack-v1.json` | A3 baseline on pre-B2 grammar | **Created** |
| `docs/fidelity-postB2-attack-v2.json` | A3 on B2-tightened grammar | **Created** |
| `docs/attack-grammar-ablation-sqlite-3.31.1.md` | Final ablation report | **Created** |

Files deliberately **not** touched:
- `fuzzer/**`, `grammartec/**`, `forksrv/**` — no fuzzer-source changes. The spec's "coverage over time" deferral and "seed control" gap are both absorbed here (Task 0 confirmed).
- `grammars/sqlite_patterns.py`, `grammars/sqlite_patterns_uniform.py` — ablation baselines must remain unchanged.
- `harness/**` — `-O1 -g` already set (Task 0 confirmed); no rebuild.

---

## Conventions

- **Project root** is `/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2`. All relative paths are rooted there; `cd` to root before running any command.
- **Env prereqs** (set once per shell):
  ```bash
  export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
  export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
  export PYTHONPATH="$(pwd)"
  ```
- **Python test framework**: `pytest`. New tests live under `tests/triage/`.
- **Commit discipline**: one logical change per commit, no `-A`, no `--no-verify`. `docs/` is gitignored → use `git add -f` for any doc file.
- **Ablation tag**: `attack-v1-frozen` refers to commit `2298743` (the pre-B2 grammar). Tag is created in Task 13, not earlier, to ensure nothing else drifts before it's captured.

---

## Task 0 — Investigation findings (pre-resolved)

The three open questions from the spec's §6 were resolved before this plan was drafted. Findings:

| Question | Finding | Consequence for plan |
|---|---|---|
| (a) Does fuzzer.rs log `bits_found_by_*` to `exec.log`? | Fields exist in `fuzzer/src/shared_state.rs:13-19` and `fuzzer/src/fuzzer.rs:90-96` as in-memory u64 counters. No `println!`/`write!` found writing them to any log path. | A2 cannot parse from existing logs. A2 captures end-of-run proxies only: file counts in `outputs/{queue,signaled,timeout}/` + last `Execution Count` parse from `exec.log`. `bits_found_by_*` dump deferred. |
| (b) Does Nautilus have RNG seed control? | `grammartec/` and `fuzzer/` both use `rand::thread_rng()` throughout (grep hit 11 call sites). No `SeedableRng::from_seed` constructor is wired to a config surface. | E2 cannot set RNG seeds. Plan uses **3 independent runs** as variance-estimate floor per spec §4.2. Report must flag this limitation. |
| (c) Harness debug flags for gdb backtraces? | `harness/Makefile:18` uses `-O1 -g`. Debug info is present; inlining is mild. | A1's gdb path works. No rebuild. |

Task 0 is documentation-only: record these findings so future readers understand why seeds use "independent runs" and why `coverage.json` schema is narrower than the spec's schema.

- [ ] **Step 1: Create `docs/task-0-findings.md`**

Write exactly this content:

```markdown
# Task 0 Findings — Nautilus coverage, seed, harness flags

**Date:** 2026-04-22
**Spec reference:** `docs/superpowers/specs/2026-04-22-measurement-and-fidelity-design.md` §6

## (a) Coverage logging

Fields `bits_found_by_havoc`, `bits_found_by_havoc_rec`, `bits_found_by_min`, `bits_found_by_min_rec`, `bits_found_by_splice`, `bits_found_by_det`, `bits_found_by_gen` are defined in `fuzzer/src/shared_state.rs:13-19` and `fuzzer/src/fuzzer.rs:90-96` as in-memory u64 counters. Grep finds no code path writing them to disk.

Consequence: A2 captures end-of-run proxies only — file counts in `outputs/{queue,signaled,timeout}/` plus the last `Execution Count: N` line from `exec.log`. Adding a `bits_found_by_*` dump would require a fuzzer-source change; that is out of scope for this spec.

## (b) RNG seed control

`grammartec/` and `fuzzer/` use `rand::thread_rng()` throughout. Found at least 11 call sites in `grammartec/src/context.rs`, `grammartec/src/mutator.rs`, `grammartec/src/tree.rs`, `fuzzer/src/dqn.rs`. No seed field in `config.ron` is wired to a `SeedableRng::from_seed` constructor.

Consequence: E2's "3 seeds × 4 variants" matrix uses 3 independent runs per variant as a variance-estimate floor. The ablation report must document this.

## (c) Harness debug flags

`harness/Makefile:18` sets `CFLAGS = -O1 -g $(ASAN_FLAGS) $(EXTRA_CFLAGS)`. Debug info is present. Inlining at `-O1` is mild; gdb can recover source-line frames inside `sqlite3.c` on SIGTRAP.

Consequence: A1's gdb-based stack dedup works without rebuilding harnesses.
```

- [ ] **Step 2: Commit the findings**

```bash
git add -f docs/task-0-findings.md
git commit -m "docs(task-0): record Nautilus coverage/seed/harness findings"
```

---

## Task 1 — A1 tests: stack-dedup happy path

**Files:**
- Create: `tests/triage/__init__.py`
- Create: `tests/triage/test_stack_dedup.py`

**Context:** TDD first. The dedup library must handle: (1) grouping crashes that gdb reports with identical top frames, (2) frame filtering (skip libc/libasan/harness wrapper), (3) emitting the JSON shape from spec §2.1.

- [ ] **Step 1: Create test scaffolding**

```bash
mkdir -p tests/triage
touch tests/triage/__init__.py
```

- [ ] **Step 2: Write the test file**

Write to `tests/triage/test_stack_dedup.py`:

```python
"""Tests for triage.stack_dedup."""
from __future__ import annotations

from triage import stack_dedup


class TestFrameFiltering:
    def test_drops_libc_frames(self) -> None:
        raw = [
            "__libc_start_main:libc-start.c:332",
            "sqlite3_str_vappendf:sqlite3.c:28528",
            "sqliteVPrintfFunc:sqlite3.c:28810",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert all("libc" not in f for f in kept)
        assert len(kept) == 2

    def test_drops_asan_frames(self) -> None:
        raw = [
            "__asan::ReportGenericError:asan_report.cc:200",
            "sqlite3_str_vappendf:sqlite3.c:28528",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert len(kept) == 1
        assert "sqlite3_str_vappendf" in kept[0]

    def test_keeps_sqlite_frames(self) -> None:
        raw = [
            "sqlite3_str_vappendf:sqlite3.c:28528",
            "sqliteVPrintfFunc:sqlite3.c:28810",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert len(kept) == 2


class TestHashing:
    def test_identical_frames_hash_identically(self) -> None:
        frames_a = ["sqlite3_str_vappendf:sqlite3.c:28528", "sqliteVPrintfFunc:sqlite3.c:28810"]
        frames_b = ["sqlite3_str_vappendf:sqlite3.c:28528", "sqliteVPrintfFunc:sqlite3.c:28810"]
        assert stack_dedup.hash_frames(frames_a) == stack_dedup.hash_frames(frames_b)

    def test_different_frames_hash_differently(self) -> None:
        frames_a = ["sqlite3_str_vappendf:sqlite3.c:28528"]
        frames_b = ["sqlite3VdbeExec:sqlite3.c:99999"]
        assert stack_dedup.hash_frames(frames_a) != stack_dedup.hash_frames(frames_b)


class TestClusterBuilding:
    def test_groups_three_crashes_with_same_frames(self) -> None:
        crashes = [
            {"file": "5_000001", "sql": "SELECT printf('%.*g', 2147483647, 0.01);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000002", "sql": "SELECT printf('%.*g', -2147483648, 3.1);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000003", "sql": "SELECT printf('abc', 2147483647, 0);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
        ]
        clusters = stack_dedup.build_clusters(crashes)
        assert len(clusters) == 1
        assert clusters[0]["count"] == 3
        assert clusters[0]["top_frame"] == "sqlite3_str_vappendf:sqlite3.c:28528"

    def test_splits_two_root_causes(self) -> None:
        crashes = [
            {"file": "5_000001", "sql": "SELECT printf(...);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000002", "sql": "SELECT printf(...);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000003", "sql": "SELECT coalesce(...);", "frames": ["sqlite3VdbeExec:sqlite3.c:99999"]},
        ]
        clusters = stack_dedup.build_clusters(crashes)
        assert len(clusters) == 2
        counts = sorted(c["count"] for c in clusters)
        assert counts == [1, 2]


class TestGdbOutputParsing:
    def test_parses_bt_5_output(self) -> None:
        gdb_output = (
            "Thread 1 \"sqlite_harness_\" received signal SIGTRAP, Trace/breakpoint trap.\n"
            "#0  sqlite3_str_vappendf (pAccum=0x0, fmt=..., ap=...) at sqlite3.c:28528\n"
            "#1  0x00007ffff7a12345 in sqliteVPrintfFunc (context=0x0) at sqlite3.c:28810\n"
            "#2  0x00007ffff7a00000 in sqlite3VdbeExec (p=0x0) at sqlite3.c:85000\n"
        )
        frames = stack_dedup.parse_gdb_bt(gdb_output)
        assert frames[0] == "sqlite3_str_vappendf:sqlite3.c:28528"
        assert frames[1] == "sqliteVPrintfFunc:sqlite3.c:28810"
        assert frames[2] == "sqlite3VdbeExec:sqlite3.c:85000"
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `pytest tests/triage/test_stack_dedup.py -v 2>&1 | tail -20`

Expected: all tests fail with `ModuleNotFoundError: No module named 'triage.stack_dedup'`.

- [ ] **Step 4: Commit the failing tests**

```bash
git add tests/triage/__init__.py tests/triage/test_stack_dedup.py
git commit -m "test(triage): add failing tests for stack_dedup filter/hash/cluster"
```

---

## Task 2 — A1 implementation: `triage/stack_dedup.py`

**Files:**
- Create or verify: `triage/__init__.py`
- Create: `triage/stack_dedup.py`

**Context:** Implement the functions tested in Task 1, plus a CLI entry point that walks a workdir, runs gdb per crash file, builds clusters, and writes `dedup.json`.

- [ ] **Step 1: Verify / create `triage/__init__.py`**

```bash
ls triage/__init__.py 2>&1 || touch triage/__init__.py
```

- [ ] **Step 2: Write `triage/stack_dedup.py`**

```python
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
    """Spawn gdb --batch on the harness with the crash as stdin; return top 5 filtered frames."""
    cmd = [
        "gdb",
        "--batch",
        "--nx",
        "--ex", "set pagination off",
        "--ex", f"run < {crash_file}",
        "--ex", "bt 5",
        "--ex", "quit",
        str(harness),
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
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
```

- [ ] **Step 3: Run tests; expect pass**

Run: `pytest tests/triage/test_stack_dedup.py -v 2>&1 | tail -20`

Expected: all PASS.

- [ ] **Step 4: Commit**

```bash
git add triage/stack_dedup.py triage/__init__.py
git commit -m "feat(triage): add stack-level root-cause dedup via gdb backtrace"
```

---

## Task 3 — A1 integration verification (manual)

**Files:** None created; either commits `docs/a1-manual-verification.md` with numbers if a workdir is available, or commits a one-liner noting deferral.

- [ ] **Step 1: Check if a workdir with crashes exists**

```bash
ls -l /tmp/nautilus_eval/*/outputs/signaled 2>&1 | head
```

If output shows at least one directory with ≥1 crash file, proceed to Step 2. Otherwise, jump to Step 3.

- [ ] **Step 2 (if workdir available): Run dedup and inspect**

Replace `<WORKDIR>` with an actual path from Step 1:

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYTHONPATH="$(pwd)"
python3 -m triage.stack_dedup <WORKDIR> \
    --harness harness/sqlite_harness_patterns_sqlite-3.31.1 \
    --output <WORKDIR>/dedup.json 2>&1 | tail
python3 -m json.tool <WORKDIR>/dedup.json | head -40
```

Then write `docs/a1-manual-verification.md`:

```markdown
# A1 Stack-Dedup Manual Verification

**Date:** <YYYY-MM-DD>
**Workdir tested:** <WORKDIR>
**Total crashes:** <N>
**Unique root causes:** <K>
**Top cluster:** count=<N>, top_frame=<FRAME>

Inspection: <one-sentence plausibility judgment — e.g. "all N crashes cluster to sqlite3_str_vappendf, consistent with CVE-2020-13434 printf overflow">.
```

```bash
git add -f docs/a1-manual-verification.md
git commit -m "docs(triage): record A1 stack-dedup manual verification"
```

- [ ] **Step 3 (if no workdir): Commit deferral note**

```bash
cat > docs/a1-manual-verification.md << 'EOF'
# A1 Stack-Dedup Manual Verification

Deferred — no live workdir at implementation time. Automatic verification happens in Task 15 (E2) when fresh workdirs exist.
EOF
git add -f docs/a1-manual-verification.md
git commit -m "docs(triage): note A1 manual verification deferred to E2"
```

---

## Task 4 — A2 helper: `scripts/capture_coverage.py`

**Files:**
- Create: `tests/triage/test_capture_coverage.py`
- Create: `scripts/capture_coverage.py`

**Context:** Per Task 0 finding (a), we cannot parse `bits_found_by_*` from logs. A2's v1 captures: `total_executions` (from last `Execution Count:` line), duration (wall clock), queue/signaled/timeout file counts. Schema is the spec §2.2 minimum-viable fallback.

- [ ] **Step 1: Write the failing tests**

Write to `tests/triage/test_capture_coverage.py`:

```python
"""Tests for scripts.capture_coverage."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import capture_coverage as cap  # noqa: E402


class TestParseExecCount:
    def test_finds_last_execution_count(self, tmp_path: Path) -> None:
        log = tmp_path / "exec.log"
        log.write_text(
            "Starting fuzzer\n"
            "Execution Count: 100\n"
            "Execution Count: 200\n"
            "Execution Count: 12345\n"
        )
        assert cap.parse_exec_count(log) == 12345

    def test_returns_none_if_absent(self, tmp_path: Path) -> None:
        log = tmp_path / "exec.log"
        log.write_text("no exec lines here\n")
        assert cap.parse_exec_count(log) is None

    def test_returns_none_on_missing_file(self, tmp_path: Path) -> None:
        assert cap.parse_exec_count(tmp_path / "missing.log") is None


class TestCountOutputs:
    def test_counts_each_output_dir(self, tmp_path: Path) -> None:
        outputs = tmp_path / "outputs"
        for sub in ("queue", "signaled", "timeout"):
            d = outputs / sub
            d.mkdir(parents=True)
            for i in range(3 if sub == "signaled" else 5):
                (d / f"file_{i}").write_text("x")
        counts = cap.count_outputs(outputs)
        assert counts == {"queue_final": 5, "signaled_final": 3, "timeout_final": 5}

    def test_missing_subdir_reports_zero(self, tmp_path: Path) -> None:
        outputs = tmp_path / "outputs"
        outputs.mkdir()
        (outputs / "queue").mkdir()
        counts = cap.count_outputs(outputs)
        assert counts["queue_final"] == 0
        assert counts["signaled_final"] == 0
        assert counts["timeout_final"] == 0


class TestBuildCoverage:
    def test_assembles_schema(self, tmp_path: Path) -> None:
        workdir = tmp_path / "wd"
        outputs = workdir / "outputs"
        for sub in ("queue", "signaled", "timeout"):
            (outputs / sub).mkdir(parents=True)
        (outputs / "queue" / "a").write_text("x")
        (outputs / "signaled" / "a").write_text("x")
        (workdir / "exec.log").write_text("Execution Count: 50000\n")
        report = cap.build_coverage(workdir, duration_seconds=600)
        assert report["duration_seconds"] == 600
        assert report["total_executions"] == 50000
        assert report["exec_per_sec"] == pytest.approx(50000 / 600, rel=1e-6)
        assert report["queue_final"] == 1
        assert report["signaled_final"] == 1
        assert report["timeout_final"] == 0
        # bits_found_by_* reserved for a future fuzzer-source change — null in v1:
        assert report["bits_found"] is None
        assert report["bits_found_new"] is None


class TestCli:
    def test_writes_json(self, tmp_path: Path) -> None:
        workdir = tmp_path / "wd"
        (workdir / "outputs" / "queue").mkdir(parents=True)
        (workdir / "outputs" / "signaled").mkdir()
        (workdir / "outputs" / "timeout").mkdir()
        (workdir / "exec.log").write_text("Execution Count: 10\n")
        out = workdir / "coverage.json"
        rc = cap.main([str(workdir), "--duration", "120", "--output", str(out)])
        assert rc == 0
        data = json.loads(out.read_text())
        assert data["total_executions"] == 10
        assert data["duration_seconds"] == 120
```

- [ ] **Step 2: Run tests — expect ModuleNotFoundError**

Run: `pytest tests/triage/test_capture_coverage.py -v 2>&1 | tail -15`

Expected: fails with `ModuleNotFoundError: No module named 'capture_coverage'`.

- [ ] **Step 3: Create `scripts/capture_coverage.py`**

```python
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

_EXEC_RE = re.compile(r"Execution Count:\s*(\d+)")


def parse_exec_count(log_path: Path) -> int | None:
    try:
        text = log_path.read_text(errors="replace")
    except (OSError, FileNotFoundError):
        return None
    hits = _EXEC_RE.findall(text)
    if not hits:
        return None
    return int(hits[-1])


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
```

- [ ] **Step 4: Run tests — expect pass**

Run: `pytest tests/triage/test_capture_coverage.py -v 2>&1 | tail -15`

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add tests/triage/test_capture_coverage.py scripts/capture_coverage.py
git commit -m "feat(scripts): add capture_coverage.py for end-of-run coverage.json"
```

---

## Task 5 — A2 wiring: extend `run_eval.sh` to emit `coverage.json`

**Files:**
- Modify: `scripts/run_eval.sh` (append coverage capture at end of run)

**Context:** Append a step that runs `capture_coverage.py` immediately after the fuzzer exits.

- [ ] **Step 1: Read the tail of `run_eval.sh` to find the right append point**

Run: `tail -20 scripts/run_eval.sh`

Identify the last line. Note the exact variable names used for the workdir path and the duration.

- [ ] **Step 2: Append the coverage capture block**

Append this block to `scripts/run_eval.sh` (use Edit with anchor on the last existing line):

```bash

# ----------------------------------------------------------------
# A2: end-of-run coverage capture (per spec 2026-04-22-measurement-and-fidelity)
# ----------------------------------------------------------------
echo "[run_eval] capturing coverage..."
python3 "$SCRIPT_DIR/capture_coverage.py" "$WORKDIR_BASE/${VERSION}_${RUN_ID}" \
    --duration "$DURATION" \
    --output "$WORKDIR_BASE/${VERSION}_${RUN_ID}/coverage.json" \
    || echo "[run_eval] warning: coverage capture failed (non-fatal)"
```

If the existing script uses different variable names for the workdir path or duration, substitute them. Do NOT introduce new variables.

- [ ] **Step 3: Dry-run with a synthetic workdir**

```bash
tmp=$(mktemp -d)
mkdir -p "$tmp/outputs"/{queue,signaled,timeout}
echo "Execution Count: 12345" > "$tmp/exec.log"
touch "$tmp/outputs/queue/a" "$tmp/outputs/signaled/a"
python3 scripts/capture_coverage.py "$tmp" --duration 600 --output "$tmp/coverage.json"
cat "$tmp/coverage.json"
rm -rf "$tmp"
```

Expected: `coverage.json` with `total_executions: 12345`, `exec_per_sec: 20.575`, `queue_final: 1`, `signaled_final: 1`, `timeout_final: 0`.

- [ ] **Step 4: Commit**

```bash
git add scripts/run_eval.sh
git commit -m "feat(scripts): capture coverage.json at end of run_eval.sh"
```

---

## Task 6 — A3 library: `triage/cve_signatures.py`

**Files:**
- Create: `tests/triage/test_cve_signatures.py`
- Create: `triage/cve_signatures.py`

**Context:** Each of the 6 corpus CVEs needs a "required nodes" pattern list — the structural tokens that must appear for generated SQL to be isomorphic to the CVE PoC. Regex-based signatures (no external deps) per spec's fallback clause.

- [ ] **Step 1: Write the tests**

Write to `tests/triage/test_cve_signatures.py`:

```python
"""Tests for triage.cve_signatures — required-node patterns per CVE."""
from __future__ import annotations

from triage import cve_signatures as sigs


class TestCoverage:
    def test_all_six_cves_present(self) -> None:
        cves = sigs.all_cves()
        ids = {c["cve"] for c in cves}
        expected = {
            "CVE-2020-15358",
            "CVE-2020-13871",
            "CVE-2020-13435",
            "CVE-2020-13434",
            "CVE-2020-9327",
            "CVE-2019-19646",
        }
        assert ids == expected

    def test_each_cve_has_required_patterns(self) -> None:
        for c in sigs.all_cves():
            assert len(c["required_patterns"]) >= 2, c["cve"]


class TestMatchP13435:
    def test_matches_real_cve_poc(self) -> None:
        poc = (
            "CREATE TABLE a(c UNIQUE);\n"
            "SELECT a.c FROM a JOIN a b ON 3 = a.c NATURAL JOIN a "
            "WHERE a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM a d WHERE a.c));"
        )
        sig = sigs.get_cve("CVE-2020-13435")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []

    def test_rejects_loose_sample(self) -> None:
        loose = "SELECT * FROM a JOIN b ON 1=1;"
        sig = sigs.get_cve("CVE-2020-13435")
        missing = sigs.missing_patterns(loose, sig)
        assert len(missing) > 0
        assert "NATURAL_JOIN" in missing


class TestMatchP13434:
    def test_matches_boundary_form(self) -> None:
        poc = "SELECT printf('%.*g', 2147483647, 0.01);"
        sig = sigs.get_cve("CVE-2020-13434")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []


class TestMatchP19646:
    def test_matches(self) -> None:
        poc = (
            "CREATE TABLE t0 (c0, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0));\n"
            "INSERT INTO t0(c0) VALUES (0);\n"
            "PRAGMA integrity_check;"
        )
        sig = sigs.get_cve("CVE-2019-19646")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []
```

- [ ] **Step 2: Run tests — expect ModuleNotFoundError**

Run: `pytest tests/triage/test_cve_signatures.py -v 2>&1 | tail -15`

Expected: fails.

- [ ] **Step 3: Create `triage/cve_signatures.py`**

```python
"""Required-node signatures per corpus CVE.

Each signature is a list of labeled regex patterns. A SQL string "matches" a
signature iff every pattern finds at least one occurrence. Patterns are
lenient on whitespace/identifier choice; they encode structural requirements
(NATURAL JOIN present, coalesce with window arg present, etc.) not byte-level
identity.

Reference: docs/cve-list.md for the original PoCs.
"""
from __future__ import annotations

import re

_CVES: list[dict] = [
    {
        "cve": "CVE-2020-15358",
        "pattern_name": "Pattern-P15358",
        "required_patterns": [
            ("CREATE_VIEW_with_ORDER_BY", re.compile(r"CREATE\s+VIEW\s+\w+.*?ORDER\s+BY", re.IGNORECASE | re.DOTALL)),
            ("INTERSECT_in_WHERE", re.compile(r"WHERE[^;]+INTERSECT", re.IGNORECASE | re.DOTALL)),
            ("SELECT_with_implicit_JOIN", re.compile(r"SELECT[^;]+FROM\s+\w+\s*,\s*\w+", re.IGNORECASE | re.DOTALL)),
        ],
    },
    {
        "cve": "CVE-2020-13871",
        "pattern_name": "Pattern-P13871",
        "required_patterns": [
            ("EXCEPT_present", re.compile(r"\bEXCEPT\b", re.IGNORECASE)),
            ("ORDER_BY_multi", re.compile(r"ORDER\s+BY\s+\w+\s*(,\s*\w+\s*){1,}", re.IGNORECASE)),
            ("Scalar_subquery", re.compile(r"SELECT\s*\(\s*SELECT", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2020-13435",
        "pattern_name": "Pattern-P13435",
        "required_patterns": [
            ("NATURAL_JOIN", re.compile(r"\bNATURAL\s+JOIN\b", re.IGNORECASE)),
            ("coalesce_call", re.compile(r"\bcoalesce\s*\(", re.IGNORECASE)),
            ("window_over", re.compile(r"\b(lead|lag|row_number|rank|dense_rank|first_value|last_value|nth_value|COUNT)\s*\([^)]*\)\s*OVER\s*\(", re.IGNORECASE)),
            ("UNIQUE_column", re.compile(r"\bUNIQUE\b", re.IGNORECASE)),
            ("IN_subquery", re.compile(r"\bIN\s*\(\s*\(", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2020-13434",
        "pattern_name": "Pattern-P13434-Boundary",
        "required_patterns": [
            ("printf_call", re.compile(r"\bprintf\s*\(", re.IGNORECASE)),
            ("INT32_boundary", re.compile(r"-?214748364[7-8]")),
        ],
    },
    {
        "cve": "CVE-2020-9327",
        "pattern_name": "Pattern-P9327",
        "required_patterns": [
            ("GENERATED_column", re.compile(r"GENERATED\s+ALWAYS\s+AS|\bAS\s*\([^)]*\)\s*(UNIQUE|NOT\s+NULL)", re.IGNORECASE)),
            ("coalesce_call", re.compile(r"\bcoalesce\s*\(", re.IGNORECASE)),
            ("JOIN_or_commajoin", re.compile(r"\bJOIN\b|FROM\s+\w+\s*,\s*\w+", re.IGNORECASE)),
            ("CREATE_VIEW", re.compile(r"CREATE\s+VIEW", re.IGNORECASE)),
        ],
    },
    {
        "cve": "CVE-2019-19646",
        "pattern_name": "Pattern-P19646",
        "required_patterns": [
            ("GENERATED_column", re.compile(r"GENERATED\s+ALWAYS\s+AS", re.IGNORECASE)),
            ("PRAGMA_integrity", re.compile(r"PRAGMA\s+integrity_check", re.IGNORECASE)),
        ],
    },
]


def all_cves() -> list[dict]:
    return list(_CVES)


def get_cve(cve_id: str) -> dict:
    for c in _CVES:
        if c["cve"] == cve_id:
            return c
    raise KeyError(cve_id)


def missing_patterns(sql: str, signature: dict) -> list[str]:
    """Return labels of patterns that do NOT match `sql`."""
    missing: list[str] = []
    for label, regex in signature["required_patterns"]:
        if not regex.search(sql):
            missing.append(label)
    return missing
```

- [ ] **Step 4: Run tests — expect pass**

Run: `pytest tests/triage/test_cve_signatures.py -v 2>&1 | tail -15`

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add tests/triage/test_cve_signatures.py triage/cve_signatures.py
git commit -m "feat(triage): add CVE signature library for per-pattern fidelity"
```

---

## Task 7 — A3 scorer: `triage/fidelity_score.py`

**Files:**
- Create: `tests/triage/test_fidelity_score.py`
- Create: `triage/fidelity_score.py`

**Context:** Drives Nautilus generator per pattern using a temp biased grammar file, pipes output through the signature library, emits `fidelity-report.json`.

- [ ] **Step 1: Write tests**

Write to `tests/triage/test_fidelity_score.py`:

```python
"""Tests for triage.fidelity_score — scores samples, writes biased grammar."""
from __future__ import annotations

from pathlib import Path

from triage import fidelity_score as fs
from triage import cve_signatures as sigs


class TestScoreSamples:
    def test_all_samples_match(self) -> None:
        samples = [
            "SELECT printf('%.*g', 2147483647, 0.01);",
            "SELECT printf('%.*g', -2147483648, 3.1);",
        ]
        sig = sigs.get_cve("CVE-2020-13434")
        result = fs.score_samples(samples, sig)
        assert result["samples_generated"] == 2
        assert result["samples_with_all_required"] == 2
        assert result["fidelity_score"] == 1.0

    def test_partial(self) -> None:
        samples = [
            "SELECT printf('%.*g', 2147483647, 0.01);",
            "SELECT length('hi');",
        ]
        sig = sigs.get_cve("CVE-2020-13434")
        result = fs.score_samples(samples, sig)
        assert result["samples_with_all_required"] == 1
        assert result["fidelity_score"] == 0.5
        assert result["samples_missing_node"]["printf_call"] == 1

    def test_zero(self) -> None:
        samples = ["SELECT 1;", "SELECT 2;"]
        sig = sigs.get_cve("CVE-2020-13435")
        result = fs.score_samples(samples, sig)
        assert result["fidelity_score"] == 0.0
        for label in ("NATURAL_JOIN", "coalesce_call", "window_over", "UNIQUE_column", "IN_subquery"):
            assert result["samples_missing_node"][label] == 2


class TestBiasedGrammar:
    def test_weights_target_high_others_zero(self, tmp_path: Path) -> None:
        base = tmp_path / "base_grammar.py"
        base.write_text(
            'ctx.rule("Sql-Stmt", "SELECT 1;")\n'
            'ctx.rule("Sql-Stmt", "{Pattern-X}")\n'
            'ctx.rule("Pattern-X", "SELECT X;")\n'
        )
        out = tmp_path / "biased.py"
        fs.write_biased_grammar(base, out, target_pattern_nt="Pattern-X", high_weight=100.0)
        text = out.read_text()
        assert 'weight=100' in text
        assert 'weight=0' in text
        # Non-Sql-Stmt rules untouched:
        assert 'ctx.rule("Pattern-X", "SELECT X;")' in text
```

- [ ] **Step 2: Run tests — expect failure**

Run: `pytest tests/triage/test_fidelity_score.py -v 2>&1 | tail -15`

Expected: fails.

- [ ] **Step 3: Create `triage/fidelity_score.py`**

```python
"""Per-pattern structural fidelity scorer.

For each pattern in the attack grammar, drives the Nautilus generator to
produce N samples biased toward that pattern's Sql-Stmt alternative, then
checks how many samples structurally match the CVE's required-node signature.

Output: fidelity-report.json matching spec §2.3 schema.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from triage import cve_signatures as sigs


def score_samples(samples: list[str], signature: dict) -> dict:
    n = len(samples)
    match_count = 0
    missing_counts: dict[str, int] = {label: 0 for label, _ in signature["required_patterns"]}
    for sql in samples:
        missing = sigs.missing_patterns(sql, signature)
        if not missing:
            match_count += 1
        for label in missing:
            missing_counts[label] += 1
    return {
        "pattern_name": signature["pattern_name"],
        "cve": signature["cve"],
        "samples_generated": n,
        "required_nodes": [label for label, _ in signature["required_patterns"]],
        "samples_with_all_required": match_count,
        "fidelity_score": (match_count / n) if n else 0.0,
        "samples_missing_node": missing_counts,
    }


def write_biased_grammar(base_grammar: Path, out: Path, target_pattern_nt: str, high_weight: float = 100.0) -> None:
    """Rewrite Sql-Stmt alternatives to bias toward the target pattern.

    Every ctx.rule("Sql-Stmt", "...") is rewritten: weight=high_weight for the
    target (matched by RHS == "{target_pattern_nt}"), weight=0 for everything
    else. Other rules are untouched.
    """
    lines_in = base_grammar.read_text().splitlines(keepends=False)
    lines_out: list[str] = []
    target_token = "{" + target_pattern_nt + "}"
    sqlstmt_re = re.compile(r'^\s*ctx\.rule\s*\(\s*"Sql-Stmt"\s*,\s*"([^"]+)"\s*\)\s*$')
    for line in lines_in:
        m = sqlstmt_re.match(line)
        if m:
            rhs = m.group(1)
            weight = high_weight if rhs == target_token else 0.0
            lines_out.append(f'ctx.rule("Sql-Stmt", "{rhs}", weight={weight})')
        else:
            lines_out.append(line)
    out.write_text("\n".join(lines_out) + "\n")


def run_generator(grammar: Path, samples: int, tree_size: int = 100) -> list[str]:
    """Invoke ./target/release/generator; split stdout into per-tree fragments."""
    cmd = [
        "./target/release/generator",
        "-g", str(grammar),
        "-t", str(tree_size),
        "-n", str(samples),
    ]
    env = os.environ.copy()
    env.setdefault("PYO3_USE_ABI3_FORWARD_COMPATIBILITY", "1")
    env.setdefault("LD_LIBRARY_PATH", "/home/linuxbrew/.linuxbrew/lib")
    env.setdefault("PYTHONPATH", str(Path.cwd()))
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=600)
    if proc.returncode != 0:
        raise RuntimeError(f"generator failed: {proc.stderr[:500]}")
    fragments: list[str] = []
    buf: list[str] = []
    for ln in proc.stdout.splitlines():
        if ln.strip() == "" and buf:
            fragments.append("\n".join(buf))
            buf = []
        else:
            buf.append(ln)
    if buf:
        fragments.append("\n".join(buf))
    return [f for f in fragments if f.strip()]


def score_all_patterns(grammar: Path, samples: int) -> dict:
    reports: list[dict] = []
    for sig in sigs.all_cves():
        pattern_nt = sig["pattern_name"]
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, dir=Path.cwd()) as tf:
            tmp_grammar = Path(tf.name)
        try:
            write_biased_grammar(grammar, tmp_grammar, pattern_nt)
            sqls = run_generator(tmp_grammar, samples)
            rep = score_samples(sqls, sig)
            reports.append(rep)
        finally:
            tmp_grammar.unlink(missing_ok=True)
    return {"patterns": reports}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--grammar", type=Path, default=Path("grammars/sqlite_attack.py"))
    p.add_argument("--samples", type=int, default=500)
    p.add_argument("--output", type=Path, default=Path("docs/fidelity-report.json"))
    args = p.parse_args(argv)
    report = score_all_patterns(args.grammar, args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2))
    for rep in report["patterns"]:
        print(f"{rep['pattern_name']:35s} fidelity={rep['fidelity_score']:.3f}  ({rep['samples_with_all_required']}/{rep['samples_generated']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run unit tests — expect pass**

Run: `pytest tests/triage/test_fidelity_score.py -v 2>&1 | tail -15`

Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add tests/triage/test_fidelity_score.py triage/fidelity_score.py
git commit -m "feat(triage): add per-pattern fidelity scorer A3"
```

---

## Task 8 — A3 baseline measurement: fidelity on attack_v1

**Files:** None created; produces `docs/fidelity-baseline-attack-v1.json`.

**Context:** Capture fidelity on the current (pre-B2) grammar as the "before" number for the ablation.

- [ ] **Step 1: Build the generator**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
export PYTHONPATH="$(pwd)"
cargo build --release --bin generator 2>&1 | tail -5
```

Expected: "Finished release..." or no-op if already built.

- [ ] **Step 2: Run A3 at N=500**

```bash
python3 -m triage.fidelity_score --grammar grammars/sqlite_attack.py --samples 500 --output docs/fidelity-baseline-attack-v1.json
```

Expected: prints per-pattern fidelity lines; writes `docs/fidelity-baseline-attack-v1.json`.

- [ ] **Step 3: Commit the baseline**

```bash
git add -f docs/fidelity-baseline-attack-v1.json
git commit -m "test(fidelity): capture attack_v1 baseline fidelity before B2"
```

---

## Task 9 — β/B2: add 7 tight NTs to `grammars/sqlite_attack.py`

**Files:**
- Modify: `grammars/sqlite_attack.py` (append Section 5b before Section 6)

**Context:** Tight NTs have one production each, encoding the exact structural skeleton of the CVE PoC. They reference loose vocabulary NTs (`Window-Func-Call`, `Agg-Func-Call`, `Col-Ref`) so composition still happens inside.

- [ ] **Step 1: Find Section 6's opening banner**

Run: `grep -n "^# SECTION 6" grammars/sqlite_attack.py`

Expected: one line number. Record it.

- [ ] **Step 2: Insert Section 5b just before Section 6**

Use Edit with `old_string` = the `# ====` line opening Section 6's banner (it's the unique `# ====` immediately above `# SECTION 6`). Prepend the Section 5b block:

Insert:

```python
# ============================================================
# SECTION 5b: Tight non-terminals for B2 fidelity (measurement-and-fidelity §3.2)
# One production each. Pattern rules in Section 6 reference these by name.
# Composition still happens INSIDE each tight rule via shared vocabulary NTs.
# ============================================================

ctx.rule("Scalar-Subquery-CoalesceWindow",
    "SELECT (SELECT coalesce({Window-Func-Call}, {Agg-Func-Call})) "
    "FROM {Table-Name} {Alias} WHERE {Col-Ref}")

ctx.rule("Join-Chain-NaturalPair",
    "JOIN {Table-Name} {Alias} ON {Expr} NATURAL JOIN {Table-Name}")

ctx.rule("Join-Chain-CommaJoin-Pair",
    ", {Table-Name}")

ctx.rule("GenCol-Def-SelfRef",
    "{Col-Name} AS ({Col-Name}) UNIQUE")

ctx.rule("GenCol-Def-NotNull",
    "{Col-Name} NOT NULL GENERATED ALWAYS AS ({Boolean-Expr})")

ctx.rule("View-Def-OrderedSelect",
    "CREATE VIEW {View-Name} AS SELECT {Col-Name} FROM {Table-Name} ORDER BY {Col-Name}")

ctx.rule("Scalar-Subquery-HavingWindow",
    "SELECT {Col-Ref} FROM {Table-Name} GROUP BY {Col-Ref} HAVING ({Coalesce-Window-Expr})")

```

- [ ] **Step 3: Python syntax check**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`

Expected: `ok`.

- [ ] **Step 4: Count `ctx.rule` lines**

Run: `grep -c "^ctx.rule" grammars/sqlite_attack.py`

Expected: `230 + 7 = 237`.

- [ ] **Step 5: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): add 7 tight NTs for B2 pattern fidelity"
```

---

## Task 10 — β/B2: rewrite 5 pattern bodies to use the tight NTs

**Files:**
- Modify: `grammars/sqlite_attack.py` (5 Edit operations in Section 6)

**Context:** One rewrite per affected pattern. P13434-Boundary and P13434-Trigger stay as-is (already high-fidelity).

- [ ] **Step 1: Rewrite `Pattern-P15358`** (use `View-Def-OrderedSelect`)

Edit `grammars/sqlite_attack.py`:

OLD:
```python
ctx.rule("Pattern-P15358",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "{View-Def};\n"
    "SELECT * FROM {Table-Name}, {Table-Name} "
    "WHERE {Col-Ref} = ({Scalar-Subquery} INTERSECT {Scalar-Subquery}) "
    "AND {Col-Ref} = {Int-Lit}")
```

NEW:
```python
ctx.rule("Pattern-P15358",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "{View-Def-OrderedSelect};\n"
    "SELECT * FROM {Table-Name}, {Table-Name} "
    "WHERE {Col-Ref} = ({Scalar-Subquery} INTERSECT {Scalar-Subquery}) "
    "AND {Col-Ref} = {Int-Lit}")
```

- [ ] **Step 2: Rewrite `Pattern-P13871`** (use `Scalar-Subquery-HavingWindow`)

OLD:
```python
ctx.rule("Pattern-P13871",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT ({Scalar-Subquery}) FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")
```

NEW:
```python
ctx.rule("Pattern-P13871",
    "CREATE TABLE {Table-Name}({Col-Name});\n"
    "SELECT ({Scalar-Subquery-HavingWindow}) FROM {Table-Name} "
    "EXCEPT SELECT {Col-Ref} FROM {Table-Name} {Order-By}")
```

- [ ] **Step 3: Rewrite `Pattern-P13435`** (use `Join-Chain-NaturalPair` + `Scalar-Subquery-CoalesceWindow`)

OLD:
```python
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery}))")
```

NEW:
```python
ctx.rule("Pattern-P13435",
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE);\n"
    "SELECT {Col-Ref} FROM {Table-Name} {Join-Chain-NaturalPair} "
    "WHERE {Col-Ref} IN (({Scalar-Subquery-CoalesceWindow}))")
```

- [ ] **Step 4: Rewrite `Pattern-P9327`** (use `Join-Chain-CommaJoin-Pair` + `GenCol-Def-SelfRef`)

OLD:
```python
ctx.rule("Pattern-P9327",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def});\n"
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE, {Col-Name} UNIQUE);\n"
    "{View-Def};\n"
    "SELECT * FROM {View-Name} {Join-Chain} WHERE {Boolean-Expr}")
```

NEW:
```python
ctx.rule("Pattern-P9327",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def-SelfRef});\n"
    "CREATE TABLE {Table-Name}({Col-Name} UNIQUE, {Col-Name} UNIQUE);\n"
    "{View-Def};\n"
    "SELECT * FROM {View-Name}{Join-Chain-CommaJoin-Pair} WHERE {Boolean-Expr}")
```

Note: no space between `{View-Name}` and `{Join-Chain-CommaJoin-Pair}` because the comma-join NT begins with `, ` itself.

- [ ] **Step 5: Rewrite `Pattern-P19646`** (use `GenCol-Def-NotNull`)

OLD:
```python
ctx.rule("Pattern-P19646",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def});\n"
    "INSERT INTO {Table-Name}({Col-Name}) VALUES ({Int-Lit});\n"
    "PRAGMA integrity_check")
```

NEW:
```python
ctx.rule("Pattern-P19646",
    "CREATE TABLE {Table-Name}({Col-Name}, {GenCol-Def-NotNull});\n"
    "INSERT INTO {Table-Name}({Col-Name}) VALUES ({Int-Lit});\n"
    "PRAGMA integrity_check")
```

- [ ] **Step 6: Python syntax check**

Run: `python3 -c "import ast; ast.parse(open('grammars/sqlite_attack.py').read()); print('ok')"`

Expected: `ok`.

- [ ] **Step 7: Smoke test**

Run: `./scripts/smoke_attack_grammar.sh 2>&1 | tail -20`

Expected: final line `SMOKE TEST PASSED`.

If it fails with "Broken Grammar" panic, inspect which NT is undefined (likely a typo in Task 9 Step 2 or one of the pattern rewrites above). Fix in place; do NOT commit broken grammar.

- [ ] **Step 8: Commit**

```bash
git add grammars/sqlite_attack.py
git commit -m "feat(grammars): rewrite 5 attack patterns to use tight NTs (B2)"
```

---

## Task 11 — Grammar spec §9 line-budget amendment

**Files:**
- Modify: `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`

**Context:** The grammar-design spec's §9 says total ~365 lines. B2 raises it to ~460. Non-behavioral amendment.

- [ ] **Step 1: Find the §9 "Total:" line**

Run: `grep -n "Total:" docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`

Expected: one line like `# Total: ~365 lines, ~58 rules`.

- [ ] **Step 2: Update it**

Edit:

OLD: `# Total: ~365 lines, ~58 rules`
NEW: `# Total: ~460 lines, ~237 rules (amended 2026-04-22 by measurement-and-fidelity spec §3.4 for B2 tight NTs)`

- [ ] **Step 3: Commit**

```bash
git add -f docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md
git commit -m "docs(spec): amend grammar §9 line budget for B2 tight NTs"
```

---

## Task 12 — A3 post-B2 measurement: fidelity on attack_v2

**Files:** None created; produces `docs/fidelity-postB2-attack-v2.json`.

- [ ] **Step 1: Run A3 at N=500 against post-B2 grammar**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="/home/linuxbrew/.linuxbrew/lib"
export PYTHONPATH="$(pwd)"
python3 -m triage.fidelity_score --grammar grammars/sqlite_attack.py --samples 500 --output docs/fidelity-postB2-attack-v2.json
```

Expected: prints per-pattern fidelity lines.

- [ ] **Step 2: Compute and display the before/after delta**

```bash
python3 - << 'PYEOF'
import json
before = json.loads(open("docs/fidelity-baseline-attack-v1.json").read())
after  = json.loads(open("docs/fidelity-postB2-attack-v2.json").read())
b = {p["pattern_name"]: p["fidelity_score"] for p in before["patterns"]}
a = {p["pattern_name"]: p["fidelity_score"] for p in after["patterns"]}
for name in sorted(a):
    bv = b.get(name, 0.0)
    av = a[name]
    print(f"{name:35s}  {bv:.3f} -> {av:.3f}   delta {av-bv:+.3f}")
PYEOF
```

Record the output. The 5 tightened patterns (P15358, P13871, P13435, P9327, P19646) should show positive deltas. If any tightened pattern shows delta < 0.1, suspect a transcription error in Task 9 or Task 10 — re-inspect the grammar.

- [ ] **Step 3: Commit post-B2 artifact**

```bash
git add -f docs/fidelity-postB2-attack-v2.json
git commit -m "test(fidelity): capture attack_v2 post-B2 fidelity"
```

---

## Task 13 — Tag `attack-v1-frozen` and materialize grammar content

**Files:** None modified (only git metadata + `/tmp` artifact).

- [ ] **Step 1: Confirm commit `2298743` exists**

Run: `git log --oneline -1 2298743 2>&1`

Expected: prints a short commit line for the pre-B2 attack grammar.

- [ ] **Step 2: Create the tag**

```bash
git tag attack-v1-frozen 2298743
git tag --list attack-v1-frozen -n
```

Expected: lists the tag.

- [ ] **Step 3: Extract the attack_v1 grammar file to `/tmp/sqlite_attack_v1.py`**

```bash
git show attack-v1-frozen:grammars/sqlite_attack.py > /tmp/sqlite_attack_v1.py
head -5 /tmp/sqlite_attack_v1.py
wc -l /tmp/sqlite_attack_v1.py
```

Expected: header comment starts with `# sqlite_attack.py — CVE-distilled attack-pattern grammar...`; line count ≈ 426.

---

## Task 14 — E2 ablation orchestrator: `scripts/run_ablation.sh`

**Files:**
- Create: `scripts/run_ablation.sh`

**Context:** Orchestrates 4 variants × 3 runs × 3600s = 12 runs sequentially against sqlite-3.31.1. Calls existing `scripts/run_eval.sh`. After each run, invokes `stack_dedup.py` to produce `dedup.json`.

- [ ] **Step 1: Create the script**

Write to `scripts/run_ablation.sh`:

```bash
#!/usr/bin/env bash
# run_ablation.sh — E2 ablation: 4 variants × 3 runs × 3600s on sqlite-3.31.1.
#
# Variants:
#   attack_v1  : /tmp/sqlite_attack_v1.py  (materialized from git tag attack-v1-frozen)
#   attack_v2  : grammars/sqlite_attack.py (current HEAD)
#   patterns   : grammars/sqlite_patterns.py
#   uniform    : grammars/sqlite_patterns_uniform.py
#
# Per Task 0 finding (b), Nautilus has no RNG seed control. The 3 runs per
# variant are independent runs (variance-estimate floor), NOT seed-controlled.
#
# Usage:
#   ./scripts/run_ablation.sh
#   DURATION=600 RUNS=1 ./scripts/run_ablation.sh    # fast debug
#
# Env overrides:
#   DURATION    seconds per run  (default: 3600)
#   RUNS        runs per variant (default: 3)
#   TARGET      SQLite version  (default: sqlite-3.31.1)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

DURATION="${DURATION:-3600}"
RUNS="${RUNS:-3}"
TARGET="${TARGET:-sqlite-3.31.1}"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

if [[ ! -f /tmp/sqlite_attack_v1.py ]]; then
    git show attack-v1-frozen:grammars/sqlite_attack.py > /tmp/sqlite_attack_v1.py
fi

HARNESS="$ROOT/harness/sqlite_harness_patterns_${TARGET}"

declare -A VARIANTS=(
    [attack_v1]="/tmp/sqlite_attack_v1.py"
    [attack_v2]="$ROOT/grammars/sqlite_attack.py"
    [patterns]="$ROOT/grammars/sqlite_patterns.py"
    [uniform]="$ROOT/grammars/sqlite_patterns_uniform.py"
)

for VARIANT in attack_v1 attack_v2 patterns uniform; do
    GRAMMAR="${VARIANTS[$VARIANT]}"
    for RUN_N in $(seq 1 "$RUNS"); do
        RUN_ID="${VARIANT}_run${RUN_N}"
        WORKDIR="/tmp/nautilus_eval/${TARGET}_${RUN_ID}"
        echo "========================================"
        echo "[ablation] $VARIANT run $RUN_N/$RUNS  grammar=$GRAMMAR"
        echo "[ablation] workdir=$WORKDIR"
        echo "========================================"
        DURATION="$DURATION" \
        GRAMMAR="$GRAMMAR" \
        HARNESS_SUFFIX=patterns_ \
        "$SCRIPT_DIR/run_eval.sh" "$TARGET" "$RUN_ID"

        echo "[ablation] running stack_dedup on $WORKDIR"
        python3 -m triage.stack_dedup "$WORKDIR" \
            --harness "$HARNESS" \
            --output "$WORKDIR/dedup.json" \
            || echo "[ablation] warning: stack_dedup failed (non-fatal)"
    done
done

echo "========================================"
echo "ABLATION SUMMARY"
echo "========================================"
printf "%-30s %-10s %-10s %-12s %-12s\n" "run_id" "signaled" "queue" "total_exec" "unique_RC"
for VARIANT in attack_v1 attack_v2 patterns uniform; do
    for RUN_N in $(seq 1 "$RUNS"); do
        RUN_ID="${VARIANT}_run${RUN_N}"
        WD="/tmp/nautilus_eval/${TARGET}_${RUN_ID}"
        SIG=$(ls "$WD/outputs/signaled/" 2>/dev/null | wc -l)
        Q=$(ls "$WD/outputs/queue/" 2>/dev/null | wc -l)
        EXEC=$(python3 -c "import json; d=json.load(open('$WD/coverage.json')); print(d.get('total_executions') or 'n/a')" 2>/dev/null || echo "n/a")
        UNQ=$(python3 -c "import json; d=json.load(open('$WD/dedup.json')); print(d.get('unique_root_causes') or 'n/a')" 2>/dev/null || echo "n/a")
        printf "%-30s %-10s %-10s %-12s %-12s\n" "$RUN_ID" "$SIG" "$Q" "$EXEC" "$UNQ"
    done
done
```

- [ ] **Step 2: Make executable**

```bash
chmod +x scripts/run_ablation.sh
```

- [ ] **Step 3: Dry-run with tiny duration**

```bash
DURATION=60 RUNS=1 ./scripts/run_ablation.sh 2>&1 | tail -40
```

Expected: runs all 4 variants at 60s each (total ~4-5 min), prints a 4-row summary table. Each workdir contains `coverage.json` and `dedup.json`. If dry-run fails, debug before the full run.

- [ ] **Step 4: Commit**

```bash
git add scripts/run_ablation.sh
git commit -m "feat(scripts): add E2 ablation orchestrator run_ablation.sh"
```

---

## Task 15 — Run the full E2 ablation (~12 hours wall time)

**Files:** None; produces 12 workdirs under `/tmp/nautilus_eval/`.

- [ ] **Step 1: Confirm preconditions**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
ls -l harness/sqlite_harness_patterns_sqlite-3.31.1
wc -l grammars/sqlite_attack.py grammars/sqlite_patterns.py grammars/sqlite_patterns_uniform.py
git tag --list attack-v1-frozen
ls -l /tmp/sqlite_attack_v1.py 2>/dev/null || git show attack-v1-frozen:grammars/sqlite_attack.py > /tmp/sqlite_attack_v1.py
```

Expected: harness exists; 4 grammar sources in place; tag exists; `/tmp/sqlite_attack_v1.py` ~426 lines.

- [ ] **Step 2: Run the full ablation**

~12 hours wall time. Dispatch a dedicated long-lived subagent or run in a detached terminal. Example foreground:

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
./scripts/run_ablation.sh 2>&1 | tee /tmp/ablation-$(date +%Y%m%d-%H%M).log
```

Expected: at the end, the script prints a 12-row summary table.

- [ ] **Step 3: Copy the raw log into the repo**

```bash
LOG=$(ls -t /tmp/ablation-*.log | head -1)
cp "$LOG" docs/ablation-raw-log-sqlite-3.31.1.txt
git add -f docs/ablation-raw-log-sqlite-3.31.1.txt
git commit -m "docs: attach raw E2 ablation log"
```

---

## Task 16 — Analyze E2 results and write the ablation report

**Files:**
- Create: `docs/attack-grammar-ablation-sqlite-3.31.1.md`

**Context:** Synthesize 12 runs into an ablation report covering the 4 acceptance criteria from spec §4.5. Record numbers honestly.

- [ ] **Step 1: Collect per-run numbers**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
python3 - << 'PYEOF'
import json, os
from statistics import mean, stdev
TARGET = "sqlite-3.31.1"
variants = ["attack_v1", "attack_v2", "patterns", "uniform"]
rows = []
for v in variants:
    for run in (1, 2, 3):
        wd = f"/tmp/nautilus_eval/{TARGET}_{v}_run{run}"
        if not os.path.isdir(wd):
            print(f"MISSING: {wd}")
            continue
        cov = json.load(open(f"{wd}/coverage.json"))
        try:
            dd = json.load(open(f"{wd}/dedup.json"))
        except FileNotFoundError:
            dd = {"unique_root_causes": None}
        rows.append({
            "variant": v, "run": run,
            "signaled": cov.get("signaled_final"),
            "queue":    cov.get("queue_final"),
            "timeout":  cov.get("timeout_final"),
            "total_exec": cov.get("total_executions"),
            "unique_rc":  dd.get("unique_root_causes"),
        })
print()
print(f"{'variant':12s} {'mean_sig':>10s} {'sd_sig':>8s} {'mean_unq':>10s} {'sd_unq':>8s} {'mean_exec':>12s}")
for v in variants:
    rs = [r for r in rows if r["variant"] == v]
    if not rs: continue
    sig = [r["signaled"] for r in rs if r["signaled"] is not None]
    unq = [r["unique_rc"] for r in rs if r["unique_rc"] is not None]
    exc = [r["total_exec"] for r in rs if r["total_exec"] is not None]
    sd_sig = stdev(sig) if len(sig) > 1 else 0
    sd_unq = stdev(unq) if len(unq) > 1 else 0
    print(f"{v:12s} {mean(sig):>10.1f} {sd_sig:>8.2f} {(mean(unq) if unq else float('nan')):>10.2f} {sd_unq:>8.2f} {(mean(exc) if exc else float('nan')):>12.0f}")
PYEOF
```

Record the table. Note any `MISSING` lines.

- [ ] **Step 2: Load fidelity scores**

```bash
python3 - << 'PYEOF'
import json
b = json.load(open("docs/fidelity-baseline-attack-v1.json"))
a = json.load(open("docs/fidelity-postB2-attack-v2.json"))
bm = {p["pattern_name"]: p["fidelity_score"] for p in b["patterns"]}
am = {p["pattern_name"]: p["fidelity_score"] for p in a["patterns"]}
print(f"{'pattern':35s} {'v1':>8s} {'v2':>8s} {'delta':>8s}")
for name in sorted(am):
    print(f"{name:35s} {bm.get(name,0):>8.3f} {am[name]:>8.3f} {am[name]-bm.get(name,0):>+8.3f}")
PYEOF
```

Record the table.

- [ ] **Step 3: Write the report**

Write to `docs/attack-grammar-ablation-sqlite-3.31.1.md`:

```markdown
# E2 Ablation Report — attack_v1 vs attack_v2 vs patterns vs uniform

**Date:** <YYYY-MM-DD from Task 15>
**Target:** sqlite-3.31.1 (ASan + UBSan, harness `sqlite_harness_patterns_sqlite-3.31.1`)
**Duration per run:** 3600 s (1 hour)
**Runs per variant:** 3 (independent — no RNG seed per Task 0 finding b)
**Spec:** `docs/superpowers/specs/2026-04-22-measurement-and-fidelity-design.md`

## TL;DR

<One sentence summarizing direction. Example:
"attack_v2 finds <X> unique root causes vs attack_v1's <Y>; criterion 2 PASS,
criterion 1 <PASS/FAIL>, criterion 3 PASS, criterion 4 <PASS/FAIL> — overall
thesis-<positive/neutral/negative>.">

## Mean ± standard deviation per variant

| Variant | mean signaled | sd signaled | mean unique_RC | sd unique_RC | mean total_exec |
|---|---|---|---|---|---|
| attack_v1 | <from Step 1> | | | | |
| attack_v2 | | | | | |
| patterns  | | | | | |
| uniform   | | | | | |

## Per-run raw numbers

| run | signaled | queue | timeout | total_exec | unique_RC |
|---|---|---|---|---|---|
| attack_v1_run1 | | | | | |
| attack_v1_run2 | | | | | |
| attack_v1_run3 | | | | | |
| attack_v2_run1 | | | | | |
| attack_v2_run2 | | | | | |
| attack_v2_run3 | | | | | |
| patterns_run1  | | | | | |
| patterns_run2  | | | | | |
| patterns_run3  | | | | | |
| uniform_run1   | | | | | |
| uniform_run2   | | | | | |
| uniform_run3   | | | | | |

## Per-pattern fidelity (A3): attack_v1 vs attack_v2

| Pattern | v1 fidelity | v2 fidelity | delta |
|---|---|---|---|
| <from Step 2> | | | |

## Acceptance per spec §4.5

| Criterion | Outcome |
|---|---|
| 1. attack_v2 hits ≥ 5 of 6 CVE classes | <PASS/FAIL + count> |
| 2. attack_v2 unique_RC > attack_v1 in all 3 seeds (median ≥ 2×) | <PASS/FAIL + numbers> |
| 3. Tight-NT patterns ≥ 50% fidelity | <PASS/FAIL + list> |
| 4. attack_v2 coverage ≥ 90% of patterns coverage | <PASS/FAIL + ratio> |

## Interpretation

<2-3 paragraphs. No spin. Hooks:>

- Did A3's fidelity gain translate to E2's unique_RC gain?
- Are the CVE classes missed by attack_v2 the same as those missed by attack_v1? If so, B2 didn't fix the scheduler-selection problem.
- Does attack_v2 uniquely hit any CVE class that no other variant hits?

## Methodology caveats

1. n=3 independent runs per variant (no seed control — Task 0 finding b). Variance estimates are lower-bounded; statistical-significance claims are weaker than a seeded design would support.
2. Coverage captured only end-of-run. `bits_found_by_*` counters not written to disk by current Nautilus (Task 0 finding a). Coverage proxy is `queue_final`.
3. CVE-class hit regex classifier has known false negatives.
4. Stack-dedup depends on gdb successfully replaying crashes; crashes that gdb cannot reproduce are excluded from unique_RC counts.

## Next steps

<branching based on outcome:>

If criteria 1, 2, 3, 4 all PASS: proceed to E3 (24h × 4 SQLite versions). Write a follow-up spec.

If criterion 1 fails but 2, 3, 4 PASS: B2 worked but scheduler-selection still misses patterns. Write a weights spec.

If criterion 2 fails: tightening did not help bug-finding despite fidelity gain. Post-mortem spec, not a weights spec.

If criterion 3 fails: A3 is measuring wrong OR tight NTs still too loose. Re-inspect one tight NT side-by-side with its CVE PoC.

If criterion 4 fails: B2 over-constrained. Roll back to B1-style partial tightening.

## Raw workdir locations

- `/tmp/nautilus_eval/sqlite-3.31.1_attack_v1_run1/` ... `run3/`
- `/tmp/nautilus_eval/sqlite-3.31.1_attack_v2_run1/` ... `run3/`
- `/tmp/nautilus_eval/sqlite-3.31.1_patterns_run1/` ... `run3/`
- `/tmp/nautilus_eval/sqlite-3.31.1_uniform_run1/` ... `run3/`

Each contains `exec.log`, `coverage.json`, `dedup.json`, and `outputs/{queue,signaled,timeout}/`.
```

Fill every `<...>` placeholder with actual numbers from Steps 1-2. Do NOT commit with placeholders remaining.

- [ ] **Step 4: Verify no placeholders**

Run: `grep -nE '<[A-Za-z/]' docs/attack-grammar-ablation-sqlite-3.31.1.md | grep -v -E '<!--' || echo "no placeholders"`

Expected: `no placeholders`.

- [ ] **Step 5: Commit**

```bash
git add -f docs/attack-grammar-ablation-sqlite-3.31.1.md
git commit -m "docs: E2 ablation report — attack_v2 vs attack_v1/patterns/uniform"
```

---

## Task 17 — Final verification

**Files:** None.

- [ ] **Step 1: Check all deliverables exist**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
echo "-- Deliverables --"
ls -l triage/stack_dedup.py triage/fidelity_score.py triage/cve_signatures.py
ls -l scripts/capture_coverage.py scripts/run_ablation.sh scripts/run_eval.sh
ls -l docs/fidelity-baseline-attack-v1.json docs/fidelity-postB2-attack-v2.json
ls -l docs/attack-grammar-ablation-sqlite-3.31.1.md
ls -l docs/task-0-findings.md
git tag --list attack-v1-frozen
echo "-- Test suite --"
pytest tests/triage/ -v 2>&1 | tail -10
echo "-- Grammar smoke --"
./scripts/smoke_attack_grammar.sh 2>&1 | tail -3
echo "-- Git log --"
git log --oneline -20
```

Expected: all deliverables listed; tests all PASS; smoke PASSES; git log shows all task commits.

- [ ] **Step 2: On any failure, report BLOCKED and go back to the failing task**

Do not declare completion if any of: grammar smoke fails, any pytest fails, any deliverable missing.

- [ ] **Step 3: Declare complete**

No commit. Produce a short status summary:
- Tests: pass / fail
- Grammar smoke: pass / fail
- E2 ablation outcome: criteria 1/2/3/4 pass/fail
- Thesis verdict (from the report's TL;DR)

---

## Out of scope (explicit exclusions)

- **Fuzzer-source changes** (Nautilus `fuzzer.rs`, `grammartec`). Specifically excludes writing `bits_found_by_*` to disk and adding RNG seed control.
- **Weights on `Sql-Stmt` alternatives.** Pattern selection remains uniform. If criterion 1 fails, a follow-up spec adds weights.
- **RL / DQN / Phase-2 RL hooks.** No changes in `fuzzer/src/dqn.rs`.
- **E3 (full 24h × 4 versions) campaign.** Deferred contingent on E2 being thesis-positive.
- **Cross-DBMS porting** (DuckDB, MySQL).
- **cve2grammar integration.** Separate thesis contribution.
- **Coverage-over-time curves and time-series analysis.** v1 captures end-of-run only.

---

## Self-review (performed at plan-write time)

**Spec coverage check:**

| Spec section | Implementing task(s) |
|---|---|
| §1 Motivation | Plan header + Task 0 |
| §2.1 A1 stack dedup | Tasks 1, 2, 3 |
| §2.2 A2 coverage capture | Tasks 4, 5 |
| §2.3 A3 fidelity scorer | Tasks 6, 7, 8, 12 |
| §3.1 B2 design principle | Tasks 9, 10 (task contexts) |
| §3.2 seven tight NTs | Task 9 |
| §3.3 pattern rewrite examples | Task 10 |
| §3.4 line budget amendment | Task 11 |
| §3.5 "does NOT" exclusions | Out-of-scope list + Task 9/10 guardrails |
| §4.1 four variants | Tasks 13, 14 |
| §4.2 matrix | Task 14, 15 |
| §4.3 metrics | Task 14 summary table + Task 16 |
| §4.4 statistics | Task 16 Step 1 |
| §4.5 acceptance criteria | Task 16 Step 3 (report structure) |
| §4.6 E2 gates E3 | Out-of-scope list + Task 16 Next Steps |
| §5 sequencing | Task ordering 0 → 17 implements Day 1-5 |
| §6 open questions | Task 0 resolves a/b/c; tree-sitter fallback honored in Task 6 regex-only |

**Placeholder scan:**
- Task 3 Step 2 template uses `<WORKDIR>`, `<N>`, `<K>`, `<FRAME>` — the task documents two commit paths (workdir-present vs deferred) explicitly. Acceptable.
- Task 5 Step 2 says "if the existing script uses different variable names, substitute them" — a deliberate lightweight instruction to the engineer, not a hand-wave.
- Task 16 Step 3 report template has `<...>` fields; Task 16 Step 4 greps for unfilled placeholders and blocks commit if any remain.
- No TBD/TODO elsewhere.

**Type consistency:**
- `dedup.json` / `coverage.json` / `fidelity-report.json` schemas match across Task 2, 4, 7 usage.
- Function names match between tests and impl: `filter_frames`, `hash_frames`, `parse_gdb_bt`, `build_clusters` (Task 1 & 2); `parse_exec_count`, `count_outputs`, `build_coverage`, `main` (Task 4); `score_samples`, `write_biased_grammar`, `run_generator`, `score_all_patterns` (Task 7); `all_cves`, `get_cve`, `missing_patterns` (Task 6).
- Variable names in `run_ablation.sh` (GRAMMAR, HARNESS_SUFFIX, DURATION, TARGET, RUN_ID) match those used by existing `run_eval.sh`.
- Ablation variant names (`attack_v1`, `attack_v2`, `patterns`, `uniform`) match across Task 13, 14, 16.

End of plan.
