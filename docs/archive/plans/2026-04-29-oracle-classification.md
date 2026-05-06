# Oracle Classification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace `triage/dedup.py` + `triage/report.py` with a single `triage/classify.py` that deduplicates, classifies (ASan/UBSan/debug_assert), and generates triage.json + dedup/ + triage_report.md in one pass.

**Architecture:** Single-pass pipeline — re-run each crash from `outputs/signaled/` once via subprocess, classify by exit code, hash stack frames for dedup, accumulate results, write three output artifacts. Integrate into run_eval.sh (auto-triage) and archive_campaign.sh (campaign.json enrichment).

**Tech Stack:** Python 3.13, subprocess, argparse, json, re, hashlib, pathlib. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-04-29-oracle-classification-design.md`

---

### Task 1: Core classification + dedup logic (classify.py)

**Files:**
- Create: `triage/classify.py`
- Test: `tests/triage/test_classify.py`

- [ ] **Step 1: Write failing tests for classification logic**

Create `tests/triage/test_classify.py` with tests for the two pure functions: `classify_crash()` and `extract_asan_frames()`.

```python
"""Tests for triage.classify."""
from __future__ import annotations

from triage.classify import classify_crash, extract_frames


class TestClassifyCrash:
    def test_asan_heap_buffer_overflow(self) -> None:
        result = classify_crash(223, "==12345==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x...")
        assert result == ("asan", "heap-buffer-overflow")

    def test_asan_use_after_free(self) -> None:
        result = classify_crash(223, "==12345==ERROR: AddressSanitizer: heap-use-after-free on address 0x...")
        assert result == ("asan", "use-after-free")

    def test_asan_stack_buffer_overflow(self) -> None:
        result = classify_crash(223, "==12345==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x...")
        assert result == ("asan", "stack-buffer-overflow")

    def test_asan_null_deref(self) -> None:
        result = classify_crash(223, "SEGV on unknown address 0x000000000000 (pc 0x...)\n...null dereference...")
        assert result == ("asan", "null-dereference")

    def test_asan_other(self) -> None:
        result = classify_crash(223, "==12345==ERROR: AddressSanitizer: something-unknown")
        assert result == ("asan", "asan-other")

    def test_ubsan_integer_overflow(self) -> None:
        result = classify_crash(1, "sqlite3.c:28528:15: runtime error: signed integer overflow: 2147483647 * 10")
        assert result == ("ubsan", "integer-overflow")

    def test_ubsan_null_pointer(self) -> None:
        result = classify_crash(1, "sqlite3.c:100:5: runtime error: null pointer passed as argument 1")
        assert result == ("ubsan", "null-pointer")

    def test_ubsan_shift(self) -> None:
        result = classify_crash(1, "sqlite3.c:500:3: runtime error: shift exponent 64 is too large")
        assert result == ("ubsan", "shift-exponent")

    def test_ubsan_other(self) -> None:
        result = classify_crash(1, "sqlite3.c:1:1: runtime error: load of misaligned address")
        assert result == ("ubsan", "ubsan-other")

    def test_ubsan_no_runtime_error_line(self) -> None:
        result = classify_crash(1, "some other stderr output without runtime error")
        assert result == ("ubsan", "ubsan-other")

    def test_debug_assert_exit_0(self) -> None:
        result = classify_crash(0, "")
        assert result == ("debug_assert", None)

    def test_signal_negative_exit(self) -> None:
        result = classify_crash(-11, "")
        assert result == ("signal", "signal-11")

    def test_timeout(self) -> None:
        result = classify_crash(-1, "")
        assert result == ("timeout", None)


