import numpy as np
import matplotlib.pyplot as plt

x_deg = np.linspace(-360, 360, 1000)
x_rad = np.deg2rad(x_deg)

p = np.exp(np.sin(x_rad)) + np.log((np.sin(0.5 * x_rad)**2) + 1) * np.cos(x_rad)
q = -np.log((np.sin(x_rad) - np.cos(x_rad))**2 + 2) + 8

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(x_deg, p, color='blue', label='p(x)')
ax1.set_title('График функции p(x)')
ax1.set_ylabel('p(x)')
ax1.grid(True)
ax1.legend()

ax2.plot(x_deg, q, color='red', label='q(x)')
ax2.set_title('График функции q(x)')
ax2.set_xlabel('Угол (градусы)')
ax2.set_ylabel('q(x)')
ax2.grid(True)
ax2.legend()

ax2.set_xticks(np.arange(-360, 361, 90))

plt.tight_layout()
plt.savefig('img/task1.png')
plt.show()