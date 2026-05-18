# Writing Constraints for "Experiments and Evaluation" Chapter

Below is a set of rules for "Experiments and Evaluation" Chapter
---

## 1. Structural Constraints

The chapter must follow this exact 6-section order, numbered X.1 → X.6:

1. **X.1 Research Questions** — pose 4-5 RQs, each with a short name in parentheses (e.g., *RQ1 (Bug Detection Capability)*).
2. **X.2 Dataset and Experimental Setup** — split into 4 subsections: Subjects under test, Seed/Input dataset, Environment, Experimental configuration.
3. **X.3 Baseline Methods** — 4-5 baselines, each representing **a distinct research direction** (not just variants of the same method). Include one weak baseline and one state-of-the-art baseline.
4. **X.4 Evaluation Metrics** — 4-5 metrics, each tied to a specific RQ. At least one metric must have a formal mathematical formula.
5. **X.5 Experimental Results** — exactly one subsection per RQ, in the same order as section X.1. Each subsection must contain a results table or figure.
6. **X.6 Analysis and Discussion** — must include 5 sub-parts: qualitative analysis, in-depth comparison with baselines, failure cases & limitations, threats to validity, summary.

## 2. Content Constraints

**Research Questions (X.1):**
- Each RQ targets a single dimension (effectiveness, efficiency, quality, ablation, etc.).
- One RQ must be an ablation/component-analysis question.
- Phrase RQs as actual questions ending with "?", not as statements.

**Experimental Setup (X.2):**
- Subjects table must include: name, version, type/category, scale (e.g., LOC, parameters, dataset size).
- Subject selection must be justified by **three criteria** (popularity, diversity, accessibility/reproducibility).
- Specify exact hardware: CPU model, RAM, storage, OS version.
- State the **number of repetitions** (≥ 3) and **time budget per run** — report mean ± standard deviation.

**Baselines (X.3):**
- Each baseline is presented in a separate paragraph (not a bullet list).
- Each baseline paragraph must state: what it is, who proposed it (with year if academic), what research direction it represents, why it is chosen.
- The proposed method is presented last, in **bold**, with the label *(proposed)*.

**Metrics (X.4):**
- Each metric has: a name in bold, a definition, and the RQ it answers.
- At least one metric must be written as a LaTeX/math formula.
- Avoid trivial metrics (e.g., raw counts without normalization).

**Results (X.5):**
- Every results table reports **mean ± std**, not raw single-run numbers.
- The proposed method's row/column is **bolded** in every table.
- Each subsection ends with a 1-2 sentence interpretation, not just numbers.
- Include at least one ablation table where rows show progressive addition of components.

**Discussion (X.6):**
- Qualitative analysis must categorize results into **3-4 named groups** with percentages.
- Must contain at least one "interesting observation" paragraph that goes beyond the headline numbers.
- Threats to validity must address all three types: **internal, external, construct**.
- Acknowledge at least 3 concrete limitations of the proposed method.

## 3. Tone and Style Constraints

- **Voice:** third-person academic, no "I" or "we" except in standard phrases ("we compare", "we observe").
- **Tense:** past tense for experiments conducted ("was measured", "were tested"); present tense for analysis ("Table 4.2 shows", "the results indicate").
- **Hedging:** use cautious language when interpreting ("suggests", "indicates", "may be due to") rather than absolute claims.
- **No marketing language:** avoid "powerful", "revolutionary", "state-of-the-art" as adjectives for your own method; let the numbers speak.
- **Paragraph length:** 3-6 sentences. Avoid one-sentence paragraphs except for transitions.
- **No bullet lists in body text** — use prose. Bullet lists allowed only inside the RQ section and the Discussion sub-parts when enumerating distinct items.

## 4. Formatting Constraints

- Tables must have: a clear header row, units in headers (%, ms, MB), and the proposed method's row bolded.
- Numbers ≥ 1000 use thousand separators (1,240 not 1240).
- Percentages reported to 1 decimal place (62.4%, not 62% or 62.41%).
- Cross-reference tables and figures explicitly ("Table 4.2 presents...", "Figure 4.1 shows...").
- All RQs are referenced by their short code (RQ1, RQ2, ...) throughout the chapter.

## 5. Quantitative Constraints (rule of thumb)

| Element | Target count |
|---|---|
| Research questions | 4-5 |
| Baseline methods | 4-5 |
| Evaluation metrics | 4-5 |
| Results subsections | = number of RQs |
| Tables | ≥ 4 (one per RQ + one ablation) |
| Discussion sub-parts | 5 |
| Limitations stated | ≥ 3 |
| Repetition runs per config | ≥ 3 |

## 6. Anti-patterns to Avoid

- Do not report only the best run; always aggregate across repetitions.
- Do not cherry-pick metrics — if your method loses on one metric (e.g., throughput), report it honestly and explain why.
- Do not skip the "threats to validity" section; reviewers expect it.
- Do not introduce new methods or design decisions in this chapter — those belong in the Methodology chapter.
- Do not use vague descriptors like "much better", "significantly faster" without numbers or statistical tests.

---