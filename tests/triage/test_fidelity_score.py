"""Tests for triage.fidelity_score — scores samples, writes biased grammar."""
from __future__ import annotations

from pathlib import Path

from triage import fidelity_score as fs
from triage import cve_signatures as sigs


class TestScoreSamples:
    def test_all_samples_match(self) -> None:
        samples = [
            "SELECT printf('%.*g', 2147483647, 0.01);",
            "SELECT printf('%.*g', -2147483648, 3.1);",
        ]
        sig = sigs.get_cve("CVE-2020-13434")
        result = fs.score_samples(samples, sig)
        assert result["samples_generated"] == 2
        assert result["samples_with_all_required"] == 2
        assert result["fidelity_score"] == 1.0

    def test_partial(self) -> None:
        samples = [
            "SELECT printf('%.*g', 2147483647, 0.01);",
            "SELECT length('hi');",
        ]
        sig = sigs.get_cve("CVE-2020-13434")
        result = fs.score_samples(samples, sig)
        assert result["samples_with_all_required"] == 1
        assert result["fidelity_score"] == 0.5
        assert result["samples_missing_node"]["printf_call"] == 1

    def test_zero(self) -> None:
        samples = ["SELECT 1;", "SELECT 2;"]
        sig = sigs.get_cve("CVE-2020-13435")
        result = fs.score_samples(samples, sig)
        assert result["fidelity_score"] == 0.0
        for label in ("NATURAL_JOIN", "coalesce_call", "window_over", "UNIQUE_column", "IN_subquery"):
            assert result["samples_missing_node"][label] == 2


class TestBiasedGrammar:
    def test_weights_target_high_others_zero(self, tmp_path: Path) -> None:
        base = tmp_path / "base_grammar.py"
        base.write_text(
            'ctx.rule("Sql-Stmt", "SELECT 1;")\n'
            'ctx.rule("Sql-Stmt", "{Pattern-X}")\n'
            'ctx.rule("Pattern-X", "SELECT X;")\n'
        )
        out = tmp_path / "biased.py"
        fs.write_biased_grammar(base, out, target_pattern_nt="Pattern-X", high_weight=100.0)
        text = out.read_text()
        assert 'weight=100' in text
        assert 'weight=0' in text
        assert 'ctx.rule("Pattern-X", "SELECT X;")' in text
