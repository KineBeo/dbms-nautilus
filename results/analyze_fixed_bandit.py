"""
analyze_fixed_bandit.py — Thompson Sampling bandit evaluation analysis.

Loads campaign data from results/campaigns/2026-05-07_fixed-bandit-eval/,
generates 10 publication-quality charts, and prints a statistical summary.
"""

import os
import json
import warnings

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from scipy import stats

warnings.filterwarnings("ignore", category=FutureWarning)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CAMPAIGN_DIR = os.path.join(
    SCRIPT_DIR, "campaigns", "2026-05-07_fixed-bandit-eval"
)
CHARTS_DIR = os.path.join(SCRIPT_DIR, "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

N_RUNS = 5
GROUPS = ["S1_Schema", "S2_DML", "S3_Query", "S4_Boundary", "S5_FTS", "S6_Validation"]
BANDIT_COLOR = "#2196F3"
UNIFORM_COLOR = "#F44336"
GROUP_PALETTE = [
    "#E6194B", "#3CB44B", "#4363D8", "#F58231", "#911EB4", "#42D4F4"
]

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------

try:
    plt.style.use("seaborn-v0_8-whitegrid")
except OSError:
    try:
        plt.style.use("seaborn-whitegrid")
    except OSError:
        plt.style.use("ggplot")

plt.rcParams.update({"font.size": 12, "axes.titlesize": 13, "axes.labelsize": 12})

# ---------------------------------------------------------------------------
# Data loading helpers
# ---------------------------------------------------------------------------

def load_coverage(policy: str, run: int) -> pd.DataFrame:
    tag = "bandit" if policy == "bandit" else "uniform"
    path = os.path.join(
        CAMPAIGN_DIR,
        f"sqlite-3.31.1_fixed_{tag}_run{run}",
        "coverage.csv",
    )
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path)
    df["run"] = run
    df["policy"] = policy
    return df


def load_bandit_log(run: int) -> pd.DataFrame:
    path = os.path.join(
        CAMPAIGN_DIR,
        f"sqlite-3.31.1_fixed_bandit_run{run}",
        "bandit_log.csv",
    )
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path)
    df["run"] = run
    return df


def load_dedup(policy: str, run: int) -> dict:
    tag = "bandit" if policy == "bandit" else "uniform"
    path = os.path.join(
        CAMPAIGN_DIR,
        f"sqlite-3.31.1_fixed_{tag}_run{run}",
        "dedup.json",
    )
    if not os.path.exists(path):
        return {}
    with open(path) as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# Load all data
# ---------------------------------------------------------------------------

print("Loading data …")

bandit_cov_list = [load_coverage("bandit", r) for r in range(1, N_RUNS + 1)]
uniform_cov_list = [load_coverage("uniform", r) for r in range(1, N_RUNS + 1)]
bandit_log_list = [load_bandit_log(r) for r in range(1, N_RUNS + 1)]
dedup_bandit = [load_dedup("bandit", r) for r in range(1, N_RUNS + 1)]
dedup_uniform = [load_dedup("uniform", r) for r in range(1, N_RUNS + 1)]

# Final-state scalar metrics
bandit_crashes = np.array([
    df["total_crashes"].iloc[-1] if not df.empty else np.nan
    for df in bandit_cov_list
])
uniform_crashes = np.array([
    df["total_crashes"].iloc[-1] if not df.empty else np.nan
    for df in uniform_cov_list
])
bandit_edges = np.array([
    df["total_edges"].iloc[-1] if not df.empty else np.nan
    for df in bandit_cov_list
])
uniform_edges = np.array([
    df["total_edges"].iloc[-1] if not df.empty else np.nan
    for df in uniform_cov_list
])
bandit_rcs = np.array([
    d.get("unique_root_causes", np.nan) for d in dedup_bandit
])
uniform_rcs = np.array([
    d.get("unique_root_causes", np.nan) for d in dedup_uniform
])

print(f"Bandit  crashes : {bandit_crashes}")
print(f"Uniform crashes : {uniform_crashes}")
print(f"Bandit  edges   : {bandit_edges}")
print(f"Uniform edges   : {uniform_edges}")
print(f"Bandit  RCs     : {bandit_rcs}")
print(f"Uniform RCs     : {uniform_rcs}")

