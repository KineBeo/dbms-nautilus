"""Tests for the Manuel Rigger scraper.

The fixture at tests/fixtures/sample_page.html is a real subset of the live page:
- Unique fixed bugs / SQLite: bugs #1, #2, #3
- Unique fixed bugs / PostgreSQL: bugs #1, #2
- Unique confirmed bugs / MySQL: bugs #1, #2

Total: 7 bugs across 3 DBMS and 2 sections.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cve2grammar.models import Bug
from cve2grammar.scraper.manuelrigger import (
    DBMS_HEADINGS,
    SECTION_LABEL,
    _parse_date,
    fetch,
)

FIXTURE = Path(__file__).parent / "fixtures" / "sample_page.html"


@pytest.fixture(scope="module")
def sample_html() -> str:
    return FIXTURE.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def all_bugs(sample_html: str) -> list[Bug]:
    return fetch(html=sample_html)


# ---------------------------------------------------------------------------
# fetch() — overall counts and routing
# ---------------------------------------------------------------------------


class TestFetchCounts:
    def test_total_bug_count(self, all_bugs: list[Bug]) -> None:
        assert len(all_bugs) == 7

    def test_sqlite_count(self, all_bugs: list[Bug]) -> None:
        assert sum(1 for b in all_bugs if b.dbms == "sqlite") == 3

    def test_postgresql_count(self, all_bugs: list[Bug]) -> None:
        assert sum(1 for b in all_bugs if b.dbms == "postgresql") == 2

    def test_mysql_count(self, all_bugs: list[Bug]) -> None:
        assert sum(1 for b in all_bugs if b.dbms == "mysql") == 2

    def test_section_routing(self, all_bugs: list[Bug]) -> None:
        sqlite = [b for b in all_bugs if b.dbms == "sqlite"]
        mysql = [b for b in all_bugs if b.dbms == "mysql"]
        assert all(b.section == "fixed" for b in sqlite)
        assert all(b.section == "confirmed" for b in mysql)


# ---------------------------------------------------------------------------
# Bug field extraction (focus on bug #1 SQLite — fully populated)
# ---------------------------------------------------------------------------


class TestBugFields:
    @pytest.fixture(scope="class")
    def bug1(self, sample_html: str) -> Bug:
        bugs = fetch(html=sample_html)
        return next(b for b in bugs if b.id == "MR-SQLITE-0001")

    def test_id_format(self, bug1: Bug) -> None:
        assert bug1.id == "MR-SQLITE-0001"

    def test_dbms(self, bug1: Bug) -> None:
        assert bug1.dbms == "sqlite"

    def test_section(self, bug1: Bug) -> None:
        assert bug1.section == "fixed"

    def test_number(self, bug1: Bug) -> None:
        assert bug1.number == 1

    def test_title(self, bug1: Bug) -> None:
        assert bug1.title == "COLLATE nocase index on a WITHOUT ROWID table malfunctions"

    def test_sql_includes_create_table(self, bug1: Bug) -> None:
        assert "CREATE TABLE test" in bug1.sql

    def test_sql_includes_select(self, bug1: Bug) -> None:
        assert "SELECT * FROM test" in bug1.sql

    def test_sql_is_stripped(self, bug1: Bug) -> None:
        assert not bug1.sql.startswith("\n")
        assert not bug1.sql.endswith("\n\n")

    def test_oracle(self, bug1: Bug) -> None:
        assert bug1.oracle == "PQS"

    def test_status(self, bug1: Bug) -> None:
        assert bug1.status == "fixed"

    def test_date_found_iso(self, bug1: Bug) -> None:
        assert bug1.date_found == "2019-05-28"

    def test_bugtracker_url(self, bug1: Bug) -> None:
        assert "sqlite.org/src/tktview" in bug1.bugtracker_url

    def test_email_url(self, bug1: Bug) -> None:
        assert "mailinglists.sqlite.org" in bug1.email_url

    def test_fix_url(self, bug1: Bug) -> None:
        assert bug1.fix_url == "https://www.sqlite.org/src/info/1b1dd4d48cd79a58"

    def test_bug_is_frozen(self, bug1: Bug) -> None:
        with pytest.raises(AttributeError):
            bug1.title = "modified"  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


class TestEdgeCases:
    def test_status_with_parens_preserved(self, all_bugs: list[Bug]) -> None:
        """Bug #2 SQLite has Status: 'fixed (in documentation)'."""
        bug = next(b for b in all_bugs if b.id == "MR-SQLITE-0002")
        assert bug.status == "fixed (in documentation)"

    def test_oracle_error(self, all_bugs: list[Bug]) -> None:
        bug = next(b for b in all_bugs if b.id == "MR-SQLITE-0002")
        assert bug.oracle == "error"

    def test_postgresql_fix_url_is_github(self, all_bugs: list[Bug]) -> None:
        bug = next(b for b in all_bugs if b.id == "MR-POSTGRESQL-0001")
        assert "github.com/postgres/postgres" in bug.fix_url

    def test_postgresql_no_bugtracker(self, all_bugs: list[Bug]) -> None:
        """PG bugs in fixture have no [bugtracker] link."""
        bug = next(b for b in all_bugs if b.id == "MR-POSTGRESQL-0001")
        assert bug.bugtracker_url == ""

    def test_mysql_no_fix_url(self, all_bugs: list[Bug]) -> None:
        """MySQL confirmed bugs have only [bugtracker], no [fix]."""
        bug = next(b for b in all_bugs if b.id == "MR-MYSQL-0001")
        assert bug.fix_url == ""
        assert "bugs.mysql.com" in bug.bugtracker_url

    def test_postgresql_repeated_email_label(self, all_bugs: list[Bug]) -> None:
        """PG bug #2 has [email] and [email 2] — first wins."""
        bug = next(b for b in all_bugs if b.id == "MR-POSTGRESQL-0002")
        assert "postgresql.org/message-id" in bug.email_url

    def test_postgresql_dd_mm_yyyy_with_padding(self, all_bugs: list[Bug]) -> None:
        """'02/07/2019' → '2019-07-02'."""
        bug = next(b for b in all_bugs if b.id == "MR-POSTGRESQL-0001")
        assert bug.date_found == "2019-07-02"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class TestParseDate:
    @pytest.mark.parametrize("raw,expected", [
        ("28/5/2019", "2019-05-28"),
        ("02/07/2019", "2019-07-02"),
        ("4/07/2019", "2019-07-04"),
        ("15/06/2019", "2019-06-15"),
        ("28.5.2019", "2019-05-28"),
        ("", ""),
        ("not a date", ""),
        ("28/5/19", ""),  # 2-digit year is rejected
    ])
    def test_parse_date(self, raw: str, expected: str) -> None:
        assert _parse_date(raw) == expected


