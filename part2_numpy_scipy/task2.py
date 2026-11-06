import numpy as np

def get_input(prompt):
    while True:
        try:
            data = input(prompt).split()
            return np.array([float(x) for x in data])
        except ValueError:
            print("Ошибка: введите числа через пробел.")

def main():
    lengths = get_input("Длины: ")
    speeds = get_input("Скорости: ")
    
    if len(lengths) != len(speeds):
        print("Ошибка: количество длин и скоростей должно совпадать!")
        return

    try:
        k = int(input("k = "))
        p = int(input("p = "))
        t = float(input("t = "))
    except ValueError:
        print("Ошибка: k и p должны быть целыми числами, t - числом.")
        return

    n = len(lengths)
    if not (1 <= k <= n and 1 <= p <= n and k <= p):
        print(f"Ошибка: k и p должны быть в диапазоне от 1 до {n}, и k <= p.")
        return

    S = np.sum(lengths[k-1:p])
    
    times = lengths[k-1:p] / speeds[k-1:p]
    T = np.sum(times)

    V = S / T

    cumulative_times = np.cumsum(times)
    
    if t > T:
        print(f"Ошибка: t ({t} ч) больше общего времени в пути ({T:.2f} ч).")
        return

    idx = np.searchsorted(cumulative_times, t)
    
    if idx == len(cumulative_times):
        idx -= 1
        
    actual_segment = k + idx
    
    time_before = cumulative_times[idx-1] if idx > 0 else 0
    time_on_segment = t - time_before
    distance_on_segment = time_on_segment * speeds[actual_segment-1]

    print(f"S = {S:.0f} км, T = {T:.2f} ч, V = {V:.2f} км/ч")
    print(f"Через {t} ч автомобиль на участке {actual_segment}, в {distance_on_segment:.1f} км от его начала")

if __name__ == "__main__":
    main()