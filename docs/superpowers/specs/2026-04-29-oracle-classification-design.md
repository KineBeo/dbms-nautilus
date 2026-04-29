# Oracle Classification — Post-Campaign Crash Triage

**Date:** 2026-04-29
**Status:** Approved
**Parent:** Phase 2 roadmap item #7

## Problem

The fuzzing harness compiled with `-DSQLITE_DEBUG -fsanitize=address,undefined` produces three distinct crash types, but the harness and campaign archive treat all crashes identically:

- **ASan crashes** (exit 223) — memory safety violations (heap-overflow, use-after-free)
- **UBSan crashes** (exit 1) — undefined behavior (integer overflow, null pointer)
- **Debug asserts** (SIGTRAP/signal 5) — `SQLITE_DEBUG` assertion failures, not security vulnerabilities

In the V3.1 campaign (121 crashes), 80% were debug asserts and 20% were CVE-2020-13434 (UBSan integer overflow). Without classification, campaign.json reports "121 crashes" with no severity breakdown.

## Design

### Detection Method: Classify by Exclusion

Re-run each crash through the harness via subprocess. The exit code determines the type:

| Exit Code | Classification | Subtype Source |
|-----------|---------------|----------------|
| 223 | `asan` | Parse stderr for ASan error type |
| 1 | `ubsan` | Parse stderr for `runtime error:` line |
| signal (< 0) | `signal` | Record signal number |
| 0 | `debug_assert` | Forksrv caught SIGTRAP, no sanitizer fires on re-run |
| timeout | `timeout` | Execution exceeded deadline |

ASan subtypes: `heap-buffer-overflow`, `stack-buffer-overflow`, `use-after-free`, `null-dereference`, `asan-other`.

UBSan subtypes: `integer-overflow`, `null-pointer`, `shift-exponent`, `signed-integer-overflow`, `ubsan-other`.

This method was validated against GDB ground truth across all 121 V3.1 crashes with 100% accuracy.

### Tool: `triage/classify.py`

Replaces `triage/dedup.py` and `triage/report.py`. Single-pass tool that re-runs each crash once, performing deduplication (stack-hash) and classification simultaneously.

Kept unchanged: `triage/stack_dedup.py` (GDB-based deep frame analysis — fundamentally different method).

#### CLI Interface

```bash
# Auto mode (called by run_eval.sh)
python3 triage/classify.py $WORKDIR --harness $HARNESS_BIN

# Standalone with campaign.json enrichment
python3 triage/classify.py $WORKDIR \
  --harness harness/sqlite_harness_sqlite-3.31.1 \
  --enrich results/campaigns/.../campaign.json

# Custom output paths
python3 triage/classify.py $WORKDIR \
  --harness $HARNESS \
  --output $WORKDIR/triage.json \
  --dedup-dir $WORKDIR/dedup \
  --report $WORKDIR/triage_report.md
```

Arguments:
- `workdir` (positional) — Nautilus workdir containing `outputs/signaled/`
- `--harness` (required) — path to harness binary
- `--output` — triage.json path (default: `$WORKDIR/triage.json`)
- `--dedup-dir` — directory for unique crash files (default: `$WORKDIR/dedup`)
- `--report` — markdown report path (default: `$WORKDIR/triage_report.md`)
- `--enrich` — path to campaign.json to merge classification summary into
- `--timeout` — per-crash re-run timeout in seconds (default: 5)

### Output Artifacts

#### 1. `triage.json`

```json
{
  "total_crashes": 121,
  "unique_crashes": 2,
  "summary": {
    "asan": 0,
    "ubsan": 1,
    "debug_assert": 1,
    "signal": 0,
    "timeout": 0
  },
  "crashes": [
    {
      "hash": "a1b2c3d4",
      "type": "ubsan",
      "subtype": "integer-overflow",
      "exit_code": 1,
      "count": 24,
      "sample_file": "a1b2c3d4_sig_001234",
      "top_frames": ["sqlite3_str_vappendf", "sqlite3VXPrintf"],
      "sql_preview": "SELECT printf('%d', -2147483648);"
    },
    {
      "hash": "f9e8d7c6",
      "type": "debug_assert",
      "subtype": null,
      "exit_code": 0,
      "count": 97,
      "sample_file": "f9e8d7c6_sig_005678",
      "top_frames": [],
      "sql_preview": "CREATE VIRTUAL TABLE fts USING fts5(...);"
    }
  ]
}
```

#### 2. `dedup/` directory

One crash file per unique stack hash (same naming as old dedup.py: `{hash}_{original_filename}`).

#### 3. `triage_report.md`

Markdown report with:
- Summary table (type × unique × total × percentage)
- Per-crash sections with type badge, exit code, SQL input, stack trace (if available)

#### 4. `campaign.json` enrichment (via `--enrich` or archive_campaign.sh)

Adds `crash_classification` to the `results` object:

```json
{
  "results": {
    "crashes": 121,
    "queue_paths": 1472,
    "crash_classification": {
      "unique_crash_sites": 2,
      "asan": 0,
      "ubsan": 24,
      "debug_assert": 97,
      "signal": 0,
      "timeout": 0
    }
  }
}
```

The `summary` in triage.json counts **unique** crash sites per type. The `crash_classification` in campaign.json counts **total** crashes per type (for thesis tables showing raw numbers).

### Pipeline Integration

Updated `run_eval.sh` flow:

1. Run fuzzer for DURATION seconds
2. Print crash/queue counts
3. `capture_coverage.py` → `coverage.json`
4. **`classify.py $WORKDIR --harness $HARNESS_BIN`** → `triage.json` + `dedup/` + `triage_report.md`
5. `archive_campaign.sh` → `results/campaigns/` (reads `triage.json`, merges into `campaign.json`)

classify.py failure is non-fatal (`|| true`) — same pattern as coverage capture.

### Script Changes

**`scripts/archive_campaign.sh`**: After writing `campaign.json`, check if `$WORKDIR/triage.json` exists. If so, read the summary and merge `crash_classification` into the campaign.json `results` object.

**`scripts/compare_campaigns.py`**: Add classification columns to comparison tables when `crash_classification` data is present. Columns: `ASan`, `UBSan`, `Assert`, `Signal`. Graceful degradation — old campaigns without classification show `—`.

## Files Changed

| File | Action | Details |
|------|--------|---------|
| `triage/classify.py` | CREATE | Unified dedup+classify+report (~250 lines) |
| `triage/dedup.py` | DELETE | Replaced by classify.py |
| `triage/report.py` | DELETE | Replaced by classify.py |
| `scripts/run_eval.sh` | MODIFY | Add classify.py step between coverage and archive |
| `scripts/archive_campaign.sh` | MODIFY | Read triage.json, merge into campaign.json |
| `scripts/compare_campaigns.py` | MODIFY | Show classification in comparison tables |

Unchanged: `triage/stack_dedup.py`, `triage/fidelity_score.py`, `triage/cve_signatures.py`.
