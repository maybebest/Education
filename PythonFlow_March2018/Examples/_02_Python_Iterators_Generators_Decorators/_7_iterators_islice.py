"""Iterators. Cicle. Islice"""

from itertools import cycle, islice

chars = cycle('Python')  # infinite
limited = islice(chars, 0, 12)  # finite

print('First char: %s', next(limited))  # First char: P

for char in limited:  # so safe to use for-loop on
    print(char, end=" ")

# y t h o n P y t h o n