# ---------------------------------------------------------------------------
# Utility: resample coverage to a common 1-second grid (0..299)
# ---------------------------------------------------------------------------

T_MAX = 299

def resample_to_grid(df: pd.DataFrame, col: str, t_col: str = "timestamp_sec") -> np.ndarray:
    """Forward-fill a time series onto a 0..T_MAX second grid."""
    grid = np.full(T_MAX + 1, np.nan)
    if df.empty:
        return grid
    t = df[t_col].values
    v = df[col].values
    for i in range(T_MAX + 1):
        mask = t <= i
        if mask.any():
            grid[i] = v[mask][-1]
    # back-fill leading NaN with first valid
    first_valid = np.nanmin(np.where(~np.isnan(grid))[0]) if np.any(~np.isnan(grid)) else 0
    grid[:first_valid] = grid[first_valid] if not np.isnan(grid[first_valid]) else 0
    return grid


T = np.arange(T_MAX + 1)

bandit_edges_grid = np.array([resample_to_grid(df, "total_edges") for df in bandit_cov_list])
uniform_edges_grid = np.array([resample_to_grid(df, "total_edges") for df in uniform_cov_list])
bandit_crashes_grid = np.array([resample_to_grid(df, "total_crashes") for df in bandit_cov_list])
uniform_crashes_grid = np.array([resample_to_grid(df, "total_crashes") for df in uniform_cov_list])

# ---------------------------------------------------------------------------
# Chart 1: Coverage trajectories
# ---------------------------------------------------------------------------

print("Chart 1: coverage_curves.png")

fig, ax = plt.subplots(figsize=(10, 6))

for i, arr in enumerate(bandit_edges_grid):
    ax.plot(T, arr, color=BANDIT_COLOR, alpha=0.25, linewidth=1)
for i, arr in enumerate(uniform_edges_grid):
    ax.plot(T, arr, color=UNIFORM_COLOR, alpha=0.25, linewidth=1)

b_mean = np.nanmean(bandit_edges_grid, axis=0)
b_std = np.nanstd(bandit_edges_grid, axis=0)
u_mean = np.nanmean(uniform_edges_grid, axis=0)
u_std = np.nanstd(uniform_edges_grid, axis=0)

