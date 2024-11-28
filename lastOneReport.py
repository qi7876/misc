import last_one_functions as l
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

from last_one_functions import B_2, U

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

R = 80.0
I_M = 0.1
miu0 = 4 * np.pi * 1e-7
N = 520

U_E = [2.00, 4.00, 5.00, 6.00, 8.00]

U_1 = [9.36, 18.65, 23.72, 28.18, 36.92]

U_2 = [-10.61, -21.41, -26.97, -31.92, -40.70]

U_average_1 = []

S_1 = []

x = [40.0, 60.0, 80.0, 100.0, 110.0, 120.0, 130.0, 140.0, 160.0, 180.0, 200.0]

x_a = [-40.0, -20.0, 0.0, 20.0, 30.0, 40.0, 50.0, 60.0, 80.0, 100.0, 120.0]

U_a_1 = [10.13, 13.92, 16.22, 15.51, 14.07, 12.23, 10.29, 8.45, 5.32, 3.11, 1.62]
U_a_2 = [
    -13.77,
    -17.56,
    -19.74,
    -18.94,
    -17.53,
    -15.72,
    -13.85,
    -11.91,
    -8.80,
    -6.61,
    -5.13,
]

U_a = []
B_a = []

x_b = [-120.0, -100.0, -80.0, -60.0, -50.0, -40.0, -30.0, -20.0, 0.0, 20.0, 40.0]

U_b_1 = [1.02, 2.21, 3.99, 6.65, 8.29, 10.12, 12.05, 13.90, 16.12, 15.41, 12.23]
U_b_2 = [
    -4.61,
    -5.81,
    -7.59,
    -10.33,
    -11.97,
    -13.80,
    -15.79,
    -17.56,
    -19.82,
    -19.11,
    -15.89,
]

U_b = []
B_b = []

x_a_b = [-80.0, -60.0, -40.0, -20.0, -10.0, 0.0, 10.0, 20.0, 40.0, 60.0, 80.0]
U_apb_1 = [13.01, 17.98, 21.82, 23.41, 23.59, 23.60, 23.60, 23.59, 22.92, 20.24, 15.75]
U_apb_2 = [
    -16.46,
    -21.2,
    -24.97,
    -26.55,
    -26.72,
    -26.73,
    -26.74,
    -26.74,
    -26.12,
    -23.48,
    -19.11,
]

U_apb = []
B_apb = []

B_a_p_B_b = []

E_1 = []

U_amb_1 = [7.55, 10.23, 10.77, 7.29, 4.06, 0.25, -3.69, -7.48, -13.01, -14.47, -12.65]
U_amb_2 = [-11.02, -13.64, -14.17, -10.78, -7.58, -3.82, 0.20, 4.05, 9.52, 10.98, 9.13]

U_amb = []
B_amb = []

B_a_m_B_b = []

E_2 = []

U_1_all = [U_a_1, U_b_1, U_apb_1, U_amb_1]
U_2_all = [U_a_2, U_b_2, U_apb_2, U_amb_2]
U_all = [U_a, U_b, U_apb, U_amb]
B_all = [B_a, B_b, B_apb, B_amb]

B_theory_O_1 = l.B_2(miu0, R, 0, N, I_M) * 1e6
print(f"B_theory_O_1: {B_theory_O_1}")

for i in range(len(U_E)):
    U_average_1.append(l.U(U_1[i], U_2[i]))
    S_1.append(l.S(U_average_1[i], U_E[i], B_theory_O_1))

print(f"U_average_1: {U_average_1}")
print(f"S_1: {S_1}")

S_2 = 8.67
U_E = 5
length = len(U_a_1)

for i in range(4):
    for j in range(len(U_a_1)):
        U_all[i].append(l.U(U_1_all[i][j], U_2_all[i][j]))
        B_all[i].append(l.B_test(U_all[i][j], U_E, S_2))

for i in range(len(B_a)):
    B_a_p_B_b.append(B_a[i] + B_b[i])
    B_a_m_B_b.append(B_a[i] - B_b[i])
    E_1.append(100 * (B_a_p_B_b[i] - B_apb[i]) / B_apb[i])
    E_2.append(100 * (B_a_m_B_b[i] - B_amb[i]) / B_amb[i])

print("U_a:", U_a)
print("U_b:", U_b)
print("U_apb:", U_apb)
print("U_amb:", U_amb)

print("B_a:", B_a)
print("B_b:", B_b)
print("B_apb:", B_apb)
print("B_a_p_B_b:", B_a_p_B_b)
print("B_amb:", B_amb)
print("B_a_m_B_b:", B_a_m_B_b)

print("E_1:", E_1)
print("E_2:", E_2)

plt.plot(
    x,
    U_a,
    label="U_a",
    color="k",
    linewidth=1,
    marker="o",
    markersize=4,
    markerfacecolor="k",
)

plt.plot(
    x,
    U_b,
    label="U_b",
    color="k",
    linewidth=1,
    marker="x",
    markersize=4,
    markerfacecolor="k",
)

plt.plot(
    x,
    U_apb,
    label="U_a+b",
    color="k",
    linewidth=1,
    marker="s",
    markersize=4,
    markerfacecolor="k",
)

plt.plot(
    x,
    U_amb,
    label="U_a-b",
    color="k",
    linewidth=1,
    marker="*",
    markersize=4,
    markerfacecolor="k",
)

plt.minorticks_on()
# Customize major ticks (control how many ticks you want)
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(10))
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(6))

# Customize minor ticks (control minor ticks frequency)
plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
plt.grid(which="both")  # Enable grid for both major and minor ticks
plt.grid(
    which="minor", linestyle=":", linewidth="0.5", color="gray"
)  # Customize minor grid
plt.grid(which="major", linestyle="-", linewidth="0.8")  # Customize major grid

plt.title("轴线传感电压测量值随x的变化曲线")
plt.xlabel("x/mm", loc="right")
plt.ylabel("U/mV", loc="top")

plt.legend()
plt.show()
