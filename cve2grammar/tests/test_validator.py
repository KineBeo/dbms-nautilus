"""Tests for the agent-payload template validator."""

from __future__ import annotations

import pytest

from cve2grammar.generalizer.validate import ValidationError, validate_template


def _good_payload(**overrides) -> dict:
    payload = {
        "template": "SELECT * FROM {Table-Name}",
        "feature_tag": "basic_select",
        "weight": 3.0,
        "notes": "smoke test",
    }
    payload.update(overrides)
    return payload


_WHITELIST = {"Table-Name", "Col-Name", "Expr", "Literal-Value"}


class TestRequiredKeys:
    @pytest.mark.parametrize("missing", ["template", "feature_tag", "weight", "notes"])
    def test_missing_required_key_raises(self, missing: str) -> None:
        payload = _good_payload()
        del payload[missing]
        with pytest.raises(ValidationError, match=f"missing required key: {missing}"):
            validate_template(payload, _WHITELIST)

    def test_extra_keys_ok(self) -> None:
        # Extra keys are allowed — the skill may emit metadata we don't use yet.
        validate_template(_good_payload(extra="whatever"), _WHITELIST)


class TestTypes:
    def test_template_must_be_str(self) -> None:
        with pytest.raises(ValidationError, match="template must be str"):
            validate_template(_good_payload(template=123), _WHITELIST)

    def test_feature_tag_must_be_str(self) -> None:
        with pytest.raises(ValidationError, match="feature_tag must be str"):
            validate_template(_good_payload(feature_tag=None), _WHITELIST)

    def test_weight_must_be_number(self) -> None:
        with pytest.raises(ValidationError, match="weight must be a number"):
            validate_template(_good_payload(weight="3.0"), _WHITELIST)

    def test_weight_int_coerced_ok(self) -> None:
        # Agent may return `weight: 3` as JSON int; accept it.
        validate_template(_good_payload(weight=3), _WHITELIST)

    def test_weight_bool_rejected(self) -> None:
        # bool is a subclass of int in Python; we must NOT accept True/False as weights.
        with pytest.raises(ValidationError, match="weight must be a number"):
            validate_template(_good_payload(weight=True), _WHITELIST)

    def test_notes_must_be_str(self) -> None:
        with pytest.raises(ValidationError, match="notes must be str"):
            validate_template(_good_payload(notes=42), _WHITELIST)


class TestFeatureTag:
    @pytest.mark.parametrize("tag", [
        "abc",               # minimum length (3)
        "basic_select",
        "printf_precision_overflow",
        "fts4_snippet_boundary_value",
        "a" * 40,            # maximum length (40)
    ])
    def test_valid_tags(self, tag: str) -> None:
        validate_template(_good_payload(feature_tag=tag), _WHITELIST)

    @pytest.mark.parametrize("tag", [
        "",
        "a",                 # too short
        "ab",                # still too short — min 3 chars
        "BadCase",
        "has-hyphen",
        "has.period",
        "_leading_underscore",
        "1leading_digit",
        "trailing_space ",
        "a" * 41,            # too long — cap 40
    ])
    def test_invalid_tags(self, tag: str) -> None:
        with pytest.raises(ValidationError, match="feature_tag"):
            validate_template(_good_payload(feature_tag=tag), _WHITELIST)


class TestWeight:
    @pytest.mark.parametrize("w", [0.5, 1.0, 2.5, 3.0, 5.0])
    def test_valid_weights(self, w: float) -> None:
        validate_template(_good_payload(weight=w), _WHITELIST)

    @pytest.mark.parametrize("w", [0.0, 0.4, 5.1, 100.0, -1.0])
    def test_out_of_range_weights(self, w: float) -> None:
        with pytest.raises(ValidationError, match="weight"):
            validate_template(_good_payload(weight=w), _WHITELIST)


