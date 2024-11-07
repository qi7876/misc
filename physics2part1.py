import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib.ticker as ticker

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

k = 171
I_H = 5.009
mu_0 = 4 * np.pi * 1e-7
N = 3409
I_M = 0.2000
L = 150.1
D = 19.4


V_01 = 1.09
V_02 = -1.09
V_03 = 1.09
V_04 = -1.09

# 减去0差后在中点附近为正值的规定为V1和V3，为负值的规定为V2和V4
X = [-30.0, -20.0, -12.0, -7.0, -3.0, 0.0, 3.0, 7.0, 12.0, 20.0, 40.0, 75.0]
V_1 = [1.20, 1.33, 1.59, 2.03, 2.66, 3.39, 4.13, 4.87, 5.38, 5.69, 5.85, 5.88]
V_2 = [
    -1.21,
    -1.33,
    -1.58,
    -2.01,
    -2.63,
    -3.35,
    -4.11,
    -4.88,
    -5.38,
    -5.68,
    -5.86,
    -5.89,
]
V_3 = [0.94, 0.82, 0.57, 0.14, -0.52, -1.21, -2.00, -2.76, -3.25, -3.53, -3.71, -3.74]
V_4 = [-0.95, -0.83, -0.56, -0.15, 0.47, 1.23, 2.01, 2.75, 3.24, 3.53, 3.70, 3.73]
V_H = []
B = []
B_theory = []
error1 = []
error2 = []


def bTheoryCaculator(x):
    return (
        (mu_0 * N * I_M)
        / (L * 2)
        * (
            np.true_divide(x, np.sqrt(x**2 + D**2 / 4))
            + np.true_divide((L - x), np.sqrt((L - x) ** 2 + D**2 / 4))
        )
    )


for i in range(12):
    V_1[i] = V_1[i] - V_01
    V_2[i] = V_2[i] - V_02
    V_3[i] = V_3[i] - V_03
    V_4[i] = V_4[i] - V_04

    V_H.append((V_1[i] - V_2[i] + V_4[i] - V_3[i]) / 4)
    B.append(V_H[i] / I_H / k * 1000)
    B_theory.append(bTheoryCaculator(X[i]) * 1e6)
    error1.append(B[i] - B_theory[i])
    error2.append(error1[i] / B_theory[i] * 100)

print("V1 - V01:\n", V_1)
print("V2 - V02:\n", V_2)
print("V3 - V03:\n", V_3)
print("V4 - V04:\n", V_4)
print("VH:\n", V_H)
print("B:\n", B)
print("B理论值:\n", B_theory)
print("误差:\n", error1)
print("相对误差:\n", error2)

plt.plot(
    X,
    B,
    label="B",
    color="k",
    linewidth=1,
    marker="o",
    markersize=4,
    markerfacecolor="k",
)
plt.plot(
    X,
    B_theory,
    label="B理论值",
    color="k",
    linewidth=1,
    marker="x",
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

plt.title("B的测量值和真实值随x的变化曲线")
plt.xlabel("x/mm", loc="right")
plt.ylabel("B/mT", loc="top")

plt.legend()
plt.show()
