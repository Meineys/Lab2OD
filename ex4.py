import time
import matplotlib.pyplot as plt


def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0: return 2
    if n == 1: return 1
    return lucas(n - 1) + lucas(n - 2)


def lucas_with_fib(n):
    if n == 0: return 2
    return fibonacci(n - 1) + fibonacci(n + 1)


def fib_with_lucas(n):
    if n == 0: return 0
    if n == 1: return 1
    i = n // 2
    j = n - i
    # F_{i+j} = (F_i * L_j + F_j * L_i) // 2
    return (fibonacci(i) * lucas_with_fib(j) + fibonacci(j) * lucas_with_fib(i)) // 2


n_vals = list(range(10, 25))
times_fib = []
times_fib_lucas = []

for n in n_vals:
    start = time.perf_counter()
    fibonacci(n)
    times_fib.append(time.perf_counter() - start)

    start = time.perf_counter()
    fib_with_lucas(n)
    times_fib_lucas.append(time.perf_counter() - start)

plt.plot(n_vals, times_fib, label='fibonacci()')
plt.plot(n_vals, times_fib_lucas, label='fib_with_lucas()')
plt.legend()
plt.show()