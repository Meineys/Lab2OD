import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(2000)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_time(sort_func, data):
    start = time.perf_counter()
    sort_func(data.copy())
    return time.perf_counter() - start


sizes = [100, 300, 500, 800, 1000]

times_sel = {'random': [], 'sorted': [], 'reversed': []}
times_quick = {'random': [], 'sorted': [], 'reversed': []}

for size in sizes:
    data_random = [random.randint(0, 1000) for _ in range(size)]
    data_sorted = list(range(size))
    data_reversed = list(range(size, 0, -1))

    times_sel['random'].append(measure_time(selection_sort, data_random))
    times_sel['sorted'].append(measure_time(selection_sort, data_sorted))
    times_sel['reversed'].append(measure_time(selection_sort, data_reversed))

    times_quick['random'].append(measure_time(quick_sort, data_random))
    times_quick['sorted'].append(measure_time(quick_sort, data_sorted))
    times_quick['reversed'].append(measure_time(quick_sort, data_reversed))

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].plot(sizes, times_sel['random'], label='Selection')
axs[0].plot(sizes, times_quick['random'], label='Quick')
axs[0].set_title('Случайные числа')
axs[0].legend()

axs[1].plot(sizes, times_sel['sorted'], label='Selection')
axs[1].plot(sizes, times_quick['sorted'], label='Quick')
axs[1].set_title('Отсортированный список')
axs[1].legend()

axs[2].plot(sizes, times_sel['reversed'], label='Selection')
axs[2].plot(sizes, times_quick['reversed'], label='Quick')
axs[2].set_title('Обратно отсортированный')
axs[2].legend()

plt.show()