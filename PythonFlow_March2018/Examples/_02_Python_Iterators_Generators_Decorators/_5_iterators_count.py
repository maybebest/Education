"""Iterators. Count"""

from itertools import count

counter = count(start=1)

print('First number: %d', next(counter))  # First number: 1

for number in counter:
    print(number, end=", ")

# 2, 3, 4..........30858
