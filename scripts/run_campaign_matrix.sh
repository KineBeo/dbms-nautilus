#!/usr/bin/env bash
# run_campaign_matrix.sh — Run bandit vs uniform across all 4 SQLite versions
#
# Usage:
#   ./scripts/run_campaign_matrix.sh
#
# Environment variables:
#   DURATION    seconds per run (default: 1800 = 30 min)
#   RUNS        number of runs per (version, policy) pair (default: 5)
#   VERSIONS    space-separated list of versions (default: all 4)
#   POLICIES    space-separated list of policies (default: "uniform bandit")

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DURATION="${DURATION:-1800}"
RUNS="${RUNS:-5}"
VERSIONS="${VERSIONS:-sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2}"
POLICIES="${POLICIES:-uniform bandit}"
GRAMMAR="$ROOT/grammars/active/sqlite_v3.py"

TOTAL=0
for v in $VERSIONS; do for p in $POLICIES; do for r in $(seq 1 $RUNS); do TOTAL=$((TOTAL+1)); done; done; done

echo "=============================================="
echo " Campaign Matrix"
echo "=============================================="
echo " Duration:   ${DURATION}s per run"
echo " Runs:       $RUNS per (version, policy)"
echo " Versions:   $VERSIONS"
echo " Policies:   $POLICIES"
echo " Total runs: $TOTAL"
echo " Est. time:  $(( TOTAL * DURATION / 60 )) minutes"
echo "=============================================="
echo ""

COMPLETED=0
FAILED=0
START_ALL=$(date +%s)

for VERSION in $VERSIONS; do
    for POLICY in $POLICIES; do
        for RUN_NUM in $(seq 1 $RUNS); do
            RUN_ID="${POLICY}_run${RUN_NUM}"
            COMPLETED=$((COMPLETED+1))

            ELAPSED_ALL=$(( $(date +%s) - START_ALL ))
            echo "[$COMPLETED/$TOTAL] $VERSION / $POLICY / run$RUN_NUM (elapsed: ${ELAPSED_ALL}s)"

            if DURATION="$DURATION" \
               POLICY="$POLICY" \
               GRAMMAR="$GRAMMAR" \
               GRAMMAR_VERSION="v3.2-${POLICY}" \
               bash "$SCRIPT_DIR/run_eval.sh" "$VERSION" "$RUN_ID" > "/tmp/campaign_${VERSION}_${RUN_ID}.log" 2>&1; then

                WORKDIR="$ROOT/workdirs/${VERSION}_${RUN_ID}"
                EDGES=$(tail -1 "$WORKDIR/coverage.csv" 2>/dev/null | cut -d, -f2 || echo "?")
                CRASHES=$(ls "$WORKDIR/outputs/signaled/" 2>/dev/null | wc -l)
                echo "  -> edges=$EDGES crashes=$CRASHES"
            else
                echo "  -> FAILED (check /tmp/campaign_${VERSION}_${RUN_ID}.log)"
                FAILED=$((FAILED+1))
            fi
        done
    done
done

END_ALL=$(date +%s)
TOTAL_TIME=$(( END_ALL - START_ALL ))

echo ""
echo "=============================================="
echo " Campaign Matrix Complete"
echo "=============================================="
echo " Total time: ${TOTAL_TIME}s ($(( TOTAL_TIME / 60 )) min)"
echo " Completed:  $COMPLETED"
echo " Failed:     $FAILED"
echo "=============================================="

echo ""
echo "Results in workdirs/. Run analysis with:"
echo "  python3 scripts/compare_campaigns.py"
