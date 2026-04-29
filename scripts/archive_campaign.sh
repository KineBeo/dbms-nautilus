#!/usr/bin/env bash
# archive_campaign.sh — Archive a campaign from a workdir into results/campaigns/
#
# Usage:
#   ./scripts/archive_campaign.sh \
#     --workdir /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
#     --grammar-version v3.0 \
#     --target sqlite-3.31.1 \
#     --duration 900 \
#     --run-id run1 \
#     [--tag E2-v3-ab-test] \
#     [--notes "15-min A/B baseline"]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

WORKDIR=""
GRAMMAR_VERSION=""
TARGET=""
DURATION=""
RUN_ID=""
TAG=""
NOTES=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --workdir) WORKDIR="$2"; shift 2 ;;
        --grammar-version) GRAMMAR_VERSION="$2"; shift 2 ;;
        --target) TARGET="$2"; shift 2 ;;
        --duration) DURATION="$2"; shift 2 ;;
        --run-id) RUN_ID="$2"; shift 2 ;;
        --tag) TAG="$2"; shift 2 ;;
        --notes) NOTES="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

if [[ -z "$WORKDIR" || -z "$GRAMMAR_VERSION" || -z "$TARGET" || -z "$DURATION" || -z "$RUN_ID" ]]; then
    echo "Usage: $0 --workdir <path> --grammar-version <vX.Y> --target <sqlite-ver> --duration <secs> --run-id <id> [--tag <tag>] [--notes <text>]"
    exit 1
fi

if [[ ! -d "$WORKDIR" ]]; then
    echo "Error: workdir not found: $WORKDIR"
    exit 1
fi

# Convert duration seconds to human-readable
duration_human() {
    local secs=$1
    if (( secs >= 86400 )); then
        echo "$((secs / 86400))d"
    elif (( secs >= 3600 )); then
        echo "$((secs / 3600))h"
    else
        echo "$((secs / 60))m"
    fi
}

TODAY=$(date +%Y-%m-%d)
DURATION_H=$(duration_human "$DURATION")
CAMPAIGN_ID="${TODAY}_${GRAMMAR_VERSION}_${TARGET}_${DURATION_H}_${RUN_ID}"

ARCHIVE_DIR="$ROOT/results/campaigns/$CAMPAIGN_ID"

if [[ -d "$ARCHIVE_DIR" ]]; then
    echo "Error: archive already exists: $ARCHIVE_DIR"
    exit 1
fi

mkdir -p "$ARCHIVE_DIR"

# Count results from workdir
CRASHES=$(ls "$WORKDIR/outputs/signaled/" 2>/dev/null | wc -l)
QUEUE=$(ls "$WORKDIR/outputs/queue/" 2>/dev/null | wc -l)

# Read total_executions from coverage.json if it exists
TOTAL_EXEC="null"
if [[ -f "$WORKDIR/coverage.json" ]]; then
    TOTAL_EXEC=$(python3 -c "import json; d=json.load(open('$WORKDIR/coverage.json')); print(d.get('total_executions') or 'null')" 2>/dev/null || echo "null")
fi

# Read unique_root_causes from dedup.json if it exists
UNIQUE_RC="null"
if [[ -f "$WORKDIR/dedup.json" ]]; then
    UNIQUE_RC=$(python3 -c "import json; d=json.load(open('$WORKDIR/dedup.json')); print(d.get('unique_root_causes') or 'null')" 2>/dev/null || echo "null")
fi

