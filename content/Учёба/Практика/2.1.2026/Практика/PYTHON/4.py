import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

m, l, g, k, h, t = sp.symbols('m l g k h t', positive=True, real=True)
A, B, phi1, phi2 = sp.symbols('A B phi1 phi2', real=True)

omega1 = sp.sqrt(g / l)
omega2 = sp.sqrt((m*g*l + 2*k*h**2) / (m*l**2))

print("Аналитическое решение:")
print("Частота синфазных колебаний (w1):", omega1)
print("Частота противофазных колебаний (w2):", omega2)

m_val, l_val, g_val, k_val, h_val = 1, 1, 9.81, 5, 0.5
w1_num = np.sqrt(g_val / l_val)
w2_num = np.sqrt((m_val*g_val*l_val + 2*k_val*h_val**2) / (m_val*l_val**2))

t_arr = np.linspace(0, 20, 400)
A_num, B_num = 0.1, 0.1

th1 = A_num * np.cos(w1_num * t_arr) + B_num * np.cos(w2_num * t_arr)
th2 = A_num * np.cos(w1_num * t_arr) - B_num * np.cos(w2_num * t_arr)

plt.figure(figsize=(10, 5))
plt.plot(t_arr, th1, 'r-', linewidth=1.5, label='Маятник 1')
plt.plot(t_arr, th2, 'b--', linewidth=1.5, label='Маятник 2')
plt.title('Явление биений в связанных маятниках')
plt.xlabel('Время t, с')
plt.ylabel('Угол отклонения θ, рад')
plt.grid(True)
plt.legend()
plt.show()