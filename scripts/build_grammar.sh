#!/usr/bin/env bash
# Render the Nautilus grammar from cve2grammar's committed cache entries.
#
# Reads cve2grammar/cache/generalizer/*.json, feeds the render CLI on stdin,
# and writes the output to grammars/sqlite_generated.py at the phase-2 root.
#
# Deterministic: same cache → identical output (modulo the header timestamp).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CVE2GRAMMAR_DIR="${REPO_ROOT}/cve2grammar"
OUTPUT="${REPO_ROOT}/grammars/sqlite_generated.py"

if [[ ! -d "${CVE2GRAMMAR_DIR}" ]]; then
  echo "error: cve2grammar subtree not found at ${CVE2GRAMMAR_DIR}" >&2
  exit 1
fi

# Collect all committed cache entries (skip .tmp sidecars) and pipe to renderer.
python3 -c "
import json, sys
from pathlib import Path
cache_dir = Path('${CVE2GRAMMAR_DIR}/cache/generalizer')
entries = []
for f in sorted(cache_dir.glob('*.json')):
    if f.suffix == '.tmp':
        continue
    with f.open() as fh:
        entries.append(json.load(fh))
json.dump(entries, sys.stdout)
" | (cd "${CVE2GRAMMAR_DIR}" && python3 -m cve2grammar.generalizer.render "${OUTPUT}")

echo "rendered: ${OUTPUT}"
