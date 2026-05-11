# Crash Evidence Archive Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `scripts/collect_crashes.py` that consolidates all unique crash findings from 40+ campaign workdirs into `results/crashes/` — a self-contained, replayable evidence archive with per-crash metadata, trigger SQL, stderr logs, and reproduction scripts.

**Architecture:** Single Python script with 4 phases: scan triage JSONs → dedup by hash → group into root cause classes → emit archive (copy SQL, replay for stderr, generate metadata). Uses existing `triage/classify.py` types for crash classification. No external dependencies.

**Tech Stack:** Python 3.13 stdlib (json, subprocess, pathlib, argparse, dataclasses, shutil)

**Key data facts:**
- 40 workdirs have `dedup_test/` dirs with 222 total crash files (SQL content)
- Files named `<16-char-hash>_<sample_file>` — content is raw SQL
- `triage_test.json` has: hash, type, subtype, exit_code, count, sample_file, top_frames, sql_preview
- 4 test harness binaries available at `harness/test/sqlite_harness_sqlite-<ver>_test`
- Version extracted from workdir name: `sqlite-<ver>_<rest>`

---

### Task 1: Scanner — read triage JSONs and dedup by hash

**Files:**
- Create: `scripts/collect_crashes.py`
- Test: `tests/test_collect_crashes.py`

- [ ] **Step 1: Write failing test for `scan_workdirs`**

```python
# tests/test_collect_crashes.py
import json
import pytest
from pathlib import Path

from scripts.collect_crashes import scan_workdirs, CrashEntry


def test_scan_deduplicates_by_hash(tmp_path):
    """Same hash in two campaigns → one CrashEntry with both campaigns listed."""
    for name in ["sqlite-3.30.1_run1", "sqlite-3.30.1_run2"]:
        wd = tmp_path / name
        wd.mkdir()
        triage = {
            "total_crashes": 10,
            "unique_crashes": 1,
            "summary": {"ubsan": 1},
            "crashes": [{
                "hash": "aabbccdd11223344",
                "type": "ubsan",
                "subtype": "signed-integer-overflow",
                "exit_code": 1,
                "count": 5,
                "sample_file": "5_000000001",
                "top_frames": [
                    "sqlite3.c:1234: runtime error: signed integer overflow: 2147483647 + 1",
                    "sqlite3_str_vappendf",
                    "printfFunc",
                ],
                "sql_preview": "SELECT printf('%.*f', 2147483647, 1e308);",
            }],
        }
        (wd / "triage_test.json").write_text(json.dumps(triage))
        dedup = wd / "dedup_test"
        dedup.mkdir()
        (dedup / "aabbccdd11223344_5_000000001").write_text(
            "SELECT printf('%.*f', 2147483647, 1e308);"
        )

    entries = scan_workdirs(tmp_path)

    assert len(entries) == 1
    e = entries["aabbccdd11223344"]
    assert e.hash == "aabbccdd11223344"
    assert e.crash_type == "ubsan"
    assert e.subtype == "signed-integer-overflow"
    assert e.version == "3.30.1"
    assert len(e.campaigns) == 2
    assert e.sql_file is not None


def test_scan_skips_non_ubsan(tmp_path):
    """debug_assert crashes are skipped — only ubsan and signal kept."""
    wd = tmp_path / "sqlite-3.31.1_run1"
    wd.mkdir()
    triage = {
        "total_crashes": 5,
        "unique_crashes": 2,
        "summary": {"debug_assert": 1, "ubsan": 1},
        "crashes": [
            {
                "hash": "1111111111111111",
                "type": "debug_assert",
                "subtype": None,
                "exit_code": -5,
                "count": 3,
                "sample_file": "5_000000001",
                "top_frames": ["some_func"],
                "sql_preview": "SELECT 1;",
            },
            {
                "hash": "2222222222222222",
                "type": "ubsan",
                "subtype": "null-pointer",
                "exit_code": 1,
                "count": 2,
                "sample_file": "5_000000002",
                "top_frames": [
                    "sqlite3.c:999: runtime error: null pointer",
                    "sqlite3Fts5GetTokenizer",
                ],
                "sql_preview": "CREATE VIRTUAL TABLE ...",
            },
        ],
    }
    (wd / "triage_test.json").write_text(json.dumps(triage))
    dedup = wd / "dedup_test"
    dedup.mkdir()
    (dedup / "2222222222222222_5_000000002").write_text("CREATE VIRTUAL TABLE ...;")

    entries = scan_workdirs(tmp_path)
    assert "1111111111111111" not in entries
    assert "2222222222222222" in entries


def test_scan_finds_sql_file_in_dedup_test(tmp_path):
    """SQL content loaded from dedup_test/<hash>_<sample> file."""
    wd = tmp_path / "sqlite-3.32.0_run1"
    wd.mkdir()
    triage = {
        "total_crashes": 1, "unique_crashes": 1,
        "summary": {"ubsan": 1},
        "crashes": [{
            "hash": "aaaa000011112222",
            "type": "ubsan", "subtype": "float-cast-overflow",
            "exit_code": 1, "count": 1,
            "sample_file": "1_000000099",
            "top_frames": ["sqlite3.c:5: runtime error: inf overflow", "alsoAnInt"],
            "sql_preview": "INSERT ...",
        }],
    }
    (wd / "triage_test.json").write_text(json.dumps(triage))
    dedup = wd / "dedup_test"
    dedup.mkdir()
    sql = "INSERT INTO p VALUES (TRUE || TRUE || TRUE);"
    (dedup / "aaaa000011112222_1_000000099").write_text(sql)

    entries = scan_workdirs(tmp_path)
    assert entries["aaaa000011112222"].sql_content == sql
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python3.13 -m pytest tests/test_collect_crashes.py -v
```

