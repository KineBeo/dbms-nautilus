"""CLI integration tests for the `generalize-candidates` subcommand."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cve2grammar.cli import main

FIXTURE = Path(__file__).parent / "fixtures" / "sample_page.html"


class TestGeneralizeCandidates:
    def test_default_oracle_is_crash(
        self, capsys: pytest.CaptureFixture,
    ) -> None:
        # The sample fixture has no crash-oracle bugs. Default should emit [].
        code = main(["generalize-candidates", "--html", str(FIXTURE)])
        assert code == 0
        out = capsys.readouterr().out
        assert json.loads(out) == []

    def test_oracle_flag_filters(self, capsys: pytest.CaptureFixture) -> None:
        code = main([
            "generalize-candidates", "--html", str(FIXTURE),
            "--oracle", "PQS",
        ])
        assert code == 0
        out = capsys.readouterr().out
        data = json.loads(out)
        assert len(data) > 0
        for bug in data:
            assert bug["oracle"] == "PQS"

    def test_output_shape(self, capsys: pytest.CaptureFixture) -> None:
        main([
            "generalize-candidates", "--html", str(FIXTURE),
            "--oracle", "PQS",
        ])
        out = capsys.readouterr().out
        data = json.loads(out)
        first = data[0]
        for key in ["id", "sql", "title", "dbms", "oracle", "date"]:
            assert key in first

    def test_dbms_filter(self, capsys: pytest.CaptureFixture) -> None:
        main([
            "generalize-candidates", "--html", str(FIXTURE),
            "--oracle", "PQS", "--dbms", "sqlite",
        ])
        out = capsys.readouterr().out
        data = json.loads(out)
        assert all(b["dbms"] == "sqlite" for b in data)

    def test_fetch_subcommand_still_works(self, tmp_path: Path) -> None:
        # Regression guard: the existing fetch subcommand is untouched.
        out = tmp_path / "grammar.py"
        code = main([
            "fetch", "--dbms", "sqlite",
            "--html", str(FIXTURE), "-o", str(out),
        ])
        assert code == 0
        assert out.exists()

    def test_dashboard_subcommand_still_works(self, tmp_path: Path) -> None:
        # Regression guard: the existing dashboard subcommand is untouched.
        out = tmp_path / "d.html"
        code = main([
            "dashboard", "--html", str(FIXTURE), "-o", str(out),
        ])
        assert code == 0
        assert out.exists()