class TestExtractFrames:
    def test_extracts_asan_frames(self) -> None:
        stderr = (
            "==12345==ERROR: AddressSanitizer: heap-buffer-overflow\n"
            "    #0 0xdeadbeef in sqlite3_str_vappendf sqlite3.c:28528\n"
            "    #1 0xcafebabe in sqlite3VXPrintf sqlite3.c:28810\n"
            "    #2 0x12345678 in __asan_report_error asan_report.cc:200\n"
        )
        frames = extract_frames(stderr)
        assert frames == ["sqlite3_str_vappendf", "sqlite3VXPrintf", "__asan_report_error"]

    def test_extracts_ubsan_runtime_error(self) -> None:
        stderr = "sqlite3.c:28528:15: runtime error: signed integer overflow: 2147483647 * 10\n"
        frames = extract_frames(stderr)
        assert len(frames) >= 1
        assert "runtime error:" in frames[0]

    def test_empty_stderr(self) -> None:
        frames = extract_frames("")
        assert frames == []

    def test_max_frames_limit(self) -> None:
        lines = [f"    #{i} 0x{i:08x} in func_{i} file.c:{i}\n" for i in range(20)]
        stderr = "".join(lines)
        frames = extract_frames(stderr, max_frames=5)
        assert len(frames) == 5
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/triage/test_classify.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'triage.classify'`

- [ ] **Step 3: Implement classify.py core functions**

Create `triage/classify.py` with the classification logic, frame extraction, crash runner, and single-pass triage pipeline:

```python
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
from dataclasses import asdict, dataclass, field
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
    if exit_code == -1:
        return ("timeout", None)
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
        m = re.search(r"runtime error:\s*(.+)", stderr)
        if m:
            kind = m.group(1).strip()
            if "integer overflow" in kind:
                return ("ubsan", "integer-overflow")
            if "null pointer" in kind:
                return ("ubsan", "null-pointer")
            if "shift exponent" in kind:
                return ("ubsan", "shift-exponent")
            if "signed integer overflow" in kind:
                return ("ubsan", "signed-integer-overflow")
            return ("ubsan", "ubsan-other")
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/triage/test_classify.py -v`
Expected: All 17 tests PASS

- [ ] **Step 5: Commit**

```bash
git add triage/classify.py tests/triage/test_classify.py
git commit -m "feat(triage): add classify.py — unified dedup + classification + report"
```

---

### Task 2: Tests for clustering, triage.json output, and report generation

**Files:**
- Modify: `tests/triage/test_classify.py`

- [ ] **Step 1: Add tests for build_clusters()**

Append to `tests/triage/test_classify.py`:

```python
from triage.classify import CrashResult, build_clusters, write_triage_json, write_report_md
import json
import tempfile
from pathlib import Path


class TestBuildClusters:
    def _make_result(self, file_name: str, crash_type: str, subtype: str | None,
                     exit_code: int, frames: tuple[str, ...] = ("func_a",),
                     stack_hash: str = "aaa") -> CrashResult:
        return CrashResult(
            file_name=file_name,
            exit_code=exit_code,
            crash_type=crash_type,
            subtype=subtype,
            frames=frames,
            sql_preview="SELECT 1;",
            stack_hash=stack_hash,
        )

    def test_groups_same_hash(self) -> None:
        results = [
            self._make_result("sig_001", "ubsan", "integer-overflow", 1, stack_hash="abc123"),
            self._make_result("sig_002", "ubsan", "integer-overflow", 1, stack_hash="abc123"),
            self._make_result("sig_003", "ubsan", "integer-overflow", 1, stack_hash="abc123"),
        ]
        clusters = build_clusters(results)
        assert len(clusters) == 1
        assert clusters[0].count == 3
        assert clusters[0].crash_type == "ubsan"

    def test_splits_different_hashes(self) -> None:
        results = [
            self._make_result("sig_001", "ubsan", "integer-overflow", 1, stack_hash="abc123"),
            self._make_result("sig_002", "debug_assert", None, 0, stack_hash="def456"),
        ]
        clusters = build_clusters(results)
        assert len(clusters) == 2

    def test_sorted_by_count_desc(self) -> None:
        results = [
            self._make_result("sig_001", "debug_assert", None, 0, stack_hash="big"),
            self._make_result("sig_002", "debug_assert", None, 0, stack_hash="big"),
            self._make_result("sig_003", "debug_assert", None, 0, stack_hash="big"),
            self._make_result("sig_004", "ubsan", "integer-overflow", 1, stack_hash="small"),
        ]
        clusters = build_clusters(results)
        assert clusters[0].count == 3
        assert clusters[1].count == 1


