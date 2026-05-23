# Figure Name Updates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update figure labels from "Proposed (v3.5)" to "DBMS-Nautilus" and "EBNF baseline" to "EBNF-Baseline" across Figures 4.2-4.4, fix legend overlaps and visual issues.

**Architecture:** Edit `scripts/generate_figures.py`, regenerate figures, rebuild thesis PDF.

**Tech Stack:** Python (matplotlib), LaTeX (pdflatex)

---

### Task 1: Update all figure names and fix visual issues

**Files:**
- Modify: `scripts/generate_figures.py`

All three figures use the same naming pattern. Fix them all at once.

- [ ] **Step 1: Update Figure 4.3 (coverage growth) — plot_f3()**

In `plot_f3()` (around line 359-384):

Change line 365:
```python
    ax.plot(t_v35, mean_v35, color=COLOR_V35, linewidth=2, label="Proposed (v3.5)")
```
to:
```python
    ax.plot(t_v35, mean_v35, color=COLOR_V35, linewidth=2, label="DBMS-Nautilus")
```

Change line 369:
```python
    ax.plot(t_ebnf, mean_ebnf, color=COLOR_EBNF, linewidth=2, label="EBNF baseline")
```
to:
```python
    ax.plot(t_ebnf, mean_ebnf, color=COLOR_EBNF, linewidth=2, label="EBNF-Baseline")
```

Change line 375 title:
```python
    ax.set_title("Coverage Growth – Proposed vs. EBNF Baseline (averaged across 4 versions × 5 runs)", fontsize=11)
```
to:
```python
    ax.set_title("Edge Coverage Growth (mean ± 1 std, 4 versions × 5 runs)", fontsize=11)
```

Fix legend overlap — move legend to upper left (away from bars):
```python
    ax.legend(fontsize=11, loc="lower right")
```

- [ ] **Step 2: Update Figure 4.4 (throughput) — plot_f4()**

In `plot_f4()` (around line 424-471):

Change line 453:
```python
                      label="Proposed (v3.5)", color=COLOR_V35, alpha=0.85,
```
to:
```python
                      label="DBMS-Nautilus", color=COLOR_V35, alpha=0.85,
```

Change line 456:
```python
                       label="EBNF baseline", color=COLOR_EBNF, alpha=0.85,
```
to:
```python
                       label="EBNF-Baseline", color=COLOR_EBNF, alpha=0.85,
```

Change line 463 title:
```python
    ax.set_title("Fuzzer Throughput – Proposed vs. EBNF Baseline (mean ± 1 std, 5 runs)", fontsize=11)
```
to:
```python
    ax.set_title("Throughput Comparison (mean ± 1 std, 5 runs)", fontsize=11)
```

Fix figure size for more room:
```python
    fig, ax = plt.subplots(figsize=(8, 5))
```
to:
```python
    fig, ax = plt.subplots(figsize=(9, 5.5))
```

Fix legend overlap — move to upper left:
```python
    ax.legend(fontsize=11, loc="upper left")
```

Fix x-axis labels — horizontal single-line:
```python
    ax.set_xticklabels([f"SQLite\n{v}" for v in VERSIONS], fontsize=10)
```
to:
```python
    ax.set_xticklabels([f"SQLite {v}" for v in VERSIONS], fontsize=10)
```

Increase EBNF bar alpha for cleaner look:
```python
                       label="EBNF-Baseline", color=COLOR_EBNF, alpha=0.85,
```
Keep alpha at 0.85 but add edgecolor for definition:
```python
                       label="EBNF-Baseline", color=COLOR_EBNF, alpha=0.85, edgecolor="#666",
```

- [ ] **Step 3: Update Figure 4.5 (time to first crash) — plot_f5()**

In `plot_f5()` (around line 560-575):

Change line 560:
```python
    make_bp(data_v35,  positions_v35,  COLOR_V35,  "Proposed (v3.5)")
```
to:
```python
    make_bp(data_v35,  positions_v35,  COLOR_V35,  "DBMS-Nautilus")
```

Change line 561:
```python
    make_bp(data_ebnf, positions_ebnf, COLOR_EBNF, "EBNF baseline")
```
to:
```python
    make_bp(data_ebnf, positions_ebnf, COLOR_EBNF, "EBNF-Baseline")
```

Change line 567 title:
```python
    ax.set_title("Time to First UBSan/ASan Crash – Proposed vs. EBNF Baseline (5 runs)", fontsize=11)
```
to:
```python
    ax.set_title("Time to First Crash (5 runs per version)", fontsize=11)
```

Fix x-axis labels — horizontal:
```python
    ax.set_xticklabels([f"SQLite\n{v}" for v in VERSIONS], fontsize=10)
```
to:
```python
    ax.set_xticklabels([f"SQLite {v}" for v in VERSIONS], fontsize=10)
```

- [ ] **Step 4: Also update the color variable comments**

Change line 33-34:
```python
COLOR_V35 = "#2196F3"   # blue – proposed grammar
COLOR_EBNF = "#9E9E9E"  # grey – EBNF baseline
```
to:
```python
COLOR_V35 = "#2196F3"   # blue – DBMS-Nautilus
COLOR_EBNF = "#9E9E9E"  # grey – EBNF-Baseline
```

- [ ] **Step 5: Regenerate all figures**

```bash
cd /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2
python3 scripts/generate_figures.py
```

- [ ] **Step 6: Build PDF and verify figures**

```bash
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH" && cd docs/thesis/v2 && pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out thesis.tex
```

- [ ] **Step 7: Commit and push**

```bash
git add scripts/generate_figures.py docs/thesis/v2/figures/fig_4_3_coverage_growth.pdf docs/thesis/v2/figures/fig_4_4_throughput.pdf docs/thesis/v2/figures/fig_4_5_time_to_first_crash.pdf
git commit -m "docs: update figure labels to DBMS-Nautilus/EBNF-Baseline, fix legend overlaps"
git push origin mit-main
```
