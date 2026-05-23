# Experiments Chapter Review Rules

This document defines the rules for systematically reviewing a thesis experiments chapter. Rules are grouped into 6 categories, ordered by review priority.

## Group 1: Data Traceability

Every number in the thesis must be traceable to a source.

- **R1.1** Every number appearing in text, tables, or figures must be traceable to an original data file (CSV, JSON, log). Record the mapping `number → source_file → row/column` in the data governance file.
- **R1.2** If a number appears in multiple places (e.g., in text and in a table), verify they match **exactly**. Flag every mismatch.
- **R1.3** Every computed value (mean, std, ratio, percentage) must be re-computed from raw data and verified against the thesis value. Flag any deviation > 0.1%.
- **R1.4** Every table must have associated metadata: campaign IDs, raw data files, extraction date, generation script. Store in data governance.
- **R1.5** If a number cannot be traced to raw data, flag it as `ORPHAN_NUMBER`. Such numbers must not remain in the thesis.

## Group 2: Consistency Across Sections

The same concept must use the same name everywhere.

- **R2.1** List every term used to refer to the same concept (e.g., "proposed grammar", "structural-primitives grammar", "compositional grammar", "DBMS-Nautilus"). Build a mapping `term → canonical_name` and flag every inconsistent usage.
- **R2.2** Every bug class ID (BC001, BC002, ...) must be either sequential or accompanied by an explanation for gaps. Flag unexplained gaps (e.g., missing BC005, BC007).
- **R2.3** Every CVE ID must follow the format `CVE-YYYY-NNNNN` consistently. Flag abbreviated forms (e.g., "13434" vs "CVE-2020-13434").
- **R2.4** Define every unit of measurement (campaign, run, version-run, crash, hash, bug class) in **exactly one place** and verify every usage matches that definition.
- **R2.5** Cross-check the number of runs declared in setup against the number of runs appearing in results. Example: if setup says "5 runs × 4 versions × 2 grammars = 40 campaigns for RQ3", verify results actually contain 40 campaigns.

## Group 3: Statistical Integrity

Statistical claims must be reproducible and complete.

- **R3.1** Every statistical claim (mean, std, p-value, effect size) must be re-computed from raw data. Flag any deviation.
- **R3.2** Every p-value must be accompanied by: test name, sample size, and effect size. Flag missing components.
- **R3.3** Every percentage or ratio must be verified by formula. Example: "61.5% lower" → check `(baseline - proposed) / baseline = 0.615`.
- **R3.4** Every "N×" claim (e.g., "79× more") must be verified: numerator, denominator, and the division.
- **R3.5** Flag every statistical claim without an associated sample size (e.g., "reliably found" without stating in how many runs).

## Group 4: Claims vs Evidence

Conclusions must not exceed what the data shows.

- **R4.1** For every concluding sentence containing words like "directs", "causes", "proves", "demonstrates", "shows that": verify the evidence is strong enough. If only correlation is shown, suggest replacing with "suggests", "is consistent with", or "indicates".
- **R4.2** Flag every claim based on **one** data point (n=1). Example: "providing evidence for X" where X occurs only once — suggest weakening to "an example of X".
- **R4.3** Every claim labeled "novel" or "previously unreported" must have evidence: searches in CVE database, bug tracker, prior work. Record the search query and results.
- **R4.4** Every quantitative claim in the abstract or summary must appear identically in the results section. Flag mismatches.

## Group 5: Reproducibility

The experiments must be reproducible from the chapter alone.

- **R5.1** Verify the setup contains: git commit hash, random seed (if applicable), exact command line, environment versions.
- **R5.2** Every hyperparameter (timeout, tree size, duration, threshold, top-N) must have a justification: pilot study, prior work citation, or resource constraint. Flag every "magic number" without justification.
- **R5.3** Verify every figure has a generation script. Record `figure → script → input_data` in data governance.
- **R5.4** Every table must have a generation script. Flag manually created tables (high risk of error).

## Group 6: Honesty and Completeness

Negative results and exclusions must be transparent.

- **R6.1** List every **negative result** in the raw data (failed runs, missed CVEs, anomalies). Verify they are reported in the thesis. If raw data contains them but the thesis omits them, flag and require explanation.
- **R6.2** Every exclusion must have a documented reason. Example: "CVE-2019-19646 excluded" — what is the reason? Is it consistent?
- **R6.3** Flag every anomalous data point (outlier, run with metric far from peers) not mentioned in the thesis.
- **R6.4** Verify every figure caption accurately describes what the figure shows. Caption and figure must not disagree.
- **R6.5** If raw data contains bugs/crashes/results not appearing in the thesis, record them in data governance as `EXCLUDED` with a reason. No silent drops allowed.

## Output Format

The review produces two files:

### `data_governance.md`

```markdown
# Data Governance Report

## 1. Data Sources Inventory
| Campaign ID | Raw log file | Timestamp | Grammar version | SQLite version |

## 2. Number-to-Source Mapping
| Number in thesis | Location (sec/table/fig) | Source file | How computed |

## 3. Terminology Consistency Report
| Term variant | Locations | Canonical form | Action |

## 4. Statistical Re-computation
| Claim | Thesis value | Re-computed value | Match? |

## 5. Excluded Data
| Data point | Reason for exclusion | Documented in thesis? |

## 6. Reproducibility Checklist
- [ ] Git commit hash recorded
- [ ] All hyperparameters justified
- [ ] All figures have generation scripts
- [ ] All tables have generation scripts
```

### `flagged_issues.md`

```markdown
# Flagged Issues

## Priority 1 (Critical — fix before next advisor meeting)
- [ ] ORPHAN_NUMBER: ...
- [ ] INCONSISTENCY: ...
- [ ] UNREPORTED_NEGATIVE: ...

## Priority 2 (Important — fix before submission)
- [ ] WEAK_CLAIM: ...
- [ ] MISSING_JUSTIFICATION: ...

## Priority 3 (Polish)
- [ ] FORMATTING: ...
- [ ] STYLE: ...
```

## Review Order

Apply rule groups in this order:
1. Group 1 (traceability) — without traceable data, nothing else can be verified
2. Group 2 (consistency) — easy to fix, high impact on reader trust
3. Group 3 (statistics) — affects credibility of main claims
4. Group 6 (honesty) — affects research integrity
5. Group 4 (claims vs evidence) — affects scientific validity
6. Group 5 (reproducibility) — affects long-term value