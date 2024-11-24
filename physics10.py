import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib import rcParams

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

a = 6
b = 10
c = 2
l_g = 0.2

mu_0 = 4 * np.pi * 1e-7

N = 2000

l_c = 2 * (a + b) - 4 * c - l_g
print("l_c =", l_c)


def H_c_calculator(
    I,
    B_g,
    N=N,
    mu_0=mu_0,
    l_g=l_g,
    l_c=l_c,
):
    H_c = (N * I * 0.001 - B_g * 0.001 * l_g * 0.01 / mu_0) / (l_c * 0.01) / 1000
    return H_c


def B_c_calculator(
    B_g,
    sigma=2.4,
):
    B_c = sigma * B_g / 1000
    return B_c


x = [
    -15,
    -14,
    -13,
    -12,
    -11,
    -10,
    -9.5,
    -9,
    -8,
    -7,
    -5,
    -3,
    0,
    3,
    5,
    7,
    8,
    9,
    9.5,
    10,
    11,
    12,
    13,
    14,
    15,
]

B_g_I_600 = [
    64.3,
    79.7,
    103.0,
    143.2,
    228.9,
    413.3,
    489.3,
    502.6,
    511.9,
    514.6,
    516.4,
    517.7,
    520.2,
    521.9,
    523.8,
    525.6,
    527.0,
    525.7,
    477.9,
    383.1,
    219.2,
    148.8,
    101.6,
    80.4,
    64.3,
]

B_g_I_0 = [
    1.2,
    1.4,
    1.8,
    2.5,
    3.8,
    6.8,
    8.4,
    8.5,
    8.7,
    8.7,
    8.7,
    8.7,
    8.7,
    8.8,
    8.9,
    8.9,
    9.0,
    9.0,
    8.6,
    6.6,
    3.8,
    2.4,
    1.8,
    1.4,
    1.1,
]

I_m_4 = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]

B_g_4 = [
    1.7,
    40.8,
    85.6,
    131.4,
    175.4,
    219.4,
    263.9,
    307.8,
    351.6,
    394.5,
    437.3,
    479.8,
    519.9,
]

I_m_5 = [
    600,
    550,
    500,
    450,
    400,
    350,
    300,
    250,
    200,
    150,
    100,
    50,
    0,
    -50,
    -100,
    -150,
    -200,
    -250,
    -300,
    -350,
    -400,
    -450,
    -500,
    -550,
    -600,
    -550,
    -500,
    -450,
    -400,
    -350,
    -300,
    -250,
    -200,
    -150,
    -100,
    -50,
    0,
    50,
    100,
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600,
]
B_g_5 = [
    532.2,
    494.5,
    453.6,
    411.1,
    367.6,
    323.3,
    279.0,
    234.6,
    189.8,
    144.8,
    100.3,
    55.5,
    9.5,
    -36.8,
    -83.6,
    -129.4,
    -174.1,
    -218.7,
    -263.3,
    -306.9,
    -351.1,
    -394.3,
    -437.6,
    -478.9,
    -519.8,
    -490.9,
    -452.3,
    -411.0,
    -367.9,
    -323.7,
    -279.2,
    -234.6,
    -190.5,
    -145.5,
    -100.6,
    -54.9,
    -9.0,
    37.5,
    85.1,
    130.9,
    176.1,
    220.3,
    265.6,
    311.5,
    353.2,
    397.1,
    440.4,
    482.4,
    524.7,
]

H_c_0 = []
B_c_0 = []

H_c_1 = []
B_c_1 = []

for i in range(len(I_m_4)):
    H_c_0.append(H_c_calculator(I_m_4[i], B_g_4[i]))
    B_c_0.append(B_c_calculator(B_g_4[i]))

    print(f"I = {I_m_4[i]}, H_c = {round(H_c_0[-1], 2)}, B_c = {round(B_c_0[-1], 2)}")

print("=====================================")

for i in range(len(I_m_5)):
    counter = 0
    H_c_1.append(H_c_calculator(I_m_5[i], B_g_5[i]))
    B_c_1.append(B_c_calculator(B_g_5[i]))
    counter += 1

    print(f"I = {I_m_5[i]}, H_c = {round(H_c_1[-1], 2)}, B_c = {round(B_c_1[-1], 2)}")

print("=====================================")


plt.plot(
    H_c_0,
    B_c_0,
    label="基本磁化曲线",
    color="k",
    linewidth=1,
    marker="o",
    markersize=4,
    markerfacecolor="k",
)
plt.plot(
    H_c_1,
    B_c_1,
    label="磁滞回线",
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

plt.title("样品的基本磁化曲线和磁滞回线")
plt.xlabel("Bc/T", loc="right")
plt.ylabel("Hc/kA/m", loc="top")

plt.legend()
plt.show()
