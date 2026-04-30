"""Tests for triage.classify."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from triage.classify import (
    CrashCluster,
    CrashResult,
    build_clusters,
    classify_crash,
    enrich_campaign_json,
    extract_frames,
    write_report_md,
    write_triage_json,
)


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

    def test_sigtrap_is_debug_assert(self) -> None:
        result = classify_crash(-5, "")
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
