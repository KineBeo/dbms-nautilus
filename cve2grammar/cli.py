"""CLI for cve2grammar.

One command does the whole job:

    cve2grammar fetch --dbms sqlite -o sqlite_grammar.py

Scrapes Manuel Rigger's DBMS bugs page, filters to one DBMS (and one section),
and emits a Nautilus-compatible grammar file.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cve2grammar.config import SUPPORTED_DBMS, SUPPORTED_SECTIONS
from cve2grammar.emitter import emit_nautilus
from cve2grammar.scraper.manuelrigger import fetch


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "fetch":
        return _cmd_fetch(args)

    parser.print_help()
    return 1


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cve2grammar",
        description="Scrape Manuel Rigger DBMS bugs and emit Nautilus grammar.",
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


if __name__ == "__main__":
    raise SystemExit(main())
