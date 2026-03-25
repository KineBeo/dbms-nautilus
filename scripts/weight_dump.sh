#!/usr/bin/env bash
# weight_dump.sh — Dump grammar weights to JSON for observability
#
# Usage:
#   ./scripts/weight_dump.sh                        # prints to stdout
#   ./scripts/weight_dump.sh workdir/              # writes to workdir/grammar_weights.json
#
# Output format:
#   {
#     "nonterminal": "Sql-Stmt",
#     "rule": "{FTS-Stress}",
#     "weight": 3.5
#   }, ...
#
# This snapshot is taken at the start of each eval run by run_eval.sh.
# It lets you verify which weights were active for a given campaign.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTDIR="${1:-}"
# Allow caller to pass the grammar path as $2; fall back to sqlite.py
GRAMMAR="${2:-$ROOT/grammars/sqlite.py}"
# If path is relative, resolve from ROOT
if [[ "$GRAMMAR" != /* ]]; then
    GRAMMAR="$ROOT/$GRAMMAR"
fi

if [ ! -f "$GRAMMAR" ]; then
    echo "Error: grammar not found at $GRAMMAR" >&2
    exit 1
fi

# Parse weight= calls from the grammar using Python.
# Reads the grammar file directly — no need to load PyO3.
python3 - <<PYEOF
import re, json, sys

grammar_path = "$GRAMMAR"
entries = []

with open(grammar_path) as f:
    content = f.read()

# Match ctx.rule/ctx.script/ctx.regex calls with weight= argument
pattern = re.compile(
    r'ctx\.(rule|script|regex)\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*(?:,[^)]*)?weight\s*=\s*([0-9.]+)',
    re.MULTILINE
)

for m in pattern.finditer(content):
    kind, nterm, rule_text, weight = m.group(1), m.group(2), m.group(3), float(m.group(4))
    entries.append({
        "nonterminal": nterm,
        "rule": rule_text[:80],   # truncate long rules
        "weight": weight,
        "kind": kind,
    })

# Sort: by nonterminal, then descending weight
entries.sort(key=lambda e: (e["nonterminal"], -e["weight"]))

output = json.dumps(entries, indent=2)

outdir = "$OUTDIR"
if outdir:
    import os
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, "grammar_weights.json")
    with open(outfile, "w") as f:
        f.write(output)
    print(f"[weight_dump] wrote {len(entries)} rules to {outfile}", file=sys.stderr)
else:
    print(output)
PYEOF
