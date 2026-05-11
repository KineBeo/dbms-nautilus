#!/usr/bin/env python3
"""Analyze per-rule attribution from exec.log.

Usage: python3 scripts/analyze_attribution.py <workdir> [--grammar <grammar.py>]

Reads exec.log with format: exec_count\tstrategy:event\tR{id}\tSQL_snippet
Produces a report showing which grammar rules find coverage and crashes.
"""
import sys
import os
from collections import defaultdict, Counter
from pathlib import Path


def load_rule_map(grammar_path: str) -> dict[int, tuple[str, float]]:
    """Parse grammar file to map rule IDs to (display_name, weight)."""
    rule_map = {}
    rule_id = 0

    class FakeCtx:
        def rule(self, nt, fmt, weight=1.0):
            nonlocal rule_id
            import re
            nts_in_fmt = re.findall(r'\{([^}]+)\}', fmt)
            if nt == "Sql-Stmt" and nts_in_fmt:
                display = nts_in_fmt[0]
            else:
                display = nt
            rule_map[rule_id] = (display, weight)
            rule_id += 1

        def script(self, nt, fmt, func):
            nonlocal rule_id
            rule_map[rule_id] = (nt + ":script", 1.0)
            rule_id += 1

        def regex(self, nt, regex):
            nonlocal rule_id
            rule_map[rule_id] = (nt + ":regex", 1.0)
            rule_id += 1

    ctx = FakeCtx()
    exec(open(grammar_path).read(), {"ctx": ctx})
    return rule_map


def parse_exec_log(log_path: str):
    """Parse exec.log into structured entries."""
    entries = []
    with open(log_path) as f:
        for line in f:
            line = line.rstrip("\n")
            parts = line.split("\t", 3)
            if len(parts) < 3:
                continue
            exec_count = int(parts[0])
            strategy_event = parts[1]
            rule_tag = parts[2]
            sql = parts[3] if len(parts) > 3 else ""

            strategy, event = strategy_event.split(":", 1)
            rule_id = int(rule_tag[1:]) if rule_tag.startswith("R") else -1

            entries.append({
                "exec": exec_count,
                "strategy": strategy,
                "event": event,
                "rule_id": rule_id,
                "sql": sql,
            })
    return entries


def analyze(entries, rule_map):
    """Produce attribution analysis."""
    rule_cov = Counter()
    rule_crash = Counter()
    rule_timeout = Counter()
    strategy_cov = Counter()
    strategy_crash = Counter()
    rule_strategy_cov = defaultdict(Counter)
    rule_first_cov = {}
    rule_first_crash = {}

    for e in entries:
        rid = e["rule_id"]
        strat = e["strategy"]
        ev = e["event"]

        if ev == "NEW_COV":
            rule_cov[rid] += 1
            strategy_cov[strat] += 1
            rule_strategy_cov[rid][strat] += 1
            if rid not in rule_first_cov:
                rule_first_cov[rid] = e["exec"]
        elif ev.startswith("SIGNAL") or ev.startswith("ASAN") or ev.startswith("UBSAN"):
            rule_crash[rid] += 1
            strategy_crash[strat] += 1
            if rid not in rule_first_crash:
                rule_first_crash[rid] = e["exec"]
        elif ev == "TIMEOUT":
            rule_timeout[rid] += 1

    return {
        "rule_cov": rule_cov,
        "rule_crash": rule_crash,
        "rule_timeout": rule_timeout,
        "strategy_cov": strategy_cov,
        "strategy_crash": strategy_crash,
        "rule_strategy_cov": rule_strategy_cov,
        "rule_first_cov": rule_first_cov,
        "rule_first_crash": rule_first_crash,
    }


