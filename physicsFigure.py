from matplotlib import rcParams

rcParams["font.family"] = "Heiti TC"  # For Chinese characters
rcParams["axes.unicode_minus"] = False

X = range(0, 80)
Y1 = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    101,
    300,
    479,
    618,
    721,
    777,
    748,
    614,
    436,
    282,
    183,
    137,
    274,
    727,
    1152,
    1428,
    1549,
    1529,
    1350,
    1000,
    607,
    329,
    193,
    164,
    503,
    1109,
    1638,
    1979,
    2122,
    2092,
    1890,
    1518,
    1064,
    684,
    434,
    358,
    703,
    1187,
    1684,
    2074,
    2319,
    2412,
    2344,
    2115,
    1763,
    1386,
    1045,
    868,
    970,
    1245,
    1614,
    1988,
    2312,
    2545,
    2658,
    2639,
    2491,
    2248,
    1956,
    1732,
    1619,
    1662,
    1819,
    2062,
    2339,
    2612,
    2843,
    2999,
    3061,
    3027,
]

Y2 = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    94,
    336,
    598,
    842,
    1037,
    1218,
    1255,
    1101,
    830,
    563,
    378,
    286,
    502,
    1408,
    2330,
    2990,
    3331,
    3362,
    3035,
    2307,
    1434,
    789,
    467,
    387,
    1081,
    2447,
    3676,
    4510,
    4899,
    4882,
    4457,
    3629,
    2582,
    1686,
    1085,
    874,
    1643,
    2778,
    3973,
    4942,
    5588,
    5876,
    5775,
    5275,
    4457,
    3549,
    2708,
    2234,
    2464,
    3127,
    4050,
    5007,
    5864,
    6507,
    6862,
    6883,
    6568,
    5995,
    5271,
    4677,
    4368,
    4457,
    5494,
    6242,
    6998,
    7660,
    8139,
    8379,
    8360,
    8107,
]

for i in range(78):
    if Y1[i + 1] < Y1[i] & Y1[i + 1] < Y1[i + 2]:
        print(i + 1)

print("=======================================")

for i in range(78):
    if Y2[i + 1] < Y2[i] & Y2[i + 1] < Y2[i + 2]:
        print(i + 1)

# plt.plot(X, Y1, label="V-1 = 2.1 V", linestyle="-", color="k")
# plt.plot(X, Y2, label="V-1 = 2.3 V", linestyle="--", color="k")
# plt.xlabel("V-GK / V", loc="right")
# plt.ylabel("I-A / nA", loc="top")
# plt.title("I-A随V-GK变化曲线")
#
# plt.minorticks_on()
# # Customize major ticks (control how many ticks you want)
# plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(10))
# plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(8))
#
# # Customize minor ticks (control minor ticks frequency)
# plt.gca().xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
# plt.gca().yaxis.set_minor_locator(ticker.AutoMinorLocator(8))
# plt.grid(which="both")  # Enable grid for both major and minor ticks
# plt.grid(
#     which="minor", linestyle=":", linewidth="0.5", color="gray"
# )  # Customize minor grid
# plt.grid(which="major", linestyle="-", linewidth="0.8")  # Customize major grid
#
# plt.legend()
# plt.show()
