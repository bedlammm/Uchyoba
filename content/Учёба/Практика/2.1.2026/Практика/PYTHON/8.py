import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x_sym = sp.Symbol('x')
y_upper = x_sym
y_lower = x_sym**2

V_expr = sp.pi * (y_upper**2 - y_lower**2)
V_sym = sp.integrate(V_expr, (x_sym, 0, 1))

print(f"Точное значение объема: {V_sym}")
print(f"Численное значение: {float(V_sym.evalf()):.4f}")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Параметризация поверхностей для вращения вокруг OX
# x остается x, y_3d = R*cos(theta), z_3d = R*sin(theta)
x_val = np.linspace(0, 1, 50)
theta = np.linspace(0, 2*np.pi, 50)
X_grid, Theta_grid = np.meshgrid(x_val, theta)

# Внешний конус (от y=x)
R_out = X_grid
Y_out = R_out * np.cos(Theta_grid)
Z_out = R_out * np.sin(Theta_grid)

# Внутренний параболоид (от y=x^2)
R_in = X_grid**2
Y_in = R_in * np.cos(Theta_grid)
Z_in = R_in * np.sin(Theta_grid)

ax.plot_surface(X_grid, Y_out, Z_out, color='blue', alpha=0.3, edgecolor='none')
ax.plot_surface(X_grid, Y_in, Z_in, color='red', alpha=0.8, edgecolor='none')

ax.set_title('Тело вращения (синий - конус, красный - параболоид)')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
ax.set_box_aspect((1, 1, 1)) 
plt.show()