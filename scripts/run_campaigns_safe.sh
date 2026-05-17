#!/usr/bin/env bash
# run_campaigns_safe.sh — Run all 30 comparison campaigns, 2 at a time
#
# Usage: ./scripts/run_campaigns_safe.sh
#
# Runs campaigns in pairs to avoid VM OOM. Each pair runs in parallel,
# then waits for both to finish before starting the next pair.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

DURATION="${DURATION:-900}"
LOG="$ROOT/campaign_progress.log"

run_one() {
    local grammar_path="$1"
    local grammar_version="$2"
    local version="$3"
    local run_id="$4"
    local workdir="$ROOT/workdirs/${version}_${run_id}"

    # Skip if already completed
    if [ -f "$workdir/triage_test.json" ]; then
        echo "[$(date +%H:%M:%S)] SKIP $grammar_version / $version / $run_id (already done)" | tee -a "$LOG"
        return 0
    fi

    # Clean incomplete workdir if exists
    if [ -d "$workdir" ]; then
        echo "[$(date +%H:%M:%S)] CLEAN incomplete $run_id" | tee -a "$LOG"
        rm -rf "$workdir"
    fi

    echo "[$(date +%H:%M:%S)] START $grammar_version / $version / $run_id" | tee -a "$LOG"
    DURATION="$DURATION" \
    GRAMMAR="$grammar_path" \
    GRAMMAR_VERSION="$grammar_version" \
    EXPERIMENT_TAG="comparison" \
        ./scripts/run_eval.sh "$version" "$run_id" 2>&1 | tail -3
    echo "[$(date +%H:%M:%S)] DONE  $grammar_version / $version / $run_id" | tee -a "$LOG"
}

# Build campaign list: (grammar_path, grammar_version, sqlite_version, run_id)
CAMPAIGNS=()

# v3.4 × 4 versions × 5 runs = 20
for VER in sqlite-3.30.1 sqlite-3.31.1 sqlite-3.32.0 sqlite-3.32.2; do
    for RUN in 1 2 3 4 5; do
        CAMPAIGNS+=("$ROOT/grammars/v3.4/sqlite_v3.py|v3.4|$VER|comparison_v3.4_run${RUN}")
    done
done

# EBNF × 2 missing versions × 5 runs = 10
for VER in sqlite-3.30.1 sqlite-3.32.0; do
    for RUN in 1 2 3 4 5; do
        CAMPAIGNS+=("$ROOT/grammars/baseline/sqlite-ebnf.py|ebnf|$VER|comparison_ebnf_run${RUN}")
    done
done

TOTAL=${#CAMPAIGNS[@]}
echo "======================================" | tee "$LOG"
echo " Safe Campaign Runner (2 parallel)" | tee -a "$LOG"
echo " Total: $TOTAL campaigns" | tee -a "$LOG"
echo " Duration: ${DURATION}s per campaign" | tee -a "$LOG"
echo " Started: $(date)" | tee -a "$LOG"
echo "======================================" | tee -a "$LOG"

COMPLETED=0
i=0
while [ $i -lt $TOTAL ]; do
    # Run up to 2 campaigns in parallel
    PIDS=()
    for j in 0 1; do
        idx=$((i + j))
        if [ $idx -lt $TOTAL ]; then
            IFS='|' read -r gpath gver sver rid <<< "${CAMPAIGNS[$idx]}"
            run_one "$gpath" "$gver" "$sver" "$rid" &
            PIDS+=($!)
        fi
    done

    # Wait for both to finish
    for pid in "${PIDS[@]}"; do
        wait "$pid" || true
    done

    i=$((i + 2))
    COMPLETED=$((COMPLETED + ${#PIDS[@]}))
    echo "[$COMPLETED/$TOTAL campaigns processed]" | tee -a "$LOG"
    echo "" | tee -a "$LOG"
done

echo "======================================" | tee -a "$LOG"
echo " ALL $TOTAL CAMPAIGNS COMPLETE" | tee -a "$LOG"
echo " Finished: $(date)" | tee -a "$LOG"
echo "======================================" | tee -a "$LOG"