def format_report(analysis, rule_map, total_entries):
    lines = []
    lines.append("# Per-Rule Attribution Report")
    lines.append(f"\nTotal log entries: {total_entries}")
    lines.append("")

    lines.append("## Strategy Summary")
    lines.append(f"{'Strategy':<12} {'NEW_COV':>8} {'Crashes':>8}")
    lines.append("-" * 30)
    all_strats = sorted(
        set(list(analysis["strategy_cov"].keys()) + list(analysis["strategy_crash"].keys()))
    )
    for s in all_strats:
        lines.append(f"{s:<12} {analysis['strategy_cov'].get(s,0):>8} {analysis['strategy_crash'].get(s,0):>8}")

    lines.append("")
    lines.append("## Per-Rule Attribution (Sql-Stmt level)")
    lines.append(f"{'Rule':<6} {'Name':<30} {'W':>4} {'COV':>5} {'Crash':>6} {'1st COV':>8} {'1st Crash':>10}")
    lines.append("-" * 75)

    all_rules = sorted(set(list(analysis["rule_cov"].keys()) + list(analysis["rule_crash"].keys())))
    rows = []
    for rid in all_rules:
        nt_name, weight = rule_map.get(rid, (f"?R{rid}", 0.0))
        cov = analysis["rule_cov"].get(rid, 0)
        crash = analysis["rule_crash"].get(rid, 0)
        first_cov = analysis["rule_first_cov"].get(rid, "")
        first_crash = analysis["rule_first_crash"].get(rid, "")
        rows.append((rid, nt_name, weight, cov, crash, first_cov, first_crash))

    rows.sort(key=lambda r: -(r[3] + r[4]))
    for rid, name, w, cov, crash, fc, fcrash in rows:
        fc_str = str(fc) if fc != "" else "-"
        fcrash_str = str(fcrash) if fcrash != "" else "-"
        lines.append(f"R{rid:<5} {name:<30} {w:>4.1f} {cov:>5} {crash:>6} {fc_str:>8} {fcrash_str:>10}")

    lines.append("")
    lines.append("## Top Rules by Coverage (with strategy breakdown)")
    top_cov = sorted(analysis["rule_cov"].items(), key=lambda x: -x[1])[:10]
    for rid, count in top_cov:
        nt_name, _ = rule_map.get(rid, (f"?R{rid}", 0.0))
        strats = analysis["rule_strategy_cov"].get(rid, {})
        strat_str = ", ".join(f"{s}={c}" for s, c in sorted(strats.items(), key=lambda x: -x[1]))
        lines.append(f"  R{rid} {nt_name}: {count} COV — {strat_str}")

    lines.append("")
    lines.append("## Top Rules by Crashes")
    top_crash = sorted(analysis["rule_crash"].items(), key=lambda x: -x[1])[:10]
    for rid, count in top_crash:
        nt_name, weight = rule_map.get(rid, (f"?R{rid}", 0.0))
        lines.append(f"  R{rid} {nt_name} (w={weight:.1f}): {count} crashes")

    lines.append("")
    lines.append("## Dead Rules (no COV, no crashes)")
    dead = []
    for rid, (nt_name, weight) in rule_map.items():
        if nt_name == "Sql-Stmt" and rid not in analysis["rule_cov"] and rid not in analysis["rule_crash"]:
            dead.append((rid, nt_name, weight))
    if dead:
        for rid, name, w in sorted(dead):
            lines.append(f"  R{rid} {name} (w={w:.1f}) — NEVER OBSERVED")
    else:
        lines.append("  (none — all Sql-Stmt rules observed)")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <workdir> [--grammar <grammar.py>]", file=sys.stderr)
        sys.exit(1)

    workdir = sys.argv[1]
    grammar_path = None
    if "--grammar" in sys.argv:
        idx = sys.argv.index("--grammar")
        grammar_path = sys.argv[idx + 1]

    if grammar_path is None:
        script_dir = Path(__file__).parent.parent
        grammar_path = str(script_dir / "grammars" / "sqlite_patterns.py")

    log_path = os.path.join(workdir, "exec.log")
    if not os.path.exists(log_path):
        print(f"Error: {log_path} not found", file=sys.stderr)
        sys.exit(1)

    rule_map = load_rule_map(grammar_path)
    entries = parse_exec_log(log_path)
    analysis = analyze(entries, rule_map)
    report = format_report(analysis, rule_map, len(entries))

    print(report)

    report_path = os.path.join(workdir, "attribution_report.txt")
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\nReport saved to: {report_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
