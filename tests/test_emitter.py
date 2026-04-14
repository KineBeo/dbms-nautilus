"""Tests for the Nautilus grammar emitter."""

from __future__ import annotations

import pytest

from cve2grammar.emitter import emit_nautilus
from cve2grammar.models import Bug


def make_bug(
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


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------


class TestHeader:
    def test_header_includes_dbms(self) -> None:
        out = emit_nautilus([make_bug()], dbms="sqlite")
        assert "Auto-generated grammar for sqlite" in out

    def test_header_includes_source_attribution(self) -> None:
        out = emit_nautilus([make_bug()], dbms="sqlite")
        assert "Manuel Rigger" in out
        assert "manuelrigger.at/dbms-bugs" in out

    def test_header_includes_count(self) -> None:
        out = emit_nautilus([make_bug(id="A", number=1), make_bug(id="B", number=2)],
                            dbms="sqlite")
        assert "Bugs: 2" in out

    def test_empty_input(self) -> None:
        out = emit_nautilus([], dbms="sqlite")
        assert "Bugs: 0" in out
        assert "No bugs to emit" in out
        assert "ctx.rule" not in out


# ---------------------------------------------------------------------------
# Per-bug rendering
# ---------------------------------------------------------------------------


class TestBugRendering:
    def test_bug_section_header_present(self) -> None:
        out = emit_nautilus([make_bug(id="MR-SQLITE-0001", oracle="PQS",
                                      status="fixed")], dbms="sqlite")
        assert "# === MR-SQLITE-0001 (PQS, fixed) ===" in out

    def test_bug_title_comment(self) -> None:
        out = emit_nautilus([make_bug(title="COLLATE issue")], dbms="sqlite")
        assert "# COLLATE issue" in out

    def test_single_line_sql_uses_double_quotes(self) -> None:
        out = emit_nautilus([make_bug(sql="SELECT 1;", oracle="PQS")], dbms="sqlite")
        assert 'ctx.rule("Sql-Stmt", "SELECT 1;", weight=2.0)' in out

    def test_multiline_sql_uses_triple_quotes(self) -> None:
        sql = "CREATE TABLE t(c);\nSELECT * FROM t;"
        out = emit_nautilus([make_bug(sql=sql, oracle="crash")], dbms="sqlite")
        assert 'ctx.rule("Sql-Stmt", """CREATE TABLE t(c);\nSELECT * FROM t;""", weight=3.0)' in out

    def test_unspecified_oracle_label(self) -> None:
        out = emit_nautilus([make_bug(oracle="")], dbms="sqlite")
        assert "(unspecified," in out

    def test_unknown_status_label(self) -> None:
        out = emit_nautilus([make_bug(status="")], dbms="sqlite")
        assert ", unknown)" in out


# ---------------------------------------------------------------------------
# Weight assignment by oracle
# ---------------------------------------------------------------------------


class TestWeights:
    @pytest.mark.parametrize("oracle,weight", [
        ("crash", 3.0),
        ("hang", 2.5),
        ("error", 2.0),
        ("PQS", 2.0),
        ("NoREC", 2.0),
        ("TLP", 2.0),
        ("", 1.5),
        ("unknown_oracle", 1.5),
    ])
    def test_weight_per_oracle(self, oracle: str, weight: float) -> None:
        out = emit_nautilus([make_bug(oracle=oracle, sql="SELECT 1;")], dbms="sqlite")
        assert f"weight={weight}" in out


# ---------------------------------------------------------------------------
# Escaping
# ---------------------------------------------------------------------------


class TestEscaping:
    def test_double_quote_in_single_line_sql_is_escaped(self) -> None:
        out = emit_nautilus([make_bug(sql='SELECT "x";')], dbms="sqlite")
        assert 'ctx.rule("Sql-Stmt", "SELECT \\"x\\";"' in out

    def test_backslash_in_single_line_sql_is_escaped(self) -> None:
        out = emit_nautilus([make_bug(sql=r"SELECT '\n';")], dbms="sqlite")
        assert r"SELECT '\\n';" in out

    def test_triple_quote_in_multiline_sql_is_escaped(self) -> None:
        sql = '''SELECT 1;
"""raw'''
        out = emit_nautilus([make_bug(sql=sql)], dbms="sqlite")
        assert '\\"\\"\\"raw' in out

    def test_emitted_grammar_is_valid_python(self, tmp_path) -> None:
        """Round-trip: write the emitted file and import it under a stub ctx."""
        bugs = [
            make_bug(id="MR-SQLITE-0001", number=1, sql="SELECT 1;", oracle="PQS"),
            make_bug(
                id="MR-SQLITE-0002", number=2, oracle="crash",
                sql='SELECT "a";\nDROP TABLE t;',
            ),
        ]
        out = emit_nautilus(bugs, dbms="sqlite")

        # Build a stub ctx and execute the emitted code as a Python module body.
        captured: list[tuple[str, str, float]] = []

        class StubCtx:
            def rule(self, nt: str, rhs: str, weight: float = 1.0) -> None:
                captured.append((nt, rhs, weight))

        namespace = {"ctx": StubCtx()}
        exec(compile(out, "<emitted>", "exec"), namespace)

        assert len(captured) == 2
        assert captured[0] == ("Sql-Stmt", "SELECT 1;", 2.0)
        assert captured[1][0] == "Sql-Stmt"
        assert captured[1][2] == 3.0
        assert 'SELECT "a";' in captured[1][1]
        assert "DROP TABLE t;" in captured[1][1]


# ---------------------------------------------------------------------------
# Ordering
# ---------------------------------------------------------------------------


class TestOrdering:
    def test_bugs_sorted_by_section_then_number(self) -> None:
        bugs = [
            make_bug(id="A", section="fixed", number=2),
            make_bug(id="B", section="confirmed", number=1),
            make_bug(id="C", section="fixed", number=1),
        ]
        out = emit_nautilus(bugs, dbms="sqlite")
        idx_a = out.index("=== A ")
        idx_b = out.index("=== B ")
        idx_c = out.index("=== C ")
        # confirmed < fixed alphabetically; then number ascending
        assert idx_b < idx_c < idx_a
