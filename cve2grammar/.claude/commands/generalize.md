---
description: Rewrite crash-oracle bug SQL into feature-scoped Nautilus grammar rules.
argument-hint: "[--html <path>] [--only <bug_id>] [--limit N] [--dry-run]"
---

# /generalize — SQL bug → grammar template pipeline

You are running the generalizer pipeline. Follow these steps IN ORDER.
Do not deviate. Do not ask the user clarifying questions — all arguments
are in `$ARGUMENTS`.

The pipeline is strictly staged:

1. **Fetch candidate bugs** as JSON (from a new CLI subcommand)
2. **Load the non-terminal whitelist** as JSON
3. **Filter** by --only / --limit
4. **Per bug:** cache get → dispatch agent → validate (with one retry on
   failure) → cache put → accumulate
5. **Render** the grammar file (unless --dry-run)
6. **Report**

## Step 1 — Parse $ARGUMENTS

Parse these optional flags out of `$ARGUMENTS`:

- `--html <path>` — a pre-fetched HTML path; pass through to the scraper.
  Skips the network.
- `--only <bug_id>` — process only the bug with this ID (e.g. `MR-SQLITE-0042`).
  Useful for targeted regeneration.
- `--limit N` — after filtering, process at most N bugs. For testing.
- `--dry-run` — do everything except write `generated/sqlite_grammar_v2.py`.

Default values: all flags unset.

## Step 2 — Fetch candidate bugs

Run (with the `--html <path>` suffix if the user passed it):

```
python3 -m cve2grammar generalize-candidates --oracle crash
```

Parse the stdout as JSON. It is an array of objects:

```json
[{"id": "MR-SQLITE-0001", "sql": "...", "title": "...", "dbms": "sqlite", "oracle": "crash", "date": "2020-..."}]
```

If the array is empty, print `No crash-oracle bugs found.` and stop.
Otherwise, call this array `bugs`.

## Step 3 — Load the non-terminal whitelist

Run:

```
python3 -m cve2grammar.generalizer.nonterminals
```

Parse stdout as a JSON array of strings. Call this `whitelist_json`.
Keep the raw JSON string around — you will embed it into each
per-bug prompt verbatim.

## Step 4 — Apply filters

- If `--only <bug_id>` was passed, filter `bugs` to exactly that ID. If
  no bug has that ID, stop with `No bug matches --only <bug_id>`.
- If `--limit N` was passed, keep only the first N entries of the
  filtered list.

## Step 5 — Per-bug loop

Maintain an in-memory `accumulator` list (starts empty). For each bug
in the filtered list:

### 5a. Compute cache key

The cache key is the first 16 hex chars of `sha256(bug.sql)`. Compute it via:

```bash
python3 -c 'import hashlib, sys; print(hashlib.sha256(sys.stdin.read().encode("utf-8")).hexdigest()[:16])' <<'SQL'
<paste bug.sql here verbatim>
SQL
```

Call the output `KEY`.

### 5b. Cache get

Run:

```bash
python3 -m cve2grammar.generalizer.cache get "$KEY"
```

If exit code is 0, parse stdout as JSON and append to `accumulator`.
Then continue to the next bug.

If exit code is 1, it's a cache miss; continue to 5c.

### 5c. Dispatch the sql-generalizer agent

Use the Task tool with `subagent_type: sql-generalizer`. The prompt is:

```
BUG:
Title: <bug.title>
Oracle: <bug.oracle>

SQL:
<bug.sql>

WHITELIST (non-terminals you may use; any {Name} not in this list will
be rejected by the validator):
<whitelist_json>

Follow the rules in .claude/skills/generalize-sql/SKILL.md. Return
EXACTLY one JSON object matching the schema described there. No prose
before or after. No markdown fences.
```

The agent's response is a string. Strip leading/trailing whitespace.
Call it `candidate_json_text`.

### 5d. Validate

Run:

```bash
python3 -m cve2grammar.generalizer.validate <<<'<candidate_json_text>'
```

If exit code is 0, the candidate is valid; continue to 5f.

If exit code is 1, read stderr. Capture the stderr text as
`validator_error`, and continue to 5e for a single retry.

### 5e. Retry once

Dispatch the sql-generalizer agent AGAIN, with the same prompt as 5c
plus an extra line PREPENDED to the BUG section:

```
Previous output failed validation: <validator_error>. Fix that specific
issue and return valid JSON.
```

Run the validator again on the retry response. If it passes, continue
to 5f. If it fails again, skip to 5g (fallback).

### 5f. Success — enrich and cache

Parse `candidate_json_text` as a dict. Add these fields:

- `bug_id`: from the bug being processed
- `sql_sha256`: full sha256 of the SQL (64 hex chars)
- `prompt_version`: 1 (matches `cve2grammar.generalizer.PROMPT_VERSION`)
- `model`: the model name you used (e.g., "sonnet-4.6")
- `created_at`: current UTC time in ISO-8601 "YYYY-MM-DDTHH:MM:SSZ" format
- `status`: "ok"

Compute the full sha256 via:

```bash
python3 -c 'import hashlib, sys; print(hashlib.sha256(sys.stdin.read().encode("utf-8")).hexdigest())' <<'SQL'
<bug.sql>
SQL
```

Write to cache:

```bash
python3 -m cve2grammar.generalizer.cache put "$KEY" <<<'<enriched_json>'
```

Append the enriched dict to `accumulator`. Continue to the next bug.

### 5g. Fallback — both attempts failed

Build a fallback entry:

```json
{
  "bug_id": "<bug.id>",
  "sql_sha256": "<full sha256>",
  "prompt_version": 1,
  "model": "<model>",
  "created_at": "<now ISO>",
  "status": "fallback",
  "template": "<bug.sql>",
  "feature_tag": "fallback",
  "weight": 3.0,
  "notes": "validator rejected two attempts: <first_error> | <second_error>"
}
```

Write it to cache via the same `cache put` command. Append to
`accumulator`. Continue to the next bug.

## Step 6 — Render the grammar file

If the user passed `--dry-run`, skip to Step 7.

Serialize `accumulator` as JSON and pipe into:

```bash
python3 -m cve2grammar.generalizer.render generated/sqlite_grammar_v2.py <<<'<accumulator_json>'
```

## Step 7 — Report

Tally metrics:

- `n_total` = len(accumulator)
- `n_cached` = number of bugs that hit the cache in step 5b
- `n_retried` = number of bugs that needed a retry in step 5e
- `n_fallback` = number of bugs that fell back in step 5g

Print exactly one line:

```
processed {n_total} bugs — {n_cached} cache hits, {n_fallback} fallbacks, {n_retried} retries. Wrote generated/sqlite_grammar_v2.py.
```

If `--dry-run`, replace `Wrote generated/sqlite_grammar_v2.py.` with
`Dry run — no grammar file written.`