class TestNonterminals:
    def test_template_with_allowed_nonterminals(self) -> None:
        validate_template(
            _good_payload(template="SELECT {Col-Name} FROM {Table-Name}"),
            _WHITELIST,
        )

    def test_template_with_unknown_nonterminal_raises(self) -> None:
        with pytest.raises(ValidationError, match=r"unknown non-terminal: \{Foo-Bar\}"):
            validate_template(
                _good_payload(template="SELECT * FROM {Foo-Bar}"),
                _WHITELIST,
            )

    def test_error_message_names_first_unknown(self) -> None:
        try:
            validate_template(
                _good_payload(template="{Unknown-A} / {Unknown-B}"),
                _WHITELIST,
            )
        except ValidationError as e:
            assert "Unknown-A" in str(e)
        else:
            pytest.fail("expected ValidationError")

    def test_lowercase_brace_tokens_are_not_nonterminals(self) -> None:
        # {foo} is not a non-terminal — the regex requires leading uppercase.
        validate_template(
            _good_payload(template="{Table-Name} has {foo} inside"),
            _WHITELIST,
        )


class TestTerminator:
    def test_no_trailing_semicolon_ok(self) -> None:
        validate_template(
            _good_payload(template="SELECT * FROM {Table-Name}"),
            _WHITELIST,
        )

    def test_trailing_semicolon_rejected(self) -> None:
        with pytest.raises(ValidationError, match="trailing"):
            validate_template(
                _good_payload(template="SELECT * FROM {Table-Name};"),
                _WHITELIST,
            )

    def test_trailing_semicolon_with_whitespace_rejected(self) -> None:
        with pytest.raises(ValidationError, match="trailing"):
            validate_template(
                _good_payload(template="SELECT * FROM {Table-Name};\n"),
                _WHITELIST,
            )

    def test_intermediate_semicolons_fine(self) -> None:
        validate_template(
            _good_payload(
                template=(
                    "CREATE TABLE {Table-Name}(a);\n"
                    "INSERT INTO {Table-Name} VALUES ({Literal-Value});\n"
                    "SELECT * FROM {Table-Name}"
                ),
            ),
            _WHITELIST,
        )


class TestEmpty:
    def test_empty_template_rejected(self) -> None:
        with pytest.raises(ValidationError, match="empty"):
            validate_template(_good_payload(template=""), _WHITELIST)

    def test_whitespace_only_template_rejected(self) -> None:
        with pytest.raises(ValidationError, match="empty"):
            validate_template(_good_payload(template="   \n  "), _WHITELIST)


import json
from pathlib import Path

from cve2grammar.generalizer.validate import main as validate_main


class _StdinStub:
    """Minimal stand-in for sys.stdin that the validator CLI can `.read()`."""

    def __init__(self, text: str) -> None:
        self._text = text

    def read(self) -> str:
        return self._text


class TestCli:
    def test_valid_payload_on_stdin_exits_0(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture,
        tmp_path: Path,
    ) -> None:
        grammar = tmp_path / "g.py"
        grammar.write_text(
            'ctx.rule("Table-Name", "x")\nctx.rule("Col-Name", "x")\n',
            encoding="utf-8",
        )
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(grammar))
        monkeypatch.setattr(
            "sys.stdin",
            _StdinStub(json.dumps(_good_payload(template="{Table-Name}"))),
        )
        assert validate_main([]) == 0

    def test_invalid_payload_exits_1_with_stderr(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture,
        tmp_path: Path,
    ) -> None:
        grammar = tmp_path / "g.py"
        grammar.write_text('ctx.rule("Table-Name", "x")\n', encoding="utf-8")
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(grammar))
        monkeypatch.setattr(
            "sys.stdin",
            _StdinStub(json.dumps(_good_payload(template="{Foo-Bar}"))),
        )
        assert validate_main([]) == 1
        err = capsys.readouterr().err
        assert "unknown non-terminal: {Foo-Bar}" in err

    def test_malformed_json_on_stdin_exits_1(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture,
        tmp_path: Path,
    ) -> None:
        grammar = tmp_path / "g.py"
        grammar.write_text('ctx.rule("Table-Name", "x")\n', encoding="utf-8")
        monkeypatch.setenv("RL_NAUTILUS_GRAMMAR", str(grammar))
        monkeypatch.setattr("sys.stdin", _StdinStub("not even json"))
        assert validate_main([]) == 1
        err = capsys.readouterr().err
        assert "malformed json" in err.lower()
