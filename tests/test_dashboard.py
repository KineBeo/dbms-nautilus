"""Tests for the dashboard emitter (HTML output for bug triage)."""

from __future__ import annotations

import json

from cve2grammar.config import SUPPORTED_DBMS
from cve2grammar.dashboard import _bug_to_dict, _build_payload, _serialize_payload
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


class TestBuildPayload:
    def test_generated_timestamp_is_iso_utc(self) -> None:
        out = _build_payload([])
        # Strict ISO-8601 UTC: "YYYY-MM-DDTHH:MM:SSZ"
        assert len(out["generated"]) == 20
        assert out["generated"].endswith("Z")
        assert out["generated"][4] == "-" and out["generated"][7] == "-"
        assert out["generated"][10] == "T"

    def test_source_url(self) -> None:
        out = _build_payload([])
        assert out["source"] == "https://www.manuelrigger.at/dbms-bugs/"

    def test_facets_dbms_matches_config(self) -> None:
        out = _build_payload([])
        assert out["facets"]["dbms"] == list(SUPPORTED_DBMS)

    def test_facets_oracles_in_priority_order(self) -> None:
        out = _build_payload([])
        # crash first (memory-safety priority), then hang, error, logic oracles,
        # empty-oracle bucket last.
        assert out["facets"]["oracles"] == [
            "crash", "hang", "error", "PQS", "NoREC", "TLP", "",
        ]

    def test_facets_sections(self) -> None:
        out = _build_payload([])
        assert out["facets"]["sections"] == [
            "fixed", "confirmed", "open", "closed",
        ]

    def test_bugs_present_as_dicts(self) -> None:
        bugs = [_make_bug(id="A", number=1), _make_bug(id="B", number=2)]
        out = _build_payload(bugs)
        assert len(out["bugs"]) == 2
        assert out["bugs"][0]["id"] == "A"
        assert out["bugs"][1]["id"] == "B"

    def test_bugs_sorted_by_section_then_number(self) -> None:
        bugs = [
            _make_bug(id="X", section="fixed", number=2),
            _make_bug(id="Y", section="confirmed", number=1),
            _make_bug(id="Z", section="fixed", number=1),
        ]
        out = _build_payload(bugs)
        ids = [b["id"] for b in out["bugs"]]
        # confirmed < fixed alphabetically; within section, ascending number
        assert ids == ["Y", "Z", "X"]

    def test_empty_bugs_list(self) -> None:
        out = _build_payload([])
        assert out["bugs"] == []


class TestSerializePayload:
    def test_roundtrip_simple_payload(self) -> None:
        payload = {"bugs": [{"id": "X", "sql": "SELECT 1;"}]}
        out = _serialize_payload(payload)
        assert json.loads(out) == payload

    def test_close_script_substring_is_escaped(self) -> None:
        payload = {"bugs": [{"sql": "x </script> y"}]}
        out = _serialize_payload(payload)
        # The raw serialized string must not contain "</" at all — that is
        # what protects the <script type="application/json"> tag.
        assert "</" not in out
        # But the original bug data must round-trip through json.loads.
        assert json.loads(out)["bugs"][0]["sql"] == "x </script> y"

    def test_close_tag_case_insensitive_substring_also_escaped(self) -> None:
        # Defensive: if someone ever switches the container tag case, we still
        # don't want any "</" anywhere in the serialized output.
        payload = {"bugs": [{"sql": "abc </SCRIPT> def", "title": "</a>"}]}
        out = _serialize_payload(payload)
        assert "</" not in out
        assert json.loads(out)["bugs"][0]["sql"] == "abc </SCRIPT> def"
        assert json.loads(out)["bugs"][0]["title"] == "</a>"

    def test_unicode_ascii_escaped(self) -> None:
        payload = {"bugs": [{"title": "café — é"}]}
        out = _serialize_payload(payload)
        # ensure_ascii=True → every non-ASCII char becomes \uXXXX
        assert "\\u00e9" in out  # é
        assert json.loads(out)["bugs"][0]["title"] == "café — é"

    def test_no_line_breaks_inside_serialized_payload(self) -> None:
        # Compact output (no indent) keeps the <script> tag on as few lines
        # as possible and avoids surprising the JS parser.
        payload = {"bugs": [{"id": "A"}, {"id": "B"}]}
        out = _serialize_payload(payload)
        assert "\n" not in out
