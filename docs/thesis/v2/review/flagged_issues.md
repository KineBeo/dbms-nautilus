# Flagged Issues — Chapter 4 Review

**Generated:** 2026-05-22

---

## Priority 1 (Critical — fix before next advisor meeting)

### From Step 1 — Inventory

- [ ] **INCONSISTENCY (R2.5):** Thesis L102 claims "80 campaigns" but only 79 workdirs exist. `sqlite-3.32.0_comparison_ebnf_run1` is missing. Either re-run the missing campaign or change the text to acknowledge n=4 for EBNF 3.32.0.
- [ ] **INCONSISTENCY (R2.5):** Table 4.5 caption says "$n=5$ per cell" but EBNF 3.32.0 has n=4. The `rq3_statistical_tests.csv` confirms `ebnf_n=4` for 3.32.0. Caption must be corrected.
- [ ] **INCONSISTENCY (R1.2):** Three different grammar versions (v3.5, v3.3, v3.4) are presented as "the proposed grammar" across RQ1/RQ2/RQ3. The thesis never discloses that different grammar snapshots were used for different RQs. This is a data integrity issue — must be documented or justified.

### From Step 2 — Traceability

- [ ] **WRONG_SOURCE (R1.1, R1.3) — CRITICAL:** Table 4.5 throughput and edge coverage for "DBMS-Nautilus" are computed from **v3.5 workdirs** (RQ1 campaigns), NOT from v3.4 comparison workdirs (RQ3 campaigns). The RQ3 comparison mixes data from different campaign sets. The `rq3_statistical_tests.csv` was built from v3.5 proposed + EBNF comparison — an apples-to-oranges comparison. All p-values and effect sizes for throughput and edges are therefore invalid.
  - Thesis throughput 3.30.1: 76.7 (v3.5) vs correct 90.6 (v3.4)
  - Thesis throughput 3.31.1: 56.8 (v3.5) vs correct 92.4 (v3.4)
  - Thesis throughput 3.32.0: 71.8 (v3.5) vs correct 84.8 (v3.4)
  - Thesis throughput 3.32.2: 103.8 (v3.5) vs correct 95.1 (v3.4)
  - Thesis edges 3.30.1: 18,867 (v3.5) vs correct 19,862 (v3.4)

- [ ] **WRONG_SOURCE (R1.1) — CRITICAL:** Table 4.6 summary inherits the same problem. Proposed grammar throughput=77.3 and edges=19,815 are from v3.5, not v3.4. Correct values: throughput=90.7, edges=20,182.

- [ ] **CASCADING_ERROR (R1.3, R3.3):** All derived ratios in prose are wrong:
  - "61.5% lower throughput" → should be ~54.8% with v3.4 data
  - "14.5% lower edge coverage" → should be ~12.9% with v3.4 data
  - "2.6x slower" → should be ~2.2x with v3.4 data
  - "mean 200.7 vs 77.3" → 77.3 is from wrong source
  - "mean 23,169 vs 19,815" → 19,815 is from wrong source

- [ ] **MISMATCH (R1.2):** CVE-2020-13871 in Table 4.2 says "Applicable Version(s) = 3.32.2, Runs Found = 4/5". But `cve_hits.csv` shows 0/5 on 3.32.2. The 4/5 figure comes from manual no-debug replay on **3.30.1** (runs 2-5), documented in `cve_replay_nodebug.md`. The table conflates two things: (a) the CVE was assigned to 3.32.2 in Table 4.1, and (b) the seed-derived crashes were found on 3.30.1. The footnote explains the mechanism but doesn't fix the version mismatch.

- [ ] **MISMATCH (R1.2):** Discussion L360 says EBNF found "sqlite3WindowListDelete" as a bug class. Raw data (`bug_classes.csv`) shows "clearSelect" instead. "WindowListDelete" appears only in archived campaigns, not in the RQ3 comparison data.

