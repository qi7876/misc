import last_one_functions as l
import numpy as np

U_x_p = -1.77
U_x_m = 1.0
U_y_p = -0.26
U_y_m = -0.56
U_z_p = -1.98
U_z_m = 1.26

U_x = l.U(U_x_p, U_x_m)
U_y = l.U(U_y_p, U_y_m)
U_z = l.U(U_z_p, U_z_m)

B_x = l.B_test(U_x, 5, 8.67)
B_y = l.B_test(U_y, 5, 8.67)
B_z = l.B_test(U_z, 5, 8.67)

B_parallel = np.sqrt(np.power(B_x, 2) + np.power(B_y, 2))
B_earth = np.sqrt(np.power(B_parallel, 2) + np.power(B_z, 2))

theta = np.arctan(B_y / B_x)
beta = np.arctan(B_z / B_parallel)

print("U x y z:", U_x, U_y, U_z)
print("B x y z:", B_x, B_y, B_z)

print("B_parallel:", B_parallel)
print("B_earth:", B_earth)

print("theta:", theta)
print("beta:", beta)
