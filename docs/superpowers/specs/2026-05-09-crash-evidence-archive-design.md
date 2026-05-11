# Crash Evidence Archive — Design Spec

**Date:** 2026-05-09
**Status:** Draft
**Goal:** Consolidate all unique crash findings from 58+ fuzzing campaigns into a self-contained, replayable, thesis-ready evidence archive.

---

## Problem

Crash data is scattered across 60+ campaign workdirs. Each `workdirs/<campaign>/triage_test.json` has per-campaign crash listings, but:
- No global dedup across campaigns (same bug hash appears in 10+ campaigns)
- No consolidated view of all distinct bugs found
- Crash SQL files live in `workdirs/<campaign>/crashes/` — ephemeral, unversioned
- No ready-to-replay packages with stderr, stack traces, reproduction commands
- Thesis Chapter 4 needs a definitive bug inventory, not campaign-by-campaign reports

## Solution

A reusable Python script (`scripts/collect_crashes.py`) that:
1. Scans all `workdirs/*/triage_test.json` files
2. Deduplicates by crash hash across all campaigns
3. Groups hashes into root cause classes (UBSan subtype + key function)
4. For each unique hash: copies trigger SQL, replays through test/ harness, captures stderr
5. Outputs a structured archive at `results/crashes/`

## Output Structure

```
results/crashes/
├── registry.json                    # master index
├── registry.md                      # human-readable summary
│
├── U01_fts5_null_pointer/           # root cause class directory
│   ├── README.md                    # class-level description
│   ├── b45ae061172a/                # one dir per unique crash hash
│   │   ├── trigger.sql              # the SQL that crashes SQLite
│   │   ├── stderr.log              # full ASan/UBSan output from test/ harness
│   │   ├── stack_trace.txt          # cleaned stack frames only
│   │   ├── metadata.json            # structured crash info
│   │   └── reproduce.sh             # one-liner to replay
│   ├── 18c7efd9c88d/
│   │   └── ...
│
├── U02_printf_subtraction_overflow/
│   └── ...
```

### Per-Crash metadata.json

```json
{
  "hash": "b45ae061172a...",
  "class_id": "U01",
  "class_name": "FTS5 Null Pointer Dereference",
  "type": "ubsan",
  "subtype": "null-pointer",
  "error_message": "applying non-zero offset 8 to null pointer",
  "exit_code": 1,
  "severity": "LOW-MED",
  "cve": null,
  "sqlite_version": "3.30.1",
  "source_campaign": "sqlite-3.30.1_bandit_run1",
  "source_file": "1_000012345",
  "first_seen_campaign": "sqlite-3.30.1_cross_v1",
  "all_campaigns": ["sqlite-3.30.1_bandit_run1", "sqlite-3.30.1_cross_v1", ...],
  "top_frames": ["sqlite3Fts5GetTokenizer", "fts5ConfigDefaultTokenizer", ...]
}
```

### reproduce.sh

```bash
#!/bin/bash
# Reproduce crash U01/b45ae061172a
HARNESS="../../harness/test/sqlite_harness_sqlite-3.30.1_test"
echo "Replaying trigger.sql through test harness..."
"$HARNESS" trigger.sql 2>stderr_replay.log
echo "Exit code: $?"
```

### registry.json

```json
{
  "metadata": {
    "generated": "2026-05-09T...",
    "total_classes": 9,
    "total_unique_hashes": 64,
    "campaigns_scanned": 40,
    "sqlite_versions": ["3.30.1", "3.31.1", "3.32.0", "3.32.2"]
  },
  "classes": [
    {
      "id": "U01",
      "name": "FTS5 Null Pointer Dereference",
      "severity": "LOW-MED",
      "subtype": "null-pointer",
      "cve": null,
      "versions": ["3.30.1", "3.31.1", "3.32.0", "3.32.2"],
      "hashes": ["b45ae061172a", "18c7efd9c88d", ...],
      "total_crashes_across_campaigns": 6329
    },
    ...
  ]
}
```

### registry.md

Human-readable table with one row per class: ID, name, severity, CVE, versions, hash count, total crashes. Links to each class README.

### Class README.md

Per-class summary: description, UBSan error message, key stack frames, affected versions, trigger pattern, CVE match if any. Lists all hashes belonging to this class.

## Script Interface

```bash
# Full collection (scan + replay + archive)
python3 scripts/collect_crashes.py

# Scan only (no replay, faster — uses existing triage data)
python3 scripts/collect_crashes.py --scan-only

# Add new campaign to existing archive
python3 scripts/collect_crashes.py --incremental
```

## Root Cause Grouping Logic

Crashes group into a root cause class when they share:
1. Same UBSan subtype (null-pointer, signed-integer-overflow, float-cast-overflow, misaligned-access)
2. Same key function in stack trace (first non-runtime-error frame)

This produces ~9 classes from 64 hashes. Manual override via a `class_overrides.json` file for cases where automatic grouping is wrong.

## Data Flow

```
workdirs/*/triage_test.json        workdirs/*/crashes/*
         │                                  │
         ▼                                  │
  scan & dedup by hash ──────────────────────┘
         │                                  │
         ▼                                  ▼
  group by root cause class        copy trigger SQL files
         │                                  │
         ▼                                  ▼
  results/crashes/<class>/<hash>/   replay through test/ harness
         │                                  │
         ▼                                  ▼
  metadata.json, README.md         stderr.log, stack_trace.txt
         │
         ▼
  registry.json + registry.md
```

## Constraints

- Script must handle missing crash files gracefully (workdir may have been cleaned)
- Replay requires test/ harness binary to exist for each version
- Script should work incrementally — skip hashes already collected
- No external dependencies beyond Python stdlib + existing triage/ module
- Output must be git-committable (no binary blobs, reasonable file count)

## Out of Scope

- Nosanit re-triage (separate pass, can be added later)
- Crash minimization (existing `triage/minimize.py` handles this separately)
- CVE matching automation (manual annotation in class_overrides.json)