Expected: `ModuleNotFoundError: No module named 'scripts.collect_crashes'`

- [ ] **Step 3: Implement `scan_workdirs` and `CrashEntry`**

```python
#!/usr/bin/env python3
"""
collect_crashes.py — Consolidate unique crashes from all campaign workdirs
into a self-contained evidence archive at results/crashes/.

Usage:
    python3 scripts/collect_crashes.py                    # full run
    python3 scripts/collect_crashes.py --scan-only        # no replay
    python3 scripts/collect_crashes.py --incremental      # skip existing
"""
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


def _extract_version(campaign_name: str) -> str:
    """Extract SQLite version from workdir name like 'sqlite-3.31.1_bandit_run1'."""
    m = re.match(r"sqlite-(\d+\.\d+\.\d+)", campaign_name)
    return m.group(1) if m else "unknown"


def _extract_error_message(frames: list[str]) -> str:
    """Extract 'runtime error: ...' message from top_frames."""
    for f in frames:
        if "runtime error:" in f:
            m = re.search(r"runtime error:\s*(.+)", f)
            if m:
                return m.group(1).strip()
    return ""


def _find_sql_file(dedup_dir: Path, crash_hash: str) -> tuple[Path | None, str | None]:
    """Find the dedup_test file matching this hash and read its SQL content."""
    if not dedup_dir.exists():
        return None, None
    for f in dedup_dir.iterdir():
        if f.name.startswith(crash_hash):
            return f, f.read_text(errors="replace")
    return None, None


def scan_workdirs(workdirs_path: Path) -> dict[str, CrashEntry]:
    """Scan all workdirs for triage_test.json, dedup by hash, return unique entries."""
    entries: dict[str, CrashEntry] = {}

    for wd in sorted(workdirs_path.iterdir()):
        if not wd.is_dir():
            continue
        triage_file = wd / "triage_test.json"
        if not triage_file.exists():
            continue

        campaign_name = wd.name
        version = _extract_version(campaign_name)

        with open(triage_file) as f:
            data = json.load(f)

        dedup_dir = wd / "dedup_test"

        for crash in data.get("crashes", []):
            ctype = crash.get("type", "")
            if ctype not in ("ubsan", "signal", "asan"):
                continue

            h = crash["hash"]

            if h not in entries:
                sql_file, sql_content = _find_sql_file(dedup_dir, h)
                entries[h] = CrashEntry(
                    hash=h,
                    crash_type=ctype,
                    subtype=crash.get("subtype"),
                    exit_code=crash.get("exit_code", 0),
                    version=version,
                    top_frames=crash.get("top_frames", []),
                    error_message=_extract_error_message(crash.get("top_frames", [])),
                    sql_preview=crash.get("sql_preview", ""),
                    sql_content=sql_content,
                    sql_file=sql_file,
                    sample_file=crash.get("sample_file", ""),
                    campaigns=[campaign_name],
                    total_count=crash.get("count", 1),
                )
            else:
                entries[h].campaigns.append(campaign_name)
                entries[h].total_count += crash.get("count", 1)
                if entries[h].sql_file is None:
                    sql_file, sql_content = _find_sql_file(dedup_dir, h)
                    entries[h].sql_file = sql_file
                    entries[h].sql_content = sql_content

    return entries
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py -v
```

