"""Reduce"""

from functools import reduce


def reducer(a, b):
    "Return sum of a, b args"
    return a + b


chars = list('Python')
numbers = (4, 6, 5, 7, 9, 3, 21, 4, 143, 42)

print(reduce(reducer, chars))  # Python
print(reduce(reducer, numbers))  # 244

print(
    reduce(lambda a, b: a if a > b else b, numbers)
) # 143

