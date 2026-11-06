import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def f1(x):
    return x * np.sin(x)

res_quad, err_quad = integrate.quad(f1, 0, np.pi)
print(f"Интеграл (quad): {res_quad:.4f}, ошибка: {err_quad}")

analytic1 = np.pi
error1 = abs(res_quad - analytic1)
print(f"Аналитическое значение: {analytic1:.4f}, абсолютная погрешность: {error1}")

def f2(y, x):
    return x + y

res_dbl, err_dbl = integrate.dblquad(f2, 0, 1, lambda x: 0, lambda x: x)
print(f"\nДвойной интеграл (dblquad): {res_dbl:.4f}, ошибка: {err_dbl}")


analytic2 = 0.5
error2 = abs(res_dbl - analytic2)
print(f"Аналитическое значение: {analytic2}, абсолютная погрешность: {error2}")

N_values = [10**3, 10**4, 10**5, 10**6]
errors_mc = []

print("\nМетод Монте-Карло:")
for N in N_values:
    x_rand = np.random.rand(N)
    y_rand = np.random.rand(N)
    
    mask = y_rand <= x_rand
    x_in = x_rand[mask]
    y_in = y_rand[mask]
    
    mean_val = np.mean(x_in + y_in)
    integral_mc = mean_val * 0.5
    
    err_mc = abs(integral_mc - analytic2)
    errors_mc.append(err_mc)
    print(f"N = {N}: интеграл = {integral_mc:.4f}, погрешность = {err_mc:.6f}")

plt.figure(figsize=(8, 6))
plt.plot(N_values, errors_mc, marker='o', linestyle='-', color='b')
plt.xscale('log')
plt.yscale('log')
plt.title('Зависимость погрешности метода Монте-Карло от N')
plt.xlabel('N (количество точек)')
plt.ylabel('Абсолютная погрешность')
plt.grid(True, which="both", ls="--")
plt.savefig('img/task4.png')
plt.show()