- [ ] **ORPHAN_NUMBER (R1.5):** TTFC values in Table 4.5 and Table 4.6 cannot be independently verified from `campaigns_summary.csv` (TTFC is not stored there). They exist only in `rq3_statistical_tests.csv` and were computed by `scripts/compute_stats.py` from workdir triage files. The proposed-grammar TTFC values are from v3.5 workdirs (same wrong-source issue).

---

### From Step 3 — Consistency

- [ ] **INCONSISTENCY (R2.1):** Intro paragraph L4 says section order is "Setup → Baselines → Metrics" but actual order is "Metrics → Baselines → Setup" (sections 4.2, 4.3, 4.4). The `\ref` labels resolve correctly but the narrative sentence is wrong. Fix: rewrite the intro sentence to match actual order.

### From Step 4 — Statistics

- [ ] **INCONSISTENT_N (R3.2):** EBNF 3.32.0 run1 outlier (throughput=418.5, edges=17218) is INCLUDED in throughput/edge statistics (n=5) but EXCLUDED from unique_bugs/TTFC statistics (n=4). Pick one: either include consistently or exclude consistently with documented justification.
- [ ] **UNDOCUMENTED_STD (R3.1):** Table 4.6 proposed-grammar std values for throughput (23.6) and edges (782) don't match either grand std or mean-of-version-stds. The computation method is undocumented. Grand std from all 20 runs gives 27.9 and 1051 respectively.
- [ ] **MIXED_SOURCES (R3.1):** The unique_root_causes p-values in Table 4.5 are computed from v3.4-vs-EBNF (confirmed match) but the same table's throughput/edge p-values are computed from v3.5-vs-EBNF. This means Table 4.5 is a hybrid of two different experimental comparisons presented as one.

- [ ] **INCONSISTENCY (R2.2):** Table 4.3 has unexplained gaps in bug class IDs: BC005 and BC007 are missing. No footnote or text explains why. Fix: either renumber sequentially (BC001-BC011) or add a footnote explaining the gaps.

### From Step 5 — Honesty

- [ ] **UNREPORTED_ANOMALY (R6.3):** v3.4_3.31.1_run1 (queue=123, RCs=43) and v3.4_3.32.0_run1 (queue=77, RCs=12) are extreme outliers never mentioned in thesis. They inflate the std in Table 4.5 (72.4 and 73.0) and drag down the means. These campaigns appear to have failed queue initialization (10-15x fewer queue items than peers).
- [ ] **UNREPORTED_ANOMALY (R6.3):** EBNF 3.32.0 run1 (throughput=418.5, edges=17218) is an extreme outlier included in statistics but never discussed. Its workdir was deleted. Its inclusion inflates EBNF 3.32.0 throughput from 197.8 to 241.9 and makes edge coverage p-value non-significant (0.151).
- [ ] **UNDOCUMENTED_EXCLUSION (R6.2):** Bug classes BC005 (sqlite3WindowListDelete, 5 crashes) and BC008 (signal-6 in sqlite3ExprCodeTarget, 1 crash) exist in `crashes_v33/registry.md` but are silently dropped from thesis Table 4.3 with no explanation.
- [ ] **MISLEADING_CAPTION (R6.4):** Figures 4.3-4.5 captions say "DBMS-Nautilus vs EBNF-Baseline" implying a controlled same-campaign comparison. Actually, DBMS-Nautilus data comes from v3.5 workdirs (different campaign set, different time, potentially different machine state) while EBNF comes from comparison workdirs.

---

## Priority 2 (Important — fix before submission)

### From Step 3 — Consistency

- [ ] **INCONSISTENCY (R2.1):** Baseline name alternates between "EBNF-Baseline" (hyphenated, in tables/captions) and "EBNF baseline" (two words, in prose). Pick one form and use it everywhere.
- [ ] **INCONSISTENCY (R2.3):** Table 4.3 CVE column uses abbreviated form (13871, 13434, 9327) while all other references use full CVE-YYYY-NNNNN format. Minor but could attract reviewer comment.

