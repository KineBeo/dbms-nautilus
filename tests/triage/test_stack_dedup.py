"""Tests for triage.stack_dedup."""
from __future__ import annotations

from triage import stack_dedup


class TestFrameFiltering:
    def test_drops_libc_frames(self) -> None:
        raw = [
            "__libc_start_main:libc-start.c:332",
            "sqlite3_str_vappendf:sqlite3.c:28528",
            "sqliteVPrintfFunc:sqlite3.c:28810",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert all("libc" not in f for f in kept)
        assert len(kept) == 2

    def test_drops_asan_frames(self) -> None:
        raw = [
            "__asan::ReportGenericError:asan_report.cc:200",
            "sqlite3_str_vappendf:sqlite3.c:28528",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert len(kept) == 1
        assert "sqlite3_str_vappendf" in kept[0]

    def test_keeps_sqlite_frames(self) -> None:
        raw = [
            "sqlite3_str_vappendf:sqlite3.c:28528",
            "sqliteVPrintfFunc:sqlite3.c:28810",
        ]
        kept = stack_dedup.filter_frames(raw)
        assert len(kept) == 2


class TestHashing:
    def test_identical_frames_hash_identically(self) -> None:
        frames_a = ["sqlite3_str_vappendf:sqlite3.c:28528", "sqliteVPrintfFunc:sqlite3.c:28810"]
        frames_b = ["sqlite3_str_vappendf:sqlite3.c:28528", "sqliteVPrintfFunc:sqlite3.c:28810"]
        assert stack_dedup.hash_frames(frames_a) == stack_dedup.hash_frames(frames_b)

    def test_different_frames_hash_differently(self) -> None:
        frames_a = ["sqlite3_str_vappendf:sqlite3.c:28528"]
        frames_b = ["sqlite3VdbeExec:sqlite3.c:99999"]
        assert stack_dedup.hash_frames(frames_a) != stack_dedup.hash_frames(frames_b)


class TestClusterBuilding:
    def test_groups_three_crashes_with_same_frames(self) -> None:
        crashes = [
            {"file": "5_000001", "sql": "SELECT printf('%.*g', 2147483647, 0.01);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000002", "sql": "SELECT printf('%.*g', -2147483648, 3.1);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000003", "sql": "SELECT printf('abc', 2147483647, 0);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
        ]
        clusters = stack_dedup.build_clusters(crashes)
        assert len(clusters) == 1
        assert clusters[0]["count"] == 3
        assert clusters[0]["top_frame"] == "sqlite3_str_vappendf:sqlite3.c:28528"

    def test_splits_two_root_causes(self) -> None:
        crashes = [
            {"file": "5_000001", "sql": "SELECT printf(...);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000002", "sql": "SELECT printf(...);", "frames": ["sqlite3_str_vappendf:sqlite3.c:28528"]},
            {"file": "5_000003", "sql": "SELECT coalesce(...);", "frames": ["sqlite3VdbeExec:sqlite3.c:99999"]},
        ]
        clusters = stack_dedup.build_clusters(crashes)
        assert len(clusters) == 2
        counts = sorted(c["count"] for c in clusters)
        assert counts == [1, 2]


class TestGdbOutputParsing:
    def test_parses_bt_5_output(self) -> None:
        gdb_output = (
            "Thread 1 \"sqlite_harness_\" received signal SIGTRAP, Trace/breakpoint trap.\n"
            "#0  sqlite3_str_vappendf (pAccum=0x0, fmt=..., ap=...) at sqlite3.c:28528\n"
            "#1  0x00007ffff7a12345 in sqliteVPrintfFunc (context=0x0) at sqlite3.c:28810\n"
            "#2  0x00007ffff7a00000 in sqlite3VdbeExec (p=0x0) at sqlite3.c:85000\n"
        )
        frames = stack_dedup.parse_gdb_bt(gdb_output)
        assert frames[0] == "sqlite3_str_vappendf:sqlite3.c:28528"
        assert frames[1] == "sqliteVPrintfFunc:sqlite3.c:28810"
        assert frames[2] == "sqlite3VdbeExec:sqlite3.c:85000"
