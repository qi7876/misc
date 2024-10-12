import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

k = 171
I_H = 5.009
mu_0 = 4 * np.pi * 1e-7
N = 3409
L = 150.1
D = 19.4


V_01 = 1.04
V_02 = -1.06
V_03 = 1.04
V_04 = -1.05

I_M = [
    0.0000,
    0.0200,
    0.0400,
    0.0600,
    0.0800,
    0.1000,
    0.1200,
    0.1400,
    0.1600,
    0.1800,
    0.2000,
    0.2200,
]
# 减去0差后在中点附近为正值的规定为V1和V3，为负值的规定为V2和V4
V_1 = [1.05, 1.53, 2.01, 2.48, 2.97, 3.45, 3.93, 4.42, 4.90, 5.38, 5.86, 6.34]
V_2 = [
    -1.05,
    -1.53,
    -2.02,
    -2.50,
    -2.98,
    -3.46,
    -3.95,
    -4.42,
    -4.90,
    -5.39,
    -5.87,
    -6.35,
]
V_3 = [1.04, 0.55, 0.07, -0.39, -0.88, -1.36, -1.84, -2.32, -2.8, -3.27, -3.76, -4.25]
V_4 = [-1.05, -0.57, -0.08, 0.37, 0.87, 1.34, 1.83, 2.31, 2.77, 3.26, 3.73, 4.23]
V_H = []
B = []

for i in range(12):
    V_1[i] = V_1[i] - V_01
    V_2[i] = V_2[i] - V_02
    V_3[i] = V_3[i] - V_03
    V_4[i] = V_4[i] - V_04

    V_H.append((V_1[i] - V_2[i] + V_4[i] - V_3[i]) / 4)
    B.append(V_H[i] / I_H / k * 1000)

print("V1 - V01:\n", V_1)
print("V2 - V02:\n", V_2)
print("V3 - V03:\n", V_3)
print("V4 - V04:\n", V_4)
print("VH:\n", V_H)
print("B:\n", B)


plt.plot(
    I_M,
    B,
    label="B",
    color="k",
    linewidth=1,
    marker="o",
    markersize=4,
    markerfacecolor="k",
)
plt.minorticks_on()
# Customize major ticks (control how many ticks you want)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(14))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(8))

# Customize minor ticks (control minor ticks frequency)
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(8))
plt.grid(which="both")  # Enable grid for both major and minor ticks
plt.grid(
    which="minor", linestyle=":", linewidth="0.5", color="gray"
)  # Customize minor grid
plt.grid(which="major", linestyle="-", linewidth="0.8")  # Customize major grid

plt.title("B的测量值随I_M的变化曲线")
plt.xlabel("I_M/A", loc="right")
plt.ylabel("B/mT", loc="top")

plt.legend()
plt.show()
