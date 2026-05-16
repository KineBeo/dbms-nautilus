#!/usr/bin/env bash
# run_comparison.sh — Run comparison campaigns: 2 grammars × 2 versions × N runs
#
# Usage:
#   ./scripts/run_comparison.sh
#   DURATION=300 RUNS=2 ./scripts/run_comparison.sh   # quick test
#
# Env overrides:
#   DURATION    seconds per run (default: 900 = 15 min)
#   RUNS        runs per (grammar, version) pair (default: 5)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

DURATION="${DURATION:-900}"
RUNS="${RUNS:-5}"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

declare -A GRAMMARS=(
    [v3.4]="$ROOT/grammars/v3.4/sqlite_v3.py"
    [ebnf]="$ROOT/grammars/baseline/sqlite-ebnf.py"
)

VERSIONS=("sqlite-3.30.1" "sqlite-3.31.1" "sqlite-3.32.0" "sqlite-3.32.2")

TOTAL=$((2 * ${#VERSIONS[@]} * RUNS))
CURRENT=0
START_ALL=$(date +%s)

echo "=============================================="
echo " Comparison Campaign Suite"
echo " Grammars: v3.4 (active) vs ebnf (baseline)"
echo " Versions: ${VERSIONS[*]}"
echo " Runs:     $RUNS per pair"
echo " Duration: ${DURATION}s per campaign"
echo " Total:    $TOTAL campaigns"
echo " Est time: $(( TOTAL * DURATION / 60 )) minutes"
echo "=============================================="

mkdir -p "$ROOT/results/comparison"

for GRAMMAR_NAME in v3.4 ebnf; do
    GRAMMAR="${GRAMMARS[$GRAMMAR_NAME]}"
    for VERSION in "${VERSIONS[@]}"; do
        for RUN_N in $(seq 1 "$RUNS"); do
            CURRENT=$((CURRENT + 1))
            RUN_ID="comparison_${GRAMMAR_NAME}_run${RUN_N}"

            echo ""
            echo "[$CURRENT/$TOTAL] $GRAMMAR_NAME / $VERSION / run $RUN_N"
            echo "  Grammar: $GRAMMAR"
            echo "  Started: $(date +%H:%M:%S)"

            GRAMMAR="$GRAMMAR" \
            DURATION="$DURATION" \
            GRAMMAR_VERSION="$GRAMMAR_NAME" \
            EXPERIMENT_TAG="comparison" \
              "$SCRIPT_DIR/run_eval.sh" "$VERSION" "$RUN_ID" \
              2>&1 | tail -5

            echo "  Finished: $(date +%H:%M:%S)"
        done
    done
done

END_ALL=$(date +%s)
ELAPSED_ALL=$((END_ALL - START_ALL))

echo ""
echo "=============================================="
echo " All $TOTAL campaigns complete"
echo " Total wall time: $((ELAPSED_ALL / 60))m $((ELAPSED_ALL % 60))s"
echo "=============================================="
echo ""
echo "Next: python3 scripts/collect_metrics.py"
