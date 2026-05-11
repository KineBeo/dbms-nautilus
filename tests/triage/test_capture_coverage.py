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
