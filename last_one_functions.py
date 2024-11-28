import numpy as np


def U(u_1, u_2):
    return (u_1 - u_2) / 2


def S(U, U_E, B_test):
    return U / (U_E * B_test)


def B_test(U, U_E, S):
    return U / (U_E * S)


def B_1(miu0, R, x, N, I):
    return (
        (miu0 * np.power(R, 2))
        / (2 * np.power((np.power(R, 2) + np.power(x, 2)), 3 / 2))
        * N
        * I
    )


def B_2(miu0, R, x, N, I):
    return (
        miu0
        * np.power(R, 2)
        * N
        * I
        * (
            np.power((np.power(R, 2) + np.power(R / 2 + x, 2)), -3 / 2)
            + np.power((np.power(R, 2) + np.power(R / 2 - x, 2)), -3 / 2)
        )
        / 2
    )
