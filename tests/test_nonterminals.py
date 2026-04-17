"""Tests for the non-terminal whitelist extractor."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cve2grammar.generalizer.nonterminals import (
    load_whitelist,
    main as nonterminals_main,
)


def _write_grammar(path: Path, body: str) -> Path:
    path.write_text(body, encoding="utf-8")
    return path


class TestLoadWhitelist:
    def test_empty_grammar_returns_empty_list(self, tmp_path: Path) -> None:
        g = _write_grammar(tmp_path / "g.py", "# just a comment\n")
        assert load_whitelist(g) == []

    def test_single_lhs_definition(self, tmp_path: Path) -> None:
        g = _write_grammar(tmp_path / "g.py", 'ctx.rule("Foo", "bar")\n')
        assert load_whitelist(g) == ["Foo"]

    def test_multiple_definitions_sorted_and_deduped(self, tmp_path: Path) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.rule("Zed", "x")\n'
            'ctx.rule("Alpha", "y")\n'
            'ctx.rule("Alpha", "z")\n'
        )
        assert load_whitelist(g) == ["Alpha", "Zed"]

    def test_rhs_references_captured(self, tmp_path: Path) -> None:
        g = _write_grammar(tmp_path / "g.py", 'ctx.rule("Foo", "{Bar}")\n')
        assert load_whitelist(g) == ["Bar", "Foo"]

    def test_multiple_rhs_references_in_one_rule(self, tmp_path: Path) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.rule("Stmt", "SELECT {Expr} FROM {Table} WHERE {Expr} = {Lit}")\n',
        )
        assert load_whitelist(g) == ["Expr", "Lit", "Stmt", "Table"]

    def test_nested_braces_in_python_dict_are_not_nonterminals(self, tmp_path: Path) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.rule("Foo", "{bar} is not a non-terminal but {Baz} is")\n',
        )
        assert load_whitelist(g) == ["Baz", "Foo"]

    def test_hyphenated_names_supported(self, tmp_path: Path) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.rule("Create-Table-Stmt", "CREATE TABLE {Table-Name}")\n',
        )
        assert load_whitelist(g) == ["Create-Table-Stmt", "Table-Name"]

    def test_ctx_regex_defines_nonterminal(self, tmp_path: Path) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.regex("Col-Alias", "[a-z][a-z0-9_]*")\n',
        )
        assert load_whitelist(g) == ["Col-Alias"]

    def test_missing_file_raises(self, tmp_path: Path) -> None:
        with pytest.raises(FileNotFoundError):
            load_whitelist(tmp_path / "does-not-exist.py")

    def test_env_var_override(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        g = _write_grammar(tmp_path / "custom.py", 'ctx.rule("FromEnv", "x")\n')
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(g))
        assert load_whitelist(None) == ["FromEnv"]


class TestCli:
    def test_cli_prints_json_array(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture,
    ) -> None:
        g = _write_grammar(
            tmp_path / "g.py",
            'ctx.rule("Foo", "{Bar}")\nctx.rule("Alpha", "x")\n',
        )
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(g))
        code = nonterminals_main([])
        assert code == 0
        out = capsys.readouterr().out
        assert json.loads(out) == ["Alpha", "Bar", "Foo"]

    def test_cli_missing_file_exits_1(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture,
    ) -> None:
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(tmp_path / "missing.py"))
        code = nonterminals_main([])
        assert code == 1
        err = capsys.readouterr().err
        assert "grammar file not found" in err.lower()

    def test_cli_accepts_path_argument(
        self, tmp_path: Path, capsys: pytest.CaptureFixture,
    ) -> None:
        g = _write_grammar(tmp_path / "g.py", 'ctx.rule("XFromArg", "y")\n')
        code = nonterminals_main([str(g)])
        assert code == 0
        assert json.loads(capsys.readouterr().out) == ["XFromArg"]
