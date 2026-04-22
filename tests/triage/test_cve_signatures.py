"""Tests for triage.cve_signatures — required-node patterns per CVE."""
from __future__ import annotations

from triage import cve_signatures as sigs


class TestCoverage:
    def test_all_six_cves_present(self) -> None:
        cves = sigs.all_cves()
        ids = {c["cve"] for c in cves}
        expected = {
            "CVE-2020-15358",
            "CVE-2020-13871",
            "CVE-2020-13435",
            "CVE-2020-13434",
            "CVE-2020-9327",
            "CVE-2019-19646",
        }
        assert ids == expected

    def test_each_cve_has_required_patterns(self) -> None:
        for c in sigs.all_cves():
            assert len(c["required_patterns"]) >= 2, c["cve"]


class TestMatchP13435:
    def test_matches_real_cve_poc(self) -> None:
        poc = (
            "CREATE TABLE a(c UNIQUE);\n"
            "SELECT a.c FROM a JOIN a b ON 3 = a.c NATURAL JOIN a "
            "WHERE a.c IN((SELECT(SELECT coalesce(lead(2) OVER(), SUM(c))) FROM a d WHERE a.c));"
        )
        sig = sigs.get_cve("CVE-2020-13435")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []

    def test_rejects_loose_sample(self) -> None:
        loose = "SELECT * FROM a JOIN b ON 1=1;"
        sig = sigs.get_cve("CVE-2020-13435")
        missing = sigs.missing_patterns(loose, sig)
        assert len(missing) > 0
        assert "NATURAL_JOIN" in missing


class TestMatchP13434:
    def test_matches_boundary_form(self) -> None:
        poc = "SELECT printf('%.*g', 2147483647, 0.01);"
        sig = sigs.get_cve("CVE-2020-13434")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []


class TestMatchP19646:
    def test_matches(self) -> None:
        poc = (
            "CREATE TABLE t0 (c0, c1 NOT NULL GENERATED ALWAYS AS (c0 = 0));\n"
            "INSERT INTO t0(c0) VALUES (0);\n"
            "PRAGMA integrity_check;"
        )
        sig = sigs.get_cve("CVE-2019-19646")
        missing = sigs.missing_patterns(poc, sig)
        assert missing == []
