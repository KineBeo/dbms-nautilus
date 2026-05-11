#!/usr/bin/env bash
# smoke_attack_grammar.sh — Pre-pilot gate for grammars/sqlite_attack.py.
#
# Checks:
#   1. Grammar loads via Nautilus generator (no Broken Grammar panic).
#   2. Generates N samples without panic.
#   3. At least 30% of samples parse cleanly as SQL by sqlite3 CLI
#      (semantic errors are fine; we only check syntactic acceptability).
#   4. Every attack pattern is observed at least once in the sample set.
#
# Usage:
#   ./scripts/smoke_attack_grammar.sh
#   SAMPLES=500 ./scripts/smoke_attack_grammar.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

GRAMMAR="grammars/sqlite_attack.py"
SAMPLES="${SAMPLES:-200}"
OUT_DIR="$(mktemp -d)"
trap 'rm -rf "$OUT_DIR"' EXIT

echo "== Step 1: Build generator =="
cargo build --release --bin generator 2>&1 | tail -5

echo "== Step 2: Generate $SAMPLES samples =="
# Note: do NOT pass -s. With -s, the Nautilus generator writes one file
# per tree to ./corpus/ and emits nothing to stdout, so the redirect
# below would capture an empty file. Omitting -s makes it unparse each
# tree to stdout, which is what we want to pipe into sqlite3.
./target/release/generator -g "$GRAMMAR" -t 100 -n "$SAMPLES" \
    > "$OUT_DIR/samples.txt"

sample_count=$(grep -c . "$OUT_DIR/samples.txt" || true)
echo "Generated $sample_count non-empty lines"
if [[ "$sample_count" -lt 50 ]]; then
    echo "FAIL: generator produced <50 samples"
    exit 1
fi

echo "== Step 3: Syntactic acceptability check via sqlite3 CLI =="
pass=0
fail=0
while IFS= read -r stmt; do
    [[ -z "$stmt" ]] && continue
    # Use :memory: DB, wrap in sqlite3's EXPLAIN to check parse without execute.
    # Exit 1 = parse error; we tolerate semantic errors (no such table, etc.).
    if output=$(sqlite3 ':memory:' "EXPLAIN $stmt" 2>&1); then
        ((pass+=1)) || true
    else
        if echo "$output" | grep -qiE 'syntax error|malformed|near "'; then
            ((fail+=1)) || true
        else
            # Semantic error is OK for syntactic smoke
            ((pass+=1)) || true
        fi
    fi
done < <(head -100 "$OUT_DIR/samples.txt")

total=$((pass + fail))
if [[ "$total" -eq 0 ]]; then total=1; fi
pct=$((pass * 100 / total))
echo "Syntactic pass rate: $pass / $total ($pct%)"
if [[ "$pct" -lt 30 ]]; then
    echo "FAIL: syntactic pass rate below 30% threshold"
    exit 1
fi

echo "== Step 4: Attack pattern presence check =="
for token in \
    "INTERSECT" \
    "EXCEPT" \
    "GENERATED ALWAYS AS" \
    "integrity_check" \
    "NATURAL JOIN" \
    "printf" \
    "group_concat" \
    "CREATE TRIGGER" \
; do
    if grep -q -- "$token" "$OUT_DIR/samples.txt"; then
        echo "  OK: '$token' observed"
    else
        echo "  FAIL: '$token' never generated in $SAMPLES samples"
        exit 1
    fi
done

echo ""
echo "SMOKE TEST PASSED"
