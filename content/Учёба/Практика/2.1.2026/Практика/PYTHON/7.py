import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.2)
y = np.sin(x + 1)

fig = plt.figure(figsize=(12, 10))
fig.suptitle('Сравнение стилей графиков', fontsize=16)

# 1. PLOT
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y, 'b-')
ax1.set_title('Стиль: plot')
ax1.grid(True)
ax1.set_xlabel('Ось X'); ax1.set_ylabel('Ось Y')

# 2. BAR
ax2 = fig.add_subplot(2, 2, 2)
ax2.bar(x, y, color='teal')
ax2.set_title('Стиль: bar')
ax2.grid(True)
ax2.set_xlabel('Ось X'); ax2.set_ylabel('Ось Y')

# 3. STEM
ax3 = fig.add_subplot(2, 2, 3)
ax3.stem(x, y, linefmt='r-', markerfmt='ro', basefmt='k-')
ax3.set_title('Стиль: stem')
ax3.grid(True)
ax3.set_xlabel('Ось X'); ax3.set_ylabel('Ось Y')

# 4. POLAR
ax4 = fig.add_subplot(2, 2, 4, polar=True)
ax4.plot(x, y, 'm-', linewidth=2)
ax4.set_title('Стиль: polar')

plt.tight_layout()
plt.show()