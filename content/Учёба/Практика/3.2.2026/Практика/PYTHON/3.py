import numpy as np
import matplotlib.pyplot as plt

a, b = 12, 6
S = np.pi * a * b
print(f"Полуоси сечения: a={a}, b={b}")
print(f"Площадь сечения при z=0: {S:.4f} (или {a*b}π)")
c = 3 # из z^2/9
u = np.linspace(-2, 2, 50)
v = np.linspace(0, 2 * np.pi, 50)
U, V = np.meshgrid(u, v)
X = a * np.cosh(U) * np.cos(V)
Y = b * np.cosh(U) * np.sin(V)
Z = c * np.sinh(U)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='jet', alpha=0.8, edgecolor='none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Высота (Z)')
ax.set_title('Однополостный гиперболоид')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
plt.show()