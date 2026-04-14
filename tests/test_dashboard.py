"""Tests for the dashboard emitter (HTML output for bug triage)."""

from __future__ import annotations

from cve2grammar.dashboard import _bug_to_dict
from cve2grammar.models import Bug


def _make_bug(
    *,
    id: str = "MR-SQLITE-0001",
    dbms: str = "sqlite",
    section: str = "fixed",
    number: int = 1,
    title: str = "test bug",
    sql: str = "SELECT 1;",
    oracle: str = "PQS",
    status: str = "fixed",
    date_found: str = "2019-05-28",
    bugtracker_url: str = "",
    email_url: str = "",
    fix_url: str = "",
) -> Bug:
    return Bug(
        id=id, dbms=dbms, section=section, number=number, title=title, sql=sql,
        oracle=oracle, status=status, date_found=date_found,
        bugtracker_url=bugtracker_url, email_url=email_url, fix_url=fix_url,
    )


class TestBugToDict:
    def test_all_core_fields_present(self) -> None:
        bug = _make_bug()
        out = _bug_to_dict(bug)
        assert out["id"] == "MR-SQLITE-0001"
        assert out["dbms"] == "sqlite"
        assert out["section"] == "fixed"
        assert out["number"] == 1
        assert out["title"] == "test bug"
        assert out["oracle"] == "PQS"
        assert out["status"] == "fixed"
        assert out["sql"] == "SELECT 1;"

    def test_month_derived_from_iso_date(self) -> None:
        out = _bug_to_dict(_make_bug(date_found="2019-05-28"))
        assert out["date"] == "2019-05-28"
        assert out["month"] == "2019-05"

    def test_month_empty_when_date_empty(self) -> None:
        out = _bug_to_dict(_make_bug(date_found=""))
        assert out["date"] == ""
        assert out["month"] == ""

    def test_links_nested_with_empty_strings_preserved(self) -> None:
        out = _bug_to_dict(_make_bug(
            bugtracker_url="https://tracker/1",
            email_url="",
            fix_url="https://fix/1",
        ))
        assert out["links"] == {
            "bugtracker": "https://tracker/1",
            "email": "",
            "fix": "https://fix/1",
        }
