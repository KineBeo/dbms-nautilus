from __future__ import annotations

import json
import stat
import tempfile
from pathlib import Path

import pytest

from scripts.collect_crashes import (
    BugClass,
    CrashEntry,
    _extract_error_message,
    _extract_key_function,
    _extract_version,
    _find_sql_file,
    _make_class_name,
    _sanitize_dirname,
    emit_archive,
    group_into_classes,
    scan_workdirs,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_triage(crashes: list[dict]) -> dict:
    return {
        "total_crashes": sum(c.get("count", 1) for c in crashes),
        "unique_crashes": len(crashes),
        "summary": {},
        "crashes": crashes,
    }


def _make_crash(
    hash_: str,
    crash_type: str = "ubsan",
    subtype: str = "signed-integer-overflow",
    exit_code: int = -6,
    count: int = 5,
    sample_file: str = "1_000001234",
    top_frames: list[str] | None = None,
    sql_preview: str = "SELECT 1;",
) -> dict:
    if top_frames is None:
        top_frames = [
            "sqlite3.c:27975:35: runtime error: signed integer overflow",
            "sqlite3_str_vappendf",
            "printfFunc",
        ]
    return {
        "hash": hash_,
        "type": crash_type,
        "subtype": subtype,
        "exit_code": exit_code,
        "count": count,
        "sample_file": sample_file,
        "top_frames": top_frames,
        "sql_preview": sql_preview,
    }


def _make_workdir(root: Path, name: str, crashes: list[dict], sql_map: dict[str, str]) -> Path:
    """Create a fake workdir with triage_test.json and dedup_test/ files."""
    wd = root / name
    wd.mkdir(parents=True)
    triage = _make_triage(crashes)
    (wd / "triage_test.json").write_text(json.dumps(triage))
    dedup = wd / "dedup_test"
    dedup.mkdir()
    for crash in crashes:
        h = crash["hash"]
        sf = crash["sample_file"]
        sql = sql_map.get(h, f"SELECT /* {h} */;")
        (dedup / f"{h}_{sf}").write_text(sql)
    return wd


# ---------------------------------------------------------------------------
# Task 1 — Scanner tests
# ---------------------------------------------------------------------------

class TestScanDeduplicatesByHash:
    def test_same_hash_in_two_campaigns_yields_one_entry(self, tmp_path):
        crash = _make_crash("aabbccdd11223344")
        sql = "SELECT 42;"
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run1", [crash], {"aabbccdd11223344": sql})
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run2", [crash], {"aabbccdd11223344": sql})

        entries = scan_workdirs(tmp_path)

        assert len(entries) == 1
        entry = entries["aabbccdd11223344"]
        assert sorted(entry.campaigns) == ["sqlite-3.31.1_bandit_run1", "sqlite-3.31.1_bandit_run2"]
        assert entry.total_count == 10  # 5 + 5

    def test_different_hashes_yield_separate_entries(self, tmp_path):
        c1 = _make_crash("aaaa000000000001")
        c2 = _make_crash("bbbb000000000002")
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run1", [c1, c2], {})

        entries = scan_workdirs(tmp_path)
        assert len(entries) == 2


class TestScanSkipsNonUbsan:
    def test_debug_assert_is_skipped(self, tmp_path):
        good = _make_crash("good000000000001", crash_type="ubsan")
        bad = _make_crash("bad0000000000001", crash_type="debug_assert")
        _make_workdir(tmp_path, "sqlite-3.31.1_uniform_run1", [good, bad], {})

        entries = scan_workdirs(tmp_path)
        assert "good000000000001" in entries
        assert "bad0000000000001" not in entries

    def test_timeout_is_skipped(self, tmp_path):
        good = _make_crash("good000000000002", crash_type="signal")
        bad = _make_crash("bad0000000000002", crash_type="timeout")
        _make_workdir(tmp_path, "sqlite-3.30.1_bandit_run1", [good, bad], {})

        entries = scan_workdirs(tmp_path)
        assert "good000000000002" in entries
        assert "bad0000000000002" not in entries

    def test_asan_is_kept(self, tmp_path):
        crash = _make_crash("asan000000000001", crash_type="asan")
        _make_workdir(tmp_path, "sqlite-3.32.0_bandit_run1", [crash], {})

        entries = scan_workdirs(tmp_path)
        assert "asan000000000001" in entries


class TestScanFindsSqlFile:
    def test_sql_content_loaded_from_dedup_test(self, tmp_path):
        sql = "SELECT printf('%.*g', -2147483649, 0.01);"
        crash = _make_crash("sql1000000000001", sample_file="5_000015161")
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run1", [crash], {"sql1000000000001": sql})

        entries = scan_workdirs(tmp_path)
        entry = entries["sql1000000000001"]
        assert entry.sql_content == sql

    def test_sql_content_is_none_when_file_missing(self, tmp_path):
        crash = _make_crash("nosql00000000001")
        wd = tmp_path / "sqlite-3.31.1_bandit_run1"
        wd.mkdir()
        (wd / "triage_test.json").write_text(json.dumps(_make_triage([crash])))
        (wd / "dedup_test").mkdir()
        # intentionally do NOT create any file in dedup_test

        entries = scan_workdirs(tmp_path)
        entry = entries["nosql00000000001"]
        assert entry.sql_content is None


class TestHelpers:
    def test_extract_version_standard(self):
        assert _extract_version("sqlite-3.31.1_bandit_run1") == "3.31.1"

    def test_extract_version_unknown(self):
        assert _extract_version("some_other_dir") == "unknown"

    def test_extract_error_message_picks_runtime_error_line(self):
        frames = [
            "sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646",
            "sqlite3_str_vappendf",
        ]
        msg = _extract_error_message(frames)
        assert "runtime error" in msg

    def test_extract_error_message_returns_empty_on_no_match(self):
        frames = ["sqlite3_str_vappendf", "printfFunc"]
        msg = _extract_error_message(frames)
        assert msg == ""

    def test_find_sql_file_returns_path_when_present(self, tmp_path):
        dedup = tmp_path / "dedup_test"
        dedup.mkdir()
        f = dedup / "abcd1234abcd1234_5_000001"
        f.write_text("SELECT 1;")
        result = _find_sql_file(dedup, "abcd1234abcd1234")
        assert result == f

    def test_find_sql_file_returns_none_when_absent(self, tmp_path):
        dedup = tmp_path / "dedup_test"
        dedup.mkdir()
        result = _find_sql_file(dedup, "nonexistent1234a")
        assert result is None


# ---------------------------------------------------------------------------
# Task 2 — Grouper tests
# ---------------------------------------------------------------------------

class TestGroupSameSubtypeAndFunction:
    def test_two_crashes_same_subtype_and_function_yield_one_class(self, tmp_path):
        frames = [
            "sqlite3.c:27975:35: runtime error: signed integer overflow",
            "sqlite3_str_vappendf",
            "printfFunc",
        ]
        c1 = _make_crash("aaaa000000000011", subtype="signed-integer-overflow", top_frames=frames)
        c2 = _make_crash("bbbb000000000022", subtype="signed-integer-overflow", top_frames=frames)
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run1", [c1, c2], {})

        entries = scan_workdirs(tmp_path)
        classes = group_into_classes(entries)

        assert len(classes) == 1
        cls = next(iter(classes.values()))
        assert len(cls.hashes) == 2
        assert "aaaa000000000011" in cls.hashes
        assert "bbbb000000000022" in cls.hashes


class TestGroupDifferentFunctionSplits:
    def test_same_subtype_different_function_yields_two_classes(self, tmp_path):
        frames1 = [
            "sqlite3.c:100: runtime error: signed integer overflow",
            "functionA",
            "callerA",
        ]
        frames2 = [
            "sqlite3.c:200: runtime error: signed integer overflow",
            "functionB",
            "callerB",
        ]
        c1 = _make_crash("cccc000000000033", subtype="signed-integer-overflow", top_frames=frames1)
        c2 = _make_crash("dddd000000000044", subtype="signed-integer-overflow", top_frames=frames2)
        _make_workdir(tmp_path, "sqlite-3.31.1_bandit_run1", [c1, c2], {})

        entries = scan_workdirs(tmp_path)
        classes = group_into_classes(entries)

        assert len(classes) == 2


# ---------------------------------------------------------------------------
# Task 3 — Emitter tests
# ---------------------------------------------------------------------------

class TestEmitCreatesDirectoryStructure:
    def test_emit_creates_expected_files(self, tmp_path):
        sql = "SELECT printf('%.*g', -2147483649, 0.01);"
        frames = [
            "sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646",
            "sqlite3_str_vappendf",
            "printfFunc",
        ]
        crash = _make_crash(
            "emit000000000001",
            subtype="signed-integer-overflow",
            top_frames=frames,
            sql_preview=sql,
        )
        workdirs_root = tmp_path / "workdirs"
        _make_workdir(workdirs_root, "sqlite-3.31.1_bandit_run1", [crash], {"emit000000000001": sql})

        entries = scan_workdirs(workdirs_root)
        classes = group_into_classes(entries)
        output_dir = tmp_path / "results" / "crashes"
        emit_archive(entries, classes, output_dir, replay=False)

        # Find the class directory (only 1 class)
        class_dirs = [d for d in output_dir.iterdir() if d.is_dir() and d.name != "by_hash"]
        assert len(class_dirs) == 1
        class_dir = class_dirs[0]

        # Find the hash subdir
        hash_dirs = [d for d in class_dir.iterdir() if d.is_dir()]
        assert len(hash_dirs) == 1
        hash_dir = hash_dirs[0]

        # Check required files exist
        assert (hash_dir / "trigger.sql").exists()
        assert (hash_dir / "metadata.json").exists()
        assert (hash_dir / "stack_trace.txt").exists()
        assert (hash_dir / "reproduce.sh").exists()

        # Check trigger.sql has SQL
        sql_content = (hash_dir / "trigger.sql").read_text()
        assert len(sql_content) > 0

        # Check metadata.json structure
        metadata = json.loads((hash_dir / "metadata.json").read_text())
        assert metadata["hash"] == "emit000000000001"
        assert metadata["crash_type"] == "ubsan"
        assert "version" in metadata
        assert "campaigns" in metadata

        # Check reproduce.sh is executable
        mode = (hash_dir / "reproduce.sh").stat().st_mode
        assert mode & stat.S_IXUSR

        # Check registry files exist at root
        assert (output_dir / "registry.json").exists()
        assert (output_dir / "registry.md").exists()

    def test_emit_registry_json_has_correct_structure(self, tmp_path):
        sql = "SELECT 1;"
        crash = _make_crash("reg0000000000001")
        workdirs_root = tmp_path / "workdirs"
        _make_workdir(workdirs_root, "sqlite-3.32.0_uniform_run1", [crash], {"reg0000000000001": sql})

        entries = scan_workdirs(workdirs_root)
        classes = group_into_classes(entries)
        output_dir = tmp_path / "results" / "crashes"
        emit_archive(entries, classes, output_dir, replay=False)

        registry = json.loads((output_dir / "registry.json").read_text())
        assert "generated_at" in registry
        assert "total_unique_crashes" in registry
        assert "total_bug_classes" in registry
        assert "campaigns_scanned" in registry
        assert "classes" in registry
        assert len(registry["classes"]) == 1


# ---------------------------------------------------------------------------
# Integration test on real workdirs
# ---------------------------------------------------------------------------

class TestIntegrationRealWorkdirs:
    @pytest.mark.skipif(
        not Path("workdirs").exists(),
        reason="workdirs/ not present — skip integration test",
    )
    def test_scan_and_emit_on_real_data(self, tmp_path: Path) -> None:
        """End-to-end: scan real workdirs, emit to temp dir, verify output."""
        entries = scan_workdirs(Path("workdirs"))
        assert len(entries) > 0, "Expected at least one crash hash from workdirs"

        classes = group_into_classes(entries)
        assert len(classes) > 0, "Expected at least one bug class"

        output_dir = tmp_path / "crashes"
        emit_archive(entries, classes, output_dir, replay=False)

        registry_path = output_dir / "registry.json"
        assert registry_path.exists()
        registry = json.loads(registry_path.read_text())
        assert registry["total_unique_crashes"] > 0
        assert registry["total_bug_classes"] > 0

        summary_path = output_dir / "registry.md"
        assert summary_path.exists()
        assert "Bug Classes" in summary_path.read_text()

        class_dirs = [d for d in output_dir.iterdir() if d.is_dir()]
        assert len(class_dirs) > 0

        first_class = class_dirs[0]
        assert (first_class / "README.md").exists()

        hash_dirs = [d for d in first_class.iterdir() if d.is_dir()]
        if hash_dirs:
            h = hash_dirs[0]
            assert (h / "trigger.sql").exists()
            assert (h / "metadata.json").exists()
            assert (h / "reproduce.sh").exists()
            assert (h / "stack_trace.txt").exists()