Expected: 3 tests PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/collect_crashes.py tests/test_collect_crashes.py
git commit -m "feat: add crash scanner with dedup — phase 1 of evidence archive"
```

---

### Task 2: Root cause grouper — classify hashes into bug classes

**Files:**
- Modify: `scripts/collect_crashes.py`
- Modify: `tests/test_collect_crashes.py`

- [ ] **Step 1: Write failing test for `group_into_classes`**

```python
# append to tests/test_collect_crashes.py
from scripts.collect_crashes import group_into_classes, BugClass


def test_group_same_subtype_and_function():
    """Two crashes with same subtype + key function → one class."""
    entries = {
        "hash1": CrashEntry(
            hash="hash1", crash_type="ubsan", subtype="signed-integer-overflow",
            exit_code=1, version="3.30.1",
            top_frames=["sqlite3.c:1: runtime error: 2147483647 + 1 overflow", "sqlite3_str_vappendf", "printfFunc"],
            error_message="2147483647 + 1 overflow",
            sql_preview="SELECT printf(...);", sql_content="SELECT printf(...);",
            sql_file=None, sample_file="5_1", campaigns=["run1"], total_count=100,
        ),
        "hash2": CrashEntry(
            hash="hash2", crash_type="ubsan", subtype="signed-integer-overflow",
            exit_code=1, version="3.31.1",
            top_frames=["sqlite3.c:2: runtime error: 2147483646 - -2 overflow", "sqlite3_str_vappendf", "printfFunc"],
            error_message="2147483646 - -2 overflow",
            sql_preview="SELECT printf(...);", sql_content="SELECT printf(...);",
            sql_file=None, sample_file="5_2", campaigns=["run2"], total_count=50,
        ),
    }

    classes = group_into_classes(entries)
    assert len(classes) == 1
    cls = list(classes.values())[0]
    assert cls.subtype == "signed-integer-overflow"
    assert cls.key_function == "sqlite3_str_vappendf"
    assert set(cls.hashes) == {"hash1", "hash2"}
    assert "3.30.1" in cls.versions
    assert "3.31.1" in cls.versions


def test_group_different_function_splits():
    """Same subtype but different key function → two classes."""
    entries = {
        "hash_a": CrashEntry(
            hash="hash_a", crash_type="ubsan", subtype="null-pointer",
            exit_code=1, version="3.30.1",
            top_frames=["sqlite3.c:1: runtime error: null pointer", "sqlite3Fts5GetTokenizer"],
            error_message="null pointer", sql_preview="...", sql_content="...",
            sql_file=None, sample_file="5_1", campaigns=["r1"], total_count=10,
        ),
        "hash_b": CrashEntry(
            hash="hash_b", crash_type="ubsan", subtype="null-pointer",
            exit_code=1, version="3.30.1",
            top_frames=["sqlite3.c:2: runtime error: null pointer", "sqlite3AtoF"],
            error_message="null pointer", sql_preview="...", sql_content="...",
            sql_file=None, sample_file="5_2", campaigns=["r2"], total_count=5,
        ),
    }

    classes = group_into_classes(entries)
    assert len(classes) == 2
```

- [ ] **Step 2: Run tests — expect fail**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py::test_group_same_subtype_and_function -v
```

- [ ] **Step 3: Implement `group_into_classes` and `BugClass`**

Add to `scripts/collect_crashes.py`:

