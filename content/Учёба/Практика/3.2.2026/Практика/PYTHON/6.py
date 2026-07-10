import numpy as np

A = np.array([
[2, 1, 3],
[4, 0, 1],
[5, 2, 3]
])
detA = round(np.linalg.det(A))
print("Матрица A:")
print(A)
print(f"Определитель матрицы A: {detA}")