class TestWriteTriageJson:
    def test_writes_valid_json(self) -> None:
        results = [
            CrashResult("sig_001", 1, "ubsan", "integer-overflow", ("sqlite3_str_vappendf",), "SELECT 1;", "abc123"),
            CrashResult("sig_002", 1, "ubsan", "integer-overflow", ("sqlite3_str_vappendf",), "SELECT 2;", "abc123"),
            CrashResult("sig_003", 0, "debug_assert", None, ("<no-stack-xyz>",), "CREATE...", "def456"),
        ]
        clusters = build_clusters(results)
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            tmp = Path(f.name)
        try:
            report = write_triage_json(clusters, 3, tmp)
            data = json.loads(tmp.read_text())
            assert data["total_crashes"] == 3
            assert data["unique_crashes"] == 2
            assert data["summary"]["ubsan"] == 1
            assert data["summary"]["debug_assert"] == 1
            assert data["summary"]["asan"] == 0
            assert len(data["crashes"]) == 2
        finally:
            tmp.unlink(missing_ok=True)


class TestWriteReportMd:
    def test_generates_markdown_with_summary_table(self) -> None:
        results = [
            CrashResult("sig_001", 1, "ubsan", "integer-overflow", ("sqlite3_str_vappendf",), "SELECT printf(...);", "abc123"),
            CrashResult("sig_002", 0, "debug_assert", None, ("<no-stack-xyz>",), "CREATE VIRTUAL TABLE...", "def456"),
        ]
        clusters = build_clusters(results)
        with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as f:
            tmp = Path(f.name)
        try:
            write_report_md(clusters, 2, tmp)
            md = tmp.read_text()
            assert "# Crash Triage Report" in md
            assert "| UBSan |" in md
            assert "| Debug Assert |" in md
            assert "```sql" in md
        finally:
            tmp.unlink(missing_ok=True)
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `python3 -m pytest tests/triage/test_classify.py -v`
Expected: All tests PASS (17 from Task 1 + 6 new = 23 total)

- [ ] **Step 3: Commit**

```bash
git add tests/triage/test_classify.py
git commit -m "test(triage): add cluster, triage.json, and report tests for classify.py"
```

---

### Task 3: Enrich campaign.json logic + tests

**Files:**
- Modify: `tests/triage/test_classify.py`

- [ ] **Step 1: Add tests for enrich_campaign_json()**

Append to `tests/triage/test_classify.py`:

```python
from triage.classify import enrich_campaign_json, CrashCluster


class TestEnrichCampaignJson:
    def test_adds_crash_classification(self) -> None:
        clusters = [
            CrashCluster("abc123", "ubsan", "integer-overflow", 1, 24, "sig_001", ["sqlite3_str_vappendf"], "SELECT..."),
            CrashCluster("def456", "debug_assert", None, 0, 97, "sig_002", [], "CREATE..."),
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump({"id": "test", "results": {"crashes": 121, "queue_paths": 1472}}, f)
            tmp = Path(f.name)
        try:
            enrich_campaign_json(clusters, tmp)
            data = json.loads(tmp.read_text())
            cc = data["results"]["crash_classification"]
            assert cc["unique_crash_sites"] == 2
            assert cc["ubsan"] == 24
            assert cc["debug_assert"] == 97
            assert cc["asan"] == 0
            assert cc["signal"] == 0
            assert cc["timeout"] == 0
        finally:
            tmp.unlink(missing_ok=True)

    def test_preserves_existing_fields(self) -> None:
        clusters = [
            CrashCluster("abc123", "asan", "heap-buffer-overflow", 223, 5, "sig_001", ["func"], "SELECT..."),
        ]
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode="w") as f:
            json.dump({"id": "test", "results": {"crashes": 5, "queue_paths": 100}, "tags": ["E1"]}, f)
            tmp = Path(f.name)
        try:
            enrich_campaign_json(clusters, tmp)
            data = json.loads(tmp.read_text())
            assert data["tags"] == ["E1"]
            assert data["results"]["crashes"] == 5
            assert data["results"]["queue_paths"] == 100
            assert data["results"]["crash_classification"]["asan"] == 5
        finally:
            tmp.unlink(missing_ok=True)
```

