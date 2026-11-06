import numpy as np

expenses = np.array([3200, 3100, 2600, 1900, 1500, 1300, 1250, 1400, 1800, 2300, 2900, 3500])


winter_months = np.array([11, 0, 1])
summer_months = np.array([5, 6, 7])

winter_sum = np.sum(expenses[winter_months])
summer_sum = np.sum(expenses[summer_months])

print(f"Зима: {winter_sum}, лето: {summer_sum} -> больше тратится {'зимой' if winter_sum > summer_sum else 'летом'}")

max_expense = np.max(expenses)
max_indices = np.where(expenses == max_expense)[0]
max_months = max_indices + 1

print(f"Максимум ({max_expense}) в месяцах: {', '.join(map(str, max_months))}")