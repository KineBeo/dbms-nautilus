"""CLI for cve2grammar.

Two commands:

    cve2grammar fetch     --dbms sqlite -o sqlite_grammar.py
    cve2grammar dashboard                -o dashboard.html

`fetch` scrapes Manuel Rigger's DBMS bugs page, filters to one DBMS (and one
section), and emits a Nautilus-compatible grammar file.

`dashboard` scrapes the same page, keeps all DBMS, and emits a single
self-contained HTML file for triaging bugs.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cve2grammar.config import SUPPORTED_DBMS, SUPPORTED_SECTIONS
from cve2grammar.dashboard import emit_dashboard
from cve2grammar.emitter import emit_nautilus
from cve2grammar.scraper.manuelrigger import fetch


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "fetch":
        return _cmd_fetch(args)
    if args.cmd == "dashboard":
        return _cmd_dashboard(args)
    if args.cmd == "generalize-candidates":
        return _cmd_generalize_candidates(args)

    parser.print_help()
    return 1


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cve2grammar",
        description="Scrape Manuel Rigger DBMS bugs; emit Nautilus grammar or HTML dashboard.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    fetch_p = sub.add_parser(
        "fetch", help="Scrape MR bugs page and emit a grammar file in one shot."
    )
    fetch_p.add_argument(
        "--dbms", required=True, choices=SUPPORTED_DBMS,
        help="DBMS to extract bugs for.",
    )
    fetch_p.add_argument(
        "--section", default="fixed", choices=SUPPORTED_SECTIONS,
        help="MR section to include (default: fixed).",
    )
    fetch_p.add_argument(
        "--output", "-o", type=Path, required=True,
        help="Path to write the generated grammar .py file.",
    )
    fetch_p.add_argument(
        "--html", type=Path, default=None,
        help="Optional path to a pre-fetched HTML file (skips network).",
    )

    dash_p = sub.add_parser(
        "dashboard",
        help="Scrape MR bugs page and emit a single-file HTML triage dashboard.",
    )
    dash_p.add_argument(
        "--section", default="fixed", choices=SUPPORTED_SECTIONS,
        help="MR section to include (default: fixed).",
    )
    dash_p.add_argument(
        "--output", "-o", type=Path, required=True,
        help="Path to write the generated .html dashboard.",
    )
    dash_p.add_argument(
        "--html", type=Path, default=None,
        help="Optional path to a pre-fetched HTML file (skips network).",
    )

    gc_p = sub.add_parser(
        "generalize-candidates",
        help=(
            "Emit crash-oracle (or other) bugs as JSON for the generalizer "
            "slash command to consume."
        ),
    )
    gc_p.add_argument(
        "--oracle", default="crash",
        help="Oracle to filter by (default: crash).",
    )
    gc_p.add_argument(
        "--dbms", default=None, choices=SUPPORTED_DBMS,
        help="Optional DBMS filter (default: all).",
    )
    gc_p.add_argument(
        "--html", type=Path, default=None,
        help="Optional path to a pre-fetched HTML file (skips network).",
    )

    return parser


def _cmd_fetch(args: argparse.Namespace) -> int:
    html = args.html.read_text(encoding="utf-8") if args.html else None
    bugs = fetch(html=html)

    bugs = [b for b in bugs if b.dbms == args.dbms]
    if args.section != "all":
        bugs = [b for b in bugs if b.section == args.section]

    if not bugs:
        print(
            f"No bugs found for dbms={args.dbms} section={args.section}",
            file=sys.stderr,
        )
        return 1

    output = emit_nautilus(bugs, dbms=args.dbms)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")

    print(f"Wrote {len(bugs)} bugs ({args.dbms}/{args.section}) → {args.output}")
    return 0


def _cmd_dashboard(args: argparse.Namespace) -> int:
    html = args.html.read_text(encoding="utf-8") if args.html else None
    bugs = fetch(html=html)

    if args.section != "all":
        bugs = [b for b in bugs if b.section == args.section]

    if not bugs:
        print(
            f"No bugs found for section={args.section}",
            file=sys.stderr,
        )
        return 1

    output = emit_dashboard(bugs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")

    print(f"Wrote {len(bugs)} bugs (all DBMS / {args.section}) → {args.output}")
    return 0


def _cmd_generalize_candidates(args: argparse.Namespace) -> int:
    """Emit bugs matching --oracle (and optionally --dbms) as JSON to stdout."""
    import json as _json  # keep json import local to this subcommand

    html = args.html.read_text(encoding="utf-8") if args.html else None
    bugs = fetch(html=html)

    bugs = [b for b in bugs if b.oracle == args.oracle]
    if args.dbms is not None:
        bugs = [b for b in bugs if b.dbms == args.dbms]

    out = [
        {
            "id": b.id,
            "sql": b.sql,
            "title": b.title,
            "dbms": b.dbms,
            "oracle": b.oracle,
            "date": b.date_found,
        }
        for b in bugs
    ]
    print(_json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