- [ ] **Step 2: Run tests to verify they pass**

Run: `python3 -m pytest tests/triage/test_classify.py -v`
Expected: All 25 tests PASS

- [ ] **Step 3: Commit**

```bash
git add tests/triage/test_classify.py
git commit -m "test(triage): add campaign.json enrichment tests"
```

---

### Task 4: Update run_eval.sh — add auto-triage step

**Files:**
- Modify: `scripts/run_eval.sh:118-157`

- [ ] **Step 1: Add classify.py call between coverage capture and archive**

In `scripts/run_eval.sh`, replace the manual triage hints (lines 125-128) with auto-triage, and add the classify.py step after coverage capture:

Replace:
```bash
echo ""
echo "Run triage:"
echo "  python3 triage/dedup.py $WORKDIR --harness $HARNESS_BIN --output $WORKDIR/dedup"
echo "  python3 triage/minimize.py <crash> --harness $HARNESS_BIN"
echo "  python3 triage/report.py $WORKDIR/dedup --harness $HARNESS_BIN --output $WORKDIR/report.md"
```

With:
```bash
echo ""
echo "Run further analysis:"
echo "  python3 triage/stack_dedup.py $WORKDIR --harness $HARNESS_BIN"
echo "  python3 triage/minimize.py <crash> --harness $HARNESS_BIN"
```

Then after the coverage capture block (after line 137), add:

```bash
# ----------------------------------------------------------------
# Auto-triage: classify + dedup crashes
# ----------------------------------------------------------------
echo "[run_eval] classifying crashes..."
python3 "$ROOT/triage/classify.py" "$WORKDIR" \
    --harness "$HARNESS_BIN" \
    --output "$WORKDIR/triage.json" \
    --dedup-dir "$WORKDIR/dedup" \
    --report "$WORKDIR/triage_report.md" \
    || echo "[run_eval] warning: crash classification failed (non-fatal)"
```

- [ ] **Step 2: Verify run_eval.sh is syntactically valid**

Run: `bash -n scripts/run_eval.sh`
Expected: No output (no syntax errors)

- [ ] **Step 3: Commit**

```bash
git add scripts/run_eval.sh
git commit -m "feat(pipeline): auto-triage crashes via classify.py in run_eval.sh"
```

---

### Task 5: Update archive_campaign.sh — merge triage into campaign.json

**Files:**
- Modify: `scripts/archive_campaign.sh:136-158`

- [ ] **Step 1: Add triage.json reading after campaign.json is written**

In `scripts/archive_campaign.sh`, after the `ENDJSON` heredoc (line 135) and before the dedup.json copy (line 138), add a block that reads triage.json and merges crash_classification into campaign.json:

After line 135 (`ENDJSON`), insert:

```bash
# Merge crash classification from triage.json if present
if [[ -f "$WORKDIR/triage.json" ]]; then
    python3 -c "
import json, sys
with open('$ARCHIVE_DIR/campaign.json') as f:
    campaign = json.load(f)
with open('$WORKDIR/triage.json') as f:
    triage = json.load(f)
totals = {'asan': 0, 'ubsan': 0, 'debug_assert': 0, 'signal': 0, 'timeout': 0}
for c in triage.get('crashes', []):
    key = c['type'] if c['type'] in totals else 'signal'
    totals[key] += c['count']
campaign['results']['crash_classification'] = {
    'unique_crash_sites': triage['unique_crashes'],
    **totals,
}
with open('$ARCHIVE_DIR/campaign.json', 'w') as f:
    json.dump(campaign, f, indent=2)
print(f'[archive] merged crash classification into campaign.json')
" || echo "[archive] warning: triage merge failed (non-fatal)"
    # Copy triage.json and report to archive
    cp "$WORKDIR/triage.json" "$ARCHIVE_DIR/triage.json" 2>/dev/null || true
    cp "$WORKDIR/triage_report.md" "$ARCHIVE_DIR/triage_report.md" 2>/dev/null || true
fi
```

- [ ] **Step 2: Verify archive_campaign.sh is syntactically valid**

Run: `bash -n scripts/archive_campaign.sh`
Expected: No output (no syntax errors)

- [ ] **Step 3: Commit**