### From Step 6 — Claims vs Evidence

- [ ] **OVERREACH (R4.1):** L358: "the additional coverage is concentrated in non-vulnerable code paths" — no code-level analysis supports this. The data shows more edges but fewer crashes; this could mean the EBNF grammar doesn't *compose* vulnerability-triggering inputs, not that it explores non-vulnerable code. Suggest: "the additional coverage does not translate into proportional crash discovery."
- [ ] **OVERREACH (R4.1):** L293: "a smaller but more vulnerability-relevant subset of the code" — same issue. Lower coverage + more crashes does not prove the explored code is more "vulnerability-relevant." Suggest: "a smaller subset of the code that yields more crashes."
- [ ] **WEAK_CLAIM (R4.2):** L231: "This demonstrates that the grammar's structural primitives can independently compose the four simultaneous elements" — based on n=2 occurrences across 20 campaigns. "Demonstrates" is too strong for 10% occurrence rate. Suggest: "provides an example of" or "suggests that."
- [ ] **WEAK_CLAIM (R4.1):** L160: "demonstrating the effectiveness of the boosted seed weight" — no control experiment (same grammar without boost). Cannot attribute 5/5 to the boost vs the grammar itself. Suggest: "consistent with the boosted seed weight being effective."
- [ ] **MISSING_EVIDENCE (R4.3):** L205: "3 newly discovered bugs that have not been previously reported in the SQLite bug tracker or CVE database" — no documented search methodology. These bugs are on 5-6 year old SQLite versions; they may have been found and fixed without CVE assignment. Suggest: add a sentence describing the search (e.g., "We searched the NVD database and SQLite changelog for versions 3.30.1-3.31.1 and found no matching reports").
- [ ] **BORDERLINE (R4.1):** L394 summary: "confirming that domain-knowledge-driven grammar engineering can reconstruct" — 4/5 CVEs with 1 failure and 1 needing manual replay. "Supporting" or "providing evidence that" would be more accurate than "confirming."

## Priority 3 (Polish)

### From Step 7 — Reproducibility

- [ ] **MISSING_JUSTIFICATION (R5.2):** 5 of 8 hyperparameters have no justification: campaign duration (900s), repetitions (5), execution timeout (500ms), bitmap size (2MB), top-N frames (5). Standard practice in fuzzing papers is to cite prior work or pilot studies for these. At minimum add: "following standard practice in grammar-based fuzzing [cite Nautilus, Aschermann et al.]" or "determined by pilot study."
- [ ] **MISSING_ITEM (R5.1):** No git commit hash recorded. A reader cannot determine which exact code version produced the results. Add the hash to the setup section or a footnote.
- [ ] **MISSING_ITEM (R5.1):** No random seed recorded. The fuzzer uses `rand::thread_rng()` (OS entropy). Campaigns are not individually reproducible. This should be acknowledged: "Individual campaigns are not deterministically reproducible; we report statistics over 5 independent repetitions to account for stochastic variance."
- [ ] **MISSING_ITEM (R5.1):** Python version not stated (PyO3 bridge requires it).
- [ ] **MISSING_ITEM (R5.1):** Exact CFLAGS/compiler flags not documented. Thesis says "ASan and UBSan" but doesn't list `-O1 -g -fsanitize=address,undefined -fno-sanitize-recover=all` or equivalent.

## Priority 3 (Polish)

- [ ] **FORMATTING:** Three figure captions (L298, L307, L343) have double spaces before "vs"/"and".
- [ ] **STYLE:** "seed-augmented grammar" (L231) used once; everywhere else says "with seed rules" or "proposed grammar with seed rules". Standardize.

## BLOCKED

- [ ] **BLOCKED (R1.3):** Cannot re-verify TTFC computation independently without running `scripts/compute_stats.py`. The script reads triage.json from workdirs, finds earliest crash exec index, maps to wall-clock time. Would need to re-run the script to confirm values.