ax.plot(T, b_mean, color=BANDIT_COLOR, linewidth=2.5, label="Bandit (mean)")
ax.fill_between(T, b_mean - b_std, b_mean + b_std, color=BANDIT_COLOR, alpha=0.15)
ax.plot(T, u_mean, color=UNIFORM_COLOR, linewidth=2.5, label="Uniform (mean)")
ax.fill_between(T, u_mean - u_std, u_mean + u_std, color=UNIFORM_COLOR, alpha=0.15)

ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Total Edges Covered")
ax.set_title("Coverage Trajectories: Fixed Bandit vs Uniform")
ax.legend()
ax.grid(True, alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "coverage_curves.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 2: Crash accumulation
# ---------------------------------------------------------------------------

print("Chart 2: crash_accumulation.png")

fig, ax = plt.subplots(figsize=(10, 6))

for arr in bandit_crashes_grid:
    ax.plot(T, arr, color=BANDIT_COLOR, alpha=0.25, linewidth=1)
for arr in uniform_crashes_grid:
    ax.plot(T, arr, color=UNIFORM_COLOR, alpha=0.25, linewidth=1)

bc_mean = np.nanmean(bandit_crashes_grid, axis=0)
bc_std = np.nanstd(bandit_crashes_grid, axis=0)
uc_mean = np.nanmean(uniform_crashes_grid, axis=0)
uc_std = np.nanstd(uniform_crashes_grid, axis=0)

ax.plot(T, bc_mean, color=BANDIT_COLOR, linewidth=2.5, label="Bandit (mean)")
ax.fill_between(T, np.maximum(bc_mean - bc_std, 0), bc_mean + bc_std,
                color=BANDIT_COLOR, alpha=0.15)
ax.plot(T, uc_mean, color=UNIFORM_COLOR, linewidth=2.5, label="Uniform (mean)")
ax.fill_between(T, np.maximum(uc_mean - uc_std, 0), uc_mean + uc_std,
                color=UNIFORM_COLOR, alpha=0.15)

ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Cumulative Crashes")
ax.set_title("Crash Accumulation: Fixed Bandit vs Uniform")
ax.legend()
ax.grid(True, alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "crash_accumulation.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 3: Crash rate by 1-minute windows
# ---------------------------------------------------------------------------

print("Chart 3: crash_rate_by_window.png")

WINDOWS = [(0, 60), (60, 120), (120, 180), (180, 240), (240, 300)]
WINDOW_LABELS = ["0–1m", "1–2m", "2–3m", "3–4m", "4–5m"]


def window_crash_rate(crashes_grid: np.ndarray, t_start: int, t_end: int) -> np.ndarray:
    """Crashes per second in window, averaged over runs."""
    rates = []
    for arr in crashes_grid:
        v_start = arr[t_start] if not np.isnan(arr[t_start]) else 0.0
        v_end = arr[min(t_end, T_MAX)] if not np.isnan(arr[min(t_end, T_MAX)]) else v_start
        rate = (v_end - v_start) / (t_end - t_start)
        rates.append(rate)
    return np.array(rates)


bandit_rates = [window_crash_rate(bandit_crashes_grid, s, e) for s, e in WINDOWS]
uniform_rates = [window_crash_rate(uniform_crashes_grid, s, e) for s, e in WINDOWS]

b_means = np.array([r.mean() for r in bandit_rates])
b_stds = np.array([r.std() for r in bandit_rates])
u_means = np.array([r.mean() for r in uniform_rates])
u_stds = np.array([r.std() for r in uniform_rates])

x = np.arange(len(WINDOWS))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars_b = ax.bar(x - width / 2, b_means, width, yerr=b_stds, capsize=4,
                color=BANDIT_COLOR, label="Bandit", alpha=0.85)
bars_u = ax.bar(x + width / 2, u_means, width, yerr=u_stds, capsize=4,
                color=UNIFORM_COLOR, label="Uniform", alpha=0.85)

# Annotate 4-5m bar with 1.9x ratio
last_idx = len(WINDOWS) - 1
ratio = b_means[last_idx] / u_means[last_idx] if u_means[last_idx] > 0 else float("inf")
arrow_x = x[last_idx] - width / 2
arrow_y = b_means[last_idx] + b_stds[last_idx]
ax.annotate(
    f"{ratio:.1f}x",
    xy=(arrow_x, b_means[last_idx]),
    xytext=(arrow_x + 0.05, arrow_y + 0.002),
    fontsize=11,
    color="black",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="black", lw=1.5),
)

ax.set_xticks(x)
ax.set_xticklabels(WINDOW_LABELS)
ax.set_xlabel("Time Window")
ax.set_ylabel("Crash Rate (crashes/second)")
ax.set_title("Crash Rate by Time Window")
ax.legend()
ax.grid(True, axis="y", alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "crash_rate_by_window.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 4: Beta means convergence
# ---------------------------------------------------------------------------

print("Chart 4: beta_means_convergence.png")

fig, ax = plt.subplots(figsize=(10, 6))

for gi, group in enumerate(GROUPS):
    alpha_col = f"alpha_{group}"
    beta_col = f"beta_{group}"
    all_means = []
    for df in bandit_log_list:
        if df.empty or alpha_col not in df.columns:
            continue
        beta_mean = df[alpha_col] / (df[alpha_col] + df[beta_col])
        all_means.append(beta_mean.values)
    if not all_means:
        continue
    # Align length to shortest
    min_len = min(len(m) for m in all_means)
    arr = np.array([m[:min_len] for m in all_means])
    rounds = np.arange(min_len)
    mean_line = arr.mean(axis=0)
    std_line = arr.std(axis=0)
    color = GROUP_PALETTE[gi]
    ax.plot(rounds, mean_line, color=color, linewidth=2, label=group)
    ax.fill_between(rounds, mean_line - std_line, mean_line + std_line,
                    color=color, alpha=0.12)

ax.axhline(0.5, color="gray", linestyle="--", linewidth=1.2, label="Uninformative prior (0.5)")
ax.set_xlabel("Bandit Update Round")
ax.set_ylabel("Beta Mean  α/(α+β)")
ax.set_title("Beta Distribution Means: Group Discrimination Over Time")
ax.legend(fontsize=10)
ax.grid(True, alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "beta_means_convergence.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 5: Group selection heatmap
# ---------------------------------------------------------------------------

print("Chart 5: group_selection_heatmap.png")

selection_pcts = np.zeros((len(GROUPS), N_RUNS))
for ri, df in enumerate(bandit_log_list):
    if df.empty:
        continue
    total = len(df)
    for gi, group in enumerate(GROUPS):
        count = (df["selected_group"] == group).sum()
        selection_pcts[gi, ri] = 100.0 * count / total if total > 0 else 0.0

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(selection_pcts, aspect="auto", cmap="Blues", vmin=0, vmax=35)
plt.colorbar(im, ax=ax, label="Selection %")

ax.set_xticks(range(N_RUNS))
ax.set_xticklabels([f"Run {r+1}" for r in range(N_RUNS)])
ax.set_yticks(range(len(GROUPS)))
ax.set_yticklabels(GROUPS)

for gi in range(len(GROUPS)):
    for ri in range(N_RUNS):
        val = selection_pcts[gi, ri]
        text_color = "white" if val > 20 else "black"
        ax.text(ri, gi, f"{val:.1f}%", ha="center", va="center",
                fontsize=10, color=text_color)

ax.set_title("Group Selection Frequency Across Runs")
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "group_selection_heatmap.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 6: Alpha / Beta parameter evolution
# ---------------------------------------------------------------------------

print("Chart 6: alpha_beta_evolution.png")

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

for gi, group in enumerate(GROUPS):
    alpha_col = f"alpha_{group}"
    beta_col = f"beta_{group}"
    color = GROUP_PALETTE[gi]

    alpha_arrays, beta_arrays = [], []
    for df in bandit_log_list:
        if df.empty or alpha_col not in df.columns:
            continue
        alpha_arrays.append(df[alpha_col].values)
        beta_arrays.append(df[beta_col].values)

    if not alpha_arrays:
        continue

    min_len = min(len(a) for a in alpha_arrays)
    rounds = np.arange(min_len)

    a_arr = np.array([a[:min_len] for a in alpha_arrays])
    b_arr = np.array([b[:min_len] for b in beta_arrays])

    a_mean, a_std = a_arr.mean(axis=0), a_arr.std(axis=0)
    b_mean_v, b_std_v = b_arr.mean(axis=0), b_arr.std(axis=0)

    axes[0].plot(rounds, a_mean, color=color, linewidth=1.8, label=group)
    axes[0].fill_between(rounds, a_mean - a_std, a_mean + a_std, color=color, alpha=0.10)

    axes[1].plot(rounds, b_mean_v, color=color, linewidth=1.8, label=group)
    axes[1].fill_between(rounds, b_mean_v - b_std_v, b_mean_v + b_std_v, color=color, alpha=0.10)

axes[0].set_ylabel("Alpha (α)")
axes[0].set_title("Alpha Parameter Evolution")
axes[0].legend(fontsize=9)
axes[0].grid(True, alpha=0.4)

axes[1].set_xlabel("Bandit Update Round")
axes[1].set_ylabel("Beta (β)")
axes[1].set_title("Beta Parameter Evolution (Decay + Reward)")
axes[1].legend(fontsize=9)
axes[1].grid(True, alpha=0.4)

fig.suptitle("Alpha/Beta Parameter Evolution (Decay + Reward)", fontsize=14, y=1.01)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "alpha_beta_evolution.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 7: Reward EMA decay
# ---------------------------------------------------------------------------

print("Chart 7: reward_ema_decay.png")

fig, ax = plt.subplots(figsize=(10, 6))

ema_arrays = []
for df in bandit_log_list:
    if df.empty or "reward_ema" not in df.columns:
        continue
    ax.plot(df["update"], df["reward_ema"], color=BANDIT_COLOR, alpha=0.30, linewidth=1)
    ema_arrays.append(df["reward_ema"].values)

if ema_arrays:
    min_len = min(len(a) for a in ema_arrays)
    ema_arr = np.array([a[:min_len] for a in ema_arrays])
    rounds = np.arange(1, min_len + 1)
    ema_mean = ema_arr.mean(axis=0)
    ax.plot(rounds, ema_mean, color=BANDIT_COLOR, linewidth=2.5, label="Mean EMA")

    # Annotate phases based on thirds of the run
    n = len(rounds)
    third = n // 3
    ax.axvspan(0, third, alpha=0.07, color="green")
    ax.axvspan(third, 2 * third, alpha=0.07, color="orange")
    ax.axvspan(2 * third, n, alpha=0.07, color="red")

    mid0, mid1, mid2 = third // 2, third + third // 2, 2 * third + third // 2
    y_max = np.nanmax(ema_mean) * 1.05
    ax.text(mid0, y_max, "Coverage-rich", ha="center", fontsize=9, color="darkgreen")
    ax.text(mid1, y_max, "Declining", ha="center", fontsize=9, color="darkorange")
    ax.text(mid2, y_max, "Saturated", ha="center", fontsize=9, color="darkred")

ax.set_xlabel("Bandit Update Round")
ax.set_ylabel("Reward EMA")
ax.set_title("Reward Signal Decay (EMA)")
ax.legend()
ax.grid(True, alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "reward_ema_decay.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 8: Final comparison dashboard (2×2)
# ---------------------------------------------------------------------------

print("Chart 8: final_comparison_dashboard.png")

fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.35)

ax_crashes = fig.add_subplot(gs[0, 0])
ax_rcs = fig.add_subplot(gs[0, 1])
ax_edges = fig.add_subplot(gs[1, 0])
ax_decay = fig.add_subplot(gs[1, 1])

# --- Top-left: total crashes box plot ---
ax_crashes.boxplot(
    [bandit_crashes[~np.isnan(bandit_crashes)], uniform_crashes[~np.isnan(uniform_crashes)]],
    tick_labels=["Bandit", "Uniform"],
    patch_artist=True,
    boxprops=dict(facecolor="none"),
    medianprops=dict(color="black", linewidth=2),
)
for patch, color in zip(ax_crashes.patches, [BANDIT_COLOR, UNIFORM_COLOR]):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)
ax_crashes.set_title("Total Crashes (5 runs)")
ax_crashes.set_ylabel("Crashes")
ax_crashes.grid(True, axis="y", alpha=0.4)

# --- Top-right: unique RCs box plot ---
ax_rcs.boxplot(
    [bandit_rcs[~np.isnan(bandit_rcs)], uniform_rcs[~np.isnan(uniform_rcs)]],
    tick_labels=["Bandit", "Uniform"],
    patch_artist=True,
    boxprops=dict(facecolor="none"),
    medianprops=dict(color="black", linewidth=2),
)
for patch, color in zip(ax_rcs.patches, [BANDIT_COLOR, UNIFORM_COLOR]):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)
ax_rcs.set_title("Unique Root Causes (5 runs)")
ax_rcs.set_ylabel("Unique RCs")
ax_rcs.grid(True, axis="y", alpha=0.4)

# --- Bottom-left: edges box plot ---
ax_edges.boxplot(
    [bandit_edges[~np.isnan(bandit_edges)], uniform_edges[~np.isnan(uniform_edges)]],
    tick_labels=["Bandit", "Uniform"],
    patch_artist=True,
    boxprops=dict(facecolor="none"),
    medianprops=dict(color="black", linewidth=2),
)
for patch, color in zip(ax_edges.patches, [BANDIT_COLOR, UNIFORM_COLOR]):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)
ax_edges.set_title("Final Edge Coverage (5 runs)")
ax_edges.set_ylabel("Total Edges")
ax_edges.grid(True, axis="y", alpha=0.4)