```python
@dataclass
class BugClass:
    class_id: str
    name: str
    subtype: str
    key_function: str
    error_message: str
    severity: str
    cve: str | None
    hashes: list[str] = field(default_factory=list)
    versions: set[str] = field(default_factory=set)
    total_crashes: int = 0
    top_frames_sample: list[str] = field(default_factory=list)


def _extract_key_function(frames: list[str]) -> str:
    """First frame that is NOT a 'runtime error:' line."""
    for f in frames:
        if "runtime error:" not in f:
            return f.strip()
    return "unknown"


# Known severity overrides based on analysis
_SEVERITY_MAP = {
    ("misaligned-access", "sqlite3WindowUnlinkFromSelect"): "HIGH",
    ("null-pointer", "sqlite3Select"): "HIGH",
}

_CVE_MAP = {
    ("signed-integer-overflow", "sqlite3_str_vappendf"): "CVE-2020-13434",
    ("misaligned-access", "sqlite3WindowUnlinkFromSelect"): "CVE-2020-13871",
    ("null-pointer", "sqlite3Select"): "CVE-2020-9327",
}

_DEFAULT_SEVERITY = {
    "null-pointer": "LOW-MED",
    "signed-integer-overflow": "MEDIUM",
    "float-cast-overflow": "MEDIUM",
    "misaligned-access": "HIGH",
}


def _make_class_name(subtype: str, key_func: str) -> str:
    """Generate human-readable class name from subtype + function."""
    subtype_label = subtype.replace("-", " ").title()
    func_clean = key_func.replace("sqlite3", "").replace("_", " ").strip()
    return f"{subtype_label} in {func_clean}"


def group_into_classes(
    entries: dict[str, CrashEntry],
    overrides_path: Path | None = None,
) -> dict[str, BugClass]:
    """Group crash entries into root cause classes by subtype + key function."""
    raw_groups: dict[tuple[str, str], list[CrashEntry]] = {}

    for entry in entries.values():
        key_func = _extract_key_function(entry.top_frames)
        subtype = entry.subtype or entry.crash_type
        group_key = (subtype, key_func)

        if group_key not in raw_groups:
            raw_groups[group_key] = []
        raw_groups[group_key].append(entry)

    classes: dict[str, BugClass] = {}
    for idx, ((subtype, key_func), group) in enumerate(
        sorted(raw_groups.items(), key=lambda x: -sum(e.total_count for e in x[1])),
        start=1,
    ):
        class_id = f"U{idx:02d}"
        severity = _SEVERITY_MAP.get((subtype, key_func), _DEFAULT_SEVERITY.get(subtype, "LOW"))
        cve = _CVE_MAP.get((subtype, key_func))

        bc = BugClass(
            class_id=class_id,
            name=_make_class_name(subtype, key_func),
            subtype=subtype,
            key_function=key_func,
            error_message=group[0].error_message,
            severity=severity,
            cve=cve,
            top_frames_sample=group[0].top_frames[:5],
        )

        for entry in group:
            bc.hashes.append(entry.hash)
            bc.versions.add(entry.version)
            bc.total_crashes += entry.total_count

        classes[class_id] = bc

    if overrides_path and overrides_path.exists():
        overrides = json.loads(overrides_path.read_text())
        for h, target_class in overrides.items():
            for bc in classes.values():
                if h in bc.hashes:
                    bc.hashes.remove(h)
            if target_class in classes:
                classes[target_class].hashes.append(h)

    return classes
```

- [ ] **Step 4: Run tests — expect pass**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py -v
```

- [ ] **Step 5: Commit**

```bash
git add scripts/collect_crashes.py tests/test_collect_crashes.py
git commit -m "feat: add root cause grouper for crash evidence classes"
```

---

### Task 3: Archive emitter — create per-crash directories

**Files:**
- Modify: `scripts/collect_crashes.py`
- Modify: `tests/test_collect_crashes.py`

- [ ] **Step 1: Write failing test for `emit_archive`**

```python
# append to tests/test_collect_crashes.py
from scripts.collect_crashes import emit_archive


