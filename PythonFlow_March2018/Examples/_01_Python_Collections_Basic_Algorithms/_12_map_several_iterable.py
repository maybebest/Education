"""Map"""

def my_pow(x, y):
    """Return x to the power y"""
    return x ** y


NUMBERS_1 = (1, 2, 3, 4, 5)
NUMBERS_2 = [1, 2, 3]

print(
    list(map(my_pow, NUMBERS_1, NUMBERS_2))
)
# [1, 4, 27]

print(
    tuple(map(my_pow, NUMBERS_2, NUMBERS_1))
)
# (1, 4, 27)