# Read config values from config.ron if it exists
MAX_TREE_SIZE=300
TIMEOUT_MS=500
THREADS=1
BITMAP_SIZE=2097152
if [[ -f "$WORKDIR/config.ron" ]]; then
    MAX_TREE_SIZE=$(grep -oP 'max_tree_size:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 300)
    TIMEOUT_MS=$(grep -oP 'timeout_in_millis:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 500)
    THREADS=$(grep -oP 'number_of_threads:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 1)
    BITMAP_SIZE=$(grep -oP 'bitmap_size:\s*\K\d+' "$WORKDIR/config.ron" 2>/dev/null || echo 2097152)
fi

# Build tags JSON array
if [[ -n "$TAG" ]]; then
    TAGS_JSON="[\"$TAG\"]"
else
    TAGS_JSON="[]"
fi

# Write campaign.json
cat > "$ARCHIVE_DIR/campaign.json" <<ENDJSON
{
  "id": "$CAMPAIGN_ID",
  "date": "$TODAY",
  "grammar_version": "$GRAMMAR_VERSION",
  "grammar_file": "grammars/$GRAMMAR_VERSION/sqlite_v3.py",
  "target": "$TARGET",
  "duration_seconds": $DURATION,
  "run_id": "$RUN_ID",
  "config": {
    "max_tree_size": $MAX_TREE_SIZE,
    "timeout_ms": $TIMEOUT_MS,
    "threads": $THREADS,
    "bitmap_size": $BITMAP_SIZE
  },
  "results": {
    "total_executions": $TOTAL_EXEC,
    "crashes": $CRASHES,
    "queue_paths": $QUEUE,
    "unique_root_causes": $UNIQUE_RC
  },
  "tags": $TAGS_JSON,
  "notes": "$NOTES"
}
ENDJSON

# Merge crash classification from triage.json if present
if [[ -f "$WORKDIR/triage.json" ]]; then
    python3 -c "
import json, sys
with open('$ARCHIVE_DIR/campaign.json') as f:
    campaign = json.load(f)
with open('$WORKDIR/triage.json') as f:
    triage = json.load(f)
totals = {'asan': 0, 'ubsan': 0, 'debug_assert': 0, 'signal': 0, 'timeout': 0}
for c in triage.get('crashes', []):
    key = c['type'] if c['type'] in totals else 'signal'
    totals[key] += c['count']
campaign['results']['crash_classification'] = {
    'unique_crash_sites': triage['unique_crashes'],
    **totals,
}
with open('$ARCHIVE_DIR/campaign.json', 'w') as f:
    json.dump(campaign, f, indent=2)
print(f'[archive] merged crash classification into campaign.json')
" || echo "[archive] warning: triage merge failed (non-fatal)"
    # Copy triage.json and report to archive
    cp "$WORKDIR/triage.json" "$ARCHIVE_DIR/triage.json" 2>/dev/null || true
    cp "$WORKDIR/triage_report.md" "$ARCHIVE_DIR/triage_report.md" 2>/dev/null || true
fi

# Copy dedup.json if present
if [[ -f "$WORKDIR/dedup.json" ]]; then
    cp "$WORKDIR/dedup.json" "$ARCHIVE_DIR/dedup.json"
fi

# Generate attribution report if exec.log exists
GRAMMAR_FILE="$ROOT/grammars/$GRAMMAR_VERSION/sqlite_v3.py"
if [[ -f "$WORKDIR/exec.log" && -f "$GRAMMAR_FILE" ]]; then
    echo "[archive] generating attribution report..."
    python3 "$SCRIPT_DIR/analyze_attribution.py" "$WORKDIR" \
        --grammar "$GRAMMAR_FILE" \
        > "$ARCHIVE_DIR/attribution.txt" 2>/dev/null \
        || echo "[archive] warning: attribution generation failed (non-fatal)"
fi

echo "========================================"
echo " Campaign archived"
echo " ID:      $CAMPAIGN_ID"
echo " Path:    $ARCHIVE_DIR"
echo " Crashes: $CRASHES"
echo " Queue:   $QUEUE"
echo "========================================"

# Update experiments.json if --tag was provided
if [[ -n "$TAG" ]]; then
    EXPERIMENTS_FILE="$ROOT/results/experiments.json"
    if [[ -f "$EXPERIMENTS_FILE" ]]; then
        python3 -c "
import json, sys
with open('$EXPERIMENTS_FILE') as f:
    data = json.load(f)
tag = '$TAG'
cid = '$CAMPAIGN_ID'
if tag not in data:
    data[tag] = {'hypothesis': '', 'campaigns': [], 'conclusion': None}
if cid not in data[tag]['campaigns']:
    data[tag]['campaigns'].append(cid)
with open('$EXPERIMENTS_FILE', 'w') as f:
    json.dump(data, f, indent=2)
print(f'[archive] added {cid} to experiment {tag}')
" || echo "[archive] warning: experiments.json update failed (non-fatal)"
    fi
fi
