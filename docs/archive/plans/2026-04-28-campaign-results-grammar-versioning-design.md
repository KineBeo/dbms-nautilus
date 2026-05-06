# Campaign Results Storage & Grammar Versioning

**Date:** 2026-04-28
**Status:** Approved
**Purpose:** Structured storage for campaign results and grammar version history, enabling thesis paper tables and reproducible experiment comparisons.

---

## Problem Statement

Campaign results are scattered across ephemeral `/tmp/nautilus_eval/` directories. Grammar versions exist only as git commits with no side-by-side diffing capability. Analysis reports live in gitignored `docs/` files. This makes it difficult to:

1. Compare campaigns side-by-side for thesis tables
2. Track grammar evolution with clear version boundaries
3. Reproduce or reference past experiments
4. Generate LaTeX-ready comparison tables

## Design

### 1. Grammar Versioning

#### Directory Structure

```
grammars/
  active/
    sqlite_v3.py              # current working grammar (fuzzer loads this)
  v3.0/
    sqlite_v3.py              # snapshot of commit e719c76
    meta.json                 # version metadata
  v3.1/
    sqlite_v3.py              # next version (e.g., weight-tuned)
    meta.json
  legacy/                     # existing old grammars (unchanged)
    sqlite_patterns.py
    sqlite_attack.py
    sqlite_patterns_uniform.py
  CHANGELOG.md                # human-readable version history
```

#### meta.json Schema

```json
{
  "version": "<semver-style: X.Y>",
  "date": "<YYYY-MM-DD>",
  "commit": "<short git hash>",
  "description": "<one-line summary>",
  "rule_count": "<integer>",
  "changes": "<what changed from parent>",
  "parent_version": "<version string or null>"
}
```

#### CHANGELOG.md Format

```markdown
# Grammar Changelog

## v3.1 — YYYY-MM-DD
- <bullet per change>

## v3.0 — 2026-04-27
- Initial structural primitives design
- 4 Sql-Stmt shapes, 6 Schema-Setup, 8 Stress-Query, 4 Validation-Op
- 449 rules total
```

#### Workflow

1. Edit `grammars/active/sqlite_v3.py`
2. Test (smoke test, short campaign)
3. When satisfied: copy to `grammars/vX.Y/sqlite_v3.py`
4. Write `meta.json` for the version
5. Update `CHANGELOG.md`
6. Commit with `feat(grammar): vX.Y — <description>`

### 2. Campaign Results Storage

#### Directory Structure

```
results/
  campaigns/
    2026-04-27_v3.0_sqlite-3.31.1_15m_run1/
      campaign.json           # metadata + stats
      attribution.txt         # attribution report output
      dedup.json              # triage dedup results
    2026-04-28_v3.1_sqlite-3.31.1_15m_run1/
      campaign.json
      attribution.txt
      dedup.json
  experiments.json            # experiment tags → campaign IDs
```

#### Campaign ID Format

```
{YYYY-MM-DD}_{grammar-version}_{sqlite-target}_{duration}_{run-id}
```

Duration is human-readable: `15m`, `1h`, `24h` (converted from seconds).

Examples:
- `2026-04-28_v3.1_sqlite-3.31.1_15m_run1`
- `2026-04-28_v3.1_sqlite-3.32.2_1h_run2`

#### campaign.json Schema

```json
{
  "id": "<campaign-id>",
  "date": "<YYYY-MM-DD>",
  "grammar_version": "<version string>",
  "grammar_file": "grammars/vX.Y/sqlite_v3.py",
  "target": "<sqlite-version>",
  "duration_seconds": "<integer>",
  "run_id": "<string>",
  "config": {
    "max_tree_size": 300,
    "timeout_ms": 500,
    "threads": 1,
    "bitmap_size": 2097152
  },
  "results": {
    "total_executions": "<integer or null>",
    "crashes": "<integer>",
    "queue_paths": "<integer>",
    "unique_root_causes": "<integer or null>"
  },
  "tags": ["<experiment-tag>"],
  "notes": "<optional free text>"
}
```

