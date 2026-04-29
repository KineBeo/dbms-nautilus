#!/usr/bin/env python3
"""Compare campaigns within an experiment for thesis tables.

Usage:
    python3 scripts/compare_campaigns.py <experiment-tag>
    python3 scripts/compare_campaigns.py <experiment-tag> --latex
    python3 scripts/compare_campaigns.py --list
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_experiments(root: Path) -> dict:
    path = root / "results" / "experiments.json"
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(path) as f:
        return json.load(f)


def load_campaign(root: Path, campaign_id: str) -> dict | None:
    path = root / "results" / "campaigns" / campaign_id / "campaign.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def format_duration(seconds: int) -> str:
    if seconds >= 86400:
        return f"{seconds // 86400}d"
    if seconds >= 3600:
        return f"{seconds // 3600}h"
    return f"{seconds // 60}m"


def shorten_id(campaign_id: str) -> str:
    parts = campaign_id.split("_")
    if len(parts) >= 5:
        return f"...{parts[-2]}_{parts[-1]}"
    return campaign_id


def render_markdown(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"## Experiment: {tag}")
    lines.append(f"**Hypothesis:** {experiment['hypothesis']}")
    lines.append("")

    if not campaigns:
        lines.append("*No archived campaigns yet.*")
        if experiment.get("conclusion"):
            lines.append(f"\n**Conclusion:** {experiment['conclusion']}")
        return "\n".join(lines)

    has_classification = any(
        c.get("results", {}).get("crash_classification") for c in campaigns
    )

    headers = ["Campaign", "Grammar", "Target", "Duration", "Crashes", "Queue", "Executions", "Unique RC"]
    if has_classification:
        headers += ["ASan", "UBSan", "Assert", "Signal"]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("total_executions", "?") or "?"),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        if has_classification:
            cc = r.get("crash_classification", {})
            row += [
                str(cc.get("asan", "—")),
                str(cc.get("ubsan", "—")),
                str(cc.get("debug_assert", "—")),
                str(cc.get("signal", "—")),
            ]
        lines.append("| " + " | ".join(row) + " |")

    conclusion = experiment.get("conclusion")
    if conclusion:
        lines.append(f"\n**Conclusion:** {conclusion}")
    else:
        lines.append("\n**Conclusion:** *pending*")

    return "\n".join(lines)


def render_latex(tag: str, experiment: dict, campaigns: list[dict]) -> str:
    lines = []
    lines.append(f"% Experiment: {tag}")
    lines.append(f"% Hypothesis: {experiment['hypothesis']}")

    has_classification = any(
        c.get("results", {}).get("crash_classification") for c in campaigns
    )

    col_spec = "lllrrrrr" + ("rrrr" if has_classification else "")
    lines.append("\\begin{table}[h]")
    lines.append("\\centering")
    lines.append(f"\\caption{{Experiment: {tag}}}")
    lines.append(f"\\begin{{tabular}}{{{col_spec}}}")
    lines.append("\\toprule")

    header = "Campaign & Grammar & Target & Duration & Crashes & Queue & Executions & Unique RC"
    if has_classification:
        header += " & ASan & UBSan & Assert & Signal"
    lines.append(header + " \\\\")
    lines.append("\\midrule")

    for c in campaigns:
        r = c.get("results", {})
        row = [
            shorten_id(c["id"]).replace("_", "\\_"),
            c.get("grammar_version", "?"),
            c.get("target", "?").replace("sqlite-", ""),
            format_duration(c.get("duration_seconds", 0)),
            str(r.get("crashes", "?")),
            str(r.get("queue_paths", "?")),
            str(r.get("total_executions", "?") or "?"),
            str(r.get("unique_root_causes", "?") or "?"),
        ]
        if has_classification:
            cc = r.get("crash_classification", {})
            row += [
                str(cc.get("asan", "--")),
                str(cc.get("ubsan", "--")),
                str(cc.get("debug_assert", "--")),
                str(cc.get("signal", "--")),
            ]
        lines.append(" & ".join(row) + " \\\\")

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    return "\n".join(lines)


def list_experiments(root: Path) -> None:
    experiments = load_experiments(root)
    print(f"{'Tag':<30} {'Campaigns':>10} {'Conclusion'}")
    print("-" * 80)
    for tag, exp in experiments.items():
        n = len(exp.get("campaigns", []))
        conclusion = exp.get("conclusion") or "pending"
        if len(conclusion) > 40:
            conclusion = conclusion[:37] + "..."
        print(f"{tag:<30} {n:>10} {conclusion}")


def main() -> None:
    root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description="Compare campaigns within an experiment")
    parser.add_argument("tag", nargs="?", help="Experiment tag from experiments.json")
    parser.add_argument("--latex", action="store_true", help="Output LaTeX table format")
    parser.add_argument("--list", action="store_true", help="List all experiments")
    args = parser.parse_args()

    if args.list:
        list_experiments(root)
        return

    if not args.tag:
        print("Error: provide an experiment tag, or use --list", file=sys.stderr)
        sys.exit(1)

    experiments = load_experiments(root)
    if args.tag not in experiments:
        print(f"Error: experiment '{args.tag}' not found in experiments.json", file=sys.stderr)
        print(f"Available: {', '.join(experiments.keys())}", file=sys.stderr)
        sys.exit(1)

    experiment = experiments[args.tag]
    campaign_ids = experiment.get("campaigns", [])

    campaigns = []
    for cid in campaign_ids:
        c = load_campaign(root, cid)
        if c:
            campaigns.append(c)
        else:
            print(f"Warning: campaign {cid} not found in results/campaigns/", file=sys.stderr)

    if args.latex:
        print(render_latex(args.tag, experiment, campaigns))
    else:
        print(render_markdown(args.tag, experiment, campaigns))


if __name__ == "__main__":
    main()
