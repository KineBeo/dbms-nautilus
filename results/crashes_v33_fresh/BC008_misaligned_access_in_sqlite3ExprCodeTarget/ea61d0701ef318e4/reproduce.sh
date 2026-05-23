#!/usr/bin/env bash
# Reproduce crash: run trigger SQL through the test harness
HARNESS=/home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/nosanit/sqlite_harness_sqlite-3.31.1_nosanit
if [ ! -f "$HARNESS" ]; then
  echo "Harness not found: $HARNESS" >&2
  exit 1
fi
"$HARNESS" trigger.sql
