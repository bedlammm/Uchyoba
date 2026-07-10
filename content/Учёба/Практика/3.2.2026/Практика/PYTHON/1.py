import numpy as np
import matplotlib.pyplot as plt

# Область определения функции
x = np.linspace(-5, 5, 400)
# Значения функции (векторизованная операция numpy)
y = 4 * x**2 - 2 * x + 6
# График
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('#4d4d4d')
ax.plot(x, y, color='yellow', linestyle='-.', linewidth=2, label='f(x) = 4x² - 2x + 6')
ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.legend()

plt.show()