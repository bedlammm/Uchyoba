import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x_sym = sp.Symbol('x')
y_sym = sp.log(sp.cos(x_sym))
dy_dx = sp.diff(y_sym, x_sym)
L_expr = sp.sqrt(1 + dy_dx**2).simplify()
L_sym = sp.integrate(L_expr, (x_sym, 0, sp.pi/4))
L_val = float(L_sym.evalf())
print(f"Аналитический интеграл длины: {L_sym}")
print(f"Численное значение: {L_val:.4f}")
x_num = np.linspace(0, np.pi/4, 100)
y_num = np.log(np.cos(x_num))
plt.figure(figsize=(8, 6))
plt.plot(x_num, y_num, 'b-', linewidth=2, label='y = ln(cos x)')
plt.scatter([0, np.pi/4], [np.log(np.cos(0)), np.log(np.cos(np.pi/4))], color='red', zorder=5, label='Границы')
plt.title(f'Длина дуги. L = {L_val:.4f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.show()