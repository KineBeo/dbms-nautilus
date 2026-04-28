#!/usr/bin/env bash
# run_ablation.sh — E2 ablation: 4 variants × 3 runs × 3600s on sqlite-3.31.1.
#
# Variants:
#   attack_v1  : /tmp/sqlite_attack_v1.py  (materialized from git tag attack-v1-frozen)
#   attack_v2  : grammars/sqlite_attack.py (current HEAD)
#   patterns   : grammars/sqlite_patterns.py
#   uniform    : grammars/sqlite_patterns_uniform.py
#
# Per Task 0 finding (b), Nautilus has no RNG seed control. The 3 runs per
# variant are independent runs (variance-estimate floor), NOT seed-controlled.
#
# Usage:
#   ./scripts/run_ablation.sh
#   DURATION=600 RUNS=1 ./scripts/run_ablation.sh    # fast debug
#
# Env overrides:
#   DURATION    seconds per run  (default: 3600)
#   RUNS        runs per variant (default: 3)
#   TARGET      SQLite version  (default: sqlite-3.31.1)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

DURATION="${DURATION:-3600}"
RUNS="${RUNS:-3}"
TARGET="${TARGET:-sqlite-3.31.1}"
GRAMMAR_VERSION="${GRAMMAR_VERSION:-}"
EXPERIMENT_TAG="${EXPERIMENT_TAG:-}"

export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/home/linuxbrew/.linuxbrew/lib}"
export PYTHONPATH="$ROOT"

if [[ ! -f /tmp/sqlite_attack_v1.py ]]; then
    git show attack-v1-frozen:grammars/sqlite_attack.py > /tmp/sqlite_attack_v1.py
fi

HARNESS="$ROOT/harness/sqlite_harness_patterns_${TARGET}"

declare -A VARIANTS=(
    [attack_v1]="/tmp/sqlite_attack_v1.py"
    [attack_v2]="$ROOT/grammars/sqlite_attack.py"
    [patterns]="$ROOT/grammars/legacy/sqlite_patterns.py"
    [uniform]="$ROOT/grammars/legacy/sqlite_patterns_uniform.py"
)

for VARIANT in attack_v1 attack_v2 patterns uniform; do
    GRAMMAR="${VARIANTS[$VARIANT]}"
    for RUN_N in $(seq 1 "$RUNS"); do
        RUN_ID="${VARIANT}_run${RUN_N}"
        WORKDIR="/tmp/nautilus_eval/${TARGET}_${RUN_ID}"
        echo "========================================"
        echo "[ablation] $VARIANT run $RUN_N/$RUNS  grammar=$GRAMMAR"
        echo "[ablation] workdir=$WORKDIR"
        echo "========================================"
        DURATION="$DURATION" \
        GRAMMAR="$GRAMMAR" \
        GRAMMAR_VERSION="$GRAMMAR_VERSION" \
        EXPERIMENT_TAG="$EXPERIMENT_TAG" \
        HARNESS_SUFFIX=patterns_ \
        "$SCRIPT_DIR/run_eval.sh" "$TARGET" "$RUN_ID"

        echo "[ablation] running stack_dedup on $WORKDIR"
        python3 -m triage.stack_dedup "$WORKDIR" \
            --harness "$HARNESS" \
            --output "$WORKDIR/dedup.json" \
            || echo "[ablation] warning: stack_dedup failed (non-fatal)"
    done
done

echo "========================================"
echo "ABLATION SUMMARY"
echo "========================================"
printf "%-30s %-10s %-10s %-12s %-12s\n" "run_id" "signaled" "queue" "total_exec" "unique_RC"
for VARIANT in attack_v1 attack_v2 patterns uniform; do
    for RUN_N in $(seq 1 "$RUNS"); do
        RUN_ID="${VARIANT}_run${RUN_N}"
        WD="/tmp/nautilus_eval/${TARGET}_${RUN_ID}"
        SIG=$(ls "$WD/outputs/signaled/" 2>/dev/null | wc -l)
        Q=$(ls "$WD/outputs/queue/" 2>/dev/null | wc -l)
        EXEC=$(python3 -c "import json; d=json.load(open('$WD/coverage.json')); print(d.get('total_executions') or 'n/a')" 2>/dev/null || echo "n/a")
        UNQ=$(python3 -c "import json; d=json.load(open('$WD/dedup.json')); print(d.get('unique_root_causes') or 'n/a')" 2>/dev/null || echo "n/a")
        printf "%-30s %-10s %-10s %-12s %-12s\n" "$RUN_ID" "$SIG" "$Q" "$EXEC" "$UNQ"
    done
done
