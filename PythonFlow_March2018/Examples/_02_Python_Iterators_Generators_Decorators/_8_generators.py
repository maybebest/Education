"""Generators. Functions. Fibonacci"""

from itertools import islice


def fibonacci():
    previous = 0
    current = 1
    while True:
        yield current
        previous, current = current, previous + current


fib = fibonacci()

print(next(fib))  # 1

fibonacci_iter_slice = islice(fib, 0, 10)

print(list(fibonacci_iter_slice))  # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