def test_emit_creates_directory_structure(tmp_path):
    """emit_archive creates class dirs, hash subdirs, and all files."""
    entries = {
        "aabb001122334455": CrashEntry(
            hash="aabb001122334455", crash_type="ubsan", subtype="null-pointer",
            exit_code=1, version="3.30.1",
            top_frames=[
                "sqlite3.c:100: runtime error: applying non-zero offset 8 to null pointer",
                "sqlite3Fts5GetTokenizer",
                "fts5ConfigDefaultTokenizer",
            ],
            error_message="applying non-zero offset 8 to null pointer",
            sql_preview="CREATE VIRTUAL TABLE ...",
            sql_content="CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(a);",
            sql_file=None, sample_file="5_000000068",
            campaigns=["sqlite-3.30.1_run1", "sqlite-3.30.1_run2"],
            total_count=200,
        ),
    }

    classes = group_into_classes(entries)
    output_dir = tmp_path / "crashes"

    emit_archive(entries, classes, output_dir, replay=False)

    # Check directory structure
    class_dirs = list(output_dir.iterdir())
    # Filter out registry files
    class_dirs = [d for d in class_dirs if d.is_dir()]
    assert len(class_dirs) == 1

    class_dir = class_dirs[0]
    assert class_dir.name.startswith("U01_")

    # Check hash subdir
    hash_dir = class_dir / "aabb001122334455"
    assert hash_dir.exists()
    assert (hash_dir / "trigger.sql").exists()
    assert (hash_dir / "metadata.json").exists()
    assert (hash_dir / "reproduce.sh").exists()
    assert (hash_dir / "stack_trace.txt").exists()

    # Check trigger.sql content
    sql = (hash_dir / "trigger.sql").read_text()
    assert "CREATE VIRTUAL TABLE" in sql

    # Check metadata.json
    meta = json.loads((hash_dir / "metadata.json").read_text())
    assert meta["hash"] == "aabb001122334455"
    assert meta["class_id"] == "U01"
    assert meta["type"] == "ubsan"
    assert meta["sqlite_version"] == "3.30.1"
    assert len(meta["all_campaigns"]) == 2

    # Check reproduce.sh is executable
    repro = hash_dir / "reproduce.sh"
    assert os.access(repro, os.X_OK) or "#!/bin/bash" in repro.read_text()

    # Check registry files
    assert (output_dir / "registry.json").exists()
    assert (output_dir / "registry.md").exists()

    # Check class README
    assert (class_dir / "README.md").exists()
```

- [ ] **Step 2: Run test — expect fail**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py::test_emit_creates_directory_structure -v
```

- [ ] **Step 3: Implement `emit_archive`**

Add to `scripts/collect_crashes.py`:

```python
def _sanitize_dirname(name: str) -> str:
    """Convert class name to filesystem-safe directory name."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:60]


def _emit_crash_dir(
    entry: CrashEntry,
    bug_class: BugClass,
    hash_dir: Path,
    harness_dir: Path,
    replay: bool,
) -> None:
    """Create all files for a single crash hash directory."""
    hash_dir.mkdir(parents=True, exist_ok=True)

    # trigger.sql
    sql = entry.sql_content or entry.sql_preview
    (hash_dir / "trigger.sql").write_text(sql)

    # stack_trace.txt
    clean_frames = [f for f in entry.top_frames if "runtime error:" not in f]
    (hash_dir / "stack_trace.txt").write_text("\n".join(entry.top_frames))

    # metadata.json
    meta = {
        "hash": entry.hash,
        "class_id": bug_class.class_id,
        "class_name": bug_class.name,
        "type": entry.crash_type,
        "subtype": entry.subtype,
        "error_message": entry.error_message,
        "exit_code": entry.exit_code,
        "severity": bug_class.severity,
        "cve": bug_class.cve,
        "sqlite_version": entry.version,
        "source_campaign": entry.campaigns[0] if entry.campaigns else None,
        "source_file": entry.sample_file,
        "first_seen_campaign": entry.campaigns[0] if entry.campaigns else None,
        "all_campaigns": sorted(entry.campaigns),
        "top_frames": entry.top_frames,
    }
    (hash_dir / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")

    # reproduce.sh
    harness_path = harness_dir / f"sqlite_harness_sqlite-{entry.version}_test"
    rel_harness = os.path.relpath(harness_path, hash_dir)
    script = f"""#!/bin/bash
# Reproduce crash {bug_class.class_id}/{entry.hash}
# Type: {entry.crash_type} ({entry.subtype})
# Version: SQLite {entry.version}
HARNESS="{rel_harness}"
if [ ! -x "$HARNESS" ]; then
    echo "ERROR: harness not found at $HARNESS"
    exit 1
fi
echo "Replaying trigger.sql through test harness..."
"$HARNESS" trigger.sql 2>stderr_replay.log
EXIT=$?
echo "Exit code: $EXIT"
[ -s stderr_replay.log ] && echo "Stderr saved to stderr_replay.log"
"""
    repro_path = hash_dir / "reproduce.sh"
    repro_path.write_text(script)
    repro_path.chmod(repro_path.stat().st_mode | stat.S_IEXEC)

    # stderr.log — replay if requested and harness exists
    if replay and harness_path.exists():
        trigger = hash_dir / "trigger.sql"
        try:
            result = subprocess.run(
                [str(harness_path), str(trigger)],
                capture_output=True, text=True, timeout=10,
            )
            (hash_dir / "stderr.log").write_text(result.stderr)
        except (subprocess.TimeoutExpired, OSError) as e:
            (hash_dir / "stderr.log").write_text(f"Replay failed: {e}\n")


def _emit_class_readme(bug_class: BugClass, class_dir: Path) -> None:
    """Write README.md for a root cause class."""
    versions_str = ", ".join(sorted(bug_class.versions))
    cve_str = bug_class.cve or "None identified"

    lines = [
        f"# {bug_class.class_id}: {bug_class.name}\n",
        f"**Severity:** {bug_class.severity}  ",
        f"**UBSan subtype:** `{bug_class.subtype}`  ",
        f"**CVE:** {cve_str}  ",
        f"**Versions affected:** {versions_str}  ",
        f"**Unique crash hashes:** {len(bug_class.hashes)}  ",
        f"**Total crashes across campaigns:** {bug_class.total_crashes}  \n",
        "## Error\n",
        f"```\n{bug_class.error_message}\n```\n",
        "## Stack Trace (representative)\n",
        "```",
    ]
    lines.extend(bug_class.top_frames_sample)
    lines.append("```\n")
    lines.append("## Crash Hashes\n")
    lines.append("| Hash | Campaigns |")
    lines.append("|------|-----------|")

    (class_dir / "README.md").write_text("\n".join(lines) + "\n")


