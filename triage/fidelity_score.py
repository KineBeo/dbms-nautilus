"""Per-pattern structural fidelity scorer.

For each pattern in the attack grammar, drives the Nautilus generator to
produce N samples biased toward that pattern's Sql-Stmt alternative, then
checks how many samples structurally match the CVE's required-node signature.

Output: fidelity-report.json matching spec §2.3 schema.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from triage import cve_signatures as sigs


def score_samples(samples: list[str], signature: dict) -> dict:
    n = len(samples)
    match_count = 0
    missing_counts: dict[str, int] = {label: 0 for label, _ in signature["required_patterns"]}
    for sql in samples:
        missing = sigs.missing_patterns(sql, signature)
        if not missing:
            match_count += 1
        for label in missing:
            missing_counts[label] += 1
    return {
        "pattern_name": signature["pattern_name"],
        "cve": signature["cve"],
        "samples_generated": n,
        "required_nodes": [label for label, _ in signature["required_patterns"]],
        "samples_with_all_required": match_count,
        "fidelity_score": (match_count / n) if n else 0.0,
        "samples_missing_node": missing_counts,
    }


def write_biased_grammar(base_grammar: Path, out: Path, target_pattern_nt: str, high_weight: float = 100.0) -> None:
    """Rewrite Sql-Stmt alternatives to bias toward the target pattern.

    Every ctx.rule("Sql-Stmt", "...") is rewritten: weight=high_weight for the
    target (matched by RHS == "{target_pattern_nt}"), weight=0 for everything
    else. Other rules are untouched.
    """
    lines_in = base_grammar.read_text().splitlines(keepends=False)
    lines_out: list[str] = []
    target_token = "{" + target_pattern_nt + "}"
    sqlstmt_re = re.compile(r'^\s*ctx\.rule\s*\(\s*"Sql-Stmt"\s*,\s*"([^"]+)"\s*\)\s*$')
    for line in lines_in:
        m = sqlstmt_re.match(line)
        if m:
            rhs = m.group(1)
            weight = high_weight if rhs == target_token else 0.0
            lines_out.append(f'ctx.rule("Sql-Stmt", "{rhs}", weight={weight})')
        else:
            lines_out.append(line)
    out.write_text("\n".join(lines_out) + "\n")


def run_generator(grammar: Path, samples: int, tree_size: int = 100) -> list[str]:
    """Invoke ./target/release/generator; split stdout into per-tree fragments."""
    cmd = [
        "./target/release/generator",
        "-g", str(grammar),
        "-t", str(tree_size),
        "-n", str(samples),
    ]
    env = os.environ.copy()
    env.setdefault("PYO3_USE_ABI3_FORWARD_COMPATIBILITY", "1")
    env.setdefault("LD_LIBRARY_PATH", "/home/linuxbrew/.linuxbrew/lib")
    env.setdefault("PYTHONPATH", str(Path.cwd()))
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=600)
    if proc.returncode != 0:
        raise RuntimeError(f"generator failed: {proc.stderr[:500]}")
    # Nautilus generator emits ONE tree per newline-terminated line, with
    # all statements inside a tree ';'-joined on that line. There is no
    # blank-line separator between trees. Each non-empty line is one sample.
    return [ln for ln in proc.stdout.splitlines() if ln.strip()]


def score_all_patterns(grammar: Path, samples: int) -> dict:
    reports: list[dict] = []
    for sig in sigs.all_cves():
        pattern_nt = sig["pattern_name"]
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False, dir=Path.cwd()) as tf:
            tmp_grammar = Path(tf.name)
        try:
            write_biased_grammar(grammar, tmp_grammar, pattern_nt)
            sqls = run_generator(tmp_grammar, samples)
            rep = score_samples(sqls, sig)
            reports.append(rep)
        finally:
            tmp_grammar.unlink(missing_ok=True)
    return {"patterns": reports}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--grammar", type=Path, default=Path("grammars/sqlite_attack.py"))
    p.add_argument("--samples", type=int, default=500)
    p.add_argument("--output", type=Path, default=Path("docs/fidelity-report.json"))
    args = p.parse_args(argv)
    report = score_all_patterns(args.grammar, args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2))
    for rep in report["patterns"]:
        print(f"{rep['pattern_name']:35s} fidelity={rep['fidelity_score']:.3f}  ({rep['samples_with_all_required']}/{rep['samples_generated']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
