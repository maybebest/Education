"""Comprehension"""

MY_LIST = [x ** 2 for x in range(7) if x % 2 == 0]

print(MY_LIST)  # [0, 4, 16, 36]

NUMBERS = [1, 2, 3]
LETTERS = ['A', 'B']

NUMBERS_LETTERS = [(n, l) for n in NUMBERS for l in LETTERS]

print(NUMBERS_LETTERS)
# [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]

PHRASE = "Python's Circus"

MY_LIST = [x for x in PHRASE if x.isupper()]

print(MY_LIST)  # ['P', 'C']
