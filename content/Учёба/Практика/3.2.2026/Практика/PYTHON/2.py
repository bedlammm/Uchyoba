import numpy as np

I = np.eye(3)
print("Исходная единичная матрица 3x3:")
print(I)
new_row = np.array([23, 46, 15])
A = np.vstack([I, new_row])
print("\nРезультирующая матрица:")
print(A)