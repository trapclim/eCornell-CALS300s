import matplotlib.pyplot as plt

# Data (reconstructed from the demo)
decades = ["Hist.", "2030s", "2050s", "2080s"]
values = [10, 20, 35, 55]

# Asymmetric error bars (only nonzero where uncertainty was shown)
lower_errors = [0, 5, 10, 15]   # midpoint - lower bound
upper_errors = [0, 5, 10, 20]   # upper bound - midpoint
yerr = [lower_errors, upper_errors]

# Modern font settings
plt.rcParams.update({
    "font.size": 14,
    "font.family": "sans-serif"
})

# Light red → dark red gradient (matching demo style)
colors = ["#f4cccc", "#ea9999", "#cc0000", "#990000"]

# 4:6 portrait figure
plt.figure(figsize=(4, 6))

plt.bar(decades, values, yerr=yerr, capsize=6, color=colors)

plt.xlabel("Decade", fontsize=16)
plt.ylabel("Days Above 90°F", fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.tight_layout()
plt.savefig("Elmira90DegExample.png", dpi=600, bbox_inches="tight")
