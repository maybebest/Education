"""Iterators. Cicle"""

from itertools import cycle

chars = cycle('Python')

print('First char: %s', next(chars)) # First char: P

for char in chars:
    print(char, end=", ")

# y, t, h, o, n, P, y, t, h, o, n...

print(chars[1])
# TypeError: 'itertools.cycle' object is not subscriptable

print(chars[::-1])
# TypeError: 'itertools.cycle' object is not subscriptable