#### experiments.json Schema

```json
{
  "<experiment-tag>": {
    "hypothesis": "<what you're testing>",
    "campaigns": ["<campaign-id-1>", "<campaign-id-2>"],
    "conclusion": "<result summary or null if pending>"
  }
}
```

#### What Gets Stored vs Excluded

| Stored in-repo | Excluded (stays in /tmp) |
|---|---|
| campaign.json (metadata + stats) | Raw corpus files |
| attribution.txt (attribution report) | Queue directory |
| dedup.json (triage results) | Signaled directory (raw crash inputs) |
| | exec.log (regenerable) |
| | config.ron (regenerable) |

### 3. Script Integration

#### run_eval.sh Changes

New environment variable: `GRAMMAR_VERSION` (required for archiving).

Post-campaign steps added to end of `run_eval.sh`:
1. Compute campaign ID from `GRAMMAR_VERSION` + target + duration + run_id
2. Create `results/campaigns/{id}/`
3. Write `campaign.json` with stats from coverage.json + directory counts
4. Copy `dedup.json` if it exists
5. Run `analyze_attribution.py` and save as `attribution.txt`
6. Print archive path

If `GRAMMAR_VERSION` is not set, archiving is skipped (backward compatible).

Duration display conversion: `900` → `15m`, `3600` → `1h`, `86400` → `24h`.

#### run_ablation.sh Changes

- Passes `GRAMMAR_VERSION` through to `run_eval.sh`
- Updates `experiments.json` with campaign IDs after each run

#### archive_campaign.sh (New)

Manual archiving for past campaigns:
```bash
./scripts/archive_campaign.sh \
  --workdir /tmp/nautilus_eval/sqlite-3.31.1_v3_baseline_15m \
  --grammar-version v3.0 \
  --target sqlite-3.31.1 \
  --duration 900 \
  --run-id run1 \
  --tag E2-v3-ab-test
```

Creates the same `results/campaigns/{id}/` structure from an existing workdir.

### 4. Thesis Convenience

#### compare_campaigns.py (New)

```bash
# Compare all campaigns in an experiment
python3 scripts/compare_campaigns.py E3-weight-tuning

# LaTeX output for thesis
python3 scripts/compare_campaigns.py E3-weight-tuning --latex
```

Reads `experiments.json`, loads each campaign's `campaign.json`, renders a comparison table.

Markdown output:
```
## Experiment: E3-weight-tuning
**Hypothesis:** Reducing S5 weight diversifies crash portfolio

| Campaign | Grammar | Target | Duration | Crashes | Queue | Executions |
|----------|---------|--------|----------|---------|-------|------------|
| ...run1  | v3.0    | 3.31.1 | 15m      | 131     | 1508  | 245000     |
| ...run2  | v3.1    | 3.31.1 | 15m      | ???     | ???   | ???        |

**Conclusion:** <from experiments.json or "pending">
```

LaTeX output: same data in `\begin{tabular}` format.

## Files Changed

| File | Change |
|------|--------|
| `scripts/run_eval.sh` | Add post-campaign archiving when GRAMMAR_VERSION set |
| `scripts/run_ablation.sh` | Pass GRAMMAR_VERSION, update experiments.json |

## Files Created

| File | Purpose |
|------|---------|
| `grammars/active/sqlite_v3.py` | Working grammar copy |
| `grammars/v3.0/sqlite_v3.py` | Snapshot of current V3 |
| `grammars/v3.0/meta.json` | Version metadata |
| `grammars/CHANGELOG.md` | Version history |
| `results/experiments.json` | Experiment registry |
| `scripts/archive_campaign.sh` | Manual campaign archiver |
| `scripts/compare_campaigns.py` | Thesis table generator |

## .gitignore Changes

No removals needed — `results/` is a new top-level directory, not affected by existing rules.
Add `results/campaigns/*/exec.log` to prevent exec.logs from accidentally being committed.
