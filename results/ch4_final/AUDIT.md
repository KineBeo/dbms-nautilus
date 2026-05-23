# Chapter 4 Pipeline Audit

**Generated:** 2026-05-22T06:05:02.691146+00:00  
**Git hash:** `a48c46c9cc94844bd70e1b42c14d316286c75941`  
**Script:** `scripts/ch4_pipeline.py`

## Workdir Inventory

| RQ | Grammar | Expected | Found | Missing |
|---|---|---|---|---|
| RQ1 | DBMS-Nautilus (v35) | 20 | 20 | 0 |
| RQ2 | DBMS-Nautilus (v33) | 20 | 20 | 0 |
| RQ3_proposed | DBMS-Nautilus (v3.4) | 20 | 20 | 0 |
| RQ3_baseline | EBNF-Baseline | 20 | 19 | 1 |

## Missing Workdirs

- `sqlite-3.32.0_comparison_ebnf_run1`

## Output Files

| File | Exists | Rows |
|---|---|---|
| `rq1_cve_hits.csv` | yes | 200 |
| `rq1_ttfc_per_cve.csv` | yes | 28 |
| `rq2_bug_classes.csv` | yes | 13 |
| `rq2_ebnf_bug_classes.csv` | yes | 4 |
| `rq2_per_run_classes.csv` | yes | 39 |
| `rq3_per_campaign.csv` | yes | 39 |
| `rq3_statistical_tests.csv` | yes | 16 |
| `rq3_summary.csv` | yes | 4 |