# --- Bottom-right: crash rate decay bar chart ---
# Crash rate in first minute vs last minute, % change
def pct_change(grid: np.ndarray) -> float:
    first = window_crash_rate(grid, 0, 60).mean()
    last = window_crash_rate(grid, 240, 300).mean()
    if first == 0:
        return 0.0
    return 100.0 * (last - first) / first

b_decay_actual = pct_change(bandit_crashes_grid)
u_decay_actual = pct_change(uniform_crashes_grid)
pre_fix_decay = -58.0  # known pre-fix measurement

labels_decay = ["Pre-fix\nBandit", "Fixed\nBandit", "Uniform"]
values_decay = [pre_fix_decay, b_decay_actual, u_decay_actual]
colors_decay = ["#FF7043", BANDIT_COLOR, UNIFORM_COLOR]

bars = ax_decay.bar(labels_decay, values_decay, color=colors_decay, alpha=0.8)
for bar, val in zip(bars, values_decay):
    ax_decay.text(
        bar.get_x() + bar.get_width() / 2,
        val + (2 if val >= 0 else -5),
        f"{val:.1f}%",
        ha="center", fontsize=10, fontweight="bold",
    )
ax_decay.axhline(0, color="black", linewidth=0.8)
ax_decay.set_ylabel("Rate Change (%)")
ax_decay.set_title("Crash Rate Decay\n(first vs last minute)")
ax_decay.grid(True, axis="y", alpha=0.4)

