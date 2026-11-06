import numpy as np

A = np.array([
    [4, -1.5, 2, 0.5],
    [1, 5, -2, 1.2],
    [-2, 1, 6, -1],
    [0.5, 2, -1, 7]
])

B = np.array([11.05, -6.82, 11.5, -0.5])

det = np.linalg.det(A)
print(f"Определитель det(A) = {det:.4f}")
if np.isclose(det, 0):
    print("Система не имеет единственного решения!")
else:
    cond = np.linalg.cond(A)
    print(f"Число обусловленности = {cond:.4f}")
    X_inv = np.dot(np.linalg.inv(A), B)
    print(f"Решение через inv: {X_inv}")

    X_solve = np.linalg.solve(A, B)
    print(f"Решение через solve: {X_solve}")

    diff_norm = np.linalg.norm(X_inv - X_solve)
    print(f"Норма разности решений: {diff_norm}")

    check_norm = np.linalg.norm(np.dot(A, X_solve) - B)
    print(f"Проверка подстановкой ||A*X - B||: {check_norm}")

    print(f"Округленный ответ: {np.round(X_solve, 1)}")