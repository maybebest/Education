"""Filter"""


def filter_more_10(num):
    "Return True if passed number is bigger then 10"
    return num > 10


numbers = (0, 4, 6, 21, 4, 143, 42)

print(
    list(filter(filter_more_10, numbers))
)  # [21, 143, 42]

print(
    list(filter(lambda num: num % 2 != 0, numbers))
)  # [21, 143]
print(
    list(filter(lambda num: num % 2 == 0, numbers))
)  # [0, 4, 6, 4, 42]

print(
    list(filter(None, numbers))
)  # [4, 6, 21, 4, 143, 42]