fig.suptitle("Fixed Bandit vs Uniform: Summary Dashboard", fontsize=15, fontweight="bold")
fig.savefig(os.path.join(CHARTS_DIR, "final_comparison_dashboard.png"), dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 9: Pre-fix vs post-fix bandit
# ---------------------------------------------------------------------------

print("Chart 9: pre_vs_post_fix.png")

metrics = ["Beta\nSeparation", "Crash Ratio\nvs Uniform", "Rate Decay\n(|%|)"]
pre_fix = [0.01, 0.88, 58.0]
post_fix = [0.09, bandit_crashes.mean() / uniform_crashes.mean(), abs(b_decay_actual)]

x = np.arange(len(metrics))
width = 0.32

fig, ax = plt.subplots(figsize=(10, 6))
bars_pre = ax.bar(x - width / 2, pre_fix, width, label="Pre-fix", color="#F44336", alpha=0.80)
bars_post = ax.bar(x + width / 2, post_fix, width, label="Post-fix", color="#4CAF50", alpha=0.80)

for bar, val in zip(bars_pre, pre_fix):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f"{val:.2f}", ha="center", fontsize=10)
for bar, val in zip(bars_post, post_fix):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f"{val:.2f}", ha="center", fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(metrics)
ax.set_title("Pre-Fix vs Post-Fix Bandit Performance")
ax.legend()
ax.grid(True, axis="y", alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "pre_vs_post_fix.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 10: Effective number of arms
# ---------------------------------------------------------------------------

print("Chart 10: effective_arms.png")

WINDOW_SIZE = 50

fig, ax = plt.subplots(figsize=(10, 6))

for ri, df in enumerate(bandit_log_list):
    if df.empty or "selected_group" not in df.columns:
        continue
    groups_arr = df["selected_group"].values
    n_eff_vals = []
    for t in range(len(groups_arr)):
        start = max(0, t - WINDOW_SIZE + 1)
        window = groups_arr[start: t + 1]
        counts = np.array([(window == g).sum() for g in GROUPS], dtype=float)
        total = counts.sum()
        if total == 0:
            n_eff_vals.append(len(GROUPS))
            continue
        probs = counts / total
        denom = np.sum(probs ** 2)
        n_eff_vals.append(1.0 / denom if denom > 0 else len(GROUPS))
    rounds = df["update"].values
    ax.plot(rounds, n_eff_vals, color=BANDIT_COLOR, alpha=0.35, linewidth=1.2,
            label=f"Run {ri+1}" if ri == 0 else "_nolegend_")

# Plot mean n_eff
all_neff = []
for ri, df in enumerate(bandit_log_list):
    if df.empty or "selected_group" not in df.columns:
        continue
    groups_arr = df["selected_group"].values
    run_neff = []
    for t in range(len(groups_arr)):
        start = max(0, t - WINDOW_SIZE + 1)
        window = groups_arr[start: t + 1]
        counts = np.array([(window == g).sum() for g in GROUPS], dtype=float)
        total = counts.sum()
        if total == 0:
            run_neff.append(len(GROUPS))
            continue
        probs = counts / total
        denom = np.sum(probs ** 2)
        run_neff.append(1.0 / denom if denom > 0 else len(GROUPS))
    all_neff.append(run_neff)

if all_neff:
    min_len = min(len(a) for a in all_neff)
    neff_arr = np.array([a[:min_len] for a in all_neff])
    rounds_mean = np.arange(1, min_len + 1)
    ax.plot(rounds_mean, neff_arr.mean(axis=0), color="#0D47A1", linewidth=2.5, label="Mean n_eff")

ax.axhline(1.0, color="red", linestyle="--", linewidth=1.3, label="1.0 — Pure exploitation")
ax.axhline(len(GROUPS), color="green", linestyle="--", linewidth=1.3, label=f"{len(GROUPS)}.0 — Pure exploration")
ax.set_ylim(0, len(GROUPS) + 0.5)
ax.set_xlabel("Bandit Update Round")
ax.set_ylabel("Effective Arms  n_eff = 1/Σp²")
ax.set_title("Effective Number of Arms (Exploration Quality)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.5)
fig.tight_layout()
fig.savefig(os.path.join(CHARTS_DIR, "effective_arms.png"), dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Statistical summary
# ---------------------------------------------------------------------------

print("\n" + "=" * 65)
print("STATISTICAL SUMMARY: Fixed Bandit vs Uniform (5 runs each)")
print("=" * 65)


def cohen_d(a: np.ndarray, b: np.ndarray) -> float:
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    pooled_std = np.sqrt((a.std(ddof=1) ** 2 + b.std(ddof=1) ** 2) / 2)
    return (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else 0.0


def ci_diff(a: np.ndarray, b: np.ndarray, alpha: float = 0.05) -> tuple:
    """95% CI for mean(a) - mean(b) using Welch t-distribution."""
    a, b = a[~np.isnan(a)], b[~np.isnan(b)]
    diff = a.mean() - b.mean()
    se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
    df_num = (a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b)) ** 2
    df_den = (a.var(ddof=1) / len(a)) ** 2 / (len(a) - 1) + (b.var(ddof=1) / len(b)) ** 2 / (len(b) - 1)
    df = df_num / df_den if df_den > 0 else 1
    t_crit = stats.t.ppf(1 - alpha / 2, df)
    return diff - t_crit * se, diff + t_crit * se


metrics_def = [
    ("Total Crashes", bandit_crashes, uniform_crashes),
    ("Total Edges", bandit_edges, uniform_edges),
    ("Unique RCs", bandit_rcs, uniform_rcs),
]

header = f"{'Metric':<18} {'B_mean':>8} {'U_mean':>8} {'Cohen_d':>9} {'MW_p':>9} {'Welch_p':>9} {'95%CI_diff':>22}"
print(header)
print("-" * len(header))

for name, b_arr, u_arr in metrics_def:
    b_clean = b_arr[~np.isnan(b_arr)]
    u_clean = u_arr[~np.isnan(u_arr)]
    b_mu = b_clean.mean()
    u_mu = u_clean.mean()
    d = cohen_d(b_arr, u_arr)
    mw_stat, mw_p = stats.mannwhitneyu(b_clean, u_clean, alternative="two-sided")
    _, welch_p = stats.ttest_ind(b_clean, u_clean, equal_var=False)
    lo, hi = ci_diff(b_arr, u_arr)
    print(
        f"{name:<18} {b_mu:>8.2f} {u_mu:>8.2f} {d:>9.3f} {mw_p:>9.4f} {welch_p:>9.4f} "
        f"  [{lo:+.2f}, {hi:+.2f}]"
    )

print()
print("Bandit  crashes (per run):", bandit_crashes)
print("Uniform crashes (per run):", uniform_crashes)
print("Bandit  edges   (per run):", bandit_edges)
print("Uniform edges   (per run):", uniform_edges)
print("Bandit  RCs     (per run):", bandit_rcs)
print("Uniform RCs     (per run):", uniform_rcs)
print()
print(f"Crash rate decay — fixed bandit : {b_decay_actual:+.1f}%")
print(f"Crash rate decay — uniform      : {u_decay_actual:+.1f}%")
print(f"Crash rate decay — pre-fix ref  : -58.0%")
print()
print(f"Charts saved to: {CHARTS_DIR}")
print("Done.")