class TestConstants:
    def test_dbms_headings_complete(self) -> None:
        assert "SQLite" in DBMS_HEADINGS
        assert DBMS_HEADINGS["SQLite"] == "sqlite"
        assert len(DBMS_HEADINGS) == 9

    def test_section_labels_complete(self) -> None:
        assert SECTION_LABEL["Unique fixed bugs"] == "fixed"
        assert SECTION_LABEL["Unique confirmed bugs"] == "confirmed"
        assert len(SECTION_LABEL) == 4


# ---------------------------------------------------------------------------
# Empty / malformed input
# ---------------------------------------------------------------------------


class TestRobustness:
    def test_empty_html(self) -> None:
        assert fetch(html="") == []

    def test_html_without_bugs(self) -> None:
        html = "<html><body><h1>Hello</h1></body></html>"
        assert fetch(html=html) == []

    def test_bug_without_pre_block_skipped(self) -> None:
        html = """
        <h2>Unique fixed bugs</h2>
        <h3>SQLite</h3>
        <ul>
          <li>
            <b>#999 No test case bug</b>
            <details>
              <b>Date found</b>: 1/1/2020<br />
              <b>Status</b>: fixed<br />
            </details>
          </li>
        </ul>
        """
        assert fetch(html=html) == []

    def test_bug_with_empty_pre_skipped(self) -> None:
        html = """
        <h2>Unique fixed bugs</h2>
        <h3>SQLite</h3>
        <ul>
          <li>
            <b>#999 Empty SQL</b>
            <details><pre>   </pre></details>
          </li>
        </ul>
        """
        assert fetch(html=html) == []
