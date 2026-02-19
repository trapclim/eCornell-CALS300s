import matplotlib.pyplot as plt


def carbon_budget_panel(ax, hist, rem_low, rem_mod, year_label):
    y_hist, y_low, y_mod = 1.0, 0.0, -1.0

    # Historical emissions (left)
    ax.barh(y_hist, -hist, left=0, height=0.6, color="black")

    # Remaining budgets (right)
    ax.barh(y_low, rem_low, left=0, height=0.6, color="#f2b6b6")  # pale red (1.5)
    ax.barh(y_mod, rem_mod, left=0, height=0.6, color="#8b0000")  # dark red (2.0)

    # Center divider
    ax.axvline(0, linewidth=2, color="black")

    # Title only
    ax.set_title(f"Carbon Budget — {year_label}", fontsize=16, pad=15)

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xlim(-hist * 1.1, max(rem_low, rem_mod) * 1.1)
    ax.set_ylim(-2, 2)


fig, axes = plt.subplots(2, 1, figsize=(8, 6))

# Panel 1 — 2019 data
carbon_budget_panel(
    axes[0],
    hist=2560,
    rem_low=400,
    rem_mod=1150,
    year_label="2019",
)

# Panel 2 — 2024 data
carbon_budget_panel(
    axes[1],
    hist=2720,
    rem_low=220,
    rem_mod=1000,
    year_label="2024",
)

plt.tight_layout()
fig.savefig("carbon_budget_combined.png", dpi=300, bbox_inches="tight")
plt.show()
