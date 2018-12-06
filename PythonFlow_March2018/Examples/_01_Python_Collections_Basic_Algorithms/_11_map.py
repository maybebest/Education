"""Map"""


def sqr(number):
    """sqr"""
    return number ** 2


NUMBERS = [1, 2, 3, 4, 5]
RESULT = []

for n in NUMBERS:
    RESULT.append(sqr(n))

print(RESULT)  # [1, 4, 9, 16, 25]

RESULT = list(map(sqr, NUMBERS))

print(RESULT)  # [1, 4, 9, 16, 25]