def _emit_registry_json(
    classes: dict[str, BugClass],
    entries: dict[str, CrashEntry],
    output_dir: Path,
    campaigns_scanned: int,
) -> None:
    """Write registry.json master index."""
    versions = set()
    for e in entries.values():
        versions.add(e.version)

    registry = {
        "metadata": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "total_classes": len(classes),
            "total_unique_hashes": len(entries),
            "campaigns_scanned": campaigns_scanned,
            "sqlite_versions": sorted(versions),
        },
        "classes": [],
    }

    for bc in classes.values():
        registry["classes"].append({
            "id": bc.class_id,
            "name": bc.name,
            "severity": bc.severity,
            "subtype": bc.subtype,
            "key_function": bc.key_function,
            "cve": bc.cve,
            "versions": sorted(bc.versions),
            "hashes": sorted(bc.hashes),
            "total_crashes_across_campaigns": bc.total_crashes,
            "error_message": bc.error_message,
        })

    (output_dir / "registry.json").write_text(json.dumps(registry, indent=2) + "\n")


def _emit_registry_md(classes: dict[str, BugClass], output_dir: Path, entries: dict[str, CrashEntry]) -> None:
    """Write registry.md human-readable summary."""
    lines = [
        "# Crash Evidence Registry\n",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Total bug classes:** {len(classes)}  ",
        f"**Total unique hashes:** {len(entries)}  \n",
        "| ID | Name | Severity | CVE | Versions | Hashes | Total Crashes |",
        "|:---|:-----|:---------|:----|:---------|-------:|--------------:|",
    ]

    for bc in classes.values():
        cve = bc.cve or "—"
        versions = ", ".join(sorted(bc.versions))
        dir_name = f"{bc.class_id}_{_sanitize_dirname(bc.name)}"
        lines.append(
            f"| [{bc.class_id}]({dir_name}/README.md) "
            f"| {bc.name} "
            f"| {bc.severity} "
            f"| {cve} "
            f"| {versions} "
            f"| {len(bc.hashes)} "
            f"| {bc.total_crashes:,} |"
        )

    (output_dir / "registry.md").write_text("\n".join(lines) + "\n")


