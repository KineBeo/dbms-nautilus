# Pilot Results — sqlite_attack.py vs sqlite_patterns.py on sqlite-3.31.1

**Date:** 2026-04-22
**Duration per run:** 900 s (15 minutes, per user directive; less than plan's 3600s baseline)
**Target:** sqlite-3.31.1 (ASan + UBSan harness, blank-DB patterns mode)
**Harness:** `harness/sqlite_harness_patterns_sqlite-3.31.1`
**Spec:** `docs/superpowers/specs/2026-04-22-attack-pattern-grammar-design.md`

**TL;DR:** 15-min pilot is thesis-negative at this sample size — attack grammar
loses on breadth (4/6 vs 6/6 CVE classes) and volume (18 vs 263 crashes). One
clean win: CVE-2020-13434 printf-boundary (14 vs 7). Verdict is preliminary;
a 3600s pilot with weight-annotated attack grammar is needed before drawing
thesis conclusions.

## Headline Numbers

> Exec-count rows marked N/A because the pilot scripts did not capture total
> execution counts to the workdir log in a parseable form. This blocks the
> crashes-per-million-execs acceptance criterion (spec §10.6). The Next Steps
> section queues a fix so the next pilot can evaluate that criterion.

| Metric | sqlite_attack.py | sqlite_patterns.py |
|---|---|---|
| Grammar lines | 426 | 1009 |
| Total executions | not captured (exec.log parsing failed) | not captured (exec.log parsing failed) |
| Exec/sec | N/A | N/A |
| Signaled crashes (raw) | 18 | 263 |
| Unique crash clusters (dedup) | 18 (100% unique by SQL byte-hash) | 263 (100% unique by SQL byte-hash) |
| Queue items | 942 | 1161 |
| Timeouts | 6 | 6 |
| CVE classes hit | 4 of 6 | 6 of 6 |
| Crashes per million execs | N/A (exec count unknown) | N/A (exec count unknown) |

## CVE Class Hits

| CVE | sqlite_attack.py | sqlite_patterns.py | Notes |
|---|---|---|---|
| CVE-2020-13434 (printf / group_concat boundary) | Y (14 matches) | Y (7 matches) | only class where attack > patterns |
| CVE-2020-9327 (gen-col + JOIN + coalesce) | N (0 matches) | Y (3 matches) | attack missed despite having pattern |
| CVE-2020-13435 (JOIN + NATURAL JOIN + coalesce-window) | N (0 matches) | Y (219 matches) | dominant patterns class; attack missed |
| CVE-2020-15358 (INTERSECT + VIEW) | Y (1 match) | Y (33 matches; 35 incl. any INTERSECT) | |
| CVE-2020-13871 (HAVING + window + EXCEPT) | Y (1 match) | Y (2 matches) | |
| CVE-2019-19646 (gen-col + integrity_check) | N (0 regex) / possibly 2+ (visual sample) | Y (1 match) | regex classifier false-negatives; wrong version — 3.31.1 has it patched |

## Pilot Acceptance (Spec §10.6)

- attack grammar hits at least 3 of 6 CVE classes in 1 hour: PASS (4/6 in 15 min; extrapolates to PASS)
- attack grammar does NOT miss any CVE class that patterns grammar found: FAIL (attack missed CVE-2020-13435, CVE-2020-9327, and CVE-2019-19646 — all three found by patterns)
- attack grammar crashes-per-million-execs at least 50% of patterns grammar rate: N/A (exec count data was not captured cleanly — workdir exec.log exists but the Execution Count parsing did not produce numbers for either run)

## Interpretation

At this 15-minute sample size, the data does not support the thesis that the
Nautilus-mruby attack-grammar shrink preserves CVE coverage at parity with the
1009-line `sqlite_patterns.py`. On raw volume, `sqlite_patterns.py` produced
263 signaled crashes vs 18 for `sqlite_attack.py` — a 14.6x gap. On breadth,
patterns hit all 6 CVE classes; attack hit 4 of 6. Attack grammar entirely
missed CVE-2020-13435 (NATURAL-JOIN + coalesce-window) and CVE-2020-9327
(generated-column + JOIN + coalesce) despite having explicit rules for both
patterns in `sqlite_attack.py`. Since Nautilus uses a uniform scheduler, this
is a diagnostic signal: with ~940 queue items in 15 min, the scheduler simply
did not pick those patterns often enough to trigger the underlying bugs.

The one clean win for the attack grammar is CVE-2020-13434 (printf-boundary),
where attack produced 14 matches vs patterns' 7. This specific class benefits
from the shrunken vocabulary — fewer competing productions mean the printf
pattern fires more often per unit wall-time. Sample crash
`attack 5_000111650` (`printf('%.*g', -2147483647, 0.01)` composed with a
coalesce-window) is a textbook CVE-2020-13434 variant and confirms the attack
grammar's literal-boundary vocabulary is doing useful work when selected.

Three methodology caveats must qualify these numbers: (1) dedup.py is blind
on this harness — all crashes are SIGTRAP (SQLITE_DEBUG asserts) or SIGABRT
with no ASan/UBSan frames, so 100% "unique" is a file-byte property, not a
bug-distinctness property; (2) the CVE-class regex classifier false-negatives
visible CVE-19646-shaped crashes because it requires the literal
`GENERATED ALWAYS AS` string; (3) CVE-2020-13435 is documented as affecting
sqlite-3.32.0, but patterns produced 219 matches on sqlite-3.31.1 — either
the pattern triggers a same-family bug on 3.31.1, or the version-range
mapping in `docs/cve-list.md` needs revisiting.

## Next Steps

- **Run a longer pilot (3600s or 24h) before declaring thesis-positive or
  thesis-negative.** 15 min is inadequate sample size; the spec's 3600s
  baseline and §10.5 24-hour campaign are the true comparison. The
  scheduler-selection gap on CVE-2020-13435 / CVE-2020-9327 should narrow
  with more wall-time.
- **Write a follow-up spec** at
  `docs/superpowers/specs/2026-04-??-attack-pattern-weights.md`.
  Assign higher weight to `Pattern-P13435` and `Pattern-P9327` (the missed
  classes). This is the RL-design spec that spec §9 deferred. The 15-min
  pilot *suggests* the deferral may need to be revisited, but n=1 at 15 min
  cannot isolate scheduler-selection variance from grammar-design variance —
  a longer re-pilot with and without weights is the appropriate next test.
- **Fix the CVE-class regex classifier** with structural matching (AST /
  parse-tree pattern-match) rather than substring matching, before trusting
  any future CVE-class counts.
- **Replace SQL-byte-hash dedup with gdb-backtrace-based dedup** so "unique
  crash clusters" actually measures unique bugs rather than unique byte
  sequences.
- **Capture exec counts properly** in Task 9 pilot scripts so the
  crashes-per-million-execs acceptance criterion (§10.6) can be evaluated on
  the next pilot.

## Raw Workdir Locations

- sqlite_attack pilot: `/tmp/nautilus_eval/sqlite-3.31.1_attack_pilot_15m/`
- sqlite_patterns pilot: `/tmp/nautilus_eval/sqlite-3.31.1_patterns_pilot_15m/`

These are ephemeral (`/tmp`) — if they need to persist, copy to a
`docs/pilot-artifacts/YYYY-MM-DD/` directory and commit separately.
