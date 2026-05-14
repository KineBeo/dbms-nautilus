#!/usr/bin/env python3
"""
EBNF-to-Nautilus Grammar Converter

Reads a tree-sitter EBNF grammar specification and produces a Nautilus
ctx.rule() Python grammar via standard EBNF-to-CFG flattening.

Algorithm (Aho et al., Compilers, 2nd ed., §4.2):
    A?     → ε | A                    (optional → 2 alternatives)
    A*     → ε | A | A A              (Kleene star → capped recursion)
    A+     → A | A A                  (Kleene plus → capped recursion)
    (A|B)  → separate rule per alt    (alternation → enumerate)
    A B    → cartesian product        (sequence → combine expansions)

Three-stage pipeline:
    1. EBNF Parser     — .ebnf file → AST per production
    2. CFG Flattener   — AST → flat (NT, body) pairs
    3. Nautilus Emitter — (NT, body) → ctx.rule() calls + domain config

Usage:
    python3 scripts/ebnf_to_nautilus.py EBNF_FILE -c CONFIG -o OUTPUT
    python3 scripts/ebnf_to_nautilus.py --diff FILE_A FILE_B
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from itertools import product as cartesian
from typing import TextIO


# ===================================================================
# Stage 1: EBNF Parser — .ebnf text → AST
# ===================================================================

@dataclass
class Literal:
    text: str

@dataclass
class NonTerminal:
    name: str

@dataclass
class Optional:
    inner: "Element"

@dataclass
class Repeat:
    inner: "Element"

@dataclass
class RepeatOne:
    inner: "Element"

@dataclass
class Group:
    alternatives: list["Element"]

@dataclass
class Sequence:
    elements: list["Element"]

Element = Literal | NonTerminal | Optional | Repeat | RepeatOne | Group | Sequence


@dataclass
class Production:
    name: str
    alternatives: list[Element]


class EBNFTokenizer:
    """Tokenize an EBNF production body into a stream of tokens."""

    TOKEN_RE = re.compile(r"""
        (?P<LPAREN>\()      |
        (?P<RPAREN>\))      |
        (?P<LBRACK>\[)      |  # character class start
        (?P<QMARK>\?)       |
        (?P<STAR>\*)        |
        (?P<PLUS>\+)        |
        (?P<PIPE>\|)        |
        (?P<SQUOTE>'[^']*') |  # single-quoted string
        (?P<DQUOTE>"[^"]*") |  # double-quoted string
        (?P<IDENT>[_a-zA-Z][_a-zA-Z0-9]*) |
        (?P<WS>\s+)
    """, re.VERBOSE)

    def __init__(self, text: str):
        self.tokens: list[tuple[str, str]] = []
        pos = 0
        while pos < len(text):
            m = self.TOKEN_RE.match(text, pos)
            if not m:
                pos += 1
                continue
            for kind, val in m.groupdict().items():
                if val is not None and kind != "WS":
                    if kind == "LBRACK":
                        end = text.find("]", pos)
                        if end == -1:
                            end = len(text)
                        char_class = text[pos:end + 1]
                        self.tokens.append(("CHARCLASS", char_class))
                        pos = end + 1
                        break
                    self.tokens.append((kind, val))
                    break
            else:
                pos = m.end()
                continue
            if m.groupdict().get("LBRACK") is not None:
                continue
            pos = m.end()
        self.pos = 0

    def peek(self) -> tuple[str, str] | None:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def next(self) -> tuple[str, str] | None:
        tok = self.peek()
        if tok:
            self.pos += 1
        return tok

    def expect(self, kind: str) -> str:
        tok = self.next()
        if tok is None or tok[0] != kind:
            raise SyntaxError(f"Expected {kind}, got {tok}")
        return tok[1]


class EBNFParser:
    """Parse EBNF production bodies into AST elements."""

    def parse_production_body(self, text: str) -> list[Element]:
        tokenizer = EBNFTokenizer(text)
        return self._parse_alternatives(tokenizer)

    def _parse_alternatives(self, tok: EBNFTokenizer) -> list[Element]:
        alts = [self._parse_sequence(tok)]
        while tok.peek() and tok.peek()[0] == "PIPE":
            tok.next()
            alts.append(self._parse_sequence(tok))
        return alts

    def _parse_sequence(self, tok: EBNFTokenizer) -> Element:
        elements: list[Element] = []
        while tok.peek() and tok.peek()[0] not in ("PIPE", "RPAREN"):
            elements.append(self._parse_postfix(tok))
        if len(elements) == 1:
            return elements[0]
        return Sequence(elements)

    def _parse_postfix(self, tok: EBNFTokenizer) -> Element:
        elem = self._parse_atom(tok)
        while tok.peek() and tok.peek()[0] in ("QMARK", "STAR", "PLUS"):
            op = tok.next()[0]
            if op == "QMARK":
                elem = Optional(elem)
            elif op == "STAR":
                elem = Repeat(elem)
            elif op == "PLUS":
                elem = RepeatOne(elem)
        return elem

    def _parse_atom(self, tok: EBNFTokenizer) -> Element:
        t = tok.peek()
        if t is None:
            raise SyntaxError("Unexpected end of input")

        if t[0] == "LPAREN":
            tok.next()
            alts = self._parse_alternatives(tok)
            if tok.peek() and tok.peek()[0] == "RPAREN":
                tok.next()
            if len(alts) == 1:
                return alts[0]
            return Group(alts)

        if t[0] in ("SQUOTE", "DQUOTE"):
            tok.next()
            text = t[1][1:-1]
            return Literal(text)

        if t[0] == "CHARCLASS":
            tok.next()
            return Literal(t[1])

        if t[0] == "IDENT":
            tok.next()
            return NonTerminal(t[1])

        raise SyntaxError(f"Unexpected token: {t}")


def parse_ebnf_file(filepath: str) -> dict[str, Production]:
    """Parse an EBNF file into a dict of productions."""
    with open(filepath) as f:
        content = f.read()

    productions: dict[str, Production] = {}
    parser = EBNFParser()

    prod_re = re.compile(r'^([_a-zA-Z][_a-zA-Z0-9]*)\s*::=\s*', re.MULTILINE)
    matches = list(prod_re.finditer(content))

    for i, m in enumerate(matches):
        name = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        body = content[start:end].strip()

        if not body:
            continue

        try:
            alts = parser.parse_production_body(body)
            productions[name] = Production(name, alts)
        except SyntaxError:
            pass

    return productions


# ===================================================================
# Stage 2: CFG Flattener — AST → flat rule bodies
# ===================================================================

def flatten(elem: Element, depth: int = 2) -> list[list[str]]:
    """
    Expand an AST element into all possible flat token sequences.

    Returns a list of alternatives, where each alternative is a list of
    string tokens (literals or {NT-Name} references).
    """
    if isinstance(elem, Literal):
        return [[elem.text]]

    if isinstance(elem, NonTerminal):
        return [[elem.name]]

    if isinstance(elem, Optional):
        inner = flatten(elem.inner, depth)
        return [[]] + inner

    if isinstance(elem, Repeat):
        if depth <= 0:
            return [[]]
        inner = flatten(elem.inner, depth - 1)
        result = [[]]
        result.extend(inner)
        if depth >= 2:
            for a in inner:
                for b in inner:
                    result.append(a + b)
        return result

    if isinstance(elem, RepeatOne):
        inner = flatten(elem.inner, depth)
        result = list(inner)
        if depth >= 2:
            for a in inner:
                for b in inner:
                    result.append(a + b)
        return result

    if isinstance(elem, Group):
        result = []
        for alt in elem.alternatives:
            result.extend(flatten(alt, depth))
        return result

    if isinstance(elem, Sequence):
        expanded = [flatten(e, depth) for e in elem.elements]
        result = []
        for combo in cartesian(*expanded):
            merged: list[str] = []
            for tokens in combo:
                merged.extend(tokens)
            result.append(merged)
        return result

    return [[]]


def flatten_production(prod: Production, max_expansions: int = 64) -> list[list[str]]:
    """Flatten all alternatives of a production, with explosion guard."""
    all_rules: list[list[str]] = []
    for alt in prod.alternatives:
        expansions = flatten(alt)
        all_rules.extend(expansions)
        if len(all_rules) > max_expansions:
            all_rules = all_rules[:max_expansions]
            break
    seen: set[tuple[str, ...]] = set()
    deduped: list[list[str]] = []
    for rule in all_rules:
        key = tuple(rule)
        if key not in seen and key != ():
            seen.add(key)
            deduped.append(rule)
    return deduped


# ===================================================================
# Stage 3: Nautilus Emitter — flat rules → ctx.rule() calls
# ===================================================================

def snake_to_kebab(name: str) -> str:
    """Convert snake_case to Kebab-Case, strip leading underscore."""
    clean = name.lstrip("_")
    return "-".join(w.capitalize() for w in clean.split("_"))


def is_keyword_production(name: str) -> bool:
    """ALL_CAPS names are keyword terminals in tree-sitter EBNF."""
    return name == name.upper() and name.isalpha()


def tokens_to_body(tokens: list[str], config: dict) -> str | None:
    """Convert a list of flat tokens into a Nautilus rule body string."""
    parts: list[str] = []
    schema = config.get("schema", {})

    for tok in tokens:
        if is_keyword_production(tok):
            parts.append(tok)
        elif tok.startswith("["):
            return None
        elif tok.startswith("'") or tok.startswith('"'):
            inner = tok[1:-1] if len(tok) >= 2 else tok
            if inner:
                parts.append(inner)
        elif tok.startswith("_") or (tok and tok[0].islower()):
            if tok in schema:
                entry = schema[tok]
                if entry.get("type") == "skip":
                    return None
                nt = entry.get("nt", snake_to_kebab(tok))
                parts.append("{" + nt + "}")
            else:
                parts.append("{" + snake_to_kebab(tok) + "}")
        else:
            parts.append(tok)

    body = " ".join(parts)
    if not body.strip():
        return None
    return body


def emit_grammar(
    productions: dict[str, Production],
    config: dict,
    out: TextIO,
) -> None:
    """Emit Nautilus grammar from parsed EBNF productions."""
    skip_set = set(config.get("skip_productions", []))
    max_exp = config.get("max_expansions_per_production", 64)
    schema = config.get("schema", {})

    out.write("# SQLite EBNF Baseline Grammar for Nautilus (auto-generated)\n")
    out.write("# Produced by ebnf_to_nautilus.py — EBNF-to-CFG flattening algorithm.\n")
    out.write("# Algorithm: Aho et al., Compilers (2nd ed.), Section 4.2.\n")
    out.write("#\n")
    out.write("# Fixed schema (harness pre-loads):\n")
    out.write("#   CREATE TABLE t1(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL)\n")
    out.write("#   CREATE TABLE t2(c1 INTEGER, c2 TEXT, c3 REAL)\n")
    out.write("#   CREATE TABLE t3(c1 INTEGER, c2 TEXT NOT NULL, c3 REAL DEFAULT 0.0)\n")
    out.write("#   CREATE VIRTUAL TABLE fts_t1 USING fts5(c1, c2)\n")
    out.write("#   CREATE VIRTUAL TABLE fts_t2 USING fts3(c1, c2)\n\n")
    out.write('# START\n')
    out.write('ctx.rule("START", "{Sql-Stmt-List}")\n')

    emitted_nts: set[str] = set()

    for name, prod in productions.items():
        if is_keyword_production(name):
            continue
        if name in skip_set:
            continue

        nt = snake_to_kebab(name)
        if name in schema:
            entry = schema[name]
            typ = entry.get("type")
            if typ in ("skip", "alias", "fixed", "enum", "regex", "inline"):
                continue
            if entry.get("nt"):
                nt = entry["nt"]

        rules = flatten_production(prod, max_exp)
        if not rules:
            continue

        out.write(f"\n# {name}\n")
        for rule_tokens in rules:
            body = tokens_to_body(rule_tokens, config)
            if body is None:
                continue
            out.write(f'ctx.rule("{nt}", "{body}")\n')
            emitted_nts.add(nt)

    emit_terminal_overrides(config, out, emitted_nts)


def emit_terminal_overrides(config: dict, out: TextIO, emitted: set[str]) -> None:
    """Emit concrete terminal rules from config (tables, columns, types, etc.)."""
    schema = config.get("schema", {})

    out.write("\n# ============================================================\n")
    out.write("# Terminal overrides from harness config\n")
    out.write("# ============================================================\n")

    tables = config.get("harness_tables", [])
    if tables:
        for t in tables:
            out.write(f'ctx.rule("Table-Name", "{t}")\n')

    columns = config.get("harness_columns", [])
    if columns:
        for c in columns:
            out.write(f'ctx.rule("Col-Name", "{c}")\n')
        out.write('ctx.rule("Col-Ref", "{Col-Name}")\n')
        out.write('ctx.rule("Col-Ref", "{Table-Name}.{Col-Name}")\n')

    for prod_name, entry in schema.items():
        if entry.get("type") == "regex":
            if "patterns" in entry:
                for nt, pat in entry["patterns"].items():
                    pat_esc = pat.replace("\\", "\\\\")
                    out.write(f'ctx.regex("{nt}", "{pat_esc}")\n')
            elif "pattern" in entry:
                nt = entry.get("nt", snake_to_kebab(prod_name))
                pat = entry["pattern"].replace("\\", "\\\\")
                out.write(f'ctx.regex("{nt}", "{pat}")\n')
        elif entry.get("type") == "enum":
            nt = entry.get("nt", snake_to_kebab(prod_name))
            for val in entry["values"]:
                out.write(f'ctx.rule("{nt}", "{val}")\n')
        elif entry.get("type") == "fixed":
            pass

    # Alias resolution: produce rules for alias NTs pointing to their targets
    for prod_name, entry in schema.items():
        if entry.get("type") == "alias":
            nt = entry.get("nt", snake_to_kebab(prod_name))
            target = entry["target"]
            target_nt = schema.get(target, {}).get("nt", snake_to_kebab(target))
            out.write(f'ctx.rule("{nt}", "{{{target_nt}}}")\n')

    # Name NT (maps to Table-Name for single-DB harness)
    out.write('\n# _name → Table-Name (single-DB harness)\n')
    out.write('ctx.rule("Name", "{Table-Name}")\n')
    out.write('ctx.rule("Name", "{Col-Name}")\n')

    # Pragma-Value
    out.write('\n# pragma_value\n')
    out.write('ctx.rule("Pragma-Value", "{Signed-Number}")\n')
    out.write('ctx.rule("Pragma-Value", "{Name}")\n')

    # Numeric-Literal → Int or Float
    out.write('\n# numeric_literal\n')
    out.write('ctx.rule("Numeric-Literal", "{Int-Literal}")\n')
    out.write('ctx.rule("Numeric-Literal", "{Float-Literal}")\n')

    types = ["INTEGER", "REAL", "TEXT", "BLOB", "NUMERIC", "INT",
             "VARCHAR(255)", "FLOAT", "BOOLEAN", "DATE"]
    out.write("\n# type_name\n")
    for t in types:
        out.write(f'ctx.rule("Type-Name", "{t}")\n')

    out.write("\n# literals\n")
    out.write('ctx.rule("Literal", "{Int-Literal}")\n')
    out.write('ctx.rule("Literal", "{Float-Literal}")\n')
    out.write('ctx.rule("Literal", "{Str-Literal}")\n')
    out.write('ctx.rule("Literal", "{Blob-Literal}")\n')
    for kw in ["NULL", "TRUE", "FALSE", "CURRENT_TIMESTAMP", "CURRENT_DATE", "CURRENT_TIME"]:
        out.write(f'ctx.rule("Literal", "{kw}")\n')

    out.write('\nctx.rule("Signed-Number", "{Int-Literal}")\n')
    out.write('ctx.rule("Signed-Number", "+{Int-Literal}")\n')
    out.write('ctx.rule("Signed-Number", "-{Int-Literal}")\n')


# ===================================================================
# Diff mode
# ===================================================================

def extract_rules(filepath: str) -> set[tuple[str, str]]:
    rules = set()
    with open(filepath) as f:
        content = f.read()
    for m in re.finditer(r'ctx\.rule\("([^"]+)",\s*"([^"]*)"', content):
        rules.add((m.group(1), m.group(2)))
    for m in re.finditer(r'ctx\.regex\("([^"]+)",\s*"([^"]*)"', content):
        rules.add((m.group(1), f"REGEX:{m.group(2)}"))
    return rules


def diff_grammars(path_a: str, path_b: str) -> None:
    rules_a = extract_rules(path_a)
    rules_b = extract_rules(path_b)

    only_a = sorted(rules_a - rules_b)
    only_b = sorted(rules_b - rules_a)

    print(f"File A ({path_a}): {len(rules_a)} rules")
    print(f"File B ({path_b}): {len(rules_b)} rules")
    print(f"In common: {len(rules_a & rules_b)} rules")
    print()

    if only_a:
        print(f"=== IN A ONLY ({len(only_a)}) ===")
        for nt, body in only_a:
            print(f'  + ctx.rule("{nt}", "{body[:80]}")')
        print()

    if only_b:
        print(f"=== IN B ONLY ({len(only_b)}) ===")
        for nt, body in only_b:
            print(f'  - ctx.rule("{nt}", "{body[:80]}")')
        print()

    if not only_a and not only_b:
        print("IDENTICAL.")


# ===================================================================
# Main
# ===================================================================

def main():
    parser = argparse.ArgumentParser(
        description="EBNF-to-Nautilus grammar converter (EBNF→CFG flattening)")
    parser.add_argument("ebnf_file", nargs="?", help="Path to .ebnf grammar file")
    parser.add_argument("-c", "--config", help="Path to harness config JSON")
    parser.add_argument("-o", "--output", help="Output .py file (default: stdout)")
    parser.add_argument("--diff", nargs=2, metavar=("A", "B"),
                        help="Diff two .py grammar files")
    parser.add_argument("--stats", action="store_true",
                        help="Print parsing stats instead of emitting grammar")
    args = parser.parse_args()

    if args.diff:
        diff_grammars(args.diff[0], args.diff[1])
        return

    if not args.ebnf_file:
        parser.error("EBNF file required (unless using --diff)")

    productions = parse_ebnf_file(args.ebnf_file)

    if args.stats:
        structural = {k: v for k, v in productions.items() if not is_keyword_production(k)}
        keywords = {k: v for k, v in productions.items() if is_keyword_production(k)}
        print(f"Total productions: {len(productions)}")
        print(f"  Keywords (ALL_CAPS): {len(keywords)}")
        print(f"  Structural: {len(structural)}")
        print()
        for name, prod in sorted(structural.items()):
            n_alts = len(prod.alternatives)
            flat = flatten_production(prod, 64)
            print(f"  {name:40s} {n_alts:2d} alts → {len(flat):3d} flat rules")
        return

    config = {}
    if args.config:
        with open(args.config) as f:
            config = json.load(f)

    if args.output:
        with open(args.output, "w") as f:
            emit_grammar(productions, config, f)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        emit_grammar(productions, config, sys.stdout)


if __name__ == "__main__":
    main()