```bash
git add scripts/archive_campaign.sh
git commit -m "feat(archive): merge triage.json crash classification into campaign.json"
```

---

### Task 6: Update compare_campaigns.py — show classification columns

**Files:**
- Modify: `scripts/compare_campaigns.py:49-117`

- [ ] **Step 1: Add classification columns to markdown render**

In `scripts/compare_campaigns.py`, modify `render_markdown()` to add classification columns when data is available:

Replace the `headers` and row-building logic in `render_markdown()`:

```python
def render_markdown(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"## Experiment: {tag}")
    lines.append(f"**Hypothesis:** {experiment['hypothesis']}")
    lines.append("")

    if not campaigns:
        lines.append("*No archived campaigns yet.*")
        if experiment.get("conclusion"):
            lines.append(f"\n**Conclusion:** {experiment['conclusion']}")
        return "\n".join(lines)

    has_classification = any(
        c.get("results", {}).get("crash_classification") for c in campaigns
    )

    headers = ["Campaign", "Grammar", "Target", "Duration", "Crashes", "Queue", "Unique RC"]
    if has_classification:
        headers += ["ASan", "UBSan", "Assert", "Signal"]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        if has_classification:
            cc = r.get("crash_classification", {})
            row += [
                str(cc.get("asan", "—")),
                str(cc.get("ubsan", "—")),
                str(cc.get("debug_assert", "—")),
                str(cc.get("signal", "—")),
            ]
        lines.append("| " + " | ".join(row) + " |")

    conclusion = experiment.get("conclusion")
    if conclusion:
        lines.append(f"\n**Conclusion:** {conclusion}")
    else:
        lines.append("\n**Conclusion:** *pending*")

    return "\n".join(lines)
```

Apply the same pattern to `render_latex()`:

```python
def render_latex(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"% Experiment: {tag}")
    lines.append(f"% Hypothesis: {experiment['hypothesis']}")

    has_classification = any(
        c.get("results", {}).get("crash_classification") for c in campaigns
    )

    col_spec = "lllrrrr" + ("rrrr" if has_classification else "")
    lines.append("\\begin{table}[h]")
    lines.append("\\centering")
    lines.append(f"\\caption{{Experiment: {tag}}}")
    lines.append(f"\\begin{{tabular}}{{{col_spec}}}")
    lines.append("\\toprule")

    header = "Campaign & Grammar & Target & Duration & Crashes & Queue & Unique RC"
    if has_classification:
        header += " & ASan & UBSan & Assert & Signal"
    lines.append(header + " \\\\")
    lines.append("\\midrule")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]).replace("_", "\\_"),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        if has_classification:
            cc = r.get("crash_classification", {})
            row += [
                str(cc.get("asan", "--")),
                str(cc.get("ubsan", "--")),
                str(cc.get("debug_assert", "--")),
                str(cc.get("signal", "--")),
            ]
        lines.append(" & ".join(row) + " \\\\")

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    return "\n".join(lines)
```

- [ ] **Step 2: Run a quick sanity check**

Run: `python3 scripts/compare_campaigns.py --list`
Expected: Lists experiments without errors

- [ ] **Step 3: Commit**

```bash
git add scripts/compare_campaigns.py
git commit -m "feat(compare): show crash classification columns in thesis tables"
```

---

### Task 7: Delete old files + update triage hints

**Files:**
- Delete: `triage/dedup.py`
- Delete: `triage/report.py`

- [ ] **Step 1: Verify no other code imports from dedup.py or report.py**

Run: `grep -r "from triage.dedup\|from triage.report\|import dedup\|import report" --include="*.py" .`
Expected: No results (or only the files themselves)

Run: `grep -r "triage/dedup.py\|triage/report.py" --include="*.sh" --include="*.py" --include="*.md" .`
Expected: No results in scripts or active docs (only in this plan or old specs)

- [ ] **Step 2: Delete the old files**

```bash
git rm triage/dedup.py triage/report.py
```

- [ ] **Step 3: Run all triage tests to confirm nothing breaks**

Run: `python3 -m pytest tests/triage/ -v`
Expected: All tests pass (test_classify.py, test_stack_dedup.py, test_fidelity_score.py, test_cve_signatures.py, test_capture_coverage.py)

