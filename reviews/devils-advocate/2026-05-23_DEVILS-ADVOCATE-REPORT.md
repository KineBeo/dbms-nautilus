# Devil's Advocate Report — DBMS-Nautilus Thesis

**Date:** 2026-05-23
**Method:** Multi-turn debate (3 rounds: Critic → Defense → Adjudication)

## Surviving Critiques

### Critical (threatens core claims)

**C1. No held-out evaluation targets.**
All 4 SQLite versions had CVEs studied during grammar design. The grammar was tuned on the same distribution it's evaluated on. Without a held-out version, generalization rests on the 9 non-CVE incidental findings.
- **Defense attempted:** RQ2 finds 9 non-CVE bugs beyond design targets; 4 CVEs rediscovered compositionally without seeds.
- **Adjudication:** Partially addressed. RQ2 mitigates but does not eliminate. A held-out version would be definitive.

**C2. No ablation study.**
The 108x improvement is attributed to "grammar design" as a monolith. Without ablating structural patterns vs weights vs boundary values vs schema templates, cannot identify which design decisions actually matter.
- **Defense attempted:** Controlled comparison isolates grammar design as a whole; ablation informative but not required for the main claim.
- **Adjudication:** Partially addressed. The aggregate claim holds but practical utility is limited without knowing which factor drives the improvement.

### Major (weakens but doesn't invalidate)

**M1. External validity absent.** All claims from one program (SQLite 150K LoC). Applicability to MySQL/PostgreSQL undemonstrated.

**M2. Baseline comparison inflates contribution.** 108x against deliberately minimal EBNF. No comparison with SQLsmith/Squirrel/SQLRight.

**M3. 15-minute campaigns may miss hard compositional bugs.** The methodology should excel at rare multi-step compositions, but the short duration cannot test this.

### Minor

**m1. Methodological novelty is engineering, not science.** Acceptable for bachelor thesis.
**m2. Statistical power marginal (n=5).** Effect size large enough to compensate.

### Dismissed

**D1. CVE rediscovery not valuable.** Dismissed — serves as ground-truth validation; RQ2 provides actual contribution.
