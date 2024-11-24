import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import rcParams

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

L = [0.25, 0.35, 0.45, 0.55, 0.65, 0.75]

V_pp = [0.0835, 0.0843, 0.0649, 0.0613, 0.0442, 0.0347]

t = [0.821, 0.866, 0.922, 0.972, 1.006, 1.078]

plt.plot(
    L,
    t,
    color="k",
    linewidth=1,
    marker="o",
    markersize=4,
    markerfacecolor="k",
)

plt.minorticks_on()
# Customize major ticks (control how many ticks you want)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(6))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(10))

# Customize minor ticks (control minor ticks frequency)
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(8))
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.grid(which="both")  # Enable grid for both major and minor ticks
plt.grid(
    which="minor", linestyle=":", linewidth="0.5", color="gray"
)  # Customize minor grid
plt.grid(which="major", linestyle="-", linewidth="0.8")  # Customize major grid

plt.title("信号峰值对应的时间位置t随天线间距L变化的关系图")
plt.xlabel("L/m", loc="right")
plt.ylabel("t/ns", loc="top")

plt.legend()
plt.show()