- [ ] **Step 4: Commit**

```bash
git rm triage/dedup.py triage/report.py
git commit -m "chore(triage): remove dedup.py and report.py (replaced by classify.py)"
```

---

### Task 8: End-to-end integration test with mock workdir

**Files:**
- Modify: `tests/triage/test_classify.py`

- [ ] **Step 1: Add integration test using a temp workdir with fake crash files**

Append to `tests/triage/test_classify.py`:

```python
class TestTriageIntegration:
    """Integration test with a mock workdir (no real harness needed)."""

    def test_full_triage_with_mocked_crashes(self, tmp_path: Path, monkeypatch) -> None:
        signaled = tmp_path / "outputs" / "signaled"
        signaled.mkdir(parents=True)
        (signaled / "sig_001").write_text("SELECT printf('%d', 2147483647);")
        (signaled / "sig_002").write_text("SELECT printf('%d', -2147483648);")
        (signaled / "sig_003").write_text("CREATE VIRTUAL TABLE fts USING fts5(a);")

        call_count = 0

        def mock_run_crash(harness: str, crash_file: str, timeout: int = 5) -> tuple[int, str]:
            nonlocal call_count
            call_count += 1
            if "sig_003" in crash_file:
                return 0, ""
            return 1, "sqlite3.c:28528:15: runtime error: signed integer overflow\n    #0 0xdead in sqlite3_str_vappendf sqlite3.c:28528\n"

        import triage.classify
        monkeypatch.setattr(triage.classify, "run_crash", mock_run_crash)

        from triage.classify import triage as run_triage
        result = run_triage(
            workdir=str(tmp_path),
            harness="/fake/harness",
            output=str(tmp_path / "triage.json"),
            dedup_dir=str(tmp_path / "dedup"),
            report=str(tmp_path / "triage_report.md"),
        )

        assert result["total_crashes"] == 3
        assert result["unique_crashes"] == 2
        assert result["summary"]["ubsan"] == 1
        assert result["summary"]["debug_assert"] == 1

        assert (tmp_path / "triage.json").exists()
        assert (tmp_path / "dedup").exists()
        assert (tmp_path / "triage_report.md").exists()
        assert len(list((tmp_path / "dedup").iterdir())) == 2

        data = json.loads((tmp_path / "triage.json").read_text())
        ubsan_crash = next(c for c in data["crashes"] if c["type"] == "ubsan")
        assert ubsan_crash["count"] == 2
        assert ubsan_crash["subtype"] == "integer-overflow"

    def test_enrich_campaign_json_via_triage(self, tmp_path: Path, monkeypatch) -> None:
        signaled = tmp_path / "outputs" / "signaled"
        signaled.mkdir(parents=True)
        (signaled / "sig_001").write_text("SELECT 1;")

        def mock_run_crash(harness: str, crash_file: str, timeout: int = 5) -> tuple[int, str]:
            return 223, "==1==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x...\n    #0 0xdead in func_a file.c:1\n"

        import triage.classify
        monkeypatch.setattr(triage.classify, "run_crash", mock_run_crash)

        campaign_json = tmp_path / "campaign.json"
        campaign_json.write_text(json.dumps({"id": "test", "results": {"crashes": 1}}))

        from triage.classify import triage as run_triage
        run_triage(
            workdir=str(tmp_path),
            harness="/fake/harness",
            output=str(tmp_path / "triage.json"),
            dedup_dir=str(tmp_path / "dedup"),
            report=str(tmp_path / "triage_report.md"),
            enrich=str(campaign_json),
        )

        data = json.loads(campaign_json.read_text())
        assert data["results"]["crash_classification"]["asan"] == 1
        assert data["results"]["crash_classification"]["unique_crash_sites"] == 1
```

- [ ] **Step 2: Run all tests**

Run: `python3 -m pytest tests/triage/test_classify.py -v`
Expected: All tests PASS (25 unit + 2 integration = 27 total)

- [ ] **Step 3: Commit**

```bash
git add tests/triage/test_classify.py
git commit -m "test(triage): add end-to-end integration tests for classify.py"
```