def emit_archive(
    entries: dict[str, CrashEntry],
    classes: dict[str, BugClass],
    output_dir: Path,
    replay: bool = False,
    incremental: bool = False,
) -> None:
    """Emit the full archive directory structure."""
    harness_dir = ROOT / "harness" / "test"
    output_dir.mkdir(parents=True, exist_ok=True)

    hash_to_class = {}
    for bc in classes.values():
        for h in bc.hashes:
            hash_to_class[h] = bc

    for entry in entries.values():
        bc = hash_to_class.get(entry.hash)
        if bc is None:
            continue

        dir_name = f"{bc.class_id}_{_sanitize_dirname(bc.name)}"
        class_dir = output_dir / dir_name
        hash_dir = class_dir / entry.hash

        if incremental and hash_dir.exists():
            continue

        _emit_crash_dir(entry, bc, hash_dir, harness_dir, replay)

    for bc in classes.values():
        dir_name = f"{bc.class_id}_{_sanitize_dirname(bc.name)}"
        class_dir = output_dir / dir_name
        class_dir.mkdir(parents=True, exist_ok=True)
        _emit_class_readme(bc, class_dir)

    campaigns_scanned = len({c for e in entries.values() for c in e.campaigns})
    _emit_registry_json(classes, entries, output_dir, campaigns_scanned)
    _emit_registry_md(classes, output_dir, entries)
```

- [ ] **Step 4: Run all tests**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py -v
```

Expected: all 6 tests PASS

- [ ] **Step 5: Commit**

```bash
git add scripts/collect_crashes.py tests/test_collect_crashes.py
git commit -m "feat: add archive emitter — creates per-crash evidence directories"
```

---

### Task 4: CLI entry point and `main()`

**Files:**
- Modify: `scripts/collect_crashes.py`

- [ ] **Step 1: Add `main()` with argparse**

Add to end of `scripts/collect_crashes.py`:

```python
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Consolidate unique crashes into evidence archive"
    )
    parser.add_argument(
        "--workdirs", type=Path, default=ROOT / "workdirs",
        help="Path to workdirs/ directory (default: workdirs/)",
    )
    parser.add_argument(
        "--output", type=Path, default=ROOT / "results" / "crashes",
        help="Output directory (default: results/crashes/)",
    )
    parser.add_argument(
        "--scan-only", action="store_true",
        help="Scan and emit without replaying through harness",
    )
    parser.add_argument(
        "--incremental", action="store_true",
        help="Skip hashes already present in output directory",
    )
    parser.add_argument(
        "--overrides", type=Path, default=None,
        help="Path to class_overrides.json for manual grouping fixes",
    )
    args = parser.parse_args()

    print(f"[collect] Scanning {args.workdirs}/ ...")
    entries = scan_workdirs(args.workdirs)
    print(f"[collect] Found {len(entries)} unique crash hashes")

    if not entries:
        print("[collect] No crashes found. Done.")
        return

    print("[collect] Grouping into root cause classes...")
    classes = group_into_classes(entries, args.overrides)
    print(f"[collect] {len(classes)} bug classes identified")

    for bc in classes.values():
        print(f"  {bc.class_id}: {bc.name} ({len(bc.hashes)} hashes, {bc.total_crashes:,} crashes)")

    replay = not args.scan_only
    print(f"\n[collect] Emitting archive to {args.output}/ (replay={'ON' if replay else 'OFF'})...")
    emit_archive(entries, classes, args.output, replay=replay, incremental=args.incremental)

    print(f"\n[collect] Done. Archive at {args.output}/")
    print(f"  registry.json: {args.output / 'registry.json'}")
    print(f"  registry.md:   {args.output / 'registry.md'}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Test CLI help works**

```bash
python3.13 scripts/collect_crashes.py --help
```

Expected: prints usage with `--scan-only`, `--incremental`, `--overrides` flags

- [ ] **Step 3: Commit**

```bash
git add scripts/collect_crashes.py
git commit -m "feat: add CLI entry point for collect_crashes.py"
```

---

### Task 5: Run full collection and verify output

**Files:**
- No new files — this is execution and verification

- [ ] **Step 1: Run scan-only first (fast, no replay)**

```bash
python3.13 scripts/collect_crashes.py --scan-only
```

Expected output: lists ~9 bug classes, creates `results/crashes/` with directories.

- [ ] **Step 2: Verify directory structure**

```bash
find results/crashes/ -maxdepth 2 -type d | sort
```

Expected: `U01_*/`, `U02_*/`, ... with hash subdirs inside each.

- [ ] **Step 3: Spot-check one crash package**

```bash
ls results/crashes/U01_*/$(ls results/crashes/U01_*/ | head -1)/
cat results/crashes/U01_*/$(ls results/crashes/U01_*/ | head -1)/metadata.json | python3 -m json.tool | head -20
cat results/crashes/U01_*/$(ls results/crashes/U01_*/ | head -1)/trigger.sql
```

Expected: trigger.sql has valid SQL, metadata.json has correct fields.

- [ ] **Step 4: Run with replay (captures stderr — takes ~2 min)**

```bash
python3.13 scripts/collect_crashes.py --incremental
```

Expected: replays each crash through test/ harness, writes stderr.log files.

- [ ] **Step 5: Verify stderr.log captured**

```bash
# Pick a crash and check stderr
find results/crashes/ -name 'stderr.log' | head -3
head -5 $(find results/crashes/ -name 'stderr.log' | head -1)
```

Expected: stderr.log contains `runtime error:` or signal info.

- [ ] **Step 6: Remove old bug_registry files**

```bash
rm -f results/bug_registry.md results/bug_registry.json
```

- [ ] **Step 7: Commit the archive**

```bash
git add results/crashes/
git rm -f results/bug_registry.md results/bug_registry.json 2>/dev/null || true
git commit -m "feat: consolidated crash evidence archive (9 classes, 64 hashes)

