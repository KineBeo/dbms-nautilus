"""CLI integration tests for the `dashboard` subcommand."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from cve2grammar.cli import main

FIXTURE = Path(__file__).parent / "fixtures" / "sample_page.html"


def _extract_bugs_json(html: str) -> dict:
    match = re.search(
        r'<script id="bugs-data" type="application/json">(.*?)</script>',
        html,
        re.DOTALL,
    )
    assert match is not None
    return json.loads(match.group(1).replace("<\\/", "</"))


class TestDashboardCli:
    def test_dashboard_writes_html_file(self, tmp_path: Path) -> None:
        out = tmp_path / "dash.html"
        code = main(["dashboard", "--html", str(FIXTURE), "-o", str(out)])
        assert code == 0
        assert out.exists()
        assert out.read_text(encoding="utf-8").startswith("<!doctype html>")

    def test_dashboard_default_section_is_fixed(self, tmp_path: Path) -> None:
        # Fixture: 5 fixed + 2 confirmed = 7 total. Default section is "fixed".
        out = tmp_path / "dash.html"
        main(["dashboard", "--html", str(FIXTURE), "-o", str(out)])
        payload = _extract_bugs_json(out.read_text(encoding="utf-8"))
        assert len(payload["bugs"]) == 5

    def test_dashboard_section_all_includes_confirmed(self, tmp_path: Path) -> None:
        out = tmp_path / "dash.html"
        main([
            "dashboard", "--section", "all",
            "--html", str(FIXTURE), "-o", str(out),
        ])
        payload = _extract_bugs_json(out.read_text(encoding="utf-8"))
        assert len(payload["bugs"]) == 7

    def test_dashboard_has_no_dbms_flag(self, tmp_path: Path) -> None:
        # --dbms is a fetch-only flag; dashboard does not accept it.
        out = tmp_path / "dash.html"
        with pytest.raises(SystemExit):
            main([
                "dashboard", "--dbms", "sqlite",
                "--html", str(FIXTURE), "-o", str(out),
            ])

    def test_dashboard_exits_1_on_zero_bugs(
        self, tmp_path: Path, capsys: pytest.CaptureFixture,
    ) -> None:
        empty = tmp_path / "empty.html"
        empty.write_text("<html><body>nothing here</body></html>", encoding="utf-8")
        out = tmp_path / "dash.html"
        code = main(["dashboard", "--html", str(empty), "-o", str(out)])
        assert code == 1
        assert not out.exists()
        err = capsys.readouterr().err
        assert "No bugs found" in err

    def test_dashboard_prints_summary_on_success(
        self, tmp_path: Path, capsys: pytest.CaptureFixture,
    ) -> None:
        out = tmp_path / "dash.html"
        main(["dashboard", "--html", str(FIXTURE), "-o", str(out)])
        stdout = capsys.readouterr().out
        assert "bugs" in stdout
        assert str(out) in stdout

    def test_fetch_still_works_unchanged(self, tmp_path: Path) -> None:
        # Regression guard: the existing `fetch` subcommand is untouched.
        out = tmp_path / "grammar.py"
        code = main([
            "fetch", "--dbms", "sqlite",
            "--html", str(FIXTURE), "-o", str(out),
        ])
        assert code == 0
        assert out.exists()
        assert 'ctx.rule("Sql-Stmt"' in out.read_text(encoding="utf-8")
