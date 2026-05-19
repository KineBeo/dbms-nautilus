#!/usr/bin/env bash
set -euo pipefail
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
LOG=log/rq2_campaigns.log
DONE_FLAG=log/rq2_all_done.flag

# Full campaign list
CAMPAIGNS=(
  "sqlite-3.30.1 run3"
  "sqlite-3.30.1 run4"
  "sqlite-3.30.1 run5"
  "sqlite-3.31.1 run1"
  "sqlite-3.31.1 run2"
  "sqlite-3.31.1 run3"
  "sqlite-3.31.1 run4"
  "sqlite-3.31.1 run5"
  "sqlite-3.32.0 run1"
  "sqlite-3.32.0 run2"
  "sqlite-3.32.0 run3"
  "sqlite-3.32.0 run4"
  "sqlite-3.32.0 run5"
  "sqlite-3.32.2 run1"
  "sqlite-3.32.2 run2"
  "sqlite-3.32.2 run3"
  "sqlite-3.32.2 run4"
  "sqlite-3.32.2 run5"
)

for ENTRY in "${CAMPAIGNS[@]}"; do
  VERSION=$(echo "$ENTRY" | cut -d' ' -f1)
  RUN=$(echo "$ENTRY" | cut -d' ' -f2)
  WDIR="workdirs/${VERSION}_v33_${RUN}"
  
  # Skip if already complete (has triage.json)
  if [ -f "$WDIR/triage.json" ]; then
    echo "=== SKIP v3.3 ${VERSION} ${RUN} (already done) ===" >> "$LOG"
    continue
  fi
  
  # Clean incomplete workdir
  [ -d "$WDIR" ] && rm -rf "$WDIR"
  
  # Drop caches before each campaign to reduce host memory pressure
  sync
  echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null 2>&1 || true

  echo "=== v3.3 ${VERSION} ${RUN} started $(date) ===" >> "$LOG"
  GRAMMAR=grammars/legacy/sqlite_patterns.py DURATION=1800 ./scripts/run_eval.sh ${VERSION} v33_${RUN} >> "$LOG" 2>&1
  echo "=== v3.3 ${VERSION} ${RUN} done $(date) ===" >> "$LOG"

  # 60s cooldown between campaigns to let host reclaim memory
  sleep 60
done

echo "=== RQ2 ALL 20 CAMPAIGNS COMPLETE $(date) ===" >> "$LOG"
touch "$DONE_FLAG"
