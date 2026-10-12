"""Figure 1: Estimated oil spill damages vs. the federal liability figure.
Built from the student's spec (capabilities/economic-research/spec.md, section 3).
Inputs are all from the spec: $55,000 and $135,000 per barrel, $725.7M, 16,996 bbl.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Liberation Serif", "Tinos", "DejaVu Serif"]

COST_KAL, COST_YEL = 55_000, 135_000          # $ per barrel (spec, Rows 21, 22)
LIMIT_M = 725.7                                # $ millions (spec, Row 17)
WCD = 16_996                                   # barrels (spec, Row 6)
BLUE, ORANGE, INK, MUTED = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e"

x = np.linspace(0, 20_000, 400)
kal = x * COST_KAL / 1e6
yel = x * COST_YEL / 1e6
x_kal = LIMIT_M * 1e6 / COST_KAL               # ~13,195
x_yel = LIMIT_M * 1e6 / COST_YEL               # ~5,376

fig, ax = plt.subplots(figsize=(6.5, 4.3), dpi=300)
ax.plot(x, kal, color=BLUE, lw=2, ls="-", label="Kalamazoo-based estimate ($55,000 per barrel)")
ax.plot(x, yel, color=ORANGE, lw=2, ls="--", label="Yellowstone-based estimate ($135,000 per barrel)")
ax.axhline(LIMIT_M, color=INK, lw=1.4, ls=":", label="Federal liability figure ($725.7 million)")
ax.axvline(WCD, color=MUTED, lw=1.2, ls="-.", label="EIS worst-case discharge (16,996 barrels)")

# crossing points
for xv, col, dx, ha in [(x_yel, ORANGE, 350, "left"), (x_kal, BLUE, 350, "left")]:
    ax.plot(xv, LIMIT_M, "o", ms=7, color=col, mec="white", mew=1.5, zorder=5)
ax.annotate(f"≈{x_yel:,.0f} barrels", (x_yel, LIMIT_M), xytext=(x_yel - 300, LIMIT_M + 330),
            fontsize=8.5, color=INK, ha="center",
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.annotate(f"≈{x_kal:,.0f} barrels", (x_kal, LIMIT_M), xytext=(x_kal + 150, LIMIT_M - 330),
            fontsize=8.5, color=INK, ha="center",
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))

# values at the worst-case discharge
for yv, col in [(WCD * COST_KAL / 1e6, BLUE), (WCD * COST_YEL / 1e6, ORANGE)]:
    ax.plot(WCD, yv, "o", ms=6, color=col, mec="white", mew=1.5, zorder=5)
ax.text(WCD - 250, WCD * COST_YEL / 1e6 + 80, f"${WCD*COST_YEL/1e6:,.0f}M", fontsize=8.5, ha="right", color=INK)
ax.text(WCD - 250, WCD * COST_KAL / 1e6 + 70, f"${WCD*COST_KAL/1e6:,.0f}M", fontsize=8.5, ha="right", color=INK)

ax.set_xlim(0, 20_000)
ax.set_ylim(0, 2_800)
ax.set_xlabel("Number of barrels spilled", fontsize=10)
ax.set_ylabel("Estimated damages (millions of U.S. dollars)", fontsize=10)
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"{v:,.0f}"))
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"${v:,.0f}"))
ax.tick_params(labelsize=9)
ax.grid(True, color="#e6e5e1", lw=0.6)
ax.set_axisbelow(True)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(loc="upper left", fontsize=8.2, frameon=False)

fig.text(0.01, 0.005,
         "Note. Author's calculations; straight lines assume a fixed cost per barrel. Worst-case discharge from the U.S. Army Corps of\n"
         "Engineers (2025); liability figure from 33 C.F.R. § 138.230(c); cost per barrel from The Official Price (2013) and Associated Press (2011).\n"
         "The liability figure is not DAPL's confirmed insurance or financial assurance.",
         fontsize=7.4, color=MUTED, ha="left", va="bottom")
fig.tight_layout(rect=(0, 0.09, 1, 1))
fig.savefig("dapl-damages-vs-liability.png", dpi=300, facecolor="white")
print(round(x_yel), round(x_kal), WCD*COST_KAL/1e6, WCD*COST_YEL/1e6)