Replaces scattered per-campaign triage data with self-contained
evidence packages. Each crash has trigger.sql, stderr.log,
stack_trace.txt, metadata.json, and reproduce.sh."
```

---

### Task 6: Integration test — end-to-end on real data

**Files:**
- Modify: `tests/test_collect_crashes.py`

- [ ] **Step 1: Add integration test that runs on real workdirs**

```python
# append to tests/test_collect_crashes.py
import subprocess

@pytest.mark.skipif(
    not Path("workdirs").exists(),
    reason="workdirs/ not present — skip integration test",
)
def test_integration_real_workdirs():
    """End-to-end: scan real workdirs, emit to temp dir, verify output."""
    result = subprocess.run(
        ["python3.13", "scripts/collect_crashes.py",
         "--scan-only", "--output", "/tmp/test_crash_archive"],
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, f"Script failed: {result.stderr}"
    assert "bug classes identified" in result.stdout

    output = Path("/tmp/test_crash_archive")
    assert (output / "registry.json").exists()
    assert (output / "registry.md").exists()

    import json
    reg = json.loads((output / "registry.json").read_text())
    assert reg["metadata"]["total_classes"] > 0
    assert reg["metadata"]["total_unique_hashes"] > 0

    # Cleanup
    shutil.rmtree(output, ignore_errors=True)
```

- [ ] **Step 2: Run integration test**

```bash
PYTHONPATH=. python3.13 -m pytest tests/test_collect_crashes.py::test_integration_real_workdirs -v
```

Expected: PASS — confirms script works on actual campaign data.

- [ ] **Step 3: Commit**

```bash
git add tests/test_collect_crashes.py
git commit -m "test: add integration test for collect_crashes on real workdirs"
```

---

### Task 7: Update docs

**Files:**
- Modify: `CLAUDE.md` (add reference to crash evidence archive)

- [ ] **Step 1: Add crash archive reference to CLAUDE.md**

Find the `## Evaluation Commands` section in CLAUDE.md and add after it:

```markdown
## Crash Evidence Archive

Consolidated bug findings live in `results/crashes/`. Each unique crash has:
- `trigger.sql` — the SQL that crashes SQLite
- `stderr.log` — ASan/UBSan output from test/ harness
- `metadata.json` — structured crash info (hash, type, version, CVE, severity)
- `reproduce.sh` — one-liner to replay

```bash
# Rebuild archive from workdirs
python3 scripts/collect_crashes.py --scan-only    # fast, no replay
python3 scripts/collect_crashes.py                # full with stderr capture
python3 scripts/collect_crashes.py --incremental  # add new campaigns only
```
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add crash evidence archive reference to CLAUDE.md"
```
