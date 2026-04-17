"""Tests for the content-addressed cache."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from cve2grammar.generalizer.cache import (
    CACHE_ROOT,
    CacheConfig,
    cache_get,
    cache_key,
    cache_put,
)


@pytest.fixture
def cache_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect CACHE_ROOT to a tmp_path dir so tests don't touch real cache."""
    root = tmp_path / "cache" / "generalizer"
    root.mkdir(parents=True)
    monkeypatch.setattr(
        "cve2grammar.generalizer.cache._config",
        CacheConfig(root=root, prompt_version=1),
    )
    return root


def _minimal_entry(**overrides) -> dict:
    entry = {
        "bug_id": "MR-SQLITE-0001",
        "sql_sha256": "abcd1234",
        "prompt_version": 1,
        "model": "sonnet-4.6",
        "created_at": "2026-04-16T09:30:00Z",
        "status": "ok",
        "template": "SELECT 1",
        "feature_tag": "smoke",
        "weight": 3.0,
        "notes": "",
    }
    entry.update(overrides)
    return entry


class TestCacheKey:
    def test_key_is_16_hex_chars(self) -> None:
        k = cache_key("SELECT 1;")
        assert len(k) == 16
        assert all(c in "0123456789abcdef" for c in k)

    def test_same_input_same_key(self) -> None:
        assert cache_key("SELECT 1;") == cache_key("SELECT 1;")

    def test_different_input_different_key(self) -> None:
        assert cache_key("SELECT 1;") != cache_key("SELECT 2;")

    def test_unicode_input_stable(self) -> None:
        a = cache_key("SELECT 'café'")
        b = cache_key("SELECT 'café'")
        assert a == b and len(a) == 16


class TestGetPut:
    def test_put_then_get_roundtrip(self, cache_root: Path) -> None:
        entry = _minimal_entry()
        cache_put("deadbeef00000001", entry)
        got = cache_get("deadbeef00000001")
        assert got == entry

    def test_get_miss_returns_none(self, cache_root: Path) -> None:
        assert cache_get("ffffffff00000000") is None

    def test_put_writes_file_at_expected_path(self, cache_root: Path) -> None:
        cache_put("0123456789abcdef", _minimal_entry())
        assert (cache_root / "0123456789abcdef.json").exists()


class TestPromptVersion:
    def test_stored_version_mismatch_is_miss(
        self, cache_root: Path, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        cache_put("aaaabbbbccccdddd", _minimal_entry(prompt_version=1))
        monkeypatch.setattr(
            "cve2grammar.generalizer.cache._config",
            CacheConfig(root=cache_root, prompt_version=2),
        )
        assert cache_get("aaaabbbbccccdddd") is None


class TestCorruption:
    def test_corrupt_json_file_treated_as_miss(self, cache_root: Path) -> None:
        (cache_root / "badfileaaaabbbb.json").write_text("{not json", encoding="utf-8")
        assert cache_get("badfileaaaabbbb") is None

    def test_missing_prompt_version_field_is_miss(self, cache_root: Path) -> None:
        (cache_root / "nofieldaaabbbccc.json").write_text(
            json.dumps({"template": "x"}), encoding="utf-8",
        )
        assert cache_get("nofieldaaabbbccc") is None


class TestAtomicity:
    def test_no_tmp_file_left_after_successful_put(self, cache_root: Path) -> None:
        cache_put("f00df00df00df00d", _minimal_entry())
        tmps = list(cache_root.glob("*.tmp"))
        assert tmps == []

    def test_put_with_crash_leaves_no_half_written_file(
        self, cache_root: Path, monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        def _boom(src, dst):
            raise OSError("simulated crash during rename")

        monkeypatch.setattr(os, "replace", _boom)
        with pytest.raises(OSError):
            cache_put("c1a5ha5ha5hc0000", _minimal_entry())
        assert not (cache_root / "c1a5ha5ha5hc0000.json").exists()
