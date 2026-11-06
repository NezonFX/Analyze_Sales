import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 1000)

y = 4 / (x**2 - 4)

mask = (np.abs(x - 2) < 0.05) | (np.abs(x + 2) < 0.05)
y[mask] = np.nan

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='green', label='y(x) = 4 / (x² - 4)')

plt.ylim(-10, 10)

plt.axvline(x=2, color='gray', linestyle='--', label='Асимптота x=2')
plt.axvline(x=-2, color='gray', linestyle='--', label='Асимптота x=-2')

plt.title('Функция с разрывами')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.savefig('img/task2.png')
plt.show()